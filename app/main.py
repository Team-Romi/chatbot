from contextlib import asynccontextmanager
from pathlib import Path
from typing import Dict

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config.database import get_async_engine
from app.db.init_db import create_tables_if_not_exists
from app.utils.logger import logger
from app.views import pages


# 프로젝트 루트 경로
BASE_DIR = Path(__file__).resolve().parent.parent


@asynccontextmanager
async def lifespan(app: FastAPI):
  logger.info("ChatBot 애플리케이션 시작")
  await create_tables_if_not_exists(get_async_engine())
  yield
  logger.info("애플리케이션 종료")


app = FastAPI(lifespan=lifespan)

# 정적 파일 서빙
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# 페이지 라우터
app.include_router(pages.router)


@app.get("/health")
async def health_check() -> Dict[str, str]:
  return { "status": "ok" }
