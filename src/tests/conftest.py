import pytest

from src.config.settings import get_test_settings


@pytest.fixture(scope="module")
def test_settings():
    yield get_test_settings()