// file: pkg/organization/examples/hierarchy.go
// version: 1.0.0
// guid: f685d855-7fdf-4026-b36e-caa18267d1e0

package examples

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/organization/hierarchy"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// ExampleHierarchy demonstrates building a simple organization hierarchy.
func ExampleHierarchy() {
	ctx := context.Background()
	tree := hierarchy.NewTree()
	root := (&orgpb.HierarchyNode_builder{Id: gproto.String("root"), ParentId: gproto.String("")}).Build()
	_ = tree.CreateNode(ctx, root)
	dept := (&orgpb.HierarchyNode_builder{Id: gproto.String("dept1"), ParentId: gproto.String("root")}).Build()
	_ = tree.CreateNode(ctx, dept)
	children, _ := tree.GetChildren(ctx, "root")
	fmt.Printf("children: %d\n", len(children))
	// Output: children: 1
}
