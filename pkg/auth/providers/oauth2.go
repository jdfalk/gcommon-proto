// file: pkg/auth/providers/oauth2.go
// version: 1.0.0
// guid: 0a1b2c3d-4e5f-6071-8899-aabbccddeeff

// Package providers implements concrete authentication providers.
package providers

import (
	"context"
	"errors"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// OAuth2Provider is a placeholder for OAuth2 authentication.
type OAuth2Provider struct{}

// NewOAuth2Provider creates a new OAuth2 provider.
func NewOAuth2Provider() *OAuth2Provider { return &OAuth2Provider{} }

func (p *OAuth2Provider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	return nil, errors.New("oauth2 authentication not implemented")
}

func (p *OAuth2Provider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	return nil, errors.New("oauth2 token validation not implemented")
}

func (p *OAuth2Provider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	return nil, errors.New("oauth2 refresh not implemented")
}

func (p *OAuth2Provider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	return nil, errors.New("oauth2 revoke not implemented")
}

var _ auth.AuthProvider = (*OAuth2Provider)(nil)
