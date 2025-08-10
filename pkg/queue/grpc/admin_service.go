// file: pkg/queue/grpc/admin_service.go
// version: 1.0.0
// guid: cc47b2b4-b308-48bc-8784-b08495f90dba
//go:build queue_grpc
// +build queue_grpc

package grpc

import (
	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type AdminService struct {
	queuepb.UnimplementedQueueAdminServiceServer
	q queue.Queue
}

func NewAdminService(q queue.Queue) *AdminService {
	return &AdminService{q: q}
}
