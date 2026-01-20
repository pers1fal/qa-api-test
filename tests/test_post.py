import pytest

@pytest.mark.regression
def test_create_post(api_client):
    playload = {
        "title": "My first post",
        "body": "Hello from API tests",
        "userId": 1
    }
    
    response = api_client.post("/posts", json=playload)
    
    assert response.status_code == 201
    
    data = response.json()
    
    
    assert data["title"] == playload["title"]
    assert data["body"] == playload["body"]
    assert data["userId"] == playload["userId"]
    
    assert "id" in data
    assert isinstance(data["id"], int)  