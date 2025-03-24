from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4


class AgentBase(BaseModel):
    """Базовая модель для агента"""
    name: str = Field(..., description="Имя агента")
    description: Optional[str] = Field(None, description="Описание агента")
    instructions: str = Field(..., description="Инструкции для агента (системный промпт)")
    model: str = Field(..., description="Модель, используемая агентом")


class AgentCreate(AgentBase):
    """Модель для создания агента"""
    workspace_id: UUID = Field(..., description="ID рабочего пространства")
    tool_ids: List[UUID] = Field(default=[], description="Список ID инструментов агента")
    model_settings: Dict[str, Any] = Field(default={}, description="Настройки модели")
    input_guardrail_ids: List[UUID] = Field(default=[], description="Список ID входных ограждений")
    output_guardrail_ids: List[UUID] = Field(default=[], description="Список ID выходных ограждений")
    handoff_agent_ids: List[UUID] = Field(default=[], description="Список ID агентов для передачи управления")


class AgentUpdate(BaseModel):
    """Модель для обновления агента"""
    name: Optional[str] = Field(None, description="Имя агента")
    description: Optional[str] = Field(None, description="Описание агента")
    instructions: Optional[str] = Field(None, description="Инструкции для агента (системный промпт)")
    model: Optional[str] = Field(None, description="Модель, используемая агентом")
    tool_ids: Optional[List[UUID]] = Field(None, description="Список ID инструментов агента")
    model_settings: Optional[Dict[str, Any]] = Field(None, description="Настройки модели")
    input_guardrail_ids: Optional[List[UUID]] = Field(None, description="Список ID входных ограждений")
    output_guardrail_ids: Optional[List[UUID]] = Field(None, description="Список ID выходных ограждений")
    handoff_agent_ids: Optional[List[UUID]] = Field(None, description="Список ID агентов для передачи управления")


class Agent(AgentBase):
    """Полная модель агента"""
    id: UUID = Field(default_factory=uuid4, description="Уникальный идентификатор агента")
    workspace_id: UUID = Field(..., description="ID рабочего пространства")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Дата создания")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Дата обновления")
    created_by: UUID = Field(..., description="ID пользователя, создавшего агента")
    tool_ids: List[UUID] = Field(default=[], description="Список ID инструментов агента")
    model_settings: Dict[str, Any] = Field(default={}, description="Настройки модели")
    input_guardrail_ids: List[UUID] = Field(default=[], description="Список ID входных ограждений")
    output_guardrail_ids: List[UUID] = Field(default=[], description="Список ID выходных ограждений")
    handoff_agent_ids: List[UUID] = Field(default=[], description="Список ID агентов для передачи управления")
    
    class Config:
        orm_mode = True
