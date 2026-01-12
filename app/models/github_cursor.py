from sqlalchemy import Enum as SqlEnum
from sqlalchemy import UniqueConstraint, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, PrimaryKeyMixin, TimestampMixin
from app.models.enums.source_type import SourceType


class GithubCursorEntity(Base, PrimaryKeyMixin, TimestampMixin):
  __tablename__ = "github_cursor"
  __table_args__ = (
    UniqueConstraint("repository_name", "source_type", name="uq_github_cursor"),
    Index("idx_github_cursor_repo_type", "repository_name", "source_type")
  )

  repository_name: Mapped[str] = mapped_column(String(200), nullable=False)

  source_type: Mapped[SourceType] = mapped_column(SqlEnum(SourceType, native_enum=False), nullable=False)

  cursor_value: Mapped[str] = mapped_column(String(500), nullable=False)
