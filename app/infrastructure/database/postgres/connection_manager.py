from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine, create_async_engine

from app.core.config import DBConfig, GlobalConfig


class PostgresConnectionManager:
    """Connection manager for PostgreSQL."""

    def __init__(self) -> None:
        self._config: DBConfig = GlobalConfig.load().db
        self._engine: AsyncEngine | None = None

    async def init(self) -> None:
        """Initialize engine."""

        if self._engine is not None:
            return

        self._engine = create_async_engine(
            f"postgresql+asyncpg://{self._config.user}:{self._config.password}"
            f"@{self._config.host}:{self._config.port}/{self._config.name}",
            future=True,
            pool_size=self._config.pool_size,
            max_overflow=5,
        )

        async with self._engine.connect() as conn:
            result = await conn.execute(select(1))
            assert result.scalar() == 1, "Database connection failed"

    @property
    def engine(self) -> AsyncEngine:
        """Engine entity."""

        if self._engine is None:
            raise RuntimeError(
                "Connection engine not initialized. Call 'init()' first."
            )
        return self._engine

    async def shutdown(self) -> None:
        """Shutdown database connection."""

        if self._engine:
            await self._engine.dispose()
            self._engine = None

    @asynccontextmanager
    async def get_connection(self) -> AsyncIterator[AsyncConnection]:
        """Get async connection to database."""

        if self._engine is None:
            await self.init()

        async with self._engine.connect() as conn:
            yield conn
