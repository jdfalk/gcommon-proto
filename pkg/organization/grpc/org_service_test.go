// file: pkg/organization/grpc/org_service_test.go
// version: 1.0.0
// guid: 6c7d8e9f-0a1b-4c2d-8e3f-4a5b6c7d8e9f

package grpc

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

func TestOrganizationLifecycle(t *testing.T) {
	ctx := context.Background()
	services := organization.NewServices()
	svc := NewOrganizationService(services.Organizations)
	org := (&orgpb.Organization_builder{Id: gproto.String("o1"), Name: gproto.String("Org")}).Build()
	_, err := svc.CreateOrganization(ctx, (&orgpb.CreateOrganizationRequest_builder{Organization: org}).Build())
	if err != nil {
		t.Fatalf("create: %v", err)
	}

	got, err := svc.GetOrganization(ctx, (&orgpb.GetOrganizationRequest_builder{OrganizationId: gproto.String("o1")}).Build())
	if err != nil || got.GetOrganization().GetName() != "Org" {
		t.Fatalf("get: %v", err)
	}

	members := (&orgpb.OrganizationMember_builder{Id: gproto.String("m1"), OrganizationId: gproto.String("o1"), UserId: gproto.String("u1")}).Build()
	_, err = svc.AddMember(ctx, (&orgpb.AddMemberRequest_builder{OrganizationId: gproto.String("o1"), Member: members}).Build())
	if err != nil {
		t.Fatalf("add member: %v", err)
	}

	list, err := svc.ListMembers(ctx, (&orgpb.ListMembersRequest_builder{OrganizationId: gproto.String("o1")}).Build())
	if err != nil || len(list.GetMembers()) != 1 {
		t.Fatalf("list members: %v len=%d", err, len(list.GetMembers()))
	}

	_, err = svc.DeleteOrganization(ctx, (&orgpb.DeleteOrganizationRequest_builder{OrganizationId: gproto.String("o1")}).Build())
	if err != nil {
		t.Fatalf("delete: %v", err)
	}
}
