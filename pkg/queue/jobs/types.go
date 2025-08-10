// file: pkg/queue/jobs/types.go
// version: 1.0.0
// guid: f432e5bb-0162-495f-9b1c-bf26af2ec4ac

package jobs

import (
	"context"
	"time"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type Job struct {
	ID      string
	Message *queuepb.Message
	RunAt   time.Time
	Handler func(context.Context, *Job) error
}

type JobStatus struct {
	ID        string
	Completed bool
	Error     string
}
