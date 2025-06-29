// file: pkg/notification/proto/messages/placeholder.go
// Placeholder file to satisfy import requirements until protobuf generation is complete

package messages

import (
	"time"
)

// TODO: These types will be replaced by generated protobuf files
// Placeholder types to satisfy import requirements

// NotificationMessage represents a notification message
type NotificationMessage struct {
	ID        string    `json:"id"`
	Title     string    `json:"title"`
	Body      string    `json:"body"`
	Timestamp time.Time `json:"timestamp"`
}

// DeliveryChannel represents a notification delivery channel
type DeliveryChannel struct {
	ID   string `json:"id"`
	Type string `json:"type"`
	Name string `json:"name"`
}

// Template represents a notification template
type Template struct {
	ID      string `json:"id"`
	Name    string `json:"name"`
	Content string `json:"content"`
}

// SubscriptionPreferences represents user notification preferences
type SubscriptionPreferences struct {
	UserID   string            `json:"user_id"`
	Channels map[string]bool   `json:"channels"`
	Settings map[string]string `json:"settings"`
}

// EventNotification represents an event-based notification
type EventNotification struct {
	ID        string                 `json:"id"`
	EventType string                 `json:"event_type"`
	Data      map[string]interface{} `json:"data"`
	Timestamp time.Time              `json:"timestamp"`
}
