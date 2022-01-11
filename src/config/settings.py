from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    films_prefix: str = "/films"
    actors_prefix: str = "/actors"
    ELASTIC_HOST: str = "es-container"
    ELASTIC_PORT: int = 9200


class TestSettings(Settings):
    test_base_url: str = "http://127.0.0.1:8000"


@lru_cache()
def get_test_settings():
    return TestSettings()


@lru_cache()
def get_settings():
    return Settings()
