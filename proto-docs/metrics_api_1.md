# metrics_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [backup_info.proto](#backup_info)
- [batch_context.proto](#batch_context)
- [batch_options.proto](#batch_options)
- [batch_stats.proto](#batch_stats)
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
---


## Detailed Documentation

### backup_info.proto {#backup_info}

**Path**: `gcommon/v1/metrics/backup_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `MetricsBackupInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/backup_info.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174026

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * BackupInfo contains information about backup operations.
 */
message MetricsBackupInfo {
  // Unique backup identifier
  string backup_id = 1 [(buf.validate.field).string.min_len = 1];

  // Location where backup is stored
  string backup_location = 2 [(buf.validate.field).string.min_len = 1];

  // Size of backup in bytes
  int64 backup_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // When backup was created
  google.protobuf.Timestamp backup_created_at = 4;

  // Backup retention period
  string backup_retention = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### batch_context.proto {#batch_context}

**Path**: `gcommon/v1/metrics/batch_context.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `BatchContext`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_context.proto
// version: 1.0.0
// guid: f2e4f42e-77e5-4086-89ea-b7d514304089

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message BatchContext {
  // Unique batch ID
  string batch_id = 1 [(buf.validate.field).string.min_len = 1];

  // Position in the batch (0-based)
  int32 batch_position = 2 [(buf.validate.field).int32.gte = 0];

  // Total size of the batch
  int32 batch_size = 3 [(buf.validate.field).int32.gte = 0];

  // Whether this is the last item in the batch
  bool is_last = 4;
}
```

---

### batch_options.proto {#batch_options}

**Path**: `gcommon/v1/metrics/batch_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `MetricsBatchOptions`

**Imports** (3):

- `gcommon/v1/common/batch_priority.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_options.proto
// version: 1.0.0
// guid: cb61183a-3b53-41cd-a131-685b4fd8be75

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/batch_priority.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * BatchOptions configures how batch operations should be processed.
 */
message MetricsBatchOptions {
  // Whether to process metrics in parallel
  bool parallel_processing = 1;

  // Maximum concurrent operations (if parallel processing is enabled)
  int32 max_concurrency = 2 [(buf.validate.field).int32.gte = 0];

  // Whether to deduplicate metrics within the batch
  bool deduplicate = 3;

  // Whether to return detailed results for each metric
  bool return_detailed_results = 4;

  // Timeout for the entire batch operation (seconds)
  int32 timeout_seconds = 5 [(buf.validate.field).int32.gt = 0];

  // Whether to enable transactional semantics (all or nothing)
  bool transactional = 6;

  // Priority level for the batch operation
  gcommon.v1.common.BatchPriority priority = 7;
}
```

---

### batch_stats.proto {#batch_stats}

**Path**: `gcommon/v1/metrics/batch_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `MetricsBatchStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_stats.proto
// version: 1.0.0
// guid: 6e20b77a-ba63-4ecc-9089-0371258fb120

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsBatchStats {
  // Total time taken to process the batch (milliseconds)
  int64 total_processing_time_ms = 1 [(buf.validate.field).int64.gte = 0];

  // Average time per metric (milliseconds)
  int64 avg_processing_time_ms = 2 [(buf.validate.field).int64.gte = 0];

  // Total size of all metrics data (bytes)
  int64 total_data_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Number of metrics that were deduplicated
  int32 deduplication_count = 4 [(buf.validate.field).int32.gte = 0];

  // Number of parallel workers used
  int32 parallel_workers = 5 [(buf.validate.field).int32.gte = 0];

  // Backend storage latency (milliseconds)
  int64 storage_latency_ms = 6 [(buf.validate.field).int64.gte = 0];

  // Memory usage during batch processing (bytes)
  int64 memory_usage_bytes = 7 [(buf.validate.field).int64.gte = 0];
}
```

---

### create_metric_request.proto {#create_metric_request}

**Path**: `gcommon/v1/metrics/create_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `CreateMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_metric_request.proto
// version: 1.0.1
// guid: 4fc0fab0-dc1a-42ff-bb58-35b524f790e1
// file: proto/gcommon/v1/metrics/v1/create_metric_request.proto
//
// Request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CreateMetricRequest {
  // Metric to create
  MetricData metric = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### create_metric_response.proto {#create_metric_response}

**Path**: `gcommon/v1/metrics/create_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `CreateMetricResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_metric_response.proto
// version: 1.0.1
// guid: 83588dec-abb1-410c-8a89-b2d53cdd2eec
// file: proto/gcommon/v1/metrics/v1/create_metric_response.proto
//
// Response returned after creating a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

**Path**: `gcommon/v1/metrics/create_provider_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `CreateProviderRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/provider_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_provider_request.proto
// version: 1.0.1
// guid: 1bbe7bf6-5552-43f2-a429-d72f7fb4385f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/provider_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
```

---

### create_provider_response.proto {#create_provider_response}

**Path**: `gcommon/v1/metrics/create_provider_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 48

**Messages** (1): `CreateProviderResponse`

**Imports** (8):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/metrics/applied_config.proto`
- `gcommon/v1/metrics/provider_endpoints.proto`
- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_provider_response.proto
// version: 1.0.0
// guid: d3b0a595-52ae-4306-be02-6d7d23e8a0df

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/metrics/applied_config.proto";
import "gcommon/v1/metrics/provider_endpoints.proto";
import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CreateProviderResponse {
  // Success status of the creation
  bool success = 1;

  // Error information if creation failed
  gcommon.v1.common.Error error = 2;

  // ID of the created provider
  string provider_id = 3;

  // When the provider was created
  google.protobuf.Timestamp created_at = 4 [ (buf.validate.field).required = true ];

  // Current status of the provider
  ProviderStatus status = 5;

  // Validation results
  gcommon.v1.common.MetricsValidationResult validation = 6;

  // Configuration details that were applied
  AppliedConfig applied_config = 7;

  // Warnings or informational messages
  repeated string warnings = 8;

  // Endpoint information for accessing the provider
  ProviderEndpoints endpoints = 9;
}
```

---

### delete_metric_request.proto {#delete_metric_request}

**Path**: `gcommon/v1/metrics/delete_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `DeleteMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_metric_request.proto
// version: 1.0.0
// guid: a9c3b698-cd8d-4405-b2f8-913d63eb25b4
// file: proto/gcommon/v1/metrics/v1/delete_metric_request.proto
//
// Request to delete an existing metric definition.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeleteMetricRequest {
  // Unique identifier of the metric
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### delete_metric_response.proto {#delete_metric_response}

**Path**: `gcommon/v1/metrics/delete_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `DeleteMetricResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_metric_response.proto
// version: 1.0.1
// guid: 8c8412a9-6dbd-4e4c-9b63-36745a456d41
// file: proto/gcommon/v1/metrics/v1/delete_metric_response.proto
//
// Response returned after deleting a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

**Path**: `gcommon/v1/metrics/delete_provider_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `DeleteProviderRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_provider_request.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-9012-3456-789abcdef012

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeleteProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to delete
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Optional force deletion (ignore dependencies)
  bool force = 3;

  // Dry run mode - just check what would be deleted
  bool dry_run = 4;
}
```

---

### delete_provider_response.proto {#delete_provider_response}

**Path**: `gcommon/v1/metrics/delete_provider_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `DeleteProviderResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/backup_info.proto`
- `gcommon/v1/metrics/deletion_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_provider_response.proto
// version: 1.0.0
// guid: 0c3bdd9f-3771-4f0b-8c33-24d5a40b6c06

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/backup_info.proto";
import "gcommon/v1/metrics/deletion_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeleteProviderResponse {
  // Success status of the deletion
  bool success = 1;

  // Error information if deletion failed
  gcommon.v1.common.Error error = 2;

  // Provider ID that was deleted
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // When the deletion was completed
  google.protobuf.Timestamp deleted_at = 4;

  // Deletion results
  DeletionResult deletion_result = 5;

  // Warnings or informational messages
  repeated string warnings = 6 [(buf.validate.field).repeated.min_items = 1];

  // Backup information (if backup was created)
  MetricsBackupInfo backup_info = 7;

  // When scheduled deletion will occur (if grace period is set)
  google.protobuf.Timestamp scheduled_deletion = 8;
}
```

---

### export_metrics_request.proto {#export_metrics_request}

**Path**: `gcommon/v1/metrics/export_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ExportMetricsRequest`

**Imports** (4):

- `gcommon/v1/common/metrics_export_format.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_metrics_request.proto
// version: 1.1.0
// guid: 2c9c223d-523d-4b0c-aa30-6249240e59d6

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_export_format.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportMetricsRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metrics provider to export from
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Desired export format
  gcommon.v1.common.MetricsExportFormat format = 3;

  // Destination URI or path
  string destination = 4 [(buf.validate.field).string.min_len = 1];

  // Specific metrics to include (optional)
  repeated string metric_names = 5 [(buf.validate.field).repeated.min_items = 1];

  // Include metadata such as descriptions and units
  bool include_metadata = 6;
}
```

---

### export_metrics_response.proto {#export_metrics_response}

**Path**: `gcommon/v1/metrics/export_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ExportMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_metrics_response.proto
// version: 1.1.0
// guid: 0d2df1e4-76e3-437b-855e-4dcc2b6f6b9e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
  string file_url = 5 [ (buf.validate.field).string.uri = true ];
}
```

---

### get_alerting_rules_request.proto {#get_alerting_rules_request}

**Path**: `gcommon/v1/metrics/get_alerting_rules_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetAlertingRulesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_request.proto
// version: 1.0.0
// guid: eb75f08e-4be4-41e8-8992-f9f95b7962bc
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_request.proto
//
// Request message for retrieving alerting rules associated with a metric.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetAlertingRulesRequest {
  // Metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_alerting_rules_response.proto {#get_alerting_rules_response}

**Path**: `gcommon/v1/metrics/get_alerting_rules_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `GetAlertingRulesResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/alerting_rule.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_response.proto
// version: 1.0.0
// guid: e6b7e2fc-4cd1-4e68-8d74-edab03688e54
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_response.proto
//
// Response message containing alerting rules for a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/alerting_rule.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetAlertingRulesResponse returns configured alerting rules.
 */
message GetAlertingRulesResponse {
  // Alerting rules for the metric
  repeated AlertingRule rules = 1 [(buf.validate.field).repeated.min_items = 1];

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}
```

---

### get_metric_metadata_request.proto {#get_metric_metadata_request}

**Path**: `gcommon/v1/metrics/get_metric_metadata_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 51

**Messages** (1): `GetMetricMetadataRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_request.proto
// version: 1.0.0
// guid: 4706d64e-ea60-4994-a732-e8377db776b5
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_request.proto
//
// Request definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricMetadataRequest retrieves metadata for specific metrics.
 */
message GetMetricMetadataRequest {
  // Provider ID to query
  string provider_id = 1 [(buf.validate.field).string.min_len = 1];

  // Specific metric names to get metadata for (if empty, get all)
  repeated string metric_names = 2 [(buf.validate.field).repeated.min_items = 1];

  // Namespace to filter by (optional)
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Include inactive metrics
  bool include_inactive = 4;

  // Pagination options
  int32 page_size = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
  string page_token = 6 [(buf.validate.field).string.min_len = 1];

  // Filter by metric type (optional)
  string metric_type = 7 [(buf.validate.field).string.min_len = 1];

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

**Path**: `gcommon/v1/metrics/get_metric_metadata_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `GetMetricMetadataResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `gcommon/v1/metrics/pagination_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_response.proto
// version: 1.0.0
// guid: 118692f7-fe67-4e13-8a1f-416220925369
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_response.proto
//
// Response definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "gcommon/v1/metrics/pagination_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricMetadataResponse contains metadata for requested metrics.
 */
message GetMetricMetadataResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Provider ID that handled the request
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Retrieved metadata entries
  repeated MetricMetadata metadata = 4;

  // Pagination information
  MetricsPaginationInfo pagination = 5;

  // Total number of matching metrics
  int64 total_count = 6 [(buf.validate.field).int64.gte = 0];

  // When the response was generated
  google.protobuf.Timestamp generated_at = 7;

  // Warnings or informational messages
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];

  // Query execution time in milliseconds
  int64 execution_time_ms = 9 [(buf.validate.field).int64.gte = 0];
}
```

---

### get_metric_request.proto {#get_metric_request}

**Path**: `gcommon/v1/metrics/get_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_request.proto
// version: 1.0.0
// guid: 48d74623-574e-4253-b0dd-784417ffe50d
// file: proto/gcommon/v1/metrics/v1/get_metric_request.proto
//
// Request message for retrieving a metric by ID.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricRequest {
  // Unique metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_metric_response.proto {#get_metric_response}

**Path**: `gcommon/v1/metrics/get_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetMetricResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_response.proto
// version: 1.0.1
// guid: dc01ceeb-c2dd-4f50-9e0b-424293f1f529
// file: proto/gcommon/v1/metrics/v1/get_metric_response.proto
//
// Response containing a metric definition and data.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

**Path**: `gcommon/v1/metrics/get_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `MetricsGetMetricsRequest`

**Imports** (8):

- `gcommon/v1/common/pagination_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metric_aggregation.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `gcommon/v1/metrics/output_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_request.proto
// version: 1.0.0
// guid: ec242bb6-5817-45b8-88de-7245b2536b35

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/pagination_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metric_aggregation.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "gcommon/v1/metrics/output_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsGetMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter to determine which metrics to retrieve
  MetricFilter filter = 2;

  // Time range for the request
  gcommon.v1.common.TimeRangeMetrics time_range = 3;

  // Aggregation options for the metrics
  MetricAggregation aggregation = 4;

  // Pagination options
  gcommon.v1.common.PaginationOptions pagination = 5;

  // Optional provider ID to query
  string provider_id = 6 [(buf.validate.field).string.min_len = 1];

  // Output format options
  OutputOptions output_options = 7;

  // Whether to include metadata with results
  bool include_metadata = 8;

  // Maximum number of metrics to return
  int32 limit = 9 [(buf.validate.field).int32.gte = 0];
}
```

---

### get_metrics_response.proto {#get_metrics_response}

**Path**: `gcommon/v1/metrics/get_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 59

**Messages** (1): `MetricsGetMetricsResponse`

**Imports** (9):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `gcommon/v1/metrics/pagination_info.proto`
- `gcommon/v1/metrics/query_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_response.proto
// version: 1.0.0
// guid: 55ced9dc-7d12-4f0b-883d-5e7de55a038e
// file: proto/gcommon/v1/metrics/v1/get_metrics_response.proto
//
// Get metrics response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "gcommon/v1/metrics/pagination_info.proto";
import "gcommon/v1/metrics/query_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricsResponse contains the retrieved metrics data.
 */
message MetricsGetMetricsResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Retrieved metrics data
  repeated MetricData metrics = 3 [(buf.validate.field).repeated.min_items = 1];

  // Metadata for the metrics (if requested)
  repeated MetricMetadata metadata = 4;

  // Pagination information
  MetricsPaginationInfo pagination = 5;

  // Query execution statistics
  MetricsQueryStats stats = 6;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 7;

  // Time range covered by the response
  gcommon.v1.common.TimeRangeMetrics time_range = 8;

  // Warnings or informational messages
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Provider that handled the request
  string provider_id = 10 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_metrics_summary_request.proto {#get_metrics_summary_request}

**Path**: `gcommon/v1/metrics/get_metrics_summary_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `GetMetricsSummaryRequest`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `gcommon/v1/metrics/summary_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_summary_request.proto
// version: 1.0.0
// guid: 9617cdf7-a614-4717-a660-aae208eb1774

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "gcommon/v1/metrics/summary_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricsSummaryRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Optional filter to limit which metrics to include in summary
  MetricFilter filter = 2;

  // Time range for the summary
  gcommon.v1.common.TimeRangeMetrics time_range = 3;

  // What summary information to include
  SummaryOptions options = 4;

  // Optional provider ID to query
  string provider_id = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to include provider-level statistics
  bool include_provider_stats = 6;

  // Whether to include health status information
  bool include_health_status = 7;
}
```

---

### get_metrics_summary_response.proto {#get_metrics_summary_response}

**Path**: `gcommon/v1/metrics/get_metrics_summary_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `GetMetricsSummaryResponse`

**Imports** (8):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metrics_health_info.proto`
- `gcommon/v1/metrics/metrics_summary.proto`
- `gcommon/v1/metrics/provider_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_summary_response.proto
// version: 1.0.0
// guid: 9cd4897b-9464-4d95-adf3-9884dbc3d363

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metrics_health_info.proto";
import "gcommon/v1/metrics/metrics_summary.proto";
import "gcommon/v1/metrics/provider_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricsSummaryResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Summary information organized by category
  MetricsSummary summary = 3;

  // Provider-level statistics (if requested)
  repeated ProviderSummary provider_summaries = 4 [(buf.validate.field).repeated.min_items = 1];

  // Health status information (if requested)
  MetricsHealthInfo health_status = 5;

  // When the summary was generated
  google.protobuf.Timestamp generated_at = 6;

  // Time range covered by the summary
  gcommon.v1.common.TimeRangeMetrics time_range = 7;

  // Warnings or informational messages
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### get_provider_stats_request.proto {#get_provider_stats_request}

**Path**: `gcommon/v1/metrics/get_provider_stats_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `GetProviderStatsRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/stats_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_provider_stats_request.proto
// version: 1.0.0
// guid: 3325d42f-84b8-46c7-85ef-e324a05386d5

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/stats_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetProviderStatsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to get stats for
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Time range for statistics
  gcommon.v1.common.TimeRangeMetrics time_range = 3;

  // What statistics to include
  StatsOptions options = 4;

  // Granularity for time-series statistics
  string granularity = 5; // e.g., "1m", "5m", "1h"

  // Whether to include real-time metrics
  bool include_realtime = 6;
}
```

---

### get_provider_stats_response.proto {#get_provider_stats_response}

**Path**: `gcommon/v1/metrics/get_provider_stats_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `GetProviderStatsResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/provider_statistics.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_provider_stats_response.proto
// version: 1.0.0
// guid: 26ba7b19-1782-4137-b19b-f6ee43e59f15

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/provider_statistics.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetProviderStatsResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Provider ID these stats are for
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Comprehensive provider statistics
  ProviderStatistics statistics = 4;

  // When the statistics were generated
  google.protobuf.Timestamp generated_at = 5;

  // Time range covered by the statistics
  gcommon.v1.common.TimeRangeMetrics time_range = 6;

  // Warnings or informational messages
  repeated string warnings = 7 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### get_stats_request.proto {#get_stats_request}

**Path**: `gcommon/v1/metrics/get_stats_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `MetricsGetStatsRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/timestamp_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_stats_request.proto
// version: 1.0.0
// guid: 2595bd64-9fd4-4bfb-af86-63535bc068c1
// file: proto/gcommon/v1/metrics/v1/get_stats_request.proto
//
// Request for retrieving metric statistics over a time range.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/timestamp_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsGetStatsRequest {
  // Metric name or ID to query
  string metric = 1 [(buf.validate.field).string.min_len = 1];

  // Time range for stats
  MetricsTimestampRange range = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### get_stats_response.proto {#get_stats_response}

**Path**: `gcommon/v1/metrics/get_stats_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricsGetStatsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/query_stats.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_stats_response.proto
// version: 1.0.1
// guid: d4229356-6c26-4e69-8437-475e88a0bdc6
// file: proto/gcommon/v1/metrics/v1/get_stats_response.proto
//
// Response containing metric statistics over a time range.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/query_stats.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetStatsResponse returns statistics for a metric.
 */
message MetricsGetStatsResponse {
  // Statistics for the query
  MetricsQueryStats stats = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/metrics/health_check_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `MetricsHealthCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/health_check_request.proto
// version: 1.0.0
// guid: ffa1c922-b413-4b2d-a7fd-0d58fcd0b048
//
// HealthCheckRequest for the metrics module

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsHealthCheckRequest {
  // Metrics subsystem name (e.g., "prometheus").
  string subsystem = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/metrics/health_check_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `MetricsHealthCheckResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/health_check_response.proto
// version: 1.0.0
// guid: 2d9c7ce3-2e5b-42d7-9473-70bef7518cdd
//
// HealthCheckResponse for the metrics module
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * HealthCheckResponse contains the result of a metrics subsystem health check.
 */
message MetricsHealthCheckResponse {
  // Health status of the subsystem.
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Time taken to execute the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Optional human-readable message.
  string message = 3 [(buf.validate.field).string.min_len = 1];

  // Error details if unhealthy.
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### import_metrics_request.proto {#import_metrics_request}

**Path**: `gcommon/v1/metrics/import_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ImportMetricsRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/import_metrics_request.proto
// version: 1.0.0
// guid: 761d0d0a-fb74-41bb-a5aa-e446fa8300bb
// file: proto/gcommon/v1/metrics/v1/import_metrics_request.proto
//
// Request message for importing multiple metrics.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ImportMetricsRequest {
  // Metrics to import
  repeated MetricData metrics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### import_metrics_response.proto {#import_metrics_response}

**Path**: `gcommon/v1/metrics/import_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ImportMetricsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/import_metrics_response.proto
// version: 1.0.0
// guid: 54556e65-80a3-4d79-b67e-d98ca9bf7b0e
// file: proto/gcommon/v1/metrics/v1/import_metrics_response.proto
//
// Response returned after importing metrics.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ImportMetricsResponse reports the result of a batch import.
 */
message ImportMetricsResponse {
  // Number of metrics successfully imported
  int32 imported_count = 1 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Error information if the import failed
  gcommon.v1.common.Error error = 2;
}
```

---

### list_metrics_request.proto {#list_metrics_request}

**Path**: `gcommon/v1/metrics/list_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `ListMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/pagination.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_metrics_request.proto
// version: 1.0.0
// guid: a5ae698c-a783-4005-b054-167c31d44c8b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/pagination.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ListMetricsRequest requests a paginated list of metrics.
 */
message ListMetricsRequest {
  // Pagination information
  gcommon.v1.common.Pagination pagination = 1;

  // Optional name filter
  string name_filter = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_metrics_response.proto {#list_metrics_response}

**Path**: `gcommon/v1/metrics/list_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `ListMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_metrics_response.proto
// version: 1.0.0
// guid: 12b3dcff-48a7-4a05-b427-45a55314dacb
// file: proto/gcommon/v1/metrics/v1/list_metrics_response.proto
//
// Response containing a list of metric metadata.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ListMetricsResponse lists available metrics.
 */
message ListMetricsResponse {
  // Available metrics
  repeated MetricMetadata metrics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### list_providers_request.proto {#list_providers_request}

**Path**: `gcommon/v1/metrics/list_providers_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ListProvidersRequest`

**Imports** (4):

- `gcommon/v1/common/pagination_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/provider_filter.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_providers_request.proto
// version: 1.0.1
// guid: cc2b7794-28e4-442f-88a3-24bcd696fe6a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/pagination_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/provider_filter.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
```

---

### list_providers_response.proto {#list_providers_response}

**Path**: `gcommon/v1/metrics/list_providers_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `ListProvidersResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/pagination_info.proto`
- `gcommon/v1/metrics/provider_info.proto`
- `gcommon/v1/metrics/provider_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_providers_response.proto
// version: 1.0.0
// guid: ec44b05b-cb74-44b5-b495-4cf1e4c0877d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/pagination_info.proto";
import "gcommon/v1/metrics/provider_info.proto";
import "gcommon/v1/metrics/provider_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ListProvidersResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // List of providers
  repeated ProviderInfo providers = 3 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information
  MetricsPaginationInfo pagination = 4;

  // Summary statistics about the providers
  ProviderSummary summary = 5;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 6;
}
```

---

### query_metrics_request.proto {#query_metrics_request}

**Path**: `gcommon/v1/metrics/query_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `QueryMetricsRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_query.proto`
- `gcommon/v1/metrics/query_output_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_metrics_request.proto
// version: 1.0.0
// guid: d6616950-fd6a-4863-9a2d-3c5bed911918

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_query.proto";
import "gcommon/v1/metrics/query_output_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // The metric query to execute
  MetricQuery query = 2;

  // Optional query timeout in seconds
  int32 timeout_seconds = 3 [(buf.validate.field).int32.gt = 0];

  // Whether to return query execution plan (for debugging)
  bool include_query_plan = 4;

  // Whether to return only metadata without actual values (for schema discovery)
  bool metadata_only = 5;

  // Output format preferences
  QueryOutputOptions output_options = 6;
}
```

---

### query_metrics_response.proto {#query_metrics_response}

**Path**: `gcommon/v1/metrics/query_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `QueryMetricsResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_series.proto`
- `gcommon/v1/metrics/query_plan.proto`
- `gcommon/v1/metrics/query_statistics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_metrics_response.proto
// version: 1.0.0
// guid: 766d3060-cb60-4a59-8d9f-371e9f4e6eed

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_series.proto";
import "gcommon/v1/metrics/query_plan.proto";
import "gcommon/v1/metrics/query_statistics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryMetricsResponse {
  // Success status of the query
  bool success = 1;

  // Error information if query failed
  gcommon.v1.common.Error error = 2;

  // Query results organized as metric series
  repeated MetricSeries series = 3 [(buf.validate.field).repeated.min_items = 1];

  // Query execution statistics
  QueryStatistics statistics = 4;

  // Query execution plan (if requested)
  QueryPlan query_plan = 5;

  // Warnings or informational messages about the query
  repeated string warnings = 6 [(buf.validate.field).repeated.min_items = 1];

  // Pagination token for retrieving more results
  string next_page_token = 7 [(buf.validate.field).string.min_len = 1];

  // Total number of results available (for pagination)
  int64 total_results = 8 [(buf.validate.field).int64.gte = 0];
}
```

---

### record_counter_request.proto {#record_counter_request}

**Path**: `gcommon/v1/metrics/record_counter_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `RecordCounterRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_counter_request.proto
// version: 1.0.0
// guid: af165336-0041-4c47-a00d-5f0470240fda
// file: proto/gcommon/v1/metrics/v1/record_counter_request.proto
//
// Record counter request definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordCounterRequest is used to record or increment a counter metric.
 */
message RecordCounterRequest {
  // Metric name (e.g., "http_requests_total")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/metrics/record_counter_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `RecordCounterResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/counter_metric.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_counter_response.proto
// version: 1.0.1
// guid: 47ec1fef-7557-4265-802c-0988b554f2a3
// file: proto/gcommon/v1/metrics/v1/record_counter_response.proto
//
// Record counter response definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/counter_metric.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

**Path**: `gcommon/v1/metrics/record_gauge_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `RecordGaugeRequest`

**Imports** (5):

- `gcommon/v1/common/gauge_operation.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_gauge_request.proto
// version: 1.1.0
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/gauge_operation.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordGaugeRequest is used to set or update a gauge metric value.
 * Gauges can increase, decrease, or be set to specific values.
 */
message RecordGaugeRequest {
  // Metric name (e.g., "memory_usage_bytes", "cpu_usage_percent")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
  gcommon.v1.common.GaugeOperation operation = 8;
}
```

---

### record_gauge_response.proto {#record_gauge_response}

**Path**: `gcommon/v1/metrics/record_gauge_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `RecordGaugeResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/gauge_metric.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_gauge_response.proto
// version: 1.2.0
// guid: c1d2e3f4-g5h6-7890-i1j2-k3l4m5n6o7p8

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/gauge_metric.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
  double previous_value = 4 [(buf.validate.field).double.gte = 0.0];

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

**Path**: `gcommon/v1/metrics/record_histogram_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 55

**Messages** (1): `RecordHistogramRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_histogram_request.proto
// version: 1.0.0
// guid: 5d38efab-f98b-4ddf-8e50-08395f5e24fc
// file: proto/gcommon/v1/metrics/v1/record_histogram_request.proto
//
// Request definitions for metrics module

//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordHistogramRequest {
  // Metric name (e.g., "request_duration_seconds", "response_size_bytes")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/metrics/record_histogram_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `RecordHistogramResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/bucket_info.proto`
- `gcommon/v1/metrics/histogram_metric.proto`
- `gcommon/v1/metrics/histogram_stats.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_histogram_response.proto
// version: 1.0.1
// guid: 33d2781c-78d0-4293-8c90-1a2b4e20c522

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/bucket_info.proto";
import "gcommon/v1/metrics/histogram_metric.proto";
import "gcommon/v1/metrics/histogram_stats.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
```

---

### record_metric_request.proto {#record_metric_request}

**Path**: `gcommon/v1/metrics/record_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 38

**Messages** (1): `RecordMetricRequest`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/batch_context.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metric_request.proto
// version: 1.0.0
// guid: 8e0ace8f-cfd2-45c0-9e30-47eefe47b60f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/batch_context.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // The metric data to record
  MetricData metric = 2;

  // Optional provider ID to use for recording
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to validate the metric before recording
  bool validate = 4;

  // Timestamp override (if not provided, current time is used)
  google.protobuf.Timestamp timestamp = 5;

  // Batch context information (if this is part of a batch operation)
  BatchContext batch_context = 6;
}
```

---

### record_metric_response.proto {#record_metric_response}

**Path**: `gcommon/v1/metrics/record_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 50

**Messages** (1): `RecordMetricResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metric_response.proto
// version: 1.0.0
// guid: f6b84950-9977-45e7-a9d6-1b3d9a800f62
// file: proto/gcommon/v1/metrics/v1/record_metric_response.proto
//
// Record metric response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordMetricResponse contains the result of recording a metric data point.
 */
message RecordMetricResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Unique ID assigned to the recorded metric (if applicable)
  string metric_id = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the metric was actually recorded
  google.protobuf.Timestamp recorded_at = 4;

  // Provider that handled the metric
  string provider_id = 5 [(buf.validate.field).string.min_len = 1];

  // Validation results if validation was requested
  gcommon.v1.common.MetricsValidationResult validation = 6;

  // Performance metrics about the recording operation
  RecordingStats stats = 7;

  // Warnings or informational messages
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### record_metrics_request.proto {#record_metrics_request}

**Path**: `gcommon/v1/metrics/record_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `RecordMetricsRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metrics_request.proto
// version: 1.0.0
// guid: a9b8c7d6-e5f4-3210-9876-543210abcdef

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordMetricsRequest represents a batch request to record multiple metrics.
 */
message RecordMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Batch of metrics to record
  repeated MetricData metrics = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether to validate all metrics before recording any
  bool atomic = 3;

  // Optional batch ID for tracking
  string batch_id = 4 [(buf.validate.field).string.min_len = 1];

  // Maximum number of retries for failed metrics
  int32 max_retries = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### record_metrics_response.proto {#record_metrics_response}

**Path**: `gcommon/v1/metrics/record_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `RecordMetricsResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/batch_stats.proto`
- `gcommon/v1/metrics/metric_result.proto`
- `gcommon/v1/metrics/validation_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metrics_response.proto
// version: 1.0.0
// guid: 14d6d2f6-2386-4f1b-a00f-086e0bfb5653

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/batch_stats.proto";
import "gcommon/v1/metrics/metric_result.proto";
import "gcommon/v1/metrics/validation_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordMetricsResponse {
  // Overall success status of the batch operation
  bool success = 1;

  // Number of metrics successfully recorded
  int32 success_count = 2 [(buf.validate.field).int32.gte = 0];

  // Number of metrics that failed to record
  int32 failure_count = 3 [(buf.validate.field).int32.gte = 0];

  // Total number of metrics processed
  int32 total_count = 4 [(buf.validate.field).int32.gte = 0];

  // Overall error information if the batch operation failed
  gcommon.v1.common.Error error = 5;

  // Detailed results for each metric (if requested)
  repeated MetricResult results = 6 [(buf.validate.field).repeated.min_items = 1];

  // Timestamp when the batch operation was completed
  google.protobuf.Timestamp completed_at = 7;

  // Provider that handled the batch
  string provider_id = 8 [(buf.validate.field).string.min_len = 1];

  // Batch processing statistics
  MetricsBatchStats stats = 9;

  // Warnings or informational messages about the batch
  repeated string warnings = 10 [(buf.validate.field).repeated.min_items = 1];

  // Summary of validation results (if validation was enabled)
  ValidationSummary validation_summary = 11;
}
```

---

### record_summary_request.proto {#record_summary_request}

**Path**: `gcommon/v1/metrics/record_summary_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `RecordSummaryRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/summary_metric.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_summary_request.proto
// version: 1.0.1
// guid: 5c052e01-88e7-4d02-b154-a1824090213b
// file: proto/gcommon/v1/metrics/v1/record_summary_request.proto
//
// Request message for recording a summary metric observation.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/summary_metric.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

**Path**: `gcommon/v1/metrics/record_summary_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `RecordSummaryResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `gcommon/v1/metrics/summary_metric.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_summary_response.proto
// version: 1.0.1
// guid: d23c6f17-2028-4070-ad58-01c921f8f75d
// file: proto/gcommon/v1/metrics/v1/record_summary_response.proto
//
// Response after recording a summary metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "gcommon/v1/metrics/summary_metric.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

