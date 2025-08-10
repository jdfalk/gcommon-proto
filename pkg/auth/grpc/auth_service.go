// file: pkg/auth/grpc/auth_service.go
// version: 1.0.0
// guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d

// Package grpc provides gRPC service implementations for auth.
package grpc

import (
	"context"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// AuthService implements the gRPC AuthService.
type AuthService struct {
	provider auth.AuthProvider
	proto.UnimplementedAuthServiceServer
}

// NewAuthService creates a new AuthService.
func NewAuthService(p auth.AuthProvider) *AuthService { return &AuthService{provider: p} }

func (s *AuthService) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	return s.provider.Authenticate(ctx, req)
}

func (s *AuthService) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	return s.provider.ValidateToken(ctx, req)
}

func (s *AuthService) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	return s.provider.RefreshToken(ctx, req)
}

func (s *AuthService) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	return s.provider.RevokeToken(ctx, req)
}
