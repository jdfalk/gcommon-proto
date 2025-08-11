// file: pkg/organization/manager.go
// version: 1.0.0
// guid: 1f2e3d4c-5b6a-7c8d-9e0f-1a2b3c4d5e6f

// Package organization implements organization and membership management.
package organization

import (
	"context"
	"errors"
	"sync"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// Manager provides in-memory organization storage and membership tracking.
type Manager struct {
	mu       sync.RWMutex
	orgs     map[string]*orgpb.Organization
	members  map[string]map[string]*orgpb.OrganizationMember // orgID -> memberID -> member
	settings map[string]*orgpb.OrganizationSettings
}

// NewManager returns an initialized Manager instance.
func NewManager() *Manager {
	return &Manager{
		orgs:     make(map[string]*orgpb.Organization),
		members:  make(map[string]map[string]*orgpb.OrganizationMember),
		settings: make(map[string]*orgpb.OrganizationSettings),
	}
}

// CreateOrganization stores a new organization definition.
func (m *Manager) CreateOrganization(ctx context.Context, org *orgpb.Organization) error {
	if org == nil || org.GetId() == "" {
		return errors.New("missing organization id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.orgs[org.GetId()]; exists {
		return errors.New("organization exists")
	}
	m.orgs[org.GetId()] = org
	return nil
}

// GetOrganization retrieves an organization by ID.
func (m *Manager) GetOrganization(ctx context.Context, orgID string) (*orgpb.Organization, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	o, ok := m.orgs[orgID]
	if !ok {
		return nil, errors.New("organization not found")
	}
	return o, nil
}

// UpdateOrganization replaces an existing organization entry.
func (m *Manager) UpdateOrganization(ctx context.Context, org *orgpb.Organization) error {
	if org == nil || org.GetId() == "" {
		return errors.New("missing organization id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.orgs[org.GetId()]; !ok {
		return errors.New("organization not found")
	}
	m.orgs[org.GetId()] = org
	return nil
}

// DeleteOrganization removes an organization and all associated members and settings.
func (m *Manager) DeleteOrganization(ctx context.Context, orgID string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.orgs[orgID]; !ok {
		return errors.New("organization not found")
	}
	delete(m.orgs, orgID)
	delete(m.members, orgID)
	delete(m.settings, orgID)
	return nil
}

// ListOrganizations returns all stored organizations.
func (m *Manager) ListOrganizations(ctx context.Context) ([]*orgpb.Organization, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := make([]*orgpb.Organization, 0, len(m.orgs))
	for _, o := range m.orgs {
		result = append(result, o)
	}
	return result, nil
}

// AddMember adds a member to the organization.
func (m *Manager) AddMember(ctx context.Context, orgID string, member *orgpb.OrganizationMember) error {
	if member == nil || member.GetId() == "" {
		return errors.New("missing member id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.orgs[orgID]; !ok {
		return errors.New("organization not found")
	}
	if _, ok := m.members[orgID]; !ok {
		m.members[orgID] = make(map[string]*orgpb.OrganizationMember)
	}
	if _, exists := m.members[orgID][member.GetId()]; exists {
		return errors.New("member exists")
	}
	m.members[orgID][member.GetId()] = member
	return nil
}

// RemoveMember deletes a member from the organization.
func (m *Manager) RemoveMember(ctx context.Context, orgID, memberID string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	members, ok := m.members[orgID]
	if !ok {
		return errors.New("organization not found")
	}
	if _, ok := members[memberID]; !ok {
		return errors.New("member not found")
	}
	delete(members, memberID)
	return nil
}

// UpdateMember updates a member's data.
func (m *Manager) UpdateMember(ctx context.Context, orgID string, member *orgpb.OrganizationMember) error {
	if member == nil || member.GetId() == "" {
		return errors.New("missing member id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	members, ok := m.members[orgID]
	if !ok {
		return errors.New("organization not found")
	}
	if _, ok := members[member.GetId()]; !ok {
		return errors.New("member not found")
	}
	members[member.GetId()] = member
	return nil
}

// ListMembers returns all members of an organization.
func (m *Manager) ListMembers(ctx context.Context, orgID string) ([]*orgpb.OrganizationMember, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	members, ok := m.members[orgID]
	if !ok {
		return nil, errors.New("organization not found")
	}
	result := make([]*orgpb.OrganizationMember, 0, len(members))
	for _, mbr := range members {
		result = append(result, mbr)
	}
	return result, nil
}

// GetSettings retrieves organization settings if present.
func (m *Manager) GetSettings(ctx context.Context, orgID string) (*orgpb.OrganizationSettings, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	s, ok := m.settings[orgID]
	if !ok {
		return nil, errors.New("settings not found")
	}
	return s, nil
}

// UpdateSettings sets organization settings.
func (m *Manager) UpdateSettings(ctx context.Context, settings *orgpb.OrganizationSettings) error {
	if settings == nil || settings.GetOrganizationId() == "" {
		return errors.New("missing organization id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	orgID := settings.GetOrganizationId()
	if _, ok := m.orgs[orgID]; !ok {
		return errors.New("organization not found")
	}
	m.settings[orgID] = settings
	return nil
}

// CloneOrganization returns a deep copy of the organization with the given ID.
// This is primarily used in tests to ensure callers do not mutate internal state.
func (m *Manager) CloneOrganization(ctx context.Context, orgID string) (*orgpb.Organization, error) {
	org, err := m.GetOrganization(ctx, orgID)
	if err != nil {
		return nil, err
	}
	return gproto.Clone(org).(*orgpb.Organization), nil
}

// CloneMember returns a deep copy of the organization member.
func (m *Manager) CloneMember(ctx context.Context, orgID, memberID string) (*orgpb.OrganizationMember, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	members, ok := m.members[orgID]
	if !ok {
		return nil, errors.New("organization not found")
	}
	member, ok := members[memberID]
	if !ok {
		return nil, errors.New("member not found")
	}
	return gproto.Clone(member).(*orgpb.OrganizationMember), nil
}

// Organizations returns a list of copies of all organizations.
func (m *Manager) Organizations(ctx context.Context) ([]*orgpb.Organization, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := make([]*orgpb.Organization, 0, len(m.orgs))
	for _, o := range m.orgs {
		result = append(result, gproto.Clone(o).(*orgpb.Organization))
	}
	return result, nil
}

// MembersMap returns a copy of member maps keyed by organization.
func (m *Manager) MembersMap(ctx context.Context) (map[string][]*orgpb.OrganizationMember, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := make(map[string][]*orgpb.OrganizationMember, len(m.members))
	for orgID, mset := range m.members {
		list := make([]*orgpb.OrganizationMember, 0, len(mset))
		for _, member := range mset {
			list = append(list, gproto.Clone(member).(*orgpb.OrganizationMember))
		}
		result[orgID] = list
	}
	return result, nil
}
