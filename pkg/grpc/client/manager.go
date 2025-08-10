// file: pkg/grpc/client/manager.go
// version: 1.0.0
// guid: babb42de-3c57-4ab6-bb3c-0f2f4de27d91

package client

import (
	"context"
	"sync"

	"google.golang.org/grpc"
)

// Manager handles gRPC client connections with pooling and reuse.
type Manager struct {
	mu    sync.Mutex
	conns map[string]*grpc.ClientConn
}

// NewManager creates a new Manager instance.
func NewManager() *Manager {
	return &Manager{conns: make(map[string]*grpc.ClientConn)}
}

// Get returns a cached connection or dials a new one.
func (m *Manager) Get(ctx context.Context, addr string, opts ...grpc.DialOption) (*grpc.ClientConn, error) {
	m.mu.Lock()
	if conn, ok := m.conns[addr]; ok {
		m.mu.Unlock()
		return conn, nil
	}
	m.mu.Unlock()
	conn, err := grpc.DialContext(ctx, addr, opts...)
	if err != nil {
		return nil, err
	}
	m.mu.Lock()
	m.conns[addr] = conn
	m.mu.Unlock()
	return conn, nil
}

// Close closes all managed connections.
func (m *Manager) Close() error {
	m.mu.Lock()
	defer m.mu.Unlock()
	var firstErr error
	for addr, c := range m.conns {
		if err := c.Close(); err != nil && firstErr == nil {
			firstErr = err
		}
		delete(m.conns, addr)
	}
	return firstErr
}
