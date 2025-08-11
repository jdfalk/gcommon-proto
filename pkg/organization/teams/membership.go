// file: pkg/organization/teams/membership.go
// version: 1.0.0
// guid: 7daa5513-0b44-45c6-a783-cf5a8b2d5fcf

// Package teams provides team membership utilities.
package teams

import (
	"context"
	"errors"
	"sync"
)

// Member represents a team member with a specific role.
type Member struct {
	UserID string
	Role   Role
}

// MembershipManager manages team memberships in memory.
type MembershipManager struct {
	mu      sync.RWMutex
	members map[string][]*Member // teamID -> members
}

// NewMembershipManager returns an initialized MembershipManager.
func NewMembershipManager() *MembershipManager {
	return &MembershipManager{members: make(map[string][]*Member)}
}

// AddMember adds a user to the team with the given role.
func (m *MembershipManager) AddMember(ctx context.Context, teamID, userID string, role Role) error {
	if teamID == "" || userID == "" {
		return errors.New("missing team or user id")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	for _, member := range m.members[teamID] {
		if member.UserID == userID {
			return errors.New("member already exists")
		}
	}
	m.members[teamID] = append(m.members[teamID], &Member{UserID: userID, Role: role})
	return nil
}

// RemoveMember removes a user from the team.
func (m *MembershipManager) RemoveMember(ctx context.Context, teamID, userID string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	members := m.members[teamID]
	for i, member := range members {
		if member.UserID == userID {
			m.members[teamID] = append(members[:i], members[i+1:]...)
			return nil
		}
	}
	return errors.New("member not found")
}

// UpdateRole changes a member's role.
func (m *MembershipManager) UpdateRole(ctx context.Context, teamID, userID string, role Role) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	members := m.members[teamID]
	for _, member := range members {
		if member.UserID == userID {
			member.Role = role
			return nil
		}
	}
	return errors.New("member not found")
}

// ListMembers returns all members of a team.
func (m *MembershipManager) ListMembers(ctx context.Context, teamID string) ([]*Member, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	members, ok := m.members[teamID]
	if !ok {
		return nil, errors.New("team not found")
	}
	result := make([]*Member, len(members))
	copy(result, members)
	return result, nil
}

// RoleOf returns the role for the specified user in the team.
func (m *MembershipManager) RoleOf(ctx context.Context, teamID, userID string) (Role, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	for _, member := range m.members[teamID] {
		if member.UserID == userID {
			return member.Role, nil
		}
	}
	return Role(""), errors.New("member not found")
}

// Clear removes all members from a team.
func (m *MembershipManager) Clear(ctx context.Context, teamID string) {
	m.mu.Lock()
	defer m.mu.Unlock()
	delete(m.members, teamID)
}
