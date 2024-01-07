from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def airports(text: str | list):
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]

    [builder.button(text=txt) for txt in text]
    return builder.as_markup()


def inline_airports(text: str | dict) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    tmp = dict()
    if isinstance(text, str):
        tmp[text] = text
    tmp = text

    for key, value in tmp.items():
        builder.button(text=f"{key}", callback_data=f"{value}")

    builder.adjust(3, 2)

    return builder.as_markup()
