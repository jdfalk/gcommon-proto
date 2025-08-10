// file: pkg/db/migration/executor_postgres.go
// version: 1.0.0
// guid: b1c2d3e4-f5a6-47b8-90c1-d2e3f4a5b6c7

package migration

import (
	"context"
	"database/sql"
	"fmt"
)

// PostgresExecutor runs migrations against PostgreSQL.
type PostgresExecutor struct {
	SQLExecutor
}

// NewPostgresExecutor creates an executor for Postgres.
func NewPostgresExecutor(db *sql.DB) PostgresExecutor {
	return PostgresExecutor{SQLExecutor{DB: db}}
}

// Execute wraps SQLExecutor.Execute with Postgres specific checks.
func (e PostgresExecutor) Execute(ctx context.Context, m Migration) error {
	if m.DB != Postgres {
		return fmt.Errorf("migration %s not for Postgres", m)
	}
	return e.SQLExecutor.Execute(ctx, m)
}

// Rollback wraps SQLExecutor.Rollback with Postgres specific checks.
func (e PostgresExecutor) Rollback(ctx context.Context, m Migration) error {
	if m.DB != Postgres {
		return fmt.Errorf("migration %s not for Postgres", m)
	}
	return e.SQLExecutor.Rollback(ctx, m)
}
