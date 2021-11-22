import pytest

from main import app
from fastapi.testclient import TestClient
from httpx import AsyncClient

client = TestClient(app)

@pytest.mark.anyio
async def test_async_resource(get_test_base_url):
    async with AsyncClient(app=app, base_url=get_test_base_url) as ac:
        response = await ac.get("/smoke/")
        assert response.status_code == 200
        assert response.json() == {"message": "Ok"}