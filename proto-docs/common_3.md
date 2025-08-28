# common_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 20
- **Services**: 0
- **Enums**: 30

## Files in this Module

- [key_value.proto](#key_value)
- [load_balance_strategy.proto](#load_balance_strategy)
- [load_balancing_strategy.proto](#load_balancing_strategy)
- [location_info.proto](#location_info)
- [log_entry.proto](#log_entry)
- [log_level.proto](#log_level)
- [log_sort_field.proto](#log_sort_field)
- [log_statistics.proto](#log_statistics)
- [logger_status.proto](#logger_status)
- [media_type.proto](#media_type)
- [member_role.proto](#member_role)
- [merge_strategy.proto](#merge_strategy)
- [message_state.proto](#message_state)
- [metadata_status.proto](#metadata_status)
- [metric_point.proto](#metric_point)
- [metric_source.proto](#metric_source)
- [metric_status.proto](#metric_status)
- [metric_type.proto](#metric_type)
- [metrics_alert_severity.proto](#metrics_alert_severity)
- [metrics_error_stats.proto](#metrics_error_stats)
- [metrics_export_format.proto](#metrics_export_format)
- [metrics_provider_type.proto](#metrics_provider_type)
- [metrics_retention_info.proto](#metrics_retention_info)
- [metrics_time_range.proto](#metrics_time_range)
- [metrics_validation_result.proto](#metrics_validation_result)
- [mfa_method.proto](#mfa_method)
- [mfa_setup_instruction.proto](#mfa_setup_instruction)
- [mfa_type.proto](#mfa_type)
- [middleware_type.proto](#middleware_type)
- [nack_error_category.proto](#nack_error_category)
- [node_state.proto](#node_state)
- [notification_channel_type.proto](#notification_channel_type)
- [notification_frequency.proto](#notification_frequency)
- [notification_message.proto](#notification_message)
- [notification_trigger.proto](#notification_trigger)
- [notification_type.proto](#notification_type)
- [numeric_format.proto](#numeric_format)
- [o_auth2_credentials.proto](#o_auth2_credentials)
- [o_auth_client.proto](#o_auth_client)
- [oauth2_flow_type.proto](#oauth2_flow_type)
- [offset_reset_strategy.proto](#offset_reset_strategy)
- [offset_type.proto](#offset_type)
- [ordering_level.proto](#ordering_level)
- [organization_access_control.proto](#organization_access_control)
- [organization_compliance_settings.proto](#organization_compliance_settings)
- [organization_notification_settings.proto](#organization_notification_settings)
- [organization_resource_limits.proto](#organization_resource_limits)
- [organization_status.proto](#organization_status)
- [pagination.proto](#pagination)
- [pagination_info.proto](#pagination_info)
---


## Detailed Documentation

### key_value.proto {#key_value}

**Path**: `gcommon/v1/common/key_value.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `KeyValue`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/key_value.proto
// version: 1.0.0
// guid: 947f80d9-fca1-447c-aa5e-4f8b18e65816
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Generic key-value pair for metadata and configuration storage.
 * Provides a simple, reusable structure for storing arbitrary
 * string-based key-value data across all GCommon modules.
 */
message KeyValue {
  // The key identifier for this pair
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // The value associated with the key
  string value = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### load_balance_strategy.proto {#load_balance_strategy}

**Path**: `gcommon/v1/common/load_balance_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `LoadBalanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/load_balance_strategy.proto
// version: 1.0.1
// guid: d147b3b5-5e20-4bf9-9cfe-467e528f59a7
//
// LoadBalanceStrategy lists supported balancing algorithms.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum LoadBalanceStrategy {
  LOAD_BALANCE_STRATEGY_UNSPECIFIED = 0;
  LOAD_BALANCE_STRATEGY_ROUND_ROBIN = 1;
  LOAD_BALANCE_STRATEGY_LEAST_CONNECTIONS = 2;
  LOAD_BALANCE_STRATEGY_IP_HASH = 3;
}
```

---

### load_balancing_strategy.proto {#load_balancing_strategy}

**Path**: `gcommon/v1/common/load_balancing_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `LoadBalancingStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/load_balancing_strategy.proto
// version: 1.0.1
// guid: 0d1e2f3a-4b5c-6d7e-8f9a-0b1c2d3e4f5a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Load balancing strategies.
 */
enum LoadBalancingStrategy {
  // Default unspecified strategy
  LOAD_BALANCING_STRATEGY_UNSPECIFIED = 0;

  // Round-robin distribution
  LOAD_BALANCING_STRATEGY_ROUND_ROBIN = 1;

  // Weighted round-robin
  LOAD_BALANCING_STRATEGY_WEIGHTED_ROUND_ROBIN = 2;

  // Least connections
  LOAD_BALANCING_STRATEGY_LEAST_CONNECTIONS = 3;

  // Random distribution
  LOAD_BALANCING_STRATEGY_RANDOM = 4;

  // Hash-based distribution
  LOAD_BALANCING_STRATEGY_HASH = 5;

  // Priority-based distribution
  LOAD_BALANCING_STRATEGY_PRIORITY = 6;
}
```

---

### location_info.proto {#location_info}

**Path**: `gcommon/v1/common/location_info.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `LocationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/location_info.proto
// version: 1.0.0
// guid: 9baeac22-b20b-45fb-89cf-b857c53282d8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message LocationInfo {
  string country = 1 [(buf.validate.field).string.min_len = 1];
  string region = 2 [(buf.validate.field).string.min_len = 1];
  string city = 3 [(buf.validate.field).string.min_len = 1];
  double latitude = 4 [(buf.validate.field).double.gte = 0.0];
  double longitude = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### log_entry.proto {#log_entry}

**Path**: `gcommon/v1/common/log_entry.proto` **Package**: `gcommon.v1.common` **Lines**: 63

**Messages** (1): `LogEntry`

**Imports** (7):

- `gcommon/v1/common/error_info.proto`
- `gcommon/v1/common/log_level.proto`
- `gcommon/v1/common/source_location.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_entry.proto
// version: 1.0.0
// guid: 86cfa864-b9da-428c-9ca9-78f614600049

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_info.proto";
import "gcommon/v1/common/log_level.proto";
import "gcommon/v1/common/source_location.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogEntry represents a single structured log event
message LogEntry {
  // Log level
  LogLevel level = 1;

  // Log message
  string message = 2;

  // Timestamp of the log event
  google.protobuf.Timestamp timestamp = 3;

  // Logger name
  string logger = 4;

  // Thread or goroutine identifier
  string thread = 5;

  // Source code location
  SourceLocation source = 6;

  // Structured fields for context
  map<string, google.protobuf.Any> fields = 7;

  // Tags for categorization
  repeated string tags = 8;

  // Trace ID for distributed tracing
  string trace_id = 9;

  // Span ID for distributed tracing
  string span_id = 10;

  // User ID associated with the log
  string user_id = 11 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request ID for correlation
  string request_id = 12;

  // Detailed error information
  ErrorInfo error_info = 13;
}
```

---

### log_level.proto {#log_level}

**Path**: `gcommon/v1/common/log_level.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `LogLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_level.proto
// version: 1.0.1
// guid: ef4e8667-0bff-4dda-bb43-56d0a1ef8421

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogLevel defines severity levels for log entries
enum LogLevel {
  LOG_LEVEL_UNSPECIFIED = 0;
  LOG_LEVEL_TRACE = 1;
  LOG_LEVEL_DEBUG = 2;
  LOG_LEVEL_INFO = 3;
  LOG_LEVEL_WARN = 4;
  LOG_LEVEL_ERROR = 5;
  LOG_LEVEL_FATAL = 6;
}
```

---

### log_sort_field.proto {#log_sort_field}

**Path**: `gcommon/v1/common/log_sort_field.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `LogSortField`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_sort_field.proto
// version: 1.0.1
// guid: 8d1776a3-51f0-43c4-8199-698ee5ba98e7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogSortField enumerates fields usable for log sorting
enum LogSortField {
  LOG_SORT_FIELD_UNSPECIFIED = 0;
  LOG_SORT_FIELD_TIMESTAMP = 1;
  LOG_SORT_FIELD_LEVEL = 2;
  LOG_SORT_FIELD_LOGGER = 3;
  LOG_SORT_FIELD_MESSAGE = 4;
}
```

---

### log_statistics.proto {#log_statistics}

**Path**: `gcommon/v1/common/log_statistics.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `LogStatistics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_statistics.proto
// version: 1.0.0
// guid: 98acfd30-4a7f-43f6-ac8d-f10a598a805a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogStatistics provides aggregated metrics about log entries
message LogStatistics {
  // Total log entries
  int64 total_entries = 1 [(buf.validate.field).int64.gte = 0];

  // Entries per second
  double entries_per_second = 2 [(buf.validate.field).double.gte = 0.0];

  // Average entry size
  int64 average_size = 3 [(buf.validate.field).int64.gte = 0];

  // Total size of all log entries
  int64 total_size = 4 [(buf.validate.field).int64.gte = 0];

  // Count of log entries with level ERROR
  int64 error_count = 5 [(buf.validate.field).int64.gte = 0];

  // Count of log entries with level WARNING
  int64 warning_count = 6 [(buf.validate.field).int64.gte = 0];
}
```

---

### logger_status.proto {#logger_status}

**Path**: `gcommon/v1/common/logger_status.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `LoggerStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logger_status.proto
// version: 1.0.1
// guid: c65806e5-27c2-4c3e-8f3b-e23b66bca610

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LoggerStatus represents health of a logger instance
enum LoggerStatus {
  LOGGER_STATUS_UNSPECIFIED = 0;
  LOGGER_STATUS_ACTIVE = 1;
  LOGGER_STATUS_INACTIVE = 2;
  LOGGER_STATUS_ERROR = 3;
}
```

---

### media_type.proto {#media_type}

**Path**: `gcommon/v1/common/media_type.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `MediaType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_type.proto
// version: 1.0.1
// guid: d13c4939-a91b-4cb8-85e6-09ddda85220e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Media type classification for library items.
enum MediaType {
  MEDIA_TYPE_UNSPECIFIED = 0;
  MEDIA_TYPE_MOVIE = 1;
  MEDIA_TYPE_TV_EPISODE = 2;
  MEDIA_TYPE_DOCUMENTARY = 3;
  MEDIA_TYPE_ANIME = 4;
  MEDIA_TYPE_AUDIOBOOK = 5;
  MEDIA_TYPE_PODCAST = 6;
  MEDIA_TYPE_MUSIC = 7;
  MEDIA_TYPE_LECTURE = 8;
  MEDIA_TYPE_INTERVIEW = 9;
  MEDIA_TYPE_RADIO_SHOW = 10;
}
```

---

### member_role.proto {#member_role}

**Path**: `gcommon/v1/common/member_role.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `MemberRole`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/member_role.proto
// version: 1.0.1
// guid: b6c7d8e9-012b-467a-1234-789012345678

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MemberRole {
  MEMBER_ROLE_UNSPECIFIED = 0;
  MEMBER_ROLE_OWNER = 1;
  MEMBER_ROLE_ADMIN = 2;
  MEMBER_ROLE_MEMBER = 3;
  MEMBER_ROLE_VIEWER = 4;
  MEMBER_ROLE_GUEST = 5;
}
```

---

### merge_strategy.proto {#merge_strategy}

**Path**: `gcommon/v1/common/merge_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `MergeStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/merge_strategy.proto
// version: 1.0.1
// guid: 559ca0d7-17d4-49ab-861d-febdc5862a47

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MergeStrategy {
  MERGE_STRATEGY_UNSPECIFIED = 0;
  MERGE_STRATEGY_REPLACE = 1;
  MERGE_STRATEGY_MERGE_DEEP = 2;
  MERGE_STRATEGY_MERGE_SHALLOW = 3;
  MERGE_STRATEGY_ARRAY_CONCAT = 4;
  MERGE_STRATEGY_ARRAY_REPLACE = 5;
  MERGE_STRATEGY_ARRAY_MERGE = 6;
  MERGE_STRATEGY_CUSTOM = 7;
}
```

---

### message_state.proto {#message_state}

**Path**: `gcommon/v1/common/message_state.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `MessageState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_state.proto
// version: 1.0.1
// guid: 4eba7921-816c-420b-8880-172c0631fa22

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// MessageState represents the lifecycle state of a queue message.
enum MessageState {
  // Default unspecified state.
  MESSAGE_STATE_UNSPECIFIED = 0;

  // Message is queued and awaiting delivery.
  MESSAGE_STATE_PENDING = 1;

  // Message has been delivered to a consumer.
  MESSAGE_STATE_DELIVERED = 2;

  // Consumer acknowledged successful processing.
  MESSAGE_STATE_ACKNOWLEDGED = 3;

  // Delivery failed and will be retried.
  MESSAGE_STATE_FAILED = 4;

  // Message moved to dead letter queue.
  MESSAGE_STATE_DEAD_LETTER = 5;

  // Message expired before processing.
  MESSAGE_STATE_EXPIRED = 6;
}
```

---

### metadata_status.proto {#metadata_status}

**Path**: `gcommon/v1/common/metadata_status.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `MetadataStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/metadata_status.proto
// version: 1.0.1
// guid: b82301c8-c50d-454c-a434-ae44d4199677

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MetadataStatus {
  METADATA_STATUS_UNSPECIFIED = 0;
  METADATA_STATUS_ACTIVE = 1;
  METADATA_STATUS_INACTIVE = 2;
  METADATA_STATUS_DRAFT = 3;
  METADATA_STATUS_DEPRECATED = 4;
  METADATA_STATUS_DELETED = 5;
  METADATA_STATUS_ERROR = 6;
}
```

---

### metric_point.proto {#metric_point}

**Path**: `gcommon/v1/common/metric_point.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `MetricPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/metric_point.proto
// version: 1.0.0
// guid: 33062748-1b9e-47b6-9fbe-be60f9f3fb7d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common metrics data point for standardized metric collection.
 * Provides a unified structure for metrics across all GCommon modules
 * with timestamp, labels, and unit information for observability.
 */
message MetricPoint {
  // Metric name identifier (e.g., "request_count", "response_time")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### metric_source.proto {#metric_source}

**Path**: `gcommon/v1/common/metric_source.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Enums** (1): `MetricSource`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_source.proto
// version: 1.0.1
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// MetricSource represents different sources of metrics data
enum MetricSource {
  // Unspecified metric source
  METRIC_SOURCE_UNSPECIFIED = 0;

  // Application metrics
  METRIC_SOURCE_APPLICATION = 1;

  // System metrics
  METRIC_SOURCE_SYSTEM = 2;

  // Infrastructure metrics
  METRIC_SOURCE_INFRASTRUCTURE = 3;

  // Container metrics
  METRIC_SOURCE_CONTAINER = 4;

  // Kubernetes metrics
  METRIC_SOURCE_KUBERNETES = 5;

  // Database metrics
  METRIC_SOURCE_DATABASE = 6;

  // Network metrics
  METRIC_SOURCE_NETWORK = 7;

  // Storage metrics
  METRIC_SOURCE_STORAGE = 8;

  // Security metrics
  METRIC_SOURCE_SECURITY = 9;

  // Business metrics
  METRIC_SOURCE_BUSINESS = 10;

  // Custom metrics
  METRIC_SOURCE_CUSTOM = 11;

  // Third-party metrics
  METRIC_SOURCE_THIRD_PARTY = 12;

  // Synthetic metrics
  METRIC_SOURCE_SYNTHETIC = 13;

  // Log-derived metrics
  METRIC_SOURCE_LOG_DERIVED = 14;
}
```

---

### metric_status.proto {#metric_status}

**Path**: `gcommon/v1/common/metric_status.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `MetricStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_status.proto
// version: 1.0.1
// guid: 0f4752cc-8120-45bb-a7c9-1fb475c11998

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MetricStatus indicates the lifecycle state of a metric definition.
 */
enum MetricStatus {
  // Unspecified status.
  METRIC_STATUS_UNSPECIFIED = 0;

  // Metric is active and being collected.
  METRIC_STATUS_ACTIVE = 1;

  // Metric is temporarily disabled.
  METRIC_STATUS_DISABLED = 2;

  // Metric is in error state and not reliable.
  METRIC_STATUS_ERROR = 3;

  // Metric has been removed and should no longer be used.
  METRIC_STATUS_DELETED = 4;
}
```

---

### metric_type.proto {#metric_type}

**Path**: `gcommon/v1/common/metric_type.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `MetricsMetricType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_type.proto
// version: 1.0.1
// guid: ca7deb46-60dd-4b1b-a48a-ad30f651f2a2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MetricType defines the different types of metrics that can be collected.
 * Each type has specific semantics for how values are interpreted and aggregated.
 */
enum MetricsMetricType {
  // Unspecified metric type
  METRIC_TYPE_UNSPECIFIED = 0;

  // Counter: A monotonically increasing value (can only go up)
  METRIC_TYPE_COUNTER = 1;

  // Gauge: A value that can go up and down
  METRIC_TYPE_GAUGE = 2;

  // Histogram: Distribution of observed values in buckets
  METRIC_TYPE_HISTOGRAM = 3;

  // Summary: Similar to histogram but with configurable quantiles
  METRIC_TYPE_SUMMARY = 4;

  // Timer: Specialized counter for measuring durations
  METRIC_TYPE_TIMER = 5;

  // Set: Track unique values (cardinality metric)
  METRIC_TYPE_SET = 6;
}
```

---

### metrics_alert_severity.proto {#metrics_alert_severity}

**Path**: `gcommon/v1/common/metrics_alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `MetricsAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alert_severity.proto
// version: 1.0.1
// guid: f1a2b3c4-5678-901c-5678-123456789012

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MetricsAlertSeverity {
  METRICS_ALERT_SEVERITY_UNSPECIFIED = 0;
  METRICS_ALERT_SEVERITY_LOW = 1;
  METRICS_ALERT_SEVERITY_MEDIUM = 2;
  METRICS_ALERT_SEVERITY_HIGH = 3;
  METRICS_ALERT_SEVERITY_CRITICAL = 4;
}
```

---

### metrics_error_stats.proto {#metrics_error_stats}

**Path**: `gcommon/v1/common/metrics_error_stats.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `MetricsErrorStats`

**Imports** (3):

- `gcommon/v1/common/error_type_count.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_stats.proto
// version: 1.1.0
// guid: ba56b09c-77ad-41e9-80ae-0a95c96c8394

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_type_count.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MetricsErrorStats {
  // Total number of errors
  int64 total_errors = 1 [(buf.validate.field).int64.gte = 0];

  // Error rate (errors per total operations)
  double error_rate = 2 [(buf.validate.field).double.gte = 0.0];

  // Most common error types
  repeated ErrorTypeCount error_types = 3 [(buf.validate.field).repeated.min_items = 1];

  // Recent error trend (increasing/decreasing/stable)
  string error_trend = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### metrics_export_format.proto {#metrics_export_format}

**Path**: `gcommon/v1/common/metrics_export_format.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `MetricsExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_format.proto
// version: 1.0.1
// guid: b4c5d6e7-890b-245a-9012-567890123456

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MetricsExportFormat {
  METRICS_EXPORT_FORMAT_UNSPECIFIED = 0;
  METRICS_EXPORT_FORMAT_PROMETHEUS = 1;
  METRICS_EXPORT_FORMAT_JSON = 2;
  METRICS_EXPORT_FORMAT_CSV = 3;
  METRICS_EXPORT_FORMAT_OPENTELEMETRY = 4;
}
```

---

### metrics_provider_type.proto {#metrics_provider_type}

**Path**: `gcommon/v1/common/metrics_provider_type.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Enums** (1): `MetricsProviderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/provider_type.proto
// version: 1.0.1
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Provider type enumeration.
 * Defines the different types of metrics providers supported.
 */
enum MetricsProviderType {
  METRICS_PROVIDER_TYPE_UNSPECIFIED = 0;
  METRICS_PROVIDER_TYPE_PROMETHEUS = 1;
  METRICS_PROVIDER_TYPE_INFLUXDB = 2;
  METRICS_PROVIDER_TYPE_GRAPHITE = 3;
  METRICS_PROVIDER_TYPE_DATADOG = 4;
  METRICS_PROVIDER_TYPE_NEW_RELIC = 5;
  METRICS_PROVIDER_TYPE_CLOUDWATCH = 6;
  METRICS_PROVIDER_TYPE_STACKDRIVER = 7;
  METRICS_PROVIDER_TYPE_CUSTOM = 8;
}
```

---

### metrics_retention_info.proto {#metrics_retention_info}

**Path**: `gcommon/v1/common/metrics_retention_info.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `MetricsRetentionInfo`

**Imports** (3):

- `gcommon/v1/common/metrics_retention_policy_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_info.proto
// version: 1.0.0
// guid: 1274ff0f-5103-48bf-a7f2-6068f7fbb53e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/metrics_retention_policy_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MetricsRetentionInfo {
  int64 total_retained_bytes = 1 [(buf.validate.field).int64.gte = 0];
  int64 total_purged_bytes = 2 [(buf.validate.field).int64.gte = 0];
  string oldest_data_age = 3 [(buf.validate.field).string.min_len = 1];
  repeated gcommon.v1.common.MetricsRetentionPolicyConfig policies = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### metrics_time_range.proto {#metrics_time_range}

**Path**: `gcommon/v1/common/metrics_time_range.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `CommonTimeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/metrics_time_range.proto
// version: 1.0.1
// guid: cdd6726e-7f39-47bb-b9d3-23e7e3a1be64
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common time range specification for filtering operations.
 * Provides standardized time-based filtering across all GCommon modules
 * for queries, reports, and data analysis.
 */
message CommonTimeRange {
  // Start time (inclusive) - operations at or after this time are included
  google.protobuf.Timestamp start_time = 1;

  // End time (exclusive) - operations before this time are included
  google.protobuf.Timestamp end_time = 2;
}
```

---

### metrics_validation_result.proto {#metrics_validation_result}

**Path**: `gcommon/v1/common/metrics_validation_result.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `MetricsValidationResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/validation_result.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174025

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ValidationResult contains validation results from creation.
 */
message MetricsValidationResult {
  // Whether the configuration is valid
  bool valid = 1;

  // Validation errors
  repeated string errors = 2 [(buf.validate.field).repeated.min_items = 1];

  // Validation warnings
  repeated string warnings = 3 [(buf.validate.field).repeated.min_items = 1];

  // Configuration suggestions
  repeated string suggestions = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### mfa_method.proto {#mfa_method}

**Path**: `gcommon/v1/common/mfa_method.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `MfaMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_method.proto
// version: 1.0.1
// guid: 123e4567-e89b-12d3-a456-426614174123

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Multi-factor authentication methods supported by the system.
 */
enum MfaMethod {
  // Unspecified MFA method
  MFA_METHOD_UNSPECIFIED = 0;

  // SMS-based verification
  MFA_METHOD_SMS = 1;

  // Email-based verification
  MFA_METHOD_EMAIL = 2;

  // Time-based one-time password (TOTP)
  MFA_METHOD_TOTP = 3;

  // Hardware security key
  MFA_METHOD_HARDWARE_KEY = 4;
}
```

---

### mfa_setup_instruction.proto {#mfa_setup_instruction}

**Path**: `gcommon/v1/common/mfa_setup_instruction.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `MfaSetupInstruction`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_setup_instruction.proto
// version: 1.0.0
// guid: bf15a5c9-23b0-4e2d-9583-24ed000c4656

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MfaSetupInstruction {
  MfaMethod method = 1;
  string instruction = 2 [(buf.validate.field).string.min_len = 1];
  string qr_code = 3 [(buf.validate.field).string.min_len = 1];
  string secret_key = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### mfa_type.proto {#mfa_type}

**Path**: `gcommon/v1/common/mfa_type.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `MFAType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_type.proto
// version: 1.0.1
// guid: a5e413ea-00e3-4585-9e9d-30348138c407

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MFAType enumerates supported multi-factor authentication methods.
 */
enum MFAType {
  // Unknown or unspecified MFA method
  MFA_TYPE_UNSPECIFIED = 0;

  // Time-based one-time password via authenticator apps
  MFA_TYPE_TOTP = 1;

  // One-time code delivered via SMS
  MFA_TYPE_SMS = 2;

  // One-time code delivered via email
  MFA_TYPE_EMAIL = 3;

  // Push notification to a trusted device
  MFA_TYPE_PUSH = 4;
}
```

---

### middleware_type.proto {#middleware_type}

**Path**: `gcommon/v1/common/middleware_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `MiddlewareType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/middleware_type.proto
// version: 1.0.1
// guid: e6a7b5cb-240b-4636-bb49-9615874e9f9d
//
// MiddlewareType represents categories of HTTP middleware.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MiddlewareType {
  MIDDLEWARE_TYPE_UNSPECIFIED = 0;
  MIDDLEWARE_TYPE_LOGGING = 1;
  MIDDLEWARE_TYPE_AUTHENTICATION = 2;
  MIDDLEWARE_TYPE_METRICS = 3;
  MIDDLEWARE_TYPE_COMPRESSION = 4;
  MIDDLEWARE_TYPE_CORS = 5;
  MIDDLEWARE_TYPE_RATE_LIMIT = 6;
}
```

---

### nack_error_category.proto {#nack_error_category}

**Path**: `gcommon/v1/common/nack_error_category.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `NackErrorCategory`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_error_category.proto
// version: 1.0.1
// guid: 8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Categories of NACK errors.
 */
enum NackErrorCategory {
  // Default unspecified category
  NACK_ERROR_CATEGORY_UNSPECIFIED = 0;

  // Temporary/transient error
  NACK_ERROR_CATEGORY_TEMPORARY = 1;

  // Permanent error (should not retry)
  NACK_ERROR_CATEGORY_PERMANENT = 2;

  // Configuration error
  NACK_ERROR_CATEGORY_CONFIGURATION = 3;

  // Network error
  NACK_ERROR_CATEGORY_NETWORK = 4;

  // Authentication/authorization error
  NACK_ERROR_CATEGORY_AUTH = 5;

  // Rate limiting error
  NACK_ERROR_CATEGORY_RATE_LIMIT = 6;
}
```

---

### node_state.proto {#node_state}

**Path**: `gcommon/v1/common/node_state.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `NodeState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/node_state.proto
// version: 1.0.1
// guid: 9ee731f7-a1ea-4298-8579-c001d3b09060

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * State of a cluster node.
 */
enum NodeState {
  // Default unspecified state
  NODE_STATE_UNSPECIFIED = 0;

  // Node is active and healthy
  NODE_STATE_ACTIVE = 1;

  // Node is inactive but reachable
  NODE_STATE_INACTIVE = 2;

  // Node is unreachable
  NODE_STATE_UNREACHABLE = 3;

  // Node is joining the cluster
  NODE_STATE_JOINING = 4;

  // Node is leaving the cluster
  NODE_STATE_LEAVING = 5;
}
```

---

### notification_channel_type.proto {#notification_channel_type}

**Path**: `gcommon/v1/common/notification_channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `NotificationChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/notification_channel_type.proto
// version: 1.0.1
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Types of notification channels.
 */
enum NotificationChannelType {
  // Default unspecified type
  NOTIFICATION_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email notifications
  NOTIFICATION_CHANNEL_TYPE_EMAIL = 1;

  // Slack notifications
  NOTIFICATION_CHANNEL_TYPE_SLACK = 2;

  // SMS notifications
  NOTIFICATION_CHANNEL_TYPE_SMS = 3;

  // Webhook notifications
  NOTIFICATION_CHANNEL_TYPE_WEBHOOK = 4;

  // PagerDuty integration
  NOTIFICATION_CHANNEL_TYPE_PAGERDUTY = 5;
}
```

---

### notification_frequency.proto {#notification_frequency}

**Path**: `gcommon/v1/common/notification_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `NotificationFrequency`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/notification_frequency.proto
// version: 1.0.0
// guid: 49798a1d-bd35-44a3-bcdc-4e5d2bfaa330

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message NotificationFrequency {
  // Daily digest enabled
  bool daily_digest = 1;

  // Weekly summary enabled
  bool weekly_summary = 2;

  // Instant notifications enabled
  bool instant_notifications = 3;

  // Quiet hours start time (24-hour format, e.g., "22:00")
  string quiet_hours_start = 4 [(buf.validate.field).string.min_len = 1];

  // Quiet hours end time (24-hour format, e.g., "08:00")
  string quiet_hours_end = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### notification_message.proto {#notification_message}

**Path**: `gcommon/v1/common/notification_message.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `NotificationMessage`

**Imports** (6):

- `gcommon/v1/common/delivery_channel.proto`
- `gcommon/v1/common/delivery_status.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/notification_message.proto
// version: 1.0.0
// guid: 145b3e1e-f6ae-4bbf-9efb-78ebe3c659c8
// file: proto/gcommon/v1/common/notification_message.proto
//
// Message definitions for notification module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_channel.proto";
import "gcommon/v1/common/delivery_status.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Notification message containing content and delivery details.
 * Supports scheduling, multi-channel delivery, and custom data.
 */
message NotificationMessage {
  // Unique notification identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Subject or title of the notification
  string subject = 2;

  // Body text or formatted content
  string body = 3;

  // Structured data payload for templating
  google.protobuf.Any data = 4 [lazy = true];

  // Delivery channels for this notification
  repeated DeliveryChannel channels = 5;

  // Desired send time (defaults to immediate)
  google.protobuf.Timestamp send_at = 6 [lazy = true];

  // Current delivery status
  DeliveryStatus status = 7;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 8 [lazy = true, (buf.validate.field).required = true];
}
```

---

### notification_trigger.proto {#notification_trigger}

**Path**: `gcommon/v1/common/notification_trigger.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `NotificationTrigger`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/notification_trigger.proto
// version: 1.0.1
// guid: e23c0d82-9395-4a27-840c-5765e4aaffbb

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum NotificationTrigger {
  NOTIFICATION_TRIGGER_UNSPECIFIED = 0;
  NOTIFICATION_TRIGGER_CHANGE = 1;
  NOTIFICATION_TRIGGER_DELETE = 2;
  NOTIFICATION_TRIGGER_ERROR = 3;
  NOTIFICATION_TRIGGER_APPROVAL = 4;
  NOTIFICATION_TRIGGER_DEPLOYMENT = 5;
  NOTIFICATION_TRIGGER_ROLLBACK = 6;
  NOTIFICATION_TRIGGER_SCHEDULE = 7;
}
```

---

### notification_type.proto {#notification_type}

**Path**: `gcommon/v1/common/notification_type.proto` **Package**: `gcommon.v1.common` **Lines**: 64

**Enums** (1): `NotificationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/types/notification_type.proto
// version: 1.0.1
// guid: c1381807-afc6-4139-8737-8691569a66f9
// file: proto/gcommon/v1/metrics/notification_type.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * NotificationType defines the types of notifications for metric alerts.
 * Used to specify how alerts should be delivered to users.
 */
enum NotificationType {
  // Unspecified notification type (default)
  NOTIFICATION_TYPE_UNSPECIFIED = 0;

  // Email notification
  NOTIFICATION_TYPE_EMAIL = 1;

  // SMS text message
  NOTIFICATION_TYPE_SMS = 2;

  // Push notification (mobile app)
  NOTIFICATION_TYPE_PUSH = 3;

  // Slack message
  NOTIFICATION_TYPE_SLACK = 4;

  // Microsoft Teams message
  NOTIFICATION_TYPE_TEAMS = 5;

  // Discord message
  NOTIFICATION_TYPE_DISCORD = 6;

  // PagerDuty incident
  NOTIFICATION_TYPE_PAGERDUTY = 7;

  // Webhook/HTTP POST
  NOTIFICATION_TYPE_WEBHOOK = 8;

  // In-app notification
  NOTIFICATION_TYPE_IN_APP = 9;

  // SNMP trap
  NOTIFICATION_TYPE_SNMP = 10;

  // Telegram message
  NOTIFICATION_TYPE_TELEGRAM = 11;

  // Matrix message
  NOTIFICATION_TYPE_MATRIX = 12;

  // Voice call
  NOTIFICATION_TYPE_VOICE = 13;
}
```

---

### numeric_format.proto {#numeric_format}

**Path**: `gcommon/v1/common/numeric_format.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `NumericFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/numeric_format.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * NumericFormat defines how numeric values should be formatted.
 * Specifies the display format for numeric metric values.
 */
enum NumericFormat {
  // Unspecified format
  NUMERIC_FORMAT_UNSPECIFIED = 0;

  // Default formatting
  NUMERIC_FORMAT_DEFAULT = 1;

  // Scientific notation
  NUMERIC_FORMAT_SCIENTIFIC = 2;

  // Engineering notation
  NUMERIC_FORMAT_ENGINEERING = 3;

  // Percentage format
  NUMERIC_FORMAT_PERCENTAGE = 4;
}
```

---

### o_auth2_credentials.proto {#o_auth2_credentials}

**Path**: `gcommon/v1/common/o_auth2_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `OAuth2Credentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/o_auth2_credentials.proto
// version: 1.0.0
// guid: ebee6621-9f47-4dc4-a8ed-59da2ba599a2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 credentials for authorization code flow authentication.
 * Implements standard OAuth2 authorization code exchange for tokens.
 */
message OAuth2Credentials {
  // Authorization code received from OAuth2 provider
  string code = 1;

  // Redirect URI that was used in the authorization request
  // Must match the URI registered with the OAuth2 provider
  string redirect_uri = 2 [ (buf.validate.field).string.uri = true ];

  // OAuth2 client identifier
  string client_id = 3;

  // OAuth2 client secret (for confidential clients only)
  // Should be omitted for public clients (e.g., mobile apps, SPAs)
  string client_secret = 4;
}
```

---

### o_auth_client.proto {#o_auth_client}

**Path**: `gcommon/v1/common/o_auth_client.proto` **Package**: `gcommon.v1.common` **Lines**: 69

**Messages** (1): `OAuthClient`

**Imports** (4):

- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/o_auth_client.proto
// version: 1.0.0
// guid: 436333b4-e6f3-4a6d-ad0c-a4b0cb8975f8
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 client configuration for third-party integrations.
 * Used for OAuth2 authorization code and implicit flows.
 * Contains client credentials and configuration.
 */
message OAuthClient {
  // Unique client identifier
  string client_id = 1;

  // Client secret (for confidential clients)
  string client_secret = 2;

  // Client name
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Client description
  string description = 4 [ (buf.validate.field).string.max_len = 1000 ];

  // Client type ("public" or "confidential")
  string client_type = 5;

  // Allowed redirect URIs
  repeated string redirect_uris = 6;

  // Allowed grant types
  repeated string grant_types = 7;

  // Allowed response types
  repeated string response_types = 8;

  // Allowed scopes
  repeated string scopes = 9;

  // Client creation timestamp
  google.protobuf.Timestamp created_at = 10 [lazy = true, (buf.validate.field).required = true];

  // Client status
  gcommon.v1.common.ResourceStatus status = 11;

  // Client metadata
  map<string, string> metadata = 12 [lazy = true];

  // Client logo URL
  string logo_url = 13 [ (buf.validate.field).string.uri = true ];

  // Client website URL
  string website_url = 14 [ (buf.validate.field).string.uri = true ];

  // Client owner user ID
  string owner_user_id = 15;
}
```

---

### oauth2_flow_type.proto {#oauth2_flow_type}

**Path**: `gcommon/v1/common/oauth2_flow_type.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Enums** (1): `OAuth2FlowType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/oauth2_flow_type.proto
// version: 1.1.1
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 flow types.
 * Defines the different OAuth2 authentication flows supported.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum OAuth2FlowType {
  // Unspecified flow type
  OAUTH2_FLOW_TYPE_UNSPECIFIED = 0;

  // Authorization code flow
  OAUTH2_FLOW_TYPE_AUTHORIZATION_CODE = 1;

  // Implicit flow
  OAUTH2_FLOW_TYPE_IMPLICIT = 2;

  // Client credentials flow
  OAUTH2_FLOW_TYPE_CLIENT_CREDENTIALS = 3;

  // Device code flow
  OAUTH2_FLOW_TYPE_DEVICE_CODE = 4;
}
```

---

### offset_reset_strategy.proto {#offset_reset_strategy}

**Path**: `gcommon/v1/common/offset_reset_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `OffsetResetStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_reset_strategy.proto
// version: 1.0.1
// guid: edeef434-6f08-4fc1-be80-abdba95096d6

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum OffsetResetStrategy {
  OFFSET_RESET_STRATEGY_UNSPECIFIED = 0;
  OFFSET_RESET_STRATEGY_EARLIEST = 1; // Start from earliest available offset
  OFFSET_RESET_STRATEGY_LATEST = 2; // Start from latest offset
  OFFSET_RESET_STRATEGY_NONE = 3; // Fail if no committed offset
  OFFSET_RESET_STRATEGY_TIMESTAMP = 4; // Start from specific timestamp
}
```

---

### offset_type.proto {#offset_type}

**Path**: `gcommon/v1/common/offset_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `OffsetType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_type.proto
// version: 1.0.1
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Types of offsets that can be retrieved.
 * Defines different offset positions in a queue or partition.
 */
enum OffsetType {
  // Unspecified offset type
  OFFSET_TYPE_UNSPECIFIED = 0;

  // Earliest available offset
  OFFSET_TYPE_EARLIEST = 1;

  // Latest available offset
  OFFSET_TYPE_LATEST = 2;

  // Current consumer offset
  OFFSET_TYPE_CURRENT = 3;

  // Committed offset for consumer group
  OFFSET_TYPE_COMMITTED = 4;
}
```

---

### ordering_level.proto {#ordering_level}

**Path**: `gcommon/v1/common/ordering_level.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `OrderingLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ordering_level.proto
// version: 1.0.1
// guid: e1d35748-c24e-4dd1-91e8-edd9e4b62959

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum OrderingLevel {
  ORDERING_LEVEL_UNSPECIFIED = 0;
  ORDERING_LEVEL_NONE = 1; // No ordering guarantees
  ORDERING_LEVEL_PARTIAL = 2; // Partial ordering
  ORDERING_LEVEL_TOTAL = 3; // Total ordering
}
```

---

### organization_access_control.proto {#organization_access_control}

**Path**: `gcommon/v1/common/organization_access_control.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `OrganizationAccessControl`

**Imports** (3):

- `gcommon/v1/common/time_restriction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_access_control.proto
// version: 1.1.0
// guid: 0327cd1d-766b-46e4-b980-f039bbde89ef

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/time_restriction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationAccessControl {
  // IP address whitelist for tenant access
  repeated string ip_whitelist = 1 [(buf.validate.field).repeated.min_items = 1];

  // Allowed authentication methods
  repeated string auth_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Session timeout in minutes
  int32 session_timeout = 3 [(buf.validate.field).int32.gt = 0];

  // Maximum concurrent sessions
  int32 max_concurrent_sessions = 4 [(buf.validate.field).int32.gte = 0];

  // Geographic access restrictions
  repeated string allowed_countries = 5 [(buf.validate.field).repeated.min_items = 1];

  // Time-based access restrictions
  repeated TimeRestriction time_restrictions = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### organization_compliance_settings.proto {#organization_compliance_settings}

**Path**: `gcommon/v1/common/organization_compliance_settings.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `OrganizationComplianceSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_compliance_settings.proto
// version: 1.0.0
// guid: 01fb3d5c-a366-4271-a336-2312368dd4f2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationComplianceSettings {
  // GDPR compliance enabled
  bool gdpr_enabled = 1;

  // Data retention period in days
  int32 data_retention_days = 2 [(buf.validate.field).int32.gte = 0];

  // Whether data export is allowed
  bool data_export_enabled = 3;

  // Whether data deletion is allowed
  bool data_deletion_enabled = 4;

  // Compliance certifications
  repeated string certifications = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### organization_notification_settings.proto {#organization_notification_settings}

**Path**: `gcommon/v1/common/organization_notification_settings.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Messages** (1): `OrganizationNotificationSettings`

**Imports** (4):

- `gcommon/v1/common/email_template.proto`
- `gcommon/v1/common/notification_frequency.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_notification_settings.proto
// version: 1.1.0
// guid: 5c93685f-3692-4596-bb11-a848cfce9365

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/email_template.proto";
import "gcommon/v1/common/notification_frequency.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationNotificationSettings {
  // Default email sender address for organization notifications
  string sender_email = 1 [ (buf.validate.field).string.email = true ];

  // Default email sender name
  string sender_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether email notifications are enabled
  bool email_enabled = 3;

  // Whether SMS notifications are enabled
  bool sms_enabled = 4;

  // Whether in-app notifications are enabled
  bool in_app_enabled = 5;

  // Email template customizations
  repeated EmailTemplate email_templates = 6;

  // Notification frequency settings
  NotificationFrequency frequency = 7;
}
```

---

### organization_resource_limits.proto {#organization_resource_limits}

**Path**: `gcommon/v1/common/organization_resource_limits.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `OrganizationResourceLimits`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_resource_limits.proto
// version: 1.0.0
// guid: 53f1daa8-81b3-439e-a815-562120cd11a8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationResourceLimits {
  // Maximum CPU usage percentage
  int32 max_cpu_percent = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum memory usage in MB
  int64 max_memory_mb = 2 [(buf.validate.field).int64.gte = 0];

  // Maximum disk I/O operations per second
  int32 max_disk_iops = 3 [(buf.validate.field).int32.gte = 0];

  // Maximum network bandwidth in Mbps
  int32 max_network_mbps = 4 [(buf.validate.field).int32.gte = 0];

  // Maximum number of processes
  int32 max_processes = 5 [(buf.validate.field).int32.gte = 0];

  // Maximum number of file descriptors
  int32 max_file_descriptors = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### organization_status.proto {#organization_status}

**Path**: `gcommon/v1/common/organization_status.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `OrganizationStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization_status.proto
// version: 1.0.1
// guid: de37f968-280f-4858-9e68-72917e89b7c8
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Organization status enumeration defining the state of an organization.
 * Used to track organization lifecycle, operational status, and access permissions.
 */
enum OrganizationStatus {
  // Default value indicating no status was specified
  ORGANIZATION_STATUS_UNSPECIFIED = 0;

  // Organization is active and operational
  ORGANIZATION_STATUS_ACTIVE = 1;

  // Organization is inactive (temporarily suspended operations)
  ORGANIZATION_STATUS_INACTIVE = 2;

  // Organization is suspended due to policy violations or billing issues
  ORGANIZATION_STATUS_SUSPENDED = 3;

  // Organization is pending verification or onboarding completion
  ORGANIZATION_STATUS_PENDING = 4;

  // Organization is archived (read-only access, no new operations)
  ORGANIZATION_STATUS_ARCHIVED = 5;

  // Organization is marked for deletion and undergoing cleanup
  ORGANIZATION_STATUS_DELETED = 6;
}
```

---

### pagination.proto {#pagination}

**Path**: `gcommon/v1/common/pagination.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `Pagination`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/pagination.proto
// version: 1.0.0
// guid: 362a2da2-f93c-4652-9287-11938d1af4c3
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common pagination parameters for list operations.
 * Provides standardized pagination controls for queries and lists
 * across all GCommon modules to ensure consistent behavior.
 */
message Pagination {
  // Maximum number of items to return in a single page (0 means use server default)
  int32 page_size = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Opaque token for retrieving the next page (empty for first page)
  string page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Optional: specific page number (alternative to page_token for simple pagination)
  int32 page_number = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
}
```

---

### pagination_info.proto {#pagination_info}

**Path**: `gcommon/v1/common/pagination_info.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `CommonPaginationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/pagination_info.proto
// version: 1.0.0
// guid: 085f52cb-b1d9-4c82-ada7-9783f2807a33

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message CommonPaginationInfo {
  // Current page number (1-based)
  int32 current_page = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items per page
  int32 page_size = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total number of items available
  int64 total_items = 3 [(buf.validate.field).int64.gte = 0];

  // Total number of pages available
  int32 total_pages = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Whether there is a next page
  bool has_next = 5;

  // Whether there is a previous page
  bool has_previous = 6;

  // Token for retrieving the next page
  string next_page_token = 7 [(buf.validate.field).string.min_len = 1];

  // Token for retrieving the previous page
  string previous_page_token = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

