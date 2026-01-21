class PostsAPI:
    BASE = "/posts"

    @staticmethod
    def collection():
        return PostsAPI.BASE

    @staticmethod
    def by_id(post_id: int):
        return f"{PostsAPI.BASE}/{post_id}"

