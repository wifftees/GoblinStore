from core import users


def check_registration(user_id):
    return users.user_exists(user_id)