// file: pkg/queue/jobs/worker.go
// version: 1.1.0
// guid: d0a9c07c-518c-4ea5-93d3-cca02f4d31ad

package jobs

import (
	"context"
	"errors"
	"time"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// Worker consumes messages from a Queue and schedules them for processing using
// the Scheduler. Each message is wrapped in a Job whose Handler invokes the
// provided Processor function.
// Subscriber defines the subset of queue operations needed by Worker. This
// interface is intentionally small to avoid circular dependencies with the
// parent queue package.
type Subscriber interface {
	Subscribe(ctx context.Context, handler func(context.Context, *queuepb.QueueMessage) error) error
}

// Worker consumes messages from a Subscriber implementation and schedules them
// for processing using the Scheduler. Each message is wrapped in a Job whose
// Handler invokes the provided Processor function.
type Worker struct {
	Scheduler *Scheduler
	Queue     Subscriber
}

// Start begins processing messages from the worker's queue. It subscribes to
// the queue and schedules incoming messages as jobs using the provided
// Processor. The worker continues running until the context is cancelled.
func (w *Worker) Start(ctx context.Context, processor Processor) error {
	if w.Scheduler == nil || w.Queue == nil {
		return errors.New("worker requires scheduler and queue")
	}
	if processor == nil {
		return errors.New("processor required")
	}

	return w.Queue.Subscribe(ctx, func(msgCtx context.Context, m *queuepb.QueueMessage) error {
		job := &Job{
			ID:      m.GetId(),
			Message: &queuepb.Message{},
			RunAt:   time.Now(),
			Handler: func(c context.Context, j *Job) error { return processor(c, j) },
		}
		return w.Scheduler.ScheduleJob(msgCtx, job)
	})
}
