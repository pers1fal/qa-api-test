import pytest


@pytest.mark.parametrize("post_id",[1,2,3,10])
def test_get_post_by_id(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["id"] == post_id
    
    assert "title" in data
    assert "body" in data
    assert "userId" in data
    
    assert isinstance(data["id"], int)
    assert isinstance(data["userId"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)