# metrics_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [metric_type_counts.proto](#metric_type_counts)
- [metric_value.proto](#metric_value)
- [metrics_health_info.proto](#metrics_health_info)
- [metrics_summary.proto](#metrics_summary)
- [network_usage.proto](#network_usage)
- [open_telemetry_settings.proto](#open_telemetry_settings)
- [open_telemetry_settings_update.proto](#open_telemetry_settings_update)
- [output_options.proto](#output_options)
- [pagination_info.proto](#pagination_info)
- [percentile_measurement.proto](#percentile_measurement)
- [performance_data_point.proto](#performance_data_point)
- [performance_stats.proto](#performance_stats)
- [performance_trend.proto](#performance_trend)
- [prometheus_settings.proto](#prometheus_settings)
- [prometheus_settings_update.proto](#prometheus_settings_update)
- [provider_endpoints.proto](#provider_endpoints)
- [provider_filter.proto](#provider_filter)
- [provider_info.proto](#provider_info)
- [provider_settings.proto](#provider_settings)
- [provider_settings_update.proto](#provider_settings_update)
- [provider_statistics.proto](#provider_statistics)
- [provider_stats.proto](#provider_stats)
- [provider_status.proto](#provider_status)
- [provider_summary.proto](#provider_summary)
- [quantile.proto](#quantile)
- [query_output_options.proto](#query_output_options)
- [query_plan.proto](#query_plan)
- [query_statistics.proto](#query_statistics)
- [query_stats.proto](#query_stats)
- [query_step.proto](#query_step)
- [recording_stats.proto](#recording_stats)
- [registration_options.proto](#registration_options)
- [registration_result.proto](#registration_result)
- [registration_validation.proto](#registration_validation)
- [resource_allocations.proto](#resource_allocations)
- [resource_data_point.proto](#resource_data_point)
- [resource_limits.proto](#resource_limits)
- [resource_limits_summary.proto](#resource_limits_summary)
- [resource_limits_update.proto](#resource_limits_update)
- [resource_usage.proto](#resource_usage)
- [resource_usage_stats.proto](#resource_usage_stats)
- [resource_usage_trend.proto](#resource_usage_trend)
- [schema_change.proto](#schema_change)
- [scrape_job.proto](#scrape_job)
- [scrape_target.proto](#scrape_target)
- [secondary_sort_field.proto](#secondary_sort_field)
- [security_summary.proto](#security_summary)
- [stats_d_settings.proto](#stats_d_settings)
- [stats_d_settings_update.proto](#stats_d_settings_update)
- [stats_options.proto](#stats_options)
---


## Detailed Documentation

### metric_type_counts.proto {#metric_type_counts}

**Path**: `gcommon/v1/metrics/metric_type_counts.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `MetricTypeCounts`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_type_counts.proto
// version: 1.0.0
// guid: 85755727-af90-4676-b807-fa6c65517840

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricTypeCounts {
  int64 counter_count = 1 [(buf.validate.field).int64.gte = 0];
  int64 gauge_count = 2 [(buf.validate.field).int64.gte = 0];
  int64 histogram_count = 3 [(buf.validate.field).int64.gte = 0];
  int64 summary_count = 4 [(buf.validate.field).int64.gte = 0];
  int64 timer_count = 5 [(buf.validate.field).int64.gte = 0];
  int64 custom_count = 6 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_value.proto {#metric_value}

**Path**: `gcommon/v1/metrics/metric_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `MetricValue`

**Imports** (5):

- `gcommon/v1/metrics/histogram_value.proto`
- `gcommon/v1/metrics/summary_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_value.proto
// version: 1.0.0
// guid: 00d0ab12-bd33-48a1-a6d2-ce2262ed6790

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/histogram_value.proto";
import "gcommon/v1/metrics/summary_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricValue {
  // Timestamp when this metric value was recorded
  google.protobuf.Timestamp timestamp = 1;

  // The metric value - using oneof to support different value types
  oneof value {
    // Double precision floating point value
    double double_value = 2 [(buf.validate.field).double.gte = 0.0];

    // Integer value (64-bit signed)
    int64 int_value = 3 [(buf.validate.field).int64.gte = 0];

    // String value (for label/text metrics)
    string string_value = 4 [(buf.validate.field).string.min_len = 1];

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
```

---

### metrics_health_info.proto {#metrics_health_info}

**Path**: `gcommon/v1/metrics/metrics_health_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `MetricsHealthInfo`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metrics_health_info.proto
// version: 1.0.0
// guid: e7ab1793-c874-4b03-ad41-59257c2f7cca

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsHealthInfo {
  gcommon.v1.common.CommonHealthStatus overall_status = 1;
  repeated string health_checks = 2 [(buf.validate.field).repeated.min_items = 1];
  repeated string warnings = 3 [(buf.validate.field).repeated.min_items = 1];
  google.protobuf.Timestamp last_check = 4;
}
```

---

### metrics_summary.proto {#metrics_summary}

**Path**: `gcommon/v1/metrics/metrics_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `MetricsSummary`

**Imports** (8):

- `gcommon/v1/common/metrics_error_stats.proto`
- `gcommon/v1/common/metrics_retention_info.proto`
- `gcommon/v1/metrics/export_status.proto`
- `gcommon/v1/metrics/metric_type_counts.proto`
- `gcommon/v1/metrics/performance_stats.proto`
- `gcommon/v1/metrics/top_metrics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metrics_summary.proto
// version: 1.0.0
// guid: df4c181e-98bb-488d-8052-2238af4f3a5c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_error_stats.proto";
import "gcommon/v1/common/metrics_retention_info.proto";
import "gcommon/v1/metrics/export_status.proto";
import "gcommon/v1/metrics/metric_type_counts.proto";
import "gcommon/v1/metrics/performance_stats.proto";
import "gcommon/v1/metrics/top_metrics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsSummary {
  // Total number of unique metrics
  int64 total_metrics = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of data points
  int64 total_data_points = 2 [(buf.validate.field).int64.gte = 0];

  // Total data volume (bytes)
  int64 total_data_volume_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Metrics by type
  MetricTypeCounts type_counts = 4;

  // Performance statistics
  MetricsPerformanceStats performance = 5;

  // Error statistics
  gcommon.v1.common.MetricsErrorStats errors = 6;

  // Top metrics by various criteria
  TopMetrics top_metrics = 7;

  // Retention information
  gcommon.v1.common.MetricsRetentionInfo retention = 8;

  // Export status information
  ExportStatus export_status = 9;
}
```

---

### network_usage.proto {#network_usage}

**Path**: `gcommon/v1/metrics/network_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `NetworkUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/network_usage.proto
// version: 1.0.0
// guid: b8df322e-99e1-49d7-97b0-fead8deb1998

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message NetworkUsage {
  // Bytes received per second
  int64 bytes_in_per_second = 1 [(buf.validate.field).int64.gte = 0];

  // Bytes sent per second
  int64 bytes_out_per_second = 2 [(buf.validate.field).int64.gte = 0];

  // Packets received per second
  int64 packets_in_per_second = 3 [(buf.validate.field).int64.gte = 0];

  // Packets sent per second
  int64 packets_out_per_second = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### open_telemetry_settings.proto {#open_telemetry_settings}

**Path**: `gcommon/v1/metrics/open_telemetry_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `OpenTelemetrySettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/open_telemetry_settings.proto
// version: 1.0.0
// guid: bc525cde-e766-4d2a-9ba9-d6383bdf2f6f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message OpenTelemetrySettings {
  // OTLP endpoint
  string endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to use TLS
  bool use_tls = 2;

  // Headers to include with requests
  map<string, string> headers = 3;

  // Resource attributes
  map<string, string> resource_attributes = 4;

  // Export timeout
  string timeout = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### open_telemetry_settings_update.proto {#open_telemetry_settings_update}

**Path**: `gcommon/v1/metrics/open_telemetry_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `OpenTelemetrySettingsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/open_telemetry_settings_update.proto
// version: 1.0.0
// guid: 191fb873-a4f2-418a-803f-6033ebcd28f4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * OpenTelemetrySettingsUpdate contains updates to OpenTelemetry settings.
 */
message OpenTelemetrySettingsUpdate {
  // Updated endpoint
  string endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Updated TLS setting
  bool use_tls = 2;

  // Header updates
  map<string, string> header_updates = 3;

  // Headers to remove
  repeated string header_removes = 4 [(buf.validate.field).repeated.min_items = 1];

  // Resource attribute updates
  map<string, string> resource_attribute_updates = 5;

  // Resource attributes to remove
  repeated string resource_attribute_removes = 6 [(buf.validate.field).repeated.min_items = 1];

  // Updated timeout
  string timeout = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### output_options.proto {#output_options}

**Path**: `gcommon/v1/metrics/output_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `OutputOptions`

**Imports** (4):

- `gcommon/v1/common/numeric_format.proto`
- `gcommon/v1/common/response_compression.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/output_options.proto
// version: 1.0.0
// guid: 8f7b7904-aab3-4d73-a893-b9ea03d7b75a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/numeric_format.proto";
import "gcommon/v1/common/response_compression.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message OutputOptions {
  // Format for numeric values
  gcommon.v1.common.NumericFormat numeric_format = 1;

  // Whether to include timestamps
  bool include_timestamps = 2;

  // Whether to include labels
  bool include_labels = 3;

  // Compression for large responses
  gcommon.v1.common.ResponseCompression compression = 4;

  // Whether to flatten nested structures
  bool flatten_response = 5;

  // Time zone for timestamp formatting
  string timezone = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### pagination_info.proto {#pagination_info}

**Path**: `gcommon/v1/metrics/pagination_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 43

**Messages** (1): `MetricsPaginationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/pagination_info.proto
// version: 1.0.0
// guid: f1e2d3c4-b5a6-9c8d-7e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * PaginationInfo contains information about paginated results.
 */
message MetricsPaginationInfo {
  // Current page number (1-based)
  uint32 page = 1 [(buf.validate.field).uint32.gte = 0];

  // Number of items per page
  uint32 page_size = 2 [(buf.validate.field).uint32.gte = 0];

  // Total number of items across all pages
  uint64 total_items = 3 [(buf.validate.field).uint64.gte = 0];

  // Total number of pages
  uint32 total_pages = 4 [(buf.validate.field).uint32.gte = 0];

  // Whether there is a next page
  bool has_next = 5;

  // Whether there is a previous page
  bool has_previous = 6;

  // Cursor for cursor-based pagination (optional)
  string next_cursor = 7 [(buf.validate.field).string.min_len = 1];

  // Cursor for previous page (optional)
  string previous_cursor = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### percentile_measurement.proto {#percentile_measurement}

**Path**: `gcommon/v1/metrics/percentile_measurement.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `PercentileMeasurement`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/percentile_measurement.proto
// version: 1.0.0
// guid: 48293be8-c475-44ee-b41d-c428b059063a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PercentileMeasurement {
  // Percentile value (e.g., 50.0 for median, 95.0 for 95th percentile)
  double percentile = 1 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Duration value at this percentile
  google.protobuf.Duration duration = 2;

  // Number of samples at or below this percentile
  int64 sample_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### performance_data_point.proto {#performance_data_point}

**Path**: `gcommon/v1/metrics/performance_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `PerformanceDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/performance_data_point.proto
// version: 1.0.0
// guid: ffe66544-9090-4908-b499-8e6c339440a6

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PerformanceDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  double ops_per_second = 2 [(buf.validate.field).double.gte = 0.0];
  double latency_ms = 3 [(buf.validate.field).double.gte = 0.0];
  double throughput_bytes_per_second = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### performance_stats.proto {#performance_stats}

**Path**: `gcommon/v1/metrics/performance_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 61

**Messages** (1): `MetricsPerformanceStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/performance_stats.proto
// version: 1.0.0
// guid: b3c4d5e6-f7a8-9b0c-1d2e-3f4a5b6c7d8e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * PerformanceStats contains performance metrics for provider operations.
 */
message MetricsPerformanceStats {
  // Average response time in milliseconds
  double avg_response_time_ms = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum response time in milliseconds
  double max_response_time_ms = 2 [(buf.validate.field).double.gte = 0.0];

  // Minimum response time in milliseconds
  double min_response_time_ms = 3 [(buf.validate.field).double.gte = 0.0];

  // 95th percentile response time in milliseconds
  double p95_response_time_ms = 4 [(buf.validate.field).double.gte = 0.0];

  // 99th percentile response time in milliseconds
  double p99_response_time_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // Requests per second
  double requests_per_second = 6 [(buf.validate.field).double.gte = 0.0];

  // Total number of requests processed
  uint64 total_requests = 7 [(buf.validate.field).uint64.gte = 0];

  // Number of successful requests
  uint64 successful_requests = 8 [(buf.validate.field).uint64.gte = 0];

  // Number of failed requests
  uint64 failed_requests = 9 [(buf.validate.field).uint64.gte = 0];

  // Success rate (0.0 to 1.0)
  double success_rate = 10 [(buf.validate.field).double.gte = 0.0];

  // CPU utilization percentage (0.0 to 100.0)
  double cpu_utilization = 11 [(buf.validate.field).double.gte = 0.0];

  // Memory utilization percentage (0.0 to 100.0)
  double memory_utilization = 12 [(buf.validate.field).double.gte = 0.0];

  // Network I/O in bytes per second
  double network_io_bytes_per_sec = 13 [(buf.validate.field).double.gte = 0.0];

  // Disk I/O in bytes per second
  double disk_io_bytes_per_sec = 14 [(buf.validate.field).double.gte = 0.0];
}
```

---

### performance_trend.proto {#performance_trend}

**Path**: `gcommon/v1/metrics/performance_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 18

**Messages** (1): `PerformanceTrend`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/performance_trend.proto
// version: 1.0.1
// guid: f45758c7-cea2-4efa-92f7-88144b8a8d03

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PerformanceTrend {
  string latency_trend = 1; // "improving", "degrading", "stable"
  string throughput_trend = 2; // "increasing", "decreasing", "stable"
  double trend_confidence = 3; // 0.0 to 1.0
}
```

---

### prometheus_settings.proto {#prometheus_settings}

**Path**: `gcommon/v1/metrics/prometheus_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `PrometheusSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/prometheus_settings.proto
// version: 1.0.0
// guid: 6ebbab41-b5f1-4b3c-beb2-5625c0756224

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PrometheusSettings {
  // Registry to use
  string registry = 1;

  // Whether to enable push gateway
  bool enable_push_gateway = 2;

  // Push gateway URL
  string push_gateway_url = 3 [ (buf.validate.field).string.uri = true ];

  // Job name for push gateway
  string job_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Instance name
  string instance = 5;

  // Additional labels
  map<string, string> labels = 6;
}
```

---

### prometheus_settings_update.proto {#prometheus_settings_update}

**Path**: `gcommon/v1/metrics/prometheus_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `PrometheusSettingsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/prometheus_settings_update.proto
// version: 1.0.0
// guid: 438c00d1-b391-4ced-b9d0-4ddbd6202b8d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * PrometheusSettingsUpdate contains updates to Prometheus-specific settings.
 */
message PrometheusSettingsUpdate {
  // Updated push gateway URL
  string push_gateway_url = 1 [ (buf.validate.field).string.uri = true ];

  // Updated job name
  string job_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated instance name
  string instance = 3;

  // Label updates
  map<string, string> label_updates = 4;

  // Labels to remove
  repeated string label_removes = 5;
}
```

---

### provider_endpoints.proto {#provider_endpoints}

**Path**: `gcommon/v1/metrics/provider_endpoints.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `ProviderEndpoints`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_endpoints.proto
// version: 1.0.0
// guid: f15d26e3-bb0f-47d8-a4f2-20cbebab5f75

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderEndpoints {
  // Main service endpoint
  string service_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Metrics endpoint (for scraping)
  string metrics_endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Health check endpoint
  string health_endpoint = 3 [(buf.validate.field).string.min_len = 1];

  // Admin/management endpoint
  string admin_endpoint = 4 [(buf.validate.field).string.min_len = 1];

  // Additional endpoints
  map<string, string> additional_endpoints = 5;
}
```

---

### provider_filter.proto {#provider_filter}

**Path**: `gcommon/v1/metrics/provider_filter.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `ProviderFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_filter.proto
// version: 1.0.0
// guid: ccf0f7e8-2de8-458d-b403-22b712773c55

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderFilter {
  // Filter by provider type
  repeated string provider_types = 1 [(buf.validate.field).repeated.min_items = 1];

  // Filter by provider state
  repeated string states = 2 [(buf.validate.field).repeated.min_items = 1];

  // Filter by tags
  map<string, string> tags = 3;

  // Filter by name pattern (regex)
  string name_pattern = 4 [(buf.validate.field).string.min_len = 1];

  // Filter by health status
  repeated string health_statuses = 5 [(buf.validate.field).repeated.min_items = 1];

  // Filter providers created after this time
  string created_after = 6 [(buf.validate.field).string.min_len = 1];

  // Filter providers created before this time
  string created_before = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### provider_info.proto {#provider_info}

**Path**: `gcommon/v1/metrics/provider_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 59

**Messages** (1): `ProviderInfo`

**Imports** (4):

- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_info.proto
// version: 1.0.0
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ProviderInfo contains information about a metrics provider.
 */
message ProviderInfo {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name of the provider
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
  google.protobuf.Timestamp created_at = 8 [ (buf.validate.field).required = true ];

  // When this provider was last updated
  google.protobuf.Timestamp last_updated = 9;

  // Whether this provider is enabled
  bool enabled = 10;

  // Tags associated with this provider
  repeated string tags = 11;

  // Description of the provider
  string description = 12 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### provider_settings.proto {#provider_settings}

**Path**: `gcommon/v1/metrics/provider_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ProviderSettings`

**Imports** (4):

- `gcommon/v1/metrics/open_telemetry_settings.proto`
- `gcommon/v1/metrics/prometheus_settings.proto`
- `gcommon/v1/metrics/stats_d_settings.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_settings.proto
// version: 1.0.1
// guid: bfca385c-e614-41b8-a78b-1d073e6e8a3d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/open_telemetry_settings.proto";
import "gcommon/v1/metrics/prometheus_settings.proto";
import "gcommon/v1/metrics/stats_d_settings.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderSettings {
  // Prometheus-specific settings
  PrometheusSettings prometheus = 1;

  // OpenTelemetry-specific settings
  OpenTelemetrySettings opentelemetry = 2;

  // StatsD-specific settings
  StatsDSettings statsd = 3;

  // Custom provider settings
  map<string, string> custom = 4;
}
```

---

### provider_settings_update.proto {#provider_settings_update}

**Path**: `gcommon/v1/metrics/provider_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `ProviderSettingsUpdate`

**Imports** (4):

- `gcommon/v1/metrics/open_telemetry_settings_update.proto`
- `gcommon/v1/metrics/prometheus_settings_update.proto`
- `gcommon/v1/metrics/stats_d_settings_update.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_settings_update.proto
// version: 1.0.1
// guid: d2e3f4a5-678d-023c-7890-345678901234

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/open_telemetry_settings_update.proto";
import "gcommon/v1/metrics/prometheus_settings_update.proto";
import "gcommon/v1/metrics/stats_d_settings_update.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderSettingsUpdate {
  // Prometheus settings update
  PrometheusSettingsUpdate prometheus = 1;

  // OpenTelemetry settings update
  OpenTelemetrySettingsUpdate opentelemetry = 2;

  // StatsD settings update
  StatsDSettingsUpdate statsd = 3;
}
```

---

### provider_statistics.proto {#provider_statistics}

**Path**: `gcommon/v1/metrics/provider_statistics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 56

**Messages** (1): `ProviderStatistics`

**Imports** (12):

- `gcommon/v1/common/metrics_error_stats.proto`
- `gcommon/v1/metrics/configuration_summary.proto`
- `gcommon/v1/metrics/data_volume_stats.proto`
- `gcommon/v1/metrics/export_stats.proto`
- `gcommon/v1/metrics/health_status_entry.proto`
- `gcommon/v1/metrics/performance_stats.proto`
- `gcommon/v1/metrics/provider_info.proto`
- `gcommon/v1/metrics/resource_usage_stats.proto`
- `gcommon/v1/metrics/top_metrics.proto`
- `gcommon/v1/metrics/trend_analysis.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_statistics.proto
// version: 1.0.0
// guid: 65d32fe6-818b-4b23-a785-3a059bf52535

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_error_stats.proto";
import "gcommon/v1/metrics/configuration_summary.proto";
import "gcommon/v1/metrics/data_volume_stats.proto";
import "gcommon/v1/metrics/export_stats.proto";
import "gcommon/v1/metrics/health_status_entry.proto";
import "gcommon/v1/metrics/performance_stats.proto";
import "gcommon/v1/metrics/provider_info.proto";
import "gcommon/v1/metrics/resource_usage_stats.proto";
import "gcommon/v1/metrics/top_metrics.proto";
import "gcommon/v1/metrics/trend_analysis.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderStatistics {
  // Basic provider information
  ProviderInfo provider_info = 1;

  // Performance statistics
  MetricsPerformanceStats performance = 2;

  // Resource usage statistics
  ResourceUsageStats resource_usage = 3;

  // Error statistics
  gcommon.v1.common.MetricsErrorStats errors = 4;

  // Data volume statistics
  DataVolumeStats data_volume = 5;

  // Export statistics
  ExportStats exports = 6;

  // Health status history
  repeated HealthStatusEntry health_history = 7 [(buf.validate.field).repeated.min_items = 1];

  // Configuration summary
  ConfigurationSummary config = 8;

  // Top metrics
  TopMetrics top_metrics = 9;

  // Trend analysis
  TrendAnalysis trends = 10;
}
```

---

### provider_stats.proto {#provider_stats}

**Path**: `gcommon/v1/metrics/provider_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ProviderStats`

**Imports** (3):

- `gcommon/v1/metrics/resource_usage.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_stats.proto
// version: 1.0.0
// guid: 50e90cb9-edcb-4e84-b110-1e41adfa7b50

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_usage.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderStats {
  // Number of metrics managed
  int64 metrics_count = 1 [(buf.validate.field).int64.gte = 0];

  // Number of data points
  int64 data_points_count = 2 [(buf.validate.field).int64.gte = 0];

  // Data volume (bytes)
  int64 data_volume_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Operations per second
  double operations_per_second = 4 [(buf.validate.field).double.gte = 0.0];

  // Error rate
  double error_rate = 5 [(buf.validate.field).double.gte = 0.0];

  // Resource usage
  ResourceUsage resource_usage = 6;
}
```

---

### provider_status.proto {#provider_status}

**Path**: `gcommon/v1/metrics/provider_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ProviderStatus`

**Imports** (4):

- `gcommon/v1/common/provider_state.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/provider_status.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174023

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/provider_state.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * Status of a metrics provider.
 */
message ProviderStatus {
  // Current state
  gcommon.v1.common.ProviderState state = 1;

  // Status message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Health check status
  string health = 3 [(buf.validate.field).string.min_len = 1];

  // Last update time
  google.protobuf.Timestamp last_updated = 4;

  // Provider version
  string version = 5 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### provider_summary.proto {#provider_summary}

**Path**: `gcommon/v1/metrics/provider_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 65

**Messages** (1): `ProviderSummary`

**Imports** (4):

- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_summary.proto
// version: 1.0.0
// guid: d5e6f7a8-b9c0-1d2e-3f4a-5b6c7d8e9f0a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ProviderSummary contains summary information about a metrics provider.
 */
message ProviderSummary {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name of the provider
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Provider type (e.g., "prometheus", "datadog", "custom")
  string provider_type = 3;

  // Current status of the provider
  ProviderStatus status = 4;

  // Number of metrics currently managed by this provider
  uint64 metric_count = 5;

  // Number of active data points
  uint64 active_data_points = 6;

  // Storage size used by this provider (in bytes)
  uint64 storage_size_bytes = 7;

  // When this provider was registered
  google.protobuf.Timestamp registered_at = 8;

  // When this provider was last updated
  google.protobuf.Timestamp last_updated = 9;

  // Whether this provider is currently enabled
  bool enabled = 10;

  // Performance score (0.0 to 100.0)
  double performance_score = 11;

  // Health score (0.0 to 100.0)
  double health_score = 12;

  // Tags associated with this provider
  repeated string tags = 13;

  // Brief description of the provider
  string description = 14 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### quantile.proto {#quantile}

**Path**: `gcommon/v1/metrics/quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `Quantile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/quantile.proto
// version: 1.0.0
// guid: 9aa0660a-bf89-48a8-856e-cbc136a634b9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message Quantile {
  // Quantile value (0.0 to 1.0, e.g., 0.95 for 95th percentile)
  double quantile = 1 [(buf.validate.field).double.gte = 0.0];

  // Value at this quantile
  double value = 2 [(buf.validate.field).double.gte = 0.0];
}
```

---

### query_output_options.proto {#query_output_options}

**Path**: `gcommon/v1/metrics/query_output_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `QueryOutputOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_output_options.proto
// version: 1.0.0
// guid: b6da5ff6-e156-4256-b53f-bebc54538f99

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryOutputOptions {
  // Whether to include timestamps in results
  bool include_timestamps = 1;

  // Whether to include label information
  bool include_labels = 2;

  // Whether to compress/optimize output for network transfer
  bool compress_output = 3;

  // Maximum precision for numeric values (decimal places)
  int32 numeric_precision = 4 [(buf.validate.field).int32.gte = 0];

  // Whether to include statistics about the query execution
  bool include_statistics = 5;
}
```

---

### query_plan.proto {#query_plan}

**Path**: `gcommon/v1/metrics/query_plan.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `QueryPlan`

**Imports** (4):

- `gcommon/v1/metrics/query_step.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_plan.proto
// version: 1.0.0
// guid: 6acf658c-3ed4-4910-a68b-dc33ce5d816b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/query_step.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryPlan {
  // Query that this plan is for
  string query_id = 1 [(buf.validate.field).string.min_len = 1];

  // Estimated execution time
  google.protobuf.Duration estimated_duration = 2;

  // Estimated number of data points to process
  int64 estimated_data_points = 3 [(buf.validate.field).int64.gte = 0];

  // Execution steps
  repeated QueryStep steps = 4 [(buf.validate.field).repeated.min_items = 1];

  // Storage backends that will be queried
  repeated string storage_backends = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### query_statistics.proto {#query_statistics}

**Path**: `gcommon/v1/metrics/query_statistics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `QueryStatistics`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_statistics.proto
// version: 1.0.0
// guid: 65eeb9f0-7dbe-4fd5-92e0-622eb37743ee

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryStatistics {
  // Total execution time
  google.protobuf.Duration execution_time = 1;

  // Number of data points processed
  int64 data_points_processed = 2 [(buf.validate.field).int64.gte = 0];

  // Number of metrics examined
  int64 metrics_examined = 3 [(buf.validate.field).int64.gte = 0];

  // Number of series returned
  int64 series_returned = 4 [(buf.validate.field).int64.gte = 0];

  // Memory used during query execution (bytes)
  int64 memory_used_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Storage backends queried
  repeated string storage_backends_used = 6 [(buf.validate.field).repeated.min_items = 1];

  // Cache hit rate (0.0 to 1.0)
  double cache_hit_rate = 7 [(buf.validate.field).double.gte = 0.0];

  // When the query was executed
  google.protobuf.Timestamp query_time = 8;
}
```

---

### query_stats.proto {#query_stats}

**Path**: `gcommon/v1/metrics/query_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricsQueryStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_stats.proto
// version: 1.0.0
// guid: f8a9b0c1-234f-689e-3456-901234567890

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsQueryStats {
  // Total queries executed
  int64 total_queries = 1 [(buf.validate.field).int64.gte = 0];

  // Average execution time in milliseconds
  double avg_execution_time_ms = 2 [(buf.validate.field).double.gte = 0.0];

  // Number of failed queries
  int64 failed_queries = 3 [(buf.validate.field).int64.gte = 0];

  // Cache hit rate
  double cache_hit_rate = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### query_step.proto {#query_step}

**Path**: `gcommon/v1/metrics/query_step.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `QueryStep`

**Imports** (4):

- `gcommon/v1/common/query_operation.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_step.proto
// version: 1.0.0
// guid: 93f6a8f4-e54a-4531-86a5-bb96d2bc3bf4

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/query_operation.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryStep {
  // Step identifier
  string step_id = 1;

  // Operation to perform in this step
  gcommon.v1.common.QueryOperation operation = 2;

  // Description of the operation
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Estimated cost/time for this step
  google.protobuf.Duration estimated_duration = 4;

  // Input from previous steps
  repeated string input_step_ids = 5;
}
```

---

### recording_stats.proto {#recording_stats}

**Path**: `gcommon/v1/metrics/recording_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `RecordingStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/recording_stats.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174028

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordingStats contains performance information about recording operations.
 */
message RecordingStats {
  // Time taken to process the request (milliseconds)
  int64 processing_time_ms = 1 [(buf.validate.field).int64.gte = 0];

  // Number of retries attempted
  int32 retry_count = 2 [(buf.validate.field).int32.gte = 0];

  // Whether data was successfully buffered
  bool buffered = 3;

  // Whether data was successfully persisted
  bool persisted = 4;
}
```

---

### registration_options.proto {#registration_options}

**Path**: `gcommon/v1/metrics/registration_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `RegistrationOptions`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_options.proto
// version: 1.0.1
// guid: c171bdc3-4ccb-4042-b2f0-c6c6b89ee6f2

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegistrationOptions {
  // Whether to validate the definition before registration
  bool validate_definition = 1;

  // Whether to perform a dry run (validation only)
  bool dry_run = 2;

  // Whether to create indices for efficient querying
  bool create_indices = 3;

  // Whether to enable real-time alerts for this metric
  bool enable_alerting = 4;
}
```

---

### registration_result.proto {#registration_result}

**Path**: `gcommon/v1/metrics/registration_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `RegistrationResult`

**Imports** (4):

- `gcommon/v1/common/registration_action.proto`
- `gcommon/v1/metrics/schema_change.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_result.proto
// version: 1.0.0
// guid: ed484bf7-ea0c-42a0-8479-e2c6a9d205eb

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/registration_action.proto";
import "gcommon/v1/metrics/schema_change.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegistrationResult {
  // Whether a new metric was created or existing one updated
  gcommon.v1.common.RegistrationAction action = 1;

  // Indices that were created for the metric
  repeated string created_indices = 2 [(buf.validate.field).repeated.min_items = 1];

  // Alert rules that were created (if alerting was enabled)
  repeated string created_alerts = 3 [(buf.validate.field).repeated.min_items = 1];

  // Export configurations that were set up
  repeated string configured_exports = 4 [(buf.validate.field).repeated.min_items = 1];

  // Retention policies that were applied
  repeated string applied_retention_policies = 5 [(buf.validate.field).repeated.min_items = 1];

  // Schema changes that were made
  repeated SchemaChange schema_changes = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### registration_validation.proto {#registration_validation}

**Path**: `gcommon/v1/metrics/registration_validation.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `RegistrationValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_validation.proto
// version: 1.0.0
// guid: eb100fbc-634b-48da-8ca6-51f2695247d3

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegistrationValidation {
  // Whether the metric definition is valid
  bool valid = 1;

  // Validation errors (if any)
  repeated string errors = 2 [(buf.validate.field).repeated.min_items = 1];

  // Validation warnings (if any)
  repeated string warnings = 3 [(buf.validate.field).repeated.min_items = 1];

  // Schema version used for validation
  string schema_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Suggestions for improving the metric definition
  repeated string suggestions = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### resource_allocations.proto {#resource_allocations}

**Path**: `gcommon/v1/metrics/resource_allocations.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ResourceAllocations`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_allocations.proto
// version: 1.0.0
// guid: 7b4880a1-d53a-4cf8-93db-907b2bd67f3b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceAllocations {
  // Allocated memory (bytes)
  int64 allocated_memory_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Allocated CPU (percentage)
  double allocated_cpu_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Allocated disk space (bytes)
  int64 allocated_disk_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Network ports allocated
  repeated int32 allocated_ports = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### resource_data_point.proto {#resource_data_point}

**Path**: `gcommon/v1/metrics/resource_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `ResourceDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_data_point.proto
// version: 1.0.0
// guid: aada674f-48f3-4943-b35d-4866b7b17399

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  double memory_usage_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
  double cpu_usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
  double disk_usage_percent = 4 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
  int64 network_bytes_per_second = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_limits.proto {#resource_limits}

**Path**: `gcommon/v1/metrics/resource_limits.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `MetricsResourceLimits`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_limits.proto
// version: 1.0.0
// guid: bb6325e2-4ef3-438c-8593-00a3c550b17a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsResourceLimits {
  // Maximum memory usage (bytes)
  int64 max_memory_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Maximum CPU usage (percentage)
  double max_cpu_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Maximum disk usage (bytes)
  int64 max_disk_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum number of metrics
  int64 max_metrics = 4 [(buf.validate.field).int64.gte = 0];

  // Maximum data points per metric
  int64 max_data_points_per_metric = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_limits_summary.proto {#resource_limits_summary}

**Path**: `gcommon/v1/metrics/resource_limits_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `ResourceLimitsSummary`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_limits_summary.proto
// version: 1.0.0
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ResourceLimitsSummary contains information about resource limits.
 */
message ResourceLimitsSummary {
  // Memory limit in bytes
  int64 memory_limit_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // CPU limit as percentage (0.0 to 100.0)
  double cpu_limit_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Disk limit in bytes
  int64 disk_limit_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Network bandwidth limit in bytes per second
  int64 network_limit_bytes_per_sec = 4 [(buf.validate.field).int64.gte = 0];

  // Current memory usage in bytes
  int64 memory_used_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Current CPU usage as percentage (0.0 to 100.0)
  double cpu_used_percent = 6 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Current disk usage in bytes
  int64 disk_used_bytes = 7 [(buf.validate.field).int64.gte = 0];

  // Current network usage in bytes per second
  int64 network_used_bytes_per_sec = 8 [(buf.validate.field).int64.gte = 0];

  // Whether limits are enforced
  bool limits_enforced = 9;

  // Number of limit violations in the last hour
  uint32 violations_count = 10 [(buf.validate.field).uint32.gte = 0];
}
```

---

### resource_limits_update.proto {#resource_limits_update}

**Path**: `gcommon/v1/metrics/resource_limits_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `ResourceLimitsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_limits_update.proto
// version: 1.0.0
// guid: cc6398cf-50af-461a-a6de-d00d8a2e61d9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ResourceLimitsUpdate contains updates to resource limits.
 */
message ResourceLimitsUpdate {
  // Updated memory limit
  int64 max_memory_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Updated CPU limit
  double max_cpu_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Updated disk limit
  int64 max_disk_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Updated metrics limit
  int64 max_metrics = 4 [(buf.validate.field).int64.gte = 0];

  // Updated data points per metric limit
  int64 max_data_points_per_metric = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_usage.proto {#resource_usage}

**Path**: `gcommon/v1/metrics/resource_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ResourceUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_usage.proto
// version: 1.0.0
// guid: 9feb7ea0-10ae-4507-9d2e-265744c25ac7

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceUsage {
  // Current memory usage (bytes)
  int64 memory_used_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Current CPU usage (percentage)
  double cpu_used_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Current disk usage (bytes)
  int64 disk_used_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Network bandwidth usage (bytes/sec)
  int64 network_bandwidth_bytes_per_sec = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_usage_stats.proto {#resource_usage_stats}

**Path**: `gcommon/v1/metrics/resource_usage_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ResourceUsageStats`

**Imports** (7):

- `gcommon/v1/metrics/cpu_usage.proto`
- `gcommon/v1/metrics/disk_usage.proto`
- `gcommon/v1/metrics/memory_usage.proto`
- `gcommon/v1/metrics/network_usage.proto`
- `gcommon/v1/metrics/resource_data_point.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_usage_stats.proto
// version: 1.0.0
// guid: 18e38b17-8e74-45c9-8f0e-1b1ce6da1c19

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/cpu_usage.proto";
import "gcommon/v1/metrics/disk_usage.proto";
import "gcommon/v1/metrics/memory_usage.proto";
import "gcommon/v1/metrics/network_usage.proto";
import "gcommon/v1/metrics/resource_data_point.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceUsageStats {
  // Current memory usage
  MemoryUsage memory = 1;

  // Current CPU usage
  CPUUsage cpu = 2;

  // Current disk usage
  DiskUsage disk = 3;

  // Network usage
  NetworkUsage network = 4;

  // Time-series resource usage data
  repeated ResourceDataPoint resource_timeseries = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### resource_usage_trend.proto {#resource_usage_trend}

**Path**: `gcommon/v1/metrics/resource_usage_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `ResourceUsageTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_usage_trend.proto
// version: 1.0.0
// guid: 36fe825a-fefc-4c27-ab0f-5f371bfab0b8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceUsageTrend {
  string memory_trend = 1; // "increasing", "decreasing", "stable"
  string cpu_trend = 2; // "increasing", "decreasing", "stable"
  string disk_trend = 3; // "increasing", "decreasing", "stable"
  double trend_confidence = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### schema_change.proto {#schema_change}

**Path**: `gcommon/v1/metrics/schema_change.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `SchemaChange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/schema_change.proto
// version: 1.0.0
// guid: 57c8fdff-d924-42a5-89a6-6a843c28e13e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SchemaChange {
  // Type of change made
  string change_type = 1;

  // Description of the change
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Whether this change is backward compatible
  bool backward_compatible = 3;

  // Migration steps required (if any)
  repeated string migration_steps = 4;
}
```

---

### scrape_job.proto {#scrape_job}

**Path**: `gcommon/v1/metrics/scrape_job.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ScrapeJob`

**Imports** (4):

- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/scrape_job.proto
// version: 1.1.0
// guid: 4c4b2cc6-1c94-4bd4-9a40-e1e36e1f9d02

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ScrapeJob represents a scheduled scraping task for metrics collection.
 */
message ScrapeJob {
  // Unique identifier for the scrape job
  string job_id = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration used for the scrape
  ScrapeConfig config = 2;

  // Whether the job is currently active
  bool active = 3;

  // Timestamp of the last successful scrape
  google.protobuf.Timestamp last_scrape_time = 4;

  // Timestamp of the next scheduled scrape
  google.protobuf.Timestamp next_scrape_time = 5;
}
```

---

### scrape_target.proto {#scrape_target}

**Path**: `gcommon/v1/metrics/scrape_target.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `ScrapeTarget`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/scrape_target.proto
// version: 1.0.0
// guid: bc47b323-f2ec-45a1-9eb1-a02cee44f29d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ScrapeTarget describes a target endpoint to scrape metrics from.
 */
message ScrapeTarget {
  // Target URL
  string url = 1 [(buf.validate.field).string.uri = true];

  // Optional labels to associate with this target
  map<string, string> labels = 2;
}
```

---

### secondary_sort_field.proto {#secondary_sort_field}

**Path**: `gcommon/v1/metrics/secondary_sort_field.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `SecondarySortField`

**Imports** (3):

- `gcommon/v1/common/sort_direction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/secondary_sort_field.proto
// version: 1.0.0
// guid: 136c5347-b8ae-4bd7-bf04-163e6e550f8a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/sort_direction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SecondarySortField {
  string field = 1 [(buf.validate.field).string.min_len = 1];
  gcommon.v1.common.SortDirection direction = 2;
}
```

---

### security_summary.proto {#security_summary}

**Path**: `gcommon/v1/metrics/security_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `SecuritySummary`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/security_summary.proto
// version: 1.0.0
// guid: 88866dac-7333-4ae4-9fa5-9985e01c00dc

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SecuritySummary {
  bool auth_enabled = 1;
  bool tls_enabled = 2;
  repeated string auth_methods = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### stats_d_settings.proto {#stats_d_settings}

**Path**: `gcommon/v1/metrics/stats_d_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `StatsDSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stats_d_settings.proto
// version: 1.0.0
// guid: 195c250a-8ebe-4d7d-9948-acc9c69848f5

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StatsDSettings {
  // StatsD server address
  string address = 1 [(buf.validate.field).string.min_len = 1];

  // Protocol to use (udp, tcp)
  string protocol = 2 [(buf.validate.field).string.min_len = 1];

  // Prefix for all metrics
  string prefix = 3 [(buf.validate.field).string.min_len = 1];

  // Sampling rate
  double sample_rate = 4 [(buf.validate.field).double.gte = 0.0];

  // Buffer size
  int32 buffer_size = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### stats_d_settings_update.proto {#stats_d_settings_update}

**Path**: `gcommon/v1/metrics/stats_d_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `StatsDSettingsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stats_d_settings_update.proto
// version: 1.0.0
// guid: d12fd84f-4de1-43f7-ad5d-5079bfa8b126

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * StatsDSettingsUpdate contains updates to StatsD settings.
 */
message StatsDSettingsUpdate {
  // Updated server address
  string address = 1 [(buf.validate.field).string.min_len = 1];

  // Updated protocol
  string protocol = 2 [(buf.validate.field).string.min_len = 1];

  // Updated prefix
  string prefix = 3 [(buf.validate.field).string.min_len = 1];

  // Updated sample rate
  double sample_rate = 4 [(buf.validate.field).double.gte = 0.0];

  // Updated buffer size
  int32 buffer_size = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### stats_options.proto {#stats_options}

**Path**: `gcommon/v1/metrics/stats_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `StatsOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stats_options.proto
// version: 1.0.0
// guid: 08b06fd3-e0a2-4e73-a871-038c11415178

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StatsOptions {
  // Include performance statistics
  bool include_performance = 1;

  // Include resource usage statistics
  bool include_resource_usage = 2;

  // Include error statistics
  bool include_errors = 3;

  // Include data volume statistics
  bool include_data_volume = 4;

  // Include export statistics
  bool include_exports = 5;

  // Include health status history
  bool include_health_history = 6;

  // Include configuration information
  bool include_config = 7;

  // Include top metrics by various criteria
  bool include_top_metrics = 8;

  // Maximum number of top metrics to include
  int32 top_metrics_limit = 9 [(buf.validate.field).int32.gte = 0];

  // Include trend analysis
  bool include_trends = 10;
}
```

---

