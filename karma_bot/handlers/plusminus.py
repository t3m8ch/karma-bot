import logging

from aiogram import types
from aiogram.dispatcher.filters import Text

from karma_bot.loader import dp, karma_service


@dp.message_handler(Text(equals=["+"]))
async def cmd_plus(message: types.Message):
    reply_to = message.reply_to_message

    reply_user = reply_to.from_user
    message_user = message.from_user

    if reply_to is not None:
        if reply_user.id == message_user.id:
            await message.reply("Нельзя себе прибавить карму!")
        else:
            await karma_service.increment_karma(reply_user.id)
            logging.info(f"+1 to {reply_user.username}. "
                         f"Current: {await karma_service.get_karma(reply_user.id)}")


@dp.message_handler(Text(equals=["-"]))
async def cmd_minus(message: types.Message):
    reply_to = message.reply_to_message

    reply_user = reply_to.from_user
    message_user = message.from_user

    if reply_to is not None:
        if reply_user.id == message_user.id:
            await message.reply("Нельзя себе убавить карму!")
        else:
            await karma_service.decrement_karma(reply_user.id)
            logging.info(f"-1 to {reply_user.username}. "
                         f"Current: {await karma_service.get_karma(reply_user.id)}")
