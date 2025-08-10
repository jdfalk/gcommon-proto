// file: pkg/notification/delivery/tracking.go
// version: 1.0.0
// guid: 99999999-9999-9999-9999-999999999999

package delivery

import (
	"context"
	"sync"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// InMemoryTracker tracks deliveries in memory.
type InMemoryTracker struct {
	mu       sync.RWMutex
	statuses map[string]pb.DeliveryStatus
}

// NewInMemoryTracker creates a tracker instance.
func NewInMemoryTracker() notification.DeliveryTracker {
	return &InMemoryTracker{statuses: make(map[string]pb.DeliveryStatus)}
}

// TrackDelivery records initial status.
func (t *InMemoryTracker) TrackDelivery(ctx context.Context, deliveryID string, status pb.DeliveryStatus) error {
	t.mu.Lock()
	defer t.mu.Unlock()
	t.statuses[deliveryID] = status
	return nil
}

// GetDeliveryStatus fetches stored status.
func (t *InMemoryTracker) GetDeliveryStatus(ctx context.Context, deliveryID string) (pb.DeliveryStatus, error) {
	t.mu.RLock()
	defer t.mu.RUnlock()
	return t.statuses[deliveryID], nil
}

// UpdateDeliveryStatus updates an existing status.
func (t *InMemoryTracker) UpdateDeliveryStatus(ctx context.Context, deliveryID string, status pb.DeliveryStatus) error {
	t.mu.Lock()
	defer t.mu.Unlock()
	t.statuses[deliveryID] = status
	return nil
}
