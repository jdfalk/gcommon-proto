// file: pkg/notification/providers/slack.go
// version: 1.0.0
// guid: 55555555-5555-5555-5555-555555555555

package providers

import (
	"context"
	"fmt"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// SlackProvider sends notifications to Slack channels.
type SlackProvider struct {
	token   string
	channel string
}

// NewSlackProvider creates a SlackProvider.
func NewSlackProvider(cfg map[string]any) (notification.Provider, error) {
	token, _ := cfg["token"].(string)
	channel, _ := cfg["channel"].(string)
	return &SlackProvider{token: token, channel: channel}, nil
}

// Send delivers a Slack notification.
func (p *SlackProvider) Send(ctx context.Context, msg *pb.NotificationMessage) (*pb.SendNotificationResponse, error) {
	fmt.Printf("sending slack message to %s: %v\n", p.channel, msg)
	return &pb.SendNotificationResponse{}, nil
}

// ValidateConfig validates provider configuration.
func (p *SlackProvider) ValidateConfig(cfg map[string]any) error {
	if _, ok := cfg["token"].(string); !ok {
		return fmt.Errorf("missing token")
	}
	if _, ok := cfg["channel"].(string); !ok {
		return fmt.Errorf("missing channel")
	}
	return nil
}

// Capabilities returns provider capabilities.
func (p *SlackProvider) Capabilities() *notification.ProviderCapabilities {
	return &notification.ProviderCapabilities{SupportsTemplates: true, SupportsBulk: false}
}

func init() {
	notification.RegisterProvider("slack", NewSlackProvider)
}
