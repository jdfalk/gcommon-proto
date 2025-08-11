// file: pkg/organization/hierarchy/department_manager_test.go
// version: 1.0.0
// guid: 4d5e6f70-8192-4a5b-bc6d-7e8f9012ab34

package hierarchy

import (
	"context"
	"testing"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

func dept(id, org, parent, name string) *orgpb.Department {
	return (&orgpb.Department_builder{Id: gproto.String(id), OrganizationId: gproto.String(org), ParentDepartmentId: gproto.String(parent), Name: gproto.String(name)}).Build()
}

func TestDepartmentLifecycle(t *testing.T) {
	ctx := context.Background()
	m := NewDepartmentManager()

	d := dept("d1", "o1", "", "Root")
	if err := m.CreateDepartment(ctx, d); err != nil {
		t.Fatalf("create: %v", err)
	}

	got, err := m.GetDepartment(ctx, "d1")
	if err != nil || got.GetName() != "Root" {
		t.Fatalf("get: %v %v", err, got)
	}

	d2 := dept("d1", "o1", "", "Renamed")
	if err := m.UpdateDepartment(ctx, d2); err != nil {
		t.Fatalf("update: %v", err)
	}

	list, err := m.ListDepartments(ctx, "o1")
	if err != nil || len(list) != 1 {
		t.Fatalf("list: %v len=%d", err, len(list))
	}

	if err := m.DeleteDepartment(ctx, "d1"); err != nil {
		t.Fatalf("delete: %v", err)
	}
	if _, err := m.GetDepartment(ctx, "d1"); err == nil {
		t.Fatalf("expected error after delete")
	}
}

func TestHierarchyOperations(t *testing.T) {
	ctx := context.Background()
	m := NewDepartmentManager()

	root := dept("root", "o1", "", "Root")
	_ = m.CreateDepartment(ctx, root)
	child := dept("child", "o1", "root", "Child")
	_ = m.CreateDepartment(ctx, child)

	children, err := m.Children(ctx, "root")
	if err != nil || len(children) != 1 {
		t.Fatalf("children: %v len=%d", err, len(children))
	}

	if err := m.MoveDepartment(ctx, "child", ""); err != nil {
		t.Fatalf("move: %v", err)
	}
	childMoved, _ := m.GetDepartment(ctx, "child")
	if childMoved.GetParentDepartmentId() != "" {
		t.Fatalf("move failed: %s", childMoved.GetParentDepartmentId())
	}
}
