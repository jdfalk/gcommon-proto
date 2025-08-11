// file: pkg/organization/grpc/org_service.go
// version: 1.2.0
// guid: 9fe51dbb-bbe9-40d4-9d9c-dff684494e8d

// Package grpc provides OrganizationService gRPC server implementations.
package grpc

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	gproto "google.golang.org/protobuf/proto"
)

// OrganizationService implements OrganizationServiceServer.
type OrganizationService struct {
	orgpb.UnimplementedOrganizationServiceServer
	om organization.OrganizationManager
}

// NewOrganizationService returns an OrganizationService using the provided manager.
func NewOrganizationService(om organization.OrganizationManager) *OrganizationService {
	return &OrganizationService{om: om}
}

func (s *OrganizationService) CreateOrganization(ctx context.Context, req *orgpb.CreateOrganizationRequest) (*orgpb.CreateOrganizationResponse, error) {
	org := req.GetOrganization()
	if org == nil {
		return nil, status.Error(codes.InvalidArgument, "missing organization")
	}
	if err := s.om.CreateOrganization(ctx, org); err != nil {
		return nil, err
	}
	resp := (&orgpb.CreateOrganizationResponse_builder{Organization: org, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) GetOrganization(ctx context.Context, req *orgpb.GetOrganizationRequest) (*orgpb.GetOrganizationResponse, error) {
	org, err := s.om.GetOrganization(ctx, req.GetOrganizationId())
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.GetOrganizationResponse_builder{Organization: org, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) UpdateOrganization(ctx context.Context, req *orgpb.UpdateOrganizationRequest) (*orgpb.UpdateOrganizationResponse, error) {
	org := req.GetOrganization()
	if org == nil {
		return nil, status.Error(codes.InvalidArgument, "missing organization")
	}
	if err := s.om.UpdateOrganization(ctx, org); err != nil {
		return nil, err
	}
	resp := (&orgpb.UpdateOrganizationResponse_builder{Organization: org, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) DeleteOrganization(ctx context.Context, req *orgpb.DeleteOrganizationRequest) (*orgpb.DeleteOrganizationResponse, error) {
	if err := s.om.DeleteOrganization(ctx, req.GetOrganizationId()); err != nil {
		return nil, err
	}
	resp := (&orgpb.DeleteOrganizationResponse_builder{Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) ListOrganizations(ctx context.Context, req *orgpb.ListOrganizationsRequest) (*orgpb.ListOrganizationsResponse, error) {
	orgs, err := s.om.ListOrganizations(ctx)
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.ListOrganizationsResponse_builder{Organizations: orgs, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) AddMember(ctx context.Context, req *orgpb.AddMemberRequest) (*orgpb.AddMemberResponse, error) {
	m := req.GetMember()
	if m == nil {
		return nil, status.Error(codes.InvalidArgument, "missing member")
	}
	if err := s.om.AddMember(ctx, req.GetOrganizationId(), m); err != nil {
		return nil, err
	}
	resp := (&orgpb.AddMemberResponse_builder{Member: m, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) RemoveMember(ctx context.Context, req *orgpb.RemoveMemberRequest) (*orgpb.RemoveMemberResponse, error) {
	if err := s.om.RemoveMember(ctx, req.GetOrganizationId(), req.GetMemberId()); err != nil {
		return nil, err
	}
	resp := (&orgpb.RemoveMemberResponse_builder{Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) UpdateMember(ctx context.Context, req *orgpb.UpdateMemberRequest) (*orgpb.UpdateMemberResponse, error) {
	m := req.GetMember()
	if m == nil {
		return nil, status.Error(codes.InvalidArgument, "missing member")
	}
	if err := s.om.UpdateMember(ctx, req.GetOrganizationId(), m); err != nil {
		return nil, err
	}
	resp := (&orgpb.UpdateMemberResponse_builder{Member: m, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) ListMembers(ctx context.Context, req *orgpb.ListMembersRequest) (*orgpb.ListMembersResponse, error) {
	members, err := s.om.ListMembers(ctx, req.GetOrganizationId())
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.ListMembersResponse_builder{Members: members, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) GetOrganizationSettings(ctx context.Context, req *orgpb.GetOrganizationSettingsRequest) (*orgpb.GetOrganizationSettingsResponse, error) {
	settings, err := s.om.GetSettings(ctx, req.GetOrganizationId())
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.GetOrganizationSettingsResponse_builder{Settings: settings, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *OrganizationService) UpdateOrganizationSettings(ctx context.Context, req *orgpb.UpdateOrganizationSettingsRequest) (*orgpb.UpdateOrganizationSettingsResponse, error) {
	settings := req.GetSettings()
	if settings == nil {
		return nil, status.Error(codes.InvalidArgument, "missing settings")
	}
	if err := s.om.UpdateSettings(ctx, settings); err != nil {
		return nil, err
	}
	resp := (&orgpb.UpdateOrganizationSettingsResponse_builder{Settings: settings, Success: gproto.Bool(true)}).Build()
	return resp, nil
}
