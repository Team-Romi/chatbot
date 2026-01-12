import uuid
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
  """
  SQLAlchemy Declarative Base
  - 모든 엔티티는 Base 상속
  """
  pass


class TimestampMixin:
  """
  created_at, updated_at 자동 관리 Mixin
  - created_at: DB 레벨 자동 설정
  - updated_at: 애플리케이션 레벨에서 명시적 관리
  """
  created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    server_default=func.now(),  # DB 레벨 - INSERT 시 자동
  )

  updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
    server_default=func.now(),  # DB 레벨 - INSERT 시 자동
  )

class PrimaryKeyMixin:
  """
  UUID Primary Key Mixin
  """
  id: Mapped[uuid.UUID] = mapped_column(
    UUID(as_uuid=True),
    primary_key=True,
    default=uuid.uuid4,
  )
