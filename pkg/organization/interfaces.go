// file: pkg/organization/interfaces.go
// version: 1.1.0
// guid: 674239c9-d92a-4b83-9ec8-c88c1b3dd040

// Package organization provides service interfaces for managing organizations.
package organization

import (
	"context"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"github.com/jdfalk/gcommon/pkg/organization/teams"
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

// TeamManager defines operations for team management.
type TeamManager interface {
	CreateTeam(ctx context.Context, team *teams.Team) error
	GetTeam(ctx context.Context, teamID string) (*teams.Team, error)
	UpdateTeam(ctx context.Context, team *teams.Team) error
	DeleteTeam(ctx context.Context, teamID string) error
	ListTeams(ctx context.Context) ([]*teams.Team, error)
	AddMember(ctx context.Context, teamID, userID string, role teams.Role) error
	RemoveMember(ctx context.Context, teamID, userID string) error
	UpdateMemberRole(ctx context.Context, teamID, userID string, role teams.Role) error
	Members(ctx context.Context, teamID string) ([]*teams.Member, error)
	RoleOf(ctx context.Context, teamID, userID string) (teams.Role, error)
}
