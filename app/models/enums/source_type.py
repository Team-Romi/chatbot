from enum import Enum


class SourceType(str, Enum):
  """
  깃허브 임베딩 대상 SourceType
  - Repository: 레포 파일/문서 (README 등)
  - ISSUE: 이슈
  - PULL_REQUEST: PR
  - COMMIT: 커밋
  - RELEASE: 릴리즈
  """
  REPOSITORY = "REPOSITORY"
  ISSUE = "ISSUE"
  PULL_REQUEST = "PULL_REQUEST"
  COMMIT = "COMMIT"
  RELEASE = "RELEASE"
