import pytest
from api.posts import PostsAPI


@pytest.mark.regression
@pytest.mark.negative
def test_delete_post_twice(api_client):
    """
    Verify that DELETE operation is idempotent
    """

    post_id = 1

    first_response = api_client.delete(
        PostsAPI.by_id(post_id)
    )
    second_response = api_client.delete(
        PostsAPI.by_id(post_id)
    )

    assert first_response.status_code == 200
    assert second_response.status_code in (200, 404)

