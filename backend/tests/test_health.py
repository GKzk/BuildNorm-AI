from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "buildnorm-api"}


def test_root_endpoint_returns_application_metadata() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "BuildNorm AI"
