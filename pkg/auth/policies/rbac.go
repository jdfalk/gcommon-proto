// file: pkg/auth/policies/rbac.go
// version: 1.1.0
// guid: 6728f648-7cdc-48ee-9483-7e916f53b185

// Package policies implements simple authorization engines.
package policies

import (
	"context"
	"sync"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

// RBACEngine provides role-based access control.
type RBACEngine struct {
	secret []byte
	mu     sync.RWMutex
	perms  map[string]map[string]map[string]bool
}

// NewRBACEngine creates a new RBAC engine.
func NewRBACEngine(secret []byte) *RBACEngine {
	return &RBACEngine{secret: secret, perms: make(map[string]map[string]map[string]bool)}
}

// Grant adds a permission for a role.
func (e *RBACEngine) Grant(role, resource, action string) {
	e.mu.Lock()
	defer e.mu.Unlock()
	if e.perms[role] == nil {
		e.perms[role] = make(map[string]map[string]bool)
	}
	if e.perms[role][resource] == nil {
		e.perms[role][resource] = make(map[string]bool)
	}
	e.perms[role][resource][action] = true
}

// Authorize checks if the token grants the requested action.
func (e *RBACEngine) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	claims, err := tokens.Parse(e.secret, req.GetToken())
	if err != nil {
		resp := &proto.AuthorizeResponse{}
		resp.SetAuthorized(false)
		resp.SetDenialReason("invalid token")
		return resp, nil
	}
	role, _ := claims["role"].(string)
	e.mu.RLock()
	allowed := e.perms[role][req.GetResource()][req.GetAction()]
	e.mu.RUnlock()
	resp := &proto.AuthorizeResponse{}
	resp.SetAuthorized(allowed)
	if allowed {
		resp.SetPermissions([]string{req.GetAction()})
	} else {
		resp.SetDenialReason("forbidden")
	}
	return resp, nil
}

// EvaluatePolicy delegates to Authorize.
func (e *RBACEngine) EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return e.Authorize(ctx, req)
}

// CreatePolicy is a stub for interface satisfaction.
func (e *RBACEngine) CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error {
	return nil
}

// Ensure RBACEngine satisfies interfaces.
var _ auth.AuthorizationProvider = (*RBACEngine)(nil)
