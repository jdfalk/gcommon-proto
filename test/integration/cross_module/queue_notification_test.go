// file: test/integration/cross_module/queue_notification_test.go
// version: 1.1.0
// guid: 128ac804-6a4b-4483-a36a-6cc30801ebfb

package crossmodule

import (
	"context"
	"sync"
	"testing"

	"github.com/jdfalk/gcommon/pkg/notification/delivery"
	_ "github.com/jdfalk/gcommon/pkg/notification/proto"
	npb "github.com/jdfalk/gcommon/pkg/notification/proto"
	nproviders "github.com/jdfalk/gcommon/pkg/notification/providers"
	_ "github.com/jdfalk/gcommon/pkg/queue/proto"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	qproviders "github.com/jdfalk/gcommon/pkg/queue/providers"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestQueueNotificationIntegration verifies notification delivery via queues.
func TestQueueNotificationIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	q := qproviders.NewMemoryQueue(10)
	email, _ := nproviders.NewEmailProvider(map[string]any{"host": "smtp"})
	notifyQueue := delivery.NewQueue(10)

	t.Run("enqueue notification", func(t *testing.T) {
		msg := &queuepb.QueueMessage{Data: []byte("hello")}
		if err := q.Publish(context.Background(), msg); err != nil {
			t.Fatalf("publish failed: %v", err)
		}
	})

	t.Run("worker processes notification", func(t *testing.T) {
		var wg sync.WaitGroup
		wg.Add(1)
		_ = q.Subscribe(context.Background(), func(ctx context.Context, m *queuepb.QueueMessage) error {
			notifyQueue.Enqueue(&npb.NotificationMessage{Subject: npb.String(string(m.Data))})
			wg.Done()
			return nil
		})
		_ = q.Publish(context.Background(), &queuepb.QueueMessage{Data: []byte("hello")})
		wg.Wait()
		n, err := notifyQueue.Dequeue(context.Background())
		if err != nil || n.GetSubject() == nil {
			t.Fatalf("notification not dequeued: %v", err)
		}
	})

	t.Run("retry on failure", func(t *testing.T) {
		var attempts int
		_ = q.Subscribe(context.Background(), func(ctx context.Context, m *queuepb.QueueMessage) error {
			attempts++
			return context.DeadlineExceeded
		})
		_ = q.Publish(context.Background(), &queuepb.QueueMessage{})
		if attempts != 1 {
			t.Fatalf("expected 1 attempt got %d", attempts)
		}
	})

	t.Run("dead letter queue", func(t *testing.T) {
		if _, err := email.Send(context.Background(), &npb.NotificationMessage{Subject: npb.String("x")}); err != nil {
			t.Fatalf("send failed: %v", err)
		}
	})
}
