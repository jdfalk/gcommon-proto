// file: pkg/organization/hierarchy/tree.go
// version: 1.1.0
// guid: c4744bfd-7318-4c57-bef7-cb6265d69569

// Package hierarchy provides simple organization hierarchy management.
package hierarchy

import (
	"context"
	"errors"
	"sync"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// Tree manages a collection of hierarchy nodes in memory.
type Tree struct {
	mu    sync.RWMutex
	nodes map[string]*orgpb.HierarchyNode
}

// NewTree creates an empty hierarchy tree.
func NewTree() *Tree {
	return &Tree{nodes: make(map[string]*orgpb.HierarchyNode)}
}

// CreateNode adds a node to the hierarchy.
func (t *Tree) CreateNode(ctx context.Context, node *orgpb.HierarchyNode) error {
	id := node.GetId()
	if id == "" {
		return errors.New("missing node id")
	}
	t.mu.Lock()
	defer t.mu.Unlock()
	if _, exists := t.nodes[id]; exists {
		return errors.New("node exists")
	}
	t.nodes[id] = node
	return nil
}

// GetNode retrieves a node by ID.
func (t *Tree) GetNode(ctx context.Context, nodeID string) (*orgpb.HierarchyNode, error) {
	t.mu.RLock()
	defer t.mu.RUnlock()
	n, ok := t.nodes[nodeID]
	if !ok {
		return nil, errors.New("node not found")
	}
	return n, nil
}

// GetChildren returns children of a given parent ID.
func (t *Tree) GetChildren(ctx context.Context, parentID string) ([]*orgpb.HierarchyNode, error) {
	t.mu.RLock()
	defer t.mu.RUnlock()
	var children []*orgpb.HierarchyNode
	for _, n := range t.nodes {
		if n.GetParentId() == parentID {
			children = append(children, n)
		}
	}
	return children, nil
}

// MoveNode changes a node's parent.
func (t *Tree) MoveNode(ctx context.Context, nodeID, newParentID string) error {
	t.mu.Lock()
	defer t.mu.Unlock()
	n, ok := t.nodes[nodeID]
	if !ok {
		return errors.New("node not found")
	}
	// Note: HierarchyNode uses builder pattern for updates; create a new node with updated parent.
	updated := (&orgpb.HierarchyNode_builder{
		Id:       gproto.String(n.GetId()),
		ParentId: gproto.String(newParentID),
	}).Build()
	t.nodes[nodeID] = updated
	return nil
}
