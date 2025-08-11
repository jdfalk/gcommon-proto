// file: pkg/queue/grpc/monitoring_service.go
// version: 1.1.0
// guid: c59f3164-6838-40da-bbeb-e4f0d1cf676c
//go:build queue_grpc
// +build queue_grpc

package grpc

import (
	"context"
	"time"

	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	"google.golang.org/grpc/metadata"
)

type MonitoringService struct {
	queuepb.UnimplementedQueueMonitoringServiceServer
	q queue.Queue
}

func NewMonitoringService(q queue.Queue) *MonitoringService {
	return &MonitoringService{q: q}
}

// GetClusterInfo returns placeholder cluster information. Real implementations
// would gather metrics from all queue nodes.
func (s *MonitoringService) GetClusterInfo(context.Context, *queuepb.GetClusterInfoRequest) (*queuepb.GetClusterInfoResponse, error) {
	return &queuepb.GetClusterInfoResponse{ClusterName: "in-memory", NodeCount: 1}, nil
}

// GetQueueHealth returns basic health status based on queue length.
func (s *MonitoringService) GetQueueHealth(ctx context.Context, req *queuepb.GetQueueHealthRequest) (*queuepb.GetQueueHealthResponse, error) {
	info, err := s.q.GetQueueInfo(ctx, req.GetQueueName())
	if err != nil {
		return nil, err
	}
	status := queuepb.HealthStatus_HEALTH_STATUS_HEALTHY
	if info.GetMessageCount() > 1000 {
		status = queuepb.HealthStatus_HEALTH_STATUS_WARNING
	}
	return &queuepb.GetQueueHealthResponse{Status: status}, nil
}

// GetQueueStats proxies queue information from the provider.
func (s *MonitoringService) GetQueueStats(ctx context.Context, req *queuepb.GetQueueStatsRequest) (*queuepb.QueueStatsResponse, error) {
	info, err := s.q.GetQueueInfo(ctx, req.GetQueueName())
	if err != nil {
		return nil, err
	}
	return &queuepb.QueueStatsResponse{Info: info}, nil
}

// StreamMetrics streams periodic metrics to the client until the context is
// cancelled. This is a basic example that sends queue length every second.
func (s *MonitoringService) StreamMetrics(req *queuepb.StreamMetricsRequest, srv queuepb.QueueMonitoringService_StreamMetricsServer) error {
	ctx := srv.Context()
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()

	for {
		select {
		case <-ctx.Done():
			return ctx.Err()
		case t := <-ticker.C:
			info, err := s.q.GetQueueInfo(ctx, req.GetQueueName())
			if err != nil {
				return err
			}
			md, _ := metadata.FromIncomingContext(ctx)
			_ = md // currently unused
			if err := srv.Send(&queuepb.MetricsEvent{Timestamp: t.Unix(), PendingMessages: info.GetMessageCount()}); err != nil {
				return err
			}
		}
	}
}
