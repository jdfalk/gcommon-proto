// file: pkg/db/migration/manager.go
// version: 1.0.0
// guid: 5cbe9eaa-9ad5-4e74-9e0d-5fd26e9dd98a

package migration

import (
	"context"
	"fmt"
	"sync"
)

// Manager coordinates database migrations, validation, and version tracking.
type Manager struct {
	Exec      Executor
	Validator Validator
	Tracker   VersionTracker
	Sources   []Source
	Parallel  bool
}

// NewManager creates a new Manager.
func NewManager(exec Executor, validator Validator, tracker VersionTracker) *Manager {
	return &Manager{Exec: exec, Validator: validator, Tracker: tracker}
}

// AddSource registers a migration source.
func (m *Manager) AddSource(src Source) {
	m.Sources = append(m.Sources, src)
}

// Migrate loads migrations from all sources and applies any that have not yet been run.
func (m *Manager) Migrate(ctx context.Context) error {
	if err := m.ensureTracker(ctx); err != nil {
		return err
	}
	migrations, err := m.loadMigrations(ctx)
	if err != nil {
		return err
	}
	current, err := m.Tracker.Current(ctx)
	if err != nil {
		return fmt.Errorf("current version: %w", err)
	}
	var pending []Migration
	for _, mg := range migrations {
		if mg.Version > current {
			pending = append(pending, mg)
		}
	}
	SortMigrations(pending)
	if m.Parallel {
		return m.migrateParallel(ctx, pending)
	}
	for _, mg := range pending {
		if err := m.applyOne(ctx, mg); err != nil {
			return err
		}
	}
	return nil
}

// Rollback reverses the last n migrations (n defaults to 1 if <=0).
func (m *Manager) Rollback(ctx context.Context, n int) error {
	if n <= 0 {
		n = 1
	}
	rb := SimpleRollback{Exec: m.Exec, Tracker: m.Tracker}
	for i := 0; i < n; i++ {
		if err := rb.Rollback(ctx); err != nil {
			return err
		}
	}
	return nil
}

// loadMigrations aggregates migrations from all sources.
func (m *Manager) loadMigrations(ctx context.Context) ([]Migration, error) {
	var all []Migration
	for _, src := range m.Sources {
		migs, err := src.Load(ctx)
		if err != nil {
			return nil, err
		}
		all = append(all, migs...)
	}
	SortMigrations(all)
	return all, nil
}

// ensureTracker ensures version tracking table exists when supported.
func (m *Manager) ensureTracker(ctx context.Context) error {
	if t, ok := m.Tracker.(interface{ EnsureTable(context.Context) error }); ok {
		return t.EnsureTable(ctx)
	}
	return nil
}

// applyOne validates and executes a single migration.
func (m *Manager) applyOne(ctx context.Context, mg Migration) error {
	if err := m.Validator.Validate(mg); err != nil {
		return fmt.Errorf("validate %s: %w", mg, err)
	}
	if err := m.Exec.Execute(ctx, mg); err != nil {
		return fmt.Errorf("execute %s: %w", mg, err)
	}
	if err := m.Tracker.SetVersion(ctx, mg.Version, mg.Name); err != nil {
		return fmt.Errorf("set version %s: %w", mg, err)
	}
	return nil
}

// migrateParallel runs pending migrations concurrently.
func (m *Manager) migrateParallel(ctx context.Context, migs []Migration) error {
	errCh := make(chan error, len(migs))
	var wg sync.WaitGroup
	for _, mg := range migs {
		mg := mg
		wg.Add(1)
		go func() {
			defer wg.Done()
			if err := m.applyOne(ctx, mg); err != nil {
				errCh <- err
			}
		}()
	}
	wg.Wait()
	close(errCh)
	for err := range errCh {
		if err != nil {
			return err
		}
	}
	return nil
}
