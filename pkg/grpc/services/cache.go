// file: pkg/grpc/services/cache.go
// version: 1.0.0
// guid: e21ba8d6-6139-4b87-b6a5-fb37481f50b3

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// CacheService defines the service interface placeholder.
type CacheService interface{}

// RegisterCacheService registers the cache service with the server registrar.
func RegisterCacheService(reg server.ServiceRegistrar, srv CacheService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
