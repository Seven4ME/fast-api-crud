from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from src.config.settings import get_settings
from src.db.elastic import ElasticDataClass, get_elastic

settings = get_settings()


class StorageController:
    @classmethod
    def get_elastic(cls, elastic_client: AsyncElasticsearch = Depends(get_elastic)):
        return elastic_client

    def search(
        index: str = ElasticDataClass.index,
    ):
        return get_elastic().search(index=index, query={"match_all": {}}, size=10)

    def get(index: str, id: str):
        return get_elastic().get(index=index, id=id)
