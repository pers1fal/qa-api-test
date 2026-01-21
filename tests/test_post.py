import pytest
from api.posts import PostsAPI

@pytest.mark.regression
def test_create_post(api_client):
    payload = {
        "title": "My first post",
        "body": "Hello from API tests",
        "userId": 1
    }

    response = api_client.post(
        PostsAPI.collection(),
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert "id" in data
    assert isinstance(data["id"], int)
