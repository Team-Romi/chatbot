import uuid
from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.enums.source_type import SourceType
from app.models.github_cursor import GithubCursorEntity


class GithubCursorRepository:
  async def find_by_repository_name_and_source_type(
    self,
    session: AsyncSession,
    repository_name: str,
    source_type: SourceType,
  ) -> Optional[GithubCursorEntity]:
    query = select(GithubCursorEntity).where(
      GithubCursorEntity.repository_name == repository_name,
      GithubCursorEntity.source_type == source_type,
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()

  async def upsert(
    self,
    session: AsyncSession,
    repository_name: str,
    source_type: SourceType,
    cursor_value: str,
  ) -> None:
    query = insert(GithubCursorEntity).values(
      id=uuid.uuid4(),
      repository_name=repository_name,
      source_type=source_type,
      cursor_value=cursor_value,
    ).on_conflict_do_update(
      index_elements=["repository_name", "source_type"],
      set_={
        "cursor_value": cursor_value,
        "updated_at": func.now(),
      },
    )
    await session.execute(query)
