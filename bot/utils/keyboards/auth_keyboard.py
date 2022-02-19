from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shared import callback_auth


def auth_keyboard():
    keyboard = InlineKeyboardMarkup()
    register_button = InlineKeyboardButton(
            text="Зарегистрироваться",
            callback_data=callback_auth.new(
                action="start"
            )
        )
    return keyboard.add(register_button)
