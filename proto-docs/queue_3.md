# queue_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 17
- **Messages**: 17
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [subscription_stats.proto](#subscription_stats)
- [sync_replication.proto](#sync_replication)
- [throughput_metrics.proto](#throughput_metrics)
- [time_range.proto](#time_range)
- [time_range_filter.proto](#time_range_filter)
- [timestamp_range.proto](#timestamp_range)
- [tls_auth.proto](#tls_auth)
- [topic_info.proto](#topic_info)
- [topic_permissions.proto](#topic_permissions)
- [topic_stats.proto](#topic_stats)
- [updated_properties.proto](#updated_properties)
- [username_password_auth.proto](#username_password_auth)
- [validation_error.proto](#validation_error)
- [validation_result.proto](#validation_result)
- [visibility_update.proto](#visibility_update)
- [workflow.proto](#workflow)
- [write_consistency.proto](#write_consistency)
---


## Detailed Documentation

### subscription_stats.proto {#subscription_stats}

**Path**: `gcommon/v1/queue/subscription_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `SubscriptionStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/subscription_stats.proto
// file: proto/gcommon/v1/queue/subscription_stats.proto
// version: 1.0.0
// guid: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics for a subscription.
 */
message SubscriptionStats {
  // Subscription identifier
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Number of messages consumed
  uint64 messages_consumed = 2 [(buf.validate.field).uint64.gte = 0];

  // Number of messages acknowledged
  uint64 messages_acknowledged = 3 [(buf.validate.field).uint64.gte = 0];

  // Number of messages rejected/nacked
  uint64 messages_rejected = 4 [(buf.validate.field).uint64.gte = 0];

  // Current lag (unprocessed messages)
  uint64 consumer_lag = 5 [(buf.validate.field).uint64.gte = 0];

  // Messages per second consumption rate
  double consumption_rate = 6 [(buf.validate.field).double.gte = 0.0];

  // Average processing time per message (milliseconds)
  double avg_processing_time_ms = 7 [(buf.validate.field).double.gte = 0.0];

  // Number of active consumers
  uint32 active_consumers = 8 [(buf.validate.field).uint32.gte = 0];

  // Last activity timestamp
  uint64 last_activity_time = 9 [(buf.validate.field).uint64.gte = 0];
}
```

---

### sync_replication.proto {#sync_replication}

**Path**: `gcommon/v1/queue/sync_replication.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `SyncReplication`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/sync_replication.proto
// version: 1.0.0
// guid: fb10fe6a-cf7a-47e7-9be7-c31f4e37b22e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SyncReplication {
  // Enable synchronous replication
  bool enabled = 1;

  // Minimum synchronous replicas
  int32 min_sync_replicas = 2 [(buf.validate.field).int32.gte = 0];

  // Timeout for synchronous replication (milliseconds)
  int32 sync_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Fallback to async on timeout
  bool fallback_to_async = 4;
}
```

---

### throughput_metrics.proto {#throughput_metrics}

**Path**: `gcommon/v1/queue/throughput_metrics.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `ThroughputMetrics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/throughput_metrics.proto
// version: 1.0.0
// guid: 238519f5-1808-4bcc-9cd5-e5700aca75e4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ThroughputMetrics {
  // Messages per second over different time windows
  double messages_per_second_1m = 1 [(buf.validate.field).double.gte = 0.0];
  double messages_per_second_5m = 2 [(buf.validate.field).double.gte = 0.0];
  double messages_per_second_15m = 3 [(buf.validate.field).double.gte = 0.0];
  double messages_per_second_1h = 4 [(buf.validate.field).double.gte = 0.0];

  // Peak throughput observed
  double peak_messages_per_second = 5 [(buf.validate.field).double.gte = 0.0];
  google.protobuf.Timestamp peak_timestamp = 6;
}
```

---

### time_range.proto {#time_range}

**Path**: `gcommon/v1/queue/time_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `QueueTimeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/time_range.proto
// file: proto/gcommon/v1/queue/time_range.proto
// version: 1.0.1
// guid: 2a1b0c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Time range for filtering messages.
 */
message QueueTimeRange {
  // Start time (inclusive)
  google.protobuf.Timestamp start_time = 1;

  // End time (exclusive)
  google.protobuf.Timestamp end_time = 2;
}
```

---

### time_range_filter.proto {#time_range_filter}

**Path**: `gcommon/v1/queue/time_range_filter.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `TimeRangeFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/time_range_filter.proto
// version: 1.0.0
// guid: a130528f-ed39-48b7-8dbf-b82f4db21916

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TimeRangeFilter {
  // Start time for the range (ISO 8601)
  string start_time = 1 [(buf.validate.field).string.min_len = 1];

  // End time for the range (ISO 8601)
  string end_time = 2 [(buf.validate.field).string.min_len = 1];

  // Granularity for aggregated data (minute, hour, day)
  string granularity = 3 [(buf.validate.field).string.min_len = 1];

  // Maximum number of data points to return
  int32 max_data_points = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### timestamp_range.proto {#timestamp_range}

**Path**: `gcommon/v1/queue/timestamp_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `QueueTimestampRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/timestamp_range.proto
// version: 1.0.1
// guid: 4fdb7c93-4616-4db9-a2d6-50f41676b4b6

// TimestampRange defines a start and end time for filtering or
// statistics queries. This implementation replaces the placeholder
// added during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// TimestampRange is used to specify a time window when querying
// statistics or messages.
message QueueTimestampRange {
  // Start of the range (inclusive).
  google.protobuf.Timestamp start = 1;

  // End of the range (exclusive).
  google.protobuf.Timestamp end = 2;
}
```

---

### tls_auth.proto {#tls_auth}

**Path**: `gcommon/v1/queue/tls_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `TLSAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/tls_auth.proto
// version: 1.0.0
// guid: f7982aad-6216-4a98-ae5a-3e86d058ae84

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TLSAuth {
  // Client certificate (PEM format)
  string cert_pem = 1 [(buf.validate.field).string.min_len = 1];

  // Client private key (PEM format)
  string key_pem = 2 [(buf.validate.field).string.min_len = 1];

  // CA certificate (PEM format)
  string ca_pem = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to verify server certificate
  bool verify_server = 4;
}
```

---

### topic_info.proto {#topic_info}

**Path**: `gcommon/v1/queue/topic_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 53

**Messages** (1): `TopicInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_info.proto
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Topic information for queue management.
 * Contains metadata and status about a message queue topic.
 */
message TopicInfo {
  // Topic name/identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Topic creation timestamp
  google.protobuf.Timestamp created_at = 3 [lazy = true, (buf.validate.field).required = true];

  // Topic last update timestamp
  google.protobuf.Timestamp updated_at = 4 [lazy = true];

  // Number of partitions
  int32 partition_count = 5;

  // Replication factor
  int32 replication_factor = 6;

  // Total message count
  int64 message_count = 7;

  // Topic size in bytes
  int64 size_bytes = 8;

  // Topic status (active, paused, etc.)
  string status = 9;

  // Topic metadata
  map<string, string> metadata = 10 [lazy = true];
}
```

---

### topic_permissions.proto {#topic_permissions}

**Path**: `gcommon/v1/queue/topic_permissions.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `TopicPermissions`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_permissions.proto
// version: 1.0.1
// guid: a2131871-2610-442f-93e7-5ab90e53e36c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TopicPermissions {
  // Can read messages from topic
  bool can_read = 1;

  // Can write messages to topic
  bool can_write = 2;

  // Can modify topic configuration
  bool can_configure = 3;

  // Can delete the topic
  bool can_delete = 4;

  // Can manage topic permissions
  bool can_manage_permissions = 5;

  // Can view topic statistics
  bool can_view_stats = 6;
}
```

---

### topic_stats.proto {#topic_stats}

**Path**: `gcommon/v1/queue/topic_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `TopicStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/topic_stats.proto
// file: proto/gcommon/v1/queue/topic_stats.proto
// version: 1.0.0
// guid: 9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics information for a topic.
 */
message TopicStats {
  // Name of the topic
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Total number of messages in the topic
  uint64 total_messages = 2;

  // Total size of all messages in bytes
  uint64 total_size_bytes = 3;

  // Number of active subscriptions
  uint32 subscription_count = 4;

  // Number of producers
  uint32 producer_count = 5;

  // Messages produced per second
  double messages_per_second = 6;

  // Bytes produced per second
  double bytes_per_second = 7;

  // Last message timestamp
  uint64 last_message_time = 8;

  // Average message size in bytes
  double average_message_size = 9;
}
```

---

### updated_properties.proto {#updated_properties}

**Path**: `gcommon/v1/queue/updated_properties.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `UpdatedProperties`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/updated_properties.proto
// version: 1.0.0
// guid: d960456c-efea-47df-8809-e0e34d8b8437

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdatedProperties {
  // New priority level (if updated)
  int32 priority_level = 1 [(buf.validate.field).int32.gte = 0];

  // New expiration time (if updated)
  google.protobuf.Timestamp expiration_time = 2;

  // New visibility timeout (if updated)
  int64 visibility_timeout_ms = 3 [(buf.validate.field).int64.gt = 0];

  // New routing key (if updated)
  string routing_key = 4 [(buf.validate.field).string.min_len = 1];

  // Updated metadata count
  int32 metadata_count = 5;

  // Updated headers count
  int32 headers_count = 6 [(buf.validate.field).int32.gte = 0];

  // Content was updated
  bool content_updated = 7;

  // Size of updated content (bytes)
  int64 content_size_bytes = 8 [(buf.validate.field).int64.gte = 0];
}
```

---

### username_password_auth.proto {#username_password_auth}

**Path**: `gcommon/v1/queue/username_password_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `UsernamePasswordAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/username_password_auth.proto
// version: 1.0.0
// guid: 3fc55294-5eb0-4d0a-8e1e-e00a7f1fdd98

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UsernamePasswordAuth {
  // Username for authentication
  string username = 1 [(buf.validate.field).string.min_len = 1];

  // Password for authentication (should be encrypted)
  string password = 2 [(buf.validate.field).string.min_len = 8];
}
```

---

### validation_error.proto {#validation_error}

**Path**: `gcommon/v1/queue/validation_error.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ValidationError`

**Imports** (3):

- `gcommon/v1/queue/offset_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/validation_error.proto
// version: 1.0.0
// guid: c3c484a5-cc5a-41e5-926d-91ba8263600e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/offset_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ValidationError {
  // Error type
  string error_type = 1;

  // Error description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Affected partition
  int32 partition_id = 3;

  // Affected offset range
  OffsetRange affected_range = 4;
}
```

---

### validation_result.proto {#validation_result}

**Path**: `gcommon/v1/queue/validation_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `QueueValidationResult`

**Imports** (7):

- `gcommon/v1/queue/checksum_validation.proto`
- `gcommon/v1/queue/integrity_validation.proto`
- `gcommon/v1/queue/schema_validation.proto`
- `gcommon/v1/queue/validation_error.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/validation_result.proto
// version: 1.0.0
// guid: 26c1b8e2-a8aa-436b-9707-1f47c8c3e8d8

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/checksum_validation.proto";
import "gcommon/v1/queue/integrity_validation.proto";
import "gcommon/v1/queue/schema_validation.proto";
import "gcommon/v1/queue/validation_error.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueValidationResult {
  // Validation success status
  bool validation_passed = 1;

  // Checksum verification results
  ChecksumValidation checksum_validation = 2;

  // Schema validation results
  SchemaValidation schema_validation = 3;

  // Data integrity validation
  IntegrityValidation integrity_validation = 4;

  // Validation errors found
  repeated ValidationError validation_errors = 5 [(buf.validate.field).repeated.min_items = 1];

  // Validation duration
  google.protobuf.Duration validation_duration = 6;
}
```

---

### visibility_update.proto {#visibility_update}

**Path**: `gcommon/v1/queue/visibility_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `VisibilityUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/visibility_update.proto
// version: 1.0.0
// guid: 9e5fd0b6-9d67-467e-b8a6-29addbcc72e4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message VisibilityUpdate {
  // New visibility timeout duration (milliseconds)
  int64 visibility_timeout_ms = 1 [(buf.validate.field).int64.gt = 0];

  // Extend current timeout (if true) or set absolute timeout
  bool extend_current = 2;

  // Maximum visibility timeout allowed
  int64 max_visibility_ms = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### workflow.proto {#workflow}

**Path**: `gcommon/v1/queue/workflow.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `QueueWorkflow`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/workflow.proto
// version: 1.0.0
// guid: 6f7e8d9c-0b1a-2534-6e7f-8a9b0c1d2e3f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Workflow represents a multi-step process definition.
 * Contains workflow metadata and execution configuration.
 */
message QueueWorkflow {
  // Unique identifier for the workflow
  string workflow_id = 1;

  // Human-readable workflow name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Workflow version
  string version = 3;

  // Workflow description
  string description = 4 [ (buf.validate.field).string.max_len = 1000 ];

  // Whether the workflow is active
  bool enabled = 5;
}
```

---

### write_consistency.proto {#write_consistency}

**Path**: `gcommon/v1/queue/write_consistency.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `WriteConsistency`

**Imports** (6):

- `gcommon/v1/common/write_level.proto`
- `gcommon/v1/queue/conflict_detection.proto`
- `gcommon/v1/queue/sync_replication.proto`
- `gcommon/v1/queue/write_retry_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/write_consistency.proto
// version: 1.0.0
// guid: 25356885-1f2a-4629-a203-6fd654cb6821

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/write_level.proto";
import "gcommon/v1/queue/conflict_detection.proto";
import "gcommon/v1/queue/sync_replication.proto";
import "gcommon/v1/queue/write_retry_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message WriteConsistency {
  // Write consistency level
  gcommon.v1.common.WriteLevel level = 1;

  // Synchronous replication requirements
  SyncReplication sync_replication = 2;

  // Write conflict detection
  ConflictDetection conflict_detection = 3;

  // Timeout for write operations (milliseconds)
  int32 timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Retry configuration for write failures
  WriteRetryConfig retry_config = 5;
}
```

---

