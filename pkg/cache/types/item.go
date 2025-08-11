// file: pkg/cache/types/item.go
// version: 1.0.0
// guid: a3b4c5d6-e7f8-49a0-b1c2-d3e4f5a6b7c8

package types

import "time"

// CacheItem represents a cache item for bulk operations.
type CacheItem struct {
	Value any
	TTL   time.Duration
}
