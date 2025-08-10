# metrics_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 35
- **Messages**: 22
- **Services**: 0
- **Enums**: 16

## Files in this Module

- [provider_state.proto](#provider_state)
- [provider_status.proto](#provider_status)
- [provider_summary.proto](#provider_summary)
- [provider_type.proto](#provider_type)
- [query_operation.proto](#query_operation)
- [query_stats.proto](#query_stats)
- [recording_stats.proto](#recording_stats)
- [registration_action.proto](#registration_action)
- [resource_limits_summary.proto](#resource_limits_summary)
- [resource_limits_update.proto](#resource_limits_update)
- [retention_policy.proto](#retention_policy)
- [retention_policy_retentionpolicy.proto](#retention_policy_retentionpolicy)
- [retention_unit.proto](#retention_unit)
- [sample_rate.proto](#sample_rate)
- [scrape_job.proto](#scrape_job)
- [scrape_status.proto](#scrape_status)
- [scrape_target.proto](#scrape_target)
- [storage_backend.proto](#storage_backend)
- [stream_compression.proto](#stream_compression)
- [stream_qos.proto](#stream_qos)
- [summary_metric.proto](#summary_metric)
- [tag_updates.proto](#tag_updates)
- [time_range.proto](#time_range)
- [time_series.proto](#time_series)
- [time_unit.proto](#time_unit)
- [time_window.proto](#time_window)
- [timer_metric.proto](#timer_metric)
- [timestamp_range.proto](#timestamp_range)
- [top_metrics.proto](#top_metrics)
- [update_action.proto](#update_action)
- [update_options.proto](#update_options)
- [update_result.proto](#update_result)
- [update_strategy.proto](#update_strategy)
- [validation_result.proto](#validation_result)
- [visualization_type.proto](#visualization_type)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_2](./config_2.md)
- [config_config_1](./config_config_1.md)
- [metrics_1](./metrics_1.md)
- [metrics_config](./metrics_config.md)

**Modules that depend on this one**:

- [auth](./auth.md)
- [common](./common.md)
- [database_api](./database_api.md)
- [metrics_1](./metrics_1.md)
- [metrics_api_1](./metrics_api_1.md)
- [metrics_api_2](./metrics_api_2.md)
- [metrics_config](./metrics_config.md)
- [queue_2](./queue_2.md)
- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [queue_config](./queue_config.md)
- [queue_services](./queue_services.md)

---

## Detailed Documentation

### provider_state.proto {#provider_state}

**Path**: `pkg/metrics/proto/provider_state.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Enums** (1): `ProviderState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/provider_state.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174024

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ProviderState defines the possible states of a provider.
 */
enum ProviderState {
  PROVIDER_STATE_UNSPECIFIED = 0;
  PROVIDER_STATE_CREATING = 1;
  PROVIDER_STATE_STARTING = 2;
  PROVIDER_STATE_RUNNING = 3;
  PROVIDER_STATE_STOPPING = 4;
  PROVIDER_STATE_STOPPED = 5;
  PROVIDER_STATE_ERROR = 6;
  PROVIDER_STATE_UNKNOWN = 7;
}

```

---

### provider_status.proto {#provider_status}

**Path**: `pkg/metrics/proto/provider_status.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ProviderStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/provider_state.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/provider_status.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174023

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/provider_state.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * Status of a metrics provider.
 */
message ProviderStatus {
  // Current state
  ProviderState state = 1;

  // Status message
  string message = 2;

  // Health check status
  string health = 3;

  // Last update time
  google.protobuf.Timestamp last_updated = 4;

  // Provider version
  string version = 5;
}

```

---

### provider_summary.proto {#provider_summary}

**Path**: `pkg/metrics/proto/provider_summary.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 62

**Messages** (1): `ProviderSummary`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/provider_status.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/provider_summary.proto
// version: 1.0.0
// guid: d5e6f7a8-b9c0-1d2e-3f4a-5b6c7d8e9f0a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/provider_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ProviderSummary contains summary information about a metrics provider.
 */
message ProviderSummary {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name of the provider
  string name = 2;

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
  string description = 14;
}

```

---

### provider_type.proto {#provider_type}

**Path**: `pkg/metrics/proto/provider_type.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Enums** (1): `ProviderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/provider_type.proto
// version: 1.0.0
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * Provider type enumeration.
 * Defines the different types of metrics providers supported.
 */
enum ProviderType {
  PROVIDER_TYPE_UNSPECIFIED = 0;
  PROVIDER_TYPE_PROMETHEUS = 1;
  PROVIDER_TYPE_OPENTELEMETRY = 2;
  PROVIDER_TYPE_STATSD = 3;
  PROVIDER_TYPE_CUSTOM = 4;
  PROVIDER_TYPE_MEMORY = 5;
  PROVIDER_TYPE_MULTI = 6;
}

```

---

### query_operation.proto {#query_operation}

**Path**: `pkg/metrics/proto/query_operation.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 60

**Enums** (1): `QueryOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/query_operation.proto
// file: metrics/proto/enums/query_operation.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * QueryOperation defines the types of operations that can be performed on metrics queries.
 * Used for aggregating, filtering, and transforming metric data.
 */
enum QueryOperation {
  // Unspecified operation (default)
  QUERY_OPERATION_UNSPECIFIED = 0;

  // Select/filter metrics by criteria
  QUERY_OPERATION_SELECT = 1;

  // Group metrics by labels
  QUERY_OPERATION_GROUP_BY = 2;

  // Sum values across time or series
  QUERY_OPERATION_SUM = 3;

  // Average values across time or series
  QUERY_OPERATION_AVG = 4;

  // Find minimum value
  QUERY_OPERATION_MIN = 5;

  // Find maximum value
  QUERY_OPERATION_MAX = 6;

  // Count number of samples
  QUERY_OPERATION_COUNT = 7;

  // Calculate rate of change
  QUERY_OPERATION_RATE = 8;

  // Calculate increase over time
  QUERY_OPERATION_INCREASE = 9;

  // Sort results
  QUERY_OPERATION_SORT = 10;

  // Limit number of results
  QUERY_OPERATION_LIMIT = 11;

  // Join multiple metric series
  QUERY_OPERATION_JOIN = 12;
}

```

---

### query_stats.proto {#query_stats}

**Path**: `pkg/metrics/proto/query_stats.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `QueryStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/query_stats.proto
// version: 1.0.0
// guid: f8a9b0c1-234f-689e-3456-901234567890

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message QueryStats {
  // Total queries executed
  int64 total_queries = 1;

  // Average execution time in milliseconds
  double avg_execution_time_ms = 2;

  // Number of failed queries
  int64 failed_queries = 3;

  // Cache hit rate
  double cache_hit_rate = 4;
}

```

---

### recording_stats.proto {#recording_stats}

**Path**: `pkg/metrics/proto/recording_stats.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `RecordingStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/recording_stats.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174028

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RecordingStats contains performance information about recording operations.
 */
message RecordingStats {
  // Time taken to process the request (milliseconds)
  int64 processing_time_ms = 1;

  // Number of retries attempted
  int32 retry_count = 2;

  // Whether data was successfully buffered
  bool buffered = 3;

  // Whether data was successfully persisted
  bool persisted = 4;
}

```

---

### registration_action.proto {#registration_action}

**Path**: `pkg/metrics/proto/registration_action.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Enums** (1): `RegistrationAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/registration_action.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RegistrationAction indicates what action was taken during registration.
 */
enum RegistrationAction {
  REGISTRATION_ACTION_UNSPECIFIED = 0;
  REGISTRATION_ACTION_CREATED = 1;
  REGISTRATION_ACTION_UPDATED = 2;
  REGISTRATION_ACTION_REPLACED = 3;
  REGISTRATION_ACTION_NO_CHANGE = 4;
}

```

---

### resource_limits_summary.proto {#resource_limits_summary}

**Path**: `pkg/metrics/proto/resource_limits_summary.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 48

**Messages** (1): `ResourceLimitsSummary`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/resource_limits_summary.proto
// version: 1.0.0
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ResourceLimitsSummary contains information about resource limits.
 */
message ResourceLimitsSummary {
  // Memory limit in bytes
  int64 memory_limit_bytes = 1;

  // CPU limit as percentage (0.0 to 100.0)
  double cpu_limit_percent = 2;

  // Disk limit in bytes
  int64 disk_limit_bytes = 3;

  // Network bandwidth limit in bytes per second
  int64 network_limit_bytes_per_sec = 4;

  // Current memory usage in bytes
  int64 memory_used_bytes = 5;

  // Current CPU usage as percentage (0.0 to 100.0)
  double cpu_used_percent = 6;

  // Current disk usage in bytes
  int64 disk_used_bytes = 7;

  // Current network usage in bytes per second
  int64 network_used_bytes_per_sec = 8;

  // Whether limits are enforced
  bool limits_enforced = 9;

  // Number of limit violations in the last hour
  uint32 violations_count = 10;
}

```

---

### resource_limits_update.proto {#resource_limits_update}

**Path**: `pkg/metrics/proto/resource_limits_update.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `ResourceLimitsUpdate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/resource_limits_update.proto
// version: 1.0.0
// guid: cc6398cf-50af-461a-a6de-d00d8a2e61d9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ResourceLimitsUpdate contains updates to resource limits.
 */
message ResourceLimitsUpdate {
  // Updated memory limit
  int64 max_memory_bytes = 1;

  // Updated CPU limit
  double max_cpu_percent = 2;

  // Updated disk limit
  int64 max_disk_bytes = 3;

  // Updated metrics limit
  int64 max_metrics = 4;

  // Updated data points per metric limit
  int64 max_data_points_per_metric = 5;
}

```

---

### retention_policy.proto {#retention_policy}

**Path**: `pkg/metrics/proto/retention_policy.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `RetentionPolicyInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/retention_policy_retentionpolicy.proto`
- `pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto` →
  [metrics_config](./metrics_config.md#retention_policy_retentionpolicyconfig)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/retention_policy.proto
// version: 1.0.0
// guid: 9b18ea2c-8470-4b90-93e1-437821fdd7f8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/retention_policy_retentionpolicy.proto";
import "pkg/metrics/proto/retention_policy_retentionpolicyconfig.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RetentionPolicyInfo combines a retention policy enum with
 * optional configuration details.
 */
message RetentionPolicyInfo {
  // Predefined policy selection
  RetentionPolicy policy = 1;

  // Detailed configuration for custom policies
  RetentionPolicyConfig config = 2;
}

```

---

### retention_policy_retentionpolicy.proto {#retention_policy_retentionpolicy}

**Path**: `pkg/metrics/proto/retention_policy_retentionpolicy.proto`
**Package**: `gcommon.v1.metrics` **Lines**: 49

**Enums** (1): `RetentionPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/retention_policy_retentionpolicy.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// RetentionPolicy represents different retention policies for metrics data
enum RetentionPolicy {
  // Unspecified retention policy
  RETENTION_POLICY_UNSPECIFIED = 0;

  // Short-term retention (minutes to hours)
  RETENTION_POLICY_SHORT_TERM = 1;

  // Medium-term retention (days to weeks)
  RETENTION_POLICY_MEDIUM_TERM = 2;

  // Long-term retention (months to years)
  RETENTION_POLICY_LONG_TERM = 3;

  // Archive retention (permanent storage)
  RETENTION_POLICY_ARCHIVE = 4;

  // Custom retention policy
  RETENTION_POLICY_CUSTOM = 5;

  // High-frequency data retention (seconds to minutes)
  RETENTION_POLICY_HIGH_FREQUENCY = 6;

  // Low-frequency data retention (hours to days)
  RETENTION_POLICY_LOW_FREQUENCY = 7;

  // Compliance retention (regulatory requirements)
  RETENTION_POLICY_COMPLIANCE = 8;

  // Real-time retention (immediate processing, no storage)
  RETENTION_POLICY_REAL_TIME = 9;

  // Aggregate retention (summary data only)
  RETENTION_POLICY_AGGREGATE = 10;
}

```

---

### retention_unit.proto {#retention_unit}

**Path**: `pkg/metrics/proto/retention_unit.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 48

**Enums** (1): `RetentionUnit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/retention_unit.proto
// file: metrics/proto/enums/retention_unit.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * RetentionUnit defines the units for data retention policies.
 * Used to specify how long metric data should be kept in storage.
 */
enum RetentionUnit {
  // Unspecified retention unit (default)
  RETENTION_UNIT_UNSPECIFIED = 0;

  // Minutes
  RETENTION_UNIT_MINUTES = 1;

  // Hours
  RETENTION_UNIT_HOURS = 2;

  // Days
  RETENTION_UNIT_DAYS = 3;

  // Weeks
  RETENTION_UNIT_WEEKS = 4;

  // Months
  RETENTION_UNIT_MONTHS = 5;

  // Years
  RETENTION_UNIT_YEARS = 6;

  // Forever (no expiration)
  RETENTION_UNIT_FOREVER = 7;

  // Custom duration (specify in seconds)
  RETENTION_UNIT_CUSTOM = 8;
}

```

---

### sample_rate.proto {#sample_rate}

**Path**: `pkg/metrics/proto/sample_rate.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 46

**Enums** (1): `SampleRate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/sample_rate.proto
// version: 1.0.0
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// SampleRate represents different sampling rates for metrics collection
enum SampleRate {
  // Unspecified sample rate
  SAMPLE_RATE_UNSPECIFIED = 0;

  // Collect every sample (100%)
  SAMPLE_RATE_FULL = 1;

  // Sample at 50% rate
  SAMPLE_RATE_HALF = 2;

  // Sample at 25% rate
  SAMPLE_RATE_QUARTER = 3;

  // Sample at 10% rate
  SAMPLE_RATE_TENTH = 4;

  // Sample at 5% rate
  SAMPLE_RATE_TWENTIETH = 5;

  // Sample at 1% rate
  SAMPLE_RATE_HUNDREDTH = 6;

  // Sample at 0.1% rate
  SAMPLE_RATE_THOUSANDTH = 7;

  // Adaptive sampling (dynamic rate)
  SAMPLE_RATE_ADAPTIVE = 8;

  // Custom sampling rate
  SAMPLE_RATE_CUSTOM = 9;
}

```

---

### scrape_job.proto {#scrape_job}

**Path**: `pkg/metrics/proto/scrape_job.proto` **Package**: `gcommon.v1.metrics`
**Lines**: 35

**Messages** (1): `ScrapeJob`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/scrape_config.proto` →
  [metrics_config](./metrics_config.md#scrape_config)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/scrape_job.proto
// version: 1.1.0
// guid: 4c4b2cc6-1c94-4bd4-9a40-e1e36e1f9d02

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/scrape_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ScrapeJob represents a scheduled scraping task for metrics collection.
 */
message ScrapeJob {
  // Unique identifier for the scrape job
  string job_id = 1;

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

### scrape_status.proto {#scrape_status}

**Path**: `pkg/metrics/proto/scrape_status.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 57

**Enums** (1): `ScrapeStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/scrape_status.proto
// file: metrics/proto/enums/scrape_status.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ScrapeStatus defines the status of metric scraping operations.
 * Used to track the health and success of metric collection from targets.
 */
enum ScrapeStatus {
  // Unspecified scrape status (default)
  SCRAPE_STATUS_UNSPECIFIED = 0;

  // Scrape completed successfully
  SCRAPE_STATUS_SUCCESS = 1;

  // Scrape failed due to network/connection issues
  SCRAPE_STATUS_NETWORK_ERROR = 2;

  // Scrape failed due to authentication/authorization issues
  SCRAPE_STATUS_AUTH_ERROR = 3;

  // Scrape failed due to timeout
  SCRAPE_STATUS_TIMEOUT = 4;

  // Scrape failed due to invalid/malformed response
  SCRAPE_STATUS_PARSE_ERROR = 5;

  // Target is unreachable/down
  SCRAPE_STATUS_TARGET_DOWN = 6;

  // Target returned HTTP error status
  SCRAPE_STATUS_HTTP_ERROR = 7;

  // Scrape was cancelled/aborted
  SCRAPE_STATUS_CANCELLED = 8;

  // Rate limited by target
  SCRAPE_STATUS_RATE_LIMITED = 9;

  // Target configuration is invalid
  SCRAPE_STATUS_CONFIG_ERROR = 10;

  // Scrape is currently in progress
  SCRAPE_STATUS_IN_PROGRESS = 11;
}

```

---

### scrape_target.proto {#scrape_target}

**Path**: `pkg/metrics/proto/scrape_target.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `ScrapeTarget`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/scrape_target.proto
// version: 1.0.0
// guid: bc47b323-f2ec-45a1-9eb1-a02cee44f29d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ScrapeTarget describes a target endpoint to scrape metrics from.
 */
message ScrapeTarget {
  // Target URL
  string url = 1;

  // Optional labels to associate with this target
  map<string, string> labels = 2;
}

```

---

### storage_backend.proto {#storage_backend}

**Path**: `pkg/metrics/proto/storage_backend.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 57

**Enums** (1): `StorageBackend`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/storage_backend.proto
// file: metrics/proto/enums/storage_backend.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StorageBackend defines the types of storage systems available for metrics.
 * Used to specify where metrics should be stored and retrieved from.
 */
enum StorageBackend {
  // Unspecified storage backend (default)
  STORAGE_BACKEND_UNSPECIFIED = 0;

  // In-memory storage (non-persistent, for testing/development)
  STORAGE_BACKEND_MEMORY = 1;

  // Prometheus time-series database
  STORAGE_BACKEND_PROMETHEUS = 2;

  // InfluxDB time-series database
  STORAGE_BACKEND_INFLUXDB = 3;

  // TimescaleDB (PostgreSQL extension for time-series)
  STORAGE_BACKEND_TIMESCALEDB = 4;

  // OpenTelemetry backend (various implementations)
  STORAGE_BACKEND_OPENTELEMETRY = 5;

  // Graphite time-series database
  STORAGE_BACKEND_GRAPHITE = 6;

  // ElasticSearch for metrics storage
  STORAGE_BACKEND_ELASTICSEARCH = 7;

  // CloudWatch (AWS managed metrics)
  STORAGE_BACKEND_CLOUDWATCH = 8;

  // Google Cloud Monitoring
  STORAGE_BACKEND_GCP_MONITORING = 9;

  // Azure Monitor
  STORAGE_BACKEND_AZURE_MONITOR = 10;

  // VictoriaMetrics time-series database
  STORAGE_BACKEND_VICTORIAMETRICS = 11;
}

```

---

### stream_compression.proto {#stream_compression}

**Path**: `pkg/metrics/proto/stream_compression.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 34

**Enums** (1): `StreamCompression`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/stream_compression.proto
// version: 1.0.0
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StreamCompression defines compression options for streaming.
 * Specifies how metrics data should be compressed during streaming.
 */
enum StreamCompression {
  // Unspecified compression
  STREAM_COMPRESSION_UNSPECIFIED = 0;

  // No compression
  STREAM_COMPRESSION_NONE = 1;

  // GZIP compression
  STREAM_COMPRESSION_GZIP = 2;

  // Snappy compression
  STREAM_COMPRESSION_SNAPPY = 3;

  // LZ4 compression
  STREAM_COMPRESSION_LZ4 = 4;
}

```

---

### stream_qos.proto {#stream_qos}

**Path**: `pkg/metrics/proto/stream_qos.proto` **Package**: `gcommon.v1.metrics`
**Lines**: 31

**Enums** (1): `StreamQOS`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/stream_qos.proto
// version: 1.0.0
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * StreamQOS defines quality of service levels for streaming.
 * Specifies delivery guarantees for streaming metrics.
 */
enum StreamQOS {
  // Unspecified QOS level
  STREAM_QOS_UNSPECIFIED = 0;

  // Best effort delivery (fire and forget)
  STREAM_QOS_BEST_EFFORT = 1;

  // At least once delivery guarantee
  STREAM_QOS_AT_LEAST_ONCE = 2;

  // Exactly once delivery guarantee
  STREAM_QOS_EXACTLY_ONCE = 3;
}

```

---

### summary_metric.proto {#summary_metric}

**Path**: `pkg/metrics/proto/summary_metric.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 62

**Messages** (2): `SummaryQuantile`, `SummaryMetric`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/summary_metric.proto
// file: metrics/proto/messages/summary_metric.proto
//
// Summary metric message definition for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message SummaryQuantile {
  // Quantile value (0.0-1.0, e.g., 0.5 for median, 0.95 for 95th percentile)
  double quantile = 1;

  // Value at this quantile
  double value = 2;
}

/**
 * SummaryMetric represents a summary distribution with quantiles.
 * Used for tracking distributions with pre-calculated quantiles.
 */
message SummaryMetric {
  // Metric name (e.g., "http_request_duration_seconds")
  string name = 1;

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

### tag_updates.proto {#tag_updates}

**Path**: `pkg/metrics/proto/tag_updates.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `TagUpdates`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/tag_updates.proto
// version: 1.0.0
// guid: 3f881144-83c6-471b-9db4-227cb066b468

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * TagUpdates contains tag update operations.
 */
message TagUpdates {
  // Tags to add or update
  map<string, string> tag_updates = 1;

  // Tag keys to remove
  repeated string tag_removes = 2;
}

```

---

### time_range.proto {#time_range}

**Path**: `pkg/metrics/proto/time_range.proto` **Package**: `gcommon.v1.metrics`
**Lines**: 25

**Messages** (1): `TimeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/time_range.proto
// version: 1.0.0
// guid: d6e7f8a9-012d-467c-1234-789012345678

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message TimeRange {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;

  // Duration in seconds
  int64 duration_seconds = 3;
}

```

---

### time_series.proto {#time_series}

**Path**: `pkg/metrics/proto/time_series.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `TimeSeries`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/metric_sample.proto` →
  [metrics_1](./metrics_1.md#metric_sample)

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/time_series.proto
// version: 1.0.0
// guid: 0f1e1fe8-f8db-4e8f-8220-628a1b9c02bf

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/metric_sample.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * TimeSeries represents a collection of metric samples over time.
 */
message TimeSeries {
  // Identifier of the metric this series belongs to
  string metric_id = 1;

  // Ordered list of samples
  repeated MetricSample samples = 2;

  // Labels associated with the series
  map<string, string> labels = 3;
}

```

---

### time_unit.proto {#time_unit}

**Path**: `pkg/metrics/proto/time_unit.proto` **Package**: `gcommon.v1.metrics`
**Lines**: 54

**Enums** (1): `TimeUnit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/time_unit.proto
// file: metrics/proto/enums/time_unit.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * TimeUnit defines the units of time for metric intervals, retention, and aggregation.
 * Used throughout the metrics system for temporal operations.
 */
enum TimeUnit {
  // Unspecified time unit (default)
  TIME_UNIT_UNSPECIFIED = 0;

  // Nanoseconds
  TIME_UNIT_NANOSECONDS = 1;

  // Microseconds
  TIME_UNIT_MICROSECONDS = 2;

  // Milliseconds
  TIME_UNIT_MILLISECONDS = 3;

  // Seconds
  TIME_UNIT_SECONDS = 4;

  // Minutes
  TIME_UNIT_MINUTES = 5;

  // Hours
  TIME_UNIT_HOURS = 6;

  // Days
  TIME_UNIT_DAYS = 7;

  // Weeks
  TIME_UNIT_WEEKS = 8;

  // Months
  TIME_UNIT_MONTHS = 9;

  // Years
  TIME_UNIT_YEARS = 10;
}

```

---

### time_window.proto {#time_window}

**Path**: `pkg/metrics/proto/time_window.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 55

**Enums** (1): `TimeWindow`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/time_window.proto
// version: 1.0.0
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// TimeWindow represents different time windows for metrics aggregation
enum TimeWindow {
  // Unspecified time window
  TIME_WINDOW_UNSPECIFIED = 0;

  // 1 minute window
  TIME_WINDOW_1_MINUTE = 1;

  // 5 minute window
  TIME_WINDOW_5_MINUTES = 2;

  // 15 minute window
  TIME_WINDOW_15_MINUTES = 3;

  // 30 minute window
  TIME_WINDOW_30_MINUTES = 4;

  // 1 hour window
  TIME_WINDOW_1_HOUR = 5;

  // 4 hour window
  TIME_WINDOW_4_HOURS = 6;

  // 12 hour window
  TIME_WINDOW_12_HOURS = 7;

  // 1 day window
  TIME_WINDOW_1_DAY = 8;

  // 1 week window
  TIME_WINDOW_1_WEEK = 9;

  // 1 month window
  TIME_WINDOW_1_MONTH = 10;

  // 1 year window
  TIME_WINDOW_1_YEAR = 11;

  // Custom time window
  TIME_WINDOW_CUSTOM = 12;
}

```

---

### timer_metric.proto {#timer_metric}

**Path**: `pkg/metrics/proto/timer_metric.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 101

**Messages** (3): `TimerMetric`, `TimerStatistics`, `PercentileMeasurement`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/messages/timer_metric.proto
// version: 1.0.0
// guid: 8d0f1a2b-7e9c-6f5e-1b0a-9f8e7d6c5b4a

// TimerMetric message definition for timing measurements
//
// This file implements the 1-1-1 pattern: one message per file.
// It defines the TimerMetric message for measuring execution times and latencies.

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// TimerMetric represents timing measurements and latency statistics
//
// This message captures timing information for operations, including
// duration, start/end times, and statistical aggregations.
message TimerMetric {
  // Unique identifier for this timer measurement
  string timer_id = 1;

  // Name or label for this timer (e.g., "api_request_duration")
  string name = 2;

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

// Statistical aggregations for timer measurements
message TimerStatistics {
  // Minimum duration observed
  google.protobuf.Duration min_duration = 1;

  // Maximum duration observed
  google.protobuf.Duration max_duration = 2;

  // Mean (average) duration
  google.protobuf.Duration mean_duration = 3;

  // Standard deviation of durations
  double standard_deviation_ms = 4;

  // Variance of durations
  double variance_ms = 5;

  // Number of samples used for these statistics
  int64 sample_count = 6;

  // Rate of measurements per second
  double rate_per_second = 7;

  // Most recent measurement duration
  google.protobuf.Duration last_duration = 8;
}

// Percentile measurement for timer statistics
message PercentileMeasurement {
  // Percentile value (e.g., 50.0 for median, 95.0 for 95th percentile)
  double percentile = 1;

  // Duration value at this percentile
  google.protobuf.Duration duration = 2;

  // Number of samples at or below this percentile
  int64 sample_count = 3;
}

```

---

### timestamp_range.proto {#timestamp_range}

**Path**: `pkg/metrics/proto/timestamp_range.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `TimestampRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/timestamp_range.proto
// version: 1.0.0
// guid: e7f8a9b0-123e-578d-2345-890123456789

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

message TimestampRange {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;
}

```

---

### top_metrics.proto {#top_metrics}

**Path**: `pkg/metrics/proto/top_metrics.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `TopMetrics`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/top_metrics.proto
// version: 1.0.0
// guid: c4d5e6f7-a8b9-0c1d-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * TopMetrics contains information about top performing/problematic metrics.
 */
message TopMetrics {
  // Most active metrics (by volume)
  repeated string most_active = 1;

  // Largest metrics by data volume
  repeated string largest_by_volume = 2;

  // Metrics with highest error rates
  repeated string highest_errors = 3;

  // Most frequently queried metrics
  repeated string most_queried = 4;

  // Slowest performing metrics
  repeated string slowest_performing = 5;

  // Most resource-intensive metrics
  repeated string most_resource_intensive = 6;
}

```

---

### update_action.proto {#update_action}

**Path**: `pkg/metrics/proto/update_action.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 26

**Enums** (1): `UpdateAction`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/validation_result.proto` →
  [config_2](./config_2.md#validation_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/update_action.proto
// version: 1.0.0
// guid: cb7f4802-67a0-4c44-a5b3-b98fc2aab61a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/validation_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UpdateAction indicates what action was taken during the update.
 */
enum UpdateAction {
  UPDATE_ACTION_UNSPECIFIED = 0;
  UPDATE_ACTION_UPDATED = 1;
  UPDATE_ACTION_NO_CHANGE = 2;
  UPDATE_ACTION_RESTARTED = 3;
  UPDATE_ACTION_RECREATED = 4;
}

```

---

### update_options.proto {#update_options}

**Path**: `pkg/metrics/proto/update_options.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `UpdateOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/update_strategy.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/update_options.proto
// version: 1.0.0
// guid: 5725505d-38a1-4c4b-861e-d159e74202ce

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/update_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UpdateOptions configure the update process.
 */
message UpdateOptions {
  // Whether to validate the configuration before updating
  bool validate_config = 1;

  // Whether to perform a dry run
  bool dry_run = 2;

  // Whether to restart the provider after update (if needed)
  bool restart_if_needed = 3;

  // Whether to backup current configuration before update
  bool backup_config = 4;

  // Update strategy
  UpdateStrategy strategy = 5;
}

```

---

### update_result.proto {#update_result}

**Path**: `pkg/metrics/proto/update_result.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 43

**Messages** (1): `UpdateResult`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/metrics/proto/config_change.proto` →
  [config_config_1](./config_config_1.md#config_change) →
  [metrics_config](./metrics_config.md#config_change)
- `pkg/metrics/proto/update_action.proto`
- `pkg/metrics/proto/validation_result.proto` →
  [config_2](./config_2.md#validation_result)

#### Source Code

```protobuf
// file: pkg/metrics/proto/update_result.proto
// version: 1.1.0
// guid: cd6fac61-b122-455b-a74b-34935efa71b0

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/metrics/proto/config_change.proto";
import "pkg/metrics/proto/update_action.proto";
import "pkg/metrics/proto/validation_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UpdateResult contains information about what was changed.
 */
message UpdateResult {
  // What update action was taken
  UpdateAction action = 1;

  // Configuration changes that were applied
  repeated ConfigChange config_changes = 2;

  // Settings that were updated
  repeated string updated_settings = 3;

  // Settings that were removed
  repeated string removed_settings = 4;

  // Whether a restart occurred
  bool restarted = 5;

  // Update strategy that was used
  string strategy_used = 6;

  // Time taken for the update
  string update_duration = 7;
}

```

---

### update_strategy.proto {#update_strategy}

**Path**: `pkg/metrics/proto/update_strategy.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 24

**Enums** (1): `UpdateStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/update_strategy.proto
// version: 1.0.0
// guid: 33aabd04-d32c-4267-94a4-dca8e8c580ad

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * UpdateStrategy defines how updates should be applied.
 */
enum UpdateStrategy {
  UPDATE_STRATEGY_UNSPECIFIED = 0;
  UPDATE_STRATEGY_ROLLING = 1;
  UPDATE_STRATEGY_BLUE_GREEN = 2;
  UPDATE_STRATEGY_IMMEDIATE = 3;
  UPDATE_STRATEGY_SCHEDULED = 4;
}

```

---

### validation_result.proto {#validation_result}

**Path**: `pkg/metrics/proto/validation_result.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `ValidationResult`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/types/validation_result.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174025

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * ValidationResult contains validation results from creation.
 */
message ValidationResult {
  // Whether the configuration is valid
  bool valid = 1;

  // Validation errors
  repeated string errors = 2;

  // Validation warnings
  repeated string warnings = 3;

  // Configuration suggestions
  repeated string suggestions = 4;
}

```

---

### visualization_type.proto {#visualization_type}

**Path**: `pkg/metrics/proto/visualization_type.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 61

**Enums** (1): `VisualizationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/metrics/proto/enums/visualization_type.proto
// version: 1.0.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

// VisualizationType represents different types of data visualizations
enum VisualizationType {
  // Unspecified visualization type
  VISUALIZATION_TYPE_UNSPECIFIED = 0;

  // Line chart
  VISUALIZATION_TYPE_LINE_CHART = 1;

  // Bar chart
  VISUALIZATION_TYPE_BAR_CHART = 2;

  // Pie chart
  VISUALIZATION_TYPE_PIE_CHART = 3;

  // Area chart
  VISUALIZATION_TYPE_AREA_CHART = 4;

  // Scatter plot
  VISUALIZATION_TYPE_SCATTER_PLOT = 5;

  // Heatmap
  VISUALIZATION_TYPE_HEATMAP = 6;

  // Histogram
  VISUALIZATION_TYPE_HISTOGRAM = 7;

  // Gauge
  VISUALIZATION_TYPE_GAUGE = 8;

  // Table
  VISUALIZATION_TYPE_TABLE = 9;

  // Single stat
  VISUALIZATION_TYPE_SINGLE_STAT = 10;

  // Graph
  VISUALIZATION_TYPE_GRAPH = 11;

  // Worldmap
  VISUALIZATION_TYPE_WORLDMAP = 12;

  // Text panel
  VISUALIZATION_TYPE_TEXT = 13;

  // Custom visualization
  VISUALIZATION_TYPE_CUSTOM = 14;
}

```

---
