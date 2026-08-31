from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "ULPF Backend is running"


def test_parse_json():
    response = client.post(
        "/parse",
        json={
            "parser": "json",
            "log": '{"event": "login", "user": "testuser", "status": "success"}'
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["parser"] == "json"
    assert data["event"] == "login"
    assert data["user"] == "testuser"


def test_get_events():
    response = client.get("/events")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_invalid_parser():
    response = client.post(
        "/parse",
        json={
            "parser": "unknown_parser",
            "log": "some test log"
        }
    )

    assert response.status_code in [200, 400]


def test_empty_log():
    response = client.post(
        "/parse",
        json={
            "parser": "json",
            "log": ""
        }
    )

    assert response.status_code in [200, 400]