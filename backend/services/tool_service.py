from typing import Any, List
from uuid import UUID

from models.tool import Tool, ToolCreate, ToolUpdate
from core.security import validate_ownership
from core.cache import redis_cache
from exceptions import NotFoundException, PermissionDenied


class ToolService:
    async def get_tools(self, user_id: UUID, workspace_id: UUID = None, 
                      tool_type: str = None, skip: int = 0, limit: int = 100) -> List[Tool]:
        # Реализация с пагинацией и фильтрацией
        query = self._build_query(workspace_id, tool_type)
        return await self.db.execute(query.offset(skip).limit(limit))

    async def create_tool(self, user_id: UUID, tool_in: ToolCreate) -> Tool:
        tool_data = tool_in.dict()
        tool_data["owner_id"] = user_id
        return await self.db.insert(Tool, tool_data)

    async def get_tool(self, tool_id: UUID) -> Tool:
        if cached := await redis_cache.get(f"tool_{tool_id}"):
            return cached
            
        tool = await self.db.query(Tool).filter(Tool.id == tool_id).first()
        if not tool:
            raise NotFoundException("Tool not found")
            
        await redis_cache.set(f"tool_{tool_id}", tool, expire=300)
        return tool

    async def update_tool(self, tool_id: UUID, tool_in: ToolUpdate) -> Tool:
        tool = await self.get_tool(tool_id)
        await validate_ownership(tool.owner_id, current_user)
        
        updated_tool = await self.db.update(
            Tool, 
            tool_id, 
            tool_in.dict(exclude_unset=True)
        )
        await redis_cache.delete(f"tool_{tool_id}")
        return updated_tool

    async def delete_tool(self, tool_id: UUID) -> Tool:
        pass

    async def execute_tool(self, tool_id: UUID, params: dict, user_id: UUID) -> dict:
        pass
