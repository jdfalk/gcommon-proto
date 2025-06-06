// file: pkg/common/proto/proto.go

// Package proto provides consolidated exports for common protobuf types
package proto

// Re-export types from various common protobuf packages for backwards compatibility
import (
	commonpb_enums "github.com/jdfalk/gcommon/pkg/common/proto/enums"
	commonpb_messages "github.com/jdfalk/gcommon/pkg/common/proto/messages"
	commonpb_types "github.com/jdfalk/gcommon/pkg/common/proto/types"
)

// Message types
type (
	RateLimit        = commonpb_messages.RateLimit
	RequestMetadata  = commonpb_messages.RequestMetadata
	ResponseMetadata = commonpb_messages.ResponseMetadata
	ErrorInfo        = commonpb_messages.ErrorInfo
	AuditLog         = commonpb_messages.AuditLog
	ServiceInfo      = commonpb_messages.ServiceInfo
)

// Type definitions
type (
	KeyValue          = commonpb_types.KeyValue
	StringArray       = commonpb_types.StringArray
	Int64Array        = commonpb_types.Int64Array
	TimeRange         = commonpb_types.TimeRange
	MetricPoint       = commonpb_types.MetricPoint
	ResourceReference = commonpb_types.ResourceReference
	ClientInfo        = commonpb_types.ClientInfo
)

// Enum types
type (
	AuditResult        = commonpb_enums.AuditResult
	FilterOperation    = commonpb_enums.FilterOperation
	ValueType          = commonpb_enums.ValueType
	SubscriptionStatus = commonpb_enums.SubscriptionStatus
	ExpirationPolicy   = commonpb_enums.ExpirationPolicy
	CacheStrategy      = commonpb_enums.CacheStrategy
	MetricType         = commonpb_enums.MetricType
	LogLevel           = commonpb_enums.LogLevel
	ComparisonOperator = commonpb_enums.ComparisonOperator
	FieldType          = commonpb_enums.FieldType
)
