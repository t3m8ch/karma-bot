import logging

from aiogram import types
from aiogram.dispatcher.filters import Text

from karma_bot.loader import dp


@dp.message_handler(Text(equals=["+"]))
async def cmd_plus(message: types.Message):
    reply_to = message.reply_to_message
    if reply_to is not None:
        if reply_to.from_user.id == message.from_user.id:
            logging.info(f"OH!")
        else:
            logging.info(f"+1 to {reply_to.from_user.username}")


@dp.message_handler(Text(equals=["-"]))
async def cmd_minus(message: types.Message):
    reply_to = message.reply_to_message
    if reply_to is not None:
        if reply_to.from_user.id == message.from_user.id:
            logging.info(f"OH!")
        else:
            logging.info(f"-1 to {reply_to.from_user.username}")
