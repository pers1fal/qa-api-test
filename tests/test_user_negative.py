import pytest

@pytest.mark.parametrize("user_id", [9999, -1, 0])
def test_get_user_not_found(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    
    
    assert response.status_code == 404
    
    data = response.json()  
    
    assert data == {} or data is None