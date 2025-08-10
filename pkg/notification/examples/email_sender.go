// file: pkg/notification/examples/email_sender.go
// version: 1.1.0
// guid: ffffffff-0000-1111-2222-333333333333

package examples

import (
	"context"

	notification "github.com/jdfalk/gcommon/pkg/notification"
	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/providers"
)

// ExampleEmail demonstrates sending an email notification.
func ExampleEmail() {
	p, _ := notification.NewProvider("email", map[string]any{"host": "localhost"})
	_, _ = p.Send(context.Background(), &pb.NotificationMessage{})
}
