// file: pkg/grpc/services/metrics.go
// version: 1.0.0
// guid: f7dd3d3c-578f-4e67-8dfb-20637804d787

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// MetricsService defines the service interface placeholder.
type MetricsService interface{}

// RegisterMetricsService registers the metrics service with the server registrar.
func RegisterMetricsService(reg server.ServiceRegistrar, srv MetricsService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
