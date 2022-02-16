

class Users:
    def __init__(self, db) -> None:
        self._users_collection = db.users
        
    # TODO encode users last and first name to store properly
    def add_user(self, user_data):
        self._users_collection.insert_one({
            "user_id": user_data["user_id"],
            "username": user_data["username"],
            "chat_id": user_data["chat_id"],
            "first_name": user_data["first_name"],
            "second_name": user_data["second_name"],
            "email": user_data["email"],
            "cart": []
        })

    def user_exists(self, user_id):
        return bool(
            self._users_collection.count_documents({"user_id": user_id})
        )

    def get_user_by_id(self, user_id):
        return self._users_collection.find_one({"user_id": user_id})

    def get_user_by_username(self, username):
        return self._users_collection.find_one({"username": username})

    def check_email(self, email):
        return bool(
            self._users_collection.count_documents({"email": email})
        )

    def add_product_in_cart(self, user_id, product_id):
        self._users_collection.update_one(
            {
                "user_id": user_id 
            }, 
            {
                "$push": {
                    "cart": product_id 
                }
            }
        )

    def delete_product_from_cart(self, user_id, product_id):
        self._users_collection.update_one(
            {
                "user_id": user_id
            },
            {
                "$pull": {
                    "cart": product_id
                }
            }
        )

    def get_cart(self, user_id):
        user = self._users_collection.find_one({
            "user_id": user_id
        })
        return user["cart"]

    def is_product_in_cart(self, user_id, product_id):
        user_cart = self.get_cart(user_id)
        return True if product_id in user_cart else False
    
    