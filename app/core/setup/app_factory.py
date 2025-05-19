from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import GlobalConfig
from app.infrastructure.database.postgres import PostgresConnectionManager


def bind_routes(app: FastAPI, routes: list[APIRouter]) -> None:
    for route in routes:
        app.include_router(route)


def get_app(config: GlobalConfig) -> FastAPI:
    """App factory function."""

    app: FastAPI = FastAPI(
        debug=config.app.debug,
        title=config.app.name,
        summary="Clean architecture based Python app template",
        description="This template tries to give you a good starting point to build apps with FastAPI",
        version="",
        lifespan="",
        terms_of_service="https://swagger.io/terms/",
        contact={"email": "mayxis@inbox.ru"},
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

    bind_routes(app, routes)

    connection_manager: PostgresConnectionManager = PostgresConnectionManager()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
