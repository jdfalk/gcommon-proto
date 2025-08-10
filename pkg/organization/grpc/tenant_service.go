// file: pkg/organization/grpc/tenant_service.go
// version: 1.1.0
// guid: e6c8dd36-ef60-4f63-b41d-7e29b84b86e4

// Package grpc provides gRPC service implementations for the organization module.
package grpc

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	gproto "google.golang.org/protobuf/proto"
)

// TenantService implements the generated gRPC server for tenant operations.
type TenantService struct {
	orgpb.UnimplementedTenantServiceServer
	tm organization.TenantManager
}

// NewTenantService returns a TenantService with the provided manager.
func NewTenantService(tm organization.TenantManager) *TenantService {
	return &TenantService{tm: tm}
}

// CreateTenant handles tenant creation.
func (s *TenantService) CreateTenant(ctx context.Context, req *orgpb.CreateTenantRequest) (*orgpb.CreateTenantResponse, error) {
	t := req.GetTenant()
	if t == nil {
		return nil, status.Error(codes.InvalidArgument, "missing tenant")
	}
	if err := s.tm.CreateTenant(ctx, t); err != nil {
		return nil, err
	}
	resp := (&orgpb.CreateTenantResponse_builder{Tenant: t, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

// GetTenant retrieves a tenant by ID.
func (s *TenantService) GetTenant(ctx context.Context, req *orgpb.GetTenantRequest) (*orgpb.GetTenantResponse, error) {
	tenant, err := s.tm.GetTenant(ctx, req.GetTenantId())
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.GetTenantResponse_builder{Tenant: tenant, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

// UpdateTenant updates an existing tenant.
func (s *TenantService) UpdateTenant(ctx context.Context, req *orgpb.UpdateTenantRequest) (*orgpb.UpdateTenantResponse, error) {
	t := req.GetTenant()
	if t == nil {
		return nil, status.Error(codes.InvalidArgument, "missing tenant")
	}
	if err := s.tm.UpdateTenant(ctx, t); err != nil {
		return nil, err
	}
	resp := (&orgpb.UpdateTenantResponse_builder{Tenant: t, Success: gproto.Bool(true)}).Build()
	return resp, nil
}

// DeleteTenant removes a tenant.
func (s *TenantService) DeleteTenant(ctx context.Context, req *orgpb.DeleteTenantRequest) (*orgpb.DeleteTenantResponse, error) {
	if err := s.tm.DeleteTenant(ctx, req.GetTenantId()); err != nil {
		return nil, err
	}
	resp := (&orgpb.DeleteTenantResponse_builder{Success: gproto.Bool(true)}).Build()
	return resp, nil
}

// ListTenants returns all tenants.
func (s *TenantService) ListTenants(ctx context.Context, req *orgpb.ListTenantsRequest) (*orgpb.ListTenantsResponse, error) {
	tenants, err := s.tm.ListTenants(ctx)
	if err != nil {
		return nil, err
	}
	resp := (&orgpb.ListTenantsResponse_builder{Tenants: tenants}).Build()
	return resp, nil
}

// Remaining RPCs are unimplemented.
func (s *TenantService) ConfigureTenantIsolation(context.Context, *orgpb.ConfigureTenantIsolationRequest) (*orgpb.ConfigureTenantIsolationResponse, error) {
	return nil, status.Error(codes.Unimplemented, "not implemented")
}

func (s *TenantService) GetTenantIsolation(context.Context, *orgpb.GetTenantIsolationRequest) (*orgpb.GetTenantIsolationResponse, error) {
	return nil, status.Error(codes.Unimplemented, "not implemented")
}

func (s *TenantService) UpdateTenantQuota(context.Context, *orgpb.UpdateTenantQuotaRequest) (*orgpb.UpdateTenantQuotaResponse, error) {
	return nil, status.Error(codes.Unimplemented, "not implemented")
}

func (s *TenantService) GetTenantUsage(context.Context, *orgpb.GetTenantUsageRequest) (*orgpb.GetTenantUsageResponse, error) {
	return nil, status.Error(codes.Unimplemented, "not implemented")
}
