from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = [[
    InlineKeyboardButton(text="Москва", callback_data='mow'),
    InlineKeyboardButton(text="Душанбе", callback_data='dyu')
]]
airports_choose = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
