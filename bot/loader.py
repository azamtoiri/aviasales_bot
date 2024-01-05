from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from constants import Settings

bot = Bot(token=Settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
