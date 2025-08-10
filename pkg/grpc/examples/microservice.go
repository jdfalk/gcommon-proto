// file: pkg/grpc/examples/microservice.go
// version: 1.0.0
// guid: a2110206-b6c9-48f2-bb62-3735714f3c9b

package examples

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/grpc/server"
	svc "github.com/jdfalk/gcommon/pkg/grpc/services"
	"google.golang.org/grpc"
)

// MicroserviceTemplate shows how a module could expose a gRPC service.
func MicroserviceTemplate(ctx context.Context, desc *grpc.ServiceDesc, impl interface{}) error {
	cfg := server.Config{Address: ":0"}
	s := cfg.Build()
	svc.RegisterConfigService(s, impl, desc)
	return s.Start(ctx)
}
