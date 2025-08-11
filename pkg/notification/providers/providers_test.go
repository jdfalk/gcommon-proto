// file: pkg/notification/providers/providers_test.go
// version: 1.1.0
// guid: 12121212-3434-4545-5656-676767676767

package providers

import (
	"context"
	"testing"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

func TestProviders(t *testing.T) {
	tests := []struct {
		name     string
		provider string
		cfg      map[string]any
	}{
		{"email", "email", map[string]any{"host": "localhost"}},
		{"sms", "sms", map[string]any{"gateway": "gw"}},
		{"push", "push", map[string]any{"service": "svc"}},
		{"webhook", "webhook", map[string]any{"url": "http://example"}},
		{"slack", "slack", map[string]any{"token": "t", "channel": "c"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			p, err := notification.NewProvider(tt.provider, tt.cfg)
			if err != nil {
				t.Fatalf("NewProvider: %v", err)
			}
			if err := p.ValidateConfig(tt.cfg); err != nil {
				t.Fatalf("ValidateConfig: %v", err)
			}
			if p.Capabilities() == nil {
				t.Fatalf("Capabilities returned nil")
			}
			if _, err := p.Send(context.Background(), &pb.NotificationMessage{}); err != nil {
				t.Fatalf("Send: %v", err)
			}
		})
	}
}
