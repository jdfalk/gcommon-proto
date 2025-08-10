// file: pkg/notification/providers/providers_test.go
// version: 1.0.0
// guid: 12121212-3434-4545-5656-676767676767

package providers

import (
	"context"
	"testing"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

func TestEmailProviderSend(t *testing.T) {
	p, err := notification.NewProvider("email", map[string]any{"host": "localhost"})
	if err != nil {
		t.Fatalf("NewProvider: %v", err)
	}
	if _, err := p.Send(context.Background(), &pb.NotificationMessage{}); err != nil {
		t.Fatalf("Send: %v", err)
	}
}
