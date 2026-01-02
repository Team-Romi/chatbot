from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# 템플릿 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

router = APIRouter()

# 목업 데이터
MOCK_REPOS = [
  {
    "owner": "Team-Romi",
    "name": "romi-chatbot",
    "issue_count": 150,
    "last_synced": "5분 전",
    "status": "synced"
  },
  {
    "owner": "Team-Romi",
    "name": "frontend",
    "issue_count": 45,
    "last_synced": "1시간 전",
    "status": "synced"
  },
]

MOCK_CHAT_MESSAGES = [
  {"role": "bot", "content": "안녕하세요! 이 레포지토리에 대해 무엇이든 물어보세요."},
  {"role": "user", "content": "로그인 기능 누가 만들었어?"},
  {"role": "bot", "content": "로그인 기능은 @developer1님이 #123 이슈에서 개발했습니다.\n\n📎 관련 이슈: #123 - 로그인 기능 구현"},
]


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
  """메인 페이지 - 레포지토리 목록"""
  return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"repos": MOCK_REPOS}
  )


@router.get("/{owner}/{repo}", response_class=HTMLResponse)
async def chat(request: Request, owner: str, repo: str):
  """챗봇 페이지"""
  repo_info = next(
    (r for r in MOCK_REPOS if r["owner"] == owner and r["name"] == repo),
    {"owner": owner, "name": repo, "issue_count": 0, "last_synced": "없음", "status": "unknown"}
  )
  return templates.TemplateResponse(
    request=request,
    name="chat.html",
    context={
      "owner": owner,
      "repo": repo,
      "repo_info": repo_info,
      "messages": MOCK_CHAT_MESSAGES
    }
  )


@router.get("/{owner}/{repo}/settings", response_class=HTMLResponse)
async def repo_settings(request: Request, owner: str, repo: str):
  """레포 설정 페이지"""
  repo_info = next(
    (r for r in MOCK_REPOS if r["owner"] == owner and r["name"] == repo),
    {"owner": owner, "name": repo, "issue_count": 0, "last_synced": "없음", "status": "unknown"}
  )
  return templates.TemplateResponse(
    request=request,
    name="repo_settings.html",
    context={
      "owner": owner,
      "repo": repo,
      "repo_info": repo_info
    }
  )
