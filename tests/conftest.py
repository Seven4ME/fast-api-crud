import pytest


@pytest.fixture(scope='module')
def get_test_base_url():
    test_base_url: str = "http://127.0.0.1:8000"
    yield test_base_url