// file: pkg/auth/policies/abac.go
// version: 1.0.0
// guid: c9e2b1a5-7c4f-4d1b-8e27-4a1d2f9c3b5e

// Package policies implements simple authorization engines.
package policies

import (
	"context"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// ABACEngine evaluates attribute-based access control policies.
type ABACEngine struct{}

// NewABACEngine creates a new ABAC engine.
func NewABACEngine() *ABACEngine { return &ABACEngine{} }

// Authorize evaluates attributes on the request.
func (e *ABACEngine) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	attrs := req.GetContext()
	resourceAttr := attrs["resource"]
	actionAttr := attrs["action"]
	allowed := resourceAttr == req.GetResource() && actionAttr == req.GetAction()
	resp := &proto.AuthorizeResponse{}
	resp.SetAuthorized(allowed)
	if !allowed {
		resp.SetDenialReason("attribute mismatch")
	}
	return resp, nil
}

// EvaluatePolicy delegates to Authorize.
func (e *ABACEngine) EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return e.Authorize(ctx, req)
}

// CreatePolicy is a stub for interface satisfaction.
func (e *ABACEngine) CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error {
	return nil
}

var _ auth.AuthorizationProvider = (*ABACEngine)(nil)
