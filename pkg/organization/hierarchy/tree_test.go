// file: pkg/organization/hierarchy/tree_test.go
// version: 1.0.0
// guid: 4cbcec60-0989-4ed3-818a-f0a4208d4f9a

package hierarchy

import (
	"context"
	"testing"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// TestTree_BasicOperations verifies basic node operations.
func TestTree_BasicOperations(t *testing.T) {
	// Setup
	tree := NewTree()
	ctx := context.Background()
	root := (&orgpb.HierarchyNode_builder{Id: gproto.String("root"), ParentId: gproto.String("")}).Build()
	if err := tree.CreateNode(ctx, root); err != nil {
		t.Fatalf("create root: %v", err)
	}
	child := (&orgpb.HierarchyNode_builder{Id: gproto.String("child"), ParentId: gproto.String("root")}).Build()
	if err := tree.CreateNode(ctx, child); err != nil {
		t.Fatalf("create child: %v", err)
	}

	// Exercise
	if err := tree.MoveNode(ctx, "child", ""); err != nil {
		t.Fatalf("move node: %v", err)
	}

	// Verify
	got, err := tree.GetNode(ctx, "child")
	if err != nil {
		t.Fatalf("get node: %v", err)
	}
	if got.GetParentId() != "" {
		t.Fatalf("expected parent '', got %s", got.GetParentId())
	}
	children, _ := tree.GetChildren(ctx, "root")
	if len(children) != 0 {
		t.Fatalf("expected no children")
	}
}
