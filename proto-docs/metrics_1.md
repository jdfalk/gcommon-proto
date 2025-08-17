# metrics_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 39
- **Services**: 0
- **Enums**: 21
- ⚠️ **Issues**: 8

## Files in this Module

- [aggregation_type.proto](#aggregation_type)
- [alert_channel_type.proto](#alert_channel_type)
- [alert_notification.proto](#alert_notification)
- [alert_severity.proto](#alert_severity)
- [alert_state.proto](#alert_state)
- [alerting_condition.proto](#alerting_condition)
- [alerting_rule.proto](#alerting_rule)
- [backup_info.proto](#backup_info)
- [batch_options.proto](#batch_options)
- [batch_priority.proto](#batch_priority)
- [buffer_overflow_strategy.proto](#buffer_overflow_strategy)
- [change_type.proto](#change_type)
- [cleanup_strategy.proto](#cleanup_strategy)
- [comparison_operator.proto](#comparison_operator)
- [compression_type.proto](#compression_type)
- [counter_metric.proto](#counter_metric)
- [dashboard_type.proto](#dashboard_type)
- [deletion_options.proto](#deletion_options)
- [dry_run_result.proto](#dry_run_result)
- [error_stats.proto](#error_stats)
- [export_destination_update.proto](#export_destination_update)
- [export_format.proto](#export_format)
- [gauge_metric.proto](#gauge_metric)
- [gauge_operation.proto](#gauge_operation)
- [health_status.proto](#health_status)
- [histogram_bucket.proto](#histogram_bucket)
- [histogram_metric.proto](#histogram_metric)
- [metric_aggregation.proto](#metric_aggregation)
- [metric_aggregation_result.proto](#metric_aggregation_result) ⚠️ 3 issues
- [metric_bucket.proto](#metric_bucket)
- [metric_data.proto](#metric_data)
- [metric_family.proto](#metric_family) ⚠️ 5 issues
- [metric_filter.proto](#metric_filter)
- [metric_health.proto](#metric_health)
- [metric_label.proto](#metric_label)
- [metric_metadata.proto](#metric_metadata)
- [metric_quantile.proto](#metric_quantile)
- [metric_query.proto](#metric_query)
- [metric_sample.proto](#metric_sample)
- [metric_source.proto](#metric_source)
- [metric_stats.proto](#metric_stats)
- [metric_status.proto](#metric_status)
- [metric_type.proto](#metric_type)
- [metric_value.proto](#metric_value)
- [notification_type.proto](#notification_type)
- [numeric_format.proto](#numeric_format)
- [pagination_info.proto](#pagination_info)
- [performance_stats.proto](#performance_stats)
- [provider_info.proto](#provider_info)
- [provider_sort_field.proto](#provider_sort_field)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_1](./config_1.md)
- [config_2](./config_2.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)
- [queue_2](./queue_2.md)
- [web](./web.md)

**Modules that depend on this one**:

- [auth_api_2](./auth_api_2.md)
- [cache](./cache.md)
- [common](./common.md)
- [config_2](./config_2.md)
- [config_api](./config_api.md)
- [database_api](./database_api.md)
- [health](./health.md)
- [metrics_2](./metrics_2.md)
- [metrics_api_1](./metrics_api_1.md)
- [metrics_api_2](./metrics_api_2.md)
- [metrics_config](./metrics_config.md)
- [metrics_services](./metrics_services.md)
- [queue_1](./queue_1.md)
- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [queue_config](./queue_config.md)
- [queue_services](./queue_services.md)
- [web_api_2](./web_api_2.md)
- [web_config_1](./web_config_1.md)

---

## Detailed Documentation

### aggregation_type.proto {#aggregation_type}

**Path**: `pkg/metrics/proto/aggregation_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 58

**Enums** (1): `AggregationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/aggregation_type.proto
// file: metrics/proto/enums/aggregation_type.proto
//
// Aggregation type enum definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

**Path**: `pkg/metrics/proto/alert_channel_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 55

**Enums** (1): `AlertChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/alert_channel_type.proto
// version: 1.0.0
// guid: 6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### alert_notification.proto {#alert_notification}

**Path**: `pkg/metrics/proto/alert_notification.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `AlertNotification`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/alert_severity.proto` → [config_1](./config_1.md#alert_severity) → [queue_1](./queue_1.md#alert_severity)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/alert_notification.proto
// version: 1.0.0
// guid: 91304a90-5966-4b20-af06-2668e7d2a958

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/alert_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * AlertNotification represents a notification event generated when an
 * alerting rule is triggered.
 */
message AlertNotification {
  // Identifier of the alerting rule that triggered.
  string rule_id = 1;

  // Timestamp when the notification was generated.
  google.protobuf.Timestamp time = 2;

  // Severity level of the alert.
  AlertSeverity severity = 3;

  // Human readable message describing the alert.
  string message = 4;
}

```

---

### alert_severity.proto {#alert_severity}

**Path**: `pkg/metrics/proto/alert_severity.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Enums** (1): `AlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/alert_severity.proto
// version: 1.0.0
// guid: f1a2b3c4-5678-901c-5678-123456789012

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum AlertSeverity {
  ALERT_SEVERITY_UNSPECIFIED = 0;
  ALERT_SEVERITY_LOW = 1;
  ALERT_SEVERITY_MEDIUM = 2;
  ALERT_SEVERITY_HIGH = 3;
  ALERT_SEVERITY_CRITICAL = 4;
}

```

---

### alert_state.proto {#alert_state}

**Path**: `pkg/metrics/proto/alert_state.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Enums** (1): `AlertState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/alert_state.proto
// file: metrics/proto/enums/alert_state.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### alerting_condition.proto {#alerting_condition}

**Path**: `pkg/metrics/proto/alerting_condition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `AlertingCondition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/comparison_operator.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/alerting_condition.proto
// version: 1.0.0
// guid: c1e0ab41-b93c-4d9f-91a4-035998d0488d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/comparison_operator.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * AlertingCondition specifies a single metric threshold comparison
 * that triggers an alert when satisfied.
 */
message AlertingCondition {
  // Operator to use when comparing the metric value to the threshold.
  ComparisonOperator operator = 1;

  // Metric name or query expression being evaluated.
  string metric = 2;

  // Threshold value to compare against.
  double threshold = 3;

  // Duration in seconds the condition must hold true before firing.
  int32 duration_seconds = 4;
}

```

---

### alerting_rule.proto {#alerting_rule}

**Path**: `pkg/metrics/proto/alerting_rule.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `AlertingRule`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/alerting_rule.proto
// version: 1.0.0
// guid: c5d6e7f8-901c-356b-0123-678901234567

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message AlertingRule {
  // Rule ID
  string id = 1;

  // Rule name
  string name = 2;

  // Query expression
  string query = 3;

  // Alert condition
  string condition = 4;

  // Threshold value
  double threshold = 5;

  // Rule enabled status
  bool enabled = 6;
}

```

---

### backup_info.proto {#backup_info}

**Path**: `pkg/metrics/proto/backup_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `BackupInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/backup_info.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174026

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * BackupInfo contains information about backup operations.
 */
message BackupInfo {
  // Unique backup identifier
  string backup_id = 1;

  // Location where backup is stored
  string backup_location = 2;

  // Size of backup in bytes
  int64 backup_size_bytes = 3;

  // When backup was created
  google.protobuf.Timestamp backup_created_at = 4;

  // Backup retention period
  string backup_retention = 5;
}

```

---

### batch_options.proto {#batch_options}

**Path**: `pkg/metrics/proto/batch_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `BatchOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/batch_priority.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/batch_options.proto
// version: 1.0.0
// guid: cb61183a-3b53-41cd-a131-685b4fd8be75

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/batch_priority.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * BatchOptions configures how batch operations should be processed.
 */
message BatchOptions {
  // Whether to process metrics in parallel
  bool parallel_processing = 1;

  // Maximum concurrent operations (if parallel processing is enabled)
  int32 max_concurrency = 2;

  // Whether to deduplicate metrics within the batch
  bool deduplicate = 3;

  // Whether to return detailed results for each metric
  bool return_detailed_results = 4;

  // Timeout for the entire batch operation (seconds)
  int32 timeout_seconds = 5;

  // Whether to enable transactional semantics (all or nothing)
  bool transactional = 6;

  // Priority level for the batch operation
  BatchPriority priority = 7;
}

```

---

### batch_priority.proto {#batch_priority}

**Path**: `pkg/metrics/proto/batch_priority.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Enums** (1): `BatchPriority`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/batch_priority.proto
// version: 1.0.0
// guid: f9429991-ff0a-4c70-a6e5-7d639281f030

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * BatchPriority defines the processing priority for batch operations.
 */
enum BatchPriority {
  BATCH_PRIORITY_UNSPECIFIED = 0;
  BATCH_PRIORITY_LOW = 1;
  BATCH_PRIORITY_NORMAL = 2;
  BATCH_PRIORITY_HIGH = 3;
  BATCH_PRIORITY_URGENT = 4;
}

```

---

### buffer_overflow_strategy.proto {#buffer_overflow_strategy}

**Path**: `pkg/metrics/proto/buffer_overflow_strategy.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Enums** (1): `BufferOverflowStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/buffer_overflow_strategy.proto
// version: 1.0.0
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### change_type.proto {#change_type}

**Path**: `pkg/metrics/proto/change_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Enums** (1): `ChangeType`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/validation_result.proto` → [config_2](./config_2.md#validation_result) → [metrics_2](./metrics_2.md#validation_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/change_type.proto
// version: 1.0.0
// guid: 43b77608-77cc-40ad-97ae-4055d556fe1f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/validation_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ChangeType defines the type of configuration change.
 */
enum ChangeType {
  CHANGE_TYPE_UNSPECIFIED = 0;
  CHANGE_TYPE_ADDED = 1;
  CHANGE_TYPE_UPDATED = 2;
  CHANGE_TYPE_REMOVED = 3;
  CHANGE_TYPE_REPLACED = 4;
}

```

---

### cleanup_strategy.proto {#cleanup_strategy}

**Path**: `pkg/metrics/proto/cleanup_strategy.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Enums** (1): `CleanupStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/cleanup_strategy.proto
// version: 1.0.0
// guid: 98464e8e-3ad4-475d-8e19-cac3b3d813ca

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### comparison_operator.proto {#comparison_operator}

**Path**: `pkg/metrics/proto/comparison_operator.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Enums** (1): `ComparisonOperator`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/comparison_operator.proto
// version: 1.0.0
// guid: a2b3c4d5-6789-012d-6789-234567890123

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### compression_type.proto {#compression_type}

**Path**: `pkg/metrics/proto/compression_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Enums** (1): `CompressionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/compression_type.proto
// version: 1.0.0
// guid: 4bf1569f-264e-4bc9-9839-ff05b968d1ac

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * CompressionType defines supported compression algorithms for stored metrics.
 */
enum CompressionType {
  // Unspecified compression type.
  COMPRESSION_TYPE_UNSPECIFIED = 0;

  // No compression.
  COMPRESSION_TYPE_NONE = 1;

  // GZIP compression.
  COMPRESSION_TYPE_GZIP = 2;

  // Snappy compression.
  COMPRESSION_TYPE_SNAPPY = 3;

  // Zstandard compression.
  COMPRESSION_TYPE_ZSTD = 4;

  // LZ4 compression.
  COMPRESSION_TYPE_LZ4 = 5;
}

```

---

### counter_metric.proto {#counter_metric}

**Path**: `pkg/metrics/proto/counter_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `CounterMetric`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/counter_metric.proto
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * CounterMetric represents a monotonically increasing counter.
 * Counters only increase in value and are typically used for tracking
 * cumulative values like total requests, errors, or bytes processed.
 */
message CounterMetric {
  // Unique identifier for this counter
  string id = 1;

  // Counter name/label
  string name = 2;

  // Current counter value (must be monotonically increasing)
  double value = 3;

  // Timestamp when this value was recorded
  google.protobuf.Timestamp timestamp = 4;

  // Counter description/help text
  string description = 5;

  // Key-value labels for this counter
  map<string, string> labels = 6;

  // Sample count (for internal tracking)
  uint64 sample_count = 7;
}

```

---

### dashboard_type.proto {#dashboard_type}

**Path**: `pkg/metrics/proto/dashboard_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 55

**Enums** (1): `DashboardType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/dashboard_type.proto
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// DashboardType represents different types of dashboards
enum DashboardType {
  // Unspecified dashboard type
  DASHBOARD_TYPE_UNSPECIFIED = 0;

  // System overview dashboard
  DASHBOARD_TYPE_SYSTEM_OVERVIEW = 1;

  // Application performance dashboard
  DASHBOARD_TYPE_APPLICATION_PERFORMANCE = 2;

  // Infrastructure monitoring dashboard
  DASHBOARD_TYPE_INFRASTRUCTURE = 3;

  // Business metrics dashboard
  DASHBOARD_TYPE_BUSINESS_METRICS = 4;

  // Security monitoring dashboard
  DASHBOARD_TYPE_SECURITY = 5;

  // Custom dashboard
  DASHBOARD_TYPE_CUSTOM = 6;

  // Real-time monitoring dashboard
  DASHBOARD_TYPE_REAL_TIME = 7;

  // Historical analysis dashboard
  DASHBOARD_TYPE_HISTORICAL = 8;

  // Alert summary dashboard
  DASHBOARD_TYPE_ALERT_SUMMARY = 9;

  // Service health dashboard
  DASHBOARD_TYPE_SERVICE_HEALTH = 10;

  // Capacity planning dashboard
  DASHBOARD_TYPE_CAPACITY_PLANNING = 11;

  // SLA/SLO tracking dashboard
  DASHBOARD_TYPE_SLA_SLO = 12;
}

```

---

### deletion_options.proto {#deletion_options}

**Path**: `pkg/metrics/proto/deletion_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 52

**Messages** (1): `DeletionOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/cleanup_strategy.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/deletion_options.proto
// version: 1.0.0
// guid: 6e247c69-d9f2-452e-bb15-e81da5c53d42

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/cleanup_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * DeletionOptions configure the deletion process.
 */
message DeletionOptions {
  // Whether to delete all associated data
  bool delete_data = 1;

  // Whether to delete associated indices
  bool delete_indices = 2;

  // Whether to delete configuration backups
  bool delete_backups = 3;

  // Whether to stop all exports before deletion
  bool stop_exports = 4;

  // Grace period before actual deletion
  string grace_period = 5;

  // Whether to perform a dry run
  bool dry_run = 6;

  // Whether to force deletion even if provider is in use
  bool force = 7;

  // Whether to create a final backup before deletion
  bool create_backup = 8;

  // Cleanup strategy to use
  CleanupStrategy cleanup_strategy = 9;

  // Whether to wait for ongoing operations to complete
  bool wait_for_completion = 10;

  // Maximum time to wait for operations to complete
  string completion_timeout = 11;
}

```

---

### dry_run_result.proto {#dry_run_result}

**Path**: `pkg/metrics/proto/dry_run_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `DryRunResult`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/dry_run_result.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174027

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * DryRunResult contains information about what would happen in a dry run.
 */
message DryRunResult {
  // Number of bytes that would be deleted
  int64 would_delete_bytes = 1;

  // Number of data points that would be deleted
  int64 would_delete_points = 2;

  // Number of indices that would be deleted
  int64 would_delete_indices = 3;

  // Number of exports that would be stopped
  int64 would_stop_exports = 4;

  // Estimated time for deletion to complete
  string estimated_deletion_time = 5;
}

```

---

### error_stats.proto {#error_stats}

**Path**: `pkg/metrics/proto/error_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (2): `ErrorStats`, `ErrorTypeCount`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/error_stats.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174029

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ErrorStats contains error-related statistics.
 */
message ErrorStats {
  // Total number of errors
  int64 total_errors = 1;

  // Error rate (errors per total operations)
  double error_rate = 2;

  // Most common error types
  repeated ErrorTypeCount error_types = 3;

  // Recent error trend (increasing/decreasing/stable)
  string error_trend = 4;
}

/**
 * ErrorTypeCount represents the count for a specific error type.
 */
message ErrorTypeCount {
  string error_type = 1;
  int64 count = 2;
  double percentage = 3;
}

```

---

### export_destination_update.proto {#export_destination_update}

**Path**: `pkg/metrics/proto/export_destination_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `ExportDestinationUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/export_destination_update.proto
// version: 1.0.0
// guid: a3b4c5d6-789a-134f-8901-456789012345

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ExportDestinationUpdate {
  // Destination ID
  string destination_id = 1;

  // Destination URL
  string url = 2;

  // Authentication token
  string auth_token = 3;

  // Enabled status
  bool enabled = 4;
}

```

---

### export_format.proto {#export_format}

**Path**: `pkg/metrics/proto/export_format.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Enums** (1): `ExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/export_format.proto
// version: 1.0.0
// guid: b4c5d6e7-890b-245a-9012-567890123456

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum ExportFormat {
  EXPORT_FORMAT_UNSPECIFIED = 0;
  EXPORT_FORMAT_PROMETHEUS = 1;
  EXPORT_FORMAT_JSON = 2;
  EXPORT_FORMAT_CSV = 3;
  EXPORT_FORMAT_OPENTELEMETRY = 4;
}

```

---

### gauge_metric.proto {#gauge_metric}

**Path**: `pkg/metrics/proto/gauge_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 45

**Messages** (1): `GaugeMetric`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/gauge_metric.proto
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GaugeMetric represents a value that can go up and down.
 * Gauges are used for tracking instantaneous values like memory usage,
 * temperature, active connections, or CPU utilization.
 */
message GaugeMetric {
  // Unique identifier for this gauge
  string id = 1;

  // Gauge name/label
  string name = 2;

  // Current gauge value (can increase or decrease)
  double value = 3;

  // Timestamp when this value was recorded
  google.protobuf.Timestamp timestamp = 4;

  // Gauge description/help text
  string description = 5;

  // Key-value labels for this gauge
  map<string, string> labels = 6;

  // Minimum allowed value (constraint)
  double min_value = 7;

  // Maximum allowed value (constraint)
  double max_value = 8;

  // Unit of measurement (e.g., "bytes", "percent", "connections")
  string unit = 9;
}

```

---

### gauge_operation.proto {#gauge_operation}

**Path**: `pkg/metrics/proto/gauge_operation.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Enums** (1): `GaugeOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/gauge_operation.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GaugeOperation defines how to update the gauge value.
 * Specifies the operation to perform on a gauge metric.
 */
enum GaugeOperation {
  // Unspecified operation (defaults to SET)
  GAUGE_OPERATION_UNSPECIFIED = 0;

  // Set the gauge to the specified value
  GAUGE_OPERATION_SET = 1;

  // Add the value to the current gauge value
  GAUGE_OPERATION_ADD = 2;

  // Subtract the value from the current gauge value
  GAUGE_OPERATION_SUBTRACT = 3;

  // Increment the gauge by 1
  GAUGE_OPERATION_INCREMENT = 4;

  // Decrement the gauge by 1
  GAUGE_OPERATION_DECREMENT = 5;
}

```

---

### health_status.proto {#health_status}

**Path**: `pkg/metrics/proto/health_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Enums** (1): `HealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/health_status.proto
// version: 1.0.0
// guid: c1d2e3f4-567c-912b-6789-234567890123

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

enum HealthStatus {
  HEALTH_STATUS_UNSPECIFIED = 0;
  HEALTH_STATUS_HEALTHY = 1;
  HEALTH_STATUS_DEGRADED = 2;
  HEALTH_STATUS_UNHEALTHY = 3;
  HEALTH_STATUS_UNKNOWN = 4;
}

```

---

### histogram_bucket.proto {#histogram_bucket}

**Path**: `pkg/metrics/proto/histogram_bucket.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `HistogramBucket`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/histogram_bucket.proto
// version: 1.0.0
// guid: a9b0c1d2-345a-790f-4567-012345678901

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message HistogramBucket {
  // Upper bound for the bucket
  double upper_bound = 1;

  // Count of observations in this bucket
  int64 count = 2;

  // Cumulative count
  int64 cumulative_count = 3;
}

```

---

### histogram_metric.proto {#histogram_metric}

**Path**: `pkg/metrics/proto/histogram_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `HistogramMetric`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/histogram_bucket.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/histogram_metric.proto
// version: 1.0.0
// guid: 1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/histogram_bucket.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// HistogramMetric represents a histogram metric with buckets
message HistogramMetric {
  // Metric name
  string name = 1;

  // Metric labels
  map<string, string> labels = 2;

  // Histogram buckets
  repeated HistogramBucket buckets = 3;

  // Sample count
  uint64 sample_count = 4;

  // Sample sum
  double sample_sum = 5;

  // Timestamp when the metric was recorded
  google.protobuf.Timestamp timestamp = 6;

  // Help text for the metric
  string help = 7;
}

```

---

### metric_aggregation.proto {#metric_aggregation}

**Path**: `pkg/metrics/proto/metric_aggregation.proto` **Package**: `gcommon.v1.metrics` **Lines**: 48

**Enums** (1): `MetricAggregation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/metric_aggregation.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174011

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * Aggregation methods for metric values.
 */
enum MetricAggregation {
  // Default aggregation method
  METRIC_AGGREGATION_UNSPECIFIED = 0;

  // Sum of all values
  METRIC_AGGREGATION_SUM = 1;

  // Average of all values
  METRIC_AGGREGATION_AVERAGE = 2;

  // Minimum value
  METRIC_AGGREGATION_MIN = 3;

  // Maximum value
  METRIC_AGGREGATION_MAX = 4;

  // Count of values
  METRIC_AGGREGATION_COUNT = 5;

  // Median value
  METRIC_AGGREGATION_MEDIAN = 6;

  // 95th percentile
  METRIC_AGGREGATION_P95 = 7;

  // 99th percentile
  METRIC_AGGREGATION_P99 = 8;

  // Standard deviation
  METRIC_AGGREGATION_STDDEV = 9;
}

```

---

### metric_aggregation_result.proto {#metric_aggregation_result}

**Path**: `pkg/metrics/proto/metric_aggregation_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricAggregation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (3)

- Line 20: Commented field - // CONFLICT_DISABLED: AggregationType type = 1;
- Line 23: Commented field - // CONFLICT_DISABLED: double value = 2;
- Line 26: Commented field - // CONFLICT_DISABLED: int64 sample_count = 3;

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_aggregation_result.proto
// file: metrics/proto/messages/metric_aggregation_result.proto
//
// Definition of aggregation results for metrics queries.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricAggregation represents aggregated metric value.
 */
// CONFLICT_DISABLED: message MetricAggregation {
// CONFLICT_DISABLED:   // Aggregation type performed
// CONFLICT_DISABLED:   AggregationType type = 1;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Value produced by aggregation
// CONFLICT_DISABLED:   double value = 2;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Number of samples aggregated
// CONFLICT_DISABLED:   int64 sample_count = 3;
// CONFLICT_DISABLED: }

```

---

### metric_bucket.proto {#metric_bucket}

**Path**: `pkg/metrics/proto/metric_bucket.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `MetricBucket`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_bucket.proto
// version: 1.0.0
// guid: 97e038af-19d9-4d0a-8f3c-0030fd6f2b89

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricBucket represents a histogram bucket with bounds and count.
 */
message MetricBucket {
  // Lower bound inclusive.
  double lower_bound = 1;

  // Upper bound exclusive.
  double upper_bound = 2;

  // Number of samples in the bucket.
  int64 count = 3;
}

```

---

### metric_data.proto {#metric_data}

**Path**: `pkg/metrics/proto/metric_data.proto` **Package**: `gcommon.v1.metrics` **Lines**: 95

**Messages** (3): `MetricData`, `MetricSeries`, `MetricFamily`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/metric_type.proto` → [queue_1](./queue_1.md#metric_type)
- `pkg/metrics/proto/metric_value.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_data.proto
// file: metrics/proto/messages/metric_data.proto
//
// Message definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/metric_type.proto";
import "pkg/metrics/proto/metric_value.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricData represents a complete metric with metadata and values.
 * This is the primary data structure for transmitting metric information.
 */
message MetricData {
  // Unique identifier for this metric
  string metric_id = 1;

  // Metric name (e.g., "http_requests_total", "cpu_usage_percent")
  string name = 2;

  // Type of metric (counter, gauge, histogram, etc.)
  MetricType type = 3;

  // Human-readable description of the metric
  string description = 4;

  // Unit of measurement (e.g., "bytes", "seconds", "requests")
  string unit = 5;

  // Base labels/tags that apply to all values in this metric
  map<string, string> labels = 6;

  // The metric values (can be multiple for time series)
  repeated MetricValue values = 7;

  // When this metric data was collected/created
  google.protobuf.Timestamp created_at = 8;

  // Source system or component that generated this metric
  string source = 9;

  // Namespace or service this metric belongs to
  string namespace = 10;

  // Version of the metric schema/definition
  string schema_version = 11;
}

/**
 * MetricSeries represents a time series of metric values.
 * Used for queries that return multiple data points over time.
 */
message MetricSeries {
  // Metric metadata
  string name = 1;
  MetricType type = 2;
  map<string, string> labels = 3;

  // Time-ordered series of values
  repeated MetricValue values = 4;

  // Resolution/step between data points
  int64 step_seconds = 5;
}

/**
 * MetricFamily groups related metrics together.
 * Similar to Prometheus metric families.
 */
message MetricFamily {
  // Family name (e.g., "http_requests")
  string name = 1;

  // Family description
  string description = 2;

  // Type of metrics in this family
  MetricType type = 3;

  // Unit of measurement for all metrics in this family
  string unit = 4;

  // All metrics in this family
  repeated MetricData metrics = 5;
}

```

---

### metric_family.proto {#metric_family}

**Path**: `pkg/metrics/proto/metric_family.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `MetricFamily`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/metric_data.proto`

#### ⚠️ Issues Found (5)

- Line 21: Commented field - // CONFLICT_DISABLED: string name = 1;
- Line 24: Commented field - // CONFLICT_DISABLED: string description = 2;
- Line 27: Commented field - // CONFLICT_DISABLED: MetricType type = 3;
- Line 30: Commented field - // CONFLICT_DISABLED: string unit = 4;
- Line 33: Commented field - // CONFLICT_DISABLED: repeated MetricData metrics = 5;

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_family.proto
// file: metrics/proto/messages/metric_family.proto
//
// MetricFamily groups related metrics together.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricFamily groups metrics of the same name and type.
 */
// CONFLICT_DISABLED: message MetricFamily {
// CONFLICT_DISABLED:   // Family name (e.g., http_requests)
// CONFLICT_DISABLED:   string name = 1;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Family description
// CONFLICT_DISABLED:   string description = 2;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Metric type for this family
// CONFLICT_DISABLED:   MetricType type = 3;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Unit of measurement
// CONFLICT_DISABLED:   string unit = 4;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Metrics in this family
// CONFLICT_DISABLED:   repeated MetricData metrics = 5;
// CONFLICT_DISABLED: }

```

---

### metric_filter.proto {#metric_filter}

**Path**: `pkg/metrics/proto/metric_filter.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `MetricFilter`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/metric_filter.proto
// version: 1.0.0
// Filter for metrics queries

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// Filter for metrics queries
message MetricFilter {
  // Metric name patterns to include
  repeated string metric_names = 1;

  // Label filters
  map<string, string> labels = 2;

  // Namespace filter
  string namespace = 3;

  // Time range filter
  int64 start_timestamp = 4;
  int64 end_timestamp = 5;

  // Value threshold filters
  double min_value = 6;
  double max_value = 7;

  // Include/exclude patterns
  repeated string include_patterns = 8;
  repeated string exclude_patterns = 9;
}

```

---

### metric_health.proto {#metric_health}

**Path**: `pkg/metrics/proto/metric_health.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `MetricHealth`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/health_status.proto` → [common](./common.md#health_status) → [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_health.proto
// version: 1.0.0
// guid: c0c75431-e37e-4748-8a0d-44a7b15c5e3b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricHealth captures the health status of a metric source or scrape job.
 */
message MetricHealth {
  // Metric identifier or scrape job id
  string target_id = 1;

  // Health status
  HealthStatus status = 2;

  // When this health status was checked
  google.protobuf.Timestamp checked_at = 3;

  // Additional message or context
  string message = 4;
}

```

---

### metric_label.proto {#metric_label}

**Path**: `pkg/metrics/proto/metric_label.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `MetricLabel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_label.proto
// version: 1.0.0
// guid: 8a39fa3e-a2eb-4df9-9dcf-0c9482a16722

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricLabel represents a single key/value label used for
 * metric identification and filtering.
 */
message MetricLabel {
  // Label key
  string key = 1;

  // Label value
  string value = 2;
}

```

---

### metric_metadata.proto {#metric_metadata}

**Path**: `pkg/metrics/proto/metric_metadata.proto` **Package**: `gcommon.v1.metrics` **Lines**: 57

**Messages** (1): `MetricMetadata`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_metadata.proto
// file: metrics/proto/messages/metric_metadata.proto
//
// Message definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricMetadata contains metadata information about a metric.
 */
message MetricMetadata {
  // Unique identifier for the metric
  string metric_id = 1;

  // Human-readable name of the metric
  string name = 2;

  // Description of what this metric measures
  string description = 3;

  // Metric type (counter, gauge, histogram, etc.)
  string type = 4;

  // Units of measurement (e.g., "bytes", "seconds", "requests")
  string unit = 5;

  // Labels associated with this metric
  map<string, string> labels = 6;

  // When this metric was first created
  google.protobuf.Timestamp created_at = 7;

  // When this metric was last updated
  google.protobuf.Timestamp updated_at = 8;

  // Whether this metric is currently active
  bool active = 9;

  // Data retention policy for this metric
  string retention_policy = 10;

  // Provider that owns this metric
  string provider_id = 11;

  // Namespace this metric belongs to
  string namespace = 12;
}

```

---

### metric_quantile.proto {#metric_quantile}

**Path**: `pkg/metrics/proto/metric_quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `MetricQuantile`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_quantile.proto
// version: 1.0.0
// guid: 9ab5b0e2-0228-47d2-9a48-d714ee6f3d6f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricQuantile represents a quantile value calculated from a
 * distribution of metric samples.
 */
message MetricQuantile {
  // Quantile (0-1, e.g., 0.95 for 95th percentile).
  double quantile = 1;

  // Value observed at this quantile.
  double value = 2;
}

```

---

### metric_query.proto {#metric_query}

**Path**: `pkg/metrics/proto/metric_query.proto` **Package**: `gcommon.v1.metrics` **Lines**: 133

**Messages** (5): `MetricQuery`, `AggregationSpec`, `GroupBySpec`, `QueryPlan`, `QueryStep`

**Imports** (8):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/sort.proto` → [common](./common.md#sort)
- `pkg/metrics/proto/aggregation_type.proto`
- `pkg/metrics/proto/metric_filter.proto`
- `pkg/metrics/proto/query_operation.proto` → [metrics_2](./metrics_2.md#query_operation)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) → [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/timestamp_range.proto` → [metrics_2](./metrics_2.md#timestamp_range) → [queue_2](./queue_2.md#timestamp_range)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_query.proto
// file: metrics/proto/messages/metric_query.proto
//
// Message definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/sort.proto";
import "pkg/metrics/proto/aggregation_type.proto";
import "pkg/metrics/proto/metric_filter.proto";
import "pkg/metrics/proto/query_operation.proto";
import "pkg/metrics/proto/time_range.proto";
import "pkg/metrics/proto/timestamp_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricQuery represents a query for retrieving and processing metric data.
 * Supports filtering, aggregation, and transformation operations.
 */
message MetricQuery {
  // Unique identifier for this query
  string query_id = 1;

  // Human-readable query name or description
  string name = 2;

  // Query string (PromQL, SQL, or custom query language)
  string query_string = 3;

  // Filter criteria for selecting metrics
  MetricFilter filter = 4;

  // Time range for the query
  TimeRange time_filter = 5;

  // Aggregation operations to apply
  repeated AggregationSpec aggregations = 6;

  // Group by specifications
  repeated GroupBySpec group_by = 7;

  // Sort criteria
  repeated gcommon.v1.common.SortOptions sort_criteria = 8;

  // Maximum number of results to return
  int32 limit = 9;

  // Offset for pagination
  int32 offset = 10;
}

/**
 * AggregationSpec defines how to aggregate metric data.
 */
message AggregationSpec {
  // Type of aggregation to perform
  AggregationType aggregation_type = 1;

  // Field to aggregate on (if applicable)
  string field = 2;

  // Time window for aggregation
  google.protobuf.Duration window = 3;

  // Step/resolution for time-based aggregation
  google.protobuf.Duration step = 4;

  // Additional parameters for complex aggregations
  map<string, string> parameters = 5;
}

/**
 * GroupBySpec defines how to group metric results.
 */
message GroupBySpec {
  // Label keys to group by
  repeated string label_keys = 1;

  // Time-based grouping (e.g., by hour, day)
  google.protobuf.Duration time_group = 2;

  // Maximum number of groups to return
  int32 max_groups = 3;
}

/**
 * QueryPlan represents an execution plan for a metric query.
 * Used for query optimization and debugging.
 */
message QueryPlan {
  // Query that this plan is for
  string query_id = 1;

  // Estimated execution time
  google.protobuf.Duration estimated_duration = 2;

  // Estimated number of data points to process
  int64 estimated_data_points = 3;

  // Execution steps
  repeated QueryStep steps = 4;

  // Storage backends that will be queried
  repeated string storage_backends = 5;
}

/**
 * QueryStep represents a single step in query execution.
 */
message QueryStep {
  // Step identifier
  string step_id = 1;

  // Operation to perform in this step
  QueryOperation operation = 2;

  // Description of the operation
  string description = 3;

  // Estimated cost/time for this step
  google.protobuf.Duration estimated_duration = 4;

  // Input from previous steps
  repeated string input_step_ids = 5;
}

```

---

### metric_sample.proto {#metric_sample}

**Path**: `pkg/metrics/proto/metric_sample.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricSample`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_sample.proto
// version: 1.0.0
// guid: 7f2e5cc8-7e1b-49d8-b994-556a6d3aa642

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricSample represents a single value for a metric at a point in time.
 */
message MetricSample {
  // Recorded value
  double value = 1;

  // Timestamp of the sample
  google.protobuf.Timestamp timestamp = 2;

  // Optional labels associated with this sample
  map<string, string> labels = 3;
}

```

---

### metric_source.proto {#metric_source}

**Path**: `pkg/metrics/proto/metric_source.proto` **Package**: `gcommon.v1.metrics` **Lines**: 61

**Enums** (1): `MetricSource`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/metric_source.proto
// version: 1.0.0
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### metric_stats.proto {#metric_stats}

**Path**: `pkg/metrics/proto/metric_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `MetricStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_stats.proto
// version: 1.0.0
// guid: 73f03142-2df5-4e09-a4cd-b067ec1a9fbb

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricStats provides summary statistics for a set of metric values.
 */
message MetricStats {
  // Minimum value observed.
  double min = 1;

  // Maximum value observed.
  double max = 2;

  // Average of all values.
  double average = 3;

  // Sum of all values.
  double sum = 4;

  // Number of samples.
  int64 count = 5;
}

```

---

### metric_status.proto {#metric_status}

**Path**: `pkg/metrics/proto/metric_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Enums** (1): `MetricStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/metric_status.proto
// version: 1.0.0
// guid: 0f4752cc-8120-45bb-a7c9-1fb475c11998

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

**Path**: `pkg/metrics/proto/metric_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Enums** (1): `MetricType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/metric_type.proto
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricType defines the different types of metrics that can be collected.
 * Each type has specific semantics for how values are interpreted and aggregated.
 */
enum MetricType {
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

### metric_value.proto {#metric_value}

**Path**: `pkg/metrics/proto/metric_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 92

**Messages** (4): `MetricValue`, `HistogramValue`, `SummaryValue`, `Quantile`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/histogram_bucket.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/metric_value.proto
// file: metrics/proto/types/metric_value.proto
//
// Type definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/histogram_bucket.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricValue represents a single metric data point with timestamp and value.
 * This is the fundamental unit of metric data in the system.
 */
message MetricValue {
  // Timestamp when this metric value was recorded
  google.protobuf.Timestamp timestamp = 1;

  // The metric value - using oneof to support different value types
  oneof value {
    // Double precision floating point value
    double double_value = 2;

    // Integer value (64-bit signed)
    int64 int_value = 3;

    // String value (for label/text metrics)
    string string_value = 4;

    // Boolean value
    bool bool_value = 5;

    // Histogram bucket values (for histogram metrics)
    HistogramValue histogram_value = 6;

    // Summary quantile values (for summary metrics)
    SummaryValue summary_value = 7;
  }

  // Optional labels/tags associated with this specific value
  map<string, string> labels = 8;

  // Optional sample count (for aggregated values)
  uint64 sample_count = 9;
}

/**
 * HistogramValue represents histogram bucket data.
 */
message HistogramValue {
  // Histogram buckets with their counts
  repeated HistogramBucket buckets = 1;

  // Total count of all samples
  uint64 count = 2;

  // Sum of all sample values
  double sum = 3;
}

/**
 * SummaryValue represents summary quantile data.
 */
message SummaryValue {
  // Quantile values
  repeated Quantile quantiles = 1;

  // Total count of all samples
  uint64 count = 2;

  // Sum of all sample values
  double sum = 3;
}

/**
 * Quantile represents a single quantile value.
 */
message Quantile {
  // Quantile value (0.0 to 1.0, e.g., 0.95 for 95th percentile)
  double quantile = 1;

  // Value at this quantile
  double value = 2;
}

```

---

### notification_type.proto {#notification_type}

**Path**: `pkg/metrics/proto/notification_type.proto` **Package**: `gcommon.v1.metrics` **Lines**: 63

**Enums** (1): `NotificationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/notification_type.proto
// file: metrics/proto/enums/notification_type.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

**Path**: `pkg/metrics/proto/numeric_format.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Enums** (1): `NumericFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/numeric_format.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### pagination_info.proto {#pagination_info}

**Path**: `pkg/metrics/proto/pagination_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `PaginationInfo`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/pagination_info.proto
// version: 1.0.0
// guid: f1e2d3c4-b5a6-9c8d-7e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * PaginationInfo contains information about paginated results.
 */
message PaginationInfo {
  // Current page number (1-based)
  uint32 page = 1;

  // Number of items per page
  uint32 page_size = 2;

  // Total number of items across all pages
  uint64 total_items = 3;

  // Total number of pages
  uint32 total_pages = 4;

  // Whether there is a next page
  bool has_next = 5;

  // Whether there is a previous page
  bool has_previous = 6;

  // Cursor for cursor-based pagination (optional)
  string next_cursor = 7;

  // Cursor for previous page (optional)
  string previous_cursor = 8;
}

```

---

### performance_stats.proto {#performance_stats}

**Path**: `pkg/metrics/proto/performance_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 60

**Messages** (1): `PerformanceStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/performance_stats.proto
// version: 1.0.0
// guid: b3c4d5e6-f7a8-9b0c-1d2e-3f4a5b6c7d8e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * PerformanceStats contains performance metrics for provider operations.
 */
message PerformanceStats {
  // Average response time in milliseconds
  double avg_response_time_ms = 1;

  // Maximum response time in milliseconds
  double max_response_time_ms = 2;

  // Minimum response time in milliseconds
  double min_response_time_ms = 3;

  // 95th percentile response time in milliseconds
  double p95_response_time_ms = 4;

  // 99th percentile response time in milliseconds
  double p99_response_time_ms = 5;

  // Requests per second
  double requests_per_second = 6;

  // Total number of requests processed
  uint64 total_requests = 7;

  // Number of successful requests
  uint64 successful_requests = 8;

  // Number of failed requests
  uint64 failed_requests = 9;

  // Success rate (0.0 to 1.0)
  double success_rate = 10;

  // CPU utilization percentage (0.0 to 100.0)
  double cpu_utilization = 11;

  // Memory utilization percentage (0.0 to 100.0)
  double memory_utilization = 12;

  // Network I/O in bytes per second
  double network_io_bytes_per_sec = 13;

  // Disk I/O in bytes per second
  double disk_io_bytes_per_sec = 14;
}

```

---

### provider_info.proto {#provider_info}

**Path**: `pkg/metrics/proto/provider_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 56

**Messages** (1): `ProviderInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/provider_status.proto` → [metrics_2](./metrics_2.md#provider_status)

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/provider_info.proto
// version: 1.0.0
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/provider_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ProviderInfo contains information about a metrics provider.
 */
message ProviderInfo {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name of the provider
  string name = 2;

  // Provider type (e.g., "prometheus", "datadog", "custom")
  string type = 3;

  // Current status of the provider
  string status = 4;

  // Detailed status information
  ProviderStatus detailed_status = 5;

  // Configuration settings
  map<string, string> config = 6;

  // Version of the provider
  string version = 7;

  // When this provider was created
  google.protobuf.Timestamp created_at = 8;

  // When this provider was last updated
  google.protobuf.Timestamp last_updated = 9;

  // Whether this provider is enabled
  bool enabled = 10;

  // Tags associated with this provider
  repeated string tags = 11;

  // Description of the provider
  string description = 12;
}

```

---

### provider_sort_field.proto {#provider_sort_field}

**Path**: `pkg/metrics/proto/provider_sort_field.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Enums** (1): `SortField`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/provider_sort_field.proto
// version: 1.0.0
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * SortField defines fields that can be used for sorting providers.
 * Specifies available fields for provider list sorting.
 */
enum SortField {
  // Unspecified sort field
  SORT_FIELD_UNSPECIFIED = 0;

  // Sort by provider name
  SORT_FIELD_NAME = 1;

  // Sort by provider type
  SORT_FIELD_TYPE = 2;

  // Sort by creation timestamp
  SORT_FIELD_CREATED_AT = 3;

  // Sort by provider state
  SORT_FIELD_STATE = 4;

  // Sort by health status
  SORT_FIELD_HEALTH = 5;
}

```

---
