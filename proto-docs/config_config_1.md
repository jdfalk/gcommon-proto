# config_config_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 64
- **Services**: 0
- **Enums**: 2

## Files in this Module

- [audit_settings.proto](#audit_settings)
- [backup_config_request.proto](#backup_config_request)
- [backup_settings.proto](#backup_settings)
- [batching_settings.proto](#batching_settings)
- [caching_settings.proto](#caching_settings)
- [compliance_settings.proto](#compliance_settings)
- [config_backup.proto](#config_backup)
- [config_change.proto](#config_change)
- [config_change_type.proto](#config_change_type)
- [config_data_type.proto](#config_data_type)
- [config_diff.proto](#config_diff)
- [config_entry.proto](#config_entry)
- [config_environment.proto](#config_environment)
- [config_schema.proto](#config_schema)
- [config_snapshot.proto](#config_snapshot)
- [config_stats.proto](#config_stats)
- [config_validation_error.proto](#config_validation_error)
- [config_validation_warning.proto](#config_validation_warning)
- [config_watch.proto](#config_watch)
- [decrypt_config_request.proto](#decrypt_config_request)
- [delete_config_request.proto](#delete_config_request)
- [encrypt_config_request.proto](#encrypt_config_request)
- [export_config_request.proto](#export_config_request)
- [get_config_history_request.proto](#get_config_history_request)
- [get_config_history_response.proto](#get_config_history_response)
- [get_config_request.proto](#get_config_request)
- [get_config_response.proto](#get_config_response)
- [get_config_stats_request.proto](#get_config_stats_request)
- [get_config_stats_response.proto](#get_config_stats_response)
- [get_multiple_config_request.proto](#get_multiple_config_request)
- [get_multiple_config_response.proto](#get_multiple_config_response)
- [import_config_request.proto](#import_config_request)
- [inheritance_settings.proto](#inheritance_settings)
- [list_config_request.proto](#list_config_request)
- [list_config_response.proto](#list_config_response)
- [monitoring_settings.proto](#monitoring_settings)
- [notification_settings.proto](#notification_settings)
- [reload_config_request.proto](#reload_config_request)
- [restore_config_request.proto](#restore_config_request)
- [retry_settings.proto](#retry_settings)
- [rollback_config_request.proto](#rollback_config_request)
- [rotation_settings.proto](#rotation_settings)
- [secret_audit_settings.proto](#secret_audit_settings)
- [secret_backup_settings.proto](#secret_backup_settings)
- [set_config_request.proto](#set_config_request)
- [set_config_response.proto](#set_config_response)
- [set_config_schema_request.proto](#set_config_schema_request)
- [set_multiple_config_request.proto](#set_multiple_config_request)
- [set_multiple_config_response.proto](#set_multiple_config_response)
- [synchronization_settings.proto](#synchronization_settings)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_1](./config_1.md)
- [config_2](./config_2.md)
- [config_events](./config_events.md)
- [metrics_config](./metrics_config.md)
- [queue_1](./queue_1.md)

**Modules that depend on this one**:

- [config_1](./config_1.md)
- [config_api](./config_api.md)
- [config_config_2](./config_config_2.md)
- [config_services](./config_services.md)
- [metrics_2](./metrics_2.md)

---

## Detailed Documentation

### audit_settings.proto {#audit_settings}

**Path**: `pkg/config/proto/audit_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 38

**Messages** (1): `AuditSettings`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` →
  [config_events](./config_events.md#audit_level)

#### Source Code

```protobuf
// file: pkg/config/proto/audit_settings.proto
// version: 1.0.0
// guid: be3f66f2-0951-46ae-b393-e44f8132948b

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/audit_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message AuditSettings {
  // Whether audit logging is enabled
  bool enabled = 1;

  // Audit log level
  AuditLevel level = 2;

  // Audit log retention period in days
  int32 retention_days = 3;

  // Whether to include sensitive data in audit logs
  bool include_sensitive_data = 4;

  // External audit destinations
  repeated string destinations = 5;

  // Audit log format
  string format = 6;

  // Additional audit metadata
  map<string, string> metadata = 7;
}

```

---

### backup_config_request.proto {#backup_config_request}

**Path**: `pkg/config/proto/backup_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 33

**Messages** (1): `BackupConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/backup_config_request.proto
// file: config/proto/requests/backup_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * BackupConfigRequest triggers creation of a configuration backup.
 */
message BackupConfigRequest {
  // Namespace or environment to back up
  string namespace = 1;

  // Optional description for the backup
  string description = 2;

  // Include secrets in the backup
  bool include_secrets = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### backup_settings.proto {#backup_settings}

**Path**: `pkg/config/proto/backup_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 38

**Messages** (1): `BackupSettings`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/backup_frequency.proto` →
  [config_1](./config_1.md#backup_frequency)

#### Source Code

```protobuf
// file: pkg/config/proto/backup_settings.proto
// version: 1.0.0
// guid: e9a07253-25f8-4306-ad78-31325ce9b271

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/backup_frequency.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message BackupSettings {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup frequency
  BackupFrequency frequency = 2;

  // Backup retention period in days
  int32 retention_days = 3;

  // Backup storage location
  string storage_location = 4;

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup metadata
  map<string, string> metadata = 7;
}

```

---

### batching_settings.proto {#batching_settings}

**Path**: `pkg/config/proto/batching_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 35

**Messages** (1): `BatchingSettings`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` →
  [config_events](./config_events.md#audit_level)
- `pkg/config/proto/backup_frequency.proto` →
  [config_1](./config_1.md#backup_frequency)
- `pkg/config/proto/channel_type.proto` → [config_1](./config_1.md#channel_type)
- `pkg/config/proto/config_data_type.proto`
- `pkg/config/proto/deprecation_level.proto` →
  [config_1](./config_1.md#deprecation_level)
- `pkg/config/proto/metadata_status.proto` →
  [config_1](./config_1.md#metadata_status)
- `pkg/config/proto/notification_trigger.proto` →
  [config_1](./config_1.md#notification_trigger)

#### Source Code

```protobuf
// file: pkg/config/proto/batching_settings.proto
// version: 1.0.0
// guid: 2814da2b-956d-4e34-b87c-7bf8c1bceb5e

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/audit_level.proto";
import "pkg/config/proto/backup_frequency.proto";
import "pkg/config/proto/channel_type.proto";
import "pkg/config/proto/config_data_type.proto";
import "pkg/config/proto/deprecation_level.proto";
import "pkg/config/proto/metadata_status.proto";
import "pkg/config/proto/notification_trigger.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message BatchingSettings {
  // Whether batching is enabled
  bool enabled = 1;

  // Batch size
  int32 batch_size = 2;

  // Batch timeout in minutes
  int32 timeout_minutes = 3;

  // Batch grouping key
  string grouping_key = 4;
}

```

---

### caching_settings.proto {#caching_settings}

**Path**: `pkg/config/proto/caching_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 34

**Messages** (1): `CachingSettings`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/cache_invalidation_trigger.proto` →
  [config_1](./config_1.md#cache_invalidation_trigger)
- `pkg/config/proto/cache_refresh_strategy.proto` →
  [config_1](./config_1.md#cache_refresh_strategy)

#### Source Code

```protobuf
// file: pkg/config/proto/caching_settings.proto
// version: 1.0.0
// guid: 2c6f8039-2855-4a31-884a-4d66d71cf897

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/cache_invalidation_trigger.proto";
import "pkg/config/proto/cache_refresh_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message CachingSettings {
  // Whether caching is enabled
  bool enabled = 1;

  // Cache TTL in seconds
  int32 ttl_seconds = 2;

  // Cache refresh strategy
  CacheRefreshStrategy refresh_strategy = 3;

  // Cache invalidation triggers
  repeated CacheInvalidationTrigger triggers = 4;

  // Cache metadata
  map<string, string> metadata = 5;
}

```

---

### compliance_settings.proto {#compliance_settings}

**Path**: `pkg/config/proto/compliance_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 36

**Messages** (1): `ComplianceSettings`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/compliance_audit.proto` →
  [config_events](./config_events.md#compliance_audit)
- `pkg/config/proto/compliance_reporting.proto` →
  [config_1](./config_1.md#compliance_reporting)

#### Source Code

```protobuf
// file: pkg/config/proto/compliance_settings.proto
// version: 1.0.0
// guid: 55ae9eb4-4811-4e34-89e6-b2c7f128297e

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/compliance_audit.proto";
import "pkg/config/proto/compliance_reporting.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceSettings {
  // Compliance frameworks
  repeated string frameworks = 1;

  // Compliance policies
  repeated string policies = 2;

  // Compliance audits
  repeated ComplianceAudit audits = 3;

  // Compliance reporting
  ComplianceReporting reporting = 4;

  // Compliance validation
  bool validation_enabled = 5;

  // Compliance metadata
  map<string, string> metadata = 6;
}

```

---

### config_backup.proto {#config_backup}

**Path**: `pkg/config/proto/config_backup.proto` **Package**:
`gcommon.v1.config` **Lines**: 63

**Messages** (1): `ConfigBackup`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_backup.proto
// version: 1.0.0
// guid: vw2xyz01-34a5-6b7c-8d9e-0f1g2h3i4j5k

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * Represents a configuration backup.
 * Stores complete configuration state for recovery purposes.
 */
message ConfigBackup {
  // Unique identifier for this backup
  string backup_id = 1;

  // Timestamp when backup was created
  google.protobuf.Timestamp created_at = 2;

  // Configuration values at backup time
  map<string, google.protobuf.Any> config_values = 3;

  // Version of the configuration
  string version = 4;

  // Environment or context (e.g., "production", "staging")
  string environment = 5;

  // User or service that created the backup
  string created_by = 6;

  // Description or reason for the backup
  string description = 7;

  // Backup type (MANUAL, SCHEDULED, AUTOMATIC)
  string backup_type = 8;

  // Checksum or hash of the configuration
  string checksum = 9;

  // Size of the backup in bytes
  int64 size_bytes = 10;

  // Compression used (if any)
  string compression = 11;

  // Storage location or path
  string storage_path = 12;

  // Retention policy for this backup
  string retention_policy = 13;

  // Additional metadata
  map<string, string> metadata = 14;
}

```

---

### config_change.proto {#config_change}

**Path**: `pkg/config/proto/config_change.proto` **Package**:
`gcommon.v1.config` **Lines**: 51

**Messages** (1): `ConfigChange`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_change.proto
// version: 1.0.0
// guid: rs8tuvwx-90y1-2z3a-4b5c-6d7e8f9g0h1i

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * Represents a configuration change event.
 * Tracks what changed, when, and who made the change.
 */
message ConfigChange {
  // Unique identifier for this change
  string change_id = 1;

  // Configuration key that changed
  string key = 2;

  // Previous value (if any)
  google.protobuf.Any old_value = 3;

  // New value
  google.protobuf.Any new_value = 4;

  // Type of change (CREATE, UPDATE, DELETE)
  string change_type = 5;

  // Timestamp of the change
  google.protobuf.Timestamp timestamp = 6;

  // User or service that made the change
  string changed_by = 7;

  // Reason for the change
  string reason = 8;

  // Configuration namespace or section
  string namespace = 9;

  // Additional metadata about the change
  map<string, string> metadata = 10;
}

```

---

### config_change_type.proto {#config_change_type}

**Path**: `pkg/config/proto/config_change_type.proto` **Package**:
`gcommon.v1.config` **Lines**: 20

**Enums** (1): `ConfigChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/enums/config_change_type.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ConfigChangeType enumerates configuration change events.
 */
enum ConfigChangeType {
  CONFIG_CHANGE_TYPE_UNSPECIFIED = 0;
  CONFIG_CHANGE_TYPE_CREATED = 1;
  CONFIG_CHANGE_TYPE_UPDATED = 2;
  CONFIG_CHANGE_TYPE_DELETED = 3;
}

```

---

### config_data_type.proto {#config_data_type}

**Path**: `pkg/config/proto/config_data_type.proto` **Package**:
`gcommon.v1.config` **Lines**: 42

**Enums** (1): `ConfigDataType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/config_data_type.proto
// version: 1.0.0
// guid: f619e4df-f067-46db-a813-30458f7fd517

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ConfigDataType {
  CONFIG_DATA_TYPE_UNSPECIFIED = 0;
  CONFIG_DATA_TYPE_STRING = 1;
  CONFIG_DATA_TYPE_INTEGER = 2;
  CONFIG_DATA_TYPE_FLOAT = 3;
  CONFIG_DATA_TYPE_BOOLEAN = 4;
  CONFIG_DATA_TYPE_ENUM = 5;
  CONFIG_DATA_TYPE_LIST = 6;
  CONFIG_DATA_TYPE_MAP = 7;
  CONFIG_DATA_TYPE_JSON = 8;
  CONFIG_DATA_TYPE_YAML = 9;
  CONFIG_DATA_TYPE_URL = 10;
  CONFIG_DATA_TYPE_EMAIL = 11;
  CONFIG_DATA_TYPE_PASSWORD = 12;
  CONFIG_DATA_TYPE_CERTIFICATE = 13;
  CONFIG_DATA_TYPE_PRIVATE_KEY = 14;
  CONFIG_DATA_TYPE_PUBLIC_KEY = 15;
  CONFIG_DATA_TYPE_DURATION = 16;
  CONFIG_DATA_TYPE_TIMESTAMP = 17;
  CONFIG_DATA_TYPE_REGEX = 18;
  CONFIG_DATA_TYPE_IPV4 = 19;
  CONFIG_DATA_TYPE_IPV6 = 20;
  CONFIG_DATA_TYPE_CIDR = 21;
  CONFIG_DATA_TYPE_PORT = 22;
  CONFIG_DATA_TYPE_UUID = 23;
  CONFIG_DATA_TYPE_BASE64 = 24;
  CONFIG_DATA_TYPE_HEX = 25;
}

```

---

### config_diff.proto {#config_diff}

**Path**: `pkg/config/proto/config_diff.proto` **Package**: `gcommon.v1.config`
**Lines**: 68

**Messages** (2): `ConfigDiff`, `ConfigDiffEntry`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_diff.proto
// version: 1.0.0
// guid: tu0vwxyz-12a3-4b5c-6d7e-8f9g0h1i2j3k

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * Represents differences between two configuration states.
 * Provides detailed comparison information for configuration changes.
 */
message ConfigDiff {
  // Unique identifier for this diff
  string diff_id = 1;

  // Source configuration version/snapshot
  string source_version = 2;

  // Target configuration version/snapshot
  string target_version = 3;

  // List of added configuration keys
  repeated ConfigDiffEntry added = 4;

  // List of modified configuration keys
  repeated ConfigDiffEntry modified = 5;

  // List of removed configuration keys
  repeated ConfigDiffEntry removed = 6;

  // Timestamp when diff was computed
  google.protobuf.Timestamp computed_at = 7;

  // User or service that requested the diff
  string requested_by = 8;

  // Additional metadata
  map<string, string> metadata = 9;
}

/**
 * Represents a single configuration difference entry.
 */
message ConfigDiffEntry {
  // Configuration key
  string key = 1;

  // Old value (for modified/removed entries)
  google.protobuf.Any old_value = 2;

  // New value (for added/modified entries)
  google.protobuf.Any new_value = 3;

  // Type of change (ADDED, MODIFIED, REMOVED)
  string change_type = 4;

  // Configuration namespace or section
  string namespace = 5;
}

```

---

### config_entry.proto {#config_entry}

**Path**: `pkg/config/proto/config_entry.proto` **Package**: `gcommon.v1.config`
**Lines**: 45

**Messages** (1): `ConfigEntry`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/config_value.proto` → [common](./common.md#config_value)
- `pkg/common/proto/resource_status.proto` →
  [common](./common.md#resource_status)

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_entry.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/config_value.proto";
import "pkg/common/proto/resource_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ConfigEntry represents a single configuration value with metadata.
 */
message ConfigEntry {
  // Configuration key
  string key = 1;

  // Configuration value
  gcommon.v1.common.ConfigValue value = 2;

  // Namespace/environment
  string namespace = 3;

  // Entry metadata
  map<string, string> metadata = 4;

  // Tags for categorization
  repeated string tags = 5;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 6;

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 7;

  // Entry version for optimistic concurrency
  int64 version = 8;

  // Entry status
  gcommon.v1.common.ResourceStatus status = 9;
}

```

---

### config_environment.proto {#config_environment}

**Path**: `pkg/config/proto/config_environment.proto` **Package**:
`gcommon.v1.config` **Lines**: 440

**Messages** (15): `ConfigEnvironment`, `PromotionRule`, `DeploymentInfo`,
`HealthCheck`, `DeploymentRollbackInfo`, `HealthStatus`, `HealthCheckResult`,
`ResourceLimits`, `BackupPolicy`, `ApprovalWorkflow`, `ApprovalStage`,
`MonitoringConfig`, `RetentionPolicy`, `EncryptionSettings`, `SyncSettings`

**Imports** (11):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/access_control.proto` →
  [config_1](./config_1.md#access_control)
- `pkg/config/proto/audit_settings.proto`
- `pkg/config/proto/compliance_settings.proto`
- `pkg/config/proto/deployment_status.proto` →
  [config_1](./config_1.md#deployment_status)
- `pkg/config/proto/environment_status.proto` →
  [config_1](./config_1.md#environment_status)
- `pkg/config/proto/environment_type.proto` →
  [config_1](./config_1.md#environment_type)
- `pkg/config/proto/health_check_type.proto` →
  [config_1](./config_1.md#health_check_type)
- `pkg/config/proto/health_state.proto` → [config_1](./config_1.md#health_state)
- `pkg/config/proto/notification_settings.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_environment.proto
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/access_control.proto";
import "pkg/config/proto/audit_settings.proto";
import "pkg/config/proto/compliance_settings.proto";
import "pkg/config/proto/deployment_status.proto";
import "pkg/config/proto/environment_status.proto";
import "pkg/config/proto/environment_type.proto";
import "pkg/config/proto/health_check_type.proto";
import "pkg/config/proto/health_state.proto";
import "pkg/config/proto/notification_settings.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

// ConfigEnvironment represents a configuration environment
message ConfigEnvironment {
  // Unique identifier for the environment
  string environment_id = 1;

  // Environment name
  string name = 2;

  // Environment description
  string description = 3;

  // Environment type
  EnvironmentType type = 4;

  // Environment status
  EnvironmentStatus status = 5;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 6;

  // Last modification timestamp
  google.protobuf.Timestamp updated_at = 7;

  // Environment owner
  string owner = 8;

  // Environment tags
  repeated string tags = 9;

  // Environment metadata
  map<string, string> metadata = 10;

  // Environment configuration
  map<string, string> config = 11;

  // Environment secrets (encrypted)
  map<string, string> secrets = 12;

  // Environment variables
  map<string, string> variables = 13;

  // Parent environment (for inheritance)
  string parent_environment_id = 14;

  // Child environments
  repeated string child_environment_ids = 15;

  // Environment promotion rules
  repeated PromotionRule promotion_rules = 16;

  // Environment access control
  repeated AccessControl access_controls = 17;

  // Environment deployment info
  DeploymentInfo deployment_info = 18;

  // Environment health status
  HealthStatus health_status = 19;

  // Environment resource limits
  ResourceLimits resource_limits = 20;

  // Environment backup policy
  BackupPolicy backup_policy = 21;

  // Environment approval workflow
  ApprovalWorkflow approval_workflow = 22;

  // Environment monitoring config
  MonitoringConfig monitoring_config = 23;

  // Environment retention policy
  RetentionPolicy retention_policy = 24;

  // Environment compliance settings
  ComplianceSettings compliance_settings = 25;

  // Environment encryption settings
  EncryptionSettings encryption_settings = 26;

  // Environment audit settings
  AuditSettings audit_settings = 27;

  // Environment notification settings
  NotificationSettings notification_settings = 28;

  // Environment sync settings
  SyncSettings sync_settings = 29;

  // Environment version
  string version = 30;
}

// PromotionRule represents rules for promoting configurations between environments
message PromotionRule {
  // Rule name
  string name = 1;

  // Source environment
  string source_environment = 2;

  // Target environment
  string target_environment = 3;

  // Promotion conditions
  repeated string conditions = 4;

  // Approval required
  bool approval_required = 5;

  // Approvers
  repeated string approvers = 6;

  // Automatic promotion
  bool automatic = 7;

  // Promotion schedule
  string schedule = 8;

  // Promotion filters
  repeated string filters = 9;

  // Promotion transformations
  repeated string transformations = 10;
}

// DeploymentInfo represents deployment information for an environment
message DeploymentInfo {
  // Deployment status
  DeploymentStatus status = 1;

  // Last deployment timestamp
  google.protobuf.Timestamp last_deployed_at = 2;

  // Deployment version
  string version = 3;

  // Deployment method
  string method = 4;

  // Deployment target
  string target = 5;

  // Deployment configuration
  map<string, string> config = 6;

  // Deployment health checks
  repeated HealthCheck health_checks = 7;

  // Deployment rollback info
  DeploymentRollbackInfo rollback_info = 8;
}

// HealthCheck represents a health check for an environment
message HealthCheck {
  // Health check name
  string name = 1;

  // Health check type
  HealthCheckType type = 2;

  // Health check endpoint
  string endpoint = 3;

  // Health check interval
  int32 interval_seconds = 4;

  // Health check timeout
  int32 timeout_seconds = 5;

  // Health check retries
  int32 retries = 6;

  // Health check conditions
  repeated string conditions = 7;
}

// DeploymentRollbackInfo represents rollback information for deployments
message DeploymentRollbackInfo {
  // Rollback available
  bool available = 1;

  // Previous version
  string previous_version = 2;

  // Rollback timestamp
  google.protobuf.Timestamp rollback_timestamp = 3;

  // Rollback reason
  string reason = 4;

  // Rollback method
  string method = 5;
}

// HealthStatus represents the health status of an environment
message HealthStatus {
  // Overall health
  HealthState overall = 1;

  // Component health
  map<string, HealthState> components = 2;

  // Health checks
  repeated HealthCheckResult health_checks = 3;

  // Last health check
  google.protobuf.Timestamp last_check = 4;

  // Health metrics
  map<string, double> metrics = 5;
}

// HealthCheckResult represents the result of a health check
message HealthCheckResult {
  // Health check name
  string name = 1;

  // Health check status
  HealthState status = 2;

  // Health check message
  string message = 3;

  // Health check timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Health check duration
  int32 duration_ms = 5;

  // Health check details
  map<string, string> details = 6;
}

// ResourceLimits represents resource limits for an environment
message ResourceLimits {
  // CPU limit
  string cpu_limit = 1;

  // Memory limit
  string memory_limit = 2;

  // Storage limit
  string storage_limit = 3;

  // Network limit
  string network_limit = 4;

  // Request rate limit
  int32 request_rate_limit = 5;

  // Concurrent connections limit
  int32 connection_limit = 6;

  // Custom limits
  map<string, string> custom_limits = 7;
}

// BackupPolicy represents backup policy for an environment
message BackupPolicy {
  // Backup enabled
  bool enabled = 1;

  // Backup schedule
  string schedule = 2;

  // Backup retention
  int32 retention_days = 3;

  // Backup location
  string location = 4;

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup verification
  bool verified = 7;

  // Backup metadata
  map<string, string> metadata = 8;
}

// ApprovalWorkflow represents approval workflow for an environment
message ApprovalWorkflow {
  // Workflow enabled
  bool enabled = 1;

  // Workflow type
  string type = 2;

  // Approval stages
  repeated ApprovalStage stages = 3;

  // Workflow timeout
  int32 timeout_hours = 4;

  // Workflow conditions
  repeated string conditions = 5;

  // Workflow notifications
  repeated string notifications = 6;
}

// ApprovalStage represents a stage in the approval workflow
message ApprovalStage {
  // Stage name
  string name = 1;

  // Required approvers
  repeated string approvers = 2;

  // Required approvals
  int32 required_approvals = 3;

  // Stage conditions
  repeated string conditions = 4;

  // Stage timeout
  int32 timeout_hours = 5;

  // Stage order
  int32 order = 6;
}

// MonitoringConfig represents monitoring configuration for an environment
message MonitoringConfig {
  // Monitoring enabled
  bool enabled = 1;

  // Monitoring provider
  string provider = 2;

  // Monitoring endpoints
  repeated string endpoints = 3;

  // Monitoring metrics
  repeated string metrics = 4;

  // Monitoring alerts
  repeated string alerts = 5;

  // Monitoring dashboards
  repeated string dashboards = 6;

  // Monitoring configuration
  map<string, string> config = 7;
}

// RetentionPolicy represents retention policy for an environment
message RetentionPolicy {
  // Retention enabled
  bool enabled = 1;

  // Configuration retention
  int32 config_retention_days = 2;

  // Audit log retention
  int32 audit_retention_days = 3;

  // Backup retention
  int32 backup_retention_days = 4;

  // Metrics retention
  int32 metrics_retention_days = 5;

  // Custom retention policies
  map<string, int32> custom_retention = 6;
}

// EncryptionSettings represents encryption settings for an environment
message EncryptionSettings {
  // Encryption enabled
  bool enabled = 1;

  // Encryption provider
  string provider = 2;

  // Encryption key
  string key_id = 3;

  // Encryption algorithm
  string algorithm = 4;

  // Encryption mode
  string mode = 5;

  // Encryption configuration
  map<string, string> config = 6;
}

// SyncSettings represents sync settings for an environment
message SyncSettings {
  // Sync enabled
  bool enabled = 1;

  // Sync source
  string source = 2;

  // Sync target
  string target = 3;

  // Sync schedule
  string schedule = 4;

  // Sync filters
  repeated string filters = 5;

  // Sync transformations
  repeated string transformations = 6;

  // Sync configuration
  map<string, string> config = 7;
}

```

---

### config_schema.proto {#config_schema}

**Path**: `pkg/config/proto/config_schema.proto` **Package**:
`gcommon.v1.config` **Lines**: 31

**Messages** (1): `ConfigSchema`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_schema.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ConfigSchema defines a configuration schema.
 */
message ConfigSchema {
  // Schema name
  string name = 1;

  // Schema version
  string version = 2;

  // Schema definition (JSON Schema)
  string definition = 3;

  // Schema metadata
  map<string, string> metadata = 4;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 5;
}

```

---

### config_snapshot.proto {#config_snapshot}

**Path**: `pkg/config/proto/config_snapshot.proto` **Package**:
`gcommon.v1.config` **Lines**: 48

**Messages** (1): `ConfigSnapshot`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_snapshot.proto
// version: 1.0.0
// guid: st9uvwxy-01z2-3a4b-5c6d-7e8f9g0h1i2j

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * Represents a point-in-time snapshot of configuration.
 * Captures the entire configuration state at a specific moment.
 */
message ConfigSnapshot {
  // Unique identifier for this snapshot
  string snapshot_id = 1;

  // Timestamp when snapshot was created
  google.protobuf.Timestamp created_at = 2;

  // Configuration values at snapshot time
  map<string, google.protobuf.Any> config_values = 3;

  // Version of the configuration
  string version = 4;

  // Environment or context (e.g., "production", "staging")
  string environment = 5;

  // User or service that created the snapshot
  string created_by = 6;

  // Description or reason for the snapshot
  string description = 7;

  // Checksum or hash of the configuration
  string checksum = 8;

  // Additional metadata
  map<string, string> metadata = 9;
}

```

---

### config_stats.proto {#config_stats}

**Path**: `pkg/config/proto/config_stats.proto` **Package**: `gcommon.v1.config`
**Lines**: 27

**Messages** (1): `ConfigStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/config_stats.proto
// version: 1.0.0
// guid: f5a6b7c8-9d0e-1234-f012-567890123456

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ConfigStats {
  // Total number of configurations
  int64 total_configs = 1;

  // Number of active configurations
  int64 active_configs = 2;

  // Number of deprecated configurations
  int64 deprecated_configs = 3;

  // Average access frequency
  double avg_access_frequency = 4;
}

```

---

### config_validation_error.proto {#config_validation_error}

**Path**: `pkg/config/proto/config_validation_error.proto` **Package**:
`gcommon.v1.config` **Lines**: 24

**Messages** (1): `ConfigValidationError`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_validation_error.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ConfigValidationError represents a validation error for a configuration entry.
 */
message ConfigValidationError {
  // Configuration key with error
  string key = 1;

  // Error message
  string message = 2;

  // Error code
  string code = 3;
}

```

---

### config_validation_warning.proto {#config_validation_warning}

**Path**: `pkg/config/proto/config_validation_warning.proto` **Package**:
`gcommon.v1.config` **Lines**: 24

**Messages** (1): `ConfigValidationWarning`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_validation_warning.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ConfigValidationWarning represents a validation warning for a configuration entry.
 */
message ConfigValidationWarning {
  // Configuration key with warning
  string key = 1;

  // Warning message
  string message = 2;

  // Warning code
  string code = 3;
}

```

---

### config_watch.proto {#config_watch}

**Path**: `pkg/config/proto/config_watch.proto` **Package**: `gcommon.v1.config`
**Lines**: 74

**Messages** (2): `ConfigWatch`, `ConfigWatchEvent`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/messages/config_watch.proto
// version: 1.0.0
// guid: uv1wxyz0-23a4-5b6c-7d8e-9f0g1h2i3j4k

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * Represents a configuration watch event.
 * Notifies about configuration changes in real-time.
 */
message ConfigWatch {
  // Watch session identifier
  string watch_id = 1;

  // Configuration key pattern being watched
  string key_pattern = 2;

  // Configuration namespace or section
  string namespace = 3;

  // Type of watch (KEY_CHANGE, NAMESPACE_CHANGE, ALL_CHANGES)
  string watch_type = 4;

  // Timestamp when watch was created
  google.protobuf.Timestamp created_at = 5;

  // User or service that created the watch
  string created_by = 6;

  // Watch configuration options
  map<string, string> options = 7;

  // Whether the watch is currently active
  bool active = 8;
}

/**
 * Represents a configuration change event from a watch.
 */
message ConfigWatchEvent {
  // Watch session identifier
  string watch_id = 1;

  // Configuration key that changed
  string key = 2;

  // Previous value (if any)
  google.protobuf.Any old_value = 3;

  // New value
  google.protobuf.Any new_value = 4;

  // Type of change (CREATE, UPDATE, DELETE)
  string change_type = 5;

  // Timestamp of the change
  google.protobuf.Timestamp timestamp = 6;

  // Configuration namespace or section
  string namespace = 7;

  // Additional event metadata
  map<string, string> metadata = 8;
}

```

---

### decrypt_config_request.proto {#decrypt_config_request}

**Path**: `pkg/config/proto/decrypt_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 30

**Messages** (1): `DecryptConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/decrypt_config_request.proto
// file: config/proto/requests/decrypt_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * DecryptConfigRequest requests decryption of a configuration value.
 */
message DecryptConfigRequest {
  // Configuration key containing encrypted value
  string key = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### delete_config_request.proto {#delete_config_request}

**Path**: `pkg/config/proto/delete_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 27

**Messages** (1): `DeleteConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/delete_config_request.proto
// file: config/proto/requests/delete_config_request.proto
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * DeleteConfigRequest removes a configuration value.
 */
message DeleteConfigRequest {
  // Configuration key to delete
  string key = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### encrypt_config_request.proto {#encrypt_config_request}

**Path**: `pkg/config/proto/encrypt_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 30

**Messages** (1): `EncryptConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/encrypt_config_request.proto
// file: config/proto/requests/encrypt_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * EncryptConfigRequest encrypts a plain configuration value.
 */
message EncryptConfigRequest {
  // Configuration key for the value to encrypt
  string key = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### export_config_request.proto {#export_config_request}

**Path**: `pkg/config/proto/export_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 30

**Messages** (1): `ExportConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/export_config_request.proto
// file: config/proto/requests/export_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ExportConfigRequest exports configuration values to an external format.
 */
message ExportConfigRequest {
  // Namespace/environment to export
  string namespace = 1;

  // Target format (e.g., JSON, YAML)
  string format = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### get_config_history_request.proto {#get_config_history_request}

**Path**: `pkg/config/proto/get_config_history_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 34

**Messages** (1): `GetConfigHistoryRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/get_config_history_request.proto
// file: config/proto/requests/get_config_history_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetConfigHistoryRequest retrieves change history for a configuration key.
 */
message GetConfigHistoryRequest {
  // Configuration key to query
  string key = 1;

  // Namespace/environment of the key
  string namespace = 2;

  // Only return changes after this time
  google.protobuf.Timestamp since = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### get_config_history_response.proto {#get_config_history_response}

**Path**: `pkg/config/proto/get_config_history_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 22

**Messages** (1): `GetConfigHistoryResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/config/proto/config_change.proto` →
  [metrics_config](./metrics_config.md#config_change)

#### Source Code

```protobuf
// file: pkg/config/proto/responses/get_config_history_response.proto
// version: 1.0.0
// guid: a0368a84-a298-4ed2-bccf-799e1e11f6ba

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/config/proto/config_change.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetConfigHistoryResponse returns configuration change history.
 */
message GetConfigHistoryResponse {
  // List of configuration changes
  repeated ConfigChange changes = 1;
}

```

---

### get_config_request.proto {#get_config_request}

**Path**: `pkg/config/proto/get_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 28

**Messages** (1): `GetConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/get_config_request.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetConfigRequest retrieves a single configuration value.
 */
message GetConfigRequest {
  // Configuration key
  string key = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;

  // Whether to decrypt encrypted values
  bool decrypt = 4;
}

```

---

### get_config_response.proto {#get_config_response}

**Path**: `pkg/config/proto/get_config_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 26

**Messages** (1): `GetConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/config/proto/config_entry.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/responses/get_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/config/proto/config_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetConfigResponse contains a configuration entry or error information.
 */
message GetConfigResponse {
  // Configuration entry
  ConfigEntry entry = 1;

  // Whether the key was found
  bool found = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}

```

---

### get_config_stats_request.proto {#get_config_stats_request}

**Path**: `pkg/config/proto/get_config_stats_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 25

**Messages** (1): `GetConfigStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/get_config_stats_request.proto
// file: config/proto/requests/get_config_stats_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message GetConfigStatsRequest {
  // Namespace or environment to query
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_config_stats_response.proto {#get_config_stats_response}

**Path**: `pkg/config/proto/get_config_stats_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 22

**Messages** (1): `GetConfigStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/config/proto/config_stats.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/responses/get_config_stats_response.proto
// version: 1.0.0
// guid: c97a7226-491a-45fd-bf2d-4c045dbd0054

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/config/proto/config_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetConfigStatsResponse contains statistics about configuration.
 */
message GetConfigStatsResponse {
  // Statistics data
  ConfigStats stats = 1;
}

```

---

### get_multiple_config_request.proto {#get_multiple_config_request}

**Path**: `pkg/config/proto/get_multiple_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 26

**Messages** (1): `GetMultipleConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/get_multiple_config_request.proto

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message GetMultipleConfigRequest {
  // Configuration keys to retrieve
  repeated string keys = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Whether to decrypt encrypted values
  bool decrypt = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### get_multiple_config_response.proto {#get_multiple_config_response}

**Path**: `pkg/config/proto/get_multiple_config_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 26

**Messages** (1): `GetMultipleConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/config/proto/config_entry.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/responses/get_multiple_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/config/proto/config_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetMultipleConfigResponse returns multiple configuration entries.
 */
message GetMultipleConfigResponse {
  // Retrieved entries mapped by key
  map<string, ConfigEntry> entries = 1;

  // Keys that were not found
  repeated string not_found = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}

```

---

### import_config_request.proto {#import_config_request}

**Path**: `pkg/config/proto/import_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 31

**Messages** (1): `ImportConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/import_config_request.proto
// file: config/proto/requests/import_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ImportConfigRequest {
  // Namespace/environment for imported values
  string namespace = 1;

  // Serialized configuration content
  bytes content = 2;

  // Input format (e.g., JSON, YAML)
  string format = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### inheritance_settings.proto {#inheritance_settings}

**Path**: `pkg/config/proto/inheritance_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 45

**Messages** (1): `InheritanceSettings`

**Imports** (7):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/inheritance_filter.proto` →
  [config_1](./config_1.md#inheritance_filter)
- `pkg/config/proto/inheritance_strategy.proto` →
  [config_1](./config_1.md#inheritance_strategy)
- `pkg/config/proto/inheritance_transformation.proto` →
  [config_1](./config_1.md#inheritance_transformation)
- `pkg/config/proto/merge_strategy.proto` →
  [config_1](./config_1.md#merge_strategy)

#### Source Code

```protobuf
// file: pkg/config/proto/inheritance_settings.proto
// version: 1.0.0
// guid: f7c6c365-e83d-4ae8-8166-fb86d2e3b6f0

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/inheritance_filter.proto";
import "pkg/config/proto/inheritance_strategy.proto";
import "pkg/config/proto/inheritance_transformation.proto";
import "pkg/config/proto/merge_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message InheritanceSettings {
  // Whether inheritance is enabled
  bool enabled = 1;

  // Inheritance strategy
  InheritanceStrategy strategy = 2;

  // Inheritance sources in order of priority
  repeated string sources = 3;

  // Inheritance filters
  repeated InheritanceFilter filters = 4;

  // Inheritance transformations
  repeated InheritanceTransformation transformations = 5;

  // Whether to merge inherited values
  bool merge_values = 6;

  // Merge strategy for complex values
  MergeStrategy merge_strategy = 7;

  // Inheritance metadata
  map<string, string> metadata = 8;
}

```

---

### list_config_request.proto {#list_config_request}

**Path**: `pkg/config/proto/list_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 38

**Messages** (1): `ListConfigRequest`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/filter_options.proto` → [common](./common.md#filter_options)
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/sort.proto` → [common](./common.md#sort)

#### Source Code

```protobuf
// file: pkg/config/proto/list_config_request.proto
//
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/filter_options.proto";
import "pkg/common/proto/pagination.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/sort.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ListConfigRequest lists configuration entries with optional filtering.
 */
message ListConfigRequest {
  // Key prefix filter
  string prefix = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Pagination options
  gcommon.v1.common.Pagination pagination = 3;

  // Filter options
  gcommon.v1.common.FilterOptions filter = 4;

  // Sort options
  gcommon.v1.common.SortOptions sort = 5;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 6;
}

```

---

### list_config_response.proto {#list_config_response}

**Path**: `pkg/config/proto/list_config_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 27

**Messages** (1): `ListConfigResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/config/proto/config_entry.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/responses/list_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/config/proto/config_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ListConfigResponse returns configuration entries for a list operation.
 */
message ListConfigResponse {
  // Configuration entries
  repeated ConfigEntry entries = 1;

  // Pagination information
  gcommon.v1.common.PaginatedResponse pagination = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}

```

---

### monitoring_settings.proto {#monitoring_settings}

**Path**: `pkg/config/proto/monitoring_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 32

**Messages** (1): `MonitoringSettings`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/monitoring_alert.proto` →
  [config_1](./config_1.md#monitoring_alert)

#### Source Code

```protobuf
// file: pkg/config/proto/monitoring_settings.proto
// version: 1.0.0
// guid: 1df1c6fa-7f81-4982-9c0e-040b1f0ad10f

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/monitoring_alert.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message MonitoringSettings {
  // Whether monitoring is enabled
  bool enabled = 1;

  // Monitoring alerts
  repeated MonitoringAlert alerts = 2;

  // Monitoring metrics
  repeated string metrics = 3;

  // Monitoring dashboard
  string dashboard = 4;

  // Monitoring retention period in days
  int32 retention_days = 5;
}

```

---

### notification_settings.proto {#notification_settings}

**Path**: `pkg/config/proto/notification_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 46

**Messages** (1): `NotificationSettings`

**Imports** (11):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` →
  [config_events](./config_events.md#audit_level)
- `pkg/config/proto/backup_frequency.proto` →
  [config_1](./config_1.md#backup_frequency)
- `pkg/config/proto/batching_settings.proto`
- `pkg/config/proto/channel_type.proto` → [config_1](./config_1.md#channel_type)
- `pkg/config/proto/config_data_type.proto`
- `pkg/config/proto/deprecation_level.proto` →
  [config_1](./config_1.md#deprecation_level)
- `pkg/config/proto/metadata_status.proto` →
  [config_1](./config_1.md#metadata_status)
- `pkg/config/proto/notification_channel.proto` →
  [config_1](./config_1.md#notification_channel) →
  [queue_1](./queue_1.md#notification_channel)
- `pkg/config/proto/notification_trigger.proto` →
  [config_1](./config_1.md#notification_trigger)

#### Source Code

```protobuf
// file: pkg/config/proto/notification_settings.proto
// version: 1.0.0
// guid: 4694674c-55fc-4ee7-8874-efe3ad5f1250

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/audit_level.proto";
import "pkg/config/proto/backup_frequency.proto";
import "pkg/config/proto/batching_settings.proto";
import "pkg/config/proto/channel_type.proto";
import "pkg/config/proto/config_data_type.proto";
import "pkg/config/proto/deprecation_level.proto";
import "pkg/config/proto/metadata_status.proto";
import "pkg/config/proto/notification_channel.proto";
import "pkg/config/proto/notification_trigger.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message NotificationSettings {
  // Whether notifications are enabled
  bool enabled = 1;

  // Notification channels
  repeated NotificationChannel channels = 2;

  // Notification triggers
  repeated NotificationTrigger triggers = 3;

  // Notification template
  string template = 4;

  // Notification recipients
  repeated string recipients = 5;

  // Notification delay in minutes
  int32 delay_minutes = 6;

  // Notification batching settings
  BatchingSettings batching = 7;
}

```

---

### reload_config_request.proto {#reload_config_request}

**Path**: `pkg/config/proto/reload_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 25

**Messages** (1): `ReloadConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/reload_config_request.proto
// file: config/proto/requests/reload_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ReloadConfigRequest {
  // Namespace to reload
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### restore_config_request.proto {#restore_config_request}

**Path**: `pkg/config/proto/restore_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 28

**Messages** (1): `RestoreConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/restore_config_request.proto
// file: config/proto/requests/restore_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RestoreConfigRequest {
  // Restore point identifier
  string restore_point_id = 1;

  // Namespace/environment to restore
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### retry_settings.proto {#retry_settings}

**Path**: `pkg/config/proto/retry_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 33

**Messages** (1): `RetrySettings`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/backoff_strategy.proto` →
  [config_1](./config_1.md#backoff_strategy)

#### Source Code

```protobuf
// file: pkg/config/proto/retry_settings.proto
// version: 1.0.0
// guid: 97d15dc6-ddeb-4e88-a455-16bb8fb5c292

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/backoff_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RetrySettings {
  // Whether retry is enabled
  bool enabled = 1;

  // Maximum retry count
  int32 max_retries = 2;

  // Retry delay in seconds
  int32 delay_seconds = 3;

  // Retry backoff strategy
  BackoffStrategy backoff_strategy = 4;

  // Retry conditions
  repeated string conditions = 5;
}

```

---

### rollback_config_request.proto {#rollback_config_request}

**Path**: `pkg/config/proto/rollback_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 28

**Messages** (1): `RollbackConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/rollback_config_request.proto
// file: config/proto/requests/rollback_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RollbackConfigRequest {
  // Version identifier to roll back to
  string version = 1;

  // Namespace/environment of the configuration
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### rotation_settings.proto {#rotation_settings}

**Path**: `pkg/config/proto/rotation_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 48

**Messages** (1): `RotationSettings`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/rotation_event.proto` →
  [config_events](./config_events.md#rotation_event)
- `pkg/config/proto/rotation_frequency.proto` →
  [config_1](./config_1.md#rotation_frequency)

#### Source Code

```protobuf
// file: pkg/config/proto/rotation_settings.proto
// version: 1.0.0
// guid: f9ec4d9b-b31b-410a-a6d5-f53e24671b44

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/rotation_event.proto";
import "pkg/config/proto/rotation_frequency.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RotationSettings {
  // Whether rotation is enabled
  bool enabled = 1;

  // Rotation frequency
  RotationFrequency frequency = 2;

  // Rotation schedule (cron expression)
  string schedule = 3;

  // Grace period before old secret expires
  int32 grace_period_days = 4;

  // Whether to automatically rotate
  bool auto_rotate = 5;

  // Rotation notification settings
  repeated string notification_recipients = 6;

  // Rotation workflow
  string workflow = 7;

  // Last rotation timestamp
  google.protobuf.Timestamp last_rotated_at = 8;

  // Next rotation timestamp
  google.protobuf.Timestamp next_rotation_at = 9;

  // Rotation history
  repeated RotationEvent rotation_history = 10;
}

```

---

### secret_audit_settings.proto {#secret_audit_settings}

**Path**: `pkg/config/proto/secret_audit_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 44

**Messages** (1): `SecretAuditSettings`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/secret_audit_level.proto` →
  [config_events](./config_events.md#secret_audit_level)

#### Source Code

```protobuf
// file: pkg/config/proto/secret_audit_settings.proto
// version: 1.0.0
// guid: 1da3c9ca-367b-4399-ba06-b6eb865ad744

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/secret_audit_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message SecretAuditSettings {
  // Whether audit logging is enabled
  bool enabled = 1;

  // Audit log level
  SecretAuditLevel level = 2;

  // Audit log retention period in days
  int32 retention_days = 3;

  // Whether to log access events
  bool log_access = 4;

  // Whether to log rotation events
  bool log_rotation = 5;

  // Whether to log modification events
  bool log_modification = 6;

  // External audit destinations
  repeated string destinations = 7;

  // Audit log format
  string format = 8;

  // Additional audit metadata
  map<string, string> metadata = 9;
}

```

---

### secret_backup_settings.proto {#secret_backup_settings}

**Path**: `pkg/config/proto/secret_backup_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 41

**Messages** (1): `SecretBackupSettings`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/secret_backup_frequency.proto` →
  [config_1](./config_1.md#secret_backup_frequency)

#### Source Code

```protobuf
// file: pkg/config/proto/secret_backup_settings.proto
// version: 1.0.0
// guid: d6d87fc0-471b-4087-857b-33284c8b1765

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/secret_backup_frequency.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message SecretBackupSettings {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup frequency
  SecretBackupFrequency frequency = 2;

  // Backup retention period in days
  int32 retention_days = 3;

  // Backup storage location
  string storage_location = 4;

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup metadata
  map<string, string> metadata = 7;

  // Last backup timestamp
  google.protobuf.Timestamp last_backup_at = 8;
}

```

---

### set_config_request.proto {#set_config_request}

**Path**: `pkg/config/proto/set_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 39

**Messages** (1): `SetConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/config_value.proto` → [common](./common.md#config_value)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/set_config_request.proto
//
// Request definitions for config module
// Generated as part of 1-1-1 migration
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/config_value.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

// Set configuration request
message SetConfigRequest {
  // Configuration key
  string key = 1;

  // Configuration value
  gcommon.v1.common.ConfigValue value = 2;

  // Optional namespace/environment
  string namespace = 3;

  // Configuration metadata
  map<string, string> metadata = 4;

  // Whether to encrypt the value
  bool encrypt = 5;

  // Tags for categorization
  repeated string tags = 6;

  // Request metadata
  gcommon.v1.common.RequestMetadata request_metadata = 7;
}

```

---

### set_config_response.proto {#set_config_response}

**Path**: `pkg/config/proto/set_config_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 26

**Messages** (1): `SetConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/config/proto/config_entry.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/responses/set_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/config/proto/config_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * SetConfigResponse indicates the result of a configuration set operation.
 */
message SetConfigResponse {
  // Whether the operation succeeded
  bool success = 1;

  // Previous value if it existed
  ConfigEntry previous_entry = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}

```

---

### set_config_schema_request.proto {#set_config_schema_request}

**Path**: `pkg/config/proto/set_config_schema_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 29

**Messages** (1): `SetConfigSchemaRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/config/proto/config_schema.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/requests/set_config_schema_request.proto
// file: config/proto/requests/set_config_schema_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/config/proto/config_schema.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message SetConfigSchemaRequest {
  // Namespace the schema applies to
  string namespace = 1;

  // Schema definition
  ConfigSchema schema = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### set_multiple_config_request.proto {#set_multiple_config_request}

**Path**: `pkg/config/proto/set_multiple_config_request.proto` **Package**:
`gcommon.v1.config` **Lines**: 32

**Messages** (1): `SetMultipleConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/config_value.proto` → [common](./common.md#config_value)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/set_multiple_config_request.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/config_value.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * SetMultipleConfigRequest stores multiple configuration values.
 */
message SetMultipleConfigRequest {
  // Configuration entries to set
  map<string, gcommon.v1.common.ConfigValue> entries = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Common metadata for all entries
  map<string, string> metadata = 3;

  // Whether to encrypt values
  bool encrypt = 4;

  // Request metadata
  gcommon.v1.common.RequestMetadata request_metadata = 5;
}

```

---

### set_multiple_config_response.proto {#set_multiple_config_response}

**Path**: `pkg/config/proto/set_multiple_config_response.proto` **Package**:
`gcommon.v1.config` **Lines**: 22

**Messages** (1): `SetMultipleConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/config/proto/responses/set_multiple_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * SetMultipleConfigResponse reports the result of a bulk set operation.
 */
message SetMultipleConfigResponse {
  // Success status for each key
  map<string, bool> results = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### synchronization_settings.proto {#synchronization_settings}

**Path**: `pkg/config/proto/synchronization_settings.proto` **Package**:
`gcommon.v1.config` **Lines**: 35

**Messages** (1): `SynchronizationSettings`

**Imports** (6):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/conflict_resolution.proto` →
  [config_1](./config_1.md#conflict_resolution)
- `pkg/config/proto/synchronization_frequency.proto` →
  [config_2](./config_2.md#synchronization_frequency)
- `pkg/config/proto/synchronization_target.proto` →
  [config_2](./config_2.md#synchronization_target)

#### Source Code

```protobuf
// file: pkg/config/proto/synchronization_settings.proto
// version: 1.0.0
// guid: e3f41f73-ecdc-4499-9a1a-8adc64cb1ed1

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/conflict_resolution.proto";
import "pkg/config/proto/synchronization_frequency.proto";
import "pkg/config/proto/synchronization_target.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message SynchronizationSettings {
  // Whether synchronization is enabled
  bool enabled = 1;

  // Synchronization targets
  repeated SynchronizationTarget targets = 2;

  // Synchronization frequency
  SynchronizationFrequency frequency = 3;

  // Synchronization conflict resolution
  ConflictResolution conflict_resolution = 4;

  // Synchronization metadata
  map<string, string> metadata = 5;
}

```

---
