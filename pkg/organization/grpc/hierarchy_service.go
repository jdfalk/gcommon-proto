// file: pkg/organization/grpc/hierarchy_service.go
// version: 1.2.0
// guid: 945d140a-9706-44d2-b754-2e7eb48e2ee0

// Package grpc implements hierarchy gRPC services.
package grpc

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	gproto "google.golang.org/protobuf/proto"
)

// HierarchyService implements HierarchyServiceServer.
type HierarchyService struct {
	orgpb.UnimplementedHierarchyServiceServer
	dm organization.DepartmentManager
}

// NewHierarchyService returns a HierarchyService using the provided manager.
func NewHierarchyService(dm organization.DepartmentManager) *HierarchyService {
	return &HierarchyService{dm: dm}
}

func (s *HierarchyService) CreateDepartment(ctx context.Context, req *orgpb.CreateDepartmentRequest) (*orgpb.CreateDepartmentResponse, error) {
	d := req.GetDepartment()
	if d == nil {
		return nil, status.Error(codes.InvalidArgument, "missing department")
	}
	if err := s.dm.CreateDepartment(ctx, d); err != nil {
		return nil, err
	}
	resp := (&orgpb.CreateDepartmentResponse_builder{Department: d, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *HierarchyService) GetDepartment(ctx context.Context, req *orgpb.GetDepartmentRequest) (*orgpb.GetDepartmentResponse, error) {
	d, err := s.dm.GetDepartment(ctx, req.GetDepartmentId())
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.GetDepartmentResponse_builder{Department: d, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *HierarchyService) UpdateDepartment(ctx context.Context, req *orgpb.UpdateDepartmentRequest) (*orgpb.UpdateDepartmentResponse, error) {
	d := req.GetDepartment()
	if d == nil {
		return nil, status.Error(codes.InvalidArgument, "missing department")
	}
	if err := s.dm.UpdateDepartment(ctx, d); err != nil {
		return nil, err
	}
	resp := (&orgpb.UpdateDepartmentResponse_builder{Department: d, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *HierarchyService) DeleteDepartment(ctx context.Context, req *orgpb.DeleteDepartmentRequest) (*orgpb.DeleteDepartmentResponse, error) {
	if err := s.dm.DeleteDepartment(ctx, req.GetDepartmentId()); err != nil {
		return nil, err
	}
	resp := (&orgpb.DeleteDepartmentResponse_builder{Success: gproto.Bool(true)}).Build()
	return resp, nil
}

func (s *HierarchyService) ListDepartments(ctx context.Context, req *orgpb.ListDepartmentsRequest) (*orgpb.ListDepartmentsResponse, error) {
	list, err := s.dm.ListDepartments(ctx, req.GetOrganizationId())
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.ListDepartmentsResponse_builder{Departments: list, Success: gproto.Bool(true)}).Build()
	return resp, nil
}
