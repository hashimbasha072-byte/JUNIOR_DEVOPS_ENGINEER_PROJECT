from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


def test_root_returns_application_name():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["application"] == "Apex Operations API"


def test_health_returns_healthy():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_ready_returns_200_when_dependency_is_available():
    main.DEPENDENCY_AVAILABLE = True
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_ready_returns_503_when_dependency_is_unavailable():
    main.DEPENDENCY_AVAILABLE = False
    response = client.get("/ready")
    assert response.status_code == 503


def test_metrics_contains_application_version():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "application_version" in response.json()


def test_unknown_endpoint_returns_404():
    response = client.get("/does-not-exist")
    assert response.status_code == 404
