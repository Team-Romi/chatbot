import uuid
from datetime import datetime

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import UniqueConstraint, Index, String, DateTime, func
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.enums.source_type import SourceType


class GithubCursorEntity(Base):
  __tablename__ = "github_cursor"
  __table_args__ = (
    UniqueConstraint("repository_name", "source_type", name="uq_github_cursor"),
    Index("idx_github_cursor_repo_type", "repository_name", "source_type")
  )

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

  repository_name: Mapped[str] = mapped_column(String(200), nullable=False)

  source_type: Mapped[SourceType] = mapped_column(SqlEnum(SourceType, native_enum=False), nullable=False)

  cursor_value: Mapped[str] = mapped_column(String(500), nullable=False)

  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
