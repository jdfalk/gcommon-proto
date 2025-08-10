// file: pkg/grpc/server/manager_test.go
// version: 1.0.0
// guid: 732664f0-f0b9-42e5-8675-9e311ec28fe1

package server

import (
	"context"
	"testing"

	health "github.com/jdfalk/gcommon/pkg/health"
	"google.golang.org/grpc"
)

// mockServer implements GRPCServer for testing purposes.
type mockServer struct {
	started int
	stopped int
}

func (m *mockServer) Start(context.Context) error {
	m.started++
	return nil
}

func (m *mockServer) Stop(context.Context) error {
	m.stopped++
	return nil
}

func (m *mockServer) RegisterService(*grpc.ServiceDesc, interface{}) {}
func (m *mockServer) RegisterHealthService(provider health.Provider) {}
func (m *mockServer) RegisterReflectionService()                     {}
func (m *mockServer) GetRegisteredServices() []string                { return nil }
func (m *mockServer) GetAddress() string                             { return "" }
func (m *mockServer) GetStats() *ServerStats                         { return &ServerStats{} }

// TestManagerStartStop verifies Manager starts and stops all servers.
func TestManagerStartStop(t *testing.T) {
	ctx := context.Background()
	m := NewManager()
	s1 := &mockServer{}
	s2 := &mockServer{}
	m.AddServer(s1)
	m.AddServer(s2)

	if err := m.StartAll(ctx); err != nil {
		t.Fatalf("StartAll failed: %v", err)
	}
	if s1.started != 1 || s2.started != 1 {
		t.Fatalf("servers not started: %d %d", s1.started, s2.started)
	}

	if err := m.StopAll(ctx); err != nil {
		t.Fatalf("StopAll failed: %v", err)
	}
	if s1.stopped != 1 || s2.stopped != 1 {
		t.Fatalf("servers not stopped: %d %d", s1.stopped, s2.stopped)
	}
}

// TestManagerEmpty ensures starting an empty manager does nothing.
func TestManagerEmpty(t *testing.T) {
	ctx := context.Background()
	m := NewManager()
	if err := m.StartAll(ctx); err != nil {
		t.Fatalf("StartAll empty failed: %v", err)
	}
	if err := m.StopAll(ctx); err != nil {
		t.Fatalf("StopAll empty failed: %v", err)
	}
}
