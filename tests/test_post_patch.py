import pytest

@pytest.mark.regression
@pytest.mark.positive
def test_patch_post_title(api_client):
    post_id = 1

    payload = {
        "title": "Patched title"
    }

    response = api_client.patch(f"/posts/{post_id}", json=payload)

    assert response.status_code == 200

    data = response.json()

    # перевіряємо, що змінилось тільки поле title
    assert data["title"] == payload["title"]

    # інші поля існують
    assert "body" in data
    assert "userId" in data
    assert "id" in data
