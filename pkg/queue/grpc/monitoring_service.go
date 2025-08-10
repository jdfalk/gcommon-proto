// file: pkg/queue/grpc/monitoring_service.go
// version: 1.0.0
// guid: c59f3164-6838-40da-bbeb-e4f0d1cf676c
//go:build queue_grpc
// +build queue_grpc

package grpc

import (
	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type MonitoringService struct {
	queuepb.UnimplementedQueueMonitoringServiceServer
	q queue.Queue
}

func NewMonitoringService(q queue.Queue) *MonitoringService {
	return &MonitoringService{q: q}
}
