import uuid
from datetime import datetime, timezone

from pydantic import EmailStr
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from app.infrastructure.database import PostgresBase


class UserORM(PostgresBase):
    __tablename__ = "users"

    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: EmailStr = Column(String(320), unique=True, nullable=False)
    name: str = Column(String(256), nullable=False)
    hashed_password: str = Column(String(256), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at: datetime = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
