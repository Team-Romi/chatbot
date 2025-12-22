from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, AsyncEngine

from app.config.settings import get_settings
from app.utils.logger import logger

_settings = get_settings()

_engine = create_async_engine(
  _settings.postgres_url,
  pool_pre_ping=True,
  echo=False,  # SQL 쿼리 로깅
)

_async_session_factory = async_sessionmaker(
  bind=_engine,
  expire_on_commit=False,
  autoflush=False,
)


def get_async_engine() -> AsyncEngine:
  return _engine


def get_async_session_factory() -> async_sessionmaker[AsyncSession]:
  return _async_session_factory


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
  async with _async_session_factory() as session:
    try:
      yield session
    except Exception as e:
      logger.error(f"Postgres DB 에러: {e}")
      await session.rollback()
      raise
    finally:
      await session.close()
