# metrics_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 17
- **Messages**: 17
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [stream_options.proto](#stream_options)
- [stream_start.proto](#stream_start)
- [summary_metric.proto](#summary_metric)
- [summary_options.proto](#summary_options)
- [summary_quantile.proto](#summary_quantile)
- [summary_value.proto](#summary_value)
- [tag_updates.proto](#tag_updates)
- [time_series.proto](#time_series)
- [timer_metric.proto](#timer_metric)
- [timer_statistics.proto](#timer_statistics)
- [timestamp_range.proto](#timestamp_range)
- [top_metrics.proto](#top_metrics)
- [trend_analysis.proto](#trend_analysis)
- [unregistration_options.proto](#unregistration_options)
- [unregistration_result.proto](#unregistration_result)
- [validation_rules.proto](#validation_rules)
- [validation_summary.proto](#validation_summary)
---


## Detailed Documentation

### stream_options.proto {#stream_options}

**Path**: `gcommon/v1/metrics/stream_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 45

**Messages** (1): `StreamOptions`

**Imports** (4):

- `gcommon/v1/common/stream_compression.proto`
- `gcommon/v1/common/stream_qos.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_options.proto
// version: 1.0.0
// guid: dfdf5759-e1b6-489a-9a64-0477334ebb2a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/stream_compression.proto";
import "gcommon/v1/common/stream_qos.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StreamOptions {
  // Whether to include historical data or only new metrics
  bool include_historical = 1;

  // Maximum number of metrics to send per message
  int32 batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum time to wait before sending a batch (milliseconds)
  int32 batch_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Whether to include metadata with each metric
  bool include_metadata = 4;

  // Compression to use for the stream
  gcommon.v1.common.StreamCompression compression = 5;

  // Whether to send heartbeat messages during idle periods
  bool send_heartbeats = 6;

  // Heartbeat interval (seconds)
  int32 heartbeat_interval_seconds = 7 [(buf.validate.field).int32.gte = 0];

  // Whether to automatically retry on errors
  bool auto_retry = 8;

  // Quality of service level
  gcommon.v1.common.StreamQOS qos = 9;
}
```

---

### stream_start.proto {#stream_start}

**Path**: `gcommon/v1/metrics/stream_start.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `StreamStart`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_start.proto
// version: 1.0.0
// guid: 035f2196-05b5-429a-be1c-e7feae4a5b49

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StreamStart {
  // Start from a specific timestamp
  google.protobuf.Timestamp from_timestamp = 1;

  // Start from the beginning of available data
  bool from_beginning = 2;

  // Start from the current time (live streaming only)
  bool from_now = 3;

  // Start from a specific offset or position
  string from_offset = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### summary_metric.proto {#summary_metric}

**Path**: `gcommon/v1/metrics/summary_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 52

**Messages** (1): `SummaryMetric`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/summary_quantile.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_metric.proto
// version: 1.0.0
// guid: b33d2c5c-ecf6-44ee-9472-340b3362d75d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/summary_quantile.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryMetric {
  // Metric name (e.g., "http_request_duration_seconds")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Total count of observations
  uint64 sample_count = 2;

  // Sum of all observed values
  double sample_sum = 3;

  // Quantiles (e.g., 0.5, 0.9, 0.95, 0.99)
  repeated SummaryQuantile quantiles = 4;

  // Labels for metric dimensions
  map<string, string> labels = 5;

  // Timestamp when metric was recorded
  google.protobuf.Timestamp timestamp = 6;

  // Help text describing the metric
  string help = 7;

  // Metric unit (e.g., "seconds", "bytes")
  string unit = 8;

  // Maximum age of observations in the summary
  google.protobuf.Duration max_age = 9;

  // Metadata for request tracing
  gcommon.v1.common.RequestMetadata metadata = 10;
}
```

---

### summary_options.proto {#summary_options}

**Path**: `gcommon/v1/metrics/summary_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `SummaryOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_options.proto
// version: 1.0.0
// guid: c4d787f0-9e09-4c12-a14d-12627a57902d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryOptions {
  // Include metric count information
  bool include_counts = 1;

  // Include data volume information
  bool include_data_volume = 2;

  // Include performance statistics
  bool include_performance = 3;

  // Include error rates and statistics
  bool include_errors = 4;

  // Include top metrics by various criteria
  bool include_top_metrics = 5;

  // Include retention policy information
  bool include_retention = 6;

  // Include export status information
  bool include_export_status = 7;

  // Maximum number of top metrics to include
  int32 top_metrics_limit = 8 [(buf.validate.field).int32.gte = 0];
}
```

---

### summary_quantile.proto {#summary_quantile}

**Path**: `gcommon/v1/metrics/summary_quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `SummaryQuantile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_quantile.proto
// version: 1.0.0
// guid: 4e691373-59b7-411a-a555-70e922bd4b72

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryQuantile {
  // Quantile value (0.0-1.0, e.g., 0.5 for median, 0.95 for 95th percentile)
  double quantile = 1 [(buf.validate.field).double.gte = 0.0];

  // Value at this quantile
  double value = 2 [(buf.validate.field).double.gte = 0.0];
}
```

---

### summary_value.proto {#summary_value}

**Path**: `gcommon/v1/metrics/summary_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `SummaryValue`

**Imports** (3):

- `gcommon/v1/metrics/quantile.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_value.proto
// version: 1.0.0
// guid: 535bdb2a-1af8-4ed2-a092-892f8d42a85c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/quantile.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryValue {
  // Quantile values
  repeated Quantile quantiles = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count of all samples
  uint64 count = 2 [(buf.validate.field).uint64.gte = 0];

  // Sum of all sample values
  double sum = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### tag_updates.proto {#tag_updates}

**Path**: `gcommon/v1/metrics/tag_updates.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `TagUpdates`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/tag_updates.proto
// version: 1.0.0
// guid: 3f881144-83c6-471b-9db4-227cb066b468

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TagUpdates contains tag update operations.
 */
message TagUpdates {
  // Tags to add or update
  map<string, string> tag_updates = 1;

  // Tag keys to remove
  repeated string tag_removes = 2 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### time_series.proto {#time_series}

**Path**: `gcommon/v1/metrics/time_series.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `TimeSeries`

**Imports** (3):

- `gcommon/v1/metrics/metric_sample.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_series.proto
// version: 1.0.0
// guid: 0f1e1fe8-f8db-4e8f-8220-628a1b9c02bf

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/metric_sample.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TimeSeries represents a collection of metric samples over time.
 */
message TimeSeries {
  // Identifier of the metric this series belongs to
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Ordered list of samples
  repeated MetricSample samples = 2 [(buf.validate.field).repeated.min_items = 1];

  // Labels associated with the series
  map<string, string> labels = 3;
}
```

---

### timer_metric.proto {#timer_metric}

**Path**: `gcommon/v1/metrics/timer_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 58

**Messages** (1): `TimerMetric`

**Imports** (6):

- `gcommon/v1/metrics/percentile_measurement.proto`
- `gcommon/v1/metrics/timer_statistics.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/timer_metric.proto
// version: 1.0.0
// guid: 13ed2d88-7499-4d64-83cb-9292a1e35065

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/percentile_measurement.proto";
import "gcommon/v1/metrics/timer_statistics.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message TimerMetric {
  // Unique identifier for this timer measurement
  string timer_id = 1;

  // Name or label for this timer (e.g., "api_request_duration")
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Start time of the measured operation
  google.protobuf.Timestamp start_time = 3;

  // End time of the measured operation
  google.protobuf.Timestamp end_time = 4;

  // Duration of the measured operation
  google.protobuf.Duration duration = 5;

  // Tags/labels for categorization and filtering
  map<string, string> tags = 6;

  // Statistical aggregations for this timer
  TimerStatistics statistics = 7;

  // Whether this timer is currently running
  bool is_running = 8;

  // Number of times this timer has been recorded
  int64 count = 9;

  // Total accumulated time across all recordings
  google.protobuf.Duration total_duration = 10;

  // Percentile measurements
  repeated PercentileMeasurement percentiles = 11;

  // Timestamp when this metric was recorded
  google.protobuf.Timestamp recorded_at = 12;
}
```

---

### timer_statistics.proto {#timer_statistics}

**Path**: `gcommon/v1/metrics/timer_statistics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `TimerStatistics`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/timer_statistics.proto
// version: 1.0.0
// guid: 19d58a3d-7ce0-4642-8116-3baba86aee49

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message TimerStatistics {
  // Minimum duration observed
  google.protobuf.Duration min_duration = 1;

  // Maximum duration observed
  google.protobuf.Duration max_duration = 2;

  // Mean (average) duration
  google.protobuf.Duration mean_duration = 3;

  // Standard deviation of durations
  double standard_deviation_ms = 4 [(buf.validate.field).double.gte = 0.0];

  // Variance of durations
  double variance_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // Number of samples used for these statistics
  int64 sample_count = 6 [(buf.validate.field).int64.gte = 0];

  // Rate of measurements per second
  double rate_per_second = 7 [(buf.validate.field).double.gte = 0.0];

  // Most recent measurement duration
  google.protobuf.Duration last_duration = 8;
}
```

---

### timestamp_range.proto {#timestamp_range}

**Path**: `gcommon/v1/metrics/timestamp_range.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `MetricsTimestampRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/timestamp_range.proto
// version: 1.0.1
// guid: e7f8a9b0-123e-578d-2345-890123456789

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsTimestampRange {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;
}
```

---

### top_metrics.proto {#top_metrics}

**Path**: `gcommon/v1/metrics/top_metrics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `TopMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/top_metrics.proto
// version: 1.0.0
// guid: c4d5e6f7-a8b9-0c1d-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TopMetrics contains information about top performing/problematic metrics.
 */
message TopMetrics {
  // Most active metrics (by volume)
  repeated string most_active = 1 [(buf.validate.field).repeated.min_items = 1];

  // Largest metrics by data volume
  repeated string largest_by_volume = 2 [(buf.validate.field).repeated.min_items = 1];

  // Metrics with highest error rates
  repeated string highest_errors = 3 [(buf.validate.field).repeated.min_items = 1];

  // Most frequently queried metrics
  repeated string most_queried = 4 [(buf.validate.field).repeated.min_items = 1];

  // Slowest performing metrics
  repeated string slowest_performing = 5 [(buf.validate.field).repeated.min_items = 1];

  // Most resource-intensive metrics
  repeated string most_resource_intensive = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### trend_analysis.proto {#trend_analysis}

**Path**: `gcommon/v1/metrics/trend_analysis.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `TrendAnalysis`

**Imports** (5):

- `gcommon/v1/metrics/data_volume_trend.proto`
- `gcommon/v1/metrics/error_trend.proto`
- `gcommon/v1/metrics/performance_trend.proto`
- `gcommon/v1/metrics/resource_usage_trend.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/trend_analysis.proto
// version: 1.0.1
// guid: cb796e78-7aa6-47b8-8545-402a70e2c9e0

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/data_volume_trend.proto";
import "gcommon/v1/metrics/error_trend.proto";
import "gcommon/v1/metrics/performance_trend.proto";
import "gcommon/v1/metrics/resource_usage_trend.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message TrendAnalysis {
  // Performance trends
  PerformanceTrend performance = 1;

  // Resource usage trends
  ResourceUsageTrend resource_usage = 2;

  // Error trends
  ErrorTrend errors = 3;

  // Data volume trends
  DataVolumeTrend data_volume = 4;
}
```

---

### unregistration_options.proto {#unregistration_options}

**Path**: `gcommon/v1/metrics/unregistration_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `UnregistrationOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/unregistration_options.proto
// version: 1.0.0
// guid: 158ebf54-a2dd-4dae-b8dc-9c9fb19344db

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UnregistrationOptions {
  // Whether to delete all associated data
  bool delete_data = 1;

  // Whether to delete associated indices
  bool delete_indices = 2;

  // Whether to remove alert rules
  bool remove_alerts = 3;

  // Whether to stop export configurations
  bool stop_exports = 4;

  // Grace period before actual deletion (duration string like "24h")
  string grace_period = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to perform a dry run (show what would be deleted)
  bool dry_run = 6;

  // Whether to force deletion even if metric is in use
  bool force = 7;

  // Whether to create a backup before deletion
  bool create_backup = 8;
}
```

---

### unregistration_result.proto {#unregistration_result}

**Path**: `gcommon/v1/metrics/unregistration_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `UnregistrationResult`

**Imports** (4):

- `gcommon/v1/metrics/dry_run_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/unregistration_result.proto
// version: 1.0.0
// guid: ada4f63c-d9d5-496b-a0f9-a70062740177

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/dry_run_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UnregistrationResult {
  // Whether the metric definition was deleted
  bool definition_deleted = 1;

  // Amount of data that was deleted (bytes)
  int64 data_deleted_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Number of data points deleted
  int64 data_points_deleted = 3 [(buf.validate.field).int64.gte = 0];

  // Indices that were deleted
  repeated string deleted_indices = 4 [(buf.validate.field).repeated.min_items = 1];

  // Alert rules that were removed
  repeated string removed_alerts = 5 [(buf.validate.field).repeated.min_items = 1];

  // Export configurations that were stopped
  repeated string stopped_exports = 6 [(buf.validate.field).repeated.min_items = 1];

  // Time when actual deletion will occur (if grace period is set)
  google.protobuf.Timestamp scheduled_deletion = 7;

  // What would be deleted (for dry run operations)
  DryRunResult dry_run_result = 8;
}
```

---

### validation_rules.proto {#validation_rules}

**Path**: `gcommon/v1/metrics/validation_rules.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ValidationRules`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/validation_rules.proto
// version: 1.0.0
// guid: 0d988017-d38b-43d4-bb5b-c076ce14326a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ValidationRules {
  // Minimum allowed value
  double min_value = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum allowed value
  double max_value = 2 [(buf.validate.field).double.gte = 0.0];

  // Whether null/zero values are allowed
  bool allow_null = 3;

  // Custom validation expressions
  repeated string validation_expressions = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### validation_summary.proto {#validation_summary}

**Path**: `gcommon/v1/metrics/validation_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ValidationSummary`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/validation_summary.proto
// version: 1.0.0
// guid: 6bc5ca1a-e2c7-4863-a193-8ee676812c63

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ValidationSummary {
  // Number of metrics that passed validation
  int32 valid_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of metrics that failed validation
  int32 invalid_count = 2 [(buf.validate.field).int32.gte = 0];

  // Most common validation errors
  repeated string common_errors = 3 [(buf.validate.field).repeated.min_items = 1];

  // Schema version used for validation
  string schema_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

