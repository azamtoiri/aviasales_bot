import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.middlewares.request_logging import logger


def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    from handlers import setup_routers

    dispatcher.include_router(setup_routers())


def setup_filters(dispatcher: Dispatcher) -> None:
    """FILTERS"""
    from filters import ChatPrivateFilter

    dispatcher.message.filter(ChatPrivateFilter(chat_type=['private']))


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    setup_middlewares(dispatcher=dispatcher, bot=bot)
    setup_filters(dispatcher=dispatcher)
    logger.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Starting polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(bot=bot, dispatcher=dispatcher)


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    """CONFIG"""
    from constants import Settings
    from aiogram.enums import ParseMode
    from aiogram.fsm.storage.memory import MemoryStorage

    bot = Bot(token=Settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    dispatcher.startup.register(aiogram_on_startup_polling)
    dispatcher.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dispatcher.start_polling(bot, close_bot_session=True))
    # allowed_updates=['message', 'chat_member']


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped!")
