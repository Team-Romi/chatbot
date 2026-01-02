from sqlalchemy.ext.asyncio import AsyncEngine

from app.models.base import Base
from app.utils.logger import logger


def _import_all_models() -> None:
  from app.models.github_cursor import GithubCursorEntity


async def create_tables_if_not_exists(engine: AsyncEngine) -> None:
  _import_all_models()

  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

  logger.info("DB 테이블 생성완료")
