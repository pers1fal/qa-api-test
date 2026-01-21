import pytest
from api.posts import PostsAPI
from models.post import Post


@pytest.mark.regression
@pytest.mark.positive
def test_update_post_with_put(api_client):
    post_id = 1

    payload = {
        "id": post_id,
        "title": "Updated title",
        "body": "Updated body content",
        "userId": 1
    }

    # ACT
    response = api_client.put(
        PostsAPI.by_id(post_id),
        json=payload
    )

    # ASSERT
    assert response.status_code == 200

    post = Post(**response.json())

    assert post.id == post_id
    assert post.title == payload["title"]
    assert post.body == payload["body"]
    assert post.userId == payload["userId"]
