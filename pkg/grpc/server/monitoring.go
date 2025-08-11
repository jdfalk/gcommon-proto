// file: pkg/grpc/server/monitoring.go
// version: 1.0.0
// guid: 28adcc0a-8e76-4c30-914d-7c32b1d2d44e

package server

import (
	"sync"
	"time"
)

// Monitor collects rudimentary statistics about server operations.
type Monitor struct {
	mu        sync.Mutex
	requests  int
	errors    int
	startedAt time.Time
}

// NewMonitor creates a new Monitor instance.
func NewMonitor() *Monitor {
	return &Monitor{startedAt: time.Now()}
}

// Record increments request counters and optionally error counters.
func (m *Monitor) Record(err error) {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.requests++
	if err != nil {
		m.errors++
	}
}

// Snapshot returns current statistics.
func (m *Monitor) Snapshot() (req int, errs int, uptime time.Duration) {
	m.mu.Lock()
	defer m.mu.Unlock()
	return m.requests, m.errors, time.Since(m.startedAt)
}
