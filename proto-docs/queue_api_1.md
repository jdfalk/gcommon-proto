# queue_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 58
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 2

## Files in this Module

- [ack_request.proto](#ack_request) ⚠️ 1 issues
- [ack_response.proto](#ack_response) ⚠️ 1 issues
- [acknowledge_request.proto](#acknowledge_request)
- [acknowledge_response.proto](#acknowledge_response)
- [backup_queue_request.proto](#backup_queue_request)
- [backup_queue_response.proto](#backup_queue_response)
- [batch_ack_request.proto](#batch_ack_request)
- [batch_ack_response.proto](#batch_ack_response)
- [batch_nack_request.proto](#batch_nack_request)
- [batch_nack_response.proto](#batch_nack_response)
- [batch_publish_request.proto](#batch_publish_request)
- [batch_publish_response.proto](#batch_publish_response)
- [batch_pull_request.proto](#batch_pull_request)
- [batch_pull_response.proto](#batch_pull_response)
- [commit_offset_request.proto](#commit_offset_request)
- [commit_offset_response.proto](#commit_offset_response)
- [create_queue_request.proto](#create_queue_request)
- [create_queue_response.proto](#create_queue_response)
- [create_subscription_request.proto](#create_subscription_request)
- [create_subscription_response.proto](#create_subscription_response)
- [create_topic_request.proto](#create_topic_request)
- [create_topic_response.proto](#create_topic_response)
- [delete_queue_request.proto](#delete_queue_request)
- [delete_queue_response.proto](#delete_queue_response)
- [delete_request.proto](#delete_request)
- [delete_response.proto](#delete_response)
- [delete_subscription_request.proto](#delete_subscription_request)
- [delete_subscription_response.proto](#delete_subscription_response)
- [delete_topic_request.proto](#delete_topic_request)
- [delete_topic_response.proto](#delete_topic_response)
- [dequeue_request.proto](#dequeue_request)
- [dequeue_response.proto](#dequeue_response)
- [enqueue_request.proto](#enqueue_request)
- [enqueue_response.proto](#enqueue_response)
- [export_queue_request.proto](#export_queue_request)
- [export_queue_response.proto](#export_queue_response)
- [flush_queue_request.proto](#flush_queue_request)
- [flush_queue_response.proto](#flush_queue_response)
- [get_cluster_info_request.proto](#get_cluster_info_request)
- [get_cluster_info_response.proto](#get_cluster_info_response)
- [get_message_request.proto](#get_message_request)
- [get_message_response.proto](#get_message_response)
- [get_node_info_request.proto](#get_node_info_request)
- [get_node_info_response.proto](#get_node_info_response)
- [get_offset_request.proto](#get_offset_request)
- [get_offset_response.proto](#get_offset_response)
- [get_partition_info_request.proto](#get_partition_info_request)
- [get_partition_info_response.proto](#get_partition_info_response)
- [get_queue_info_request.proto](#get_queue_info_request)
- [get_queue_info_response.proto](#get_queue_info_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)
- [queue_2](./queue_2.md)
- [queue_config](./queue_config.md)

**Modules that depend on this one**:

- [cache_services](./cache_services.md)
- [queue_services](./queue_services.md)

---

## Detailed Documentation

### ack_request.proto {#ack_request}

**Path**: `pkg/queue/proto/ack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `AckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 5: Implementation needed - // removes it from the queue. This file was previously a placeholder

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/ack_request.proto
// version: 1.0.0
// guid: 3a91b3b5-86fd-443c-876b-5b7b4da2fa73
// AckRequest acknowledges successful processing of a message and
// removes it from the queue. This file was previously a placeholder
// and now contains the full request definition following the 1-1-1
// protobuf pattern.
// AckRequest contains the information required to acknowledge a
// single message. The receipt handle is provided by the queue when
// the message is received.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message AckRequest {
  // Name of the queue containing the message.
  string queue_name = 1;

  // Receipt handle identifying the message instance.
  string receipt_handle = 2;

  // Standard request metadata including authentication and tracing.
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### ack_response.proto {#ack_response}

**Path**: `pkg/queue/proto/ack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `AckResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### ⚠️ Issues Found (1)

- Line 6: Implementation needed - // successfully processed. This replaces the previous placeholder

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/ack_response.proto
// version: 1.0.0
// guid: e0629319-177a-44c0-9ec6-f97c73c03cbc

// AckResponse indicates whether a message acknowledgment was
// successfully processed. This replaces the previous placeholder
// created during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// AckResponse is returned after successfully acknowledging a message.
// If `success` is false, the `error` field contains additional
// information about why the acknowledgment failed.
message AckResponse {
  // True if the message was removed from the queue.
  bool success = 1;

  // Optional error information when success is false.
  gcommon.v1.common.Error error = 2;
}

```

---

### acknowledge_request.proto {#acknowledge_request}

**Path**: `pkg/queue/proto/acknowledge_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 83

**Messages** (1): `AcknowledgeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/acknowledge_request.proto
// version: 1.0.0
// guid: 3f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * AcknowledgeRequest confirms successful processing of one or more messages.
 * Once acknowledged, messages are permanently removed from the queue
 * and will not be redelivered.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AcknowledgeRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue containing the messages.
   * Must match the queue from which messages were dequeued.
   */
  string queue_name = 1;

  /**
   * Receipt handles of messages to acknowledge.
   * These handles were provided in the DequeueResponse.
   */
  repeated string receipt_handles = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Consumer ID that processed these messages.
   * Used for tracking and metrics.
   */
  string consumer_id = 12;

  /**
   * Processing result for each message (same order as receipt_handles).
   * Valid values: "success", "failed", "retry", "skip".
   * If not provided, "success" is assumed for all messages.
   */
  repeated string processing_results = 13;

  /**
   * Optional processing notes or error details for each message.
   * Useful for debugging and audit trails.
   */
  repeated string processing_notes = 14;

  /**
   * Processing time in milliseconds for each message.
   * Used for performance monitoring and SLA tracking.
   */
  repeated int64 processing_times_ms = 15;

  /**
   * Whether to force acknowledgment even if visibility timeout expired.
   * Use with caution as it may cause duplicate processing. Default: false.
   */
  bool force_acknowledge = 16;

  /**
   * Batch acknowledgment mode. If true, all messages succeed or fail together.
   * If false, each message is processed individually. Default: false.
   */
  bool batch_mode = 17;
}

```

---

### acknowledge_response.proto {#acknowledge_response}

**Path**: `pkg/queue/proto/acknowledge_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 146

**Messages** (2): `MessageAckResult`, `AcknowledgeResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/acknowledge_response.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * MessageAckResult represents the acknowledgment result for a single message.
 * Contains success status and any error information for individual messages
 * within a batch acknowledgment request.
 */
message MessageAckResult {
  /**
   * Receipt handle of the message this result applies to.
   */
  string receipt_handle = 1;

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
  string message_id = 4;

  /**
   * Processing result that was recorded (echoed from request).
   */
  string processing_result = 5;
}

/**
 * AcknowledgeResponse confirms the acknowledgment of processed messages.
 * Returns success status for each message and overall operation metrics
 * for monitoring and debugging.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AcknowledgeResponse {
  // Required fields (1-10)

  /**
   * Overall success status of the acknowledgment operation.
   * True if all messages were successfully acknowledged.
   */
  bool success = 1;

  /**
   * Number of messages that were successfully acknowledged.
   */
  int32 acknowledged_count = 2;

  /**
   * Number of messages that failed to be acknowledged.
   */
  int32 failed_count = 3;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue where messages were acknowledged.
   * Echoed from the request for verification.
   */
  string queue_name = 12;

  /**
   * Detailed results for each message acknowledgment.
   * Only populated if there were failures or if detailed results were requested.
   */
  repeated MessageAckResult message_results = 13;

  /**
   * Consumer ID that was used for acknowledgment.
   * Echoed from the request for verification.
   */
  string consumer_id = 14;

  /**
   * Total processing time for the acknowledgment operation in milliseconds.
   */
  int64 operation_time_ms = 15;

  /**
   * Whether the operation was completed in batch mode.
   * Echoed from the request for verification.
   */
  bool batch_mode = 16;

  /**
   * Number of messages that were already acknowledged (duplicates).
   * These don't count as failures but indicate potential issues.
   */
  int32 already_acknowledged_count = 17;

  /**
   * Number of messages with expired visibility timeouts.
   * These may have been redelivered to other consumers.
   */
  int32 expired_timeout_count = 18;

  // Status and error fields (61-70)

  /**
   * Error information if the overall acknowledgment operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the acknowledgment operation was processed.
   */
  google.protobuf.Timestamp acknowledged_at = 51;

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}

```

---

### backup_queue_request.proto {#backup_queue_request}

**Path**: `pkg/queue/proto/backup_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `BackupQueueRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/backup_queue_request.proto
// version: 1.0.0
// Request to backup a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to backup a queue
message BackupQueueRequest {
  // Queue name to backup
  string queue_name = 1;

  // Backup destination path
  string backup_path = 2;

  // Include message data
  bool include_messages = 3;

  // Include metadata only
  bool metadata_only = 4;

  // Backup format (JSON, binary, etc.)
  string format = 5;

  // Compression type (none, gzip, etc.)
  string compression = 6;

  // Start timestamp for backup range
  int64 start_timestamp = 7;

  // End timestamp for backup range
  int64 end_timestamp = 8;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 9;
}

```

---

### backup_queue_response.proto {#backup_queue_response}

**Path**: `pkg/queue/proto/backup_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `BackupQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/backup_queue_response.proto
// version: 1.0.0
// Response for queue backup operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue backup operations
message BackupQueueResponse {
  // Whether the backup was successful
  bool success = 1;

  // Backup file path or identifier
  string backup_location = 2;

  // Number of messages backed up
  int64 messages_backed_up = 3;

  // Size of backup in bytes
  int64 backup_size_bytes = 4;

  // Backup duration (milliseconds)
  int32 backup_duration_ms = 5;

  // Backup checksum for integrity verification
  string checksum = 6;

  // Backup timestamp
  int64 backup_timestamp = 7;

  // Error message if backup failed
  string error = 8;
}

```

---

### batch_ack_request.proto {#batch_ack_request}

**Path**: `pkg/queue/proto/batch_ack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `BatchAckRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/batch_ack_request.proto
// version: 1.0.0
// Request for batch acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request for batch acknowledgment operations
message BatchAckRequest {
  // List of message IDs to acknowledge
  repeated string message_ids = 1;

  // Consumer group ID
  string consumer_group_id = 2;

  // Subscription ID
  string subscription_id = 3;

  // Acknowledgment level
  string ack_level = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}

```

---

### batch_ack_response.proto {#batch_ack_response}

**Path**: `pkg/queue/proto/batch_ack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (2): `BatchAckResponse`, `FailedAck`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/batch_ack_response.proto
// version: 1.0.0
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for batch acknowledgment operations.
 * Contains results of acknowledging multiple messages.
 */
message BatchAckResponse {
  // Overall success status
  bool success = 1;

  // Number of messages successfully acknowledged
  int32 acknowledged_count = 2;

  // Number of messages that failed to acknowledge
  int32 failed_count = 3;

  // Failed message IDs and their error reasons
  repeated FailedAck failed_acks = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;

  // Batch ID for tracking
  string batch_id = 6;
}

/**
 * Information about a failed acknowledgment.
 */
message FailedAck {
  // Message ID that failed to acknowledge
  string message_id = 1;

  // Reason for acknowledgment failure
  string error_reason = 2;

  // Error code
  string error_code = 3;
}

```

---

### batch_nack_request.proto {#batch_nack_request}

**Path**: `pkg/queue/proto/batch_nack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 77

**Messages** (2): `BatchNackRequest`, `MessageNack`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/nack_error_category.proto` → [queue_1](./queue_1.md#nack_error_category)

#### Source Code

```protobuf
// file: pkg/queue/proto/batch_nack_request.proto
// version: 1.1.0
// Request to negative acknowledge multiple messages in batch

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/nack_error_category.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// BatchNackRequest negatively acknowledges multiple messages at once
message BatchNackRequest {
  // Consumer group ID performing the nack
  string consumer_group_id = 1;

  // Consumer ID within the group
  string consumer_id = 2;

  // Messages to negative acknowledge
  repeated MessageNack message_nacks = 3;

  // Requeue messages after nack
  bool requeue_messages = 4;

  // Delay before requeuing (milliseconds)
  int64 requeue_delay_ms = 5;

  // Maximum number of requeue attempts
  int32 max_requeue_attempts = 6;

  // Send failed messages to dead letter queue
  bool send_to_dlq = 7;

  // Reason for batch nack operation
  string nack_reason = 8;

  // Additional metadata for the nack operation
  map<string, string> metadata = 9;
}

// Individual message negative acknowledgment
message MessageNack {
  // Message identifier
  string message_id = 1;

  // Message delivery tag
  string delivery_tag = 2;

  // Partition ID containing the message
  int32 partition_id = 3;

  // Message offset
  int64 message_offset = 4;

  // Reason for negative acknowledgment
  string nack_reason = 5;

  // Error category for the nack
  NackErrorCategory error_category = 6;

  // Specific error code
  string error_code = 7;

  // Retry this specific message
  bool retry_message = 8;

  // Custom retry delay for this message (milliseconds)
  int64 retry_delay_ms = 9;

  // Message-specific metadata
  map<string, string> message_metadata = 10;
}

```

---

### batch_nack_response.proto {#batch_nack_response}

**Path**: `pkg/queue/proto/batch_nack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `BatchNackResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/batch_nack_response.proto
// version: 1.0.0
// Response for batch negative acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for batch negative acknowledgment operations
message BatchNackResponse {
  // Number of messages successfully nacked
  int32 successful_count = 1;

  // Number of messages that failed to nack
  int32 failed_count = 2;

  // List of message IDs that were successfully nacked
  repeated string successful_message_ids = 3;

  // List of message IDs that failed to nack
  repeated string failed_message_ids = 4;

  // Error messages for failed nacks (indexed by failed_message_ids)
  repeated string error_messages = 5;

  // Overall operation error if any
  string error = 6;
}

```

---

### batch_publish_request.proto {#batch_publish_request}

**Path**: `pkg/queue/proto/batch_publish_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `BatchPublishRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/batch_publish_request.proto
// version: 1.0.0
// guid: e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/queue_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to publish multiple messages to a queue in a single operation.
 * Provides better performance for high-throughput scenarios.
 */
message BatchPublishRequest {
  // Queue name to publish messages to
  string queue_name = 1;

  // Messages to publish
  repeated gcommon.v1.queue.QueueMessage messages = 2;

  // Whether to use a transaction for the batch
  bool use_transaction = 3;

  // Timeout for the batch operation (milliseconds)
  int32 timeout_ms = 4;

  // Whether to wait for acknowledgment from all brokers
  bool wait_for_all = 5;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;

  // Maximum number of retries for failed messages
  int32 max_retries = 7;

  // Batch ID for tracking (optional)
  string batch_id = 8;
}

```

---

### batch_publish_response.proto {#batch_publish_response}

**Path**: `pkg/queue/proto/batch_publish_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `BatchPublishResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/publish_result.proto` → [queue_1](./queue_1.md#publish_result)

#### Source Code

```protobuf
// file: pkg/queue/proto/batch_publish_response.proto
// version: 1.0.0
// Response for batch publish operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/publish_result.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for batch publish operations
message BatchPublishResponse {
  // Results for each published message
  repeated PublishResult results = 1;

  // Total number of messages attempted
  int32 total_attempted = 2;

  // Number of successful publishes
  int32 successful_count = 3;

  // Number of failed publishes
  int32 failed_count = 4;

  // Overall error message if any
  string error = 5;
}

```

---

### batch_pull_request.proto {#batch_pull_request}

**Path**: `pkg/queue/proto/batch_pull_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `BatchPullRequest`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/batch_pull_request.proto
// file: queue/proto/requests/batch_pull_request.proto
// version: 1.0.0
// guid: 7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to pull multiple messages from a queue in a single operation.
 */
message BatchPullRequest {
  // Name of the queue to pull from
  string queue_name = 1;

  // Maximum number of messages to pull
  uint32 max_messages = 2;

  // Maximum time to wait for messages
  google.protobuf.Duration wait_timeout = 3;

  // Whether to acknowledge messages automatically
  bool auto_acknowledge = 4;

  // Consumer group ID (optional)
  string consumer_group = 5;

  // Subscription name (optional)
  string subscription = 6;

  // Maximum payload size in bytes
  uint64 max_payload_size = 7;
}

```

---

### batch_pull_response.proto {#batch_pull_response}

**Path**: `pkg/queue/proto/batch_pull_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `BatchPullResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/batch_pull_response.proto
// file: queue/proto/responses/batch_pull_response.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d
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
 * Response for batch pull operations containing multiple messages.
 */
message BatchPullResponse {
  // List of messages pulled from the queue
  repeated gcommon.v1.queue.QueueMessage messages = 1;

  // Total number of messages retrieved
  uint32 message_count = 2;

  // Whether more messages are available
  bool has_more = 3;

  // Next token for pagination
  string next_token = 4;

  // Total bytes of message payloads
  uint64 total_bytes = 5;
}

```

---

### commit_offset_request.proto {#commit_offset_request}

**Path**: `pkg/queue/proto/commit_offset_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `CommitOffsetRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/commit_offset_request.proto
// version: 1.0.0
// guid: dd17ade2-5399-4fe8-83ba-ffe1227da728
// CommitOffsetRequest records the latest processed offset for a
// consumer group. This allows the queue provider to resume message
// delivery from the correct position on reconnect.
// CommitOffsetRequest stores the offset a consumer has successfully
// processed within a queue or topic.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message CommitOffsetRequest {
  // Name of the queue or topic.
  string queue_name = 1;

  // Identifier for the consumer group.
  string consumer_group = 2;

  // Offset that was last processed successfully.
  int64 offset = 3;

  // Optional request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### commit_offset_response.proto {#commit_offset_response}

**Path**: `pkg/queue/proto/commit_offset_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 71

**Messages** (2): `CommitOffsetResponse`, `PartitionCommitResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/commit_offset_response.proto
// version: 1.1.0
// Response to offset commit operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// CommitOffsetResponse returns the result of committing consumer offsets
message CommitOffsetResponse {
  // Overall success status
  bool success = 1;

  // Error message if commit failed
  string error_message = 2;

  // Error code for programmatic handling
  string error_code = 3;

  // Results for each partition commit
  repeated PartitionCommitResult partition_results = 4;

  // Total number of offsets committed
  int32 committed_count = 5;

  // Total number of failed commits
  int32 failed_count = 6;

  // Commit timestamp
  google.protobuf.Timestamp commit_timestamp = 7;

  // Consumer group generation at time of commit
  int64 consumer_generation = 8;

  // Additional metadata about the commit operation
  map<string, string> metadata = 9;
}

// Result of committing offset for a specific partition
message PartitionCommitResult {
  // Partition ID
  int32 partition_id = 1;

  // Success status for this partition
  bool success = 2;

  // Committed offset value
  int64 committed_offset = 3;

  // Previous offset before commit
  int64 previous_offset = 4;

  // Error message if commit failed for this partition
  string error_message = 5;

  // Error code for this partition
  string error_code = 6;

  // Timestamp when this offset was committed
  google.protobuf.Timestamp commit_timestamp = 7;

  // Metadata for this partition commit
  map<string, string> partition_metadata = 8;
}

```

---

### create_queue_request.proto {#create_queue_request}

**Path**: `pkg/queue/proto/create_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `CreateQueueRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/queue_config.proto` → [queue_config](./queue_config.md#queue_config)

#### Source Code

```protobuf
// file: pkg/queue/proto/create_queue_request.proto
// version: 1.0.0
// guid: c6d7e8f9-a0b1-2c3d-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/queue_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to create a new queue.
 * Defines the queue name and configuration parameters.
 */
message CreateQueueRequest {
  // Name of the queue to create (required)
  string queue_name = 1;

  // Configuration for the new queue
  gcommon.v1.queue.QueueConfig config = 2;

  // Whether to create the queue even if it already exists
  bool if_not_exists = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Tags to associate with the queue
  map<string, string> tags = 5;

  // Description of the queue
  string description = 6;
}

```

---

### create_queue_response.proto {#create_queue_response}

**Path**: `pkg/queue/proto/create_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `CreateQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/create_queue_response.proto
// version: 1.0.0
// Response for queue creation operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue creation operations
message CreateQueueResponse {
  // Whether the queue was successfully created
  bool success = 1;

  // Name of the created queue
  string queue_name = 2;

  // Queue endpoint URL
  string queue_endpoint = 3;

  // Number of partitions created
  int32 partition_count = 4;

  // Queue configuration that was applied
  map<string, string> applied_config = 5;

  // Error message if creation failed
  string error = 6;
}

```

---

### create_subscription_request.proto {#create_subscription_request}

**Path**: `pkg/queue/proto/create_subscription_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `CreateSubscriptionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/subscription_config.proto` → [queue_config](./queue_config.md#subscription_config)

#### Source Code

```protobuf
// file: pkg/queue/proto/create_subscription_request.proto
// version: 1.0.0
// Request to create a new subscription

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/subscription_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to create a new subscription
message CreateSubscriptionRequest {
  // Subscription name
  string subscription_name = 1;

  // Topic to subscribe to
  string topic = 2;

  // Consumer group ID
  string consumer_group_id = 3;

  // Subscription configuration
  SubscriptionConfig config = 4;

  // Starting position (earliest, latest, or specific offset)
  string start_position = 5;

  // Specific offset (if start_position is "offset")
  int64 start_offset = 6;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 7;
}

```

---

### create_subscription_response.proto {#create_subscription_response}

**Path**: `pkg/queue/proto/create_subscription_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `CreateSubscriptionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/create_subscription_response.proto
// file: queue/proto/responses/create_subscription_response.proto
// version: 1.0.0
// guid: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for creating a subscription.
 */
message CreateSubscriptionResponse {
  // Whether the subscription was created successfully
  bool success = 1;

  // Error message if creation failed
  string error_message = 2;

  // ID of the created subscription
  string subscription_id = 3;

  // Name of the created subscription
  string subscription_name = 4;

  // Timestamp when subscription was created
  uint64 created_at = 5;

  // Initial position in the queue
  uint64 initial_position = 6;
}

```

---

### create_topic_request.proto {#create_topic_request}

**Path**: `pkg/queue/proto/create_topic_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `CreateTopicRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/topic_config.proto` → [queue_config](./queue_config.md#topic_config)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/create_topic_request.proto
// file: queue/proto/requests/create_topic_request.proto
// version: 1.0.0
// guid: 3f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/topic_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to create a new topic.
 */
message CreateTopicRequest {
  // Name of the topic to create
  string topic_name = 1;

  // Configuration for the topic
  gcommon.v1.queue.TopicConfig config = 2;

  // Whether the topic should be durable
  bool durable = 3;

  // Whether to auto-delete when unused
  bool auto_delete = 4;

  // Optional arguments for topic creation
  map<string, string> arguments = 5;
}

```

---

### create_topic_response.proto {#create_topic_response}

**Path**: `pkg/queue/proto/create_topic_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `CreateTopicResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/topic_config.proto` → [queue_config](./queue_config.md#topic_config)
- `pkg/queue/proto/topic_info.proto` → [queue_2](./queue_2.md#topic_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/create_topic_response.proto
// file: queue/proto/responses/create_topic_response.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/topic_config.proto";
import "pkg/queue/proto/topic_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for topic creation operations.
 */
message CreateTopicResponse {
  // Information about the created topic
  gcommon.v1.queue.TopicInfo topic_info = 1;

  // Whether the topic was actually created (false if it already existed)
  bool created = 2;

  // Timestamp when the topic was created
  google.protobuf.Timestamp created_at = 3;

  // Any warnings during topic creation
  repeated string warnings = 4;

  // Topic configuration that was applied
  gcommon.v1.queue.TopicConfig applied_config = 5;
}
// This file needs proper implementation

```

---

### delete_queue_request.proto {#delete_queue_request}

**Path**: `pkg/queue/proto/delete_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `DeleteQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/delete_queue_request.proto
// file: queue/proto/requests/delete_queue_request.proto
// version: 1.0.0
// guid: 9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message DeleteQueueRequest {
  // Queue ID or name to delete
  string queue = 1;

  // Force deletion even if not empty
  bool force = 2;

  // Purge messages before deletion
  bool purge_first = 3;
}

/**
 * Request to delete a queue and all its messages.
 * This is a destructive operation that cannot be undone.
 */
// This file needs proper implementation

```

---

### delete_queue_response.proto {#delete_queue_response}

**Path**: `pkg/queue/proto/delete_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `DeleteQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/delete_queue_response.proto
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for deleting a queue.
 * Confirms successful deletion and provides cleanup information.
 */
message DeleteQueueResponse {
  // Whether the queue was successfully deleted
  bool success = 1;

  // Number of messages that were purged during deletion
  int64 purged_messages = 2;

  // Human-readable message describing the deletion result
  string message = 3;
}

```

---

### delete_request.proto {#delete_request}

**Path**: `pkg/queue/proto/delete_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 68

**Messages** (2): `DeleteRequest`, `DeleteCriteria`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/message_state.proto` → [queue_1](./queue_1.md#message_state)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/delete_request.proto
// file: queue/proto/requests/delete_request.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/message_state.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to delete a specific message from a queue.
 */
message DeleteRequest {
  // Name of the queue containing the message
  string queue_name = 1;

  // Unique identifier of the message to delete
  string message_id = 2;

  // Acknowledgment token (if message was previously consumed)
  string ack_token = 3;

  // Whether to force deletion even if message is locked
  bool force = 4;

  // Reason for deletion
  string reason = 5;

  // Delete criteria (alternative to message_id)
  DeleteCriteria criteria = 6;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}

/**
 * Criteria for deleting messages based on conditions.
 */
message DeleteCriteria {
  // Delete messages older than this timestamp
  int64 older_than_timestamp = 1;

  // Delete messages with specific headers
  map<string, string> header_filters = 2;

  // Delete messages with specific priority
  int32 priority = 3;

  // Delete messages with specific correlation ID
  string correlation_id = 4;

  // Maximum number of messages to delete
  int32 max_messages = 5;

  // Delete messages in specific state
  gcommon.v1.queue.MessageState state = 6;
}
// This file needs proper implementation

```

---

### delete_response.proto {#delete_response}

**Path**: `pkg/queue/proto/delete_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 84

**Messages** (3): `DeleteResponse`, `DeletionStats`, `BackupInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/delete_response.proto
// version: 1.1.0
// Response to delete operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// DeleteResponse returns the result of a delete operation
message DeleteResponse {
  // Success status of the delete operation
  bool success = 1;

  // Identifier of the deleted resource
  string deleted_resource_id = 2;

  // Type of resource that was deleted
  string resource_type = 3;

  // Timestamp when deletion completed
  google.protobuf.Timestamp deleted_at = 4;

  // Error message if deletion failed
  string error_message = 5;

  // Error code for programmatic handling
  string error_code = 6;

  // Statistics about the deletion
  DeletionStats deletion_stats = 7;

  // Backup information (if backup was created)
  BackupInfo backup_info = 8;

  // Warning messages
  repeated string warnings = 9;

  // Operation metadata
  map<string, string> metadata = 10;
}

// Statistics about what was deleted
message DeletionStats {
  // Number of messages deleted
  int64 messages_deleted = 1;

  // Amount of data deleted (bytes)
  int64 data_deleted_bytes = 2;

  // Number of subscriptions deleted
  int32 subscriptions_deleted = 3;

  // Number of partitions deleted
  int32 partitions_deleted = 4;

  // Time taken for deletion (milliseconds)
  int64 deletion_duration_ms = 5;
}

// Backup information (if backup was created)
message BackupInfo {
  // Backup identifier
  string backup_id = 1;

  // Backup location
  string backup_location = 2;

  // Backup size (bytes)
  int64 backup_size_bytes = 3;

  // Backup timestamp
  google.protobuf.Timestamp backup_created_at = 4;

  // Backup expiration time
  google.protobuf.Timestamp backup_expires_at = 5;
}
// This file needs proper implementation

```

---

### delete_subscription_request.proto {#delete_subscription_request}

**Path**: `pkg/queue/proto/delete_subscription_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `DeleteSubscriptionRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/delete_subscription_request.proto
// version: 1.0.0
// Request to delete a subscription

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to delete a subscription
message DeleteSubscriptionRequest {
  // Subscription ID to delete
  string subscription_id = 1;

  // Force deletion even if active
  bool force = 2;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 3;
}

```

---

### delete_subscription_response.proto {#delete_subscription_response}

**Path**: `pkg/queue/proto/delete_subscription_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `DeleteSubscriptionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/delete_subscription_response.proto
// version: 1.0.0
// Response for delete subscription operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for deleting a subscription
message DeleteSubscriptionResponse {
  // Whether the subscription was successfully deleted
  bool success = 1;

  // Number of undelivered messages that were purged
  int64 purged_messages = 2;

  // Human-readable message describing the deletion result
  string message = 3;

  // Error message if deletion failed
  string error = 4;
}

```

---

### delete_topic_request.proto {#delete_topic_request}

**Path**: `pkg/queue/proto/delete_topic_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `DeleteTopicRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/delete_topic_request.proto
// version: 1.1.0
// Request to delete a topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message DeleteTopicRequest {
  // Topic ID or name to delete
  string topic = 1;

  // Force deletion even if not empty
  bool force = 2;
}

// DeleteTopicRequest removes a topic and its associated resources
// This file needs proper implementation

```

---

### delete_topic_response.proto {#delete_topic_response}

**Path**: `pkg/queue/proto/delete_topic_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `DeleteTopicResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/delete_topic_response.proto
// version: 1.0.0
// Response for topic deletion operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for deleting a topic
message DeleteTopicResponse {
  // Whether the topic was successfully deleted
  bool success = 1;

  // Number of active subscriptions that were also deleted
  int64 deleted_subscriptions = 2;

  // Number of messages that were purged during deletion
  int64 purged_messages = 3;

  // Human-readable message describing the deletion result
  string message = 4;

  // Error message if deletion failed
  string error = 5;
}

```

---

### dequeue_request.proto {#dequeue_request}

**Path**: `pkg/queue/proto/dequeue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 110

**Messages** (1): `DequeueRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/dequeue_request.proto
// version: 1.0.0
// guid: ce6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

// Standard imports
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * DequeueRequest retrieves one or more messages from a queue.
 * Supports various consumption patterns including polling,
 * long polling, and batch operations.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message DequeueRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue to receive messages from.
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
   * Maximum number of messages to receive in this request.
   * Range: 1-100. Default: 1.
   */
  int32 max_messages = 12;

  /**
   * Visibility timeout - how long the message is hidden from
   * other consumers after being received. Must be acknowledged
   * or rejected within this time. Default: queue configuration.
   */
  google.protobuf.Duration visibility_timeout = 13;

  /**
   * Wait time for long polling. If no messages are available,
   * the request will wait up to this duration for messages
   * to arrive. Set to 0 for immediate return.
   */
  google.protobuf.Duration wait_time = 14;

  /**
   * Message group ID filter. If specified, only messages
   * from this group will be returned. Useful for ordered processing.
   */
  string group_id_filter = 15;

  /**
   * Attribute filters for selective message consumption.
   * Only messages matching all specified attributes will be returned.
   */
  map<string, string> attribute_filters = 16;

  /**
   * Message type filter. If specified, only messages of
   * this type will be returned.
   */
  string message_type_filter = 17;

  /**
   * Consumer ID for tracking and load balancing.
   * Helps with consumer group coordination and metrics.
   */
  string consumer_id = 18;

  /**
   * Include message attributes in the response.
   * Default: true. Set to false to reduce response size.
   */
  bool include_attributes = 19;

  /**
   * Include message metadata (timestamps, delivery count, etc.)
   * in the response. Default: true.
   */
  bool include_metadata = 20;

  /**
   * Peek mode - return messages without removing them from
   * the queue. Useful for inspection. Default: false.
   */
  bool peek_only = 21;

  /**
   * Priority threshold - only return messages with priority
   * greater than or equal to this value. Range: 0-255.
   */
  int32 min_priority = 22;
}

```

---

### dequeue_response.proto {#dequeue_response}

**Path**: `pkg/queue/proto/dequeue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 111

**Messages** (1): `DequeueResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/queue_message.proto` → [queue_2](./queue_2.md#queue_message)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/dequeue_response.proto
// version: 1.0.0
// guid: ea8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

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
 * DequeueResponse returns messages retrieved from a queue.
 * Contains message data, delivery metadata, and operation status
 * for consumption and acknowledgment processing.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message DequeueResponse {
  // Required fields (1-10)

  /**
   * Messages retrieved from the queue.
   * Empty if no messages were available.
   */
  repeated gcommon.v1.queue.QueueMessage messages = 1;

  /**
   * Indicates whether the dequeue operation was successful.
   */
  bool success = 2;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue messages were retrieved from.
   * Echoed from the request for verification.
   */
  string queue_name = 12;

  /**
   * Number of messages that were available but not returned
   * due to max_messages limit.
   */
  int32 messages_remaining = 13;

  /**
   * Approximate number of messages currently in the queue.
   * Useful for monitoring and capacity planning.
   */
  int64 approximate_queue_size = 14;

  /**
   * Consumer ID that was used for this request.
   * Helpful for debugging and load balancing.
   */
  string consumer_id = 15;

  /**
   * Time the request waited for messages (for long polling).
   * Useful for performance monitoring.
   */
  google.protobuf.Timestamp wait_started_at = 16;

  /**
   * Duration the request waited for messages.
   */
  int64 wait_duration_ms = 17;

  /**
   * Indicates if the response was due to wait timeout
   * rather than message availability.
   */
  bool timed_out = 18;

  // Status and error fields (61-70)

  /**
   * Error information if the dequeue operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the dequeue operation started.
   */
  google.protobuf.Timestamp operation_started_at = 51;

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}

```

---

### enqueue_request.proto {#enqueue_request}

**Path**: `pkg/queue/proto/enqueue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 123

**Messages** (1): `EnqueueRequest`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/enqueue_request.proto
// version: 1.0.0
// guid: bd5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * EnqueueRequest adds a message to a queue.
 * Supports both simple message enqueuing and advanced features
 * like scheduling, priority, and message grouping.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message EnqueueRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue to send the message to.
   * Must be a valid queue that exists or will be created.
   */
  string queue_name = 1;

  /**
   * The message payload. Can contain any data type.
   * The receiving application is responsible for deserializing.
   */
  google.protobuf.Any payload = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Message priority (0-255, where 255 is highest priority).
   * Higher priority messages are delivered first. Default: 128.
   */
  int32 priority = 12;

  /**
   * Delay before the message becomes available for consumption.
   * Use for scheduled message delivery.
   */
  google.protobuf.Duration delay = 13;

  /**
   * Message expiration time. Message will be removed if not
   * consumed before this time. If not set, uses queue default.
   */
  google.protobuf.Timestamp expires_at = 14;

  /**
   * Message group ID for ordered processing. Messages with
   * the same group_id are processed in FIFO order.
   */
  string group_id = 15;

  /**
   * Deduplication ID to prevent duplicate message processing.
   * If a message with the same dedup_id is already in the queue,
   * this request will be ignored.
   */
  string deduplication_id = 16;

  /**
   * Maximum number of delivery attempts before the message
   * is moved to dead letter queue. Default: queue configuration.
   */
  int32 max_delivery_attempts = 17;

  /**
   * Custom attributes/headers for the message.
   * Can be used for routing, filtering, or application-specific metadata.
   */
  map<string, string> attributes = 18;

  /**
   * Content type of the payload (e.g., "application/json", "text/plain").
   * Helps consumers understand how to process the message.
   */
  string content_type = 19;

  /**
   * Message source identifier. Useful for tracking which
   * application or service generated the message.
   */
  string source = 20;

  /**
   * Message type/event name. Helps consumers route messages
   * to appropriate handlers.
   */
  string message_type = 21;

  /**
   * Correlation ID for linking related messages across
   * different queues or processing stages.
   */
  string correlation_id = 22;

  /**
   * Reply-to queue name for request-response patterns.
   * If set, response should be sent to this queue.
   */
  string reply_to = 23;
}

```

---

### enqueue_response.proto {#enqueue_response}

**Path**: `pkg/queue/proto/enqueue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 125

**Messages** (1): `EnqueueResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/enqueue_response.proto
// version: 1.0.0
// guid: df7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * EnqueueResponse confirms successful message enqueuing.
 * Returns message identifiers and metadata for tracking
 * and potential message management operations.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message EnqueueResponse {
  // Required fields (1-10)

  /**
   * Unique identifier assigned to the enqueued message.
   * Can be used for message tracking, cancellation, or status queries.
   */
  string message_id = 1;

  /**
   * Indicates whether the message was successfully enqueued.
   * True if the message is now in the queue and will be processed.
   */
  bool success = 2;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue where the message was enqueued.
   * Echoed from the request for verification.
   */
  string queue_name = 12;

  /**
   * MD5 hash of the message payload for integrity verification.
   * Can be used to detect corruption during transmission.
   */
  string payload_md5 = 13;

  /**
   * Size of the enqueued message in bytes.
   * Useful for monitoring and capacity planning.
   */
  int64 message_size = 14;

  /**
   * Position/sequence number of the message in the queue.
   * Useful for ordered queues and processing metrics.
   */
  int64 sequence_number = 15;

  /**
   * Assigned priority of the message (may differ from requested
   * priority due to queue configuration or policy).
   */
  int32 assigned_priority = 16;

  /**
   * Deduplication ID that was used (if any).
   * Helps track duplicate detection results.
   */
  string deduplication_id = 17;

  /**
   * Message group ID that was assigned (if any).
   * Important for ordered processing verification.
   */
  string group_id = 18;

  /**
   * Estimated time when the message will become available
   * for consumption (considering delays).
   */
  google.protobuf.Timestamp available_at = 19;

  /**
   * Message expiration time as stored in the queue.
   * May differ from requested expiration due to queue policies.
   */
  google.protobuf.Timestamp expires_at = 20;

  // Status and error fields (61-70)

  /**
   * Error information if the enqueue operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the message was enqueued.
   * Precise timing for SLA and performance monitoring.
   */
  google.protobuf.Timestamp enqueued_at = 51;

  /**
   * Timestamp when this response was generated.
   * Useful for measuring request processing time.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}

```

---

### export_queue_request.proto {#export_queue_request}

**Path**: `pkg/queue/proto/export_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `ExportQueueRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/export_format.proto` → [metrics_1](./metrics_1.md#export_format) → [queue_1](./queue_1.md#export_format)
- `pkg/queue/proto/time_range.proto` → [common](./common.md#time_range) → [metrics_2](./metrics_2.md#time_range) → [queue_2](./queue_2.md#time_range)

#### Source Code

```protobuf
// file: pkg/queue/proto/requests/export_queue_request.proto
// file: queue/proto/requests/export_queue_request.proto
// version: 1.0.0
// guid: 4a3b2c1d-0e9f-8a7b-6c5d-4e3f2a1b0c9d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/export_format.proto";
import "pkg/queue/proto/time_range.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to export queue data for backup or migration purposes.
 */
message ExportQueueRequest {
  // Name of the queue to export
  string queue_name = 1;

  // Export destination (file path, cloud storage URI, etc.)
  string destination = 2;

  // Export format
  gcommon.v1.queue.ExportFormat format = 3;

  // Whether to include message data or just metadata
  bool include_message_data = 4;

  // Time range for export (optional)
  gcommon.v1.queue.TimeRange time_range = 5;

  // Whether to compress the export
  bool compress = 6;

  // Maximum number of messages to export (0 = no limit)
  int64 max_messages = 7;

  // Export configuration options
  map<string, string> options = 8;
}
// This file needs proper implementation

```

---

### export_queue_response.proto {#export_queue_response}

**Path**: `pkg/queue/proto/export_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `ExportQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/export_queue_response.proto
// version: 1.0.0
// Response for queue export operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue export operations
message ExportQueueResponse {
  // Export job ID
  string export_id = 1;

  // Export status
  string status = 2;

  // File path or URL where export is stored
  string export_path = 3;

  // Number of messages exported
  int64 message_count = 4;

  // Size of exported data in bytes
  int64 data_size_bytes = 5;

  // Export format (JSON, CSV, etc.)
  string format = 6;

  // Start timestamp of exported data
  int64 start_timestamp = 7;

  // End timestamp of exported data
  int64 end_timestamp = 8;

  // Error message if export failed
  string error = 9;
}

```

---

### flush_queue_request.proto {#flush_queue_request}

**Path**: `pkg/queue/proto/flush_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `FlushQueueRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/queue/proto/flush_policy.proto` → [queue_1](./queue_1.md#flush_policy)

#### Source Code

```protobuf
// file: pkg/queue/proto/flush_queue_request.proto
// version: 1.1.0
// Request to flush queue messages to persistent storage

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/queue/proto/flush_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// FlushQueueRequest forces queue messages to be flushed to persistent storage
message FlushQueueRequest {
  // Queue identifier to flush
  string queue_id = 1;

  // Flush policy to apply
  FlushPolicy flush_policy = 2;

  // Wait for flush completion before returning
  bool wait_for_completion = 3;

  // Maximum time to wait for flush completion (milliseconds)
  int32 timeout_ms = 4;

  // Flush only messages up to this timestamp
  google.protobuf.Timestamp flush_until = 5;

  // Include specific partitions only (empty = all partitions)
  repeated int32 partition_ids = 6;

  // Force flush even if not needed
  bool force_flush = 7;

  // Optional metadata for the flush operation
  map<string, string> metadata = 8;
}

```

---

### flush_queue_response.proto {#flush_queue_response}

**Path**: `pkg/queue/proto/flush_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `FlushQueueResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/flush_queue_response.proto
// version: 1.0.0
// Response for queue flush operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for queue flush operations
message FlushQueueResponse {
  // Whether the flush was successful
  bool success = 1;

  // Number of messages flushed
  int64 messages_flushed = 2;

  // Bytes flushed from queue
  int64 bytes_flushed = 3;

  // Time taken for flush operation (milliseconds)
  int32 flush_duration_ms = 4;

  // Error message if flush failed
  string error = 5;
}

```

---

### get_cluster_info_request.proto {#get_cluster_info_request}

**Path**: `pkg/queue/proto/get_cluster_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `GetClusterInfoRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/get_cluster_info_request.proto
// version: 1.0.0
// Request to get cluster information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to get cluster information
message GetClusterInfoRequest {
  // Include node details
  bool include_nodes = 1;

  // Include performance metrics
  bool include_metrics = 2;

  // Include health status
  bool include_health = 3;

  // Include resource usage
  bool include_resources = 4;

  // Include topology information
  bool include_topology = 5;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 6;
}

```

---

### get_cluster_info_response.proto {#get_cluster_info_response}

**Path**: `pkg/queue/proto/get_cluster_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `GetClusterInfoResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/cluster_info.proto` → [queue_1](./queue_1.md#cluster_info)
- `pkg/queue/proto/node_info.proto` → [queue_1](./queue_1.md#node_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/get_cluster_info_response.proto
// file: queue/proto/responses/get_cluster_info_response.proto
// version: 1.0.0
// guid: 3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/cluster_info.proto";
import "pkg/queue/proto/node_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response containing cluster information.
 */
message GetClusterInfoResponse {
  // Detailed cluster information
  gcommon.v1.queue.ClusterInfo cluster_info = 1;

  // Node information
  repeated gcommon.v1.queue.NodeInfo nodes = 2;

  // Whether the cluster is currently healthy
  bool is_healthy = 3;

  // Any warnings or issues with the cluster
  repeated string warnings = 4;

  // Error message if failed to get info
  string error_message = 5;
}
// This file needs proper implementation

```

---

### get_message_request.proto {#get_message_request}

**Path**: `pkg/queue/proto/get_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `GetMessageRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/get_message_request.proto
// version: 1.0.0
// Request to get a specific message

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to get a specific message
message GetMessageRequest {
  // Topic name
  string topic = 1;

  // Message ID to retrieve
  string message_id = 2;

  // Partition ID (optional)
  int32 partition_id = 3;

  // Offset within partition (optional)
  int64 offset = 4;

  // Include message metadata
  bool include_metadata = 5;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 6;
}

```

---

### get_message_response.proto {#get_message_response}

**Path**: `pkg/queue/proto/get_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `GetMessageResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/message_envelope.proto` → [queue_1](./queue_1.md#message_envelope)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/get_message_response.proto
// file: queue/proto/responses/get_message_response.proto
// version: 1.0.0
// guid: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/message_envelope.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response containing a message retrieved from a queue.
 */
message GetMessageResponse {
  // The retrieved message (null if no message available)
  gcommon.v1.queue.MessageEnvelope message = 1;

  // Acknowledgment token for this message (used to ack/nack)
  string ack_token = 2;

  // Whether more messages are available in the queue
  bool has_more = 3;

  // Position/offset of this message in the queue
  int64 message_offset = 4;

  // Queue depth at the time of retrieval
  int64 queue_depth = 5;
}

```

---

### get_node_info_request.proto {#get_node_info_request}

**Path**: `pkg/queue/proto/get_node_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `GetNodeInfoRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/get_node_info_request.proto
// version: 1.0.0
// Request to get node information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to get node information
message GetNodeInfoRequest {
  // Node ID to get info for (optional, defaults to current node)
  string node_id = 1;

  // Include performance metrics
  bool include_metrics = 2;

  // Include health status
  bool include_health = 3;

  // Include resource usage
  bool include_resources = 4;

  // Include network topology
  bool include_topology = 5;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 6;
}

```

---

### get_node_info_response.proto {#get_node_info_response}

**Path**: `pkg/queue/proto/get_node_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `GetNodeInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/node_info.proto` → [queue_1](./queue_1.md#node_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/get_node_info_response.proto
// version: 1.0.0
// Response with node information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/node_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response with node information
message GetNodeInfoResponse {
  // Node information
  NodeInfo node_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3;
}

```

---

### get_offset_request.proto {#get_offset_request}

**Path**: `pkg/queue/proto/get_offset_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `GetOffsetRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/queue/proto/offset_type.proto` → [queue_1](./queue_1.md#offset_type)

#### Source Code

```protobuf
// file: pkg/queue/proto/get_offset_request.proto
// version: 1.1.0
// guid: d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/offset_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to get the current offset for a consumer or partition.
 * Used for tracking message consumption progress.
 */
message GetOffsetRequest {
  // Queue or topic name
  string queue_name = 1;

  // Partition ID (for partitioned queues)
  int32 partition_id = 2;

  // Consumer group ID (optional)
  string consumer_group = 3;

  // Consumer ID within the group (optional)
  string consumer_id = 4;

  // Type of offset to retrieve
  OffsetType offset_type = 5;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}

```

---

### get_offset_response.proto {#get_offset_response}

**Path**: `pkg/queue/proto/get_offset_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `GetOffsetResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/get_offset_response.proto
// version: 1.0.0
// guid: 28ce7fa9-da40-4119-8167-285e4ff6179a
// GetOffsetResponse returns the current committed offset for a
// consumer group within a queue or topic.
// GetOffsetResponse provides offset information for a consumer group.

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

message GetOffsetResponse {
  // The currently committed offset.
  int64 offset = 1;

  // Name of the queue or topic.
  string queue_name = 2;

  // Optional request metadata.
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### get_partition_info_request.proto {#get_partition_info_request}

**Path**: `pkg/queue/proto/get_partition_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `GetPartitionInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/get_queue_info_request.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/get_partition_info_request.proto
// version: 1.1.0
// Request to get partition information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/get_queue_info_request.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// GetPartitionInfoRequest retrieves information about topic partitions
message GetPartitionInfoRequest {
  // Topic identifier
  string topic_id = 1;

  // Specific partition IDs (empty = all partitions)
  repeated int32 partition_ids = 2;

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
  string access_token = 10;
}
// This file needs proper implementation

```

---

### get_partition_info_response.proto {#get_partition_info_response}

**Path**: `pkg/queue/proto/get_partition_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `GetPartitionInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/partition_info.proto` → [queue_1](./queue_1.md#partition_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/get_partition_info_response.proto
// version: 1.0.0
// Response with partition information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/partition_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response with partition information
message GetPartitionInfoResponse {
  // Partition information
  PartitionInfo partition_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3;
}

```

---

### get_queue_info_request.proto {#get_queue_info_request}

**Path**: `pkg/queue/proto/get_queue_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 64

**Messages** (2): `GetQueueInfoRequest`, `TimeRangeFilter`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/get_queue_info_request.proto
// version: 1.1.0
// Request to get detailed information about a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// GetQueueInfoRequest retrieves detailed information about a specific queue
message GetQueueInfoRequest {
  // Queue identifier
  string queue_id = 1;

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
  repeated string info_sections = 10;

  // Access control context
  string access_token = 11;
}

// Time range filter for historical data
message TimeRangeFilter {
  // Start time for the range (ISO 8601)
  string start_time = 1;

  // End time for the range (ISO 8601)
  string end_time = 2;

  // Granularity for aggregated data (minute, hour, day)
  string granularity = 3;

  // Maximum number of data points to return
  int32 max_data_points = 4;
}

```

---

### get_queue_info_response.proto {#get_queue_info_response}

**Path**: `pkg/queue/proto/get_queue_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `GetQueueInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/queue_info.proto` → [queue_2](./queue_2.md#queue_info)

#### Source Code

```protobuf
// file: pkg/queue/proto/get_queue_info_response.proto
// version: 1.0.0
// Response with queue information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/queue_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response with queue information
message GetQueueInfoResponse {
  // Queue information
  QueueInfo queue_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3;
}

```

---
