# metrics_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 29
- **Messages**: 30
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [api_key_config_update.proto](#api_key_config_update)
- [applied_config.proto](#applied_config)
- [buffer_config.proto](#buffer_config)
- [configuration_summary.proto](#configuration_summary)
- [counter_config.proto](#counter_config)
- [export_config.proto](#export_config)
- [export_config_update.proto](#export_config_update)
- [gauge_config.proto](#gauge_config)
- [get_metric_config_request.proto](#get_metric_config_request)
- [get_metric_config_response.proto](#get_metric_config_response)
- [get_scrape_config_request.proto](#get_scrape_config_request)
- [get_scrape_config_response.proto](#get_scrape_config_response)
- [histogram_config.proto](#histogram_config)
- [import_config.proto](#import_config)
- [metric_config.proto](#metric_config)
- [metric_type_config.proto](#metric_type_config)
- [provider_config.proto](#provider_config)
- [provider_config_summary.proto](#provider_config_summary)
- [provider_config_update.proto](#provider_config_update)
- [scrape_config.proto](#scrape_config)
- [security_config.proto](#security_config)
- [security_config_update.proto](#security_config_update)
- [set_metric_config_request.proto](#set_metric_config_request)
- [set_metric_config_response.proto](#set_metric_config_response)
- [set_scrape_config_request.proto](#set_scrape_config_request)
- [set_scrape_config_response.proto](#set_scrape_config_response)
- [summary_config.proto](#summary_config)
- [tls_config.proto](#tls_config)
- [tls_config_update.proto](#tls_config_update)
---


## Detailed Documentation

### api_key_config_update.proto {#api_key_config_update}

**Path**: `gcommon/v1/metrics/api_key_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `APIKeyConfigUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/api_key_config_update.proto
// version: 1.0.0
// guid: f04936d2-7273-4746-bc4b-9a2c0794658f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * APIKeyConfigUpdate contains updates to API key configuration.
 */
message APIKeyConfigUpdate {
  // Updated header name
  string header_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated required setting
  bool required = 2;

  // API key updates
  repeated string allowed_key_updates = 3;

  // API keys to remove
  repeated string allowed_key_removes = 4;
}
```

---

### applied_config.proto {#applied_config}

**Path**: `gcommon/v1/metrics/applied_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `AppliedConfig`

**Imports** (3):

- `gcommon/v1/metrics/resource_allocations.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/applied_config.proto
// version: 1.0.0
// guid: d569fe55-1ee6-4cbb-94c5-f4bd79df578d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_allocations.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message AppliedConfig {
  // Configuration that was actually applied (may differ from requested)
  string config_summary = 1 [(buf.validate.field).string.min_len = 1];

  // Default values that were applied
  map<string, string> applied_defaults = 2;

  // Configuration overrides that were applied
  map<string, string> applied_overrides = 3;

  // Resource allocations that were made
  ResourceAllocations resource_allocations = 4;
}
```

---

### buffer_config.proto {#buffer_config}

**Path**: `gcommon/v1/metrics/buffer_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `BufferConfig`

**Imports** (3):

- `gcommon/v1/common/buffer_overflow_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/buffer_config.proto
// version: 1.0.0
// guid: 3cbd27e2-8ac4-4dad-8b12-6ae61bca9e6c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/buffer_overflow_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message BufferConfig {
  // Maximum number of metrics to buffer
  int32 max_buffer_size = 1 [(buf.validate.field).int32.gte = 0];

  // Buffer overflow strategy
  gcommon.v1.common.BufferOverflowStrategy overflow_strategy = 2;

  // Whether to persist buffer to disk during streaming
  bool persist_buffer = 3;

  // Maximum memory usage for buffering (bytes)
  int64 max_memory_bytes = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### configuration_summary.proto {#configuration_summary}

**Path**: `gcommon/v1/metrics/configuration_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `ConfigurationSummary`

**Imports** (4):

- `gcommon/v1/metrics/resource_limits_summary.proto`
- `gcommon/v1/metrics/security_summary.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/configuration_summary.proto
// version: 1.0.0
// guid: 9af1b63b-741f-454d-a992-90c457764c2d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_limits_summary.proto";
import "gcommon/v1/metrics/security_summary.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ConfigurationSummary {
  // Number of configured exporters
  int32 exporter_count = 1 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Security settings summary
  SecuritySummary security = 2;

  // Resource limits summary
  ResourceLimitsSummary resource_limits = 3;

  // Configuration version
  string config_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### counter_config.proto {#counter_config}

**Path**: `gcommon/v1/metrics/counter_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `CounterConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/counter_config.proto
// version: 1.0.0
// guid: 574d7f46-80ea-4a48-9dad-c55f07c5f558

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CounterConfig {
  // Starting value for the counter
  double initial_value = 1 [(buf.validate.field).double.gte = 0.0];

  // Whether the counter can be reset
  bool allow_reset = 2;

  // Maximum value before rolling over
  double max_value = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### export_config.proto {#export_config}

**Path**: `gcommon/v1/metrics/export_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 63

**Messages** (2): `ExportConfig`, `MetricsRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_config.proto
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// Configuration for exporting metrics data
message ExportConfig {
  // Export destination URL or endpoint
  string destination = 1 [(buf.validate.field).string.min_len = 1];

  // Export format (json, csv, prometheus, etc.)
  string format = 2 [(buf.validate.field).string.min_len = 1];

  // Export frequency in seconds
  int32 frequency_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Whether to compress exported data
  bool compress = 4;

  // Batch size for exports
  int32 batch_size = 5 [(buf.validate.field).int32.gte = 0];

  // Timeout for export operations in seconds
  int32 timeout_seconds = 6 [(buf.validate.field).int32.gt = 0];

  // Custom headers for HTTP exports
  map<string, string> headers = 7;

  // Authentication configuration
  map<string, string> auth_config = 8;

  // Retry configuration
  MetricsRetryConfig retry_config = 9;

  // Filtering rules for what to export
  repeated string include_patterns = 10 [(buf.validate.field).repeated.min_items = 1];
  repeated string exclude_patterns = 11 [(buf.validate.field).repeated.min_items = 1];
}

// Retry configuration for exports
message MetricsRetryConfig {
  // Maximum number of retries
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay in seconds
  int32 initial_delay_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay in seconds
  int32 max_delay_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### export_config_update.proto {#export_config_update}

**Path**: `gcommon/v1/metrics/export_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `ExportConfigUpdate`

**Imports** (3):

- `gcommon/v1/metrics/export_destination_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_config_update.proto
// version: 1.0.0
// guid: fd6ebe54-a1db-4c08-84b4-a91b690e9af6

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_destination_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ExportConfigUpdate contains updates to export configuration.
 */
message ExportConfigUpdate {
  // Updated enabled status
  bool enabled = 1;

  // Format updates
  repeated string format_updates = 2 [(buf.validate.field).repeated.min_items = 1];

  // Formats to remove
  repeated string format_removes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Destination updates
  repeated ExportDestinationUpdate destination_updates = 4 [(buf.validate.field).repeated.min_items = 1];

  // Destinations to remove
  repeated string destination_removes = 5 [(buf.validate.field).repeated.min_items = 1];

  // Updated export frequency
  string frequency = 6 [(buf.validate.field).string.min_len = 1];

  // Updated batch size
  int32 batch_size = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### gauge_config.proto {#gauge_config}

**Path**: `gcommon/v1/metrics/gauge_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `GaugeConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/gauge_config.proto
// version: 1.0.0
// guid: 9f7c124b-e567-4c31-ad6b-19c05836a84b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GaugeConfig {
  // Minimum allowed value
  double min_value = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum allowed value
  double max_value = 2 [(buf.validate.field).double.gte = 0.0];

  // Whether the gauge can go negative
  bool allow_negative = 3;
}
```

---

### get_metric_config_request.proto {#get_metric_config_request}

**Path**: `gcommon/v1/metrics/get_metric_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetMetricConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_config_request.proto
// version: 1.0.0
// guid: 82add51b-b9ac-4042-be4d-4acada2ae127
// file: proto/gcommon/v1/metrics/v1/get_metric_config_request.proto
//
// Request message to retrieve metric configuration.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricConfigRequest {
  // Metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_metric_config_response.proto {#get_metric_config_response}

**Path**: `gcommon/v1/metrics/get_metric_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetMetricConfigResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_config_response.proto
// version: 1.0.1
// guid: 1d1401a7-7986-407f-9b51-d77ceae3b42b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricConfigResponse contains metric configuration information.
 */
message GetMetricConfigResponse {
  // Operation success flag
  bool success = 1;

  // Error details if any
  gcommon.v1.common.Error error = 2;

  // Retrieved configuration
  MetricConfig config = 3;
}
```

---

### get_scrape_config_request.proto {#get_scrape_config_request}

**Path**: `gcommon/v1/metrics/get_scrape_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetScrapeConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_request.proto
// version: 1.0.0
// guid: 9ddccca8-f23d-4cc8-b483-9aea96bae473
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_request.proto
//
// Request message for retrieving scrape configuration.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetScrapeConfigRequest {
  // Provider identifier
  string provider_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_scrape_config_response.proto {#get_scrape_config_response}

**Path**: `gcommon/v1/metrics/get_scrape_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetScrapeConfigResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_response.proto
// version: 1.0.1
// guid: fa33c699-3eb3-4466-82b0-f7983815994e
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_response.proto
//
// Response containing scraping configuration for a provider.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetScrapeConfigResponse returns provider scrape configuration.
 */
message GetScrapeConfigResponse {
  // Current scrape configuration
  ScrapeConfig config = 1;

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}
```

---

### histogram_config.proto {#histogram_config}

**Path**: `gcommon/v1/metrics/histogram_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `HistogramConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_config.proto
// version: 1.0.0
// guid: d859806f-1fdc-4c74-a05d-c8872810e652

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramConfig {
  // Predefined buckets for the histogram
  repeated double buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Whether to automatically adjust buckets based on data
  bool auto_buckets = 2;

  // Maximum number of buckets to maintain
  int32 max_buckets = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### import_config.proto {#import_config}

**Path**: `gcommon/v1/metrics/import_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ImportConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/import_config.proto
// version: 1.0.0
// guid: f2e3c94f-e0d7-4e2d-9799-1a4005b10c64

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ImportConfig defines how external metrics should be imported
 * into the system.
 */
message ImportConfig {
  // List of source identifiers or URLs
  repeated string sources = 1 [(buf.validate.field).repeated.min_items = 1];

  // Cron-style schedule for imports
  string schedule = 2 [(buf.validate.field).string.min_len = 1];

  // Whether importing is enabled
  bool enabled = 3;
}
```

---

### metric_config.proto {#metric_config}

**Path**: `gcommon/v1/metrics/metric_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `MetricConfig`

**Imports** (4):

- `gcommon/v1/metrics/export_config.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_config.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_config.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricConfig contains configuration settings for a specific metric.
 */
message MetricConfig {
  // Metric name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Metric type (counter, gauge, histogram, summary, etc.)
  string metric_type = 2;

  // Whether this metric is enabled
  bool enabled = 3;

  // Collection interval
  google.protobuf.Duration collection_interval = 4;

  // Retention period for this metric
  google.protobuf.Duration retention_period = 5;

  // Labels to automatically add to this metric
  map<string, string> default_labels = 6;

  // Description of the metric
  string description = 7 [ (buf.validate.field).string.max_len = 1000 ];

  // Unit of measurement
  string unit = 8;

  // Sampling rate (0.0 to 1.0)
  double sampling_rate = 9;

  // Export configuration
  ExportConfig export_config = 10;
}
```

---

### metric_type_config.proto {#metric_type_config}

**Path**: `gcommon/v1/metrics/metric_type_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `MetricTypeConfig`

**Imports** (5):

- `gcommon/v1/metrics/counter_config.proto`
- `gcommon/v1/metrics/gauge_config.proto`
- `gcommon/v1/metrics/histogram_config.proto`
- `gcommon/v1/metrics/summary_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_type_config.proto
// version: 1.0.1
// guid: 440003e9-c836-4e1c-8e6f-754798a23832

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/counter_config.proto";
import "gcommon/v1/metrics/gauge_config.proto";
import "gcommon/v1/metrics/histogram_config.proto";
import "gcommon/v1/metrics/summary_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricTypeConfig {
  // Configuration for histogram metrics
  HistogramConfig histogram = 1;

  // Configuration for summary metrics
  SummaryConfig summary = 2;

  // Configuration for gauge metrics
  GaugeConfig gauge = 3;

  // Configuration for counter metrics
  CounterConfig counter = 4;
}
```

---

### provider_config.proto {#provider_config}

**Path**: `gcommon/v1/metrics/provider_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 50

**Messages** (1): `ProviderConfig`

**Imports** (7):

- `gcommon/v1/common/metrics_provider_type.proto`
- `gcommon/v1/common/organization_resource_limits.proto`
- `gcommon/v1/metrics/export_config.proto`
- `gcommon/v1/metrics/provider_settings.proto`
- `gcommon/v1/metrics/security_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_config.proto
// version: 1.0.0
// guid: 3539da64-8631-416f-8d05-17a4810ed876

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_provider_type.proto";
import "gcommon/v1/common/organization_resource_limits.proto";
import "gcommon/v1/metrics/export_config.proto";
import "gcommon/v1/metrics/provider_settings.proto";
import "gcommon/v1/metrics/security_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderConfig {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name for the provider
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of provider (prometheus, opentelemetry, custom, etc.)
  gcommon.v1.common.MetricsProviderType type = 3;

  // Provider-specific configuration
  ProviderSettings settings = 4;

  // Export configuration for this provider
  ExportConfig export_config = 5;

  // Resource limits imposed by the organization
  gcommon.v1.common.OrganizationResourceLimits resource_limits = 6;

  // Security configuration
  MetricsSecurityConfig security_config = 7;

  // Tags for provider organization
  map<string, string> tags = 8;

  // Description of the provider
  string description = 9 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### provider_config_summary.proto {#provider_config_summary}

**Path**: `gcommon/v1/metrics/provider_config_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ProviderConfigSummary`

**Imports** (3):

- `gcommon/v1/metrics/resource_limits_summary.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_config_summary.proto
// version: 1.0.0
// guid: 394dfc33-7acb-4583-bd49-44bdcb86e5ba

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_limits_summary.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderConfigSummary {
  // Number of configured exporters
  int32 exporter_count = 1 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Whether security is enabled
  bool security_enabled = 2;

  // Resource limits summary
  ResourceLimitsSummary resource_limits = 3;

  // Export destinations
  repeated string export_destinations = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### provider_config_update.proto {#provider_config_update}

**Path**: `gcommon/v1/metrics/provider_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `ProviderConfigUpdate`

**Imports** (7):

- `gcommon/v1/metrics/export_config_update.proto`
- `gcommon/v1/metrics/provider_settings_update.proto`
- `gcommon/v1/metrics/resource_limits_update.proto`
- `gcommon/v1/metrics/security_config_update.proto`
- `gcommon/v1/metrics/tag_updates.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_config_update.proto
// version: 1.0.0
// guid: 175e030e-5a4a-4d94-9f2a-6d8bb006602a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_config_update.proto";
import "gcommon/v1/metrics/provider_settings_update.proto";
import "gcommon/v1/metrics/resource_limits_update.proto";
import "gcommon/v1/metrics/security_config_update.proto";
import "gcommon/v1/metrics/tag_updates.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ProviderConfigUpdate contains the configuration updates to apply.
 */
message ProviderConfigUpdate {
  // Updated name (if changing)
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated description (if changing)
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Provider settings updates
  ProviderSettingsUpdate settings_update = 3;

  // Export configuration updates
  ExportConfigUpdate export_config_update = 4;

  // Resource limits updates
  ResourceLimitsUpdate resource_limits_update = 5;

  // Security configuration updates
  SecurityConfigUpdate security_config_update = 6;

  // Tag updates
  TagUpdates tag_updates = 7;
}
```

---

### scrape_config.proto {#scrape_config}

**Path**: `gcommon/v1/metrics/scrape_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `ScrapeConfig`

**Imports** (3):

- `gcommon/v1/metrics/scrape_target.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/scrape_config.proto
// version: 1.0.0
// guid: a754fb7e-a819-4731-82fd-6a587b928a9e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/scrape_target.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ScrapeConfig defines how metrics should be scraped from targets.
 */
message ScrapeConfig {
  // Job name for the scrape configuration
  string job_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Targets to scrape
  repeated ScrapeTarget targets = 2;

  // Interval between scrapes in seconds
  int32 scrape_interval_seconds = 3;
}
```

---

### security_config.proto {#security_config}

**Path**: `gcommon/v1/metrics/security_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `MetricsSecurityConfig`

**Imports** (4):

- `gcommon/v1/common/metrics_api_key_config.proto`
- `gcommon/v1/metrics/tls_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/security_config.proto
// version: 1.0.0
// guid: 61377102-cbd1-4223-8342-a2f11b1c4d47

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_api_key_config.proto";
import "gcommon/v1/metrics/tls_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsSecurityConfig {
  // Whether authentication is required
  bool require_auth = 1;

  // Allowed authentication methods
  repeated string auth_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether TLS is required
  bool require_tls = 3;

  // TLS configuration
  MetricsTLSConfig tls_config = 4;

  // API key configuration
  gcommon.v1.common.MetricsAPIKeyConfig api_key_config = 5;
}
```

---

### security_config_update.proto {#security_config_update}

**Path**: `gcommon/v1/metrics/security_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `SecurityConfigUpdate`

**Imports** (4):

- `gcommon/v1/metrics/api_key_config_update.proto`
- `gcommon/v1/metrics/tls_config_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/security_config_update.proto
// version: 1.0.0
// guid: 94abaf44-d603-4b65-8bd3-d98ca462c20e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/api_key_config_update.proto";
import "gcommon/v1/metrics/tls_config_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SecurityConfigUpdate contains updates to security configuration.
 */
message SecurityConfigUpdate {
  // Updated authentication requirement
  bool require_auth = 1;

  // Updated authentication methods
  repeated string auth_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Updated TLS requirement
  bool require_tls = 3;

  // TLS configuration updates
  TLSConfigUpdate tls_config_update = 4;

  // API key configuration updates
  APIKeyConfigUpdate api_key_config_update = 5;
}
```

---

### set_metric_config_request.proto {#set_metric_config_request}

**Path**: `gcommon/v1/metrics/set_metric_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `SetMetricConfigRequest`

**Imports** (2):

- `gcommon/v1/metrics/metric_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_metric_config_request.proto
// version: 1.0.1
// guid: d1b98b0c-98f7-47fc-9bb5-f18ebfbbe1d3

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/metric_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetMetricConfigRequest updates configuration for a metric.
 */
message SetMetricConfigRequest {
  // Updated configuration
  MetricConfig config = 1;
}
```

---

### set_metric_config_response.proto {#set_metric_config_response}

**Path**: `gcommon/v1/metrics/set_metric_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `SetMetricConfigResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_metric_config_response.proto
// version: 1.0.1
// guid: 5faba194-b6ab-42ba-99c3-62eb07df9265

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetMetricConfigResponse is returned after updating metric config.
 */
message SetMetricConfigResponse {
  // Operation success flag
  bool success = 1;

  // Error details if any
  gcommon.v1.common.Error error = 2;
}
```

---

### set_scrape_config_request.proto {#set_scrape_config_request}

**Path**: `gcommon/v1/metrics/set_scrape_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `SetScrapeConfigRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_request.proto
// version: 1.0.0
// guid: 239855c3-0df1-42c3-a9dd-c6d7709f048f
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_request.proto
//
// Request message to set scraping configuration for a provider.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SetScrapeConfigRequest {
  // Provider identifier
  string provider_id = 1 [(buf.validate.field).string.min_len = 1];

  // New scrape configuration
  ScrapeConfig config = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### set_scrape_config_response.proto {#set_scrape_config_response}

**Path**: `gcommon/v1/metrics/set_scrape_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `SetScrapeConfigResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_response.proto
// version: 1.0.1
// guid: e328641f-32d3-4439-b78e-d7fbd14ede9d
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_response.proto
//
// Response after updating scrape configuration.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetScrapeConfigResponse confirms new configuration.
 */
message SetScrapeConfigResponse {
  // Whether the update succeeded
  bool success = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### summary_config.proto {#summary_config}

**Path**: `gcommon/v1/metrics/summary_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `SummaryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_config.proto
// version: 1.0.0
// guid: f54bfb16-e799-4222-881b-a86425813aa6

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryConfig {
  // Quantiles to calculate (e.g., 0.5, 0.95, 0.99)
  repeated double quantiles = 1 [(buf.validate.field).repeated.min_items = 1];

  // Time window for calculating quantiles
  string time_window = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum age of observations to include
  string max_age = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### tls_config.proto {#tls_config}

**Path**: `gcommon/v1/metrics/tls_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricsTLSConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/tls_config.proto
// version: 1.0.0
// guid: 7da056fd-4d1f-48fa-8ee0-fbad667fa085

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsTLSConfig {
  // Certificate file path
  string cert_file = 1 [(buf.validate.field).string.min_len = 1];

  // Private key file path
  string key_file = 2 [(buf.validate.field).string.min_len = 1];

  // CA certificate file path
  string ca_file = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to verify certificates
  bool verify_certs = 4;
}
```

---

### tls_config_update.proto {#tls_config_update}

**Path**: `gcommon/v1/metrics/tls_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `TLSConfigUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/tls_config_update.proto
// version: 1.0.0
// guid: d61cb51c-f2b6-403b-bf24-6b5fe08c3e61

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TLSConfigUpdate contains updates to TLS configuration.
 */
message TLSConfigUpdate {
  // Updated certificate file path
  string cert_file = 1 [(buf.validate.field).string.min_len = 1];

  // Updated private key file path
  string key_file = 2 [(buf.validate.field).string.min_len = 1];

  // Updated CA certificate file path
  string ca_file = 3 [(buf.validate.field).string.min_len = 1];

  // Updated certificate verification setting
  bool verify_certs = 4;
}
```

---

