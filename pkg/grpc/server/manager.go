// file: pkg/grpc/server/manager.go
// version: 1.0.0
// guid: a7152ca2-3531-41f8-ac92-1273baf0ccea

// Package server provides unified server lifecycle management utilities.
package server

import (
	"context"
	"sync"
)

// Manager coordinates the startup and shutdown of one or more gRPC servers.
type Manager struct {
	servers []GRPCServer
	mu      sync.Mutex
}

// NewManager creates a new empty Manager instance.
func NewManager() *Manager {
	return &Manager{}
}

// AddServer registers a GRPCServer with the manager.
func (m *Manager) AddServer(s GRPCServer) {
	if s == nil {
		return
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	m.servers = append(m.servers, s)
}

// StartAll starts all managed servers concurrently and waits for completion.
func (m *Manager) StartAll(ctx context.Context) error {
	m.mu.Lock()
	servers := append([]GRPCServer(nil), m.servers...)
	m.mu.Unlock()

	var wg sync.WaitGroup
	wg.Add(len(servers))
	errs := make(chan error, len(servers))
	for _, srv := range servers {
		go func(s GRPCServer) {
			defer wg.Done()
			if err := s.Start(ctx); err != nil {
				errs <- err
			}
		}(srv)
	}
	wg.Wait()
	close(errs)
	for err := range errs {
		if err != nil {
			return err
		}
	}
	return nil
}

// StopAll stops all managed servers concurrently and waits for completion.
func (m *Manager) StopAll(ctx context.Context) error {
	m.mu.Lock()
	servers := append([]GRPCServer(nil), m.servers...)
	m.mu.Unlock()

	var wg sync.WaitGroup
	wg.Add(len(servers))
	errChan := make(chan error, len(servers))
	for _, srv := range servers {
		go func(s GRPCServer) {
			defer wg.Done()
			if err := s.Stop(ctx); err != nil {
				errChan <- err
			}
		}(srv)
	}
	wg.Wait()
	close(errChan)
	for err := range errChan {
		if err != nil {
			return err
		}
	}
	return nil
}

// Servers returns a snapshot of managed servers.
func (m *Manager) Servers() []GRPCServer {
	m.mu.Lock()
	defer m.mu.Unlock()
	return append([]GRPCServer(nil), m.servers...)
}
