# metrics_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [aggregation_spec.proto](#aggregation_spec)
- [alert_notification.proto](#alert_notification)
- [alerting_condition.proto](#alerting_condition)
- [alerting_rule.proto](#alerting_rule)
- [bucket_info.proto](#bucket_info)
- [counter_metric.proto](#counter_metric)
- [cpu_usage.proto](#cpu_usage)
- [data_volume_data_point.proto](#data_volume_data_point)
- [data_volume_stats.proto](#data_volume_stats)
- [data_volume_trend.proto](#data_volume_trend)
- [deletion_options.proto](#deletion_options)
- [deletion_result.proto](#deletion_result)
- [disk_usage.proto](#disk_usage)
- [dry_run_result.proto](#dry_run_result)
- [error_data_point.proto](#error_data_point)
- [error_entry.proto](#error_entry)
- [error_trend.proto](#error_trend)
- [error_type_count.proto](#error_type_count)
- [error_type_stats.proto](#error_type_stats)
- [export_destination.proto](#export_destination)
- [export_destination_stats.proto](#export_destination_stats)
- [export_destination_update.proto](#export_destination_update)
- [export_stats.proto](#export_stats)
- [export_status.proto](#export_status)
- [exporter_status.proto](#exporter_status)
- [gauge_metric.proto](#gauge_metric)
- [group_by_spec.proto](#group_by_spec)
- [health_status_entry.proto](#health_status_entry)
- [histogram_bucket.proto](#histogram_bucket)
- [histogram_metric.proto](#histogram_metric)
- [histogram_stats.proto](#histogram_stats)
- [histogram_value.proto](#histogram_value)
- [label_definition.proto](#label_definition)
- [memory_usage.proto](#memory_usage)
- [metric_aggregation.proto](#metric_aggregation)
- [metric_bucket.proto](#metric_bucket)
- [metric_data.proto](#metric_data)
- [metric_definition.proto](#metric_definition)
- [metric_filter.proto](#metric_filter)
- [metric_health.proto](#metric_health)
- [metric_info.proto](#metric_info)
- [metric_label.proto](#metric_label)
- [metric_metadata.proto](#metric_metadata)
- [metric_quantile.proto](#metric_quantile)
- [metric_query.proto](#metric_query)
- [metric_result.proto](#metric_result)
- [metric_sample.proto](#metric_sample)
- [metric_series.proto](#metric_series)
- [metric_stats.proto](#metric_stats)
- [metric_summary.proto](#metric_summary)
---


## Detailed Documentation

### aggregation_spec.proto {#aggregation_spec}

**Path**: `gcommon/v1/metrics/aggregation_spec.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `AggregationSpec`

**Imports** (4):

- `gcommon/v1/common/aggregation_type.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/aggregation_spec.proto
// version: 1.0.0
// guid: 169a9fb5-9a9e-4ba6-beaa-63915a9a9839

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/aggregation_type.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message AggregationSpec {
  // Type of aggregation to perform
  gcommon.v1.common.AggregationType aggregation_type = 1;

  // Field to aggregate on (if applicable)
  string field = 2 [(buf.validate.field).string.min_len = 1];

  // Time window for aggregation
  google.protobuf.Duration window = 3;

  // Step/resolution for time-based aggregation
  google.protobuf.Duration step = 4;

  // Additional parameters for complex aggregations
  map<string, string> parameters = 5;
}
```

---

### alert_notification.proto {#alert_notification}

**Path**: `gcommon/v1/metrics/alert_notification.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `AlertNotification`

**Imports** (4):

- `gcommon/v1/common/metrics_alert_severity.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alert_notification.proto
// version: 1.0.0
// guid: 91304a90-5966-4b20-af06-2668e7d2a958

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_alert_severity.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * AlertNotification represents a notification event generated when an
 * alerting rule is triggered.
 */
message AlertNotification {
  // Identifier of the alerting rule that triggered.
  string rule_id = 1 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the notification was generated.
  google.protobuf.Timestamp time = 2;

  // Severity level of the alert.
  gcommon.v1.common.MetricsAlertSeverity severity = 3;

  // Human readable message describing the alert.
  string message = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### alerting_condition.proto {#alerting_condition}

**Path**: `gcommon/v1/metrics/alerting_condition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `AlertingCondition`

**Imports** (3):

- `gcommon/v1/common/comparison_operator.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alerting_condition.proto
// version: 1.0.0
// guid: c1e0ab41-b93c-4d9f-91a4-035998d0488d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/comparison_operator.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * AlertingCondition specifies a single metric threshold comparison
 * that triggers an alert when satisfied.
 */
message AlertingCondition {
  // Operator to use when comparing the metric value to the threshold.
  gcommon.v1.common.ComparisonOperator operator = 1;

  // Metric name or query expression being evaluated.
  string metric = 2 [(buf.validate.field).string.min_len = 1];

  // Threshold value to compare against.
  double threshold = 3 [(buf.validate.field).double.gte = 0.0];

  // Duration in seconds the condition must hold true before firing.
  int32 duration_seconds = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### alerting_rule.proto {#alerting_rule}

**Path**: `gcommon/v1/metrics/alerting_rule.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `AlertingRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alerting_rule.proto
// version: 1.0.0
// guid: c5d6e7f8-901c-356b-0123-678901234567

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message AlertingRule {
  // Rule ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Rule name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### bucket_info.proto {#bucket_info}

**Path**: `gcommon/v1/metrics/bucket_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `BucketInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/bucket_info.proto
// version: 1.0.0
// guid: 1e2d379b-a3a4-4bc6-9bc8-121a62e7c85b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message BucketInfo {
  // Upper bound of the bucket
  double upper_bound = 1 [(buf.validate.field).double.gte = 0.0];

  // Count in this bucket after the observation
  uint64 count = 2 [(buf.validate.field).uint64.gte = 0];

  // Bucket index
  int32 bucket_index = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### counter_metric.proto {#counter_metric}

**Path**: `gcommon/v1/metrics/counter_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `CounterMetric`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/counter_metric.proto
// version: 1.0.0
// guid: 22048541-e8e6-4cf5-b476-cf12764abfb4
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * CounterMetric represents a monotonically increasing counter.
 * Counters only increase in value and are typically used for tracking
 * cumulative values like total requests, errors, or bytes processed.
 */
message CounterMetric {
  // Unique identifier for this counter
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Counter name/label
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current counter value (must be monotonically increasing)
  double value = 3;

  // Timestamp when this value was recorded
  google.protobuf.Timestamp timestamp = 4;

  // Counter description/help text
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

  // Key-value labels for this counter
  map<string, string> labels = 6;

  // Sample count (for internal tracking)
  uint64 sample_count = 7;
}
```

---

### cpu_usage.proto {#cpu_usage}

**Path**: `gcommon/v1/metrics/cpu_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `CPUUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/cpu_usage.proto
// version: 1.0.0
// guid: cda5276c-5b68-4519-b1f6-c245a74b2d66

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CPUUsage {
  // Current CPU usage (percentage)
  double current_percent = 1 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Average CPU usage (percentage)
  double avg_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Peak CPU usage (percentage)
  double peak_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### data_volume_data_point.proto {#data_volume_data_point}

**Path**: `gcommon/v1/metrics/data_volume_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `DataVolumeDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/data_volume_data_point.proto
// version: 1.0.0
// guid: c039b372-c314-4b88-82b6-3838745f0299

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DataVolumeDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 total_bytes = 2 [(buf.validate.field).int64.gte = 0];
  int64 total_metrics = 3 [(buf.validate.field).int64.gte = 0];
  int64 total_data_points = 4 [(buf.validate.field).int64.gte = 0];
  double ingestion_rate = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### data_volume_stats.proto {#data_volume_stats}

**Path**: `gcommon/v1/metrics/data_volume_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 38

**Messages** (1): `DataVolumeStats`

**Imports** (3):

- `gcommon/v1/metrics/data_volume_data_point.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/data_volume_stats.proto
// version: 1.0.0
// guid: 85a18add-5de2-4de6-9e3a-05e4959520e4

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/data_volume_data_point.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DataVolumeStats {
  // Total data stored (bytes)
  int64 total_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of metrics
  int64 total_metrics = 2 [(buf.validate.field).int64.gte = 0];

  // Total number of data points
  int64 total_data_points = 3 [(buf.validate.field).int64.gte = 0];

  // Data ingestion rate (bytes per second)
  double ingestion_rate_bytes_per_second = 4 [(buf.validate.field).double.gte = 0.0];

  // Data points ingestion rate (points per second)
  double ingestion_rate_points_per_second = 5 [(buf.validate.field).double.gte = 0.0];

  // Compression ratio
  double compression_ratio = 6 [(buf.validate.field).double.gte = 0.0];

  // Time-series data volume
  repeated DataVolumeDataPoint volume_timeseries = 7 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### data_volume_trend.proto {#data_volume_trend}

**Path**: `gcommon/v1/metrics/data_volume_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `DataVolumeTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/data_volume_trend.proto
// version: 1.0.0
// guid: 069bcf6d-438e-4623-85fa-d0c875cc7370

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DataVolumeTrend {
  string volume_trend = 1; // "increasing", "decreasing", "stable"
  string ingestion_trend = 2; // "increasing", "decreasing", "stable"
  double trend_confidence = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### deletion_options.proto {#deletion_options}

**Path**: `gcommon/v1/metrics/deletion_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `DeletionOptions`

**Imports** (3):

- `gcommon/v1/common/cleanup_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/deletion_options.proto
// version: 1.0.0
// guid: 6e247c69-d9f2-452e-bb15-e81da5c53d42

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/cleanup_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
  string grace_period = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to perform a dry run
  bool dry_run = 6;

  // Whether to force deletion even if provider is in use
  bool force = 7;

  // Whether to create a final backup before deletion
  bool create_backup = 8;

  // Cleanup strategy to use
  gcommon.v1.common.CleanupStrategy cleanup_strategy = 9;

  // Whether to wait for ongoing operations to complete
  bool wait_for_completion = 10;

  // Maximum time to wait for operations to complete
  string completion_timeout = 11 [(buf.validate.field).string.min_len = 1];
}
```

---

### deletion_result.proto {#deletion_result}

**Path**: `gcommon/v1/metrics/deletion_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `DeletionResult`

**Imports** (3):

- `gcommon/v1/metrics/dry_run_result.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/deletion_result.proto
// version: 1.0.0
// guid: a612d279-a201-40da-99b2-e6f962d0335f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/dry_run_result.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeletionResult {
  // Whether the provider was actually deleted
  bool provider_deleted = 1;

  // Amount of data that was deleted
  int64 data_deleted_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Number of metrics that were deleted
  int64 metrics_deleted = 3 [(buf.validate.field).int64.gte = 0];

  // Number of data points that were deleted
  int64 data_points_deleted = 4 [(buf.validate.field).int64.gte = 0];

  // Indices that were deleted
  repeated string deleted_indices = 5 [(buf.validate.field).repeated.min_items = 1];

  // Exports that were stopped
  repeated string stopped_exports = 6 [(buf.validate.field).repeated.min_items = 1];

  // Backups that were deleted
  repeated string deleted_backups = 7 [(buf.validate.field).repeated.min_items = 1];

  // Cleanup strategy that was used
  string cleanup_strategy_used = 8 [(buf.validate.field).string.min_len = 1];

  // Time taken for the deletion
  string deletion_duration = 9 [(buf.validate.field).string.min_len = 1];

  // What would be deleted (for dry run operations)
  DryRunResult dry_run_result = 10;
}
```

---

### disk_usage.proto {#disk_usage}

**Path**: `gcommon/v1/metrics/disk_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `DiskUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/disk_usage.proto
// version: 1.0.0
// guid: 1c6c18b3-8797-41ff-ba40-b31de4bb0e6d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DiskUsage {
  // Currently used disk space (bytes)
  int64 used_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Disk space limit (bytes)
  int64 limit_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Usage percentage
  double usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // I/O operations per second
  double iops = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### dry_run_result.proto {#dry_run_result}

**Path**: `gcommon/v1/metrics/dry_run_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `DryRunResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/dry_run_result.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174027

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * DryRunResult contains information about what would happen in a dry run.
 */
message DryRunResult {
  // Number of bytes that would be deleted
  int64 would_delete_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Number of data points that would be deleted
  int64 would_delete_points = 2 [(buf.validate.field).int64.gte = 0];

  // Number of indices that would be deleted
  int64 would_delete_indices = 3 [(buf.validate.field).int64.gte = 0];

  // Number of exports that would be stopped
  int64 would_stop_exports = 4 [(buf.validate.field).int64.gte = 0];

  // Estimated time for deletion to complete
  string estimated_deletion_time = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### error_data_point.proto {#error_data_point}

**Path**: `gcommon/v1/metrics/error_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `ErrorDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_data_point.proto
// version: 1.0.0
// guid: fc39a17b-849c-4ff7-ba0d-2d1afb9ff84c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 error_count = 2 [(buf.validate.field).int64.gte = 0];
  double error_rate = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### error_entry.proto {#error_entry}

**Path**: `gcommon/v1/metrics/error_entry.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `ErrorEntry`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_entry.proto
// version: 1.0.0
// guid: bbfe0393-e730-465d-a5fb-b1b75d58a866

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorEntry {
  google.protobuf.Timestamp timestamp = 1;
  string error_type = 2 [(buf.validate.field).string.min_len = 1];
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
  int32 count = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### error_trend.proto {#error_trend}

**Path**: `gcommon/v1/metrics/error_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `ErrorTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_trend.proto
// version: 1.0.0
// guid: 8dd5518b-cd7a-4978-b7c5-24368e5b51aa

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorTrend {
  string error_rate_trend = 1; // "improving", "worsening", "stable"
  double trend_confidence = 2 [(buf.validate.field).double.gte = 0.0];
  repeated string emerging_error_types = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### error_type_count.proto {#error_type_count}

**Path**: `gcommon/v1/metrics/error_type_count.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `ErrorTypeCount`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/error_type_count.proto
// version: 1.0.0
// guid: 8116a2bc-950e-407c-9db8-2f3985e9394d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorTypeCount {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double percentage = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### error_type_stats.proto {#error_type_stats}

**Path**: `gcommon/v1/metrics/error_type_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `ErrorTypeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/error_type_stats.proto
// version: 1.0.0
// guid: 93946dec-5ff0-40d4-8fd3-ff3d9c0b3dc4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorTypeStats {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double rate = 3 [(buf.validate.field).double.gte = 0.0];
  double percentage = 4 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### export_destination.proto {#export_destination}

**Path**: `gcommon/v1/metrics/export_destination.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `ExportDestination`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_destination.proto
// version: 1.0.0
// guid: c917e7d5-f72f-494a-b1f4-7e72c44daa5c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportDestination {
  // Destination type (file, http, s3, etc.)
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Destination configuration
  map<string, string> config = 2;

  // Whether this destination is enabled
  bool enabled = 3;
}
```

---

### export_destination_stats.proto {#export_destination_stats}

**Path**: `gcommon/v1/metrics/export_destination_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `ExportDestinationStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_destination_stats.proto
// version: 1.0.0
// guid: 11866630-71dc-417d-b08e-c9e3802eb0fa

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportDestinationStats {
  string destination_id = 1 [(buf.validate.field).string.min_len = 1];
  string destination_type = 2 [(buf.validate.field).string.min_len = 1];
  int64 exported_metrics = 3 [(buf.validate.field).int64.gte = 0];
  int64 failed_exports = 4 [(buf.validate.field).int64.gte = 0];
  double success_rate = 5 [(buf.validate.field).double.gte = 0.0];
  google.protobuf.Timestamp last_export = 6;
}
```

---

### export_destination_update.proto {#export_destination_update}

**Path**: `gcommon/v1/metrics/export_destination_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ExportDestinationUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_destination_update.proto
// version: 1.0.0
// guid: a3b4c5d6-789a-134f-8901-456789012345

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportDestinationUpdate {
  // Destination ID
  string destination_id = 1 [(buf.validate.field).string.min_len = 1];

  // Destination URL
  string url = 2 [(buf.validate.field).string.uri = true];

  // Authentication token
  string auth_token = 3 [(buf.validate.field).string.min_len = 1];

  // Enabled status
  bool enabled = 4;
}
```

---

### export_stats.proto {#export_stats}

**Path**: `gcommon/v1/metrics/export_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `ExportStats`

**Imports** (4):

- `gcommon/v1/metrics/export_destination_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_stats.proto
// version: 1.0.0
// guid: 30936733-3e37-4587-a41e-e036c6532c58

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_destination_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportStats {
  // Total exported metrics
  int64 total_exported_metrics = 1 [(buf.validate.field).int64.gte = 0];

  // Total exported data points
  int64 total_exported_data_points = 2 [(buf.validate.field).int64.gte = 0];

  // Export rate (metrics per second)
  double export_rate_metrics_per_second = 3 [(buf.validate.field).double.gte = 0.0];

  // Failed exports
  int64 failed_exports = 4 [(buf.validate.field).int64.gte = 0];

  // Export success rate
  double export_success_rate = 5 [(buf.validate.field).double.gte = 0.0];

  // Exports by destination
  repeated ExportDestinationStats export_destinations = 6 [(buf.validate.field).repeated.min_items = 1];

  // Last successful export
  google.protobuf.Timestamp last_successful_export = 7;
}
```

---

### export_status.proto {#export_status}

**Path**: `gcommon/v1/metrics/export_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `ExportStatus`

**Imports** (4):

- `gcommon/v1/metrics/exporter_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/export_status.proto
// version: 1.0.0
// guid: 5893a5fc-3748-4c46-a896-6058cdc22a34

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/exporter_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportStatus {
  int64 total_exported_metrics = 1 [(buf.validate.field).int64.gte = 0];
  int64 failed_exports = 2 [(buf.validate.field).int64.gte = 0];
  google.protobuf.Timestamp last_export = 3;
  repeated ExporterStatus exporters = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### exporter_status.proto {#exporter_status}

**Path**: `gcommon/v1/metrics/exporter_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `ExporterStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/exporter_status.proto
// version: 1.0.0
// guid: 852f34ef-6a24-4d4c-a324-3cd1192428e9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExporterStatus {
  string exporter_id = 1 [(buf.validate.field).string.min_len = 1];
  string exporter_type = 2 [(buf.validate.field).string.min_len = 1];
  string status = 3 [(buf.validate.field).string.min_len = 1];
  int64 exported_count = 4 [(buf.validate.field).int64.gte = 0];
  google.protobuf.Timestamp last_export = 5;
}
```

---

### gauge_metric.proto {#gauge_metric}

**Path**: `gcommon/v1/metrics/gauge_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `GaugeMetric`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/gauge_metric.proto
// version: 1.0.0
// guid: 027d4584-4656-45f0-9b73-2493b0ce219b
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GaugeMetric represents a value that can go up and down.
 * Gauges are used for tracking instantaneous values like memory usage,
 * temperature, active connections, or CPU utilization.
 */
message GaugeMetric {
  // Unique identifier for this gauge
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Gauge name/label
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current gauge value (can increase or decrease)
  double value = 3;

  // Timestamp when this value was recorded
  google.protobuf.Timestamp timestamp = 4;

  // Gauge description/help text
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

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

### group_by_spec.proto {#group_by_spec}

**Path**: `gcommon/v1/metrics/group_by_spec.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `GroupBySpec`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/group_by_spec.proto
// version: 1.0.0
// guid: 26a4cef4-118d-40a4-b4dc-daaed23b54a4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GroupBySpec {
  // Label keys to group by
  repeated string label_keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Time-based grouping (e.g., by hour, day)
  google.protobuf.Duration time_group = 2;

  // Maximum number of groups to return
  int32 max_groups = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### health_status_entry.proto {#health_status_entry}

**Path**: `gcommon/v1/metrics/health_status_entry.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `HealthStatusEntry`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/health_status_entry.proto
// version: 1.0.0
// guid: 9f50a418-6ad2-49ca-a7bc-f065f79e9a43

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HealthStatusEntry {
  google.protobuf.Timestamp timestamp = 1;
  string health_status = 2 [(buf.validate.field).string.min_len = 1];
  string status_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### histogram_bucket.proto {#histogram_bucket}

**Path**: `gcommon/v1/metrics/histogram_bucket.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `HistogramBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_bucket.proto
// version: 1.0.0
// guid: a9b0c1d2-345a-790f-4567-012345678901

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramBucket {
  // Upper bound for the bucket
  double upper_bound = 1 [(buf.validate.field).double.gte = 0.0];

  // Count of observations in this bucket
  int64 count = 2 [(buf.validate.field).int64.gte = 0];

  // Cumulative count
  int64 cumulative_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### histogram_metric.proto {#histogram_metric}

**Path**: `gcommon/v1/metrics/histogram_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `HistogramMetric`

**Imports** (4):

- `gcommon/v1/metrics/histogram_bucket.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_metric.proto
// version: 1.0.0
// guid: 1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/histogram_bucket.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// HistogramMetric represents a histogram metric with buckets
message HistogramMetric {
  // Metric name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### histogram_stats.proto {#histogram_stats}

**Path**: `gcommon/v1/metrics/histogram_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `HistogramStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_stats.proto
// version: 1.0.0
// guid: 7cf98dfc-ae0d-4d1b-95c2-cc76b9e021e1

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramStats {
  // Total number of observations
  uint64 total_count = 1 [(buf.validate.field).uint64.gte = 0];

  // Sum of all observed values
  double total_sum = 2 [(buf.validate.field).double.gte = 0.0];

  // Mean value
  double mean = 3 [(buf.validate.field).double.gte = 0.0];

  // Minimum observed value
  double min_value = 4 [(buf.validate.field).double.gte = 0.0];

  // Maximum observed value
  double max_value = 5 [(buf.validate.field).double.gte = 0.0];

  // Standard deviation (if calculated)
  double std_deviation = 6 [(buf.validate.field).double.gte = 0.0];
}
```

---

### histogram_value.proto {#histogram_value}

**Path**: `gcommon/v1/metrics/histogram_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `HistogramValue`

**Imports** (3):

- `gcommon/v1/metrics/histogram_bucket.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_value.proto
// version: 1.0.0
// guid: eb817cca-e34f-456c-8769-cb7f42cb931c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/histogram_bucket.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramValue {
  // Histogram buckets with their counts
  repeated HistogramBucket buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count of all samples
  uint64 count = 2 [(buf.validate.field).uint64.gte = 0];

  // Sum of all sample values
  double sum = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### label_definition.proto {#label_definition}

**Path**: `gcommon/v1/metrics/label_definition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `LabelDefinition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/label_definition.proto
// version: 1.0.0
// guid: 56dd3a22-ceda-4620-bfb2-c279efc6fab3

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message LabelDefinition {
  // Name of the label
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of what this label represents
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Whether this label is required
  bool required = 3;

  // Allowed values for this label (empty = any value allowed)
  repeated string allowed_values = 4;

  // Pattern for validating label values (regex)
  string validation_pattern = 5;

  // Default value if not specified
  string default_value = 6;
}
```

---

### memory_usage.proto {#memory_usage}

**Path**: `gcommon/v1/metrics/memory_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MemoryUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/memory_usage.proto
// version: 1.0.0
// guid: 7ae5e6f3-835f-4ab4-aa43-31e84d7fc642

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MemoryUsage {
  // Currently used memory (bytes)
  int64 used_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Memory limit (bytes)
  int64 limit_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Usage percentage
  double usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Peak memory usage (bytes)
  int64 peak_bytes = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_aggregation.proto {#metric_aggregation}

**Path**: `gcommon/v1/metrics/metric_aggregation.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricAggregation`

**Imports** (3):

- `gcommon/v1/common/aggregation_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_aggregation.proto
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/aggregation_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// Configuration for metric aggregation operations
message MetricAggregation {
  // Type of aggregation
  gcommon.v1.common.AggregationType type = 1;

  // Time window for aggregation
  int32 window_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Group by fields
  repeated string group_by = 3 [(buf.validate.field).repeated.min_items = 1];

  // Percentiles to calculate (for percentile aggregation)
  repeated double percentiles = 4 [(buf.validate.field).repeated.min_items = 1];

  // Custom aggregation function (for custom type)
  string custom_function = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to include null values in aggregation
  bool include_nulls = 6;

  // Minimum number of samples required
  int32 min_samples = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### metric_bucket.proto {#metric_bucket}

**Path**: `gcommon/v1/metrics/metric_bucket.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_bucket.proto
// version: 1.0.0
// guid: 97e038af-19d9-4d0a-8f3c-0030fd6f2b89

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricBucket represents a histogram bucket with bounds and count.
 */
message MetricBucket {
  // Lower bound inclusive.
  double lower_bound = 1 [(buf.validate.field).double.gte = 0.0];

  // Upper bound exclusive.
  double upper_bound = 2 [(buf.validate.field).double.gte = 0.0];

  // Number of samples in the bucket.
  int64 count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_data.proto {#metric_data}

**Path**: `gcommon/v1/metrics/metric_data.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `MetricData`

**Imports** (5):

- `gcommon/v1/common/metric_type.proto`
- `gcommon/v1/metrics/metric_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_data.proto
// version: 1.0.0
// guid: f9fcef53-3bbb-4860-9b50-b0a96ba93bd0

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metric_type.proto";
import "gcommon/v1/metrics/metric_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricData {
  // Unique identifier for this metric
  string metric_id = 1;

  // Metric name (e.g., "http_requests_total", "cpu_usage_percent")
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of metric (counter, gauge, histogram, etc.)
  gcommon.v1.common.MetricsMetricType type = 3;

  // Human-readable description of the metric
  string description = 4 [ (buf.validate.field).string.max_len = 1000 ];

  // Unit of measurement (e.g., "bytes", "seconds", "requests")
  string unit = 5;

  // Base labels/tags that apply to all values in this metric
  map<string, string> labels = 6;

  // The metric values (can be multiple for time series)
  repeated MetricValue values = 7;

  // When this metric data was collected/created
  google.protobuf.Timestamp created_at = 8 [ (buf.validate.field).required = true ];

  // Source system or component that generated this metric
  string source = 9;

  // Namespace or service this metric belongs to
  string namespace = 10;

  // Version of the metric schema/definition
  string schema_version = 11;
}
```

---

### metric_definition.proto {#metric_definition}

**Path**: `gcommon/v1/metrics/metric_definition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `MetricDefinition`

**Imports** (8):

- `gcommon/v1/common/metric_type.proto`
- `gcommon/v1/common/metrics_retention_policy_config.proto`
- `gcommon/v1/metrics/export_config.proto`
- `gcommon/v1/metrics/label_definition.proto`
- `gcommon/v1/metrics/metric_type_config.proto`
- `gcommon/v1/metrics/validation_rules.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_definition.proto
// version: 1.0.0
// guid: 4368bdba-c3ff-4d80-bfa1-886b807d497b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metric_type.proto";
import "gcommon/v1/common/metrics_retention_policy_config.proto";
import "gcommon/v1/metrics/export_config.proto";
import "gcommon/v1/metrics/label_definition.proto";
import "gcommon/v1/metrics/metric_type_config.proto";
import "gcommon/v1/metrics/validation_rules.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricDefinition {
  // Unique name for the metric
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of metric (counter, gauge, histogram, etc.)
  gcommon.v1.common.MetricsMetricType type = 2;

  // Human-readable description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Unit of measurement (e.g., "bytes", "requests", "seconds")
  string unit = 4;

  // Labels that this metric supports
  repeated LabelDefinition labels = 5;

  // Metric-specific configuration
  MetricTypeConfig config = 6;

  // Retention policy for this metric
  gcommon.v1.common.MetricsRetentionPolicyConfig retention = 7;

  // Export configuration for this metric
  ExportConfig export_config = 8;

  // Validation rules for metric values
  ValidationRules validation = 9;

  // Tags for metric organization and discovery
  map<string, string> tags = 10;
}
```

---

### metric_filter.proto {#metric_filter}

**Path**: `gcommon/v1/metrics/metric_filter.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_filter.proto
// version: 1.0.0
// guid: 0608db8b-1fd3-4b4b-96f4-0635b55980e8
// Filter for metrics queries

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// Filter for metrics queries
message MetricFilter {
  // Metric name patterns to include
  repeated string metric_names = 1 [(buf.validate.field).repeated.min_items = 1];

  // Label filters
  map<string, string> labels = 2;

  // Namespace filter
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Time range filter
  int64 start_timestamp = 4;
  int64 end_timestamp = 5;

  // Value threshold filters
  double min_value = 6 [(buf.validate.field).double.gte = 0.0];
  double max_value = 7 [(buf.validate.field).double.gte = 0.0];

  // Include/exclude patterns
  repeated string include_patterns = 8 [(buf.validate.field).repeated.min_items = 1];
  repeated string exclude_patterns = 9 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### metric_health.proto {#metric_health}

**Path**: `gcommon/v1/metrics/metric_health.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `MetricHealth`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_health.proto
// version: 1.0.0
// guid: c0c75431-e37e-4748-8a0d-44a7b15c5e3b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricHealth captures the health status of a metric source or scrape job.
 */
message MetricHealth {
  // Metric identifier or scrape job id
  string target_id = 1 [(buf.validate.field).string.min_len = 1];

  // Health status
  gcommon.v1.common.CommonHealthStatus status = 2;

  // When this health status was checked
  google.protobuf.Timestamp checked_at = 3;

  // Additional message or context
  string message = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### metric_info.proto {#metric_info}

**Path**: `gcommon/v1/metrics/metric_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_info.proto
// version: 1.0.0
// guid: 6e676b06-ec6f-40bb-bc0b-e2ce4484763e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricInfo {
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  string metric_type = 2;
  int64 data_points = 3;
  int64 data_volume_bytes = 4;
  double error_rate = 5;
  google.protobuf.Timestamp last_updated = 6;
}
```

---

### metric_label.proto {#metric_label}

**Path**: `gcommon/v1/metrics/metric_label.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricLabel`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_label.proto
// version: 1.0.0
// guid: 8a39fa3e-a2eb-4df9-9dcf-0c9482a16722

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricLabel represents a single key/value label used for
 * metric identification and filtering.
 */
message MetricLabel {
  // Label key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Label value
  string value = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### metric_metadata.proto {#metric_metadata}

**Path**: `gcommon/v1/metrics/metric_metadata.proto` **Package**: `gcommon.v1.metrics` **Lines**: 62

**Messages** (1): `MetricMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_metadata.proto
// version: 1.0.0
// guid: 2f161084-caee-424c-a121-9b4907586446
// file: proto/gcommon/v1/metrics/v1/metric_metadata.proto
//
// Message definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricMetadata contains metadata information about a metric.
 */
message MetricMetadata {
  // Unique identifier for the metric
  string metric_id = 1;

  // Human-readable name of the metric
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of what this metric measures
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Metric type (counter, gauge, histogram, etc.)
  string type = 4;

  // Units of measurement (e.g., "bytes", "seconds", "requests")
  string unit = 5;

  // Labels associated with this metric
  map<string, string> labels = 6;

  // When this metric was first created
  google.protobuf.Timestamp created_at = 7 [ (buf.validate.field).required = true ];

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

**Path**: `gcommon/v1/metrics/metric_quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricQuantile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_quantile.proto
// version: 1.0.0
// guid: 9ab5b0e2-0228-47d2-9a48-d714ee6f3d6f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricQuantile represents a quantile value calculated from a
 * distribution of metric samples.
 */
message MetricQuantile {
  // Quantile (0-1, e.g., 0.95 for 95th percentile).
  double quantile = 1 [(buf.validate.field).double.gte = 0.0];

  // Value observed at this quantile.
  double value = 2 [(buf.validate.field).double.gte = 0.0];
}
```

---

### metric_query.proto {#metric_query}

**Path**: `gcommon/v1/metrics/metric_query.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `MetricQuery`

**Imports** (7):

- `gcommon/v1/common/sort_options.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/aggregation_spec.proto`
- `gcommon/v1/metrics/group_by_spec.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_query.proto
// version: 1.0.0
// guid: b48baa90-492c-496f-bcef-674b2fa2d6d4

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/sort_options.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/aggregation_spec.proto";
import "gcommon/v1/metrics/group_by_spec.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricQuery {
  // Unique identifier for this query
  string query_id = 1;

  // Human-readable query name or description
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Query string (PromQL, SQL, or custom query language)
  string query_string = 3;

  // Filter criteria for selecting metrics
  MetricFilter filter = 4;

  // Time range for the query
  gcommon.v1.common.TimeRangeMetrics time_filter = 5;

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
```

---

### metric_result.proto {#metric_result}

**Path**: `gcommon/v1/metrics/metric_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricResult`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_result.proto
// version: 1.0.0
// guid: ad1215aa-2323-42d2-aeeb-b89ff72ab926

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricResult {
  // Index of the metric in the original batch (0-based)
  int32 index = 1 [(buf.validate.field).int32.gte = 0];

  // Success status for this specific metric
  bool success = 2;

  // Error information if this metric failed
  gcommon.v1.common.Error error = 3;

  // Unique ID assigned to the metric (if successful)
  string metric_id = 4 [(buf.validate.field).string.min_len = 1];

  // Timestamp when this metric was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Warnings specific to this metric
  repeated string warnings = 6 [(buf.validate.field).repeated.min_items = 1];

  // Whether this metric was deduplicated
  bool deduplicated = 7;
}
```

---

### metric_sample.proto {#metric_sample}

**Path**: `gcommon/v1/metrics/metric_sample.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `MetricSample`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_sample.proto
// version: 1.0.0
// guid: 7f2e5cc8-7e1b-49d8-b994-556a6d3aa642

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricSample represents a single value for a metric at a point in time.
 */
message MetricSample {
  // Recorded value
  double value = 1 [(buf.validate.field).double.gte = 0.0];

  // Timestamp of the sample
  google.protobuf.Timestamp timestamp = 2;

  // Optional labels associated with this sample
  map<string, string> labels = 3;
}
```

---

### metric_series.proto {#metric_series}

**Path**: `gcommon/v1/metrics/metric_series.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `MetricSeries`

**Imports** (4):

- `gcommon/v1/common/metric_type.proto`
- `gcommon/v1/metrics/metric_value.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_series.proto
// version: 1.0.0
// guid: 642e0c7a-6461-4167-b3e3-746ed9f6e413

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metric_type.proto";
import "gcommon/v1/metrics/metric_value.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricSeries {
  // Metric metadata
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  gcommon.v1.common.MetricsMetricType type = 2;
  map<string, string> labels = 3;

  // Time-ordered series of values
  repeated MetricValue values = 4;

  // Resolution/step between data points
  int64 step_seconds = 5;
}
```

---

### metric_stats.proto {#metric_stats}

**Path**: `gcommon/v1/metrics/metric_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `MetricStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_stats.proto
// version: 1.0.0
// guid: 73f03142-2df5-4e09-a4cd-b067ec1a9fbb

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricStats provides summary statistics for a set of metric values.
 */
message MetricStats {
  // Minimum value observed.
  double min = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum value observed.
  double max = 2 [(buf.validate.field).double.gte = 0.0];

  // Average of all values.
  double average = 3 [(buf.validate.field).double.gte = 0.0];

  // Sum of all values.
  double sum = 4 [(buf.validate.field).double.gte = 0.0];

  // Number of samples.
  int64 count = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_summary.proto {#metric_summary}

**Path**: `gcommon/v1/metrics/metric_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricSummary`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_summary.proto
// version: 1.0.0
// guid: 3bf744e5-01f0-4074-b7b9-5235934749bf

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricSummary {
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  string type = 2;
  int64 data_points = 3;
  int64 data_volume_bytes = 4;
  double error_rate = 5;
  google.protobuf.Timestamp last_updated = 6;
}
```

---

