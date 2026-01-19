def test_get_user_by_id(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    assert data["id"] == 1
    assert "name" in data
    assert "username" in data
    assert "email" in data

    assert "address" in data
    assert "company" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
