import requests


def test_get_single_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    # перевіряємо статус код
    assert response.status_code == 200

    # перетворюємо response у JSON
    data = response.json()

    # перевіряємо, що це саме користувач
    assert data["id"] == 1
    assert "username" in data
    assert "email" in data
