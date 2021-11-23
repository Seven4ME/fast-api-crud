from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    api_prefix: str = '/api/v1'


class TestSettings(Settings):
    test_base_url: str = "http://127.0.0.1:8000"


@lru_cache()
def get_test_settings():
    return TestSettings()


@lru_cache()
def get_settings():
    return Settings()
