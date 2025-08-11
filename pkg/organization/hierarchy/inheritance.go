// file: pkg/organization/hierarchy/inheritance.go
// version: 1.0.0
// guid: d6d5b61f-068c-4c52-87de-4dc3e9509afa

// Package hierarchy provides permission inheritance utilities for organization structures.
package hierarchy

import (
	"context"
	"errors"
)

// InheritanceResolver resolves effective permissions for principals considering hierarchy relationships.
type InheritanceResolver struct {
	Tree        *Tree
	Permissions *PermissionManager
}

// NewInheritanceResolver returns a resolver with provided tree and permission manager.
func NewInheritanceResolver(t *Tree, pm *PermissionManager) *InheritanceResolver {
	return &InheritanceResolver{Tree: t, Permissions: pm}
}

// EffectivePermissions returns the accumulated permissions for a principal at the specified node.
// It traverses up the hierarchy to aggregate inherited permissions.
func (r *InheritanceResolver) EffectivePermissions(ctx context.Context, nodeID, principal string) (PermissionSet, error) {
	if r.Tree == nil || r.Permissions == nil {
		return nil, errors.New("resolver not initialized")
	}
	result := NewPermissionSet()
	current := nodeID
	for current != "" {
		pset, err := r.Permissions.Permissions(ctx, current, principal)
		if err == nil {
			result.Add(pset.AsSlice()...)
		}
		node, err := r.Tree.GetNode(ctx, current)
		if err != nil {
			break
		}
		current = node.GetParentId()
	}
	return result, nil
}

// HasPermission checks if the principal has the specified permission at the node considering inheritance.
func (r *InheritanceResolver) HasPermission(ctx context.Context, nodeID, principal string, perm Permission) (bool, error) {
	perms, err := r.EffectivePermissions(ctx, nodeID, principal)
	if err != nil {
		return false, err
	}
	return perms.Has(perm), nil
}

// Inherit assigns permissions from parent to child node for a principal.
// This function copies current permissions of the principal on the parent node and grants them to the child.
func (r *InheritanceResolver) Inherit(ctx context.Context, parentID, childID, principal string) error {
	if parentID == "" || childID == "" {
		return errors.New("missing parent or child id")
	}
	pset, err := r.Permissions.Permissions(ctx, parentID, principal)
	if err != nil {
		return err
	}
	return r.Permissions.Grant(ctx, childID, principal, pset)
}

// RevokeInherited removes permissions on a child that were inherited from the parent.
// It determines the parent's permissions and revokes them from the child node.
func (r *InheritanceResolver) RevokeInherited(ctx context.Context, parentID, childID, principal string) error {
	pset, err := r.Permissions.Permissions(ctx, parentID, principal)
	if err != nil {
		return err
	}
	return r.Permissions.Revoke(ctx, childID, principal, pset)
}

// Sync ensures that child nodes mirror the parent's permissions for the principal.
// Any additional permissions on the child not present on parent are removed.
func (r *InheritanceResolver) Sync(ctx context.Context, parentID, childID, principal string) error {
	parentSet, err := r.Permissions.Permissions(ctx, parentID, principal)
	if err != nil {
		return err
	}
	childSet, err := r.Permissions.Permissions(ctx, childID, principal)
	if err != nil {
		return err
	}
	// Revoke permissions on child not present on parent
	for p := range childSet {
		if !parentSet.Has(p) {
			childSet.Remove(p)
		}
	}
	// Grant missing permissions from parent
	for p := range parentSet {
		if !childSet.Has(p) {
			childSet.Add(p)
		}
	}
	// Clear current assignment and set updated permissions
	r.Permissions.Clear(ctx, childID, principal)
	return r.Permissions.Grant(ctx, childID, principal, childSet)
}
