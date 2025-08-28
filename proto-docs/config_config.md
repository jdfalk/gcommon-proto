# config_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 42
- **Messages**: 42
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [backup_config_request.proto](#backup_config_request)
- [config_backup.proto](#config_backup)
- [config_change.proto](#config_change)
- [config_diff.proto](#config_diff)
- [config_diff_entry.proto](#config_diff_entry)
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
- [list_config_request.proto](#list_config_request)
- [list_config_response.proto](#list_config_response)
- [monitoring_config.proto](#monitoring_config)
- [reload_config_request.proto](#reload_config_request)
- [restore_config_request.proto](#restore_config_request)
- [rollback_config_request.proto](#rollback_config_request)
- [set_config_request.proto](#set_config_request)
- [set_config_response.proto](#set_config_response)
- [set_config_schema_request.proto](#set_config_schema_request)
- [set_multiple_config_request.proto](#set_multiple_config_request)
- [set_multiple_config_response.proto](#set_multiple_config_response)
- [unwatch_config_request.proto](#unwatch_config_request)
- [validate_config_request.proto](#validate_config_request)
- [validate_config_response.proto](#validate_config_response)
- [watch_config_request.proto](#watch_config_request)
- [watch_config_response.proto](#watch_config_response)
---


## Detailed Documentation

### backup_config_request.proto {#backup_config_request}

**Path**: `gcommon/v1/config/backup_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 35

**Messages** (1): `BackupConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/backup_config_request.proto
// version: 1.0.0
// guid: f67411e8-9bc7-4f38-9f6b-271a45af468e
// file: proto/gcommon/v1/config/backup_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * BackupConfigRequest triggers creation of a configuration backup.
 */
message BackupConfigRequest {
  // Namespace or environment to back up
  string namespace = 1;

  // Optional description for the backup
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Include secrets in the backup
  bool include_secrets = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### config_backup.proto {#config_backup}

**Path**: `gcommon/v1/config/config_backup.proto` **Package**: `gcommon.v1.config` **Lines**: 63

**Messages** (1): `ConfigBackup`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_backup.proto
// version: 1.0.0
// guid: vw2xyz01-34a5-6b7c-8d9e-0f1g2h3i4j5k

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * Represents a configuration backup.
 * Stores complete configuration state for recovery purposes.
 */
message ConfigBackup {
  // Unique identifier for this backup
  string backup_id = 1;

  // Timestamp when backup was created
  google.protobuf.Timestamp created_at = 2 [ (buf.validate.field).required = true ];

  // Configuration values at backup time
  map<string, google.protobuf.Any> config_values = 3;

  // Version of the configuration
  string version = 4;

  // Environment or context (e.g., "production", "staging")
  string environment = 5;

  // User or service that created the backup
  string created_by = 6 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Description or reason for the backup
  string description = 7 [ (buf.validate.field).string.max_len = 1000 ];

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

**Path**: `gcommon/v1/config/config_change.proto` **Package**: `gcommon.v1.config` **Lines**: 52

**Messages** (1): `ConfigConfigChange`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_change.proto
// version: 1.0.0
// guid: rs8tuvwx-90y1-2z3a-4b5c-6d7e8f9g0h1i

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * Represents a configuration change event.
 * Tracks what changed, when, and who made the change.
 */
message ConfigConfigChange {
  // Unique identifier for this change
  string change_id = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration key that changed
  string key = 2 [(buf.validate.field).string.min_len = 1];

  // Previous value (if any)
  google.protobuf.Any old_value = 3;

  // New value
  google.protobuf.Any new_value = 4;

  // Type of change (CREATE, UPDATE, DELETE)
  string change_type = 5 [(buf.validate.field).string.min_len = 1];

  // Timestamp of the change
  google.protobuf.Timestamp timestamp = 6;

  // User or service that made the change
  string changed_by = 7 [(buf.validate.field).string.min_len = 1];

  // Reason for the change
  string reason = 8 [(buf.validate.field).string.min_len = 1];

  // Configuration namespace or section
  string namespace = 9 [(buf.validate.field).string.min_len = 1];

  // Additional metadata about the change
  map<string, string> metadata = 10;
}
```

---

### config_diff.proto {#config_diff}

**Path**: `gcommon/v1/config/config_diff.proto` **Package**: `gcommon.v1.config` **Lines**: 45

**Messages** (1): `ConfigDiff`

**Imports** (4):

- `gcommon/v1/config/config_diff_entry.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_diff.proto
// version: 1.0.0
// guid: 1d9db67e-5b10-4366-8b2b-b962194a0951

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/config_diff_entry.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigDiff {
  // Unique identifier for this diff
  string diff_id = 1 [(buf.validate.field).string.min_len = 1];

  // Source configuration version/snapshot
  string source_version = 2 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Target configuration version/snapshot
  string target_version = 3 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // List of added configuration keys
  repeated ConfigDiffEntry added = 4 [(buf.validate.field).repeated.min_items = 1];

  // List of modified configuration keys
  repeated ConfigDiffEntry modified = 5 [(buf.validate.field).repeated.min_items = 1];

  // List of removed configuration keys
  repeated ConfigDiffEntry removed = 6 [(buf.validate.field).repeated.min_items = 1];

  // Timestamp when diff was computed
  google.protobuf.Timestamp computed_at = 7;

  // User or service that requested the diff
  string requested_by = 8 [(buf.validate.field).string.min_len = 1];

  // Additional metadata
  map<string, string> metadata = 9;
}
```

---

### config_diff_entry.proto {#config_diff_entry}

**Path**: `gcommon/v1/config/config_diff_entry.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `ConfigDiffEntry`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_diff_entry.proto
// version: 1.0.0
// guid: 4ea54599-5e08-4917-9e80-97649dceb863

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigDiffEntry {
  // Configuration key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Old value (for modified/removed entries)
  google.protobuf.Any old_value = 2;

  // New value (for added/modified entries)
  google.protobuf.Any new_value = 3;

  // Type of change (ADDED, MODIFIED, REMOVED)
  string change_type = 4 [(buf.validate.field).string.min_len = 1];

  // Configuration namespace or section
  string namespace = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### config_entry.proto {#config_entry}

**Path**: `gcommon/v1/config/config_entry.proto` **Package**: `gcommon.v1.config` **Lines**: 47

**Messages** (1): `ConfigEntry`

**Imports** (5):

- `gcommon/v1/common/config_value.proto`
- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_entry.proto
// version: 1.0.0
// guid: 9cbaf2b4-aa14-40f2-91cb-a5a0a7f0a87d
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_value.proto";
import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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
  google.protobuf.Timestamp created_at = 6 [ (buf.validate.field).required = true ];

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

**Path**: `gcommon/v1/config/config_environment.proto` **Package**: `gcommon.v1.config` **Lines**: 130

**Messages** (1): `ConfigEnvironment`

**Imports** (19):

- `gcommon/v1/common/environment_status.proto`
- `gcommon/v1/common/environment_type.proto`
- `gcommon/v1/common/health_status.proto`
- `gcommon/v1/common/organization_access_control.proto`
- `gcommon/v1/common/organization_compliance_settings.proto`
- `gcommon/v1/common/organization_notification_settings.proto`
- `gcommon/v1/common/organization_resource_limits.proto`
- `gcommon/v1/common/retention_policy.proto`
- `gcommon/v1/config/approval_workflow.proto`
- `gcommon/v1/config/audit_settings.proto`
- `gcommon/v1/config/backup_policy.proto`
- `gcommon/v1/config/deployment_info.proto`
- `gcommon/v1/config/encryption_settings.proto`
- `gcommon/v1/config/monitoring_config.proto`
- `gcommon/v1/config/promotion_rule.proto`
- `gcommon/v1/config/sync_settings.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_environment.proto
// version: 1.0.1
// guid: 167ed450-2130-48be-8d18-2ad5bd34cf7e

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/environment_status.proto";
import "gcommon/v1/common/environment_type.proto";
import "gcommon/v1/common/health_status.proto";
import "gcommon/v1/common/organization_access_control.proto";
import "gcommon/v1/common/organization_compliance_settings.proto";
import "gcommon/v1/common/organization_notification_settings.proto";
import "gcommon/v1/common/organization_resource_limits.proto";
import "gcommon/v1/common/retention_policy.proto";
import "gcommon/v1/config/approval_workflow.proto";
import "gcommon/v1/config/audit_settings.proto";
import "gcommon/v1/config/backup_policy.proto";
import "gcommon/v1/config/deployment_info.proto";
import "gcommon/v1/config/encryption_settings.proto";
import "gcommon/v1/config/monitoring_config.proto";
import "gcommon/v1/config/promotion_rule.proto";
import "gcommon/v1/config/sync_settings.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Config-local types

// Metrics enums referenced by this message

// Organization-scoped settings used by environments

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigEnvironment {
  // Unique identifier for the environment
  string environment_id = 1;

  // Environment name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Environment description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Environment type
  gcommon.v1.common.EnvironmentType type = 4;

  // Environment status
  gcommon.v1.common.EnvironmentStatus status = 5;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 6 [ (buf.validate.field).required = true ];

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
  repeated gcommon.v1.common.OrganizationAccessControl access_controls = 17;

  // Environment deployment info
  DeploymentInfo deployment_info = 18;

  // Environment health status
  gcommon.v1.common.CommonHealthStatus health_status = 19;

  // Environment resource limits
  gcommon.v1.common.OrganizationResourceLimits resource_limits = 20;

  // Environment backup policy
  BackupPolicy backup_policy = 21;

  // Environment approval workflow
  ApprovalWorkflow approval_workflow = 22;

  // Environment monitoring config
  ConfigMonitoringConfig monitoring_config = 23;

  // Environment retention policy
  gcommon.v1.common.MetricsRetentionPolicy retention_policy = 24;

  // Environment compliance settings
  gcommon.v1.common.OrganizationComplianceSettings compliance_settings = 25;

  // Environment encryption settings
  EncryptionSettings encryption_settings = 26;

  // Environment audit settings
  AuditSettings audit_settings = 27;

  // Environment notification settings
  gcommon.v1.common.OrganizationNotificationSettings notification_settings = 28;

  // Environment sync settings
  SyncSettings sync_settings = 29;

  // Environment version
  string version = 30;
}
```

---

### config_schema.proto {#config_schema}

**Path**: `gcommon/v1/config/config_schema.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `ConfigSchema`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_schema.proto
// version: 1.0.0
// guid: 9e149f8a-076f-4c2b-8e8c-ddaf1b41707a
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ConfigSchema defines a configuration schema.
 */
message ConfigSchema {
  // Schema name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Schema version
  string version = 2;

  // Schema definition (JSON Schema)
  string definition = 3;

  // Schema metadata
  map<string, string> metadata = 4;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];
}
```

---

### config_snapshot.proto {#config_snapshot}

**Path**: `gcommon/v1/config/config_snapshot.proto` **Package**: `gcommon.v1.config` **Lines**: 48

**Messages** (1): `ConfigSnapshot`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_snapshot.proto
// version: 1.0.0
// guid: st9uvwxy-01z2-3a4b-5c6d-7e8f9g0h1i2j

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * Represents a point-in-time snapshot of configuration.
 * Captures the entire configuration state at a specific moment.
 */
message ConfigSnapshot {
  // Unique identifier for this snapshot
  string snapshot_id = 1;

  // Timestamp when snapshot was created
  google.protobuf.Timestamp created_at = 2 [ (buf.validate.field).required = true ];

  // Configuration values at snapshot time
  map<string, google.protobuf.Any> config_values = 3;

  // Version of the configuration
  string version = 4;

  // Environment or context (e.g., "production", "staging")
  string environment = 5;

  // User or service that created the snapshot
  string created_by = 6 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Description or reason for the snapshot
  string description = 7 [ (buf.validate.field).string.max_len = 1000 ];

  // Checksum or hash of the configuration
  string checksum = 8;

  // Additional metadata
  map<string, string> metadata = 9;
}
```

---

### config_stats.proto {#config_stats}

**Path**: `gcommon/v1/config/config_stats.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Messages** (1): `ConfigStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_stats.proto
// version: 1.0.0
// guid: f5a6b7c8-9d0e-1234-f012-567890123456

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigStats {
  // Total number of configurations
  int64 total_configs = 1 [(buf.validate.field).int64.gte = 0];

  // Number of active configurations
  int64 active_configs = 2 [(buf.validate.field).int64.gte = 0];

  // Number of deprecated configurations
  int64 deprecated_configs = 3 [(buf.validate.field).int64.gte = 0];

  // Average access frequency
  double avg_access_frequency = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### config_validation_error.proto {#config_validation_error}

**Path**: `gcommon/v1/config/config_validation_error.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `ConfigValidationError`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_validation_error.proto
// version: 1.0.0
// guid: 61a67e2a-6560-4367-b262-2f0e262764bd
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ConfigValidationError represents a validation error for a configuration entry.
 */
message ConfigValidationError {
  // Configuration key with error
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Error message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Error code
  string code = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### config_validation_warning.proto {#config_validation_warning}

**Path**: `gcommon/v1/config/config_validation_warning.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `ConfigValidationWarning`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_validation_warning.proto
// version: 1.0.0
// guid: 6d77d329-052f-4301-9627-79d2680d5cb4
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ConfigValidationWarning represents a validation warning for a configuration entry.
 */
message ConfigValidationWarning {
  // Configuration key with warning
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Warning message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Warning code
  string code = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### config_watch.proto {#config_watch}

**Path**: `gcommon/v1/config/config_watch.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `ConfigWatch`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_watch.proto
// version: 1.0.0
// guid: f0257edb-14c0-4d70-9a2a-82b1784ca863

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // User or service that created the watch
  string created_by = 6 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];

  // Watch configuration options
  map<string, string> options = 7;

  // Whether the watch is currently active
  bool active = 8;
}
```

---

### decrypt_config_request.proto {#decrypt_config_request}

**Path**: `gcommon/v1/config/decrypt_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `DecryptConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/decrypt_config_request.proto
// version: 1.0.0
// guid: 9601c041-6660-4091-b17d-ca336ebe9e1d
// file: proto/gcommon/v1/config/decrypt_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * DecryptConfigRequest requests decryption of a configuration value.
 */
message DecryptConfigRequest {
  // Configuration key containing encrypted value
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### delete_config_request.proto {#delete_config_request}

**Path**: `gcommon/v1/config/delete_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `DeleteConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/delete_config_request.proto
// version: 1.0.0
// guid: 6d17b97b-a8c2-4e72-83fb-0ca1ecb75daf
// file: proto/gcommon/v1/config/delete_config_request.proto
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * DeleteConfigRequest removes a configuration value.
 */
message DeleteConfigRequest {
  // Configuration key to delete
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### encrypt_config_request.proto {#encrypt_config_request}

**Path**: `gcommon/v1/config/encrypt_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `EncryptConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/encrypt_config_request.proto
// version: 1.0.0
// guid: dabeec2c-e6f7-49fa-9750-adfc41fca9ca
// file: proto/gcommon/v1/config/encrypt_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * EncryptConfigRequest encrypts a plain configuration value.
 */
message EncryptConfigRequest {
  // Configuration key for the value to encrypt
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### export_config_request.proto {#export_config_request}

**Path**: `gcommon/v1/config/export_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `ExportConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/export_config_request.proto
// version: 1.0.0
// guid: 59b9200c-f564-4f8b-99ae-ce3bdbe5810f
// file: proto/gcommon/v1/config/export_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ExportConfigRequest exports configuration values to an external format.
 */
message ExportConfigRequest {
  // Namespace/environment to export
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Target format (e.g., JSON, YAML)
  string format = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### get_config_history_request.proto {#get_config_history_request}

**Path**: `gcommon/v1/config/get_config_history_request.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `GetConfigHistoryRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/get_config_history_request.proto
// version: 1.0.0
// guid: 3e7b6154-2e0b-4f37-b278-51bc35fd7fe1
// file: proto/gcommon/v1/config/get_config_history_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * GetConfigHistoryRequest retrieves change history for a configuration key.
 */
message GetConfigHistoryRequest {
  // Configuration key to query
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Namespace/environment of the key
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Only return changes after this time
  google.protobuf.Timestamp since = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### get_config_history_response.proto {#get_config_history_response}

**Path**: `gcommon/v1/config/get_config_history_response.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Messages** (1): `GetConfigHistoryResponse`

**Imports** (3):

- `gcommon/v1/common/metrics_config_change.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_config_history_response.proto
// version: 1.0.0
// guid: a0368a84-a298-4ed2-bccf-799e1e11f6ba

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/metrics_config_change.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * GetConfigHistoryResponse returns configuration change history.
 */
message GetConfigHistoryResponse {
  // List of configuration changes
  repeated gcommon.v1.common.MetricsConfigChange changes = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### get_config_request.proto {#get_config_request}

**Path**: `gcommon/v1/config/get_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 31

**Messages** (1): `GetConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_config_request.proto
// version: 1.0.0
// guid: 86fbcecd-9557-4fc3-ab87-80bcc888d2bc
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * GetConfigRequest retrieves a single configuration value.
 */
message GetConfigRequest {
  // Configuration key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;

  // Whether to decrypt encrypted values
  bool decrypt = 4;
}
```

---

### get_config_response.proto {#get_config_response}

**Path**: `gcommon/v1/config/get_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `GetConfigResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/config/config_entry.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_config_response.proto
// version: 1.0.1
// guid: 0fdacefb-f7a3-40cd-9ed7-2faf4e61c032
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/config/config_entry.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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

**Path**: `gcommon/v1/config/get_config_stats_request.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Messages** (1): `GetConfigStatsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/get_config_stats_request.proto
// version: 1.0.0
// guid: 844f249a-a794-44ba-a9b1-5a6bf3d82ca5
// file: proto/gcommon/v1/config/get_config_stats_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message GetConfigStatsRequest {
  // Namespace or environment to query
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_config_stats_response.proto {#get_config_stats_response}

**Path**: `gcommon/v1/config/get_config_stats_response.proto` **Package**: `gcommon.v1.config` **Lines**: 21

**Messages** (1): `GetConfigStatsResponse`

**Imports** (2):

- `gcommon/v1/config/config_stats.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_config_stats_response.proto
// version: 1.0.1
// guid: c97a7226-491a-45fd-bf2d-4c045dbd0054

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/config_stats.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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

**Path**: `gcommon/v1/config/get_multiple_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `GetMultipleConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_multiple_config_request.proto
// version: 1.0.0
// guid: 40dcbc9d-69ee-4f5e-896b-c9d8bca277b7

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message GetMultipleConfigRequest {
  // Configuration keys to retrieve
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Whether to decrypt encrypted values
  bool decrypt = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### get_multiple_config_response.proto {#get_multiple_config_response}

**Path**: `gcommon/v1/config/get_multiple_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `GetMultipleConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/config/config_entry.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_multiple_config_response.proto
// version: 1.0.0
// guid: 91678eea-cc13-4a84-b125-e494149256fd
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/config/config_entry.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * GetMultipleConfigResponse returns multiple configuration entries.
 */
message GetMultipleConfigResponse {
  // Retrieved entries mapped by key
  map<string, ConfigEntry> entries = 1;

  // Keys that were not found
  repeated string not_found = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error information
  gcommon.v1.common.Error error = 3;
}
```

---

### import_config_request.proto {#import_config_request}

**Path**: `gcommon/v1/config/import_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `ImportConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/import_config_request.proto
// version: 1.0.0
// guid: 11934c0f-bfea-49e2-9b8a-5a9774e120cf
// file: proto/gcommon/v1/config/import_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ImportConfigRequest {
  // Namespace/environment for imported values
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Serialized configuration content
  bytes content = 2;

  // Input format (e.g., JSON, YAML)
  string format = 3 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### list_config_request.proto {#list_config_request}

**Path**: `gcommon/v1/config/list_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 41

**Messages** (1): `ListConfigRequest`

**Imports** (6):

- `gcommon/v1/common/filter_options.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/sort_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/list_config_request.proto
// version: 1.0.0
// guid: f18f6b5b-d699-4e53-a44b-0934ef94b688
//
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/filter_options.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/sort_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ListConfigRequest lists configuration entries with optional filtering.
 */
message ListConfigRequest {
  // Key prefix filter
  string prefix = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

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

**Path**: `gcommon/v1/config/list_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `ListConfigResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/config/config_entry.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/list_config_response.proto
// version: 1.0.0
// guid: 38867866-6d7f-4022-a74d-b2c09cdca946
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/config/config_entry.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ListConfigResponse returns configuration entries for a list operation.
 */
message ListConfigResponse {
  // Configuration entries
  repeated ConfigEntry entries = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information
  gcommon.v1.common.PaginatedResponse pagination = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}
```

---

### monitoring_config.proto {#monitoring_config}

**Path**: `gcommon/v1/config/monitoring_config.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `ConfigMonitoringConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/monitoring_config.proto
// version: 1.0.0
// guid: 07482bbc-1eea-451a-aa74-bbacfd829710

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigMonitoringConfig {
  // Monitoring enabled
  bool enabled = 1;

  // Monitoring provider
  string provider = 2 [(buf.validate.field).string.min_len = 1];

  // Monitoring endpoints
  repeated string endpoints = 3 [(buf.validate.field).repeated.min_items = 1];

  // Monitoring metrics
  repeated string metrics = 4 [(buf.validate.field).repeated.min_items = 1];

  // Monitoring alerts
  repeated string alerts = 5 [(buf.validate.field).repeated.min_items = 1];

  // Monitoring dashboards
  repeated string dashboards = 6 [(buf.validate.field).repeated.min_items = 1];

  // Monitoring configuration
  map<string, string> config = 7;
}
```

---

### reload_config_request.proto {#reload_config_request}

**Path**: `gcommon/v1/config/reload_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Messages** (1): `ReloadConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/reload_config_request.proto
// version: 1.0.0
// guid: 5d1ecbb6-f500-42a2-85a1-ee831ecb1936
// file: proto/gcommon/v1/config/reload_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ReloadConfigRequest {
  // Namespace to reload
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### restore_config_request.proto {#restore_config_request}

**Path**: `gcommon/v1/config/restore_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 31

**Messages** (1): `RestoreConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/restore_config_request.proto
// version: 1.0.0
// guid: 02590a49-63a8-4dc3-8ad9-2604a2244f0c
// file: proto/gcommon/v1/config/restore_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RestoreConfigRequest {
  // Restore point identifier
  string restore_point_id = 1 [(buf.validate.field).string.min_len = 1];

  // Namespace/environment to restore
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### rollback_config_request.proto {#rollback_config_request}

**Path**: `gcommon/v1/config/rollback_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 31

**Messages** (1): `RollbackConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/rollback_config_request.proto
// version: 1.0.0
// guid: bc3346ab-a699-4ab7-b8ca-95aa3357446f
// file: proto/gcommon/v1/config/rollback_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RollbackConfigRequest {
  // Version identifier to roll back to
  string version = 1 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Namespace/environment of the configuration
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### set_config_request.proto {#set_config_request}

**Path**: `gcommon/v1/config/set_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `SetConfigRequest`

**Imports** (4):

- `gcommon/v1/common/config_value.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/set_config_request.proto
// version: 1.0.0
// guid: 93685ade-6d8d-4400-b36f-c436cc41282a
//
// Request definitions for config module
// Generated as part of 1-1-1 migration
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_value.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

// Set configuration request
message SetConfigRequest {
  // Configuration key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration value
  gcommon.v1.common.ConfigValue value = 2;

  // Optional namespace/environment
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Configuration metadata
  map<string, string> metadata = 4;

  // Whether to encrypt the value
  bool encrypt = 5;

  // Tags for categorization
  repeated string tags = 6 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata request_metadata = 7;
}
```

---

### set_config_response.proto {#set_config_response}

**Path**: `gcommon/v1/config/set_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `SetConfigResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/config/config_entry.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/set_config_response.proto
// version: 1.0.1
// guid: 7da90b1f-9e44-4c7f-aa9d-1ad6d42ad675
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/config/config_entry.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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

**Path**: `gcommon/v1/config/set_config_schema_request.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `SetConfigSchemaRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/config/config_schema.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/set_config_schema_request.proto
// version: 1.0.0
// guid: 5031e4d6-2d21-40cf-b382-0a95e6ba91c7
// file: proto/gcommon/v1/config/set_config_schema_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/config/config_schema.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SetConfigSchemaRequest {
  // Namespace the schema applies to
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Schema definition
  ConfigSchema schema = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### set_multiple_config_request.proto {#set_multiple_config_request}

**Path**: `gcommon/v1/config/set_multiple_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 35

**Messages** (1): `SetMultipleConfigRequest`

**Imports** (4):

- `gcommon/v1/common/config_value.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/set_multiple_config_request.proto
// version: 1.0.0
// guid: 94773fcc-1702-4036-be15-d69ba58bcf4f
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_value.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * SetMultipleConfigRequest stores multiple configuration values.
 */
message SetMultipleConfigRequest {
  // Configuration entries to set
  map<string, gcommon.v1.common.ConfigValue> entries = 1;

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

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

**Path**: `gcommon/v1/config/set_multiple_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Messages** (1): `SetMultipleConfigResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/set_multiple_config_response.proto
// version: 1.0.1
// guid: e0520017-355f-4584-a5c7-d2bff7d21b3c
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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

### unwatch_config_request.proto {#unwatch_config_request}

**Path**: `gcommon/v1/config/unwatch_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Messages** (1): `UnwatchConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/unwatch_config_request.proto
// version: 1.0.0
// guid: 4fb39ff9-1c85-43d6-9246-d2cc5683ce22
// file: proto/gcommon/v1/config/unwatch_config_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message UnwatchConfigRequest {
  // Watch identifier returned by WatchConfigRequest
  string watch_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### validate_config_request.proto {#validate_config_request}

**Path**: `gcommon/v1/config/validate_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 31

**Messages** (1): `ValidateConfigRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/config/config_entry.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/validate_config_request.proto
// version: 1.0.0
// guid: da084b25-bf67-46da-8d18-395212e00e71
// file: proto/gcommon/v1/config/validate_config_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/config/config_entry.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValidateConfigRequest {
  // Configuration entries to validate
  repeated ConfigEntry entries = 1;

  // Schema to validate against
  string schema_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### validate_config_response.proto {#validate_config_response}

**Path**: `gcommon/v1/config/validate_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `ValidateConfigResponse`

**Imports** (4):

- `gcommon/v1/config/config_validation_error.proto`
- `gcommon/v1/config/config_validation_warning.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validate_config_response.proto
// version: 1.0.0
// guid: 3a5b4e78-277c-4940-aea5-6407836cbd4f
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/config_validation_error.proto";
import "gcommon/v1/config/config_validation_warning.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * ValidateConfigResponse contains validation results for configuration entries.
 */
message ValidateConfigResponse {
  // Validation result
  bool valid = 1;

  // Validation errors
  repeated ConfigValidationError errors = 2 [(buf.validate.field).repeated.min_items = 1];

  // Validation warnings
  repeated ConfigValidationWarning warnings = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### watch_config_request.proto {#watch_config_request}

**Path**: `gcommon/v1/config/watch_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Messages** (1): `WatchConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/watch_config_request.proto
// version: 1.0.0
// guid: c9ab6390-55d9-4d48-91c2-69b36288f4d2
// file: proto/gcommon/v1/config/watch_config_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message WatchConfigRequest {
  // Key or key pattern to watch
  string key_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace/environment
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### watch_config_response.proto {#watch_config_response}

**Path**: `gcommon/v1/config/watch_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 31

**Messages** (1): `WatchConfigResponse`

**Imports** (4):

- `gcommon/v1/common/config_config_change_type.proto`
- `gcommon/v1/config/config_entry.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/watch_config_response.proto
// version: 1.0.1
// guid: 88670dcd-4cd2-4a07-be66-f2d4db54a4a4
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_config_change_type.proto";
import "gcommon/v1/config/config_entry.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * WatchConfigResponse describes a configuration change event.
 */
message WatchConfigResponse {
  // Type of change
  gcommon.v1.common.ConfigChangeType change_type = 1;

  // Configuration entry
  ConfigEntry entry = 2;

  // Previous value for updates/deletes
  ConfigEntry previous_entry = 3;

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;
}
```

---

