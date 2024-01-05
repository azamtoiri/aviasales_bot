from aiogram import F
from aiogram import Router, types

from bot.keyboards.inline.buttons import are_you_sure_markup

router = Router()


@router.message()
async def start_user(msg: types.Message):
    await msg.answer(msg.text, reply_markup=are_you_sure_markup)


@router.callback_query(F.data == "yes")
async def test_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer("You clicked YES")
    try:
        await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id,
                                                message_id=callback_query.message.message_id)
    except Exception as e:
        print(e)


@router.callback_query(F.data == "no")
async def test_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer("You clicked NO!!!")
