// file: pkg/auth/policies/policy_engine.go
// version: 1.0.0
// guid: 4e1f2a3b-6c7d-8e9f-0a1b-2c3d4e5f6a7b

// Package policies implements simple authorization engines.
package policies

import (
	"context"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// PolicyEngine coordinates multiple authorization providers.
type PolicyEngine struct {
	rbac auth.AuthorizationProvider
	abac auth.AuthorizationProvider
}

// NewPolicyEngine creates a new policy engine.
func NewPolicyEngine(rbac, abac auth.AuthorizationProvider) *PolicyEngine {
	return &PolicyEngine{rbac: rbac, abac: abac}
}

// Authorize checks RBAC first then ABAC policies.
func (e *PolicyEngine) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	if e.rbac != nil {
		if resp, err := e.rbac.Authorize(ctx, req); err == nil && resp.GetAuthorized() {
			return resp, nil
		}
	}
	if e.abac != nil {
		return e.abac.Authorize(ctx, req)
	}
	resp := &proto.AuthorizeResponse{}
	resp.SetAuthorized(false)
	resp.SetDenialReason("no policy matched")
	return resp, nil
}

// EvaluatePolicy delegates to Authorize.
func (e *PolicyEngine) EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return e.Authorize(ctx, req)
}

// CreatePolicy is a stub.
func (e *PolicyEngine) CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error {
	return nil
}

var _ auth.AuthorizationProvider = (*PolicyEngine)(nil)
