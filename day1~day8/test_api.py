import sqlite3

import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture
def client(tmp_path):
    original_db_path = main.DB_PATH
    main.DB_PATH = tmp_path / "test_guestbook.db"
    with TestClient(main.app) as test_client:
        yield test_client
    main.DB_PATH = original_db_path


def test_page_and_empty_list(client):
    assert client.get("/").status_code == 200
    assert client.get("/static/styles.css").status_code == 200
    assert client.get("/api/entries").json() == []


def test_create_and_list_entry(client):
    response = client.post(
        "/api/entries", json={"name": "홍길동", "message": "안녕하세요"}
    )

    assert response.status_code == 201
    assert response.json()["name"] == "홍길동"
    assert response.json()["message"] == "안녕하세요"
    assert len(client.get("/api/entries").json()) == 1


@pytest.mark.parametrize(
    "body",
    [{"name": "", "message": "메시지"}, {"name": "이름", "message": ""}],
)
def test_invalid_entry_is_rejected(client, body):
    response = client.post("/api/entries", json=body)

    assert response.status_code == 422


def test_delete_entry(client):
    created = client.post(
        "/api/entries", json={"name": "삭제할 글", "message": "내용"}
    ).json()

    response = client.delete(f"/api/entries/{created['id']}")

    assert response.status_code == 204
    assert client.get("/api/entries").json() == []


def test_database_has_one_table(client, tmp_path):
    client.post("/api/entries", json={"name": "확인", "message": "테이블"})
    connection = sqlite3.connect(main.DB_PATH)
    tables = connection.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table'"
    ).fetchall()
    connection.close()

    user_tables = [name for (name,) in tables if not name.startswith("sqlite_")]
    assert user_tables == ["entries"]
