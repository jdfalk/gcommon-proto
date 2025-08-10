// file: pkg/notification/grpc/server.go
// version: 1.0.0
// guid: cccccccc-dddd-eeee-ffff-000000000000

package grpcsvc

import (
	"google.golang.org/grpc"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// NewServer creates a gRPC server with notification services registered.
func NewServer(tracker notification.DeliveryTracker) *grpc.Server {
	srv := grpc.NewServer()
	pb.RegisterNotificationServiceServer(srv, NewService(tracker))
	return srv
}
