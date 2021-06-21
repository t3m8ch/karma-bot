from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from karma_bot.loader import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.reply("Hello!")
