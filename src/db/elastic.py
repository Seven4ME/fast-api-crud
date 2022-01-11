from dataclasses import dataclass
from functools import lru_cache
from typing import Optional

from elasticsearch import AsyncElasticsearch

es: Optional[AsyncElasticsearch] = None


@dataclass
class ElasticDataClass:
    index: str = "movies"
    size: int = 1
    limit: Optional[int] = 10
    film_id: str = 1
    es_query: dict = None


@lru_cache()
def get_elastic() -> AsyncElasticsearch:
    return es
