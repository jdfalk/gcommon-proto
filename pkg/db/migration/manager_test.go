package migration

import (
	"context"
	"fmt"
	"os"
	"path/filepath"
	"testing"
)

// dummyExecutor records executed migrations.
type dummyExecutor struct {
	applied  []Migration
	rolled   []Migration
	failExec bool
	failRoll bool
}

func (d *dummyExecutor) Execute(_ context.Context, m Migration) error {
	if d.failExec {
		return fmt.Errorf("exec fail")
	}
	d.applied = append(d.applied, m)
	return nil
}

func (d *dummyExecutor) Rollback(_ context.Context, m Migration) error {
	if d.failRoll {
		return fmt.Errorf("rollback fail")
	}
	d.rolled = append(d.rolled, m)
	return nil
}

func (d *dummyExecutor) List(_ context.Context) ([]Migration, error) { return d.applied, nil }

// dummyTracker tracks versions in memory.
type dummyTracker struct {
	versions []Migration
}

func (t *dummyTracker) Current(context.Context) (int, error) {
	if len(t.versions) == 0 {
		return 0, nil
	}
	return t.versions[len(t.versions)-1].Version, nil
}

func (t *dummyTracker) SetVersion(_ context.Context, v int, name string) error {
	t.versions = append(t.versions, Migration{Version: v, Name: name})
	return nil
}

func (t *dummyTracker) Last(context.Context) (Migration, error) {
	if len(t.versions) == 0 {
		return Migration{}, nil
	}
	return t.versions[len(t.versions)-1], nil
}

func (t *dummyTracker) RemoveVersion(_ context.Context, v int) error {
	for i, m := range t.versions {
		if m.Version == v {
			t.versions = append(t.versions[:i], t.versions[i+1:]...)
			return nil
		}
	}
	return nil
}

// TestManager_MigrateApplyPending verifies migrations are executed and tracked.
func TestManager_MigrateApplyPending(t *testing.T) {
	dir := t.TempDir()
	up1 := filepath.Join(dir, "001_init.up.sql")
	down1 := filepath.Join(dir, "001_init.down.sql")
	os.WriteFile(up1, []byte("CREATE TABLE t1();"), 0644)
	os.WriteFile(down1, []byte("DROP TABLE t1;"), 0644)

	up2 := filepath.Join(dir, "002_add.up.sql")
	down2 := filepath.Join(dir, "002_add.down.sql")
	os.WriteFile(up2, []byte("ALTER TABLE t1 ADD COLUMN c1 INT;"), 0644)
	os.WriteFile(down2, []byte("ALTER TABLE t1 DROP COLUMN c1;"), 0644)

	src := FileSource{Dir: dir, DB: Postgres}
	exec := &dummyExecutor{}
	tracker := &dummyTracker{}
	mgr := NewManager(exec, BasicValidator{}, tracker)
	mgr.AddSource(src)
	if err := mgr.Migrate(context.Background()); err != nil {
		t.Fatalf("migrate: %v", err)
	}
	if len(exec.applied) != 2 {
		t.Fatalf("expected 2 applied, got %d", len(exec.applied))
	}
	if v, _ := tracker.Current(context.Background()); v != 2 {
		t.Fatalf("expected version 2, got %d", v)
	}
}

// TestManager_Rollback reverses last migration.
func TestManager_Rollback(t *testing.T) {
	exec := &dummyExecutor{}
	tracker := &dummyTracker{versions: []Migration{{Version: 1, Name: "init"}}}
	mgr := NewManager(exec, BasicValidator{}, tracker)
	mgr.Exec = exec
	mgr.Tracker = tracker
	if err := mgr.Rollback(context.Background(), 1); err != nil {
		t.Fatalf("rollback: %v", err)
	}
	if len(exec.rolled) != 1 {
		t.Fatalf("expected 1 rolled, got %d", len(exec.rolled))
	}
	if v, _ := tracker.Current(context.Background()); v != 0 {
		t.Fatalf("expected version 0, got %d", v)
	}
}
