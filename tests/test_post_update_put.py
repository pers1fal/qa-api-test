import pytest


@pytest.mark.regression
@pytest.mark.positive
def test_update_post_with_put(api_client):
    """
    Verify that a post can be fully updated using PUT
    """

    post_id = 1

    payload = {
        "id": post_id,
        "title": "Updated title",
        "body": "Updated body content",
        "userId": 1
    }

    # ACT
    response = api_client.put(f"/posts/{post_id}", json=payload)

    # ASSERT: status code
    assert response.status_code == 200

    data = response.json()

    # ASSERT: response body
    assert data["id"] == post_id
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
