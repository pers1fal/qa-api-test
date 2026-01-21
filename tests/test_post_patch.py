import pytest
from api.posts import PostsAPI
from models.post import Post


@pytest.mark.regression
@pytest.mark.positive
def test_patch_post_title(api_client):
    post_id = 1

    payload = {
        "title": "Patched title"
    }

    # ACT
    response = api_client.patch(
        PostsAPI.by_id(post_id),
        json=payload
    )

    # ASSERT: status code
    assert response.status_code == 200

    # ASSERT: schema
    post = Post(**response.json())

    # ASSERT: business logic
    assert post.title == payload["title"]
    assert post.id == post_id
