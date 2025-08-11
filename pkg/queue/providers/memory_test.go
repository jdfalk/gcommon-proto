// file: pkg/queue/providers/memory_test.go
// version: 1.1.0
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

// TestMemoryQueue_NamedQueue verifies that messages published to a named queue
// are routed only to subscribers of that queue.
func TestMemoryQueue_NamedQueue(t *testing.T) {
	t.Parallel()
	q := NewMemoryQueue(2)

	ctxA := queue.WithQueueName(context.Background(), "A")
	ctxB := queue.WithQueueName(context.Background(), "B")

	cfgA := &queuepb.QueueConfig{}
	cfgA.SetName("A")
	if err := q.CreateQueue(context.Background(), cfgA); err != nil {
		t.Fatalf("create queue A: %v", err)
	}
	receivedA := make(chan *queuepb.QueueMessage, 1)
	if err := q.Subscribe(ctxA, queue.MessageHandler(func(_ context.Context, m *queuepb.QueueMessage) error {
		receivedA <- m
		return nil
	})); err != nil {
		t.Fatalf("subscribe A: %v", err)
	}

	// Create queue B and subscribe
	cfg := &queuepb.QueueConfig{}
	cfg.SetName("B")
	if err := q.CreateQueue(context.Background(), cfg); err != nil {
		t.Fatalf("create queue B: %v", err)
	}
	receivedB := make(chan *queuepb.QueueMessage, 1)
	if err := q.Subscribe(ctxB, queue.MessageHandler(func(_ context.Context, m *queuepb.QueueMessage) error {
		receivedB <- m
		return nil
	})); err != nil {
		t.Fatalf("subscribe B: %v", err)
	}

	// Publish message to queue B only
	msg := &queuepb.QueueMessage{}
	msg.SetId("msgB")
	if err := q.Publish(ctxB, msg); err != nil {
		t.Fatalf("publish B: %v", err)
	}

	select {
	case <-receivedA:
		t.Fatal("queue A should not receive message for queue B")
	case m := <-receivedB:
		if m.GetId() != "msgB" {
			t.Fatalf("unexpected message id: %s", m.GetId())
		}
	case <-time.After(time.Second):
		t.Fatal("timeout waiting for message")
	}
}
