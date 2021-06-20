import logging

from aiogram.utils import executor

from karma_bot.config import LOGGING_LEVEL, LOGGING_FORMAT
from karma_bot.loader import dp, event_loop

import karma_bot.handlers  # Don't delete this!


def run():
    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT
    )
    # TODO: Change to webhook
    executor.start_polling(dp, loop=event_loop)


if __name__ == "__main__":
    run()
