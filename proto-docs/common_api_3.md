# common_api_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 40
- **Services**: 0
- **Enums**: 10

## Files in this Module

- [logout_response.proto](#logout_response)
- [mark_as_read_request.proto](#mark_as_read_request)
- [mark_as_read_response.proto](#mark_as_read_response)
- [paginated_response.proto](#paginated_response)
- [queue_alert_severity.proto](#queue_alert_severity)
- [queue_consistency_level.proto](#queue_consistency_level)
- [queue_export_format.proto](#queue_export_format)
- [queue_metric_type.proto](#queue_metric_type)
- [queue_state.proto](#queue_state)
- [queue_type.proto](#queue_type)
- [read_logs_request.proto](#read_logs_request)
- [read_logs_response.proto](#read_logs_response)
- [refresh_token_request.proto](#refresh_token_request)
- [refresh_token_response.proto](#refresh_token_response)
- [register_check_request.proto](#register_check_request)
- [register_check_response.proto](#register_check_response)
- [register_user_request.proto](#register_user_request)
- [register_user_response.proto](#register_user_response)
- [remove_role_request.proto](#remove_role_request)
- [remove_role_response.proto](#remove_role_response)
- [resend_verification_request.proto](#resend_verification_request)
- [reset_health_stats_request.proto](#reset_health_stats_request)
- [reset_health_stats_response.proto](#reset_health_stats_response)
- [reset_password_request.proto](#reset_password_request)
- [reset_password_response.proto](#reset_password_response)
- [restore_point_status.proto](#restore_point_status)
- [restore_point_type.proto](#restore_point_type)
- [revoke_api_key_request.proto](#revoke_api_key_request)
- [revoke_api_key_response.proto](#revoke_api_key_response)
- [revoke_permission_request.proto](#revoke_permission_request)
- [revoke_permission_response.proto](#revoke_permission_response)
- [revoke_role_request.proto](#revoke_role_request)
- [revoke_role_response.proto](#revoke_role_response)
- [revoke_token_request.proto](#revoke_token_request)
- [revoke_token_response.proto](#revoke_token_response)
- [rollback_method.proto](#rollback_method)
- [run_check_request.proto](#run_check_request)
- [run_check_response.proto](#run_check_response)
- [send_notification_request.proto](#send_notification_request)
- [send_notification_response.proto](#send_notification_response)
- [send_verification_email_request.proto](#send_verification_email_request)
- [send_verification_email_response.proto](#send_verification_email_response)
- [set_health_request.proto](#set_health_request)
- [set_health_response.proto](#set_health_response)
- [terminate_session_request.proto](#terminate_session_request)
- [terminate_session_response.proto](#terminate_session_response)
- [unregister_check_request.proto](#unregister_check_request)
- [unregister_check_response.proto](#unregister_check_response)
- [update_action.proto](#update_action)
- [update_permission_request.proto](#update_permission_request)
---


## Detailed Documentation

### logout_response.proto {#logout_response}

**Path**: `gcommon/v1/common/logout_response.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `LogoutResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logout_response.proto
// version: 1.0.1
// guid: 96821169-cc26-45e4-a7e3-b81f44ddeb99

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogoutResponse provides the result of a logout request
message LogoutResponse {
  // Whether the logout was successful
  bool success = 1;

  // Optional error information if logout failed
  gcommon.v1.common.Error error = 2;
}
```

---

### mark_as_read_request.proto {#mark_as_read_request}

**Path**: `gcommon/v1/common/mark_as_read_request.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `MarkAsReadRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mark_as_read_request.proto
// version: 1.0.0
// guid: 106b287f-61f9-4551-8526-53a606fbd0d1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MarkAsReadRequest {
  // Identifier of the notification to mark as read.
  string notification_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### mark_as_read_response.proto {#mark_as_read_response}

**Path**: `gcommon/v1/common/mark_as_read_response.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `MarkAsReadResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mark_as_read_response.proto
// version: 1.0.1
// guid: 1fd2817b-1b04-474f-ba5b-190ee82693bd

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for marking a notification as read.
 */
message MarkAsReadResponse {
  // True if the operation succeeded.
  bool success = 1;
}
```

---

### paginated_response.proto {#paginated_response}

**Path**: `gcommon/v1/common/paginated_response.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `PaginatedResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/paginated_response.proto
// version: 1.0.0
// guid: b51b64d3-29b8-4d03-bde5-dcaeb915a1f2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Standard pagination response metadata for list operations.
 * Provides comprehensive pagination information to clients for
 * implementing pagination controls and navigation.
 */
message PaginatedResponse {
  // Opaque token for retrieving the next page (empty if no more pages)
  string next_page_token = 1 [(buf.validate.field).string.min_len = 1];

  // Opaque token for retrieving the previous page (empty if first page)
  string prev_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total number of items across all pages (may be expensive to compute)
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];

  // Current page number (starts from 1)
  int32 current_page = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total number of pages available
  int32 total_pages = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items in the current page
  int32 page_size = 6 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
}
```

---

### queue_alert_severity.proto {#queue_alert_severity}

**Path**: `gcommon/v1/common/queue_alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `QueueAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alert_severity.proto
// version: 1.0.1
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Alert severity levels.
 */
enum QueueAlertSeverity {
  // Default unspecified severity
  QUEUE_ALERT_SEVERITY_UNSPECIFIED = 0;

  // Informational alert
  QUEUE_ALERT_SEVERITY_INFO = 1;

  // Warning level alert
  QUEUE_ALERT_SEVERITY_WARNING = 2;

  // Error level alert
  QUEUE_ALERT_SEVERITY_ERROR = 3;

  // Critical alert requiring immediate attention
  QUEUE_ALERT_SEVERITY_CRITICAL = 4;
}
```

---

### queue_consistency_level.proto {#queue_consistency_level}

**Path**: `gcommon/v1/common/queue_consistency_level.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `QueueConsistencyLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/consistency_level.proto
// file: proto/gcommon/v1/queue/consistency_level.proto
// version: 1.0.1
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Consistency level for queue operations.
 */
enum QueueConsistencyLevel {
  // Default unspecified consistency level
  QUEUE_CONSISTENCY_LEVEL_UNSPECIFIED = 0;

  // Eventual consistency (fastest, may read stale data)
  QUEUE_CONSISTENCY_LEVEL_EVENTUAL = 1;

  // Weak consistency (balance between speed and consistency)
  QUEUE_CONSISTENCY_LEVEL_WEAK = 2;

  // Strong consistency (slower, guarantees latest data)
  QUEUE_CONSISTENCY_LEVEL_STRONG = 3;

  // Sequential consistency (operations appear in some sequential order)
  QUEUE_CONSISTENCY_LEVEL_SEQUENTIAL = 4;

  // Linearizable consistency (strongest, operations appear instantaneous)
  QUEUE_CONSISTENCY_LEVEL_LINEARIZABLE = 5;
}
```

---

### queue_export_format.proto {#queue_export_format}

**Path**: `gcommon/v1/common/queue_export_format.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `QueueExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/export_format.proto
// file: proto/gcommon/v1/queue/export_format.proto
// version: 1.0.1
// guid: 3a2b1c0d-9e8f-7a6b-5c4d-3e2f1a0b9c8d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Export format options.
 */
enum QueueExportFormat {
  // Default unspecified format
  QUEUE_EXPORT_FORMAT_UNSPECIFIED = 0;

  // JSON format
  QUEUE_EXPORT_FORMAT_JSON = 1;

  // Protocol Buffers binary format
  QUEUE_EXPORT_FORMAT_PROTOBUF = 2;

  // CSV format (metadata only)
  QUEUE_EXPORT_FORMAT_CSV = 3;

  // Custom format
  QUEUE_EXPORT_FORMAT_CUSTOM = 4;
}
```

---

### queue_metric_type.proto {#queue_metric_type}

**Path**: `gcommon/v1/common/queue_metric_type.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `QueueMetricType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/metric_type.proto
// version: 1.0.1
// guid: 8b7a6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MetricType represents the types of metrics that can be monitored.
 * Specifies different types of queue metrics for monitoring and analysis.
 */
enum QueueMetricType {
  // Default unspecified type
  QUEUE_METRIC_TYPE_UNSPECIFIED = 0;

  // Message count
  QUEUE_METRIC_TYPE_MESSAGE_COUNT = 1;

  // Message rate (per second)
  QUEUE_METRIC_TYPE_MESSAGE_RATE = 2;

  // Processing time
  QUEUE_METRIC_TYPE_PROCESSING_TIME = 3;

  // Error rate
  QUEUE_METRIC_TYPE_ERROR_RATE = 4;

  // Consumer count
  QUEUE_METRIC_TYPE_CONSUMER_COUNT = 5;

  // Queue depth
  QUEUE_METRIC_TYPE_QUEUE_DEPTH = 6;
}
```

---

### queue_state.proto {#queue_state}

**Path**: `gcommon/v1/common/queue_state.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `QueueState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_state.proto
// version: 1.0.1
// guid: 8f9a0b1c-2d3e-4f5a-6b7c-8d9e0f1a2b3c
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Represents the operational state of a queue.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum QueueState {
  // Default unknown state
  QUEUE_STATE_UNSPECIFIED = 0;

  // Queue is active and processing messages
  QUEUE_STATE_ACTIVE = 1;

  // Queue is paused (not processing messages but accepting them)
  QUEUE_STATE_PAUSED = 2;

  // Queue is suspended (not accepting new messages)
  QUEUE_STATE_SUSPENDED = 3;

  // Queue is in the process of being deleted
  QUEUE_STATE_DELETING = 4;

  // Queue is in maintenance mode
  QUEUE_STATE_MAINTENANCE = 5;

  // Queue has encountered an error and needs attention
  QUEUE_STATE_ERROR = 6;
}
```

---

### queue_type.proto {#queue_type}

**Path**: `gcommon/v1/common/queue_type.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `QueueType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_type.proto
// version: 1.0.1
// guid: d6bb0e83-91d3-406a-9a66-519b5860d137

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// QueueType enumerates supported queue implementations.
enum QueueType {
  // Default unspecified implementation.
  QUEUE_TYPE_UNSPECIFIED = 0;
  // In-memory queue for testing or lightweight workloads.
  QUEUE_TYPE_MEMORY = 1;
  // Redis-backed queue.
  QUEUE_TYPE_REDIS = 2;
  // NATS-based streaming queue.
  QUEUE_TYPE_NATS = 3;
  // Cloud provider queue (e.g., AWS SQS).
  QUEUE_TYPE_CLOUD = 4;
}
```

---

### read_logs_request.proto {#read_logs_request}

**Path**: `gcommon/v1/common/read_logs_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `ReadLogsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/read_logs_request.proto
// version: 1.0.0
// guid: 9f0e1d2c-3b4a-5867-9e0f-1a2b3c4d5e6f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ReadLogsRequest defines the request for reading log entries.
 */
message ReadLogsRequest {
  // Filter by log level
  string level = 1 [(buf.validate.field).string.min_len = 1];

  // Filter by source
  string source = 2 [(buf.validate.field).string.min_len = 1];

  // Start time for log range
  int64 start_time = 3 [(buf.validate.field).int64.gte = 0];

  // End time for log range
  int64 end_time = 4 [(buf.validate.field).int64.gte = 0];

  // Maximum number of entries to return
  int32 limit = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### read_logs_response.proto {#read_logs_response}

**Path**: `gcommon/v1/common/read_logs_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `ReadLogsResponse`

**Imports** (3):

- `gcommon/v1/common/log_entry.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/read_logs_response.proto
// version: 1.0.0
// guid: 0f1e2d3c-4b5a-6978-0e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/log_entry.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ReadLogsResponse defines the response from reading log entries.
 */
message ReadLogsResponse {
  // Retrieved log entries
  repeated LogEntry entries = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count of matching entries
  int32 total_count = 2 [(buf.validate.field).int32.gte = 0];

  // Error message if any
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### refresh_token_request.proto {#refresh_token_request}

**Path**: `gcommon/v1/common/refresh_token_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `RefreshTokenRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/refresh_token_request.proto
// version: 1.0.0
// guid: b0a6426f-06af-49ad-85eb-2a4eb2bc2de6
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to refresh an access token using a refresh token.
 * Exchanges a valid refresh token for a new access token.
 * Optionally requests new scopes for the refreshed token.
 */
message RefreshTokenRequest {
  // Refresh token to exchange for new access token
  string refresh_token = 1 [(buf.validate.field).string.min_len = 1];

  // Requested scopes for the new access token
  repeated string scopes = 2 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### refresh_token_response.proto {#refresh_token_response}

**Path**: `gcommon/v1/common/refresh_token_response.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `RefreshTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/refresh_token_response.proto
// version: 1.0.0
// guid: 6dee199f-3a40-4f11-8207-16c802534230
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to token refresh request.
 * Contains new access token and potentially new refresh token.
 * Follows OAuth2 token response format.
 */
message RefreshTokenResponse {
  // New access token for API authentication
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // New refresh token (may be the same as input)
  string refresh_token = 2 [(buf.validate.field).string.min_len = 1];

  // Token type (always "Bearer")
  string token_type = 3 [(buf.validate.field).string.min_len = 1];

  // Access token expiration time in seconds
  int32 expires_in = 4 [(buf.validate.field).int32.gte = 0];

  // Granted scopes for the new access token
  repeated string scopes = 5 [(buf.validate.field).repeated.min_items = 1];
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### register_check_request.proto {#register_check_request}

**Path**: `gcommon/v1/common/register_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `RegisterCheckRequest`

**Imports** (4):

- `gcommon/v1/common/health_check_request.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/register_check_request.proto
// version: 1.0.0
// guid: d0def031-b6c4-482c-8e68-7d395ac76697
// file: proto/gcommon/v1/common/register_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_check_request.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RegisterCheckRequest {
  // Service name this check belongs to
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Parameters describing the check to execute
  HealthHealthCheckRequest check = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### register_check_response.proto {#register_check_response}

**Path**: `gcommon/v1/common/register_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `RegisterCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/register_check_response.proto
// version: 1.0.0
// guid: c52bced5-89bc-4021-81d6-491a104872a8
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for health check registration.
 * Contains the result of registering a new health check.
 */
message RegisterCheckResponse {
  // Success status
  bool success = 1;

  // Registered check ID
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information
  gcommon.v1.common.Error error = 3;
}
```

---

### register_user_request.proto {#register_user_request}

**Path**: `gcommon/v1/common/register_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 68

**Messages** (1): `RegisterUserRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/register_user_request.proto
// version: 1.0.0
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to register a new user account.
 * Creates a new user with the provided credentials and profile information.
 */
message RegisterUserRequest {
  // Username for the new account (required)
  string username = 1;

  // Email address for the new account (required)
  string email = 2 [ (buf.validate.field).string.email = true ];

  // Password for the new account (required)
  string password = 3;

  // First name of the user
  string first_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Last name of the user
  string last_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Phone number (optional)
  string phone_number = 6;

  // Initial organization to associate user with (optional)
  string organization_id = 7 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Whether email verification is required
  bool require_email_verification = 8;

  // Invitation token (if registering via invitation)
  string invitation_token = 9;

  // Additional user metadata
  map<string, string> metadata = 10;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Terms of service acceptance timestamp
  int64 tos_accepted_at = 12;

  // Privacy policy acceptance timestamp
  int64 privacy_accepted_at = 13;
}
```

---

### register_user_response.proto {#register_user_response}

**Path**: `gcommon/v1/common/register_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `RegisterUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/register_user_response.proto
// version: 1.0.0
// guid: 5bda08f2-024d-4dfb-8ba4-45b84fe8d4ef
// file: proto/gcommon/v1/common/register_user_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RegisterUserResponse {
  // Registration success
  bool success = 1;

  // User ID of created user
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Whether email verification is required
  bool email_verification_required = 3;

  // Error message if registration failed
  string error_message = 4;

  // Session token if immediate login is allowed
  string session_token = 5;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### remove_role_request.proto {#remove_role_request}

**Path**: `gcommon/v1/common/remove_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `RemoveRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/remove_role_request.proto
// version: 1.0.0
// guid: dfde5734-62db-444c-b390-fda716da06e1
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to remove a role from a user.
 * Used for role-based access control management.
 * Removes the specified role assignment from the user.
 */
message RemoveRoleRequest {
  // User ID to remove role from
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID to remove
  string role_id = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### remove_role_response.proto {#remove_role_response}

**Path**: `gcommon/v1/common/remove_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Messages** (1): `RemoveRoleResponse`

**Imports** (4):

- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/remove_role_response.proto
// version: 1.0.0
// guid: d8f9ff14-27d8-4495-bba6-2a8a944df6be
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RemoveRoleResponse confirms successful role removal from a user.
 * Provides information about the removal operation including
 * the removed role and removal metadata for audit purposes.
 */
message RemoveRoleResponse {
  // User ID from whom the role was removed
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username of the user
  string username = 2;

  // Role that was removed from the user
  Role role = 3;

  // Timestamp when the role was removed
  google.protobuf.Timestamp removed_at = 4;

  // ID of the admin user who performed the removal
  string removed_by_user_id = 5;

  // Username of the admin who performed the removal
  string removed_by_username = 6;

  // Whether this removal was effective immediately
  bool effective_immediately = 7;

  // Whether the user still has other roles assigned
  bool has_remaining_roles = 8;

  // Count of remaining roles for the user
  int32 remaining_role_count = 9;

  // Success message describing the removal
  string message = 10;
}
```

---

### resend_verification_request.proto {#resend_verification_request}

**Path**: `gcommon/v1/common/resend_verification_request.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `ResendVerificationRequest`

**Imports** (3):

- `gcommon/v1/common/verification_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/resend_verification_request.proto
// version: 1.0.0
// guid: 59477f5d-a132-4166-97a0-58e8a4534c3e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/verification_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ResendVerificationRequest {
  // User ID or email address
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Verification type

  AuthVerificationType type = 2;
}
```

---

### reset_health_stats_request.proto {#reset_health_stats_request}

**Path**: `gcommon/v1/common/reset_health_stats_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `ResetHealthStatsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/reset_health_stats_request.proto
// version: 1.0.0
// guid: e8903f7e-5da9-40bf-8b9b-1a6747e1391e
// file: proto/gcommon/v1/common/reset_health_stats_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ResetHealthStatsRequest {
  // Service name whose stats should be reset
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### reset_health_stats_response.proto {#reset_health_stats_response}

**Path**: `gcommon/v1/common/reset_health_stats_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ResetHealthStatsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/reset_health_stats_response.proto
// version: 1.0.0
// guid: 6b989b99-80f9-42fe-8a61-817a735351b1
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for resetting health statistics.
 * Contains the result of clearing stored health metrics and statistics.
 */
message ResetHealthStatsResponse {
  // Success status
  bool success = 1;

  // Number of statistics entries cleared
  int32 cleared_entries = 2 [(buf.validate.field).int32.gte = 0];

  // Reset timestamp
  google.protobuf.Timestamp reset_at = 3;

  // Error information if reset failed
  gcommon.v1.common.Error error = 4;

  // Statistics categories that were reset
  repeated string reset_categories = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### reset_password_request.proto {#reset_password_request}

**Path**: `gcommon/v1/common/reset_password_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `ResetPasswordRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/reset_password_request.proto
// version: 1.0.0
// guid: 79c62bc6-23ed-4b2e-9bb4-4e3091880b22

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ResetPasswordRequest triggers a password reset for a user.
 */
message ResetPasswordRequest {
  // User ID to reset password for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Temporary reset token provided to the user
  string token = 2;

  // New password to set
  string new_password = 3;

  // Metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### reset_password_response.proto {#reset_password_response}

**Path**: `gcommon/v1/common/reset_password_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `ResetPasswordResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/reset_password_response.proto
// version: 1.0.0
// guid: 9de139b4-5d77-49c3-b18b-7cf12ea5c132

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ResetPasswordResponse indicates success or failure of password reset.
 */
message ResetPasswordResponse {
  // Whether the reset was successful
  bool success = 1;

  // Optional message describing the result
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Response metadata for rate limiting and tracing
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### restore_point_status.proto {#restore_point_status}

**Path**: `gcommon/v1/common/restore_point_status.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `RestorePointStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/restore_point_status.proto
// version: 1.0.1
// guid: 83838713-4e8f-494e-93ec-7bdf0b406982

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RestorePointStatus {
  RESTORE_POINT_STATUS_UNSPECIFIED = 0;
  RESTORE_POINT_STATUS_CREATING = 1;
  RESTORE_POINT_STATUS_ACTIVE = 2;
  RESTORE_POINT_STATUS_EXPIRED = 3;
  RESTORE_POINT_STATUS_DELETED = 4;
  RESTORE_POINT_STATUS_ERROR = 5;
}
```

---

### restore_point_type.proto {#restore_point_type}

**Path**: `gcommon/v1/common/restore_point_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `RestorePointType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/restore_point_type.proto
// version: 1.0.1
// guid: 2f531175-07c6-46a3-a5ab-01b240355ab8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RestorePointType {
  RESTORE_POINT_TYPE_UNSPECIFIED = 0;
  RESTORE_POINT_TYPE_MANUAL = 1; // Manually created restore point
  RESTORE_POINT_TYPE_AUTOMATIC = 2; // Automatically created restore point
  RESTORE_POINT_TYPE_SCHEDULED = 3; // Scheduled restore point
  RESTORE_POINT_TYPE_PRE_CHANGE = 4; // Created before configuration change
  RESTORE_POINT_TYPE_MILESTONE = 5; // Milestone restore point
  RESTORE_POINT_TYPE_BACKUP = 6; // Backup restore point
}
```

---

### revoke_api_key_request.proto {#revoke_api_key_request}

**Path**: `gcommon/v1/common/revoke_api_key_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `RevokeApiKeyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/revoke_api_key_request.proto
// version: 1.0.0
// guid: 889f38ad-dde7-41cd-aa20-ec974b0207f1
// file: proto/gcommon/v1/common/revoke_api_key_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokeApiKeyRequest {
  // API key ID to revoke
  string key_id = 1 [(buf.validate.field).string.min_len = 1];

  // Reason for revocation
  string reason = 2 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### revoke_api_key_response.proto {#revoke_api_key_response}

**Path**: `gcommon/v1/common/revoke_api_key_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `RevokeApiKeyResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/revoke_api_key_response.proto
// version: 1.0.0
// guid: 408b6755-7ee3-44e4-80c2-af76cc4cf87b
// file: proto/gcommon/v1/common/revoke_api_key_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokeApiKeyResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Revocation timestamp
  int64 revoked_at = 3 [(buf.validate.field).int64.gte = 0];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### revoke_permission_request.proto {#revoke_permission_request}

**Path**: `gcommon/v1/common/revoke_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `RevokePermissionRequest`

**Imports** (3):

- `gcommon/v1/common/subject_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_permission_request.proto
// version: 1.0.0
// guid: 08a90c9d-4730-427a-b445-35cbadc141a6

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/subject_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokePermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subject type

  AuthSubjectType subject_type = 2;

  // Permission ID to revoke
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### revoke_permission_response.proto {#revoke_permission_response}

**Path**: `gcommon/v1/common/revoke_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `RevokePermissionResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_permission_response.proto
// version: 1.0.0
// guid: f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for permission revocation operations.
 * Indicates whether the permission was successfully revoked.
 */
message RevokePermissionResponse {
  // Whether the permission revocation was successful
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // The revoked permission ID
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];

  // User or entity the permission was revoked from
  string revokee_id = 4 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}
```

---

### revoke_role_request.proto {#revoke_role_request}

**Path**: `gcommon/v1/common/revoke_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 48

**Messages** (1): `RevokeRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_role_request.proto
// version: 1.0.0
// guid: a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to revoke a role from a user.
 * Used for role-based access control management.
 * Removes the specified role permissions from the user.
 */
message RevokeRoleRequest {
  // User ID to revoke role from (required)
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID to revoke (required)
  string role_id = 2;

  // Optional organization context for scoped role revocation
  string organization_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Audit information for tracking who made the revocation
  string revoked_by = 5;

  // Reason for role revocation (optional)
  string reason = 6;

  // Whether to force revocation even if user has dependencies
  bool force = 7;
}
```

---

### revoke_role_response.proto {#revoke_role_response}

**Path**: `gcommon/v1/common/revoke_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `RevokeRoleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/revoke_role_response.proto
// version: 1.0.0
// guid: acfab4c3-a30b-45ba-9590-745f492f55bd
// file: proto/gcommon/v1/common/revoke_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokeRoleResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Remaining permissions after revocation
  repeated string remaining_permissions = 3 [(buf.validate.field).repeated.min_items = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### revoke_token_request.proto {#revoke_token_request}

**Path**: `gcommon/v1/common/revoke_token_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `RevokeTokenRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_token_request.proto
// version: 1.0.0
// guid: 0fc4421f-09e3-4cf7-8e64-d11797c80088
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to revoke a token (access or refresh).
 * Invalidates the specified token and prevents further use.
 * Used for logout operations and security revocation.
 */
message RevokeTokenRequest {
  // Token to revoke (access or refresh token)
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Token type hint ("access_token" or "refresh_token")
  string token_type_hint = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### revoke_token_response.proto {#revoke_token_response}

**Path**: `gcommon/v1/common/revoke_token_response.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Messages** (1): `RevokeTokenResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_token_response.proto
// version: 1.0.0
// guid: f25b7f00-5a70-4776-8dfd-fb942ffd6980
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RevokeTokenResponse confirms successful token revocation.
 * Provides information about the revoked token and revocation timestamp
 * for audit logging and confirmation purposes.
 */
message RevokeTokenResponse {
  // Token ID that was revoked
  string token_id = 1;

  // Type of token that was revoked (access, refresh, etc.)
  string token_type = 2;

  // Timestamp when the token was revoked
  google.protobuf.Timestamp revoked_at = 3;

  // User ID associated with the revoked token
  string user_id = 4 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Reason for revocation (logout, security, expiry, etc.)
  string revocation_reason = 5;

  // Whether this was the last token for the user session
  bool last_token_in_session = 6;
}
```

---

### rollback_method.proto {#rollback_method}

**Path**: `gcommon/v1/common/rollback_method.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `RollbackMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rollback_method.proto
// version: 1.0.1
// guid: b0c1d2e3-f4a5-6b7c-8d9e-0f1a2b3c4d5e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RollbackMethod represents how the rollback was performed.
 * Specifies the technique used to revert configuration changes.
 */
enum RollbackMethod {
  // Unspecified rollback method
  ROLLBACK_METHOD_UNSPECIFIED = 0;

  // Restore individual values
  ROLLBACK_METHOD_VALUE_RESTORE = 1;

  // Restore from version history
  ROLLBACK_METHOD_VERSION_RESTORE = 2;

  // Restore from snapshot
  ROLLBACK_METHOD_SNAPSHOT_RESTORE = 3;

  // Manual rollback process
  ROLLBACK_METHOD_MANUAL = 4;
}
```

---

### run_check_request.proto {#run_check_request}

**Path**: `gcommon/v1/common/run_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `RunCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/run_check_request.proto
// version: 1.0.0
// guid: baa819a3-645e-4309-9473-1bb8bbd18e40
// file: proto/gcommon/v1/common/run_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RunCheckRequest {
  // Name or ID of the check to run
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata used for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### run_check_response.proto {#run_check_response}

**Path**: `gcommon/v1/common/run_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `RunCheckResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/run_check_response.proto
// version: 1.0.0
// guid: 573c89a4-b638-49c8-bb99-29d1e4db5b60
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for manually running a health check.
 * Contains the result of executing a health check on demand.
 */
message RunCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was executed
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Health status result
  gcommon.v1.common.CommonHealthStatus status = 3;

  // Execution timestamp
  google.protobuf.Timestamp executed_at = 4;

  // Execution duration
  google.protobuf.Duration execution_time = 5;

  // Check result message
  string message = 6 [(buf.validate.field).string.min_len = 1];

  // Error information if check failed
  gcommon.v1.common.Error error = 7;
}
```

---

### send_notification_request.proto {#send_notification_request}

**Path**: `gcommon/v1/common/send_notification_request.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `SendNotificationRequest`

**Imports** (3):

- `gcommon/v1/common/notification_message.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/send_notification_request.proto
// version: 1.0.1
// guid: 42b9620e-9388-4ee6-be25-e4a3a0928211

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/notification_message.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SendNotificationRequest {
  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Notification to be delivered.
  NotificationMessage notification = 2;
}
```

---

### send_notification_response.proto {#send_notification_response}

**Path**: `gcommon/v1/common/send_notification_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `SendNotificationResponse`

**Imports** (3):

- `gcommon/v1/common/delivery_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/send_notification_response.proto
// version: 1.0.0
// guid: 4c4e1ac6-1393-496b-80b5-cb0bd7ef41f1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response returned after sending a notification.
 */
message SendNotificationResponse {
  // Unique identifier for the queued notification.
  string notification_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the notification was accepted for delivery
  bool accepted = 2;

  // Current delivery status of the notification
  gcommon.v1.common.DeliveryStatus status = 3;
}
```

---

### send_verification_email_request.proto {#send_verification_email_request}

**Path**: `gcommon/v1/common/send_verification_email_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `SendVerificationEmailRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/send_verification_email_request.proto
// version: 1.0.0
// guid: 0e006386-d269-49b5-b99f-3794275714db
// file: proto/gcommon/v1/common/send_verification_email_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SendVerificationEmailRequest {
  // User ID or email address
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Template to use for email
  string template = 2 [(buf.validate.field).string.min_len = 1];

  // Additional context data
  map<string, string> context = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### send_verification_email_response.proto {#send_verification_email_response}

**Path**: `gcommon/v1/common/send_verification_email_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `SendVerificationEmailResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/send_verification_email_response.proto
// version: 1.0.0
// guid: f17880d2-6f37-4b9d-a6d6-06c70e75e7d6
// file: proto/gcommon/v1/common/send_verification_email_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SendVerificationEmailResponse {
  // Send success
  bool sent = 1;

  // Error message if send failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Token expiry time
  int64 expires_at = 3 [(buf.validate.field).int64.gte = 0];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### set_health_request.proto {#set_health_request}

**Path**: `gcommon/v1/common/set_health_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `SetHealthRequest`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/set_health_request.proto
// version: 1.0.0
// guid: 448c2377-fccd-47a6-bb60-977a92b8eaac
// file: proto/gcommon/v1/common/set_health_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_status.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SetHealthRequest {
  // Service name to update
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Desired health status
  gcommon.v1.common.CommonHealthStatus status = 2;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### set_health_response.proto {#set_health_response}

**Path**: `gcommon/v1/common/set_health_response.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `SetHealthResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/set_health_response.proto
// version: 1.0.0
// guid: 5ec27f13-872f-47b7-acb8-58d9d37ae159
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for manually setting health status.
 * Contains the result of administratively setting the health status.
 */
message SetHealthResponse {
  // Success status
  bool success = 1;

  // Previous health status before the change
  gcommon.v1.common.CommonHealthStatus previous_status = 2;

  // New health status after the change
  gcommon.v1.common.CommonHealthStatus new_status = 3;

  // Timestamp when status was changed
  google.protobuf.Timestamp changed_at = 4;

  // Error information if setting failed
  gcommon.v1.common.Error error = 5;

  // Reason for the manual status change
  string reason = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### terminate_session_request.proto {#terminate_session_request}

**Path**: `gcommon/v1/common/terminate_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 102

**Messages** (1): `TerminateSessionRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/terminate_session_request.proto
// version: 1.0.0
// guid: 9b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * TerminateSessionRequest terminates one or more user sessions.
 * Used by administrators to forcibly terminate user sessions,
 * or by users to terminate their own sessions (e.g., "log out all devices").
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message TerminateSessionRequest {
  // Required fields (1-10)

  /**
   * The ID of the user whose session(s) should be terminated.
   * This can be the requesting user's own ID or another user's ID
   * if the requester has appropriate permissions.
   */
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  /**
   * Specific session IDs to terminate. If empty, the termination
   * scope is determined by other filters.
   */
  repeated string session_ids = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Terminate all sessions for this user. When true, ignores
   * session_ids and other filters. Requires admin permissions
   * unless user is terminating their own sessions.
   */
  bool terminate_all = 12;

  /**
   * Only terminate sessions matching this device type filter.
   * Valid values: "web", "mobile", "api", "desktop".
   * If not specified, applies to all device types.
   */
  string device_type_filter = 13;

  /**
   * Only terminate sessions created before this timestamp.
   * Useful for terminating old/stale sessions.
   */
  google.protobuf.Timestamp created_before = 14;

  /**
   * Only terminate sessions with last activity before this timestamp.
   * Useful for terminating inactive sessions.
   */
  google.protobuf.Timestamp last_activity_before = 15;

  /**
   * Exclude the current session (the one making this request)
   * from termination. Defaults to true to prevent self-logout.
   */
  bool exclude_current_session = 16;

  /**
   * Reason for termination (for audit logging).
   * Examples: "user_logout", "admin_action", "security_breach", "policy_violation".
   */
  string termination_reason = 17;

  /**
   * Send notification to user about session termination.
   * May include email, push notification, etc. Defaults to true.
   */
  bool send_notification = 18;

  /**
   * Force immediate termination without graceful cleanup.
   * Use with caution as it may result in data loss. Defaults to false.
   */
  bool force_immediate = 19;
}
```

---

### terminate_session_response.proto {#terminate_session_response}

**Path**: `gcommon/v1/common/terminate_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 53

**Messages** (1): `TerminateSessionResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/terminate_session_response.proto
// version: 1.0.0
// guid: b183b962-3ed6-499a-8c81-3fd2bcaaf65b
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * TerminateSessionResponse confirms successful session termination.
 * Provides information about the terminated session and cleanup operations
 * for audit logging and confirmation purposes.
 */
message TerminateSessionResponse {
  // Session ID that was terminated
  string session_id = 1;

  // User ID whose session was terminated
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username of the user
  string username = 3;

  // Timestamp when the session was terminated
  google.protobuf.Timestamp terminated_at = 4;

  // Reason for termination (logout, timeout, security, admin, etc.)
  string termination_reason = 5;

  // Whether any associated tokens were revoked
  bool tokens_revoked = 6;

  // Number of tokens that were revoked
  int32 revoked_token_count = 7;

  // Whether this was a forced termination (by admin or security)
  bool forced_termination = 8;

  // Number of remaining active sessions for this user
  int32 remaining_session_count = 9;

  // Success message describing the termination
  string message = 10;
}
```

---

### unregister_check_request.proto {#unregister_check_request}

**Path**: `gcommon/v1/common/unregister_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `UnregisterCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/unregister_check_request.proto
// version: 1.0.0
// guid: 97f6ba81-dd35-4406-a842-01af8b19471b
// file: proto/gcommon/v1/common/unregister_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UnregisterCheckRequest {
  // ID of the check to unregister
  string check_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### unregister_check_response.proto {#unregister_check_response}

**Path**: `gcommon/v1/common/unregister_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `UnregisterCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/unregister_check_response.proto
// version: 1.0.0
// guid: 6acc368e-830b-4b51-be8d-104cf86040f4
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for unregistering a health check.
 * Contains the result of removing a health check from the system.
 */
message UnregisterCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was unregistered
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if unregistration failed
  gcommon.v1.common.Error error = 3;

  // Confirmation message
  string message = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_action.proto {#update_action}

**Path**: `gcommon/v1/common/update_action.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `UpdateAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_action.proto
// version: 1.0.1
// guid: cb7f4802-67a0-4c44-a5b3-b98fc2aab61a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * UpdateAction indicates what action was taken during the update.
 */
enum UpdateAction {
  UPDATE_ACTION_UNSPECIFIED = 0;
  UPDATE_ACTION_UPDATED = 1;
  UPDATE_ACTION_NO_CHANGE = 2;
  UPDATE_ACTION_RESTARTED = 3;
  UPDATE_ACTION_RECREATED = 4;
}
```

---

### update_permission_request.proto {#update_permission_request}

**Path**: `gcommon/v1/common/update_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 53

**Messages** (1): `UpdatePermissionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_permission_request.proto
// version: 1.0.0
// guid: e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update an existing permission.
 * Allows modification of permission properties and constraints.
 */
message UpdatePermissionRequest {
  // Permission ID to update (required)
  string permission_id = 1;

  // New permission name (optional)
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // New permission description (optional)
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // New resource this permission applies to (optional)
  string resource = 4;

  // New action this permission allows (optional)
  string action = 5;

  // New conditions for the permission (optional)
  repeated string conditions = 6;

  // Whether the permission should be active (optional)
  bool active = 7;

  // Fields to update (field mask)
  repeated string update_mask = 8;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 9;

  // Reason for the update
  string reason = 10;
}
```

---

