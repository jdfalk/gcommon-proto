// file: pkg/organization/teams/manager_test.go
// version: 1.0.0
// guid: 3fb1b858-2942-41fc-870c-a61d25388ceb

package teams

import (
	"context"
	"testing"
)

// TestManager_TeamAndMembers verifies team and membership operations.
func TestManager_TeamAndMembers(t *testing.T) {
	// Setup
	ctx := context.Background()
	m := NewManager()
	team := &Team{ID: "t1", Name: "TeamOne"}
	if err := m.CreateTeam(ctx, team); err != nil {
		t.Fatalf("create team: %v", err)
	}

	// Add members
	if err := m.AddMember(ctx, "t1", "u1", RoleOwner); err != nil {
		t.Fatalf("add member: %v", err)
	}
	if err := m.AddMember(ctx, "t1", "u2", RoleMember); err != nil {
		t.Fatalf("add member: %v", err)
	}

	// Verify members
	members, err := m.Members(ctx, "t1")
	if err != nil {
		t.Fatalf("members: %v", err)
	}
	if len(members) != 2 {
		t.Fatalf("expected 2 members")
	}

	// Update role
	if err := m.UpdateMemberRole(ctx, "t1", "u2", RoleAdmin); err != nil {
		t.Fatalf("update role: %v", err)
	}
	role, err := m.RoleOf(ctx, "t1", "u2")
	if err != nil {
		t.Fatalf("role of: %v", err)
	}
	if role != RoleAdmin {
		t.Fatalf("expected admin role")
	}

	// Remove member
	if err := m.RemoveMember(ctx, "t1", "u1"); err != nil {
		t.Fatalf("remove member: %v", err)
	}
	members, _ = m.Members(ctx, "t1")
	if len(members) != 1 {
		t.Fatalf("expected 1 member after removal")
	}
}
