from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

reply_keyboard = [[
    KeyboardButton(text='Купить билет'),
    KeyboardButton(text='Посмотреть цены')
]]

ask_user = ReplyKeyboardMarkup(
    keyboard=reply_keyboard,
    resize_keyboard=True,
    input_field_placeholder="Выберите что вы хотите сделать"
)
