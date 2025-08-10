// file: pkg/notification/providers/push.go
// version: 1.0.0
// guid: 33333333-3333-3333-3333-333333333333

package providers

import (
	"context"
	"fmt"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// PushProvider sends mobile push notifications.
type PushProvider struct {
	service string
}

// NewPushProvider creates a PushProvider.
func NewPushProvider(cfg map[string]any) (notification.Provider, error) {
	service, _ := cfg["service"].(string)
	return &PushProvider{service: service}, nil
}

// Send delivers a push notification.
func (p *PushProvider) Send(ctx context.Context, msg *pb.NotificationMessage) (*pb.SendNotificationResponse, error) {
	fmt.Printf("sending push via %s: %v\n", p.service, msg)
	return &pb.SendNotificationResponse{}, nil
}

// ValidateConfig validates provider configuration.
func (p *PushProvider) ValidateConfig(cfg map[string]any) error {
	if _, ok := cfg["service"].(string); !ok {
		return fmt.Errorf("missing service")
	}
	return nil
}

// Capabilities returns provider capabilities.
func (p *PushProvider) Capabilities() *notification.ProviderCapabilities {
	return &notification.ProviderCapabilities{SupportsTemplates: true, SupportsBulk: true}
}

func init() {
	notification.RegisterProvider("push", NewPushProvider)
}
