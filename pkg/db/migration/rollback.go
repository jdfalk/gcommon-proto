// file: pkg/db/migration/rollback.go
// version: 1.0.0
// guid: a3b4c5d6-e7f8-40a9-b0c1-d2e3f4a5b6c7

package migration

import (
	"context"
	"fmt"
)

// SimpleRollback provides rollback utilities.
type SimpleRollback struct {
	Exec    Executor
	Tracker VersionTracker
}

// Rollback reverses the most recent migration.
func (r *SimpleRollback) Rollback(ctx context.Context) error {
	last, err := r.Tracker.Last(ctx)
	if err != nil {
		return fmt.Errorf("get last: %w", err)
	}
	if last.Version == 0 {
		return nil
	}
	if err := r.Exec.Rollback(ctx, last); err != nil {
		return fmt.Errorf("rollback: %w", err)
	}
	if err := r.Tracker.RemoveVersion(ctx, last.Version); err != nil {
		return fmt.Errorf("remove version: %w", err)
	}
	return nil
}
