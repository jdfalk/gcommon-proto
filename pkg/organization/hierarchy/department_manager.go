// file: pkg/organization/hierarchy/department_manager.go
// version: 1.0.0
// guid: 3c4d5e6f-7081-4a92-bc3d-5e6f708192a0

// Package hierarchy provides department management for organizations.
package hierarchy

import (
	"context"
	"errors"
	"sync"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
)

// DepartmentManager manages departments and their hierarchy in memory.
type DepartmentManager struct {
	mu          sync.RWMutex
	departments map[string]*orgpb.Department
}

// NewDepartmentManager returns an initialized DepartmentManager.
func NewDepartmentManager() *DepartmentManager {
	return &DepartmentManager{departments: make(map[string]*orgpb.Department)}
}

// CreateDepartment adds a department definition.
func (m *DepartmentManager) CreateDepartment(ctx context.Context, d *orgpb.Department) error {
	if d == nil || d.GetId() == "" {
		return errors.New("missing department id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.departments[d.GetId()]; exists {
		return errors.New("department exists")
	}
	m.departments[d.GetId()] = d
	return nil
}

// GetDepartment retrieves a department by ID.
func (m *DepartmentManager) GetDepartment(ctx context.Context, id string) (*orgpb.Department, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	d, ok := m.departments[id]
	if !ok {
		return nil, errors.New("department not found")
	}
	return d, nil
}

// UpdateDepartment replaces an existing department.
func (m *DepartmentManager) UpdateDepartment(ctx context.Context, d *orgpb.Department) error {
	if d == nil || d.GetId() == "" {
		return errors.New("missing department id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.departments[d.GetId()]; !ok {
		return errors.New("department not found")
	}
	m.departments[d.GetId()] = d
	return nil
}

// DeleteDepartment removes a department.
func (m *DepartmentManager) DeleteDepartment(ctx context.Context, id string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.departments[id]; !ok {
		return errors.New("department not found")
	}
	delete(m.departments, id)
	return nil
}

// ListDepartments returns departments for an organization.
func (m *DepartmentManager) ListDepartments(ctx context.Context, orgID string) ([]*orgpb.Department, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := []*orgpb.Department{}
	for _, d := range m.departments {
		if d.GetOrganizationId() == orgID {
			result = append(result, d)
		}
	}
	return result, nil
}

// Children returns child departments of the given parent.
func (m *DepartmentManager) Children(ctx context.Context, parentID string) ([]*orgpb.Department, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := []*orgpb.Department{}
	for _, d := range m.departments {
		if d.GetParentDepartmentId() == parentID {
			result = append(result, d)
		}
	}
	return result, nil
}

// MoveDepartment changes the parent of a department.
func (m *DepartmentManager) MoveDepartment(ctx context.Context, id, newParent string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	d, ok := m.departments[id]
	if !ok {
		return errors.New("department not found")
	}
	b := &orgpb.Department_builder{}
	*b = *d.AsBuilder()
	b.ParentDepartmentId = &newParent
	m.departments[id] = b.Build()
	return nil
}
