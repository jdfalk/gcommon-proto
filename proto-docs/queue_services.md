# queue_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 6
- **Messages**: 2
- **Services**: 4
- **Enums**: 0

## Files in this Module

- [external_auth_service.proto](#external_auth_service)
- [key_validation_service.proto](#key_validation_service)
- [queue_admin_service.proto](#queue_admin_service)
- [queue_monitoring_service.proto](#queue_monitoring_service)
- [queue_service.proto](#queue_service)
- [workflow_service.proto](#workflow_service)
---


## Detailed Documentation

### external_auth_service.proto {#external_auth_service}

**Path**: `gcommon/v1/queue/external_auth_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `ExternalAuthService`

**Imports** (4):

- `gcommon/v1/queue/auth_cache_config.proto`
- `gcommon/v1/queue/retry_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/external_auth_service.proto
// version: 1.0.0
// guid: 888d52ef-a351-4fe1-a31e-6d7085e83b26

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/auth_cache_config.proto";
import "gcommon/v1/queue/retry_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ExternalAuthService {
  // Enable external authorization
  bool enabled = 1;

  // Authorization service endpoint
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Request timeout (milliseconds)
  int32 timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Retry configuration - references existing RetryConfig
  QueueRetryConfig retry_config = 4;

  // Cache configuration
  AuthCacheConfig cache_config = 5;

  // Headers to include in authorization requests
  map<string, string> request_headers = 6;
}
```

---

### key_validation_service.proto {#key_validation_service}

**Path**: `gcommon/v1/queue/key_validation_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `KeyValidationService`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/key_validation_service.proto
// version: 1.0.0
// guid: 796890cb-3593-41dc-bd46-52b840d476a4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message KeyValidationService {
  // Service type (local, external, etc.)
  string service_type = 1 [(buf.validate.field).string.min_len = 1];

  // Service endpoint (for external validation)
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Timeout for validation requests (milliseconds)
  int32 timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Cache TTL for validation results (seconds)
  int32 cache_ttl_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

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

