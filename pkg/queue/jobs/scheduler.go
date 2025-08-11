// file: pkg/queue/jobs/scheduler.go
// version: 1.1.0
// guid: 617260de-03ba-4067-865d-2c83af7a4049

package jobs

import (
	"context"
	"fmt"
	"sync"
	"time"
)

type Scheduler struct {
	mu      sync.Mutex
	jobs    map[string]*JobStatus
	cancel  map[string]context.CancelFunc
	running sync.WaitGroup
}

// NewScheduler creates a scheduler capable of running single-run and recurring
// jobs. Jobs are tracked in-memory and no persistence is provided.
func NewScheduler() *Scheduler {
	return &Scheduler{
		jobs:   make(map[string]*JobStatus),
		cancel: make(map[string]context.CancelFunc),
	}
}

// ScheduleJob schedules a one-time job to run at the specified time.
func (s *Scheduler) ScheduleJob(ctx context.Context, job *Job) error {
	s.mu.Lock()
	s.jobs[job.ID] = &JobStatus{ID: job.ID}
	s.mu.Unlock()

	s.running.Add(1)
	time.AfterFunc(time.Until(job.RunAt), func() {
		defer s.running.Done()
		err := job.Handler(ctx, job)
		s.mu.Lock()
		defer s.mu.Unlock()
		status := s.jobs[job.ID]
		if err != nil {
			status.Error = err.Error()
		} else {
			status.Completed = true
		}
	})
	return nil
}

// ScheduleRecurringJob schedules a job to run repeatedly at the given interval
// until the context is cancelled or CancelJob is called.
func (s *Scheduler) ScheduleRecurringJob(ctx context.Context, job *Job, interval time.Duration) error {
	s.mu.Lock()
	if _, exists := s.jobs[job.ID]; exists {
		s.mu.Unlock()
		return fmt.Errorf("job %s already scheduled", job.ID)
	}
	s.jobs[job.ID] = &JobStatus{ID: job.ID}
	ctx, cancel := context.WithCancel(ctx)
	s.cancel[job.ID] = cancel
	s.mu.Unlock()

	s.running.Add(1)
	go func() {
		defer s.running.Done()
		ticker := time.NewTicker(interval)
		defer ticker.Stop()
		for {
			select {
			case <-ctx.Done():
				return
			case <-ticker.C:
				if err := job.Handler(ctx, job); err != nil {
					s.mu.Lock()
					s.jobs[job.ID].Error = err.Error()
					s.mu.Unlock()
				}
			}
		}
	}()
	return nil
}

// CancelJob stops a scheduled or recurring job if present.
func (s *Scheduler) CancelJob(ctx context.Context, jobID string) error {
	s.mu.Lock()
	if cancel, ok := s.cancel[jobID]; ok {
		cancel()
		delete(s.cancel, jobID)
	}
	delete(s.jobs, jobID)
	s.mu.Unlock()
	return nil
}

// GetJobStatus retrieves the status for a job.
func (s *Scheduler) GetJobStatus(ctx context.Context, jobID string) (*JobStatus, error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	status, ok := s.jobs[jobID]
	if !ok {
		return nil, fmt.Errorf("job %s not found", jobID)
	}
	return status, nil
}

// Wait blocks until all scheduled jobs have completed. This is mainly useful
// for tests to ensure all goroutines have finished processing.
func (s *Scheduler) Wait() {
	s.running.Wait()
}
