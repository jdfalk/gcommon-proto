// file: pkg/organization/teams/manager.go
// version: 1.1.0
// guid: 06c314f0-0e40-4ac7-8c2e-ce2577b0905a

// Package teams implements in-memory team management services.
package teams

import (
	"context"
	"errors"
	"sync"
)

// Team represents a collection of users.
type Team struct {
	ID   string
	Name string
}

// Manager provides team CRUD operations and membership management.
type Manager struct {
	mu         sync.RWMutex
	teams      map[string]*Team
	membership *MembershipManager
}

// NewManager returns a Manager with initialized maps and membership manager.
func NewManager() *Manager {
	return &Manager{
		teams:      make(map[string]*Team),
		membership: NewMembershipManager(),
	}
}

// CreateTeam stores a team definition.
func (m *Manager) CreateTeam(ctx context.Context, team *Team) error {
	if team == nil || team.ID == "" {
		return errors.New("missing team id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.teams[team.ID]; exists {
		return errors.New("team exists")
	}
	m.teams[team.ID] = team
	return nil
}

// GetTeam retrieves a team by ID.
func (m *Manager) GetTeam(ctx context.Context, teamID string) (*Team, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	t, ok := m.teams[teamID]
	if !ok {
		return nil, errors.New("team not found")
	}
	return t, nil
}

// UpdateTeam updates a team name.
func (m *Manager) UpdateTeam(ctx context.Context, team *Team) error {
	if team == nil || team.ID == "" {
		return errors.New("missing team id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.teams[team.ID]; !ok {
		return errors.New("team not found")
	}
	m.teams[team.ID] = team
	return nil
}

// DeleteTeam removes a team and its memberships.
func (m *Manager) DeleteTeam(ctx context.Context, teamID string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, ok := m.teams[teamID]; !ok {
		return errors.New("team not found")
	}
	delete(m.teams, teamID)
	m.membership.Clear(ctx, teamID)
	return nil
}

// ListTeams returns all stored teams.
func (m *Manager) ListTeams(ctx context.Context) ([]*Team, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	result := make([]*Team, 0, len(m.teams))
	for _, t := range m.teams {
		result = append(result, t)
	}
	return result, nil
}

// AddMember adds a user to the team with the specified role.
func (m *Manager) AddMember(ctx context.Context, teamID, userID string, role Role) error {
	if _, err := m.GetTeam(ctx, teamID); err != nil {
		return err
	}
	return m.membership.AddMember(ctx, teamID, userID, role)
}

// RemoveMember removes a user from the team.
func (m *Manager) RemoveMember(ctx context.Context, teamID, userID string) error {
	if _, err := m.GetTeam(ctx, teamID); err != nil {
		return err
	}
	return m.membership.RemoveMember(ctx, teamID, userID)
}

// UpdateMemberRole updates the role for a team member.
func (m *Manager) UpdateMemberRole(ctx context.Context, teamID, userID string, role Role) error {
	if _, err := m.GetTeam(ctx, teamID); err != nil {
		return err
	}
	return m.membership.UpdateRole(ctx, teamID, userID, role)
}

// Members returns a list of members for a team.
func (m *Manager) Members(ctx context.Context, teamID string) ([]*Member, error) {
	if _, err := m.GetTeam(ctx, teamID); err != nil {
		return nil, err
	}
	return m.membership.ListMembers(ctx, teamID)
}

// RoleOf retrieves a member's role within a team.
func (m *Manager) RoleOf(ctx context.Context, teamID, userID string) (Role, error) {
	if _, err := m.GetTeam(ctx, teamID); err != nil {
		return Role(""), err
	}
	return m.membership.RoleOf(ctx, teamID, userID)
}
