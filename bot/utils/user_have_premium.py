from core import users


def user_have_premium(user_id):
    return users.check_premium(user_id)