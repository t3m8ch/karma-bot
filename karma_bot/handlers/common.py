from aiogram import types

from karma_bot.loader import dp


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Hello!")
