# queue_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [message_id.proto](#message_id)
- [message_metadata.proto](#message_metadata)
- [message_nack.proto](#message_nack)
- [message_properties.proto](#message_properties)
- [message_state_counts.proto](#message_state_counts)
- [message_update_properties.proto](#message_update_properties)
- [metadata_update.proto](#metadata_update)
- [nack_error.proto](#nack_error)
- [node_info.proto](#node_info)
- [node_stats.proto](#node_stats)
- [notification_channel.proto](#notification_channel)
- [o_auth2_auth.proto](#o_auth2_auth)
- [offset_info.proto](#offset_info)
- [offset_range.proto](#offset_range)
- [original_queue_info.proto](#original_queue_info)
- [owner_info.proto](#owner_info)
- [partition_assignment.proto](#partition_assignment)
- [partition_commit_result.proto](#partition_commit_result)
- [partition_info.proto](#partition_info)
- [partition_offset.proto](#partition_offset)
- [partition_restore_result.proto](#partition_restore_result)
- [performance_metrics.proto](#performance_metrics)
- [performance_options.proto](#performance_options)
- [permission_rule.proto](#permission_rule)
- [preserved_stats.proto](#preserved_stats)
- [priority_range.proto](#priority_range)
- [priority_update.proto](#priority_update)
- [purge_options.proto](#purge_options)
- [read_consistency.proto](#read_consistency)
- [rebalance_stats.proto](#rebalance_stats)
- [received_message.proto](#received_message)
- [replication_consistency.proto](#replication_consistency)
- [resume_stats.proto](#resume_stats)
- [retention_info.proto](#retention_info)
- [retention_policy.proto](#retention_policy)
- [retry_policy.proto](#retry_policy)
- [retry_settings.proto](#retry_settings)
- [role_based_access_control.proto](#role_based_access_control)
- [role_inheritance.proto](#role_inheritance)
- [routing_condition.proto](#routing_condition)
- [routing_info.proto](#routing_info)
- [routing_key.proto](#routing_key)
- [routing_rule.proto](#routing_rule)
- [routing_settings.proto](#routing_settings)
- [sasl_auth.proto](#sasl_auth)
- [schema_validation.proto](#schema_validation)
- [size_bucket.proto](#size_bucket)
- [size_distribution.proto](#size_distribution)
- [size_range.proto](#size_range)
- [subscription_info.proto](#subscription_info)
---


## Detailed Documentation

### message_id.proto {#message_id}

**Path**: `gcommon/v1/queue/message_id.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `MessageId`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_id.proto
// version: 1.0.0
// guid: 9bd8b62d-3655-4ff5-9f3a-4d5da241dc77

// MessageId is a simple wrapper type used for referencing messages
// in a type-safe manner across the Queue API. This replaces the
// placeholder created during the migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// MessageId uniquely identifies a message within a queue.
// It can be referenced by other messages or API calls.
message MessageId {
  // Opaque identifier assigned by the queue implementation.
  string value = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_metadata.proto {#message_metadata}

**Path**: `gcommon/v1/queue/message_metadata.proto` **Package**: `gcommon.v1.queue` **Lines**: 56

**Messages** (1): `MessageMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/message_metadata.proto
// file: proto/gcommon/v1/queue/message_metadata.proto
// version: 1.0.0
// guid: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Metadata associated with a queue message.
 */
message MessageMetadata {
  // Unique message identifier
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Message timestamp
  google.protobuf.Timestamp timestamp = 2;

  // Producer/sender identifier
  string producer_id = 3 [(buf.validate.field).string.min_len = 1];

  // Content type of the message
  string content_type = 4 [(buf.validate.field).string.min_len = 1];

  // Content encoding (gzip, deflate, etc.)
  string content_encoding = 5 [(buf.validate.field).string.min_len = 1];

  // Message priority (0-255, higher is more priority)
  uint32 priority = 6 [(buf.validate.field).uint32.gte = 0];

  // Time-to-live in milliseconds
  uint64 ttl_ms = 7 [(buf.validate.field).uint64.gte = 0];

  // Custom headers
  map<string, string> headers = 8;

  // Routing key
  string routing_key = 9 [(buf.validate.field).string.min_len = 1];

  // Correlation ID for request-response patterns
  string correlation_id = 10 [(buf.validate.field).string.min_len = 1];

  // Reply-to address
  string reply_to = 11 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_nack.proto {#message_nack}

**Path**: `gcommon/v1/queue/message_nack.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `MessageNack`

**Imports** (3):

- `gcommon/v1/common/nack_error_category.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_nack.proto
// version: 1.0.0
// guid: b5bb9e75-3346-4684-9529-764a3cdb3e3d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/nack_error_category.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageNack {
  // Message identifier
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Message delivery tag
  string delivery_tag = 2 [(buf.validate.field).string.min_len = 1];

  // Partition ID containing the message
  int32 partition_id = 3 [(buf.validate.field).int32.gte = 0];

  // Message offset
  int64 message_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Reason for negative acknowledgment
  string nack_reason = 5 [(buf.validate.field).string.min_len = 1];

  // Error category for the nack
  gcommon.v1.common.NackErrorCategory error_category = 6;

  // Specific error code
  string error_code = 7 [(buf.validate.field).string.min_len = 1];

  // Retry this specific message
  bool retry_message = 8;

  // Custom retry delay for this message (milliseconds)
  int64 retry_delay_ms = 9 [(buf.validate.field).int64.gte = 0];

  // Message-specific metadata
  map<string, string> message_metadata = 10;
}
```

---

### message_properties.proto {#message_properties}

**Path**: `gcommon/v1/queue/message_properties.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `MessageProperties`

**Imports** (5):

- `gcommon/v1/common/delivery_mode.proto`
- `gcommon/v1/common/priority_level.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_properties.proto
// version: 1.0.0
// guid: 57ef0850-feeb-42b0-b724-f14b542cfd08

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/delivery_mode.proto";
import "gcommon/v1/common/priority_level.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageProperties {
  // Message priority level
  gcommon.v1.common.PriorityLevel priority = 1;

  // Delivery mode for the message
  gcommon.v1.common.DeliveryMode delivery_mode = 2;

  // Message expiration time
  google.protobuf.Timestamp expiration_time = 3;

  // Correlation ID for request-response patterns
  string correlation_id = 4 [(buf.validate.field).string.min_len = 1];

  // Reply-to address/topic
  string reply_to = 5 [(buf.validate.field).string.min_len = 1];

  // Content type of the payload
  string content_type = 6 [(buf.validate.field).string.min_len = 1];

  // Content encoding
  string content_encoding = 7 [(buf.validate.field).string.min_len = 1];

  // Compression applied to payload
  string compression = 8 [(buf.validate.field).string.min_len = 1];

  // Message deduplication ID
  string deduplication_id = 9 [(buf.validate.field).string.min_len = 1];

  // Delay before message becomes available (milliseconds)
  int64 delivery_delay_ms = 10 [(buf.validate.field).int64.gte = 0];
}
```

---

### message_state_counts.proto {#message_state_counts}

**Path**: `gcommon/v1/queue/message_state_counts.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `MessageStateCounts`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_state_counts.proto
// version: 1.0.0
// guid: ed6cdf6e-a32e-4ea4-942c-92e90ea2d061

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageStateCounts {
  int64 pending = 1 [(buf.validate.field).int64.gte = 0];
  int64 processing = 2 [(buf.validate.field).int64.gte = 0];
  int64 completed = 3 [(buf.validate.field).int64.gte = 0];
  int64 failed = 4 [(buf.validate.field).int64.gte = 0];
  int64 retrying = 5 [(buf.validate.field).int64.gte = 0];
  int64 dead_letter = 6 [(buf.validate.field).int64.gte = 0];
}
```

---

### message_update_properties.proto {#message_update_properties}

**Path**: `gcommon/v1/queue/message_update_properties.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `MessageUpdateProperties`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_update_properties.proto
// version: 1.0.0
// guid: db9a2627-8ff1-4dc6-b551-e15416cd3bbe

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageUpdateProperties {
  // New expiration time
  google.protobuf.Timestamp expiration_time = 1;

  // New delivery delay
  int64 delivery_delay_ms = 2 [(buf.validate.field).int64.gte = 0];

  // New retry count
  int32 retry_count = 3 [(buf.validate.field).int32.gte = 0];

  // New routing key
  string routing_key = 4 [(buf.validate.field).string.min_len = 1];

  // New correlation ID
  string correlation_id = 5 [(buf.validate.field).string.min_len = 1];

  // New reply-to address
  string reply_to = 6 [(buf.validate.field).string.min_len = 1];

  // Updated message headers
  map<string, string> headers = 7;
}
```

---

### metadata_update.proto {#metadata_update}

**Path**: `gcommon/v1/queue/metadata_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `MetadataUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/metadata_update.proto
// version: 1.0.0
// guid: 6cb1a95a-0fdd-464d-a156-b7cff3414a7d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MetadataUpdate {
  // Metadata fields to add or update
  map<string, string> add_metadata = 1;

  // Metadata fields to remove
  repeated string remove_metadata = 2;

  // Replace all metadata with new values
  map<string, string> replace_metadata = 3;

  // Update operation (add, remove, replace)
  string operation_type = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### nack_error.proto {#nack_error}

**Path**: `gcommon/v1/queue/nack_error.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `NackError`

**Imports** (3):

- `gcommon/v1/common/nack_error_category.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_error.proto
// version: 1.0.0
// guid: 9c0d1e2f-3a4b-5c6d-7e8f-9a0b1c2d3e4f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/nack_error_category.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Error information for NACK operations.
 */
message NackError {
  // Error code
  string code = 1 [(buf.validate.field).string.min_len = 1];

  // Error message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Error category
  gcommon.v1.common.NackErrorCategory category = 3;

  // Whether the error is retryable
  bool retryable = 4;

  // Stack trace or additional details
  string details = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### node_info.proto {#node_info}

**Path**: `gcommon/v1/queue/node_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `NodeInfo`

**Imports** (5):

- `gcommon/v1/common/node_state.proto`
- `gcommon/v1/queue/node_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/node_info.proto
// version: 1.0.0
// guid: d73ea780-8ed0-4b73-8aae-ab5c4fc1a48f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/node_state.proto";
import "gcommon/v1/queue/node_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Information about a single node in the cluster.
 */
message NodeInfo {
  // Unique identifier for the node
  string node_id = 1 [(buf.validate.field).string.min_len = 1];

  // Hostname or address of the node
  string hostname = 2 [(buf.validate.field).string.min_len = 1];

  // Port number for the node
  int32 port = 3 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Current state of the node
  gcommon.v1.common.NodeState state = 4;

  // Node roles (leader, follower, etc.)
  repeated string roles = 5 [(buf.validate.field).repeated.min_items = 1];

  // Timestamp when node was last seen
  google.protobuf.Timestamp last_heartbeat = 6;

  // Node-specific statistics
  NodeStats stats = 7;
}
```

---

### node_stats.proto {#node_stats}

**Path**: `gcommon/v1/queue/node_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `NodeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/node_stats.proto
// version: 1.0.0
// guid: f64f009b-e23d-4540-9785-817fe7acb9f3

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics for a single node.
 */
message NodeStats {
  // Number of queues hosted on this node
  int32 queue_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of messages on this node
  int64 message_count = 2 [(buf.validate.field).int64.gte = 0];

  // CPU usage percentage
  double cpu_usage = 3 [(buf.validate.field).double.gte = 0.0];

  // Memory usage in bytes
  int64 memory_usage = 4 [(buf.validate.field).int64.gte = 0];

  // Disk usage in bytes
  int64 disk_usage = 5 [(buf.validate.field).int64.gte = 0];

  // Network throughput in bytes per second
  double network_throughput = 6 [(buf.validate.field).double.gte = 0.0];
}
```

---

### notification_channel.proto {#notification_channel}

**Path**: `gcommon/v1/queue/notification_channel.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `QueueNotificationChannel`

**Imports** (4):

- `gcommon/v1/common/metrics_alert_severity.proto`
- `gcommon/v1/common/notification_channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/notification_channel.proto
// version: 1.0.0
// guid: 6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_alert_severity.proto";
import "gcommon/v1/common/notification_channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Notification channel for sending alerts.
 */
message QueueNotificationChannel {
  // Unique identifier for the channel
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Type of notification channel
  gcommon.v1.common.NotificationChannelType type = 2;

  // Configuration specific to the channel type
  map<string, string> config = 3;

  // Whether the channel is enabled
  bool enabled = 4;

  // Minimum severity level for notifications
  gcommon.v1.common.MetricsAlertSeverity min_severity = 5;
}
```

---

### o_auth2_auth.proto {#o_auth2_auth}

**Path**: `gcommon/v1/queue/o_auth2_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `OAuth2Auth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/o_auth2_auth.proto
// version: 1.0.0
// guid: ed719ecf-6477-4d68-b022-dc57bed659ce

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OAuth2Auth {
  // OAuth2 token endpoint
  string token_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Client ID
  string client_id = 2 [(buf.validate.field).string.min_len = 1];

  // Client secret
  string client_secret = 3 [(buf.validate.field).string.min_len = 1];

  // Scopes to request
  repeated string scopes = 4 [(buf.validate.field).repeated.min_items = 1];

  // Additional OAuth2 parameters
  map<string, string> parameters = 5;
}
```

---

### offset_info.proto {#offset_info}

**Path**: `gcommon/v1/queue/offset_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `OffsetInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/offset_info.proto
// file: proto/gcommon/v1/queue/offset_info.proto
// version: 1.0.0
// guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Information about message offset position in a queue.
 */
message OffsetInfo {
  // The offset value
  uint64 offset = 1 [(buf.validate.field).uint64.gte = 0];

  // Partition this offset belongs to
  uint32 partition_id = 2 [(buf.validate.field).uint32.gte = 0];

  // Timestamp of the message at this offset
  google.protobuf.Timestamp timestamp = 3;

  // Size of the message at this offset
  uint64 message_size = 4 [(buf.validate.field).uint64.gte = 0];

  // Whether this offset is valid/available
  bool is_valid = 5;

  // Consumer group that owns this offset
  string consumer_group = 6 [(buf.validate.field).string.min_len = 1];

  // Last committed offset for this consumer
  uint64 committed_offset = 7 [(buf.validate.field).uint64.gte = 0];
}
```

---

### offset_range.proto {#offset_range}

**Path**: `gcommon/v1/queue/offset_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `OffsetRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_range.proto
// version: 1.0.0
// guid: 83e606c1-e57b-4ca4-a62b-2460a5ae302f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OffsetRange {
  // Start offset
  int64 start_offset = 1 [(buf.validate.field).int64.gte = 0];

  // End offset
  int64 end_offset = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### original_queue_info.proto {#original_queue_info}

**Path**: `gcommon/v1/queue/original_queue_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `OriginalQueueInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/original_queue_info.proto
// version: 1.0.0
// guid: a939a9d0-aaf5-4d3a-b47d-16dad566fe50

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OriginalQueueInfo {
  // Original queue ID
  string queue_id = 1;

  // Original queue name
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Original partition count
  int32 partition_count = 3;

  // Original configuration snapshot
  map<string, string> config_snapshot = 4;

  // Backup creation point
  google.protobuf.Timestamp backup_point = 5;
}
```

---

### owner_info.proto {#owner_info}

**Path**: `gcommon/v1/queue/owner_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `OwnerInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/owner_info.proto
// version: 1.0.0
// guid: bafca048-b678-49a0-853b-ba2cb7e220a9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OwnerInfo {
  // Owner user ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Owner username
  string username = 2;

  // Owner email
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Organization/team
  string organization = 4;

  // Ownership timestamp
  google.protobuf.Timestamp owned_since = 5;
}
```

---

### partition_assignment.proto {#partition_assignment}

**Path**: `gcommon/v1/queue/partition_assignment.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PartitionAssignment`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_assignment.proto
// version: 1.0.0
// guid: 7da7ff24-741c-4f7d-840c-ae433c0bf313

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PartitionAssignment {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Assigned consumer ID
  string consumer_id = 2 [(buf.validate.field).string.min_len = 1];

  // Current offset position
  int64 current_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Committed offset
  int64 committed_offset = 4 [(buf.validate.field).int64.gte = 0];

  // High water mark (latest available offset)
  int64 high_water_mark = 5 [(buf.validate.field).int64.gte = 0];

  // Assignment timestamp
  google.protobuf.Timestamp assigned_at = 6;

  // Last commit timestamp
  google.protobuf.Timestamp last_commit = 7;
}
```

---

### partition_commit_result.proto {#partition_commit_result}

**Path**: `gcommon/v1/queue/partition_commit_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PartitionCommitResult`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_commit_result.proto
// version: 1.0.0
// guid: c39fc412-24d3-4f3f-873f-f825a3dee3af

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PartitionCommitResult {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Success status for this partition
  bool success = 2;

  // Committed offset value
  int64 committed_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Previous offset before commit
  int64 previous_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Error message if commit failed for this partition
  string error_message = 5 [(buf.validate.field).string.min_len = 1];

  // Error code for this partition
  string error_code = 6 [(buf.validate.field).string.min_len = 1];

  // Timestamp when this offset was committed
  google.protobuf.Timestamp commit_timestamp = 7;

  // Metadata for this partition commit
  map<string, string> partition_metadata = 8;
}
```

---

### partition_info.proto {#partition_info}

**Path**: `gcommon/v1/queue/partition_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `PartitionInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/partition_info.proto
// file: proto/gcommon/v1/queue/partition_info.proto
// version: 1.0.0
// guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c
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
 * Information about a queue partition.
 */
message PartitionInfo {
  // Partition identifier
  uint32 partition_id = 1 [(buf.validate.field).uint32.gte = 0];

  // Leader node for this partition
  string leader_node = 2 [(buf.validate.field).string.min_len = 1];

  // Replica nodes for this partition
  repeated string replica_nodes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Current offset (latest message)
  uint64 current_offset = 4 [(buf.validate.field).uint64.gte = 0];

  // Earliest available offset
  uint64 earliest_offset = 5 [(buf.validate.field).uint64.gte = 0];

  // Number of messages in partition
  uint64 message_count = 6 [(buf.validate.field).uint64.gte = 0];

  // Partition size in bytes
  uint64 size_bytes = 7 [(buf.validate.field).uint64.gte = 0];

  // Whether partition is online
  bool is_online = 8;
}
```

---

### partition_offset.proto {#partition_offset}

**Path**: `gcommon/v1/queue/partition_offset.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PartitionOffset`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_offset.proto
// version: 1.0.0
// guid: 0d54df2b-ee96-4361-8361-b047c9a198f6
// Partition offset information for queue operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// PartitionOffset represents the offset position within a partition
message PartitionOffset {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Starting offset value
  int64 offset = 2 [(buf.validate.field).int64.gte = 0];

  // Offset timestamp
  google.protobuf.Timestamp offset_timestamp = 3;

  // High water mark for this partition
  int64 high_water_mark = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### partition_restore_result.proto {#partition_restore_result}

**Path**: `gcommon/v1/queue/partition_restore_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `PartitionRestoreResult`

**Imports** (4):

- `gcommon/v1/queue/restore_error.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_restore_result.proto
// version: 1.0.0
// guid: b39d8964-9b75-4f60-9e91-1c838aa2546e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/restore_error.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PartitionRestoreResult {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Success status for this partition
  bool success = 2;

  // Messages restored in this partition
  int64 messages_restored = 3 [(buf.validate.field).int64.gte = 0];

  // Bytes restored in this partition
  int64 bytes_restored = 4 [(buf.validate.field).int64.gte = 0];

  // Start offset restored
  int64 start_offset = 5 [(buf.validate.field).int64.gte = 0];

  // End offset restored
  int64 end_offset = 6 [(buf.validate.field).int64.gte = 0];

  // Partition restore duration
  google.protobuf.Duration restore_duration = 7;

  // Any partition-specific errors
  repeated RestoreError partition_errors = 8 [(buf.validate.field).repeated.min_items = 1];

  // Partition metadata
  map<string, string> partition_metadata = 9;
}
```

---

### performance_metrics.proto {#performance_metrics}

**Path**: `gcommon/v1/queue/performance_metrics.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PerformanceMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/performance_metrics.proto
// version: 1.0.0
// guid: 05dd3b07-903d-4e03-97dc-1a79fa3bd75b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PerformanceMetrics {
  // Memory usage
  int64 memory_used_bytes = 1 [(buf.validate.field).int64.gte = 0];
  int64 memory_available_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // CPU usage percentage
  double cpu_usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Disk usage for persistent storage
  int64 disk_used_bytes = 4 [(buf.validate.field).int64.gte = 0];
  int64 disk_available_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Network metrics
  double network_bytes_per_second = 6 [(buf.validate.field).double.gte = 0.0];

  // Connection metrics
  int32 active_connections = 7 [(buf.validate.field).int32.gte = 0];
  int32 max_connections = 8 [(buf.validate.field).int32.gte = 0];
}
```

---

### performance_options.proto {#performance_options}

**Path**: `gcommon/v1/queue/performance_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PerformanceOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/performance_options.proto
// version: 1.0.0
// guid: da533c28-4c1d-47aa-af5b-b6f7ec77d916

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PerformanceOptions {
  // Parallel restore workers
  int32 worker_count = 1 [(buf.validate.field).int32.gte = 0];

  // Batch size for restore operations
  int32 batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Buffer size for reading backup data
  int32 buffer_size_mb = 3 [(buf.validate.field).int32.gte = 0];

  // Compression during restore
  bool enable_compression = 4;

  // Throttle restore rate (messages/second)
  int32 throttle_rate = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### permission_rule.proto {#permission_rule}

**Path**: `gcommon/v1/queue/permission_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PermissionRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/permission_rule.proto
// version: 1.0.0
// guid: a9f45dd7-43a2-47cd-812c-8a08ee0100e2

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PermissionRule {
  // Resource pattern (queue name, topic name, etc.)
  string resource_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Operation (read, write, admin, etc.)
  string operation = 2 [(buf.validate.field).string.min_len = 1];

  // Required roles or permissions
  repeated string required_roles = 3 [(buf.validate.field).repeated.min_items = 1];

  // Allow or deny rule
  bool allow = 4;

  // Priority of this rule (higher number = higher priority)
  int32 priority = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### preserved_stats.proto {#preserved_stats}

**Path**: `gcommon/v1/queue/preserved_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PreservedStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/preserved_stats.proto
// version: 1.0.0
// guid: d380f24a-2b42-4096-bfe3-4e251cf55325

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PreservedStats {
  // Total message count (lifetime)
  int64 lifetime_message_count = 1;

  // Queue creation timestamp
  google.protobuf.Timestamp created_at = 2 [ (buf.validate.field).required = true ];

  // Last configuration change timestamp
  google.protobuf.Timestamp last_config_change = 3;

  // Peak message count (historical high)
  int64 peak_message_count = 4;

  // Peak throughput (historical high)
  double peak_throughput = 5;

  // Total uptime (milliseconds)
  int64 total_uptime_ms = 6;
}
```

---

### priority_range.proto {#priority_range}

**Path**: `gcommon/v1/queue/priority_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `PriorityRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/priority_range.proto
// version: 1.0.0
// guid: 1efceade-7805-4b90-bdd0-2484a86cb6c9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Priority range for filtering.
 */
message PriorityRange {
  // Minimum priority (inclusive)
  int32 min_priority = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum priority (inclusive)
  int32 max_priority = 2 [(buf.validate.field).int32.gte = 0];
}
```

---

### priority_update.proto {#priority_update}

**Path**: `gcommon/v1/queue/priority_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `PriorityUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/priority_update.proto
// version: 1.0.0
// guid: 65ef02ba-9810-4cd5-9b8e-d1db580b22f6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PriorityUpdate {
  // New priority level
  int32 priority_level = 1 [(buf.validate.field).int32.gte = 0];

  // Priority change reason
  string priority_reason = 2 [(buf.validate.field).string.min_len = 1];

  // Maintain relative priority ordering
  bool maintain_order = 3;
}
```

---

### purge_options.proto {#purge_options}

**Path**: `gcommon/v1/queue/purge_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PurgeOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/purge_options.proto
// version: 1.0.0
// guid: 05f20447-a209-4b0a-bbe3-d46d178c07c6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PurgeOptions {
  // Whether to purge all messages (if true, other filters are ignored)
  bool purge_all = 1;

  // Purge messages older than this timestamp
  google.protobuf.Timestamp older_than = 2;

  // Purge messages with specific headers (all headers must match)
  map<string, string> header_filters = 3;

  // Purge messages with priority below this value
  int32 priority_below = 4 [(buf.validate.field).int32.gte = 0];

  // Purge messages with priority above this value
  int32 priority_above = 5 [(buf.validate.field).int32.gte = 0];

  // Maximum number of messages to purge (0 = no limit)
  int64 max_messages = 6 [(buf.validate.field).int64.gte = 0];

  // Whether to purge only failed/undeliverable messages
  bool only_failed = 7;

  // Whether to purge only expired messages
  bool only_expired = 8;
}
```

---

### read_consistency.proto {#read_consistency}

**Path**: `gcommon/v1/queue/read_consistency.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `ReadConsistency`

**Imports** (4):

- `gcommon/v1/common/read_level.proto`
- `gcommon/v1/queue/read_retry_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/read_consistency.proto
// version: 1.0.0
// guid: 76f69c9b-abbb-4704-a74e-3dddcab24330

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/read_level.proto";
import "gcommon/v1/queue/read_retry_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReadConsistency {
  // Read consistency level
  gcommon.v1.common.ReadLevel level = 1;

  // Maximum staleness allowed for reads (milliseconds)
  int64 max_staleness_ms = 2 [(buf.validate.field).int64.gte = 0];

  // Enable read-your-writes consistency
  bool read_your_writes = 3;

  // Enable monotonic read consistency
  bool monotonic_reads = 4;

  // Timeout for read operations (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];

  // Retry configuration for read failures
  ReadRetryConfig retry_config = 6;
}
```

---

### rebalance_stats.proto {#rebalance_stats}

**Path**: `gcommon/v1/queue/rebalance_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `RebalanceStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/rebalance_stats.proto
// version: 1.0.0
// guid: 3a965b27-4706-4f72-ada6-d9f3547ebd00

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RebalanceStats {
  // Total number of rebalances
  int64 total_rebalances = 1 [(buf.validate.field).int64.gte = 0];

  // Last rebalance timestamp
  google.protobuf.Timestamp last_rebalance = 2;

  // Average rebalance duration (milliseconds)
  int64 avg_rebalance_duration_ms = 3 [(buf.validate.field).int64.gt = 0];

  // Failed rebalances
  int64 failed_rebalances = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### received_message.proto {#received_message}

**Path**: `gcommon/v1/queue/received_message.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `ReceivedMessage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/received_message.proto
// version: 1.0.0
// guid: c7d8e9f0-123a-567b-8901-123456789012

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReceivedMessage {
  // Message ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Message data
  bytes data = 2;

  // Message attributes
  map<string, string> attributes = 3;

  // Receive timestamp
  int64 receive_timestamp = 4;

  // Acknowledgment ID
  string ack_id = 5;
}
```

---

### replication_consistency.proto {#replication_consistency}

**Path**: `gcommon/v1/queue/replication_consistency.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `ReplicationConsistency`

**Imports** (3):

- `gcommon/v1/common/replication_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/replication_consistency.proto
// version: 1.0.0
// guid: 6edbf0fb-990f-446b-bec1-14f1ec84397c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/replication_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReplicationConsistency {
  // Minimum number of replicas that must acknowledge writes
  int32 min_write_replicas = 1 [(buf.validate.field).int32.gte = 0];

  // Minimum number of replicas that must be available for reads
  int32 min_read_replicas = 2 [(buf.validate.field).int32.gte = 0];

  // Replication factor (total number of replicas)
  int32 replication_factor = 3 [(buf.validate.field).int32.gte = 0];

  // Consistency level for replication
  gcommon.v1.common.ReplicationLevel replication_level = 4;

  // Enable anti-entropy repair
  bool anti_entropy_enabled = 5;

  // Anti-entropy repair interval (seconds)
  int32 repair_interval_seconds = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### resume_stats.proto {#resume_stats}

**Path**: `gcommon/v1/queue/resume_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ResumeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resume_stats.proto
// version: 1.0.0
// guid: dd734c97-7ac1-4b56-8ea6-dbd08cac6e27

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResumeStats {
  // Number of partitions resumed
  int32 partitions_resumed = 1 [(buf.validate.field).int32.gte = 0];

  // Number of subscriptions reactivated
  int32 subscriptions_reactivated = 2 [(buf.validate.field).int32.gte = 0];

  // Number of consumers reconnected
  int32 consumers_reconnected = 3 [(buf.validate.field).int32.gte = 0];

  // Time taken to complete resume (milliseconds)
  int64 resume_time_ms = 4 [(buf.validate.field).int64.gte = 0];

  // Messages processed immediately after resume
  int64 immediate_messages_processed = 5 [(buf.validate.field).int64.gte = 0];

  // Throughput after resume (messages/second)
  double post_resume_throughput = 6 [(buf.validate.field).double.gte = 0.0];
}
```

---

### retention_info.proto {#retention_info}

**Path**: `gcommon/v1/queue/retention_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `QueueRetentionInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retention_info.proto
// version: 1.0.0
// guid: ecd5cb6b-db6b-42d3-b953-fa57bdfd4483

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueRetentionInfo {
  // Current retention policy
  string retention_policy = 1 [(buf.validate.field).string.min_len = 1];

  // Retention period (seconds)
  int64 retention_seconds = 2 [(buf.validate.field).int64.gte = 0];

  // Size-based retention limit (bytes)
  int64 retention_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Number of messages retained
  int64 retained_messages = 4 [(buf.validate.field).int64.gte = 0];

  // Oldest message timestamp
  google.protobuf.Timestamp oldest_message_time = 5;

  // Next cleanup scheduled time
  google.protobuf.Timestamp next_cleanup_time = 6;
}
```

---

### retention_policy.proto {#retention_policy}

**Path**: `gcommon/v1/queue/retention_policy.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `QueueRetentionPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retention_policy.proto
// version: 1.0.0
// guid: 5a069bb8-66bf-413e-a9e8-a1856f52eb01

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// RetentionPolicy controls how long messages are kept before deletion.
message QueueRetentionPolicy {
  // Maximum age of a message before it is removed.
  google.protobuf.Duration max_age = 1;
  // Maximum total storage size for the queue in bytes.
  int64 max_size_bytes = 2 [(buf.validate.field).int64.gte = 0];
  // If true, older messages are discarded when limits are reached.
  bool discard_old = 3;
}
```

---

### retry_policy.proto {#retry_policy}

**Path**: `gcommon/v1/queue/retry_policy.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `QueueRetryPolicy`

**Imports** (4):

- `gcommon/v1/common/retry_delay_strategy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_policy.proto
// version: 1.1.0
// guid: 4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/retry_delay_strategy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Retry policy for failed message processing.
 * Defines how failed messages should be retried before being
 * sent to dead letter queue.
 */
message QueueRetryPolicy {
  // Maximum number of retry attempts
  int32 max_attempts = 1 [(buf.validate.field).int32.gte = 0];

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 2;

  // Maximum delay between retries
  google.protobuf.Duration max_delay = 3;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Retry delay strategy
  gcommon.v1.common.RetryDelayStrategy delay_strategy = 5;

  // Whether to enable jitter in retry delays
  bool enable_jitter = 6;

  // Jitter factor (0.0 to 1.0) for randomizing delays
  double jitter_factor = 7 [(buf.validate.field).double.gte = 0.0];
}
```

---

### retry_settings.proto {#retry_settings}

**Path**: `gcommon/v1/queue/retry_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `QueueRetrySettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_settings.proto
// version: 1.0.0
// guid: dc848673-c62f-4cd2-b373-ed1570d3f5aa

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueRetrySettings {
  // Maximum retry attempts
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Dead letter queue topic
  string dead_letter_topic = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### role_based_access_control.proto {#role_based_access_control}

**Path**: `gcommon/v1/queue/role_based_access_control.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `RoleBasedAccessControl`

**Imports** (4):

- `gcommon/v1/queue/external_role_provider.proto`
- `gcommon/v1/queue/role_inheritance.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/role_based_access_control.proto
// version: 1.0.0
// guid: 090db6f2-ad16-49c5-aa6c-ef8f279279e2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/external_role_provider.proto";
import "gcommon/v1/queue/role_inheritance.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoleBasedAccessControl {
  // Enable RBAC
  bool enabled = 1;

  // Default roles for new users
  repeated string default_roles = 2 [(buf.validate.field).repeated.min_items = 1];

  // Role inheritance rules
  map<string, RoleInheritance> role_inheritance = 3;

  // External role provider settings
  ExternalRoleProvider external_provider = 4;
}
```

---

### role_inheritance.proto {#role_inheritance}

**Path**: `gcommon/v1/queue/role_inheritance.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `RoleInheritance`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/role_inheritance.proto
// version: 1.0.0
// guid: 85442141-e1a3-4392-94b8-44d4f53e79fb

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoleInheritance {
  // Parent roles that this role inherits from
  repeated string inherits_from = 1 [(buf.validate.field).repeated.min_items = 1];

  // Additional permissions for this role
  repeated string additional_permissions = 2 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### routing_condition.proto {#routing_condition}

**Path**: `gcommon/v1/queue/routing_condition.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `RoutingCondition`

**Imports** (4):

- `gcommon/v1/queue/priority_range.proto`
- `gcommon/v1/queue/size_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_condition.proto
// version: 1.0.0
// guid: c5586126-e8b2-47e8-b657-e837b38179bd

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/priority_range.proto";
import "gcommon/v1/queue/size_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Condition for routing rules.
 */
message RoutingCondition {
  // Header-based conditions
  map<string, string> header_matches = 1;

  // Content pattern matching
  string content_pattern = 2 [(buf.validate.field).string.min_len = 1];

  // Routing key pattern
  string routing_key_pattern = 3 [(buf.validate.field).string.min_len = 1];

  // Message type filter
  string message_type = 4 [(buf.validate.field).string.min_len = 1];

  // Priority range filter
  PriorityRange priority_range = 5;

  // Size range filter
  SizeRange size_range = 6;
}
```

---

### routing_info.proto {#routing_info}

**Path**: `gcommon/v1/queue/routing_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `RoutingInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_info.proto
// version: 1.0.0
// guid: 08017b3e-df77-4338-ba13-aadde0c41612

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoutingInfo {
  // Routing key for topic-based routing
  string routing_key = 1;

  // Specific partition ID (if applicable)
  int32 partition_id = 2;

  // Partition key for automatic partitioning
  string partition_key = 3;

  // Exchange name (for exchange-based routing)
  string exchange_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Routing tags for advanced routing
  repeated string routing_tags = 5;
}
```

---

### routing_key.proto {#routing_key}

**Path**: `gcommon/v1/queue/routing_key.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `RoutingKey`

**Imports** (3):

- `gcommon/v1/common/routing_pattern.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_key.proto
// version: 1.1.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/routing_pattern.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Routing key for message delivery.
 * Determines how messages are routed to queues and consumers.
 */
message RoutingKey {
  // The routing key string
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Pattern type for key matching
  gcommon.v1.common.RoutingPattern pattern_type = 2;

  // Whether the pattern is case sensitive
  bool case_sensitive = 3;

  // Priority for routing (higher numbers = higher priority)
  int32 priority = 4 [(buf.validate.field).int32.gte = 0];

  // Additional routing attributes
  map<string, string> attributes = 5;
}
```

---

### routing_rule.proto {#routing_rule}

**Path**: `gcommon/v1/queue/routing_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `RoutingRule`

**Imports** (3):

- `gcommon/v1/queue/routing_condition.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_rule.proto
// version: 1.0.0
// guid: 6ce2389f-a9b6-4850-bdf9-6b5225cd61d4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/routing_condition.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Individual routing rule.
 */
message RoutingRule {
  // Unique name for the rule
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Priority of the rule (higher numbers = higher priority)
  int32 priority = 2;

  // Condition for applying the rule
  RoutingCondition condition = 3;

  // Target destination for matching messages
  string destination = 4;

  // Whether the rule is enabled
  bool enabled = 5;

  // Additional metadata for the rule
  map<string, string> metadata = 6;
}
```

---

### routing_settings.proto {#routing_settings}

**Path**: `gcommon/v1/queue/routing_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `RoutingSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_settings.proto
// version: 1.0.0
// guid: f9f28b94-889d-4b4b-859e-dd55251a2aa6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoutingSettings {
  // Routing key pattern
  string routing_key_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Target partitions
  repeated int32 target_partitions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Routing strategy
  string routing_strategy = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### sasl_auth.proto {#sasl_auth}

**Path**: `gcommon/v1/queue/sasl_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `SASLAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/sasl_auth.proto
// version: 1.0.0
// guid: 24c2c7a1-8dbb-44e3-9d87-bb207c23207d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SASLAuth {
  // SASL mechanism (PLAIN, SCRAM-SHA-256, etc.)
  string mechanism = 1 [(buf.validate.field).string.min_len = 1];

  // Username
  string username = 2 [(buf.validate.field).string.min_len = 1];

  // Password
  string password = 3 [(buf.validate.field).string.min_len = 8];

  // Additional SASL properties
  map<string, string> properties = 4;
}
```

---

### schema_validation.proto {#schema_validation}

**Path**: `gcommon/v1/queue/schema_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `SchemaValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_validation.proto
// version: 1.0.0
// guid: ee7fffd9-460b-48d0-bea8-533482d34e85

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SchemaValidation {
  // Schema validation passed
  bool passed = 1;

  // Schema version in backup
  string backup_schema_version = 2 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Current schema version
  string current_schema_version = 3 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Schema compatibility status
  string compatibility_status = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### size_bucket.proto {#size_bucket}

**Path**: `gcommon/v1/queue/size_bucket.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `SizeBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/size_bucket.proto
// version: 1.0.0
// guid: 01e90e2f-62e8-47a9-86bf-0a684d65a463

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SizeBucket {
  int64 min_size_bytes = 1 [(buf.validate.field).int64.gte = 0];
  int64 max_size_bytes = 2 [(buf.validate.field).int64.gte = 0];
  int64 message_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### size_distribution.proto {#size_distribution}

**Path**: `gcommon/v1/queue/size_distribution.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `SizeDistribution`

**Imports** (3):

- `gcommon/v1/queue/size_bucket.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/size_distribution.proto
// version: 1.0.0
// guid: 6a630c77-ef52-498c-b0c7-0be5177f3a90

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/size_bucket.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SizeDistribution {
  // Size buckets in bytes
  repeated SizeBucket buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Summary statistics
  int64 min_size_bytes = 2 [(buf.validate.field).int64.gte = 0];
  int64 max_size_bytes = 3 [(buf.validate.field).int64.gte = 0];
  double average_size_bytes = 4 [(buf.validate.field).double.gte = 0.0];
  double median_size_bytes = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### size_range.proto {#size_range}

**Path**: `gcommon/v1/queue/size_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `SizeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/size_range.proto
// version: 1.0.0
// guid: 644269a7-7ae9-4ab3-98d3-d7111c89451b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Size range for filtering.
 */
message SizeRange {
  // Minimum size in bytes (inclusive)
  int64 min_size = 1 [(buf.validate.field).int64.gte = 0];

  // Maximum size in bytes (inclusive)
  int64 max_size = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### subscription_info.proto {#subscription_info}

**Path**: `gcommon/v1/queue/subscription_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `QueueSubscriptionInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_info.proto
// version: 1.0.0
// guid: 9b9d0532-72ff-4a42-b3b2-689a1a26dd9f

// SubscriptionInfo provides metadata about a subscription to a topic
// or queue. It replaces the placeholder file created during the
// 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * SubscriptionInfo describes a subscriber's configuration and status.
 */
message QueueSubscriptionInfo {
  // Name of the subscription
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic or queue this subscription belongs to
  string topic = 2;

  // Whether the subscription is currently active
  bool active = 3;

  // Number of pending messages for this subscription
  int64 pending_message_count = 4;

  // Time when the subscription was created
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // Arbitrary labels associated with the subscription
  map<string, string> labels = 6;
}
```

---

