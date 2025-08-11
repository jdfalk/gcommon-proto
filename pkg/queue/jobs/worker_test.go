// file: pkg/queue/jobs/worker_test.go
// version: 1.0.0
// guid: 661cb72e-0291-4820-b56c-b8c49988f642

package jobs

import (
	"context"
	"sync"
	"testing"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// dummyQueue is a minimal in-memory implementation of the Subscriber
// interface used for testing the Worker without introducing package
// dependencies that could result in import cycles.
type dummyQueue struct{ ch chan *queuepb.QueueMessage }

func newDummyQueue() *dummyQueue { return &dummyQueue{ch: make(chan *queuepb.QueueMessage, 1)} }

func (d *dummyQueue) Publish(msg *queuepb.QueueMessage) { d.ch <- msg }

func (d *dummyQueue) Subscribe(ctx context.Context, h func(context.Context, *queuepb.QueueMessage) error) error {
	go func() {
		for {
			select {
			case <-ctx.Done():
				return
			case m := <-d.ch:
				_ = h(ctx, m)
			}
		}
	}()
	return nil
}

// TestWorker_Start ensures that the worker subscribes to the queue and schedules
// jobs for processing.
func TestWorker_Start(t *testing.T) {
	t.Parallel()
	dq := newDummyQueue()
	sched := NewScheduler()
	worker := &Worker{Scheduler: sched, Queue: dq}

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	var mu sync.Mutex
	processed := 0
	processor := func(ctx context.Context, j *Job) error {
		mu.Lock()
		processed++
		mu.Unlock()
		cancel()
		return nil
	}

	if err := worker.Start(ctx, processor); err != nil {
		t.Fatalf("start worker: %v", err)
	}

	msg := &queuepb.QueueMessage{}
	msg.SetId("1")
	dq.Publish(msg)

	<-ctx.Done()
	sched.Wait()

	mu.Lock()
	defer mu.Unlock()
	if processed != 1 {
		t.Fatalf("expected 1 job processed, got %d", processed)
	}
}
