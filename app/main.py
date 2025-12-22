from contextlib import asynccontextmanager
from typing import Dict

from fastapi import FastAPI

from app.config.database import get_async_engine
from app.db.init_db import create_tables_if_not_exists
from app.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
  logger.info("ChatBot 애플리케이션 시작")
  await create_tables_if_not_exists(get_async_engine())
  yield
  logger.info("애플리케이션 종료")


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health_check() -> Dict[str, str]:
  return { "status": "ok" }
