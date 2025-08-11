// file: pkg/queue/grpc/admin_service.go
// version: 1.1.0
// guid: cc47b2b4-b308-48bc-8784-b08495f90dba
//go:build queue_grpc
// +build queue_grpc

package grpc

import (
	"context"
	"errors"

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

// CreateQueue delegates to the underlying Queue implementation to create a new
// queue with the provided configuration.
func (s *AdminService) CreateQueue(ctx context.Context, req *queuepb.CreateQueueRequest) (*queuepb.CreateQueueResponse, error) {
	if req.GetConfig() == nil {
		return nil, errors.New("queue config required")
	}
	if err := s.q.CreateQueue(ctx, req.GetConfig()); err != nil {
		return nil, err
	}
	resp := &queuepb.CreateQueueResponse{}
	resp.SetQueue(req.GetConfig())
	return resp, nil
}

// DeleteTopic removes a queue. The proto uses DeleteTopic for historical
// reasons though it maps directly to Queue.DeleteQueue in the provider.
func (s *AdminService) DeleteTopic(ctx context.Context, req *queuepb.DeleteTopicRequest) (*queuepb.DeleteTopicResponse, error) {
	if err := s.q.DeleteQueue(ctx, req.GetName()); err != nil {
		return nil, err
	}
	return &queuepb.DeleteTopicResponse{}, nil
}

// GetQueueInfo returns statistics about a queue from the provider.
func (s *AdminService) GetQueueInfo(ctx context.Context, req *queuepb.GetQueueInfoRequest) (*queuepb.GetQueueInfoResponse, error) {
	info, err := s.q.GetQueueInfo(ctx, req.GetName())
	if err != nil {
		return nil, err
	}
	resp := &queuepb.GetQueueInfoResponse{}
	resp.SetInfo(info)
	return resp, nil
}

// PauseQueue is not supported by the basic queue implementations and returns
// an unimplemented error.
func (s *AdminService) PauseQueue(context.Context, *queuepb.PauseQueueRequest) (*queuepb.PauseQueueResponse, error) {
	return nil, errors.New("pause queue not implemented")
}

// ResumeQueue is not supported by the basic queue implementations and returns
// an unimplemented error.
func (s *AdminService) ResumeQueue(context.Context, *queuepb.ResumeQueueRequest) (*queuepb.ResumeQueueResponse, error) {
	return nil, errors.New("resume queue not implemented")
}

// PurgeQueue removes all messages from a queue if supported. For the in-memory
// and Redis implementations this equates to deleting and recreating the queue.
func (s *AdminService) PurgeQueue(ctx context.Context, req *queuepb.PurgeRequest) (*queuepb.PurgeResponse, error) {
	name := req.GetQueueName()
	info, err := s.q.GetQueueInfo(ctx, name)
	if err != nil {
		return nil, err
	}
	if err := s.q.DeleteQueue(ctx, name); err != nil {
		return nil, err
	}
	cfg := &queuepb.QueueConfig{}
	cfg.SetName(name)
	if err := s.q.CreateQueue(ctx, cfg); err != nil {
		return nil, err
	}
	resp := &queuepb.PurgeResponse{}
	resp.SetSuccess(true)
	resp.SetMessagesPurged(info.GetMessageCount())
	return resp, nil
}

// ResetQueueStats resets the statistics for a queue. For in-memory and Redis
// implementations this is equivalent to purging the queue.
func (s *AdminService) ResetQueueStats(ctx context.Context, req *queuepb.ResetQueueStatsRequest) (*queuepb.ResetQueueStatsResponse, error) {
	if _, err := s.PurgeQueue(ctx, &queuepb.PurgeRequest{QueueName: req.GetQueueName()}); err != nil {
		return nil, err
	}
	return &queuepb.ResetQueueStatsResponse{}, nil
}
