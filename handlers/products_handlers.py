from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher
from core import bot, products, users
from utils.keyboards import product_keyboard
from utils.keyboards import auth_keyboard
from aiogram.types import InputFile, Message, CallbackQuery
from shared import callback_product

    
async def weapons(message: Message):
    chat_id = message.chat.id
    weapons = products.get_products_by_category("weapon")
    for weapon in weapons:
        img = InputFile.from_url(weapon["url"])
        keyboard = product_keyboard(weapon["id"])
        product_name = weapon["product_name"]
        await bot.send_photo(chat_id, img, product_name, reply_markup=keyboard)
    

async def armors(message: Message):
    chat_id = message.chat.id
    armors = products.get_products_by_category("armor")
    for armor in armors:
        img = InputFile.from_url(armor["url"])
        keyboard = product_keyboard(armor["id"])
        product_name = armor["product_name"]
        await bot.send_photo(chat_id, img, product_name, reply_markup=keyboard)   
        

async def poisons(message: Message):
    chat_id = message.chat.id
    poisons = products.get_products_by_category("poison")
    for poison in poisons:
        img = InputFile.from_url(poison["url"])
        keyboard = product_keyboard(poison["id"])
        product_name = poison["product_name"]
        await bot.send_photo(chat_id, img, product_name, reply_markup=keyboard)


async def more_callback(call: CallbackQuery, callback_data: dict):
    product_id = callback_data["id"]
    product = products.get_product_by_id(product_id)
    await call.message.answer(product["description"])
    await call.answer()
    

async def add_callback(call: CallbackQuery, callback_data: dict):
    message = call.message
    user_id = call.from_user.id
    product_id = callback_data["id"]
    if not users.user_exists(user_id):
        keyboard = auth_keyboard(product_id)
        await message.answer("Прежде чем добавлять товары в корзину вы должны зарегистрироваться",
                             reply_markup=keyboard)
    else:
        if users.is_product_in_cart(user_id, product_id):
            await message.answer("Товар уже добавлен в вашу корзину.")
        else:
            added_product_name = products.get_product_by_id(
                product_id
            )["product_name"]
            print(product_id)
            users.add_product_in_cart(user_id, product_id)
            await message.answer(f'Товар под наименованием: "{added_product_name}" был добавлен в вашу корзину')
    await call.answer()
    

def register_products_handlers(dp: Dispatcher):
    dp.register_message_handler(weapons, Text(equals="Оружие"))
    dp.register_message_handler(armors, Text(equals="Броня"))
    dp.register_message_handler(poisons, Text(equals="Зелья"))
    dp.register_callback_query_handler(more_callback, callback_product.filter(action=["more"]))
    dp.register_callback_query_handler(add_callback, callback_product.filter(action=["add"]))
