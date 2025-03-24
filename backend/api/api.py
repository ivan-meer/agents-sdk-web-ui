from fastapi import APIRouter

from api.endpoints import agents, tools, models, runs, users, workspaces, traces

# Создание основного роутера API
api_router = APIRouter()

# Подключение роутеров ресурсов
api_router.include_router(
    agents.router,
    prefix="/agents",
    tags=["agents"],
)

api_router.include_router(
    tools.router,
    prefix="/tools",
    tags=["tools"],
)

api_router.include_router(
    models.router,
    prefix="/models",
    tags=["models"],
)

api_router.include_router(
    runs.router,
    prefix="/runs",
    tags=["runs"],
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)

api_router.include_router(
    workspaces.router,
    prefix="/workspaces",
    tags=["workspaces"],
)

api_router.include_router(
    traces.router,
    prefix="/traces",
    tags=["traces"],
)
