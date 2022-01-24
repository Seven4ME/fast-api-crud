from fastapi import APIRouter

from src.api.v1 import actors, films, smoke
from src.config.settings import get_settings

settings = get_settings()
api_router = APIRouter(prefix=settings.api_prefix)

api_router.include_router(smoke.router)
api_router.include_router(films.router)
api_router.include_router(actors.router)
