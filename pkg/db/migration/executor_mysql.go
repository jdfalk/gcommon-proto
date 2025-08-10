// file: pkg/db/migration/executor_mysql.go
// version: 1.0.0
// guid: e4f5a6b7-c8d9-40e1-f2a3-b4c5d6e7f8a9

package migration

import (
	"context"
	"database/sql"
	"fmt"
)

// MySQLExecutor runs migrations against MySQL databases.
type MySQLExecutor struct {
	SQLExecutor
}

// NewMySQLExecutor creates an executor for MySQL.
func NewMySQLExecutor(db *sql.DB) MySQLExecutor {
	return MySQLExecutor{SQLExecutor{DB: db}}
}

// Execute ensures the migration is for MySQL before running.
func (e MySQLExecutor) Execute(ctx context.Context, m Migration) error {
	if m.DB != MySQL {
		return fmt.Errorf("migration %s not for MySQL", m)
	}
	return e.SQLExecutor.Execute(ctx, m)
}

// Rollback ensures the migration is for MySQL before running.
func (e MySQLExecutor) Rollback(ctx context.Context, m Migration) error {
	if m.DB != MySQL {
		return fmt.Errorf("migration %s not for MySQL", m)
	}
	return e.SQLExecutor.Rollback(ctx, m)
}
