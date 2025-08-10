// file: pkg/notification/channels/manager.go
// version: 1.0.0
// guid: dddddddd-eeee-ffff-0000-111111111111

package channels

import "sync"

// Manager handles channel enablement.
type Manager struct {
	mu      sync.RWMutex
	enabled map[string]bool
}

// NewManager creates a Manager.
func NewManager() *Manager {
	return &Manager{enabled: make(map[string]bool)}
}

// Enable marks a channel as enabled.
func (m *Manager) Enable(ch string) {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.enabled[ch] = true
}

// Disable marks a channel as disabled.
func (m *Manager) Disable(ch string) {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.enabled[ch] = false
}

// IsEnabled checks if a channel is enabled.
func (m *Manager) IsEnabled(ch string) bool {
	m.mu.RLock()
	defer m.mu.RUnlock()
	return m.enabled[ch]
}
