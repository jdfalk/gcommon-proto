// file: pkg/db/migration/executor_cockroach.go
// version: 1.0.0
// guid: d3e4f5a6-b7c8-49d0-1e2f-3a4b5c6d7e8f

package migration

import (
	"context"
	"database/sql"
	"fmt"
)

// CockroachExecutor runs migrations against CockroachDB.
type CockroachExecutor struct {
	SQLExecutor
}

// NewCockroachExecutor creates an executor for CockroachDB.
func NewCockroachExecutor(db *sql.DB) CockroachExecutor {
	return CockroachExecutor{SQLExecutor{DB: db}}
}

// Execute ensures the migration is for CockroachDB before running.
func (e CockroachExecutor) Execute(ctx context.Context, m Migration) error {
	if m.DB != Cockroach {
		return fmt.Errorf("migration %s not for CockroachDB", m)
	}
	return e.SQLExecutor.Execute(ctx, m)
}

// Rollback ensures the migration is for CockroachDB before running.
func (e CockroachExecutor) Rollback(ctx context.Context, m Migration) error {
	if m.DB != Cockroach {
		return fmt.Errorf("migration %s not for CockroachDB", m)
	}
	return e.SQLExecutor.Rollback(ctx, m)
}
