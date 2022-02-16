from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher
from aiogram.types import Message
from utils.keyboards import categories_keyboard, create_keyboard


async def games(message: Message):
    await message.answer('Игры')


async def products(message: Message):
    user_id = message.from_user.id
    await message.answer('Вы сделали хороший выбор зайдя\
        в наш магазин. Посмотри товары на полках, все\
        это твое, были бы только деньги', reply_markup=categories_keyboard(user_id))


async def home(message: Message):
    await message.answer("Вы вернулись на стартовую страницу", reply_markup=create_keyboard(['Игры', 'Товары']))


def register_home_handlers(dp: Dispatcher):
    dp.register_message_handler(games, Text(equals='Игры', ignore_case=True))
    dp.register_message_handler(products, Text(equals='Товары', ignore_case=True))
    dp.register_message_handler(home, Text(equals="Домой", ignore_case=True))
