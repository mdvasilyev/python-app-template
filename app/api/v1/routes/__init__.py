"""API v1 routes module."""

from fastapi import APIRouter

users_router = APIRouter(prefix="/v1", tags=["Users"])

routes = [users_router]

__all__ = [
    "routes",
]
