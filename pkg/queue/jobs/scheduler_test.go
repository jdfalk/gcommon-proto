// file: pkg/queue/jobs/scheduler_test.go
// version: 1.1.0
// guid: e4f528b7-359e-45b8-83a7-b20b807cfa27

package jobs

import (
	"context"
	"sync"
	"testing"
	"time"
)

func TestScheduler_ScheduleJob(t *testing.T) {
	t.Parallel()
	s := NewScheduler()
	done := make(chan struct{})
	job := &Job{
		ID:    "test",
		RunAt: time.Now().Add(10 * time.Millisecond),
		Handler: func(context.Context, *Job) error {
			close(done)
			return nil
		},
	}
	if err := s.ScheduleJob(context.Background(), job); err != nil {
		t.Fatalf("schedule job: %v", err)
	}
	select {
	case <-done:
	case <-time.After(time.Second):
		t.Fatal("job did not run")
	}
}

// TestScheduler_ScheduleRecurringJob ensures recurring jobs execute multiple times
// until cancelled.
func TestScheduler_ScheduleRecurringJob(t *testing.T) {
	t.Parallel()
	s := NewScheduler()

	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	var mu sync.Mutex
	count := 0
	job := &Job{
		ID: "recur",
		Handler: func(context.Context, *Job) error {
			mu.Lock()
			count++
			mu.Unlock()
			if count >= 3 {
				cancel()
			}
			return nil
		},
	}
	if err := s.ScheduleRecurringJob(ctx, job, 10*time.Millisecond); err != nil {
		t.Fatalf("schedule recurring: %v", err)
	}

	// Wait for cancellation
	<-ctx.Done()
	s.Wait()

	mu.Lock()
	defer mu.Unlock()
	if count < 3 {
		t.Fatalf("expected at least 3 executions, got %d", count)
	}
}
