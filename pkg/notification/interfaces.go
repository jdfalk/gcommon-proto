// file: pkg/notification/interfaces.go
// version: 1.0.0
// guid: b4d2df14-1c5e-4a84-9eab-9a6b0c4f8079

package notification

import (
	"context"

	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// Provider defines a notification delivery provider.
type Provider interface {
	Send(ctx context.Context, msg *pb.NotificationMessage) (*pb.SendNotificationResponse, error)
	ValidateConfig(cfg map[string]any) error
	Capabilities() *ProviderCapabilities
}

// ProviderCapabilities describes features supported by a provider.
type ProviderCapabilities struct {
	SupportsTemplates bool
	SupportsBulk      bool
}

// TemplateEngine parses and renders notification templates.
type TemplateEngine interface {
	ParseTemplate(tmpl string) (*pb.Template, error)
	RenderTemplate(tmpl *pb.Template, data map[string]any) (string, error)
	ValidateTemplate(tmpl string) error
}

// DeliveryTracker tracks notification delivery state.
type DeliveryTracker interface {
	TrackDelivery(ctx context.Context, deliveryID string, status pb.DeliveryStatus) error
	GetDeliveryStatus(ctx context.Context, deliveryID string) (pb.DeliveryStatus, error)
	UpdateDeliveryStatus(ctx context.Context, deliveryID string, status pb.DeliveryStatus) error
}
