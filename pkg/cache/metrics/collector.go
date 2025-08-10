// file: pkg/cache/metrics/collector.go
// version: 1.0.0
// guid: b1c2d3e4-f5a6-47b8-9c0d-1e2f3a4b5c6d

package metrics

import "sync/atomic"

// Collector aggregates cache metrics in memory.
type Collector struct {
	hits   int64
	misses int64
}

// Hit increments the hit counter.
func (c *Collector) Hit() { atomic.AddInt64(&c.hits, 1) }

// Miss increments the miss counter.
func (c *Collector) Miss() { atomic.AddInt64(&c.misses, 1) }

// Stats returns a snapshot of the metrics.
func (c *Collector) Stats() Stats {
	return Stats{Hits: atomic.LoadInt64(&c.hits), Misses: atomic.LoadInt64(&c.misses)}
}
