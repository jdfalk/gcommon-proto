// file: pkg/plugins/manager.go
// version: 1.0.0
// guid: c05997e0-04db-4cb3-a610-103e85fe8eae

package plugins

import "context"

// Manager coordinates plugin lifecycle, security, and communication.
type Manager struct {
	registry *Registry
	bus      Bus
	checker  Checker
	policies map[string]Policy
}

// NewManager creates a plugin manager.
func NewManager(r *Registry, bus Bus, checker Checker) *Manager {
	if r == nil {
		r = NewRegistry()
	}
	if bus == nil {
		bus = NewInMemoryBus()
	}
	if checker == nil {
		checker = DefaultChecker{}
	}
	return &Manager{registry: r, bus: bus, checker: checker, policies: make(map[string]Policy)}
}

// Register adds a plugin and its metadata to the underlying registry.
func (m *Manager) Register(p Plugin, md Metadata, policy Policy) error {
	wrapped := WithMetadata(p, md)
	if err := m.registry.Register(wrapped, md); err != nil {
		return err
	}
	m.policies[p.Name()] = policy
	return nil
}

// StartAll initializes and starts all registered plugins with security checks.
func (m *Manager) StartAll(ctx context.Context) error {
	for _, p := range m.registry.List() {
		policy := m.policies[p.Name()]
		if err := m.checker.Validate(p, policy); err != nil {
			return err
		}
		if err := p.Start(ctx); err != nil {
			return err
		}
	}
	return nil
}

// StopAll stops all registered plugins.
func (m *Manager) StopAll(ctx context.Context) error {
	for _, p := range m.registry.List() {
		if err := p.Stop(ctx); err != nil {
			return err
		}
	}
	return nil
}

// Registry returns the internal registry.
func (m *Manager) Registry() *Registry {
	return m.registry
}

// Bus returns the communication bus.
func (m *Manager) Bus() Bus {
	return m.bus
}
