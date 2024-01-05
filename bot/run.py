import asyncio
import logging

from constants import Settings

from aiogram import Bot, Dispatcher

from bot.filters import register_all_filters
from bot.handlers import register_all_handlers
from bot.database.models import register_models

# Настройка логирования
logging.basicConfig(level=logging.INFO)


async def __on_start_up(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()


async def main():
    bot = Bot(token=Settings.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    await dp.start_polling(bot, __on_start_up=__on_start_up)


if __name__ == "__main__":
    asyncio.run(main())