import pytest

@pytest.mark.negative
def test_get_user_not_found(api_client):
    response = api_client.get("/users/9999")

    assert response.status_code == 404

    data = response.json()

    assert data == {}