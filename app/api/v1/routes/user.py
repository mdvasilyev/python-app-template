from uuid import UUID

from fastapi import Path, Query, Request
from pydantic import EmailStr
from starlette import status

from app.api.v1.routes import users_router as router
from app.api.v1.schemas import Ok, User, UserPatch, UserPost, UserPut
from app.infrastructure.services import UserService


@router.get(
    "users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(
    request: Request,
    user_id: UUID = Path(..., description="User id"),
) -> User:
    """Get user by id."""

    user_service: UserService = request.state.user_service

    return await user_service.get_user_by_id(user_id)


@router.get(
    "users/",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def get_user_by_email(
    request: Request,
    email: EmailStr = Query(..., description="User email"),
) -> User:
    """Get user by email."""

    user_service: UserService = request.state.user_service

    return await user_service.get_user_by_email(email)


@router.post(
    "users/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
async def post_user(
    request: Request,
    user: UserPost,
) -> User:
    """Post user."""

    user_service: UserService = request.state.user_service

    return await user_service.create_user(user.to_domain())


@router.put(
    "users/",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def put_user(
    request: Request,
    user: UserPut,
) -> User:
    """Put user."""

    user_service: UserService = request.state.user_service

    return await user_service.update_user(user.to_domain())


@router.patch(
    "users/",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def patch_user(
    request: Request,
    user: UserPatch,
) -> User:
    """Patch user."""

    user_service: UserService = request.state.user_service

    return await user_service.partially_update_user(user.to_domain())


@router.delete(
    "users/{user_id}",
    response_model=Ok,
    status_code=status.HTTP_200_OK,
)
async def delete_user(
    request: Request,
    user_id: UUID = Path(..., description="User id"),
) -> Ok:
    """Delete user by id."""

    user_service: UserService = request.state.user_service

    await user_service.delete_user_by_id(user_id)

    return Ok()
