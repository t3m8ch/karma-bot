from aiogram import types
from aiogram.dispatcher.filters import Text

from karma_bot.loader import dp, karma_service


@dp.message_handler(commands=["karma"])
@dp.message_handler(Text(equals=["karma", "карма"]))
async def cmd_karma(message: types.Message):
    user_id = message.from_user.id
    karma = await karma_service.get_karma(user_id)
    await message.reply(f"Ваша карма - {karma}")
