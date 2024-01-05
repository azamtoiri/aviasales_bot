from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import LoginUrl


def create_inline_button() -> InlineKeyboardMarkup:
    # Создание инлайн-клавиш для других событий
    button = [[InlineKeyboardButton("Нажми меня", callback_data='inline_button_click')]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


url = LoginUrl(url="https://t.me/azamtoiri_work")
operating_mode = InlineKeyboardButton(text='Часы работы', callback_data="inline_button_click")

kb_client = InlineKeyboardMarkup()
kb_client.add(operating_mode)
