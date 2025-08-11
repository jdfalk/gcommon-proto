// file: pkg/queue/logging.go
// version: 1.0.0
// guid: 065436e2-471f-463d-8920-ead7fe587544

package queue

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/log"
	"github.com/jdfalk/gcommon/pkg/queue/jobs"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// LoggedQueue wraps a Queue and logs operations.
type LoggedQueue struct {
	q      Queue
	logger log.Logger
}

// NewLoggedQueue creates a LoggedQueue.
func NewLoggedQueue(q Queue, l log.Logger) *LoggedQueue { return &LoggedQueue{q: q, logger: l} }

// Publish logs message publishing.
func (l *LoggedQueue) Publish(ctx context.Context, message *queuepb.QueueMessage) error {
	l.logger.InfoContext(ctx, "queue publish", log.Field{Key: "id", Value: message.GetId()})
	if err := l.q.Publish(ctx, message); err != nil {
		l.logger.ErrorContext(ctx, "queue publish failed", log.Field{Key: "id", Value: message.GetId()}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "queue publish success", log.Field{Key: "id", Value: message.GetId()})
	return nil
}

// Subscribe logs subscription registration.
func (l *LoggedQueue) Subscribe(ctx context.Context, handler MessageHandler) error {
	l.logger.InfoContext(ctx, "queue subscribe")
	if err := l.q.Subscribe(ctx, handler); err != nil {
		l.logger.ErrorContext(ctx, "queue subscribe failed", log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "queue subscribe success")
	return nil
}

// CreateQueue logs queue creation.
func (l *LoggedQueue) CreateQueue(ctx context.Context, cfg *queuepb.QueueConfig) error {
	l.logger.InfoContext(ctx, "queue create", log.Field{Key: "name", Value: cfg.GetName()})
	if err := l.q.CreateQueue(ctx, cfg); err != nil {
		l.logger.ErrorContext(ctx, "queue create failed", log.Field{Key: "name", Value: cfg.GetName()}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "queue create success", log.Field{Key: "name", Value: cfg.GetName()})
	return nil
}

// DeleteQueue logs queue deletion.
func (l *LoggedQueue) DeleteQueue(ctx context.Context, name string) error {
	l.logger.InfoContext(ctx, "queue delete", log.Field{Key: "name", Value: name})
	if err := l.q.DeleteQueue(ctx, name); err != nil {
		l.logger.ErrorContext(ctx, "queue delete failed", log.Field{Key: "name", Value: name}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "queue delete success", log.Field{Key: "name", Value: name})
	return nil
}

// GetQueueInfo logs queue info retrieval.
func (l *LoggedQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	l.logger.InfoContext(ctx, "queue info", log.Field{Key: "name", Value: name})
	info, err := l.q.GetQueueInfo(ctx, name)
	if err != nil {
		l.logger.ErrorContext(ctx, "queue info failed", log.Field{Key: "name", Value: name}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "queue info success", log.Field{Key: "name", Value: name})
	return info, nil
}

// LoggedScheduler wraps a Scheduler and logs job scheduling.
type LoggedScheduler struct {
	s      Scheduler
	logger log.Logger
}

// NewLoggedScheduler creates a LoggedScheduler.
func NewLoggedScheduler(s Scheduler, l log.Logger) *LoggedScheduler {
	return &LoggedScheduler{s: s, logger: l}
}

// ScheduleJob logs job scheduling events.
func (l *LoggedScheduler) ScheduleJob(ctx context.Context, job *jobs.Job) error {
	l.logger.InfoContext(ctx, "schedule job", log.Field{Key: "id", Value: job.ID})
	if err := l.s.ScheduleJob(ctx, job); err != nil {
		l.logger.ErrorContext(ctx, "schedule job failed", log.Field{Key: "id", Value: job.ID}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "schedule job success", log.Field{Key: "id", Value: job.ID})
	return nil
}

// CancelJob logs job cancellation.
func (l *LoggedScheduler) CancelJob(ctx context.Context, jobID string) error {
	l.logger.InfoContext(ctx, "cancel job", log.Field{Key: "id", Value: jobID})
	if err := l.s.CancelJob(ctx, jobID); err != nil {
		l.logger.ErrorContext(ctx, "cancel job failed", log.Field{Key: "id", Value: jobID}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.InfoContext(ctx, "cancel job success", log.Field{Key: "id", Value: jobID})
	return nil
}

// GetJobStatus logs job status retrieval.
func (l *LoggedScheduler) GetJobStatus(ctx context.Context, jobID string) (*jobs.JobStatus, error) {
	l.logger.InfoContext(ctx, "job status", log.Field{Key: "id", Value: jobID})
	st, err := l.s.GetJobStatus(ctx, jobID)
	if err != nil {
		l.logger.ErrorContext(ctx, "job status failed", log.Field{Key: "id", Value: jobID}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "job status success", log.Field{Key: "id", Value: jobID})
	return st, nil
}
