import pytest
from api.posts import PostsAPI


@pytest.mark.regression
@pytest.mark.negative
def test_patch_post_empty_payload(api_client):
    post_id = 1

    response = api_client.patch(
        PostsAPI.by_id(post_id),
        json={}
    )

    assert response.status_code == 200

    data = response.json()

    # PATCH with empty payload returns unchanged resource
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
    assert "userId" in data


@pytest.mark.regression
@pytest.mark.negative
def test_patch_post_with_invalid_field(api_client):
    post_id = 1

    payload = {
        "invalid_field": "some value"
    }

    response = api_client.patch(
        PostsAPI.by_id(post_id),
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    # existing fields are preserved
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
    assert "userId" in data

    # invalid field is echoed back
    assert data["invalid_field"] == payload["invalid_field"]
