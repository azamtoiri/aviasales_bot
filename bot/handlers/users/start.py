from aiogram import Router, types
from aiogram.filters.command import CommandStart

from bot.keyboards.reply.start_buttons import ask_user

router = Router()


@router.message(CommandStart())
async def do_start(msg: types.Message):
    telegram_id = msg.from_user.id
    full_name = msg.from_user.full_name
    username = msg.from_user.username
    text = f'Привет {full_name}\nваше имя пользователя:{username}\nваш id:{telegram_id}\n'
    await msg.answer(text=''.join(text), reply_markup=ask_user)
