// file: pkg/queue/examples/consumer.go
// version: 1.0.0
// guid: 6062c1b4-11e9-4b57-a9c3-822ff7822423

package examples

import (
	"context"
	"fmt"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	"github.com/jdfalk/gcommon/pkg/queue/providers"
)

func ConsumerExample(ctx context.Context) error {
	q := providers.NewMemoryQueue(10)
	return q.Subscribe(ctx, func(_ context.Context, m *queuepb.QueueMessage) error {
		fmt.Println("received message", m)
		return nil
	})
}
