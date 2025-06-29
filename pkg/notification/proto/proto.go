// file: pkg/notification/proto/proto.go

// Package proto provides consolidated exports for notification protobuf types
package proto

// Re-export types from notification protobuf packages for backwards compatibility
import (
	notepb_enums "github.com/jdfalk/gcommon/pkg/notification/proto/enums"
	notepb_messages "github.com/jdfalk/gcommon/pkg/notification/proto/messages"
)

// Message types
type (
	NotificationMessage     = notepb_messages.NotificationMessage
	DeliveryChannel         = notepb_messages.DeliveryChannel
	Template                = notepb_messages.Template
	SubscriptionPreferences = notepb_messages.SubscriptionPreferences
	EventNotification       = notepb_messages.EventNotification
)

// Enum types
type (
	DeliveryStatus      = notepb_enums.DeliveryStatus
	DeliveryChannelType = notepb_messages.DeliveryChannelType
)
