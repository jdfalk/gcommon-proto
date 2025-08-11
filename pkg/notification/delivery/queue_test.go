// file: pkg/notification/delivery/queue_test.go
// version: 1.0.0
// guid: 8f1d2c3b-4a5e-6f7d-8e9f-0a1b2c3d4e5f

package delivery

import (
	"context"
	"testing"

	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

func TestQueueEnqueueDequeue(t *testing.T) {
	q := NewQueue(1)
	msg := &pb.NotificationMessage{}
	msg.SetId("q1")
	q.Enqueue(msg)
	got, err := q.Dequeue(context.Background())
	if err != nil {
		t.Fatalf("Dequeue: %v", err)
	}
	if got.GetId() != "q1" {
		t.Fatalf("unexpected message: %v", got)
	}
}

func TestQueueDequeueContextCancel(t *testing.T) {
	q := NewQueue(0)
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	if _, err := q.Dequeue(ctx); err == nil {
		t.Fatalf("expected context error")
	}
}
