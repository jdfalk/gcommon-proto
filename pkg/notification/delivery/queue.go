// file: pkg/notification/delivery/queue.go
// version: 1.0.0
// guid: aaaabbbb-cccc-dddd-eeee-ffff00000001

package delivery

import (
	"context"

	pb "github.com/jdfalk/gcommon/pkg/notification/proto"
)

// Queue buffers notifications for delivery.
type Queue struct {
	ch chan *pb.NotificationMessage
}

// NewQueue creates a Queue with buffer size.
func NewQueue(size int) *Queue {
	return &Queue{ch: make(chan *pb.NotificationMessage, size)}
}

// Enqueue adds a message to the queue.
func (q *Queue) Enqueue(msg *pb.NotificationMessage) {
	q.ch <- msg
}

// Dequeue removes a message from the queue or returns context error.
func (q *Queue) Dequeue(ctx context.Context) (*pb.NotificationMessage, error) {
	select {
	case msg := <-q.ch:
		return msg, nil
	case <-ctx.Done():
		return nil, ctx.Err()
	}
}
