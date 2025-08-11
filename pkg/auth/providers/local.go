// file: pkg/auth/providers/local.go
// version: 1.2.0
// guid: 168d7b6e-f281-429f-a163-aec1732219ad

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

// LocalProvider authenticates users against an in-memory store.
type LocalProvider struct {
	secret    []byte
	users     map[string]string
	roles     map[string]string
	blacklist *tokens.Blacklist
}

// NewLocalProvider creates a LocalProvider.
func NewLocalProvider(secret []byte, users, roles map[string]string, bl *tokens.Blacklist) *LocalProvider {
	if bl == nil {
		bl = tokens.NewBlacklist()
	}
	return &LocalProvider{secret: secret, users: users, roles: roles, blacklist: bl}
}

// Authenticate verifies username and password credentials.
func (p *LocalProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	creds := req.GetPassword()
	if creds == nil {
		return nil, errors.New("password credentials required")
	}
	pass, ok := p.users[creds.GetUsername()]
	if !ok || pass != creds.GetPassword() {
		return nil, errors.New("invalid credentials")
	}
	role := p.roles[creds.GetUsername()]
	token, err := tokens.Generate(p.secret, jwt.SigningMethodHS256, creds.GetUsername(), time.Hour, map[string]any{"role": role})
	if err != nil {
		return nil, err
	}
	refresh, err := tokens.GenerateRefresh(p.secret, jwt.SigningMethodHS256, creds.GetUsername(), int64(time.Hour.Seconds()), map[string]any{"role": role})
	if err != nil {
		return nil, err
	}
	resp := &proto.AuthenticateResponse{}
	resp.SetAccessToken(token)
	resp.SetRefreshToken(refresh)
	resp.SetTokenType("bearer")
	resp.SetExpiresIn(int32(time.Hour.Seconds()))
	return resp, nil
}

// ValidateToken verifies a JWT access token.
func (p *LocalProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	claims, err := tokens.Validate(req.GetAccessToken(), p.secret)
	if err != nil {
		return &proto.ValidateTokenResponse{}, err
	}
	if p.blacklist.IsRevoked(req.GetAccessToken()) {
		resp := &proto.ValidateTokenResponse{}
		resp.SetValid(false)
		return resp, nil
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

// RefreshToken issues a new access token using a refresh token.
func (p *LocalProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
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

// RevokeToken is a no-op for the local provider.
func (p *LocalProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	claims, _ := tokens.Parse(p.secret, req.GetToken())
	var exp time.Time
	if v, ok := claims["exp"].(float64); ok {
		exp = time.Unix(int64(v), 0)
	} else {
		exp = time.Now().Add(time.Hour)
	}
	p.blacklist.Revoke(req.GetToken(), exp)
	resp := &proto.RevokeTokenResponse{}
	resp.SetTokenId("local")
	resp.SetTokenType("access")
	resp.SetRevokedAt(timestamppb.New(time.Now()))
	return resp, nil
}

// Ensure LocalProvider satisfies interfaces.
var _ auth.AuthProvider = (*LocalProvider)(nil)
