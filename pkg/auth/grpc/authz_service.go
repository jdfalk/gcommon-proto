// file: pkg/auth/grpc/authz_service.go
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f

package grpc

import (
	"context"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// AuthzService implements the AuthorizationService.
type AuthzService struct {
	provider auth.AuthorizationProvider
	proto.UnimplementedAuthorizationServiceServer
}

// NewAuthzService creates a new AuthzService.
func NewAuthzService(p auth.AuthorizationProvider) *AuthzService {
	return &AuthzService{provider: p}
}

func (s *AuthzService) Authorize(ctx context.Context, req *proto.AuthorizeRequest) (*proto.AuthorizeResponse, error) {
	return s.provider.Authorize(ctx, req)
}
