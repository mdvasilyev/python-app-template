from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from pydantic import EmailStr

from .entities import User, UserCreate, UserPartialUpdate, UserUpdate


class AbstractUserRepository(Protocol):
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User | None:
        """Get user by id."""

    @abstractmethod
    async def get_by_email(self, email: EmailStr) -> User | None:
        """Get user by email."""

    @abstractmethod
    async def post(self, user: UserCreate) -> User:
        """Post user entity."""

    @abstractmethod
    async def put(self, user: UserUpdate) -> User:
        """Put user entity."""

    @abstractmethod
    async def patch(self, user: UserPartialUpdate) -> User:
        """Patch user entity."""

    @abstractmethod
    async def delete_by_id(self, user_id: UUID) -> None:
        """Delete user by id."""
