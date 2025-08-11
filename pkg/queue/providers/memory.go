// file: pkg/queue/providers/memory.go
// version: 1.1.0
// guid: 2295c946-d671-4f1f-8dd4-85f7aa6d56be

package providers

import (
	"context"
	"errors"
	"fmt"
	"sync"

	"github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// memoryQueue stores messages and statistics for a single logical queue.
type memoryQueue struct {
	name  string
	ch    chan *queuepb.QueueMessage
	mu    sync.Mutex
	count int64
}

// MemoryQueue provides an in-memory implementation of the Queue interface.
// It supports multiple named queues with simple statistics tracking. This
// implementation is intended for development and testing scenarios and is not
// suitable for production use where durability and distributed processing are
// required.
type MemoryQueue struct {
	mu      sync.RWMutex
	queues  map[string]*memoryQueue
	buffer  int
	running sync.WaitGroup
}

// NewMemoryQueue creates a new MemoryQueue instance with the specified buffer
// size. A default queue named "default" is automatically created to provide
// backwards compatibility with earlier placeholder implementations.
func NewMemoryQueue(buffer int) *MemoryQueue {
	mq := &MemoryQueue{
		queues: make(map[string]*memoryQueue),
		buffer: buffer,
	}
	mq.queues["default"] = &memoryQueue{name: "default", ch: make(chan *queuepb.QueueMessage, buffer)}
	return mq
}

// Publish enqueues a message to the queue specified in the context. If the
// queue does not exist, an error is returned. The context may be cancelled to
// abort the publish operation.
func (m *MemoryQueue) Publish(ctx context.Context, message *queuepb.QueueMessage) error {
	name, ok := queue.QueueNameFromContext(ctx)
	if !ok {
		name = "default"
	}
	m.mu.RLock()
	q, ok := m.queues[name]
	m.mu.RUnlock()
	if !ok {
		return fmt.Errorf("queue %s not found", name)
	}
	select {
	case <-ctx.Done():
		return ctx.Err()
	case q.ch <- message:
		q.mu.Lock()
		q.count++
		q.mu.Unlock()
		return nil
	}
}

// Subscribe registers a handler that will receive messages from the queue
// specified in the context. The handler is executed asynchronously for each
// message. If the queue does not exist the subscription fails.
func (m *MemoryQueue) Subscribe(ctx context.Context, handler queue.MessageHandler) error {
	name, ok := queue.QueueNameFromContext(ctx)
	if !ok {
		name = "default"
	}
	m.mu.RLock()
	q, ok := m.queues[name]
	m.mu.RUnlock()
	if !ok {
		return fmt.Errorf("queue %s not found", name)
	}

	m.running.Add(1)
	go func() {
		defer m.running.Done()
		for {
			select {
			case <-ctx.Done():
				return
			case msg := <-q.ch:
				if err := handler(ctx, msg); err != nil {
					// For in-memory provider we simply ignore handler errors but in
					// real providers this would route to DLQ or retry mechanisms.
				}
			}
		}
	}()
	return nil
}

// CreateQueue creates a new named queue with the provided configuration. If
// the queue already exists an error is returned.
func (m *MemoryQueue) CreateQueue(ctx context.Context, config *queuepb.QueueConfig) error {
	if config.GetName() == "" {
		return errors.New("queue name required")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	if _, exists := m.queues[config.GetName()]; exists {
		return fmt.Errorf("queue %s already exists", config.GetName())
	}
	m.queues[config.GetName()] = &memoryQueue{name: config.GetName(), ch: make(chan *queuepb.QueueMessage, m.buffer)}
	return nil
}

// DeleteQueue removes a queue and all pending messages.
func (m *MemoryQueue) DeleteQueue(ctx context.Context, name string) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	q, ok := m.queues[name]
	if !ok {
		return fmt.Errorf("queue %s not found", name)
	}
	close(q.ch)
	delete(m.queues, name)
	return nil
}

// GetQueueInfo returns basic statistics about a queue.
func (m *MemoryQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	m.mu.RLock()
	q, ok := m.queues[name]
	m.mu.RUnlock()
	if !ok {
		return nil, fmt.Errorf("queue %s not found", name)
	}
	q.mu.Lock()
	pending := int64(len(q.ch))
	q.mu.Unlock()

	info := &queuepb.QueueInfo{}
	info.SetName(name)
	info.SetMessageCount(pending)
	return info, nil
}

// Shutdown waits for all active subscribers to finish processing.
func (m *MemoryQueue) Shutdown(ctx context.Context) {
	ch := make(chan struct{})
	go func() {
		m.running.Wait()
		close(ch)
	}()
	select {
	case <-ctx.Done():
	case <-ch:
	}
}
