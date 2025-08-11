// file: pkg/organization/manager_test.go
// version: 1.0.0
// guid: 2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d

package organization

import (
	"context"
	"testing"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// helper organization object
func testOrg(id, name string) *orgpb.Organization {
	return (&orgpb.Organization_builder{Id: gproto.String(id), Name: gproto.String(name)}).Build()
}

// helper member object
func testMember(id, orgID, userID string) *orgpb.OrganizationMember {
	return (&orgpb.OrganizationMember_builder{Id: gproto.String(id), OrganizationId: gproto.String(orgID), UserId: gproto.String(userID)}).Build()
}

func TestManagerCRUD(t *testing.T) {
	ctx := context.Background()
	m := NewManager()

	org := testOrg("org1", "Acme")
	if err := m.CreateOrganization(ctx, org); err != nil {
		t.Fatalf("create: %v", err)
	}

	got, err := m.GetOrganization(ctx, "org1")
	if err != nil {
		t.Fatalf("get: %v", err)
	}
	if got.GetName() != "Acme" {
		t.Fatalf("name mismatch: %s", got.GetName())
	}

	org2 := testOrg("org1", "NewName")
	if err := m.UpdateOrganization(ctx, org2); err != nil {
		t.Fatalf("update: %v", err)
	}
	got, _ = m.GetOrganization(ctx, "org1")
	if got.GetName() != "NewName" {
		t.Fatalf("update failed: %s", got.GetName())
	}

	list, err := m.ListOrganizations(ctx)
	if err != nil || len(list) != 1 {
		t.Fatalf("list: %v len=%d", err, len(list))
	}

	if err := m.DeleteOrganization(ctx, "org1"); err != nil {
		t.Fatalf("delete: %v", err)
	}
	if _, err := m.GetOrganization(ctx, "org1"); err == nil {
		t.Fatalf("expected error after delete")
	}
}

func TestMemberManagement(t *testing.T) {
	ctx := context.Background()
	m := NewManager()
	org := testOrg("o1", "Org")
	if err := m.CreateOrganization(ctx, org); err != nil {
		t.Fatalf("create org: %v", err)
	}

	mem := testMember("m1", "o1", "u1")
	if err := m.AddMember(ctx, "o1", mem); err != nil {
		t.Fatalf("add member: %v", err)
	}

	members, err := m.ListMembers(ctx, "o1")
	if err != nil || len(members) != 1 {
		t.Fatalf("list members: %v len=%d", err, len(members))
	}

	mem2 := testMember("m1", "o1", "u2")
	if err := m.UpdateMember(ctx, "o1", mem2); err != nil {
		t.Fatalf("update member: %v", err)
	}
	cloned, err := m.CloneMember(ctx, "o1", "m1")
	if err != nil || cloned.GetUserId() != "u2" {
		t.Fatalf("clone member: %v uid=%s", err, cloned.GetUserId())
	}

	if err := m.RemoveMember(ctx, "o1", "m1"); err != nil {
		t.Fatalf("remove member: %v", err)
	}
	if _, err := m.CloneMember(ctx, "o1", "m1"); err == nil {
		t.Fatalf("expected error after remove")
	}
}

func TestSettings(t *testing.T) {
	ctx := context.Background()
	m := NewManager()
	org := testOrg("o1", "Org")
	_ = m.CreateOrganization(ctx, org)

	s := (&orgpb.OrganizationSettings_builder{OrganizationId: gproto.String("o1")}).Build()
	if err := m.UpdateSettings(ctx, s); err != nil {
		t.Fatalf("update settings: %v", err)
	}
	got, err := m.GetSettings(ctx, "o1")
	if err != nil || got.GetOrganizationId() != "o1" {
		t.Fatalf("get settings: %v", err)
	}
}
