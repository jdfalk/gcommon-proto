// file: pkg/auth/interfaces.go
// version: 1.0.0
// guid: 94d777eb-58c3-4771-a2b3-e90201d07864

// Package auth provides authentication and authorization interfaces.
package auth

import (
	"context"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// AuthProvider defines authentication operations.
type AuthProvider interface {
	// Authenticate verifies credentials and returns access tokens.
	Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error)
	// ValidateToken checks the validity of an access token.
	ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error)
	// RefreshToken issues a new access token using a refresh token.
	RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error)
	// RevokeToken invalidates an existing token.
	RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error)
}

// AuthorizationProvider defines authorization operations.
type AuthorizationProvider interface {
	// Authorize evaluates whether a token grants access to a resource.
	Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error)
	// EvaluatePolicy evaluates policies against a request.
	EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error)
	// CreatePolicy registers a new security policy.
	CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error
}
