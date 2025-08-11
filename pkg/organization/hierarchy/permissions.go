// file: pkg/organization/hierarchy/permissions.go
// version: 1.0.0
// guid: 9ba185ed-256c-40f9-987d-5a1b3e027aa4

// Package hierarchy implements hierarchical permission management.
package hierarchy

import (
	"context"
	"errors"
	"sync"
)

// Permission defines an action that can be performed within the hierarchy.
type Permission string

const (
	// PermRead allows read access to a node.
	PermRead Permission = "read"
	// PermWrite allows write access to a node.
	PermWrite Permission = "write"
	// PermAdmin allows administrative actions on a node.
	PermAdmin Permission = "admin"
)

// PermissionSet represents a collection of permissions.
type PermissionSet map[Permission]struct{}

// NewPermissionSet creates a PermissionSet from a list of permissions.
func NewPermissionSet(perms ...Permission) PermissionSet {
	ps := make(PermissionSet)
	for _, p := range perms {
		ps[p] = struct{}{}
	}
	return ps
}

// Has reports whether the permission set contains the permission.
func (ps PermissionSet) Has(p Permission) bool {
	_, ok := ps[p]
	return ok
}

// Add inserts permissions into the set.
func (ps PermissionSet) Add(perms ...Permission) {
	for _, p := range perms {
		ps[p] = struct{}{}
	}
}

// Remove deletes permissions from the set.
func (ps PermissionSet) Remove(perms ...Permission) {
	for _, p := range perms {
		delete(ps, p)
	}
}

// Copy returns a shallow copy of the permission set.
func (ps PermissionSet) Copy() PermissionSet {
	cp := make(PermissionSet)
	for p := range ps {
		cp[p] = struct{}{}
	}
	return cp
}

// PermissionManager stores permissions per hierarchy node and principal.
type PermissionManager struct {
	mu          sync.RWMutex
	assignments map[string]map[string]PermissionSet // nodeID -> principal -> perms
}

// NewPermissionManager returns an initialized PermissionManager.
func NewPermissionManager() *PermissionManager {
	return &PermissionManager{assignments: make(map[string]map[string]PermissionSet)}
}

// Grant adds permissions for the principal on the node.
func (m *PermissionManager) Grant(ctx context.Context, nodeID, principal string, perms PermissionSet) error {
	if nodeID == "" || principal == "" {
		return errors.New("missing node or principal")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.assignments[nodeID]; !ok {
		m.assignments[nodeID] = make(map[string]PermissionSet)
	}
	if _, ok := m.assignments[nodeID][principal]; !ok {
		m.assignments[nodeID][principal] = make(PermissionSet)
	}
	m.assignments[nodeID][principal].Add(perms.AsSlice()...)
	return nil
}

// Revoke removes permissions for the principal on the node.
func (m *PermissionManager) Revoke(ctx context.Context, nodeID, principal string, perms PermissionSet) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	principals, ok := m.assignments[nodeID]
	if !ok {
		return errors.New("node not found")
	}
	pset, ok := principals[principal]
	if !ok {
		return errors.New("principal not found")
	}
	pset.Remove(perms.AsSlice()...)
	if len(pset) == 0 {
		delete(principals, principal)
	}
	return nil
}

// Permissions retrieves permissions for a principal on a node.
func (m *PermissionManager) Permissions(ctx context.Context, nodeID, principal string) (PermissionSet, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	principals, ok := m.assignments[nodeID]
	if !ok {
		return nil, errors.New("node not found")
	}
	pset, ok := principals[principal]
	if !ok {
		return nil, errors.New("principal not found")
	}
	return pset.Copy(), nil
}

// Clear removes all permissions for a node or, if principal provided, for that principal on the node.
func (m *PermissionManager) Clear(ctx context.Context, nodeID, principal string) {
	m.mu.Lock()
	defer m.mu.Unlock()
	if principal == "" {
		delete(m.assignments, nodeID)
		return
	}
	if principals, ok := m.assignments[nodeID]; ok {
		delete(principals, principal)
		if len(principals) == 0 {
			delete(m.assignments, nodeID)
		}
	}
}

// AsSlice converts the permission set into a slice.
func (ps PermissionSet) AsSlice() []Permission {
	result := make([]Permission, 0, len(ps))
	for p := range ps {
		result = append(result, p)
	}
	return result
}
