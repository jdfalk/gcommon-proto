// file: pkg/organization/tenant/isolation.go
// version: 1.1.0
// guid: e0e9b8e1-fd68-4d0f-b71c-21107150ba42

// Package tenant provides tenant isolation and data segregation helpers.
package tenant

import (
	"context"
	"errors"
	"sync"
)

// Usage captures resource consumption metrics.
type Usage struct {
	CpuSeconds   int64
	MemoryBytes  int64
	StorageBytes int64
	NetworkBytes int64
}

// IsolationConfig defines resource isolation rules for a tenant.
type IsolationConfig struct {
	// AllowedDomains enumerates domains a tenant may access.
	AllowedDomains []string
	// RestrictedResources lists resource identifiers the tenant cannot touch.
	RestrictedResources []string
	// CustomPolicies references optional policy identifiers applied to the tenant.
	CustomPolicies []string
}

// IsolationManager manages tenant isolation configurations in memory.
type IsolationManager struct {
	mu      sync.RWMutex
	configs map[string]*IsolationConfig
	usage   map[string]*Usage
}

// NewIsolationManager creates an initialized IsolationManager.
func NewIsolationManager() *IsolationManager {
	return &IsolationManager{
		configs: make(map[string]*IsolationConfig),
		usage:   make(map[string]*Usage),
	}
}

// Configure sets isolation rules for a tenant, replacing any existing config.
// It also initializes usage tracking if not present.
func (m *IsolationManager) Configure(ctx context.Context, tenantID string, cfg *IsolationConfig) error {
	if tenantID == "" {
		return errors.New("missing tenant id")
	}
	if cfg == nil {
		return errors.New("missing isolation config")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	m.configs[tenantID] = cfg
	if _, ok := m.usage[tenantID]; !ok {
		m.usage[tenantID] = &Usage{}
	}
	return nil
}

// Get returns the isolation configuration for a tenant.
func (m *IsolationManager) Get(ctx context.Context, tenantID string) (*IsolationConfig, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	cfg, ok := m.configs[tenantID]
	if !ok {
		return nil, errors.New("isolation config not found")
	}
	return cfg, nil
}

// RecordUsage updates usage statistics for a tenant.
// This function is thread-safe and accumulates resource counts per category.
func (m *IsolationManager) RecordUsage(ctx context.Context, tenantID string, usage *Usage) error {
	if usage == nil {
		return errors.New("missing usage")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	current, ok := m.usage[tenantID]
	if !ok {
		current = &Usage{}
		m.usage[tenantID] = current
	}
	current.CpuSeconds += usage.CpuSeconds
	current.MemoryBytes += usage.MemoryBytes
	current.StorageBytes += usage.StorageBytes
	current.NetworkBytes += usage.NetworkBytes
	return nil
}

// Usage returns current usage statistics for a tenant.
func (m *IsolationManager) Usage(ctx context.Context, tenantID string) (*Usage, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	usage, ok := m.usage[tenantID]
	if !ok {
		return nil, errors.New("usage not found")
	}
	copy := *usage
	return &copy, nil
}

// Enforce checks whether a resource access is permitted under the tenant's isolation rules.
// It returns an error if the tenant attempts to access a restricted resource or domain.
func (m *IsolationManager) Enforce(ctx context.Context, tenantID, domain, resource string) error {
	m.mu.RLock()
	cfg, ok := m.configs[tenantID]
	m.mu.RUnlock()
	if !ok {
		return errors.New("isolation config not found")
	}
	for _, d := range cfg.AllowedDomains {
		if d == domain {
			// Domain allowed, proceed to resource check.
			for _, r := range cfg.RestrictedResources {
				if r == resource {
					return errors.New("resource access denied")
				}
			}
			return nil
		}
	}
	return errors.New("domain access denied")
}

// Remove deletes isolation settings and usage tracking for a tenant.
func (m *IsolationManager) Remove(ctx context.Context, tenantID string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	delete(m.configs, tenantID)
	delete(m.usage, tenantID)
	return nil
}

// List returns all tenant IDs with isolation configurations.
func (m *IsolationManager) List(ctx context.Context) []string {
	m.mu.RLock()
	defer m.mu.RUnlock()
	ids := make([]string, 0, len(m.configs))
	for id := range m.configs {
		ids = append(ids, id)
	}
	return ids
}
