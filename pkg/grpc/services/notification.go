// file: pkg/grpc/services/notification.go
// version: 1.0.0
// guid: 3844d098-1eb8-4f8f-b90b-4f88458c2798

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// NotificationService defines the service interface placeholder.
type NotificationService interface{}

// RegisterNotificationService registers the notification service with the server registrar.
func RegisterNotificationService(reg server.ServiceRegistrar, srv NotificationService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
