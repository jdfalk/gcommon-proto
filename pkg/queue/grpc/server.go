// file: pkg/queue/grpc/server.go
// version: 1.0.0
// guid: 739634b6-cbd8-471b-b71b-1e2f8c4d3120
//go:build queue_grpc
// +build queue_grpc

package grpc

import (
	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	"google.golang.org/grpc"
)

// NewServer creates a gRPC server with queue services registered.
func NewServer(q queue.Queue) *grpc.Server {
	srv := grpc.NewServer()
	queuepb.RegisterQueueServiceServer(srv, NewQueueService(q))
	return srv
}
