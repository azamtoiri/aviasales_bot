from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

# from bot.keyboards.inline import create_inline_button, kb_client


# async def send_inline_button(message: Message):
#     await message.reply("Для того чтобы начать нажмите 'Начать!'", reply_markup=kb_client)


# async def echo(msg: Message):
#     await msg.answer(msg.text, reply_markup=create_inline_button())


async def send_welcome(message: Message):
    await message.reply("Привет! Я бот.")


# async def handle_inline_button_click(callback_query: CallbackQuery):
#     Обработчик для нажатия на кнопку инлайн-клавиатуры
    # await callback_query.answer("Вы нажали на кнопку!")


# async def handle_other_event(message: Message, state: FSMContext):
#     Обработчик других событий
# await message.answer("Это другое событие.", reply_markup=create_inline_button())


def register_other_handlers(dp: Dispatcher) -> None:
    # dp.message.register(send_inline_button, commands=['button'])
    # dp.callback_query.register(handle_inline_button_click, text='inline_button_click')
    dp.message.register(send_welcome, Command('start'))
