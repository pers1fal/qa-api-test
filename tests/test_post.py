def test_create_post(api_client):
    playload = {
        "title": "My first post",
        "body": "Hello from API tests",
        "userID": 1
    }
    
    response = api_client.post("/posts", json=playload)
    
    assert response.status_code == 201
    
    data = response.json()
    
    
    assert data["title"] == playload["title"]
    assert data["body"] == playload["body"]
    assert data["userID"] == playload["userID"]
    
    assert "id" in data
    assert isinstance(data["id"], int)  