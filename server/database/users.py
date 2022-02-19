class Users:
    def __init__(self, database) -> None:
        self._users_collection = database.users

    def get_all_users(self):
        return self._users_collection.find({})

    def get_premium_users(self):
        return self._users_collection.find({
            "premium": True
        })

    def get_default_users(self):
        return self._users_collection.find({
            "premium": False
        })
