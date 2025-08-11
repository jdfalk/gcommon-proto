// file: pkg/organization/grpc/tenant_service_test.go
// version: 1.0.0
// guid: 5b6c7d8e-9f01-4a2b-b3c4-d5e6f708192a

package grpc

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/organization"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

func TestTenantIsolation(t *testing.T) {
	ctx := context.Background()
	tm := organization.NewServices().Tenant
	svc := NewTenantService(tm)
	tenant := (&orgpb.Tenant_builder{Id: gproto.String("t1"), Name: gproto.String("T")}).Build()
	_, err := svc.CreateTenant(ctx, (&orgpb.CreateTenantRequest_builder{Tenant: tenant}).Build())
	if err != nil {
		t.Fatalf("create: %v", err)
	}

	iso := (&orgpb.TenantIsolation_builder{TenantId: gproto.String("t1")}).Build()
	_, err = svc.ConfigureTenantIsolation(ctx, (&orgpb.ConfigureTenantIsolationRequest_builder{TenantId: gproto.String("t1"), Isolation: iso}).Build())
	if err != nil {
		t.Fatalf("configure: %v", err)
	}

	resp, err := svc.GetTenantIsolation(ctx, (&orgpb.GetTenantIsolationRequest_builder{TenantId: gproto.String("t1")}).Build())
	if err != nil || resp.GetIsolation() == nil {
		t.Fatalf("get isolation: %v", err)
	}
}

func TestTenantQuota(t *testing.T) {
	ctx := context.Background()
	tm := organization.NewServices().Tenant
	svc := NewTenantService(tm)
	tenant := (&orgpb.Tenant_builder{Id: gproto.String("t2"), Name: gproto.String("T2")}).Build()
	_, _ = svc.CreateTenant(ctx, (&orgpb.CreateTenantRequest_builder{Tenant: tenant}).Build())

	quota := (&orgpb.TenantQuota_builder{TenantId: gproto.String("t2"), MaxUsers: gproto.Int32(10)}).Build()
	_, err := svc.UpdateTenantQuota(ctx, (&orgpb.UpdateTenantQuotaRequest_builder{TenantId: gproto.String("t2"), Quota: quota}).Build())
	if err != nil {
		t.Fatalf("update quota: %v", err)
	}

	resp, err := svc.GetTenantUsage(ctx, (&orgpb.GetTenantUsageRequest_builder{TenantId: gproto.String("t2")}).Build())
	if err != nil {
		t.Fatalf("get usage: %v", err)
	}
	if len(resp.GetUsageStats()) != 0 {
		t.Fatalf("expected empty usage stats")
	}
}

func TestListTenants(t *testing.T) {
	ctx := context.Background()
	svc := NewTenantService(organization.NewServices().Tenant)
	t1 := (&orgpb.Tenant_builder{Id: gproto.String("lt1"), Name: gproto.String("L1")}).Build()
	t2 := (&orgpb.Tenant_builder{Id: gproto.String("lt2"), Name: gproto.String("L2")}).Build()
	_, _ = svc.CreateTenant(ctx, (&orgpb.CreateTenantRequest_builder{Tenant: t1}).Build())
	_, _ = svc.CreateTenant(ctx, (&orgpb.CreateTenantRequest_builder{Tenant: t2}).Build())
	resp, err := svc.ListTenants(ctx, (&orgpb.ListTenantsRequest_builder{}).Build())
	if err != nil || len(resp.GetTenants()) != 2 {
		t.Fatalf("list tenants: %v len=%d", err, len(resp.GetTenants()))
	}
}
