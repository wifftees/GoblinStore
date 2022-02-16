from aiogram import types


def create_keyboard(buttons):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


def create_inline_keyboard(buttons):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard
