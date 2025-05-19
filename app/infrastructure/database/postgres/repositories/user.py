from uuid import UUID

from pydantic import EmailStr

from app.domain.user.entities import (User, UserCreate, UserPartialUpdate,
                                      UserUpdate)
from app.domain.user.interfaces import AbstractUserRepository
from app.infrastructure.database.postgres import PostgresConnectionManager


class PostgresUserRepository(AbstractUserRepository):
    def __init__(self, connection_manager: PostgresConnectionManager):
        self._connection_manager = connection_manager

    async def get_by_id(self, user_id: UUID) -> User | None:
        pass

    async def get_by_email(self, email: EmailStr) -> User | None:
        pass

    async def post(self, user: UserCreate) -> User:
        pass

    async def put(self, user: UserUpdate) -> User:
        pass

    async def patch(self, user: UserPartialUpdate) -> User:
        pass

    async def delete_by_id(self, user_id: UUID) -> None:
        pass
