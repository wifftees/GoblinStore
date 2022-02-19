from aiogram import Dispatcher
from aiogram.types import Message
from utils.keyboards import create_keyboard
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext


async def start(message: Message):
    await message.answer(
        'Здравствуй путешественник. Добро пожаловать в мою скромную лавку. Здесь ты можешь найти все: '
        + 'от мечей любого размера, до тех зелий которые нельзя называть.',
        reply_markup=create_keyboard(['Игры', 'Товары']))


async def cancel_registration(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Процесс регистрации остановлен", reply_markup=create_keyboard(['Игры', 'Товары']))

    
def register_command_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(cancel_registration, Text(equals="Отменить", ignore_case=True), state="*")

