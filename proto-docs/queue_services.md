# queue_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 9
- **Services**: 3
- **Enums**: 0

## Files in this Module

- [queue_admin_service.proto](#queue_admin_service)
- [queue_monitoring_service.proto](#queue_monitoring_service)
- [queue_service.proto](#queue_service)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)
- [queue_2](./queue_2.md)
- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [web](./web.md)

---

## Detailed Documentation

### queue_admin_service.proto {#queue_admin_service}

**Path**: `pkg/queue/proto/queue_admin_service.proto` **Package**:
`gcommon.v1.queue` **Lines**: 51

**Services** (1): `QueueAdminService`

**Imports** (15):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/create_queue_request.proto` →
  [queue_api_1](./queue_api_1.md#create_queue_request)
- `pkg/queue/proto/create_queue_response.proto` →
  [queue_api_1](./queue_api_1.md#create_queue_response)
- `pkg/queue/proto/delete_topic_request.proto` →
  [queue_api_1](./queue_api_1.md#delete_topic_request)
- `pkg/queue/proto/delete_topic_response.proto` →
  [queue_api_1](./queue_api_1.md#delete_topic_response)
- `pkg/queue/proto/get_queue_info_request.proto` →
  [queue_api_1](./queue_api_1.md#get_queue_info_request)
- `pkg/queue/proto/get_queue_info_response.proto` →
  [queue_api_1](./queue_api_1.md#get_queue_info_response)
- `pkg/queue/proto/pause_queue_request.proto` →
  [queue_api_2](./queue_api_2.md#pause_queue_request)
- `pkg/queue/proto/pause_queue_response.proto` →
  [queue_api_2](./queue_api_2.md#pause_queue_response)
- `pkg/queue/proto/purge_request.proto` →
  [queue_api_2](./queue_api_2.md#purge_request)
- `pkg/queue/proto/purge_response.proto` →
  [queue_api_2](./queue_api_2.md#purge_response)
- `pkg/queue/proto/reset_queue_stats_request.proto` →
  [queue_api_2](./queue_api_2.md#reset_queue_stats_request)
- `pkg/queue/proto/reset_queue_stats_response.proto` →
  [queue_api_2](./queue_api_2.md#reset_queue_stats_response)
- `pkg/queue/proto/resume_queue_request.proto` →
  [queue_api_2](./queue_api_2.md#resume_queue_request)
- `pkg/queue/proto/resume_queue_response.proto` →
  [queue_api_2](./queue_api_2.md#resume_queue_response)

#### Source Code

```protobuf
// file: pkg/queue/proto/queue_admin_service.proto
// version: 1.0.0
// Administrative service for queue management

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/create_queue_request.proto";
import "pkg/queue/proto/create_queue_response.proto";
import "pkg/queue/proto/delete_topic_request.proto";
import "pkg/queue/proto/delete_topic_response.proto";
import "pkg/queue/proto/get_queue_info_request.proto";
import "pkg/queue/proto/get_queue_info_response.proto";
import "pkg/queue/proto/pause_queue_request.proto";
import "pkg/queue/proto/pause_queue_response.proto";
import "pkg/queue/proto/purge_request.proto";
import "pkg/queue/proto/purge_response.proto";
import "pkg/queue/proto/reset_queue_stats_request.proto";
import "pkg/queue/proto/reset_queue_stats_response.proto";
import "pkg/queue/proto/resume_queue_request.proto";
import "pkg/queue/proto/resume_queue_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Administrative service for queue management operations
service QueueAdminService {
  // Create a new queue
  rpc CreateQueue(CreateQueueRequest) returns (CreateQueueResponse);

  // Delete a queue/topic
  rpc DeleteTopic(DeleteTopicRequest) returns (DeleteTopicResponse);

  // Get queue information
  rpc GetQueueInfo(GetQueueInfoRequest) returns (GetQueueInfoResponse);

  // Pause queue operations
  rpc PauseQueue(PauseQueueRequest) returns (PauseQueueResponse);

  // Resume queue operations
  rpc ResumeQueue(ResumeQueueRequest) returns (ResumeQueueResponse);

  // Purge queue contents
  rpc PurgeQueue(PurgeRequest) returns (PurgeResponse);

  // Reset queue statistics
  rpc ResetQueueStats(ResetQueueStatsRequest) returns (ResetQueueStatsResponse);
}

```

---

### queue_monitoring_service.proto {#queue_monitoring_service}

**Path**: `pkg/queue/proto/queue_monitoring_service.proto` **Package**:
`gcommon.v1.queue` **Lines**: 174

**Messages** (9): `GetQueueHealthRequest`, `GetQueueHealthResponse`,
`QueueHealth`, `ClusterHealth`, `GetQueueStatsRequest`, `QueueStatsResponse`,
`QueueStatsPoint`, `StreamMetricsRequest`, `MetricsEvent`

**Services** (1): `QueueMonitoringService`

**Imports** (12):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/queue/proto/cluster_info.proto` → [queue_1](./queue_1.md#cluster_info)
- `pkg/queue/proto/get_cluster_info_request.proto` →
  [queue_api_1](./queue_api_1.md#get_cluster_info_request)
- `pkg/queue/proto/get_cluster_info_response.proto` →
  [queue_api_1](./queue_api_1.md#get_cluster_info_response)
- `pkg/queue/proto/get_queue_stats_response.proto` →
  [queue_api_2](./queue_api_2.md#get_queue_stats_response)
- `pkg/queue/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)
- `pkg/queue/proto/metric_type.proto` → [metrics_1](./metrics_1.md#metric_type)
  → [queue_1](./queue_1.md#metric_type)
- `pkg/queue/proto/stats_granularity.proto` →
  [queue_2](./queue_2.md#stats_granularity)
- `pkg/queue/proto/time_range.proto` → [common](./common.md#time_range) →
  [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)
- `pkg/queue/proto/topic_info.proto` → [queue_2](./queue_2.md#topic_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/services/queue_monitoring_service.proto
// file: queue/proto/services/queue_monitoring_service.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d
//
// Service definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/time_range.proto";
import "pkg/queue/proto/cluster_info.proto";
import "pkg/queue/proto/get_cluster_info_request.proto";
import "pkg/queue/proto/get_cluster_info_response.proto";
import "pkg/queue/proto/get_queue_stats_response.proto";
import "pkg/queue/proto/health_status.proto";
import "pkg/queue/proto/metric_type.proto";
import "pkg/queue/proto/stats_granularity.proto";
import "pkg/queue/proto/time_range.proto";
import "pkg/queue/proto/topic_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Service for monitoring queue health, performance, and statistics.
 * Provides read-only access to queue metrics and operational data.
 */
service QueueMonitoringService {
  // Get information about the queue cluster
  rpc GetClusterInfo(GetClusterInfoRequest) returns (gcommon.v1.queue.GetClusterInfoResponse);

  // Get health status of all queues
  rpc GetQueueHealth(GetQueueHealthRequest) returns (GetQueueHealthResponse);

  // Get detailed statistics for a specific queue
  rpc GetQueueStats(GetQueueStatsRequest) returns (QueueStatsResponse);

  // Get real-time metrics stream
  rpc StreamMetrics(StreamMetricsRequest) returns (stream MetricsEvent);
}

/**
 * Request to get queue health information.
 */
message GetQueueHealthRequest {
  // Specific queue names to check (empty = all queues)
  repeated string queue_names = 1;

  // Whether to include detailed health metrics
  bool include_details = 2;
}

/**
 * Response containing queue health information.
 */
message GetQueueHealthResponse {
  // Health status for each queue
  repeated QueueHealth queue_health = 1;

  // Overall cluster health
  ClusterHealth cluster_health = 2;
}

/**
 * Health status for a single queue.
 */
message QueueHealth {
  // Name of the queue
  string queue_name = 1;

  // Health status
  gcommon.v1.queue.HealthStatus status = 2;

  // Health score (0-100)
  int32 health_score = 3;

  // List of health issues
  repeated string issues = 4;

  // Last health check timestamp
  google.protobuf.Timestamp last_check = 5;
}

/**
 * Overall cluster health information.
 */
message ClusterHealth {
  // Overall health status
  gcommon.v1.queue.HealthStatus status = 1;

  // Number of healthy nodes
  int32 healthy_nodes = 2;

  // Total number of nodes
  int32 total_nodes = 3;

  // Health issues affecting the cluster
  repeated string issues = 4;
}

/**
 * Request to get queue statistics.
 */
message GetQueueStatsRequest {
  // Name of the queue
  string queue_name = 1;

  // Time range for statistics
  TimeRange time_range = 2;

  // Granularity of statistics (hourly, daily, etc.)
  StatsGranularity granularity = 3;
}

/**
 * Response containing queue statistics from monitoring service.
 */
message QueueStatsResponse {
  // Queue statistics
  QueueStats stats = 1;

  // Time series data
  repeated QueueStatsPoint time_series = 2;
}

/**
 * Point-in-time queue statistics.
 */
message QueueStatsPoint {
  // Timestamp for this data point
  google.protobuf.Timestamp timestamp = 1;

  // Statistics at this point in time
  QueueStats stats = 2;
}

/**
 * Request to stream real-time metrics.
 */
message StreamMetricsRequest {
  // Queue names to monitor (empty = all queues)
  repeated string queue_names = 1;

  // Types of metrics to include
  repeated MetricType metric_types = 2;

  // Streaming interval in seconds
  int32 interval_seconds = 3;
}

/**
 * Real-time metrics event.
 */
message MetricsEvent {
  // Timestamp of the event
  google.protobuf.Timestamp timestamp = 1;

  // Queue name
  string queue_name = 2;

  // Type of metric
  MetricType metric_type = 3;

  // Metric value
  double value = 4;

  // Additional metadata
  map<string, string> labels = 5;
}

```

---

### queue_service.proto {#queue_service}

**Path**: `pkg/queue/proto/queue_service.proto` **Package**: `gcommon.v1.queue`
**Lines**: 32

**Services** (1): `QueueManagementService`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/services/queue_service.proto
// version: 1.0.0
// guid: 6b8d9e0f-5c7a-4e3d-9f8e-7d6c5b4a3e2d

// QueueService definition
//
// This file implements the 1-1-1 pattern for service definitions.
// NOTE: The main QueueService is defined in pkg/queue/proto/queue.proto
// This file is reserved for future additional queue services or service extensions.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Future queue service extensions can be defined here
// The main QueueService is defined in queue.proto to avoid duplication

// Example additional service for queue management:
/*
   service QueueManagementService {
     // Administrative operations
     rpc CreateQueue(CreateQueueRequest) returns (CreateQueueResponse);
     rpc DeleteQueue(DeleteQueueRequest) returns (DeleteQueueResponse);
     rpc ListQueues(ListQueuesRequest) returns (ListQueuesResponse);
   }
*/

```

---
