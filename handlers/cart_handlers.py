from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from core import users, products
from utils.keyboards import cart_delete_keyboard, show_cart_products, create_keyboard
from shared import callback_delete_item, callback_select_product
from utils import get_user_cart_message


async def show_cart(message: Message):
    user_id = message.from_user.id
    user_cart = users.get_cart(user_id)
    is_empty = not bool(len(user_cart))
    if is_empty:
        await message.answer("На данный момент ваша корзина пуста, отличный повод чтобы совершить покупку!")
    else:
        cart_message = get_user_cart_message(products, user_cart)
        await message.answer(cart_message, reply_markup=cart_delete_keyboard())

async def select_product(call: CallbackQuery):
    message = call.message
    user_id = call.from_user.id
    # do not pass cart products through call dict, cause of dict size limit
    user_cart = users.get_cart(user_id)
    user_cart_products = [
        products.get_product_by_id(product_id) for product_id in user_cart
    ]
    user_cart_products_names = [product["product_name"] for product in user_cart_products]
    await message.edit_reply_markup(show_cart_products(user_cart, user_cart_products_names))
    await call.answer()


async def delete_product(call: CallbackQuery, callback_data: dict):
    message = call.message
    user_id = call.from_user.id
    product_id = callback_data["product_id"]
    users.delete_product_from_cart(user_id, product_id)
    user_cart = users.get_cart(user_id)
    cart_message = get_user_cart_message(products, user_cart)
    if cart_message == "":
        await message.edit_text("На данный момент ваша корзина пуста, отличный повод чтобы совершить покупку!")

    else:
        await message.edit_text(cart_message, reply_markup=cart_delete_keyboard())


def register_cart_handlers(dp: Dispatcher):
    dp.register_message_handler(show_cart, Text(equals="Корзина", ignore_case=True))
    dp.register_callback_query_handler(select_product, callback_select_product.filter())
    dp.register_callback_query_handler(delete_product, callback_delete_item.filter())
