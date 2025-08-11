// file: pkg/organization/grpc/hierarchy_service.go
// version: 1.1.0
// guid: 945d140a-9706-44d2-b754-2e7eb48e2ee0

// Package grpc implements hierarchy gRPC services.
package grpc

import (
	"context"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// HierarchyService implements HierarchyServiceServer.
type HierarchyService struct {
	orgpb.UnimplementedHierarchyServiceServer
}

// NewHierarchyService returns a stub HierarchyService.
// TODO: Implement full hierarchy management.
func NewHierarchyService() *HierarchyService { return &HierarchyService{} }

func (s *HierarchyService) CreateDepartment(context.Context, *orgpb.CreateDepartmentRequest) (*orgpb.CreateDepartmentResponse, error) {
	return nil, status.Error(codes.Unimplemented, "CreateDepartment not implemented")
}

func (s *HierarchyService) GetDepartment(context.Context, *orgpb.GetDepartmentRequest) (*orgpb.GetDepartmentResponse, error) {
	return nil, status.Error(codes.Unimplemented, "GetDepartment not implemented")
}

func (s *HierarchyService) UpdateDepartment(context.Context, *orgpb.UpdateDepartmentRequest) (*orgpb.UpdateDepartmentResponse, error) {
	return nil, status.Error(codes.Unimplemented, "UpdateDepartment not implemented")
}

func (s *HierarchyService) DeleteDepartment(context.Context, *orgpb.DeleteDepartmentRequest) (*orgpb.DeleteDepartmentResponse, error) {
	return nil, status.Error(codes.Unimplemented, "DeleteDepartment not implemented")
}

func (s *HierarchyService) ListDepartments(context.Context, *orgpb.ListDepartmentsRequest) (*orgpb.ListDepartmentsResponse, error) {
	return nil, status.Error(codes.Unimplemented, "ListDepartments not implemented")
}
