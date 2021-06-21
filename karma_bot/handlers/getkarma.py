from aiogram import types
from aiogram.dispatcher.filters import Text

from karma_bot.loader import dp, karma_service


@dp.message_handler(lambda m: len(m.text.split()) == 2, commands=["karma"])
@dp.message_handler(lambda m: len(m.text.split()) == 2,
                    Text(contains=["karma", "карма"]))
async def cmd_karma_of_user(message: types.Message):
    user_info = message.text.split()[1]
    if "@" in user_info:
        pass  # TODO: Implement the ability to use the user name as an argument to the command
    elif user_info.isnumeric():
        karma = await karma_service.get_karma(int(user_info))
        await message.reply(f"Карма пользователя - {karma}")
    else:
        await message.reply(f"После команды вы должны написать ID или @имя_пользователя,\n"
                            f"Либо ничего не писать: /karma")


@dp.message_handler(lambda m: len(m.text.split()) == 1, commands=["karma"])
@dp.message_handler(Text(equals=["karma", "карма"]))
async def cmd_karma_of_self(message: types.Message):
    user_id = message.from_user.id
    karma = await karma_service.get_karma(user_id)
    await message.reply(f"Ваша карма - {karma}")
