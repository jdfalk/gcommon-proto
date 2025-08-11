// file: pkg/auth/providers/oauth2.go
// version: 1.1.0
// guid: 0a1b2c3d-4e5f-6071-8899-aabbccddeeff

// Package providers implements concrete authentication providers.
package providers

import (
	"context"
	"encoding/json"
	"errors"
	"net/http"
	"net/url"
	"strings"
	"time"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
	"golang.org/x/oauth2"
	"google.golang.org/protobuf/types/known/timestamppb"
)

// OAuth2Provider implements generic OAuth2 authentication flows.
type OAuth2Provider struct {
	config        *oauth2.Config
	httpClient    *http.Client
	introspectURL string
	revokeURL     string
	blacklist     *tokens.Blacklist
}

// NewOAuth2Provider creates a new OAuth2 provider.
func NewOAuth2Provider(cfg *oauth2.Config, client *http.Client, introspectURL, revokeURL string, bl *tokens.Blacklist) *OAuth2Provider {
	if client == nil {
		client = http.DefaultClient
	}
	if bl == nil {
		bl = tokens.NewBlacklist()
	}
	return &OAuth2Provider{config: cfg, httpClient: client, introspectURL: introspectURL, revokeURL: revokeURL, blacklist: bl}
}

// Authenticate exchanges an authorization code for tokens.
func (p *OAuth2Provider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	creds := req.GetOauth2()
	if creds == nil {
		return nil, errors.New("oauth2 credentials required")
	}
	ctx = context.WithValue(ctx, oauth2.HTTPClient, p.httpClient)
	tok, err := p.config.Exchange(ctx, creds.GetCode())
	if err != nil {
		return nil, err
	}
	resp := &proto.AuthenticateResponse{}
	resp.SetAccessToken(tok.AccessToken)
	resp.SetTokenType(tok.TokenType)
	if tok.RefreshToken != "" {
		resp.SetRefreshToken(tok.RefreshToken)
	}
	if !tok.Expiry.IsZero() {
		resp.SetExpiresIn(int32(time.Until(tok.Expiry).Seconds()))
	}
	return resp, nil
}

// ValidateToken calls the introspection endpoint when available.
func (p *OAuth2Provider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	if p.blacklist.IsRevoked(req.GetAccessToken()) {
		resp := &proto.ValidateTokenResponse{}
		resp.SetValid(false)
		return resp, nil
	}
	if p.introspectURL == "" {
		resp := &proto.ValidateTokenResponse{}
		resp.SetValid(false)
		return resp, nil
	}
	form := url.Values{}
	form.Set("token", req.GetAccessToken())
	httpReq, err := http.NewRequestWithContext(ctx, http.MethodPost, p.introspectURL, strings.NewReader(form.Encode()))
	if err != nil {
		return nil, err
	}
	httpReq.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	res, err := p.httpClient.Do(httpReq)
	if err != nil {
		return nil, err
	}
	defer res.Body.Close()
	var data struct {
		Active bool   `json:"active"`
		Sub    string `json:"sub"`
		Exp    int64  `json:"exp"`
	}
	if err := json.NewDecoder(res.Body).Decode(&data); err != nil {
		return nil, err
	}
	resp := &proto.ValidateTokenResponse{}
	if data.Active {
		resp.SetValid(true)
		resp.SetSubject(data.Sub)
		if data.Exp > 0 {
			resp.SetExpiresAt(timestamppb.New(time.Unix(data.Exp, 0)))
		}
	} else {
		resp.SetValid(false)
	}
	return resp, nil
}

// RefreshToken uses the refresh token to obtain a new access token.
func (p *OAuth2Provider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	ts := p.config.TokenSource(ctx, &oauth2.Token{RefreshToken: req.GetRefreshToken()})
	tok, err := ts.Token()
	if err != nil {
		return nil, err
	}
	resp := &proto.RefreshTokenResponse{}
	resp.SetAccessToken(tok.AccessToken)
	if tok.RefreshToken != "" {
		resp.SetRefreshToken(tok.RefreshToken)
	}
	return resp, nil
}

// RevokeToken calls the revocation endpoint and blacklists the token locally.
func (p *OAuth2Provider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	if p.revokeURL != "" {
		form := url.Values{}
		form.Set("token", req.GetToken())
		httpReq, _ := http.NewRequestWithContext(ctx, http.MethodPost, p.revokeURL, strings.NewReader(form.Encode()))
		httpReq.Header.Set("Content-Type", "application/x-www-form-urlencoded")
		p.httpClient.Do(httpReq)
	}
	p.blacklist.Revoke(req.GetToken(), time.Now().Add(time.Hour))
	resp := &proto.RevokeTokenResponse{}
	resp.SetTokenId(req.GetToken())
	resp.SetTokenType("access")
	resp.SetRevokedAt(timestamppb.New(time.Now()))
	return resp, nil
}

var _ auth.AuthProvider = (*OAuth2Provider)(nil)
