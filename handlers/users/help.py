from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command('help'))
async def bot_help(msg: types.Message):
    text = ("Команды:",
            "/start - Старт бота",
            "/help - получить помощь")
    await msg.answer(text='\n'.join(text))
