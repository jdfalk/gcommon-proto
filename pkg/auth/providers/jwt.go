// file: pkg/auth/providers/jwt.go
// version: 1.0.0
// guid: d1f2e3a4-b5c6-4d7e-8f90-1a2b3c4d5e6f

// Package providers implements concrete authentication providers.
package providers

import (
	"context"
	"errors"
	"time"

	"github.com/golang-jwt/jwt/v5"
	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
	"google.golang.org/protobuf/types/known/timestamppb"
)

// JWTProvider validates externally issued JWTs.
type JWTProvider struct {
	secret []byte
}

// NewJWTProvider creates a new JWT provider.
func NewJWTProvider(secret []byte) *JWTProvider { return &JWTProvider{secret: secret} }

// Authenticate is not supported for JWT provider.
func (p *JWTProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	return nil, errors.New("jwt provider does not support credential authentication")
}

// ValidateToken verifies a JWT access token.
func (p *JWTProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	claims, err := tokens.Validate(req.GetAccessToken(), p.secret)
	if err != nil {
		return &proto.ValidateTokenResponse{}, err
	}
	resp := &proto.ValidateTokenResponse{}
	resp.SetValid(true)
	if sub, ok := claims["sub"].(string); ok {
		resp.SetSubject(sub)
	}
	if exp, ok := claims["exp"].(float64); ok {
		resp.SetExpiresAt(timestamppb.New(time.Unix(int64(exp), 0)))
	}
	return resp, nil
}

// RefreshToken issues a new access token using the same claims.
func (p *JWTProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	claims, err := tokens.Parse(p.secret, req.GetRefreshToken())
	if err != nil {
		return nil, err
	}
	sub, _ := claims["sub"].(string)
	role, _ := claims["role"].(string)
	token, err := tokens.Generate(p.secret, jwt.SigningMethodHS256, sub, time.Hour, map[string]any{"role": role})
	if err != nil {
		return nil, err
	}
	refresh, err := tokens.RotateRefresh(p.secret, jwt.SigningMethodHS256, req.GetRefreshToken(), int64(time.Hour.Seconds()))
	if err != nil {
		return nil, err
	}
	resp := &proto.RefreshTokenResponse{}
	resp.SetAccessToken(token)
	resp.SetRefreshToken(refresh)
	return resp, nil
}

// RevokeToken is a no-op.
func (p *JWTProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	resp := &proto.RevokeTokenResponse{}
	resp.SetTokenId(req.GetToken())
	resp.SetTokenType("access")
	resp.SetRevokedAt(timestamppb.New(time.Now()))
	return resp, nil
}

var _ auth.AuthProvider = (*JWTProvider)(nil)
