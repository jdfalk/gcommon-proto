// file: pkg/queue/providers/redis.go
// version: 1.0.0
// guid: 17ce4e70-7beb-4eea-9b16-69139474add4

package providers

import (
	"context"
	"errors"

	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type RedisQueue struct{}

func NewRedisQueue() *RedisQueue { return &RedisQueue{} }

func (r *RedisQueue) Publish(ctx context.Context, message *queuepb.QueueMessage) error {
	return errors.New("redis provider not implemented")
}

func (r *RedisQueue) Subscribe(ctx context.Context, handler queue.MessageHandler) error {
	return errors.New("redis provider not implemented")
}

func (r *RedisQueue) CreateQueue(ctx context.Context, config *queuepb.QueueConfig) error {
	return errors.New("redis provider not implemented")
}

func (r *RedisQueue) DeleteQueue(ctx context.Context, name string) error {
	return errors.New("redis provider not implemented")
}

func (r *RedisQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	return nil, errors.New("redis provider not implemented")
}
