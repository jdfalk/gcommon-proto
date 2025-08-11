package grpc

import (
	"context"
	"net"
	"testing"

	"google.golang.org/grpc"
	"google.golang.org/grpc/test/bufconn"

	"github.com/jdfalk/gcommon/pkg/db/migration"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// setupTestClient prepares a MigrationClient with in-memory server.
func setupTestClient(t *testing.T) (*MigrationClient, *grpc.Server, *migration.Manager) {
	lis := bufconn.Listen(bufSize)
	s := grpc.NewServer()
	exec := &dummyExecutor{}
	track := &dummyTracker{}
	mgr := migration.NewManager(exec, migration.BasicValidator{}, track)
	ms := NewMigrationServer(mgr)
	ms.Register(s)
	go func() { _ = s.Serve(lis) }()
	conn, err := grpc.DialContext(context.Background(), "bufnet", grpc.WithContextDialer(func(context.Context, string) (net.Conn, error) { return lis.Dial() }), grpc.WithInsecure())
	if err != nil {
		t.Fatalf("dial: %v", err)
	}
	client := NewMigrationClient(conn)
	return client, s, mgr
}

func TestMigrationClient_Wrapper(t *testing.T) {
	client, server, mgr := setupTestClient(t)
	defer server.Stop()
	mgr.AddSource(SourceFunc(func(context.Context) ([]migration.Migration, error) {
		return []migration.Migration{{Version: 1, Name: "init", Up: []string{"CREATE"}, Down: []string{"DROP"}}}, nil
	}))
	if _, err := client.ApplyMigration(context.Background(), &dbpb.RunMigrationRequest{}); err != nil {
		t.Fatalf("apply: %v", err)
	}
	if _, err := client.GetMigrationStatus(context.Background(), &dbpb.GetMigrationStatusRequest{}); err != nil {
		t.Fatalf("status: %v", err)
	}
	if _, err := client.ListMigrations(context.Background(), &dbpb.ListMigrationsRequest{}); err != nil {
		t.Fatalf("list: %v", err)
	}
	if _, err := client.RevertMigration(context.Background(), &dbpb.RevertMigrationRequest{TargetVersion: "0"}); err != nil {
		t.Fatalf("revert: %v", err)
	}
}
