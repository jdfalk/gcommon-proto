// file: pkg/organization/policies/security.go
// version: 1.0.0
// guid: 9ba15281-3de3-4379-86e4-30d38df290e2

// Package policies contains security policy enforcement for organizations.
package policies

import (
	"context"
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"sync"
)

// SecurityPolicy defines cross-tenant security restrictions.
type SecurityPolicy struct {
	AllowedHashes []string
}

// SecurityManager stores security policies per tenant and verifies access tokens.
type SecurityManager struct {
	mu       sync.RWMutex
	policies map[string]*SecurityPolicy
}

// NewSecurityManager returns an initialized manager.
func NewSecurityManager() *SecurityManager {
	return &SecurityManager{policies: make(map[string]*SecurityPolicy)}
}

// SetPolicy sets the security policy for a tenant.
func (m *SecurityManager) SetPolicy(ctx context.Context, tenantID string, p *SecurityPolicy) error {
	if tenantID == "" || p == nil {
		return errors.New("invalid input")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	m.policies[tenantID] = p
	return nil
}

// ValidateToken verifies that the token hash is allowed for the tenant.
func (m *SecurityManager) ValidateToken(ctx context.Context, tenantID, token string) error {
	m.mu.RLock()
	p, ok := m.policies[tenantID]
	m.mu.RUnlock()
	if !ok {
		return errors.New("policy not found")
	}
	h := sha256.Sum256([]byte(token))
	hash := hex.EncodeToString(h[:])
	for _, allowed := range p.AllowedHashes {
		if hash == allowed {
			return nil
		}
	}
	return errors.New("token not allowed")
}
