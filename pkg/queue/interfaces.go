// file: pkg/queue/interfaces.go
// version: 1.0.0
// guid: 7f091a3a-39fe-439e-a435-e01e561fe5cd

package queue

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/queue/jobs"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type MessageHandler func(ctx context.Context, message *queuepb.QueueMessage) error

type Queue interface {
	Publish(ctx context.Context, message *queuepb.QueueMessage) error
	Subscribe(ctx context.Context, handler MessageHandler) error
	CreateQueue(ctx context.Context, config *queuepb.QueueConfig) error
	DeleteQueue(ctx context.Context, name string) error
	GetQueueInfo(ctx context.Context, name string) (*queuepb.QueueInfo, error)
}

type Scheduler interface {
	ScheduleJob(ctx context.Context, job *jobs.Job) error
	CancelJob(ctx context.Context, jobID string) error
	GetJobStatus(ctx context.Context, jobID string) (*jobs.JobStatus, error)
}
