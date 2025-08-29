# Queue Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 4
- **Services**: 4

## Table of Contents

### Services

- [`QueueAdminService`](#queue_admin_service) - from queue_admin_service.proto
- [`QueueMonitoringService`](#queue_monitoring_service) - from queue_monitoring_service.proto
- [`QueueService`](#queue_service) - from queue_service.proto
- [`WorkflowService`](#workflow_service) - from workflow_service.proto

### Files in this Module

- [queue_admin_service.proto](#queue_admin_service)
- [queue_monitoring_service.proto](#queue_monitoring_service)
- [queue_service.proto](#queue_service)
- [workflow_service.proto](#workflow_service)

---


## Services Documentation

### queue_admin_service.proto {#queue_admin_service}

**Path**: `gcommon/v1/queue/queue_admin_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Services** (1): `QueueAdminService`

**Imports** (13):

- `gcommon/v1/queue/create_queue_request.proto`
- `gcommon/v1/queue/create_queue_response.proto`
- `gcommon/v1/queue/delete_topic_request.proto`
- `gcommon/v1/queue/delete_topic_response.proto`
- `gcommon/v1/queue/pause_queue_request.proto`
- `gcommon/v1/queue/pause_queue_response.proto`
- `gcommon/v1/queue/purge_request.proto`
- `gcommon/v1/queue/purge_response.proto`
- `gcommon/v1/queue/reset_queue_stats_request.proto`
- `gcommon/v1/queue/reset_queue_stats_response.proto`
- `gcommon/v1/queue/resume_queue_request.proto`
- `gcommon/v1/queue/resume_queue_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_admin_service.proto
// version: 1.0.1
// guid: b54b440b-f4c1-40fc-a40f-8b4c0626fc32
// Administrative service for queue management

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/create_queue_request.proto";
import "gcommon/v1/queue/create_queue_response.proto";
import "gcommon/v1/queue/delete_topic_request.proto";
import "gcommon/v1/queue/delete_topic_response.proto";
import "gcommon/v1/queue/pause_queue_request.proto";
import "gcommon/v1/queue/pause_queue_response.proto";
import "gcommon/v1/queue/purge_request.proto";
import "gcommon/v1/queue/purge_response.proto";
import "gcommon/v1/queue/reset_queue_stats_request.proto";
import "gcommon/v1/queue/reset_queue_stats_response.proto";
import "gcommon/v1/queue/resume_queue_request.proto";
import "gcommon/v1/queue/resume_queue_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Administrative service for queue management operations
service QueueAdminService {
  // Create a new queue
  rpc CreateQueue(CreateQueueRequest) returns (CreateQueueResponse);

  // Delete a queue/topic
  rpc DeleteTopic(DeleteTopicRequest) returns (DeleteTopicResponse);

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

**Path**: `gcommon/v1/queue/queue_monitoring_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Services** (1): `QueueMonitoringService`

**Imports** (9):

- `gcommon/v1/queue/get_cluster_info_request.proto`
- `gcommon/v1/queue/get_cluster_info_response.proto`
- `gcommon/v1/queue/get_queue_health_request.proto`
- `gcommon/v1/queue/get_queue_health_response.proto`
- `gcommon/v1/queue/get_queue_stats_request.proto`
- `gcommon/v1/queue/metrics_event.proto`
- `gcommon/v1/queue/queue_stats_response.proto`
- `gcommon/v1/queue/stream_metrics_request.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_monitoring_service.proto
// version: 1.0.1
// guid: 63f72754-e7c0-40b6-a40d-29f3645d55fc

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/get_cluster_info_request.proto";
import "gcommon/v1/queue/get_cluster_info_response.proto";
import "gcommon/v1/queue/get_queue_health_request.proto";
import "gcommon/v1/queue/get_queue_health_response.proto";
import "gcommon/v1/queue/get_queue_stats_request.proto";
import "gcommon/v1/queue/metrics_event.proto";
import "gcommon/v1/queue/queue_stats_response.proto";
import "gcommon/v1/queue/stream_metrics_request.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

service QueueMonitoringService {
  // Get information about the queue cluster
  rpc GetClusterInfo(GetClusterInfoRequest) returns (GetClusterInfoResponse);

  // Get health status of all queues
  rpc GetQueueHealth(GetQueueHealthRequest) returns (GetQueueHealthResponse);

  // Get detailed statistics for a specific queue
  rpc GetQueueStats(GetQueueStatsRequest) returns (QueueStatsResponse);

  // Get real-time metrics stream
  rpc StreamMetrics(QueueStreamMetricsRequest) returns (stream MetricsEvent);
}
```

---

### queue_service.proto {#queue_service}

**Path**: `gcommon/v1/queue/queue_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Services** (1): `QueueService`

**Imports** (13):

- `gcommon/v1/queue/dequeue_request.proto`
- `gcommon/v1/queue/dequeue_response.proto`
- `gcommon/v1/queue/enqueue_request.proto`
- `gcommon/v1/queue/enqueue_response.proto`
- `gcommon/v1/queue/get_queue_info_request.proto`
- `gcommon/v1/queue/get_queue_info_response.proto`
- `gcommon/v1/queue/peek_request.proto`
- `gcommon/v1/queue/peek_response.proto`
- `gcommon/v1/queue/publish_request.proto`
- `gcommon/v1/queue/publish_response.proto`
- `gcommon/v1/queue/subscribe_request.proto`
- `gcommon/v1/queue/subscribe_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_service.proto
// version: 1.0.1
// guid: 1f2e3d4c-5b6a-7980-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/dequeue_request.proto";
import "gcommon/v1/queue/dequeue_response.proto";
import "gcommon/v1/queue/enqueue_request.proto";
import "gcommon/v1/queue/enqueue_response.proto";
import "gcommon/v1/queue/get_queue_info_request.proto";
import "gcommon/v1/queue/get_queue_info_response.proto";
import "gcommon/v1/queue/peek_request.proto";
import "gcommon/v1/queue/peek_response.proto";
import "gcommon/v1/queue/publish_request.proto";
import "gcommon/v1/queue/publish_response.proto";
import "gcommon/v1/queue/subscribe_request.proto";
import "gcommon/v1/queue/subscribe_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * QueueService provides core queue operations for message handling,
 * task distribution, and asynchronous processing.
 */
service QueueService {
  // Enqueue a message or task
  rpc Enqueue(EnqueueRequest) returns (EnqueueResponse);

  // Dequeue a message or task
  rpc Dequeue(DequeueRequest) returns (DequeueResponse);

  // Peek at the next message without removing it
  rpc Peek(PeekRequest) returns (PeekResponse);

  // Get information about a queue
  rpc GetQueueInfo(GetQueueInfoRequest) returns (GetQueueInfoResponse);

  // Subscribe to queue messages (streaming)
  rpc Subscribe(QueueSubscribeRequest) returns (stream SubscribeResponse);

  // Publish message to queue topic
  rpc Publish(QueuePublishRequest) returns (PublishResponse);
}
```

---

### workflow_service.proto {#workflow_service}

**Path**: `gcommon/v1/queue/workflow_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Services** (1): `WorkflowService`

**Imports** (5):

- `gcommon/v1/queue/start_workflow_request.proto`
- `gcommon/v1/queue/start_workflow_response.proto`
- `gcommon/v1/queue/stop_workflow_request.proto`
- `gcommon/v1/queue/stop_workflow_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/workflow_service.proto
// version: 1.0.1
// guid: 6f7e8d9c-0b1a-2534-6e7f-8a9b0c1d2e3f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/start_workflow_request.proto";
import "gcommon/v1/queue/start_workflow_response.proto";
import "gcommon/v1/queue/stop_workflow_request.proto";
import "gcommon/v1/queue/stop_workflow_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * WorkflowService provides workflow management operations for
 * orchestrating complex, multi-step processes.
 */
service WorkflowService {
  // Start a new workflow execution
  rpc StartWorkflow(StartWorkflowRequest) returns (StartWorkflowResponse);

  // Stop a running workflow execution
  rpc StopWorkflow(StopWorkflowRequest) returns (StopWorkflowResponse);
}
```

---

