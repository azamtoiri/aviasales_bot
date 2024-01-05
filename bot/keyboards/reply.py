from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_start_keyboard() -> ReplyKeyboardMarkup:
    button = [[KeyboardButton(text="Начать!")],]
    keyboard = ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)

    return keyboard
