// file: pkg/notification/proto/proto.go

// Package notificationpb provides consolidated exports for notification protobuf types
package notificationpb

// Re-export types from notification protobuf packages for backwards compatibility
import (
	notepb_enums "github.com/jdfalk/gcommon/pkg/notification/proto/enums"
	notepb_messages "github.com/jdfalk/gcommon/pkg/notification/proto/messages"
	notepb_requests "github.com/jdfalk/gcommon/pkg/notification/proto/requests"
	notepb_responses "github.com/jdfalk/gcommon/pkg/notification/proto/responses"
	notepb_services "github.com/jdfalk/gcommon/pkg/notification/proto/services"
)

// Message types
type (
	NotificationMessage       = notepb_messages.NotificationMessage
	DeliveryChannel           = notepb_messages.DeliveryChannel
	Template                  = notepb_messages.Template
	SubscriptionPreferences   = notepb_messages.SubscriptionPreferences
	EventNotification         = notepb_messages.EventNotification
	SendNotificationRequest   = notepb_requests.SendNotificationRequest
	UpdatePreferencesRequest  = notepb_requests.UpdatePreferencesRequest
	GetTemplateRequest        = notepb_requests.GetTemplateRequest
	SendNotificationResponse  = notepb_responses.SendNotificationResponse
	UpdatePreferencesResponse = notepb_responses.UpdatePreferencesResponse
	GetTemplateResponse       = notepb_responses.GetTemplateResponse
)

// Enum types
type (
	DeliveryStatus            = notepb_enums.DeliveryStatus
	DeliveryChannelType       = notepb_messages.DeliveryChannelType
	NotificationServiceServer = notepb_services.NotificationServiceServer
)
