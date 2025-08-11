// file: pkg/auth/logging_test.go
// version: 1.0.0
// guid: 93a82613-9462-4261-a660-7ee16fee3758

package auth

import (
	"context"
	"fmt"
	"testing"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/log/testlogger"
)

// stubAuthProvider implements AuthProvider with no-op logic.
type stubAuthProvider struct{}

func (s *stubAuthProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	return &proto.AuthenticateResponse{}, nil
}
func (s *stubAuthProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	return &proto.ValidateTokenResponse{}, nil
}
func (s *stubAuthProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	return &proto.RefreshTokenResponse{}, nil
}
func (s *stubAuthProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	return &proto.RevokeTokenResponse{}, nil
}

// stubAuthzProvider implements AuthorizationProvider with no-op logic.
type stubAuthzProvider struct{}

func (s *stubAuthzProvider) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return &proto.AuthorizeResponse{}, nil
}
func (s *stubAuthzProvider) EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return &proto.AuthorizeResponse{}, nil
}
func (s *stubAuthzProvider) CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error {
	return nil
}

func TestLoggedAuthProvider_Authenticate(t *testing.T) {
	l := testlogger.New()
	p := NewLoggedAuthProvider(&stubAuthProvider{}, l)
	_, err := p.Authenticate(context.Background(), &proto.AuthenticateRequest{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 2 {
		t.Fatalf("expected 2 log entries, got %d", len(l.Entries()))
	}
	if l.Entries()[0].Message != "auth authenticate" {
		t.Fatalf("unexpected message: %+v", l.Entries()[0])
	}
}

func TestLoggedAuthorizationProvider_Authorize(t *testing.T) {
	l := testlogger.New()
	p := NewLoggedAuthorizationProvider(&stubAuthzProvider{}, l)
	_, err := p.Authorize(context.Background(), &proto.AuthorizeRequest{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 2 {
		t.Fatalf("expected 2 log entries, got %d", len(l.Entries()))
	}
	if l.Entries()[0].Message != "auth authorize" {
		t.Fatalf("unexpected message: %+v", l.Entries()[0])
	}
}

// errAuthProvider returns errors for all methods.
type errAuthProvider struct{}

func (errAuthProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (errAuthProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (errAuthProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (errAuthProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	return nil, fmt.Errorf("fail")
}

// errAuthzProvider returns errors for all methods.
type errAuthzProvider struct{}

func (errAuthzProvider) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (errAuthzProvider) EvaluatePolicy(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (errAuthzProvider) CreatePolicy(ctx context.Context, policy *proto.SecurityPolicy) error {
	return fmt.Errorf("fail")
}

func TestLoggedAuthProvider_OtherMethods(t *testing.T) {
	l := testlogger.New()
	p := NewLoggedAuthProvider(&stubAuthProvider{}, l)
	if _, err := p.ValidateToken(context.Background(), &proto.ValidateTokenRequest{}); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if _, err := p.RefreshToken(context.Background(), &proto.RefreshTokenRequest{}); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if _, err := p.RevokeToken(context.Background(), &proto.RevokeTokenRequest{}); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 6 {
		t.Fatalf("expected 6 entries, got %d", len(l.Entries()))
	}
}

func TestLoggedAuthProvider_Errors(t *testing.T) {
	l := testlogger.New()
	p := NewLoggedAuthProvider(errAuthProvider{}, l)
	if _, err := p.Authenticate(context.Background(), &proto.AuthenticateRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := p.ValidateToken(context.Background(), &proto.ValidateTokenRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := p.RefreshToken(context.Background(), &proto.RefreshTokenRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := p.RevokeToken(context.Background(), &proto.RevokeTokenRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if len(l.Entries()) != 8 {
		t.Fatalf("expected 8 entries, got %d", len(l.Entries()))
	}
}

func TestLoggedAuthorizationProvider_OtherMethods(t *testing.T) {
	l := testlogger.New()
	p := NewLoggedAuthorizationProvider(&stubAuthzProvider{}, l)
	if _, err := p.EvaluatePolicy(context.Background(), &proto.AuthorizeRequest{}); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if err := p.CreatePolicy(context.Background(), &proto.SecurityPolicy{}); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 4 {
		t.Fatalf("expected 4 entries, got %d", len(l.Entries()))
	}
}

func TestLoggedAuthorizationProvider_Errors(t *testing.T) {
	l := testlogger.New()
	p := NewLoggedAuthorizationProvider(errAuthzProvider{}, l)
	if _, err := p.Authorize(context.Background(), &proto.AuthorizeRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := p.EvaluatePolicy(context.Background(), &proto.AuthorizeRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if err := p.CreatePolicy(context.Background(), &proto.SecurityPolicy{}); err == nil {
		t.Fatalf("expected error")
	}
	if len(l.Entries()) != 6 {
		t.Fatalf("expected 6 entries, got %d", len(l.Entries()))
	}
}
