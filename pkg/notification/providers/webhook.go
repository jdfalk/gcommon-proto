// file: pkg/notification/providers/webhook.go
// version: 1.0.0
// guid: 44444444-4444-4444-4444-444444444444

package providers

import (
	"bytes"
	"context"
	"fmt"
	"net/http"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// WebhookProvider sends notifications to HTTP endpoints.
type WebhookProvider struct {
	url string
}

// NewWebhookProvider creates a WebhookProvider.
func NewWebhookProvider(cfg map[string]any) (notification.Provider, error) {
	url, _ := cfg["url"].(string)
	return &WebhookProvider{url: url}, nil
}

// Send delivers a webhook notification.
func (p *WebhookProvider) Send(ctx context.Context, msg *pb.NotificationMessage) (*pb.SendNotificationResponse, error) {
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, p.url, bytes.NewBufferString(msg.GetBody()))
	if err != nil {
		return nil, err
	}
	_, err = http.DefaultClient.Do(req)
	return &pb.SendNotificationResponse{}, err
}

// ValidateConfig validates provider configuration.
func (p *WebhookProvider) ValidateConfig(cfg map[string]any) error {
	if _, ok := cfg["url"].(string); !ok {
		return fmt.Errorf("missing url")
	}
	return nil
}

// Capabilities returns provider capabilities.
func (p *WebhookProvider) Capabilities() *notification.ProviderCapabilities {
	return &notification.ProviderCapabilities{SupportsTemplates: true, SupportsBulk: false}
}

func init() {
	notification.RegisterProvider("webhook", NewWebhookProvider)
}
