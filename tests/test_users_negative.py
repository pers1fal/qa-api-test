import pytest

@pytest.mark.negative
@pytest.mark.parametrize(
    "user_id",
    [0, -1, 9999]
)
def test_get_user_with_invalid_id(api_client, user_id):
    """
    Negative test:
    Verify that API returns 404 for invalid user IDs
    """

    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 404

    data = response.json()

    assert data == {}
