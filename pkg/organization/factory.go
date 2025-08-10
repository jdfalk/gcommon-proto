// file: pkg/organization/factory.go
// version: 1.0.0
// guid: 2b80b967-fa14-4400-8c4e-cd7d63efd1bd

// Package organization exposes constructors for service implementations.
package organization

import (
	"github.com/jdfalk/gcommon/pkg/organization/hierarchy"
	"github.com/jdfalk/gcommon/pkg/organization/tenant"
)

// Services groups organization service implementations.
type Services struct {
	Tenant    TenantManager
	Hierarchy HierarchyManager
}

// NewServices returns initialized organization service implementations.
func NewServices() *Services {
	return &Services{
		Tenant:    tenant.NewManager(),
		Hierarchy: hierarchy.NewTree(),
	}
}
