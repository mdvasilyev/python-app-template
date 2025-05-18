from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime, timezone


class User(BaseModel):
    """User schema for GET request."""

    id: UUID = Field(..., description="User's id", examples=["550e8400-e29b-41d4-a716-446655440000"])
    email: EmailStr = Field(..., description="User's email", examples=["address@example.com"])
    name: str = Field(..., description="User's name", examples=["John Doe"])
    hashed_password: str = Field(..., description="User's hashed password")
    is_active: bool = Field(..., description="Active status", examples=[True, False])
    is_superuser: bool = Field(..., description="Superuser status", examples=[True, False])
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Time of creation")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Time of update")


class UserPost(BaseModel):
    """User schema for POST request."""

    email: EmailStr = Field(..., description="User's email", examples=["address@example.com"])
    name: str = Field(..., description="User's name", examples=["John Doe"])
    password: str = Field(..., description="User's password")


class UserPut(BaseModel):
    """User schema for PUT request."""

    email: EmailStr = Field(..., description="User's email", examples=["address@example.com"])
    name: str = Field(..., description="User's name", examples=["John Doe"])
    password: str = Field(..., description="User's password")


class UserPatch(BaseModel):
    """User schema for PATCH request."""

    email: EmailStr = Field(None, description="User's email", examples=["address@example.com"])
    name: str = Field(None, description="User's name", examples=["John Doe"])
    password: str = Field(None, description="User's password")
