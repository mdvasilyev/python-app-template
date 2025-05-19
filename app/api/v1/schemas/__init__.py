"""API v1 schemas module."""

from .user import User, UserPatch, UserPost, UserPut

__all__ = [
    "User",
    "UserPost",
    "UserPut",
    "UserPatch",
]
