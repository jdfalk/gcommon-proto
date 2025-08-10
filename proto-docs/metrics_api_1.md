# metrics_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 123
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [create_metric_request.proto](#create_metric_request)
- [create_metric_response.proto](#create_metric_response)
- [create_provider_request.proto](#create_provider_request)
- [create_provider_response.proto](#create_provider_response)
- [delete_metric_request.proto](#delete_metric_request)
- [delete_metric_response.proto](#delete_metric_response)
- [delete_provider_request.proto](#delete_provider_request)
- [delete_provider_response.proto](#delete_provider_response)
- [export_metrics_request.proto](#export_metrics_request)
- [export_metrics_response.proto](#export_metrics_response)
- [get_alerting_rules_request.proto](#get_alerting_rules_request)
- [get_alerting_rules_response.proto](#get_alerting_rules_response)
- [get_metric_metadata_request.proto](#get_metric_metadata_request)
- [get_metric_metadata_response.proto](#get_metric_metadata_response)
- [get_metric_request.proto](#get_metric_request)
- [get_metric_response.proto](#get_metric_response)
- [get_metrics_request.proto](#get_metrics_request)
- [get_metrics_response.proto](#get_metrics_response)
- [get_metrics_summary_request.proto](#get_metrics_summary_request)
- [get_metrics_summary_response.proto](#get_metrics_summary_response)
- [get_provider_stats_request.proto](#get_provider_stats_request)
- [get_provider_stats_response.proto](#get_provider_stats_response)
- [get_stats_request.proto](#get_stats_request)
- [get_stats_response.proto](#get_stats_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [import_metrics_request.proto](#import_metrics_request)
- [import_metrics_response.proto](#import_metrics_response)
- [list_metrics_request.proto](#list_metrics_request)
- [list_metrics_response.proto](#list_metrics_response)
- [list_providers_request.proto](#list_providers_request)
- [list_providers_response.proto](#list_providers_response)
- [query_metrics_request.proto](#query_metrics_request)
- [query_metrics_response.proto](#query_metrics_response)
- [record_counter_request.proto](#record_counter_request)
- [record_counter_response.proto](#record_counter_response)
- [record_gauge_request.proto](#record_gauge_request)
- [record_gauge_response.proto](#record_gauge_response)
- [record_histogram_request.proto](#record_histogram_request)
- [record_histogram_response.proto](#record_histogram_response)
- [record_metric_request.proto](#record_metric_request)
- [record_metric_response.proto](#record_metric_response)
- [record_metrics_request.proto](#record_metrics_request)
- [record_metrics_response.proto](#record_metrics_response)
- [record_summary_request.proto](#record_summary_request)
- [record_summary_response.proto](#record_summary_response)
- [register_metric_request.proto](#register_metric_request)
- [register_metric_response.proto](#register_metric_response)
- [reset_metrics_request.proto](#reset_metrics_request)
- [reset_metrics_response.proto](#reset_metrics_response)

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)
- [common](./common.md)
- [config_2](./config_2.md)
- [database](./database.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [metrics_api_2](./metrics_api_2.md)
- [metrics_config](./metrics_config.md)
- [queue_1](./queue_1.md)
- [queue_2](./queue_2.md)
- [web](./web.md)

**Modules that depend on this one**:

- [cache_services](./cache_services.md)
- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)
- [metrics_services](./metrics_services.md)

---

## Detailed Documentation

### create_metric_request.proto {#create_metric_request}

**Path**: `pkg/metrics/proto/create_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `CreateMetricRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/create_metric_request.proto
// file: metrics/proto/requests/create_metric_request.proto
//
// Request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message CreateMetricRequest {
  // Metric to create
  MetricData metric = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### create_metric_response.proto {#create_metric_response}

**Path**: `pkg/metrics/proto/create_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `CreateMetricResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/create_metric_response.proto
// file: metrics/proto/responses/create_metric_response.proto
//
// Response returned after creating a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * CreateMetricResponse contains the result of a metric creation.
 */
message CreateMetricResponse {
  // Created metric metadata
  MetricMetadata metadata = 1;

  // Operation error details if any
  gcommon.v1.common.Error error = 2;
}

```

---

### create_provider_request.proto {#create_provider_request}

**Path**: `pkg/metrics/proto/create_provider_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 233

**Messages** (11): `CreateProviderRequest`, `ProviderConfig`,
`ProviderSettings`, `PrometheusSettings`, `OpenTelemetrySettings`,
`StatsDSettings`, `ExportDestination`, `ResourceLimits`, `SecurityConfig`,
`TLSConfig`, `APIKeyConfig`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/export_config.proto` →
  [metrics_config](./metrics_config.md#export_config)
- `pkg/metrics/proto/provider_type.proto` → [auth](./auth.md#provider_type) →
  [metrics_2](./metrics_2.md#provider_type)

#### Source Code

```protobuf
// file: pkg/metrics/proto/create_provider_request.proto
// version: 1.2.0
// guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/export_config.proto";
import "pkg/metrics/proto/provider_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * CreateProviderRequest represents a request to create a new metrics provider.
 */
message CreateProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider configuration
  ProviderConfig config = 2;

  // Whether to validate the configuration before creating
  bool validate_config = 3;

  // Whether to perform a dry run (validation only)
  bool dry_run = 4;

  // Whether to start the provider immediately after creation
  bool auto_start = 5;
}

/**
 * ProviderConfig contains the configuration for a metrics provider.
 */
message ProviderConfig {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name for the provider
  string name = 2;

  // Type of provider (prometheus, opentelemetry, custom, etc.)
  ProviderType type = 3;

  // Provider-specific configuration
  ProviderSettings settings = 4;

  // Export configuration for this provider
  ExportConfig export_config = 5;

  // Resource limits for this provider
  ResourceLimits resource_limits = 6;

  // Security configuration
  SecurityConfig security_config = 7;

  // Tags for provider organization
  map<string, string> tags = 8;

  // Description of the provider
  string description = 9;
}

/**
 * ProviderSettings contains type-specific configuration.
 */
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

/**
 * PrometheusSettings contains Prometheus-specific configuration.
 */
message PrometheusSettings {
  // Registry to use
  string registry = 1;

  // Whether to enable push gateway
  bool enable_push_gateway = 2;

  // Push gateway URL
  string push_gateway_url = 3;

  // Job name for push gateway
  string job_name = 4;

  // Instance name
  string instance = 5;

  // Additional labels
  map<string, string> labels = 6;
}

/**
 * OpenTelemetrySettings contains OpenTelemetry-specific configuration.
 */
message OpenTelemetrySettings {
  // OTLP endpoint
  string endpoint = 1;

  // Whether to use TLS
  bool use_tls = 2;

  // Headers to include with requests
  map<string, string> headers = 3;

  // Resource attributes
  map<string, string> resource_attributes = 4;

  // Export timeout
  string timeout = 5;
}

/**
 * StatsDSettings contains StatsD-specific configuration.
 */
message StatsDSettings {
  // StatsD server address
  string address = 1;

  // Protocol to use (udp, tcp)
  string protocol = 2;

  // Prefix for all metrics
  string prefix = 3;

  // Sampling rate
  double sample_rate = 4;

  // Buffer size
  int32 buffer_size = 5;
}

/**
 * ExportDestination defines a destination for metric exports.
 */
message ExportDestination {
  // Destination type (file, http, s3, etc.)
  string type = 1;

  // Destination configuration
  map<string, string> config = 2;

  // Whether this destination is enabled
  bool enabled = 3;
}

/**
 * ResourceLimits defines resource limits for the provider.
 */
message ResourceLimits {
  // Maximum memory usage (bytes)
  int64 max_memory_bytes = 1;

  // Maximum CPU usage (percentage)
  double max_cpu_percent = 2;

  // Maximum disk usage (bytes)
  int64 max_disk_bytes = 3;

  // Maximum number of metrics
  int64 max_metrics = 4;

  // Maximum data points per metric
  int64 max_data_points_per_metric = 5;
}

/**
 * SecurityConfig defines security configuration for the provider.
 */
message SecurityConfig {
  // Whether authentication is required
  bool require_auth = 1;

  // Allowed authentication methods
  repeated string auth_methods = 2;

  // Whether TLS is required
  bool require_tls = 3;

  // TLS configuration
  TLSConfig tls_config = 4;

  // API key configuration
  APIKeyConfig api_key_config = 5;
}

/**
 * TLSConfig defines TLS configuration.
 */
message TLSConfig {
  // Certificate file path
  string cert_file = 1;

  // Private key file path
  string key_file = 2;

  // CA certificate file path
  string ca_file = 3;

  // Whether to verify certificates
  bool verify_certs = 4;
}

/**
 * APIKeyConfig defines API key configuration.
 */
message APIKeyConfig {
  // Header name for API key
  string header_name = 1;

  // Whether API key is required
  bool required = 2;

  // Allowed API keys (for validation)
  repeated string allowed_keys = 3;
}

```

---

### create_provider_response.proto {#create_provider_response}

**Path**: `pkg/metrics/proto/create_provider_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 104

**Messages** (4): `CreateProviderResponse`, `AppliedConfig`,
`ResourceAllocations`, `ProviderEndpoints`

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
// file: pkg/metrics/proto/responses/create_provider_response.proto
// file: metrics/proto/responses/create_provider_response.proto
//
// Create provider response definitions for metrics module
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
 * CreateProviderResponse contains the result of creating a metrics provider.
 */
message CreateProviderResponse {
  // Success status of the creation
  bool success = 1;

  // Error information if creation failed
  gcommon.v1.common.Error error = 2;

  // ID of the created provider
  string provider_id = 3;

  // When the provider was created
  google.protobuf.Timestamp created_at = 4;

  // Current status of the provider
  ProviderStatus status = 5;

  // Validation results
  ValidationResult validation = 6;

  // Configuration details that were applied
  AppliedConfig applied_config = 7;

  // Warnings or informational messages
  repeated string warnings = 8;

  // Endpoint information for accessing the provider
  ProviderEndpoints endpoints = 9;
}

/**
 * AppliedConfig contains information about the configuration that was applied.
 */
message AppliedConfig {
  // Configuration that was actually applied (may differ from requested)
  string config_summary = 1;

  // Default values that were applied
  map<string, string> applied_defaults = 2;

  // Configuration overrides that were applied
  map<string, string> applied_overrides = 3;

  // Resource allocations that were made
  ResourceAllocations resource_allocations = 4;
}

/**
 * ResourceAllocations contains information about allocated resources.
 */
message ResourceAllocations {
  // Allocated memory (bytes)
  int64 allocated_memory_bytes = 1;

  // Allocated CPU (percentage)
  double allocated_cpu_percent = 2;

  // Allocated disk space (bytes)
  int64 allocated_disk_bytes = 3;

  // Network ports allocated
  repeated int32 allocated_ports = 4;
}

/**
 * ProviderEndpoints contains endpoint information for the provider.
 */
message ProviderEndpoints {
  // Main service endpoint
  string service_endpoint = 1;

  // Metrics endpoint (for scraping)
  string metrics_endpoint = 2;

  // Health check endpoint
  string health_endpoint = 3;

  // Admin/management endpoint
  string admin_endpoint = 4;

  // Additional endpoints
  map<string, string> additional_endpoints = 5;
}

```

---

### delete_metric_request.proto {#delete_metric_request}

**Path**: `pkg/metrics/proto/delete_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `DeleteMetricRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/delete_metric_request.proto
// file: metrics/proto/requests/delete_metric_request.proto
//
// Request to delete an existing metric definition.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message DeleteMetricRequest {
  // Unique identifier of the metric
  string metric_id = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### delete_metric_response.proto {#delete_metric_response}

**Path**: `pkg/metrics/proto/delete_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `DeleteMetricResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/delete_metric_response.proto
// file: metrics/proto/responses/delete_metric_response.proto
//
// Response returned after deleting a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * DeleteMetricResponse confirms metric deletion.
 */
message DeleteMetricResponse {
  // Whether the delete succeeded
  bool success = 1;

  // Error details if the operation failed
  gcommon.v1.common.Error error = 2;
}

```

---

### delete_provider_request.proto {#delete_provider_request}

**Path**: `pkg/metrics/proto/delete_provider_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `DeleteProviderRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/delete_provider_request.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-9012-3456-789abcdef012

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message DeleteProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to delete
  string provider_id = 2;

  // Optional force deletion (ignore dependencies)
  bool force = 3;

  // Dry run mode - just check what would be deleted
  bool dry_run = 4;
}

```

---

### delete_provider_response.proto {#delete_provider_response}

**Path**: `pkg/metrics/proto/delete_provider_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 86

**Messages** (2): `DeleteProviderResponse`, `DeletionResult`

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
// file: pkg/metrics/proto/responses/delete_provider_response.proto
// file: metrics/proto/responses/delete_provider_response.proto
//
// Delete provider response definitions for metrics module
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
 * DeleteProviderResponse contains the result of deleting a metrics provider.
 */
message DeleteProviderResponse {
  // Success status of the deletion
  bool success = 1;

  // Error information if deletion failed
  gcommon.v1.common.Error error = 2;

  // Provider ID that was deleted
  string provider_id = 3;

  // When the deletion was completed
  google.protobuf.Timestamp deleted_at = 4;

  // Deletion results
  DeletionResult deletion_result = 5;

  // Warnings or informational messages
  repeated string warnings = 6;

  // Backup information (if backup was created)
  BackupInfo backup_info = 7;

  // When scheduled deletion will occur (if grace period is set)
  google.protobuf.Timestamp scheduled_deletion = 8;
}

/**
 * DeletionResult contains information about what was deleted.
 */
message DeletionResult {
  // Whether the provider was actually deleted
  bool provider_deleted = 1;

  // Amount of data that was deleted
  int64 data_deleted_bytes = 2;

  // Number of metrics that were deleted
  int64 metrics_deleted = 3;

  // Number of data points that were deleted
  int64 data_points_deleted = 4;

  // Indices that were deleted
  repeated string deleted_indices = 5;

  // Exports that were stopped
  repeated string stopped_exports = 6;

  // Backups that were deleted
  repeated string deleted_backups = 7;

  // Cleanup strategy that was used
  string cleanup_strategy_used = 8;

  // Time taken for the deletion
  string deletion_duration = 9;

  // What would be deleted (for dry run operations)
  DryRunResult dry_run_result = 10;
}

/**
 * DryRunResult shows what would be deleted in a dry run operation.
 */

```

---

### export_metrics_request.proto {#export_metrics_request}

**Path**: `pkg/metrics/proto/export_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ExportMetricsRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/export_format.proto` →
  [metrics_1](./metrics_1.md#export_format) →
  [queue_1](./queue_1.md#export_format)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/export_metrics_request.proto
// version: 1.1.0
// guid: 2c9c223d-523d-4b0c-aa30-6249240e59d6

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/export_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ExportMetricsRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metrics provider to export from
  string provider_id = 2;

  // Desired export format
  ExportFormat format = 3;

  // Destination URI or path
  string destination = 4;

  // Specific metrics to include (optional)
  repeated string metric_names = 5;

  // Include metadata such as descriptions and units
  bool include_metadata = 6;
}

```

---

### export_metrics_response.proto {#export_metrics_response}

**Path**: `pkg/metrics/proto/export_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ExportMetricsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/export_metrics_response.proto
// version: 1.1.0
// guid: 0d2df1e4-76e3-437b-855e-4dcc2b6f6b9e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ExportMetricsResponse returns the result of a metrics export operation.
 */
message ExportMetricsResponse {
  // Whether the export succeeded
  bool success = 1;

  // Error information if the export failed
  gcommon.v1.common.Error error = 2;

  // Number of records exported
  int64 exported_records = 3;

  // Timestamp when the export completed
  google.protobuf.Timestamp exported_at = 4;

  // Location of the exported data
  string file_url = 5;
}

```

---

### get_alerting_rules_request.proto {#get_alerting_rules_request}

**Path**: `pkg/metrics/proto/get_alerting_rules_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `GetAlertingRulesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_alerting_rules_request.proto
// file: metrics/proto/requests/get_alerting_rules_request.proto
//
// Request message for retrieving alerting rules associated with a metric.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetAlertingRulesRequest {
  // Metric identifier
  string metric_id = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_alerting_rules_response.proto {#get_alerting_rules_response}

**Path**: `pkg/metrics/proto/get_alerting_rules_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetAlertingRulesResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/alerting_rule.proto` →
  [metrics_1](./metrics_1.md#alerting_rule)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_alerting_rules_response.proto
// file: metrics/proto/responses/get_alerting_rules_response.proto
//
// Response message containing alerting rules for a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/alerting_rule.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetAlertingRulesResponse returns configured alerting rules.
 */
message GetAlertingRulesResponse {
  // Alerting rules for the metric
  repeated AlertingRule rules = 1;

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}

```

---

### get_metric_metadata_request.proto {#get_metric_metadata_request}

**Path**: `pkg/metrics/proto/get_metric_metadata_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 48

**Messages** (1): `GetMetricMetadataRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_metric_metadata_request.proto
// file: metrics/proto/requests/get_metric_metadata_request.proto
//
// Request definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetMetricMetadataRequest retrieves metadata for specific metrics.
 */
message GetMetricMetadataRequest {
  // Provider ID to query
  string provider_id = 1;

  // Specific metric names to get metadata for (if empty, get all)
  repeated string metric_names = 2;

  // Namespace to filter by (optional)
  string namespace = 3;

  // Include inactive metrics
  bool include_inactive = 4;

  // Pagination options
  int32 page_size = 5;
  string page_token = 6;

  // Filter by metric type (optional)
  string metric_type = 7;

  // Filter by labels (optional)
  map<string, string> label_filters = 8;

  // Whether to include retention policy information
  bool include_retention_info = 9;

  // Whether to include usage statistics
  bool include_usage_stats = 10;
}

```

---

### get_metric_metadata_response.proto {#get_metric_metadata_response}

**Path**: `pkg/metrics/proto/get_metric_metadata_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 51

**Messages** (1): `GetMetricMetadataResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)
- `pkg/metrics/proto/pagination_info.proto` →
  [metrics_1](./metrics_1.md#pagination_info)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_metric_metadata_response.proto
// file: metrics/proto/responses/get_metric_metadata_response.proto
//
// Response definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_metadata.proto";
import "pkg/metrics/proto/pagination_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetMetricMetadataResponse contains metadata for requested metrics.
 */
message GetMetricMetadataResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Provider ID that handled the request
  string provider_id = 3;

  // Retrieved metadata entries
  repeated MetricMetadata metadata = 4;

  // Pagination information
  PaginationInfo pagination = 5;

  // Total number of matching metrics
  int64 total_count = 6;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 7;

  // Warnings or informational messages
  repeated string warnings = 8;

  // Query execution time in milliseconds
  int64 execution_time_ms = 9;
}

```

---

### get_metric_request.proto {#get_metric_request}

**Path**: `pkg/metrics/proto/get_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `GetMetricRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_metric_request.proto
// file: metrics/proto/requests/get_metric_request.proto
//
// Request message for retrieving a metric by ID.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetMetricRequest {
  // Unique metric identifier
  string metric_id = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_metric_response.proto {#get_metric_response}

**Path**: `pkg/metrics/proto/get_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetMetricResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_metric_response.proto
// file: metrics/proto/responses/get_metric_response.proto
//
// Response containing a metric definition and data.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetMetricResponse returns metric data.
 */
message GetMetricResponse {
  // Metric data requested
  MetricData metric = 1;

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}

```

---

### get_metrics_request.proto {#get_metrics_request}

**Path**: `pkg/metrics/proto/get_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 86

**Messages** (3): `GetMetricsRequest`, `SecondarySortField`, `OutputOptions`

**Imports** (10):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination_options.proto` →
  [common](./common.md#pagination_options)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/sort_direction.proto` → [common](./common.md#sort_direction)
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/metric_aggregation.proto` →
  [metrics_1](./metrics_1.md#metric_aggregation)
- `pkg/metrics/proto/metric_filter.proto` →
  [metrics_1](./metrics_1.md#metric_filter)
- `pkg/metrics/proto/numeric_format.proto` →
  [metrics_1](./metrics_1.md#numeric_format)
- `pkg/metrics/proto/response_compression.proto` →
  [metrics_api_2](./metrics_api_2.md#response_compression)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/metrics/proto/get_metrics_request.proto
// version: 1.1.0
// guid: f58f7623-0d53-495a-b959-3ed3770d0b39

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination_options.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/sort_direction.proto";
import "pkg/common/proto/time_range.proto";
import "pkg/metrics/proto/metric_aggregation.proto";
import "pkg/metrics/proto/metric_filter.proto";
import "pkg/metrics/proto/numeric_format.proto";
import "pkg/metrics/proto/response_compression.proto";
import "pkg/metrics/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetMetricsRequest represents a request to retrieve metrics data.
 * Provides filtering, aggregation, and pagination capabilities.
 */
message GetMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter to determine which metrics to retrieve
  MetricFilter filter = 2;

  // Time range for the request
  TimeRange time_range = 3;

  // Aggregation options for the metrics
  MetricAggregation aggregation = 4;

  // Pagination options
  gcommon.v1.common.PaginationOptions pagination = 5;

  // Optional provider ID to query
  string provider_id = 6;

  // Output format options
  OutputOptions output_options = 7;

  // Whether to include metadata with results
  bool include_metadata = 8;

  // Maximum number of metrics to return
  int32 limit = 9;
}

/**
 * SecondarySortField defines additional sort criteria.
 */
message SecondarySortField {
  string field = 1;
  gcommon.v1.common.SortDirection direction = 2;
}

/**
 * OutputOptions configures the format of returned data.
 */
message OutputOptions {
  // Format for numeric values
  NumericFormat numeric_format = 1;

  // Whether to include timestamps
  bool include_timestamps = 2;

  // Whether to include labels
  bool include_labels = 3;

  // Compression for large responses
  ResponseCompression compression = 4;

  // Whether to flatten nested structures
  bool flatten_response = 5;

  // Time zone for timestamp formatting
  string timezone = 6;
}

```

---

### get_metrics_response.proto {#get_metrics_response}

**Path**: `pkg/metrics/proto/get_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 57

**Messages** (1): `GetMetricsResponse`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)
- `pkg/metrics/proto/pagination_info.proto` →
  [metrics_1](./metrics_1.md#pagination_info)
- `pkg/metrics/proto/query_stats.proto` → [database](./database.md#query_stats)
  → [metrics_2](./metrics_2.md#query_stats)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_metrics_response.proto
// file: metrics/proto/responses/get_metrics_response.proto
//
// Get metrics response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/time_range.proto";
import "pkg/metrics/proto/metric_data.proto";
import "pkg/metrics/proto/metric_metadata.proto";
import "pkg/metrics/proto/pagination_info.proto";
import "pkg/metrics/proto/query_stats.proto";
import "pkg/metrics/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetMetricsResponse contains the retrieved metrics data.
 */
message GetMetricsResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Retrieved metrics data
  repeated MetricData metrics = 3;

  // Metadata for the metrics (if requested)
  repeated MetricMetadata metadata = 4;

  // Pagination information
  PaginationInfo pagination = 5;

  // Query execution statistics
  QueryStats stats = 6;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 7;

  // Time range covered by the response
  TimeRange time_range = 8;

  // Warnings or informational messages
  repeated string warnings = 9;

  // Provider that handled the request
  string provider_id = 10;
}

```

---

### get_metrics_summary_request.proto {#get_metrics_summary_request}

**Path**: `pkg/metrics/proto/get_metrics_summary_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 71

**Messages** (2): `GetMetricsSummaryRequest`, `SummaryOptions`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/metric_filter.proto` →
  [metrics_1](./metrics_1.md#metric_filter)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_metrics_summary_request.proto
// file: metrics/proto/requests/get_metrics_summary_request.proto
//
// Get metrics summary request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/time_range.proto";
import "pkg/metrics/proto/metric_filter.proto";
import "pkg/metrics/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetMetricsSummaryRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Optional filter to limit which metrics to include in summary
  MetricFilter filter = 2;

  // Time range for the summary
  TimeRange time_range = 3;

  // What summary information to include
  SummaryOptions options = 4;

  // Optional provider ID to query
  string provider_id = 5;

  // Whether to include provider-level statistics
  bool include_provider_stats = 6;

  // Whether to include health status information
  bool include_health_status = 7;
}

/**
 * SummaryOptions configures what information to include in the summary.
 */
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
  int32 top_metrics_limit = 8;
}

```

---

### get_metrics_summary_response.proto {#get_metrics_summary_response}

**Path**: `pkg/metrics/proto/get_metrics_summary_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 150

**Messages** (8): `GetMetricsSummaryResponse`, `MetricsSummary`,
`MetricTypeCounts`, `MetricInfo`, `MetricsHealthInfo`, `RetentionInfo`,
`ExportStatus`, `ExporterStatus`

**Imports** (11):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/error_stats.proto` →
  [metrics_1](./metrics_1.md#error_stats)
- `pkg/metrics/proto/health_status.proto` → [common](./common.md#health_status)
  → [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)
- `pkg/metrics/proto/performance_stats.proto` →
  [metrics_1](./metrics_1.md#performance_stats) →
  [web](./web.md#performance_stats)
- `pkg/metrics/proto/provider_summary.proto` →
  [metrics_2](./metrics_2.md#provider_summary)
- `pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto` →
  [metrics_config](./metrics_config.md#retention_policy_retentionpolicyconfig)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/top_metrics.proto` →
  [metrics_2](./metrics_2.md#top_metrics)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_metrics_summary_response.proto
// file: metrics/proto/responses/get_metrics_summary_response.proto
//
// Get metrics summary response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/time_range.proto";
import "pkg/metrics/proto/error_stats.proto";
import "pkg/metrics/proto/health_status.proto";
import "pkg/metrics/proto/performance_stats.proto";
import "pkg/metrics/proto/provider_summary.proto";
import "pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto";
import "pkg/metrics/proto/time_range.proto";
import "pkg/metrics/proto/top_metrics.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetMetricsSummaryResponse contains summary information about metrics data.
 */
message GetMetricsSummaryResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Summary information organized by category
  MetricsSummary summary = 3;

  // Provider-level statistics (if requested)
  repeated ProviderSummary provider_summaries = 4;

  // Health status information (if requested)
  MetricsHealthInfo health_status = 5;

  // When the summary was generated
  google.protobuf.Timestamp generated_at = 6;

  // Time range covered by the summary
  TimeRange time_range = 7;

  // Warnings or informational messages
  repeated string warnings = 8;
}

/**
 * MetricsSummary contains aggregate information about metrics.
 */
message MetricsSummary {
  // Total number of unique metrics
  int64 total_metrics = 1;

  // Total number of data points
  int64 total_data_points = 2;

  // Total data volume (bytes)
  int64 total_data_volume_bytes = 3;

  // Metrics by type
  MetricTypeCounts type_counts = 4;

  // Performance statistics
  PerformanceStats performance = 5;

  // Error statistics
  ErrorStats errors = 6;

  // Top metrics by various criteria
  TopMetrics top_metrics = 7;

  // Retention information
  RetentionInfo retention = 8;

  // Export status information
  ExportStatus export_status = 9;
}

/**
 * MetricTypeCounts breaks down metrics by type.
 */
message MetricTypeCounts {
  int64 counter_count = 1;
  int64 gauge_count = 2;
  int64 histogram_count = 3;
  int64 summary_count = 4;
  int64 timer_count = 5;
  int64 custom_count = 6;
}

/**
 * MetricInfo contains basic information about a metric.
 */
message MetricInfo {
  string name = 1;
  string metric_type = 2;
  int64 data_points = 3;
  int64 data_volume_bytes = 4;
  double error_rate = 5;
  google.protobuf.Timestamp last_updated = 6;
}

/**
 * MetricsHealthInfo contains health information about the metrics system.
 */
message MetricsHealthInfo {
  HealthStatus overall_status = 1;
  repeated string health_checks = 2;
  repeated string warnings = 3;
  google.protobuf.Timestamp last_check = 4;
}

/**
 * RetentionInfo contains information about data retention.
 */
message RetentionInfo {
  int64 total_retained_bytes = 1;
  int64 total_purged_bytes = 2;
  string oldest_data_age = 3;
  repeated RetentionPolicyConfig policies = 4;
}

/**
 * ExportStatus contains information about data export operations.
 */
message ExportStatus {
  int64 total_exported_metrics = 1;
  int64 failed_exports = 2;
  google.protobuf.Timestamp last_export = 3;
  repeated ExporterStatus exporters = 4;
}

/**
 * ExporterStatus contains status information for a specific exporter.
 */
message ExporterStatus {
  string exporter_id = 1;
  string exporter_type = 2;
  string status = 3;
  int64 exported_count = 4;
  google.protobuf.Timestamp last_export = 5;
}

```

---

### get_provider_stats_request.proto {#get_provider_stats_request}

**Path**: `pkg/metrics/proto/get_provider_stats_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 70

**Messages** (2): `GetProviderStatsRequest`, `StatsOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/metrics/proto/get_provider_stats_request.proto
// version: 1.1.0
// guid: e5f6a7b8-c9d0-1234-5678-9abcdef01234

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetProviderStatsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to get stats for
  string provider_id = 2;

  // Time range for statistics
  TimeRange time_range = 3;

  // What statistics to include
  StatsOptions options = 4;

  // Granularity for time-series statistics
  string granularity = 5; // e.g., "1m", "5m", "1h"

  // Whether to include real-time metrics
  bool include_realtime = 6;
}

/**
 * StatsOptions configures what statistics to include.
 */
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
  int32 top_metrics_limit = 9;

  // Include trend analysis
  bool include_trends = 10;
}

```

---

### get_provider_stats_response.proto {#get_provider_stats_response}

**Path**: `pkg/metrics/proto/get_provider_stats_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 395

**Messages** (25): `GetProviderStatsResponse`, `ProviderStatistics`,
`PerformanceDataPoint`, `ResourceUsageStats`, `MemoryUsage`, `CPUUsage`,
`DiskUsage`, `NetworkUsage`, `ResourceDataPoint`, `ErrorTypeStats`,
`ErrorEntry`, `ErrorDataPoint`, `DataVolumeStats`, `DataVolumeDataPoint`,
`ExportStats`, `ExportDestinationStats`, `HealthStatusEntry`,
`ConfigurationSummary`, `SecuritySummary`, `MetricSummary`, `TrendAnalysis`,
`PerformanceTrend`, `ResourceUsageTrend`, `ErrorTrend`, `DataVolumeTrend`

**Imports** (10):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/error_stats.proto` →
  [metrics_1](./metrics_1.md#error_stats)
- `pkg/metrics/proto/performance_stats.proto` →
  [metrics_1](./metrics_1.md#performance_stats) →
  [web](./web.md#performance_stats)
- `pkg/metrics/proto/provider_info.proto` →
  [metrics_1](./metrics_1.md#provider_info)
- `pkg/metrics/proto/resource_limits_summary.proto` →
  [metrics_2](./metrics_2.md#resource_limits_summary)
- `pkg/metrics/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/metrics/proto/top_metrics.proto` →
  [metrics_2](./metrics_2.md#top_metrics)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_provider_stats_response.proto
// file: metrics/proto/responses/get_provider_stats_response.proto
//
// Get provider stats response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/time_range.proto";
import "pkg/metrics/proto/error_stats.proto";
import "pkg/metrics/proto/performance_stats.proto";
import "pkg/metrics/proto/provider_info.proto";
import "pkg/metrics/proto/resource_limits_summary.proto";
import "pkg/metrics/proto/time_range.proto";
import "pkg/metrics/proto/top_metrics.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetProviderStatsResponse contains statistics for a metrics provider.
 */
message GetProviderStatsResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Provider ID these stats are for
  string provider_id = 3;

  // Comprehensive provider statistics
  ProviderStatistics statistics = 4;

  // When the statistics were generated
  google.protobuf.Timestamp generated_at = 5;

  // Time range covered by the statistics
  TimeRange time_range = 6;

  // Warnings or informational messages
  repeated string warnings = 7;
}

/**
 * ProviderStatistics contains comprehensive statistics for a provider.
 */
message ProviderStatistics {
  // Basic provider information
  ProviderInfo provider_info = 1;

  // Performance statistics
  PerformanceStats performance = 2;

  // Resource usage statistics
  ResourceUsageStats resource_usage = 3;

  // Error statistics
  ErrorStats errors = 4;

  // Data volume statistics
  DataVolumeStats data_volume = 5;

  // Export statistics
  ExportStats exports = 6;

  // Health status history
  repeated HealthStatusEntry health_history = 7;

  // Configuration summary
  ConfigurationSummary config = 8;

  // Top metrics
  TopMetrics top_metrics = 9;

  // Trend analysis
  TrendAnalysis trends = 10;
}

/**
 * PerformanceDataPoint represents a single performance measurement.
 */
message PerformanceDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  double ops_per_second = 2;
  double latency_ms = 3;
  double throughput_bytes_per_second = 4;
}

/**
 * ResourceUsageStats contains resource usage statistics.
 */
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
  repeated ResourceDataPoint resource_timeseries = 5;
}

/**
 * MemoryUsage contains memory usage information.
 */
message MemoryUsage {
  // Currently used memory (bytes)
  int64 used_bytes = 1;

  // Memory limit (bytes)
  int64 limit_bytes = 2;

  // Usage percentage
  double usage_percent = 3;

  // Peak memory usage (bytes)
  int64 peak_bytes = 4;
}

/**
 * CPUUsage contains CPU usage information.
 */
message CPUUsage {
  // Current CPU usage (percentage)
  double current_percent = 1;

  // Average CPU usage (percentage)
  double avg_percent = 2;

  // Peak CPU usage (percentage)
  double peak_percent = 3;
}

/**
 * DiskUsage contains disk usage information.
 */
message DiskUsage {
  // Currently used disk space (bytes)
  int64 used_bytes = 1;

  // Disk space limit (bytes)
  int64 limit_bytes = 2;

  // Usage percentage
  double usage_percent = 3;

  // I/O operations per second
  double iops = 4;
}

/**
 * NetworkUsage contains network usage information.
 */
message NetworkUsage {
  // Bytes received per second
  int64 bytes_in_per_second = 1;

  // Bytes sent per second
  int64 bytes_out_per_second = 2;

  // Packets received per second
  int64 packets_in_per_second = 3;

  // Packets sent per second
  int64 packets_out_per_second = 4;
}

/**
 * ResourceDataPoint represents a single resource usage measurement.
 */
message ResourceDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  double memory_usage_percent = 2;
  double cpu_usage_percent = 3;
  double disk_usage_percent = 4;
  int64 network_bytes_per_second = 5;
}

/**
 * ErrorTypeStats contains statistics for a specific error type.
 */
message ErrorTypeStats {
  string error_type = 1;
  int64 count = 2;
  double rate = 3;
  double percentage = 4;
}

/**
 * ErrorEntry represents a single error occurrence.
 */
message ErrorEntry {
  google.protobuf.Timestamp timestamp = 1;
  string error_type = 2;
  string error_message = 3;
  int32 count = 4;
}

/**
 * ErrorDataPoint represents error statistics at a point in time.
 */
message ErrorDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 error_count = 2;
  double error_rate = 3;
}

/**
 * DataVolumeStats contains data volume statistics.
 */
message DataVolumeStats {
  // Total data stored (bytes)
  int64 total_bytes = 1;

  // Total number of metrics
  int64 total_metrics = 2;

  // Total number of data points
  int64 total_data_points = 3;

  // Data ingestion rate (bytes per second)
  double ingestion_rate_bytes_per_second = 4;

  // Data points ingestion rate (points per second)
  double ingestion_rate_points_per_second = 5;

  // Compression ratio
  double compression_ratio = 6;

  // Time-series data volume
  repeated DataVolumeDataPoint volume_timeseries = 7;
}

/**
 * DataVolumeDataPoint represents data volume at a point in time.
 */
message DataVolumeDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 total_bytes = 2;
  int64 total_metrics = 3;
  int64 total_data_points = 4;
  double ingestion_rate = 5;
}

/**
 * ExportStats contains export-related statistics.
 */
message ExportStats {
  // Total exported metrics
  int64 total_exported_metrics = 1;

  // Total exported data points
  int64 total_exported_data_points = 2;

  // Export rate (metrics per second)
  double export_rate_metrics_per_second = 3;

  // Failed exports
  int64 failed_exports = 4;

  // Export success rate
  double export_success_rate = 5;

  // Exports by destination
  repeated ExportDestinationStats export_destinations = 6;

  // Last successful export
  google.protobuf.Timestamp last_successful_export = 7;
}

/**
 * ExportDestinationStats contains statistics for a specific export destination.
 */
message ExportDestinationStats {
  string destination_id = 1;
  string destination_type = 2;
  int64 exported_metrics = 3;
  int64 failed_exports = 4;
  double success_rate = 5;
  google.protobuf.Timestamp last_export = 6;
}

/**
 * HealthStatusEntry represents a health status at a point in time.
 */
message HealthStatusEntry {
  google.protobuf.Timestamp timestamp = 1;
  string health_status = 2;
  string status_message = 3;
}

/**
 * ConfigurationSummary contains a summary of the provider configuration.
 */
message ConfigurationSummary {
  // Number of configured exporters
  int32 exporter_count = 1;

  // Security settings summary
  SecuritySummary security = 2;

  // Resource limits summary
  ResourceLimitsSummary resource_limits = 3;

  // Configuration version
  string config_version = 4;
}

/**
 * SecuritySummary contains security configuration summary.
 */
message SecuritySummary {
  bool auth_enabled = 1;
  bool tls_enabled = 2;
  repeated string auth_methods = 3;
}

/**
 * MetricSummary contains summary information about a metric.
 */
message MetricSummary {
  string name = 1;
  string type = 2;
  int64 data_points = 3;
  int64 data_volume_bytes = 4;
  double error_rate = 5;
  google.protobuf.Timestamp last_updated = 6;
}

/**
 * TrendAnalysis contains trend analysis for the provider.
 */
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

/**
 * PerformanceTrend contains performance trend information.
 */
message PerformanceTrend {
  string latency_trend = 1; // "improving", "degrading", "stable"
  string throughput_trend = 2; // "increasing", "decreasing", "stable"
  double trend_confidence = 3; // 0.0 to 1.0
}

/**
 * ResourceUsageTrend contains resource usage trend information.
 */
message ResourceUsageTrend {
  string memory_trend = 1; // "increasing", "decreasing", "stable"
  string cpu_trend = 2; // "increasing", "decreasing", "stable"
  string disk_trend = 3; // "increasing", "decreasing", "stable"
  double trend_confidence = 4;
}

/**
 * ErrorTrend contains error trend information.
 */
message ErrorTrend {
  string error_rate_trend = 1; // "improving", "worsening", "stable"
  double trend_confidence = 2;
  repeated string emerging_error_types = 3;
}

/**
 * DataVolumeTrend contains data volume trend information.
 */
message DataVolumeTrend {
  string volume_trend = 1; // "increasing", "decreasing", "stable"
  string ingestion_trend = 2; // "increasing", "decreasing", "stable"
  double trend_confidence = 3;
}

```

---

### get_stats_request.proto {#get_stats_request}

**Path**: `pkg/metrics/proto/get_stats_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetStatsRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/timestamp_range.proto` →
  [metrics_2](./metrics_2.md#timestamp_range) →
  [queue_2](./queue_2.md#timestamp_range)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/get_stats_request.proto
// file: metrics/proto/requests/get_stats_request.proto
//
// Request for retrieving metric statistics over a time range.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/timestamp_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message GetStatsRequest {
  // Metric name or ID to query
  string metric = 1;

  // Time range for stats
  TimestampRange range = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### get_stats_response.proto {#get_stats_response}

**Path**: `pkg/metrics/proto/get_stats_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetStatsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/query_stats.proto` → [database](./database.md#query_stats)
  → [metrics_2](./metrics_2.md#query_stats)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/get_stats_response.proto
// file: metrics/proto/responses/get_stats_response.proto
//
// Response containing metric statistics over a time range.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/query_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * GetStatsResponse returns statistics for a metric.
 */
message GetStatsResponse {
  // Statistics for the query
  QueryStats stats = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/metrics/proto/health_check_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/health_check_request.proto
// version: 1.0.0
// guid: ffa1c922-b413-4b2d-a7fd-0d58fcd0b048
//
// HealthCheckRequest for the metrics module

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message HealthCheckRequest {
  // Metrics subsystem name (e.g., "prometheus").
  string subsystem = 1;

  // Request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### health_check_response.proto {#health_check_response}

**Path**: `pkg/metrics/proto/health_check_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `HealthCheckResponse`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/health_check_response.proto
// version: 1.0.0
// guid: 2d9c7ce3-2e5b-42d7-9473-70bef7518cdd
//
// HealthCheckResponse for the metrics module
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * HealthCheckResponse contains the result of a metrics subsystem health check.
 */
message HealthCheckResponse {
  // Health status of the subsystem.
  gcommon.v1.common.HealthStatus status = 1;

  // Time taken to execute the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Optional human-readable message.
  string message = 3;

  // Error details if unhealthy.
  gcommon.v1.common.Error error = 4 [lazy = true];
}

```

---

### import_metrics_request.proto {#import_metrics_request}

**Path**: `pkg/metrics/proto/import_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `ImportMetricsRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/import_metrics_request.proto
// file: metrics/proto/requests/import_metrics_request.proto
//
// Request message for importing multiple metrics.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ImportMetricsRequest {
  // Metrics to import
  repeated MetricData metrics = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### import_metrics_response.proto {#import_metrics_response}

**Path**: `pkg/metrics/proto/import_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `ImportMetricsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/import_metrics_response.proto
// file: metrics/proto/responses/import_metrics_response.proto
//
// Response returned after importing metrics.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ImportMetricsResponse reports the result of a batch import.
 */
message ImportMetricsResponse {
  // Number of metrics successfully imported
  int32 imported_count = 1;

  // Error information if the import failed
  gcommon.v1.common.Error error = 2;
}

```

---

### list_metrics_request.proto {#list_metrics_request}

**Path**: `pkg/metrics/proto/list_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `ListMetricsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/list_metrics_request.proto
// version: 1.0.0
// guid: a5ae698c-a783-4005-b054-167c31d44c8b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ListMetricsRequest requests a paginated list of metrics.
 */
message ListMetricsRequest {
  // Pagination information
  gcommon.v1.common.Pagination pagination = 1;

  // Optional name filter
  string name_filter = 2;
}

```

---

### list_metrics_response.proto {#list_metrics_response}

**Path**: `pkg/metrics/proto/list_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `ListMetricsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_metadata.proto` →
  [metrics_1](./metrics_1.md#metric_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/list_metrics_response.proto
// file: metrics/proto/responses/list_metrics_response.proto
//
// Response containing a list of metric metadata.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ListMetricsResponse lists available metrics.
 */
message ListMetricsResponse {
  // Available metrics
  repeated MetricMetadata metrics = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### list_providers_request.proto {#list_providers_request}

**Path**: `pkg/metrics/proto/list_providers_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 65

**Messages** (2): `ListProvidersRequest`, `ProviderFilter`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination_options.proto` →
  [common](./common.md#pagination_options)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/provider_sort_field.proto` →
  [metrics_1](./metrics_1.md#provider_sort_field)

#### Source Code

```protobuf
// file: pkg/metrics/proto/list_providers_request.proto
// version: 1.2.0
// guid: 8f89d21d-fa76-4c1a-b6c7-d10ee9c708a7

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination_options.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/provider_sort_field.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ListProvidersRequest represents a request to list metrics providers.
 */
message ListProvidersRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter options for the list
  ProviderFilter filter = 2;

  // Pagination options
  gcommon.v1.common.PaginationOptions pagination = 3;

  // Whether to include detailed status information
  bool include_status = 4;

  // Whether to include configuration details
  bool include_config = 5;

  // Whether to include statistics
  bool include_stats = 6;
}

/**
 * ProviderFilter contains filtering options for listing providers.
 */
message ProviderFilter {
  // Filter by provider type
  repeated string provider_types = 1;

  // Filter by provider state
  repeated string states = 2;

  // Filter by tags
  map<string, string> tags = 3;

  // Filter by name pattern (regex)
  string name_pattern = 4;

  // Filter by health status
  repeated string health_statuses = 5;

  // Filter providers created after this time
  string created_after = 6;

  // Filter providers created before this time
  string created_before = 7;
}

```

---

### list_providers_response.proto {#list_providers_response}

**Path**: `pkg/metrics/proto/list_providers_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 100

**Messages** (4): `ListProvidersResponse`, `ProviderConfigSummary`,
`ProviderStats`, `ResourceUsage`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/pagination_info.proto` →
  [metrics_1](./metrics_1.md#pagination_info)
- `pkg/metrics/proto/provider_info.proto` →
  [metrics_1](./metrics_1.md#provider_info)
- `pkg/metrics/proto/provider_summary.proto` →
  [metrics_2](./metrics_2.md#provider_summary)
- `pkg/metrics/proto/resource_limits_summary.proto` →
  [metrics_2](./metrics_2.md#resource_limits_summary)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/list_providers_response.proto
// file: metrics/proto/responses/list_providers_response.proto
//
// List providers response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/pagination_info.proto";
import "pkg/metrics/proto/provider_info.proto";
import "pkg/metrics/proto/provider_summary.proto";
import "pkg/metrics/proto/resource_limits_summary.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ListProvidersResponse contains the list of metrics providers.
 */
message ListProvidersResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // List of providers
  repeated ProviderInfo providers = 3;

  // Pagination information
  PaginationInfo pagination = 4;

  // Summary statistics about the providers
  ProviderSummary summary = 5;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 6;
}

/**
 * ProviderConfigSummary contains a summary of provider configuration.
 */
message ProviderConfigSummary {
  // Number of configured exporters
  int32 exporter_count = 1;

  // Whether security is enabled
  bool security_enabled = 2;

  // Resource limits summary
  ResourceLimitsSummary resource_limits = 3;

  // Export destinations
  repeated string export_destinations = 4;
}

/**
 * ProviderStats contains statistics for a provider.
 */
message ProviderStats {
  // Number of metrics managed
  int64 metrics_count = 1;

  // Number of data points
  int64 data_points_count = 2;

  // Data volume (bytes)
  int64 data_volume_bytes = 3;

  // Operations per second
  double operations_per_second = 4;

  // Error rate
  double error_rate = 5;

  // Resource usage
  ResourceUsage resource_usage = 6;
}

/**
 * ResourceUsage contains current resource usage.
 */
message ResourceUsage {
  // Current memory usage (bytes)
  int64 memory_used_bytes = 1;

  // Current CPU usage (percentage)
  double cpu_used_percent = 2;

  // Current disk usage (bytes)
  int64 disk_used_bytes = 3;

  // Network bandwidth usage (bytes/sec)
  int64 network_bandwidth_bytes_per_sec = 4;
}

```

---

### query_metrics_request.proto {#query_metrics_request}

**Path**: `pkg/metrics/proto/query_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 55

**Messages** (2): `QueryMetricsRequest`, `QueryOutputOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_query.proto` →
  [metrics_1](./metrics_1.md#metric_query)

#### Source Code

```protobuf
// file: pkg/metrics/proto/query_metrics_request.proto
// version: 1.2.0
// guid: b1c2d3e4-f5g6-7890-h1i2-j3k4l5m6n7o8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_query.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message QueryMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // The metric query to execute
  MetricQuery query = 2;

  // Optional query timeout in seconds
  int32 timeout_seconds = 3;

  // Whether to return query execution plan (for debugging)
  bool include_query_plan = 4;

  // Whether to return only metadata without actual values (for schema discovery)
  bool metadata_only = 5;

  // Output format preferences
  QueryOutputOptions output_options = 6;
}

/**
 * QueryOutputOptions specifies how query results should be formatted.
 */
message QueryOutputOptions {
  // Whether to include timestamps in results
  bool include_timestamps = 1;

  // Whether to include label information
  bool include_labels = 2;

  // Whether to compress/optimize output for network transfer
  bool compress_output = 3;

  // Maximum precision for numeric values (decimal places)
  int32 numeric_precision = 4;

  // Whether to include statistics about the query execution
  bool include_statistics = 5;
}

```

---

### query_metrics_response.proto {#query_metrics_response}

**Path**: `pkg/metrics/proto/query_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 76

**Messages** (2): `QueryMetricsResponse`, `QueryStatistics`

**Imports** (6):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)
- `pkg/metrics/proto/metric_query.proto` →
  [metrics_1](./metrics_1.md#metric_query)

#### Source Code

```protobuf
// file: pkg/metrics/proto/query_metrics_response.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-7890-1234-567890abcdef

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/metric_data.proto";
import "pkg/metrics/proto/metric_query.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * QueryMetricsResponse contains the results of a metric query.
 */
message QueryMetricsResponse {
  // Success status of the query
  bool success = 1;

  // Error information if query failed
  gcommon.v1.common.Error error = 2;

  // Query results organized as metric series
  repeated MetricSeries series = 3;

  // Query execution statistics
  QueryStatistics statistics = 4;

  // Query execution plan (if requested)
  QueryPlan query_plan = 5;

  // Warnings or informational messages about the query
  repeated string warnings = 6;

  // Pagination token for retrieving more results
  string next_page_token = 7;

  // Total number of results available (for pagination)
  int64 total_results = 8;
}

/**
 * QueryStatistics provides information about query execution.
 */
message QueryStatistics {
  // Total execution time
  google.protobuf.Duration execution_time = 1;

  // Number of data points processed
  int64 data_points_processed = 2;

  // Number of metrics examined
  int64 metrics_examined = 3;

  // Number of series returned
  int64 series_returned = 4;

  // Memory used during query execution (bytes)
  int64 memory_used_bytes = 5;

  // Storage backends queried
  repeated string storage_backends_used = 6;

  // Cache hit rate (0.0 to 1.0)
  double cache_hit_rate = 7;

  // When the query was executed
  google.protobuf.Timestamp query_time = 8;
}

```

---

### record_counter_request.proto {#record_counter_request}

**Path**: `pkg/metrics/proto/record_counter_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `RecordCounterRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/record_counter_request.proto
// file: metrics/proto/requests/record_counter_request.proto
//
// Record counter request definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordCounterRequest is used to record or increment a counter metric.
 */
message RecordCounterRequest {
  // Metric name (e.g., "http_requests_total")
  string name = 1;

  // Value to add to the counter (default: 1.0)
  double value = 2;

  // Labels for metric dimensions
  map<string, string> labels = 3;

  // Help text describing the metric
  string help = 4;

  // Metric unit (e.g., "requests", "bytes")
  string unit = 5;

  // Sample rate (0.0-1.0, used for sampling)
  double sample_rate = 6;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 7;
}

```

---

### record_counter_response.proto {#record_counter_response}

**Path**: `pkg/metrics/proto/record_counter_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `RecordCounterResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/counter_metric.proto` →
  [metrics_1](./metrics_1.md#counter_metric)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/record_counter_response.proto
// file: metrics/proto/responses/record_counter_response.proto
//
// Record counter response definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/counter_metric.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message RecordCounterResponse {
  // Whether the operation was successful
  bool success = 1;

  // The recorded counter metric with updated value
  CounterMetric metric = 2;

  // Timestamp when the metric was recorded
  google.protobuf.Timestamp recorded_at = 3;

  // Error information if operation failed
  gcommon.v1.common.Error error = 4;

  // Response metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 5;
}

```

---

### record_gauge_request.proto {#record_gauge_request}

**Path**: `pkg/metrics/proto/record_gauge_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `RecordGaugeRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/gauge_operation.proto` →
  [metrics_1](./metrics_1.md#gauge_operation)

#### Source Code

```protobuf
// file: pkg/metrics/proto/record_gauge_request.proto
// version: 1.1.0
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/gauge_operation.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordGaugeRequest is used to set or update a gauge metric value.
 * Gauges can increase, decrease, or be set to specific values.
 */
message RecordGaugeRequest {
  // Metric name (e.g., "memory_usage_bytes", "cpu_usage_percent")
  string name = 1;

  // Value to set the gauge to
  double value = 2;

  // Labels for metric dimensions
  map<string, string> labels = 3;

  // Help text describing the metric
  string help = 4;

  // Metric unit (e.g., "bytes", "percent", "connections")
  string unit = 5;

  // Optional timestamp when the measurement was taken
  google.protobuf.Timestamp timestamp = 6;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 7;

  // Operation type for the gauge
  GaugeOperation operation = 8;
}

```

---

### record_gauge_response.proto {#record_gauge_response}

**Path**: `pkg/metrics/proto/record_gauge_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 43

**Messages** (1): `RecordGaugeResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/gauge_metric.proto` →
  [metrics_1](./metrics_1.md#gauge_metric)
- `pkg/metrics/proto/recording_stats.proto` →
  [metrics_2](./metrics_2.md#recording_stats)

#### Source Code

```protobuf
// file: pkg/metrics/proto/record_gauge_response.proto
// version: 1.2.0
// guid: c1d2e3f4-g5h6-7890-i1j2-k3l4m5n6o7p8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/gauge_metric.proto";
import "pkg/metrics/proto/recording_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordGaugeResponse is returned after recording a gauge metric.
 */
message RecordGaugeResponse {
  // Whether the operation was successful
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // The recorded gauge metric with updated value
  GaugeMetric metric = 3;

  // Previous value of the gauge (if applicable)
  double previous_value = 4;

  // Timestamp when the gauge was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Whether this was a new gauge or an update to existing
  bool is_new_metric = 6;

  // Processing statistics
  RecordingStats stats = 7;
}

```

---

### record_histogram_request.proto {#record_histogram_request}

**Path**: `pkg/metrics/proto/record_histogram_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 50

**Messages** (1): `RecordHistogramRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/record_histogram_request.proto
// file: metrics/proto/requests/record_histogram_request.proto
//
// Request definitions for metrics module

//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message RecordHistogramRequest {
  // Metric name (e.g., "request_duration_seconds", "response_size_bytes")
  string name = 1;

  // Value to observe/record in the histogram
  double value = 2;

  // Labels for metric dimensions
  map<string, string> labels = 3;

  // Help text describing the metric
  string help = 4;

  // Metric unit (e.g., "seconds", "bytes", "milliseconds")
  string unit = 5;

  // Histogram bucket configuration (if not already defined)
  repeated double buckets = 6;

  // Optional timestamp when the observation was made
  google.protobuf.Timestamp timestamp = 7;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 8;

  // Optional sample weight (for weighted observations)
  double sample_weight = 9;

  // Whether to create the histogram if it doesn't exist
  bool create_if_missing = 10;
}

```

---

### record_histogram_response.proto {#record_histogram_response}

**Path**: `pkg/metrics/proto/record_histogram_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 85

**Messages** (3): `RecordHistogramResponse`, `BucketInfo`, `HistogramStats`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/histogram_metric.proto` →
  [metrics_1](./metrics_1.md#histogram_metric)
- `pkg/metrics/proto/recording_stats.proto` →
  [metrics_2](./metrics_2.md#recording_stats)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/record_histogram_response.proto
// file: metrics/proto/responses/record_histogram_response.proto
//
// Response definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/histogram_metric.proto";
import "pkg/metrics/proto/recording_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordHistogramResponse is returned after recording a histogram observation.
 */
message RecordHistogramResponse {
  // Whether the operation was successful
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // The histogram metric with updated bucket counts
  HistogramMetric metric = 3;

  // Current histogram statistics
  HistogramStats current_stats = 4;

  // Timestamp when the observation was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Whether this was a new histogram or an update to existing
  bool is_new_metric = 6;

  // Bucket that the observation fell into
  BucketInfo affected_bucket = 7;

  // Processing statistics
  RecordingStats recording_stats = 8;
}

/**
 * BucketInfo provides information about a histogram bucket.
 */
message BucketInfo {
  // Upper bound of the bucket
  double upper_bound = 1;

  // Count in this bucket after the observation
  uint64 count = 2;

  // Bucket index
  int32 bucket_index = 3;
}

/**
 * HistogramStats provides current statistics for a histogram.
 */
message HistogramStats {
  // Total number of observations
  uint64 total_count = 1;

  // Sum of all observed values
  double total_sum = 2;

  // Mean value
  double mean = 3;

  // Minimum observed value
  double min_value = 4;

  // Maximum observed value
  double max_value = 5;

  // Standard deviation (if calculated)
  double std_deviation = 6;
}

```

---

### record_metric_request.proto {#record_metric_request}

**Path**: `pkg/metrics/proto/record_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 55

**Messages** (2): `RecordMetricRequest`, `BatchContext`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/record_metric_request.proto
// file: metrics/proto/requests/record_metric_request.proto
//
// Record metric request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message RecordMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // The metric data to record
  MetricData metric = 2;

  // Optional provider ID to use for recording
  string provider_id = 3;

  // Whether to validate the metric before recording
  bool validate = 4;

  // Timestamp override (if not provided, current time is used)
  google.protobuf.Timestamp timestamp = 5;

  // Batch context information (if this is part of a batch operation)
  BatchContext batch_context = 6;
}

/**
 * BatchContext provides information when this request is part of a batch operation.
 */
message BatchContext {
  // Unique batch ID
  string batch_id = 1;

  // Position in the batch (0-based)
  int32 batch_position = 2;

  // Total size of the batch
  int32 batch_size = 3;

  // Whether this is the last item in the batch
  bool is_last = 4;
}

```

---

### record_metric_response.proto {#record_metric_response}

**Path**: `pkg/metrics/proto/record_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `RecordMetricResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/recording_stats.proto` →
  [metrics_2](./metrics_2.md#recording_stats)
- `pkg/metrics/proto/validation_result.proto` →
  [config_2](./config_2.md#validation_result) →
  [metrics_2](./metrics_2.md#validation_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/record_metric_response.proto
// file: metrics/proto/responses/record_metric_response.proto
//
// Record metric response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/recording_stats.proto";
import "pkg/metrics/proto/validation_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordMetricResponse contains the result of recording a metric data point.
 */
message RecordMetricResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Unique ID assigned to the recorded metric (if applicable)
  string metric_id = 3;

  // Timestamp when the metric was actually recorded
  google.protobuf.Timestamp recorded_at = 4;

  // Provider that handled the metric
  string provider_id = 5;

  // Validation results if validation was requested
  ValidationResult validation = 6;

  // Performance metrics about the recording operation
  RecordingStats stats = 7;

  // Warnings or informational messages
  repeated string warnings = 8;
}

```

---

### record_metrics_request.proto {#record_metrics_request}

**Path**: `pkg/metrics/proto/record_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `RecordMetricsRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)

#### Source Code

```protobuf
// file: pkg/metrics/proto/record_metrics_request.proto
// version: 1.0.0
// guid: a9b8c7d6-e5f4-3210-9876-543210abcdef

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordMetricsRequest represents a batch request to record multiple metrics.
 */
message RecordMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Batch of metrics to record
  repeated MetricData metrics = 2;

  // Whether to validate all metrics before recording any
  bool atomic = 3;

  // Optional batch ID for tracking
  string batch_id = 4;

  // Maximum number of retries for failed metrics
  int32 max_retries = 5;
}

```

---

### record_metrics_response.proto {#record_metrics_response}

**Path**: `pkg/metrics/proto/record_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 123

**Messages** (4): `RecordMetricsResponse`, `MetricResult`, `BatchStats`,
`ValidationSummary`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/record_metrics_response.proto
// file: metrics/proto/responses/record_metrics_response.proto
//
// Batch record metrics response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordMetricsResponse contains the results of recording multiple metrics in batch.
 */
message RecordMetricsResponse {
  // Overall success status of the batch operation
  bool success = 1;

  // Number of metrics successfully recorded
  int32 success_count = 2;

  // Number of metrics that failed to record
  int32 failure_count = 3;

  // Total number of metrics processed
  int32 total_count = 4;

  // Overall error information if the batch operation failed
  gcommon.v1.common.Error error = 5;

  // Detailed results for each metric (if requested)
  repeated MetricResult results = 6;

  // Timestamp when the batch operation was completed
  google.protobuf.Timestamp completed_at = 7;

  // Provider that handled the batch
  string provider_id = 8;

  // Performance metrics about the batch operation
  BatchStats stats = 9;

  // Warnings or informational messages about the batch
  repeated string warnings = 10;

  // Summary of validation results (if validation was enabled)
  ValidationSummary validation_summary = 11;
}

/**
 * MetricResult contains the result of processing a single metric within the batch.
 */
message MetricResult {
  // Index of the metric in the original batch (0-based)
  int32 index = 1;

  // Success status for this specific metric
  bool success = 2;

  // Error information if this metric failed
  gcommon.v1.common.Error error = 3;

  // Unique ID assigned to the metric (if successful)
  string metric_id = 4;

  // Timestamp when this metric was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Warnings specific to this metric
  repeated string warnings = 6;

  // Whether this metric was deduplicated
  bool deduplicated = 7;
}

/**
 * BatchStats contains performance information about the batch operation.
 */
message BatchStats {
  // Total time taken to process the batch (milliseconds)
  int64 total_processing_time_ms = 1;

  // Average time per metric (milliseconds)
  int64 avg_processing_time_ms = 2;

  // Total size of all metrics data (bytes)
  int64 total_data_size_bytes = 3;

  // Number of metrics that were deduplicated
  int32 deduplication_count = 4;

  // Number of parallel workers used
  int32 parallel_workers = 5;

  // Backend storage latency (milliseconds)
  int64 storage_latency_ms = 6;

  // Memory usage during batch processing (bytes)
  int64 memory_usage_bytes = 7;
}

/**
 * ValidationSummary provides an overview of validation results for the batch.
 */
message ValidationSummary {
  // Number of metrics that passed validation
  int32 valid_count = 1;

  // Number of metrics that failed validation
  int32 invalid_count = 2;

  // Most common validation errors
  repeated string common_errors = 3;

  // Schema version used for validation
  string schema_version = 4;
}

```

---

### record_summary_request.proto {#record_summary_request}

**Path**: `pkg/metrics/proto/record_summary_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `RecordSummaryRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/summary_metric.proto` →
  [metrics_2](./metrics_2.md#summary_metric)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/record_summary_request.proto
// file: metrics/proto/requests/record_summary_request.proto
//
// Request message for recording a summary metric observation.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/summary_metric.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message RecordSummaryRequest {
  // Summary metric data
  SummaryMetric metric = 1;

  // Optional timestamp for the observation
  google.protobuf.Timestamp observed_at = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### record_summary_response.proto {#record_summary_response}

**Path**: `pkg/metrics/proto/record_summary_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `RecordSummaryResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/recording_stats.proto` →
  [metrics_2](./metrics_2.md#recording_stats)
- `pkg/metrics/proto/summary_metric.proto` →
  [metrics_2](./metrics_2.md#summary_metric)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/record_summary_response.proto
// file: metrics/proto/responses/record_summary_response.proto
//
// Response after recording a summary metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/recording_stats.proto";
import "pkg/metrics/proto/summary_metric.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordSummaryResponse returns updated summary stats.
 */
message RecordSummaryResponse {
  // Updated summary metric
  SummaryMetric metric = 1;

  // Processing stats
  RecordingStats stats = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}

```

---

### register_metric_request.proto {#register_metric_request}

**Path**: `pkg/metrics/proto/register_metric_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 201

**Messages** (10): `RegisterMetricRequest`, `MetricDefinition`,
`LabelDefinition`, `MetricTypeConfig`, `HistogramConfig`, `SummaryConfig`,
`GaugeConfig`, `CounterConfig`, `ValidationRules`, `RegistrationOptions`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/metrics/proto/export_config.proto` →
  [metrics_config](./metrics_config.md#export_config)
- `pkg/metrics/proto/metric_type.proto` →
  [metrics_1](./metrics_1.md#metric_type) → [queue_1](./queue_1.md#metric_type)
- `pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto` →
  [metrics_config](./metrics_config.md#retention_policy_retentionpolicyconfig)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/register_metric_request.proto
// file: metrics/proto/requests/register_metric_request.proto
//
// Register metric request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/metrics/proto/export_config.proto";
import "pkg/metrics/proto/metric_type.proto";
import "pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message RegisterMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metric definition to register
  MetricDefinition definition = 2;

  // Optional provider ID to register with
  string provider_id = 3;

  // Whether to replace an existing metric with the same name
  bool replace_existing = 4;

  // Validation options for the registration
  RegistrationOptions options = 5;
}

/**
 * MetricDefinition contains the complete definition of a metric.
 */
message MetricDefinition {
  // Unique name for the metric
  string name = 1;

  // Type of metric (counter, gauge, histogram, etc.)
  MetricType type = 2;

  // Human-readable description
  string description = 3;

  // Unit of measurement (e.g., "bytes", "requests", "seconds")
  string unit = 4;

  // Labels that this metric supports
  repeated LabelDefinition labels = 5;

  // Metric-specific configuration
  MetricTypeConfig config = 6;

  // Retention policy for this metric
  RetentionPolicyConfig retention = 7;

  // Export configuration for this metric
  ExportConfig export_config = 8;

  // Validation rules for metric values
  ValidationRules validation = 9;

  // Tags for metric organization and discovery
  map<string, string> tags = 10;
}

/**
 * LabelDefinition defines a label that can be attached to the metric.
 */
message LabelDefinition {
  // Name of the label
  string name = 1;

  // Description of what this label represents
  string description = 2;

  // Whether this label is required
  bool required = 3;

  // Allowed values for this label (empty = any value allowed)
  repeated string allowed_values = 4;

  // Pattern for validating label values (regex)
  string validation_pattern = 5;

  // Default value if not specified
  string default_value = 6;
}

/**
 * MetricTypeConfig contains type-specific configuration for metrics.
 */
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

/**
 * HistogramConfig contains configuration specific to histogram metrics.
 */
message HistogramConfig {
  // Predefined buckets for the histogram
  repeated double buckets = 1;

  // Whether to automatically adjust buckets based on data
  bool auto_buckets = 2;

  // Maximum number of buckets to maintain
  int32 max_buckets = 3;
}

/**
 * SummaryConfig contains configuration specific to summary metrics.
 */
message SummaryConfig {
  // Quantiles to calculate (e.g., 0.5, 0.95, 0.99)
  repeated double quantiles = 1;

  // Time window for calculating quantiles
  string time_window = 2;

  // Maximum age of observations to include
  string max_age = 3;
}

/**
 * GaugeConfig contains configuration specific to gauge metrics.
 */
message GaugeConfig {
  // Minimum allowed value
  double min_value = 1;

  // Maximum allowed value
  double max_value = 2;

  // Whether the gauge can go negative
  bool allow_negative = 3;
}

/**
 * CounterConfig contains configuration specific to counter metrics.
 */
message CounterConfig {
  // Starting value for the counter
  double initial_value = 1;

  // Whether the counter can be reset
  bool allow_reset = 2;

  // Maximum value before rolling over
  double max_value = 3;
}

/**
 * ValidationRules define validation rules for metric values.
 */
message ValidationRules {
  // Minimum allowed value
  double min_value = 1;

  // Maximum allowed value
  double max_value = 2;

  // Whether null/zero values are allowed
  bool allow_null = 3;

  // Custom validation expressions
  repeated string validation_expressions = 4;
}

/**
 * RegistrationOptions configure the registration process.
 */
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

### register_metric_response.proto {#register_metric_response}

**Path**: `pkg/metrics/proto/register_metric_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 111

**Messages** (4): `RegisterMetricResponse`, `RegistrationValidation`,
`RegistrationResult`, `SchemaChange`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/metrics/proto/registration_action.proto` →
  [metrics_2](./metrics_2.md#registration_action)

#### Source Code

```protobuf
// file: pkg/metrics/proto/register_metric_response.proto
// version: 1.1.0
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/metrics/proto/registration_action.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RegisterMetricResponse contains the result of registering a metric definition.
 */
message RegisterMetricResponse {
  // Success status of the registration
  bool success = 1;

  // Error information if registration failed
  gcommon.v1.common.Error error = 2;

  // Unique ID assigned to the registered metric
  string metric_id = 3;

  // Name of the registered metric
  string metric_name = 4;

  // When the metric was registered
  google.protobuf.Timestamp registered_at = 5;

  // Provider that handled the registration
  string provider_id = 6;

  // Validation results from the registration process
  RegistrationValidation validation = 7;

  // Information about what was created/updated
  RegistrationResult result = 8;

  // Warnings or informational messages
  repeated string warnings = 9;

  // Whether this replaced an existing metric
  bool replaced_existing = 10;
}

/**
 * RegistrationValidation contains validation results from registration.
 */
message RegistrationValidation {
  // Whether the metric definition is valid
  bool valid = 1;

  // Validation errors (if any)
  repeated string errors = 2;

  // Validation warnings (if any)
  repeated string warnings = 3;

  // Schema version used for validation
  string schema_version = 4;

  // Suggestions for improving the metric definition
  repeated string suggestions = 5;
}

/**
 * RegistrationResult contains information about what was created/updated.
 */
message RegistrationResult {
  // Whether a new metric was created or existing one updated
  RegistrationAction action = 1;

  // Indices that were created for the metric
  repeated string created_indices = 2;

  // Alert rules that were created (if alerting was enabled)
  repeated string created_alerts = 3;

  // Export configurations that were set up
  repeated string configured_exports = 4;

  // Retention policies that were applied
  repeated string applied_retention_policies = 5;

  // Schema changes that were made
  repeated SchemaChange schema_changes = 6;
}

/**
 * SchemaChange describes a change made to the metric schema.
 */
message SchemaChange {
  // Type of change made
  string change_type = 1;

  // Description of the change
  string description = 2;

  // Whether this change is backward compatible
  bool backward_compatible = 3;

  // Migration steps required (if any)
  repeated string migration_steps = 4;
}

```

---

### reset_metrics_request.proto {#reset_metrics_request}

**Path**: `pkg/metrics/proto/reset_metrics_request.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `ResetMetricsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/requests/reset_metrics_request.proto
// file: metrics/proto/requests/reset_metrics_request.proto
//
// Request message for resetting stored metric data.
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message ResetMetricsRequest {
  // Metric name or ID to reset
  string metric = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### reset_metrics_response.proto {#reset_metrics_response}

**Path**: `pkg/metrics/proto/reset_metrics_response.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `ResetMetricsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/metrics/proto/responses/reset_metrics_response.proto
// file: metrics/proto/responses/reset_metrics_response.proto
//
// Response after resetting metric data.
//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ResetMetricsResponse reports reset status.
 */
message ResetMetricsResponse {
  // Whether the reset succeeded
  bool success = 1;

  // Error information if reset failed
  gcommon.v1.common.Error error = 2;
}

```

---
