// file: pkg/notification/providers/sms.go
// version: 1.0.0
// guid: 22222222-2222-2222-2222-222222222222

package providers

import (
	"context"
	"fmt"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// SMSProvider sends notifications via SMS gateway.
type SMSProvider struct {
	gateway string
}

// NewSMSProvider creates an SMSProvider.
func NewSMSProvider(cfg map[string]any) (notification.Provider, error) {
	gateway, _ := cfg["gateway"].(string)
	return &SMSProvider{gateway: gateway}, nil
}

// Send delivers an SMS notification.
func (p *SMSProvider) Send(ctx context.Context, msg *pb.NotificationMessage) (*pb.SendNotificationResponse, error) {
	fmt.Printf("sending sms via %s: %v\n", p.gateway, msg)
	return &pb.SendNotificationResponse{}, nil
}

// ValidateConfig validates provider configuration.
func (p *SMSProvider) ValidateConfig(cfg map[string]any) error {
	if _, ok := cfg["gateway"].(string); !ok {
		return fmt.Errorf("missing gateway")
	}
	return nil
}

// Capabilities returns provider capabilities.
func (p *SMSProvider) Capabilities() *notification.ProviderCapabilities {
	return &notification.ProviderCapabilities{SupportsTemplates: false, SupportsBulk: true}
}

func init() {
	notification.RegisterProvider("sms", NewSMSProvider)
}
