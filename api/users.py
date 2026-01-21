class UsersAPI:
    BASE = "/users"

    @staticmethod
    def collection():
        return UsersAPI.BASE

    @staticmethod
    def by_id(user_id: int):
        return f"{UsersAPI.BASE}/{user_id}"
