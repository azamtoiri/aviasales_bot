import logging

from aiogram import Bot


async def on_startup_notify(bot: Bot):
    try:
        bot_properties = await bot.me()
        message = ["<b>Bot ishga tushdi.</b>\n",
                   f"<b>Bot ID:</b> {bot_properties.id}",
                   f"<b>Bot Username:</b> {bot_properties.username}"]
        await bot.send_message('6083203294', "\n".join(message))
    except Exception as err:
        logging.exception(err)