import requests
from config.settings import BASE_URL, TIMEOUT


class APIClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    def get(self, endpoint: str, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers, timeout=TIMEOUT)
        return response

    def post(self, endpoint, json=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=json
            )