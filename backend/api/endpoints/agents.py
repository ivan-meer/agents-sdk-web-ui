from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Body, Query, Path
from uuid import UUID

from models.agent import Agent, AgentCreate, AgentUpdate
from services.agent_service import AgentService
from core.dependencies import get_agent_service, get_current_user

router = APIRouter()


@router.get("/", response_model=List[Agent])
async def list_agents(
    skip: int = Query(0, description="Пропустить указанное количество записей"),
    limit: int = Query(100, description="Максимальное количество записей"),
    workspace_id: UUID = Query(None, description="ID рабочего пространства для фильтрации"),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Получить список агентов.
    """
    return await agent_service.get_agents(
        user_id=current_user.id,
        workspace_id=workspace_id,
        skip=skip,
        limit=limit
    )


@router.post("/", response_model=Agent)
async def create_agent(
    agent_in: AgentCreate = Body(...),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Создать нового агента.
    """
    return await agent_service.create_agent(
        user_id=current_user.id,
        agent_in=agent_in
    )


@router.get("/{agent_id}", response_model=Agent)
async def get_agent(
    agent_id: UUID = Path(..., description="ID агента"),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Получить агента по ID.
    """
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Агент не найден")
    return agent


@router.put("/{agent_id}", response_model=Agent)
async def update_agent(
    agent_id: UUID = Path(..., description="ID агента"),
    agent_in: AgentUpdate = Body(...),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Обновить агента.
    """
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Агент не найден")
    
    return await agent_service.update_agent(
        agent_id=agent_id,
        agent_in=agent_in
    )


@router.delete("/{agent_id}", response_model=Agent)
async def delete_agent(
    agent_id: UUID = Path(..., description="ID агента"),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Удалить агента.
    """
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Агент не найден")
    
    return await agent_service.delete_agent(agent_id=agent_id)


@router.post("/{agent_id}/run", response_model=dict)
async def run_agent(
    agent_id: UUID = Path(..., description="ID агента"),
    input_text: str = Body(..., embed=True),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Запустить агента с заданным входным текстом.
    Возвращает результат выполнения агента.
    """
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Агент не найден")
    
    result = await agent_service.run_agent(
        agent_id=agent_id,
        input_text=input_text,
        user_id=current_user.id
    )
    
    return result


@router.post("/{agent_id}/as-tool", response_model=Agent)
async def create_agent_as_tool(
    agent_id: UUID = Path(..., description="ID агента"),
    tool_name: str = Body(...),
    tool_description: str = Body(...),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Создать инструмент на основе агента.
    Возвращает обновленного агента с информацией о созданном инструменте.
    """
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Агент не найден")
    
    return await agent_service.create_agent_as_tool(
        agent_id=agent_id,
        tool_name=tool_name,
        tool_description=tool_description,
        user_id=current_user.id
    )


@router.get("/{agent_id}/runs", response_model=List[dict])
async def get_agent_runs(
    agent_id: UUID = Path(..., description="ID агента"),
    skip: int = Query(0, description="Пропустить указанное количество записей"),
    limit: int = Query(100, description="Максимальное количество записей"),
    agent_service: AgentService = Depends(get_agent_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Получить историю запусков агента.
    """
    agent = await agent_service.get_agent(agent_id=agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Агент не найден")
    
    return await agent_service.get_agent_runs(
        agent_id=agent_id,
        skip=skip,
        limit=limit
    )
