// file: pkg/auth/logging.go
// version: 1.0.0
// guid: 1df353d9-e33d-432b-aec7-4f7f496163ff

package auth

import (
	"context"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/log"
)

// LoggedAuthProvider wraps AuthProvider with logging.
type LoggedAuthProvider struct {
	p      AuthProvider
	logger log.Logger
}

// NewLoggedAuthProvider creates a LoggedAuthProvider.
func NewLoggedAuthProvider(p AuthProvider, l log.Logger) *LoggedAuthProvider {
	return &LoggedAuthProvider{p: p, logger: l}
}

// Authenticate logs authentication attempts.
func (l *LoggedAuthProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	l.logger.InfoContext(ctx, "auth authenticate")
	resp, err := l.p.Authenticate(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "auth authenticate failed", log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "auth authenticate success")
	return resp, nil
}

// ValidateToken logs token validations.
func (l *LoggedAuthProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	l.logger.InfoContext(ctx, "auth validate token")
	resp, err := l.p.ValidateToken(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "auth validate token failed", log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "auth validate token success")
	return resp, nil
}

// RefreshToken logs token refresh operations.
func (l *LoggedAuthProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	l.logger.InfoContext(ctx, "auth refresh token")
	resp, err := l.p.RefreshToken(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "auth refresh token failed", log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "auth refresh token success")
	return resp, nil
}

// RevokeToken logs token revocations.
func (l *LoggedAuthProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	l.logger.InfoContext(ctx, "auth revoke token")
	resp, err := l.p.RevokeToken(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "auth revoke token failed", log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "auth revoke token success")
	return resp, nil
}

// LoggedAuthorizationProvider wraps AuthorizationProvider with logging.
type LoggedAuthorizationProvider struct {
	p      AuthorizationProvider
	logger log.Logger
}

// NewLoggedAuthorizationProvider creates a LoggedAuthorizationProvider.
func NewLoggedAuthorizationProvider(p AuthorizationProvider, l log.Logger) *LoggedAuthorizationProvider {
	return &LoggedAuthorizationProvider{p: p, logger: l}
}

// Authorize logs authorization decisions.
func (l *LoggedAuthorizationProvider) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	l.logger.InfoContext(ctx, "auth authorize", log.Field{Key: "resource", Value: req.GetResource()})
	resp, err := l.p.Authorize(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "auth authorize failed", log.Field{Key: "resource", Value: req.GetResource()}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "auth authorize success", log.Field{Key: "resource", Value: req.GetResource()})
	return resp, nil
}

// EvaluatePolicy logs policy evaluations.
func (l *LoggedAuthorizationProvider) EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	l.logger.InfoContext(ctx, "auth evaluate policy", log.Field{Key: "resource", Value: req.GetResource()})
	resp, err := l.p.EvaluatePolicy(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "auth evaluate policy failed", log.Field{Key: "resource", Value: req.GetResource()}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "auth evaluate policy success", log.Field{Key: "resource", Value: req.GetResource()})
	return resp, nil
}

// CreatePolicy logs policy creation.
func (l *LoggedAuthorizationProvider) CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error {
	l.logger.InfoContext(ctx, "auth create policy")
	if err := l.p.CreatePolicy(ctx, policy); err != nil {
		l.logger.ErrorContext(ctx, "auth create policy failed", log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "auth create policy success")
	return nil
}
