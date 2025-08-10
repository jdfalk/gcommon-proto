// file: pkg/queue/dlq/handler_test.go
// version: 1.0.0
// guid: 69f41a44-0826-4c83-8bf4-963639030c31

package dlq

import (
	"context"
	"testing"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

func TestHandler_AddAndRetrieve(t *testing.T) {
	t.Parallel()
	h := NewHandler()
	msg := &queuepb.QueueMessage{}
	h.Add(context.Background(), msg)

	msgs := h.Messages()
	if len(msgs) != 1 {
		t.Fatalf("expected 1 message, got %d", len(msgs))
	}
	if msgs[0] == nil {
		t.Fatal("expected message")
	}
}
