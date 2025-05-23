import pytest
from fastapi.testclient import TestClient

from good_morning_sonar.app import app


@pytest.fixture
def client():
    return TestClient(app)
