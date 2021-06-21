from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Text

from karma_bot.loader import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.reply("Hello!")


@dp.message_handler(Text(contains=["спаси"]), lambda m: len(m.text.split()) == 2)
async def help(message: types.Message):
    await message.reply("HI")
