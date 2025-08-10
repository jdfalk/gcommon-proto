// file: pkg/grpc/services/health.go
// version: 1.0.0
// guid: 395f5306-edf9-44b2-a223-832dc5d0ec0a

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// HealthService defines the service interface placeholder.
type HealthService interface{}

// RegisterHealthService registers the health service with the server registrar.
func RegisterHealthService(reg server.ServiceRegistrar, srv HealthService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
