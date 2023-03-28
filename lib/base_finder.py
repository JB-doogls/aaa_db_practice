from datetime import datetime
from typing import Optional


class DatabaseClient:
    def __init__(self):
        self.database = ...  # PostgresClient() or RedisClient()

    async def find_last_users_contact(self, sender: int, recipient: int) -> Optional[datetime]:
        ...

    async def is_users_the_same(self, sender: int, recipient: int) -> bool:
        ...


class Finder:
    def __init__(self):
        self.db = DatabaseClient()

    async def check_contact(self, sender: int, recipient: int) -> bool:
        ...
