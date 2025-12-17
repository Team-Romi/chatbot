from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
async def health_check() -> Dict[str, str]:
  return { "status": "ok" }
