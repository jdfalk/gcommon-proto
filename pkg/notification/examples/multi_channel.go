// file: pkg/notification/examples/multi_channel.go
// version: 1.0.0
// guid: 11112222-3333-4444-5555-666677778888

package examples

import (
	"context"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/providers"
)

// ExampleMultiChannel demonstrates sending via multiple providers.
func ExampleMultiChannel() {
	channels := []string{"email", "sms"}
	for _, ch := range channels {
		p, _ := notification.NewProvider(ch, map[string]any{})
		_, _ = p.Send(context.Background(), &pb.NotificationMessage{})
	}
}
