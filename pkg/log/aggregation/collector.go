// file: pkg/log/aggregation/collector.go
// version: 1.0.0
// guid: b1c2d3e4-f5a6-47b8-9c0d-1234567890cd

package aggregation

import (
	"context"
	"sync"

	"github.com/jdfalk/gcommon/pkg/log"
)

// Collector collects log entries for later processing.
type Collector struct {
	mu      sync.RWMutex
	entries []log.LogEntry
}

// NewCollector creates an empty Collector.
func NewCollector() *Collector {
	return &Collector{entries: make([]log.LogEntry, 0, 128)}
}

// Collect adds an entry to the collector.
func (c *Collector) Collect(_ context.Context, entry log.LogEntry) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.entries = append(c.entries, entry)
}

// Entries returns a copy of collected entries.
func (c *Collector) Entries() []log.LogEntry {
	c.mu.RLock()
	defer c.mu.RUnlock()
	out := make([]log.LogEntry, len(c.entries))
	copy(out, c.entries)
	return out
}

// Reset clears all collected entries.
func (c *Collector) Reset() {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.entries = c.entries[:0]
}
