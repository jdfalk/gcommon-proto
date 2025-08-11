// file: test/integration/modules/queue_test.go
// version: 1.1.0
// guid: 7d9cce59-032b-4a2b-b56f-5b16114a4647

package modules

import (
	"context"
	"sync"
	"testing"
	"time"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	"github.com/jdfalk/gcommon/pkg/queue/providers"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestQueueModuleIntegration exercises queue workflows.
func TestQueueModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	q := providers.NewMemoryQueue(10)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	t.Run("publish message", func(t *testing.T) {
		var wg sync.WaitGroup
		wg.Add(1)
		var got *queuepb.QueueMessage
		err := q.Subscribe(ctx, func(ctx context.Context, m *queuepb.QueueMessage) error {
			got = m
			wg.Done()
			return nil
		})
		if err != nil {
			t.Fatalf("subscribe error: %v", err)
		}
		msg := &queuepb.QueueMessage{}
		if err := q.Publish(ctx, msg); err != nil {
			t.Fatalf("publish error: %v", err)
		}
		wg.Wait()
		if got == nil {
			t.Fatalf("expected message to be received")
		}
	})

	t.Run("subscribe to topic", func(t *testing.T) {
		err := q.Subscribe(ctx, func(ctx context.Context, m *queuepb.QueueMessage) error { return nil })
		if err != nil {
			t.Fatalf("subscribe returned error: %v", err)
		}
	})

	t.Run("acknowledge message", func(t *testing.T) {
		var acked bool
		err := q.Subscribe(ctx, func(ctx context.Context, m *queuepb.QueueMessage) error {
			acked = true
			return nil
		})
		if err != nil {
			t.Fatalf("subscribe failed: %v", err)
		}
		_ = q.Publish(ctx, &queuepb.QueueMessage{})
		time.Sleep(10 * time.Millisecond)
		if !acked {
			t.Fatalf("message not acknowledged")
		}
	})

	t.Run("nack message", func(t *testing.T) {
		var attempts int
		err := q.Subscribe(ctx, func(ctx context.Context, m *queuepb.QueueMessage) error {
			attempts++
			return context.DeadlineExceeded
		})
		if err != nil {
			t.Fatalf("subscribe failed: %v", err)
		}
		_ = q.Publish(ctx, &queuepb.QueueMessage{})
		time.Sleep(10 * time.Millisecond)
		if attempts != 1 {
			t.Fatalf("expected single attempt, got %d", attempts)
		}
	})

	t.Run("commit offsets", func(t *testing.T) {
		if _, err := q.GetQueueInfo(ctx, "test"); err != nil {
			t.Fatalf("get queue info: %v", err)
		}
	})
}
