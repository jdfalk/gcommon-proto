// file: templates/event-driven-service/internal/worker/worker.go
// version: 1.0.0
// guid: ec046bdf-9095-459c-8ee3-5fcb23f2b699

package worker

import (
	"context"

	glog "github.com/jdfalk/gcommon/pkg/log"
	gqueue "github.com/jdfalk/gcommon/pkg/queue"
)

type Worker struct {
	queue  gqueue.Provider
	logger glog.Provider
}

func New(q gqueue.Provider, logger glog.Provider) *Worker {
	return &Worker{queue: q, logger: logger}
}

// Start begins consuming messages from the queue. This implementation is a
// placeholder and should be replaced with real message handling logic.
func (w *Worker) Start(ctx context.Context) error {
	ch, err := w.queue.Consume(ctx, "events")
	if err != nil {
		return err
	}
	for msg := range ch {
		w.logger.Info("processed message", glog.Field{Key: "msg", Value: string(msg)})
	}
	return nil
}
