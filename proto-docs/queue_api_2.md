# queue_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 117
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 6

## Files in this Module

- [get_queue_stats_response.proto](#get_queue_stats_response)
- [get_subscription_info_request.proto](#get_subscription_info_request)
- [get_subscription_info_response.proto](#get_subscription_info_response)
- [get_topic_info_request.proto](#get_topic_info_request)
- [get_topic_info_response.proto](#get_topic_info_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [import_queue_request.proto](#import_queue_request)
- [import_queue_response.proto](#import_queue_response)
- [list_messages_request.proto](#list_messages_request)
- [list_messages_response.proto](#list_messages_response)
- [list_queues_request.proto](#list_queues_request) ⚠️ 1 issues
- [list_queues_response.proto](#list_queues_response) ⚠️ 1 issues
- [list_subscriptions_request.proto](#list_subscriptions_request) ⚠️ 1 issues
- [list_subscriptions_response.proto](#list_subscriptions_response) ⚠️ 1 issues
- [list_topics_request.proto](#list_topics_request)
- [list_topics_response.proto](#list_topics_response)
- [migrate_queue_request.proto](#migrate_queue_request)
- [migrate_queue_response.proto](#migrate_queue_response)
- [nack_request.proto](#nack_request)
- [nack_response.proto](#nack_response)
- [pause_queue_request.proto](#pause_queue_request)
- [pause_queue_response.proto](#pause_queue_response)
- [peek_request.proto](#peek_request)
- [peek_response.proto](#peek_response)
- [publish_request.proto](#publish_request)
- [publish_response.proto](#publish_response)
- [pull_request.proto](#pull_request) ⚠️ 1 issues
- [pull_response.proto](#pull_response) ⚠️ 1 issues
- [purge_request.proto](#purge_request)
- [purge_response.proto](#purge_response)
- [push_request.proto](#push_request)
- [push_response.proto](#push_response)
- [reset_queue_stats_request.proto](#reset_queue_stats_request)
- [reset_queue_stats_response.proto](#reset_queue_stats_response)
- [restore_queue_request.proto](#restore_queue_request)
- [restore_queue_response.proto](#restore_queue_response)
- [resume_queue_request.proto](#resume_queue_request)
- [resume_queue_response.proto](#resume_queue_response)
- [seek_request.proto](#seek_request)
- [seek_response.proto](#seek_response)
- [send_message_request.proto](#send_message_request)
- [send_message_response.proto](#send_message_response)
- [stream_messages_request.proto](#stream_messages_request)
- [stream_messages_response.proto](#stream_messages_response)
- [subscribe_request.proto](#subscribe_request)
- [subscribe_response.proto](#subscribe_response)
- [unsubscribe_request.proto](#unsubscribe_request)
- [unsubscribe_response.proto](#unsubscribe_response)
- [update_message_request.proto](#update_message_request)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)
- [queue_2](./queue_2.md)
- [queue_config](./queue_config.md)
- [web](./web.md)

**Modules that depend on this one**:

- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)
- [queue_1](./queue_1.md)
- [queue_services](./queue_services.md)

---

## Detailed Documentation

### get_queue_stats_response.proto {#get_queue_stats_response}

**Path**: `pkg/queue/proto/get_queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 262

**Messages** (18): `GetQueueStatsResponse`, `QueueStatsSummary`, `QueueStats`, `MessageStateCounts`, `ThroughputMetrics`, `LatencyMetrics`, `QueueDepthSample`, `SizeDistribution`, `SizeBucket`, `AgeDistribution`, `AgeBucket`,
`QueueConfiguration`, `QueueConsumerStats`, `HistoricalStats`, `HistoricalDataPoint`, `ErrorStats`, `ErrorTypeStat`, `PerformanceMetrics`

**Imports** (5):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)
- `pkg/queue/proto/consumer_stats.proto` → [queue_1](./queue_1.md#consumer_stats)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/get_queue_stats_response.proto
// version: 1.0.0
// guid: 4e9b8c7d-6a5f-3e2d-8c1b-7a9e8d7c6b5a

// GetQueueStatsResponse message definition for queue statistics retrieval
//
// This file implements the 1-1-1 pattern: one message per file.
// It defines the response message containing queue statistics and metrics.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/response_metadata.proto";
import "pkg/queue/proto/consumer_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// GetQueueStatsResponse contains comprehensive queue statistics
//
// This message provides detailed metrics about queue performance,
// message processing, and system health.
message GetQueueStatsResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Overall statistics summary
  QueueStatsSummary summary = 2;

  // Per-queue statistics (if multiple queues requested)
  repeated QueueStats queue_stats = 3;

  // Consumer statistics (if requested)
  repeated ConsumerStats consumer_stats = 4;

  // Historical statistics (if requested)
  HistoricalStats historical_stats = 5;

  // Error statistics (if requested)
  ErrorStats error_stats = 6;

  // Performance metrics
  PerformanceMetrics performance_metrics = 7;

  // Timestamp when these statistics were generated
  google.protobuf.Timestamp generated_at = 8;
}

// Summary of overall queue system statistics
message QueueStatsSummary {
  // Total number of queues
  int64 total_queues = 1;

  // Total messages across all queues
  int64 total_messages = 2;

  // Total messages processed in the last hour
  int64 messages_processed_last_hour = 3;

  // Average processing time across all queues
  google.protobuf.Duration average_processing_time = 4;

  // Overall system health score (0-100)
  int32 health_score = 5;

  // Total active consumers
  int64 active_consumers = 6;

  // Total storage used by messages
  int64 total_storage_bytes = 7;
}

// Statistics for a specific queue
message QueueStats {
  // Queue name
  string queue_name = 1;

  // Current message count
  int64 message_count = 2;

  // Messages in different states
  MessageStateCounts state_counts = 3;

  // Throughput metrics
  ThroughputMetrics throughput = 4;

  // Latency metrics
  LatencyMetrics latency = 5;

  // Queue depth over time
  repeated QueueDepthSample depth_samples = 6;

  // Message size distribution
  SizeDistribution size_distribution = 7;

  // Message age distribution
  AgeDistribution age_distribution = 8;

  // Queue configuration details
  QueueConfiguration configuration = 9;

  // Last activity timestamp
  google.protobuf.Timestamp last_activity = 10;
}

// Message counts by state
message MessageStateCounts {
  int64 pending = 1;
  int64 processing = 2;
  int64 completed = 3;
  int64 failed = 4;
  int64 retrying = 5;
  int64 dead_letter = 6;
}

// Throughput-related metrics
message ThroughputMetrics {
  // Messages per second over different time windows
  double messages_per_second_1m = 1;
  double messages_per_second_5m = 2;
  double messages_per_second_15m = 3;
  double messages_per_second_1h = 4;

  // Peak throughput observed
  double peak_messages_per_second = 5;
  google.protobuf.Timestamp peak_timestamp = 6;
}

// Latency-related metrics
message LatencyMetrics {
  // Processing latency percentiles (in milliseconds)
  double p50_processing_latency_ms = 1;
  double p95_processing_latency_ms = 2;
  double p99_processing_latency_ms = 3;

  // Queue latency (time from enqueue to dequeue)
  double average_queue_latency_ms = 4;
  double p95_queue_latency_ms = 5;

  // End-to-end latency (enqueue to completion)
  double average_e2e_latency_ms = 6;
  double p95_e2e_latency_ms = 7;
}

// Queue depth at a specific time
message QueueDepthSample {
  google.protobuf.Timestamp timestamp = 1;
  int64 depth = 2;
}

// Distribution of message sizes
message SizeDistribution {
  // Size buckets in bytes
  repeated SizeBucket buckets = 1;

  // Summary statistics
  int64 min_size_bytes = 2;
  int64 max_size_bytes = 3;
  double average_size_bytes = 4;
  double median_size_bytes = 5;
}

// Size bucket for distribution
message SizeBucket {
  int64 min_size_bytes = 1;
  int64 max_size_bytes = 2;
  int64 message_count = 3;
}

// Distribution of message ages
message AgeDistribution {
  // Age buckets in seconds
  repeated AgeBucket buckets = 1;

  // Summary statistics
  double average_age_seconds = 2;
  double oldest_message_age_seconds = 3;
}

// Age bucket for distribution
message AgeBucket {
  int64 min_age_seconds = 1;
  int64 max_age_seconds = 2;
  int64 message_count = 3;
}

// Queue configuration information
message QueueConfiguration {
  int64 max_messages = 1;
  google.protobuf.Duration visibility_timeout = 2;
  google.protobuf.Duration message_retention_period = 3;
  int32 max_retry_attempts = 4;
  bool dead_letter_queue_enabled = 5;
}

// Statistics for individual consumers in queue stats
message QueueConsumerStats {
  string consumer_id = 1;
  string queue_name = 2;
  int64 messages_processed = 3;
  double processing_rate = 4;
  double success_rate = 5;
  google.protobuf.Timestamp last_activity = 6;
  google.protobuf.Duration average_processing_time = 7;
}

// Historical statistics over time
message HistoricalStats {
  repeated HistoricalDataPoint data_points = 1;
  google.protobuf.Duration aggregation_period = 2;
}

// A single historical data point
message HistoricalDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 message_count = 2;
  double throughput = 3;
  double average_latency_ms = 4;
  double error_rate = 5;
}

// Error-related statistics
message ErrorStats {
  int64 total_errors = 1;
  double error_rate = 2;
  repeated ErrorTypeStat error_types = 3;
  repeated string recent_error_messages = 4;
}

// Statistics for a specific error type
message ErrorTypeStat {
  string error_type = 1;
  int64 count = 2;
  double rate = 3;
  string last_occurrence = 4;
}

// Performance metrics for the queue system
message PerformanceMetrics {
  // Memory usage
  int64 memory_used_bytes = 1;
  int64 memory_available_bytes = 2;

  // CPU usage percentage
  double cpu_usage_percent = 3;

  // Disk usage for persistent storage
  int64 disk_used_bytes = 4;
  int64 disk_available_bytes = 5;

  // Network metrics
  double network_bytes_per_second = 6;

  // Connection metrics
  int32 active_connections = 7;
  int32 max_connections = 8;
}

```

---

### get_subscription_info_request.proto {#get_subscription_info_request}

**Path**: `pkg/queue/proto/get_subscription_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `GetSubscriptionInfoRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/get_subscription_info_request.proto
// version: 1.0.0
// Request to get subscription information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to get subscription information
message GetSubscriptionInfoRequest {
  // Subscription ID to get info for
  string subscription_id = 1;

  // Include detailed metrics
  bool include_metrics = 2;

  // Include consumer group details
  bool include_consumer_details = 3;

  // Include partition assignments
  bool include_partitions = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}

```

---

### get_subscription_info_response.proto {#get_subscription_info_response}

**Path**: `pkg/queue/proto/get_subscription_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 61

**Messages** (1): `GetSubscriptionInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/get_subscription_info_response.proto
// file: queue/proto/responses/get_subscription_info_response.proto
// version: 1.0.0
// guid: 3f2e1d0c-9b8a-7f6e-5d4c-3b2a1f0e9d8c
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response message for subscription information retrieval.
 */
message GetSubscriptionInfoResponse {
  // Unique identifier for the subscription
  string subscription_id = 1;

  // Name of the subscription
  string subscription_name = 2;

  // Topic this subscription is bound to
  string topic_name = 3;

  // Current state of the subscription
  string state = 4;

  // Consumer group associated with this subscription
  string consumer_group = 5;

  // Current message offset position
  uint64 current_offset = 6;

  // Latest available message offset
  uint64 latest_offset = 7;

  // Number of unacknowledged messages
  uint64 unacked_count = 8;

  // Subscription creation timestamp
  google.protobuf.Timestamp created_at = 9;

  // Last activity timestamp
  google.protobuf.Timestamp last_activity = 10;

  // Number of active consumers
  uint32 active_consumers = 11;

  // Total messages consumed
  uint64 total_consumed = 12;

  // Message consumption rate (messages per second)
  double consumption_rate = 13;
}

```

---

### get_topic_info_request.proto {#get_topic_info_request}

**Path**: `pkg/queue/proto/get_topic_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `GetTopicInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/get_topic_info_request.proto
// version: 1.0.0
// guid: f3a4b5c6-d7e8-9f0a-1b2c-3d4e5f6a7b8c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to get information about a topic.
 * Used for retrieving topic metadata and configuration.
 */
message GetTopicInfoRequest {
  // Name of the topic to get information for
  string topic_name = 1;

  // Whether to include detailed statistics
  bool include_stats = 2;

  // Whether to include partition information
  bool include_partitions = 3;

  // Whether to include consumer group information
  bool include_consumer_groups = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;
}

```

---

### get_topic_info_response.proto {#get_topic_info_response}

**Path**: `pkg/queue/proto/get_topic_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 154

**Messages** (5): `GetTopicInfoResponse`, `TopicConfiguration`, `TopicPermissions`, `OwnerInfo`, `RetentionInfo`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/partition_info.proto` → [queue_1](./queue_1.md#partition_info)
- `pkg/queue/proto/topic_stats.proto` → [queue_2](./queue_2.md#topic_stats)

#### Source Code

```protobuf
// file: pkg/queue/proto/get_topic_info_response.proto
// version: 1.1.0
// Response containing topic information and metadata

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/partition_info.proto";
import "pkg/queue/proto/topic_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// GetTopicInfoResponse returns detailed information about a topic
message GetTopicInfoResponse {
  // Topic identifier
  string topic_id = 1;

  // Topic name
  string topic_name = 2;

  // Topic description
  string description = 3;

  // Topic creation timestamp
  google.protobuf.Timestamp created_at = 4;

  // Last modification timestamp
  google.protobuf.Timestamp updated_at = 5;

  // Topic statistics
  TopicStats stats = 6;

  // Partition information
  repeated PartitionInfo partitions = 7;

  // Topic configuration
  TopicConfiguration config = 8;

  // Topic state (active, paused, deleted)
  string state = 9;

  // Access permissions for the requesting user
  TopicPermissions permissions = 10;

  // Topic metadata
  map<string, string> metadata = 11;

  // Topic tags for categorization
  repeated string tags = 12;

  // Owner information
  OwnerInfo owner = 13;

  // Retention policy details
  RetentionInfo retention = 14;
}

// Topic configuration details
message TopicConfiguration {
  // Number of partitions
  int32 partition_count = 1;

  // Replication factor
  int32 replication_factor = 2;

  // Message retention period (seconds)
  int64 retention_period_seconds = 3;

  // Maximum message size (bytes)
  int64 max_message_size_bytes = 4;

  // Compression enabled
  bool compression_enabled = 5;

  // Compression algorithm
  string compression_algorithm = 6;

  // Encryption enabled
  bool encryption_enabled = 7;

  // Cleanup policy (delete, compact)
  string cleanup_policy = 8;

  // Minimum in-sync replicas
  int32 min_insync_replicas = 9;

  // Segment size (bytes)
  int64 segment_size_bytes = 10;
}

// Topic access permissions
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

// Topic owner information
message OwnerInfo {
  // Owner user ID
  string user_id = 1;

  // Owner username
  string username = 2;

  // Owner email
  string email = 3;

  // Organization/team
  string organization = 4;

  // Ownership timestamp
  google.protobuf.Timestamp owned_since = 5;
}

// Topic retention information
message RetentionInfo {
  // Current retention policy
  string retention_policy = 1;

  // Retention period (seconds)
  int64 retention_seconds = 2;

  // Size-based retention limit (bytes)
  int64 retention_bytes = 3;

  // Number of messages retained
  int64 retained_messages = 4;

  // Oldest message timestamp
  google.protobuf.Timestamp oldest_message_time = 5;

  // Next cleanup scheduled time
  google.protobuf.Timestamp next_cleanup_time = 6;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/queue/proto/health_check_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/health_check_request.proto
// version: 1.0.0
// guid: e9e95e53-7d2b-4dbf-896d-e9dea8853bd0
//
// HealthCheckRequest for the queue module

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message HealthCheckRequest {
  // Name of the queue to check.
  string queue = 1;

  // Request metadata for tracing.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### health_check_response.proto {#health_check_response}

**Path**: `pkg/queue/proto/health_check_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `HealthCheckResponse`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) → [metrics_1](./metrics_1.md#health_status) → [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/health_check_response.proto
// version: 1.0.0
// guid: 24f4fcb1-f84d-4f02-845d-01b9759bfb6a
//
// HealthCheckResponse for the queue module
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * HealthCheckResponse returns queue service health status.
 */
message HealthCheckResponse {
  // Overall queue service health.
  gcommon.v1.common.HealthStatus status = 1;

  // Whether the queue connection is operational.
  bool connection_ok = 2;

  // Time taken to check the queue health.
  google.protobuf.Duration response_time = 3 [lazy = true];

  // Error information if the check failed.
  gcommon.v1.common.Error error = 4 [lazy = true];
}

```

---

### import_queue_request.proto {#import_queue_request}

**Path**: `pkg/queue/proto/import_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `ImportQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/export_format.proto` → [metrics_1](./metrics_1.md#export_format) → [queue_1](./queue_1.md#export_format)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/import_queue_request.proto
// file: queue/proto/requests/import_queue_request.proto
// version: 1.0.0
// guid: 5d6e7f8a-9b0c-1d2e-3f4a-5b6c7d8e9f0a
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/export_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to import queue data from external source.
 */
message ImportQueueRequest {
  // Name of the queue to import into
  string queue_name = 1;

  // Source location for import data
  string source_path = 2;

  // Format of the import data
  gcommon.v1.queue.ExportFormat format = 3;

  // Whether to overwrite existing data
  bool overwrite = 4;

  // Whether to validate data before import
  bool validate = 5;

  // Maximum number of messages to import
  uint64 max_messages = 6;

  // Import timeout in milliseconds
  uint64 timeout_ms = 7;
}

```

---

### import_queue_response.proto {#import_queue_response}

**Path**: `pkg/queue/proto/import_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `ImportQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/import_queue_response.proto
// file: queue/proto/responses/import_queue_response.proto
// version: 1.0.0
// guid: 5d4c3b2a-1f0e-9d8c-7b6a-5e4f3a2b1c0d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response message for queue import operations.
 */
message ImportQueueResponse {
  // Unique identifier for the import operation
  string import_id = 1;

  // Whether the import was successful
  bool success = 2;

  // Error message if import failed
  string error_message = 3;

  // Number of messages imported
  uint64 imported_count = 4;

  // Number of messages that failed to import
  uint64 failed_count = 5;

  // Total number of messages processed
  uint64 total_count = 6;

  // Timestamp when import started
  google.protobuf.Timestamp start_time = 7;

  // Timestamp when import completed
  google.protobuf.Timestamp end_time = 8;

  // Import duration in milliseconds
  uint64 duration_ms = 9;

  // Import progress as percentage (0-100)
  float progress_percent = 10;
}

```

---

### list_messages_request.proto {#list_messages_request}

**Path**: `pkg/queue/proto/list_messages_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `ListMessagesRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/list_messages_request.proto
// version: 1.0.0
// Request to list messages in a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to list messages in a queue
message ListMessagesRequest {
  // Topic name
  string topic = 1;

  // Partition ID (optional, all partitions if not specified)
  int32 partition_id = 2;

  // Starting offset
  int64 start_offset = 3;

  // Maximum number of messages to return
  int32 limit = 4;

  // Include message headers
  bool include_headers = 5;

  // Include message metadata
  bool include_metadata = 6;

  // Filter by message status (optional)
  string status_filter = 7;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 8;
}

```

---

### list_messages_response.proto {#list_messages_response}

**Path**: `pkg/queue/proto/list_messages_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `ListMessagesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/list_messages_response.proto
// version: 1.0.0
// Response for listing messages

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for listing messages
message ListMessagesResponse {
  // List of messages
  repeated QueueMessage messages = 1;

  // Total number of messages available
  int64 total_count = 2;

  // Next page token for pagination
  string next_page_token = 3;

  // Whether there are more messages
  bool has_more = 4;

  // Error message if listing failed
  string error = 5;
}

```

---

### list_queues_request.proto {#list_queues_request}

**Path**: `pkg/queue/proto/list_queues_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ListQueuesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 5: Implementation needed - // user or service account. This file was a placeholder and now

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/list_queues_request.proto
// version: 1.0.0
// guid: 10aa0104-6a4e-4092-98f4-8eabba61ea69
// ListQueuesRequest retrieves available queues for the current
// user or service account. This file was a placeholder and now
// implements the request following the 1-1-1 pattern.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ListQueuesRequest {
  // Standard request metadata used across all services
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Optional page size for results
  int32 page_size = 2;

  // Optional token for fetching the next page
  string page_token = 3;
}

```

---

### list_queues_response.proto {#list_queues_response}

**Path**: `pkg/queue/proto/list_queues_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ListQueuesResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)
- `pkg/queue/proto/queue_info.proto` → [queue_2](./queue_2.md#queue_info)

#### ⚠️ Issues Found (1)

- Line 7: Implementation needed - // placeholder file generated during the migration.

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/list_queues_response.proto
// version: 1.0.0
// guid: c2ffc959-d7b5-451f-94f4-a9334e02725f

// ListQueuesResponse returns a list of queues visible to the
// requester along with pagination information. This replaces the
// placeholder file generated during the migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";
import "pkg/queue/proto/queue_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ListQueuesResponse {
  // Collection of queues
  repeated QueueInfo queues = 1;

  // Token to retrieve the next page
  string next_page_token = 2;

  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 3;
}

```

---

### list_subscriptions_request.proto {#list_subscriptions_request}

**Path**: `pkg/queue/proto/list_subscriptions_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListSubscriptionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 5: Implementation needed - // Previously a placeholder, this file now contains the full request definition.

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/list_subscriptions_request.proto
// version: 1.0.0
// guid: 781a6513-601b-4ef8-87bf-7c881f4b8a79
// ListSubscriptionsRequest returns subscriptions for a given topic or queue.
// Previously a placeholder, this file now contains the full request definition.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ListSubscriptionsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Name of the topic or queue to list subscriptions for
  string parent = 2;

  // Optional page size
  int32 page_size = 3;

  // Optional page token
  string page_token = 4;
}

```

---

### list_subscriptions_response.proto {#list_subscriptions_response}

**Path**: `pkg/queue/proto/list_subscriptions_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ListSubscriptionsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)
- `pkg/queue/proto/subscription_info.proto` → [common](./common.md#subscription_info) → [queue_2](./queue_2.md#subscription_info)

#### ⚠️ Issues Found (1)

- Line 7: Implementation needed - // rather than acting as a placeholder.

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/list_subscriptions_response.proto
// version: 1.0.0
// guid: c20dc6c8-336b-4626-b709-22be9663d29d

// ListSubscriptionsResponse contains the subscriptions under a
// specific topic or queue. This file now implements the message
// rather than acting as a placeholder.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";
import "pkg/queue/proto/subscription_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ListSubscriptionsResponse {
  // Subscriptions returned
  repeated SubscriptionInfo subscriptions = 1;

  // Token for fetching the next page
  string next_page_token = 2;

  // Response metadata common across services
  gcommon.v1.common.ResponseMetadata metadata = 3;
}

```

---

### list_topics_request.proto {#list_topics_request}

**Path**: `pkg/queue/proto/list_topics_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `ListTopicsRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/list_topics_request.proto
// version: 1.1.0
// Request to list available topics in the queue system

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ListTopicsRequest retrieves a list of available topics
message ListTopicsRequest {
  // Filter topics by name pattern (supports wildcards)
  string name_pattern = 1;

  // Filter topics by namespace/category
  string namespace = 2;

  // Include topic metadata in response
  bool include_metadata = 3;

  // Include topic statistics in response
  bool include_stats = 4;

  // Maximum number of topics to return
  int32 limit = 5;

  // Pagination token for continued listing
  string page_token = 6;

  // Sort topics by specified field (name, created_at, message_count)
  string sort_by = 7;

  // Sort order (asc, desc)
  string sort_order = 8;

  // Filter by topic state (active, paused, deleted)
  repeated string topic_states = 9;

  // Include only topics user has access to
  bool access_check = 10;

  // Additional filter criteria
  map<string, string> filters = 11;
}

```

---

### list_topics_response.proto {#list_topics_response}

**Path**: `pkg/queue/proto/list_topics_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ListTopicsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/topic_info.proto` → [queue_2](./queue_2.md#topic_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/list_topics_response.proto
// version: 1.1.0
// Response containing list of available topics

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/topic_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message ListTopicsResponse {
  // List of topics
  repeated TopicInfo topics = 1;

  // Next page token
  string next_page_token = 2;

  // Total count
  int32 total_count = 3;
}

// ListTopicsResponse returns a list of available topics
// This file needs proper implementation

```

---

### migrate_queue_request.proto {#migrate_queue_request}

**Path**: `pkg/queue/proto/migrate_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `MigrateQueueRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/migrate_queue_request.proto
// version: 1.0.0
// Request to migrate a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to migrate a queue to a new location
message MigrateQueueRequest {
  // Source queue name to migrate from
  string source_queue = 1;

  // Destination queue name to migrate to
  string destination_queue = 2;

  // Destination endpoint/server
  string destination_endpoint = 3;

  // Whether to preserve message ordering
  bool preserve_order = 4;

  // Whether to verify data integrity after migration
  bool verify_integrity = 5;

  // Maximum migration duration (milliseconds)
  int32 max_duration_ms = 6;

  // Batch size for migration
  int32 batch_size = 7;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 8;
}

```

---

### migrate_queue_response.proto {#migrate_queue_response}

**Path**: `pkg/queue/proto/migrate_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `MigrateQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/migrate_queue_response.proto
// version: 1.0.0
// Response for queue migration operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue migration operations
message MigrateQueueResponse {
  // Whether the migration was successful
  bool success = 1;

  // New queue location/endpoint
  string new_queue_endpoint = 2;

  // Number of messages migrated
  int64 messages_migrated = 3;

  // Migration duration (milliseconds)
  int32 migration_duration_ms = 4;

  // Source queue name
  string source_queue = 5;

  // Destination queue name
  string destination_queue = 6;

  // Error message if migration failed
  string error = 7;
}

```

---

### nack_request.proto {#nack_request}

**Path**: `pkg/queue/proto/nack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `NackRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/nack_error.proto` → [queue_1](./queue_1.md#nack_error)

#### Source Code

```protobuf
// file: pkg/queue/proto/nack_request.proto
// version: 1.1.0
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/nack_error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to negatively acknowledge (NACK) a message.
 * This indicates that the message could not be processed and may need to be requeued.
 */
message NackRequest {
  // Acknowledgment token received with the message
  string ack_token = 1;

  // Whether the message should be requeued for retry
  bool requeue = 2;

  // Reason for the negative acknowledgment
  string reason = 3;

  // Error details if processing failed
  NackError error = 4;

  // Delay before requeuing (if requeue is true)
  int64 requeue_delay_seconds = 5;

  // Maximum number of retry attempts for this message
  int32 max_retries = 6;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}

```

---

### nack_response.proto {#nack_response}

**Path**: `pkg/queue/proto/nack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `NackResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/nack_response.proto
// version: 1.0.0
// Response for negative acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for negative acknowledgment operations
message NackResponse {
  // Whether the nack was successful
  bool success = 1;

  // Error message if nack failed
  string error = 2;

  // Message ID that was nacked
  string message_id = 3;

  // Timestamp when nack was processed
  int64 timestamp = 4;
}

```

---

### pause_queue_request.proto {#pause_queue_request}

**Path**: `pkg/queue/proto/pause_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PauseQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/pause_queue_request.proto
// version: 1.0.0
// guid: a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to pause a queue.
 * Stops message processing while keeping messages in the queue.
 */
message PauseQueueRequest {
  // Name of the queue to pause
  string queue_name = 1;

  // Reason for pausing the queue
  string reason = 2;

  // Whether to wait for current messages to finish processing
  bool graceful = 3;

  // Timeout for graceful pause (milliseconds)
  int32 timeout_ms = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;

  // Whether to pause specific partitions only
  repeated int32 partition_ids = 6;
}

```

---

### pause_queue_response.proto {#pause_queue_response}

**Path**: `pkg/queue/proto/pause_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PauseQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/pause_queue_response.proto
// version: 1.0.0
// Response for queue pause operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue pause operations
message PauseQueueResponse {
  // Whether the pause was successful
  bool success = 1;

  // Queue name that was paused
  string queue_name = 2;

  // Current pause status
  string pause_status = 3;

  // Number of active consumers affected
  int32 affected_consumers = 4;

  // Timestamp when pause took effect
  int64 pause_timestamp = 5;

  // Error message if pause failed
  string error = 6;
}

```

---

### peek_request.proto {#peek_request}

**Path**: `pkg/queue/proto/peek_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 97

**Messages** (1): `PeekRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/peek_request.proto
// version: 1.0.0
// guid: 1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
// Standard imports

// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * PeekRequest allows viewing messages in a queue without removing them.
 * Useful for inspection, monitoring, and debugging queue contents
 * without affecting message processing.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message PeekRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue to peek into.
   * Must be a valid existing queue.
   */
  string queue_name = 1;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Maximum number of messages to peek at.
   * Range: 1-100. Default: 1.
   */
  int32 max_messages = 12;

  /**
   * Starting position in the queue for peeking.
   * 0 = first message, 1 = second message, etc.
   * Default: 0 (peek at head of queue).
   */
  int32 start_position = 13;

  /**
   * Message group ID filter. If specified, only messages
   * from this group will be returned.
   */
  string group_id_filter = 14;

  /**
   * Attribute filters for selective message viewing.
   * Only messages matching all specified attributes will be returned.
   */
  map<string, string> attribute_filters = 15;

  /**
   * Message type filter. If specified, only messages of
   * this type will be returned.
   */
  string message_type_filter = 16;

  /**
   * Priority threshold - only return messages with priority
   * greater than or equal to this value. Range: 0-255.
   */
  int32 min_priority = 17;

  /**
   * Include message content/payload in the response.
   * Default: true. Set to false to only get metadata.
   */
  bool include_payload = 18;

  /**
   * Include message attributes in the response.
   * Default: true. Set to false to reduce response size.
   */
  bool include_attributes = 19;

  /**
   * Include detailed delivery metadata (timestamps, delivery count, etc.).
   * Default: false for performance.
   */
  bool include_delivery_metadata = 20;
}

```

---

### peek_response.proto {#peek_response}

**Path**: `pkg/queue/proto/peek_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 123

**Messages** (1): `PeekResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/peek_response.proto
// version: 1.0.0
// guid: 2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";
// Queue message types
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * PeekResponse returns messages viewed from a queue without removing them.
 * Contains message data and metadata for inspection purposes
 * without affecting the queue state.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message PeekResponse {
  // Required fields (1-10)

  /**
   * Messages viewed from the queue.
   * Empty if no messages were found matching the criteria.
   */
  repeated gcommon.v1.queue.QueueMessage messages = 1;

  /**
   * Indicates whether the peek operation was successful.
   */
  bool success = 2;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue that was peeked.
   * Echoed from the request for verification.
   */
  string queue_name = 12;

  /**
   * Total number of messages that matched the peek criteria.
   * May be larger than the number of messages returned due to max_messages limit.
   */
  int32 total_matching_messages = 13;

  /**
   * Approximate total number of messages currently in the queue.
   * Useful for monitoring and capacity planning.
   */
  int64 approximate_queue_size = 14;

  /**
   * Position in the queue where peeking started.
   * Echoed from the request for verification.
   */
  int32 start_position = 15;

  /**
   * Position in the queue where peeking ended.
   * Helpful for subsequent peek operations.
   */
  int32 end_position = 16;

  /**
   * Whether there are more messages available beyond the returned set.
   * True if total_matching_messages > returned messages count.
   */
  bool has_more_messages = 17;

  /**
   * Number of messages that were skipped due to filters.
   * Useful for understanding filter effectiveness.
   */
  int32 filtered_message_count = 18;

  /**
   * Oldest message timestamp in the peeked set.
   * Useful for understanding queue age/staleness.
   */
  google.protobuf.Timestamp oldest_message_time = 19;

  /**
   * Newest message timestamp in the peeked set.
   */
  google.protobuf.Timestamp newest_message_time = 20;

  // Status and error fields (61-70)

  /**
   * Error information if the peek operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the peek operation was performed.
   */
  google.protobuf.Timestamp peeked_at = 51;

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}

```

---

### publish_request.proto {#publish_request}

**Path**: `pkg/queue/proto/publish_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `PublishRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/delivery_options.proto` → [queue_1](./queue_1.md#delivery_options)
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/publish_request.proto
// version: 1.0.0
// guid: 59dc8120-bc2f-4d56-a9f1-f0957cb9bafb
// PublishRequest publishes a single message to a named topic. It is
// used for pub/sub style messaging where consumers subscribe to
// topics rather than specific queues.
// PublishRequest contains all information required to publish a
// message to a topic.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/delivery_options.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message PublishRequest {
  // Name of the topic to publish to.
  string topic_name = 1;

  // Message to publish.
  QueueMessage message = 2;

  // Optional delivery parameters controlling retries and delays.
  DeliveryOptions delivery_options = 3;

  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### publish_response.proto {#publish_response}

**Path**: `pkg/queue/proto/publish_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `PublishResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/publish_response.proto
// version: 1.0.0
// guid: 8b12b279-f7c6-40fe-9147-4a663fb0c9c6

// PublishResponse reports the outcome of publishing a message to a
// topic.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// PublishResponse contains the identifier of the published message
// and success status.
message PublishResponse {
  // Unique identifier of the message as stored by the broker.
  string message_id = 1;

  // Whether the publish operation succeeded.
  bool success = 2;

  // Error information when success is false.
  gcommon.v1.common.Error error = 3;

  // Request metadata echoed back for tracing.
  gcommon.v1.common.RequestMetadata request_metadata = 4;
}

```

---

### pull_request.proto {#pull_request}

**Path**: `pkg/queue/proto/pull_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `PullRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // placeholder generated during migration.

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/pull_request.proto
// version: 1.0.0
// guid: dae5ea8a-77c7-4b90-ab25-d2981ba423df
// PullRequest retrieves a single message from the specified queue
// without establishing a subscription. This file replaces the
// placeholder generated during migration.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message PullRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Queue to pull from
  string queue_name = 2;

  // Optional visibility timeout for the pulled message
  int32 visibility_timeout_seconds = 3;
}

```

---

### pull_response.proto {#pull_response}

**Path**: `pkg/queue/proto/pull_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `PullResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)
- `pkg/queue/proto/received_message.proto` → [queue_2](./queue_2.md#received_message)

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // now contains the actual response definition instead of a placeholder.

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/pull_response.proto
// version: 1.0.0
// guid: 5c55b3fd-beda-4758-90c9-2084f2d6ea8f

// PullResponse returns a message pulled from the queue. This file
// now contains the actual response definition instead of a placeholder.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";
import "pkg/queue/proto/received_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message PullResponse {
  // The received message. May be null if no message was available.
  ReceivedMessage message = 1;

  // Response metadata including error details
  gcommon.v1.common.ResponseMetadata metadata = 2;
}

```

---

### purge_request.proto {#purge_request}

**Path**: `pkg/queue/proto/purge_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 62

**Messages** (2): `PurgeRequest`, `PurgeOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/purge_request.proto
// file: queue/proto/requests/purge_request.proto
// version: 1.0.0
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to purge (delete) messages from a queue.
 * Can purge all messages or selectively based on criteria.
 */
message PurgeRequest {
  // Name of the queue to purge
  string queue_name = 1;

  // Purge options
  PurgeOptions options = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}

/**
 * Options for purging messages from a queue.
 */
message PurgeOptions {
  // Whether to purge all messages (if true, other filters are ignored)
  bool purge_all = 1;

  // Purge messages older than this timestamp
  google.protobuf.Timestamp older_than = 2;

  // Purge messages with specific headers (all headers must match)
  map<string, string> header_filters = 3;

  // Purge messages with priority below this value
  int32 priority_below = 4;

  // Purge messages with priority above this value
  int32 priority_above = 5;

  // Maximum number of messages to purge (0 = no limit)
  int64 max_messages = 6;

  // Whether to purge only failed/undeliverable messages
  bool only_failed = 7;

  // Whether to purge only expired messages
  bool only_expired = 8;
}

```

---

### purge_response.proto {#purge_response}

**Path**: `pkg/queue/proto/purge_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PurgeResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/purge_response.proto
// version: 1.0.0
// Response for queue purge operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue purge operations
message PurgeResponse {
  // Whether the purge was successful
  bool success = 1;

  // Number of messages purged
  int64 messages_purged = 2;

  // Number of bytes freed
  int64 bytes_freed = 3;

  // Purge duration (milliseconds)
  int32 purge_duration_ms = 4;

  // Partitions that were purged
  repeated int32 purged_partitions = 5;

  // Error message if purge failed
  string error = 6;
}

```

---

### push_request.proto {#push_request}

**Path**: `pkg/queue/proto/push_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 154

**Messages** (6): `PushRequest`, `Message`, `MessageProperties`, `RoutingInfo`, `PublishConfig`, `BatchSettings`

**Imports** (7):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/delivery_mode.proto` → [queue_1](./queue_1.md#delivery_mode)
- `pkg/queue/proto/message_metadata.proto` → [queue_1](./queue_1.md#message_metadata)
- `pkg/queue/proto/priority_level.proto` → [queue_1](./queue_1.md#priority_level)
- `pkg/queue/proto/retry_config.proto` → [queue_config](./queue_config.md#retry_config)

#### Source Code

```protobuf
// file: pkg/queue/proto/push_request.proto
// version: 1.1.0
// Request to push/publish messages to a queue or topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/delivery_mode.proto";
import "pkg/queue/proto/message_metadata.proto";
import "pkg/queue/proto/priority_level.proto";
import "pkg/queue/proto/retry_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// PushRequest publishes one or more messages to a queue or topic
message PushRequest {
  // Target topic or queue identifier
  string topic = 1;

  // Messages to publish
  repeated Message messages = 2;

  // Publishing configuration
  PublishConfig publish_config = 3;

  // Batch publishing settings
  BatchSettings batch_settings = 4;

  // Transaction ID for transactional publishing
  string transaction_id = 5;

  // Producer ID for message tracking
  string producer_id = 6;

  // Publishing metadata
  map<string, string> metadata = 7;
}

// Individual message to be published
message Message {
  // Message payload
  google.protobuf.Any payload = 1;

  // Message headers
  map<string, string> headers = 2;

  // Message properties
  MessageProperties properties = 3;

  // Routing information
  RoutingInfo routing_info = 4;

  // Message metadata - references existing MessageMetadata
  MessageMetadata message_metadata = 5;
}

// Message properties and configuration
message MessageProperties {
  // Message priority level
  PriorityLevel priority = 1;

  // Delivery mode for the message
  DeliveryMode delivery_mode = 2;

  // Message expiration time
  google.protobuf.Timestamp expiration_time = 3;

  // Correlation ID for request-response patterns
  string correlation_id = 4;

  // Reply-to address/topic
  string reply_to = 5;

  // Content type of the payload
  string content_type = 6;

  // Content encoding
  string content_encoding = 7;

  // Compression applied to payload
  string compression = 8;

  // Message deduplication ID
  string deduplication_id = 9;

  // Delay before message becomes available (milliseconds)
  int64 delivery_delay_ms = 10;
}

// Message routing information
message RoutingInfo {
  // Routing key for topic-based routing
  string routing_key = 1;

  // Specific partition ID (if applicable)
  int32 partition_id = 2;

  // Partition key for automatic partitioning
  string partition_key = 3;

  // Exchange name (for exchange-based routing)
  string exchange_name = 4;

  // Routing tags for advanced routing
  repeated string routing_tags = 5;
}

// Publishing configuration
message PublishConfig {
  // Wait for acknowledgment before returning
  bool wait_for_ack = 1;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 2;

  // Enable duplicate detection
  bool duplicate_detection = 3;

  // Compression for message batch
  bool enable_compression = 4;

  // Enable message ordering
  bool enable_ordering = 5;

  // Retry configuration for failed publishes - references existing RetryConfig
  RetryConfig retry_config = 6;

  // Persistence level required
  string persistence_level = 7;
}

// Batch publishing settings
message BatchSettings {
  // Enable batch publishing
  bool enabled = 1;

  // Maximum messages per batch
  int32 max_batch_size = 2;

  // Maximum batch size in bytes
  int64 max_batch_bytes = 3;

  // Maximum time to wait for batch completion (milliseconds)
  int32 batch_timeout_ms = 4;

  // Flush batch on publish request completion
  bool flush_on_complete = 5;
}

```

---

### push_response.proto {#push_response}

**Path**: `pkg/queue/proto/push_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PushResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/push_response.proto
// file: queue/proto/responses/push_response.proto
// version: 1.0.0
// guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for message publishing operations.
 */
message PushResponse {
  // Unique identifier assigned to the published message
  string message_id = 1;

  // Timestamp when the message was accepted by the queue
  google.protobuf.Timestamp accepted_at = 2;

  // Position/offset of the message in the queue
  int64 message_offset = 3;

  // Current queue depth after the message was added
  int64 queue_depth = 4;

  // Whether the message was persisted to storage
  bool persisted = 5;

  // Estimated delivery time (for delayed messages)
  google.protobuf.Timestamp estimated_delivery_time = 6;
}
// This file needs proper implementation

```

---

### reset_queue_stats_request.proto {#reset_queue_stats_request}

**Path**: `pkg/queue/proto/reset_queue_stats_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ResetQueueStatsRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/reset_queue_stats_request.proto
// version: 1.0.0
// Request to reset queue statistics

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to reset queue statistics
message ResetQueueStatsRequest {
  // Queue name to reset stats for
  string queue_name = 1;

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

**Path**: `pkg/queue/proto/reset_queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 98

**Messages** (3): `ResetQueueStatsResponse`, `PreservedStats`, `ResetDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/reset_queue_stats_response.proto
// version: 1.1.0
// Response to queue statistics reset operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ResetQueueStatsResponse returns the result of resetting queue statistics
message ResetQueueStatsResponse {
  // Success status of the reset operation
  bool success = 1;

  // Queue identifier whose stats were reset
  string queue_id = 2;

  // Timestamp when reset operation completed
  google.protobuf.Timestamp reset_at = 3;

  // Statistics that were preserved before reset
  PreservedStats preserved_stats = 4;

  // Types of statistics that were reset
  repeated string reset_stat_types = 5;

  // Types of statistics that were preserved
  repeated string preserved_stat_types = 6;

  // Error message if reset failed
  string error_message = 7;

  // Error code for programmatic handling
  string error_code = 8;

  // Warning messages about the reset operation
  repeated string warnings = 9;

  // Reset operation details
  ResetDetails reset_details = 10;

  // Operation metadata
  map<string, string> metadata = 11;
}

// Statistics that were preserved during reset
message PreservedStats {
  // Total message count (lifetime)
  int64 lifetime_message_count = 1;

  // Queue creation timestamp
  google.protobuf.Timestamp created_at = 2;

  // Last configuration change timestamp
  google.protobuf.Timestamp last_config_change = 3;

  // Peak message count (historical high)
  int64 peak_message_count = 4;

  // Peak throughput (historical high)
  double peak_throughput = 5;

  // Total uptime (milliseconds)
  int64 total_uptime_ms = 6;
}

// Details about the reset operation
message ResetDetails {
  // Number of metrics reset
  int32 metrics_reset_count = 1;

  // Number of counters reset
  int32 counters_reset_count = 2;

  // Number of histograms reset
  int32 histograms_reset_count = 3;

  // Number of partitions affected
  int32 partitions_affected = 4;

  // Time taken to complete reset (milliseconds)
  int64 reset_duration_ms = 5;

  // Whether reset was partial or complete
  bool partial_reset = 6;

  // Reason for reset operation
  string reset_reason = 7;

  // User or system that initiated reset
  string initiated_by = 8;
}

```

---

### restore_queue_request.proto {#restore_queue_request}

**Path**: `pkg/queue/proto/restore_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 170

**Messages** (7): `RestoreQueueRequest`, `BackupSource`, `OriginalQueueInfo`, `EncryptionInfo`, `RestoreOptions`, `FilterCriteria`, `PerformanceOptions`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/restore_config.proto` → [queue_config](./queue_config.md#restore_config)
- `pkg/queue/proto/restore_queue_response.proto`
- `pkg/queue/proto/time_range.proto` → [common](./common.md#time_range) → [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/queue/proto/restore_queue_request.proto
// version: 1.1.0
// Request to restore queue from backup

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/restore_config.proto";
import "pkg/queue/proto/restore_queue_response.proto";
import "pkg/queue/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// RestoreQueueRequest initiates restoration of a queue from backup
message RestoreQueueRequest {
  // Target queue identifier for restoration
  string target_queue_id = 1;

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
  repeated int32 partition_ids = 7;

  // Restore options
  RestoreOptions options = 8;

  // Operation metadata
  map<string, string> metadata = 9;
}

// Backup source configuration
message BackupSource {
  // Backup identifier
  string backup_id = 1;

  // Backup location/path
  string backup_path = 2;

  // Backup storage type (s3, gcs, local, etc.)
  string storage_type = 3;

  // Storage credentials
  map<string, string> credentials = 4;

  // Backup creation timestamp
  google.protobuf.Timestamp backup_timestamp = 5;

  // Original queue information
  OriginalQueueInfo original_queue = 6;

  // Backup format version
  string backup_version = 7;

  // Backup compression format
  string compression_format = 8;

  // Backup encryption details
  EncryptionInfo encryption = 9;
}

// Original queue information from backup
message OriginalQueueInfo {
  // Original queue ID
  string queue_id = 1;

  // Original queue name
  string queue_name = 2;

  // Original partition count
  int32 partition_count = 3;

  // Original configuration snapshot
  map<string, string> config_snapshot = 4;

  // Backup creation point
  google.protobuf.Timestamp backup_point = 5;
}

// Backup encryption information
message EncryptionInfo {
  // Encryption enabled
  bool enabled = 1;

  // Encryption algorithm
  string algorithm = 2;

  // Key management service
  string kms_provider = 3;

  // Key identifier
  string key_id = 4;
}

// Restore operation options
message RestoreOptions {
  // Skip message content (restore structure only)
  bool skip_message_content = 1;

  // Restore message metadata only
  bool metadata_only = 2;

  // Maximum number of messages to restore
  int64 max_messages = 3;

  // Restore messages from specific offset range
  OffsetRange offset_range = 4;

  // Restore messages within time range
  TimeRange time_range = 5;

  // Restore specific message priorities
  repeated int32 priority_levels = 6;

  // Include/exclude patterns for message filtering
  FilterCriteria filter_criteria = 7;

  // Performance tuning options
  PerformanceOptions performance = 8;
}

// Message filtering criteria
message FilterCriteria {
  // Include message patterns
  repeated string include_patterns = 1;

  // Exclude message patterns
  repeated string exclude_patterns = 2;

  // Header-based filters
  map<string, string> header_filters = 3;

  // Content-type filters
  repeated string content_types = 4;
}

// Performance tuning options
message PerformanceOptions {
  // Parallel restore workers
  int32 worker_count = 1;

  // Batch size for restore operations
  int32 batch_size = 2;

  // Buffer size for reading backup data
  int32 buffer_size_mb = 3;

  // Compression during restore
  bool enable_compression = 4;

  // Throttle restore rate (messages/second)
  int32 throttle_rate = 5;
}

```

---

### restore_queue_response.proto {#restore_queue_response}

**Path**: `pkg/queue/proto/restore_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 276

**Messages** (12): `RestoreQueueResponse`, `RestoreStatistics`, `RestoreStatus`, `RestoreError`, `RestoreWarning`, `PartitionRestoreResult`, `ValidationResult`, `ChecksumValidation`, `SchemaValidation`, `IntegrityValidation`,
`ValidationError`, `OffsetRange`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/restore_queue_response.proto
// version: 1.1.0
// Response to queue restoration operation

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// RestoreQueueResponse returns the result of a queue restoration operation
message RestoreQueueResponse {
  // Operation success status
  bool success = 1;

  // Restore operation ID for tracking
  string operation_id = 2;

  // Restored queue identifier
  string restored_queue_id = 3;

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
  repeated RestoreError errors = 9;

  // Warnings generated during restore
  repeated RestoreWarning warnings = 10;

  // Partition restoration results
  repeated PartitionRestoreResult partition_results = 11;

  // Validation results if validation was requested
  ValidationResult validation_result = 12;

  // Operation metadata
  map<string, string> metadata = 13;
}

// Statistics about the restoration operation
message RestoreStatistics {
  // Total messages restored
  int64 messages_restored = 1;

  // Total bytes restored
  int64 bytes_restored = 2;

  // Number of partitions restored
  int32 partitions_restored = 3;

  // Messages skipped due to filters
  int64 messages_skipped = 4;

  // Messages failed to restore
  int64 messages_failed = 5;

  // Average restore rate (messages/second)
  double restore_rate = 6;

  // Throughput (bytes/second)
  double throughput_bps = 7;

  // Backup file size processed
  int64 backup_size_bytes = 8;

  // Compression ratio achieved
  double compression_ratio = 9;
}

// Current status of the restoration operation
message RestoreStatus {
  // Status code (pending, in_progress, completed, failed, cancelled)
  string status_code = 1;

  // Human-readable status message
  string status_message = 2;

  // Progress percentage (0-100)
  int32 progress_percentage = 3;

  // Current operation phase
  string current_phase = 4;

  // Estimated time remaining
  google.protobuf.Duration estimated_remaining = 5;

  // Last status update timestamp
  google.protobuf.Timestamp last_update = 6;
}

// Error information from restoration
message RestoreError {
  // Error code for programmatic handling
  string error_code = 1;

  // Human-readable error message
  string error_message = 2;

  // Error category (validation, io, corruption, etc.)
  string error_category = 3;

  // Specific component that failed
  string failed_component = 4;

  // Partition ID if error is partition-specific
  int32 partition_id = 5;

  // Message offset range affected by error
  OffsetRange affected_range = 6;

  // Error timestamp
  google.protobuf.Timestamp error_time = 7;

  // Whether error is recoverable
  bool recoverable = 8;
}

// Warning information from restoration
message RestoreWarning {
  // Warning code
  string warning_code = 1;

  // Warning message
  string warning_message = 2;

  // Warning category
  string warning_category = 3;

  // Affected component
  string affected_component = 4;

  // Partition ID if warning is partition-specific
  int32 partition_id = 5;

  // Warning timestamp
  google.protobuf.Timestamp warning_time = 6;
}

// Result of restoring a specific partition
message PartitionRestoreResult {
  // Partition ID
  int32 partition_id = 1;

  // Success status for this partition
  bool success = 2;

  // Messages restored in this partition
  int64 messages_restored = 3;

  // Bytes restored in this partition
  int64 bytes_restored = 4;

  // Start offset restored
  int64 start_offset = 5;

  // End offset restored
  int64 end_offset = 6;

  // Partition restore duration
  google.protobuf.Duration restore_duration = 7;

  // Any partition-specific errors
  repeated RestoreError partition_errors = 8;

  // Partition metadata
  map<string, string> partition_metadata = 9;
}

// Backup validation results
message ValidationResult {
  // Validation success status
  bool validation_passed = 1;

  // Checksum verification results
  ChecksumValidation checksum_validation = 2;

  // Schema validation results
  SchemaValidation schema_validation = 3;

  // Data integrity validation
  IntegrityValidation integrity_validation = 4;

  // Validation errors found
  repeated ValidationError validation_errors = 5;

  // Validation duration
  google.protobuf.Duration validation_duration = 6;
}

// Checksum validation details
message ChecksumValidation {
  // Overall checksum validation passed
  bool passed = 1;

  // Expected checksum
  string expected_checksum = 2;

  // Actual checksum
  string actual_checksum = 3;

  // Checksum algorithm used
  string checksum_algorithm = 4;
}

// Schema validation details
message SchemaValidation {
  // Schema validation passed
  bool passed = 1;

  // Schema version in backup
  string backup_schema_version = 2;

  // Current schema version
  string current_schema_version = 3;

  // Schema compatibility status
  string compatibility_status = 4;
}

// Data integrity validation details
message IntegrityValidation {
  // Integrity validation passed
  bool passed = 1;

  // Corrupted message count
  int64 corrupted_messages = 2;

  // Missing message count
  int64 missing_messages = 3;

  // Duplicate message count
  int64 duplicate_messages = 4;
}

// Validation error details
message ValidationError {
  // Error type
  string error_type = 1;

  // Error description
  string description = 2;

  // Affected partition
  int32 partition_id = 3;

  // Affected offset range
  OffsetRange affected_range = 4;
}

// Offset range specification
message OffsetRange {
  // Start offset
  int64 start_offset = 1;

  // End offset
  int64 end_offset = 2;
}

```

---

### resume_queue_request.proto {#resume_queue_request}

**Path**: `pkg/queue/proto/resume_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `ResumeQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/resume_queue_request.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to resume a paused queue.
 * Restarts message processing for a previously paused queue.
 */
message ResumeQueueRequest {
  // Name of the queue to resume
  string queue_name = 1;

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

**Path**: `pkg/queue/proto/resume_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 78

**Messages** (2): `ResumeQueueResponse`, `ResumeStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/queue_state.proto` → [queue_2](./queue_2.md#queue_state)

#### Source Code

```protobuf
// file: pkg/queue/proto/resume_queue_response.proto
// version: 1.1.0
// Response to queue resume operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/queue_state.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ResumeQueueResponse returns the result of resuming a paused queue
message ResumeQueueResponse {
  // Success status of the resume operation
  bool success = 1;

  // Queue identifier that was resumed
  string queue_id = 2;

  // Previous queue state before resume
  QueueState previous_state = 3;

  // Current queue state after resume
  QueueState current_state = 4;

  // Timestamp when resume operation completed
  google.protobuf.Timestamp resumed_at = 5;

  // Duration the queue was paused (milliseconds)
  int64 pause_duration_ms = 6;

  // Messages that were queued during pause
  int64 messages_queued_during_pause = 7;

  // Consumer groups affected by resume
  repeated string affected_consumer_groups = 8;

  // Error message if resume failed
  string error_message = 9;

  // Error code for programmatic handling
  string error_code = 10;

  // Warning messages about resume operation
  repeated string warnings = 11;

  // Resume operation statistics
  ResumeStats resume_stats = 12;

  // Operation metadata
  map<string, string> metadata = 13;
}

// Statistics about the resume operation
message ResumeStats {
  // Number of partitions resumed
  int32 partitions_resumed = 1;

  // Number of subscriptions reactivated
  int32 subscriptions_reactivated = 2;

  // Number of consumers reconnected
  int32 consumers_reconnected = 3;

  // Time taken to complete resume (milliseconds)
  int64 resume_time_ms = 4;

  // Messages processed immediately after resume
  int64 immediate_messages_processed = 5;

  // Throughput after resume (messages/second)
  double post_resume_throughput = 6;
}

```

---

### seek_request.proto {#seek_request}

**Path**: `pkg/queue/proto/seek_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `SeekRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/seek_request.proto
// file: queue/proto/requests/seek_request.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to seek to a specific position in a queue or topic.
 * Used for replaying messages from a particular point in time or offset.
 */
message SeekRequest {
  // Name of the queue or topic to seek within
  string queue_name = 1;

  // Subscription name (for topics with multiple subscribers)
  string subscription_name = 2;

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

**Path**: `pkg/queue/proto/seek_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `SeekResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/seek_response.proto
// version: 1.0.0
// guid: d1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for seek operations on a queue.
 * Contains the result of attempting to seek to a specific position.
 */
message SeekResponse {
  // Whether the seek operation was successful
  bool success = 1;

  // The actual position seeked to
  int64 position = 2;

  // The offset within the partition (for partitioned queues)
  int64 offset = 3;

  // The partition ID (for partitioned queues)
  int32 partition_id = 4;

  // Error message if seek failed
  string error_message = 5;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 6;
}

```

---

### send_message_request.proto {#send_message_request}

**Path**: `pkg/queue/proto/send_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `SendMessageRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/delivery_options.proto` → [queue_1](./queue_1.md#delivery_options)
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: queue/proto/requests/send_message_request.proto
// version: 1.0.0
// guid: 0acd1eb1-8464-4f9c-8fd2-0562acde190f
// SendMessageRequest sends a single message to a queue.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/delivery_options.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message SendMessageRequest {
  // Name of the target queue.
  string queue_name = 1;

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

**Path**: `pkg/queue/proto/send_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `SendMessageResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: queue/proto/responses/send_message_response.proto
// version: 1.0.0
// guid: 2bbac133-fc81-4653-a03a-e5227ae81d4e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// SendMessageResponse contains the result of a send operation.
message SendMessageResponse {
  // Identifier of the queued message.
  string message_id = 1;

  // Whether the send operation succeeded.
  bool success = 2;

  // Position in the queue if known.
  int64 queue_position = 3;

  // Error information when `success` is false.
  gcommon.v1.common.Error error = 4;
}

```

---

### stream_messages_request.proto {#stream_messages_request}

**Path**: `pkg/queue/proto/stream_messages_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 113

**Messages** (4): `StreamMessagesRequest`, `OffsetConfig`, `MessageFilter`, `FlowControlConfig`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/ack_level.proto` → [queue_1](./queue_1.md#ack_level)
- `pkg/queue/proto/offset_type.proto` → [queue_1](./queue_1.md#offset_type)
- `pkg/queue/proto/stream_config.proto` → [queue_config](./queue_config.md#stream_config)

#### Source Code

```protobuf
// file: pkg/queue/proto/stream_messages_request.proto
// version: 1.1.0
// Request to stream messages from a queue or topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/ack_level.proto";
import "pkg/queue/proto/offset_type.proto";
import "pkg/queue/proto/stream_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// StreamMessagesRequest initiates a message stream from a queue or topic
message StreamMessagesRequest {
  // Topic or queue identifier to stream from
  string topic = 1;

  // Consumer group ID for coordinated consumption
  string consumer_group_id = 2;

  // Individual consumer ID within the group
  string consumer_id = 3;

  // Starting offset configuration
  OffsetConfig offset_config = 4;

  // Maximum number of messages to stream
  int64 max_messages = 5;

  // Maximum time to keep stream open (milliseconds)
  int32 stream_timeout_ms = 6;

  // Acknowledgment level required
  AckLevel ack_level = 7;

  // Batch size for message delivery
  int32 batch_size = 8;

  // Message filter criteria
  MessageFilter filter = 9;

  // Auto-acknowledge messages after delivery
  bool auto_acknowledge = 10;

  // Pause stream on error
  bool pause_on_error = 11;

  // Include message metadata in stream
  bool include_metadata = 12;

  // Specific partition IDs to stream from (empty = all partitions)
  repeated int32 partition_ids = 13;

  // Stream configuration options
  StreamConfig stream_config = 14;
}

// Offset configuration for stream starting point
message OffsetConfig {
  // Offset type (earliest, latest, timestamp, specific)
  OffsetType offset_type = 1;

  // Specific offset value (when offset_type = specific)
  int64 offset_value = 2;

  // Timestamp to start from (when offset_type = timestamp)
  google.protobuf.Timestamp start_timestamp = 3;

  // Reset to beginning if offset not found
  bool reset_on_not_found = 4;
}

// Message filtering criteria
message MessageFilter {
  // Filter by message headers
  map<string, string> header_filters = 1;

  // Filter by message properties
  map<string, string> property_filters = 2;

  // Minimum message priority
  int32 min_priority = 3;

  // Maximum message age (seconds)
  int32 max_age_seconds = 4;

  // Content type filter
  string content_type = 5;

  // Custom filter expression
  string filter_expression = 6;
}

// Flow control configuration
message FlowControlConfig {
  // Enable flow control
  bool enabled = 1;

  // Maximum outstanding messages
  int32 max_outstanding_messages = 2;

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 3;

  // Flow control algorithm (token_bucket, leaky_bucket, sliding_window)
  string algorithm = 4;
}

```

---

### stream_messages_response.proto {#stream_messages_response}

**Path**: `pkg/queue/proto/stream_messages_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `StreamMessagesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/stream_messages_response.proto
// file: queue/proto/responses/stream_messages_response.proto
// version: 1.0.0
// guid: 4c5d6e7f-8a9b-0c1d-2e3f-4a5b6c7d8e9f
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for streaming messages from a queue.
 */
message StreamMessagesResponse {
  // List of messages in the stream
  repeated gcommon.v1.queue.QueueMessage messages = 1;

  // Whether there are more messages available
  bool has_more = 2;

  // Continuation token for next batch
  string continuation_token = 3;

  // Total number of messages available
  uint64 total_messages = 4;

  // Current stream position
  uint64 stream_position = 5;

  // Whether the stream has ended
  bool stream_ended = 6;
}

```

---

### subscribe_request.proto {#subscribe_request}

**Path**: `pkg/queue/proto/subscribe_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 246

**Messages** (12): `SubscribeRequest`, `SubscriptionConfiguration`, `MessageFilterConfig`, `ContentFilter`, `DeliveryConfiguration`, `DeliveryRetryConfig`, `BatchDeliveryConfig`, `FlowControlSettings`, `ErrorHandlingConfig`,
`DeadLetterQueueConfig`, `ErrorActionConfig`, `ErrorNotificationConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/ack_level.proto` → [queue_1](./queue_1.md#ack_level)
- `pkg/queue/proto/delivery_mode.proto` → [queue_1](./queue_1.md#delivery_mode)

#### Source Code

```protobuf
// file: pkg/queue/proto/subscribe_request.proto
// version: 1.1.0
// Request to create a subscription to a queue or topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/ack_level.proto";
import "pkg/queue/proto/delivery_mode.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// SubscribeRequest creates a new subscription to a queue or topic
message SubscribeRequest {
  // Topic or queue to subscribe to
  string topic = 1;

  // Subscription name/identifier
  string subscription_name = 2;

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

// Configuration for the subscription
message SubscriptionConfiguration {
  // Acknowledgment level required
  AckLevel ack_level = 1;

  // Delivery mode for messages
  DeliveryMode delivery_mode = 2;

  // Maximum number of unacknowledged messages
  int32 max_unacked_messages = 3;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 4;

  // Message priority filter (minimum priority)
  int32 min_priority = 5;

  // Enable message ordering
  bool ordered_delivery = 6;

  // Auto-acknowledge messages after delivery
  bool auto_acknowledge = 7;

  // Subscription expiration time (seconds, 0 = no expiration)
  int64 expiration_seconds = 8;

  // Enable duplicate message detection
  bool duplicate_detection = 9;

  // Maximum message age to accept (seconds)
  int64 max_message_age_seconds = 10;
}

// Message filtering configuration
message MessageFilterConfig {
  // Header-based filters
  map<string, string> header_filters = 1;

  // Content-based filters
  repeated ContentFilter content_filters = 2;

  // Routing key patterns
  repeated string routing_key_patterns = 3;

  // Message type filters
  repeated string message_types = 4;

  // Custom filter expressions
  repeated string filter_expressions = 5;

  // Exclude messages matching these criteria
  bool exclude_matching = 6;
}

// Content-based message filter
message ContentFilter {
  // JSON path or field name
  string field_path = 1;

  // Filter operator (equals, contains, regex, gt, lt, etc.)
  string operator = 2;

  // Filter value
  string value = 3;

  // Case sensitive matching
  bool case_sensitive = 4;
}

// Delivery configuration for the subscription
message DeliveryConfiguration {
  // Delivery endpoint (for push subscriptions)
  string push_endpoint = 1;

  // Delivery timeout (milliseconds)
  int32 delivery_timeout_ms = 2;

  // Retry configuration for failed deliveries
  DeliveryRetryConfig retry_config = 3;

  // Batch delivery settings
  BatchDeliveryConfig batch_config = 4;

  // Flow control settings
  FlowControlSettings flow_control = 5;

  // Enable compression for delivery
  bool enable_compression = 6;

  // Authentication for push endpoints
  map<string, string> auth_headers = 7;
}

// Retry configuration for delivery failures
message DeliveryRetryConfig {
  // Enable retry on delivery failures
  bool enabled = 1;

  // Maximum retry attempts
  int32 max_retries = 2;

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 3;

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 4;

  // Backoff multiplier
  double backoff_multiplier = 5;

  // Retry only for specific error codes
  repeated string retry_error_codes = 6;
}

// Batch delivery configuration
message BatchDeliveryConfig {
  // Enable batch delivery
  bool enabled = 1;

  // Maximum messages per batch
  int32 max_batch_size = 2;

  // Maximum batch size in bytes
  int64 max_batch_bytes = 3;

  // Maximum time to wait for batch completion (milliseconds)
  int32 batch_timeout_ms = 4;
}

// Flow control settings
message FlowControlSettings {
  // Maximum outstanding messages
  int32 max_outstanding_messages = 1;

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 2;

  // Flow control algorithm
  string algorithm = 3;
}

// Error handling configuration
message ErrorHandlingConfig {
  // Dead letter queue configuration
  DeadLetterQueueConfig dlq_config = 1;

  // Maximum delivery attempts before DLQ
  int32 max_delivery_attempts = 2;

  // Actions to take on specific errors
  repeated ErrorActionConfig error_actions = 3;

  // Enable error logging
  bool enable_error_logging = 4;

  // Error notification settings
  ErrorNotificationConfig notification_config = 5;
}

// Dead letter queue configuration
message DeadLetterQueueConfig {
  // Enable dead letter queue
  bool enabled = 1;

  // Dead letter queue topic
  string dlq_topic = 2;

  // Maximum message age in DLQ (seconds)
  int64 dlq_max_age_seconds = 3;

  // Include original error information
  bool include_error_info = 4;
}

// Error action configuration
message ErrorActionConfig {
  // Error code or pattern
  string error_pattern = 1;

  // Action to take (retry, dlq, drop, pause)
  string action = 2;

  // Action parameters
  map<string, string> action_params = 3;
}

// Error notification configuration
message ErrorNotificationConfig {
  // Enable error notifications
  bool enabled = 1;

  // Notification channels
  repeated string notification_channels = 2;

  // Error threshold for notifications
  int32 error_threshold = 3;

  // Notification frequency (seconds)
  int32 notification_frequency_seconds = 4;
}

```

---

### subscribe_response.proto {#subscribe_response}

**Path**: `pkg/queue/proto/subscribe_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `SubscribeResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/connection_details.proto` → [queue_1](./queue_1.md#connection_details)
- `pkg/queue/proto/partition_offset.proto` → [queue_1](./queue_1.md#partition_offset)
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/subscribe_response.proto
// version: 1.0.0
// Response for queue subscription with messages

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/connection_details.proto";
import "pkg/queue/proto/partition_offset.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for subscription requests
message SubscribeResponse {
  // Message data
  QueueMessage message = 1;

  // Partition assignment info
  PartitionOffset partition_offset = 2;

  // Connection details for streaming
  ConnectionDetails connection_details = 3;

  // Subscription ID
  string subscription_id = 4;

  // Error message if any
  string error = 5;
}

```

---

### unsubscribe_request.proto {#unsubscribe_request}

**Path**: `pkg/queue/proto/unsubscribe_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `UnsubscribeRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/unsubscribe_request.proto
// version: 1.0.0
// Request to unsubscribe from a topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to unsubscribe from a topic
message UnsubscribeRequest {
  // Subscription ID to unsubscribe
  string subscription_id = 1;

  // Consumer group ID
  string consumer_group_id = 2;

  // Force unsubscribe even if messages are pending
  bool force = 3;

  // Close underlying connections
  bool close_connections = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}

```

---

### unsubscribe_response.proto {#unsubscribe_response}

**Path**: `pkg/queue/proto/unsubscribe_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `UnsubscribeResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/unsubscribe_response.proto
// file: queue/proto/responses/unsubscribe_response.proto
// version: 1.0.0
// guid: 5a4b3c2d-1e0f-9a8b-7c6d-5e4f3a2b1c0d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for unsubscription operations.
 */
message UnsubscribeResponse {
  // Whether the unsubscription was successful
  bool success = 1;

  // Name of the subscription that was removed
  string subscription_name = 2;

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

### update_message_request.proto {#update_message_request}

**Path**: `pkg/queue/proto/update_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 156

**Messages** (7): `UpdateMessageRequest`, `MessageUpdateProperties`, `VisibilityUpdate`, `PriorityUpdate`, `MetadataUpdate`, `ContentUpdate`, `UpdateCondition`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/update_message_request.proto
// version: 1.1.0
// Request to update message properties or metadata

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// UpdateMessageRequest modifies properties of an existing message
message UpdateMessageRequest {
  // Message identifier to update
  string message_id = 1;

  // Topic or queue containing the message
  string topic = 2;

  // Partition ID (if applicable)
  int32 partition_id = 3;

  // Message offset (for precise identification)
  int64 message_offset = 4;

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
  repeated string update_fields = 10;

  // Conditional update based on current state
  UpdateCondition condition = 11;

  // Update operation metadata
  map<string, string> operation_metadata = 12;
}

// Properties to update for the message
message MessageUpdateProperties {
  // New expiration time
  google.protobuf.Timestamp expiration_time = 1;

  // New delivery delay
  int64 delivery_delay_ms = 2;

  // New retry count
  int32 retry_count = 3;

  // New routing key
  string routing_key = 4;

  // New correlation ID
  string correlation_id = 5;

  // New reply-to address
  string reply_to = 6;

  // Updated message headers
  map<string, string> headers = 7;
}

// Visibility timeout update
message VisibilityUpdate {
  // New visibility timeout duration (milliseconds)
  int64 visibility_timeout_ms = 1;

  // Extend current timeout (if true) or set absolute timeout
  bool extend_current = 2;

  // Maximum visibility timeout allowed
  int64 max_visibility_ms = 3;
}

// Priority update for the message
message PriorityUpdate {
  // New priority level
  int32 priority_level = 1;

  // Priority change reason
  string priority_reason = 2;

  // Maintain relative priority ordering
  bool maintain_order = 3;
}

// Metadata update for the message
message MetadataUpdate {
  // Metadata fields to add or update
  map<string, string> add_metadata = 1;

  // Metadata fields to remove
  repeated string remove_metadata = 2;

  // Replace all metadata with new values
  map<string, string> replace_metadata = 3;

  // Update operation (add, remove, replace)
  string operation_type = 4;
}

// Content update for the message (if supported)
message ContentUpdate {
  // New message payload
  google.protobuf.Any new_payload = 1;

  // Content encoding
  string content_encoding = 2;

  // Content type
  string content_type = 3;

  // Compression applied to content
  string compression = 4;

  // Checksum of new content
  string content_checksum = 5;
}

// Conditional update criteria
message UpdateCondition {
  // Expected current version/etag
  string expected_version = 1;

  // Expected current state
  string expected_state = 2;

  // Maximum age for update (seconds)
  int64 max_age_seconds = 3;

  // Update only if message hasn't been delivered
  bool only_if_not_delivered = 4;

  // Update only if message is visible
  bool only_if_visible = 5;

  // Custom condition expression
  string condition_expression = 6;
}

```

---
