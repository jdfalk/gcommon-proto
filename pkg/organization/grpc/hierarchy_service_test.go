// file: pkg/organization/grpc/hierarchy_service_test.go
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-4d5e-8f6a-7b8c9d0e1f2a

package grpc

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

func TestDepartmentLifecycle(t *testing.T) {
	ctx := context.Background()
	services := organization.NewServices()
	svc := NewHierarchyService(services.Departments)
	dept := (&orgpb.Department_builder{Id: gproto.String("d1"), OrganizationId: gproto.String("o1"), Name: gproto.String("Dept")}).Build()
	_, err := svc.CreateDepartment(ctx, (&orgpb.CreateDepartmentRequest_builder{Department: dept}).Build())
	if err != nil {
		t.Fatalf("create: %v", err)
	}

	got, err := svc.GetDepartment(ctx, (&orgpb.GetDepartmentRequest_builder{DepartmentId: gproto.String("d1")}).Build())
	if err != nil || got.GetDepartment().GetName() != "Dept" {
		t.Fatalf("get: %v", err)
	}

	list, err := svc.ListDepartments(ctx, (&orgpb.ListDepartmentsRequest_builder{OrganizationId: gproto.String("o1")}).Build())
	if err != nil || len(list.GetDepartments()) != 1 {
		t.Fatalf("list: %v len=%d", err, len(list.GetDepartments()))
	}

	_, err = svc.DeleteDepartment(ctx, (&orgpb.DeleteDepartmentRequest_builder{DepartmentId: gproto.String("d1")}).Build())
	if err != nil {
		t.Fatalf("delete: %v", err)
	}
}
