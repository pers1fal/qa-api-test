import pytest
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    client = APIClient()
    return client
