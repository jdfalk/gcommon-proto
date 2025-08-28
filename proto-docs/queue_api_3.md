# queue_api_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 31
- **Messages**: 31
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [queue_stats_summary.proto](#queue_stats_summary)
- [reset_details.proto](#reset_details)
- [reset_queue_stats_request.proto](#reset_queue_stats_request)
- [reset_queue_stats_response.proto](#reset_queue_stats_response)
- [restore_error.proto](#restore_error)
- [restore_options.proto](#restore_options)
- [restore_queue_request.proto](#restore_queue_request)
- [restore_queue_response.proto](#restore_queue_response)
- [restore_statistics.proto](#restore_statistics)
- [restore_status.proto](#restore_status)
- [restore_warning.proto](#restore_warning)
- [resume_queue_request.proto](#resume_queue_request)
- [resume_queue_response.proto](#resume_queue_response)
- [seek_request.proto](#seek_request)
- [seek_response.proto](#seek_response)
- [send_message_request.proto](#send_message_request)
- [send_message_response.proto](#send_message_response)
- [start_workflow_request.proto](#start_workflow_request)
- [start_workflow_response.proto](#start_workflow_response)
- [stop_workflow_request.proto](#stop_workflow_request)
- [stop_workflow_response.proto](#stop_workflow_response)
- [stream_messages_request.proto](#stream_messages_request)
- [stream_messages_response.proto](#stream_messages_response)
- [stream_metrics_request.proto](#stream_metrics_request)
- [subscribe_request.proto](#subscribe_request)
- [subscribe_response.proto](#subscribe_response)
- [unsubscribe_request.proto](#unsubscribe_request)
- [unsubscribe_response.proto](#unsubscribe_response)
- [update_condition.proto](#update_condition)
- [update_message_request.proto](#update_message_request)
- [update_message_response.proto](#update_message_response)
---


## Detailed Documentation

### queue_stats_summary.proto {#queue_stats_summary}

**Path**: `gcommon/v1/queue/queue_stats_summary.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `QueueStatsSummary`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats_summary.proto
// version: 1.0.0
// guid: beb6cfcc-70db-4a5a-9ec1-2e241e98f71f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStatsSummary {
  // Total number of queues
  int64 total_queues = 1 [(buf.validate.field).int64.gte = 0];

  // Total messages across all queues
  int64 total_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Total messages processed in the last hour
  int64 messages_processed_last_hour = 3 [(buf.validate.field).int64.gte = 0];

  // Average processing time across all queues
  google.protobuf.Duration average_processing_time = 4;

  // Overall system health score (0-100)
  int32 health_score = 5 [(buf.validate.field).int32.gte = 0];

  // Total active consumers
  int64 active_consumers = 6 [(buf.validate.field).int64.gte = 0];

  // Total storage used by messages
  int64 total_storage_bytes = 7 [(buf.validate.field).int64.gte = 0];
}
```

---

### reset_details.proto {#reset_details}

**Path**: `gcommon/v1/queue/reset_details.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `ResetDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/reset_details.proto
// version: 1.0.0
// guid: b0e2cbdc-ca09-41a1-81b3-771cf6e15072

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResetDetails {
  // Number of metrics reset
  int32 metrics_reset_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of counters reset
  int32 counters_reset_count = 2 [(buf.validate.field).int32.gte = 0];

  // Number of histograms reset
  int32 histograms_reset_count = 3 [(buf.validate.field).int32.gte = 0];

  // Number of partitions affected
  int32 partitions_affected = 4 [(buf.validate.field).int32.gte = 0];

  // Time taken to complete reset (milliseconds)
  int64 reset_duration_ms = 5 [(buf.validate.field).int64.gt = 0];

  // Whether reset was partial or complete
  bool partial_reset = 6;

  // Reason for reset operation
  string reset_reason = 7 [(buf.validate.field).string.min_len = 1];

  // User or system that initiated reset
  string initiated_by = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### reset_queue_stats_request.proto {#reset_queue_stats_request}

**Path**: `gcommon/v1/queue/reset_queue_stats_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `ResetQueueStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/reset_queue_stats_request.proto
// version: 1.0.0
// guid: d2059a85-daa1-4c7e-85c1-e55409000e9d
// Request to reset queue statistics

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to reset queue statistics
message ResetQueueStatsRequest {
  // Queue name to reset stats for
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reset specific stat types (empty means reset all)
  repeated string stat_types = 2;

  // Reset stats for specific partitions only
  repeated int32 partition_ids = 3;

  // Preserve historical data before this timestamp
  int64 preserve_before_timestamp = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}
```

---

### reset_queue_stats_response.proto {#reset_queue_stats_response}

**Path**: `gcommon/v1/queue/reset_queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `ResetQueueStatsResponse`

**Imports** (5):

- `gcommon/v1/queue/preserved_stats.proto`
- `gcommon/v1/queue/reset_details.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/reset_queue_stats_response.proto
// version: 1.0.0
// guid: 11f82fe8-4d3f-4188-b0c9-4fb2a7d24591

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/preserved_stats.proto";
import "gcommon/v1/queue/reset_details.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResetQueueStatsResponse {
  // Success status of the reset operation
  bool success = 1;

  // Queue identifier whose stats were reset
  string queue_id = 2 [(buf.validate.field).string.min_len = 1];

  // Timestamp when reset operation completed
  google.protobuf.Timestamp reset_at = 3;

  // Statistics that were preserved before reset
  PreservedStats preserved_stats = 4;

  // Types of statistics that were reset
  repeated string reset_stat_types = 5 [(buf.validate.field).repeated.min_items = 1];

  // Types of statistics that were preserved
  repeated string preserved_stat_types = 6 [(buf.validate.field).repeated.min_items = 1];

  // Error message if reset failed
  string error_message = 7 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 8 [(buf.validate.field).string.min_len = 1];

  // Warning messages about the reset operation
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Reset operation details
  ResetDetails reset_details = 10;

  // Operation metadata
  map<string, string> metadata = 11;
}
```

---

### restore_error.proto {#restore_error}

**Path**: `gcommon/v1/queue/restore_error.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `RestoreError`

**Imports** (4):

- `gcommon/v1/queue/offset_range.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_error.proto
// version: 1.0.0
// guid: 9b5c3655-3a8b-40fa-ab5d-ddcec3f98462

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/offset_range.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreError {
  // Error code for programmatic handling
  string error_code = 1 [(buf.validate.field).string.min_len = 1];

  // Human-readable error message
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Error category (validation, io, corruption, etc.)
  string error_category = 3 [(buf.validate.field).string.min_len = 1];

  // Specific component that failed
  string failed_component = 4 [(buf.validate.field).string.min_len = 1];

  // Partition ID if error is partition-specific
  int32 partition_id = 5 [(buf.validate.field).int32.gte = 0];

  // Message offset range affected by error
  OffsetRange affected_range = 6;

  // Error timestamp
  google.protobuf.Timestamp error_time = 7;

  // Whether error is recoverable
  bool recoverable = 8;
}
```

---

### restore_options.proto {#restore_options}

**Path**: `gcommon/v1/queue/restore_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `RestoreOptions`

**Imports** (6):

- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/queue/filter_criteria.proto`
- `gcommon/v1/queue/offset_range.proto`
- `gcommon/v1/queue/performance_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_options.proto
// version: 1.0.0
// guid: 5747b00e-cec5-49aa-adb9-514b7eefc3c4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/queue/filter_criteria.proto";
import "gcommon/v1/queue/offset_range.proto";
import "gcommon/v1/queue/performance_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreOptions {
  // Skip message content (restore structure only)
  bool skip_message_content = 1;

  // Restore message metadata only
  bool metadata_only = 2;

  // Maximum number of messages to restore
  int64 max_messages = 3 [(buf.validate.field).int64.gte = 0];

  // Restore messages from specific offset range
  OffsetRange offset_range = 4;

  // Restore messages within time range
  // Time range for restore
  gcommon.v1.common.TimeRangeMetrics time_range = 5;

  // Restore specific message priorities
  repeated int32 priority_levels = 6 [(buf.validate.field).repeated.min_items = 1];

  // Include/exclude patterns for message filtering
  FilterCriteria filter_criteria = 7;

  // Performance tuning options
  PerformanceOptions performance = 8;
}
```

---

### restore_queue_request.proto {#restore_queue_request}

**Path**: `gcommon/v1/queue/restore_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `RestoreQueueRequest`

**Imports** (6):

- `gcommon/v1/queue/backup_source.proto`
- `gcommon/v1/queue/restore_config.proto`
- `gcommon/v1/queue/restore_options.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_queue_request.proto
// version: 1.0.0
// guid: 8dbc0f2d-31af-48e8-9785-3d801a7d7e95

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/backup_source.proto";
import "gcommon/v1/queue/restore_config.proto";
import "gcommon/v1/queue/restore_options.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreQueueRequest {
  // Target queue identifier for restoration
  string target_queue_id = 1 [(buf.validate.field).string.min_len = 1];

  // Backup source information
  BackupSource backup_source = 2;

  // Restoration configuration
  RestoreConfig restore_config = 3;

  // Restore to specific point in time
  google.protobuf.Timestamp restore_point = 4;

  // Overwrite existing queue if it exists
  bool overwrite_existing = 5;

  // Validate backup integrity before restore
  bool validate_backup = 6;

  // Restore only specific partitions (empty = all partitions)
  repeated int32 partition_ids = 7 [(buf.validate.field).repeated.min_items = 1];

  // Restore options
  RestoreOptions options = 8;

  // Operation metadata
  map<string, string> metadata = 9;
}
```

---

### restore_queue_response.proto {#restore_queue_response}

**Path**: `gcommon/v1/queue/restore_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 63

**Messages** (1): `RestoreQueueResponse`

**Imports** (10):

- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/queue/partition_restore_result.proto`
- `gcommon/v1/queue/restore_error.proto`
- `gcommon/v1/queue/restore_statistics.proto`
- `gcommon/v1/queue/restore_status.proto`
- `gcommon/v1/queue/restore_warning.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_queue_response.proto
// version: 1.0.0
// guid: 949d5078-96a1-43dd-adb1-5e57d6a82a57

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/queue/partition_restore_result.proto";
import "gcommon/v1/queue/restore_error.proto";
import "gcommon/v1/queue/restore_statistics.proto";
import "gcommon/v1/queue/restore_status.proto";
import "gcommon/v1/queue/restore_warning.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreQueueResponse {
  // Operation success status
  bool success = 1;

  // Restore operation ID for tracking
  string operation_id = 2 [(buf.validate.field).string.min_len = 1];

  // Restored queue identifier
  string restored_queue_id = 3 [(buf.validate.field).string.min_len = 1];

  // Restoration start timestamp
  google.protobuf.Timestamp start_time = 4;

  // Restoration completion timestamp
  google.protobuf.Timestamp completion_time = 5;

  // Total restoration duration
  google.protobuf.Duration duration = 6;

  // Restoration statistics
  RestoreStatistics statistics = 7;

  // Restoration status details
  RestoreStatus status = 8;

  // Any errors encountered during restore
  repeated RestoreError errors = 9 [(buf.validate.field).repeated.min_items = 1];

  // Warnings generated during restore
  repeated RestoreWarning warnings = 10 [(buf.validate.field).repeated.min_items = 1];

  // Partition restoration results
  repeated PartitionRestoreResult partition_results = 11 [(buf.validate.field).repeated.min_items = 1];

  // Validation results if validation was requested
  gcommon.v1.common.MetricsValidationResult validation_result = 12;

  // Operation metadata
  map<string, string> metadata = 13;
}
```

---

### restore_statistics.proto {#restore_statistics}

**Path**: `gcommon/v1/queue/restore_statistics.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `RestoreStatistics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_statistics.proto
// version: 1.0.0
// guid: f83290f6-3fb7-42fe-9473-6cf7028461e1

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreStatistics {
  // Total messages restored
  int64 messages_restored = 1 [(buf.validate.field).int64.gte = 0];

  // Total bytes restored
  int64 bytes_restored = 2 [(buf.validate.field).int64.gte = 0];

  // Number of partitions restored
  int32 partitions_restored = 3 [(buf.validate.field).int32.gte = 0];

  // Messages skipped due to filters
  int64 messages_skipped = 4 [(buf.validate.field).int64.gte = 0];

  // Messages failed to restore
  int64 messages_failed = 5 [(buf.validate.field).int64.gte = 0];

  // Average restore rate (messages/second)
  double restore_rate = 6 [(buf.validate.field).double.gte = 0.0];

  // Throughput (bytes/second)
  double throughput_bps = 7 [(buf.validate.field).double.gte = 0.0];

  // Backup file size processed
  int64 backup_size_bytes = 8 [(buf.validate.field).int64.gte = 0];

  // Compression ratio achieved
  double compression_ratio = 9 [(buf.validate.field).double.gte = 0.0];
}
```

---

### restore_status.proto {#restore_status}

**Path**: `gcommon/v1/queue/restore_status.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `RestoreStatus`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_status.proto
// version: 1.0.0
// guid: 49efaefe-393a-43b4-8e5e-af25695292fc

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreStatus {
  // Status code (pending, in_progress, completed, failed, cancelled)
  string status_code = 1 [(buf.validate.field).string.min_len = 1];

  // Human-readable status message
  string status_message = 2 [(buf.validate.field).string.min_len = 1];

  // Progress percentage (0-100)
  int32 progress_percentage = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Current operation phase
  string current_phase = 4 [(buf.validate.field).string.min_len = 1];

  // Estimated time remaining
  google.protobuf.Duration estimated_remaining = 5;

  // Last status update timestamp
  google.protobuf.Timestamp last_update = 6;
}
```

---

### restore_warning.proto {#restore_warning}

**Path**: `gcommon/v1/queue/restore_warning.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `RestoreWarning`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_warning.proto
// version: 1.0.0
// guid: 97e72ea7-3c16-4e40-8dba-5845c294bf28

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreWarning {
  // Warning code
  string warning_code = 1 [(buf.validate.field).string.min_len = 1];

  // Warning message
  string warning_message = 2 [(buf.validate.field).string.min_len = 1];

  // Warning category
  string warning_category = 3 [(buf.validate.field).string.min_len = 1];

  // Affected component
  string affected_component = 4 [(buf.validate.field).string.min_len = 1];

  // Partition ID if warning is partition-specific
  int32 partition_id = 5 [(buf.validate.field).int32.gte = 0];

  // Warning timestamp
  google.protobuf.Timestamp warning_time = 6;
}
```

---

### resume_queue_request.proto {#resume_queue_request}

**Path**: `gcommon/v1/queue/resume_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `ResumeQueueRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resume_queue_request.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to resume a paused queue.
 * Restarts message processing for a previously paused queue.
 */
message ResumeQueueRequest {
  // Name of the queue to resume
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reason for resuming the queue
  string reason = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;

  // Whether to resume specific partitions only
  repeated int32 partition_ids = 4;

  // Whether to start processing from where it left off
  bool resume_from_last_position = 5;
}
```

---

### resume_queue_response.proto {#resume_queue_response}

**Path**: `gcommon/v1/queue/resume_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 58

**Messages** (1): `ResumeQueueResponse`

**Imports** (5):

- `gcommon/v1/common/queue_state.proto`
- `gcommon/v1/queue/resume_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resume_queue_response.proto
// version: 1.0.0
// guid: 43e76b2f-3350-49a8-b002-e38b946919ad

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/queue_state.proto";
import "gcommon/v1/queue/resume_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResumeQueueResponse {
  // Success status of the resume operation
  bool success = 1;

  // Queue identifier that was resumed
  string queue_id = 2 [(buf.validate.field).string.min_len = 1];

  // Previous queue state before resume
  gcommon.v1.common.QueueState previous_state = 3;

  // Current queue state after resume
  gcommon.v1.common.QueueState current_state = 4;

  // Timestamp when resume operation completed
  google.protobuf.Timestamp resumed_at = 5;

  // Duration the queue was paused (milliseconds)
  int64 pause_duration_ms = 6 [(buf.validate.field).int64.gt = 0];

  // Messages that were queued during pause
  int64 messages_queued_during_pause = 7 [(buf.validate.field).int64.gte = 0];

  // Consumer groups affected by resume
  repeated string affected_consumer_groups = 8 [(buf.validate.field).repeated.min_items = 1];

  // Error message if resume failed
  string error_message = 9 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 10 [(buf.validate.field).string.min_len = 1];

  // Warning messages about resume operation
  repeated string warnings = 11 [(buf.validate.field).repeated.min_items = 1];

  // Resume operation statistics
  ResumeStats resume_stats = 12;

  // Operation metadata
  map<string, string> metadata = 13;
}
```

---

### seek_request.proto {#seek_request}

**Path**: `gcommon/v1/queue/seek_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 58

**Messages** (1): `SeekRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/seek_request.proto
// file: proto/gcommon/v1/queue/seek_request.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to seek to a specific position in a queue or topic.
 * Used for replaying messages from a particular point in time or offset.
 */
message SeekRequest {
  // Name of the queue or topic to seek within
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Subscription name (for topics with multiple subscribers)
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Seek position specification
  oneof seek_position {
    // Seek to a specific timestamp
    google.protobuf.Timestamp timestamp = 3;

    // Seek to a specific message offset/position
    int64 offset = 4;

    // Seek to the beginning of the queue
    bool beginning = 5;

    // Seek to the end of the queue (latest message)
    bool end = 6;

    // Seek to a specific message ID
    string message_id = 7;
  }

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
// This file needs proper implementation
```

---

### seek_response.proto {#seek_response}

**Path**: `gcommon/v1/queue/seek_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `SeekResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/seek_response.proto
// version: 1.0.0
// guid: d1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for seek operations on a queue.
 * Contains the result of attempting to seek to a specific position.
 */
message SeekResponse {
  // Whether the seek operation was successful
  bool success = 1;

  // The actual position seeked to
  int64 position = 2 [(buf.validate.field).int64.gte = 0];

  // The offset within the partition (for partitioned queues)
  int64 offset = 3 [(buf.validate.field).int64.gte = 0];

  // The partition ID (for partitioned queues)
  int32 partition_id = 4 [(buf.validate.field).int32.gte = 0];

  // Error message if seek failed
  string error_message = 5 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 6;
}
```

---

### send_message_request.proto {#send_message_request}

**Path**: `gcommon/v1/queue/send_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `SendMessageRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/delivery_options.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/send_message_request.proto
// version: 1.0.0
// guid: 0acd1eb1-8464-4f9c-8fd2-0562acde190f
// SendMessageRequest sends a single message to a queue.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/delivery_options.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SendMessageRequest {
  // Name of the target queue.
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Message to be enqueued.
  QueueMessage message = 2;

  // Optional delivery parameters.
  DeliveryOptions delivery_options = 3;

  // Standard request metadata.
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### send_message_response.proto {#send_message_response}

**Path**: `gcommon/v1/queue/send_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `SendMessageResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/send_message_response.proto
// version: 1.0.0
// guid: 2bbac133-fc81-4653-a03a-e5227ae81d4e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// SendMessageResponse contains the result of a send operation.
message SendMessageResponse {
  // Identifier of the queued message.
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the send operation succeeded.
  bool success = 2;

  // Position in the queue if known.
  int64 queue_position = 3 [(buf.validate.field).int64.gte = 0];

  // Error information when `success` is false.
  gcommon.v1.common.Error error = 4;
}
```

---

### start_workflow_request.proto {#start_workflow_request}

**Path**: `gcommon/v1/queue/start_workflow_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `StartWorkflowRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/start_workflow_request.proto
// version: 1.0.0
// guid: 2f3e4d5c-6b7a-8190-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StartWorkflowRequest defines the request for starting a workflow.
 */
message StartWorkflowRequest {
  // Workflow identifier
  string workflow_id = 1 [(buf.validate.field).string.min_len = 1];

  // Workflow definition or template
  string workflow_definition = 2 [(buf.validate.field).string.min_len = 1];

  // Input parameters for the workflow
  map<string, string> parameters = 3;
}
```

---

### start_workflow_response.proto {#start_workflow_response}

**Path**: `gcommon/v1/queue/start_workflow_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `StartWorkflowResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/start_workflow_response.proto
// version: 1.0.0
// guid: 3f4e5d6c-7b8a-9201-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StartWorkflowResponse defines the response from starting a workflow.
 */
message StartWorkflowResponse {
  // Workflow execution ID
  string execution_id = 1 [(buf.validate.field).string.min_len = 1];

  // Status of the workflow start
  string status = 2 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_workflow_request.proto {#stop_workflow_request}

**Path**: `gcommon/v1/queue/stop_workflow_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `StopWorkflowRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stop_workflow_request.proto
// version: 1.0.0
// guid: 4f5e6d7c-8b9a-0312-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StopWorkflowRequest defines the request for stopping a workflow.
 */
message StopWorkflowRequest {
  // Workflow execution ID
  string execution_id = 1 [(buf.validate.field).string.min_len = 1];

  // Reason for stopping
  string reason = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_workflow_response.proto {#stop_workflow_response}

**Path**: `gcommon/v1/queue/stop_workflow_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `StopWorkflowResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stop_workflow_response.proto
// version: 1.0.0
// guid: 5f6e7d8c-9b0a-1423-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StopWorkflowResponse defines the response from stopping a workflow.
 */
message StopWorkflowResponse {
  // Status of the workflow stop
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### stream_messages_request.proto {#stream_messages_request}

**Path**: `gcommon/v1/queue/stream_messages_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 62

**Messages** (1): `StreamMessagesRequest`

**Imports** (6):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/queue/message_filter.proto`
- `gcommon/v1/queue/offset_config.proto`
- `gcommon/v1/queue/stream_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stream_messages_request.proto
// version: 1.0.0
// guid: 8571acf9-5131-45f6-b0ad-b227ce7f2980

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/queue/message_filter.proto";
import "gcommon/v1/queue/offset_config.proto";
import "gcommon/v1/queue/stream_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message StreamMessagesRequest {
  // Topic or queue identifier to stream from
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer group ID for coordinated consumption
  string consumer_group_id = 2 [(buf.validate.field).string.min_len = 1];

  // Individual consumer ID within the group
  string consumer_id = 3 [(buf.validate.field).string.min_len = 1];

  // Starting offset configuration
  OffsetConfig offset_config = 4;

  // Maximum number of messages to stream
  int64 max_messages = 5 [(buf.validate.field).int64.gte = 0];

  // Maximum time to keep stream open (milliseconds)
  int32 stream_timeout_ms = 6 [(buf.validate.field).int32.gt = 0];

  // Acknowledgment level required
  gcommon.v1.common.AckLevel ack_level = 7;

  // Batch size for message delivery
  int32 batch_size = 8 [(buf.validate.field).int32.gte = 0];

  // Message filter criteria
  MessageFilter filter = 9;

  // Auto-acknowledge messages after delivery
  bool auto_acknowledge = 10;

  // Pause stream on error
  bool pause_on_error = 11;

  // Include message metadata in stream
  bool include_metadata = 12;

  // Specific partition IDs to stream from (empty = all partitions)
  repeated int32 partition_ids = 13 [(buf.validate.field).repeated.min_items = 1];

  // Stream configuration options
  StreamConfig stream_config = 14;
}
```

---

### stream_messages_response.proto {#stream_messages_response}

**Path**: `gcommon/v1/queue/stream_messages_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `StreamMessagesResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/stream_messages_response.proto
// file: proto/gcommon/v1/queue/stream_messages_response.proto
// version: 1.0.0
// guid: 4c5d6e7f-8a9b-0c1d-2e3f-4a5b6c7d8e9f
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for streaming messages from a queue.
 */
message StreamMessagesResponse {
  // List of messages in the stream
  repeated QueueMessage messages = 1 [(buf.validate.field).repeated.min_items = 1];

  // Whether there are more messages available
  bool has_more = 2;

  // Continuation token for next batch
  string continuation_token = 3 [(buf.validate.field).string.min_len = 1];

  // Total number of messages available
  uint64 total_messages = 4 [(buf.validate.field).uint64.gte = 0];

  // Current stream position
  uint64 stream_position = 5 [(buf.validate.field).uint64.gte = 0];

  // Whether the stream has ended
  bool stream_ended = 6;
}
```

---

### stream_metrics_request.proto {#stream_metrics_request}

**Path**: `gcommon/v1/queue/stream_metrics_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `QueueStreamMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/metric_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stream_metrics_request.proto
// version: 1.0.0
// guid: 7ec20686-7f14-4488-9222-e6d189b494fe

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metric_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStreamMetricsRequest {
  // Queue names to monitor (empty = all queues)
  repeated string queue_names = 1 [(buf.validate.field).repeated.min_items = 1];

  // Types of metrics to include
  repeated gcommon.v1.common.MetricsMetricType metric_types = 2 [(buf.validate.field).repeated.min_items = 1];

  // Streaming interval in seconds
  int32 interval_seconds = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### subscribe_request.proto {#subscribe_request}

**Path**: `gcommon/v1/queue/subscribe_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `QueueSubscribeRequest`

**Imports** (6):

- `gcommon/v1/queue/delivery_configuration.proto`
- `gcommon/v1/queue/error_handling_config.proto`
- `gcommon/v1/queue/message_filter_config.proto`
- `gcommon/v1/queue/subscription_configuration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscribe_request.proto
// version: 1.0.0
// guid: 6a573217-0297-4408-bcce-72b9172dd071

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/delivery_configuration.proto";
import "gcommon/v1/queue/error_handling_config.proto";
import "gcommon/v1/queue/message_filter_config.proto";
import "gcommon/v1/queue/subscription_configuration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueSubscribeRequest {
  // Topic or queue to subscribe to
  string topic = 1;

  // Subscription name/identifier
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Consumer group ID for coordinated consumption
  string consumer_group_id = 3;

  // Individual consumer ID
  string consumer_id = 4;

  // Subscription configuration
  SubscriptionConfiguration config = 5;

  // Message filtering criteria
  MessageFilterConfig filter_config = 6;

  // Delivery configuration
  DeliveryConfiguration delivery_config = 7;

  // Error handling configuration
  ErrorHandlingConfig error_handling = 8;

  // Subscription metadata
  map<string, string> metadata = 9;
}
```

---

### subscribe_response.proto {#subscribe_response}

**Path**: `gcommon/v1/queue/subscribe_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `SubscribeResponse`

**Imports** (5):

- `gcommon/v1/queue/connection_details.proto`
- `gcommon/v1/queue/partition_offset.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscribe_response.proto
// version: 1.0.0
// guid: 0d059538-5ecd-4438-9e3e-8aca86b7cf82
// Response for queue subscription with messages

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/connection_details.proto";
import "gcommon/v1/queue/partition_offset.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for subscription requests
message SubscribeResponse {
  // Message data
  QueueMessage message = 1;

  // Partition assignment info
  PartitionOffset partition_offset = 2;

  // Connection details for streaming
  ConnectionDetails connection_details = 3;

  // Subscription ID
  string subscription_id = 4 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### unsubscribe_request.proto {#unsubscribe_request}

**Path**: `gcommon/v1/queue/unsubscribe_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `QueueUnsubscribeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/unsubscribe_request.proto
// version: 1.0.0
// guid: 69c55038-151d-4d97-a390-6bf4dc28d4aa
// Request to unsubscribe from a topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to unsubscribe from a topic
message QueueUnsubscribeRequest {
  // Subscription ID to unsubscribe
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer group ID
  string consumer_group_id = 2 [(buf.validate.field).string.min_len = 1];

  // Force unsubscribe even if messages are pending
  bool force = 3;

  // Close underlying connections
  bool close_connections = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### unsubscribe_response.proto {#unsubscribe_response}

**Path**: `gcommon/v1/queue/unsubscribe_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `UnsubscribeResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/unsubscribe_response.proto
// file: proto/gcommon/v1/queue/unsubscribe_response.proto
// version: 1.0.0
// guid: 5a4b3c2d-1e0f-9a8b-7c6d-5e4f3a2b1c0d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for unsubscription operations.
 */
message UnsubscribeResponse {
  // Whether the unsubscription was successful
  bool success = 1;

  // Name of the subscription that was removed
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Timestamp when the unsubscription occurred
  google.protobuf.Timestamp unsubscribed_at = 3;

  // Number of pending messages that were lost due to unsubscription
  int64 lost_messages = 4;

  // Any warnings related to the unsubscription
  repeated string warnings = 5;
}
// This file needs proper implementation
```

---

### update_condition.proto {#update_condition}

**Path**: `gcommon/v1/queue/update_condition.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `UpdateCondition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_condition.proto
// version: 1.0.0
// guid: a5897f37-2d03-405d-b7c0-dc980257f2b4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateCondition {
  // Expected current version/etag
  string expected_version = 1 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Expected current state
  string expected_state = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum age for update (seconds)
  int64 max_age_seconds = 3 [(buf.validate.field).int64.gte = 0];

  // Update only if message hasn't been delivered
  bool only_if_not_delivered = 4;

  // Update only if message is visible
  bool only_if_visible = 5;

  // Custom condition expression
  string condition_expression = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_message_request.proto {#update_message_request}

**Path**: `gcommon/v1/queue/update_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 58

**Messages** (1): `UpdateMessageRequest`

**Imports** (8):

- `gcommon/v1/queue/content_update.proto`
- `gcommon/v1/queue/message_update_properties.proto`
- `gcommon/v1/queue/metadata_update.proto`
- `gcommon/v1/queue/priority_update.proto`
- `gcommon/v1/queue/update_condition.proto`
- `gcommon/v1/queue/visibility_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_message_request.proto
// version: 1.0.0
// guid: 78c4ac61-c4dc-4bfc-bfa1-93a723303fbb

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/content_update.proto";
import "gcommon/v1/queue/message_update_properties.proto";
import "gcommon/v1/queue/metadata_update.proto";
import "gcommon/v1/queue/priority_update.proto";
import "gcommon/v1/queue/update_condition.proto";
import "gcommon/v1/queue/visibility_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateMessageRequest {
  // Message identifier to update
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Topic or queue containing the message
  string topic = 2 [(buf.validate.field).string.min_len = 1];

  // Partition ID (if applicable)
  int32 partition_id = 3 [(buf.validate.field).int32.gte = 0];

  // Message offset (for precise identification)
  int64 message_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Updated message properties
  MessageUpdateProperties properties = 5;

  // Update visibility timeout for the message
  VisibilityUpdate visibility_update = 6;

  // Update message priority
  PriorityUpdate priority_update = 7;

  // Update message metadata
  MetadataUpdate metadata_update = 8;

  // Update message content (if allowed)
  ContentUpdate content_update = 9;

  // Specify which fields to update
  repeated string update_fields = 10 [(buf.validate.field).repeated.min_items = 1];

  // Conditional update based on current state
  UpdateCondition condition = 11;

  // Update operation metadata
  map<string, string> operation_metadata = 12;
}
```

---

### update_message_response.proto {#update_message_response}

**Path**: `gcommon/v1/queue/update_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `UpdateMessageResponse`

**Imports** (5):

- `gcommon/v1/queue/failed_field_update.proto`
- `gcommon/v1/queue/updated_properties.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_message_response.proto
// version: 1.0.0
// guid: f8af2c52-28d1-49c0-9813-a87e5f5a411d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/failed_field_update.proto";
import "gcommon/v1/queue/updated_properties.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateMessageResponse {
  // Success status of the update operation
  bool success = 1;

  // Updated message identifier
  string message_id = 2 [(buf.validate.field).string.min_len = 1];

  // New message version/etag after update
  string new_version = 3 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Timestamp when update was applied
  google.protobuf.Timestamp updated_at = 4;

  // Fields that were successfully updated
  repeated string updated_fields = 5 [(buf.validate.field).repeated.min_items = 1];

  // Fields that failed to update
  repeated FailedFieldUpdate failed_fields = 6 [(buf.validate.field).repeated.min_items = 1];

  // Error message if update failed
  string error_message = 7 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 8 [(buf.validate.field).string.min_len = 1];

  // Warning messages for partial updates
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Updated message properties summary
  UpdatedProperties updated_properties = 10;

  // Operation metadata
  map<string, string> metadata = 11;
}
```

---

