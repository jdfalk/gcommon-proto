// file: pkg/organization/interfaces.go
// version: 1.0.0
// guid: 674239c9-d92a-4b83-9ec8-c88c1b3dd040

// Package organization provides service interfaces for managing organizations.
package organization

import (
	"context"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
)

// TenantManager defines operations for tenant lifecycle management.
type TenantManager interface {
	CreateTenant(ctx context.Context, tenant *orgpb.Tenant) error
	GetTenant(ctx context.Context, tenantID string) (*orgpb.Tenant, error)
	UpdateTenant(ctx context.Context, tenant *orgpb.Tenant) error
	DeleteTenant(ctx context.Context, tenantID string) error
	ListTenants(ctx context.Context) ([]*orgpb.Tenant, error)
}

// HierarchyManager defines operations for organization hierarchy management.
type HierarchyManager interface {
	CreateNode(ctx context.Context, node *orgpb.HierarchyNode) error
	GetNode(ctx context.Context, nodeID string) (*orgpb.HierarchyNode, error)
	GetChildren(ctx context.Context, parentID string) ([]*orgpb.HierarchyNode, error)
	MoveNode(ctx context.Context, nodeID, newParentID string) error
}
