# queue_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [acknowledgment.proto](#acknowledgment)
- [age_bucket.proto](#age_bucket)
- [age_distribution.proto](#age_distribution)
- [alert_rule.proto](#alert_rule)
- [anti_affinity_rule.proto](#anti_affinity_rule)
- [api_key_auth.proto](#api_key_auth)
- [basic_queue_stats.proto](#basic_queue_stats)
- [binding_info.proto](#binding_info)
- [checksum_validation.proto](#checksum_validation)
- [cluster_health.proto](#cluster_health)
- [cluster_info.proto](#cluster_info)
- [cluster_stats.proto](#cluster_stats)
- [conflict_detection.proto](#conflict_detection)
- [conflict_resolution.proto](#conflict_resolution)
- [connection_details.proto](#connection_details)
- [consistency_validation.proto](#consistency_validation)
- [consumer.proto](#consumer)
- [consumer_client.proto](#consumer_client)
- [consumer_error_stats.proto](#consumer_error_stats)
- [consumer_group.proto](#consumer_group)
- [consumer_group_stats.proto](#consumer_group_stats)
- [consumer_stats.proto](#consumer_stats)
- [content_filter.proto](#content_filter)
- [content_update.proto](#content_update)
- [custom_resolution.proto](#custom_resolution)
- [dead_letter_policy.proto](#dead_letter_policy)
- [deletion_stats.proto](#deletion_stats)
- [delivery_options.proto](#delivery_options)
- [delivery_settings.proto](#delivery_settings)
- [encryption_info.proto](#encryption_info)
- [error_stats.proto](#error_stats)
- [error_type_stat.proto](#error_type_stat)
- [external_role_provider.proto](#external_role_provider)
- [failed_ack.proto](#failed_ack)
- [failed_field_update.proto](#failed_field_update)
- [filter_criteria.proto](#filter_criteria)
- [filter_settings.proto](#filter_settings)
- [flow_control.proto](#flow_control)
- [flow_control_settings.proto](#flow_control_settings)
- [format_options.proto](#format_options)
- [group_coordinator.proto](#group_coordinator)
- [historical_data_point.proto](#historical_data_point)
- [historical_stats.proto](#historical_stats)
- [integrity_validation.proto](#integrity_validation)
- [jwt_auth.proto](#jwt_auth)
- [last_writer_wins.proto](#last_writer_wins)
- [latency_metrics.proto](#latency_metrics)
- [message_ack_result.proto](#message_ack_result)
- [message_envelope.proto](#message_envelope)
- [message_filter.proto](#message_filter)
---


## Detailed Documentation

### acknowledgment.proto {#acknowledgment}

**Path**: `gcommon/v1/queue/acknowledgment.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `Acknowledgment`

**Imports** (4):

- `gcommon/v1/common/ack_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/acknowledgment.proto
// version: 1.1.0
// guid: c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

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
  string queue_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Partition ID (for partitioned queues)
  int32 partition_id = 4;

  // Message offset within the partition
  int64 offset = 5;

  // Acknowledgment type
  gcommon.v1.common.AckType ack_type = 6;

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

### age_bucket.proto {#age_bucket}

**Path**: `gcommon/v1/queue/age_bucket.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `AgeBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/age_bucket.proto
// version: 1.0.0
// guid: b9e2ab5f-72b7-4a4b-bade-21762099184a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AgeBucket {
  int64 min_age_seconds = 1 [(buf.validate.field).int64.gte = 0];
  int64 max_age_seconds = 2 [(buf.validate.field).int64.gte = 0];
  int64 message_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### age_distribution.proto {#age_distribution}

**Path**: `gcommon/v1/queue/age_distribution.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `AgeDistribution`

**Imports** (3):

- `gcommon/v1/queue/age_bucket.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/age_distribution.proto
// version: 1.0.0
// guid: 5599d940-19cf-4e9c-a4ce-d102c9c0ae57

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/age_bucket.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AgeDistribution {
  // Age buckets in seconds
  repeated AgeBucket buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Summary statistics
  double average_age_seconds = 2 [(buf.validate.field).double.gte = 0.0];
  double oldest_message_age_seconds = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### alert_rule.proto {#alert_rule}

**Path**: `gcommon/v1/queue/alert_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `AlertRule`

**Imports** (5):

- `gcommon/v1/common/alert_condition.proto`
- `gcommon/v1/common/metrics_alert_severity.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alert_rule.proto
// version: 1.0.0
// guid: 5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/alert_condition.proto";
import "gcommon/v1/common/metrics_alert_severity.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * An individual alert rule.
 */
message AlertRule {
  // Unique name for the rule
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Human-readable description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Metric to monitor
  string metric_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Condition for triggering the alert
  gcommon.v1.common.AlertCondition condition = 4;

  // Threshold value
  double threshold = 5;

  // Duration the condition must persist before alerting
  google.protobuf.Duration duration = 6;

  // Severity of the alert
  gcommon.v1.common.MetricsAlertSeverity severity = 7;

  // Whether the rule is enabled
  bool enabled = 8;

  // Labels to attach to the alert
  map<string, string> labels = 9;
}
```

---

### anti_affinity_rule.proto {#anti_affinity_rule}

**Path**: `gcommon/v1/queue/anti_affinity_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `AntiAffinityRule`

**Imports** (3):

- `gcommon/v1/common/anti_affinity_scope.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/anti_affinity_rule.proto
// version: 1.0.0
// guid: a0d26ff8-7127-4e69-b8f3-eec85c695787

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/anti_affinity_scope.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Anti-affinity rule for replica placement.
 */
message AntiAffinityRule {
  // Label key to check for anti-affinity
  string label_key = 1 [(buf.validate.field).string.min_len = 1];

  // Label values that should not be co-located
  repeated string label_values = 2 [(buf.validate.field).repeated.min_items = 1];

  // Scope of the anti-affinity rule
  gcommon.v1.common.AntiAffinityScope scope = 3;
}
```

---

### api_key_auth.proto {#api_key_auth}

**Path**: `gcommon/v1/queue/api_key_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `APIKeyAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api_key_auth.proto
// version: 1.0.0
// guid: 4ac6d133-bd64-491e-8c17-2a716164dd87

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message APIKeyAuth {
  // API key for authentication
  string api_key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional API key ID
  string key_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### basic_queue_stats.proto {#basic_queue_stats}

**Path**: `gcommon/v1/queue/basic_queue_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `BasicQueueStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/basic_queue_stats.proto
// file: proto/gcommon/v1/queue/basic_queue_stats.proto
// version: 1.0.0
// guid: 0e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b
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
 * Basic statistics for a queue.
 */
message BasicQueueStats {
  // Queue name
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### binding_info.proto {#binding_info}

**Path**: `gcommon/v1/queue/binding_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `BindingInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/binding_info.proto
// file: proto/gcommon/v1/queue/binding_info.proto
// version: 1.0.0
// guid: 1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a
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
 * Information about queue and topic bindings.
 */
message BindingInfo {
  // Name of the binding
  string binding_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### checksum_validation.proto {#checksum_validation}

**Path**: `gcommon/v1/queue/checksum_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ChecksumValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/checksum_validation.proto
// version: 1.0.0
// guid: 34bd9a2b-54d5-4c3e-aa17-382d38a98306

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ChecksumValidation {
  // Overall checksum validation passed
  bool passed = 1;

  // Expected checksum
  string expected_checksum = 2 [(buf.validate.field).string.min_len = 1];

  // Actual checksum
  string actual_checksum = 3 [(buf.validate.field).string.min_len = 1];

  // Checksum algorithm used
  string checksum_algorithm = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### cluster_health.proto {#cluster_health}

**Path**: `gcommon/v1/queue/cluster_health.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ClusterHealth`

**Imports** (3):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_health.proto
// version: 1.0.0
// guid: a0aa1fd8-9db2-427a-b5d5-359c620f271a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ClusterHealth {
  // Overall health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Number of healthy nodes
  int32 healthy_nodes = 2 [(buf.validate.field).int32.gte = 0];

  // Total number of nodes
  int32 total_nodes = 3 [(buf.validate.field).int32.gte = 0];

  // Health issues affecting the cluster
  repeated string issues = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### cluster_info.proto {#cluster_info}

**Path**: `gcommon/v1/queue/cluster_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 59

**Messages** (1): `ClusterInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_info.proto
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Cluster information for queue management.
 * Contains metadata about the message queue cluster.
 */
message ClusterInfo {
  // Cluster identifier
  string cluster_id = 1;

  // Cluster name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### cluster_stats.proto {#cluster_stats}

**Path**: `gcommon/v1/queue/cluster_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ClusterStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_stats.proto
// version: 1.0.0
// guid: 6318f554-f8e9-434a-a33f-84ab2582e93c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics for the entire cluster.
 */
message ClusterStats {
  // Total number of queues across all nodes
  int64 total_queues = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of messages across all queues
  int64 total_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Total throughput (messages per second)
  double total_throughput = 3 [(buf.validate.field).double.gte = 0.0];

  // Number of active connections
  int64 active_connections = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### conflict_detection.proto {#conflict_detection}

**Path**: `gcommon/v1/queue/conflict_detection.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ConflictDetection`

**Imports** (4):

- `gcommon/v1/common/conflict_strategy.proto`
- `gcommon/v1/queue/timestamp_config.proto`
- `gcommon/v1/queue/vector_clock_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/conflict_detection.proto
// version: 1.0.1
// guid: 49cc6bab-66b1-4e09-9337-76d6644a2b81

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/conflict_strategy.proto";
import "gcommon/v1/queue/timestamp_config.proto";
import "gcommon/v1/queue/vector_clock_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConflictDetection {
  // Enable conflict detection
  bool enabled = 1;

  // Conflict detection strategy
  gcommon.v1.common.ConflictStrategy strategy = 2;

  // Vector clock configuration
  VectorClockConfig vector_clock = 3;

  // Timestamp-based detection settings
  TimestampConfig timestamp_config = 4;
}
```

---

### conflict_resolution.proto {#conflict_resolution}

**Path**: `gcommon/v1/queue/conflict_resolution.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `QueueConflictResolution`

**Imports** (5):

- `gcommon/v1/common/resolution_strategy.proto`
- `gcommon/v1/queue/custom_resolution.proto`
- `gcommon/v1/queue/last_writer_wins.proto`
- `gcommon/v1/queue/multi_value_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/conflict_resolution.proto
// version: 1.0.1
// guid: 6757adde-ed50-4ff7-9771-170223aaeca8

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/resolution_strategy.proto";
import "gcommon/v1/queue/custom_resolution.proto";
import "gcommon/v1/queue/last_writer_wins.proto";
import "gcommon/v1/queue/multi_value_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueConflictResolution {
  // Conflict resolution strategy
  gcommon.v1.common.ResolutionStrategy strategy = 1;

  // Custom resolution function settings
  CustomResolution custom_resolution = 2;

  // Last-writer-wins settings
  LastWriterWins lww_config = 3;

  // Multi-value conflict handling
  MultiValueConfig multi_value = 4;
}
```

---

### connection_details.proto {#connection_details}

**Path**: `gcommon/v1/queue/connection_details.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `ConnectionDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/connection_details.proto
// version: 1.0.0
// guid: e63faacd-909b-487c-9be3-1cba61d1e2c9
// Connection details for queue message delivery

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ConnectionDetails contains information for establishing message delivery connections
message ConnectionDetails {
  // Delivery endpoint (for push mode)
  string delivery_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Authentication token for delivery
  string auth_token = 2 [(buf.validate.field).string.min_len = 1];

  // Heartbeat interval (milliseconds)
  int32 heartbeat_interval_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Keep-alive timeout (milliseconds)
  int32 keep_alive_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // SSL/TLS configuration
  bool ssl_enabled = 5;

  // Connection metadata
  map<string, string> connection_metadata = 6;
}
```

---

### consistency_validation.proto {#consistency_validation}

**Path**: `gcommon/v1/queue/consistency_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ConsistencyValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consistency_validation.proto
// version: 1.0.0
// guid: ed16a632-9594-4189-90f8-2d0db13c7f9d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsistencyValidation {
  // Enable consistency validation
  bool enabled = 1;

  // Validation interval (seconds)
  int32 validation_interval_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Validation scope (local, cluster, global)
  string validation_scope = 3 [(buf.validate.field).string.min_len = 1];

  // Actions to take on validation failure
  repeated string failure_actions = 4 [(buf.validate.field).repeated.min_items = 1];

  // Validation timeout (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### consumer.proto {#consumer}

**Path**: `gcommon/v1/queue/consumer.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `Consumer`

**Imports** (7):

- `gcommon/v1/common/consumer_state.proto`
- `gcommon/v1/queue/consumer_client.proto`
- `gcommon/v1/queue/consumer_config.proto`
- `gcommon/v1/queue/consumer_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer.proto
// version: 1.0.0
// guid: 1bb92667-7d61-4aea-b8df-a372aa46cf8a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/consumer_state.proto";
import "gcommon/v1/queue/consumer_client.proto";
import "gcommon/v1/queue/consumer_config.proto";
import "gcommon/v1/queue/consumer_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message Consumer {
  // Unique consumer identifier
  string consumer_id = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer client information
  ConsumerClient client_info = 2;

  // Consumer state
  gcommon.v1.common.ConsumerState state = 3;

  // Assigned partitions
  repeated int32 assigned_partitions = 4 [(buf.validate.field).repeated.min_items = 1];

  // Consumer configuration
  ConsumerConfig config = 5;

  // Consumer statistics
  ConsumerStats stats = 6;

  // Last heartbeat timestamp
  google.protobuf.Timestamp last_heartbeat = 7;

  // Join timestamp
  google.protobuf.Timestamp joined_at = 8;
}
```

---

### consumer_client.proto {#consumer_client}

**Path**: `gcommon/v1/queue/consumer_client.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ConsumerClient`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_client.proto
// version: 1.0.0
// guid: 30ccc081-9c0b-470f-8c9a-fcc26b8b9cde

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerClient {
  // Client ID
  string client_id = 1 [(buf.validate.field).string.min_len = 1];

  // Client host/IP address
  string client_host = 2 [(buf.validate.field).string.min_len = 1];

  // Client application name
  string client_app = 3 [(buf.validate.field).string.min_len = 1];

  // Client version
  string client_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Client rack (for rack-aware assignment)
  string client_rack = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### consumer_error_stats.proto {#consumer_error_stats}

**Path**: `gcommon/v1/queue/consumer_error_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `ConsumerErrorStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_error_stats.proto
// version: 1.0.0
// guid: 1d9e7970-3641-4541-a107-2c4736fa88be

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerErrorStats {
  // Total processing errors
  int64 total_errors = 1 [(buf.validate.field).int64.gte = 0];

  // Connection errors
  int64 connection_errors = 2 [(buf.validate.field).int64.gte = 0];

  // Timeout errors
  int64 timeout_errors = 3 [(buf.validate.field).int64.gt = 0];

  // Serialization errors
  int64 serialization_errors = 4 [(buf.validate.field).int64.gte = 0];

  // Last error timestamp
  google.protobuf.Timestamp last_error = 5;
}
```

---

### consumer_group.proto {#consumer_group}

**Path**: `gcommon/v1/queue/consumer_group.proto` **Package**: `gcommon.v1.queue` **Lines**: 61

**Messages** (1): `ConsumerGroup`

**Imports** (9):

- `gcommon/v1/common/consumer_group_state.proto`
- `gcommon/v1/queue/consumer.proto`
- `gcommon/v1/queue/consumer_group_config.proto`
- `gcommon/v1/queue/consumer_group_stats.proto`
- `gcommon/v1/queue/group_coordinator.proto`
- `gcommon/v1/queue/partition_assignment.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group.proto
// version: 1.0.0
// guid: 04a92687-cec2-4eac-a15d-f6f0c884eab3

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/consumer_group_state.proto";
import "gcommon/v1/queue/consumer.proto";
import "gcommon/v1/queue/consumer_group_config.proto";
import "gcommon/v1/queue/consumer_group_stats.proto";
import "gcommon/v1/queue/group_coordinator.proto";
import "gcommon/v1/queue/partition_assignment.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerGroup {
  // Unique identifier for the consumer group
  string group_id = 1;

  // Group name (human-readable)
  string group_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic or queue this group is consuming from
  string topic = 3;

  // Consumer group configuration
  ConsumerGroupConfig config = 4;

  // Current group state
  gcommon.v1.common.ConsumerGroupState state = 5;

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
  google.protobuf.Timestamp created_at = 11 [ (buf.validate.field).required = true ];

  // Last updated timestamp
  google.protobuf.Timestamp updated_at = 12;
}
```

---

### consumer_group_stats.proto {#consumer_group_stats}

**Path**: `gcommon/v1/queue/consumer_group_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `ConsumerGroupStats`

**Imports** (4):

- `gcommon/v1/queue/consumer_error_stats.proto`
- `gcommon/v1/queue/rebalance_stats.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group_stats.proto
// version: 1.0.0
// guid: b8b6993f-38ea-4912-8d9b-b5d70c3968fc

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/consumer_error_stats.proto";
import "gcommon/v1/queue/rebalance_stats.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerGroupStats {
  // Total number of active consumers
  int32 active_consumers = 1 [(buf.validate.field).int32.gte = 0];

  // Total number of assigned partitions
  int32 assigned_partitions = 2 [(buf.validate.field).int32.gte = 0];

  // Total messages consumed by the group
  int64 total_messages_consumed = 3 [(buf.validate.field).int64.gte = 0];

  // Total bytes consumed by the group
  int64 total_bytes_consumed = 4 [(buf.validate.field).int64.gte = 0];

  // Average group consumption rate (messages/second)
  double group_consumption_rate = 5 [(buf.validate.field).double.gte = 0.0];

  // Total group lag
  int64 total_lag = 6 [(buf.validate.field).int64.gte = 0];

  // Rebalance statistics
  RebalanceStats rebalance_stats = 7;

  // Error statistics for the consumer group
  ConsumerErrorStats error_stats = 8;
}
```

---

### consumer_stats.proto {#consumer_stats}

**Path**: `gcommon/v1/queue/consumer_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ConsumerStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_stats.proto
// version: 1.0.0
// guid: f4a5b6c7-890d-234e-5678-890123456789

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerStats {
  // Consumer ID
  string consumer_id = 1 [(buf.validate.field).string.min_len = 1];

  // Messages processed
  int64 messages_processed = 2 [(buf.validate.field).int64.gte = 0];

  // Processing rate per second
  double processing_rate = 3 [(buf.validate.field).double.gte = 0.0];

  // Error count
  int64 error_count = 4 [(buf.validate.field).int64.gte = 0];

  // Last active timestamp
  int64 last_active = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### content_filter.proto {#content_filter}

**Path**: `gcommon/v1/queue/content_filter.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ContentFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/content_filter.proto
// version: 1.0.0
// guid: 54ce7d22-49b5-4c41-86a5-4a5156d1e74b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ContentFilter {
  // JSON path or field name
  string field_path = 1 [(buf.validate.field).string.min_len = 1];

  // Filter operator (equals, contains, regex, gt, lt, etc.)
  string operator = 2 [(buf.validate.field).string.min_len = 1];

  // Filter value
  string value = 3 [(buf.validate.field).string.min_len = 1];

  // Case sensitive matching
  bool case_sensitive = 4;
}
```

---

### content_update.proto {#content_update}

**Path**: `gcommon/v1/queue/content_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `ContentUpdate`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/content_update.proto
// version: 1.0.0
// guid: 9acab812-6e9a-44f3-8206-8aee653ad5da

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ContentUpdate {
  // New message payload
  google.protobuf.Any new_payload = 1;

  // Content encoding
  string content_encoding = 2 [(buf.validate.field).string.min_len = 1];

  // Content type
  string content_type = 3 [(buf.validate.field).string.min_len = 1];

  // Compression applied to content
  string compression = 4 [(buf.validate.field).string.min_len = 1];

  // Checksum of new content
  string content_checksum = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### custom_resolution.proto {#custom_resolution}

**Path**: `gcommon/v1/queue/custom_resolution.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `CustomResolution`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/custom_resolution.proto
// version: 1.0.0
// guid: 94eb8c9d-f368-4910-9841-128a9ceee9c8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message CustomResolution {
  // Resolution function name or identifier
  string function_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Function parameters
  map<string, string> parameters = 2;

  // Timeout for resolution function (milliseconds)
  int32 timeout_ms = 3;
}
```

---

### dead_letter_policy.proto {#dead_letter_policy}

**Path**: `gcommon/v1/queue/dead_letter_policy.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `DeadLetterPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/dead_letter_policy.proto
// file: proto/gcommon/v1/queue/dead_letter_policy.proto
// version: 1.0.0
// guid: 5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Dead letter policy configuration for handling failed messages.
 * Messages that exceed retry limits or cannot be processed will be
 * sent to a dead letter queue for manual inspection.
 */
message DeadLetterPolicy {
  // Name of the dead letter queue where failed messages will be sent
  string dead_letter_queue = 1 [(buf.validate.field).string.min_len = 1];

  // Maximum number of delivery attempts before sending to dead letter queue
  int32 max_delivery_attempts = 2 [(buf.validate.field).int32.gte = 0];

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

### deletion_stats.proto {#deletion_stats}

**Path**: `gcommon/v1/queue/deletion_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `DeletionStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/deletion_stats.proto
// version: 1.0.0
// guid: 671eaddd-dddd-48e2-8910-428b3f80a7d1

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeletionStats {
  // Number of messages deleted
  int64 messages_deleted = 1 [(buf.validate.field).int64.gte = 0];

  // Amount of data deleted (bytes)
  int64 data_deleted_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Number of subscriptions deleted
  int32 subscriptions_deleted = 3 [(buf.validate.field).int32.gte = 0];

  // Number of partitions deleted
  int32 partitions_deleted = 4 [(buf.validate.field).int32.gte = 0];

  // Time taken for deletion (milliseconds)
  int64 deletion_duration_ms = 5 [(buf.validate.field).int64.gt = 0];
}
```

---

### delivery_options.proto {#delivery_options}

**Path**: `gcommon/v1/queue/delivery_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `DeliveryOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_options.proto
// version: 1.0.0
// guid: 226d4794-23ca-4b54-9a0d-7c6671093c04

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// DeliveryOptions control message routing and retries.
message DeliveryOptions {
  // Optional delivery delay.
  google.protobuf.Duration delay = 1;

  // Maximum retry attempts before sending to dead letter queue.
  int32 max_retries = 2 [(buf.validate.field).int32.gte = 0];

  // Delay between retry attempts.
  google.protobuf.Duration retry_delay = 3;

  // Multiplier for exponential backoff.
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Maximum delay allowed between retries.
  google.protobuf.Duration max_retry_delay = 5;

  // Name of the dead letter queue.
  string dead_letter_queue = 6 [(buf.validate.field).string.min_len = 1];

  // Whether acknowledgment is required for delivery.
  bool require_ack = 7;

  // Timeout waiting for acknowledgment.
  google.protobuf.Duration ack_timeout = 8;
}
```

---

### delivery_settings.proto {#delivery_settings}

**Path**: `gcommon/v1/queue/delivery_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `DeliverySettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_settings.proto
// version: 1.0.0
// guid: 90fc8ba9-b70c-41e9-afaf-a90b7097d4dd

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeliverySettings {
  // Delivery mode (push, pull, streaming)
  string delivery_mode = 1 [(buf.validate.field).string.min_len = 1];

  // Endpoint for push delivery
  string push_endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Delivery timeout (milliseconds)
  int32 delivery_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Enable ordered delivery
  bool ordered_delivery = 4;
}
```

---

### encryption_info.proto {#encryption_info}

**Path**: `gcommon/v1/queue/encryption_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `EncryptionInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/encryption_info.proto
// version: 1.0.0
// guid: 79dc45f4-d25b-40cb-8380-45f54e170aa7

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message EncryptionInfo {
  // Encryption enabled
  bool enabled = 1;

  // Encryption algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Key management service
  string kms_provider = 3 [(buf.validate.field).string.min_len = 1];

  // Key identifier
  string key_id = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### error_stats.proto {#error_stats}

**Path**: `gcommon/v1/queue/error_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `QueueErrorStats`

**Imports** (3):

- `gcommon/v1/queue/error_type_stat.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_stats.proto
// version: 1.0.0
// guid: f679dd1a-539c-42a7-aa4e-0c14ef8adac2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/error_type_stat.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueErrorStats {
  int64 total_errors = 1 [(buf.validate.field).int64.gte = 0];
  double error_rate = 2 [(buf.validate.field).double.gte = 0.0];
  repeated ErrorTypeStat error_types = 3 [(buf.validate.field).repeated.min_items = 1];
  repeated string recent_error_messages = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### error_type_stat.proto {#error_type_stat}

**Path**: `gcommon/v1/queue/error_type_stat.proto` **Package**: `gcommon.v1.queue` **Lines**: 21

**Messages** (1): `ErrorTypeStat`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_type_stat.proto
// version: 1.0.0
// guid: 14988398-e55c-484b-a755-0e18d26b7d8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorTypeStat {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double rate = 3 [(buf.validate.field).double.gte = 0.0];
  string last_occurrence = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### external_role_provider.proto {#external_role_provider}

**Path**: `gcommon/v1/queue/external_role_provider.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ExternalRoleProvider`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/external_role_provider.proto
// version: 1.0.0
// guid: 890e55e1-8627-452f-95dc-f799e0316fec

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ExternalRoleProvider {
  // Provider type (ldap, oauth, etc.)
  string provider_type = 1 [(buf.validate.field).string.min_len = 1];

  // Provider endpoint URL
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Authentication credentials for provider
  map<string, string> credentials = 3;

  // Cache TTL for role lookups (seconds)
  int32 cache_ttl_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### failed_ack.proto {#failed_ack}

**Path**: `gcommon/v1/queue/failed_ack.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `FailedAck`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/failed_ack.proto
// version: 1.0.0
// guid: 576df787-4718-4249-a439-b368117dec41

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FailedAck {
  // Message ID that failed to acknowledge
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Reason for acknowledgment failure
  string error_reason = 2 [(buf.validate.field).string.min_len = 1];

  // Error code
  string error_code = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### failed_field_update.proto {#failed_field_update}

**Path**: `gcommon/v1/queue/failed_field_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `FailedFieldUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/failed_field_update.proto
// version: 1.0.0
// guid: 3fbfa5f5-c2fc-4c93-9fec-823125628ddb

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FailedFieldUpdate {
  // Field name that failed to update
  string field_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reason for failure
  string failure_reason = 2;

  // Error code specific to this field
  string error_code = 3;

  // Original value that couldn't be updated
  string original_value = 4;

  // Attempted new value
  string attempted_value = 5;
}
```

---

### filter_criteria.proto {#filter_criteria}

**Path**: `gcommon/v1/queue/filter_criteria.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `FilterCriteria`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/filter_criteria.proto
// version: 1.0.0
// guid: 202f243e-e814-4448-8117-d5f74fc966a0

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FilterCriteria {
  // Include message patterns
  repeated string include_patterns = 1 [(buf.validate.field).repeated.min_items = 1];

  // Exclude message patterns
  repeated string exclude_patterns = 2 [(buf.validate.field).repeated.min_items = 1];

  // Header-based filters
  map<string, string> header_filters = 3;

  // Content-type filters
  repeated string content_types = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### filter_settings.proto {#filter_settings}

**Path**: `gcommon/v1/queue/filter_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `FilterSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/filter_settings.proto
// version: 1.0.0
// guid: aae01edc-d403-456d-9c93-e9f4c0c8c699

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FilterSettings {
  // Content-based filters
  map<string, string> content_filters = 1;

  // Header-based filters
  map<string, string> header_filters = 2;

  // Filter expression
  string filter_expression = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### flow_control.proto {#flow_control}

**Path**: `gcommon/v1/queue/flow_control.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `FlowControl`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flow_control.proto
// version: 1.0.0
// guid: 40b0fde3-4f0f-4bef-b893-248588fbf4a6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// FlowControl settings influence how the queue handles
// bursts of incoming messages.
message FlowControl {
  // Maximum number of unacknowledged messages allowed.
  int32 max_in_flight = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum amount of data in flight (bytes).
  int64 max_bytes_in_flight = 2 [(buf.validate.field).int64.gte = 0];

  // Deadline before a message is redelivered if not acknowledged.
  google.protobuf.Duration ack_deadline = 3;
}
```

---

### flow_control_settings.proto {#flow_control_settings}

**Path**: `gcommon/v1/queue/flow_control_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `FlowControlSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flow_control_settings.proto
// version: 1.0.0
// guid: 072cab5f-9831-4a0e-8727-f69e8354fe4a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FlowControlSettings {
  // Maximum outstanding messages
  int32 max_outstanding_messages = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Flow control algorithm
  string algorithm = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### format_options.proto {#format_options}

**Path**: `gcommon/v1/queue/format_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `FormatOptions`

**Imports** (4):

- `gcommon/v1/common/compression_algorithm.proto`
- `gcommon/v1/common/serialization_format.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/format_options.proto
// version: 1.0.0
// guid: be0dbb05-7495-4e4c-b7c7-97774a7e0489

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/compression_algorithm.proto";
import "gcommon/v1/common/serialization_format.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Serialization options for a specific format.
 */
message FormatOptions {
  // Serialization format
  gcommon.v1.common.SerializationFormat format = 1;

  // Format-specific configuration
  map<string, string> options = 2;

  // Whether to enable compression for this format
  bool enable_compression = 3;

  // Compression algorithm
  gcommon.v1.common.CompressionAlgorithm compression_algorithm = 4;

  // Maximum message size for this format
  int64 max_message_size = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### group_coordinator.proto {#group_coordinator}

**Path**: `gcommon/v1/queue/group_coordinator.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `GroupCoordinator`

**Imports** (3):

- `gcommon/v1/common/coordinator_state.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/group_coordinator.proto
// version: 1.0.0
// guid: e3e0d17b-a593-44ec-a32c-8b282cf136fc

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/coordinator_state.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GroupCoordinator {
  // Coordinator node ID
  string node_id = 1 [(buf.validate.field).string.min_len = 1];

  // Coordinator host
  string host = 2 [(buf.validate.field).string.min_len = 1];

  // Coordinator port
  int32 port = 3 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Coordinator state
  gcommon.v1.common.CoordinatorState state = 4;

  // Leadership epoch
  int64 epoch = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### historical_data_point.proto {#historical_data_point}

**Path**: `gcommon/v1/queue/historical_data_point.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `HistoricalDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/historical_data_point.proto
// version: 1.0.0
// guid: 8e947e6d-7509-4f8b-931c-cb36d515b5e5

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message HistoricalDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 message_count = 2 [(buf.validate.field).int64.gte = 0];
  double throughput = 3 [(buf.validate.field).double.gte = 0.0];
  double average_latency_ms = 4 [(buf.validate.field).double.gte = 0.0];
  double error_rate = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### historical_stats.proto {#historical_stats}

**Path**: `gcommon/v1/queue/historical_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 21

**Messages** (1): `HistoricalStats`

**Imports** (4):

- `gcommon/v1/queue/historical_data_point.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/historical_stats.proto
// version: 1.0.0
// guid: 7e6ca4d3-82ff-42f7-9761-fbb25977f58d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/historical_data_point.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message HistoricalStats {
  repeated HistoricalDataPoint data_points = 1 [(buf.validate.field).repeated.min_items = 1];
  google.protobuf.Duration aggregation_period = 2;
}
```

---

### integrity_validation.proto {#integrity_validation}

**Path**: `gcommon/v1/queue/integrity_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `IntegrityValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/integrity_validation.proto
// version: 1.0.0
// guid: 98819329-10f2-4edf-85cb-52919123d92f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message IntegrityValidation {
  // Integrity validation passed
  bool passed = 1;

  // Corrupted message count
  int64 corrupted_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Missing message count
  int64 missing_messages = 3 [(buf.validate.field).int64.gte = 0];

  // Duplicate message count
  int64 duplicate_messages = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### jwt_auth.proto {#jwt_auth}

**Path**: `gcommon/v1/queue/jwt_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `JwtAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/jwt_auth.proto
// version: 1.0.0
// guid: 105a22e1-20d6-4414-9bf3-36161857c31d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message JwtAuth {
  // Enable JWT authentication
  bool enabled = 1;

  // JWT signing algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Public key or secret for verification
  string verification_key = 3 [(buf.validate.field).string.min_len = 1];

  // Expected issuer
  string expected_issuer = 4 [(buf.validate.field).string.min_len = 1];

  // Expected audience
  repeated string expected_audience = 5 [(buf.validate.field).repeated.min_items = 1];

  // Clock skew tolerance (seconds)
  int32 clock_skew_seconds = 6 [(buf.validate.field).int32.gte = 0];

  // Required claims
  map<string, string> required_claims = 7;
}
```

---

### last_writer_wins.proto {#last_writer_wins}

**Path**: `gcommon/v1/queue/last_writer_wins.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `LastWriterWins`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/last_writer_wins.proto
// version: 1.0.1
// guid: 39e817ba-1ee6-4093-97a2-d4fda4de5312

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message LastWriterWins {
  // Use server timestamp instead of client timestamp
  bool use_server_timestamp = 1;

  // Timestamp precision for comparison
  string timestamp_precision = 2;
}
```

---

### latency_metrics.proto {#latency_metrics}

**Path**: `gcommon/v1/queue/latency_metrics.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `LatencyMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/latency_metrics.proto
// version: 1.0.0
// guid: 3e90b50a-4d0c-440a-911c-75bf6da02e43

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message LatencyMetrics {
  // Processing latency percentiles (in milliseconds)
  double p50_processing_latency_ms = 1 [(buf.validate.field).double.gte = 0.0];
  double p95_processing_latency_ms = 2 [(buf.validate.field).double.gte = 0.0];
  double p99_processing_latency_ms = 3 [(buf.validate.field).double.gte = 0.0];

  // Queue latency (time from enqueue to dequeue)
  double average_queue_latency_ms = 4 [(buf.validate.field).double.gte = 0.0];
  double p95_queue_latency_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // End-to-end latency (enqueue to completion)
  double average_e2e_latency_ms = 6 [(buf.validate.field).double.gte = 0.0];
  double p95_e2e_latency_ms = 7 [(buf.validate.field).double.gte = 0.0];
}
```

---

### message_ack_result.proto {#message_ack_result}

**Path**: `gcommon/v1/queue/message_ack_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `MessageAckResult`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_ack_result.proto
// version: 1.0.0
// guid: d7c68f75-1f4d-4758-ba66-a6aaa0dcf1a4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageAckResult {
  /**
   * Receipt handle of the message this result applies to.
   */
  string receipt_handle = 1 [(buf.validate.field).string.min_len = 1];

  /**
   * Whether this specific message was successfully acknowledged.
   */
  bool success = 2;

  /**
   * Error information if acknowledgment failed for this message.
   */
  gcommon.v1.common.Error error = 3;

  /**
   * Message ID for correlation (if available).
   */
  string message_id = 4 [(buf.validate.field).string.min_len = 1];

  /**
   * Processing result that was recorded (echoed from request).
   */
  string processing_result = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_envelope.proto {#message_envelope}

**Path**: `gcommon/v1/queue/message_envelope.proto` **Package**: `gcommon.v1.queue` **Lines**: 66

**Messages** (1): `MessageEnvelope`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/message_envelope.proto
// file: proto/gcommon/v1/queue/message_envelope.proto
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
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

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
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

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

### message_filter.proto {#message_filter}

**Path**: `gcommon/v1/queue/message_filter.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `MessageFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_filter.proto
// version: 1.0.0
// guid: 705dd4ef-6cef-458f-b70b-588f3e13eda0

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageFilter {
  // Filter by message headers
  map<string, string> header_filters = 1;

  // Filter by message properties
  map<string, string> property_filters = 2;

  // Minimum message priority
  int32 min_priority = 3 [(buf.validate.field).int32.gte = 0];

  // Maximum message age (seconds)
  int32 max_age_seconds = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Content type filter
  string content_type = 5 [(buf.validate.field).string.min_len = 1];

  // Custom filter expression
  string filter_expression = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

