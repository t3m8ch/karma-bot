from abc import ABC, abstractmethod


class BaseKarmaService(ABC):
    @abstractmethod
    async def increment_karma(self, telegram_id: int):
        pass

    @abstractmethod
    async def decrement_karma(self, telegram_id: int):
        pass

    @abstractmethod
    async def get_karma(self, telegram_id: int):
        pass


class MemoryKarmaService(BaseKarmaService):
    def __init__(self):
        self._users = {}

    async def increment_karma(self, telegram_id: int):
        if telegram_id in self._users.keys():
            self._users[telegram_id] += 1
        else:
            self._users[telegram_id] = 1

    async def decrement_karma(self, telegram_id: int):
        if telegram_id in self._users.keys():
            self._users[telegram_id] -= 1
        else:
            self._users[telegram_id] = -1

    async def get_karma(self, telegram_id: int) -> int:
        if telegram_id in self._users.keys():
            return self._users[telegram_id]
        else:
            return 0
