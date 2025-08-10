// file: pkg/queue/jobs/scheduler.go
// version: 1.0.0
// guid: 617260de-03ba-4067-865d-2c83af7a4049

package jobs

import (
	"context"
	"fmt"
	"sync"
	"time"
)

type Scheduler struct {
	mu   sync.Mutex
	jobs map[string]*JobStatus
}

func NewScheduler() *Scheduler {
	return &Scheduler{jobs: make(map[string]*JobStatus)}
}

func (s *Scheduler) ScheduleJob(ctx context.Context, job *Job) error {
	s.mu.Lock()
	s.jobs[job.ID] = &JobStatus{ID: job.ID}
	s.mu.Unlock()
	time.AfterFunc(time.Until(job.RunAt), func() {
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

func (s *Scheduler) CancelJob(ctx context.Context, jobID string) error {
	s.mu.Lock()
	delete(s.jobs, jobID)
	s.mu.Unlock()
	return nil
}

func (s *Scheduler) GetJobStatus(ctx context.Context, jobID string) (*JobStatus, error) {
	s.mu.Lock()
	defer s.mu.Unlock()
	status, ok := s.jobs[jobID]
	if !ok {
		return nil, fmt.Errorf("job %s not found", jobID)
	}
	return status, nil
}
