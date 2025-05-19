from uuid import UUID

from pydantic import EmailStr

from .entities import User, UserCreate, UserPartialUpdate, UserUpdate
from .interfaces import AbstractUserRepository


class GetUserByIdUseCase:
    """Getting user by id use-case."""

    def __init__(self, repo: AbstractUserRepository) -> None:
        self.repo = repo

    async def execute(self, user_id: UUID) -> User | None:
        return await self.repo.get_by_id(user_id)


class GetUserByEmailUseCase:
    """Getting user by email use-case."""

    def __init__(self, repo: AbstractUserRepository) -> None:
        self.repo = repo

    async def execute(self, email: EmailStr) -> User | None:
        return await self.repo.get_by_email(email)


class CreateUserUseCase:
    """Creating user use-case."""

    def __init__(self, repo: AbstractUserRepository) -> None:
        self.repo = repo

    async def execute(self, user: UserCreate) -> User:
        return await self.repo.post(user)


class UpdateUserUseCase:
    """Updating all user attributes use-case."""

    def __init__(self, repo: AbstractUserRepository) -> None:
        self.repo = repo

    async def execute(self, user: UserUpdate) -> User:
        return await self.repo.put(user)


class PartialUpdateUserUseCase:
    """Updating some user attributes use-case."""

    def __init__(self, repo: AbstractUserRepository) -> None:
        self.repo = repo

    async def execute(self, user: UserPartialUpdate) -> User:
        return await self.repo.patch(user)


class DeleteUserByIdUseCase:
    """Deleting user by id use-case."""

    def __init__(self, repo: AbstractUserRepository) -> None:
        self.repo = repo

    async def execute(self, user_id: UUID) -> None:
        return await self.repo.delete_by_id(user_id)
