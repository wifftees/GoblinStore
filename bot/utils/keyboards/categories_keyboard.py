from utils.keyboards import create_keyboard
from core import users


def categories_keyboard(user_id):
    if users.user_exists(user_id) and len(users.get_cart(user_id)):
        return create_keyboard([
            'Оружие',
            'Броня',
            'Зелья',
            "Корзина",
            "Домой"
        ])
    else:
        return create_keyboard([
            'Оружие',
            'Броня',
            'Зелья',
            "Домой"
        ])

