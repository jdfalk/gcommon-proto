// file: pkg/config/proto/proto.go

// Package proto provides consolidated exports for config protobuf types
package proto

// Re-export types from various config protobuf packages for backwards compatibility
import (
	configpb_requests "github.com/jdfalk/gcommon/pkg/config/proto/requests"
)

// Request types
type (
	GetConfigRequest = configpb_requests.GetConfigRequest
)
