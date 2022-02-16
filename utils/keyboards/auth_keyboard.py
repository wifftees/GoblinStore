from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shared import callback_auth


def auth_keyboard(product_id):
    keyboard = InlineKeyboardMarkup()
    register_button = InlineKeyboardButton(
            text="Зарегистрироваться",
            callback_data=callback_auth.new(
                action="start",
                product_id=product_id
            )
        )
    return keyboard.add(register_button)
