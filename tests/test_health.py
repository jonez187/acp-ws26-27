from pathlib import Path

from fastapi.testclient import TestClient

from app.main import create_app


def test_health_endpoint_reports_ok(tmp_path: Path) -> None:
    db_path = tmp_path / "test.db"

    with TestClient(create_app(db_path)) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_database_file_is_created_on_startup(tmp_path: Path) -> None:
    db_path = tmp_path / "nested" / "running_coach.db"
    assert not db_path.exists()

    with TestClient(create_app(db_path)):
        pass

    assert db_path.exists()
