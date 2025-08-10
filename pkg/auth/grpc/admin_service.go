// file: pkg/auth/grpc/admin_service.go
// version: 1.0.0
// guid: 1f2e3d4c-5b6a-7980-1a2b-3c4d5e6f7a8b

package grpc

import (
	"context"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"google.golang.org/protobuf/types/known/emptypb"
)

// AdminService implements the AuthAdminService.
type AdminService struct {
	provider auth.AuthorizationProvider
	proto.UnimplementedAuthAdminServiceServer
}

// NewAdminService creates a new AdminService.
func NewAdminService(p auth.AuthorizationProvider) *AdminService { return &AdminService{provider: p} }

func (s *AdminService) CreatePolicy(ctx context.Context, req *proto.SecurityPolicy) (*emptypb.Empty, error) {
	if err := s.provider.CreatePolicy(ctx, req); err != nil {
		return nil, err
	}
	return &emptypb.Empty{}, nil
}
