// file: pkg/cache/metrics/stats.go
// version: 1.0.0
// guid: a0b1c2d3-e4f5-46a7-8b9c-0d1e2f3a4b5c

package metrics

// Stats holds basic cache statistics.
type Stats struct {
	Hits   int64
	Misses int64
}
