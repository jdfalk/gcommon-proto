# metrics_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 24
- **Messages**: 24
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 3

## Files in this Module

- [apikey_config_update.proto](#apikey_config_update)
- [config_change.proto](#config_change)
- [export_config.proto](#export_config)
- [export_config_options.proto](#export_config_options) ⚠️ 3 issues
- [export_config_update.proto](#export_config_update)
- [get_metric_config_request.proto](#get_metric_config_request)
- [get_metric_config_response.proto](#get_metric_config_response)
- [get_scrape_config_request.proto](#get_scrape_config_request)
- [get_scrape_config_response.proto](#get_scrape_config_response)
- [import_config.proto](#import_config)
- [metric_config.proto](#metric_config)
- [open_telemetry_settings_update.proto](#open_telemetry_settings_update)
- [prometheus_settings_update.proto](#prometheus_settings_update)
- [provider_config_update.proto](#provider_config_update)
- [provider_settings_update.proto](#provider_settings_update)
- [retention_policy_retentionpolicyconfig.proto](#retention_policy_retentionpolicyconfig)
- [scrape_config.proto](#scrape_config)
- [security_config_update.proto](#security_config_update)
- [set_metric_config_request.proto](#set_metric_config_request)
- [set_metric_config_response.proto](#set_metric_config_response)
- [set_scrape_config_request.proto](#set_scrape_config_request)
- [set_scrape_config_response.proto](#set_scrape_config_response)
- [stats_dsettings_update.proto](#stats_dsettings_update)
- [tlsconfig_update.proto](#tlsconfig_update)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_1](./config_1.md)
- [config_2](./config_2.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)

**Modules that depend on this one**:

- [config_config_1](./config_config_1.md)
- [metrics_2](./metrics_2.md)
- [metrics_api_1](./metrics_api_1.md)
- [metrics_api_2](./metrics_api_2.md)

---

## Detailed Documentation

### apikey_config_update.proto {#apikey_config_update}

**Path**: `pkg/metrics/proto/apikey_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `APIKeyConfigUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/apikey_config_update.proto
// version: 1.0.0
// guid: f04936d2-7273-4746-bc4b-9a2c0794658f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * APIKeyConfigUpdate contains updates to API key configuration.
 */
message APIKeyConfigUpdate {
  // Updated header name
  string header_name = 1;

  // Updated required setting
  bool required = 2;

  // API key updates
  repeated string allowed_key_updates = 3;

  // API keys to remove
  repeated string allowed_key_removes = 4;
}

```

---

### config_change.proto {#config_change}

**Path**: `pkg/metrics/proto/config_change.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ConfigChange`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/change_type.proto` → [config_1](./config_1.md#change_type) → [metrics_1](./metrics_1.md#change_type)
- `pkg/metrics/proto/validation_result.proto` → [config_2](./config_2.md#validation_result) → [metrics_2](./metrics_2.md#validation_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/config_change.proto
// version: 1.1.0
// guid: 29bbb593-9903-43ef-a25e-1c3c7c0a4e64

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/change_type.proto";
import "pkg/metrics/proto/validation_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ConfigChange describes a configuration change that was made.
 */
message ConfigChange {
  // Type of change
  ChangeType change_type = 1;

  // Setting that was changed
  string setting_path = 2;

  // Old value (if applicable)
  string old_value = 3;

  // New value
  string new_value = 4;

  // Description of the change
  string description = 5;
}

```

---

### export_config.proto {#export_config}

**Path**: `pkg/metrics/proto/export_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `ExportConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/export_config.proto
// version: 1.0.0
// guid: b0c1d2e3-456b-801a-5678-123456789012

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ExportConfig {
  // Export enabled status
  bool enabled = 1;

  // Export interval in seconds
  int32 interval_seconds = 2;

  // Export destinations
  repeated string destinations = 3;

  // Export format
  string format = 4;
}

```

---

### export_config_options.proto {#export_config_options}

**Path**: `pkg/metrics/proto/export_config_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ExportConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (3)

- Line 20: Commented field - // CONFLICT_DISABLED: ExportFormat format = 1;
- Line 23: Commented field - // CONFLICT_DISABLED: CompressionType compression = 2;
- Line 26: Commented field - // CONFLICT_DISABLED: string destination = 3;

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/export_config_options.proto
// file: metrics/proto/messages/export_config_options.proto
//
// Configuration options for exporting metrics to external systems.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ExportConfig defines how metrics are exported.
 */
// CONFLICT_DISABLED: message ExportConfig {
// CONFLICT_DISABLED:   // Output format (e.g., prometheus, json)
// CONFLICT_DISABLED:   ExportFormat format = 1;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Compression algorithm to use
// CONFLICT_DISABLED:   CompressionType compression = 2;
// CONFLICT_DISABLED:
// CONFLICT_DISABLED:   // Destination URL or path
// CONFLICT_DISABLED:   string destination = 3;
// CONFLICT_DISABLED: }

```

---

### export_config_update.proto {#export_config_update}

**Path**: `pkg/metrics/proto/export_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `ExportConfigUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/export_destination_update.proto` → [metrics_1](./metrics_1.md#export_destination_update)

#### Source Code

```protobuf
// file: pkg/metrics/proto/export_config_update.proto
// version: 1.0.0
// guid: fd6ebe54-a1db-4c08-84b4-a91b690e9af6

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/export_destination_update.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ExportConfigUpdate contains updates to export configuration.
 */
message ExportConfigUpdate {
  // Updated enabled status
  bool enabled = 1;

  // Format updates
  repeated string format_updates = 2;

  // Formats to remove
  repeated string format_removes = 3;

  // Destination updates
  repeated ExportDestinationUpdate destination_updates = 4;

  // Destinations to remove
  repeated string destination_removes = 5;

  // Updated export frequency
  string frequency = 6;

  // Updated batch size
  int32 batch_size = 7;
}

```

---

### get_metric_config_request.proto {#get_metric_config_request}

**Path**: `pkg/metrics/proto/get_metric_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `GetMetricConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_metric_config_request.proto
// file: metrics/proto/requests/get_metric_config_request.proto
//
// Request message to retrieve metric configuration.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetMetricConfigRequest {
  // Metric identifier
  string metric_id = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_metric_config_response.proto {#get_metric_config_response}

**Path**: `pkg/metrics/proto/get_metric_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `GetMetricConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_config.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_metric_config_response.proto
// version: 1.0.0
// guid: 1d1401a7-7986-407f-9b51-d77ceae3b42b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

**Path**: `pkg/metrics/proto/get_scrape_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `GetScrapeConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_scrape_config_request.proto
// file: metrics/proto/requests/get_scrape_config_request.proto
//
// Request message for retrieving scrape configuration.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetScrapeConfigRequest {
  // Provider identifier
  string provider_id = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_scrape_config_response.proto {#get_scrape_config_response}

**Path**: `pkg/metrics/proto/get_scrape_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetScrapeConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/scrape_config.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_scrape_config_response.proto
// file: metrics/proto/responses/get_scrape_config_response.proto
//
// Response containing scraping configuration for a provider.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/scrape_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### import_config.proto {#import_config}

**Path**: `pkg/metrics/proto/import_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ImportConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/import_config.proto
// version: 1.0.0
// guid: f2e3c94f-e0d7-4e2d-9799-1a4005b10c64

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ImportConfig defines how external metrics should be imported
 * into the system.
 */
message ImportConfig {
  // List of source identifiers or URLs
  repeated string sources = 1;

  // Cron-style schedule for imports
  string schedule = 2;

  // Whether importing is enabled
  bool enabled = 3;
}

```

---

### metric_config.proto {#metric_config}

**Path**: `pkg/metrics/proto/metric_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 50

**Messages** (1): `MetricConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/export_config.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/metric_config.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/export_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricConfig contains configuration settings for a specific metric.
 */
message MetricConfig {
  // Metric name
  string name = 1;

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
  string description = 7;

  // Unit of measurement
  string unit = 8;

  // Sampling rate (0.0 to 1.0)
  double sampling_rate = 9;

  // Export configuration
  ExportConfig export_config = 10;
}

```

---

### open_telemetry_settings_update.proto {#open_telemetry_settings_update}

**Path**: `pkg/metrics/proto/open_telemetry_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `OpenTelemetrySettingsUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/open_telemetry_settings_update.proto
// version: 1.0.0
// guid: 191fb873-a4f2-418a-803f-6033ebcd28f4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * OpenTelemetrySettingsUpdate contains updates to OpenTelemetry settings.
 */
message OpenTelemetrySettingsUpdate {
  // Updated endpoint
  string endpoint = 1;

  // Updated TLS setting
  bool use_tls = 2;

  // Header updates
  map<string, string> header_updates = 3;

  // Headers to remove
  repeated string header_removes = 4;

  // Resource attribute updates
  map<string, string> resource_attribute_updates = 5;

  // Resource attributes to remove
  repeated string resource_attribute_removes = 6;

  // Updated timeout
  string timeout = 7;
}

```

---

### prometheus_settings_update.proto {#prometheus_settings_update}

**Path**: `pkg/metrics/proto/prometheus_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `PrometheusSettingsUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/prometheus_settings_update.proto
// version: 1.0.0
// guid: 438c00d1-b391-4ced-b9d0-4ddbd6202b8d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * PrometheusSettingsUpdate contains updates to Prometheus-specific settings.
 */
message PrometheusSettingsUpdate {
  // Updated push gateway URL
  string push_gateway_url = 1;

  // Updated job name
  string job_name = 2;

  // Updated instance name
  string instance = 3;

  // Label updates
  map<string, string> label_updates = 4;

  // Labels to remove
  repeated string label_removes = 5;
}

```

---

### provider_config_update.proto {#provider_config_update}

**Path**: `pkg/metrics/proto/provider_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `ProviderConfigUpdate`

**Imports** (6):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/export_config_update.proto`
- `pkg/metrics/proto/provider_settings_update.proto`
- `pkg/metrics/proto/resource_limits_update.proto` → [metrics_2](./metrics_2.md#resource_limits_update)
- `pkg/metrics/proto/security_config_update.proto`
- `pkg/metrics/proto/tag_updates.proto` → [metrics_2](./metrics_2.md#tag_updates)

#### Source Code

```protobuf
// file: pkg/metrics/proto/provider_config_update.proto
// version: 1.0.0
// guid: 175e030e-5a4a-4d94-9f2a-6d8bb006602a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/export_config_update.proto";
import "pkg/metrics/proto/provider_settings_update.proto";
import "pkg/metrics/proto/resource_limits_update.proto";
import "pkg/metrics/proto/security_config_update.proto";
import "pkg/metrics/proto/tag_updates.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ProviderConfigUpdate contains the configuration updates to apply.
 */
message ProviderConfigUpdate {
  // Updated name (if changing)
  string name = 1;

  // Updated description (if changing)
  string description = 2;

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

### provider_settings_update.proto {#provider_settings_update}

**Path**: `pkg/metrics/proto/provider_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `ProviderSettingsUpdate`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/open_telemetry_settings_update.proto`
- `pkg/metrics/proto/prometheus_settings_update.proto`
- `pkg/metrics/proto/stats_dsettings_update.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/provider_settings_update.proto
// version: 1.0.0
// guid: d2e3f4a5-678d-023c-7890-345678901234

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/open_telemetry_settings_update.proto";
import "pkg/metrics/proto/prometheus_settings_update.proto";
import "pkg/metrics/proto/stats_dsettings_update.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### retention_policy_retentionpolicyconfig.proto {#retention_policy_retentionpolicyconfig}

**Path**: `pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `RetentionPolicyConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/retention_policy_retentionpolicyconfig.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174024

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * Retention policy configuration for metric data.
 */
message RetentionPolicyConfig {
  // How long to retain data
  google.protobuf.Duration duration = 1;

  // Storage tier configuration
  string storage_tier = 2;

  // Compression settings
  string compression = 3;
}

```

---

### scrape_config.proto {#scrape_config}

**Path**: `pkg/metrics/proto/scrape_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ScrapeConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/scrape_target.proto` → [metrics_2](./metrics_2.md#scrape_target)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/scrape_config.proto
// version: 1.0.0
// guid: a754fb7e-a819-4731-82fd-6a587b928a9e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/scrape_target.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ScrapeConfig defines how metrics should be scraped from targets.
 */
message ScrapeConfig {
  // Job name for the scrape configuration
  string job_name = 1;

  // Targets to scrape
  repeated ScrapeTarget targets = 2;

  // Interval between scrapes in seconds
  int32 scrape_interval_seconds = 3;
}

```

---

### security_config_update.proto {#security_config_update}

**Path**: `pkg/metrics/proto/security_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `SecurityConfigUpdate`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/apikey_config_update.proto`
- `pkg/metrics/proto/tlsconfig_update.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/security_config_update.proto
// version: 1.0.0
// guid: 94abaf44-d603-4b65-8bd3-d98ca462c20e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/apikey_config_update.proto";
import "pkg/metrics/proto/tlsconfig_update.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * SecurityConfigUpdate contains updates to security configuration.
 */
message SecurityConfigUpdate {
  // Updated authentication requirement
  bool require_auth = 1;

  // Updated authentication methods
  repeated string auth_methods = 2;

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

**Path**: `pkg/metrics/proto/set_metric_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `SetMetricConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/metric_config.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/set_metric_config_request.proto
// version: 1.0.0
// guid: d1b98b0c-98f7-47fc-9bb5-f18ebfbbe1d3

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/metric_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

**Path**: `pkg/metrics/proto/set_metric_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `SetMetricConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/set_metric_config_response.proto
// version: 1.0.0
// guid: 5faba194-b6ab-42ba-99c3-62eb07df9265

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

**Path**: `pkg/metrics/proto/set_scrape_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `SetScrapeConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/metrics/proto/scrape_config.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/set_scrape_config_request.proto
// file: metrics/proto/requests/set_scrape_config_request.proto
//
// Request message to set scraping configuration for a provider.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/scrape_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message SetScrapeConfigRequest {
  // Provider identifier
  string provider_id = 1;

  // New scrape configuration
  ScrapeConfig config = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### set_scrape_config_response.proto {#set_scrape_config_response}

**Path**: `pkg/metrics/proto/set_scrape_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `SetScrapeConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/set_scrape_config_response.proto
// file: metrics/proto/responses/set_scrape_config_response.proto
//
// Response after updating scrape configuration.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

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

### stats_dsettings_update.proto {#stats_dsettings_update}

**Path**: `pkg/metrics/proto/stats_dsettings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `StatsDSettingsUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/stats_dsettings_update.proto
// version: 1.0.0
// guid: d12fd84f-4de1-43f7-ad5d-5079bfa8b126

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StatsDSettingsUpdate contains updates to StatsD settings.
 */
message StatsDSettingsUpdate {
  // Updated server address
  string address = 1;

  // Updated protocol
  string protocol = 2;

  // Updated prefix
  string prefix = 3;

  // Updated sample rate
  double sample_rate = 4;

  // Updated buffer size
  int32 buffer_size = 5;
}

```

---

### tlsconfig_update.proto {#tlsconfig_update}

**Path**: `pkg/metrics/proto/tlsconfig_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `TLSConfigUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/tlsconfig_update.proto
// version: 1.0.0
// guid: d61cb51c-f2b6-403b-bf24-6b5fe08c3e61

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * TLSConfigUpdate contains updates to TLS configuration.
 */
message TLSConfigUpdate {
  // Updated certificate file path
  string cert_file = 1;

  // Updated private key file path
  string key_file = 2;

  // Updated CA certificate file path
  string ca_file = 3;

  // Updated certificate verification setting
  bool verify_certs = 4;
}

```

---
