// file: pkg/organization/tenant/manager.go
// version: 1.1.0
// guid: 8974f08a-188a-467d-8849-aede36294cbb

// Package tenant implements tenant lifecycle management.
package tenant

import (
	"context"
	"errors"
	"sync"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
)

// Manager provides in-memory tenant management.
type Manager struct {
	mu      sync.RWMutex
	tenants map[string]*orgpb.Tenant
}

// NewManager returns a new Manager instance.
func NewManager() *Manager {
	return &Manager{tenants: make(map[string]*orgpb.Tenant)}
}

// CreateTenant stores a new tenant if it does not already exist.
func (m *Manager) CreateTenant(ctx context.Context, tenant *orgpb.Tenant) error {
	id := tenant.GetId()
	if id == "" {
		return errors.New("missing tenant id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.tenants[id]; exists {
		return errors.New("tenant already exists")
	}
	m.tenants[id] = tenant
	return nil
}

// GetTenant retrieves a tenant by ID.
func (m *Manager) GetTenant(ctx context.Context, tenantID string) (*orgpb.Tenant, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	t, ok := m.tenants[tenantID]
	if !ok {
		return nil, errors.New("tenant not found")
	}
	return t, nil
}

// UpdateTenant replaces an existing tenant entry.
func (m *Manager) UpdateTenant(ctx context.Context, tenant *orgpb.Tenant) error {
	id := tenant.GetId()
	if id == "" {
		return errors.New("missing tenant id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.tenants[id]; !exists {
		return errors.New("tenant not found")
	}
	m.tenants[id] = tenant
	return nil
}

// DeleteTenant removes a tenant by ID.
func (m *Manager) DeleteTenant(ctx context.Context, tenantID string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.tenants[tenantID]; !exists {
		return errors.New("tenant not found")
	}
	delete(m.tenants, tenantID)
	return nil
}

// ListTenants returns all stored tenants.
func (m *Manager) ListTenants(ctx context.Context) ([]*orgpb.Tenant, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := make([]*orgpb.Tenant, 0, len(m.tenants))
	for _, t := range m.tenants {
		result = append(result, t)
	}
	return result, nil
}
