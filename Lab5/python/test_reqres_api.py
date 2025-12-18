from api_client import JsonPlaceholderClient


def test_get_user(session, base_url, user_id):
    client = JsonPlaceholderClient(base_url=base_url, session=session)

    r = client.get_user(user_id)
    assert r.status_code == 200

    data = r.json()
    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data


def test_create_user(session, base_url):
    client = JsonPlaceholderClient(base_url=base_url, session=session)

    payload = {"name": "John", "username": "john01", "email": "john@test.com"}
    r = client.create_user(payload)
    assert r.status_code == 201

    data = r.json()
    assert data["name"] == "John"
    assert "id" in data


def test_update_user(session, base_url, user_id):
    client = JsonPlaceholderClient(base_url=base_url, session=session)

    payload = {"id": user_id, "name": "John Updated", "username": "john02", "email": "john.updated@test.com"}
    r = client.update_user(user_id, payload)
    assert r.status_code == 200

    data = r.json()
    assert data["id"] == user_id
    assert data["name"] == "John Updated"
