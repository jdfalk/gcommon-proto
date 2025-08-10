# queue_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 36
- **Services**: 0
- **Enums**: 28
- ⚠️ **Issues**: 2

## Files in this Module

- [ack_level.proto](#ack_level)
- [ack_type.proto](#ack_type)
- [acknowledgment.proto](#acknowledgment)
- [acknowledgment_mode.proto](#acknowledgment_mode) ⚠️ 1 issues
- [alert_condition.proto](#alert_condition)
- [alert_rule.proto](#alert_rule)
- [alert_severity.proto](#alert_severity)
- [anti_affinity_rule.proto](#anti_affinity_rule)
- [anti_affinity_scope.proto](#anti_affinity_scope)
- [binding_info.proto](#binding_info)
- [cluster_info.proto](#cluster_info)
- [cluster_state.proto](#cluster_state)
- [cluster_stats.proto](#cluster_stats)
- [compression_algorithm.proto](#compression_algorithm)
- [connection_details.proto](#connection_details)
- [consistency_level.proto](#consistency_level)
- [consumer_group.proto](#consumer_group)
- [consumer_state.proto](#consumer_state)
- [consumer_stats.proto](#consumer_stats)
- [dead_letter_policy.proto](#dead_letter_policy)
- [delivery_mode.proto](#delivery_mode)
- [delivery_options.proto](#delivery_options)
- [durability_level.proto](#durability_level)
- [export_format.proto](#export_format)
- [flow_control.proto](#flow_control)
- [flush_policy.proto](#flush_policy)
- [format_options.proto](#format_options)
- [health_status.proto](#health_status)
- [load_balancing_strategy.proto](#load_balancing_strategy)
- [message.proto](#message)
- [message_envelope.proto](#message_envelope)
- [message_id.proto](#message_id) ⚠️ 1 issues
- [message_metadata.proto](#message_metadata)
- [message_state.proto](#message_state)
- [metric_type.proto](#metric_type)
- [nack_error.proto](#nack_error)
- [nack_error_category.proto](#nack_error_category)
- [node_info.proto](#node_info)
- [node_state.proto](#node_state)
- [node_stats.proto](#node_stats)
- [notification_channel.proto](#notification_channel)
- [notification_channel_type.proto](#notification_channel_type)
- [offset_info.proto](#offset_info)
- [offset_type.proto](#offset_type)
- [partition_info.proto](#partition_info)
- [partition_offset.proto](#partition_offset)
- [partition_strategy.proto](#partition_strategy)
- [priority_level.proto](#priority_level)
- [priority_range.proto](#priority_range)
- [publish_result.proto](#publish_result)

## Module Dependencies

**This module depends on**:

- [cache_api_2](./cache_api_2.md)
- [config_1](./config_1.md)
- [database](./database.md)
- [metrics_1](./metrics_1.md)
- [queue_2](./queue_2.md)
- [queue_api_2](./queue_api_2.md)

**Modules that depend on this one**:

- [auth_api_2](./auth_api_2.md)
- [cache](./cache.md)
- [config_api](./config_api.md)
- [config_config_1](./config_config_1.md)
- [database](./database.md)
- [database_api](./database_api.md)
- [health](./health.md)
- [metrics_1](./metrics_1.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_2](./queue_2.md)
- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [queue_config](./queue_config.md)
- [queue_services](./queue_services.md)
- [web_api_2](./web_api_2.md)

---

## Detailed Documentation

### ack_level.proto {#ack_level}

**Path**: `pkg/queue/proto/ack_level.proto` **Package**: `gcommon.v1.queue`
**Lines**: 36

**Enums** (1): `AckLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/ack_level.proto
// file: queue/proto/enums/ack_level.proto
// version: 1.0.0
// guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Acknowledgment level for durability guarantees.
 */
enum AckLevel {
  // Default unspecified level
  ACK_LEVEL_UNSPECIFIED = 0;

  // No acknowledgment required (fire and forget)
  ACK_LEVEL_NONE = 1;

  // Wait for leader acknowledgment only
  ACK_LEVEL_LEADER = 2;

  // Wait for all replicas to acknowledge
  ACK_LEVEL_ALL = 3;

  // Wait for majority of replicas
  ACK_LEVEL_MAJORITY = 4;
}

```

---

### ack_type.proto {#ack_type}

**Path**: `pkg/queue/proto/ack_type.proto` **Package**: `gcommon.v1.queue`
**Lines**: 34

**Enums** (1): `AckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/ack_type.proto
// version: 1.0.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Types of acknowledgments.
 * Defines how a consumed message was processed.
 */
enum AckType {
  // Unspecified acknowledgment type
  ACK_TYPE_UNSPECIFIED = 0;

  // Successful processing acknowledgment
  ACK_TYPE_SUCCESS = 1;

  // Failed processing - retry message
  ACK_TYPE_RETRY = 2;

  // Failed processing - reject message (dead letter)
  ACK_TYPE_REJECT = 3;

  // Processing timeout
  ACK_TYPE_TIMEOUT = 4;
}

```

---

### acknowledgment.proto {#acknowledgment}

**Path**: `pkg/queue/proto/acknowledgment.proto` **Package**: `gcommon.v1.queue`
**Lines**: 51

**Messages** (1): `Acknowledgment`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/ack_type.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/acknowledgment.proto
// version: 1.1.0
// guid: c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/ack_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Message acknowledgment information.
 * Tracks the processing status of consumed messages.
 */
message Acknowledgment {
  // Message ID being acknowledged
  string message_id = 1;

  // Consumer ID that processed the message
  string consumer_id = 2;

  // Queue or topic name
  string queue_name = 3;

  // Partition ID (for partitioned queues)
  int32 partition_id = 4;

  // Message offset within the partition
  int64 offset = 5;

  // Acknowledgment type
  AckType ack_type = 6;

  // Timestamp when message was acknowledged
  google.protobuf.Timestamp ack_timestamp = 7;

  // Processing duration in milliseconds
  int64 processing_duration_ms = 8;

  // Error message if processing failed
  string error_message = 9;

  // Number of retry attempts made
  int32 retry_count = 10;
}

```

---

### acknowledgment_mode.proto {#acknowledgment_mode}

**Path**: `pkg/queue/proto/acknowledgment_mode.proto` **Package**:
`gcommon.v1.queue` **Lines**: 37

**Enums** (1): `AcknowledgmentMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // queue consumer. This was previously left as
  a placeholder during the

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/acknowledgment_mode.proto
// version: 1.0.0
// guid: 6f4b2414-998e-4fc3-bc68-188dff6d2f25

// Enumeration describing how message acknowledgments are handled by a
// queue consumer. This was previously left as a placeholder during the
// 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// AcknowledgmentMode specifies how a message should be acknowledged
// by the consumer. It provides flexibility for different delivery
// guarantees and consumer implementations.
enum AcknowledgmentMode {
  // Default mode. The broker chooses a sensible default based on
  // queue configuration.
  ACKNOWLEDGMENT_MODE_UNSPECIFIED = 0;

  // Messages are automatically acknowledged immediately after
  // successful processing by the consumer.
  ACKNOWLEDGMENT_MODE_AUTO = 1;

  // The consumer is responsible for explicitly sending an AckRequest
  // after processing the message.
  ACKNOWLEDGMENT_MODE_MANUAL = 2;

  // No acknowledgment is required. Messages are considered processed
  // once delivered. Use with care.
  ACKNOWLEDGMENT_MODE_NONE = 3;
}

```

---

### alert_condition.proto {#alert_condition}

**Path**: `pkg/queue/proto/alert_condition.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Enums** (1): `AlertCondition`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/alert_condition.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Condition types for alerts.
 */
enum AlertCondition {
  // Default unspecified condition
  ALERT_CONDITION_UNSPECIFIED = 0;

  // Metric greater than threshold
  ALERT_CONDITION_GREATER_THAN = 1;

  // Metric less than threshold
  ALERT_CONDITION_LESS_THAN = 2;

  // Metric equal to threshold
  ALERT_CONDITION_EQUALS = 3;

  // Metric not equal to threshold
  ALERT_CONDITION_NOT_EQUALS = 4;

  // Metric increasing rapidly
  ALERT_CONDITION_INCREASING = 5;

  // Metric decreasing rapidly
  ALERT_CONDITION_DECREASING = 6;
}

```

---

### alert_rule.proto {#alert_rule}

**Path**: `pkg/queue/proto/alert_rule.proto` **Package**: `gcommon.v1.queue`
**Lines**: 48

**Messages** (1): `AlertRule`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/alert_condition.proto`
- `pkg/queue/proto/alert_severity.proto` →
  [config_1](./config_1.md#alert_severity) →
  [metrics_1](./metrics_1.md#alert_severity)

#### Source Code

```protobuf
// file: pkg/queue/proto/alert_rule.proto
// version: 1.0.0
// guid: 5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/alert_condition.proto";
import "pkg/queue/proto/alert_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * An individual alert rule.
 */
message AlertRule {
  // Unique name for the rule
  string name = 1;

  // Human-readable description
  string description = 2;

  // Metric to monitor
  string metric_name = 3;

  // Condition for triggering the alert
  AlertCondition condition = 4;

  // Threshold value
  double threshold = 5;

  // Duration the condition must persist before alerting
  google.protobuf.Duration duration = 6;

  // Severity of the alert
  AlertSeverity severity = 7;

  // Whether the rule is enabled
  bool enabled = 8;

  // Labels to attach to the alert
  map<string, string> labels = 9;
}

```

---

### alert_severity.proto {#alert_severity}

**Path**: `pkg/queue/proto/alert_severity.proto` **Package**: `gcommon.v1.queue`
**Lines**: 33

**Enums** (1): `AlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/alert_severity.proto
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Alert severity levels.
 */
enum AlertSeverity {
  // Default unspecified severity
  ALERT_SEVERITY_UNSPECIFIED = 0;

  // Informational alert
  ALERT_SEVERITY_INFO = 1;

  // Warning level alert
  ALERT_SEVERITY_WARNING = 2;

  // Error level alert
  ALERT_SEVERITY_ERROR = 3;

  // Critical alert requiring immediate attention
  ALERT_SEVERITY_CRITICAL = 4;
}

```

---

### anti_affinity_rule.proto {#anti_affinity_rule}

**Path**: `pkg/queue/proto/anti_affinity_rule.proto` **Package**:
`gcommon.v1.queue` **Lines**: 31

**Messages** (1): `AntiAffinityRule`

**Imports** (5):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/anti_affinity_scope.proto`
- `pkg/queue/proto/consistency_level.proto` →
  [database](./database.md#consistency_level)
- `pkg/queue/proto/replication_mode.proto` →
  [queue_2](./queue_2.md#replication_mode)

#### Source Code

```protobuf
// file: pkg/queue/proto/anti_affinity_rule.proto
// version: 1.0.0
// guid: a0d26ff8-7127-4e69-b8f3-eec85c695787

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/anti_affinity_scope.proto";
import "pkg/queue/proto/consistency_level.proto";
import "pkg/queue/proto/replication_mode.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Anti-affinity rule for replica placement.
 */
message AntiAffinityRule {
  // Label key to check for anti-affinity
  string label_key = 1;

  // Label values that should not be co-located
  repeated string label_values = 2;

  // Scope of the anti-affinity rule
  AntiAffinityScope scope = 3;
}

```

---

### anti_affinity_scope.proto {#anti_affinity_scope}

**Path**: `pkg/queue/proto/anti_affinity_scope.proto` **Package**:
`gcommon.v1.queue` **Lines**: 36

**Enums** (1): `AntiAffinityScope`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/consistency_level.proto` →
  [database](./database.md#consistency_level)
- `pkg/queue/proto/replication_mode.proto` →
  [queue_2](./queue_2.md#replication_mode)

#### Source Code

```protobuf
// file: pkg/queue/proto/anti_affinity_scope.proto
// version: 1.0.0
// guid: 719f1256-5001-4957-aa05-7b676cc4b90b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/consistency_level.proto";
import "pkg/queue/proto/replication_mode.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Scope for anti-affinity rules.
 */
enum AntiAffinityScope {
  // Default unspecified scope
  ANTI_AFFINITY_SCOPE_UNSPECIFIED = 0;

  // Same node
  ANTI_AFFINITY_SCOPE_NODE = 1;

  // Same rack
  ANTI_AFFINITY_SCOPE_RACK = 2;

  // Same datacenter
  ANTI_AFFINITY_SCOPE_DATACENTER = 3;

  // Same region
  ANTI_AFFINITY_SCOPE_REGION = 4;
}

```

---

### binding_info.proto {#binding_info}

**Path**: `pkg/queue/proto/binding_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 48

**Messages** (1): `BindingInfo`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/binding_info.proto
// file: queue/proto/messages/binding_info.proto
// version: 1.0.0
// guid: 1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Information about queue and topic bindings.
 */
message BindingInfo {
  // Name of the binding
  string binding_name = 1;

  // Source queue or topic name
  string source = 2;

  // Destination queue or topic name
  string destination = 3;

  // Routing key for the binding
  string routing_key = 4;

  // Arguments for the binding (key-value pairs)
  map<string, string> arguments = 5;

  // Whether the binding is durable
  bool durable = 6;

  // Whether to auto-delete when unused
  bool auto_delete = 7;

  // Binding type (direct, topic, fanout, headers)
  string binding_type = 8;

  // Creation timestamp
  uint64 created_at = 9;
}

```

---

### cluster_info.proto {#cluster_info}

**Path**: `pkg/queue/proto/cluster_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 56

**Messages** (1): `ClusterInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/cluster_info.proto
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Cluster information for queue management.
 * Contains metadata about the message queue cluster.
 */
message ClusterInfo {
  // Cluster identifier
  string cluster_id = 1;

  // Cluster name
  string name = 2;

  // Cluster version
  string version = 3;

  // Number of nodes in cluster
  int32 node_count = 4;

  // Number of active brokers
  int32 active_brokers = 5;

  // Cluster status (healthy, degraded, offline)
  string status = 6;

  // Cluster uptime in seconds
  int64 uptime_seconds = 7;

  // Total topics in cluster
  int32 total_topics = 8;

  // Total partitions in cluster
  int32 total_partitions = 9;

  // Cluster leader node
  string leader_node = 10;

  // Cluster metadata
  map<string, string> metadata = 11 [lazy = true];

  // Last health check timestamp
  google.protobuf.Timestamp last_health_check = 12 [lazy = true];
}

```

---

### cluster_state.proto {#cluster_state}

**Path**: `pkg/queue/proto/cluster_state.proto` **Package**: `gcommon.v1.queue`
**Lines**: 37

**Enums** (1): `ClusterState`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/cluster_state.proto
// version: 1.0.0
// guid: f68fdc5e-d25f-4790-9362-9bf09eb27f4d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * State of the cluster.
 */
enum ClusterState {
  // Default unspecified state
  CLUSTER_STATE_UNSPECIFIED = 0;

  // Cluster is healthy and operational
  CLUSTER_STATE_HEALTHY = 1;

  // Cluster is degraded but operational
  CLUSTER_STATE_DEGRADED = 2;

  // Cluster is in recovery mode
  CLUSTER_STATE_RECOVERING = 3;

  // Cluster is down
  CLUSTER_STATE_DOWN = 4;

  // Cluster is in maintenance mode
  CLUSTER_STATE_MAINTENANCE = 5;
}

```

---

### cluster_stats.proto {#cluster_stats}

**Path**: `pkg/queue/proto/cluster_stats.proto` **Package**: `gcommon.v1.queue`
**Lines**: 31

**Messages** (1): `ClusterStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/cluster_stats.proto
// version: 1.0.0
// guid: 6318f554-f8e9-434a-a33f-84ab2582e93c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Statistics for the entire cluster.
 */
message ClusterStats {
  // Total number of queues across all nodes
  int64 total_queues = 1;

  // Total number of messages across all queues
  int64 total_messages = 2;

  // Total throughput (messages per second)
  double total_throughput = 3;

  // Number of active connections
  int64 active_connections = 4;
}

```

---

### compression_algorithm.proto {#compression_algorithm}

**Path**: `pkg/queue/proto/compression_algorithm.proto` **Package**:
`gcommon.v1.queue` **Lines**: 40

**Enums** (1): `CompressionAlgorithm`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/serialization_format.proto` →
  [queue_2](./queue_2.md#serialization_format)

#### Source Code

```protobuf
// file: pkg/queue/proto/compression_algorithm.proto
// version: 1.0.0
// guid: 46070a52-0998-4b61-b36f-05b4861f8f6c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Compression algorithms for serialization.
 */
enum CompressionAlgorithm {
  // Default unspecified algorithm
  COMPRESSION_ALGORITHM_UNSPECIFIED = 0;

  // No compression
  COMPRESSION_ALGORITHM_NONE = 1;

  // GZIP compression
  COMPRESSION_ALGORITHM_GZIP = 2;

  // LZ4 compression
  COMPRESSION_ALGORITHM_LZ4 = 3;

  // Snappy compression
  COMPRESSION_ALGORITHM_SNAPPY = 4;

  // ZSTD compression
  COMPRESSION_ALGORITHM_ZSTD = 5;

  // Brotli compression
  COMPRESSION_ALGORITHM_BROTLI = 6;
}

```

---

### connection_details.proto {#connection_details}

**Path**: `pkg/queue/proto/connection_details.proto` **Package**:
`gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ConnectionDetails`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/connection_details.proto
// version: 1.0.0
// Connection details for queue message delivery

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ConnectionDetails contains information for establishing message delivery connections
message ConnectionDetails {
  // Delivery endpoint (for push mode)
  string delivery_endpoint = 1;

  // Authentication token for delivery
  string auth_token = 2;

  // Heartbeat interval (milliseconds)
  int32 heartbeat_interval_ms = 3;

  // Keep-alive timeout (milliseconds)
  int32 keep_alive_timeout_ms = 4;

  // SSL/TLS configuration
  bool ssl_enabled = 5;

  // Connection metadata
  map<string, string> connection_metadata = 6;
}

```

---

### consistency_level.proto {#consistency_level}

**Path**: `pkg/queue/proto/consistency_level.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Enums** (1): `ConsistencyLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/consistency_level.proto
// file: queue/proto/enums/consistency_level.proto
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Consistency level for queue operations.
 */
enum ConsistencyLevel {
  // Default unspecified consistency level
  CONSISTENCY_LEVEL_UNSPECIFIED = 0;

  // Eventual consistency (fastest, may read stale data)
  CONSISTENCY_LEVEL_EVENTUAL = 1;

  // Weak consistency (balance between speed and consistency)
  CONSISTENCY_LEVEL_WEAK = 2;

  // Strong consistency (slower, guarantees latest data)
  CONSISTENCY_LEVEL_STRONG = 3;

  // Sequential consistency (operations appear in some sequential order)
  CONSISTENCY_LEVEL_SEQUENTIAL = 4;

  // Linearizable consistency (strongest, operations appear instantaneous)
  CONSISTENCY_LEVEL_LINEARIZABLE = 5;
}

```

---

### consumer_group.proto {#consumer_group}

**Path**: `pkg/queue/proto/consumer_group.proto` **Package**: `gcommon.v1.queue`
**Lines**: 325

**Messages** (12): `ConsumerGroup`, `ConsumerGroupConfig`, `AutoCommitConfig`,
`RetryDelayConfig`, `Consumer`, `ConsumerClient`, `ConsumerConfig`,
`PartitionAssignment`, `GroupCoordinator`, `ConsumerGroupStats`,
`RebalanceStats`, `ConsumerErrorStats`

**Enums** (4): `RebalanceStrategy`, `OffsetResetStrategy`, `ConsumerGroupState`,
`CoordinatorState`

**Imports** (6):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/consumer_state.proto`
- `pkg/queue/proto/consumer_stats.proto`
- `pkg/queue/proto/load_balancing_strategy.proto`
- `pkg/queue/proto/subscribe_request.proto` →
  [cache_api_2](./cache_api_2.md#subscribe_request) →
  [queue_api_2](./queue_api_2.md#subscribe_request)

#### Source Code

```protobuf
// file: pkg/queue/proto/consumer_group.proto
// version: 1.1.0
// Consumer group management for queue message consumption

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/consumer_state.proto";
import "pkg/queue/proto/consumer_stats.proto";
import "pkg/queue/proto/load_balancing_strategy.proto";
import "pkg/queue/proto/subscribe_request.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ConsumerGroup represents a group of consumers that coordinate message consumption
message ConsumerGroup {
  // Unique identifier for the consumer group
  string group_id = 1;

  // Group name (human-readable)
  string group_name = 2;

  // Topic or queue this group is consuming from
  string topic = 3;

  // Consumer group configuration
  ConsumerGroupConfig config = 4;

  // Current group state
  ConsumerGroupState state = 5;

  // List of active consumers in the group
  repeated Consumer consumers = 6;

  // Partition assignments
  repeated PartitionAssignment partition_assignments = 7;

  // Group coordinator information
  GroupCoordinator coordinator = 8;

  // Consumer group statistics
  ConsumerGroupStats stats = 9;

  // Group metadata
  map<string, string> metadata = 10;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 11;

  // Last updated timestamp
  google.protobuf.Timestamp updated_at = 12;
}

// Consumer group configuration
message ConsumerGroupConfig {
  // Load balancing strategy for partition assignment
  LoadBalancingStrategy load_balancing_strategy = 1;

  // Rebalance strategy when consumers join/leave
  RebalanceStrategy rebalance_strategy = 2;

  // Session timeout for consumer heartbeats (milliseconds)
  int32 session_timeout_ms = 3;

  // Heartbeat interval (milliseconds)
  int32 heartbeat_interval_ms = 4;

  // Maximum poll interval (milliseconds)
  int32 max_poll_interval_ms = 5;

  // Auto-commit configuration
  AutoCommitConfig auto_commit = 6;

  // Offset reset strategy for new consumers
  OffsetResetStrategy offset_reset_strategy = 7;

  // Maximum number of consumers allowed in the group
  int32 max_consumers = 8;

  // Enable exactly-once semantics
  bool exactly_once_enabled = 9;

  // Dead letter queue configuration
  DeadLetterQueueConfig dlq_config = 10;
}

// Rebalance strategy for consumer group changes
enum RebalanceStrategy {
  REBALANCE_STRATEGY_UNSPECIFIED = 0;
  REBALANCE_STRATEGY_EAGER = 1; // Stop all consumers, then reassign
  REBALANCE_STRATEGY_COOPERATIVE = 2; // Incremental cooperative rebalancing
  REBALANCE_STRATEGY_STATIC = 3; // Static assignment (no rebalancing)
}

// Auto-commit configuration
message AutoCommitConfig {
  // Enable auto-commit of offsets
  bool enabled = 1;

  // Auto-commit interval (milliseconds)
  int32 interval_ms = 2;

  // Commit on message processing completion
  bool commit_on_completion = 3;

  // Batch size for auto-commit
  int32 batch_size = 4;
}

// Offset reset strategy for new consumers
enum OffsetResetStrategy {
  OFFSET_RESET_STRATEGY_UNSPECIFIED = 0;
  OFFSET_RESET_STRATEGY_EARLIEST = 1; // Start from earliest available offset
  OFFSET_RESET_STRATEGY_LATEST = 2; // Start from latest offset
  OFFSET_RESET_STRATEGY_NONE = 3; // Fail if no committed offset
  OFFSET_RESET_STRATEGY_TIMESTAMP = 4; // Start from specific timestamp
}

// Retry delay configuration
message RetryDelayConfig {
  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 1;

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 2;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 3;

  // Enable jitter for retry delays
  bool jitter_enabled = 4;
}

// Consumer group state
enum ConsumerGroupState {
  CONSUMER_GROUP_STATE_UNSPECIFIED = 0;
  CONSUMER_GROUP_STATE_STABLE = 1; // Group is stable with assigned partitions
  CONSUMER_GROUP_STATE_PREPARING_REBALANCE = 2; // Preparing for rebalance
  CONSUMER_GROUP_STATE_COMPLETING_REBALANCE = 3; // Completing rebalance operation
  CONSUMER_GROUP_STATE_DEAD = 4; // Group has no active consumers
  CONSUMER_GROUP_STATE_EMPTY = 5; // Group exists but no consumers
}

// Individual consumer in the group
message Consumer {
  // Unique consumer identifier
  string consumer_id = 1;

  // Consumer client information
  ConsumerClient client_info = 2;

  // Consumer state
  ConsumerState state = 3;

  // Assigned partitions
  repeated int32 assigned_partitions = 4;

  // Consumer configuration
  ConsumerConfig config = 5;

  // Consumer statistics
  ConsumerStats stats = 6;

  // Last heartbeat timestamp
  google.protobuf.Timestamp last_heartbeat = 7;

  // Join timestamp
  google.protobuf.Timestamp joined_at = 8;
}

// Consumer client information
message ConsumerClient {
  // Client ID
  string client_id = 1;

  // Client host/IP address
  string client_host = 2;

  // Client application name
  string client_app = 3;

  // Client version
  string client_version = 4;

  // Client rack (for rack-aware assignment)
  string client_rack = 5;
}

// Individual consumer configuration
message ConsumerConfig {
  // Consumer timeout (milliseconds)
  int32 timeout_ms = 1;

  // Maximum messages to poll at once
  int32 max_poll_records = 2;

  // Fetch minimum bytes
  int32 fetch_min_bytes = 3;

  // Fetch maximum wait time (milliseconds)
  int32 fetch_max_wait_ms = 4;

  // Enable auto-offset reset
  bool auto_offset_reset = 5;

  // Consumer priority (for priority-based assignment)
  int32 priority = 6;
}

// Consumer statistics

// Partition assignment for the group
message PartitionAssignment {
  // Partition ID
  int32 partition_id = 1;

  // Assigned consumer ID
  string consumer_id = 2;

  // Current offset position
  int64 current_offset = 3;

  // Committed offset
  int64 committed_offset = 4;

  // High water mark (latest available offset)
  int64 high_water_mark = 5;

  // Assignment timestamp
  google.protobuf.Timestamp assigned_at = 6;

  // Last commit timestamp
  google.protobuf.Timestamp last_commit = 7;
}

// Group coordinator information
message GroupCoordinator {
  // Coordinator node ID
  string node_id = 1;

  // Coordinator host
  string host = 2;

  // Coordinator port
  int32 port = 3;

  // Coordinator state
  CoordinatorState state = 4;

  // Leadership epoch
  int64 epoch = 5;
}

// Coordinator state
enum CoordinatorState {
  COORDINATOR_STATE_UNSPECIFIED = 0;
  COORDINATOR_STATE_ACTIVE = 1; // Coordinator is active
  COORDINATOR_STATE_LOADING = 2; // Coordinator is loading metadata
  COORDINATOR_STATE_NOT_COORDINATOR = 3; // Node is not the coordinator
}

// Consumer group statistics
message ConsumerGroupStats {
  // Total number of active consumers
  int32 active_consumers = 1;

  // Total number of assigned partitions
  int32 assigned_partitions = 2;

  // Total messages consumed by the group
  int64 total_messages_consumed = 3;

  // Total bytes consumed by the group
  int64 total_bytes_consumed = 4;

  // Average group consumption rate (messages/second)
  double group_consumption_rate = 5;

  // Total group lag
  int64 total_lag = 6;

  // Rebalance statistics
  RebalanceStats rebalance_stats = 7;

  // Error statistics for the consumer group
  ConsumerErrorStats error_stats = 8;
}

// Rebalance statistics
message RebalanceStats {
  // Total number of rebalances
  int64 total_rebalances = 1;

  // Last rebalance timestamp
  google.protobuf.Timestamp last_rebalance = 2;

  // Average rebalance duration (milliseconds)
  int64 avg_rebalance_duration_ms = 3;

  // Failed rebalances
  int64 failed_rebalances = 4;
}

// Consumer group error statistics
message ConsumerErrorStats {
  // Total processing errors
  int64 total_errors = 1;

  // Connection errors
  int64 connection_errors = 2;

  // Timeout errors
  int64 timeout_errors = 3;

  // Serialization errors
  int64 serialization_errors = 4;

  // Last error timestamp
  google.protobuf.Timestamp last_error = 5;
}

```

---

### consumer_state.proto {#consumer_state}

**Path**: `pkg/queue/proto/consumer_state.proto` **Package**: `gcommon.v1.queue`
**Lines**: 45

**Enums** (1): `ConsumerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/consumer_state.proto
// file: queue/proto/enums/consumer_state.proto
// version: 1.0.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * State of a queue consumer.
 */
enum ConsumerState {
  // Default unspecified state
  CONSUMER_STATE_UNSPECIFIED = 0;

  // Consumer is active and processing messages
  CONSUMER_STATE_ACTIVE = 1;

  // Consumer is idle (connected but not processing)
  CONSUMER_STATE_IDLE = 2;

  // Consumer is paused
  CONSUMER_STATE_PAUSED = 3;

  // Consumer is stopped
  CONSUMER_STATE_STOPPED = 4;

  // Consumer has encountered an error
  CONSUMER_STATE_ERROR = 5;

  // Consumer is connecting
  CONSUMER_STATE_CONNECTING = 6;

  // Consumer is disconnected
  CONSUMER_STATE_DISCONNECTED = 7;
}

```

---

### consumer_stats.proto {#consumer_stats}

**Path**: `pkg/queue/proto/consumer_stats.proto` **Package**: `gcommon.v1.queue`
**Lines**: 30

**Messages** (1): `ConsumerStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/consumer_stats.proto
// version: 1.0.0
// guid: f4a5b6c7-890d-234e-5678-890123456789

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ConsumerStats {
  // Consumer ID
  string consumer_id = 1;

  // Messages processed
  int64 messages_processed = 2;

  // Processing rate per second
  double processing_rate = 3;

  // Error count
  int64 error_count = 4;

  // Last active timestamp
  int64 last_active = 5;
}

```

---

### dead_letter_policy.proto {#dead_letter_policy}

**Path**: `pkg/queue/proto/dead_letter_policy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 42

**Messages** (1): `DeadLetterPolicy`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/dead_letter_policy.proto
// file: queue/proto/messages/dead_letter_policy.proto
// version: 1.0.0
// guid: 5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Dead letter policy configuration for handling failed messages.
 * Messages that exceed retry limits or cannot be processed will be
 * sent to a dead letter queue for manual inspection.
 */
message DeadLetterPolicy {
  // Name of the dead letter queue where failed messages will be sent
  string dead_letter_queue = 1;

  // Maximum number of delivery attempts before sending to dead letter queue
  int32 max_delivery_attempts = 2;

  // Maximum age of a message before it's considered expired and sent to DLQ
  google.protobuf.Duration max_message_age = 3;

  // Whether to include the original failure reason in the dead letter message
  bool include_failure_reason = 4;

  // Additional metadata to attach to dead letter messages
  map<string, string> dead_letter_metadata = 5;

  // Whether dead letter policy is enabled
  bool enabled = 6;
}

```

---

### delivery_mode.proto {#delivery_mode}

**Path**: `pkg/queue/proto/delivery_mode.proto` **Package**: `gcommon.v1.queue`
**Lines**: 36

**Enums** (1): `DeliveryMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/delivery_mode.proto
// file: queue/proto/enums/delivery_mode.proto
// version: 1.0.0
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Message delivery mode for queue operations.
 */
enum DeliveryMode {
  // Default unspecified delivery mode
  DELIVERY_MODE_UNSPECIFIED = 0;

  // At most once delivery (may lose messages, no duplicates)
  DELIVERY_MODE_AT_MOST_ONCE = 1;

  // At least once delivery (no message loss, may have duplicates)
  DELIVERY_MODE_AT_LEAST_ONCE = 2;

  // Exactly once delivery (no loss, no duplicates - when supported)
  DELIVERY_MODE_EXACTLY_ONCE = 3;

  // Best effort delivery (no guarantees)
  DELIVERY_MODE_BEST_EFFORT = 4;
}

```

---

### delivery_options.proto {#delivery_options}

**Path**: `pkg/queue/proto/delivery_options.proto` **Package**:
`gcommon.v1.queue` **Lines**: 41

**Messages** (1): `DeliveryOptions`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: queue/proto/messages/delivery_options.proto
// version: 1.0.0
// guid: 226d4794-23ca-4b54-9a0d-7c6671093c04

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// DeliveryOptions control message routing and retries.
message DeliveryOptions {
  // Optional delivery delay.
  google.protobuf.Duration delay = 1;

  // Maximum retry attempts before sending to dead letter queue.
  int32 max_retries = 2;

  // Delay between retry attempts.
  google.protobuf.Duration retry_delay = 3;

  // Multiplier for exponential backoff.
  double backoff_multiplier = 4;

  // Maximum delay allowed between retries.
  google.protobuf.Duration max_retry_delay = 5;

  // Name of the dead letter queue.
  string dead_letter_queue = 6;

  // Whether acknowledgment is required for delivery.
  bool require_ack = 7;

  // Timeout waiting for acknowledgment.
  google.protobuf.Duration ack_timeout = 8;
}

```

---

### durability_level.proto {#durability_level}

**Path**: `pkg/queue/proto/durability_level.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Enums** (1): `DurabilityLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/durability_level.proto
// file: queue/proto/enums/durability_level.proto
// version: 1.0.0
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Durability levels for message persistence guarantees.
 */
enum DurabilityLevel {
  // Default unspecified level
  DURABILITY_LEVEL_UNSPECIFIED = 0;

  // No durability - messages may be lost on restart
  DURABILITY_LEVEL_NONE = 1;

  // Memory-only persistence with periodic snapshots
  DURABILITY_LEVEL_MEMORY = 2;

  // Synchronous disk persistence for each message
  DURABILITY_LEVEL_DISK_SYNC = 3;

  // Asynchronous disk persistence with batching
  DURABILITY_LEVEL_DISK_ASYNC = 4;

  // Replicated across multiple nodes with disk persistence
  DURABILITY_LEVEL_REPLICATED = 5;
}

```

---

### export_format.proto {#export_format}

**Path**: `pkg/queue/proto/export_format.proto` **Package**: `gcommon.v1.queue`
**Lines**: 36

**Enums** (1): `ExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/export_format.proto
// file: queue/proto/enums/export_format.proto
// version: 1.0.0
// guid: 3a2b1c0d-9e8f-7a6b-5c4d-3e2f1a0b9c8d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Export format options.
 */
enum ExportFormat {
  // Default unspecified format
  EXPORT_FORMAT_UNSPECIFIED = 0;

  // JSON format
  EXPORT_FORMAT_JSON = 1;

  // Protocol Buffers binary format
  EXPORT_FORMAT_PROTOBUF = 2;

  // CSV format (metadata only)
  EXPORT_FORMAT_CSV = 3;

  // Custom format
  EXPORT_FORMAT_CUSTOM = 4;
}

```

---

### flow_control.proto {#flow_control}

**Path**: `pkg/queue/proto/flow_control.proto` **Package**: `gcommon.v1.queue`
**Lines**: 27

**Messages** (1): `FlowControl`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/flow_control.proto
// version: 1.0.0
// guid: 40b0fde3-4f0f-4bef-b893-248588fbf4a6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// FlowControl settings influence how the queue handles
// bursts of incoming messages.
message FlowControl {
  // Maximum number of unacknowledged messages allowed.
  int32 max_in_flight = 1;

  // Maximum amount of data in flight (bytes).
  int64 max_bytes_in_flight = 2;

  // Deadline before a message is redelivered if not acknowledged.
  google.protobuf.Duration ack_deadline = 3;
}

```

---

### flush_policy.proto {#flush_policy}

**Path**: `pkg/queue/proto/flush_policy.proto` **Package**: `gcommon.v1.queue`
**Lines**: 39

**Enums** (1): `FlushPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/flush_policy.proto
// file: queue/proto/enums/flush_policy.proto
// version: 1.0.0
// guid: 0a9b8c7d-6e5f-4a3b-2c1d-0e9f8a7b6c5d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Policy for when to flush messages to persistent storage.
 */
enum FlushPolicy {
  // Default unspecified policy
  FLUSH_POLICY_UNSPECIFIED = 0;

  // Flush immediately after each message
  FLUSH_POLICY_IMMEDIATE = 1;

  // Flush after a certain number of messages
  FLUSH_POLICY_BATCH = 2;

  // Flush after a time interval
  FLUSH_POLICY_TIMED = 3;

  // Flush when buffer is full
  FLUSH_POLICY_BUFFER_FULL = 4;

  // Manual flush only
  FLUSH_POLICY_MANUAL = 5;
}

```

---

### format_options.proto {#format_options}

**Path**: `pkg/queue/proto/format_options.proto` **Package**: `gcommon.v1.queue`
**Lines**: 35

**Messages** (1): `FormatOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/compression_algorithm.proto`
- `pkg/queue/proto/serialization_format.proto` →
  [queue_2](./queue_2.md#serialization_format)

#### Source Code

```protobuf
// file: pkg/queue/proto/format_options.proto
// version: 1.0.0
// guid: be0dbb05-7495-4e4c-b7c7-97774a7e0489

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/compression_algorithm.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Serialization options for a specific format.
 */
message FormatOptions {
  // Serialization format
  gcommon.v1.queue.SerializationFormat format = 1;

  // Format-specific configuration
  map<string, string> options = 2;

  // Whether to enable compression for this format
  bool enable_compression = 3;

  // Compression algorithm
  CompressionAlgorithm compression_algorithm = 4;

  // Maximum message size for this format
  int64 max_message_size = 5;
}

```

---

### health_status.proto {#health_status}

**Path**: `pkg/queue/proto/health_status.proto` **Package**: `gcommon.v1.queue`
**Lines**: 31

**Enums** (1): `HealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/health_status.proto
// version: 1.0.0
// guid: c5459257-5e52-46bb-a6f6-fb2b6a1e315d
//
// HealthStatus enumeration for the queue module
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * HealthStatus represents queue service availability.
 */
enum HealthStatus {
  // Unspecified status.
  HEALTH_STATUS_UNSPECIFIED = 0;

  // Queue service operating normally.
  HEALTH_STATUS_HEALTHY = 1;

  // Queue service experiencing issues.
  HEALTH_STATUS_DEGRADED = 2;

  // Queue service unavailable.
  HEALTH_STATUS_UNAVAILABLE = 3;
}

```

---

### load_balancing_strategy.proto {#load_balancing_strategy}

**Path**: `pkg/queue/proto/load_balancing_strategy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Enums** (1): `LoadBalancingStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/load_balancing_strategy.proto
// version: 1.0.0
// guid: 0d1e2f3a-4b5c-6d7e-8f9a-0b1c2d3e4f5a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Load balancing strategies.
 */
enum LoadBalancingStrategy {
  // Default unspecified strategy
  LOAD_BALANCING_STRATEGY_UNSPECIFIED = 0;

  // Round-robin distribution
  LOAD_BALANCING_STRATEGY_ROUND_ROBIN = 1;

  // Weighted round-robin
  LOAD_BALANCING_STRATEGY_WEIGHTED_ROUND_ROBIN = 2;

  // Least connections
  LOAD_BALANCING_STRATEGY_LEAST_CONNECTIONS = 3;

  // Random distribution
  LOAD_BALANCING_STRATEGY_RANDOM = 4;

  // Hash-based distribution
  LOAD_BALANCING_STRATEGY_HASH = 5;

  // Priority-based distribution
  LOAD_BALANCING_STRATEGY_PRIORITY = 6;
}

```

---

### message.proto {#message}

**Path**: `pkg/queue/proto/message.proto` **Package**: `gcommon.v1.queue`
**Lines**: 19

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/message.proto
// file: queue/proto/messages/message.proto
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// This file provides imports for queue message types
// ReceivedMessage is defined in received_message.proto to avoid conflicts

```

---

### message_envelope.proto {#message_envelope}

**Path**: `pkg/queue/proto/message_envelope.proto` **Package**:
`gcommon.v1.queue` **Lines**: 66

**Messages** (1): `MessageEnvelope`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/message_envelope.proto
// file: queue/proto/messages/message_envelope.proto
// version: 1.0.0
// guid: 2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Message envelope that wraps the actual message payload with metadata.
 * This is the container that gets stored and transmitted through the queue system.
 */
message MessageEnvelope {
  // Unique identifier for this message
  string message_id = 1;

  // The actual message payload
  google.protobuf.Any payload = 2;

  // Message headers for routing and metadata
  map<string, string> headers = 3;

  // Priority of the message (higher numbers = higher priority)
  int32 priority = 4;

  // Timestamp when the message was created
  google.protobuf.Timestamp created_at = 5;

  // Timestamp when the message should be processed (for delayed messages)
  google.protobuf.Timestamp process_at = 6;

  // Timestamp when the message expires
  google.protobuf.Timestamp expires_at = 7;

  // Number of delivery attempts for this message
  int32 delivery_count = 8;

  // Correlation ID for linking related messages
  string correlation_id = 9;

  // Reply-to queue for response messages
  string reply_to = 10;

  // Content type of the payload
  string content_type = 11;

  // Encoding of the payload (e.g., "gzip", "none")
  string content_encoding = 12;

  // Whether this message requires acknowledgment
  bool requires_ack = 13;

  // Trace context for distributed tracing
  map<string, string> trace_context = 14;
}

```

---

### message_id.proto {#message_id}

**Path**: `pkg/queue/proto/message_id.proto` **Package**: `gcommon.v1.queue`
**Lines**: 23

**Messages** (1): `MessageId`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 7: Implementation needed - // placeholder created during the migration.

#### Source Code

```protobuf
// file: pkg/queue/proto/types/message_id.proto
// version: 1.0.0
// guid: 9bd8b62d-3655-4ff5-9f3a-4d5da241dc77

// MessageId is a simple wrapper type used for referencing messages
// in a type-safe manner across the Queue API. This replaces the
// placeholder created during the migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// MessageId uniquely identifies a message within a queue.
// It can be referenced by other messages or API calls.
message MessageId {
  // Opaque identifier assigned by the queue implementation.
  string value = 1;
}

```

---

### message_metadata.proto {#message_metadata}

**Path**: `pkg/queue/proto/message_metadata.proto` **Package**:
`gcommon.v1.queue` **Lines**: 55

**Messages** (1): `MessageMetadata`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/message_metadata.proto
// file: queue/proto/messages/message_metadata.proto
// version: 1.0.0
// guid: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Metadata associated with a queue message.
 */
message MessageMetadata {
  // Unique message identifier
  string message_id = 1;

  // Message timestamp
  google.protobuf.Timestamp timestamp = 2;

  // Producer/sender identifier
  string producer_id = 3;

  // Content type of the message
  string content_type = 4;

  // Content encoding (gzip, deflate, etc.)
  string content_encoding = 5;

  // Message priority (0-255, higher is more priority)
  uint32 priority = 6;

  // Time-to-live in milliseconds
  uint64 ttl_ms = 7;

  // Custom headers
  map<string, string> headers = 8;

  // Routing key
  string routing_key = 9;

  // Correlation ID for request-response patterns
  string correlation_id = 10;

  // Reply-to address
  string reply_to = 11;
}

```

---

### message_state.proto {#message_state}

**Path**: `pkg/queue/proto/message_state.proto` **Package**: `gcommon.v1.queue`
**Lines**: 37

**Enums** (1): `MessageState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: queue/proto/enums/message_state.proto
// version: 1.0.0
// guid: 4eba7921-816c-420b-8880-172c0631fa22

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// MessageState represents the lifecycle state of a queue message.
enum MessageState {
  // Default unspecified state.
  MESSAGE_STATE_UNSPECIFIED = 0;

  // Message is queued and awaiting delivery.
  MESSAGE_STATE_PENDING = 1;

  // Message has been delivered to a consumer.
  MESSAGE_STATE_DELIVERED = 2;

  // Consumer acknowledged successful processing.
  MESSAGE_STATE_ACKNOWLEDGED = 3;

  // Delivery failed and will be retried.
  MESSAGE_STATE_FAILED = 4;

  // Message moved to dead letter queue.
  MESSAGE_STATE_DEAD_LETTER = 5;

  // Message expired before processing.
  MESSAGE_STATE_EXPIRED = 6;
}

```

---

### metric_type.proto {#metric_type}

**Path**: `pkg/queue/proto/metric_type.proto` **Package**: `gcommon.v1.queue`
**Lines**: 40

**Enums** (1): `MetricType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/metric_type.proto
// version: 1.0.0
// guid: 8b7a6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * MetricType represents the types of metrics that can be monitored.
 * Specifies different types of queue metrics for monitoring and analysis.
 */
enum MetricType {
  // Default unspecified type
  METRIC_TYPE_UNSPECIFIED = 0;

  // Message count
  METRIC_TYPE_MESSAGE_COUNT = 1;

  // Message rate (per second)
  METRIC_TYPE_MESSAGE_RATE = 2;

  // Processing time
  METRIC_TYPE_PROCESSING_TIME = 3;

  // Error rate
  METRIC_TYPE_ERROR_RATE = 4;

  // Consumer count
  METRIC_TYPE_CONSUMER_COUNT = 5;

  // Queue depth
  METRIC_TYPE_QUEUE_DEPTH = 6;
}

```

---

### nack_error.proto {#nack_error}

**Path**: `pkg/queue/proto/nack_error.proto` **Package**: `gcommon.v1.queue`
**Lines**: 34

**Messages** (1): `NackError`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/nack_error_category.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/nack_error.proto
// version: 1.0.0
// guid: 9c0d1e2f-3a4b-5c6d-7e8f-9a0b1c2d3e4f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/nack_error_category.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Error information for NACK operations.
 */
message NackError {
  // Error code
  string code = 1;

  // Error message
  string message = 2;

  // Error category
  NackErrorCategory category = 3;

  // Whether the error is retryable
  bool retryable = 4;

  // Stack trace or additional details
  string details = 5;
}

```

---

### nack_error_category.proto {#nack_error_category}

**Path**: `pkg/queue/proto/nack_error_category.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Enums** (1): `NackErrorCategory`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/nack_error_category.proto
// version: 1.0.0
// guid: 8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Categories of NACK errors.
 */
enum NackErrorCategory {
  // Default unspecified category
  NACK_ERROR_CATEGORY_UNSPECIFIED = 0;

  // Temporary/transient error
  NACK_ERROR_CATEGORY_TEMPORARY = 1;

  // Permanent error (should not retry)
  NACK_ERROR_CATEGORY_PERMANENT = 2;

  // Configuration error
  NACK_ERROR_CATEGORY_CONFIGURATION = 3;

  // Network error
  NACK_ERROR_CATEGORY_NETWORK = 4;

  // Authentication/authorization error
  NACK_ERROR_CATEGORY_AUTH = 5;

  // Rate limiting error
  NACK_ERROR_CATEGORY_RATE_LIMIT = 6;
}

```

---

### node_info.proto {#node_info}

**Path**: `pkg/queue/proto/node_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 42

**Messages** (1): `NodeInfo`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/node_state.proto`
- `pkg/queue/proto/node_stats.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/node_info.proto
// version: 1.0.0
// guid: d73ea780-8ed0-4b73-8aae-ab5c4fc1a48f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/node_state.proto";
import "pkg/queue/proto/node_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Information about a single node in the cluster.
 */
message NodeInfo {
  // Unique identifier for the node
  string node_id = 1;

  // Hostname or address of the node
  string hostname = 2;

  // Port number for the node
  int32 port = 3;

  // Current state of the node
  NodeState state = 4;

  // Node roles (leader, follower, etc.)
  repeated string roles = 5;

  // Timestamp when node was last seen
  google.protobuf.Timestamp last_heartbeat = 6;

  // Node-specific statistics
  NodeStats stats = 7;
}

```

---

### node_state.proto {#node_state}

**Path**: `pkg/queue/proto/node_state.proto` **Package**: `gcommon.v1.queue`
**Lines**: 37

**Enums** (1): `NodeState`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/node_state.proto
// version: 1.0.0
// guid: 9ee731f7-a1ea-4298-8579-c001d3b09060

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * State of a cluster node.
 */
enum NodeState {
  // Default unspecified state
  NODE_STATE_UNSPECIFIED = 0;

  // Node is active and healthy
  NODE_STATE_ACTIVE = 1;

  // Node is inactive but reachable
  NODE_STATE_INACTIVE = 2;

  // Node is unreachable
  NODE_STATE_UNREACHABLE = 3;

  // Node is joining the cluster
  NODE_STATE_JOINING = 4;

  // Node is leaving the cluster
  NODE_STATE_LEAVING = 5;
}

```

---

### node_stats.proto {#node_stats}

**Path**: `pkg/queue/proto/node_stats.proto` **Package**: `gcommon.v1.queue`
**Lines**: 37

**Messages** (1): `NodeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/node_stats.proto
// version: 1.0.0
// guid: f64f009b-e23d-4540-9785-817fe7acb9f3

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Statistics for a single node.
 */
message NodeStats {
  // Number of queues hosted on this node
  int32 queue_count = 1;

  // Number of messages on this node
  int64 message_count = 2;

  // CPU usage percentage
  double cpu_usage = 3;

  // Memory usage in bytes
  int64 memory_usage = 4;

  // Disk usage in bytes
  int64 disk_usage = 5;

  // Network throughput in bytes per second
  double network_throughput = 6;
}

```

---

### notification_channel.proto {#notification_channel}

**Path**: `pkg/queue/proto/notification_channel.proto` **Package**:
`gcommon.v1.queue` **Lines**: 35

**Messages** (1): `NotificationChannel`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/alert_severity.proto` →
  [config_1](./config_1.md#alert_severity) →
  [metrics_1](./metrics_1.md#alert_severity)
- `pkg/queue/proto/notification_channel_type.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/notification_channel.proto
// version: 1.0.0
// guid: 6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/alert_severity.proto";
import "pkg/queue/proto/notification_channel_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Notification channel for sending alerts.
 */
message NotificationChannel {
  // Unique identifier for the channel
  string id = 1;

  // Type of notification channel
  NotificationChannelType type = 2;

  // Configuration specific to the channel type
  map<string, string> config = 3;

  // Whether the channel is enabled
  bool enabled = 4;

  // Minimum severity level for notifications
  AlertSeverity min_severity = 5;
}

```

---

### notification_channel_type.proto {#notification_channel_type}

**Path**: `pkg/queue/proto/notification_channel_type.proto` **Package**:
`gcommon.v1.queue` **Lines**: 36

**Enums** (1): `NotificationChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/notification_channel_type.proto
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Types of notification channels.
 */
enum NotificationChannelType {
  // Default unspecified type
  NOTIFICATION_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email notifications
  NOTIFICATION_CHANNEL_TYPE_EMAIL = 1;

  // Slack notifications
  NOTIFICATION_CHANNEL_TYPE_SLACK = 2;

  // SMS notifications
  NOTIFICATION_CHANNEL_TYPE_SMS = 3;

  // Webhook notifications
  NOTIFICATION_CHANNEL_TYPE_WEBHOOK = 4;

  // PagerDuty integration
  NOTIFICATION_CHANNEL_TYPE_PAGERDUTY = 5;
}

```

---

### offset_info.proto {#offset_info}

**Path**: `pkg/queue/proto/offset_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 43

**Messages** (1): `OffsetInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/offset_info.proto
// file: queue/proto/messages/offset_info.proto
// version: 1.0.0
// guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Information about message offset position in a queue.
 */
message OffsetInfo {
  // The offset value
  uint64 offset = 1;

  // Partition this offset belongs to
  uint32 partition_id = 2;

  // Timestamp of the message at this offset
  google.protobuf.Timestamp timestamp = 3;

  // Size of the message at this offset
  uint64 message_size = 4;

  // Whether this offset is valid/available
  bool is_valid = 5;

  // Consumer group that owns this offset
  string consumer_group = 6;

  // Last committed offset for this consumer
  uint64 committed_offset = 7;
}

```

---

### offset_type.proto {#offset_type}

**Path**: `pkg/queue/proto/offset_type.proto` **Package**: `gcommon.v1.queue`
**Lines**: 34

**Enums** (1): `OffsetType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/offset_type.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Types of offsets that can be retrieved.
 * Defines different offset positions in a queue or partition.
 */
enum OffsetType {
  // Unspecified offset type
  OFFSET_TYPE_UNSPECIFIED = 0;

  // Earliest available offset
  OFFSET_TYPE_EARLIEST = 1;

  // Latest available offset
  OFFSET_TYPE_LATEST = 2;

  // Current consumer offset
  OFFSET_TYPE_CURRENT = 3;

  // Committed offset for consumer group
  OFFSET_TYPE_COMMITTED = 4;
}

```

---

### partition_info.proto {#partition_info}

**Path**: `pkg/queue/proto/partition_info.proto` **Package**: `gcommon.v1.queue`
**Lines**: 45

**Messages** (1): `PartitionInfo`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/partition_info.proto
// file: queue/proto/messages/partition_info.proto
// version: 1.0.0
// guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Information about a queue partition.
 */
message PartitionInfo {
  // Partition identifier
  uint32 partition_id = 1;

  // Leader node for this partition
  string leader_node = 2;

  // Replica nodes for this partition
  repeated string replica_nodes = 3;

  // Current offset (latest message)
  uint64 current_offset = 4;

  // Earliest available offset
  uint64 earliest_offset = 5;

  // Number of messages in partition
  uint64 message_count = 6;

  // Partition size in bytes
  uint64 size_bytes = 7;

  // Whether partition is online
  bool is_online = 8;
}

```

---

### partition_offset.proto {#partition_offset}

**Path**: `pkg/queue/proto/partition_offset.proto` **Package**:
`gcommon.v1.queue` **Lines**: 29

**Messages** (1): `PartitionOffset`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/partition_offset.proto
// version: 1.0.0
// Partition offset information for queue operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// PartitionOffset represents the offset position within a partition
message PartitionOffset {
  // Partition ID
  int32 partition_id = 1;

  // Starting offset value
  int64 offset = 2;

  // Offset timestamp
  google.protobuf.Timestamp offset_timestamp = 3;

  // High water mark for this partition
  int64 high_water_mark = 4;
}

```

---

### partition_strategy.proto {#partition_strategy}

**Path**: `pkg/queue/proto/partition_strategy.proto` **Package**:
`gcommon.v1.queue` **Lines**: 40

**Enums** (1): `PartitionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/partition_strategy.proto
// version: 1.0.0
// guid: f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Partitioning strategies for queue messages.
 * Determines how messages are distributed across partitions.
 */
enum PartitionStrategy {
  // Default partitioning strategy
  PARTITION_STRATEGY_UNSPECIFIED = 0;

  // Round-robin distribution across partitions
  PARTITION_STRATEGY_ROUND_ROBIN = 1;

  // Hash-based partitioning using message key
  PARTITION_STRATEGY_HASH = 2;

  // Random partition assignment
  PARTITION_STRATEGY_RANDOM = 3;

  // Manual partition specification
  PARTITION_STRATEGY_MANUAL = 4;

  // Sticky partitioning (same producer uses same partition)
  PARTITION_STRATEGY_STICKY = 5;

  // Load-based partitioning (least loaded partition)
  PARTITION_STRATEGY_LOAD_BALANCED = 6;
}

```

---

### priority_level.proto {#priority_level}

**Path**: `pkg/queue/proto/priority_level.proto` **Package**: `gcommon.v1.queue`
**Lines**: 27

**Enums** (1): `PriorityLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/enums/priority_level.proto
// version: 1.0.0
// guid: e13c77fc-1bf7-42ed-947a-6e1ed4914bb2

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// PriorityLevel defines generic priority classes for queue messages.
enum PriorityLevel {
  // Default unspecified priority.
  PRIORITY_LEVEL_UNSPECIFIED = 0;
  // Low priority messages are processed after normal traffic.
  PRIORITY_LEVEL_LOW = 1;
  // Normal priority for standard workload.
  PRIORITY_LEVEL_MEDIUM = 2;
  // High priority messages are processed before others.
  PRIORITY_LEVEL_HIGH = 3;
  // Critical messages are processed immediately with highest importance.
  PRIORITY_LEVEL_CRITICAL = 4;
}

```

---

### priority_range.proto {#priority_range}

**Path**: `pkg/queue/proto/priority_range.proto` **Package**: `gcommon.v1.queue`
**Lines**: 24

**Messages** (1): `PriorityRange`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/priority_range.proto
// version: 1.0.0
// guid: 1efceade-7805-4b90-bdd0-2484a86cb6c9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Priority range for filtering.
 */
message PriorityRange {
  // Minimum priority (inclusive)
  int32 min_priority = 1;

  // Maximum priority (inclusive)
  int32 max_priority = 2;
}

```

---

### publish_result.proto {#publish_result}

**Path**: `pkg/queue/proto/publish_result.proto` **Package**: `gcommon.v1.queue`
**Lines**: 34

**Messages** (1): `PublishResult`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/publish_result.proto
// version: 1.0.0
// Result information for individual message publish operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Result for an individual message publish
message PublishResult {
  // Message ID assigned by the queue
  string message_id = 1;

  // Whether the publish was successful
  bool success = 2;

  // Error message if publish failed
  string error = 3;

  // Partition ID where message was published
  int32 partition_id = 4;

  // Offset within the partition
  int64 offset = 5;

  // Timestamp when message was published
  int64 timestamp = 6;
}

```

---
