// file: pkg/auth/grpc/auth_service_test.go
// version: 1.0.0
// guid: 5c4d3e2f-1a0b-9c8d-7e6f-5a4b3c2d1e0f

package grpc

import (
	"context"
	"testing"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

type stubAuthProvider struct{}

func (stubAuthProvider) Authenticate(ctx context.Context, req *proto.AuthenticateRequest) (*proto.AuthenticateResponse, error) {
	resp := &proto.AuthenticateResponse{}
	resp.SetAccessToken("tok")
	return resp, nil
}
func (stubAuthProvider) ValidateToken(ctx context.Context, req *proto.ValidateTokenRequest) (*proto.ValidateTokenResponse, error) {
	resp := &proto.ValidateTokenResponse{}
	resp.SetValid(true)
	return resp, nil
}
func (stubAuthProvider) RefreshToken(ctx context.Context, req *proto.RefreshTokenRequest) (*proto.RefreshTokenResponse, error) {
	return &proto.RefreshTokenResponse{}, nil
}
func (stubAuthProvider) RevokeToken(ctx context.Context, req *proto.RevokeTokenRequest) (*proto.RevokeTokenResponse, error) {
	return &proto.RevokeTokenResponse{}, nil
}

var _ auth.AuthProvider = (*stubAuthProvider)(nil)

func TestAuthServiceAuthenticate(t *testing.T) {
	s := NewAuthService(stubAuthProvider{})
	resp, err := s.Authenticate(context.Background(), &proto.AuthenticateRequest{})
	if err != nil {
		t.Fatalf("authenticate: %v", err)
	}
	if resp.GetAccessToken() != "tok" {
		t.Fatalf("unexpected token")
	}
}
