from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Старт бота"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/find_ticket", description="Поиск билетов")
    ]
    await bot.set_my_commands(commands=commands)
