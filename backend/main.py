import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from core.settings import settings
from api.api import api_router
from api.websockets.connections import websocket_router
from core.events import startup_event, shutdown_event


# Настройка логирования
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Обработчик событий жизненного цикла приложения FastAPI.
    """
    # Выполняется при запуске приложения
    await startup_event()
    
    yield
    
    # Выполняется при остановке приложения
    await shutdown_event()


# Создание FastAPI приложения
app = FastAPI(
    title="AI Agents Platform API",
    description="API для управления ИИ-агентами",
    version="0.1.0",
    lifespan=lifespan,
)


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Подключение роутеров
app.include_router(api_router, prefix="/api")
app.include_router(websocket_router)


@app.get("/")
async def root():
    """
    Корневой endpoint для проверки работоспособности API.
    """
    return {
        "status": "ok",
        "message": "AI Agents Platform API is running",
        "docs_url": "/docs",
    }


if __name__ == "__main__":
    import uvicorn
    
    # Запуск приложения
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
