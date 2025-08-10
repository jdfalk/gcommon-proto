// file: pkg/db/migration/versioning.go
// version: 1.0.0
// guid: 1d9c1d6f-e76b-48f1-9a34-b1587da83211

package migration

import (
	"context"
	"database/sql"
	"fmt"
)

// VersionTracker tracks applied migration versions and metadata.
type VersionTracker interface {
	Current(context.Context) (int, error)
	SetVersion(context.Context, int, string) error
	Last(context.Context) (Migration, error)
	RemoveVersion(context.Context, int) error
}

// SQLVersionTracker implements VersionTracker using a database table.
type SQLVersionTracker struct {
	DB    *sql.DB
	Table string
}

// EnsureTable creates the version tracking table if it does not exist.
func (t SQLVersionTracker) EnsureTable(ctx context.Context) error {
	query := fmt.Sprintf(`CREATE TABLE IF NOT EXISTS %s (
        id SERIAL PRIMARY KEY,
        version INTEGER NOT NULL,
        name TEXT NOT NULL,
        applied_at TIMESTAMP DEFAULT NOW()
    )`, t.Table)
	if _, err := t.DB.ExecContext(ctx, query); err != nil {
		return fmt.Errorf("create version table: %w", err)
	}
	return nil
}

// Current returns the latest applied migration version.
func (t SQLVersionTracker) Current(ctx context.Context) (int, error) {
	var v int
	query := fmt.Sprintf("SELECT COALESCE(MAX(version),0) FROM %s", t.Table)
	if err := t.DB.QueryRowContext(ctx, query).Scan(&v); err != nil {
		return 0, fmt.Errorf("query current version: %w", err)
	}
	return v, nil
}

// SetVersion records a migration as applied.
func (t SQLVersionTracker) SetVersion(ctx context.Context, v int, name string) error {
	query := fmt.Sprintf("INSERT INTO %s (version, name) VALUES ($1, $2)", t.Table)
	if _, err := t.DB.ExecContext(ctx, query, v, name); err != nil {
		return fmt.Errorf("insert version: %w", err)
	}
	return nil
}

// RemoveVersion deletes a version record.
func (t SQLVersionTracker) RemoveVersion(ctx context.Context, v int) error {
	query := fmt.Sprintf("DELETE FROM %s WHERE version=$1", t.Table)
	if _, err := t.DB.ExecContext(ctx, query, v); err != nil {
		return fmt.Errorf("delete version: %w", err)
	}
	return nil
}

// Last returns the last applied migration.
func (t SQLVersionTracker) Last(ctx context.Context) (Migration, error) {
	query := fmt.Sprintf("SELECT version, name FROM %s ORDER BY version DESC LIMIT 1", t.Table)
	var m Migration
	if err := t.DB.QueryRowContext(ctx, query).Scan(&m.Version, &m.Name); err != nil {
		if err == sql.ErrNoRows {
			return Migration{}, nil
		}
		return Migration{}, fmt.Errorf("query last: %w", err)
	}
	return m, nil
}
