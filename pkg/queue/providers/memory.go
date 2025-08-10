// file: pkg/queue/providers/memory.go
// version: 1.0.0
// guid: 2295c946-d671-4f1f-8dd4-85f7aa6d56be

package providers

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type MemoryQueue struct {
	ch chan *queuepb.QueueMessage
}

func NewMemoryQueue(buffer int) *MemoryQueue {
	return &MemoryQueue{ch: make(chan *queuepb.QueueMessage, buffer)}
}

func (m *MemoryQueue) Publish(ctx context.Context, message *queuepb.QueueMessage) error {
	select {
	case <-ctx.Done():
		return ctx.Err()
	case m.ch <- message:
		return nil
	}
}

func (m *MemoryQueue) Subscribe(ctx context.Context, handler queue.MessageHandler) error {
	go func() {
		for {
			select {
			case <-ctx.Done():
				return
			case msg := <-m.ch:
				_ = handler(ctx, msg)
			}
		}
	}()
	return nil
}

func (m *MemoryQueue) CreateQueue(ctx context.Context, config *queuepb.QueueConfig) error {
	return nil
}

func (m *MemoryQueue) DeleteQueue(ctx context.Context, name string) error {
	return nil
}

func (m *MemoryQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	return &queuepb.QueueInfo{}, nil
}
