// file: cmd/examples/database/migration/main.go
// version: 0.1.0
// guid: 12345678-1234-5678-9abc-def012345678

// This example demonstrates how to start a migration gRPC server.
// TODO: expand example to include real database connections and CLI flags.
package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"

	"github.com/jdfalk/gcommon/pkg/db/migration"
	mggrpc "github.com/jdfalk/gcommon/pkg/db/migration/grpc"
)

func main() {
	lis, err := net.Listen("tcp", ":50052")
	if err != nil {
		log.Fatalf("listen: %v", err)
	}
	s := grpc.NewServer()
	exec := noopExecutor{}
	tracker := &memoryTracker{}
	mgr := migration.NewManager(exec, migration.BasicValidator{}, tracker)
	srv := mgrpc.NewMigrationServer(mgr)
	srv.Register(s)
	go func() {
		if err := s.Serve(lis); err != nil {
			log.Fatalf("serve: %v", err)
		}
	}()
	// Block forever
	<-context.Background().Done()
}

// noopExecutor is a stub executor for example purposes.
type noopExecutor struct{}

func (noopExecutor) Execute(context.Context, migration.Migration) error  { return nil }
func (noopExecutor) Rollback(context.Context, migration.Migration) error { return nil }
func (noopExecutor) List(context.Context) ([]migration.Migration, error) { return nil, nil }

// memoryTracker is a stub version tracker.
type memoryTracker struct{ current int }

func (m *memoryTracker) Current(context.Context) (int, error)          { return m.current, nil }
func (m *memoryTracker) SetVersion(context.Context, int, string) error { return nil }
func (m *memoryTracker) Last(context.Context) (migration.Migration, error) {
	return migration.Migration{Version: m.current}, nil
}
func (m *memoryTracker) RemoveVersion(context.Context, int) error { return nil }
