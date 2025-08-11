package grpc

import (
	"context"
	"fmt"
	"net"
	"testing"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/test/bufconn"

	"github.com/jdfalk/gcommon/pkg/db/migration"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

const bufSize = 1024 * 1024

// dummy implementations copied from migration tests

type dummyExecutor struct {
	applied []migration.Migration
	fail    bool
}

func (d *dummyExecutor) Execute(_ context.Context, m migration.Migration) error {
	if d.fail {
		return fmt.Errorf("exec fail")
	}
	d.applied = append(d.applied, m)
	return nil
}

func (d *dummyExecutor) Rollback(_ context.Context, m migration.Migration) error {
	if len(d.applied) > 0 {
		d.applied = d.applied[:len(d.applied)-1]
	}
	return nil
}

func (d *dummyExecutor) List(_ context.Context) ([]migration.Migration, error) { return d.applied, nil }

type dummyTracker struct {
	versions []migration.Migration
}

// SourceFunc helps create inline migration sources for tests.
type SourceFunc func(context.Context) ([]migration.Migration, error)

// Load implements the Source interface.
func (f SourceFunc) Load(ctx context.Context) ([]migration.Migration, error) { return f(ctx) }

func (t *dummyTracker) Current(context.Context) (int, error) {
	if len(t.versions) == 0 {
		return 0, nil
	}
	return t.versions[len(t.versions)-1].Version, nil
}

func (t *dummyTracker) SetVersion(_ context.Context, v int, name string) error {
	t.versions = append(t.versions, migration.Migration{Version: v, Name: name})
	return nil
}

func (t *dummyTracker) Last(context.Context) (migration.Migration, error) {
	if len(t.versions) == 0 {
		return migration.Migration{}, nil
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

// helper to create server and client
type testEnv struct {
	conn   *grpc.ClientConn
	server *grpc.Server
	exec   *dummyExecutor
	track  *dummyTracker
	mgr    *migration.Manager
}

func newTestEnv(t *testing.T) *testEnv {
	t.Helper()
	lis := bufconn.Listen(bufSize)
	s := grpc.NewServer()
	exec := &dummyExecutor{}
	track := &dummyTracker{}
	mgr := migration.NewManager(exec, migration.BasicValidator{}, track)
	ms := NewMigrationServer(mgr)
	ms.Register(s)
	go func() {
		_ = s.Serve(lis)
	}()
	ctx := context.Background()
	conn, err := grpc.DialContext(ctx, "bufnet", grpc.WithContextDialer(func(context.Context, string) (net.Conn, error) { return lis.Dial() }), grpc.WithInsecure())
	if err != nil {
		t.Fatalf("dial: %v", err)
	}
	return &testEnv{conn: conn, server: s, exec: exec, track: track, mgr: mgr}
}

func (e *testEnv) close() {
	e.conn.Close()
	e.server.Stop()
}

func (e *testEnv) execFail() { e.exec.fail = true }

func TestMigrationServer_ApplyAndStatus(t *testing.T) {
	env := newTestEnv(t)
	defer env.close()
	client := dbpb.NewMigrationServiceClient(env.conn)
	// Add file source with two migrations
	env.mgr.AddSource(migration.SourceFunc(func(context.Context) ([]migration.Migration, error) {
		return []migration.Migration{{Version: 1, Name: "init", Up: []string{"CREATE TABLE t1"}, Down: []string{"DROP TABLE t1"}}, {Version: 2, Name: "add", Up: []string{"ALTER"}, Down: []string{"ALTER"}}}, nil
	}))
	if _, err := client.ApplyMigration(context.Background(), &dbpb.RunMigrationRequest{}); err != nil {
		t.Fatalf("apply: %v", err)
	}
	statusResp, err := client.GetMigrationStatus(context.Background(), &dbpb.GetMigrationStatusRequest{})
	if err != nil {
		t.Fatalf("status: %v", err)
	}
	if statusResp.CurrentVersion != "2" || len(statusResp.AppliedVersions) != 2 {
		t.Fatalf("unexpected status %+v", statusResp)
	}
}

func TestMigrationServer_Revert(t *testing.T) {
	env := newTestEnv(t)
	defer env.close()
	client := dbpb.NewMigrationServiceClient(env.conn)
	env.mgr.AddSource(migration.SourceFunc(func(context.Context) ([]migration.Migration, error) {
		return []migration.Migration{{Version: 1, Name: "init", Up: []string{"CREATE"}, Down: []string{"DROP"}}}, nil
	}))
	if _, err := client.ApplyMigration(context.Background(), &dbpb.RunMigrationRequest{}); err != nil {
		t.Fatalf("apply: %v", err)
	}
	resp, err := client.RevertMigration(context.Background(), &dbpb.RevertMigrationRequest{TargetVersion: "0"})
	if err != nil {
		t.Fatalf("revert: %v", err)
	}
	if !resp.Success {
		t.Fatalf("expected success")
	}
	cur, _ := env.track.Current(context.Background())
	if cur != 0 {
		t.Fatalf("expected version 0, got %d", cur)
	}
}

func TestMigrationServer_InvalidTarget(t *testing.T) {
	env := newTestEnv(t)
	defer env.close()
	client := dbpb.NewMigrationServiceClient(env.conn)
	_, err := client.RevertMigration(context.Background(), &dbpb.RevertMigrationRequest{TargetVersion: "a"})
	if status.Code(err) != codes.InvalidArgument {
		t.Fatalf("expected invalid argument, got %v", err)
	}
}

// Additional tests for coverage and line count

func TestMigrationServer_ListMigrations(t *testing.T) {
	env := newTestEnv(t)
	defer env.close()
	client := dbpb.NewMigrationServiceClient(env.conn)
	env.mgr.AddSource(SourceFunc(func(context.Context) ([]migration.Migration, error) {
		return []migration.Migration{
			{Version: 1, Name: "init", Up: []string{"CREATE"}, Down: []string{"DROP"}},
			{Version: 2, Name: "add", Up: []string{"ALTER"}, Down: []string{"ALTER"}},
		}, nil
	}))
	if _, err := client.ApplyMigration(context.Background(), &dbpb.RunMigrationRequest{}); err != nil {
		t.Fatalf("apply: %v", err)
	}
	resp, err := client.ListMigrations(context.Background(), &dbpb.ListMigrationsRequest{StatusFilter: "applied"})
	if err != nil {
		t.Fatalf("list: %v", err)
	}
	if len(resp.Migrations) != 2 {
		t.Fatalf("expected 2 migrations, got %d", len(resp.Migrations))
	}
	resp, err = client.ListMigrations(context.Background(), &dbpb.ListMigrationsRequest{StatusFilter: "pending"})
	if err != nil {
		t.Fatalf("list pending: %v", err)
	}
	if len(resp.Migrations) != 0 {
		t.Fatalf("expected 0 pending, got %d", len(resp.Migrations))
	}
}

func TestMigrationServer_ApplyMigrationError(t *testing.T) {
	env := newTestEnv(t)
	defer env.close()
	env.execFail()
	client := dbpb.NewMigrationServiceClient(env.conn)
	env.mgr.AddSource(SourceFunc(func(context.Context) ([]migration.Migration, error) {
		return []migration.Migration{{Version: 1, Name: "bad", Up: []string{"CREATE"}, Down: []string{"DROP"}}}, nil
	}))
	resp, err := client.ApplyMigration(context.Background(), &dbpb.RunMigrationRequest{})
	if err != nil {
		t.Fatalf("apply: %v", err)
	}
	if resp.Success {
		t.Fatalf("expected failure")
	}
}
