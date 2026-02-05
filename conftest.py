import pytest
from api.clients.auth_client import AuthClient


BASE_URL = "http://www.example.com"

@pytest.fixture
def auth_cookies():
    auth_client = AuthClient(BASE_URL)
    return auth_client.login_stub()


    