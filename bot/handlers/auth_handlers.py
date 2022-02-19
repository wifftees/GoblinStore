from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from shared import callback_auth, callback_payment
from aiogram.types import Message
from core import users
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils import validate_name, validate_email, user_have_premium
from utils.keyboards import create_keyboard, categories_keyboard, payment_keyboard


class RegistrationSteps(StatesGroup):
    first_name = State()
    second_name = State()
    email = State()


async def start_registration(call: CallbackQuery, callback_data: dict, state: FSMContext):
    chat_id = call.message.chat.id
    username = call.from_user.username
    user_id = call.from_user.id
    await state.update_data(username=username, chat_id=chat_id, user_id=user_id)
    await call.message.answer("Пожалуйста, введите свое имя: ", reply_markup=create_keyboard(["Отменить"]))
    await RegistrationSteps.first_name.set()
    await call.answer()


async def first_name(message: Message, state: FSMContext):
    name = message.text
    if validate_name(name):
        await state.update_data(first_name=name)
        await message.answer("Пожалуйста введите фамилию: ")
        await RegistrationSteps.next()
    else:
        await message.answer("Пожалуйста, введите корректное имя: ")


async def second_name(message: Message, state: FSMContext):
    name = message.text
    if validate_name(name):
        await state.update_data(second_name=name)
        await message.answer("Пожалуйста введите свою электронную почту: ")
        await RegistrationSteps.next()
    else:
        await message.answer("Пожалуйста, введите корректную фамилию: ")


async def email(message: Message, state: FSMContext):
    email_address = message.text
    if validate_email(email_address):
        if not users.check_email(email_address):
            await state.update_data(email=email_address)
            # adding user in database
            user_data = await state.get_data()
            user_id = user_data["user_id"]
            users.add_user(user_data)
            await message.answer("Вы успешно зарегистрировались.", reply_markup=categories_keyboard(user_id))
            await state.finish()
            # premium offer, using as a mockup
            if not user_have_premium(user_id):
                await message.answer("Предлагаем вам получить премиум доступ, который предоставит вам доступ к играм,"
                                     " а также к некоторым дополнительным функция бота",
                                     reply_markup=payment_keyboard())

        else:
            await message.answer("Данный адрес электронной почты уже зерегистрирован, пожалуйста попробуйте другой.")
    else:
        await message.answer("Пожалуйста, введите корректный адрес электронной почты. ")


async def premium_access(call: CallbackQuery, callback_data: dict):
    user_id = call.from_user.id
    message = call.message
    answer = callback_data["answer"]
    if answer:
        users.add_premium(user_id)
        await message.delete()
        await message.answer("Премиум доступ успешно получен")
    else:
        await message.delete()

def register_auth_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_registration, callback_auth.filter(action=["start"]), state="*")
    dp.register_message_handler(first_name, state=RegistrationSteps.first_name)
    dp.register_message_handler(second_name, state=RegistrationSteps.second_name)
    dp.register_message_handler(email, state=RegistrationSteps.email)
    dp.register_callback_query_handler(premium_access, callback_payment.filter())

