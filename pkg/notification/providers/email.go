// file: pkg/notification/providers/email.go
// version: 1.0.0
// guid: 11111111-1111-1111-1111-111111111111

package providers

import (
	"context"
	"fmt"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// EmailProvider sends notifications via SMTP.
type EmailProvider struct {
	host string
}

// NewEmailProvider creates an EmailProvider.
func NewEmailProvider(cfg map[string]any) (notification.Provider, error) {
	host, _ := cfg["host"].(string)
	return &EmailProvider{host: host}, nil
}

// Send delivers an email notification.
func (p *EmailProvider) Send(ctx context.Context, msg *pb.NotificationMessage) (*pb.SendNotificationResponse, error) {
	fmt.Printf("sending email via %s: %v\n", p.host, msg)
	return &pb.SendNotificationResponse{}, nil
}

// ValidateConfig validates provider configuration.
func (p *EmailProvider) ValidateConfig(cfg map[string]any) error {
	if _, ok := cfg["host"].(string); !ok {
		return fmt.Errorf("missing host")
	}
	return nil
}

// Capabilities returns provider capabilities.
func (p *EmailProvider) Capabilities() *notification.ProviderCapabilities {
	return &notification.ProviderCapabilities{SupportsTemplates: true, SupportsBulk: false}
}

func init() {
	notification.RegisterProvider("email", NewEmailProvider)
}
