# common_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 14
- **Services**: 0
- **Enums**: 36

## Files in this Module

- [acknowledgment_mode.proto](#acknowledgment_mode)
- [aggregation_type.proto](#aggregation_type)
- [alert_channel_type.proto](#alert_channel_type)
- [alert_condition.proto](#alert_condition)
- [alert_severity.proto](#alert_severity)
- [alert_state.proto](#alert_state)
- [alert_type.proto](#alert_type)
- [anti_affinity_scope.proto](#anti_affinity_scope)
- [api_key.proto](#api_key)
- [api_key_credentials.proto](#api_key_credentials)
- [api_key_stats.proto](#api_key_stats)
- [appender_type.proto](#appender_type)
- [approval_status.proto](#approval_status)
- [archive_criteria.proto](#archive_criteria)
- [audit_action.proto](#audit_action)
- [audit_level.proto](#audit_level)
- [audit_log.proto](#audit_log)
- [audit_operation_type.proto](#audit_operation_type)
- [audit_result.proto](#audit_result)
- [auth_context.proto](#auth_context)
- [auth_method.proto](#auth_method)
- [auth_provider.proto](#auth_provider)
- [auth_token.proto](#auth_token)
- [backoff_strategy.proto](#backoff_strategy)
- [buffer_overflow_strategy.proto](#buffer_overflow_strategy)
- [cache_invalidation_trigger.proto](#cache_invalidation_trigger)
- [cache_policy.proto](#cache_policy)
- [cache_refresh_strategy.proto](#cache_refresh_strategy)
- [cache_strategy.proto](#cache_strategy)
- [channel_type.proto](#channel_type)
- [check_result.proto](#check_result)
- [check_type.proto](#check_type)
- [circuit_breaker_state.proto](#circuit_breaker_state)
- [claims.proto](#claims)
- [cleanup_strategy.proto](#cleanup_strategy)
- [client_info.proto](#client_info)
- [cluster_state.proto](#cluster_state)
- [comparison_operator.proto](#comparison_operator)
- [component_health.proto](#component_health)
- [compression_algorithm.proto](#compression_algorithm)
- [compression_type.proto](#compression_type)
- [conflict_resolution.proto](#conflict_resolution)
- [conflict_strategy.proto](#conflict_strategy)
- [consistency_level.proto](#consistency_level)
- [consumer_group_state.proto](#consumer_group_state)
- [consumer_state.proto](#consumer_state)
- [content_type.proto](#content_type)
- [cookie_same_site.proto](#cookie_same_site)
- [coordinator_state.proto](#coordinator_state)
- [daily_usage.proto](#daily_usage)
---


## Detailed Documentation

### acknowledgment_mode.proto {#acknowledgment_mode}

**Path**: `gcommon/v1/common/acknowledgment_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `AcknowledgmentMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/acknowledgment_mode.proto
// version: 1.0.1
// guid: 6f4b2414-998e-4fc3-bc68-188dff6d2f25

// Enumeration describing how message acknowledgments are handled by a
// queue consumer. This was previously left as a placeholder during the
// 1-1-1 migration.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AcknowledgmentMode specifies how a message should be acknowledged
// by the consumer. It provides flexibility for different delivery
// guarantees and consumer implementations.
enum AcknowledgmentMode {
  // Default mode. The broker chooses a sensible default based on
  // queue configuration.
  ACKNOWLEDGMENT_MODE_UNSPECIFIED = 0;

  // Messages are automatically acknowledged immediately after
  // successful processing by the consumer.
  ACKNOWLEDGMENT_MODE_AUTO = 1;

  // The consumer is responsible for explicitly sending an AckRequest
  // after processing the message.
  ACKNOWLEDGMENT_MODE_MANUAL = 2;

  // No acknowledgment is required. Messages are considered processed
  // once delivered. Use with care.
  ACKNOWLEDGMENT_MODE_NONE = 3;
}
```

---

### aggregation_type.proto {#aggregation_type}

**Path**: `gcommon/v1/common/aggregation_type.proto` **Package**: `gcommon.v1.common` **Lines**: 59

**Enums** (1): `AggregationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/types/aggregation_type.proto
// version: 1.0.1
// guid: ab90e4af-40b2-4a70-94d5-3aef1bf40b63
// file: proto/gcommon/v1/metrics/aggregation_type.proto
//
// Aggregation type enum definitions for metrics module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AggregationType defines how metrics should be aggregated over time.
 */
enum AggregationType {
  // Unspecified aggregation type
  AGGREGATION_TYPE_UNSPECIFIED = 0;

  // Sum all values
  AGGREGATION_TYPE_SUM = 1;

  // Average all values
  AGGREGATION_TYPE_AVERAGE = 2;

  // Take minimum value
  AGGREGATION_TYPE_MIN = 3;

  // Take maximum value
  AGGREGATION_TYPE_MAX = 4;

  // Count number of values
  AGGREGATION_TYPE_COUNT = 5;

  // Standard deviation
  AGGREGATION_TYPE_STDDEV = 6;

  // Variance
  AGGREGATION_TYPE_VARIANCE = 7;

  // Median (50th percentile)
  AGGREGATION_TYPE_MEDIAN = 8;

  // 95th percentile
  AGGREGATION_TYPE_P95 = 9;

  // 99th percentile
  AGGREGATION_TYPE_P99 = 10;

  // Rate of change
  AGGREGATION_TYPE_RATE = 11;

  // Increase over time
  AGGREGATION_TYPE_INCREASE = 12;
}
```

---

### alert_channel_type.proto {#alert_channel_type}

**Path**: `gcommon/v1/common/alert_channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `AlertChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/alert_channel_type.proto
// version: 1.0.1
// guid: 6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AlertChannelType represents different types of alert channels
enum AlertChannelType {
  // Unspecified alert channel type
  ALERT_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email notification
  ALERT_CHANNEL_TYPE_EMAIL = 1;

  // Slack notification
  ALERT_CHANNEL_TYPE_SLACK = 2;

  // PagerDuty notification
  ALERT_CHANNEL_TYPE_PAGERDUTY = 3;

  // Webhook notification
  ALERT_CHANNEL_TYPE_WEBHOOK = 4;

  // SMS notification
  ALERT_CHANNEL_TYPE_SMS = 5;

  // Microsoft Teams notification
  ALERT_CHANNEL_TYPE_TEAMS = 6;

  // Discord notification
  ALERT_CHANNEL_TYPE_DISCORD = 7;

  // Telegram notification
  ALERT_CHANNEL_TYPE_TELEGRAM = 8;

  // Push notification
  ALERT_CHANNEL_TYPE_PUSH = 9;

  // JIRA ticket creation
  ALERT_CHANNEL_TYPE_JIRA = 10;

  // ServiceNow incident creation
  ALERT_CHANNEL_TYPE_SERVICENOW = 11;

  // Custom alert channel
  ALERT_CHANNEL_TYPE_CUSTOM = 12;
}
```

---

### alert_condition.proto {#alert_condition}

**Path**: `gcommon/v1/common/alert_condition.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `AlertCondition`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alert_condition.proto
// version: 1.0.1
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Condition types for alerts.
 */
enum AlertCondition {
  // Default unspecified condition
  ALERT_CONDITION_UNSPECIFIED = 0;

  // Metric greater than threshold
  ALERT_CONDITION_GREATER_THAN = 1;

  // Metric less than threshold
  ALERT_CONDITION_LESS_THAN = 2;

  // Metric equal to threshold
  ALERT_CONDITION_EQUALS = 3;

  // Metric not equal to threshold
  ALERT_CONDITION_NOT_EQUALS = 4;

  // Metric increasing rapidly
  ALERT_CONDITION_INCREASING = 5;

  // Metric decreasing rapidly
  ALERT_CONDITION_DECREASING = 6;
}
```

---

### alert_severity.proto {#alert_severity}

**Path**: `gcommon/v1/common/alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Enums** (1): `CommonAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/alert_severity.proto
// version: 1.0.1
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AlertSeverity enumerates alert severity levels used across all systems
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonAlertSeverity {
  ALERT_SEVERITY_UNSPECIFIED = 0;
  ALERT_SEVERITY_LOW = 1;
  ALERT_SEVERITY_MEDIUM = 2;
  ALERT_SEVERITY_HIGH = 3;
  ALERT_SEVERITY_CRITICAL = 4;
  ALERT_SEVERITY_INFO = 5; // From queue version
  ALERT_SEVERITY_WARNING = 6; // From queue version
  ALERT_SEVERITY_ERROR = 7; // From queue version
}
```

---

### alert_state.proto {#alert_state}

**Path**: `gcommon/v1/common/alert_state.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Enums** (1): `AlertState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alert_state.proto
// version: 1.0.1
// guid: a1dd0c23-a3f3-4e37-a662-d61897f80c3a
// file: proto/gcommon/v1/metrics/v1/alert_state.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AlertState defines the current state of a metric alert.
 * Represents the lifecycle states of alerts from creation to resolution.
 */
enum AlertState {
  // Unspecified state (default)
  ALERT_STATE_UNSPECIFIED = 0;

  // Alert condition is being evaluated but hasn't triggered
  ALERT_STATE_PENDING = 1;

  // Alert condition has been met and is actively firing
  ALERT_STATE_FIRING = 2;

  // Alert was firing but condition is no longer met
  ALERT_STATE_RESOLVED = 3;

  // Alert has been acknowledged by an operator
  ALERT_STATE_ACKNOWLEDGED = 4;

  // Alert has been manually silenced/suppressed
  ALERT_STATE_SILENCED = 5;

  // Alert is in an error state (evaluation failed)
  ALERT_STATE_ERROR = 6;
}
```

---

### alert_type.proto {#alert_type}

**Path**: `gcommon/v1/common/alert_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `AlertType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/alert_type.proto
// version: 1.0.1
// guid: 54407766-3304-4e90-90d6-973ac6ff0fc3

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum AlertType {
  ALERT_TYPE_UNSPECIFIED = 0;
  ALERT_TYPE_EXPIRATION = 1;
  ALERT_TYPE_ACCESS_ANOMALY = 2;
  ALERT_TYPE_FAILED_ACCESS = 3;
  ALERT_TYPE_ROTATION_FAILURE = 4;
  ALERT_TYPE_BACKUP_FAILURE = 5;
  ALERT_TYPE_COMPLIANCE_VIOLATION = 6;
  ALERT_TYPE_SECURITY_INCIDENT = 7;
}
```

---

### anti_affinity_scope.proto {#anti_affinity_scope}

**Path**: `gcommon/v1/common/anti_affinity_scope.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `AntiAffinityScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/anti_affinity_scope.proto
// version: 1.0.1
// guid: 719f1256-5001-4957-aa05-7b676cc4b90b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Scope for anti-affinity rules.
 */
enum AntiAffinityScope {
  // Default unspecified scope
  ANTI_AFFINITY_SCOPE_UNSPECIFIED = 0;

  // Same node
  ANTI_AFFINITY_SCOPE_NODE = 1;

  // Same rack
  ANTI_AFFINITY_SCOPE_RACK = 2;

  // Same datacenter
  ANTI_AFFINITY_SCOPE_DATACENTER = 3;

  // Same region
  ANTI_AFFINITY_SCOPE_REGION = 4;
}
```

---

### api_key.proto {#api_key}

**Path**: `gcommon/v1/common/api_key.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `APIKey`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/api_key.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-789a-b0c1-d2e3f4a5b6c7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto"; // Added for field validation rules

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * APIKey represents a user-issued API key used for authenticating
 * programmatic access. The key value itself should be stored securely
 * and only the hashed form transmitted.
 */
message APIKey {
  // Unique identifier for the API key (UUID required)
  string id = 1 [
    (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    (buf.validate.field).required = true
  ];

  // ID of the user this key belongs to (UUID required)
  string user_id = 2 [
    (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    (buf.validate.field).required = true
  ];

  // Human readable description for the key (limit length)
  string description = 3 [(buf.validate.field).string.max_len = 500];

  // Hash of the API key value (non-empty)
  string key_hash = 4 [(buf.validate.field).string.min_len = 1];

  // Creation timestamp (must be present)
  google.protobuf.Timestamp created_at = 5 [lazy = true, (buf.validate.field).required = true];

  // Optional expiration timestamp
  google.protobuf.Timestamp expires_at = 6 [lazy = true];

  // Whether the key is currently active
  bool active = 7;
}

```

---

### api_key_credentials.proto {#api_key_credentials}

**Path**: `gcommon/v1/common/api_key_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `APIKeyCredentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/api_key_credentials.proto
// version: 1.0.0
// guid: 3a18b7a0-491c-4ddb-a97e-81168333896d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * API key credentials for programmatic authentication.
 * Supports both simple API key and key-pair authentication schemes.
 */
message APIKeyCredentials {
  // API key value used for authentication
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional API key ID for key-pair authentication schemes
  // Used when the API key is associated with a specific key identifier
  string key_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### api_key_stats.proto {#api_key_stats}

**Path**: `gcommon/v1/common/api_key_stats.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `ApiKeyStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/api_key_stats.proto
// version: 1.0.0
// guid: 118f177f-69fa-465e-9cc9-88c6aa87643f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

// TODO FIX THIS
//

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ApiKeyStats {
  int32 total_requests = 1 [(buf.validate.field).int32.gte = 0];
  int32 successful_requests = 2 [(buf.validate.field).int32.gte = 0];
  int32 failed_requests = 3 [(buf.validate.field).int32.gte = 0];
  int64 last_used_at = 4 [(buf.validate.field).int64.gte = 0];
  // TODO FIX THIS
  // repeated DailyUsage daily_usage = 5;
}
```

---

### appender_type.proto {#appender_type}

**Path**: `gcommon/v1/common/appender_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `AppenderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/appender_type.proto
// version: 1.0.1
// guid: 5e2f63bf-35c4-4a2a-b35a-54017c979940

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AppenderType enumerates logging output backends
enum AppenderType {
  APPENDER_TYPE_UNSPECIFIED = 0;
  APPENDER_TYPE_CONSOLE = 1;
  APPENDER_TYPE_FILE = 2;
  APPENDER_TYPE_ROLLING_FILE = 3;
  APPENDER_TYPE_SYSLOG = 4;
  APPENDER_TYPE_NETWORK = 5;
  APPENDER_TYPE_DATABASE = 6;
}
```

---

### approval_status.proto {#approval_status}

**Path**: `gcommon/v1/common/approval_status.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `ApprovalStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/approval_status.proto
// version: 1.0.1
// guid: a9b0c1d2-e3f4-5a6b-7c8d-9e0f1a2b3c4d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ApprovalStatus represents the approval status.
 * Specifies the current state of configuration change approval.
 */
enum ApprovalStatus {
  // Unspecified approval status
  APPROVAL_STATUS_UNSPECIFIED = 0;

  // Approval is pending
  APPROVAL_STATUS_PENDING = 1;

  // Change has been approved
  APPROVAL_STATUS_APPROVED = 2;

  // Change has been rejected
  APPROVAL_STATUS_REJECTED = 3;

  // Approval was cancelled
  APPROVAL_STATUS_CANCELLED = 4;

  // Approval request expired
  APPROVAL_STATUS_EXPIRED = 5;
}
```

---

### archive_criteria.proto {#archive_criteria}

**Path**: `gcommon/v1/common/archive_criteria.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `ArchiveCriteria`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/archive_criteria.proto
// version: 1.0.0
// guid: b7d23f2c-0017-462f-a6d2-51ca4405bc2c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ArchiveCriteria defines rules for selecting log files to archive
message ArchiveCriteria {
  // Only archive logs older than this duration
  google.protobuf.Duration older_than = 1;

  // Minimum size threshold in bytes
  int64 size_threshold_bytes = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### audit_action.proto {#audit_action}

**Path**: `gcommon/v1/common/audit_action.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Enums** (1): `AuditAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_action.proto
// version: 1.0.1
// guid: fe20f23e-ff61-4f78-b548-99cc5aded7b4
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Audit action enumeration for tracking user and system actions.
 * Used for security auditing and compliance logging.
 */
enum AuditAction {
  // Unspecified audit action
  AUDIT_ACTION_UNSPECIFIED = 0;

  // Authentication actions
  AUDIT_ACTION_LOGIN = 1;
  AUDIT_ACTION_LOGOUT = 2;
  AUDIT_ACTION_LOGIN_FAILED = 3;

  // Authorization actions
  AUDIT_ACTION_ACCESS_GRANTED = 4;
  AUDIT_ACTION_ACCESS_DENIED = 5;

  // User management actions
  AUDIT_ACTION_USER_CREATED = 6;
  AUDIT_ACTION_USER_UPDATED = 7;
  AUDIT_ACTION_USER_DELETED = 8;
  AUDIT_ACTION_USER_SUSPENDED = 9;

  // Role management actions
  AUDIT_ACTION_ROLE_ASSIGNED = 10;
  AUDIT_ACTION_ROLE_REMOVED = 11;
  AUDIT_ACTION_ROLE_CREATED = 12;
  AUDIT_ACTION_ROLE_UPDATED = 13;
  AUDIT_ACTION_ROLE_DELETED = 14;

  // Permission actions
  AUDIT_ACTION_PERMISSION_GRANTED = 15;
  AUDIT_ACTION_PERMISSION_REVOKED = 16;

  // Session actions
  AUDIT_ACTION_SESSION_CREATED = 17;
  AUDIT_ACTION_SESSION_TERMINATED = 18;

  // Configuration changes
  AUDIT_ACTION_CONFIG_UPDATED = 19;

  // System actions
  AUDIT_ACTION_SYSTEM_BACKUP = 20;
  AUDIT_ACTION_SYSTEM_RESTORE = 21;
}
```

---

### audit_level.proto {#audit_level}

**Path**: `gcommon/v1/common/audit_level.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `AuditLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/audit_level.proto
// version: 1.0.1
// guid: 8576474b-84f1-4a99-ab88-a865fb4e28ca

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum AuditLevel {
  AUDIT_LEVEL_UNSPECIFIED = 0;
  AUDIT_LEVEL_NONE = 1;
  AUDIT_LEVEL_MINIMAL = 2;
  AUDIT_LEVEL_STANDARD = 3;
  AUDIT_LEVEL_DETAILED = 4;
  AUDIT_LEVEL_VERBOSE = 5;
}
```

---

### audit_log.proto {#audit_log}

**Path**: `gcommon/v1/common/audit_log.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Messages** (1): `CommonAuditLog`

**Imports** (5):

- `gcommon/v1/common/audit_result.proto`
- `gcommon/v1/common/resource_reference.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_log.proto
// version: 1.0.0
// guid: 95446d3f-aa5e-4be7-a7bb-5b0b0b1cf19b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/audit_result.proto";
import "gcommon/v1/common/resource_reference.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Audit log entry for tracking operations and security events.
 * Provides comprehensive audit trail with user identification,
 * action details, and contextual metadata for compliance and debugging.
 */
message CommonAuditLog {
  // Unique audit log entry identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User identifier who performed the action
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

### audit_operation_type.proto {#audit_operation_type}

**Path**: `gcommon/v1/common/audit_operation_type.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Enums** (1): `AuditOperationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/audit_operation_type.proto
// version: 1.0.1
// guid: d6e7f8a9-b0c1-2d3e-4f5a-6b7c8d9e0f1a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuditOperationType represents the type of configuration operation.
 * Specifies the category of configuration change being audited.
 */
enum AuditOperationType {
  // Unspecified operation type
  AUDIT_OPERATION_TYPE_UNSPECIFIED = 0;

  // Create new configuration
  AUDIT_OPERATION_TYPE_CREATE = 1;

  // Update existing configuration
  AUDIT_OPERATION_TYPE_UPDATE = 2;

  // Delete configuration
  AUDIT_OPERATION_TYPE_DELETE = 3;

  // Bulk create multiple configurations
  AUDIT_OPERATION_TYPE_BULK_CREATE = 4;

  // Bulk update multiple configurations
  AUDIT_OPERATION_TYPE_BULK_UPDATE = 5;

  // Bulk delete multiple configurations
  AUDIT_OPERATION_TYPE_BULK_DELETE = 6;

  // Import configuration data
  AUDIT_OPERATION_TYPE_IMPORT = 7;

  // Export configuration data
  AUDIT_OPERATION_TYPE_EXPORT = 8;

  // Backup configuration
  AUDIT_OPERATION_TYPE_BACKUP = 9;

  // Restore configuration from backup
  AUDIT_OPERATION_TYPE_RESTORE = 10;

  // Rollback configuration changes
  AUDIT_OPERATION_TYPE_ROLLBACK = 11;

  // Validate configuration
  AUDIT_OPERATION_TYPE_VALIDATE = 12;

  // Synchronize configuration
  AUDIT_OPERATION_TYPE_SYNC = 13;
}
```

---

### audit_result.proto {#audit_result}

**Path**: `gcommon/v1/common/audit_result.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `AuditResult`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_result.proto
// version: 1.0.1
// guid: 27e8e7bb-a068-4e4b-b7d0-d69c6747f9bc
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### auth_context.proto {#auth_context}

**Path**: `gcommon/v1/common/auth_context.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `AuthContext`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_context.proto
// version: 1.0.0
// guid: 70848c6a-eeb6-46ee-b108-9159435b2475

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthContext carries user identity and authorization details
 * generated during authentication.
 */
message AuthContext {
  // ID of the authenticated user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Roles assigned to the user
  repeated string roles = 2;

  // Permissions granted to the user
  repeated string permissions = 3;

  // When this context was generated
  google.protobuf.Timestamp issued_at = 4 [lazy = true];

  // Arbitrary metadata passed between services
  map<string, string> metadata = 5;
}
```

---

### auth_method.proto {#auth_method}

**Path**: `gcommon/v1/common/auth_method.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Enums** (1): `AuthAuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_method.proto
// version: 1.0.1
// guid: 815bb886-5864-44fd-ae07-c6102c110fd7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthMethod enumerates the supported authentication mechanisms.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthAuthMethod {
  // Default unknown method
  COMMON_AUTH_METHOD_UNSPECIFIED = 0;

  // Traditional username and password authentication
  COMMON_AUTH_METHOD_PASSWORD = 1;

  // API key based authentication
  COMMON_AUTH_METHOD_API_KEY = 2;

  // OAuth2 or OpenID Connect authentication
  COMMON_AUTH_METHOD_OAUTH2 = 3;

  // SAML identity provider authentication
  COMMON_AUTH_METHOD_SAML = 4;

  // LDAP directory authentication
  COMMON_AUTH_METHOD_LDAP = 5;

  // Multi-factor authentication method
  COMMON_AUTH_METHOD_MFA = 6;

  // Token-based authentication (e.g., JWT, bearer tokens)
  COMMON_AUTH_METHOD_TOKEN = 7;

  // No authentication required
  COMMON_AUTH_METHOD_NONE = 8;
}
```

---

### auth_provider.proto {#auth_provider}

**Path**: `gcommon/v1/common/auth_provider.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `AuthProvider`

**Imports** (3):

- `gcommon/v1/common/provider_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_provider.proto
// version: 1.0.0
// guid: 7293f6cc-7049-493d-9e7c-b17f00dd8a76

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/provider_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthProvider represents an external authentication provider configuration.
 * It defines the provider type and connection details used for authentication.
 */
message AuthProvider {
  // Unique provider identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human readable provider name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Provider type (e.g., LDAP, OAUTH2, SAML)
  gcommon.v1.common.AuthProviderType type = 3;

  // Provider-specific configuration reference or JSON blob
  string config = 4;
}
```

---

### auth_token.proto {#auth_token}

**Path**: `gcommon/v1/common/auth_token.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `AuthToken`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_token.proto
// version: 1.0.0
// guid: 61671511-e4c8-4e25-a0a6-5f82f7e45002

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Combined authentication token pair containing access and refresh tokens.
 */
message AuthToken {
  // Access token used for authenticated requests.
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // Refresh token used to obtain new access tokens.
  string refresh_token = 2 [(buf.validate.field).string.min_len = 1];

  // Expiration time of the access token.
  google.protobuf.Timestamp expires_at = 3 [lazy = true];

  // Optional metadata associated with the token pair.
  map<string, string> metadata = 4 [lazy = true];
}
```

---

### backoff_strategy.proto {#backoff_strategy}

**Path**: `gcommon/v1/common/backoff_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `BackoffStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/backoff_strategy.proto
// version: 1.0.1
// guid: 5aec3abd-38af-4436-a59a-c4140f44a461

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum BackoffStrategy {
  BACKOFF_STRATEGY_UNSPECIFIED = 0;
  BACKOFF_STRATEGY_FIXED = 1;
  BACKOFF_STRATEGY_LINEAR = 2;
  BACKOFF_STRATEGY_EXPONENTIAL = 3;
  BACKOFF_STRATEGY_CUSTOM = 4;
}
```

---

### buffer_overflow_strategy.proto {#buffer_overflow_strategy}

**Path**: `gcommon/v1/common/buffer_overflow_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `BufferOverflowStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/buffer_overflow_strategy.proto
// version: 1.0.1
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * BufferOverflowStrategy defines how to handle buffer overflow.
 * Specifies behavior when metric streaming buffers are full.
 */
enum BufferOverflowStrategy {
  // Unspecified strategy
  BUFFER_OVERFLOW_STRATEGY_UNSPECIFIED = 0;

  // Drop oldest entries when buffer is full
  BUFFER_OVERFLOW_STRATEGY_DROP_OLDEST = 1;

  // Drop newest entries when buffer is full
  BUFFER_OVERFLOW_STRATEGY_DROP_NEWEST = 2;

  // Block when buffer is full
  BUFFER_OVERFLOW_STRATEGY_BLOCK = 3;

  // Return error when buffer is full
  BUFFER_OVERFLOW_STRATEGY_ERROR = 4;
}
```

---

### cache_invalidation_trigger.proto {#cache_invalidation_trigger}

**Path**: `gcommon/v1/common/cache_invalidation_trigger.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `CacheInvalidationTrigger`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/cache_invalidation_trigger.proto
// version: 1.0.1
// guid: b09e744e-1475-4fcb-a8cc-0d121530e6b7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CacheInvalidationTrigger {
  CACHE_INVALIDATION_TRIGGER_UNSPECIFIED = 0;
  CACHE_INVALIDATION_TRIGGER_CHANGE = 1;
  CACHE_INVALIDATION_TRIGGER_DELETE = 2;
  CACHE_INVALIDATION_TRIGGER_EXPIRE = 3;
  CACHE_INVALIDATION_TRIGGER_MANUAL = 4;
  CACHE_INVALIDATION_TRIGGER_SCHEDULE = 5;
}
```

---

### cache_policy.proto {#cache_policy}

**Path**: `gcommon/v1/common/cache_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `CachePolicy`

**Imports** (5):

- `gcommon/v1/common/eviction_policy.proto`
- `gcommon/v1/common/expiration_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/cache_policy.proto
// version: 1.0.0
// guid: c37fc88f-0b7c-4fa4-9c60-23736d2bed76
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/eviction_policy.proto";
import "gcommon/v1/common/expiration_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Cache policy configuration for cache behavior and performance tuning.
 * Defines expiration, eviction, sizing, and operational policies
 * for consistent cache management across GCommon modules.
 */
message CachePolicy {
  // Cache expiration policy strategy
  gcommon.v1.common.ExpirationPolicy expiration = 1;

  // Eviction policy when cache reaches capacity
  gcommon.v1.common.EvictionPolicy eviction = 2;

  // Maximum cache size in bytes (0 for unlimited)
  int64 max_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum number of cache entries (0 for unlimited)
  int64 max_entries = 4 [(buf.validate.field).int64.gte = 0];

  // Default time-to-live for cache entries
  google.protobuf.Duration default_ttl = 5;

  // Whether to refresh entries before they expire
  bool refresh_ahead = 6;

  // Whether to collect and expose cache statistics
  bool enable_stats = 7;
}
```

---

### cache_refresh_strategy.proto {#cache_refresh_strategy}

**Path**: `gcommon/v1/common/cache_refresh_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `CacheRefreshStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/cache_refresh_strategy.proto
// version: 1.0.1
// guid: c38dfb62-6d18-4f59-a901-6c4b5e659952

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CacheRefreshStrategy {
  CACHE_REFRESH_STRATEGY_UNSPECIFIED = 0;
  CACHE_REFRESH_STRATEGY_TTL = 1;
  CACHE_REFRESH_STRATEGY_LAZY = 2;
  CACHE_REFRESH_STRATEGY_PROACTIVE = 3;
  CACHE_REFRESH_STRATEGY_BACKGROUND = 4;
}
```

---

### cache_strategy.proto {#cache_strategy}

**Path**: `gcommon/v1/common/cache_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `CacheStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cache_strategy.proto
// version: 1.0.1
// guid: a2c186e6-9e1e-402b-802f-39fc7b4dfc0d
//
// CacheStrategy defines caching policies for HTTP handlers.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Available caching policies for responses.
enum CacheStrategy {
  CACHE_STRATEGY_UNSPECIFIED = 0;
  // Do not cache responses.
  CACHE_STRATEGY_NONE = 1;
  // Use in-memory caching only.
  CACHE_STRATEGY_MEMORY = 2;
  // Use distributed cache (e.g., Redis).
  CACHE_STRATEGY_DISTRIBUTED = 3;
  // Use external CDN cache.
  CACHE_STRATEGY_CDN = 4;
}
```

---

### channel_type.proto {#channel_type}

**Path**: `gcommon/v1/common/channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `ChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/channel_type.proto
// version: 1.0.1
// guid: 6f6a3985-1560-40b0-b6d5-b2985349b649

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ChannelType {
  CHANNEL_TYPE_UNSPECIFIED = 0;
  CHANNEL_TYPE_EMAIL = 1;
  CHANNEL_TYPE_SLACK = 2;
  CHANNEL_TYPE_WEBHOOK = 3;
  CHANNEL_TYPE_SMS = 4;
  CHANNEL_TYPE_PAGERDUTY = 5;
  CHANNEL_TYPE_TEAMS = 6;
  CHANNEL_TYPE_DISCORD = 7;
  CHANNEL_TYPE_JIRA = 8;
}
```

---

### check_result.proto {#check_result}

**Path**: `gcommon/v1/common/check_result.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Messages** (1): `CheckResult`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_result.proto
// version: 1.0.0
// guid: 0e8f3ad4-be75-42b2-b880-fda7ebd7de1c
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
 * Individual health check result for a specific component or subsystem.
 * Provides detailed information about the health status of a single check.
 */
message CheckResult {
  // Check name or identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Health status of this specific check
  // Overall status of the health check
  gcommon.v1.common.CommonHealthStatus status = 2;

  // Check execution timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Time taken to execute this check
  google.protobuf.Duration execution_time = 4;

  // Human-readable message about the check result
  string message = 5;

  // Error details if the check failed
  gcommon.v1.common.Error error = 6;

  // Additional metadata for this check
  map<string, string> metadata = 7;
}
```

---

### check_type.proto {#check_type}

**Path**: `gcommon/v1/common/check_type.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Enums** (1): `CheckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_type.proto
// version: 1.0.1
// guid: 38e1041c-a418-4fe7-8834-b48f3c71f401
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * CheckType indicates the type of health check
 */
enum CheckType {
  // Unspecified check type
  CHECK_TYPE_UNSPECIFIED = 0;
  // Liveness check
  CHECK_TYPE_LIVENESS = 1;
  // Readiness check
  CHECK_TYPE_READINESS = 2;
  // Startup check
  CHECK_TYPE_STARTUP = 3;
  // Component check
  CHECK_TYPE_COMPONENT = 4;
  // Dependency check
  CHECK_TYPE_DEPENDENCY = 5;
}
```

---

### circuit_breaker_state.proto {#circuit_breaker_state}

**Path**: `gcommon/v1/common/circuit_breaker_state.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `CircuitBreakerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/circuit_breaker_state.proto
// version: 1.0.1
// guid: 1d26f112-976e-48db-b531-58892638701d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### claims.proto {#claims}

**Path**: `gcommon/v1/common/claims.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Messages** (1): `Claims`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/claims.proto
// version: 1.0.0
// guid: 47901ef8-6b22-4b73-8bba-9c53ccaa46c8
// file: proto/gcommon/v1/common/claims.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Claims {
  // Standard JWT claims
  string issuer = 1; // iss
  string subject = 2; // sub
  repeated string audience = 3; // aud
  int64 expires_at = 4; // exp
  int64 not_before = 5; // nbf
  int64 issued_at = 6; // iat
  string jwt_id = 7; // jti

  // Custom claims
  string user_id = 8 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
  string username = 9;
  string email = 10 [ (buf.validate.field).string.email = true ];
  bool email_verified = 11;
  repeated string roles = 12;
  repeated string permissions = 13;
  repeated string scopes = 14;

  // MFA claims
  bool mfa_verified = 15;
  string mfa_method = 16;

  // Session claims
  string session_id = 17;
  bool is_refresh_token = 18;

  // Additional metadata
  map<string, string> metadata = 19;
}
```

---

### cleanup_strategy.proto {#cleanup_strategy}

**Path**: `gcommon/v1/common/cleanup_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `CleanupStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/cleanup_strategy.proto
// version: 1.0.1
// guid: 98464e8e-3ad4-475d-8e19-cac3b3d813ca

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * CleanupStrategy defines how cleanup should be performed.
 */
enum CleanupStrategy {
  CLEANUP_STRATEGY_UNSPECIFIED = 0;
  CLEANUP_STRATEGY_IMMEDIATE = 1;
  CLEANUP_STRATEGY_GRACEFUL = 2;
  CLEANUP_STRATEGY_BACKGROUND = 3;
  CLEANUP_STRATEGY_SCHEDULED = 4;
}
```

---

### client_info.proto {#client_info}

**Path**: `gcommon/v1/common/client_info.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `ClientInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/client_info.proto
// version: 1.0.0
// guid: d1b1396a-9610-4eb4-b5ea-bc7218024dee
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Client information for request identification and monitoring.
 * Provides standardized client metadata for logging, analytics,
 * and security purposes across all GCommon modules.
 */
message ClientInfo {
  // Client application name (e.g., "mobile-app", "web-frontend")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### cluster_state.proto {#cluster_state}

**Path**: `gcommon/v1/common/cluster_state.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `ClusterState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_state.proto
// version: 1.0.1
// guid: f68fdc5e-d25f-4790-9362-9bf09eb27f4d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * State of the cluster.
 */
enum ClusterState {
  // Default unspecified state
  CLUSTER_STATE_UNSPECIFIED = 0;

  // Cluster is healthy and operational
  CLUSTER_STATE_HEALTHY = 1;

  // Cluster is degraded but operational
  CLUSTER_STATE_DEGRADED = 2;

  // Cluster is in recovery mode
  CLUSTER_STATE_RECOVERING = 3;

  // Cluster is down
  CLUSTER_STATE_DOWN = 4;

  // Cluster is in maintenance mode
  CLUSTER_STATE_MAINTENANCE = 5;
}
```

---

### comparison_operator.proto {#comparison_operator}

**Path**: `gcommon/v1/common/comparison_operator.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `ComparisonOperator`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/comparison_operator.proto
// version: 1.0.1
// guid: a2b3c4d5-6789-012d-6789-234567890123

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ComparisonOperator {
  COMPARISON_OPERATOR_UNSPECIFIED = 0;
  COMPARISON_OPERATOR_EQUAL = 1;
  COMPARISON_OPERATOR_NOT_EQUAL = 2;
  COMPARISON_OPERATOR_GREATER_THAN = 3;
  COMPARISON_OPERATOR_GREATER_THAN_OR_EQUAL = 4;
  COMPARISON_OPERATOR_LESS_THAN = 5;
  COMPARISON_OPERATOR_LESS_THAN_OR_EQUAL = 6;
}
```

---

### component_health.proto {#component_health}

**Path**: `gcommon/v1/common/component_health.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `ComponentHealth`

**Imports** (3):

- `gcommon/v1/common/serving_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/component_health.proto
// version: 1.0.0
// guid: 1eb070ba-060f-44c9-97ad-8a3d68800129

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/serving_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ComponentHealth {
  // Component name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  // Component status
  gcommon.v1.common.ServingStatus status = 2;
  // Component-specific message
  string message = 3;
  // Component check duration in milliseconds
  int64 duration_ms = 4;
}
```

---

### compression_algorithm.proto {#compression_algorithm}

**Path**: `gcommon/v1/common/compression_algorithm.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `CompressionAlgorithm`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/compression_algorithm.proto
// version: 1.0.1
// guid: 46070a52-0998-4b61-b36f-05b4861f8f6c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Compression algorithms for serialization.
 */
enum CompressionAlgorithm {
  // Default unspecified algorithm
  COMPRESSION_ALGORITHM_UNSPECIFIED = 0;

  // No compression
  COMPRESSION_ALGORITHM_NONE = 1;

  // GZIP compression
  COMPRESSION_ALGORITHM_GZIP = 2;

  // LZ4 compression
  COMPRESSION_ALGORITHM_LZ4 = 3;

  // Snappy compression
  COMPRESSION_ALGORITHM_SNAPPY = 4;

  // ZSTD compression
  COMPRESSION_ALGORITHM_ZSTD = 5;

  // Brotli compression
  COMPRESSION_ALGORITHM_BROTLI = 6;
}
```

---

### compression_type.proto {#compression_type}

**Path**: `gcommon/v1/common/compression_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `LogCompressionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/compression_type.proto
// version: 1.0.1
// guid: 357b1a04-97e4-4d82-86a3-b6672180ce22

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// CompressionType enumerates archive compression formats
// buf:lint:ignore ENUM_VALUE_PREFIX
enum LogCompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  COMPRESSION_TYPE_NONE = 1;
  COMPRESSION_TYPE_GZIP = 2;
  COMPRESSION_TYPE_ZIP = 3;
  COMPRESSION_TYPE_BZIP2 = 4;
  COMPRESSION_TYPE_TAR_GZ = 5;
}
```

---

### conflict_resolution.proto {#conflict_resolution}

**Path**: `gcommon/v1/common/conflict_resolution.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `ConflictResolution`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/conflict_resolution.proto
// version: 1.0.1
// guid: 8535d30e-d232-4d73-9362-10e717955b66

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConflictResolution {
  COMMON_CONFLICT_RESOLUTION_UNSPECIFIED = 0;
  COMMON_CONFLICT_RESOLUTION_MERGE = 1;
  COMMON_CONFLICT_RESOLUTION_OVERWRITE = 2;
  COMMON_CONFLICT_RESOLUTION_FAIL = 3;
}
```

---

### conflict_strategy.proto {#conflict_strategy}

**Path**: `gcommon/v1/common/conflict_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `ConflictStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/conflict_strategy.proto
// version: 1.0.1
// guid: 1f8fb98d-0197-472d-9b17-681ebc9772bf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConflictStrategy {
  CONFLICT_STRATEGY_UNSPECIFIED = 0;
  CONFLICT_STRATEGY_TIMESTAMP = 1; // Timestamp-based detection
  CONFLICT_STRATEGY_VECTOR_CLOCK = 2; // Vector clock-based detection
  CONFLICT_STRATEGY_CAUSAL = 3; // Causal consistency detection
}
```

---

### consistency_level.proto {#consistency_level}

**Path**: `gcommon/v1/common/consistency_level.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Enums** (1): `DatabaseConsistencyLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/consistency_level.proto
// version: 1.0.1
// guid: 5eaa6727-c2ff-40f4-b746-6782b5b18b05
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConsistencyLevel defines the data consistency requirements for database operations.
 * Controls the trade-off between consistency, availability, and partition tolerance.
 */
enum DatabaseConsistencyLevel {
  // Default unspecified consistency level
  DATABASE_CONSISTENCY_LEVEL_UNSPECIFIED = 0;

  // Eventual consistency - may read stale data but eventually consistent
  DATABASE_CONSISTENCY_LEVEL_EVENTUAL = 1;

  // Strong consistency - always reads most recent committed data
  DATABASE_CONSISTENCY_LEVEL_STRONG = 2;

  // Bounded staleness - reads data within specified time bounds
  DATABASE_CONSISTENCY_LEVEL_BOUNDED_STALENESS = 3;
}
```

---

### consumer_group_state.proto {#consumer_group_state}

**Path**: `gcommon/v1/common/consumer_group_state.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ConsumerGroupState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group_state.proto
// version: 1.0.1
// guid: 3c66ccb4-a4d4-43f9-952e-510a7b8086c9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConsumerGroupState {
  CONSUMER_GROUP_STATE_UNSPECIFIED = 0;
  CONSUMER_GROUP_STATE_STABLE = 1; // Group is stable with assigned partitions
  CONSUMER_GROUP_STATE_PREPARING_REBALANCE = 2; // Preparing for rebalance
  CONSUMER_GROUP_STATE_COMPLETING_REBALANCE = 3; // Completing rebalance operation
  CONSUMER_GROUP_STATE_DEAD = 4; // Group has no active consumers
  CONSUMER_GROUP_STATE_EMPTY = 5; // Group exists but no consumers
}
```

---

### consumer_state.proto {#consumer_state}

**Path**: `gcommon/v1/common/consumer_state.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Enums** (1): `ConsumerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/consumer_state.proto
// file: proto/gcommon/v1/queue/consumer_state.proto
// version: 1.0.1
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * State of a queue consumer.
 */
enum ConsumerState {
  // Default unspecified state
  CONSUMER_STATE_UNSPECIFIED = 0;

  // Consumer is active and processing messages
  CONSUMER_STATE_ACTIVE = 1;

  // Consumer is idle (connected but not processing)
  CONSUMER_STATE_IDLE = 2;

  // Consumer is paused
  CONSUMER_STATE_PAUSED = 3;

  // Consumer is stopped
  CONSUMER_STATE_STOPPED = 4;

  // Consumer has encountered an error
  CONSUMER_STATE_ERROR = 5;

  // Consumer is connecting
  CONSUMER_STATE_CONNECTING = 6;

  // Consumer is disconnected
  CONSUMER_STATE_DISCONNECTED = 7;
}
```

---

### content_type.proto {#content_type}

**Path**: `gcommon/v1/common/content_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `ContentType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/content_type.proto
// version: 1.0.1
// guid: 8bb9871c-690b-4fb4-83e1-735d6815a620
//
// ContentType enumerates common MIME types.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Well-known MIME types supported by the server.
enum ContentType {
  CONTENT_TYPE_UNSPECIFIED = 0;
  CONTENT_TYPE_HTML = 1;
  CONTENT_TYPE_JSON = 2;
  CONTENT_TYPE_XML = 3;
  CONTENT_TYPE_TEXT = 4;
  CONTENT_TYPE_BINARY = 5;
}
```

---

### cookie_same_site.proto {#cookie_same_site}

**Path**: `gcommon/v1/common/cookie_same_site.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `CookieSameSite`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cookie_same_site.proto
// version: 1.0.1
// guid: b38945ee-58e0-4d5a-9637-f2c57a5a9b31
//
// CookieSameSite defines SameSite settings for cookies.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CookieSameSite {
  COOKIE_SAME_SITE_UNSPECIFIED = 0;
  COOKIE_SAME_SITE_DEFAULT = 1;
  COOKIE_SAME_SITE_LAX = 2;
  COOKIE_SAME_SITE_STRICT = 3;
  COOKIE_SAME_SITE_NONE = 4;
}
```

---

### coordinator_state.proto {#coordinator_state}

**Path**: `gcommon/v1/common/coordinator_state.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `CoordinatorState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/coordinator_state.proto
// version: 1.0.1
// guid: 834ccf4a-176f-479d-87af-833f052ccf71

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CoordinatorState {
  COORDINATOR_STATE_UNSPECIFIED = 0;
  COORDINATOR_STATE_ACTIVE = 1; // Coordinator is active
  COORDINATOR_STATE_LOADING = 2; // Coordinator is loading metadata
  COORDINATOR_STATE_NOT_COORDINATOR = 3; // Node is not the coordinator
}
```

---

### daily_usage.proto {#daily_usage}

**Path**: `gcommon/v1/common/daily_usage.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Messages** (1): `DailyUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/daily_usage.proto
// version: 1.0.0
// guid: d5da361d-f967-4f15-9afa-951271665ecb

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DailyUsage {
  string date = 1; // YYYY-MM-DD format
  int32 request_count = 2 [(buf.validate.field).int32.gte = 0];
}
```

---

