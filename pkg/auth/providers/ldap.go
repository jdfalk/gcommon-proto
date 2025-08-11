// file: pkg/auth/providers/ldap.go
// version: 1.1.0
// guid: f1e2d3c4-b5a6-7980-1b2c-3d4e5f6a7b8c

// Package providers implements concrete authentication providers.
package providers

import (
	"context"
	"errors"
	"fmt"
	"time"

	"github.com/go-ldap/ldap/v3"
	"github.com/golang-jwt/jwt/v5"
	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
	"google.golang.org/protobuf/types/known/timestamppb"
)

// LDAPProvider authenticates users against an LDAP directory and issues JWTs.
type LDAPProvider struct {
	addr      string
	baseDN    string
	userAttr  string
	secret    []byte
	blacklist *tokens.Blacklist
}

// NewLDAPProvider creates a new LDAP provider.
func NewLDAPProvider(addr, baseDN, userAttr string, secret []byte, bl *tokens.Blacklist) *LDAPProvider {
	if bl == nil {
		bl = tokens.NewBlacklist()
	}
	return &LDAPProvider{addr: addr, baseDN: baseDN, userAttr: userAttr, secret: secret, blacklist: bl}
}

// Authenticate binds to the LDAP server using the provided credentials and issues tokens.
func (p *LDAPProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	creds := req.GetPassword()
	if creds == nil {
		return nil, errors.New("password credentials required")
	}
	l, err := ldap.DialURL(p.addr)
	if err != nil {
		return nil, err
	}
	defer l.Close()
	filter := fmt.Sprintf("(%s=%s)", p.userAttr, ldap.EscapeFilter(creds.GetUsername()))
	sr, err := l.Search(&ldap.SearchRequest{BaseDN: p.baseDN, Scope: ldap.ScopeWholeSubtree, Filter: filter, Attributes: []string{"dn"}})
	if err != nil || len(sr.Entries) == 0 {
		return nil, errors.New("user not found")
	}
	userDN := sr.Entries[0].DN
	if err := l.Bind(userDN, creds.GetPassword()); err != nil {
		return nil, errors.New("invalid credentials")
	}
	token, err := tokens.Generate(p.secret, jwt.SigningMethodHS256, creds.GetUsername(), time.Hour, nil)
	if err != nil {
		return nil, err
	}
	refresh, err := tokens.GenerateRefresh(p.secret, jwt.SigningMethodHS256, creds.GetUsername(), int64(time.Hour.Seconds()), nil)
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

// ValidateToken verifies the JWT token and checks revocation.
func (p *LDAPProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
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

// RefreshToken issues a new access token using the refresh token.
func (p *LDAPProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	claims, err := tokens.Parse(p.secret, req.GetRefreshToken())
	if err != nil {
		return nil, err
	}
	sub, _ := claims["sub"].(string)
	token, err := tokens.Generate(p.secret, jwt.SigningMethodHS256, sub, time.Hour, nil)
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

// RevokeToken records the token in the blacklist.
func (p *LDAPProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	claims, _ := tokens.Parse(p.secret, req.GetToken())
	var exp time.Time
	if v, ok := claims["exp"].(float64); ok {
		exp = time.Unix(int64(v), 0)
	} else {
		exp = time.Now().Add(time.Hour)
	}
	p.blacklist.Revoke(req.GetToken(), exp)
	resp := &proto.RevokeTokenResponse{}
	resp.SetTokenId(req.GetToken())
	resp.SetTokenType("access")
	resp.SetRevokedAt(timestamppb.New(time.Now()))
	return resp, nil
}

var _ auth.AuthProvider = (*LDAPProvider)(nil)
