# queue_config_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [alerting_config.proto](#alerting_config)
- [auth_cache_config.proto](#auth_cache_config)
- [authentication_config.proto](#authentication_config)
- [authorization_config.proto](#authorization_config)
- [auto_commit_config.proto](#auto_commit_config)
- [backup_config.proto](#backup_config)
- [batch_config.proto](#batch_config)
- [batch_delivery_config.proto](#batch_delivery_config)
- [circuit_breaker_config.proto](#circuit_breaker_config)
- [cluster_config.proto](#cluster_config)
- [compression_config.proto](#compression_config)
- [consistency_config.proto](#consistency_config)
- [consumer_config.proto](#consumer_config)
- [consumer_group_config.proto](#consumer_group_config)
- [dead_letter_config.proto](#dead_letter_config)
- [dead_letter_queue_config.proto](#dead_letter_queue_config)
- [delivery_configuration.proto](#delivery_configuration)
- [delivery_retry_config.proto](#delivery_retry_config)
- [deserialization_config.proto](#deserialization_config)
- [durability_config.proto](#durability_config)
- [encryption_config.proto](#encryption_config)
- [error_action_config.proto](#error_action_config)
- [error_handling_config.proto](#error_handling_config)
- [error_notification_config.proto](#error_notification_config)
- [exchange_config.proto](#exchange_config)
- [flow_control_config.proto](#flow_control_config)
- [header_routing_config.proto](#header_routing_config)
- [load_balancing_config.proto](#load_balancing_config)
- [message_filter_config.proto](#message_filter_config)
- [migration_config.proto](#migration_config)
- [monitoring_config.proto](#monitoring_config)
- [multi_value_config.proto](#multi_value_config)
- [offset_config.proto](#offset_config)
- [ordering_config.proto](#ordering_config)
- [partition_config.proto](#partition_config)
- [performance_config.proto](#performance_config)
- [publish_config.proto](#publish_config)
- [queue_config.proto](#queue_config)
- [queue_configuration.proto](#queue_configuration)
- [rate_limit_config.proto](#rate_limit_config)
- [read_retry_config.proto](#read_retry_config)
- [replication_config.proto](#replication_config)
- [restore_config.proto](#restore_config)
- [retry_config.proto](#retry_config)
- [retry_delay_config.proto](#retry_delay_config)
- [routing_config.proto](#routing_config)
- [schema_config.proto](#schema_config)
- [serialization_config.proto](#serialization_config)
- [stream_config.proto](#stream_config)
- [subscription_config.proto](#subscription_config)
---


## Detailed Documentation

### alerting_config.proto {#alerting_config}

**Path**: `gcommon/v1/queue/alerting_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `AlertingConfig`

**Imports** (6):

- `gcommon/v1/common/alert_severity.proto`
- `gcommon/v1/queue/alert_rule.proto`
- `gcommon/v1/queue/notification_channel.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alerting_config.proto
// version: 1.1.0
// guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/alert_severity.proto";
import "gcommon/v1/queue/alert_rule.proto";
import "gcommon/v1/queue/notification_channel.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for queue alerting and notifications.
 */
message AlertingConfig {
  // Whether alerting is enabled
  bool enabled = 1;

  // List of alert rules
  repeated AlertRule rules = 2 [(buf.validate.field).repeated.min_items = 1];

  // Notification channels for alerts
  repeated QueueNotificationChannel channels = 3 [(buf.validate.field).repeated.min_items = 1];

  // Default alert severity level
  gcommon.v1.common.CommonAlertSeverity default_severity = 4;

  // Alert aggregation window
  google.protobuf.Duration aggregation_window = 5;
}
```

---

### auth_cache_config.proto {#auth_cache_config}

**Path**: `gcommon/v1/queue/auth_cache_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `AuthCacheConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/auth_cache_config.proto
// version: 1.0.0
// guid: 4282b3d6-375a-4b30-aaad-1763d882936a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AuthCacheConfig {
  // Enable caching
  bool enabled = 1;

  // Cache TTL (seconds)
  int32 ttl_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum cache size
  int32 max_size = 3 [(buf.validate.field).int32.gte = 0];

  // Cache cleanup interval (seconds)
  int32 cleanup_interval_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### authentication_config.proto {#authentication_config}

**Path**: `gcommon/v1/queue/authentication_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `AuthenticationConfig`

**Imports** (6):

- `gcommon/v1/queue/api_key_auth.proto`
- `gcommon/v1/queue/o_auth2_auth.proto`
- `gcommon/v1/queue/sasl_auth.proto`
- `gcommon/v1/queue/tls_auth.proto`
- `gcommon/v1/queue/username_password_auth.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/authentication_config.proto
// version: 1.0.1
// guid: b6fb3968-5534-4c9b-a4bb-55245fb334e3

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/api_key_auth.proto";
import "gcommon/v1/queue/o_auth2_auth.proto";
import "gcommon/v1/queue/sasl_auth.proto";
import "gcommon/v1/queue/tls_auth.proto";
import "gcommon/v1/queue/username_password_auth.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AuthenticationConfig {
  // Authentication type
  oneof auth_type {
    // No authentication required
    bool none = 1;

    // Username/password authentication
    UsernamePasswordAuth username_password = 2;

    // API key authentication
    APIKeyAuth api_key = 3;

    // TLS certificate authentication
    TLSAuth tls = 4;

    // SASL authentication
    SASLAuth sasl = 5;

    // OAuth2 authentication
    OAuth2Auth oauth2 = 6;
  }
}
```

---

### authorization_config.proto {#authorization_config}

**Path**: `gcommon/v1/queue/authorization_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `AuthorizationConfig`

**Imports** (7):

- `gcommon/v1/queue/api_key_auth.proto`
- `gcommon/v1/queue/external_auth_service.proto`
- `gcommon/v1/queue/jwt_auth.proto`
- `gcommon/v1/queue/permission_rule.proto`
- `gcommon/v1/queue/role_based_access_control.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/authorization_config.proto
// version: 1.0.0
// guid: 813cabd6-f8af-423b-be9a-0c4d74b35cf2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/api_key_auth.proto";
import "gcommon/v1/queue/external_auth_service.proto";
import "gcommon/v1/queue/jwt_auth.proto";
import "gcommon/v1/queue/permission_rule.proto";
import "gcommon/v1/queue/role_based_access_control.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AuthorizationConfig {
  // Enable authorization checking
  bool enabled = 1;

  // Default permission policy (allow/deny)
  string default_policy = 2 [(buf.validate.field).string.min_len = 1];

  // Permission rules for different operations
  repeated PermissionRule rules = 3 [(buf.validate.field).repeated.min_items = 1];

  // Role-based access control settings
  RoleBasedAccessControl rbac = 4;

  // API key authentication settings
  APIKeyAuth api_key_auth = 5;

  // JWT token authentication settings
  JwtAuth jwt_auth = 6;

  // External authorization service settings
  ExternalAuthService external_auth = 7;
}
```

---

### auto_commit_config.proto {#auto_commit_config}

**Path**: `gcommon/v1/queue/auto_commit_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `AutoCommitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/auto_commit_config.proto
// version: 1.0.0
// guid: 7f79c66e-a2a7-427d-844c-6010e165135d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AutoCommitConfig {
  // Enable auto-commit of offsets
  bool enabled = 1;

  // Auto-commit interval (milliseconds)
  int32 interval_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Commit on message processing completion
  bool commit_on_completion = 3;

  // Batch size for auto-commit
  int32 batch_size = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### backup_config.proto {#backup_config}

**Path**: `gcommon/v1/queue/backup_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `QueueBackupConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/backup_config.proto
// version: 1.0.0
// guid: 2e127d68-6db3-4c2e-a0ff-bb7a2e5542b8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// BackupConfig defines how queued messages should be backed up
// for disaster recovery.
message QueueBackupConfig {
  // Interval between automatic backups.
  google.protobuf.Duration interval = 1;

  // Duration to retain each backup before deletion.
  google.protobuf.Duration retention = 2;

  // Storage location for backups (e.g., S3 bucket).
  string location = 3 [(buf.validate.field).string.min_len = 1];

  // Whether backups are enabled for this queue.
  bool enabled = 4;
}
```

---

### batch_config.proto {#batch_config}

**Path**: `gcommon/v1/queue/batch_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `BatchConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/batch_config.proto
// file: proto/gcommon/v1/queue/batch_config.proto
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a
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
 * Configuration for batch operations in queue processing.
 */
message BatchConfig {
  // Maximum number of messages per batch
  uint32 max_batch_size = 1 [(buf.validate.field).uint32.gte = 0];

  // Maximum time to wait before sending partial batch
  google.protobuf.Duration max_wait_time = 2;

  // Maximum total size of batch in bytes
  uint64 max_batch_bytes = 3 [(buf.validate.field).uint64.gte = 0];

  // Whether to enable batch compression
  bool enable_compression = 4;

  // Number of parallel batch workers
  uint32 worker_count = 5 [(buf.validate.field).uint32.gte = 0];

  // Buffer size for pending batches
  uint32 buffer_size = 6 [(buf.validate.field).uint32.gte = 0];
}
```

---

### batch_delivery_config.proto {#batch_delivery_config}

**Path**: `gcommon/v1/queue/batch_delivery_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `BatchDeliveryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_delivery_config.proto
// version: 1.0.0
// guid: 2f43a02c-2696-4c1f-820c-b97ddd38fe31

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message BatchDeliveryConfig {
  // Enable batch delivery
  bool enabled = 1;

  // Maximum messages per batch
  int32 max_batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum batch size in bytes
  int64 max_batch_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum time to wait for batch completion (milliseconds)
  int32 batch_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### circuit_breaker_config.proto {#circuit_breaker_config}

**Path**: `gcommon/v1/queue/circuit_breaker_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `QueueCircuitBreakerConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/circuit_breaker_config.proto
// file: proto/gcommon/v1/queue/circuit_breaker_config.proto
// version: 1.0.0
// guid: 6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f
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
 * Configuration for circuit breaker pattern in queue operations.
 */
message QueueCircuitBreakerConfig {
  // Whether circuit breaker is enabled
  bool enabled = 1;

  // Failure threshold to open circuit
  uint32 failure_threshold = 2 [(buf.validate.field).uint32.gte = 0];

  // Success threshold to close circuit
  uint32 success_threshold = 3 [(buf.validate.field).uint32.gte = 0];

  // Timeout before attempting to close circuit
  google.protobuf.Duration timeout = 4;

  // Maximum number of concurrent requests in half-open state
  uint32 max_requests = 5 [(buf.validate.field).uint32.gte = 0];

  // Time window for failure counting
  google.protobuf.Duration interval = 6;
}
```

---

### cluster_config.proto {#cluster_config}

**Path**: `gcommon/v1/queue/cluster_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ClusterConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_config.proto
// version: 1.0.0
// guid: 6ab9cf18-3f43-40f4-b289-163545acdc05

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for the cluster.
 */
message ClusterConfig {
  // Minimum number of nodes for quorum
  int32 quorum_size = 1 [(buf.validate.field).int32.gte = 0];

  // Replication factor
  int32 replication_factor = 2 [(buf.validate.field).int32.gte = 0];

  // Heartbeat interval in seconds
  int32 heartbeat_interval = 3 [(buf.validate.field).int32.gte = 0];

  // Election timeout in seconds
  int32 election_timeout = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### compression_config.proto {#compression_config}

**Path**: `gcommon/v1/queue/compression_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `QueueCompressionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/compression_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174000

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// CompressionConfig message definition.
message QueueCompressionConfig {
  // Enable compression
  bool enabled = 1;

  // Compression algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Compression level (0-9)
  int32 level = 3 [(buf.validate.field).int32.gte = 0];

  // Minimum message size to compress
  int32 min_size_bytes = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### consistency_config.proto {#consistency_config}

**Path**: `gcommon/v1/queue/consistency_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `ConsistencyConfig`

**Imports** (9):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/common/conflict_resolution.proto`
- `gcommon/v1/common/durability_level.proto`
- `gcommon/v1/queue/consistency_validation.proto`
- `gcommon/v1/queue/ordering_config.proto`
- `gcommon/v1/queue/read_consistency.proto`
- `gcommon/v1/queue/replication_consistency.proto`
- `gcommon/v1/queue/write_consistency.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consistency_config.proto
// version: 1.0.1
// guid: 038986e0-4267-432c-99a3-7271a9427b29

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/common/conflict_resolution.proto";
import "gcommon/v1/common/durability_level.proto";
import "gcommon/v1/queue/consistency_validation.proto";
import "gcommon/v1/queue/ordering_config.proto";
import "gcommon/v1/queue/read_consistency.proto";
import "gcommon/v1/queue/replication_consistency.proto";
import "gcommon/v1/queue/write_consistency.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsistencyConfig {
  // Durability level for message persistence
  gcommon.v1.common.DurabilityLevel durability_level = 1;

  // Acknowledgment level required for message delivery
  gcommon.v1.common.AckLevel ack_level = 2;

  // Replication configuration
  ReplicationConsistency replication = 3;

  // Read consistency settings
  ReadConsistency read_consistency = 4;

  // Write consistency settings
  WriteConsistency write_consistency = 5;

  // Ordering guarantees
  OrderingConfig ordering = 6;

  // Conflict resolution settings
  gcommon.v1.common.ConflictResolution conflict_resolution = 7;

  // Consistency validation settings
  ConsistencyValidation validation = 8;
}
```

---

### consumer_config.proto {#consumer_config}

**Path**: `gcommon/v1/queue/consumer_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ConsumerConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_config.proto
// version: 1.0.0
// guid: 75004ee5-2574-4d9a-bbf6-5d010b09af89

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerConfig {
  // Consumer timeout (milliseconds)
  int32 timeout_ms = 1 [(buf.validate.field).int32.gt = 0];

  // Maximum messages to poll at once
  int32 max_poll_records = 2 [(buf.validate.field).int32.gte = 0];

  // Fetch minimum bytes
  int32 fetch_min_bytes = 3 [(buf.validate.field).int32.gte = 0];

  // Fetch maximum wait time (milliseconds)
  int32 fetch_max_wait_ms = 4 [(buf.validate.field).int32.gte = 0];

  // Enable auto-offset reset
  bool auto_offset_reset = 5;

  // Consumer priority (for priority-based assignment)
  int32 priority = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### consumer_group_config.proto {#consumer_group_config}

**Path**: `gcommon/v1/queue/consumer_group_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `ConsumerGroupConfig`

**Imports** (7):

- `gcommon/v1/common/load_balancing_strategy.proto`
- `gcommon/v1/common/offset_reset_strategy.proto`
- `gcommon/v1/common/rebalance_strategy.proto`
- `gcommon/v1/queue/auto_commit_config.proto`
- `gcommon/v1/queue/dead_letter_queue_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group_config.proto
// version: 1.0.0
// guid: 8f71a5d7-ed37-4020-94fb-4c8960ef1e5d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/load_balancing_strategy.proto";
import "gcommon/v1/common/offset_reset_strategy.proto";
import "gcommon/v1/common/rebalance_strategy.proto";
import "gcommon/v1/queue/auto_commit_config.proto";
import "gcommon/v1/queue/dead_letter_queue_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerGroupConfig {
  // Load balancing strategy for partition assignment
  gcommon.v1.common.LoadBalancingStrategy load_balancing_strategy = 1;

  // Rebalance strategy when consumers join/leave
  gcommon.v1.common.RebalanceStrategy rebalance_strategy = 2;

  // Session timeout for consumer heartbeats (milliseconds)
  int32 session_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Heartbeat interval (milliseconds)
  int32 heartbeat_interval_ms = 4 [(buf.validate.field).int32.gte = 0];

  // Maximum poll interval (milliseconds)
  int32 max_poll_interval_ms = 5 [(buf.validate.field).int32.gte = 0];

  // Auto-commit configuration
  AutoCommitConfig auto_commit = 6;

  // Offset reset strategy for new consumers
  gcommon.v1.common.OffsetResetStrategy offset_reset_strategy = 7;

  // Maximum number of consumers allowed in the group
  int32 max_consumers = 8 [(buf.validate.field).int32.gte = 0];

  // Enable exactly-once semantics
  bool exactly_once_enabled = 9;

  // Dead letter queue configuration
  DeadLetterQueueConfig dlq_config = 10;
}
```

---

### dead_letter_config.proto {#dead_letter_config}

**Path**: `gcommon/v1/queue/dead_letter_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `DeadLetterConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/dead_letter_config.proto
// file: proto/gcommon/v1/queue/dead_letter_config.proto
// version: 1.0.0
// guid: 8a7b6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d
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
 * Configuration for dead letter queue behavior.
 * Defines how messages that cannot be processed are handled.
 */
message DeadLetterConfig {
  // Whether dead letter queue functionality is enabled
  bool enabled = 1;

  // Name of the dead letter queue
  string dead_letter_queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Maximum number of delivery attempts before sending to DLQ
  int32 max_delivery_attempts = 3;

  // Time to live for messages in the dead letter queue
  google.protobuf.Duration ttl = 4;

  // Whether to preserve the original message headers
  bool preserve_headers = 5;

  // Additional metadata to attach to dead letter messages
  map<string, string> additional_metadata = 6;
}
```

---

### dead_letter_queue_config.proto {#dead_letter_queue_config}

**Path**: `gcommon/v1/queue/dead_letter_queue_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `DeadLetterQueueConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/dead_letter_queue_config.proto
// version: 1.0.0
// guid: f8d651b6-6f08-48f8-96a3-ad28ada68da7

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeadLetterQueueConfig {
  // Enable dead letter queue
  bool enabled = 1;

  // Dead letter queue topic
  string dlq_topic = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum message age in DLQ (seconds)
  int64 dlq_max_age_seconds = 3 [(buf.validate.field).int64.gte = 0];

  // Include original error information
  bool include_error_info = 4;
}
```

---

### delivery_configuration.proto {#delivery_configuration}

**Path**: `gcommon/v1/queue/delivery_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `DeliveryConfiguration`

**Imports** (5):

- `gcommon/v1/queue/batch_delivery_config.proto`
- `gcommon/v1/queue/delivery_retry_config.proto`
- `gcommon/v1/queue/flow_control_settings.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_configuration.proto
// version: 1.0.0
// guid: 4f995a26-dac9-451d-9d56-fb21aa66e2fa

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/batch_delivery_config.proto";
import "gcommon/v1/queue/delivery_retry_config.proto";
import "gcommon/v1/queue/flow_control_settings.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeliveryConfiguration {
  // Delivery endpoint (for push subscriptions)
  string push_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Delivery timeout (milliseconds)
  int32 delivery_timeout_ms = 2 [(buf.validate.field).int32.gt = 0];

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
```

---

### delivery_retry_config.proto {#delivery_retry_config}

**Path**: `gcommon/v1/queue/delivery_retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `DeliveryRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_retry_config.proto
// version: 1.0.0
// guid: b4d42c13-fbcd-4e8b-a74d-ac360b2f5814

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeliveryRetryConfig {
  // Enable retry on delivery failures
  bool enabled = 1;

  // Maximum retry attempts
  int32 max_retries = 2 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 4 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 5 [(buf.validate.field).double.gte = 0.0];

  // Retry only for specific error codes
  repeated string retry_error_codes = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### deserialization_config.proto {#deserialization_config}

**Path**: `gcommon/v1/queue/deserialization_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `DeserializationConfig`

**Imports** (3):

- `gcommon/v1/common/serialization_format.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/deserialization_config.proto
// file: proto/gcommon/v1/queue/deserialization_config.proto
// version: 1.0.0
// guid: 1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/serialization_format.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message deserialization.
 */
message DeserializationConfig {
  // Supported serialization formats
  repeated gcommon.v1.common.SerializationFormat supported_formats = 1 [(buf.validate.field).repeated.min_items = 1];

  // Default format if not specified
  gcommon.v1.common.SerializationFormat default_format = 2;

  // Whether to validate schema during deserialization
  bool validate_schema = 3;

  // Whether to allow unknown fields
  bool allow_unknown_fields = 4;

  // Custom deserializer class name
  string custom_deserializer = 5 [(buf.validate.field).string.min_len = 1];

  // Maximum message size for deserialization (bytes)
  uint64 max_message_size = 6 [(buf.validate.field).uint64.gte = 0];
}
```

---

### durability_config.proto {#durability_config}

**Path**: `gcommon/v1/queue/durability_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `DurabilityConfig`

**Imports** (5):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/common/flush_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/durability_config.proto
// file: proto/gcommon/v1/queue/durability_config.proto
// version: 1.0.0
// guid: 1a0b9c8d-7e6f-5a4b-3c2d-1e0f9a8b7c6d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/common/flush_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message durability and persistence.
 */
message DurabilityConfig {
  // Whether messages are persisted to disk
  bool persistent = 1;

  // Flush policy for writing messages to storage
  gcommon.v1.common.FlushPolicy flush_policy = 2;

  // Number of replicas for each message
  int32 replication_factor = 3 [(buf.validate.field).int32.gte = 0];

  // Acknowledgment level required before considering message durable
  gcommon.v1.common.AckLevel ack_level = 4;

  // Timeout for durability operations
  google.protobuf.Duration durability_timeout = 5;

  // Whether to use write-ahead logging
  bool write_ahead_log = 6;

  // Sync frequency for flushing to disk
  google.protobuf.Duration sync_interval = 7;

  // Whether to verify checksums on read
  bool verify_checksums = 8;
}
```

---

### encryption_config.proto {#encryption_config}

**Path**: `gcommon/v1/queue/encryption_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `QueueEncryptionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/encryption_config.proto
// file: proto/gcommon/v1/queue/encryption_config.proto
// version: 1.0.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b
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
 * Configuration for message encryption in queues.
 */
message QueueEncryptionConfig {
  // Whether encryption is enabled
  bool enabled = 1;

  // Encryption algorithm (AES256, ChaCha20, etc.)
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Key derivation function (PBKDF2, scrypt, argon2)
  string key_derivation = 3 [(buf.validate.field).string.min_len = 1];

  // Encryption key identifier
  string key_id = 4 [(buf.validate.field).string.min_len = 1];

  // Whether to encrypt message headers
  bool encrypt_headers = 5;

  // Whether to encrypt routing keys
  bool encrypt_routing_keys = 6;

  // Key rotation interval in hours
  uint32 rotation_interval_hours = 7 [(buf.validate.field).uint32.gte = 0];
}
```

---

### error_action_config.proto {#error_action_config}

**Path**: `gcommon/v1/queue/error_action_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `ErrorActionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_action_config.proto
// version: 1.0.0
// guid: 97538011-4ce0-4da2-8495-54204f07556a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorActionConfig {
  // Error code or pattern
  string error_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Action to take (retry, dlq, drop, pause)
  string action = 2 [(buf.validate.field).string.min_len = 1];

  // Action parameters
  map<string, string> action_params = 3;
}
```

---

### error_handling_config.proto {#error_handling_config}

**Path**: `gcommon/v1/queue/error_handling_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ErrorHandlingConfig`

**Imports** (5):

- `gcommon/v1/queue/dead_letter_queue_config.proto`
- `gcommon/v1/queue/error_action_config.proto`
- `gcommon/v1/queue/error_notification_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_handling_config.proto
// version: 1.0.0
// guid: 49c9649a-c944-4438-b21f-d3645782576f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/dead_letter_queue_config.proto";
import "gcommon/v1/queue/error_action_config.proto";
import "gcommon/v1/queue/error_notification_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorHandlingConfig {
  // Dead letter queue configuration
  DeadLetterQueueConfig dlq_config = 1;

  // Maximum delivery attempts before DLQ
  int32 max_delivery_attempts = 2 [(buf.validate.field).int32.gte = 0];

  // Actions to take on specific errors
  repeated ErrorActionConfig error_actions = 3 [(buf.validate.field).repeated.min_items = 1];

  // Enable error logging
  bool enable_error_logging = 4;

  // Error notification settings
  ErrorNotificationConfig notification_config = 5;
}
```

---

### error_notification_config.proto {#error_notification_config}

**Path**: `gcommon/v1/queue/error_notification_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ErrorNotificationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_notification_config.proto
// version: 1.0.0
// guid: 0fffcb32-c66a-4876-acb0-c7d756601f4d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorNotificationConfig {
  // Enable error notifications
  bool enabled = 1;

  // Notification channels
  repeated string notification_channels = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error threshold for notifications
  int32 error_threshold = 3 [(buf.validate.field).int32.gte = 0];

  // Notification frequency (seconds)
  int32 notification_frequency_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### exchange_config.proto {#exchange_config}

**Path**: `gcommon/v1/queue/exchange_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `ExchangeConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/exchange_config.proto
// file: proto/gcommon/v1/queue/exchange_config.proto
// version: 1.0.0
// guid: 4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b
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
 * Configuration for message exchange operations between queues.
 */
message ExchangeConfig {
  // Exchange name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Exchange type (direct, topic, fanout, headers)
  string exchange_type = 2;

  // Whether exchange is durable
  bool durable = 3;

  // Whether to auto-delete when unused
  bool auto_delete = 4;

  // Whether exchange is internal
  bool internal = 5;

  // Custom exchange arguments
  map<string, string> arguments = 6;

  // Routing configuration
  string routing_key = 7;

  // Whether to enable alternate exchange
  string alternate_exchange = 8;
}
```

---

### flow_control_config.proto {#flow_control_config}

**Path**: `gcommon/v1/queue/flow_control_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `FlowControlConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flow_control_config.proto
// version: 1.0.0
// guid: e0dba279-5bac-45a2-8bd5-b341fa734230

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FlowControlConfig {
  // Enable flow control
  bool enabled = 1;

  // Maximum outstanding messages
  int32 max_outstanding_messages = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Flow control algorithm (token_bucket, leaky_bucket, sliding_window)
  string algorithm = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### header_routing_config.proto {#header_routing_config}

**Path**: `gcommon/v1/queue/header_routing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `HeaderRoutingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/header_routing_config.proto
// version: 1.0.0
// guid: 048332dd-afed-41ee-b803-dd1574fd07d9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Header-based routing configuration.
 */
message HeaderRoutingConfig {
  // Header key to use for routing
  string routing_header = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to use exact match or pattern matching
  bool exact_match = 2;

  // Case sensitivity for header matching
  bool case_sensitive = 3;
}
```

---

### load_balancing_config.proto {#load_balancing_config}

**Path**: `gcommon/v1/queue/load_balancing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `LoadBalancingConfig`

**Imports** (3):

- `gcommon/v1/common/load_balancing_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/load_balancing_config.proto
// version: 1.1.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/load_balancing_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for load balancing across queue consumers.
 */
message LoadBalancingConfig {
  // Load balancing strategy
  gcommon.v1.common.LoadBalancingStrategy strategy = 1;

  // Weight for this consumer (for weighted strategies)
  int32 weight = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum concurrent messages per consumer
  int32 max_concurrent_messages = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Prefetch count for batch consumption
  int32 prefetch_count = 4 [(buf.validate.field).int32.gte = 0];

  // Consumer priority (higher numbers = higher priority)
  int32 priority = 5 [(buf.validate.field).int32.gte = 0];

  // Whether to enable sticky sessions
  bool sticky_sessions = 6;

  // Session affinity key
  string affinity_key = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_filter_config.proto {#message_filter_config}

**Path**: `gcommon/v1/queue/message_filter_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `MessageFilterConfig`

**Imports** (3):

- `gcommon/v1/queue/content_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_filter_config.proto
// version: 1.0.0
// guid: e63e4778-4555-4c0c-a835-7f83564e8513

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/content_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageFilterConfig {
  // Header-based filters
  map<string, string> header_filters = 1;

  // Content-based filters
  repeated ContentFilter content_filters = 2 [(buf.validate.field).repeated.min_items = 1];

  // Routing key patterns
  repeated string routing_key_patterns = 3 [(buf.validate.field).repeated.min_items = 1];

  // Message type filters
  repeated string message_types = 4 [(buf.validate.field).repeated.min_items = 1];

  // Custom filter expressions
  repeated string filter_expressions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Exclude messages matching these criteria
  bool exclude_matching = 6;
}
```

---

### migration_config.proto {#migration_config}

**Path**: `gcommon/v1/queue/migration_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `MigrationConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/migration_config.proto
// file: proto/gcommon/v1/queue/migration_config.proto
// version: 1.0.0
// guid: 3d4e5f6a-7b8c-9d0e-1f2a-3b4c5d6e7f8a
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
 * Configuration for queue migration operations.
 */
message MigrationConfig {
  // Source queue configuration
  string source_queue = 1 [(buf.validate.field).string.min_len = 1];

  // Destination queue configuration
  string destination_queue = 2 [(buf.validate.field).string.min_len = 1];

  // Migration strategy (live, batch, hybrid)
  string migration_strategy = 3 [(buf.validate.field).string.min_len = 1];

  // Batch size for batch migration
  uint32 batch_size = 4 [(buf.validate.field).uint32.gte = 0];

  // Migration timeout
  google.protobuf.Duration timeout = 5;

  // Whether to verify data integrity
  bool verify_integrity = 6;

  // Whether to keep source after migration
  bool keep_source = 7;

  // Maximum concurrent operations
  uint32 max_concurrency = 8 [(buf.validate.field).uint32.gte = 0];
}
```

---

### monitoring_config.proto {#monitoring_config}

**Path**: `gcommon/v1/queue/monitoring_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `QueueMonitoringConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/monitoring_config.proto
// version: 1.0.0
// guid: 81f93ee4-708c-478c-9c19-1baf15830c08

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// MonitoringConfig controls runtime monitoring for a queue.
message QueueMonitoringConfig {
  // Enable or disable monitoring for this queue.
  bool enabled = 1;

  // Optional endpoint for publishing metrics.
  string metrics_endpoint = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### multi_value_config.proto {#multi_value_config}

**Path**: `gcommon/v1/queue/multi_value_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `MultiValueConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/multi_value_config.proto
// version: 1.0.0
// guid: 9ed9dcb6-f12f-4eea-92c1-7ee4a199f462

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MultiValueConfig {
  // Maximum number of concurrent values to keep
  int32 max_values = 1 [(buf.validate.field).int32.gte = 0];

  // Value expiration time (seconds)
  int32 value_ttl_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Conflict value cleanup strategy
  string cleanup_strategy = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### offset_config.proto {#offset_config}

**Path**: `gcommon/v1/queue/offset_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `OffsetConfig`

**Imports** (4):

- `gcommon/v1/common/offset_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_config.proto
// version: 1.0.0
// guid: 4c4657d1-5745-47d4-b9e3-6e685a1d4785

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/offset_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OffsetConfig {
  // Offset type (earliest, latest, timestamp, specific)
  gcommon.v1.common.OffsetType offset_type = 1;

  // Specific offset value (when offset_type = specific)
  int64 offset_value = 2 [(buf.validate.field).int64.gte = 0];

  // Timestamp to start from (when offset_type = timestamp)
  google.protobuf.Timestamp start_timestamp = 3;

  // Reset to beginning if offset not found
  bool reset_on_not_found = 4;
}
```

---

### ordering_config.proto {#ordering_config}

**Path**: `gcommon/v1/queue/ordering_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `OrderingConfig`

**Imports** (3):

- `gcommon/v1/common/ordering_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ordering_config.proto
// version: 1.0.0
// guid: 38b7cd46-8313-4c25-86de-04401a1cb1ae

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ordering_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OrderingConfig {
  // Global ordering guarantee level
  gcommon.v1.common.OrderingLevel global_ordering = 1;

  // Per-partition ordering guarantee
  gcommon.v1.common.OrderingLevel partition_ordering = 2;

  // Per-producer ordering guarantee
  gcommon.v1.common.OrderingLevel producer_ordering = 3;

  // Enable causal ordering
  bool causal_ordering = 4;

  // Ordering timeout (milliseconds)
  int32 ordering_timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### partition_config.proto {#partition_config}

**Path**: `gcommon/v1/queue/partition_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `PartitionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/partition_config.proto
// file: proto/gcommon/v1/queue/partition_config.proto
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f
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
 * Configuration for queue partitioning.
 */
message PartitionConfig {
  // Number of partitions
  uint32 partition_count = 1 [(buf.validate.field).uint32.gte = 0];

  // Partitioning strategy (hash, round-robin, custom)
  string partition_strategy = 2 [(buf.validate.field).string.min_len = 1];

  // Key field to use for partitioning
  string partition_key = 3 [(buf.validate.field).string.min_len = 1];

  // Custom partition function (if strategy is custom)
  string custom_partition_function = 4 [(buf.validate.field).string.min_len = 1];

  // Whether to enable partition auto-scaling
  bool auto_scale = 5;

  // Minimum number of partitions
  uint32 min_partitions = 6 [(buf.validate.field).uint32.gte = 0];

  // Maximum number of partitions
  uint32 max_partitions = 7 [(buf.validate.field).uint32.gte = 0];

  // Partition size threshold for auto-scaling (in MB)
  uint64 scale_threshold_mb = 8 [(buf.validate.field).uint64.gte = 0];
}
```

---

### performance_config.proto {#performance_config}

**Path**: `gcommon/v1/queue/performance_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 56

**Messages** (1): `PerformanceConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/performance_config.proto
// file: proto/gcommon/v1/queue/performance_config.proto
// version: 1.0.0
// guid: 2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b
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
 * Configuration for performance tuning and optimization.
 */
message PerformanceConfig {
  // Buffer size for batching operations
  uint32 buffer_size = 1 [(buf.validate.field).uint32.gte = 0];

  // Maximum batch size for operations
  uint32 max_batch_size = 2 [(buf.validate.field).uint32.gte = 0];

  // Flush interval for buffered operations
  google.protobuf.Duration flush_interval = 3;

  // Number of worker threads
  uint32 worker_threads = 4 [(buf.validate.field).uint32.gte = 0];

  // Queue capacity for in-memory operations
  uint32 queue_capacity = 5 [(buf.validate.field).uint32.gte = 0];

  // Enable async processing
  bool async_processing = 6;

  // Connection pool size
  uint32 connection_pool_size = 7 [(buf.validate.field).uint32.gte = 0];

  // Maximum idle time for connections
  google.protobuf.Duration max_idle_time = 8;

  // Enable connection multiplexing
  bool enable_multiplexing = 9;

  // Read timeout
  google.protobuf.Duration read_timeout = 10;

  // Write timeout
  google.protobuf.Duration write_timeout = 11;
}
```

---

### publish_config.proto {#publish_config}

**Path**: `gcommon/v1/queue/publish_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PublishConfig`

**Imports** (3):

- `gcommon/v1/common/retry_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_config.proto
// version: 1.0.0
// guid: 684eaa80-e0bc-4fa2-876a-8d97d9865ae8

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/retry_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PublishConfig {
  // Wait for acknowledgment before returning
  bool wait_for_ack = 1;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 2 [(buf.validate.field).int32.gt = 0];

  // Enable duplicate detection
  bool duplicate_detection = 3;

  // Compression for message batch
  bool enable_compression = 4;

  // Enable message ordering
  bool enable_ordering = 5;

  // Retry configuration for failed publishes - references existing RetryConfig
  gcommon.v1.common.CommonRetryPolicy retry_config = 6;

  // Persistence level required
  string persistence_level = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### queue_config.proto {#queue_config}

**Path**: `gcommon/v1/queue/queue_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `QueueConfig`

**Imports** (5):

- `gcommon/v1/common/priority_level.proto`
- `gcommon/v1/common/queue_type.proto`
- `gcommon/v1/common/retention_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_config.proto
// version: 1.0.0
// guid: c64defde-30d1-41e5-bfac-b415cbf929c6

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/priority_level.proto";
import "gcommon/v1/common/queue_type.proto";
import "gcommon/v1/common/retention_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// QueueConfig defines settings for creating a queue instance.
message QueueConfig {
  // Name of the queue.
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  // Queue implementation type.
  gcommon.v1.common.QueueType type = 2;
  // Number of partitions for the queue.
  int32 partitions = 3;
  // Retention policy for stored messages.
  gcommon.v1.common.MetricsRetentionPolicy retention = 4;
  // Default priority applied when publishing.
  gcommon.v1.common.PriorityLevel default_priority = 5;
  // If true, queue persists messages to disk.
  bool durable = 6;
  // Whether the queue should be automatically deleted when unused.
  bool auto_delete = 7;
}
```

---

### queue_configuration.proto {#queue_configuration}

**Path**: `gcommon/v1/queue/queue_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `QueueConfiguration`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_configuration.proto
// version: 1.0.0
// guid: a7660f75-3be5-49a6-bcd6-fc522e7e5c9a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueConfiguration {
  int64 max_messages = 1 [(buf.validate.field).int64.gte = 0];
  google.protobuf.Duration visibility_timeout = 2;
  google.protobuf.Duration message_retention_period = 3;
  int32 max_retry_attempts = 4 [(buf.validate.field).int32.gte = 0];
  bool dead_letter_queue_enabled = 5;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/queue/rate_limit_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `QueueRateLimitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/rate_limit_config.proto
// version: 1.0.0
// guid: 436ea189-70d7-4f1d-bf93-3c88f1f0de3b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// RateLimitConfig defines throughput limits for a queue.
message QueueRateLimitConfig {
  // Maximum messages allowed per second.
  int32 max_per_second = 1 [(buf.validate.field).int32.gte = 0];

  // Allowed burst capacity above the per-second rate.
  int32 burst = 2 [(buf.validate.field).int32.gte = 0];

  // Whether rate limiting is enabled.
  bool enabled = 3;
}
```

---

### read_retry_config.proto {#read_retry_config}

**Path**: `gcommon/v1/queue/read_retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ReadRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/read_retry_config.proto
// version: 1.0.0
// guid: 123c273c-25e2-4af1-85ab-48ac7f8a28d5

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReadRetryConfig {
  // Maximum retry attempts
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Retry on different replica
  bool retry_different_replica = 5;
}
```

---

### replication_config.proto {#replication_config}

**Path**: `gcommon/v1/queue/replication_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ReplicationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/replication_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ReplicationConfig message definition.
message ReplicationConfig {
  // Number of replicas
  int32 replica_count = 1 [(buf.validate.field).int32.gte = 0];

  // Replication factor
  int32 factor = 2 [(buf.validate.field).int32.gte = 0];

  // Enable synchronous replication
  bool synchronous = 3;

  // Minimum in-sync replicas
  int32 min_in_sync_replicas = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### restore_config.proto {#restore_config}

**Path**: `gcommon/v1/queue/restore_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `RestoreConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/restore_config.proto
// file: proto/gcommon/v1/queue/restore_config.proto
// version: 1.0.0
// guid: 9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a
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
 * Configuration for queue restore operations.
 */
message RestoreConfig {
  // Source backup location
  string backup_source = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to verify backup integrity before restore
  bool verify_integrity = 2;

  // Restore strategy (full, incremental, selective)
  string restore_strategy = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to overwrite existing data
  bool overwrite_existing = 4;

  // Restore timeout
  google.protobuf.Duration timeout = 5;

  // Whether to preserve original timestamps
  bool preserve_timestamps = 6;

  // Maximum concurrent restore operations
  uint32 max_concurrency = 7 [(buf.validate.field).uint32.gte = 0];

  // Whether to skip corrupted messages
  bool skip_corrupted = 8;
}
```

---

### retry_config.proto {#retry_config}

**Path**: `gcommon/v1/queue/retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `QueueRetryConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/retry_config.proto
// file: proto/gcommon/v1/queue/retry_config.proto
// version: 1.0.0
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
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
 * Configuration for retry behavior in queue operations.
 */
message QueueRetryConfig {
  // Whether retry is enabled
  bool enabled = 1;

  // Maximum number of retry attempts
  uint32 max_retries = 2 [(buf.validate.field).uint32.gte = 0];

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 3;

  // Maximum delay between retries
  google.protobuf.Duration max_delay = 4;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 5 [(buf.validate.field).double.gte = 0.0];

  // Jitter factor to randomize delays (0.0 to 1.0)
  double jitter_factor = 6 [(buf.validate.field).double.gte = 0.0];

  // Total timeout for all retry attempts
  google.protobuf.Duration total_timeout = 7;
}
```

---

### retry_delay_config.proto {#retry_delay_config}

**Path**: `gcommon/v1/queue/retry_delay_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `RetryDelayConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_delay_config.proto
// version: 1.0.0
// guid: b8735b0b-be09-4ce0-8445-a49b8b97e6db

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RetryDelayConfig {
  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 3 [(buf.validate.field).double.gte = 0.0];

  // Enable jitter for retry delays
  bool jitter_enabled = 4;
}
```

---

### routing_config.proto {#routing_config}

**Path**: `gcommon/v1/queue/routing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `RoutingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174002

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// RoutingConfig message definition.
message RoutingConfig {
  // Routing strategy
  string strategy = 1 [(buf.validate.field).string.min_len = 1];

  // Routing key pattern
  string key_pattern = 2 [(buf.validate.field).string.min_len = 1];

  // Enable sticky routing
  bool sticky = 3;

  // Load balancing algorithm
  string load_balancer = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### schema_config.proto {#schema_config}

**Path**: `gcommon/v1/queue/schema_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `SchemaConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174003

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// SchemaConfig message definition.
message SchemaConfig {
  // Schema version
  int32 version = 1 [(buf.validate.field).int32.gte = 0];

  // Schema definition
  string definition = 2 [(buf.validate.field).string.min_len = 1];

  // Schema type
  string type = 3 [(buf.validate.field).string.min_len = 1];

  // Enable schema validation
  bool validate = 4;
}
```

---

### serialization_config.proto {#serialization_config}

**Path**: `gcommon/v1/queue/serialization_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `SerializationConfig`

**Imports** (5):

- `gcommon/v1/common/compression_algorithm.proto`
- `gcommon/v1/common/serialization_format.proto`
- `gcommon/v1/queue/format_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/serialization_config.proto
// version: 1.0.0
// guid: e5f6a7b8-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/compression_algorithm.proto";
import "gcommon/v1/common/serialization_format.proto";
import "gcommon/v1/queue/format_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message serialization and deserialization.
 */
message SerializationConfig {
  // Default serialization format
  gcommon.v1.common.SerializationFormat default_format = 1;

  // Supported serialization formats
  repeated gcommon.v1.common.SerializationFormat supported_formats = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether to auto-detect format from message headers
  bool auto_detect_format = 3;

  // Default compression algorithm
  gcommon.v1.common.CompressionAlgorithm default_compression = 4;

  // Supported compression algorithms
  repeated gcommon.v1.common.CompressionAlgorithm supported_compressions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Whether to auto-detect compression from message headers
  bool auto_detect_compression = 6;

  // Format-specific options
  map<string, FormatOptions> format_options = 7;

  // Whether to validate message format on deserialization
  bool validate_on_deserialize = 8;

  // Maximum message size for serialization
  uint64 max_message_size = 9 [(buf.validate.field).uint64.gte = 0];

  // Whether to enable backwards compatibility mode
  bool backwards_compatible = 10;
}
```

---

### stream_config.proto {#stream_config}

**Path**: `gcommon/v1/queue/stream_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `StreamConfig`

**Imports** (4):

- `gcommon/v1/common/stream_restart_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/stream_config.proto
// file: proto/gcommon/v1/queue/stream_config.proto
// version: 1.0.0
// guid: 7a6b5c4d-3e2f-1a0b-9c8d-7e6f5a4b3c2d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/stream_restart_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for streaming message consumption.
 */
message StreamConfig {
  // Maximum number of messages to buffer
  int32 buffer_size = 1 [(buf.validate.field).int32.gte = 0];

  // Timeout for stream read operations
  google.protobuf.Duration read_timeout = 2;

  // Whether to enable flow control
  bool flow_control_enabled = 3;

  // Maximum outstanding messages before flow control kicks in
  int32 max_outstanding_messages = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Maximum outstanding bytes before flow control kicks in
  int64 max_outstanding_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Whether to automatically acknowledge messages
  bool auto_ack = 6;

  // Acknowledgment deadline for manually acknowledged messages
  google.protobuf.Duration ack_deadline = 7;

  // Whether to enable message ordering
  bool enable_message_ordering = 8;

  // Stream restart policy on failure
  gcommon.v1.common.StreamRestartPolicy restart_policy = 9;
}
```

---

### subscription_config.proto {#subscription_config}

**Path**: `gcommon/v1/queue/subscription_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `SubscriptionConfig`

**Imports** (6):

- `gcommon/v1/common/priority_level.proto`
- `gcommon/v1/common/routing_strategy.proto`
- `gcommon/v1/common/subscription_state.proto`
- `gcommon/v1/queue/delivery_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_config.proto
// version: 1.0.0
// guid: 27b1d56b-2e7b-4003-9ddd-6b30086ff0fb

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/priority_level.proto";
import "gcommon/v1/common/routing_strategy.proto";
import "gcommon/v1/common/subscription_state.proto";
import "gcommon/v1/queue/delivery_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// SubscriptionConfig describes how a consumer subscribes to a queue.
message SubscriptionConfig {
  // Name of the subscription.
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  // Current state of the subscription.
  gcommon.v1.common.SubscriptionState state = 2;
  // Message routing strategy for this subscription.
  gcommon.v1.common.RoutingStrategy routing_strategy = 3;
  // Default priority applied to published messages if unspecified.
  gcommon.v1.common.PriorityLevel default_priority = 4;
  // Delivery options controlling retries and dead letter handling.
  DeliveryOptions delivery_options = 5;
  // Maximum number of unacknowledged messages allowed.
  int32 max_inflight = 6;
}
```

---

