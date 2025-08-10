// file: pkg/notification/delivery/tracking_test.go
// version: 1.0.0
// guid: 34343434-5656-6767-7878-898989898989

package delivery

import (
	"context"
	"testing"

	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

func TestInMemoryTracker(t *testing.T) {
	tr := NewInMemoryTracker().(*InMemoryTracker)
	id := "1"
	if err := tr.TrackDelivery(context.Background(), id, pb.DeliveryStatus_DELIVERY_STATUS_PENDING); err != nil {
		t.Fatalf("TrackDelivery: %v", err)
	}
	status, _ := tr.GetDeliveryStatus(context.Background(), id)
	if status != pb.DeliveryStatus_DELIVERY_STATUS_PENDING {
		t.Fatalf("unexpected status: %v", status)
	}
}
