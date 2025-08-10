// file: pkg/queue/dlq/handler.go
// version: 1.0.0
// guid: 5b333253-6466-44fd-9130-ac2e955735c4

package dlq

import (
	"context"
	"sync"

	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
)

type Handler struct {
	mu       sync.Mutex
	messages []*queuepb.QueueMessage
}

func NewHandler() *Handler {
	return &Handler{}
}

func (h *Handler) Add(_ context.Context, msg *queuepb.QueueMessage) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.messages = append(h.messages, msg)
}

func (h *Handler) Messages() []*queuepb.QueueMessage {
	h.mu.Lock()
	defer h.mu.Unlock()
	return append([]*queuepb.QueueMessage(nil), h.messages...)
}
