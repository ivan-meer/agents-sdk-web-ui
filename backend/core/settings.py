import os
from typing import List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    """
    Настройки приложения
    """
    # Основные настройки приложения
    PROJECT_NAME: str = "AI Agents Platform"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    LOG_LEVEL: str = "INFO"
    
    # CORS
    CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # База данных
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: Optional[str] = None
    
    # Настройки API-ключей для LLM провайдеров
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    GOOGLE_AI_API_KEY: Optional[str] = None
    MISTRAL_API_KEY: Optional[str] = None
    
    # Настройки моделей по умолчанию
    DEFAULT_MODEL: str = "gpt-4o"
    DEFAULT_TEMPERATURE: float = 0.7
    DEFAULT_MAX_TOKENS: int = 1000
    
    # Настройки трассировки
    ENABLE_TRACING: bool = True
    TRACING_BACKEND_URL: Optional[str] = None
    
    # Настройки генерации изображений
    ENABLE_IMAGE_GENERATION: bool = False
    STABILITY_API_KEY: Optional[str] = None
    DALLE_API_ENABLED: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Экземпляр настроек для использования в приложении
settings = Settings()
