# queue_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 49
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [get_partition_info_request.proto](#get_partition_info_request)
- [get_partition_info_response.proto](#get_partition_info_response)
- [get_queue_health_request.proto](#get_queue_health_request)
- [get_queue_health_response.proto](#get_queue_health_response)
- [get_queue_info_request.proto](#get_queue_info_request)
- [get_queue_info_response.proto](#get_queue_info_response)
- [get_queue_stats_request.proto](#get_queue_stats_request)
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
- [list_queues_request.proto](#list_queues_request)
- [list_queues_response.proto](#list_queues_response)
- [list_subscriptions_request.proto](#list_subscriptions_request)
- [list_subscriptions_response.proto](#list_subscriptions_response)
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
- [publish_result.proto](#publish_result)
- [pull_request.proto](#pull_request)
- [pull_response.proto](#pull_response)
- [purge_request.proto](#purge_request)
- [purge_response.proto](#purge_response)
- [push_request.proto](#push_request)
- [push_response.proto](#push_response)
- [queue.proto](#queue)
- [queue_consumer_stats.proto](#queue_consumer_stats)
- [queue_depth_sample.proto](#queue_depth_sample)
- [queue_health.proto](#queue_health)
- [queue_info.proto](#queue_info)
- [queue_message.proto](#queue_message)
- [queue_stats.proto](#queue_stats)
- [queue_stats_point.proto](#queue_stats_point)
- [queue_stats_response.proto](#queue_stats_response)
---


## Detailed Documentation

### get_partition_info_request.proto {#get_partition_info_request}

**Path**: `gcommon/v1/queue/get_partition_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 50

**Messages** (1): `GetPartitionInfoRequest`

**Imports** (3):

- `gcommon/v1/queue/time_range_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_partition_info_request.proto
// version: 1.1.0
// guid: 7478ffad-9bff-42f2-b8c9-cd583c1adcea
// Request to get partition information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/time_range_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// GetPartitionInfoRequest retrieves information about topic partitions
message GetPartitionInfoRequest {
  // Topic identifier
  string topic_id = 1 [(buf.validate.field).string.min_len = 1];

  // Specific partition IDs (empty = all partitions)
  repeated int32 partition_ids = 2 [(buf.validate.field).repeated.min_items = 1];

  // Include partition statistics
  bool include_stats = 3;

  // Include consumer information
  bool include_consumers = 4;

  // Include offset information
  bool include_offsets = 5;

  // Include partition health status
  bool include_health_status = 6;

  // Include leader/replica information
  bool include_leader_info = 7;

  // Include partition configuration
  bool include_config = 8;

  // Time range for historical statistics - references existing TimeRangeFilter from get_queue_info_request.proto
  TimeRangeFilter time_range = 9;

  // Access control context
  string access_token = 10 [(buf.validate.field).string.min_len = 1];
}
// This file needs proper implementation
```

---

### get_partition_info_response.proto {#get_partition_info_response}

**Path**: `gcommon/v1/queue/get_partition_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `GetPartitionInfoResponse`

**Imports** (3):

- `gcommon/v1/queue/partition_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_partition_info_response.proto
// version: 1.0.0
// guid: 414613a0-0192-43b0-9f7f-347bd35d0bfc
// Response with partition information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/partition_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response with partition information
message GetPartitionInfoResponse {
  // Partition information
  PartitionInfo partition_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_queue_health_request.proto {#get_queue_health_request}

**Path**: `gcommon/v1/queue/get_queue_health_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `GetQueueHealthRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_health_request.proto
// version: 1.0.0
// guid: 9862f197-381f-41d3-a980-953ef636c78d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueHealthRequest {
  // Specific queue names to check (empty = all queues)
  repeated string queue_names = 1 [(buf.validate.field).repeated.min_items = 1];

  // Whether to include detailed health metrics
  bool include_details = 2;
}
```

---

### get_queue_health_response.proto {#get_queue_health_response}

**Path**: `gcommon/v1/queue/get_queue_health_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `GetQueueHealthResponse`

**Imports** (4):

- `gcommon/v1/queue/cluster_health.proto`
- `gcommon/v1/queue/queue_health.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_health_response.proto
// version: 1.0.0
// guid: ca800078-3add-48f9-9559-c95d23232cea

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/cluster_health.proto";
import "gcommon/v1/queue/queue_health.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueHealthResponse {
  // Health status for each queue
  repeated QueueHealth queue_health = 1 [(buf.validate.field).repeated.min_items = 1];

  // Overall cluster health
  ClusterHealth cluster_health = 2;
}
```

---

### get_queue_info_request.proto {#get_queue_info_request}

**Path**: `gcommon/v1/queue/get_queue_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 50

**Messages** (1): `GetQueueInfoRequest`

**Imports** (3):

- `gcommon/v1/queue/time_range_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_info_request.proto
// version: 1.0.0
// guid: 9c3c8693-8a62-4458-86af-19a28b6b250a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/time_range_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueInfoRequest {
  // Queue identifier
  string queue_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include queue statistics in response
  bool include_stats = 2;

  // Include queue configuration in response
  bool include_config = 3;

  // Include partition information
  bool include_partitions = 4;

  // Include consumer group information
  bool include_consumer_groups = 5;

  // Include current subscriptions
  bool include_subscriptions = 6;

  // Include topic binding information
  bool include_bindings = 7;

  // Include recent error information
  bool include_errors = 8;

  // Time range for statistics (if not specified, returns current state)
  TimeRangeFilter time_range = 9;

  // Specific information sections to retrieve
  repeated string info_sections = 10 [(buf.validate.field).repeated.min_items = 1];

  // Access control context
  string access_token = 11 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_queue_info_response.proto {#get_queue_info_response}

**Path**: `gcommon/v1/queue/get_queue_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `GetQueueInfoResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_info_response.proto
// version: 1.0.0
// guid: 06258d4a-8574-4cd1-977b-59927a7ad597
// Response with queue information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response with queue information
message GetQueueInfoResponse {
  // Queue information
  QueueInfo queue_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_queue_stats_request.proto {#get_queue_stats_request}

**Path**: `gcommon/v1/queue/get_queue_stats_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `GetQueueStatsRequest`

**Imports** (4):

- `gcommon/v1/common/stats_granularity.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_stats_request.proto
// version: 1.0.0
// guid: 7dc18176-1123-444f-8040-b7e352b501d6

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/stats_granularity.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueStatsRequest {
  // Name of the queue
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Time range for statistics
  gcommon.v1.common.TimeRangeMetrics time_range = 2;

  // Granularity of statistics (hourly, daily, etc.)
  gcommon.v1.common.StatsGranularity granularity = 3;
}
```

---

### get_queue_stats_response.proto {#get_queue_stats_response}

**Path**: `gcommon/v1/queue/get_queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `GetQueueStatsResponse`

**Imports** (10):

- `gcommon/v1/common/metrics_error_stats.proto`
- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/consumer_stats.proto`
- `gcommon/v1/queue/historical_stats.proto`
- `gcommon/v1/queue/performance_metrics.proto`
- `gcommon/v1/queue/queue_stats.proto`
- `gcommon/v1/queue/queue_stats_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_stats_response.proto
// version: 1.0.0
// guid: 7014296b-b332-416c-9de8-7d0fd264251c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_error_stats.proto";
import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/consumer_stats.proto";
import "gcommon/v1/queue/historical_stats.proto";
import "gcommon/v1/queue/performance_metrics.proto";
import "gcommon/v1/queue/queue_stats.proto";
import "gcommon/v1/queue/queue_stats_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueStatsResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Overall statistics summary
  QueueStatsSummary summary = 2;

  // Per-queue statistics (if multiple queues requested)
  repeated QueueStats queue_stats = 3 [(buf.validate.field).repeated.min_items = 1];

  // Consumer statistics (if requested)
  repeated ConsumerStats consumer_stats = 4 [(buf.validate.field).repeated.min_items = 1];

  // Historical statistics (if requested)
  HistoricalStats historical_stats = 5;

  // Error statistics (if requested)
  gcommon.v1.common.MetricsErrorStats error_stats = 6;

  // Performance metrics
  PerformanceMetrics performance_metrics = 7;

  // Timestamp when these statistics were generated
  google.protobuf.Timestamp generated_at = 8;
}
```

---

### get_subscription_info_request.proto {#get_subscription_info_request}

**Path**: `gcommon/v1/queue/get_subscription_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `GetSubscriptionInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_subscription_info_request.proto
// version: 1.0.0
// guid: 560f1d95-f68d-41e7-821f-fbb741872dc8
// Request to get subscription information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to get subscription information
message GetSubscriptionInfoRequest {
  // Subscription ID to get info for
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include detailed metrics
  bool include_metrics = 2;

  // Include consumer group details
  bool include_consumer_details = 3;

  // Include partition assignments
  bool include_partitions = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### get_subscription_info_response.proto {#get_subscription_info_response}

**Path**: `gcommon/v1/queue/get_subscription_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 67

**Messages** (1): `GetSubscriptionInfoResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/get_subscription_info_response.proto
// file: proto/gcommon/v1/queue/get_subscription_info_response.proto
// version: 1.0.0
// guid: 3f2e1d0c-9b8a-7f6e-5d4c-3b2a1f0e9d8c
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
 * Response message for subscription information retrieval.
 */
message GetSubscriptionInfoResponse {
  // Unique identifier for the subscription
  string subscription_id = 1;

  // Name of the subscription
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic this subscription is bound to
  string topic_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
  google.protobuf.Timestamp created_at = 9 [ (buf.validate.field).required = true ];

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

**Path**: `gcommon/v1/queue/get_topic_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `GetTopicInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_topic_info_request.proto
// version: 1.0.0
// guid: f3a4b5c6-d7e8-9f0a-1b2c-3d4e5f6a7b8c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to get information about a topic.
 * Used for retrieving topic metadata and configuration.
 */
message GetTopicInfoRequest {
  // Name of the topic to get information for
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/queue/get_topic_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 67

**Messages** (1): `GetTopicInfoResponse`

**Imports** (9):

- `gcommon/v1/common/metrics_retention_info.proto`
- `gcommon/v1/queue/owner_info.proto`
- `gcommon/v1/queue/partition_info.proto`
- `gcommon/v1/queue/topic_configuration.proto`
- `gcommon/v1/queue/topic_permissions.proto`
- `gcommon/v1/queue/topic_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_topic_info_response.proto
// version: 1.0.0
// guid: 1a5f0bc1-5c84-4d82-9730-028810eadf04

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_retention_info.proto";
import "gcommon/v1/queue/owner_info.proto";
import "gcommon/v1/queue/partition_info.proto";
import "gcommon/v1/queue/topic_configuration.proto";
import "gcommon/v1/queue/topic_permissions.proto";
import "gcommon/v1/queue/topic_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetTopicInfoResponse {
  // Topic identifier
  string topic_id = 1;

  // Topic name
  string topic_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Topic creation timestamp
  google.protobuf.Timestamp created_at = 4 [ (buf.validate.field).required = true ];

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

  // Retention policy for messages in this topic
  gcommon.v1.common.MetricsRetentionInfo retention = 14;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/queue/health_check_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `QueueHealthCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/health_check_request.proto
// version: 1.0.0
// guid: e9e95e53-7d2b-4dbf-896d-e9dea8853bd0
//
// HealthCheckRequest for the queue module

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueHealthCheckRequest {
  // Name of the queue to check.
  string queue = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/queue/health_check_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `QueueHealthCheckResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/health_check_response.proto
// version: 1.0.1
// guid: 24f4fcb1-f84d-4f02-845d-01b9759bfb6a
//
// HealthCheckResponse for the queue module
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * HealthCheckResponse returns queue service health status.
 */
message QueueHealthCheckResponse {
  // Overall queue service health.
  gcommon.v1.common.CommonHealthStatus status = 1;

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

**Path**: `gcommon/v1/queue/import_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `ImportQueueRequest`

**Imports** (3):

- `gcommon/v1/common/queue_export_format.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/import_queue_request.proto
// file: proto/gcommon/v1/queue/import_queue_request.proto
// version: 1.0.0
// guid: 5d6e7f8a-9b0c-1d2e-3f4a-5b6c7d8e9f0a
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/queue_export_format.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to import queue data from external source.
 */
message ImportQueueRequest {
  // Name of the queue to import into
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Source location for import data
  string source_path = 2;

  // Format of the import data
  gcommon.v1.common.QueueExportFormat format = 3;

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

**Path**: `gcommon/v1/queue/import_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 53

**Messages** (1): `ImportQueueResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/import_queue_response.proto
// file: proto/gcommon/v1/queue/import_queue_response.proto
// version: 1.0.0
// guid: 5d4c3b2a-1f0e-9d8c-7b6a-5e4f3a2b1c0d
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
 * Response message for queue import operations.
 */
message ImportQueueResponse {
  // Unique identifier for the import operation
  string import_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the import was successful
  bool success = 2;

  // Error message if import failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];

  // Number of messages imported
  uint64 imported_count = 4 [(buf.validate.field).uint64.gte = 0];

  // Number of messages that failed to import
  uint64 failed_count = 5 [(buf.validate.field).uint64.gte = 0];

  // Total number of messages processed
  uint64 total_count = 6 [(buf.validate.field).uint64.gte = 0];

  // Timestamp when import started
  google.protobuf.Timestamp start_time = 7;

  // Timestamp when import completed
  google.protobuf.Timestamp end_time = 8;

  // Import duration in milliseconds
  uint64 duration_ms = 9 [(buf.validate.field).uint64.gte = 0];

  // Import progress as percentage (0-100)
  float progress_percent = 10 [(buf.validate.field).float.gte = 0.0, (buf.validate.field).float.lte = 100.0];
}
```

---

### list_messages_request.proto {#list_messages_request}

**Path**: `gcommon/v1/queue/list_messages_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `ListMessagesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_messages_request.proto
// version: 1.0.0
// guid: 176dd26f-bea8-4823-aa6a-eda00afdfeb6
// Request to list messages in a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to list messages in a queue
message ListMessagesRequest {
  // Topic name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Partition ID (optional, all partitions if not specified)
  int32 partition_id = 2 [(buf.validate.field).int32.gte = 0];

  // Starting offset
  int64 start_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum number of messages to return
  int32 limit = 4 [(buf.validate.field).int32.gte = 0];

  // Include message headers
  bool include_headers = 5;

  // Include message metadata
  bool include_metadata = 6;

  // Filter by message status (optional)
  string status_filter = 7 [(buf.validate.field).string.min_len = 1];

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 8 [(buf.validate.field).int32.gt = 0];
}
```

---

### list_messages_response.proto {#list_messages_response}

**Path**: `gcommon/v1/queue/list_messages_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ListMessagesResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_messages_response.proto
// version: 1.0.0
// guid: 2a7aef43-6b98-462f-a3bd-9f06cb6636de
// Response for listing messages

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for listing messages
message ListMessagesResponse {
  // List of messages
  repeated QueueMessage messages = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of messages available
  int64 total_count = 2 [(buf.validate.field).int64.gte = 0];

  // Next page token for pagination
  string next_page_token = 3 [(buf.validate.field).string.min_len = 1];

  // Whether there are more messages
  bool has_more = 4;

  // Error message if listing failed
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_queues_request.proto {#list_queues_request}

**Path**: `gcommon/v1/queue/list_queues_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ListQueuesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_queues_request.proto
// version: 1.0.0
// guid: 10aa0104-6a4e-4092-98f4-8eabba61ea69
// ListQueuesRequest retrieves available queues for the current
// user or service account. This file was a placeholder and now
// implements the request following the 1-1-1 pattern.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListQueuesRequest {
  // Standard request metadata used across all services
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Optional page size for results
  int32 page_size = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Optional token for fetching the next page
  string page_token = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_queues_response.proto {#list_queues_response}

**Path**: `gcommon/v1/queue/list_queues_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListQueuesResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/queue_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_queues_response.proto
// version: 1.0.0
// guid: c2ffc959-d7b5-451f-94f4-a9334e02725f

// ListQueuesResponse returns a list of queues visible to the
// requester along with pagination information. This replaces the
// placeholder file generated during the migration.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/queue_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListQueuesResponse {
  // Collection of queues
  repeated QueueInfo queues = 1 [(buf.validate.field).repeated.min_items = 1];

  // Token to retrieve the next page
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### list_subscriptions_request.proto {#list_subscriptions_request}

**Path**: `gcommon/v1/queue/list_subscriptions_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `QueueListSubscriptionsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_subscriptions_request.proto
// version: 1.0.0
// guid: 781a6513-601b-4ef8-87bf-7c881f4b8a79
// ListSubscriptionsRequest returns subscriptions for a given topic or queue.
// Previously a placeholder, this file now contains the full request definition.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueListSubscriptionsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Name of the topic or queue to list subscriptions for
  string parent = 2 [(buf.validate.field).string.min_len = 1];

  // Optional page size
  int32 page_size = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Optional page token
  string page_token = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_subscriptions_response.proto {#list_subscriptions_response}

**Path**: `gcommon/v1/queue/list_subscriptions_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListSubscriptionsResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/common/subscription_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_subscriptions_response.proto
// version: 1.0.0
// guid: c20dc6c8-336b-4626-b709-22be9663d29d

// ListSubscriptionsResponse contains the subscriptions under a
// specific topic or queue. This file now implements the message
// rather than acting as a placeholder.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/common/subscription_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListSubscriptionsResponse {
  // Subscriptions returned
  repeated gcommon.v1.common.CommonSubscriptionInfo subscriptions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Token for fetching the next page
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Response metadata common across services
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### list_topics_request.proto {#list_topics_request}

**Path**: `gcommon/v1/queue/list_topics_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `ListTopicsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_topics_request.proto
// version: 1.1.0
// guid: f939cf46-c0f6-4815-a201-7cebdf9c255d
// Request to list available topics in the queue system

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ListTopicsRequest retrieves a list of available topics
message ListTopicsRequest {
  // Filter topics by name pattern (supports wildcards)
  string name_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Filter topics by namespace/category
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Include topic metadata in response
  bool include_metadata = 3;

  // Include topic statistics in response
  bool include_stats = 4;

  // Maximum number of topics to return
  int32 limit = 5 [(buf.validate.field).int32.gte = 0];

  // Pagination token for continued listing
  string page_token = 6 [(buf.validate.field).string.min_len = 1];

  // Sort topics by specified field (name, created_at, message_count)
  string sort_by = 7 [(buf.validate.field).string.min_len = 1];

  // Sort order (asc, desc)
  string sort_order = 8 [(buf.validate.field).string.min_len = 1];

  // Filter by topic state (active, paused, deleted)
  repeated string topic_states = 9 [(buf.validate.field).repeated.min_items = 1];

  // Include only topics user has access to
  bool access_check = 10;

  // Additional filter criteria
  map<string, string> filters = 11;
}
```

---

### list_topics_response.proto {#list_topics_response}

**Path**: `gcommon/v1/queue/list_topics_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListTopicsResponse`

**Imports** (3):

- `gcommon/v1/queue/topic_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_topics_response.proto
// version: 1.1.0
// guid: 64d60266-e2ca-4927-9db1-d3824b83d9a5
// Response containing list of available topics

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/topic_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListTopicsResponse {
  // List of topics
  repeated TopicInfo topics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Next page token
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total count
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}

// ListTopicsResponse returns a list of available topics
// This file needs proper implementation
```

---

### migrate_queue_request.proto {#migrate_queue_request}

**Path**: `gcommon/v1/queue/migrate_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `MigrateQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/migrate_queue_request.proto
// version: 1.0.0
// guid: 2d4044aa-7bd3-43a9-91c7-d4f8c0be36f9
// Request to migrate a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to migrate a queue to a new location
message MigrateQueueRequest {
  // Source queue name to migrate from
  string source_queue = 1 [(buf.validate.field).string.min_len = 1];

  // Destination queue name to migrate to
  string destination_queue = 2 [(buf.validate.field).string.min_len = 1];

  // Destination endpoint/server
  string destination_endpoint = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to preserve message ordering
  bool preserve_order = 4;

  // Whether to verify data integrity after migration
  bool verify_integrity = 5;

  // Maximum migration duration (milliseconds)
  int32 max_duration_ms = 6 [(buf.validate.field).int32.gt = 0];

  // Batch size for migration
  int32 batch_size = 7 [(buf.validate.field).int32.gte = 0];

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 8 [(buf.validate.field).int32.gt = 0];
}
```

---

### migrate_queue_response.proto {#migrate_queue_response}

**Path**: `gcommon/v1/queue/migrate_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `MigrateQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/migrate_queue_response.proto
// version: 1.0.0
// guid: 331ebb05-f30d-46d3-8d6e-ef766fd0cc51
// Response for queue migration operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue migration operations
message MigrateQueueResponse {
  // Whether the migration was successful
  bool success = 1;

  // New queue location/endpoint
  string new_queue_endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Number of messages migrated
  int64 messages_migrated = 3 [(buf.validate.field).int64.gte = 0];

  // Migration duration (milliseconds)
  int32 migration_duration_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Source queue name
  string source_queue = 5 [(buf.validate.field).string.min_len = 1];

  // Destination queue name
  string destination_queue = 6 [(buf.validate.field).string.min_len = 1];

  // Error message if migration failed
  string error = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### nack_request.proto {#nack_request}

**Path**: `gcommon/v1/queue/nack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `NackRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/nack_error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_request.proto
// version: 1.1.0
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/nack_error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to negatively acknowledge (NACK) a message.
 * This indicates that the message could not be processed and may need to be requeued.
 */
message NackRequest {
  // Acknowledgment token received with the message
  string ack_token = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the message should be requeued for retry
  bool requeue = 2;

  // Reason for the negative acknowledgment
  string reason = 3 [(buf.validate.field).string.min_len = 1];

  // Error details if processing failed
  NackError error = 4;

  // Delay before requeuing (if requeue is true)
  int64 requeue_delay_seconds = 5 [(buf.validate.field).int64.gte = 0];

  // Maximum number of retry attempts for this message
  int32 max_retries = 6 [(buf.validate.field).int32.gte = 0];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
```

---

### nack_response.proto {#nack_response}

**Path**: `gcommon/v1/queue/nack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `NackResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_response.proto
// version: 1.0.0
// guid: 70f01290-1e6f-484c-aa71-1cd5f50aa7f5
// Response for negative acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for negative acknowledgment operations
message NackResponse {
  // Whether the nack was successful
  bool success = 1;

  // Error message if nack failed
  string error = 2 [(buf.validate.field).string.min_len = 1];

  // Message ID that was nacked
  string message_id = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when nack was processed
  int64 timestamp = 4;
}
```

---

### pause_queue_request.proto {#pause_queue_request}

**Path**: `gcommon/v1/queue/pause_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PauseQueueRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pause_queue_request.proto
// version: 1.0.0
// guid: a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to pause a queue.
 * Stops message processing while keeping messages in the queue.
 */
message PauseQueueRequest {
  // Name of the queue to pause
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/queue/pause_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PauseQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pause_queue_response.proto
// version: 1.0.0
// guid: 8d32dd33-5b24-4d1f-b32c-fc9e172e7b9a
// Response for queue pause operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue pause operations
message PauseQueueResponse {
  // Whether the pause was successful
  bool success = 1;

  // Queue name that was paused
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/queue/peek_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 100

**Messages** (1): `PeekRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/peek_request.proto
// version: 1.0.0
// guid: 1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";
// Standard imports

// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

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
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/queue/peek_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 127

**Messages** (1): `PeekResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/peek_response.proto
// version: 1.0.0
// guid: 2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

// Queue message types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

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
  repeated QueueMessage messages = 1;

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
  string queue_name = 12 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/queue/publish_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `QueuePublishRequest`

**Imports** (5):

- `buf/validate/validate.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/delivery_options.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_request.proto
// version: 1.1.0
// guid: 59dc8120-bc2f-4d56-a9f1-f0957cb9bafb
// PublishRequest publishes a single message to a named topic. It is
// used for pub/sub style messaging where consumers subscribe to
// topics rather than specific queues.
// PublishRequest contains all information required to publish a
// message to a topic.

edition = "2023";

package gcommon.v1.queue;

import "buf/validate/validate.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/delivery_options.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueuePublishRequest {
  // Name of the topic to publish to - required, alphanumeric with dots/hyphens, 3-255 chars
  string topic_name = 1 [
    (buf.validate.field).required = true,
    (buf.validate.field).string.pattern = "^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$",
    (buf.validate.field).string.min_len = 3,
    (buf.validate.field).string.max_len = 255
  ];

  // Message to publish - required
  QueueMessage message = 2 [(buf.validate.field).required = true];

  // Optional delivery parameters controlling retries and delays
  DeliveryOptions delivery_options = 3;

  // Standard request metadata for tracing and auth - required
  gcommon.v1.common.RequestMetadata metadata = 4 [(buf.validate.field).required = true];
}
```

---

### publish_response.proto {#publish_response}

**Path**: `gcommon/v1/queue/publish_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PublishResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_response.proto
// version: 1.0.0
// guid: 8b12b279-f7c6-40fe-9147-4a663fb0c9c6

// PublishResponse reports the outcome of publishing a message to a
// topic.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// PublishResponse contains the identifier of the published message
// and success status.
message PublishResponse {
  // Unique identifier of the message as stored by the broker.
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the publish operation succeeded.
  bool success = 2;

  // Error information when success is false.
  gcommon.v1.common.Error error = 3;

  // Request metadata echoed back for tracing.
  gcommon.v1.common.RequestMetadata request_metadata = 4;
}
```

---

### publish_result.proto {#publish_result}

**Path**: `gcommon/v1/queue/publish_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `PublishResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_result.proto
// version: 1.0.0
// guid: aabfd67d-e9a2-40c7-99b8-464c242bc864
// Result information for individual message publish operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Result for an individual message publish
message PublishResult {
  // Message ID assigned by the queue
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the publish was successful
  bool success = 2;

  // Error message if publish failed
  string error = 3 [(buf.validate.field).string.min_len = 1];

  // Partition ID where message was published
  int32 partition_id = 4 [(buf.validate.field).int32.gte = 0];

  // Offset within the partition
  int64 offset = 5 [(buf.validate.field).int64.gte = 0];

  // Timestamp when message was published
  int64 timestamp = 6;
}
```

---

### pull_request.proto {#pull_request}

**Path**: `gcommon/v1/queue/pull_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PullRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pull_request.proto
// version: 1.0.0
// guid: dae5ea8a-77c7-4b90-ab25-d2981ba423df
// PullRequest retrieves a single message from the specified queue
// without establishing a subscription. This file replaces the
// placeholder generated during migration.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PullRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Queue to pull from
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional visibility timeout for the pulled message
  int32 visibility_timeout_seconds = 3;
}
```

---

### pull_response.proto {#pull_response}

**Path**: `gcommon/v1/queue/pull_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `PullResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/received_message.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pull_response.proto
// version: 1.0.1
// guid: 5c55b3fd-beda-4758-90c9-2084f2d6ea8f

// PullResponse returns a message pulled from the queue. This file
// now contains the actual response definition instead of a placeholder.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/received_message.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PullResponse {
  // The received message. May be null if no message was available.
  ReceivedMessage message = 1;

  // Response metadata including error details
  gcommon.v1.common.ResponseMetadata metadata = 2;
}
```

---

### purge_request.proto {#purge_request}

**Path**: `gcommon/v1/queue/purge_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `PurgeRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/purge_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/purge_request.proto
// version: 1.0.0
// guid: 8d7b880f-5830-44c2-ab26-58afb465d587

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/purge_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PurgeRequest {
  // Name of the queue to purge
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Purge options
  PurgeOptions options = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
```

---

### purge_response.proto {#purge_response}

**Path**: `gcommon/v1/queue/purge_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `PurgeResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/purge_response.proto
// version: 1.0.0
// guid: 14d5741d-3af8-49b9-8ec4-887527a72cfb
// Response for queue purge operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue purge operations
message PurgeResponse {
  // Whether the purge was successful
  bool success = 1;

  // Number of messages purged
  int64 messages_purged = 2 [(buf.validate.field).int64.gte = 0];

  // Number of bytes freed
  int64 bytes_freed = 3 [(buf.validate.field).int64.gte = 0];

  // Purge duration (milliseconds)
  int32 purge_duration_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Partitions that were purged
  repeated int32 purged_partitions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Error message if purge failed
  string error = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### push_request.proto {#push_request}

**Path**: `gcommon/v1/queue/push_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `PushRequest`

**Imports** (5):

- `gcommon/v1/queue/batch_settings.proto`
- `gcommon/v1/queue/publish_config.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/push_request.proto
// version: 1.0.0
// guid: ab6bdde8-25b2-424c-a85a-db3364d8cdaf

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/batch_settings.proto";
import "gcommon/v1/queue/publish_config.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PushRequest {
  // Target topic or queue identifier
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Messages to publish
  repeated QueueMessage messages = 2 [(buf.validate.field).repeated.min_items = 1];

  // Publishing configuration
  PublishConfig publish_config = 3;

  // Batch publishing settings
  BatchSettings batch_settings = 4;

  // Transaction ID for transactional publishing
  string transaction_id = 5 [(buf.validate.field).string.min_len = 1];

  // Producer ID for message tracking
  string producer_id = 6 [(buf.validate.field).string.min_len = 1];

  // Publishing metadata
  map<string, string> metadata = 7;
}
```

---

### push_response.proto {#push_response}

**Path**: `gcommon/v1/queue/push_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `PushResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/push_response.proto
// file: proto/gcommon/v1/queue/push_response.proto
// version: 1.0.0
// guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d
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
 * Response for message publishing operations.
 */
message PushResponse {
  // Unique identifier assigned to the published message
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the message was accepted by the queue
  google.protobuf.Timestamp accepted_at = 2;

  // Position/offset of the message in the queue
  int64 message_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Current queue depth after the message was added
  int64 queue_depth = 4 [(buf.validate.field).int64.gte = 0];

  // Whether the message was persisted to storage
  bool persisted = 5;

  // Estimated delivery time (for delayed messages)
  google.protobuf.Timestamp estimated_delivery_time = 6;
}
// This file needs proper implementation
```

---

### queue.proto {#queue}

**Path**: `gcommon/v1/queue/queue.proto` **Package**: `gcommon.v1.queue` **Lines**: 12


**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue.proto
// version: 1.0.1
// guid: 1f2e3d4c-5b6a-7980-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";
```

---

### queue_consumer_stats.proto {#queue_consumer_stats}

**Path**: `gcommon/v1/queue/queue_consumer_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `QueueConsumerStats`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_consumer_stats.proto
// version: 1.0.0
// guid: b0ed0505-1d76-4961-8937-36fcad7a7185

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueConsumerStats {
  string consumer_id = 1;
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  int64 messages_processed = 3;
  double processing_rate = 4;
  double success_rate = 5;
  google.protobuf.Timestamp last_activity = 6;
  google.protobuf.Duration average_processing_time = 7;
}
```

---

### queue_depth_sample.proto {#queue_depth_sample}

**Path**: `gcommon/v1/queue/queue_depth_sample.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `QueueDepthSample`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_depth_sample.proto
// version: 1.0.0
// guid: 6f770e99-3809-4efb-848d-f2c554a669f8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueDepthSample {
  google.protobuf.Timestamp timestamp = 1;
  int64 depth = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### queue_health.proto {#queue_health}

**Path**: `gcommon/v1/queue/queue_health.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `QueueHealth`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_health.proto
// version: 1.0.0
// guid: 1524854f-4eb8-4bb2-8942-cd7ca2544b2d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueHealth {
  // Name of the queue
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Health status
  gcommon.v1.common.CommonHealthStatus status = 2;

  // Health score (0-100)
  int32 health_score = 3;

  // List of health issues
  repeated string issues = 4;

  // Last health check timestamp
  google.protobuf.Timestamp last_check = 5;
}
```

---

### queue_info.proto {#queue_info}

**Path**: `gcommon/v1/queue/queue_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `QueueInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_info.proto
// version: 1.0.0
// guid: d2ab2b72-14e2-4afe-80f7-2ecf00daacac

// QueueInfo provides metadata about a queue instance. This replaces the
// empty placeholder created during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * QueueInfo describes the configuration and current status of a queue.
 * It is returned by administrative APIs such as ListQueues.
 */
message QueueInfo {
  // Name of the queue
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of queue implementation (e.g., "rabbitmq", "nats")
  string type = 2;

  // Current approximate number of messages in the queue
  int64 message_count = 3;

  // Number of active consumers
  int32 consumer_count = 4;

  // Time when the queue was created
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // Additional metadata or labels for the queue
  map<string, string> labels = 6;
}
```

---

### queue_message.proto {#queue_message}

**Path**: `gcommon/v1/queue/queue_message.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `QueueMessage`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_message.proto
// version: 1.0.0
// guid: a2597962-4731-4f47-b6dd-4da9a937c834

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// QueueMessage represents a single item in a queue.
message QueueMessage {
  // Message ID (auto-generated if not provided).
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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
  google.protobuf.Timestamp created_at = 11 [ (buf.validate.field).required = true ];
}
```

---

### queue_stats.proto {#queue_stats}

**Path**: `gcommon/v1/queue/queue_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `QueueStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Statistics for a specific queue
message QueueStats {
  // Queue name
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current message count
  int64 message_count = 2;

  // Total bytes stored
  int64 total_bytes = 3;

  // Average message size
  double avg_message_size = 4;

  // Messages processed per second
  double throughput = 5;

  // Queue depth over time
  int64 current_depth = 6;

  // Peak depth in the measurement period
  int64 peak_depth = 7;

  // Last activity timestamp
  google.protobuf.Timestamp last_activity = 8;
}
```

---

### queue_stats_point.proto {#queue_stats_point}

**Path**: `gcommon/v1/queue/queue_stats_point.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `QueueStatsPoint`

**Imports** (3):

- `gcommon/v1/queue/queue_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats_point.proto
// version: 1.0.1
// guid: f6478b51-fafb-4571-b43b-cac8ec0cfd13

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStatsPoint {
  // Timestamp for this data point
  google.protobuf.Timestamp timestamp = 1;

  // Statistics at this point in time
  QueueStats stats = 2;
}
```

---

### queue_stats_response.proto {#queue_stats_response}

**Path**: `gcommon/v1/queue/queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `QueueStatsResponse`

**Imports** (4):

- `gcommon/v1/queue/queue_stats.proto`
- `gcommon/v1/queue/queue_stats_point.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats_response.proto
// version: 1.0.0
// guid: 5944c9a3-ae37-4aac-b6dc-36b7a9c0eaa5

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_stats.proto";
import "gcommon/v1/queue/queue_stats_point.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStatsResponse {
  // Queue statistics
  QueueStats stats = 1;

  // Time series data
  repeated QueueStatsPoint time_series = 2 [(buf.validate.field).repeated.min_items = 1];
}
```

---

