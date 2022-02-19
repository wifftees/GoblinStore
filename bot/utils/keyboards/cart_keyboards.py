from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shared import callback_delete_item, callback_select_product


def cart_delete_keyboard():
    keyboard = InlineKeyboardMarkup()
    delete_button = InlineKeyboardButton(text="Удалить товар", callback_data=callback_select_product.new())
    return keyboard.add(delete_button)


def show_cart_products(products_ids, product_names):
    keyboard = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton(
            text=product_names[index],
            callback_data=callback_delete_item.new(product_in)
        ) for index, product_in in enumerate(products_ids)
    ]
    return keyboard.add(*buttons)
