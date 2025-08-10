// file: pkg/auth/providers/ldap.go
// version: 1.0.0
// guid: f1e2d3c4-b5a6-7980-1b2c-3d4e5f6a7b8c

// Package providers implements concrete authentication providers.
package providers

import (
	"context"
	"errors"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// LDAPProvider is a placeholder for LDAP authentication.
type LDAPProvider struct{}

// NewLDAPProvider creates a new LDAP provider.
func NewLDAPProvider() *LDAPProvider { return &LDAPProvider{} }

func (p *LDAPProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	return nil, errors.New("ldap authentication not implemented")
}

func (p *LDAPProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	return nil, errors.New("ldap token validation not implemented")
}

func (p *LDAPProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	return nil, errors.New("ldap refresh not implemented")
}

func (p *LDAPProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	return nil, errors.New("ldap revoke not implemented")
}

var _ auth.AuthProvider = (*LDAPProvider)(nil)
