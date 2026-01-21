import pytest
from api.posts import PostsAPI
from models.post import Post

@pytest.mark.regression
@pytest.mark.positive
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(api_client, post_id):
    response = api_client.get(
        PostsAPI.by_id(post_id)
    )

    assert response.status_code == 200

    post = Post(**response.json())
    assert post.id == post_id

