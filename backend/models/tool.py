from typing import Optional

from pydantic import BaseModel


class ToolBase(BaseModel):
    name: str
    description: Optional[str] = None


class ToolCreate(ToolBase):
    pass


class ToolUpdate(ToolBase):
    pass


class Tool(ToolBase):
    id: int

    class Config:
        orm_mode = True
