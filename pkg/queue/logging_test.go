// file: pkg/queue/logging_test.go
// version: 1.0.0
// guid: 669fbf93-9433-450a-ad9b-5cf611cf0b8b

package queue

import (
	"context"
	"fmt"
	"testing"

	"github.com/jdfalk/gcommon/pkg/log/testlogger"
	"github.com/jdfalk/gcommon/pkg/queue/jobs"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

// stubQueue implements Queue with no-op methods for testing.
type stubQueue struct{}

func (s *stubQueue) Publish(ctx context.Context, m *queuepb.QueueMessage) error      { return nil }
func (s *stubQueue) Subscribe(ctx context.Context, h MessageHandler) error           { return nil }
func (s *stubQueue) CreateQueue(ctx context.Context, cfg *queuepb.QueueConfig) error { return nil }
func (s *stubQueue) DeleteQueue(ctx context.Context, name string) error              { return nil }
func (s *stubQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	return &queuepb.QueueInfo{}, nil
}

// stubScheduler implements Scheduler with no-op methods.
type stubScheduler struct{}

func (s *stubScheduler) ScheduleJob(ctx context.Context, job *jobs.Job) error { return nil }
func (s *stubScheduler) CancelJob(ctx context.Context, jobID string) error    { return nil }
func (s *stubScheduler) GetJobStatus(ctx context.Context, jobID string) (*jobs.JobStatus, error) {
	return &jobs.JobStatus{ID: jobID}, nil
}

func TestLoggedQueue_Publish(t *testing.T) {
	l := testlogger.New()
	q := NewLoggedQueue(&stubQueue{}, l)
	msg := &queuepb.QueueMessage{}
	msg.SetId("1")
	if err := q.Publish(context.Background(), msg); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 2 {
		t.Fatalf("expected 2 log entries, got %d", len(l.Entries()))
	}
	if l.Entries()[0].Message != "queue publish" {
		t.Fatalf("unexpected message: %+v", l.Entries()[0])
	}
}

func TestLoggedScheduler_ScheduleJob(t *testing.T) {
	l := testlogger.New()
	s := NewLoggedScheduler(&stubScheduler{}, l)
	job := &jobs.Job{ID: "job1"}
	if err := s.ScheduleJob(context.Background(), job); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 2 {
		t.Fatalf("expected 2 log entries, got %d", len(l.Entries()))
	}
	if l.Entries()[0].Message != "schedule job" {
		t.Fatalf("unexpected message: %+v", l.Entries()[0])
	}
}

// errQueue returns errors for all methods.
type errQueue struct{}

func (errQueue) Publish(ctx context.Context, m *queuepb.QueueMessage) error {
	return fmt.Errorf("fail")
}
func (errQueue) Subscribe(ctx context.Context, h MessageHandler) error { return fmt.Errorf("fail") }
func (errQueue) CreateQueue(ctx context.Context, cfg *queuepb.QueueConfig) error {
	return fmt.Errorf("fail")
}
func (errQueue) DeleteQueue(ctx context.Context, name string) error { return fmt.Errorf("fail") }
func (errQueue) GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error) {
	return nil, fmt.Errorf("fail")
}

// errScheduler returns errors for all operations.
type errScheduler struct{}

func (errScheduler) ScheduleJob(ctx context.Context, job *jobs.Job) error { return fmt.Errorf("fail") }
func (errScheduler) CancelJob(ctx context.Context, jobID string) error    { return fmt.Errorf("fail") }
func (errScheduler) GetJobStatus(ctx context.Context, jobID string) (*jobs.JobStatus, error) {
	return nil, fmt.Errorf("fail")
}

func TestLoggedQueue_Errors(t *testing.T) {
	l := testlogger.New()
	q := NewLoggedQueue(errQueue{}, l)
	if err := q.Publish(context.Background(), func() *queuepb.QueueMessage { m := &queuepb.QueueMessage{}; m.SetId("1"); return m }()); err == nil {
		t.Fatalf("expected error")
	}
	if err := q.Subscribe(context.Background(), func(context.Context, *queuepb.QueueMessage) error { return nil }); err == nil {
		t.Fatalf("expected error")
	}
	if err := q.CreateQueue(context.Background(), func() *queuepb.QueueConfig { c := &queuepb.QueueConfig{}; c.SetName("n"); return c }()); err == nil {
		t.Fatalf("expected error")
	}
	if err := q.DeleteQueue(context.Background(), "n"); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := q.GetQueueInfo(context.Background(), "n"); err == nil {
		t.Fatalf("expected error")
	}
	if len(l.Entries()) != 10 {
		t.Fatalf("expected 10 entries, got %d", len(l.Entries()))
	}
}

func TestLoggedScheduler_Errors(t *testing.T) {
	l := testlogger.New()
	s := NewLoggedScheduler(errScheduler{}, l)
	if err := s.ScheduleJob(context.Background(), &jobs.Job{ID: "1"}); err == nil {
		t.Fatalf("expected error")
	}
	if err := s.CancelJob(context.Background(), "1"); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := s.GetJobStatus(context.Background(), "1"); err == nil {
		t.Fatalf("expected error")
	}
	if len(l.Entries()) != 6 {
		t.Fatalf("expected 6 entries, got %d", len(l.Entries()))
	}
}

func TestLoggedQueue_CreateDeleteInfo(t *testing.T) {
	l := testlogger.New()
	q := NewLoggedQueue(&stubQueue{}, l)
	if err := q.CreateQueue(context.Background(), func() *queuepb.QueueConfig { c := &queuepb.QueueConfig{}; c.SetName("q"); return c }()); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if err := q.DeleteQueue(context.Background(), "q"); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if _, err := q.GetQueueInfo(context.Background(), "q"); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(l.Entries()) != 6 {
		t.Fatalf("expected 6 log entries, got %d", len(l.Entries()))
	}
}
