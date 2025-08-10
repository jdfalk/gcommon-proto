// file: pkg/db/migration/executor_sql.go
// version: 1.0.0
// guid: a7b8c9d0-e1f2-4a3b-b4c5-d6e7f8a9b0c1

package migration

import (
	"context"
	"database/sql"
	"fmt"
)

// SQLExecutor executes SQL statements using a sql.DB connection.
type SQLExecutor struct {
	DB *sql.DB
}

// Execute runs the migration's Up statements in order.
func (e SQLExecutor) Execute(ctx context.Context, m Migration) error {
	tx, err := e.DB.BeginTx(ctx, nil)
	if err != nil {
		return fmt.Errorf("begin tx: %w", err)
	}
	for i, stmt := range m.Up {
		if _, err := tx.ExecContext(ctx, stmt); err != nil {
			tx.Rollback()
			return fmt.Errorf("exec up %d: %w", i, err)
		}
	}
	if err := tx.Commit(); err != nil {
		return fmt.Errorf("commit: %w", err)
	}
	return nil
}

// Rollback executes the Down statements in reverse order.
func (e SQLExecutor) Rollback(ctx context.Context, m Migration) error {
	tx, err := e.DB.BeginTx(ctx, nil)
	if err != nil {
		return fmt.Errorf("begin tx: %w", err)
	}
	for i := len(m.Down) - 1; i >= 0; i-- {
		if _, err := tx.ExecContext(ctx, m.Down[i]); err != nil {
			tx.Rollback()
			return fmt.Errorf("exec down %d: %w", i, err)
		}
	}
	if err := tx.Commit(); err != nil {
		return fmt.Errorf("commit: %w", err)
	}
	return nil
}

// List is not supported for SQLExecutor directly; use Source instead.
func (e SQLExecutor) List(ctx context.Context) ([]Migration, error) {
	_ = ctx
	return nil, fmt.Errorf("list unsupported; use migration source")
}
