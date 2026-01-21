import pytest


@pytest.mark.regression
@pytest.mark.positive
def test_delete_post_by_id(api_client):
    """
    Verify that a post can be deleted by ID
    """

    post_id = 1

    response = api_client.delete(f"/posts/{post_id}")

    assert response.status_code == 200

    data = response.json()
    assert data == {}
