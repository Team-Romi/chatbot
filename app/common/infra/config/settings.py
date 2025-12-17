from anyio.functools import lru_cache
from pydantic.v1 import BaseSettings, Field


class Settings(BaseSettings):
  """
  .env 에서 환경변수 로딩
  """

  github_api_base_url: str = Field(alias="GITHUB_API_BASE_URL")

  ollama_base_url: str = Field(alias="OLLAMA_BASE_URL")
  ollama_api_key: str = Field(alias="OLLAMA_API_KEY")
  ollama_model: str = Field(alias="OLLAMA_MODEL")
  ollama_timeout_seconds: int = Field(alias="OLLAMA_TIMEOUT_SECONDS")

  qdrant_base_url: str = Field(alias="QDRANT_BASE_URL")
  qdrant_collection: str = Field(alias="QDRANT_COLLECTION")
  qdrant_api_key: str = Field(alias="QDRANT_API_KEY")

  text_chunk_max_chars: int = Field(alias="TEXT_CHUNK_MAX_CHARS")
  text_chunk_overlap_chars: int = Field(alias="TEXT_CHUNK_OVERLAP_CHARS")
  text_chunk_hard_max_chars: int = Field(alias="TEXT_CHUNK_HARD_MAX_CHARS")

  concurrency_embedding_max_concurrency: int = Field(alias="CONCURRENCY_EMBEDDING_MAX_CONCURRENCY")

  postgres_url: str = Field(alias="POSTGRES_URL")

@lru_cache(maxsize=1)
def get_settings() -> Settings:
  return Settings