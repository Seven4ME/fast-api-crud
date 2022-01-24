from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI

from src.api.routes import api_router
from src.config.settings import get_settings
from src.db import elastic

app = FastAPI()
settings = get_settings()

app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    elastic.es = AsyncElasticsearch(
        hosts=[f"{settings.ELASTIC_HOST}:{settings.ELASTIC_PORT}"]
    )


@app.on_event("shutdown")
async def shutdown_event():
    await elastic.es.close()
