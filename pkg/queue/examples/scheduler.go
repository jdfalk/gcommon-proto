// file: pkg/queue/examples/scheduler.go
// version: 1.0.0
// guid: c193225c-7d1c-48af-a02e-0a7896615fa0

package examples

import (
	"context"
	"time"

	"github.com/jdfalk/gcommon/pkg/queue/jobs"
)

func SchedulerExample(ctx context.Context) error {
	s := jobs.NewScheduler()
	job := &jobs.Job{
		ID:    "example",
		RunAt: time.Now().Add(10 * time.Millisecond),
		Handler: func(context.Context, *jobs.Job) error {
			return nil
		},
	}
	return s.ScheduleJob(ctx, job)
}
