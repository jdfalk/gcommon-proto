// file: pkg/queue/providers/memory_test.go
// version: 1.0.0
// guid: eb1cb3f1-9651-4ffc-b83d-954f0fc32713

package providers

import (
	"context"
	"testing"
	"time"

	queue "github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

func TestMemoryQueue_PublishSubscribe(t *testing.T) {
	t.Parallel()
	q := NewMemoryQueue(1)
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	received := make(chan *queuepb.QueueMessage, 1)
	if err := q.Subscribe(ctx, queue.MessageHandler(func(_ context.Context, m *queuepb.QueueMessage) error {
		received <- m
		return nil
	})); err != nil {
		t.Fatalf("subscribe: %v", err)
	}

	msg := &queuepb.QueueMessage{}
	if err := q.Publish(ctx, msg); err != nil {
		t.Fatalf("publish: %v", err)
	}

	select {
	case got := <-received:
		if got == nil {
			t.Fatal("expected message")
		}
	case <-time.After(time.Second):
		t.Fatal("timeout waiting for message")
	}
}
