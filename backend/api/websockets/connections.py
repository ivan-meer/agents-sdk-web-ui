from typing import Dict, List, Optional, Any
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Query
from uuid import UUID, uuid4
import json
import logging
import asyncio

from services.agent_service import AgentService
from core.dependencies import get_agent_service, get_current_user_from_token

# Создаем роутер для WebSocket
websocket_router = APIRouter()

# Настройка логирования
logger = logging.getLogger(__name__)

# Хранилище активных соединений
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.user_connections: Dict[UUID, List[str]] = {}
    
    async def connect(self, websocket: WebSocket, connection_id: str, user_id: UUID):
        await websocket.accept()
        self.active_connections[connection_id] = websocket
        
        if user_id not in self.user_connections:
            self.user_connections[user_id] = []
        
        self.user_connections[user_id].append(connection_id)
        logger.info(f"WebSocket подключение {connection_id} установлено для пользователя {user_id}")
    
    def disconnect(self, connection_id: str, user_id: UUID):
        if connection_id in self.active_connections:
            del self.active_connections[connection_id]
        
        if user_id in self.user_connections and connection_id in self.user_connections[user_id]:
            self.user_connections[user_id].remove(connection_id)
            if not self.user_connections[user_id]:
                del self.user_connections[user_id]
        
        logger.info(f"WebSocket подключение {connection_id} закрыто для пользователя {user_id}")
    
    async def send_to_user(self, user_id: UUID, message: Any):
        if user_id in self.user_connections:
            for connection_id in self.user_connections[user_id]:
                if connection_id in self.active_connections:
                    await self.active_connections[connection_id].send_json(message)
    
    async def send_to_connection(self, connection_id: str, message: Any):
        if connection_id in self.active_connections:
            await self.active_connections[connection_id].send_json(message)
    
    async def broadcast(self, message: Any):
        for connection in self.active_connections.values():
            await connection.send_json(message)


# Создаем менеджер соединений
manager = ConnectionManager()


@websocket_router.websocket("/ws/agent/{agent_id}")
async def websocket_agent_endpoint(
    websocket: WebSocket,
    agent_id: UUID,
    token: str = Query(...),
    agent_service: AgentService = Depends(get_agent_service)
):
    """
    WebSocket для стриминга результатов выполнения агента.
    """
    connection_id = str(uuid4())
    
    # Получаем пользователя из токена
    try:
        current_user = await get_current_user_from_token(token)
    except Exception as e:
        await websocket.close(code=1008, reason="Ошибка аутентификации")
        return
    
    # Проверяем существование агента
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        await websocket.close(code=1008, reason="Агент не найден")
        return
    
    # Подключаем WebSocket
    await manager.connect(websocket, connection_id, current_user.id)
    
    try:
        while True:
            # Получаем сообщение от клиента
            data = await websocket.receive_json()
            
            # Обрабатываем команду
            if data["type"] == "run":
                # Запускаем выполнение агента асинхронно
                asyncio.create_task(
                    handle_agent_run(
                        agent_id=agent_id,
                        input_text=data.get("input", ""),
                        connection_id=connection_id,
                        user_id=current_user.id,
                        agent_service=agent_service
                    )
                )
            elif data["type"] == "stop":
                # Останавливаем выполнение агента
                await agent_service.stop_agent_run(
                    agent_id=agent_id,
                    run_id=data.get("run_id")
                )
                await manager.send_to_connection(
                    connection_id, 
                    {"type": "stopped", "run_id": data.get("run_id")}
                )
    
    except WebSocketDisconnect:
        manager.disconnect(connection_id, current_user.id)
    except Exception as e:
        logger.error(f"Ошибка WebSocket: {str(e)}")
        manager.disconnect(connection_id, current_user.id)
        await websocket.close(code=1011, reason="Внутренняя ошибка сервера")


async def handle_agent_run(
    agent_id: UUID,
    input_text: str,
    connection_id: str,
    user_id: UUID,
    agent_service: AgentService
):
    """
    Обработка запуска агента через WebSocket.
    """
    try:
        # Создаем запуск агента
        run_id = await agent_service.create_run(
            agent_id=agent_id,
            input_text=input_text,
            user_id=user_id
        )
        
        # Отправляем информацию о начале выполнения
        await manager.send_to_connection(
            connection_id, 
            {"type": "run_started", "run_id": str(run_id)}
        )
        
        # Запускаем агента в режиме стриминга
        async for event in agent_service.stream_agent_run(
            agent_id=agent_id,
            run_id=run_id,
            input_text=input_text,
            user_id=user_id
        ):
            # Отправляем события клиенту
            await manager.send_to_connection(connection_id, event)
        
        # Отправляем информацию о завершении выполнения
        await manager.send_to_connection(
            connection_id, 
            {"type": "run_completed", "run_id": str(run_id)}
        )
    
    except Exception as e:
        logger.error(f"Ошибка выполнения агента: {str(e)}")
        # Отправляем информацию об ошибке
        await manager.send_to_connection(
            connection_id, 
            {"type": "error", "message": str(e)}
        )
