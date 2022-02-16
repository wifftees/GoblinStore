from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from shared import callback_auth
from aiogram.types import Message
from core import users, products
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils import validate_name, validate_email
from utils.keyboards import create_keyboard, categories_keyboard


class RegistrationSteps(StatesGroup):
    first_name = State()
    second_name = State()
    email = State()


async def start_registration(call: CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data["product_id"]
    chat_id = call.message.chat.id
    username = call.from_user.username
    user_id = call.from_user.id
    await state.update_data(username=username, chat_id=chat_id, user_id=user_id, product_id=product_id)
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
            product_id = user_data["product_id"]
            user_id = user_data["user_id"]
            users.add_user(user_data)
            await message.answer("Вы успешно зарегистрировались.")
            # adding product in user's cart
            users.add_product_in_cart(user_id, product_id)
            added_product_name = products.get_product_by_id(
                product_id
            )["product_name"]
            await message.answer(
                f'Товар под наименованием: "{added_product_name}" был добавлен в вашу корзину.',
                reply_markup=categories_keyboard(user_id))
            await state.finish()
        else:
            await message.answer("Данный адрес электронной почты уже зерегистрирован, пожалуйста попробуйте другой.")
    else:
        await message.answer("Пожалуйста, введите корректный адрес электронной почты. ")


def register_auth_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_registration, callback_auth.filter(action=["start"]), state="*")
    dp.register_message_handler(first_name, state=RegistrationSteps.first_name)
    dp.register_message_handler(second_name, state=RegistrationSteps.second_name)
    dp.register_message_handler(email, state=RegistrationSteps.email)

