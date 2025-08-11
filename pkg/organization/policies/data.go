// file: pkg/organization/policies/data.go
// version: 1.0.0
// guid: 077dc19f-a8ca-435c-8ef8-fc00cb359db1

// Package policies defines data governance rules for organizations.
package policies

import (
	"context"
	"errors"
	"sync"
	"time"
)

// DataPolicy enforces data retention and locality rules.
type DataPolicy struct {
	RetentionPeriod time.Duration
	AllowedRegions  []string
}

// DataPolicyManager manages policies per tenant.
type DataPolicyManager struct {
	mu       sync.RWMutex
	policies map[string]*DataPolicy
}

// NewDataPolicyManager creates a manager instance.
func NewDataPolicyManager() *DataPolicyManager {
	return &DataPolicyManager{policies: make(map[string]*DataPolicy)}
}

// SetPolicy sets the data policy for a tenant.
func (m *DataPolicyManager) SetPolicy(ctx context.Context, tenantID string, p *DataPolicy) error {
	if tenantID == "" || p == nil {
		return errors.New("invalid input")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	m.policies[tenantID] = p
	return nil
}

// GetPolicy retrieves the data policy for a tenant.
func (m *DataPolicyManager) GetPolicy(ctx context.Context, tenantID string) (*DataPolicy, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	p, ok := m.policies[tenantID]
	if !ok {
		return nil, errors.New("policy not found")
	}
	cp := *p
	return &cp, nil
}

// Enforce checks whether data access complies with policy.
func (m *DataPolicyManager) Enforce(ctx context.Context, tenantID, region string, created time.Time) error {
	m.mu.RLock()
	p, ok := m.policies[tenantID]
	m.mu.RUnlock()
	if !ok {
		return errors.New("policy not found")
	}
	if time.Since(created) > p.RetentionPeriod {
		return errors.New("data retention exceeded")
	}
	for _, r := range p.AllowedRegions {
		if r == region {
			return nil
		}
	}
	return errors.New("region not allowed")
}
