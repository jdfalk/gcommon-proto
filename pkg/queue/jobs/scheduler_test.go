// file: pkg/queue/jobs/scheduler_test.go
// version: 1.0.0
// guid: e4f528b7-359e-45b8-83a7-b20b807cfa27

package jobs

import (
	"context"
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
