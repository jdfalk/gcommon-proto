// file: test/integration/modules/notification_test.go
// version: 1.1.0
// guid: 8fa0a06b-27d4-4c06-8d25-8342ee742d73

package modules

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/notification/delivery"
	_ "github.com/jdfalk/gcommon/pkg/notification/proto"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
	"github.com/jdfalk/gcommon/pkg/notification/providers"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestNotificationModuleIntegration checks notification delivery.
func TestNotificationModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	email, _ := providers.NewEmailProvider(map[string]any{"host": "smtp"})
	sms, _ := providers.NewSMSProvider(map[string]any{"number": "123"})
	webhook, _ := providers.NewWebhookProvider(map[string]any{"url": "http://example"})
	msg := &pb.NotificationMessage{Subject: pb.String("hi")}

	t.Run("send email", func(t *testing.T) {
		if _, err := email.Send(context.Background(), msg); err != nil {
			t.Fatalf("email send failed: %v", err)
		}
	})

	t.Run("send sms", func(t *testing.T) {
		if _, err := sms.Send(context.Background(), msg); err != nil {
			t.Fatalf("sms send failed: %v", err)
		}
	})

	t.Run("send webhook", func(t *testing.T) {
		if _, err := webhook.Send(context.Background(), msg); err != nil {
			t.Fatalf("webhook send failed: %v", err)
		}
	})

	t.Run("queue fallback", func(t *testing.T) {
		q := delivery.NewQueue(1)
		q.Enqueue(msg)
		if _, err := q.Dequeue(context.Background()); err != nil {
			t.Fatalf("dequeue failed: %v", err)
		}
	})

	t.Run("notification stats", func(t *testing.T) {
		if caps := email.Capabilities(); !caps.SupportsTemplates {
			t.Fatalf("expected template support")
		}
	})
}
