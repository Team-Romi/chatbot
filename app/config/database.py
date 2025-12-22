from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config.settings import get_settings

_settings = get_settings()

_engine = create_async_engine(
  _settings.postgres_url,
  pool_pre_ping=True,
)

_async_session_factory = async_sessionmaker(
  bind=_engine,
  expire_on_commit=False,
  autoflush=False,
)


def get_async_session_factory() -> async_sessionmaker[AsyncSession]:
  return _async_session_factory


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
  async with _async_session_factory() as session:
    yield session
