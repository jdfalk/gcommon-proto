# queue_config_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 17
- **Messages**: 17
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [subscription_config_update.proto](#subscription_config_update)
- [subscription_configuration.proto](#subscription_configuration)
- [timeout_config.proto](#timeout_config)
- [timestamp_config.proto](#timestamp_config)
- [topic_config.proto](#topic_config)
- [topic_configuration.proto](#topic_configuration)
- [topic_routing_config.proto](#topic_routing_config)
- [transformation_config.proto](#transformation_config)
- [update_queue_config_request.proto](#update_queue_config_request)
- [update_queue_config_response.proto](#update_queue_config_response)
- [update_subscription_config_request.proto](#update_subscription_config_request)
- [update_subscription_config_response.proto](#update_subscription_config_response)
- [update_topic_config_request.proto](#update_topic_config_request)
- [update_topic_config_response.proto](#update_topic_config_response)
- [validation_config.proto](#validation_config)
- [vector_clock_config.proto](#vector_clock_config)
- [write_retry_config.proto](#write_retry_config)
---


## Detailed Documentation

### subscription_config_update.proto {#subscription_config_update}

**Path**: `gcommon/v1/queue/subscription_config_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `SubscriptionConfigUpdate`

**Imports** (6):

- `gcommon/v1/common/config_retry_settings.proto`
- `gcommon/v1/queue/delivery_settings.proto`
- `gcommon/v1/queue/filter_settings.proto`
- `gcommon/v1/queue/routing_settings.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_config_update.proto
// version: 1.0.0
// guid: 4ec44184-d7ed-48cf-af8f-5984c57c687d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/config_retry_settings.proto";
import "gcommon/v1/queue/delivery_settings.proto";
import "gcommon/v1/queue/filter_settings.proto";
import "gcommon/v1/queue/routing_settings.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SubscriptionConfigUpdate {
  // Updated subscription name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated delivery settings
  DeliverySettings delivery_settings = 2;

  // Updated retry configuration
  gcommon.v1.common.ConfigRetrySettings retry_settings = 3;

  // Updated filtering rules
  FilterSettings filter_settings = 4;

  // Updated routing configuration
  RoutingSettings routing_settings = 5;

  // Maximum inflight messages
  int32 max_inflight_messages = 6;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 7;

  // Priority level for messages
  int32 priority_level = 8;
}
```

---

### subscription_configuration.proto {#subscription_configuration}

**Path**: `gcommon/v1/queue/subscription_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `SubscriptionConfiguration`

**Imports** (4):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/common/delivery_mode.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_configuration.proto
// version: 1.0.0
// guid: c1883113-aa7a-4cba-b38a-4d695cefecf3

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/common/delivery_mode.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SubscriptionConfiguration {
  // Acknowledgment level required
  gcommon.v1.common.AckLevel ack_level = 1;

  // Delivery mode for messages
  gcommon.v1.common.DeliveryMode delivery_mode = 2;

  // Maximum number of unacknowledged messages
  int32 max_unacked_messages = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Message priority filter (minimum priority)
  int32 min_priority = 5 [(buf.validate.field).int32.gte = 0];

  // Enable message ordering
  bool ordered_delivery = 6;

  // Auto-acknowledge messages after delivery
  bool auto_acknowledge = 7;

  // Subscription expiration time (seconds, 0 = no expiration)
  int64 expiration_seconds = 8 [(buf.validate.field).int64.gte = 0];

  // Enable duplicate message detection
  bool duplicate_detection = 9;

  // Maximum message age to accept (seconds)
  int64 max_message_age_seconds = 10 [(buf.validate.field).int64.gte = 0];
}
```

---

### timeout_config.proto {#timeout_config}

**Path**: `gcommon/v1/queue/timeout_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `QueueTimeoutConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/timeout_config.proto
// file: proto/gcommon/v1/queue/timeout_config.proto
// version: 1.0.1
// guid: 3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Timeout configuration for various queue operations.
 */
message QueueTimeoutConfig {
  // Timeout for message publishing operations
  google.protobuf.Duration publish_timeout = 1;

  // Timeout for message consumption operations
  google.protobuf.Duration consume_timeout = 2;

  // Timeout for acknowledgment operations
  google.protobuf.Duration ack_timeout = 3;

  // Timeout for connection establishment
  google.protobuf.Duration connect_timeout = 4;

  // Timeout for message processing before automatic nack
  google.protobuf.Duration processing_timeout = 5;

  // Timeout for queue management operations (create, delete, etc.)
  google.protobuf.Duration management_timeout = 6;

  // Timeout for health check operations
  google.protobuf.Duration health_check_timeout = 7;

  // Timeout for subscription operations
  google.protobuf.Duration subscription_timeout = 8;
}
```

---

### timestamp_config.proto {#timestamp_config}

**Path**: `gcommon/v1/queue/timestamp_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `TimestampConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/timestamp_config.proto
// version: 1.0.0
// guid: 5767f48a-e0df-4536-9127-4fcbd0ed4e1e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TimestampConfig {
  // Timestamp source (system, ntp, atomic)
  string source = 1 [(buf.validate.field).string.min_len = 1];

  // Clock synchronization interval (seconds)
  int32 sync_interval_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum timestamp skew tolerance (milliseconds)
  int64 max_skew_ms = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### topic_config.proto {#topic_config}

**Path**: `gcommon/v1/queue/topic_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `TopicConfig`

**Imports** (4):

- `gcommon/v1/queue/partition_config.proto`
- `gcommon/v1/queue/retention_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/topic_config.proto
// file: proto/gcommon/v1/queue/topic_config.proto
// version: 1.0.0
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/partition_config.proto";
import "gcommon/v1/queue/retention_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration settings for a topic.
 */
message TopicConfig {
  // Maximum number of messages in the topic
  uint64 max_messages = 1 [(buf.validate.field).uint64.gte = 0];

  // Maximum size of the topic in bytes
  uint64 max_size_bytes = 2 [(buf.validate.field).uint64.gte = 0];

  // Message retention policy
  QueueRetentionPolicy retention_policy = 3;

  // Partitioning configuration
  PartitionConfig partition_config = 4;

  // Whether messages are persistent
  bool persistent = 5;

  // Whether topic is replicated
  bool replicated = 6;

  // Replication factor
  uint32 replication_factor = 7 [(buf.validate.field).uint32.gte = 0];

  // Whether to compact duplicate messages
  bool enable_compaction = 8;
}
```

---

### topic_configuration.proto {#topic_configuration}

**Path**: `gcommon/v1/queue/topic_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `TopicConfiguration`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_configuration.proto
// version: 1.0.0
// guid: 5214c267-e8b7-4b1c-af8d-d3343914c498

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TopicConfiguration {
  // Number of partitions
  int32 partition_count = 1 [(buf.validate.field).int32.gte = 0];

  // Replication factor
  int32 replication_factor = 2 [(buf.validate.field).int32.gte = 0];

  // Message retention period (seconds)
  int64 retention_period_seconds = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum message size (bytes)
  int64 max_message_size_bytes = 4 [(buf.validate.field).int64.gte = 0];

  // Compression enabled
  bool compression_enabled = 5;

  // Compression algorithm
  string compression_algorithm = 6 [(buf.validate.field).string.min_len = 1];

  // Encryption enabled
  bool encryption_enabled = 7;

  // Cleanup policy (delete, compact)
  string cleanup_policy = 8 [(buf.validate.field).string.min_len = 1];

  // Minimum in-sync replicas
  int32 min_insync_replicas = 9 [(buf.validate.field).int32.gte = 0];

  // Segment size (bytes)
  int64 segment_size_bytes = 10 [(buf.validate.field).int64.gte = 0];
}
```

---

### topic_routing_config.proto {#topic_routing_config}

**Path**: `gcommon/v1/queue/topic_routing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `TopicRoutingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_routing_config.proto
// version: 1.0.0
// guid: 502467f7-3d79-4329-8e44-4e499071092b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Topic-based routing configuration.
 */
message TopicRoutingConfig {
  // Topic exchange name
  string exchange_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Default routing key
  string default_routing_key = 2;

  // Whether to use wildcard matching
  bool wildcard_matching = 3;
}
```

---

### transformation_config.proto {#transformation_config}

**Path**: `gcommon/v1/queue/transformation_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `TransformationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/transformation_config.proto
// file: proto/gcommon/v1/queue/transformation_config.proto
// version: 1.0.0
// guid: 2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f
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
 * Configuration for message transformation operations.
 */
message TransformationConfig {
  // Whether transformation is enabled
  bool enabled = 1;

  // Transformation script or function name
  string transformation_script = 2 [(buf.validate.field).string.min_len = 1];

  // Script language (javascript, python, lua, etc.)
  string script_language = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to transform on ingress
  bool transform_on_ingress = 4;

  // Whether to transform on egress
  bool transform_on_egress = 5;

  // Transformation timeout in milliseconds
  uint64 timeout_ms = 6 [(buf.validate.field).uint64.gte = 0];

  // Maximum script execution memory in MB
  uint32 max_memory_mb = 7 [(buf.validate.field).uint32.gte = 0];

  // Custom transformation parameters
  map<string, string> parameters = 8;
}
```

---

### update_queue_config_request.proto {#update_queue_config_request}

**Path**: `gcommon/v1/queue/update_queue_config_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `UpdateQueueConfigRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_queue_config_request.proto
// version: 1.0.0
// guid: e2f3a4b5-c6d7-8e9f-0a1b-2c3d4e5f6a7b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to update configuration for an existing queue.
 * Allows modification of queue properties after creation.
 */
message UpdateQueueConfigRequest {
  // Name of the queue to update
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // New configuration for the queue
  // New queue configuration
  QueueConfig config = 2;

  // Fields to update (field mask)
  repeated string update_mask = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Force update even if it might cause data loss
  bool force = 5;

  // Reason for the configuration update
  string reason = 6;
}
```

---

### update_queue_config_response.proto {#update_queue_config_response}

**Path**: `gcommon/v1/queue/update_queue_config_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `UpdateQueueConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/update_queue_config_response.proto
// file: proto/gcommon/v1/queue/update_queue_config_response.proto
// version: 1.0.0
// guid: 6e7f8a9b-0c1d-2e3f-4a5b-6c7d8e9f0a1b
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for updating queue configuration.
 */
message UpdateQueueConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Error message if update failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Updated configuration version
  uint64 config_version = 3 [(buf.validate.field).uint64.gte = 0];

  // Timestamp of the update
  uint64 updated_at = 4 [(buf.validate.field).uint64.gte = 0];

  // List of configuration fields that were updated
  repeated string updated_fields = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### update_subscription_config_request.proto {#update_subscription_config_request}

**Path**: `gcommon/v1/queue/update_subscription_config_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `UpdateSubscriptionConfigRequest`

**Imports** (3):

- `gcommon/v1/queue/subscription_config_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_subscription_config_request.proto
// version: 1.0.0
// guid: 9ffb7149-231c-448f-9678-a8fa3130fe10

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/subscription_config_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateSubscriptionConfigRequest {
  // Subscription identifier
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration updates to apply
  SubscriptionConfigUpdate config_update = 2;

  // Specify which fields to update (empty = update all)
  repeated string update_fields = 3 [(buf.validate.field).repeated.min_items = 1];

  // Validate configuration without applying changes
  bool validate_only = 4;

  // Force update even if subscription is active
  bool force_update = 5;

  // Apply changes immediately or schedule for later
  bool immediate_apply = 6;

  // Optional reason for the configuration change
  string change_reason = 7 [(buf.validate.field).string.min_len = 1];

  // Metadata for the update operation
  map<string, string> metadata = 8;
}
```

---

### update_subscription_config_response.proto {#update_subscription_config_response}

**Path**: `gcommon/v1/queue/update_subscription_config_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `UpdateSubscriptionConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_subscription_config_response.proto
// version: 1.0.0
// guid: 43035b6d-1872-4b79-af8d-8852b38643e3
// Response for subscription configuration updates

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for subscription configuration updates
message UpdateSubscriptionConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Subscription ID that was updated
  string subscription_id = 2 [(buf.validate.field).string.min_len = 1];

  // Configuration changes that were applied
  map<string, string> applied_changes = 3;

  // Validation warnings (non-fatal)
  repeated string warnings = 4 [(buf.validate.field).repeated.min_items = 1];

  // Error message if update failed
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_topic_config_request.proto {#update_topic_config_request}

**Path**: `gcommon/v1/queue/update_topic_config_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `UpdateTopicConfigRequest`

**Imports** (3):

- `gcommon/v1/queue/topic_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_topic_config_request.proto
// version: 1.0.0
// guid: b7623d06-10e5-4b18-9b4f-976ff9116f5c
// Request to update topic configuration

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/topic_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to update topic configuration
message UpdateTopicConfigRequest {
  // Topic name to update
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // New topic configuration
  TopicConfig config = 2;

  // Whether to validate config before applying
  bool validate_only = 3;

  // Apply changes incrementally if possible
  bool incremental_update = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}
```

---

### update_topic_config_response.proto {#update_topic_config_response}

**Path**: `gcommon/v1/queue/update_topic_config_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `UpdateTopicConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/update_topic_config_response.proto
// file: proto/gcommon/v1/queue/update_topic_config_response.proto
// version: 1.0.0
// guid: 2e1f0d9c-8b7a-6e5f-4d3c-2b1a0f9e8d7c
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
 * Response message for topic configuration update operations.
 */
message UpdateTopicConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Error message if update failed
  string error_message = 2;

  // The name of the topic that was updated
  string topic_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Timestamp when the update was applied
  google.protobuf.Timestamp updated_at = 4;

  // Configuration revision number after update
  uint64 config_revision = 5;

  // List of configuration fields that were modified
  repeated string modified_fields = 6;

  // Validation warnings (non-fatal issues)
  repeated string warnings = 7;
}
```

---

### validation_config.proto {#validation_config}

**Path**: `gcommon/v1/queue/validation_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `ValidationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/validation_config.proto
// version: 1.0.0
// guid: 50a55c81-98ea-49a5-8d18-c188a48acc5f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ValidationConfig defines rules for validating queued messages.
message ValidationConfig {
  // Whether to validate message schema.
  bool validate_schema = 1;
  // Maximum allowed size of the message body in bytes.
  int64 max_body_bytes = 2 [(buf.validate.field).int64.gte = 0];
  // If true, reject messages that exceed validation limits.
  bool reject_invalid = 3;
}
```

---

### vector_clock_config.proto {#vector_clock_config}

**Path**: `gcommon/v1/queue/vector_clock_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `VectorClockConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/vector_clock_config.proto
// version: 1.0.0
// guid: 3374bcbe-3bf2-4e5f-b46a-03e4131fcd98

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message VectorClockConfig {
  // Enable vector clocks
  bool enabled = 1;

  // Clock precision (nanoseconds, microseconds, milliseconds)
  string precision = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum clock drift tolerance (milliseconds)
  int64 max_drift_ms = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### write_retry_config.proto {#write_retry_config}

**Path**: `gcommon/v1/queue/write_retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `WriteRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/write_retry_config.proto
// version: 1.0.0
// guid: c409f58a-7032-4fd2-b236-bd6bb3fc6f4c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message WriteRetryConfig {
  // Maximum retry attempts
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Retry idempotent operations only
  bool idempotent_only = 5;
}
```

---

