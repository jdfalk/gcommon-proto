# queue_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 41
- **Messages**: 75
- **Services**: 0
- **Enums**: 6

## Files in this Module

- [alerting_config.proto](#alerting_config)
- [authentication_config.proto](#authentication_config)
- [authorization_config.proto](#authorization_config)
- [backup_config.proto](#backup_config)
- [batch_config.proto](#batch_config)
- [circuit_breaker_config.proto](#circuit_breaker_config)
- [cluster_config.proto](#cluster_config)
- [compression_config.proto](#compression_config)
- [consistency_config.proto](#consistency_config)
- [dead_letter_config.proto](#dead_letter_config)
- [deserialization_config.proto](#deserialization_config)
- [durability_config.proto](#durability_config)
- [encryption_config.proto](#encryption_config)
- [exchange_config.proto](#exchange_config)
- [header_routing_config.proto](#header_routing_config)
- [load_balancing_config.proto](#load_balancing_config)
- [migration_config.proto](#migration_config)
- [monitoring_config.proto](#monitoring_config)
- [partition_config.proto](#partition_config)
- [performance_config.proto](#performance_config)
- [queue_config.proto](#queue_config)
- [rate_limit_config.proto](#rate_limit_config)
- [replication_config.proto](#replication_config)
- [restore_config.proto](#restore_config)
- [retry_config.proto](#retry_config)
- [routing_config.proto](#routing_config)
- [schema_config.proto](#schema_config)
- [serialization_config.proto](#serialization_config)
- [stream_config.proto](#stream_config)
- [subscription_config.proto](#subscription_config)
- [timeout_config.proto](#timeout_config)
- [topic_config.proto](#topic_config)
- [topic_routing_config.proto](#topic_routing_config)
- [transformation_config.proto](#transformation_config)
- [update_queue_config_request.proto](#update_queue_config_request)
- [update_queue_config_response.proto](#update_queue_config_response)
- [update_subscription_config_request.proto](#update_subscription_config_request)
- [update_subscription_config_response.proto](#update_subscription_config_response)
- [update_topic_config_request.proto](#update_topic_config_request)
- [update_topic_config_response.proto](#update_topic_config_response)
- [validation_config.proto](#validation_config)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_1](./config_1.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)
- [queue_2](./queue_2.md)

**Modules that depend on this one**:

- [queue_api_1](./queue_api_1.md)
- [queue_api_2](./queue_api_2.md)

---

## Detailed Documentation

### alerting_config.proto {#alerting_config}

**Path**: `pkg/queue/proto/alerting_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 37

**Messages** (1): `AlertingConfig`

**Imports** (5):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/alert_rule.proto` → [queue_1](./queue_1.md#alert_rule)
- `pkg/queue/proto/alert_severity.proto` →
  [config_1](./config_1.md#alert_severity) →
  [metrics_1](./metrics_1.md#alert_severity) →
  [queue_1](./queue_1.md#alert_severity)
- `pkg/queue/proto/notification_channel.proto` →
  [config_1](./config_1.md#notification_channel) →
  [queue_1](./queue_1.md#notification_channel)

#### Source Code

```protobuf
// file: pkg/queue/proto/alerting_config.proto
// version: 1.1.0
// guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/alert_rule.proto";
import "pkg/queue/proto/alert_severity.proto";
import "pkg/queue/proto/notification_channel.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for queue alerting and notifications.
 */
message AlertingConfig {
  // Whether alerting is enabled
  bool enabled = 1;

  // List of alert rules
  repeated AlertRule rules = 2;

  // Notification channels for alerts
  repeated NotificationChannel channels = 3;

  // Default alert severity level
  AlertSeverity default_severity = 4;

  // Alert aggregation window
  google.protobuf.Duration aggregation_window = 5;
}

```

---

### authentication_config.proto {#authentication_config}

**Path**: `pkg/queue/proto/authentication_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 116

**Messages** (6): `AuthenticationConfig`, `UsernamePasswordAuth`, `APIKeyAuth`,
`TLSAuth`, `SASLAuth`, `OAuth2Auth`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/authentication_config.proto
// version: 1.0.0
// guid: b5c6d7e8-f9a0-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Authentication configuration for queue connections.
 * Supports multiple authentication mechanisms.
 */
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

/**
 * Username and password authentication.
 */
message UsernamePasswordAuth {
  // Username for authentication
  string username = 1;

  // Password for authentication (should be encrypted)
  string password = 2;
}

/**
 * API key based authentication.
 */
message APIKeyAuth {
  // API key for authentication
  string api_key = 1;

  // Optional API key ID
  string key_id = 2;
}

/**
 * TLS certificate authentication.
 */
message TLSAuth {
  // Client certificate (PEM format)
  string cert_pem = 1;

  // Client private key (PEM format)
  string key_pem = 2;

  // CA certificate (PEM format)
  string ca_pem = 3;

  // Whether to verify server certificate
  bool verify_server = 4;
}

/**
 * SASL authentication configuration.
 */
message SASLAuth {
  // SASL mechanism (PLAIN, SCRAM-SHA-256, etc.)
  string mechanism = 1;

  // Username
  string username = 2;

  // Password
  string password = 3;

  // Additional SASL properties
  map<string, string> properties = 4;
}

/**
 * OAuth2 authentication configuration.
 */
message OAuth2Auth {
  // OAuth2 token endpoint
  string token_endpoint = 1;

  // Client ID
  string client_id = 2;

  // Client secret
  string client_secret = 3;

  // Scopes to request
  repeated string scopes = 4;

  // Additional OAuth2 parameters
  map<string, string> parameters = 5;
}

```

---

### authorization_config.proto {#authorization_config}

**Path**: `pkg/queue/proto/authorization_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 185

**Messages** (10): `AuthorizationConfig`, `PermissionRule`,
`RoleBasedAccessControl`, `RoleInheritance`, `ExternalRoleProvider`,
`ApiKeyAuth`, `KeyValidationService`, `JwtAuth`, `ExternalAuthService`,
`AuthCacheConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/retry_config.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/authorization_config.proto
// version: 1.1.0
// Authorization configuration for queue access control

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/retry_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// AuthorizationConfig configures access control and permissions for queue operations
message AuthorizationConfig {
  // Enable authorization checking
  bool enabled = 1;

  // Default permission policy (allow/deny)
  string default_policy = 2;

  // Permission rules for different operations
  repeated PermissionRule rules = 3;

  // Role-based access control settings
  RoleBasedAccessControl rbac = 4;

  // API key authentication settings
  ApiKeyAuth api_key_auth = 5;

  // JWT token authentication settings
  JwtAuth jwt_auth = 6;

  // External authorization service settings
  ExternalAuthService external_auth = 7;
}

// Permission rule for specific operations
message PermissionRule {
  // Resource pattern (queue name, topic name, etc.)
  string resource_pattern = 1;

  // Operation (read, write, admin, etc.)
  string operation = 2;

  // Required roles or permissions
  repeated string required_roles = 3;

  // Allow or deny rule
  bool allow = 4;

  // Priority of this rule (higher number = higher priority)
  int32 priority = 5;
}

// Role-based access control configuration
message RoleBasedAccessControl {
  // Enable RBAC
  bool enabled = 1;

  // Default roles for new users
  repeated string default_roles = 2;

  // Role inheritance rules
  map<string, RoleInheritance> role_inheritance = 3;

  // External role provider settings
  ExternalRoleProvider external_provider = 4;
}

// Role inheritance configuration
message RoleInheritance {
  // Parent roles that this role inherits from
  repeated string inherits_from = 1;

  // Additional permissions for this role
  repeated string additional_permissions = 2;
}

// External role provider configuration
message ExternalRoleProvider {
  // Provider type (ldap, oauth, etc.)
  string provider_type = 1;

  // Provider endpoint URL
  string endpoint = 2;

  // Authentication credentials for provider
  map<string, string> credentials = 3;

  // Cache TTL for role lookups (seconds)
  int32 cache_ttl_seconds = 4;
}

// API key authentication configuration
message ApiKeyAuth {
  // Enable API key authentication
  bool enabled = 1;

  // Header name for API key
  string header_name = 2;

  // Query parameter name for API key (alternative to header)
  string query_param_name = 3;

  // Key validation service
  KeyValidationService validation_service = 4;
}

// Key validation service configuration
message KeyValidationService {
  // Service type (local, external, etc.)
  string service_type = 1;

  // Service endpoint (for external validation)
  string endpoint = 2;

  // Timeout for validation requests (milliseconds)
  int32 timeout_ms = 3;

  // Cache TTL for validation results (seconds)
  int32 cache_ttl_seconds = 4;
}

// JWT authentication configuration
message JwtAuth {
  // Enable JWT authentication
  bool enabled = 1;

  // JWT signing algorithm
  string algorithm = 2;

  // Public key or secret for verification
  string verification_key = 3;

  // Expected issuer
  string expected_issuer = 4;

  // Expected audience
  repeated string expected_audience = 5;

  // Clock skew tolerance (seconds)
  int32 clock_skew_seconds = 6;

  // Required claims
  map<string, string> required_claims = 7;
}

// External authorization service configuration
message ExternalAuthService {
  // Enable external authorization
  bool enabled = 1;

  // Authorization service endpoint
  string endpoint = 2;

  // Request timeout (milliseconds)
  int32 timeout_ms = 3;

  // Retry configuration - references existing RetryConfig
  RetryConfig retry_config = 4;

  // Cache configuration
  AuthCacheConfig cache_config = 5;

  // Headers to include in authorization requests
  map<string, string> request_headers = 6;
}

// Cache configuration for authorization results
message AuthCacheConfig {
  // Enable caching
  bool enabled = 1;

  // Cache TTL (seconds)
  int32 ttl_seconds = 2;

  // Maximum cache size
  int32 max_size = 3;

  // Cache cleanup interval (seconds)
  int32 cleanup_interval_seconds = 4;
}

```

---

### backup_config.proto {#backup_config}

**Path**: `pkg/queue/proto/backup_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 30

**Messages** (1): `BackupConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/backup_config.proto
// version: 1.0.0
// guid: 2e127d68-6db3-4c2e-a0ff-bb7a2e5542b8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// BackupConfig defines how queued messages should be backed up
// for disaster recovery.
message BackupConfig {
  // Interval between automatic backups.
  google.protobuf.Duration interval = 1;

  // Duration to retain each backup before deletion.
  google.protobuf.Duration retention = 2;

  // Storage location for backups (e.g., S3 bucket).
  string location = 3;

  // Whether backups are enabled for this queue.
  bool enabled = 4;
}

```

---

### batch_config.proto {#batch_config}

**Path**: `pkg/queue/proto/batch_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 40

**Messages** (1): `BatchConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/batch_config.proto
// file: queue/proto/messages/batch_config.proto
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a
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
 * Configuration for batch operations in queue processing.
 */
message BatchConfig {
  // Maximum number of messages per batch
  uint32 max_batch_size = 1;

  // Maximum time to wait before sending partial batch
  google.protobuf.Duration max_wait_time = 2;

  // Maximum total size of batch in bytes
  uint64 max_batch_bytes = 3;

  // Whether to enable batch compression
  bool enable_compression = 4;

  // Number of parallel batch workers
  uint32 worker_count = 5;

  // Buffer size for pending batches
  uint32 buffer_size = 6;
}

```

---

### circuit_breaker_config.proto {#circuit_breaker_config}

**Path**: `pkg/queue/proto/circuit_breaker_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 40

**Messages** (1): `CircuitBreakerConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/circuit_breaker_config.proto
// file: queue/proto/messages/circuit_breaker_config.proto
// version: 1.0.0
// guid: 6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f
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
 * Configuration for circuit breaker pattern in queue operations.
 */
message CircuitBreakerConfig {
  // Whether circuit breaker is enabled
  bool enabled = 1;

  // Failure threshold to open circuit
  uint32 failure_threshold = 2;

  // Success threshold to close circuit
  uint32 success_threshold = 3;

  // Timeout before attempting to close circuit
  google.protobuf.Duration timeout = 4;

  // Maximum number of concurrent requests in half-open state
  uint32 max_requests = 5;

  // Time window for failure counting
  google.protobuf.Duration interval = 6;
}

```

---

### cluster_config.proto {#cluster_config}

**Path**: `pkg/queue/proto/cluster_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 31

**Messages** (1): `ClusterConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/cluster_config.proto
// version: 1.0.0
// guid: 6ab9cf18-3f43-40f4-b289-163545acdc05

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for the cluster.
 */
message ClusterConfig {
  // Minimum number of nodes for quorum
  int32 quorum_size = 1;

  // Replication factor
  int32 replication_factor = 2;

  // Heartbeat interval in seconds
  int32 heartbeat_interval = 3;

  // Election timeout in seconds
  int32 election_timeout = 4;
}

```

---

### compression_config.proto {#compression_config}

**Path**: `pkg/queue/proto/compression_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 28

**Messages** (1): `CompressionConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/compression_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174000

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// CompressionConfig message definition.
message CompressionConfig {
  // Enable compression
  bool enabled = 1;

  // Compression algorithm
  string algorithm = 2;

  // Compression level (0-9)
  int32 level = 3;

  // Minimum message size to compress
  int32 min_size_bytes = 4;
}

```

---

### consistency_config.proto {#consistency_config}

**Path**: `pkg/queue/proto/consistency_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 328

**Messages** (16): `ConsistencyConfig`, `ReplicationConsistency`,
`ReadConsistency`, `WriteConsistency`, `SyncReplication`, `ConflictDetection`,
`VectorClockConfig`, `TimestampConfig`, `OrderingConfig`, `ConflictResolution`,
`CustomResolution`, `LastWriterWins`, `MultiValueConfig`,
`ConsistencyValidation`, `ReadRetryConfig`, `WriteRetryConfig`

**Enums** (6): `ReplicationLevel`, `ReadLevel`, `WriteLevel`,
`ConflictStrategy`, `OrderingLevel`, `ResolutionStrategy`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/ack_level.proto` → [queue_1](./queue_1.md#ack_level)
- `pkg/queue/proto/durability_level.proto` →
  [queue_1](./queue_1.md#durability_level)

#### Source Code

```protobuf
// file: pkg/queue/proto/consistency_config.proto
// version: 1.1.0
// Consistency configuration for queue data and messaging guarantees

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/ack_level.proto";
import "pkg/queue/proto/durability_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ConsistencyConfig configures data consistency and messaging guarantees
message ConsistencyConfig {
  // Durability level for message persistence
  DurabilityLevel durability_level = 1;

  // Acknowledgment level required for message delivery
  AckLevel ack_level = 2;

  // Replication configuration
  ReplicationConsistency replication = 3;

  // Read consistency settings
  ReadConsistency read_consistency = 4;

  // Write consistency settings
  WriteConsistency write_consistency = 5;

  // Ordering guarantees
  OrderingConfig ordering = 6;

  // Conflict resolution settings
  ConflictResolution conflict_resolution = 7;

  // Consistency validation settings
  ConsistencyValidation validation = 8;
}

// Replication consistency configuration
message ReplicationConsistency {
  // Minimum number of replicas that must acknowledge writes
  int32 min_write_replicas = 1;

  // Minimum number of replicas that must be available for reads
  int32 min_read_replicas = 2;

  // Replication factor (total number of replicas)
  int32 replication_factor = 3;

  // Consistency level for replication
  ReplicationLevel replication_level = 4;

  // Enable anti-entropy repair
  bool anti_entropy_enabled = 5;

  // Anti-entropy repair interval (seconds)
  int32 repair_interval_seconds = 6;
}

// Replication consistency level
enum ReplicationLevel {
  REPLICATION_LEVEL_UNSPECIFIED = 0;
  REPLICATION_LEVEL_ONE = 1; // At least one replica
  REPLICATION_LEVEL_QUORUM = 2; // Majority of replicas
  REPLICATION_LEVEL_ALL = 3; // All replicas
}

// Read consistency configuration
message ReadConsistency {
  // Read consistency level
  ReadLevel level = 1;

  // Maximum staleness allowed for reads (milliseconds)
  int64 max_staleness_ms = 2;

  // Enable read-your-writes consistency
  bool read_your_writes = 3;

  // Enable monotonic read consistency
  bool monotonic_reads = 4;

  // Timeout for read operations (milliseconds)
  int32 timeout_ms = 5;

  // Retry configuration for read failures
  ReadRetryConfig retry_config = 6;
}

// Read consistency level
enum ReadLevel {
  READ_LEVEL_UNSPECIFIED = 0;
  READ_LEVEL_EVENTUAL = 1; // Eventually consistent reads
  READ_LEVEL_STRONG = 2; // Strongly consistent reads
  READ_LEVEL_BOUNDED_STALENESS = 3; // Bounded staleness reads
  READ_LEVEL_SESSION = 4; // Session consistency
}

// Write consistency configuration
message WriteConsistency {
  // Write consistency level
  WriteLevel level = 1;

  // Synchronous replication requirements
  SyncReplication sync_replication = 2;

  // Write conflict detection
  ConflictDetection conflict_detection = 3;

  // Timeout for write operations (milliseconds)
  int32 timeout_ms = 4;

  // Retry configuration for write failures
  WriteRetryConfig retry_config = 5;
}

// Write consistency level
enum WriteLevel {
  WRITE_LEVEL_UNSPECIFIED = 0;
  WRITE_LEVEL_ASYNC = 1; // Asynchronous writes
  WRITE_LEVEL_SYNC_ONE = 2; // Synchronous to one replica
  WRITE_LEVEL_SYNC_QUORUM = 3; // Synchronous to quorum
  WRITE_LEVEL_SYNC_ALL = 4; // Synchronous to all replicas
}

// Synchronous replication configuration
message SyncReplication {
  // Enable synchronous replication
  bool enabled = 1;

  // Minimum synchronous replicas
  int32 min_sync_replicas = 2;

  // Timeout for synchronous replication (milliseconds)
  int32 sync_timeout_ms = 3;

  // Fallback to async on timeout
  bool fallback_to_async = 4;
}

// Conflict detection configuration
message ConflictDetection {
  // Enable conflict detection
  bool enabled = 1;

  // Conflict detection strategy
  ConflictStrategy strategy = 2;

  // Vector clock configuration
  VectorClockConfig vector_clock = 3;

  // Timestamp-based detection settings
  TimestampConfig timestamp_config = 4;
}

// Conflict detection strategy
enum ConflictStrategy {
  CONFLICT_STRATEGY_UNSPECIFIED = 0;
  CONFLICT_STRATEGY_TIMESTAMP = 1; // Timestamp-based detection
  CONFLICT_STRATEGY_VECTOR_CLOCK = 2; // Vector clock-based detection
  CONFLICT_STRATEGY_CAUSAL = 3; // Causal consistency detection
}

// Vector clock configuration
message VectorClockConfig {
  // Enable vector clocks
  bool enabled = 1;

  // Clock precision (nanoseconds, microseconds, milliseconds)
  string precision = 2;

  // Maximum clock drift tolerance (milliseconds)
  int64 max_drift_ms = 3;
}

// Timestamp configuration
message TimestampConfig {
  // Timestamp source (system, ntp, atomic)
  string source = 1;

  // Clock synchronization interval (seconds)
  int32 sync_interval_seconds = 2;

  // Maximum timestamp skew tolerance (milliseconds)
  int64 max_skew_ms = 3;
}

// Message ordering configuration
message OrderingConfig {
  // Global ordering guarantee level
  OrderingLevel global_ordering = 1;

  // Per-partition ordering guarantee
  OrderingLevel partition_ordering = 2;

  // Per-producer ordering guarantee
  OrderingLevel producer_ordering = 3;

  // Enable causal ordering
  bool causal_ordering = 4;

  // Ordering timeout (milliseconds)
  int32 ordering_timeout_ms = 5;
}

// Ordering guarantee level
enum OrderingLevel {
  ORDERING_LEVEL_UNSPECIFIED = 0;
  ORDERING_LEVEL_NONE = 1; // No ordering guarantees
  ORDERING_LEVEL_PARTIAL = 2; // Partial ordering
  ORDERING_LEVEL_TOTAL = 3; // Total ordering
}

// Conflict resolution configuration
message ConflictResolution {
  // Conflict resolution strategy
  ResolutionStrategy strategy = 1;

  // Custom resolution function settings
  CustomResolution custom_resolution = 2;

  // Last-writer-wins settings
  LastWriterWins lww_config = 3;

  // Multi-value conflict handling
  MultiValueConfig multi_value = 4;
}

// Conflict resolution strategy
enum ResolutionStrategy {
  RESOLUTION_STRATEGY_UNSPECIFIED = 0;
  RESOLUTION_STRATEGY_LAST_WRITER_WINS = 1; // Last writer wins
  RESOLUTION_STRATEGY_FIRST_WRITER_WINS = 2; // First writer wins
  RESOLUTION_STRATEGY_MERGE = 3; // Automatic merge
  RESOLUTION_STRATEGY_CUSTOM = 4; // Custom resolution function
  RESOLUTION_STRATEGY_MULTI_VALUE = 5; // Keep all conflicting values
}

// Custom conflict resolution configuration
message CustomResolution {
  // Resolution function name or identifier
  string function_name = 1;

  // Function parameters
  map<string, string> parameters = 2;

  // Timeout for resolution function (milliseconds)
  int32 timeout_ms = 3;
}

// Last-writer-wins configuration
message LastWriterWins {
  // Use server timestamp instead of client timestamp
  bool use_server_timestamp = 1;

  // Timestamp precision for comparison
  string timestamp_precision = 2;
}

// Multi-value conflict configuration
message MultiValueConfig {
  // Maximum number of concurrent values to keep
  int32 max_values = 1;

  // Value expiration time (seconds)
  int32 value_ttl_seconds = 2;

  // Conflict value cleanup strategy
  string cleanup_strategy = 3;
}

// Consistency validation configuration
message ConsistencyValidation {
  // Enable consistency validation
  bool enabled = 1;

  // Validation interval (seconds)
  int32 validation_interval_seconds = 2;

  // Validation scope (local, cluster, global)
  string validation_scope = 3;

  // Actions to take on validation failure
  repeated string failure_actions = 4;

  // Validation timeout (milliseconds)
  int32 timeout_ms = 5;
}

// Read retry configuration
message ReadRetryConfig {
  // Maximum retry attempts
  int32 max_retries = 1;

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2;

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3;

  // Backoff multiplier
  double backoff_multiplier = 4;

  // Retry on different replica
  bool retry_different_replica = 5;
}

// Write retry configuration
message WriteRetryConfig {
  // Maximum retry attempts
  int32 max_retries = 1;

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2;

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3;

  // Backoff multiplier
  double backoff_multiplier = 4;

  // Retry idempotent operations only
  bool idempotent_only = 5;
}

```

---

### dead_letter_config.proto {#dead_letter_config}

**Path**: `pkg/queue/proto/dead_letter_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 41

**Messages** (1): `DeadLetterConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/dead_letter_config.proto
// file: queue/proto/messages/dead_letter_config.proto
// version: 1.0.0
// guid: 8a7b6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d
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
 * Configuration for dead letter queue behavior.
 * Defines how messages that cannot be processed are handled.
 */
message DeadLetterConfig {
  // Whether dead letter queue functionality is enabled
  bool enabled = 1;

  // Name of the dead letter queue
  string dead_letter_queue_name = 2;

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

### deserialization_config.proto {#deserialization_config}

**Path**: `pkg/queue/proto/deserialization_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 40

**Messages** (1): `DeserializationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/serialization_format.proto` →
  [queue_2](./queue_2.md#serialization_format)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/deserialization_config.proto
// file: queue/proto/messages/deserialization_config.proto
// version: 1.0.0
// guid: 1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for message deserialization.
 */
message DeserializationConfig {
  // Supported serialization formats
  repeated gcommon.v1.queue.SerializationFormat supported_formats = 1;

  // Default format if not specified
  gcommon.v1.queue.SerializationFormat default_format = 2;

  // Whether to validate schema during deserialization
  bool validate_schema = 3;

  // Whether to allow unknown fields
  bool allow_unknown_fields = 4;

  // Custom deserializer class name
  string custom_deserializer = 5;

  // Maximum message size for deserialization (bytes)
  uint64 max_message_size = 6;
}

```

---

### durability_config.proto {#durability_config}

**Path**: `pkg/queue/proto/durability_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 48

**Messages** (1): `DurabilityConfig`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/ack_level.proto` → [queue_1](./queue_1.md#ack_level)
- `pkg/queue/proto/flush_policy.proto` → [queue_1](./queue_1.md#flush_policy)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/durability_config.proto
// file: queue/proto/messages/durability_config.proto
// version: 1.0.0
// guid: 1a0b9c8d-7e6f-5a4b-3c2d-1e0f9a8b7c6d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/ack_level.proto";
import "pkg/queue/proto/flush_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for message durability and persistence.
 */
message DurabilityConfig {
  // Whether messages are persisted to disk
  bool persistent = 1;

  // Flush policy for writing messages to storage
  gcommon.v1.queue.FlushPolicy flush_policy = 2;

  // Number of replicas for each message
  int32 replication_factor = 3;

  // Acknowledgment level required before considering message durable
  gcommon.v1.queue.AckLevel ack_level = 4;

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

**Path**: `pkg/queue/proto/encryption_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 42

**Messages** (1): `EncryptionConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/encryption_config.proto
// file: queue/proto/messages/encryption_config.proto
// version: 1.0.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for message encryption in queues.
 */
message EncryptionConfig {
  // Whether encryption is enabled
  bool enabled = 1;

  // Encryption algorithm (AES256, ChaCha20, etc.)
  string algorithm = 2;

  // Key derivation function (PBKDF2, scrypt, argon2)
  string key_derivation = 3;

  // Encryption key identifier
  string key_id = 4;

  // Whether to encrypt message headers
  bool encrypt_headers = 5;

  // Whether to encrypt routing keys
  bool encrypt_routing_keys = 6;

  // Key rotation interval in hours
  uint32 rotation_interval_hours = 7;
}

```

---

### exchange_config.proto {#exchange_config}

**Path**: `pkg/queue/proto/exchange_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 45

**Messages** (1): `ExchangeConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/exchange_config.proto
// file: queue/proto/messages/exchange_config.proto
// version: 1.0.0
// guid: 4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for message exchange operations between queues.
 */
message ExchangeConfig {
  // Exchange name
  string name = 1;

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

### header_routing_config.proto {#header_routing_config}

**Path**: `pkg/queue/proto/header_routing_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 27

**Messages** (1): `HeaderRoutingConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/header_routing_config.proto
// version: 1.0.0
// guid: 048332dd-afed-41ee-b803-dd1574fd07d9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Header-based routing configuration.
 */
message HeaderRoutingConfig {
  // Header key to use for routing
  string routing_header = 1;

  // Whether to use exact match or pattern matching
  bool exact_match = 2;

  // Case sensitivity for header matching
  bool case_sensitive = 3;
}

```

---

### load_balancing_config.proto {#load_balancing_config}

**Path**: `pkg/queue/proto/load_balancing_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 40

**Messages** (1): `LoadBalancingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/load_balancing_strategy.proto` →
  [queue_1](./queue_1.md#load_balancing_strategy)

#### Source Code

```protobuf
// file: pkg/queue/proto/load_balancing_config.proto
// version: 1.1.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/load_balancing_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for load balancing across queue consumers.
 */
message LoadBalancingConfig {
  // Load balancing strategy
  LoadBalancingStrategy strategy = 1;

  // Weight for this consumer (for weighted strategies)
  int32 weight = 2;

  // Maximum concurrent messages per consumer
  int32 max_concurrent_messages = 3;

  // Prefetch count for batch consumption
  int32 prefetch_count = 4;

  // Consumer priority (higher numbers = higher priority)
  int32 priority = 5;

  // Whether to enable sticky sessions
  bool sticky_sessions = 6;

  // Session affinity key
  string affinity_key = 7;
}

```

---

### migration_config.proto {#migration_config}

**Path**: `pkg/queue/proto/migration_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 46

**Messages** (1): `MigrationConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/migration_config.proto
// file: queue/proto/messages/migration_config.proto
// version: 1.0.0
// guid: 3d4e5f6a-7b8c-9d0e-1f2a-3b4c5d6e7f8a
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
 * Configuration for queue migration operations.
 */
message MigrationConfig {
  // Source queue configuration
  string source_queue = 1;

  // Destination queue configuration
  string destination_queue = 2;

  // Migration strategy (live, batch, hybrid)
  string migration_strategy = 3;

  // Batch size for batch migration
  uint32 batch_size = 4;

  // Migration timeout
  google.protobuf.Duration timeout = 5;

  // Whether to verify data integrity
  bool verify_integrity = 6;

  // Whether to keep source after migration
  bool keep_source = 7;

  // Maximum concurrent operations
  uint32 max_concurrency = 8;
}

```

---

### monitoring_config.proto {#monitoring_config}

**Path**: `pkg/queue/proto/monitoring_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 22

**Messages** (1): `MonitoringConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/monitoring_config.proto
// version: 1.0.0
// guid: 81f93ee4-708c-478c-9c19-1baf15830c08

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// MonitoringConfig controls runtime monitoring for a queue.
message MonitoringConfig {
  // Enable or disable monitoring for this queue.
  bool enabled = 1;

  // Optional endpoint for publishing metrics.
  string metrics_endpoint = 2;
}

```

---

### partition_config.proto {#partition_config}

**Path**: `pkg/queue/proto/partition_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 45

**Messages** (1): `PartitionConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/partition_config.proto
// file: queue/proto/messages/partition_config.proto
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for queue partitioning.
 */
message PartitionConfig {
  // Number of partitions
  uint32 partition_count = 1;

  // Partitioning strategy (hash, round-robin, custom)
  string partition_strategy = 2;

  // Key field to use for partitioning
  string partition_key = 3;

  // Custom partition function (if strategy is custom)
  string custom_partition_function = 4;

  // Whether to enable partition auto-scaling
  bool auto_scale = 5;

  // Minimum number of partitions
  uint32 min_partitions = 6;

  // Maximum number of partitions
  uint32 max_partitions = 7;

  // Partition size threshold for auto-scaling (in MB)
  uint64 scale_threshold_mb = 8;
}

```

---

### performance_config.proto {#performance_config}

**Path**: `pkg/queue/proto/performance_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 55

**Messages** (1): `PerformanceConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/performance_config.proto
// file: queue/proto/messages/performance_config.proto
// version: 1.0.0
// guid: 2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b
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
 * Configuration for performance tuning and optimization.
 */
message PerformanceConfig {
  // Buffer size for batching operations
  uint32 buffer_size = 1;

  // Maximum batch size for operations
  uint32 max_batch_size = 2;

  // Flush interval for buffered operations
  google.protobuf.Duration flush_interval = 3;

  // Number of worker threads
  uint32 worker_threads = 4;

  // Queue capacity for in-memory operations
  uint32 queue_capacity = 5;

  // Enable async processing
  bool async_processing = 6;

  // Connection pool size
  uint32 connection_pool_size = 7;

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

### queue_config.proto {#queue_config}

**Path**: `pkg/queue/proto/queue_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 34

**Messages** (1): `QueueConfig`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/priority_level.proto` →
  [queue_1](./queue_1.md#priority_level)
- `pkg/queue/proto/queue_type.proto` → [queue_2](./queue_2.md#queue_type)
- `pkg/queue/proto/retention_policy.proto` →
  [metrics_2](./metrics_2.md#retention_policy) →
  [queue_2](./queue_2.md#retention_policy)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/queue_config.proto
// version: 1.0.0
// guid: c64defde-30d1-41e5-bfac-b415cbf929c6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/priority_level.proto";
import "pkg/queue/proto/queue_type.proto";
import "pkg/queue/proto/retention_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// QueueConfig defines settings for creating a queue instance.
message QueueConfig {
  // Name of the queue.
  string name = 1;
  // Queue implementation type.
  QueueType type = 2;
  // Number of partitions for the queue.
  int32 partitions = 3;
  // Retention policy for stored messages.
  RetentionPolicy retention = 4;
  // Default priority applied when publishing.
  PriorityLevel default_priority = 5;
  // If true, queue persists messages to disk.
  bool durable = 6;
  // Whether the queue should be automatically deleted when unused.
  bool auto_delete = 7;
}

```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `pkg/queue/proto/rate_limit_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 25

**Messages** (1): `RateLimitConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/rate_limit_config.proto
// version: 1.0.0
// guid: 436ea189-70d7-4f1d-bf93-3c88f1f0de3b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// RateLimitConfig defines throughput limits for a queue.
message RateLimitConfig {
  // Maximum messages allowed per second.
  int32 max_per_second = 1;

  // Allowed burst capacity above the per-second rate.
  int32 burst = 2;

  // Whether rate limiting is enabled.
  bool enabled = 3;
}

```

---

### replication_config.proto {#replication_config}

**Path**: `pkg/queue/proto/replication_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ReplicationConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/replication_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ReplicationConfig message definition.
message ReplicationConfig {
  // Number of replicas
  int32 replica_count = 1;

  // Replication factor
  int32 factor = 2;

  // Enable synchronous replication
  bool synchronous = 3;

  // Minimum in-sync replicas
  int32 min_in_sync_replicas = 4;
}

```

---

### restore_config.proto {#restore_config}

**Path**: `pkg/queue/proto/restore_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 46

**Messages** (1): `RestoreConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/restore_config.proto
// file: queue/proto/messages/restore_config.proto
// version: 1.0.0
// guid: 9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a
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
 * Configuration for queue restore operations.
 */
message RestoreConfig {
  // Source backup location
  string backup_source = 1;

  // Whether to verify backup integrity before restore
  bool verify_integrity = 2;

  // Restore strategy (full, incremental, selective)
  string restore_strategy = 3;

  // Whether to overwrite existing data
  bool overwrite_existing = 4;

  // Restore timeout
  google.protobuf.Duration timeout = 5;

  // Whether to preserve original timestamps
  bool preserve_timestamps = 6;

  // Maximum concurrent restore operations
  uint32 max_concurrency = 7;

  // Whether to skip corrupted messages
  bool skip_corrupted = 8;
}

```

---

### retry_config.proto {#retry_config}

**Path**: `pkg/queue/proto/retry_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 43

**Messages** (1): `RetryConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/retry_config.proto
// file: queue/proto/messages/retry_config.proto
// version: 1.0.0
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
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
 * Configuration for retry behavior in queue operations.
 */
message RetryConfig {
  // Whether retry is enabled
  bool enabled = 1;

  // Maximum number of retry attempts
  uint32 max_retries = 2;

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 3;

  // Maximum delay between retries
  google.protobuf.Duration max_delay = 4;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 5;

  // Jitter factor to randomize delays (0.0 to 1.0)
  double jitter_factor = 6;

  // Total timeout for all retry attempts
  google.protobuf.Duration total_timeout = 7;
}

```

---

### routing_config.proto {#routing_config}

**Path**: `pkg/queue/proto/routing_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 28

**Messages** (1): `RoutingConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/routing_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174002

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// RoutingConfig message definition.
message RoutingConfig {
  // Routing strategy
  string strategy = 1;

  // Routing key pattern
  string key_pattern = 2;

  // Enable sticky routing
  bool sticky = 3;

  // Load balancing algorithm
  string load_balancer = 4;
}

```

---

### schema_config.proto {#schema_config}

**Path**: `pkg/queue/proto/schema_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 28

**Messages** (1): `SchemaConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/schema_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174003

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// SchemaConfig message definition.
message SchemaConfig {
  // Schema version
  int32 version = 1;

  // Schema definition
  string definition = 2;

  // Schema type
  string type = 3;

  // Enable schema validation
  bool validate = 4;
}

```

---

### serialization_config.proto {#serialization_config}

**Path**: `pkg/queue/proto/serialization_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 51

**Messages** (1): `SerializationConfig`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/compression_algorithm.proto` →
  [queue_1](./queue_1.md#compression_algorithm)
- `pkg/queue/proto/format_options.proto` →
  [queue_1](./queue_1.md#format_options)
- `pkg/queue/proto/serialization_format.proto` →
  [queue_2](./queue_2.md#serialization_format)

#### Source Code

```protobuf
// file: pkg/queue/proto/serialization_config.proto
// version: 1.0.0
// guid: e5f6a7b8-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/compression_algorithm.proto";
import "pkg/queue/proto/format_options.proto";
import "pkg/queue/proto/serialization_format.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for message serialization and deserialization.
 */
message SerializationConfig {
  // Default serialization format
  gcommon.v1.queue.SerializationFormat default_format = 1;

  // Supported serialization formats
  repeated gcommon.v1.queue.SerializationFormat supported_formats = 2;

  // Whether to auto-detect format from message headers
  bool auto_detect_format = 3;

  // Default compression algorithm
  CompressionAlgorithm default_compression = 4;

  // Supported compression algorithms
  repeated CompressionAlgorithm supported_compressions = 5;

  // Whether to auto-detect compression from message headers
  bool auto_detect_compression = 6;

  // Format-specific options
  map<string, FormatOptions> format_options = 7;

  // Whether to validate message format on deserialization
  bool validate_on_deserialize = 8;

  // Maximum message size for serialization
  uint64 max_message_size = 9;

  // Whether to enable backwards compatibility mode
  bool backwards_compatible = 10;
}

```

---

### stream_config.proto {#stream_config}

**Path**: `pkg/queue/proto/stream_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 50

**Messages** (1): `StreamConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/stream_restart_policy.proto` →
  [queue_2](./queue_2.md#stream_restart_policy)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/stream_config.proto
// file: queue/proto/messages/stream_config.proto
// version: 1.0.0
// guid: 7a6b5c4d-3e2f-1a0b-9c8d-7e6f5a4b3c2d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/stream_restart_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for streaming message consumption.
 */
message StreamConfig {
  // Maximum number of messages to buffer
  int32 buffer_size = 1;

  // Timeout for stream read operations
  google.protobuf.Duration read_timeout = 2;

  // Whether to enable flow control
  bool flow_control_enabled = 3;

  // Maximum outstanding messages before flow control kicks in
  int32 max_outstanding_messages = 4;

  // Maximum outstanding bytes before flow control kicks in
  int64 max_outstanding_bytes = 5;

  // Whether to automatically acknowledge messages
  bool auto_ack = 6;

  // Acknowledgment deadline for manually acknowledged messages
  google.protobuf.Duration ack_deadline = 7;

  // Whether to enable message ordering
  bool enable_message_ordering = 8;

  // Stream restart policy on failure
  gcommon.v1.queue.StreamRestartPolicy restart_policy = 9;
}

```

---

### subscription_config.proto {#subscription_config}

**Path**: `pkg/queue/proto/subscription_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 33

**Messages** (1): `SubscriptionConfig`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/delivery_options.proto` →
  [queue_1](./queue_1.md#delivery_options)
- `pkg/queue/proto/priority_level.proto` →
  [queue_1](./queue_1.md#priority_level)
- `pkg/queue/proto/routing_strategy.proto` →
  [queue_2](./queue_2.md#routing_strategy)
- `pkg/queue/proto/subscription_state.proto` →
  [queue_2](./queue_2.md#subscription_state)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/subscription_config.proto
// version: 1.0.0
// guid: 27b1d56b-2e7b-4003-9ddd-6b30086ff0fb

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/delivery_options.proto";
import "pkg/queue/proto/priority_level.proto";
import "pkg/queue/proto/routing_strategy.proto";
import "pkg/queue/proto/subscription_state.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// SubscriptionConfig describes how a consumer subscribes to a queue.
message SubscriptionConfig {
  // Name of the subscription.
  string name = 1;
  // Current state of the subscription.
  SubscriptionState state = 2;
  // Message routing strategy for this subscription.
  RoutingStrategy routing_strategy = 3;
  // Default priority applied to published messages if unspecified.
  PriorityLevel default_priority = 4;
  // Delivery options controlling retries and dead letter handling.
  DeliveryOptions delivery_options = 5;
  // Maximum number of unacknowledged messages allowed.
  int32 max_inflight = 6;
}

```

---

### timeout_config.proto {#timeout_config}

**Path**: `pkg/queue/proto/timeout_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 46

**Messages** (1): `TimeoutConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/timeout_config.proto
// file: queue/proto/messages/timeout_config.proto
// version: 1.0.0
// guid: 3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d
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
 * Timeout configuration for various queue operations.
 */
message TimeoutConfig {
  // Timeout for message publishing operations
  google.protobuf.Duration publish_timeout = 1;

  // Timeout for message consumption operations
  google.protobuf.Duration consume_timeout = 2;

  // Timeout for acknowledgment operations
  google.protobuf.Duration ack_timeout = 3;

  // Timeout for connection establishment
  google.protobuf.Duration connect_timeout = 4;

  // Timeout for message processing before automatic nack
  google.protobuf.Duration processing_timeout = 5;

  // Timeout for queue management operations (create, delete, etc.)
  google.protobuf.Duration management_timeout = 6;

  // Timeout for health check operations
  google.protobuf.Duration health_check_timeout = 7;

  // Timeout for subscription operations
  google.protobuf.Duration subscription_timeout = 8;
}

```

---

### topic_config.proto {#topic_config}

**Path**: `pkg/queue/proto/topic_config.proto` **Package**: `gcommon.v1.queue`
**Lines**: 48

**Messages** (1): `TopicConfig`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/queue/proto/partition_config.proto`
- `pkg/queue/proto/retention_policy.proto` →
  [metrics_2](./metrics_2.md#retention_policy) →
  [queue_2](./queue_2.md#retention_policy)

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/topic_config.proto
// file: queue/proto/messages/topic_config.proto
// version: 1.0.0
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/queue/proto/partition_config.proto";
import "pkg/queue/proto/retention_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration settings for a topic.
 */
message TopicConfig {
  // Maximum number of messages in the topic
  uint64 max_messages = 1;

  // Maximum size of the topic in bytes
  uint64 max_size_bytes = 2;

  // Message retention policy
  gcommon.v1.queue.RetentionPolicy retention_policy = 3;

  // Partitioning configuration
  gcommon.v1.queue.PartitionConfig partition_config = 4;

  // Whether messages are persistent
  bool persistent = 5;

  // Whether topic is replicated
  bool replicated = 6;

  // Replication factor
  uint32 replication_factor = 7;

  // Whether to compact duplicate messages
  bool enable_compaction = 8;
}

```

---

### topic_routing_config.proto {#topic_routing_config}

**Path**: `pkg/queue/proto/topic_routing_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 27

**Messages** (1): `TopicRoutingConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/topic_routing_config.proto
// version: 1.0.0
// guid: 502467f7-3d79-4329-8e44-4e499071092b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Topic-based routing configuration.
 */
message TopicRoutingConfig {
  // Topic exchange name
  string exchange_name = 1;

  // Default routing key
  string default_routing_key = 2;

  // Whether to use wildcard matching
  bool wildcard_matching = 3;
}

```

---

### transformation_config.proto {#transformation_config}

**Path**: `pkg/queue/proto/transformation_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 45

**Messages** (1): `TransformationConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/transformation_config.proto
// file: queue/proto/messages/transformation_config.proto
// version: 1.0.0
// guid: 2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Configuration for message transformation operations.
 */
message TransformationConfig {
  // Whether transformation is enabled
  bool enabled = 1;

  // Transformation script or function name
  string transformation_script = 2;

  // Script language (javascript, python, lua, etc.)
  string script_language = 3;

  // Whether to transform on ingress
  bool transform_on_ingress = 4;

  // Whether to transform on egress
  bool transform_on_egress = 5;

  // Transformation timeout in milliseconds
  uint64 timeout_ms = 6;

  // Maximum script execution memory in MB
  uint32 max_memory_mb = 7;

  // Custom transformation parameters
  map<string, string> parameters = 8;
}

```

---

### update_queue_config_request.proto {#update_queue_config_request}

**Path**: `pkg/queue/proto/update_queue_config_request.proto` **Package**:
`gcommon.v1.queue` **Lines**: 39

**Messages** (1): `UpdateQueueConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/queue/proto/queue_config.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/update_queue_config_request.proto
// version: 1.0.0
// guid: e2f3a4b5-c6d7-8e9f-0a1b-2c3d4e5f6a7b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/queue/proto/queue_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Request to update configuration for an existing queue.
 * Allows modification of queue properties after creation.
 */
message UpdateQueueConfigRequest {
  // Name of the queue to update
  string queue_name = 1;

  // New configuration for the queue
  gcommon.v1.queue.QueueConfig config = 2;

  // Fields to update (field mask)
  repeated string update_mask = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Force update even if it might cause data loss
  bool force = 5;

  // Reason for the configuration update
  string reason = 6;
}

```

---

### update_queue_config_response.proto {#update_queue_config_response}

**Path**: `pkg/queue/proto/update_queue_config_response.proto` **Package**:
`gcommon.v1.queue` **Lines**: 36

**Messages** (1): `UpdateQueueConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/update_queue_config_response.proto
// file: queue/proto/responses/update_queue_config_response.proto
// version: 1.0.0
// guid: 6e7f8a9b-0c1d-2e3f-4a5b-6c7d8e9f0a1b
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

/**
 * Response for updating queue configuration.
 */
message UpdateQueueConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Error message if update failed
  string error_message = 2;

  // Updated configuration version
  uint64 config_version = 3;

  // Timestamp of the update
  uint64 updated_at = 4;

  // List of configuration fields that were updated
  repeated string updated_fields = 5;
}

```

---

### update_subscription_config_request.proto {#update_subscription_config_request}

**Path**: `pkg/queue/proto/update_subscription_config_request.proto`
**Package**: `gcommon.v1.queue` **Lines**: 124

**Messages** (6): `UpdateSubscriptionConfigRequest`, `SubscriptionConfigUpdate`,
`DeliverySettings`, `RetrySettings`, `FilterSettings`, `RoutingSettings`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/update_subscription_config_request.proto
// version: 1.1.0
// Request to update subscription configuration

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// UpdateSubscriptionConfigRequest modifies subscription configuration settings
message UpdateSubscriptionConfigRequest {
  // Subscription identifier
  string subscription_id = 1;

  // Configuration updates to apply
  SubscriptionConfigUpdate config_update = 2;

  // Specify which fields to update (empty = update all)
  repeated string update_fields = 3;

  // Validate configuration without applying changes
  bool validate_only = 4;

  // Force update even if subscription is active
  bool force_update = 5;

  // Apply changes immediately or schedule for later
  bool immediate_apply = 6;

  // Optional reason for the configuration change
  string change_reason = 7;

  // Metadata for the update operation
  map<string, string> metadata = 8;
}

// Configuration updates for a subscription
message SubscriptionConfigUpdate {
  // Updated subscription name
  string name = 1;

  // Updated delivery settings
  DeliverySettings delivery_settings = 2;

  // Updated retry configuration
  RetrySettings retry_settings = 3;

  // Updated filtering rules
  FilterSettings filter_settings = 4;

  // Updated routing configuration
  RoutingSettings routing_settings = 5;

  // Maximum inflight messages
  int32 max_inflight_messages = 6;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 7;

  // Priority level for messages
  int32 priority_level = 8;
}

// Delivery settings for subscription
message DeliverySettings {
  // Delivery mode (push, pull, streaming)
  string delivery_mode = 1;

  // Endpoint for push delivery
  string push_endpoint = 2;

  // Delivery timeout (milliseconds)
  int32 delivery_timeout_ms = 3;

  // Enable ordered delivery
  bool ordered_delivery = 4;
}

// Retry settings for failed deliveries
message RetrySettings {
  // Maximum retry attempts
  int32 max_retries = 1;

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2;

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3;

  // Backoff multiplier
  double backoff_multiplier = 4;

  // Dead letter queue topic
  string dead_letter_topic = 5;
}

// Message filtering settings
message FilterSettings {
  // Content-based filters
  map<string, string> content_filters = 1;

  // Header-based filters
  map<string, string> header_filters = 2;

  // Filter expression
  string filter_expression = 3;
}

// Message routing settings
message RoutingSettings {
  // Routing key pattern
  string routing_key_pattern = 1;

  // Target partitions
  repeated int32 target_partitions = 2;

  // Routing strategy
  string routing_strategy = 3;
}

```

---

### update_subscription_config_response.proto {#update_subscription_config_response}

**Path**: `pkg/queue/proto/update_subscription_config_response.proto`
**Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `UpdateSubscriptionConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/update_subscription_config_response.proto
// version: 1.0.0
// Response for subscription configuration updates

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Response for subscription configuration updates
message UpdateSubscriptionConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Subscription ID that was updated
  string subscription_id = 2;

  // Configuration changes that were applied
  map<string, string> applied_changes = 3;

  // Validation warnings (non-fatal)
  repeated string warnings = 4;

  // Error message if update failed
  string error = 5;
}

```

---

### update_topic_config_request.proto {#update_topic_config_request}

**Path**: `pkg/queue/proto/update_topic_config_request.proto` **Package**:
`gcommon.v1.queue` **Lines**: 32

**Messages** (1): `UpdateTopicConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/queue/proto/topic_config.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/update_topic_config_request.proto
// version: 1.0.0
// Request to update topic configuration

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "pkg/queue/proto/topic_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// Request to update topic configuration
message UpdateTopicConfigRequest {
  // Topic name to update
  string topic_name = 1;

  // New topic configuration
  TopicConfig config = 2;

  // Whether to validate config before applying
  bool validate_only = 3;

  // Apply changes incrementally if possible
  bool incremental_update = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}

```

---

### update_topic_config_response.proto {#update_topic_config_response}

**Path**: `pkg/queue/proto/update_topic_config_response.proto` **Package**:
`gcommon.v1.queue` **Lines**: 43

**Messages** (1): `UpdateTopicConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/responses/update_topic_config_response.proto
// file: queue/proto/responses/update_topic_config_response.proto
// version: 1.0.0
// guid: 2e1f0d9c-8b7a-6e5f-4d3c-2b1a0f9e8d7c
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
 * Response message for topic configuration update operations.
 */
message UpdateTopicConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Error message if update failed
  string error_message = 2;

  // The name of the topic that was updated
  string topic_name = 3;

  // Timestamp when the update was applied
  google.protobuf.Timestamp updated_at = 4;

  // Configuration revision number after update
  uint64 config_revision = 5;

  // List of configuration fields that were modified
  repeated string modified_fields = 6;

  // Validation warnings (non-fatal issues)
  repeated string warnings = 7;
}

```

---

### validation_config.proto {#validation_config}

**Path**: `pkg/queue/proto/validation_config.proto` **Package**:
`gcommon.v1.queue` **Lines**: 23

**Messages** (1): `ValidationConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/queue/proto/messages/validation_config.proto
// version: 1.0.0
// guid: 50a55c81-98ea-49a5-8d18-c188a48acc5f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto";

// ValidationConfig defines rules for validating queued messages.
message ValidationConfig {
  // Whether to validate message schema.
  bool validate_schema = 1;
  // Maximum allowed size of the message body in bytes.
  int64 max_body_bytes = 2;
  // If true, reject messages that exceed validation limits.
  bool reject_invalid = 3;
}

```

---
