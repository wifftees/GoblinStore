from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shared import callback_payment


# testing inline button
def payment_keyboard():
    keyboard = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
            text="Получить",
            callback_data=callback_payment.new(True)
        )
    no_button = InlineKeyboardButton(
            text="Нет",
            callback_data=callback_payment.new(False)
        )
    return keyboard.add(yes_button, no_button)
