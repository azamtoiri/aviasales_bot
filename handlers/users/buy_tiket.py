from aiogram import Router
from aiogram.types import Message
from aiogram import F

router = Router()


@router.message(F.text == 'Купить билет')
async def but_ticket(msg: Message):
    await msg.answer("You are buying ticket")
