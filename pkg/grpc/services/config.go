// file: pkg/grpc/services/config.go
// version: 1.0.0
// guid: 97724ed0-22e2-4cb2-847c-b805c1bf1a26

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// ConfigService defines the service interface placeholder.
type ConfigService interface{}

// RegisterConfigService registers the config service with the server registrar.
func RegisterConfigService(reg server.ServiceRegistrar, srv ConfigService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
