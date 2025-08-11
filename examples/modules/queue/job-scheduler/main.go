//go:build ignore

// file: examples/modules/queue/job-scheduler/main.go
// version: 1.1.0
// guid: 1d47db8d-acf5-4664-abb8-7f3003d389fb

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/queue/jobs"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// schedulerApp wraps the job scheduler used in this example.
type schedulerApp struct {
	s *jobs.Scheduler
}

// setup creates a new scheduler instance.
func setup(ctx context.Context) (*schedulerApp, error) {
	return &schedulerApp{s: jobs.NewScheduler()}, nil
}

// run schedules a job to execute after one second and waits for completion.
func run(ctx context.Context, app *schedulerApp) error {
	job := &jobs.Job{
		ID:      "demo",
		Message: &queuepb.Message{Body: "payload"},
		RunAt:   time.Now().Add(time.Second),
		Handler: func(ctx context.Context, j *jobs.Job) error {
			fmt.Println("executing job:", j.Message.Body)
			return nil
		},
	}
	if err := app.s.ScheduleJob(ctx, job); err != nil {
		return err
	}
	// Wait for job completion
	time.Sleep(1500 * time.Millisecond)
	status, err := app.s.GetJobStatus(ctx, "demo")
	if err != nil {
		return err
	}
	fmt.Printf("job completed: %v\n", status.Completed)
	return nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	app, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	if err := run(ctx, app); err != nil {
		panic(err)
	}
}
