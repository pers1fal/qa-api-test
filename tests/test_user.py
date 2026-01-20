import pytest
from models.user import User

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    # 1. Статус код
    assert response.status_code == 200

    # 2. JSON
    data = response.json()

    # 3. КОНТРАКТНА ВАЛІДАЦІЯ ЧЕРЕЗ PYDANTIC
    user = User(**data)

    # 4. Бізнес перевірка
    assert user.id == user_id
