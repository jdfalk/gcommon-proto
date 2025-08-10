// file: pkg/db/migration/executor_sqlite.go
// version: 1.0.0
// guid: c2d3e4f5-a6b7-48c9-0d1e-2f3a4b5c6d7e

package migration

import (
	"context"
	"database/sql"
	"fmt"
)

// SQLiteExecutor runs migrations against SQLite databases.
type SQLiteExecutor struct {
	SQLExecutor
}

// NewSQLiteExecutor creates an executor for SQLite.
func NewSQLiteExecutor(db *sql.DB) SQLiteExecutor {
	return SQLiteExecutor{SQLExecutor{DB: db}}
}

// Execute ensures the migration is for SQLite before running.
func (e SQLiteExecutor) Execute(ctx context.Context, m Migration) error {
	if m.DB != SQLite {
		return fmt.Errorf("migration %s not for SQLite", m)
	}
	return e.SQLExecutor.Execute(ctx, m)
}

// Rollback ensures the migration is for SQLite before running.
func (e SQLiteExecutor) Rollback(ctx context.Context, m Migration) error {
	if m.DB != SQLite {
		return fmt.Errorf("migration %s not for SQLite", m)
	}
	return e.SQLExecutor.Rollback(ctx, m)
}
