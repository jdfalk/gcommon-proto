// file: pkg/queue/providers/redis_test.go
// version: 1.0.0
// guid: fb4ee00a-7d62-4c2a-8585-0f47871b0284

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/alicebob/miniredis/v2"
	queue "github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// TestRedisQueue_PublishSubscribe validates basic publish/subscribe flow using
// a miniredis server.
func TestRedisQueue_PublishSubscribe(t *testing.T) {
	t.Parallel()
	mr, err := miniredis.Run()
	if err != nil {
		t.Fatalf("miniredis: %v", err)
	}
	defer mr.Close()

	rq, err := NewRedisQueue(mr.Addr(), "")
	if err != nil {
		t.Fatalf("new redis queue: %v", err)
	}
	defer rq.Close()

	ctx := queue.WithQueueName(context.Background(), "test")
	cfg := &queuepb.QueueConfig{}
	cfg.SetName("test")
	if err := rq.CreateQueue(context.Background(), cfg); err != nil {
		t.Fatalf("create queue: %v", err)
	}

	received := make(chan *queuepb.QueueMessage, 1)
	if err := rq.Subscribe(ctx, queue.MessageHandler(func(_ context.Context, m *queuepb.QueueMessage) error {
		received <- m
		return nil
	})); err != nil {
		t.Fatalf("subscribe: %v", err)
	}

	msg := &queuepb.QueueMessage{}
	msg.SetId("1")
	if err := rq.Publish(ctx, msg); err != nil {
		t.Fatalf("publish: %v", err)
	}

	select {
	case m := <-received:
		if m.GetId() != "1" {
			t.Fatalf("unexpected message id: %s", m.GetId())
		}
	case <-time.After(time.Second):
		t.Fatal("timeout waiting for message")
	}
}
