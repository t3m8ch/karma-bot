import asyncio

from aiogram import Bot, Dispatcher

from karma_bot.config import TG_TOKEN

event_loop = asyncio.get_event_loop()

bot = Bot(token=TG_TOKEN, loop=event_loop)
dp = Dispatcher(bot, loop=event_loop)
