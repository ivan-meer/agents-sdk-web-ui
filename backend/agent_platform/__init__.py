"""
Ядро платформы агентов.

Этот модуль содержит основные компоненты для создания, настройки и запуска 
интеллектуальных агентов на базе различных языковых моделей.
"""

__version__ = "0.1.0"

# Настройка логирования
import logging

logger = logging.getLogger(__name__)

# Функции для настройки платформы
def set_default_openai_key(api_key: str) -> None:
    """
    Устанавливает API-ключ OpenAI по умолчанию.
    
    Args:
        api_key: API-ключ OpenAI.
    """
    from .model_settings import set_openai_api_key
    set_openai_api_key(api_key)

def set_default_anthropic_key(api_key: str) -> None:
    """
    Устанавливает API-ключ Anthropic по умолчанию.
    
    Args:
        api_key: API-ключ Anthropic.
    """
    from .model_settings import set_anthropic_api_key
    set_anthropic_api_key(api_key)

def set_tracing_enabled(enabled: bool = True) -> None:
    """
    Включает или отключает трассировку.
    
    Args:
        enabled: True для включения трассировки, False для отключения.
    """
    from tracing.setup import set_tracing_enabled
    set_tracing_enabled(enabled)

def enable_verbose_logging() -> None:
    """
    Включает подробное логирование для отладки.
    """
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
