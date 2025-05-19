from uuid import UUID

from pydantic import EmailStr

from app.domain.user import User, UserCreate, UserPartialUpdate, UserUpdate
from app.domain.user.usecases import (
    CreateUserUseCase,
    DeleteUserByIdUseCase,
    GetUserByEmailUseCase,
    GetUserByIdUseCase,
    PartialUpdateUserUseCase,
    UpdateUserUseCase,
)
from app.infrastructure.database import PostgresConnectionManager
from app.infrastructure.database.postgres.repositories import PostgresUserRepository


class UserService:
    """User service."""

    def __init__(self, db: PostgresConnectionManager):
        self.db = db

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        async with self.db.get_connection() as conn:
            repo = PostgresUserRepository(conn)
            use_case = GetUserByIdUseCase(repo)
            return await use_case.execute(user_id)

    async def get_user_by_email(self, email: EmailStr) -> User | None:
        async with self.db.get_connection() as conn:
            repo = PostgresUserRepository(conn)
            use_case = GetUserByEmailUseCase(repo)
            return await use_case.execute(email)

    async def create_user(self, user: UserCreate) -> User:
        async with self.db.get_connection() as conn:
            repo = PostgresUserRepository(conn)
            use_case = CreateUserUseCase(repo)
            return await use_case.execute(user)

    async def update_user(self, user: UserUpdate) -> User:
        async with self.db.get_connection() as conn:
            repo = PostgresUserRepository(conn)
            use_case = UpdateUserUseCase(repo)
            return await use_case.execute(user)

    async def partially_update_user(self, user: UserPartialUpdate) -> User:
        async with self.db.get_connection() as conn:
            repo = PostgresUserRepository(conn)
            use_case = PartialUpdateUserUseCase(repo)
            return await use_case.execute(user)

    async def delete_user_by_id(self, user_id: UUID) -> None:
        async with self.db.get_connection() as conn:
            repo = PostgresUserRepository(conn)
            use_case = DeleteUserByIdUseCase(repo)
            return await use_case.execute(user_id)
