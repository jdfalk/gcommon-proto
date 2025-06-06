// file: pkg/cache/proto/proto.go

// Package proto provides consolidated exports for cache protobuf types
package proto

// Re-export types from various cache protobuf packages for backwards compatibility
import (
	cachepb_messages "github.com/jdfalk/gcommon/pkg/cache/proto/messages"
	cachepb_requests "github.com/jdfalk/gcommon/pkg/cache/proto/requests"
	cachepb_responses "github.com/jdfalk/gcommon/pkg/cache/proto/responses"
)

// Request types
type (
	GetRequest    = cachepb_requests.GetRequest
	SetRequest    = cachepb_requests.SetRequest
	DeleteRequest = cachepb_requests.DeleteRequest
)

// Response types
type (
	GetResponse = cachepb_responses.GetResponse
	SetResponse = cachepb_responses.SetResponse
)

// Message types
type (
	CacheEntry = cachepb_messages.CacheEntry
)
