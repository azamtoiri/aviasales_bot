from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = [[
    KeyboardButton(text='Москва'),
    KeyboardButton(text='Душанбе')
]]

airports = ReplyKeyboardMarkup(
    keyboard=reply_keyboard,
    resize_keyboard=True,
    input_field_placeholder="Выберите что вы хотите сделать"
)
