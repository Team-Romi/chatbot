from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  """
  .env 에서 환경변수 로딩
  """

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
    extra="ignore"
  )

  # GitHub API 설정
  github_api_base_url: str
  github_api_token: str | None = None

  # Ollama 설정
  ollama_base_url: str
  ollama_api_key: str
  ollama_model: str
  ollama_timeout_seconds: int

  # Qdrant 설정
  qdrant_base_url: str
  qdrant_collection: str
  qdrant_api_key: str

  # 텍스트 청크 설정
  text_chunk_max_chars: int
  text_chunk_overlap_chars: int
  text_chunk_hard_max_chars: int

  # 동시성 설정
  concurrency_embedding_max_concurrency: int

  # PostgreSQL 설정
  postgres_url: str


@lru_cache(maxsize=1)
def get_settings() -> Settings:
  return Settings()
