# metrics_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 16
- **Messages**: 20
- **Services**: 0
- **Enums**: 1

## Files in this Module

- [response_compression.proto](#response_compression)
- [set_alerting_rules_request.proto](#set_alerting_rules_request)
- [set_alerting_rules_response.proto](#set_alerting_rules_response)
- [set_metric_metadata_request.proto](#set_metric_metadata_request)
- [set_metric_metadata_response.proto](#set_metric_metadata_response)
- [start_scraping_request.proto](#start_scraping_request)
- [start_scraping_response.proto](#start_scraping_response)
- [stop_scraping_request.proto](#stop_scraping_request)
- [stop_scraping_response.proto](#stop_scraping_response)
- [stream_metrics_request.proto](#stream_metrics_request)
- [unregister_metric_request.proto](#unregister_metric_request)
- [unregister_metric_response.proto](#unregister_metric_response)
- [update_metric_request.proto](#update_metric_request)
- [update_metric_response.proto](#update_metric_response)
- [update_provider_request.proto](#update_provider_request)
- [update_provider_response.proto](#update_provider_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_2](./config_2.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [metrics_config](./metrics_config.md)

**Modules that depend on this one**:

- [metrics_api_1](./metrics_api_1.md)
- [metrics_services](./metrics_services.md)

---

## Detailed Documentation

### response_compression.proto {#response_compression}

**Path**: `pkg/metrics/proto/response_compression.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 31

**Enums** (1): `ResponseCompression`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/response_compression.proto
// version: 1.0.0
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ResponseCompression defines compression options for responses.
 * Specifies compression algorithms for metric response data.
 */
enum ResponseCompression {
  // Unspecified compression
  RESPONSE_COMPRESSION_UNSPECIFIED = 0;

  // No compression
  RESPONSE_COMPRESSION_NONE = 1;

  // GZIP compression
  RESPONSE_COMPRESSION_GZIP = 2;

  // Snappy compression
  RESPONSE_COMPRESSION_SNAPPY = 3;
}

```

---

### set_alerting_rules_request.proto {#set_alerting_rules_request}

**Path**: `pkg/metrics/proto/set_alerting_rules_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `SetAlertingRulesRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/alerting_rule.proto` →
  [metrics_1](./metrics_1.md#alerting_rule)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/set_alerting_rules_request.proto
// file: metrics/proto/requests/set_alerting_rules_request.proto
//
// Request message for configuring alerting rules for a metric.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/alerting_rule.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message SetAlertingRulesRequest {
  // Metric identifier
  string metric_id = 1;

  // Rules to set
  repeated AlertingRule rules = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### set_alerting_rules_response.proto {#set_alerting_rules_response}

**Path**: `pkg/metrics/proto/set_alerting_rules_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `SetAlertingRulesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/set_alerting_rules_response.proto
// file: metrics/proto/responses/set_alerting_rules_response.proto
//
// Response after setting alerting rules.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * SetAlertingRulesResponse confirms alert rule configuration.
 */
message SetAlertingRulesResponse {
  // Whether the operation succeeded
  bool success = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### set_metric_metadata_request.proto {#set_metric_metadata_request}

**Path**: `pkg/metrics/proto/set_metric_metadata_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `SetMetricMetadataRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/set_metric_metadata_request.proto
// file: metrics/proto/requests/set_metric_metadata_request.proto
//
// Request message for updating metric metadata.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message SetMetricMetadataRequest {
  // Metric metadata to apply
  MetricMetadata metadata = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata request_meta = 2 [lazy = true];
}

```

---

### set_metric_metadata_response.proto {#set_metric_metadata_response}

**Path**: `pkg/metrics/proto/set_metric_metadata_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `SetMetricMetadataResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/set_metric_metadata_response.proto
// file: metrics/proto/responses/set_metric_metadata_response.proto
//
// Response after updating metric metadata.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * SetMetricMetadataResponse returns updated metadata.
 */
message SetMetricMetadataResponse {
  // Updated metadata
  MetricMetadata metadata = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### start_scraping_request.proto {#start_scraping_request}

**Path**: `pkg/metrics/proto/start_scraping_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `StartScrapingRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/scrape_config.proto` →
  [metrics_config](./metrics_config.md#scrape_config)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/start_scraping_request.proto
// version: 1.1.0
// guid: 3bf09215-7dbf-4f23-97b5-911aeb40f125

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/scrape_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message StartScrapingRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metrics provider identifier
  string provider_id = 2;

  // Scrape configuration to use
  ScrapeConfig config = 3;
}

```

---

### start_scraping_response.proto {#start_scraping_response}

**Path**: `pkg/metrics/proto/start_scraping_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `StartScrapingResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/scrape_job.proto` → [metrics_2](./metrics_2.md#scrape_job)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/start_scraping_response.proto
// version: 1.1.0
// guid: 83543cf4-50e7-4161-9c5f-5ddca3a0655f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/scrape_job.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StartScrapingResponse returns the result of starting a scrape job.
 */
message StartScrapingResponse {
  // Whether the job was started successfully
  bool success = 1;

  // Error information if unsuccessful
  gcommon.v1.common.Error error = 2;

  // Details of the started scrape job
  ScrapeJob job = 3;

  // Timestamp when the job started
  google.protobuf.Timestamp started_at = 4;
}

```

---

### stop_scraping_request.proto {#stop_scraping_request}

**Path**: `pkg/metrics/proto/stop_scraping_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `StopScrapingRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/stop_scraping_request.proto
// version: 1.1.0
// guid: 4fac5447-f3bb-4627-94d7-4d6115c265f1

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message StopScrapingRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier of the job to stop
  string job_id = 2;
}

```

---

### stop_scraping_response.proto {#stop_scraping_response}

**Path**: `pkg/metrics/proto/stop_scraping_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `StopScrapingResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/scrape_job.proto` → [metrics_2](./metrics_2.md#scrape_job)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/stop_scraping_response.proto
// version: 1.1.0
// guid: 7d2eb263-b398-4b98-af07-c9950ab73d05

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/scrape_job.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StopScrapingResponse returns the result of stopping a scrape job.
 */
message StopScrapingResponse {
  // Whether the job was stopped successfully
  bool success = 1;

  // Error information if unsuccessful
  gcommon.v1.common.Error error = 2;

  // Details of the stopped job
  ScrapeJob job = 3;

  // Timestamp when the job stopped
  google.protobuf.Timestamp stopped_at = 4;
}

```

---

### stream_metrics_request.proto {#stream_metrics_request}

**Path**: `pkg/metrics/proto/stream_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 109

**Messages** (4): `StreamMetricsRequest`, `StreamOptions`, `StreamStart`,
`BufferConfig`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/buffer_overflow_strategy.proto` →
  [metrics_1](./metrics_1.md#buffer_overflow_strategy)
- `pkg/metrics/proto/metric_filter.proto` →
  [metrics_1](./metrics_1.md#metric_filter)
- `pkg/metrics/proto/stream_compression.proto` →
  [metrics_2](./metrics_2.md#stream_compression)
- `pkg/metrics/proto/stream_qos.proto` → [metrics_2](./metrics_2.md#stream_qos)

#### Source Code

```protobuf
// file: pkg/metrics/proto/stream_metrics_request.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/buffer_overflow_strategy.proto";
import "pkg/metrics/proto/metric_filter.proto";
import "pkg/metrics/proto/stream_compression.proto";
import "pkg/metrics/proto/stream_qos.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StreamMetricsRequest represents a request to stream metrics data in real-time.
 * This enables continuous monitoring and real-time metric consumption.
 */
message StreamMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter to determine which metrics to stream
  MetricFilter filter = 2;

  // Streaming configuration options
  StreamOptions options = 3;

  // Optional provider ID to stream from
  string provider_id = 4;

  // Starting point for the stream
  StreamStart start = 5;

  // Buffer configuration for the stream
  BufferConfig buffer_config = 6;
}

/**
 * StreamOptions configures how metrics streaming should behave.
 */
message StreamOptions {
  // Whether to include historical data or only new metrics
  bool include_historical = 1;

  // Maximum number of metrics to send per message
  int32 batch_size = 2;

  // Maximum time to wait before sending a batch (milliseconds)
  int32 batch_timeout_ms = 3;

  // Whether to include metadata with each metric
  bool include_metadata = 4;

  // Compression to use for the stream
  StreamCompression compression = 5;

  // Whether to send heartbeat messages during idle periods
  bool send_heartbeats = 6;

  // Heartbeat interval (seconds)
  int32 heartbeat_interval_seconds = 7;

  // Whether to automatically retry on errors
  bool auto_retry = 8;

  // Quality of service level
  StreamQOS qos = 9;
}

/**
 * StreamStart defines where to start the stream.
 */
message StreamStart {
  // Start from a specific timestamp
  google.protobuf.Timestamp from_timestamp = 1;

  // Start from the beginning of available data
  bool from_beginning = 2;

  // Start from the current time (live streaming only)
  bool from_now = 3;

  // Start from a specific offset or position
  string from_offset = 4;
}

/**
 * BufferConfig configures buffering behavior for the stream.
 */
message BufferConfig {
  // Maximum number of metrics to buffer
  int32 max_buffer_size = 1;

  // Buffer overflow strategy
  BufferOverflowStrategy overflow_strategy = 2;

  // Whether to persist buffer to disk during streaming
  bool persist_buffer = 3;

  // Maximum memory usage for buffering (bytes)
  int64 max_memory_bytes = 4;
}

```

---

### unregister_metric_request.proto {#unregister_metric_request}

**Path**: `pkg/metrics/proto/unregister_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 65

**Messages** (2): `UnregisterMetricRequest`, `UnregistrationOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/unregister_metric_request.proto
// file: metrics/proto/requests/unregister_metric_request.proto
//
// Unregister metric request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message UnregisterMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metric identifier (either name or ID)
  oneof metric_identifier {
    // Metric name to unregister
    string metric_name = 2;

    // Metric ID to unregister
    string metric_id = 3;
  }

  // Optional provider ID to unregister from
  string provider_id = 4;

  // Options for the unregistration process
  UnregistrationOptions options = 5;
}

/**
 * UnregistrationOptions configure the unregistration process.
 */
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
  string grace_period = 5;

  // Whether to perform a dry run (show what would be deleted)
  bool dry_run = 6;

  // Whether to force deletion even if metric is in use
  bool force = 7;

  // Whether to create a backup before deletion
  bool create_backup = 8;
}

```

---

### unregister_metric_response.proto {#unregister_metric_response}

**Path**: `pkg/metrics/proto/unregister_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 79

**Messages** (2): `UnregisterMetricResponse`, `UnregistrationResult`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/backup_info.proto` →
  [metrics_1](./metrics_1.md#backup_info)
- `pkg/metrics/proto/dry_run_result.proto` →
  [metrics_1](./metrics_1.md#dry_run_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/unregister_metric_response.proto
// file: metrics/proto/responses/unregister_metric_response.proto
//
// Unregister metric response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/backup_info.proto";
import "pkg/metrics/proto/dry_run_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UnregisterMetricResponse contains the result of unregistering a metric.
 */
message UnregisterMetricResponse {
  // Success status of the unregistration
  bool success = 1;

  // Error information if unregistration failed
  gcommon.v1.common.Error error = 2;

  // ID of the metric that was unregistered
  string metric_id = 3;

  // Name of the metric that was unregistered
  string metric_name = 4;

  // When the metric was unregistered
  google.protobuf.Timestamp unregistered_at = 5;

  // Provider that handled the unregistration
  string provider_id = 6;

  // Information about what was deleted/cleaned up
  UnregistrationResult result = 7;

  // Warnings or informational messages
  repeated string warnings = 8;

  // Backup information (if backup was created)
  BackupInfo backup_info = 9;
}

/**
 * UnregistrationResult contains information about what was deleted/cleaned up.
 */
message UnregistrationResult {
  // Whether the metric definition was deleted
  bool definition_deleted = 1;

  // Amount of data that was deleted (bytes)
  int64 data_deleted_bytes = 2;

  // Number of data points deleted
  int64 data_points_deleted = 3;

  // Indices that were deleted
  repeated string deleted_indices = 4;

  // Alert rules that were removed
  repeated string removed_alerts = 5;

  // Export configurations that were stopped
  repeated string stopped_exports = 6;

  // Time when actual deletion will occur (if grace period is set)
  google.protobuf.Timestamp scheduled_deletion = 7;

  // What would be deleted (for dry run operations)
  DryRunResult dry_run_result = 8;
}

```

---

### update_metric_request.proto {#update_metric_request}

**Path**: `pkg/metrics/proto/update_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `UpdateMetricRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/update_metric_request.proto
// file: metrics/proto/requests/update_metric_request.proto
//
// Request message to update an existing metric definition.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message UpdateMetricRequest {
  // Updated metric data
  MetricData metric = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### update_metric_response.proto {#update_metric_response}

**Path**: `pkg/metrics/proto/update_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `UpdateMetricResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/update_metric_response.proto
// file: metrics/proto/responses/update_metric_response.proto
//
// Response returned after updating a metric definition.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UpdateMetricResponse returns updated metadata.
 */
message UpdateMetricResponse {
  // Updated metric metadata
  MetricMetadata metadata = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### update_provider_request.proto {#update_provider_request}

**Path**: `pkg/metrics/proto/update_provider_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `UpdateProviderRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/update_provider_request.proto
// version: 1.0.0
// guid: b2c3d4e5-f6a7-8901-2345-6789abcdef01

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message UpdateProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to update
  string provider_id = 2;

  // Updated configuration
  string name = 3;
  string type = 4;
  map<string, string> config = 5;
  string description = 6;
  bool enabled = 7;
}

```

---

### update_provider_response.proto {#update_provider_response}

**Path**: `pkg/metrics/proto/update_provider_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 48

**Messages** (1): `UpdateProviderResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/provider_status.proto` →
  [metrics_2](./metrics_2.md#provider_status)
- `pkg/metrics/proto/validation_result.proto` →
  [config_2](./config_2.md#validation_result) →
  [metrics_2](./metrics_2.md#validation_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/update_provider_response.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d

// Update provider response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/provider_status.proto";
import "pkg/metrics/proto/validation_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UpdateProviderResponse contains the result of updating a metrics provider.
 */
message UpdateProviderResponse {
  // Success status of the update
  bool success = 1;

  // Provider ID that was updated
  string provider_id = 2;

  // Updated provider status
  ProviderStatus status = 3;

  // Validation results from the update operation
  repeated ValidationResult validation_results = 4;

  // Error information if update failed
  gcommon.v1.common.Error error = 5;

  // Timestamp when the update was processed
  google.protobuf.Timestamp updated_at = 6;

  // Configuration changes that were applied
  repeated string applied_changes = 7;

  // Warning messages about the update
  repeated string warnings = 8;
}

```

---
