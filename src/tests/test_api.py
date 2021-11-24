import http

import pytest
from httpx import AsyncClient

from src.config.settings import TestSettings
from src.main import app


@pytest.mark.anyio
async def test_async_resource(test_settings: TestSettings):
    async with AsyncClient(app=app, base_url=test_settings.test_base_url) as ac:
        response = await ac.get(f"{test_settings.api_prefix}/smoke/")
        assert response.status_code == http.HTTPStatus.OK
        assert response.json() == {"message": "OK", "status": http.HTTPStatus.OK}
