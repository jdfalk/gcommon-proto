// file: pkg/organization/examples/multi_tenant.go
// version: 1.1.0
// guid: 51e90824-0beb-4d35-bd8d-cd3c8c8385f2

package examples

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/organization"
	"github.com/jdfalk/gcommon/pkg/organization/grpc"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// ExampleMultiTenant demonstrates tenant creation and isolation configuration.
func ExampleMultiTenant() {
	ctx := context.Background()
	services := organization.NewServices()
	tenantSvc := grpc.NewTenantService(services.Tenant)

	t := (&orgpb.Tenant_builder{Id: gproto.String("tenant1"), Name: gproto.String("Tenant One")}).Build()
	_, _ = tenantSvc.CreateTenant(ctx, (&orgpb.CreateTenantRequest_builder{Tenant: t}).Build())

	iso := (&orgpb.TenantIsolation_builder{TenantId: gproto.String("tenant1")}).Build()
	_, _ = tenantSvc.ConfigureTenantIsolation(ctx, (&orgpb.ConfigureTenantIsolationRequest_builder{TenantId: gproto.String("tenant1"), Isolation: iso}).Build())

	resp, _ := tenantSvc.GetTenantIsolation(ctx, (&orgpb.GetTenantIsolationRequest_builder{TenantId: gproto.String("tenant1")}).Build())
	fmt.Printf("has isolation: %v\n", resp.GetIsolation() != nil)
	// Output: has isolation: true
}
