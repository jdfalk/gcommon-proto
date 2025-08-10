// file: pkg/queue/examples/producer.go
// version: 1.0.0
// guid: d77be7df-8b27-4441-b042-cf83c37c8aec

package examples

import (
	"context"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	"github.com/jdfalk/gcommon/pkg/queue/providers"
)

func ProducerExample(ctx context.Context) error {
	q := providers.NewMemoryQueue(10)
	return q.Publish(ctx, &queuepb.QueueMessage{})
}
