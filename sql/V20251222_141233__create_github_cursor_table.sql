CREATE TABLE IF NOT EXISTS github_cursor (
    id UUID PRIMARY KEY,
    repository_name VARCHAR(200) NOT NULL,
    source_type VARCHAR(50) NOT NULL,
    cursor_value VARCHAR(500) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_github_cursor UNIQUE (repository_name, source_type),

    CONSTRAINT ck_github_cursor_source_type
        CHECK (source_type IN ('REPOSITORY', 'ISSUE', 'PULL_REQUEST', 'COMMIT', 'RELEASE'))
);

-- 인덱스 생성
CREATE INDEX IF NOT EXISTS idx_github_cursor_repo_type
    ON github_cursor (repository_name, source_type);