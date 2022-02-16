from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shared.callback_data import callback_product


def product_keyboard(id, added=False):
    keyboard = InlineKeyboardMarkup()
    more_button = InlineKeyboardButton(
            text="Подробнее",
            callback_data=callback_product.new(
                id=id,
                action="more"
            )
        )
    add_button = InlineKeyboardButton(
            text="В корзину",
            callback_data=callback_product.new(
                id=id,
                action="add"
            )
        )
    added_button = InlineKeyboardButton(
            text="Добавлено",
            callback_data=callback_product.new(
                id=id,
                action="added"
            )
        )
    keyboard.add(more_button)
    if added:
        return keyboard.add(added_button)
    else:
        return keyboard.add(add_button)
