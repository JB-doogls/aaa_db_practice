import asyncio
from typing import List

from lib.pg_client import PostgresClient


class ContactChecker:
    def __init__(self):
        self.db = PostgresClient()
        # use it like await self.db.client.fetch(...)

    @staticmethod
    def extract_from_rows(rows: List[dict], key: str) -> set:
        result = set()
        for row in rows:
            result.add(row[key])
        return result

    async def is_users_has_contact(self, sender_id: int, recipient_id: int) -> bool:
        """ этот метод необходимо реализовать """
        ...

    async def get_user_cookie(self, user_id: int) -> List[dict]:
        """ этот метод необходимо реализовать """
        ...

    async def get_user_ip(self, user_id: int) -> List[dict]:
        """ этот метод необходимо реализовать """
        ...

    async def is_users_the_same(self, sender_id: int, recipient_id: int) -> bool:
        # получаем cookie обоих пользователей
        sender_cookie = await self.get_user_cookie(sender_id)
        recipient_cookie = await self.get_user_cookie(recipient_id)

        # получаем set из найденных записей, находим пересечение
        same_cookie = (
                self.extract_from_rows(sender_cookie, 'cookie')
                & self.extract_from_rows(recipient_cookie, 'cookie')
        )

        # если нет пересечения cookie, значит не было накрутки
        if not same_cookie:
            return False

        # получаем set из найденных записей, находим пересечение
        sender_ip = await self.get_user_ip(sender_id)
        recipient_ip = await self.get_user_ip(recipient_id)
        same_ip = self.extract_from_rows(sender_ip, 'ip') & self.extract_from_rows(recipient_ip, 'ip')

        return bool(same_ip)

    async def check_users(self, sender_id: int, recipient_id: int) -> None:
        """
            этот метод необходимо реализовать
              - проверить наличие контакта. Если был хотя бы 1 контакт
              - проверить наличие накрутки
              - напечатать результат проверок в консоль в удобном вам формате
        """
        await self.db.connect()

        # тут должен быть ваш код :)

        await self.db.disconnect()


if __name__ == '__main__':
    sender, recipient = input('give me sender and recipient: ').split(',')
    checker = ContactChecker()
    asyncio.run(checker.check_users(int(sender), int(recipient)))
