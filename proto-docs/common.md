# common Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 40
- **Messages**: 30
- **Services**: 0
- **Enums**: 12
- ⚠️ **Issues**: 1

## Files in this Module

- [ack_mode.proto](#ack_mode)
- [audit_log.proto](#audit_log)
- [audit_result.proto](#audit_result)
- [batch_operation.proto](#batch_operation)
- [batch_options.proto](#batch_options)
- [cache_policy.proto](#cache_policy)
- [circuit_breaker_config.proto](#circuit_breaker_config)
- [circuit_breaker_state.proto](#circuit_breaker_state)
- [client_info.proto](#client_info)
- [config_value.proto](#config_value)
- [debug_info.proto](#debug_info)
- [error.proto](#error)
- [error_code.proto](#error_code) ⚠️ 1 issues
- [eviction_policy.proto](#eviction_policy)
- [expiration_policy.proto](#expiration_policy)
- [filter_operation.proto](#filter_operation)
- [filter_options.proto](#filter_options)
- [filter_value.proto](#filter_value)
- [health_status.proto](#health_status)
- [int64_array.proto](#int64_array)
- [key_value.proto](#key_value)
- [metric_point.proto](#metric_point)
- [paginated_response.proto](#paginated_response)
- [pagination.proto](#pagination)
- [pagination_options.proto](#pagination_options)
- [rate_limit.proto](#rate_limit)
- [request_metadata.proto](#request_metadata)
- [resource_reference.proto](#resource_reference)
- [resource_status.proto](#resource_status)
- [response_metadata.proto](#response_metadata)
- [retry_policy.proto](#retry_policy)
- [service_version.proto](#service_version)
- [sort.proto](#sort)
- [sort_direction.proto](#sort_direction)
- [string_array.proto](#string_array)
- [subscription_info.proto](#subscription_info)
- [subscription_options.proto](#subscription_options)
- [subscription_status.proto](#subscription_status)
- [time_range.proto](#time_range)
- [value_type.proto](#value_type)

## Module Dependencies

**This module depends on**:

- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [queue_2](./queue_2.md)

**Modules that depend on this one**:

- [auth](./auth.md)
- [auth_api_1](./auth_api_1.md)
- [auth_api_2](./auth_api_2.md)
- [auth_api_3](./auth_api_3.md)
- [cache](./cache.md)
- [cache_api_1](./cache_api_1.md)
- [cache_api_2](./cache_api_2.md)
- [cache_config](./cache_config.md)
- [config_2](./config_2.md)
- [config_api](./config_api.md)
- [config_config_1](./config_config_1.md)
- [config_config_2](./config_config_2.md)
- [config_events](./config_events.md)
- [database](./database.md)
- [database_api](./database_api.md)
- [health](./health.md)
- [log](./log.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [metrics_api_1](./metrics_api_1.md)
- [metrics_api_2](./metrics_api_2.md)
- [metrics_config](./metrics_config.md)
- [notification](./notification.md)
- [organization](./organization.md)
- [organization_api_1](./organization_api_1.md)
- [organization_api_2](./organization_api_2.md)
- [organization_config](./organization_config.md)
- [queue_2](./queue_2.md)
- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [queue_config](./queue_config.md)
- [queue_services](./queue_services.md)
- [web_api_1](./web_api_1.md)
- [web_api_2](./web_api_2.md)
- [web_api_3](./web_api_3.md)
- [web_config_1](./web_config_1.md)
- [web_events](./web_events.md)

---

## Detailed Documentation

### ack_mode.proto {#ack_mode}

**Path**: `pkg/common/proto/ack_mode.proto` **Package**: `gcommon.v1.common`
**Lines**: 29

**Enums** (1): `AckMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/ack_mode.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Acknowledgment mode enumeration for message processing.
 * Defines how message acknowledgments are handled in streaming operations,
 * queue processing, and event handling across all GCommon modules.
 */
enum AckMode {
  // Default value indicating no acknowledgment mode was specified
  ACK_MODE_UNSPECIFIED = 0;

  // Manual acknowledgment - client must explicitly acknowledge messages
  ACK_MODE_MANUAL = 1;

  // Automatic acknowledgment - messages are acknowledged upon delivery
  ACK_MODE_AUTO = 2;

  // Client-side acknowledgment - acknowledgment is handled by client logic
  ACK_MODE_CLIENT = 3;
}

```

---

### audit_log.proto {#audit_log}

**Path**: `pkg/common/proto/audit_log.proto` **Package**: `gcommon.v1.common`
**Lines**: 50

**Messages** (1): `AuditLog`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_result.proto`
- `pkg/common/proto/resource_reference.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/audit_log.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_result.proto";
import "pkg/common/proto/resource_reference.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Audit log entry for tracking operations and security events.
 * Provides comprehensive audit trail with user identification,
 * action details, and contextual metadata for compliance and debugging.
 */
message AuditLog {
  // Unique audit log entry identifier
  string id = 1;

  // User identifier who performed the action
  string user_id = 2;

  // Action or operation that was performed
  string action = 3;

  // Resource that was acted upon
  ResourceReference resource = 4;

  // Timestamp when the action occurred
  google.protobuf.Timestamp timestamp = 5;

  // Source IP address of the request
  string source_ip = 6;

  // User agent string from the client
  string user_agent = 7;

  // Additional contextual metadata about the action
  map<string, string> metadata = 8;

  // Result of the action (success, failure, partial)
  AuditResult result = 9;

  // Session identifier if applicable
  string session_id = 10;
}

```

---

### audit_result.proto {#audit_result}

**Path**: `pkg/common/proto/audit_result.proto` **Package**: `gcommon.v1.common`
**Lines**: 29

**Enums** (1): `AuditResult`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/audit_result.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Audit result enumeration for tracking operation outcomes in audit logs.
 * Provides standardized result classification for security and compliance
 * auditing across all GCommon modules.
 */
enum AuditResult {
  // Default value indicating no audit result was specified
  AUDIT_RESULT_UNSPECIFIED = 0;

  // Operation completed successfully
  AUDIT_RESULT_SUCCESS = 1;

  // Operation failed to complete
  AUDIT_RESULT_FAILURE = 2;

  // Operation completed with partial success/failure
  AUDIT_RESULT_PARTIAL = 3;
}

```

---

### batch_operation.proto {#batch_operation}

**Path**: `pkg/common/proto/batch_operation.proto` **Package**:
`gcommon.v1.common` **Lines**: 35

**Messages** (1): `BatchOperation`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/batch_options.proto` →
  [metrics_1](./metrics_1.md#batch_options)
- `pkg/common/proto/request_metadata.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/batch_operation.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/batch_options.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Batch operation wrapper for bulk request processing.
 * Enables efficient processing of multiple operations with
 * configurable parallelism, error handling, and timeout policies.
 */
message BatchOperation {
  // Unique identifier for this batch operation
  string batch_id = 1;

  // Type of operation being performed in batch
  string operation_type = 2;

  // Individual operations within the batch (type-specific)
  repeated google.protobuf.Any operations = 3 [lazy = true];

  // Batch processing configuration options
  BatchOptions options = 4 [lazy = true];

  // Request metadata for tracing and correlation
  RequestMetadata metadata = 5 [lazy = true];
}

```

---

### batch_options.proto {#batch_options}

**Path**: `pkg/common/proto/batch_options.proto` **Package**:
`gcommon.v1.common` **Lines**: 30

**Messages** (1): `BatchOptions`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/batch_options.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Batch processing options for configuring bulk operation behavior.
 * Controls parallelism, error handling, timeout policies, and
 * result handling for efficient batch processing.
 */
message BatchOptions {
  // Maximum number of operations to process in parallel
  int32 max_parallel = 1;

  // Whether to stop processing on the first error encountered
  bool fail_fast = 2;

  // Total timeout for the entire batch operation
  google.protobuf.Duration timeout = 3;

  // Whether to return partial results if timeout is reached
  bool return_partial = 4;
}

```

---

### cache_policy.proto {#cache_policy}

**Path**: `pkg/common/proto/cache_policy.proto` **Package**: `gcommon.v1.common`
**Lines**: 41

**Messages** (1): `CachePolicy`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/eviction_policy.proto`
- `pkg/common/proto/expiration_policy.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/cache_policy.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/eviction_policy.proto";
import "pkg/common/proto/expiration_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Cache policy configuration for cache behavior and performance tuning.
 * Defines expiration, eviction, sizing, and operational policies
 * for consistent cache management across GCommon modules.
 */
message CachePolicy {
  // Cache expiration policy strategy
  ExpirationPolicy expiration = 1;

  // Eviction policy when cache reaches capacity
  EvictionPolicy eviction = 2;

  // Maximum cache size in bytes (0 for unlimited)
  int64 max_size_bytes = 3;

  // Maximum number of cache entries (0 for unlimited)
  int64 max_entries = 4;

  // Default time-to-live for cache entries
  google.protobuf.Duration default_ttl = 5;

  // Whether to refresh entries before they expire
  bool refresh_ahead = 6;

  // Whether to collect and expose cache statistics
  bool enable_stats = 7;
}

```

---

### circuit_breaker_config.proto {#circuit_breaker_config}

**Path**: `pkg/common/proto/circuit_breaker_config.proto` **Package**:
`gcommon.v1.common` **Lines**: 37

**Messages** (1): `CircuitBreakerConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/circuit_breaker_state.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/circuit_breaker_config.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/circuit_breaker_state.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Circuit breaker configuration for fault tolerance and system protection.
 * Implements the circuit breaker pattern with configurable thresholds,
 * timeouts, and state management for preventing cascade failures.
 */
message CircuitBreakerConfig {
  // Number of consecutive failures to trigger circuit opening
  int32 failure_threshold = 1;

  // Number of consecutive successes to close the circuit
  int32 success_threshold = 2;

  // Duration to keep circuit open before attempting half-open
  google.protobuf.Duration timeout = 3;

  // Maximum concurrent requests allowed in half-open state
  int32 max_requests = 4;

  // Time window for counting failures and successes
  google.protobuf.Duration window_size = 5;

  // Current state of the circuit breaker
  CircuitBreakerState state = 6;
}

```

---

### circuit_breaker_state.proto {#circuit_breaker_state}

**Path**: `pkg/common/proto/circuit_breaker_state.proto` **Package**:
`gcommon.v1.common` **Lines**: 29

**Enums** (1): `CircuitBreakerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/circuit_breaker_state.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Circuit breaker state enumeration for fault tolerance patterns.
 * Defines the current state of circuit breaker components used
 * for resilience and stability across all GCommon modules.
 */
enum CircuitBreakerState {
  // Default value indicating no circuit breaker state was specified
  CIRCUIT_BREAKER_STATE_UNSPECIFIED = 0;

  // Circuit is closed - requests are flowing normally
  CIRCUIT_BREAKER_STATE_CLOSED = 1;

  // Circuit is open - requests are blocked due to failures
  CIRCUIT_BREAKER_STATE_OPEN = 2;

  // Circuit is half-open - testing if service has recovered
  CIRCUIT_BREAKER_STATE_HALF_OPEN = 3;
}

```

---

### client_info.proto {#client_info}

**Path**: `pkg/common/proto/client_info.proto` **Package**: `gcommon.v1.common`
**Lines**: 32

**Messages** (1): `ClientInfo`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/client_info.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Client information for request identification and monitoring.
 * Provides standardized client metadata for logging, analytics,
 * and security purposes across all GCommon modules.
 */
message ClientInfo {
  // Client application name (e.g., "mobile-app", "web-frontend")
  string name = 1;

  // Client version using semantic versioning (e.g., "1.2.3")
  string version = 2;

  // Client IP address (IPv4 or IPv6)
  string ip_address = 3;

  // User agent string for web clients or application identifier
  string user_agent = 4;

  // Platform information (e.g., "iOS 15.0", "Chrome 95", "Go 1.19")
  string platform = 5;
}

```

---

### config_value.proto {#config_value}

**Path**: `pkg/common/proto/config_value.proto` **Package**: `gcommon.v1.common`
**Lines**: 49

**Messages** (1): `ConfigValue`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/value_type.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/config_value.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/value_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Configuration value with type information and metadata.
 * Supports multiple value types with encryption and validation capabilities
 * for secure and type-safe configuration management.
 */
message ConfigValue {
  // The configuration value (one of the supported types)
  oneof value {
    // String value for text configuration
    string string_value = 1;

    // Integer value for numeric configuration
    int64 int_value = 2;

    // Double value for floating-point configuration
    double double_value = 3;

    // Boolean value for true/false configuration
    bool bool_value = 4;

    // Binary data for complex configuration
    bytes bytes_value = 5;

    // Any protobuf message for structured configuration
    google.protobuf.Any any_value = 6 [lazy = true];
  }

  // Value type for validation and serialization
  ValueType type = 7;

  // Whether the value is encrypted at rest
  bool encrypted = 8;

  // Additional metadata about the configuration value
  map<string, string> metadata = 9 [lazy = true];
}

```

---

### debug_info.proto {#debug_info}

**Path**: `pkg/common/proto/debug_info.proto` **Package**: `gcommon.v1.common`
**Lines**: 37

**Messages** (1): `DebugInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/debug_info.proto
// version: 1.0.0
// guid: 5cfc62b5-b458-4d97-bf91-b5a1c3eccadf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * DebugInfo provides supplemental debugging information
 * that can be included in request or response messages.
 * It captures contextual details useful for tracing and
 * troubleshooting complex issues.
 */
message DebugInfo {
  // Service or component name emitting this debug info
  string service = 1;

  // Optional method or operation identifier
  string method = 2;

  // Time when this debug info was generated
  google.protobuf.Timestamp timestamp = 3;

  // Arbitrary key/value details for debugging
  map<string, string> details = 4;

  // Additional tags to categorize or filter debug entries
  repeated string tags = 5;
}

```

---

### error.proto {#error}

**Path**: `pkg/common/proto/error.proto` **Package**: `gcommon.v1.common`
**Lines**: 37

**Messages** (1): `Error`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error_code.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/error.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error_code.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common error message structure for standardized error handling.
 * Provides comprehensive error information including code, message,
 * debugging details, and traceability across all GCommon modules.
 */
message Error {
  // Standardized error code for programmatic handling
  ErrorCode code = 1;

  // Human-readable error message describing what went wrong
  string message = 2;

  // Additional error details for debugging and troubleshooting
  map<string, string> details = 3;

  // Distributed trace ID for request correlation across services
  string trace_id = 4;

  // Timestamp when the error occurred
  google.protobuf.Timestamp timestamp = 5;

  // Source module or component that generated the error
  string source = 6;
}

```

---

### error_code.proto {#error_code}

**Path**: `pkg/common/proto/error_code.proto` **Package**: `gcommon.v1.common`
**Lines**: 63

**Enums** (1): `ErrorCode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 57: Implementation needed - // Operation is not implemented or not
  supported

#### Source Code

```protobuf
// file: pkg/common/proto/enums/error_code.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Standardized error codes following gRPC conventions.
 * These codes provide consistent error handling across all GCommon modules.
 *
 * Each error code maps to standard gRPC status codes for cross-language compatibility.
 */
enum ErrorCode {
  // Default value indicating no error code was specified
  ERROR_CODE_UNSPECIFIED = 0;

  // Client specified an invalid argument. Request should not be retried without modification
  ERROR_CODE_INVALID_ARGUMENT = 1;

  // Some requested entity was not found
  ERROR_CODE_NOT_FOUND = 2;

  // The entity that a client attempted to create already exists
  ERROR_CODE_ALREADY_EXISTS = 3;

  // The caller does not have permission to execute the specified operation
  ERROR_CODE_PERMISSION_DENIED = 4;

  // The request does not have valid authentication credentials
  ERROR_CODE_UNAUTHENTICATED = 5;

  // Internal server error. Client should not retry
  ERROR_CODE_INTERNAL = 6;

  // The service is currently unavailable. Client may retry
  ERROR_CODE_UNAVAILABLE = 7;

  // Deadline expired before operation could complete
  ERROR_CODE_TIMEOUT = 8;

  // Resource has been exhausted (e.g., quota exceeded)
  ERROR_CODE_RESOURCE_EXHAUSTED = 9;

  // Operation was rejected because the system is not in required state
  ERROR_CODE_FAILED_PRECONDITION = 10;

  // The operation was aborted, typically due to concurrency issue
  ERROR_CODE_ABORTED = 11;

  // Operation was attempted past the valid range
  ERROR_CODE_OUT_OF_RANGE = 12;

  // Operation is not implemented or not supported
  ERROR_CODE_UNIMPLEMENTED = 13;

  // Unrecoverable data loss or corruption
  ERROR_CODE_DATA_LOSS = 14;
}

```

---

### eviction_policy.proto {#eviction_policy}

**Path**: `pkg/common/proto/eviction_policy.proto` **Package**:
`gcommon.v1.common` **Lines**: 32

**Enums** (1): `EvictionPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/eviction_policy.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Cache eviction policy enumeration for cache management.
 * Defines which cached items should be removed when cache capacity
 * is reached across all GCommon modules.
 */
enum EvictionPolicy {
  // Default value indicating no eviction policy was specified
  EVICTION_POLICY_UNSPECIFIED = 0;

  // Least Recently Used - evict items that haven't been accessed recently
  EVICTION_POLICY_LRU = 1;

  // Least Frequently Used - evict items that are accessed least often
  EVICTION_POLICY_LFU = 2;

  // First In, First Out - evict items in order they were added
  EVICTION_POLICY_FIFO = 3;

  // Random eviction - evict randomly selected items
  EVICTION_POLICY_RANDOM = 4;
}

```

---

### expiration_policy.proto {#expiration_policy}

**Path**: `pkg/common/proto/expiration_policy.proto` **Package**:
`gcommon.v1.common` **Lines**: 32

**Enums** (1): `ExpirationPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/expiration_policy.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Cache expiration policy enumeration for cache management.
 * Defines how cached items expire and when they should be evicted
 * from cache storage across all GCommon modules.
 */
enum ExpirationPolicy {
  // Default value indicating no expiration policy was specified
  EXPIRATION_POLICY_UNSPECIFIED = 0;

  // Time-to-live based expiration - items expire after a fixed duration
  EXPIRATION_POLICY_TTL = 1;

  // Idle time expiration - items expire after being unused for a duration
  EXPIRATION_POLICY_IDLE = 2;

  // Write time expiration - items expire after a duration from last write
  EXPIRATION_POLICY_WRITE = 3;

  // Never expire - items remain in cache until explicitly removed
  EXPIRATION_POLICY_NEVER = 4;
}

```

---

### filter_operation.proto {#filter_operation}

**Path**: `pkg/common/proto/filter_operation.proto` **Package**:
`gcommon.v1.common` **Lines**: 53

**Enums** (1): `FilterOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/filter_operation.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Filter operation types for query filtering across all GCommon modules.
 * Provides standardized filtering operations for database queries, search,
 * and other filtering requirements.
 */
enum FilterOperation {
  // Default value indicating no filter operation was specified
  FILTER_OPERATION_UNSPECIFIED = 0;

  // Exact equality match
  FILTER_OPERATION_EQUALS = 1;

  // Not equal to the specified value
  FILTER_OPERATION_NOT_EQUALS = 2;

  // Greater than the specified value (numeric/date comparison)
  FILTER_OPERATION_GREATER_THAN = 3;

  // Less than the specified value (numeric/date comparison)
  FILTER_OPERATION_LESS_THAN = 4;

  // Greater than or equal to the specified value
  FILTER_OPERATION_GREATER_THAN_OR_EQUAL = 5;

  // Less than or equal to the specified value
  FILTER_OPERATION_LESS_THAN_OR_EQUAL = 6;

  // Contains the specified substring (case-sensitive)
  FILTER_OPERATION_CONTAINS = 7;

  // Starts with the specified prefix
  FILTER_OPERATION_STARTS_WITH = 8;

  // Ends with the specified suffix
  FILTER_OPERATION_ENDS_WITH = 9;

  // Value is contained in the specified list
  FILTER_OPERATION_IN = 10;

  // Value is not contained in the specified list
  FILTER_OPERATION_NOT_IN = 11;
}

```

---

### filter_options.proto {#filter_options}

**Path**: `pkg/common/proto/filter_options.proto` **Package**:
`gcommon.v1.common` **Lines**: 30

**Messages** (1): `FilterOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/filter_value.proto`
- `pkg/common/proto/time_range.proto` → [metrics_2](./metrics_2.md#time_range) →
  [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/common/proto/messages/filter_options.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/filter_value.proto";
import "pkg/common/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common filtering options for search and query operations.
 * Provides a unified interface for filtering data across all GCommon modules.
 *
 * Supports field-based filters, text search, and time range filtering,
 * enabling flexible and powerful query capabilities.
 */
message FilterOptions {
  // Field-based filters with typed values and operations
  map<string, FilterValue> filters = 1;

  // Full-text search query for text-based filtering
  string search_query = 2;

  // Time range filter for temporal data
  TimeRange time_range = 3;
}

```

---

### filter_value.proto {#filter_value}

**Path**: `pkg/common/proto/filter_value.proto` **Package**: `gcommon.v1.common`
**Lines**: 46

**Messages** (1): `FilterValue`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/filter_operation.proto`
- `pkg/common/proto/int64_array.proto`
- `pkg/common/proto/string_array.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/filter_value.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/filter_operation.proto";
import "pkg/common/proto/int64_array.proto";
import "pkg/common/proto/string_array.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Filter value with multiple type support and operation specification.
 * Enables type-safe filtering with various data types and comparison operations.
 *
 * Supports scalar values (string, int, double, bool) and array values
 * for IN/NOT_IN operations, with explicit operation specification.
 */
message FilterValue {
  // The value to filter by (one of the supported types)
  oneof value {
    // String value for text-based filtering
    string string_value = 1;

    // Integer value for numeric filtering
    int64 int_value = 2;

    // Double value for floating-point filtering
    double double_value = 3;

    // Boolean value for true/false filtering
    bool bool_value = 4;

    // Array of strings for multi-value filtering
    StringArray string_array = 5 [lazy = true];

    // Array of integers for multi-value filtering
    Int64Array int_array = 6 [lazy = true];
  }

  // Filter operation type (equals, contains, greater than, etc.)
  FilterOperation operation = 7;
}

```

---

### health_status.proto {#health_status}

**Path**: `pkg/common/proto/health_status.proto` **Package**:
`gcommon.v1.common` **Lines**: 34

**Enums** (1): `HealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/health_status.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common health status enumeration used across all GCommon modules.
 * Provides consistent health reporting for services, components, and resources.
 */
enum HealthStatus {
  // Default value indicating health status was not specified
  HEALTH_STATUS_UNSPECIFIED = 0;

  // Service/component is operating normally
  HEALTH_STATUS_HEALTHY = 1;

  // Service/component is not functioning properly
  HEALTH_STATUS_UNHEALTHY = 2;

  // Service/component is partially functioning with degraded performance
  HEALTH_STATUS_DEGRADED = 3;

  // Service/component is in the process of starting up
  HEALTH_STATUS_STARTING = 4;

  // Service/component is in the process of shutting down
  HEALTH_STATUS_STOPPING = 5;
}

```

---

### int64_array.proto {#int64_array}

**Path**: `pkg/common/proto/int64_array.proto` **Package**: `gcommon.v1.common`
**Lines**: 20

**Messages** (1): `Int64Array`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/int64_array.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Int64 array wrapper for oneof usage in filter values and other contexts.
 * Required because oneof fields cannot directly contain repeated types,
 * so arrays must be wrapped in a message.
 */
message Int64Array {
  // Array of 64-bit signed integer values
  repeated int64 values = 1;
}

```

---

### key_value.proto {#key_value}

**Path**: `pkg/common/proto/key_value.proto` **Package**: `gcommon.v1.common`
**Lines**: 23

**Messages** (1): `KeyValue`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/key_value.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Generic key-value pair for metadata and configuration storage.
 * Provides a simple, reusable structure for storing arbitrary
 * string-based key-value data across all GCommon modules.
 */
message KeyValue {
  // The key identifier for this pair
  string key = 1;

  // The value associated with the key
  string value = 2;
}

```

---

### metric_point.proto {#metric_point}

**Path**: `pkg/common/proto/metric_point.proto` **Package**: `gcommon.v1.common`
**Lines**: 33

**Messages** (1): `MetricPoint`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/metric_point.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common metrics data point for standardized metric collection.
 * Provides a unified structure for metrics across all GCommon modules
 * with timestamp, labels, and unit information for observability.
 */
message MetricPoint {
  // Metric name identifier (e.g., "request_count", "response_time")
  string name = 1;

  // Numeric value of the metric
  double value = 2;

  // Timestamp when the metric was recorded
  google.protobuf.Timestamp timestamp = 3;

  // Key-value labels for metric dimensions and filtering
  map<string, string> labels = 4;

  // Unit of measurement (e.g., "seconds", "bytes", "requests")
  string unit = 5;
}

```

---

### paginated_response.proto {#paginated_response}

**Path**: `pkg/common/proto/paginated_response.proto` **Package**:
`gcommon.v1.common` **Lines**: 35

**Messages** (1): `PaginatedResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/paginated_response.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Standard pagination response metadata for list operations.
 * Provides comprehensive pagination information to clients for
 * implementing pagination controls and navigation.
 */
message PaginatedResponse {
  // Opaque token for retrieving the next page (empty if no more pages)
  string next_page_token = 1;

  // Opaque token for retrieving the previous page (empty if first page)
  string prev_page_token = 2;

  // Total number of items across all pages (may be expensive to compute)
  int32 total_count = 3;

  // Current page number (starts from 1)
  int32 current_page = 4;

  // Total number of pages available
  int32 total_pages = 5;

  // Number of items in the current page
  int32 page_size = 6;
}

```

---

### pagination.proto {#pagination}

**Path**: `pkg/common/proto/pagination.proto` **Package**: `gcommon.v1.common`
**Lines**: 26

**Messages** (1): `Pagination`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/pagination.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common pagination parameters for list operations.
 * Provides standardized pagination controls for queries and lists
 * across all GCommon modules to ensure consistent behavior.
 */
message Pagination {
  // Maximum number of items to return in a single page (0 means use server default)
  int32 page_size = 1;

  // Opaque token for retrieving the next page (empty for first page)
  string page_token = 2;

  // Optional: specific page number (alternative to page_token for simple pagination)
  int32 page_number = 3;
}

```

---

### pagination_options.proto {#pagination_options}

**Path**: `pkg/common/proto/pagination_options.proto` **Package**:
`gcommon.v1.common` **Lines**: 22

**Messages** (1): `PaginationOptions`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/pagination_options.proto
// version: 1.1.0
// guid: 5c1c9ffd-3554-4f8b-91d6-82d7a453683f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

// PaginationOptions defines standard paging parameters.
message PaginationOptions {
  // Maximum number of items to return.
  int32 page_size = 1;

  // Opaque token representing the next page.
  string page_token = 2;
}

```

---

### rate_limit.proto {#rate_limit}

**Path**: `pkg/common/proto/rate_limit.proto` **Package**: `gcommon.v1.common`
**Lines**: 30

**Messages** (1): `RateLimit`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/rate_limit.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Rate limiting information for API throttling and quota management.
 * Provides current rate limit status and reset timing information
 * for client-side rate limit handling and backoff strategies.
 */
message RateLimit {
  // Maximum number of requests allowed per time window
  int32 limit = 1;

  // Duration of the time window for rate limiting
  google.protobuf.Duration window = 2;

  // Number of requests remaining in the current window
  int32 remaining = 3;

  // Time until the rate limit window resets
  google.protobuf.Duration reset_time = 4;
}

```

---

### request_metadata.proto {#request_metadata}

**Path**: `pkg/common/proto/request_metadata.proto` **Package**:
`gcommon.v1.common` **Lines**: 40

**Messages** (1): `RequestMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/client_info.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/request_metadata.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/client_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common request metadata for observability and security.
 * Provides standardized metadata that should be included with all
 * requests for distributed tracing, monitoring, and security auditing.
 */
message RequestMetadata {
  // Distributed tracing ID for correlating requests across services
  string trace_id = 1;

  // User ID of the authenticated user making the request
  string user_id = 2;

  // Correlation ID for grouping related requests in a workflow
  string correlation_id = 3;

  // HTTP headers or gRPC metadata from the original request
  map<string, string> headers = 4;

  // Client application information
  ClientInfo client = 5;

  // Timestamp when the request was initiated
  google.protobuf.Timestamp timestamp = 6;

  // Session ID if the request is part of a user session
  string session_id = 7;
}

```

---

### resource_reference.proto {#resource_reference}

**Path**: `pkg/common/proto/resource_reference.proto` **Package**:
`gcommon.v1.common` **Lines**: 29

**Messages** (1): `ResourceReference`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/resource_reference.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Resource reference for cross-module operations and relationships.
 * Provides a standardized way to reference resources across different
 * GCommon modules with consistent identification and ownership tracking.
 */
message ResourceReference {
  // Resource type identifier (e.g., "user", "config", "queue", "metric")
  string type = 1;

  // Unique resource identifier within the module
  string id = 2;

  // Human-readable resource name for display purposes
  string name = 3;

  // Module that owns and manages this resource
  string module = 4;
}

```

---

### resource_status.proto {#resource_status}

**Path**: `pkg/common/proto/resource_status.proto` **Package**:
`gcommon.v1.common` **Lines**: 35

**Enums** (1): `ResourceStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/resource_status.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common resource status enumeration used across all GCommon modules.
 * Provides consistent status reporting for various resources like configurations,
 * cache entries, database connections, etc.
 */
enum ResourceStatus {
  // Default value indicating resource status was not specified
  RESOURCE_STATUS_UNSPECIFIED = 0;

  // Resource is active and available for use
  RESOURCE_STATUS_ACTIVE = 1;

  // Resource is inactive but can be activated
  RESOURCE_STATUS_INACTIVE = 2;

  // Resource is pending activation or processing
  RESOURCE_STATUS_PENDING = 3;

  // Resource has been marked for deletion or is deleted
  RESOURCE_STATUS_DELETED = 4;

  // Resource is in an error state and requires attention
  RESOURCE_STATUS_ERROR = 5;
}

```

---

### response_metadata.proto {#response_metadata}

**Path**: `pkg/common/proto/response_metadata.proto` **Package**:
`gcommon.v1.common` **Lines**: 99

**Messages** (3): `ResponseMetadata`, `RateLimitInfo`, `PaginationInfo`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/response_metadata.proto
// version: 1.0.0
// guid: 5a7c8e9f-4b6d-2a1c-9e8d-7c6b5a4e3d2c

// ResponseMetadata message definition for standardized response metadata
//
// This file implements the 1-1-1 pattern: one message per file.
// It defines the standard metadata included in all service responses.

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

// ResponseMetadata provides standardized metadata for all service responses
//
// This message contains common fields that should be included in response
// messages for observability, tracing, and error handling.
message ResponseMetadata {
  // Trace ID from the corresponding request for correlation
  string trace_id = 1;

  // Request ID for unique identification of this specific request
  string request_id = 2;

  // Timestamp when the response was generated
  google.protobuf.Timestamp timestamp = 3;

  // Total processing time for the request
  google.protobuf.Duration processing_time = 4;

  // Service version that processed the request
  string service_version = 5;

  // Success indicator (true if operation succeeded)
  bool success = 6;

  // Error information if the operation failed
  Error error = 7;

  // Additional metadata specific to the response
  map<string, string> metadata = 8;

  // Rate limiting information
  RateLimitInfo rate_limit = 9;

  // Pagination information for list responses
  PaginationInfo pagination = 10;
}

// Rate limiting information in response metadata
message RateLimitInfo {
  // Number of requests remaining in the current window
  int64 remaining = 1;

  // Total requests allowed in the current window
  int64 limit = 2;

  // Time when the current rate limit window resets
  google.protobuf.Timestamp reset_time = 3;

  // Duration until the rate limit resets
  google.protobuf.Duration retry_after = 4;
}

// Pagination information for list responses
message PaginationInfo {
  // Current page number (1-based)
  int32 current_page = 1;

  // Number of items per page
  int32 page_size = 2;

  // Total number of items available
  int64 total_items = 3;

  // Total number of pages available
  int32 total_pages = 4;

  // Whether there is a next page
  bool has_next = 5;

  // Whether there is a previous page
  bool has_previous = 6;

  // Token for retrieving the next page
  string next_page_token = 7;

  // Token for retrieving the previous page
  string previous_page_token = 8;
}

```

---

### retry_policy.proto {#retry_policy}

**Path**: `pkg/common/proto/retry_policy.proto` **Package**: `gcommon.v1.common`
**Lines**: 40

**Messages** (1): `RetryPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error_code.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/retry_policy.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error_code.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Retry policy configuration for resilient operation handling.
 * Defines retry behavior with exponential backoff, jitter,
 * and configurable error handling for robust service interactions.
 */
message RetryPolicy {
  // Maximum number of retry attempts (including initial attempt)
  int32 max_attempts = 1;

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 2;

  // Maximum delay between retry attempts
  google.protobuf.Duration max_delay = 3;

  // Multiplier for exponential backoff (e.g., 2.0 for doubling)
  double backoff_multiplier = 4;

  // Whether to add random jitter to retry timing
  bool enable_jitter = 5;

  // List of error codes that should trigger retries
  repeated ErrorCode retryable_errors = 6;

  // Total timeout for all retry attempts combined
  google.protobuf.Duration total_timeout = 7;
}

```

---

### service_version.proto {#service_version}

**Path**: `pkg/common/proto/service_version.proto` **Package**:
`gcommon.v1.common` **Lines**: 33

**Messages** (1): `ServiceVersion`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/service_version.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Service version information for deployment tracking and compatibility.
 * Provides comprehensive build and version metadata for service
 * identification, debugging, and compatibility checking.
 */
message ServiceVersion {
  // Service name identifier
  string name = 1;

  // Semantic version string (e.g., "1.2.3")
  string version = 2;

  // Git commit hash used for the build
  string commit = 3;

  // Timestamp when the service was built
  google.protobuf.Timestamp build_time = 4;

  // Go version used for compilation
  string go_version = 5;
}

```

---

### sort.proto {#sort}

**Path**: `pkg/common/proto/sort.proto` **Package**: `gcommon.v1.common`
**Lines**: 26

**Messages** (1): `SortOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/sort_direction.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/sort.proto
// version: 1.1.0
// guid: 34507f56-8bd2-4dd8-af7e-c9045ddbf029

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/sort_direction.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Sort options for configuring list sorting.
 * Defines field and direction for sorting operations.
 */
message SortOptions {
  // Field to sort by
  string sort_field = 1;

  // Sort direction
  SortDirection direction = 2;
}

```

---

### sort_direction.proto {#sort_direction}

**Path**: `pkg/common/proto/sort_direction.proto` **Package**:
`gcommon.v1.common` **Lines**: 28

**Enums** (1): `SortDirection`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/sort_direction.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Sort direction enumeration.
 * Defines ascending or descending order for sorting operations.
 */
enum SortDirection {
  // Unspecified sort direction
  SORT_DIRECTION_UNSPECIFIED = 0;

  // Ascending order (A-Z, 0-9, oldest-newest)
  SORT_DIRECTION_ASC = 1;

  // Descending order (Z-A, 9-0, newest-oldest)
  SORT_DIRECTION_DESC = 2;
}

```

---

### string_array.proto {#string_array}

**Path**: `pkg/common/proto/string_array.proto` **Package**: `gcommon.v1.common`
**Lines**: 20

**Messages** (1): `StringArray`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/string_array.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * String array wrapper for oneof usage in filter values and other contexts.
 * Required because oneof fields cannot directly contain repeated types,
 * so arrays must be wrapped in a message.
 */
message StringArray {
  // Array of string values
  repeated string values = 1;
}

```

---

### subscription_info.proto {#subscription_info}

**Path**: `pkg/common/proto/subscription_info.proto` **Package**:
`gcommon.v1.common` **Lines**: 43

**Messages** (1): `SubscriptionInfo`

**Imports** (6):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/client_info.proto`
- `pkg/common/proto/filter_options.proto`
- `pkg/common/proto/subscription_options.proto`
- `pkg/common/proto/subscription_status.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/subscription_info.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/client_info.proto";
import "pkg/common/proto/filter_options.proto";
import "pkg/common/proto/subscription_options.proto";
import "pkg/common/proto/subscription_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Subscription information for streaming and event-driven operations.
 * Manages long-lived subscriptions with filtering, time ranges,
 * and client-specific configuration for real-time data streaming.
 */
message SubscriptionInfo {
  // Unique identifier for this subscription
  string subscription_id = 1;

  // Filter criteria for subscription events
  FilterOptions filter = 2;

  // When the subscription started
  google.protobuf.Timestamp start_time = 3;

  // Optional end time for the subscription (null for indefinite)
  google.protobuf.Timestamp end_time = 4;

  // Information about the subscribing client
  ClientInfo subscriber = 5;

  // Subscription configuration options
  SubscriptionOptions options = 6;

  // Current status of the subscription
  SubscriptionStatus status = 7;
}

```

---

### subscription_options.proto {#subscription_options}

**Path**: `pkg/common/proto/subscription_options.proto` **Package**:
`gcommon.v1.common` **Lines**: 31

**Messages** (1): `SubscriptionOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/ack_mode.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/messages/subscription_options.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/ack_mode.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Subscription options for configuring streaming behavior.
 * Controls historical data inclusion, batching, acknowledgment,
 * and keep-alive settings for optimal streaming performance.
 */
message SubscriptionOptions {
  // Whether to include historical data in the subscription
  bool include_history = 1;

  // Maximum number of events to batch together
  int32 max_batch_size = 2;

  // Acknowledgment mode for message delivery
  AckMode ack_mode = 3;

  // Keep-alive interval to maintain connection
  google.protobuf.Duration keep_alive = 4;
}

```

---

### subscription_status.proto {#subscription_status}

**Path**: `pkg/common/proto/subscription_status.proto` **Package**:
`gcommon.v1.common` **Lines**: 32

**Enums** (1): `SubscriptionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/subscription_status.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Subscription status enumeration for streaming operations.
 * Provides consistent status tracking for event subscriptions, data streams,
 * and real-time updates across all GCommon modules.
 */
enum SubscriptionStatus {
  // Default value indicating no subscription status was specified
  SUBSCRIPTION_STATUS_UNSPECIFIED = 0;

  // Subscription is active and receiving events
  SUBSCRIPTION_STATUS_ACTIVE = 1;

  // Subscription is temporarily paused
  SUBSCRIPTION_STATUS_PAUSED = 2;

  // Subscription has been cancelled by client or system
  SUBSCRIPTION_STATUS_CANCELLED = 3;

  // Subscription is in an error state
  SUBSCRIPTION_STATUS_ERROR = 4;
}

```

---

### time_range.proto {#time_range}

**Path**: `pkg/common/proto/time_range.proto` **Package**: `gcommon.v1.common`
**Lines**: 24

**Messages** (1): `TimeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/types/time_range.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Common time range specification for filtering operations.
 * Provides standardized time-based filtering across all GCommon modules
 * for queries, reports, and data analysis.
 */
message TimeRange {
  // Start time (inclusive) - operations at or after this time are included
  google.protobuf.Timestamp start_time = 1;

  // End time (exclusive) - operations before this time are included
  google.protobuf.Timestamp end_time = 2;
}

```

---

### value_type.proto {#value_type}

**Path**: `pkg/common/proto/value_type.proto` **Package**: `gcommon.v1.common`
**Lines**: 41

**Enums** (1): `ValueType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/common/proto/enums/value_type.proto
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/common/proto";

/**
 * Value type enumeration for configuration values and other typed data.
 * Provides type safety and validation hints for stored values across
 * all GCommon modules.
 */
enum ValueType {
  // Default value indicating no value type was specified
  VALUE_TYPE_UNSPECIFIED = 0;

  // UTF-8 encoded string value
  VALUE_TYPE_STRING = 1;

  // 64-bit signed integer value
  VALUE_TYPE_INT = 2;

  // Double precision floating point value
  VALUE_TYPE_DOUBLE = 3;

  // Boolean true/false value
  VALUE_TYPE_BOOL = 4;

  // Raw binary data
  VALUE_TYPE_BYTES = 5;

  // JSON-formatted string that should be parsed as JSON
  VALUE_TYPE_JSON = 6;

  // YAML-formatted string that should be parsed as YAML
  VALUE_TYPE_YAML = 7;
}

```

---
