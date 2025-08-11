// file: pkg/organization/grpc/tenant_service.go
// version: 1.2.0
// guid: e6c8dd36-ef60-4f63-b41d-7e29b84b86e4

// Package grpc provides gRPC service implementations for the organization module.
package grpc

import (
	"context"
	"sync"

	commonpb "github.com/jdfalk/gcommon/pkg/common/proto"
	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	gproto "google.golang.org/protobuf/proto"
)

// TenantService implements the generated gRPC server for tenant operations.
type TenantService struct {
	orgpb.UnimplementedTenantServiceServer
	tm         organization.TenantManager
	mu         sync.RWMutex
	isolations map[string]*orgpb.TenantIsolation
	quotas     map[string]*orgpb.TenantQuota
	usage      map[string][]*commonpb.KeyValue
}

// NewTenantService returns a TenantService with the provided manager.
func NewTenantService(tm organization.TenantManager) *TenantService {
	return &TenantService{
		tm:         tm,
		isolations: make(map[string]*orgpb.TenantIsolation),
		quotas:     make(map[string]*orgpb.TenantQuota),
		usage:      make(map[string][]*commonpb.KeyValue),
	}
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

// ConfigureTenantIsolation sets isolation configuration for a tenant.
func (s *TenantService) ConfigureTenantIsolation(ctx context.Context, req *orgpb.ConfigureTenantIsolationRequest) (*orgpb.ConfigureTenantIsolationResponse, error) {
	iso := req.GetIsolation()
	id := req.GetTenantId()
	if id == "" || iso == nil {
		return nil, status.Error(codes.InvalidArgument, "missing tenant or isolation")
	}
	s.mu.Lock()
	s.isolations[id] = iso
	s.mu.Unlock()
	resp := (&orgpb.ConfigureTenantIsolationResponse_builder{Success: gproto.Bool(true), Isolation: iso}).Build()
	return resp, nil
}

// GetTenantIsolation retrieves stored isolation configuration.
func (s *TenantService) GetTenantIsolation(ctx context.Context, req *orgpb.GetTenantIsolationRequest) (*orgpb.GetTenantIsolationResponse, error) {
	id := req.GetTenantId()
	s.mu.RLock()
	iso, ok := s.isolations[id]
	s.mu.RUnlock()
	if !ok {
		return nil, status.Error(codes.NotFound, "isolation not found")
	}
	resp := (&orgpb.GetTenantIsolationResponse_builder{Success: gproto.Bool(true), Isolation: iso}).Build()
	return resp, nil
}

// UpdateTenantQuota stores quota configuration.
func (s *TenantService) UpdateTenantQuota(ctx context.Context, req *orgpb.UpdateTenantQuotaRequest) (*orgpb.UpdateTenantQuotaResponse, error) {
	id := req.GetTenantId()
	quota := req.GetQuota()
	if id == "" || quota == nil {
		return nil, status.Error(codes.InvalidArgument, "missing tenant or quota")
	}
	s.mu.Lock()
	s.quotas[id] = quota
	s.mu.Unlock()
	resp := (&orgpb.UpdateTenantQuotaResponse_builder{Success: gproto.Bool(true), Quota: quota}).Build()
	return resp, nil
}

// GetTenantUsage returns usage statistics for a tenant.
func (s *TenantService) GetTenantUsage(ctx context.Context, req *orgpb.GetTenantUsageRequest) (*orgpb.GetTenantUsageResponse, error) {
	id := req.GetTenantId()
	s.mu.RLock()
	stats, ok := s.usage[id]
	s.mu.RUnlock()
	if !ok {
		stats = []*commonpb.KeyValue{}
	}
	resp := (&orgpb.GetTenantUsageResponse_builder{Success: gproto.Bool(true), UsageStats: stats}).Build()
	return resp, nil
}
