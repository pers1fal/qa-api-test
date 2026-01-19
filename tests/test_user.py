import pytest

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200

    data = response.json()
    
    assert isinstance(data, dict)

    assert data["id"] == user_id
    assert "name" in data
    assert "username" in data
    assert "email" in data
    assert "address" in data
    assert "company" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
