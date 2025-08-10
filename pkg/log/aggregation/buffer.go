// file: pkg/log/aggregation/buffer.go
// version: 1.0.0
// guid: d3e4f5a6-b7c8-49d0-1e2f-3456789012ef

package aggregation

import (
	"context"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/log"
)

// Buffer temporarily stores log entries before forwarding.
type Buffer struct {
	mu       sync.Mutex
	entries  []log.LogEntry
	capacity int
	flush    func(context.Context, []log.LogEntry)
}

// NewBuffer creates a Buffer with a capacity and flush function.
func NewBuffer(cap int, flush func(context.Context, []log.LogEntry)) *Buffer {
	return &Buffer{entries: make([]log.LogEntry, 0, cap), capacity: cap, flush: flush}
}

// Add stores an entry and flushes if capacity is reached.
func (b *Buffer) Add(ctx context.Context, entry log.LogEntry) {
	b.mu.Lock()
	b.entries = append(b.entries, entry)
	if len(b.entries) >= b.capacity {
		entries := b.entries
		b.entries = make([]log.LogEntry, 0, b.capacity)
		b.mu.Unlock()
		b.flush(ctx, entries)
		return
	}
	b.mu.Unlock()
}

// Flush forces the buffer to flush all entries.
func (b *Buffer) Flush(ctx context.Context) {
	b.mu.Lock()
	entries := b.entries
	b.entries = make([]log.LogEntry, 0, b.capacity)
	b.mu.Unlock()
	if len(entries) > 0 {
		b.flush(ctx, entries)
	}
}

// AutoFlush periodically flushes the buffer using the provided interval.
func (b *Buffer) AutoFlush(ctx context.Context, interval time.Duration) {
	ticker := time.NewTicker(interval)
	defer ticker.Stop()
	for {
		select {
		case <-ticker.C:
			b.Flush(ctx)
		case <-ctx.Done():
			return
		}
	}
}
