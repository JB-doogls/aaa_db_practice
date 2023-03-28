from typing import Optional

import asyncpg


class PostgresClient:
    def __init__(self):
        self.client: Optional[asyncpg.connection.Connection] = None

    async def connect(self):
        self.client = await asyncpg.connect()

    async def disconnect(self):
        if not self.client:
            return
        await self.client.close()
