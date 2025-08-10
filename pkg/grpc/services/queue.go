// file: pkg/grpc/services/queue.go
// version: 1.0.0
// guid: 518331ab-1310-486e-b9ab-7a8b1143f000

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// QueueService defines the service interface placeholder.
type QueueService interface{}

// RegisterQueueService registers the queue service with the server registrar.
func RegisterQueueService(reg server.ServiceRegistrar, srv QueueService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
