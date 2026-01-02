"""
로깅 유틸리티 모듈

애플리케이션 전역에서 사용할 로거를 설정합니다.
"""
import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logger(
  name: str = "chatbot",
  log_level: str = "INFO",
  log_file: Optional[str] = None,
  format_string: Optional[str] = None,
) -> logging.Logger:
  """
  로거를 설정하고 반환합니다.

  Args:
      name: 로거 이름 (기본값: "chatbot")
      log_level: 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
      log_file: 로그 파일 경로 (None이면 파일 로깅 안 함)
      format_string: 커스텀 포맷 문자열 (None이면 기본 포맷 사용)

  Returns:
      설정된 Logger 인스턴스
  """
  logger = logging.getLogger(name)

  # 이미 핸들러가 설정되어 있으면 기존 로거 반환
  if logger.handlers:
    return logger

  # 로그 레벨 설정
  level = getattr(logging, log_level.upper(), logging.INFO)
  logger.setLevel(level)

  # 기본 포맷 설정
  if format_string is None:
    format_string = (
      "%(asctime)s - %(name)s - %(levelname)s - "
      "%(filename)s:%(lineno)d - %(message)s"
    )

  formatter = logging.Formatter(format_string, datefmt="%Y-%m-%d %H:%M:%S")

  # 콘솔 핸들러 설정
  console_handler = logging.StreamHandler(sys.stdout)
  console_handler.setLevel(level)
  console_handler.setFormatter(formatter)
  logger.addHandler(console_handler)

  # 파일 핸들러 설정 (선택적)
  if log_file:
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

  return logger


# 기본 로거 인스턴스 생성
logger = setup_logger()
