// file: pkg/queue/grpc/queue_service.go
// version: 1.0.0
// guid: d2baf1b8-775f-4232-8a53-cc24003aa217
//go:build queue_grpc
// +build queue_grpc

package grpc

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type QueueService struct {
	queuepb.UnimplementedQueueServiceServer
	q queue.Queue
}

func NewQueueService(q queue.Queue) *QueueService {
	return &QueueService{q: q}
}

func (s *QueueService) Publish(ctx context.Context, req *queuepb.PublishRequest) (*queuepb.PublishResponse, error) {
	if err := s.q.Publish(ctx, req.GetMessage()); err != nil {
		return nil, err
	}
	return &queuepb.PublishResponse{MessageId: req.GetMessage().GetId()}, nil
}
