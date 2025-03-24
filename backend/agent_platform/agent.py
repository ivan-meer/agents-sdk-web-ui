# backend/agent_platform/agent.py
from typing import Dict, List, Any, Optional, Type, Union, Callable
import uuid
from pydantic import BaseModel, Field

from .tool import BaseTool
from .memory import Memory
from .context import ExecutionContext


class AgentConfig(BaseModel):
    """Конфигурация агента"""
    name: str
    description: str = ""
    instructions: str
    tools: List[Type[BaseTool]] = []
    model_name: str = "gpt-4o"
    temperature: float = 0.7
    max_tokens: int = 4000
    stream: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Agent:
    """Базовый класс агента"""
    
    def __init__(
        self,
        config: AgentConfig,
        memory: Optional[Memory] = None,
    ):
        self.id = str(uuid.uuid4())
        self.config = config
        self.memory = memory or Memory()
        self.tools = [tool() for tool in config.tools]
        self.execution_context = None
    
    async def run(self, prompt: str, context: Dict[str, Any] = None) -> Union[str, Any]:
        """Запуск агента для выполнения задачи"""
        self.execution_context = ExecutionContext(
            agent_id=self.id,
            agent_name=self.config.name,
            user_prompt=prompt,
            context=context or {},
        )
        
        # TODO: Реализация логики агента
        # ...
        
        return "Ответ агента на запрос"
    
    async def stream_run(self, prompt: str, context: Dict[str, Any] = None) -> AsyncIterator[str]:
        """Потоковый запуск агента с возвратом промежуточных результатов"""
        # Реализация потокового выполнения
        # ...
        yield "Часть ответа агента"


# backend/agent_platform/tool.py
from typing import Dict, Any, Optional, Callable, List, Type
from pydantic import BaseModel, Field
import inspect


class ToolParameter(BaseModel):
    """Параметр инструмента"""
    name: str
    description: str
    type: str
    required: bool = True
    default: Optional[Any] = None


class ToolMetadata(BaseModel):
    """Метаданные инструмента"""
    name: str
    description: str
    parameters: List[ToolParameter] = Field(default_factory=list)


class BaseTool:
    """Базовый класс для инструментов агента"""
    
    name: str = ""
    description: str = ""
    
    def __init__(self):
        if not self.name:
            self.name = self.__class__.__name__
    
    @classmethod
    def get_metadata(cls) -> ToolMetadata:
        """Получить метаданные инструмента"""
        # Анализ сигнатуры метода execute
        sig = inspect.signature(cls.execute)
        parameters = []
        
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
                
            param_info = ToolParameter(
                name=name,
                description=getattr(cls, f"{name}_description", f"Parameter {name}"),
                type=str(param.annotation),
                required=param.default == inspect.Parameter.empty,
                default=None if param.default == inspect.Parameter.empty else param.default
            )
            parameters.append(param_info)
        
        return ToolMetadata(
            name=cls.name,
            description=cls.description,
            parameters=parameters
        )
    
    async def execute(self, **kwargs) -> Any:
        """Выполнить инструмент с заданными параметрами"""
        raise NotImplementedError("Подклассы должны реализовать метод execute")


# backend/agent_platform/model.py
from typing import Dict, List, Any, Optional, AsyncIterator
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field


class Message(BaseModel):
    """Сообщение в формате чата"""
    role: str
    content: str
    name: Optional[str] = None


class ModelConfig(BaseModel):
    """Конфигурация модели"""
    model_name: str
    temperature: float = 0.7
    max_tokens: int = 4000
    stream: bool = False
    stop_sequences: List[str] = Field(default_factory=list)
    system_prompt: Optional[str] = None
    extra_params: Dict[str, Any] = Field(default_factory=dict)


class LLMModel(ABC):
    """Абстрактный класс для работы с языковыми моделями"""
    
    def __init__(self, config: ModelConfig):
        self.config = config
    
    @abstractmethod
    async def generate(self, messages: List[Message]) -> str:
        """Генерировать ответ на основе сообщений"""
        pass
    
    @abstractmethod
    async def stream_generate(self, messages: List[Message]) -> AsyncIterator[str]:
        """Потоковая генерация ответа"""
        pass


# backend/agent_platform/memory.py
from typing import Dict, List, Any, Optional
import time
from pydantic import BaseModel, Field


class MemoryItem(BaseModel):
    """Элемент памяти агента"""
    timestamp: float = Field(default_factory=time.time)
    content: Dict[str, Any]
    type: str  # "message", "tool_call", "observation", etc.
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Memory:
    """Память агента для хранения истории взаимодействия"""
    
    def __init__(self):
        self.items: List[MemoryItem] = []
    
    def add(self, content: Dict[str, Any], type: str, metadata: Dict[str, Any] = None) -> None:
        """Добавить элемент в память"""
        item = MemoryItem(
            content=content,
            type=type,
            metadata=metadata or {}
        )
        self.items.append(item)
    
    def get_chat_history(self) -> List[Dict[str, Any]]:
        """Получить историю чата в формате, пригодном для LLM"""
        return [
            {
                "role": item.content.get("role", "user"),
                "content": item.content.get("content", "")
            }
            for item in self.items
            if item.type == "message"
        ]
    
    def get_by_type(self, type: str) -> List[MemoryItem]:
        """Получить все элементы памяти определенного типа"""
        return [item for item in self.items if item.type == type]
    
    def clear(self) -> None:
        """Очистить память"""
        self.items = []


# backend/agent_platform/run.py
from typing import Dict, List, Any, Optional, Union, AsyncIterator
import uuid
import time
from enum import Enum
from pydantic import BaseModel, Field

from .agent import Agent
from .context import ExecutionContext


class RunStatus(str, Enum):
    """Статус выполнения запуска агента"""
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"


class RunStep(BaseModel):
    """Шаг выполнения запуска агента"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str  # "message", "tool_call", "tool_result", etc.
    content: Dict[str, Any]
    timestamp: float = Field(default_factory=time.time)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Run:
    """Запуск агента"""
    
    def __init__(
        self,
        agent: Agent,
        prompt: str,
        context: Dict[str, Any] = None,
        run_id: Optional[str] = None,
    ):
        self.id = run_id or str(uuid.uuid4())
        self.agent = agent
        self.prompt = prompt
        self.context = context or {}
        self.status = RunStatus.CREATED
        self.steps: List[RunStep] = []
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.error: Optional[str] = None
        self.result: Optional[Any] = None
    
    def add_step(self, type: str, content: Dict[str, Any], metadata: Dict[str, Any] = None) -> RunStep:
        """Добавить шаг выполнения"""
        step = RunStep(
            type=type,
            content=content,
            metadata=metadata or {}
        )
        self.steps.append(step)
        return step
    
    async def execute(self) -> Any:
        """Выполнить запуск агента"""
        self.status = RunStatus.RUNNING
        self.start_time = time.time()
        
        try:
            self.result = await self.agent.run(self.prompt, self.context)
            self.status = RunStatus.COMPLETED
            return self.result
        except Exception as e:
            self.status = RunStatus.FAILED
            self.error = str(e)
            raise
        finally:
            self.end_time = time.time()
    
    async def stream_execute(self) -> AsyncIterator[Union[str, RunStep]]:
        """Потоковое выполнение запуска агента"""
        self.status = RunStatus.RUNNING
        self.start_time = time.time()
        
        try:
            async for chunk in self.agent.stream_run(self.prompt, self.context):
                step = self.add_step("chunk", {"content": chunk})
                yield chunk
            
            self.status = RunStatus.COMPLETED
        except Exception as e:
            self.status = RunStatus.FAILED
            self.error = str(e)
            raise
        finally:
            self.end_time = time.time()
    
    def cancel(self) -> None:
        """Отменить выполнение запуска"""
        if self.status == RunStatus.RUNNING:
            self.status = RunStatus.CANCELED
            self.end_time = time.time()


# backend/agent_platform/context.py
from typing import Dict, List, Any, Optional
import uuid
from pydantic import BaseModel, Field


class ExecutionContext(BaseModel):
    """Контекст выполнения агента"""
    
    agent_id: str
    agent_name: str
    user_prompt: str
    context: Dict[str, Any] = Field(default_factory=dict)
    execution_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    variables: Dict[str, Any] = Field(default_factory=dict)
    
    def get_variable(self, name: str, default: Any = None) -> Any:
        """Получить значение переменной из контекста"""
        return self.variables.get(name, default)
    
    def set_variable(self, name: str, value: Any) -> None:
        """Установить значение переменной в контексте"""
        self.variables[name] = value
    
    def update_context(self, new_context: Dict[str, Any]) -> None:
        """Обновить контекст выполнения"""
        self.context.update(new_context)