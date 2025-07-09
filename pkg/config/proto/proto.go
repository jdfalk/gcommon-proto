// file: pkg/config/proto/proto.go

// Package configpb provides consolidated exports for config protobuf types
package configpb

// Re-export types from various config protobuf packages for backwards compatibility
import (
	configpb_requests "github.com/jdfalk/gcommon/pkg/config/proto/requests"
)

// Request types
type (
	GetConfigRequest = configpb_requests.GetConfigRequest
)
