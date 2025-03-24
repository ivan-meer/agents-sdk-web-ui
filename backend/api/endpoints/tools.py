from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Body, Query, Path
from uuid import UUID

from models.tool import Tool, ToolCreate, ToolUpdate
from services.tool_service import ToolService
from core.dependencies import get_tool_service, get_current_user

router = APIRouter()


@router.get("/", response_model=List[Tool])
async def list_tools(
    skip: int = Query(0, description="Пропустить указанное количество записей"),
    limit: int = Query(100, description="Максимальное количество записей"),
    workspace_id: UUID = Query(None, description="ID рабочего пространства для фильтрации"),
    tool_type: str = Query(None, description="Тип инструмента для фильтрации"),
    tool_service: ToolService = Depends(get_tool_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Получить список инструментов.
    """
    return await tool_service.get_tools(
        user_id=current_user.id,
        workspace_id=workspace_id,
        tool_type=tool_type,
        skip=skip,
        limit=limit
    )


@router.post("/", response_model=Tool)
async def create_tool(
    tool_in: ToolCreate = Body(...),
    tool_service: ToolService = Depends(get_tool_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Создать новый инструмент.
    """
    return await tool_service.create_tool(
        user_id=current_user.id,
        tool_in=tool_in
    )


@router.get("/{tool_id}", response_model=Tool)
async def get_tool(
    tool_id: UUID = Path(..., description="ID инструмента"),
    tool_service: ToolService = Depends(get_tool_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Получить инструмент по ID.
    """
    tool = await tool_service.get_tool(tool_id=tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Инструмент не найден")
    return tool


@router.put("/{tool_id}", response_model=Tool)
async def update_tool(
    tool_id: UUID = Path(..., description="ID инструмента"),
    tool_in: ToolUpdate = Body(...),
    tool_service: ToolService = Depends(get_tool_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Обновить инструмент.
    """
    tool = await tool_service.get_tool(tool_id=tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Инструмент не найден")
    
    return await tool_service.update_tool(
        tool_id=tool_id,
        tool_in=tool_in
    )


@router.delete("/{tool_id}", response_model=Tool)
async def delete_tool(
    tool_id: UUID = Path(..., description="ID инструмента"),
    tool_service: ToolService = Depends(get_tool_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Удалить инструмент.
    """
    tool = await tool_service.get_tool(tool_id=tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Инструмент не найден")
    
    return await tool_service.delete_tool(tool_id=tool_id)


@router.post("/{tool_id}/execute", response_model=dict)
async def execute_tool(
    tool_id: UUID = Path(..., description="ID инструмента"),
    params: dict = Body(...),
    tool_service: ToolService = Depends(get_tool_service),
    current_user = Depends(get_current_user)
) -> Any:
    """
    Выполнить инструмент с указанными параметрами.
    """
    tool = await tool_service.get_tool(tool_id=tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Инструмент не найден")
    
    result = await tool_service.execute_tool(
        tool_id=tool_id,
        params=params,
        user_id=current_user.id
    )
    
    return result
