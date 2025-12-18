import pytest
import requests


@pytest.fixture(scope="session")
def base_url() -> str:

    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s


@pytest.fixture(scope="session")
def user_id() -> int:
    return 2
