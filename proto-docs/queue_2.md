# queue_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 31
- **Messages**: 16
- **Services**: 0
- **Enums**: 15
- ⚠️ **Issues**: 3

## Files in this Module

- [queue_info.proto](#queue_info) ⚠️ 1 issues
- [queue_message.proto](#queue_message)
- [queue_state.proto](#queue_state)
- [queue_stats.proto](#queue_stats)
- [queue_type.proto](#queue_type)
- [received_message.proto](#received_message)
- [replication_mode.proto](#replication_mode)
- [retention_policy.proto](#retention_policy)
- [retry_delay_strategy.proto](#retry_delay_strategy)
- [retry_policy.proto](#retry_policy)
- [routing_condition.proto](#routing_condition)
- [routing_key.proto](#routing_key)
- [routing_pattern.proto](#routing_pattern)
- [routing_rule.proto](#routing_rule)
- [routing_strategy.proto](#routing_strategy)
- [schema_compatibility_mode.proto](#schema_compatibility_mode)
- [schema_evolution_strategy.proto](#schema_evolution_strategy)
- [schema_format.proto](#schema_format)
- [serialization_format.proto](#serialization_format)
- [size_range.proto](#size_range)
- [statistic_grouping.proto](#statistic_grouping)
- [statistic_type.proto](#statistic_type)
- [stats_granularity.proto](#stats_granularity)
- [stream_restart_policy.proto](#stream_restart_policy)
- [subscription_info.proto](#subscription_info) ⚠️ 1 issues
- [subscription_state.proto](#subscription_state)
- [subscription_stats.proto](#subscription_stats)
- [time_range.proto](#time_range)
- [timestamp_range.proto](#timestamp_range) ⚠️ 1 issues
- [topic_info.proto](#topic_info)
- [topic_stats.proto](#topic_stats)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)

**Modules that depend on this one**:

- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_1](./queue_1.md)
- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [queue_config](./queue_config.md)
- [queue_services](./queue_services.md)

---

## Detailed Documentation

### queue_info.proto {#queue_info}

**Path**: `pkg/queue/proto/queue_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 40

**Messages** (1): `QueueInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // empty placeholder created during the 1-1-1
  migration.

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/queue_info.proto
// version: 1.0.0
// guid: d2ab2b72-14e2-4afe-80f7-2ecf00daacac

// QueueInfo provides metadata about a queue instance. This replaces the
// empty placeholder created during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * QueueInfo describes the configuration and current status of a queue.
 * It is returned by administrative APIs such as ListQueues.
 */
message QueueInfo {
  // Name of the queue
  string name = 1;

  // Type of queue implementation (e.g., "rabbitmq", "nats")
  string type = 2;

  // Current approximate number of messages in the queue
  int64 message_count = 3;

  // Number of active consumers
  int32 consumer_count = 4;

  // Time when the queue was created
  google.protobuf.Timestamp created_at = 5;

  // Additional metadata or labels for the queue
  map<string, string> labels = 6;
}

```

---

### queue_message.proto {#queue_message}

**Path**: `pkg/queue/proto/queue_message.proto` **Package**: `gcommon.v1.queue`
**Lines**: 51

**Messages** (1): `QueueMessage`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: queue/proto/messages/queue_message.proto
// version: 1.0.0
// guid: a2597962-4731-4f47-b6dd-4da9a937c834

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// QueueMessage represents a single item in a queue.
message QueueMessage {
  // Message ID (auto-generated if not provided).
  string id = 1;

  // Arbitrary payload for the message.
  google.protobuf.Any body = 2;

  // Custom key/value attributes for routing or metadata.
  map<string, string> attributes = 3;

  // Additional headers attached to the message.
  map<string, string> headers = 4;

  // Priority value (0-255, higher values processed first).
  int32 priority = 5;

  // Expiration time for the message.
  google.protobuf.Timestamp expires_at = 6;

  // Optional correlation identifier.
  string correlation_id = 7;

  // Queue name for replies.
  string reply_to = 8;

  // MIME type of the message body.
  string content_type = 9;

  // Encoding used for the message body.
  string content_encoding = 10;

  // Creation timestamp of the message.
  google.protobuf.Timestamp created_at = 11;
}

```

---

### queue_state.proto {#queue_state}

**Path**: `pkg/queue/proto/queue_state.proto` **Package**: `gcommon.v1.queue`
**Lines**: 42

**Enums** (1): `QueueState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/queue_state.proto
// file: queue/proto/enums/queue_state.proto
// version: 1.0.0
// guid: 8f9a0b1c-2d3e-4f5a-6b7c-8d9e0f1a2b3c
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Represents the operational state of a queue.
 */
enum QueueState {
  // Default unknown state
  QUEUE_STATE_UNSPECIFIED = 0;

  // Queue is active and processing messages
  QUEUE_STATE_ACTIVE = 1;

  // Queue is paused (not processing messages but accepting them)
  QUEUE_STATE_PAUSED = 2;

  // Queue is suspended (not accepting new messages)
  QUEUE_STATE_SUSPENDED = 3;

  // Queue is in the process of being deleted
  QUEUE_STATE_DELETING = 4;

  // Queue is in maintenance mode
  QUEUE_STATE_MAINTENANCE = 5;

  // Queue has encountered an error and needs attention
  QUEUE_STATE_ERROR = 6;
}

```

---

### queue_stats.proto {#queue_stats}

**Path**: `pkg/queue/proto/queue_stats.proto` **Package**: `gcommon.v1.queue`
**Lines**: 51

**Messages** (1): `BasicQueueStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/queue_stats.proto
// file: queue/proto/messages/queue_stats.proto
// version: 1.0.0
// guid: 0e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Basic statistics for a queue.
 */
message BasicQueueStats {
  // Queue name
  string queue_name = 1;

  // Total number of messages in the queue
  uint64 total_messages = 2;

  // Number of unacknowledged messages
  uint64 unacked_messages = 3;

  // Queue size in bytes
  uint64 size_bytes = 4;

  // Number of consumers
  uint32 consumer_count = 5;

  // Number of producers
  uint32 producer_count = 6;

  // Messages per second (ingress rate)
  double ingress_rate = 7;

  // Messages per second (egress rate)
  double egress_rate = 8;

  // Average message size in bytes
  double avg_message_size = 9;

  // Queue depth (oldest unprocessed message age)
  uint64 queue_depth_ms = 10;
}

```

---

### queue_type.proto {#queue_type}

**Path**: `pkg/queue/proto/queue_type.proto` **Package**: `gcommon.v1.queue`
**Lines**: 27

**Enums** (1): `QueueType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/queue_type.proto
// version: 1.0.0
// guid: d6bb0e83-91d3-406a-9a66-519b5860d137

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// QueueType enumerates supported queue implementations.
enum QueueType {
  // Default unspecified implementation.
  QUEUE_TYPE_UNSPECIFIED = 0;
  // In-memory queue for testing or lightweight workloads.
  QUEUE_TYPE_MEMORY = 1;
  // Redis-backed queue.
  QUEUE_TYPE_REDIS = 2;
  // NATS-based streaming queue.
  QUEUE_TYPE_NATS = 3;
  // Cloud provider queue (e.g., AWS SQS).
  QUEUE_TYPE_CLOUD = 4;
}

```

---

### received_message.proto {#received_message}

**Path**: `pkg/queue/proto/received_message.proto` **Package**:
`gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ReceivedMessage`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/received_message.proto
// version: 1.0.0
// guid: c7d8e9f0-123a-567b-8901-123456789012

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ReceivedMessage {
  // Message ID
  string id = 1;

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

### replication_mode.proto {#replication_mode}

**Path**: `pkg/queue/proto/replication_mode.proto` **Package**:
`gcommon.v1.queue` **Lines**: 42

**Enums** (1): `ReplicationMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/replication_mode.proto
// file: queue/proto/enums/replication_mode.proto
// version: 1.0.0
// guid: 6d7e8f9a-0b1c-2d3e-4f5a-6b7c8d9e0f1a
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Replication mode for queue data across multiple nodes.
 */
enum ReplicationMode {
  // Default unspecified replication mode
  REPLICATION_MODE_UNSPECIFIED = 0;

  // No replication - single node only
  REPLICATION_MODE_NONE = 1;

  // Synchronous replication - wait for all replicas
  REPLICATION_MODE_SYNC = 2;

  // Asynchronous replication - don't wait for replicas
  REPLICATION_MODE_ASYNC = 3;

  // Quorum-based replication - wait for majority
  REPLICATION_MODE_QUORUM = 4;

  // Leader-follower replication
  REPLICATION_MODE_LEADER_FOLLOWER = 5;

  // Master-slave replication (legacy term)
  REPLICATION_MODE_MASTER_SLAVE = 6;
}

```

---

### retention_policy.proto {#retention_policy}

**Path**: `pkg/queue/proto/retention_policy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 24

**Messages** (1): `RetentionPolicy`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/retention_policy.proto
// version: 1.0.0
// guid: 5a069bb8-66bf-413e-a9e8-a1856f52eb01

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// RetentionPolicy controls how long messages are kept before deletion.
message RetentionPolicy {
  // Maximum age of a message before it is removed.
  google.protobuf.Duration max_age = 1;
  // Maximum total storage size for the queue in bytes.
  int64 max_size_bytes = 2;
  // If true, older messages are discarded when limits are reached.
  bool discard_old = 3;
}

```

---

### retry_delay_strategy.proto {#retry_delay_strategy}

**Path**: `pkg/queue/proto/retry_delay_strategy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 34

**Enums** (1): `RetryDelayStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/retry_delay_strategy.proto
// version: 1.0.0
// guid: e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Strategy for calculating retry delays.
 * Specifies how delays between retry attempts are computed.
 */
enum RetryDelayStrategy {
  // Default unspecified strategy
  RETRY_DELAY_STRATEGY_UNSPECIFIED = 0;

  // Fixed delay between retries
  RETRY_DELAY_STRATEGY_FIXED = 1;

  // Linear backoff (delay increases linearly)
  RETRY_DELAY_STRATEGY_LINEAR = 2;

  // Exponential backoff (delay doubles each time)
  RETRY_DELAY_STRATEGY_EXPONENTIAL = 3;

  // Custom backoff strategy
  RETRY_DELAY_STRATEGY_CUSTOM = 4;
}

```

---

### retry_policy.proto {#retry_policy}

**Path**: `pkg/queue/proto/retry_policy.proto` **Package**: `gcommon.v1.queue`
**Lines**: 43

**Messages** (1): `RetryPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/retry_delay_strategy.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/retry_policy.proto
// version: 1.1.0
// guid: 4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/retry_delay_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Retry policy for failed message processing.
 * Defines how failed messages should be retried before being
 * sent to dead letter queue.
 */
message RetryPolicy {
  // Maximum number of retry attempts
  int32 max_attempts = 1;

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 2;

  // Maximum delay between retries
  google.protobuf.Duration max_delay = 3;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 4;

  // Retry delay strategy
  RetryDelayStrategy delay_strategy = 5;

  // Whether to enable jitter in retry delays
  bool enable_jitter = 6;

  // Jitter factor (0.0 to 1.0) for randomizing delays
  double jitter_factor = 7;
}

```

---

### routing_condition.proto {#routing_condition}

**Path**: `pkg/queue/proto/routing_condition.proto` **Package**:
`gcommon.v1.queue` **Lines**: 38

**Messages** (1): `RoutingCondition`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/priority_range.proto` →
  [queue_1](./queue_1.md#priority_range)
- `pkg/queue/proto/size_range.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/routing_condition.proto
// version: 1.0.0
// guid: c5586126-e8b2-47e8-b657-e837b38179bd

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/priority_range.proto";
import "pkg/queue/proto/size_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Condition for routing rules.
 */
message RoutingCondition {
  // Header-based conditions
  map<string, string> header_matches = 1;

  // Content pattern matching
  string content_pattern = 2;

  // Routing key pattern
  string routing_key_pattern = 3;

  // Message type filter
  string message_type = 4;

  // Priority range filter
  PriorityRange priority_range = 5;

  // Size range filter
  SizeRange size_range = 6;
}

```

---

### routing_key.proto {#routing_key}

**Path**: `pkg/queue/proto/routing_key.proto` **Package**: `gcommon.v1.queue`
**Lines**: 35

**Messages** (1): `RoutingKey`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/routing_pattern.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/routing_key.proto
// version: 1.1.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/routing_pattern.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Routing key for message delivery.
 * Determines how messages are routed to queues and consumers.
 */
message RoutingKey {
  // The routing key string
  string key = 1;

  // Pattern type for key matching
  RoutingPattern pattern_type = 2;

  // Whether the pattern is case sensitive
  bool case_sensitive = 3;

  // Priority for routing (higher numbers = higher priority)
  int32 priority = 4;

  // Additional routing attributes
  map<string, string> attributes = 5;
}

```

---

### routing_pattern.proto {#routing_pattern}

**Path**: `pkg/queue/proto/routing_pattern.proto` **Package**:
`gcommon.v1.queue` **Lines**: 37

**Enums** (1): `RoutingPattern`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/routing_pattern.proto
// version: 1.0.0
// guid: f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Routing pattern types for key matching.
 * Specifies how routing keys are matched against patterns.
 */
enum RoutingPattern {
  // Exact string match
  ROUTING_PATTERN_EXACT = 0;

  // Wildcard pattern (* and ?)
  ROUTING_PATTERN_WILDCARD = 1;

  // Regular expression pattern
  ROUTING_PATTERN_REGEX = 2;

  // Topic-style pattern (dot separated, # and * wildcards)
  ROUTING_PATTERN_TOPIC = 3;

  // Prefix match
  ROUTING_PATTERN_PREFIX = 4;

  // Suffix match
  ROUTING_PATTERN_SUFFIX = 5;
}

```

---

### routing_rule.proto {#routing_rule}

**Path**: `pkg/queue/proto/routing_rule.proto` **Package**: `gcommon.v1.queue`
**Lines**: 37

**Messages** (1): `RoutingRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/routing_condition.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/routing_rule.proto
// version: 1.0.0
// guid: 6ce2389f-a9b6-4850-bdf9-6b5225cd61d4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/routing_condition.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Individual routing rule.
 */
message RoutingRule {
  // Unique name for the rule
  string name = 1;

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

### routing_strategy.proto {#routing_strategy}

**Path**: `pkg/queue/proto/routing_strategy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Enums** (1): `RoutingStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/routing_strategy.proto
// version: 1.0.0
// guid: c0da3188-9710-4555-bbda-9632f6b3f29b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Routing strategies.
 */
enum RoutingStrategy {
  // Default unspecified strategy
  ROUTING_STRATEGY_UNSPECIFIED = 0;

  // Direct routing based on destination name
  ROUTING_STRATEGY_DIRECT = 1;

  // Topic-based routing using routing key
  ROUTING_STRATEGY_TOPIC = 2;

  // Fanout routing to all bound queues
  ROUTING_STRATEGY_FANOUT = 3;

  // Header-based routing using message headers
  ROUTING_STRATEGY_HEADER = 4;

  // Content-based routing using message content
  ROUTING_STRATEGY_CONTENT = 5;

  // Hash-based routing for load distribution
  ROUTING_STRATEGY_HASH = 6;
}

```

---

### schema_compatibility_mode.proto {#schema_compatibility_mode}

**Path**: `pkg/queue/proto/schema_compatibility_mode.proto` **Package**:
`gcommon.v1.queue` **Lines**: 31

**Enums** (1): `SchemaCompatibilityMode`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/serialization_format.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/schema_compatibility_mode.proto
// version: 1.0.0
// guid: 6c24f62f-1d37-4098-b5d4-a49e4a58d05e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Schema compatibility modes.
 */
enum SchemaCompatibilityMode {
  // Default unspecified mode
  SCHEMA_COMPATIBILITY_MODE_UNSPECIFIED = 0;

  // Strict compatibility checking
  SCHEMA_COMPATIBILITY_MODE_STRICT = 1;

  // Lenient compatibility checking
  SCHEMA_COMPATIBILITY_MODE_LENIENT = 2;

  // No compatibility checking
  SCHEMA_COMPATIBILITY_MODE_NONE = 3;
}

```

---

### schema_evolution_strategy.proto {#schema_evolution_strategy}

**Path**: `pkg/queue/proto/schema_evolution_strategy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 37

**Enums** (1): `SchemaEvolutionStrategy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/serialization_format.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/schema_evolution_strategy.proto
// version: 1.0.0
// guid: ef5f0572-3b2c-44c1-8e1c-247b8fad9c9c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Schema evolution strategies.
 */
enum SchemaEvolutionStrategy {
  // Default unspecified strategy
  SCHEMA_EVOLUTION_STRATEGY_UNSPECIFIED = 0;

  // No evolution allowed
  SCHEMA_EVOLUTION_STRATEGY_NONE = 1;

  // Forward compatibility (new schema can read old data)
  SCHEMA_EVOLUTION_STRATEGY_FORWARD = 2;

  // Backward compatibility (old schema can read new data)
  SCHEMA_EVOLUTION_STRATEGY_BACKWARD = 3;

  // Full compatibility (bidirectional)
  SCHEMA_EVOLUTION_STRATEGY_FULL = 4;

  // No compatibility checks
  SCHEMA_EVOLUTION_STRATEGY_NONE_CHECK = 5;
}

```

---

### schema_format.proto {#schema_format}

**Path**: `pkg/queue/proto/schema_format.proto` **Package**: `gcommon.v1.queue`
**Lines**: 37

**Enums** (1): `SchemaFormat`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/serialization_format.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/schema_format.proto
// version: 1.0.0
// guid: 8dbf53aa-e92d-4de4-84a8-ec3fb37ce521

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Schema format types.
 */
enum SchemaFormat {
  // Default unspecified format
  SCHEMA_FORMAT_UNSPECIFIED = 0;

  // JSON Schema format
  SCHEMA_FORMAT_JSON_SCHEMA = 1;

  // Apache Avro schema
  SCHEMA_FORMAT_AVRO = 2;

  // Protocol Buffers schema
  SCHEMA_FORMAT_PROTOBUF = 3;

  // XML Schema (XSD)
  SCHEMA_FORMAT_XML_SCHEMA = 4;

  // Custom schema format
  SCHEMA_FORMAT_CUSTOM = 5;
}

```

---

### serialization_format.proto {#serialization_format}

**Path**: `pkg/queue/proto/serialization_format.proto` **Package**:
`gcommon.v1.queue` **Lines**: 45

**Enums** (1): `SerializationFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/serialization_format.proto
// file: queue/proto/enums/serialization_format.proto
// version: 1.0.0
// guid: 7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Supported message serialization formats for queue messages.
 */
enum SerializationFormat {
  // Default unspecified format
  SERIALIZATION_FORMAT_UNSPECIFIED = 0;

  // Protocol Buffers binary format
  SERIALIZATION_FORMAT_PROTOBUF = 1;

  // JSON text format
  SERIALIZATION_FORMAT_JSON = 2;

  // MessagePack binary format
  SERIALIZATION_FORMAT_MSGPACK = 3;

  // Apache Avro binary format
  SERIALIZATION_FORMAT_AVRO = 4;

  // Raw binary data (no specific format)
  SERIALIZATION_FORMAT_BINARY = 5;

  // Plain text format
  SERIALIZATION_FORMAT_TEXT = 6;

  // XML format
  SERIALIZATION_FORMAT_XML = 7;
}

```

---

### size_range.proto {#size_range}

**Path**: `pkg/queue/proto/size_range.proto` **Package**: `gcommon.v1.queue`
**Lines**: 24

**Messages** (1): `SizeRange`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/size_range.proto
// version: 1.0.0
// guid: 644269a7-7ae9-4ab3-98d3-d7111c89451b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Size range for filtering.
 */
message SizeRange {
  // Minimum size in bytes (inclusive)
  int64 min_size = 1;

  // Maximum size in bytes (inclusive)
  int64 max_size = 2;
}

```

---

### statistic_grouping.proto {#statistic_grouping}

**Path**: `pkg/queue/proto/statistic_grouping.proto` **Package**:
`gcommon.v1.queue` **Lines**: 23

**Enums** (1): `StatisticGrouping`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/statistic_grouping.proto
// version: 1.0.0
// guid: a8a72b1a-cc3a-46d1-a1ab-87af3535faac

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

enum StatisticGrouping {
  STATISTIC_GROUPING_UNSPECIFIED = 0;
  STATISTIC_GROUPING_NONE = 1; // No grouping, flat statistics
  STATISTIC_GROUPING_BY_QUEUE = 2; // Group by queue name
  STATISTIC_GROUPING_BY_CONSUMER = 3; // Group by consumer
  STATISTIC_GROUPING_BY_TIME_PERIOD = 4; // Group by time periods
  STATISTIC_GROUPING_BY_MESSAGE_TYPE = 5; // Group by message type
}

```

---

### statistic_type.proto {#statistic_type}

**Path**: `pkg/queue/proto/statistic_type.proto` **Package**: `gcommon.v1.queue`
**Lines**: 28

**Enums** (1): `StatisticType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/statistic_type.proto
// version: 1.0.0
// guid: cb4f227d-f3e9-4698-aa3e-776544976e01

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

enum StatisticType {
  STATISTIC_TYPE_UNSPECIFIED = 0;
  STATISTIC_TYPE_MESSAGE_COUNT = 1;
  STATISTIC_TYPE_THROUGHPUT = 2;
  STATISTIC_TYPE_LATENCY = 3;
  STATISTIC_TYPE_ERROR_RATE = 4;
  STATISTIC_TYPE_QUEUE_DEPTH = 5;
  STATISTIC_TYPE_PROCESSING_TIME = 6;
  STATISTIC_TYPE_CONSUMER_COUNT = 7;
  STATISTIC_TYPE_MESSAGE_SIZE = 8;
  STATISTIC_TYPE_AGE_DISTRIBUTION = 9;
  STATISTIC_TYPE_SUCCESS_RATE = 10;
}

```

---

### stats_granularity.proto {#stats_granularity}

**Path**: `pkg/queue/proto/stats_granularity.proto` **Package**:
`gcommon.v1.queue` **Lines**: 34

**Enums** (1): `StatsGranularity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/stats_granularity.proto
// version: 1.0.0
// guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * StatsGranularity represents the granularity for statistics.
 * Specifies the time interval granularity for statistical data collection and aggregation.
 */
enum StatsGranularity {
  // Default unspecified granularity
  STATS_GRANULARITY_UNSPECIFIED = 0;

  // Minute-level granularity
  STATS_GRANULARITY_MINUTE = 1;

  // Hour-level granularity
  STATS_GRANULARITY_HOUR = 2;

  // Day-level granularity
  STATS_GRANULARITY_DAY = 3;

  // Week-level granularity
  STATS_GRANULARITY_WEEK = 4;
}

```

---

### stream_restart_policy.proto {#stream_restart_policy}

**Path**: `pkg/queue/proto/stream_restart_policy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 36

**Enums** (1): `StreamRestartPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/stream_restart_policy.proto
// file: queue/proto/enums/stream_restart_policy.proto
// version: 1.0.0
// guid: 6a5b4c3d-2e1f-0a9b-8c7d-6e5f4a3b2c1d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Stream restart behavior on failures.
 */
enum StreamRestartPolicy {
  // Default unspecified policy
  STREAM_RESTART_POLICY_UNSPECIFIED = 0;

  // Never restart streams automatically
  STREAM_RESTART_POLICY_NEVER = 1;

  // Restart immediately on failure
  STREAM_RESTART_POLICY_IMMEDIATE = 2;

  // Restart with exponential backoff
  STREAM_RESTART_POLICY_EXPONENTIAL_BACKOFF = 3;

  // Restart with fixed delay
  STREAM_RESTART_POLICY_FIXED_DELAY = 4;
}

```

---

### subscription_info.proto {#subscription_info}

**Path**: `pkg/queue/proto/subscription_info.proto` **Package**:
`gcommon.v1.queue` **Lines**: 40

**Messages** (1): `SubscriptionInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // or queue. It replaces the placeholder file
  created during the

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/subscription_info.proto
// version: 1.0.0
// guid: 9b9d0532-72ff-4a42-b3b2-689a1a26dd9f

// SubscriptionInfo provides metadata about a subscription to a topic
// or queue. It replaces the placeholder file created during the
// 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * SubscriptionInfo describes a subscriber's configuration and status.
 */
message SubscriptionInfo {
  // Name of the subscription
  string name = 1;

  // Topic or queue this subscription belongs to
  string topic = 2;

  // Whether the subscription is currently active
  bool active = 3;

  // Number of pending messages for this subscription
  int64 pending_message_count = 4;

  // Time when the subscription was created
  google.protobuf.Timestamp created_at = 5;

  // Arbitrary labels associated with the subscription
  map<string, string> labels = 6;
}

```

---

### subscription_state.proto {#subscription_state}

**Path**: `pkg/queue/proto/subscription_state.proto` **Package**:
`gcommon.v1.queue` **Lines**: 25

**Enums** (1): `SubscriptionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/subscription_state.proto
// version: 1.0.0
// guid: ddd7bd85-a329-4347-be1d-18983916cd3e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// SubscriptionState describes the lifecycle state of a subscription.
enum SubscriptionState {
  // Default state. Server decides behavior.
  SUBSCRIPTION_STATE_UNSPECIFIED = 0;
  // Actively receiving messages.
  SUBSCRIPTION_STATE_ACTIVE = 1;
  // Temporarily paused from delivering messages.
  SUBSCRIPTION_STATE_PAUSED = 2;
  // Permanently closed and cannot be resumed.
  SUBSCRIPTION_STATE_CLOSED = 3;
}

```

---

### subscription_stats.proto {#subscription_stats}

**Path**: `pkg/queue/proto/subscription_stats.proto` **Package**:
`gcommon.v1.queue` **Lines**: 48

**Messages** (1): `SubscriptionStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/subscription_stats.proto
// file: queue/proto/messages/subscription_stats.proto
// version: 1.0.0
// guid: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Statistics for a subscription.
 */
message SubscriptionStats {
  // Subscription identifier
  string subscription_id = 1;

  // Number of messages consumed
  uint64 messages_consumed = 2;

  // Number of messages acknowledged
  uint64 messages_acknowledged = 3;

  // Number of messages rejected/nacked
  uint64 messages_rejected = 4;

  // Current lag (unprocessed messages)
  uint64 consumer_lag = 5;

  // Messages per second consumption rate
  double consumption_rate = 6;

  // Average processing time per message (milliseconds)
  double avg_processing_time_ms = 7;

  // Number of active consumers
  uint32 active_consumers = 8;

  // Last activity timestamp
  uint64 last_activity_time = 9;
}

```

---

### time_range.proto {#time_range}

**Path**: `pkg/queue/proto/time_range.proto` **Package**: `gcommon.v1.queue`
**Lines**: 29

**Messages** (1): `TimeRange`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/time_range.proto
// file: queue/proto/messages/time_range.proto
// version: 1.0.0
// guid: 2a1b0c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Time range for filtering messages.
 */
message TimeRange {
  // Start time (inclusive)
  google.protobuf.Timestamp start_time = 1;

  // End time (exclusive)
  google.protobuf.Timestamp end_time = 2;
}

```

---

### timestamp_range.proto {#timestamp_range}

**Path**: `pkg/queue/proto/timestamp_range.proto` **Package**:
`gcommon.v1.queue` **Lines**: 27

**Messages** (1): `TimestampRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // statistics queries. This implementation
  replaces the placeholder

#### Source Code

```protobuf
// file: pkg/queue/proto/types/timestamp_range.proto
// version: 1.0.0
// guid: 4fdb7c93-4616-4db9-a2d6-50f41676b4b6

// TimestampRange defines a start and end time for filtering or
// statistics queries. This implementation replaces the placeholder
// added during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// TimestampRange is used to specify a time window when querying
// statistics or messages.
message TimestampRange {
  // Start of the range (inclusive).
  google.protobuf.Timestamp start = 1;

  // End of the range (exclusive).
  google.protobuf.Timestamp end = 2;
}

```

---

### topic_info.proto {#topic_info}

**Path**: `pkg/queue/proto/topic_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 50

**Messages** (1): `TopicInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/topic_info.proto
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Topic information for queue management.
 * Contains metadata and status about a message queue topic.
 */
message TopicInfo {
  // Topic name/identifier
  string name = 1;

  // Topic description
  string description = 2;

  // Topic creation timestamp
  google.protobuf.Timestamp created_at = 3 [lazy = true];

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

### topic_stats.proto {#topic_stats}

**Path**: `pkg/queue/proto/topic_stats.proto` **Package**: `gcommon.v1.queue`
**Lines**: 48

**Messages** (1): `TopicStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/topic_stats.proto
// file: queue/proto/messages/topic_stats.proto
// version: 1.0.0
// guid: 9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Statistics information for a topic.
 */
message TopicStats {
  // Name of the topic
  string topic_name = 1;

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
