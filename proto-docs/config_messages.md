# Config Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 112
- **Messages**: 112

## Table of Contents

### Messages

- [`AccessRestriction`](#access_restriction) - from access_restriction.proto
- [`ApprovalInfo`](#approval_info) - from approval_info.proto
- [`ApprovalRequirement`](#approval_requirement) - from approval_requirement.proto
- [`ApprovalStage`](#approval_stage) - from approval_stage.proto
- [`ApprovalWorkflow`](#approval_workflow) - from approval_workflow.proto
- [`AuditSettings`](#audit_settings) - from audit_settings.proto
- [`BackupConfigRequest`](#backup_config_request) - from backup_config_request.proto
- [`BackupPolicy`](#backup_policy) - from backup_policy.proto
- [`BackupSettings`](#backup_settings) - from backup_settings.proto
- [`BatchingSettings`](#batching_settings) - from batching_settings.proto
- [`CachingSettings`](#caching_settings) - from caching_settings.proto
- [`ComplianceAudit`](#compliance_audit) - from compliance_audit.proto
- [`ComplianceReporting`](#compliance_reporting) - from compliance_reporting.proto
- [`ConfigAccessControl`](#access_control) - from access_control.proto
- [`ConfigBackup`](#config_backup) - from config_backup.proto
- [`ConfigComplianceSettings`](#compliance_settings) - from compliance_settings.proto
- [`ConfigConfigChange`](#config_change) - from config_change.proto
- [`ConfigDiff`](#config_diff) - from config_diff.proto
- [`ConfigDiffEntry`](#config_diff_entry) - from config_diff_entry.proto
- [`ConfigEntry`](#config_entry) - from config_entry.proto
- [`ConfigEnvironment`](#config_environment) - from config_environment.proto
- [`ConfigHealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`ConfigHealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`ConfigHealthCheckResult`](#health_check_result) - from health_check_result.proto
- [`ConfigHealthStatus`](#health_status) - from health_status.proto
- [`ConfigMonitoringConfig`](#monitoring_config) - from monitoring_config.proto
- [`ConfigNotificationChannel`](#notification_channel) - from notification_channel.proto
- [`ConfigNotificationSettings`](#notification_settings) - from notification_settings.proto
- [`ConfigResourceLimits`](#resource_limits) - from resource_limits.proto
- [`ConfigRetentionPolicy`](#retention_policy) - from retention_policy.proto
- [`ConfigSchema`](#config_schema) - from config_schema.proto
- [`ConfigSnapshot`](#config_snapshot) - from config_snapshot.proto
- [`ConfigStats`](#config_stats) - from config_stats.proto
- [`ConfigValidationError`](#config_validation_error) - from config_validation_error.proto
- [`ConfigValidationResult`](#validation_result) - from validation_result.proto
- [`ConfigValidationWarning`](#config_validation_warning) - from config_validation_warning.proto
- [`ConfigWatch`](#config_watch) - from config_watch.proto
- [`ConfigWatchEvent`](#config_watch_event) - from config_watch_event.proto
- [`DecryptConfigRequest`](#decrypt_config_request) - from decrypt_config_request.proto
- [`DeleteConfigRequest`](#delete_config_request) - from delete_config_request.proto
- [`DeploymentInfo`](#deployment_info) - from deployment_info.proto
- [`DeploymentRollbackInfo`](#deployment_rollback_info) - from deployment_rollback_info.proto
- [`DeprecationInfo`](#deprecation_info) - from deprecation_info.proto
- [`EncryptConfigRequest`](#encrypt_config_request) - from encrypt_config_request.proto
- [`EncryptionSettings`](#encryption_settings) - from encryption_settings.proto
- [`ExportConfigRequest`](#export_config_request) - from export_config_request.proto
- [`GetConfigHistoryRequest`](#get_config_history_request) - from get_config_history_request.proto
- [`GetConfigHistoryResponse`](#get_config_history_response) - from get_config_history_response.proto
- [`GetConfigRequest`](#get_config_request) - from get_config_request.proto
- [`GetConfigResponse`](#get_config_response) - from get_config_response.proto
- [`GetConfigStatsRequest`](#get_config_stats_request) - from get_config_stats_request.proto
- [`GetConfigStatsResponse`](#get_config_stats_response) - from get_config_stats_response.proto
- [`GetMultipleConfigRequest`](#get_multiple_config_request) - from get_multiple_config_request.proto
- [`GetMultipleConfigResponse`](#get_multiple_config_response) - from get_multiple_config_response.proto
- [`GetSchemaRequest`](#get_schema_request) - from get_schema_request.proto
- [`GetSchemaResponse`](#get_schema_response) - from get_schema_response.proto
- [`HealthCheck`](#health_check) - from health_check.proto
- [`ImportConfigRequest`](#import_config_request) - from import_config_request.proto
- [`InheritanceFilter`](#inheritance_filter) - from inheritance_filter.proto
- [`InheritanceSettings`](#inheritance_settings) - from inheritance_settings.proto
- [`InheritanceTransformation`](#inheritance_transformation) - from inheritance_transformation.proto
- [`ListConfigRequest`](#list_config_request) - from list_config_request.proto
- [`ListConfigResponse`](#list_config_response) - from list_config_response.proto
- [`MonitoringAlert`](#monitoring_alert) - from monitoring_alert.proto
- [`MonitoringSettings`](#monitoring_settings) - from monitoring_settings.proto
- [`PromotionRule`](#promotion_rule) - from promotion_rule.proto
- [`RateLimits`](#rate_limits) - from rate_limits.proto
- [`ReloadConfigRequest`](#reload_config_request) - from reload_config_request.proto
- [`RestoreConfigRequest`](#restore_config_request) - from restore_config_request.proto
- [`RollbackConfigRequest`](#rollback_config_request) - from rollback_config_request.proto
- [`RollbackInfo`](#rollback_info) - from rollback_info.proto
- [`RotationEvent`](#rotation_event) - from rotation_event.proto
- [`RotationSettings`](#rotation_settings) - from rotation_settings.proto
- [`SecretAuditSettings`](#secret_audit_settings) - from secret_audit_settings.proto
- [`SecretBackupSettings`](#secret_backup_settings) - from secret_backup_settings.proto
- [`SecretValidationResult`](#secret_validation_result) - from secret_validation_result.proto
- [`SetConfigRequest`](#set_config_request) - from set_config_request.proto
- [`SetConfigResponse`](#set_config_response) - from set_config_response.proto
- [`SetConfigSchemaRequest`](#set_config_schema_request) - from set_config_schema_request.proto
- [`SetMultipleConfigRequest`](#set_multiple_config_request) - from set_multiple_config_request.proto
- [`SetMultipleConfigResponse`](#set_multiple_config_response) - from set_multiple_config_response.proto
- [`SyncSettings`](#sync_settings) - from sync_settings.proto
- [`SynchronizationSettings`](#synchronization_settings) - from synchronization_settings.proto
- [`SynchronizationTarget`](#synchronization_target) - from synchronization_target.proto
- [`TemplateChange`](#template_change) - from template_change.proto
- [`TemplateHook`](#template_hook) - from template_hook.proto
- [`TemplateOutput`](#template_output) - from template_output.proto
- [`TransformationSettings`](#transformation_settings) - from transformation_settings.proto
- [`TransformationStep`](#transformation_step) - from transformation_step.proto
- [`UnwatchConfigRequest`](#unwatch_config_request) - from unwatch_config_request.proto
- [`UsageStatistics`](#usage_statistics) - from usage_statistics.proto
- [`UsageTrend`](#usage_trend) - from usage_trend.proto
- [`ValidateConfigRequest`](#validate_config_request) - from validate_config_request.proto
- [`ValidateConfigResponse`](#validate_config_response) - from validate_config_response.proto
- [`ValidationRule`](#validation_rule) - from validation_rule.proto
- [`ValidationSettings`](#validation_settings) - from validation_settings.proto
- [`ValueDependency`](#value_dependency) - from value_dependency.proto
- [`ValueHistoryEntry`](#value_history_entry) - from value_history_entry.proto
- [`ValueReference`](#value_reference) - from value_reference.proto
- [`ValueUsageStatistics`](#value_usage_statistics) - from value_usage_statistics.proto
- [`ValueUsageTrend`](#value_usage_trend) - from value_usage_trend.proto
- [`ValueValidationResult`](#value_validation_result) - from value_validation_result.proto
- [`VersionArtifact`](#version_artifact) - from version_artifact.proto
- [`VersionCompatibilityInfo`](#version_compatibility_info) - from version_compatibility_info.proto
- [`VersionDependency`](#version_dependency) - from version_dependency.proto
- [`VersionDeploymentInfo`](#version_deployment_info) - from version_deployment_info.proto
- [`VersionPromotionEvent`](#version_promotion_event) - from version_promotion_event.proto
- [`VersionQualityIssue`](#version_quality_issue) - from version_quality_issue.proto
- [`VersionQualityMetrics`](#version_quality_metrics) - from version_quality_metrics.proto
- [`VersioningSettings`](#versioning_settings) - from versioning_settings.proto
- [`WatchConfigRequest`](#watch_config_request) - from watch_config_request.proto
- [`WatchConfigResponse`](#watch_config_response) - from watch_config_response.proto

### Files in this Module

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
- [access_control.proto](#access_control)
- [access_restriction.proto](#access_restriction)
- [approval_info.proto](#approval_info)
- [approval_requirement.proto](#approval_requirement)
- [approval_stage.proto](#approval_stage)
- [approval_workflow.proto](#approval_workflow)
- [audit_settings.proto](#audit_settings)
- [batching_settings.proto](#batching_settings)
- [caching_settings.proto](#caching_settings)
- [compliance_audit.proto](#compliance_audit)
- [compliance_reporting.proto](#compliance_reporting)
- [compliance_settings.proto](#compliance_settings)
- [deployment_info.proto](#deployment_info)
- [deployment_rollback_info.proto](#deployment_rollback_info)
- [deprecation_info.proto](#deprecation_info)
- [encryption_settings.proto](#encryption_settings)
- [health_check.proto](#health_check)
- [health_check_result.proto](#health_check_result)
- [health_status.proto](#health_status)
- [inheritance_filter.proto](#inheritance_filter)
- [inheritance_settings.proto](#inheritance_settings)
- [inheritance_transformation.proto](#inheritance_transformation)
- [monitoring_alert.proto](#monitoring_alert)
- [monitoring_settings.proto](#monitoring_settings)
- [notification_channel.proto](#notification_channel)
- [notification_settings.proto](#notification_settings)
- [promotion_rule.proto](#promotion_rule)
- [rate_limits.proto](#rate_limits)
- [resource_limits.proto](#resource_limits)
- [retention_policy.proto](#retention_policy)
- [rotation_settings.proto](#rotation_settings)
- [secret_audit_settings.proto](#secret_audit_settings)
- [secret_backup_settings.proto](#secret_backup_settings)
- [secret_validation_result.proto](#secret_validation_result)
- [sync_settings.proto](#sync_settings)
- [synchronization_settings.proto](#synchronization_settings)
- [synchronization_target.proto](#synchronization_target)
- [template_change.proto](#template_change)
- [template_hook.proto](#template_hook)
- [template_output.proto](#template_output)
- [transformation_settings.proto](#transformation_settings)
- [transformation_step.proto](#transformation_step)
- [usage_statistics.proto](#usage_statistics)
- [usage_trend.proto](#usage_trend)
- [validation_result.proto](#validation_result)
- [validation_rule.proto](#validation_rule)
- [validation_settings.proto](#validation_settings)
- [value_dependency.proto](#value_dependency)
- [value_history_entry.proto](#value_history_entry)
- [value_reference.proto](#value_reference)
- [value_usage_statistics.proto](#value_usage_statistics)
- [value_usage_trend.proto](#value_usage_trend)
- [value_validation_result.proto](#value_validation_result)
- [version_artifact.proto](#version_artifact)
- [version_compatibility_info.proto](#version_compatibility_info)
- [version_dependency.proto](#version_dependency)
- [version_deployment_info.proto](#version_deployment_info)
- [version_quality_issue.proto](#version_quality_issue)
- [version_quality_metrics.proto](#version_quality_metrics)
- [versioning_settings.proto](#versioning_settings)
- [backup_policy.proto](#backup_policy)
- [backup_settings.proto](#backup_settings)
- [get_schema_request.proto](#get_schema_request)
- [get_schema_response.proto](#get_schema_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [rollback_info.proto](#rollback_info)
- [config_watch_event.proto](#config_watch_event)
- [rotation_event.proto](#rotation_event)
- [version_promotion_event.proto](#version_promotion_event)

---


## Messages Documentation

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

### access_control.proto {#access_control}

**Path**: `gcommon/v1/config/access_control.proto` **Package**: `gcommon.v1.config` **Lines**: 48

**Messages** (1): `ConfigAccessControl`

**Imports** (4):

- `gcommon/v1/config/access_restriction.proto`
- `gcommon/v1/config/rate_limits.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/access_control.proto
// version: 1.0.0
// guid: 5707e31a-b72e-4cc1-b3ba-87269e99e05b

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/access_restriction.proto";
import "gcommon/v1/config/rate_limits.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigAccessControl {
  // Access policy
  string policy = 1 [(buf.validate.field).string.min_len = 1];

  // Allowed users
  repeated string allowed_users = 2 [(buf.validate.field).repeated.min_items = 1];

  // Allowed roles
  repeated string allowed_roles = 3 [(buf.validate.field).repeated.min_items = 1];

  // Allowed services
  repeated string allowed_services = 4 [(buf.validate.field).repeated.min_items = 1];

  // Allowed environments
  repeated string allowed_environments = 5 [(buf.validate.field).repeated.min_items = 1];

  // Access restrictions
  repeated AccessRestriction restrictions = 6 [(buf.validate.field).repeated.min_items = 1];

  // Maximum access count
  int32 max_access_count = 7 [(buf.validate.field).int32.gte = 0];

  // Access rate limits
  RateLimits rate_limits = 8;

  // Access approval required
  bool approval_required = 9;

  // Access audit enabled
  bool audit_enabled = 10;
}
```

---

### access_restriction.proto {#access_restriction}

**Path**: `gcommon/v1/config/access_restriction.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `AccessRestriction`

**Imports** (3):

- `gcommon/v1/common/restriction_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/access_restriction.proto
// version: 1.0.0
// guid: cfdd7cdc-6bb3-4b8f-b3a9-fa8a84cc84ad

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/restriction_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message AccessRestriction {
  // Restriction type
  gcommon.v1.common.RestrictionType type = 1;

  // Restriction value
  string value = 2 [(buf.validate.field).string.min_len = 1];

  // Restriction operator
  string operator = 3 [(buf.validate.field).string.min_len = 1];

  // Restriction reason
  string reason = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### approval_info.proto {#approval_info}

**Path**: `gcommon/v1/config/approval_info.proto` **Package**: `gcommon.v1.config` **Lines**: 41

**Messages** (1): `ApprovalInfo`

**Imports** (4):

- `gcommon/v1/common/approval_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/approval_info.proto
// version: 1.0.0
// guid: 28dbf45a-ffed-40b5-8bad-30879b48ddcd

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/approval_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ApprovalInfo {
  // Whether approval was required
  bool required = 1;

  // Approval status
  gcommon.v1.common.ApprovalStatus status = 2;

  // User who approved
  string approved_by = 3;

  // Approval timestamp
  google.protobuf.Timestamp approved_at = 4;

  // Approval comments
  string comments = 5;

  // Approval workflow ID
  string workflow_id = 6;

  // Approval policy applied
  string policy_name = 7 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### approval_requirement.proto {#approval_requirement}

**Path**: `gcommon/v1/config/approval_requirement.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `ApprovalRequirement`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/approval_requirement.proto
// version: 1.0.0
// guid: 54ae6b55-a574-4ad5-89ea-9cadf541517a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ApprovalRequirement {
  // Whether approval is required
  bool required = 1;

  // Number of approvals required
  int32 approval_count = 2 [(buf.validate.field).int32.gte = 0];

  // Required approver roles
  repeated string approver_roles = 3 [(buf.validate.field).repeated.min_items = 1];

  // Required approver users
  repeated string approver_users = 4 [(buf.validate.field).repeated.min_items = 1];

  // Approval policy
  string policy = 5 [(buf.validate.field).string.min_len = 1];

  // Approval workflow
  string workflow = 6 [(buf.validate.field).string.min_len = 1];

  // Auto-approval conditions
  repeated string auto_approval_conditions = 7 [(buf.validate.field).repeated.min_items = 1];

  // Approval timeout
  int32 approval_timeout_hours = 8 [(buf.validate.field).int32.gt = 0];
}
```

---

### approval_stage.proto {#approval_stage}

**Path**: `gcommon/v1/config/approval_stage.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `ApprovalStage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/approval_stage.proto
// version: 1.0.0
// guid: 40bf0e9f-ef92-44c7-94fe-0b5f3ac6e653

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ApprovalStage {
  // Stage name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
```

---

### approval_workflow.proto {#approval_workflow}

**Path**: `gcommon/v1/config/approval_workflow.proto` **Package**: `gcommon.v1.config` **Lines**: 35

**Messages** (1): `ApprovalWorkflow`

**Imports** (3):

- `gcommon/v1/config/approval_stage.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/approval_workflow.proto
// version: 1.0.0
// guid: b19bfc28-1770-4f3d-a1d5-cb8f6e45ad88

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/approval_stage.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ApprovalWorkflow {
  // Workflow enabled
  bool enabled = 1;

  // Workflow type
  string type = 2 [(buf.validate.field).string.min_len = 1];

  // Approval stages
  repeated gcommon.v1.config.ApprovalStage stages = 3 [(buf.validate.field).repeated.min_items = 1];

  // Workflow timeout
  int32 timeout_hours = 4 [(buf.validate.field).int32.gt = 0];

  // Workflow conditions
  repeated string conditions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Workflow notifications
  repeated string notifications = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### audit_settings.proto {#audit_settings}

**Path**: `gcommon/v1/config/audit_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `AuditSettings`

**Imports** (3):

- `gcommon/v1/common/audit_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/audit_settings.proto
// version: 1.0.0
// guid: be3f66f2-0951-46ae-b393-e44f8132948b

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/audit_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message AuditSettings {
  // Whether audit logging is enabled
  bool enabled = 1;

  // Audit log level
  gcommon.v1.common.AuditLevel level = 2;

  // Audit log retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Whether to include sensitive data in audit logs
  bool include_sensitive_data = 4;

  // External audit destinations
  repeated string destinations = 5 [(buf.validate.field).repeated.min_items = 1];

  // Audit log format
  string format = 6 [(buf.validate.field).string.min_len = 1];

  // Additional audit metadata
  map<string, string> metadata = 7;
}
```

---

### batching_settings.proto {#batching_settings}

**Path**: `gcommon/v1/config/batching_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 28

**Messages** (1): `BatchingSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/batching_settings.proto
// version: 1.0.0
// guid: 2814da2b-956d-4e34-b87c-7bf8c1bceb5e

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message BatchingSettings {
  // Whether batching is enabled
  bool enabled = 1;

  // Batch size
  int32 batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Batch timeout in minutes
  int32 timeout_minutes = 3 [(buf.validate.field).int32.gt = 0];

  // Batch grouping key
  string grouping_key = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### caching_settings.proto {#caching_settings}

**Path**: `gcommon/v1/config/caching_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `CachingSettings`

**Imports** (4):

- `gcommon/v1/common/cache_invalidation_trigger.proto`
- `gcommon/v1/common/cache_refresh_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/caching_settings.proto
// version: 1.0.0
// guid: 2c6f8039-2855-4a31-884a-4d66d71cf897

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/cache_invalidation_trigger.proto";
import "gcommon/v1/common/cache_refresh_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message CachingSettings {
  // Whether caching is enabled
  bool enabled = 1;

  // Cache TTL in seconds
  int32 ttl_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Cache refresh strategy
  gcommon.v1.common.CacheRefreshStrategy refresh_strategy = 3;

  // Cache invalidation triggers
  repeated gcommon.v1.common.CacheInvalidationTrigger triggers = 4 [(buf.validate.field).repeated.min_items = 1];

  // Cache metadata
  map<string, string> metadata = 5;
}
```

---

### compliance_audit.proto {#compliance_audit}

**Path**: `gcommon/v1/config/compliance_audit.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `ComplianceAudit`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/compliance_audit.proto
// version: 1.0.0
// guid: d3e4f5a6-7b8c-9012-def0-345678901234

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ComplianceAudit {
  // Audit ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Audit name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Audit type
  string type = 3;

  // Audit enabled status
  bool enabled = 4;
}
```

---

### compliance_reporting.proto {#compliance_reporting}

**Path**: `gcommon/v1/config/compliance_reporting.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Messages** (1): `ComplianceReporting`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/compliance_reporting.proto
// version: 1.0.0
// guid: e4f5a6b7-8c9d-0123-ef01-456789012345

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ComplianceReporting {
  // Reporting enabled status
  bool enabled = 1;

  // Report frequency in hours
  int32 frequency_hours = 2 [(buf.validate.field).int32.gte = 0];

  // Report recipients
  repeated string recipients = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### compliance_settings.proto {#compliance_settings}

**Path**: `gcommon/v1/config/compliance_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `ConfigComplianceSettings`

**Imports** (4):

- `gcommon/v1/config/compliance_audit.proto`
- `gcommon/v1/config/compliance_reporting.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/compliance_settings.proto
// version: 1.0.0
// guid: 55ae9eb4-4811-4e34-89e6-b2c7f128297e

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/compliance_audit.proto";
import "gcommon/v1/config/compliance_reporting.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigComplianceSettings {
  // Compliance frameworks
  repeated string frameworks = 1 [(buf.validate.field).repeated.min_items = 1];

  // Compliance policies
  repeated string policies = 2 [(buf.validate.field).repeated.min_items = 1];

  // Compliance audits
  repeated gcommon.v1.config.ComplianceAudit audits = 3 [(buf.validate.field).repeated.min_items = 1];

  // Compliance reporting
  gcommon.v1.config.ComplianceReporting reporting = 4;

  // Compliance validation
  bool validation_enabled = 5;

  // Compliance metadata
  map<string, string> metadata = 6;
}
```

---

### deployment_info.proto {#deployment_info}

**Path**: `gcommon/v1/config/deployment_info.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `DeploymentInfo`

**Imports** (6):

- `gcommon/v1/common/deployment_status.proto`
- `gcommon/v1/config/deployment_rollback_info.proto`
- `gcommon/v1/config/health_check.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deployment_info.proto
// version: 1.0.0
// guid: 07fcdb63-0b96-42e8-ab5e-6656870d6f03

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/deployment_status.proto";
import "gcommon/v1/config/deployment_rollback_info.proto";
import "gcommon/v1/config/health_check.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message DeploymentInfo {
  // Deployment status
  gcommon.v1.common.DeploymentStatus status = 1;

  // Last deployment timestamp
  google.protobuf.Timestamp last_deployed_at = 2;

  // Deployment version
  string version = 3 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Deployment method
  string method = 4 [(buf.validate.field).string.min_len = 1];

  // Deployment target
  string target = 5 [(buf.validate.field).string.min_len = 1];

  // Deployment configuration
  map<string, string> config = 6;

  // Deployment health checks
  repeated HealthCheck health_checks = 7 [(buf.validate.field).repeated.min_items = 1];

  // Deployment rollback info
  DeploymentRollbackInfo rollback_info = 8;
}
```

---

### deployment_rollback_info.proto {#deployment_rollback_info}

**Path**: `gcommon/v1/config/deployment_rollback_info.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `DeploymentRollbackInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deployment_rollback_info.proto
// version: 1.0.0
// guid: a7d7152b-5b23-4a12-aa77-0914b3db2822

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message DeploymentRollbackInfo {
  // Rollback available
  bool available = 1;

  // Previous version
  string previous_version = 2 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Rollback timestamp
  google.protobuf.Timestamp rollback_timestamp = 3;

  // Rollback reason
  string reason = 4 [(buf.validate.field).string.min_len = 1];

  // Rollback method
  string method = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### deprecation_info.proto {#deprecation_info}

**Path**: `gcommon/v1/config/deprecation_info.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Messages** (1): `DeprecationInfo`

**Imports** (4):

- `gcommon/v1/common/deprecation_level.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deprecation_info.proto
// version: 1.0.0
// guid: 8431c848-ce8a-41cf-9848-ee052647463a

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/deprecation_level.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message DeprecationInfo {
  // Whether the configuration is deprecated
  bool deprecated = 1;

  // Deprecation reason
  string reason = 2 [(buf.validate.field).string.min_len = 1];

  // Deprecation date
  google.protobuf.Timestamp deprecated_at = 3;

  // Replacement configuration key
  string replacement_key = 4 [(buf.validate.field).string.min_len = 1];

  // Removal date
  google.protobuf.Timestamp removal_date = 5;

  // Migration guide
  string migration_guide = 6 [(buf.validate.field).string.min_len = 1];

  // Deprecation level
  gcommon.v1.common.DeprecationLevel level = 7;
}
```

---

### encryption_settings.proto {#encryption_settings}

**Path**: `gcommon/v1/config/encryption_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `EncryptionSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/encryption_settings.proto
// version: 1.0.0
// guid: 60653f55-24f4-4171-936f-a6c0643044de

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message EncryptionSettings {
  // Encryption enabled
  bool enabled = 1;

  // Encryption provider
  string provider = 2 [(buf.validate.field).string.min_len = 1];

  // Encryption key
  string key_id = 3 [(buf.validate.field).string.min_len = 1];

  // Encryption algorithm
  string algorithm = 4 [(buf.validate.field).string.min_len = 1];

  // Encryption mode
  string mode = 5 [(buf.validate.field).string.min_len = 1];

  // Encryption configuration
  map<string, string> config = 6;
}
```

---

### health_check.proto {#health_check}

**Path**: `gcommon/v1/config/health_check.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `HealthCheck`

**Imports** (3):

- `gcommon/v1/common/health_check_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check.proto
// version: 1.0.0
// guid: a4cee3ca-9b9b-4b61-bc58-0a9b8d4fa96f

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/health_check_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message HealthCheck {
  // Health check name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Health check type
  gcommon.v1.common.HealthCheckType type = 2;

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
```

---

### health_check_result.proto {#health_check_result}

**Path**: `gcommon/v1/config/health_check_result.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `ConfigHealthCheckResult`

**Imports** (4):

- `gcommon/v1/common/health_state.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_result.proto
// version: 1.0.0
// guid: 5a4b2cbd-08cd-42f3-9fbb-b55de4ffd527

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/health_state.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigHealthCheckResult {
  // Health check name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Health check status
  gcommon.v1.common.HealthState status = 2;

  // Health check message
  string message = 3;

  // Health check timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Health check duration
  int32 duration_ms = 5;

  // Health check details
  map<string, string> details = 6;
}
```

---

### health_status.proto {#health_status}

**Path**: `gcommon/v1/config/health_status.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `ConfigHealthStatus`

**Imports** (5):

- `gcommon/v1/common/health_state.proto`
- `gcommon/v1/config/health_check_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_status.proto
// version: 1.0.0
// guid: 0be35195-6cee-4fad-b426-eddc99a61e0c

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/health_state.proto";
import "gcommon/v1/config/health_check_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigHealthStatus {
  // Overall health
  gcommon.v1.common.HealthState overall = 1;

  // Component health
  map<string, gcommon.v1.common.HealthState> components = 2;

  // Health checks
  repeated ConfigHealthCheckResult health_checks = 3 [(buf.validate.field).repeated.min_items = 1];

  // Last health check
  google.protobuf.Timestamp last_check = 4;

  // Health metrics
  map<string, double> metrics = 5;
}
```

---

### inheritance_filter.proto {#inheritance_filter}

**Path**: `gcommon/v1/config/inheritance_filter.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `InheritanceFilter`

**Imports** (4):

- `gcommon/v1/common/filter_action.proto`
- `gcommon/v1/common/filter_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/inheritance_filter.proto
// version: 1.0.0
// guid: 0cda004b-8fb1-47de-a58b-fb17ec38d92f

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/filter_action.proto";
import "gcommon/v1/common/filter_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message InheritanceFilter {
  // Filter type
  gcommon.v1.common.LogFilterType type = 1;

  // Filter expression
  string expression = 2 [(buf.validate.field).string.min_len = 1];

  // Filter action
  gcommon.v1.common.FilterAction action = 3;

  // Filter metadata
  map<string, string> metadata = 4;
}
```

---

### inheritance_settings.proto {#inheritance_settings}

**Path**: `gcommon/v1/config/inheritance_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `InheritanceSettings`

**Imports** (6):

- `gcommon/v1/common/inheritance_strategy.proto`
- `gcommon/v1/common/merge_strategy.proto`
- `gcommon/v1/config/inheritance_filter.proto`
- `gcommon/v1/config/inheritance_transformation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/inheritance_settings.proto
// version: 1.0.0
// guid: f7c6c365-e83d-4ae8-8166-fb86d2e3b6f0

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/inheritance_strategy.proto";
import "gcommon/v1/common/merge_strategy.proto";
import "gcommon/v1/config/inheritance_filter.proto";
import "gcommon/v1/config/inheritance_transformation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message InheritanceSettings {
  // Whether inheritance is enabled
  bool enabled = 1;

  // Inheritance strategy
  gcommon.v1.common.InheritanceStrategy strategy = 2;

  // Inheritance sources in order of priority
  repeated string sources = 3 [(buf.validate.field).repeated.min_items = 1];

  // Inheritance filters
  repeated InheritanceFilter filters = 4 [(buf.validate.field).repeated.min_items = 1];

  // Inheritance transformations
  repeated InheritanceTransformation transformations = 5 [(buf.validate.field).repeated.min_items = 1];

  // Whether to merge inherited values
  bool merge_values = 6;

  // Merge strategy for complex values
  gcommon.v1.common.MergeStrategy merge_strategy = 7;

  // Inheritance metadata
  map<string, string> metadata = 8;
}
```

---

### inheritance_transformation.proto {#inheritance_transformation}

**Path**: `gcommon/v1/config/inheritance_transformation.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `InheritanceTransformation`

**Imports** (3):

- `gcommon/v1/common/transformation_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/inheritance_transformation.proto
// version: 1.0.0
// guid: 9983db27-ce0c-4ed1-9433-20495b86b257

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/transformation_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message InheritanceTransformation {
  // Transformation type
  gcommon.v1.common.TransformationType type = 1;

  // Transformation expression
  string expression = 2 [(buf.validate.field).string.min_len = 1];

  // Transformation parameters
  map<string, string> parameters = 3;

  // Transformation metadata
  map<string, string> metadata = 4;
}
```

---

### monitoring_alert.proto {#monitoring_alert}

**Path**: `gcommon/v1/config/monitoring_alert.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `MonitoringAlert`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/monitoring_alert.proto
// version: 1.0.0
// guid: a6b7c8d9-0e1f-2345-0123-678901234567

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message MonitoringAlert {
  // Alert ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Alert name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Alert condition
  string condition = 3;

  // Alert threshold
  double threshold = 4;

  // Alert enabled status
  bool enabled = 5;
}
```

---

### monitoring_settings.proto {#monitoring_settings}

**Path**: `gcommon/v1/config/monitoring_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `MonitoringSettings`

**Imports** (3):

- `gcommon/v1/config/monitoring_alert.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/monitoring_settings.proto
// version: 1.0.0
// guid: 1df1c6fa-7f81-4982-9c0e-040b1f0ad10f

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/monitoring_alert.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message MonitoringSettings {
  // Whether monitoring is enabled
  bool enabled = 1;

  // Monitoring alerts
  repeated gcommon.v1.config.MonitoringAlert alerts = 2 [(buf.validate.field).repeated.min_items = 1];

  // Monitoring metrics
  repeated string metrics = 3 [(buf.validate.field).repeated.min_items = 1];

  // Monitoring dashboard
  string dashboard = 4 [(buf.validate.field).string.min_len = 1];

  // Monitoring retention period in days
  int32 retention_days = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### notification_channel.proto {#notification_channel}

**Path**: `gcommon/v1/config/notification_channel.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `ConfigNotificationChannel`

**Imports** (3):

- `gcommon/v1/common/channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/notification_channel.proto
// version: 1.0.0
// guid: 81ed59c5-4e0f-499a-97c8-57a2a375fd75

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigNotificationChannel {
  // Channel type
  gcommon.v1.common.ChannelType type = 1;

  // Channel configuration
  map<string, string> config = 2;

  // Whether channel is enabled
  bool enabled = 3;

  // Channel priority
  int32 priority = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### notification_settings.proto {#notification_settings}

**Path**: `gcommon/v1/config/notification_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `ConfigNotificationSettings`

**Imports** (5):

- `gcommon/v1/common/notification_trigger.proto`
- `gcommon/v1/config/batching_settings.proto`
- `gcommon/v1/config/notification_channel.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/notification_settings.proto
// version: 1.0.0
// guid: 4694674c-55fc-4ee7-8874-efe3ad5f1250

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/notification_trigger.proto";
import "gcommon/v1/config/batching_settings.proto";
import "gcommon/v1/config/notification_channel.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigNotificationSettings {
  // Whether notifications are enabled
  bool enabled = 1;

  // Notification channels
  repeated ConfigNotificationChannel channels = 2 [(buf.validate.field).repeated.min_items = 1];

  // Notification triggers
  repeated gcommon.v1.common.NotificationTrigger triggers = 3 [(buf.validate.field).repeated.min_items = 1];

  // Notification template
  string template = 4 [(buf.validate.field).string.min_len = 1];

  // Notification recipients
  repeated string recipients = 5 [(buf.validate.field).repeated.min_items = 1];

  // Notification delay in minutes
  int32 delay_minutes = 6 [(buf.validate.field).int32.gte = 0];

  // Notification batching settings
  BatchingSettings batching = 7;
}
```

---

### promotion_rule.proto {#promotion_rule}

**Path**: `gcommon/v1/config/promotion_rule.proto` **Package**: `gcommon.v1.config` **Lines**: 48

**Messages** (1): `PromotionRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/promotion_rule.proto
// version: 1.0.0
// guid: 6333713c-4522-4225-aa2f-46423912d1ec

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message PromotionRule {
  // Rule name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
```

---

### rate_limits.proto {#rate_limits}

**Path**: `gcommon/v1/config/rate_limits.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Messages** (1): `RateLimits`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rate_limits.proto
// version: 1.0.0
// guid: c2d3e4f5-6a7b-8901-cdef-234567890123

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RateLimits {
  // Maximum requests per second
  int32 requests_per_second = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum burst size
  int32 burst_size = 2 [(buf.validate.field).int32.gte = 0];

  // Rate limit window in seconds
  int32 window_seconds = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### resource_limits.proto {#resource_limits}

**Path**: `gcommon/v1/config/resource_limits.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `ConfigResourceLimits`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/resource_limits.proto
// version: 1.0.0
// guid: 8b09091e-5119-4f60-b274-2cdfe2ce451d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigResourceLimits {
  // CPU limit
  string cpu_limit = 1 [(buf.validate.field).string.min_len = 1];

  // Memory limit
  string memory_limit = 2 [(buf.validate.field).string.min_len = 1];

  // Storage limit
  string storage_limit = 3 [(buf.validate.field).string.min_len = 1];

  // Network limit
  string network_limit = 4 [(buf.validate.field).string.min_len = 1];

  // Request rate limit
  int32 request_rate_limit = 5 [(buf.validate.field).int32.gte = 0];

  // Concurrent connections limit
  int32 connection_limit = 6 [(buf.validate.field).int32.gte = 0];

  // Custom limits
  map<string, string> custom_limits = 7;
}
```

---

### retention_policy.proto {#retention_policy}

**Path**: `gcommon/v1/config/retention_policy.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `ConfigRetentionPolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/retention_policy.proto
// version: 1.0.0
// guid: 6144fe44-891b-4c63-818e-572c219e36a7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigRetentionPolicy {
  // Retention enabled
  bool enabled = 1;

  // Configuration retention
  int32 config_retention_days = 2 [(buf.validate.field).int32.gte = 0];

  // Audit log retention
  int32 audit_retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup retention
  int32 backup_retention_days = 4 [(buf.validate.field).int32.gte = 0];

  // Metrics retention
  int32 metrics_retention_days = 5 [(buf.validate.field).int32.gte = 0];

  // Custom retention policies
  map<string, int32> custom_retention = 6;
}
```

---

### rotation_settings.proto {#rotation_settings}

**Path**: `gcommon/v1/config/rotation_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 49

**Messages** (1): `RotationSettings`

**Imports** (5):

- `gcommon/v1/common/rotation_frequency.proto`
- `gcommon/v1/config/rotation_event.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/rotation_settings.proto
// version: 1.0.0
// guid: f9ec4d9b-b31b-410a-a6d5-f53e24671b44

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/rotation_frequency.proto";
import "gcommon/v1/config/rotation_event.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RotationSettings {
  // Whether rotation is enabled
  bool enabled = 1;

  // Rotation frequency
  gcommon.v1.common.RotationFrequency frequency = 2;

  // Rotation schedule (cron expression)
  string schedule = 3 [(buf.validate.field).string.min_len = 1];

  // Grace period before old secret expires
  int32 grace_period_days = 4 [(buf.validate.field).int32.gte = 0];

  // Whether to automatically rotate
  bool auto_rotate = 5;

  // Rotation notification settings
  repeated string notification_recipients = 6 [(buf.validate.field).repeated.min_items = 1];

  // Rotation workflow
  string workflow = 7 [(buf.validate.field).string.min_len = 1];

  // Last rotation timestamp
  google.protobuf.Timestamp last_rotated_at = 8;

  // Next rotation timestamp
  google.protobuf.Timestamp next_rotation_at = 9;

  // Rotation history
  repeated gcommon.v1.config.RotationEvent rotation_history = 10 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### secret_audit_settings.proto {#secret_audit_settings}

**Path**: `gcommon/v1/config/secret_audit_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `SecretAuditSettings`

**Imports** (3):

- `gcommon/v1/common/secret_audit_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/secret_audit_settings.proto
// version: 1.0.0
// guid: 1da3c9ca-367b-4399-ba06-b6eb865ad744

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/secret_audit_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SecretAuditSettings {
  // Whether audit logging is enabled
  bool enabled = 1;

  // Audit log level
  gcommon.v1.common.SecretAuditLevel level = 2;

  // Audit log retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Whether to log access events
  bool log_access = 4;

  // Whether to log rotation events
  bool log_rotation = 5;

  // Whether to log modification events
  bool log_modification = 6;

  // External audit destinations
  repeated string destinations = 7 [(buf.validate.field).repeated.min_items = 1];

  // Audit log format
  string format = 8 [(buf.validate.field).string.min_len = 1];

  // Additional audit metadata
  map<string, string> metadata = 9;
}
```

---

### secret_backup_settings.proto {#secret_backup_settings}

**Path**: `gcommon/v1/config/secret_backup_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `SecretBackupSettings`

**Imports** (4):

- `gcommon/v1/common/secret_backup_frequency.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/secret_backup_settings.proto
// version: 1.0.0
// guid: d6d87fc0-471b-4087-857b-33284c8b1765

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/secret_backup_frequency.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SecretBackupSettings {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup frequency
  gcommon.v1.common.SecretBackupFrequency frequency = 2;

  // Backup retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup storage location
  string storage_location = 4 [(buf.validate.field).string.min_len = 1];

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

### secret_validation_result.proto {#secret_validation_result}

**Path**: `gcommon/v1/config/secret_validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Messages** (1): `SecretValidationResult`

**Imports** (5):

- `gcommon/v1/common/secret_validation_result_type.proto`
- `gcommon/v1/common/secret_validation_severity.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_validation_result.proto
// version: 1.0.0
// guid: 59941566-6573-4333-bf99-4652471115b0

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/secret_validation_result_type.proto";
import "gcommon/v1/common/secret_validation_severity.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SecretValidationResult {
  // Validation name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Validation result
  gcommon.v1.common.SecretValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Validation severity
  gcommon.v1.common.SecretValidationSeverity severity = 4;

  // Validation timestamp
  google.protobuf.Timestamp timestamp = 5;

  // Validation details
  map<string, string> details = 6;
}
```

---

### sync_settings.proto {#sync_settings}

**Path**: `gcommon/v1/config/sync_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `SyncSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/sync_settings.proto
// version: 1.0.0
// guid: 4e62c57b-c2aa-4462-b51c-4077876bfb37

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SyncSettings {
  // Sync enabled
  bool enabled = 1;

  // Sync source
  string source = 2 [(buf.validate.field).string.min_len = 1];

  // Sync target
  string target = 3 [(buf.validate.field).string.min_len = 1];

  // Sync schedule
  string schedule = 4 [(buf.validate.field).string.min_len = 1];

  // Sync filters
  repeated string filters = 5 [(buf.validate.field).repeated.min_items = 1];

  // Sync transformations
  repeated string transformations = 6 [(buf.validate.field).repeated.min_items = 1];

  // Sync configuration
  map<string, string> config = 7;
}
```

---

### synchronization_settings.proto {#synchronization_settings}

**Path**: `gcommon/v1/config/synchronization_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `SynchronizationSettings`

**Imports** (5):

- `gcommon/v1/common/conflict_resolution.proto`
- `gcommon/v1/common/synchronization_frequency.proto`
- `gcommon/v1/config/synchronization_target.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/synchronization_settings.proto
// version: 1.0.0
// guid: e3f41f73-ecdc-4499-9a1a-8adc64cb1ed1

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/conflict_resolution.proto";
import "gcommon/v1/common/synchronization_frequency.proto";
import "gcommon/v1/config/synchronization_target.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SynchronizationSettings {
  // Whether synchronization is enabled
  bool enabled = 1;

  // Synchronization targets
  repeated gcommon.v1.config.SynchronizationTarget targets = 2 [(buf.validate.field).repeated.min_items = 1];

  // Synchronization frequency
  gcommon.v1.common.SynchronizationFrequency frequency = 3;

  // Synchronization conflict resolution
  gcommon.v1.common.ConflictResolution conflict_resolution = 4;

  // Synchronization metadata
  map<string, string> metadata = 5;
}
```

---

### synchronization_target.proto {#synchronization_target}

**Path**: `gcommon/v1/config/synchronization_target.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `SynchronizationTarget`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/synchronization_target.proto
// version: 1.0.0
// guid: cefe82ce-a5cb-44d8-a069-e773d0b9658d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message SynchronizationTarget {
  // Target name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Target type
  string type = 2;

  // Target configuration
  map<string, string> config = 3;

  // Target enabled
  bool enabled = 4;

  // Target priority
  int32 priority = 5;
}
```

---

### template_change.proto {#template_change}

**Path**: `gcommon/v1/config/template_change.proto` **Package**: `gcommon.v1.config` **Lines**: 41

**Messages** (1): `TemplateChange`

**Imports** (4):

- `gcommon/v1/common/config_change_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_change.proto
// version: 1.0.0
// guid: 801fc1c2-3a27-4a37-a1e2-0d540b0f4dd8

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_change_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message TemplateChange {
  // Change version
  string version = 1;

  // Change description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Change author
  string author = 3;

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Change type
  gcommon.v1.common.TemplateChangeType type = 5;

  // Breaking change flag
  bool breaking = 6;

  // Change details
  repeated string details = 7;

  // Migration notes
  string migration_notes = 8;
}
```

---

### template_hook.proto {#template_hook}

**Path**: `gcommon/v1/config/template_hook.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `TemplateHook`

**Imports** (4):

- `gcommon/v1/common/hook_error_handling.proto`
- `gcommon/v1/common/hook_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_hook.proto
// version: 1.0.0
// guid: 48a58147-b1e9-4c28-ad50-58952adc0ffe

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/hook_error_handling.proto";
import "gcommon/v1/common/hook_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message TemplateHook {
  // Hook name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Hook type
  gcommon.v1.common.HookType type = 2;

  // Hook command or script
  string command = 3;

  // Hook timeout
  int32 timeout_seconds = 4;

  // Hook working directory
  string working_directory = 5;

  // Hook environment variables
  map<string, string> environment = 6;

  // Hook conditions
  map<string, string> conditions = 7;

  // Hook error handling
  gcommon.v1.common.HookErrorHandling error_handling = 8;
}
```

---

### template_output.proto {#template_output}

**Path**: `gcommon/v1/config/template_output.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `TemplateOutput`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_output.proto
// version: 1.0.0
// guid: 579f8ac6-c06e-4a4f-9e96-232802698bc1

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message TemplateOutput {
  // Output name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Output description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Output type
  string type = 3;

  // Output value expression
  string value = 4;

  // Whether output is sensitive
  bool sensitive = 5;

  // Output group
  string group = 6;

  // Output format
  string format = 7;

  // Output examples
  repeated string examples = 8;
}
```

---

### transformation_settings.proto {#transformation_settings}

**Path**: `gcommon/v1/config/transformation_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `TransformationSettings`

**Imports** (3):

- `gcommon/v1/config/transformation_step.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/transformation_settings.proto
// version: 1.0.0
// guid: aadcd103-6f7c-4b6c-a58a-5c4ee2500cbf

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/transformation_step.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message TransformationSettings {
  // Whether transformation is enabled
  bool enabled = 1;

  // Transformation pipeline
  repeated TransformationStep pipeline = 2 [(buf.validate.field).repeated.min_items = 1];

  // Transformation on read
  bool transform_on_read = 3;

  // Transformation on write
  bool transform_on_write = 4;

  // Transformation metadata
  map<string, string> metadata = 5;
}
```

---

### transformation_step.proto {#transformation_step}

**Path**: `gcommon/v1/config/transformation_step.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `TransformationStep`

**Imports** (3):

- `gcommon/v1/common/transformation_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/transformation_step.proto
// version: 1.0.0
// guid: 4b3c1c96-82eb-4c1d-84ac-362e461d5793

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/transformation_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message TransformationStep {
  // Step name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Step type
  gcommon.v1.common.TransformationType type = 2;

  // Step expression
  string expression = 3;

  // Step parameters
  map<string, string> parameters = 4;

  // Step enabled
  bool enabled = 5;

  // Step order
  int32 order = 6;
}
```

---

### usage_statistics.proto {#usage_statistics}

**Path**: `gcommon/v1/config/usage_statistics.proto` **Package**: `gcommon.v1.config` **Lines**: 48

**Messages** (1): `UsageStatistics`

**Imports** (4):

- `gcommon/v1/config/usage_trend.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/usage_statistics.proto
// version: 1.0.0
// guid: cc21dcd3-5d5b-42a8-9602-b3b08c2ff649

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/usage_trend.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message UsageStatistics {
  // Total access count
  int64 total_access_count = 1 [(buf.validate.field).int64.gte = 0];

  // Access count in last 24 hours
  int64 access_count_24h = 2 [(buf.validate.field).int64.gte = 0];

  // Access count in last 7 days
  int64 access_count_7d = 3 [(buf.validate.field).int64.gte = 0];

  // Access count in last 30 days
  int64 access_count_30d = 4 [(buf.validate.field).int64.gte = 0];

  // Unique users count
  int64 unique_users_count = 5 [(buf.validate.field).int64.gte = 0];

  // Unique services count
  int64 unique_services_count = 6 [(buf.validate.field).int64.gte = 0];

  // Average access frequency per day
  double avg_access_frequency = 7 [(buf.validate.field).double.gte = 0.0];

  // Peak access timestamp
  google.protobuf.Timestamp peak_access_at = 8;

  // Peak access count
  int64 peak_access_count = 9 [(buf.validate.field).int64.gte = 0];

  // Usage trends
  repeated gcommon.v1.config.UsageTrend trends = 10 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### usage_trend.proto {#usage_trend}

**Path**: `gcommon/v1/config/usage_trend.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Messages** (1): `UsageTrend`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/usage_trend.proto
// version: 1.0.0
// guid: d9e0f1a2-3456-789a-3456-901234567890

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message UsageTrend {
  // Timestamp
  google.protobuf.Timestamp timestamp = 1;

  // Usage count
  int64 usage_count = 2 [(buf.validate.field).int64.gte = 0];

  // Trend direction
  string direction = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### validation_result.proto {#validation_result}

**Path**: `gcommon/v1/config/validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `ConfigValidationResult`

**Imports** (4):

- `gcommon/v1/common/validation_result_type.proto`
- `gcommon/v1/common/validation_severity.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_result.proto
// version: 1.0.0
// guid: 24d2ce27-6b21-4f7b-82f6-2a7b060fe004

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/validation_result_type.proto";
import "gcommon/v1/common/validation_severity.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigValidationResult {
  // Validation rule name
  string rule_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Validation result
  gcommon.v1.common.ValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Severity level
  gcommon.v1.common.ValidationSeverity severity = 4;

  // Field that was validated
  string field = 5;

  // Additional context
  map<string, string> context = 6;
}
```

---

### validation_rule.proto {#validation_rule}

**Path**: `gcommon/v1/config/validation_rule.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `ValidationRule`

**Imports** (3):

- `gcommon/v1/common/validation_severity.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_rule.proto
// version: 1.0.0
// guid: 6cc709c2-996e-4e1c-aa4d-0c7741fadb21

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/validation_severity.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValidationRule {
  // Rule name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Rule description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Rule expression
  string expression = 3;

  // Error message if validation fails
  string error_message = 4;

  // Rule severity
  gcommon.v1.common.ValidationSeverity severity = 5;

  // Parameters this rule applies to
  repeated string parameters = 6;

  // Rule conditions
  map<string, string> conditions = 7;
}
```

---

### validation_settings.proto {#validation_settings}

**Path**: `gcommon/v1/config/validation_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Messages** (1): `ValidationSettings`

**Imports** (4):

- `gcommon/v1/common/config_retry_settings.proto`
- `gcommon/v1/config/validation_rule.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/validation_settings.proto
// version: 1.0.0
// guid: b6a8294f-3f5c-4bcc-95ad-9369bd1addd5

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_retry_settings.proto";
import "gcommon/v1/config/validation_rule.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValidationSettings {
  // Whether validation is enabled
  bool enabled = 1;

  // Validation rules (using ValidationRule from config_template.proto)
  repeated ValidationRule rules = 2 [(buf.validate.field).repeated.min_items = 1];

  // Validation on change
  bool validate_on_change = 3;

  // Validation on access
  bool validate_on_access = 4;

  // Validation timeout in seconds
  int32 timeout_seconds = 5 [(buf.validate.field).int32.gt = 0];

  // Validation retry settings
  gcommon.v1.common.ConfigRetrySettings retry = 6;

  // Validation metadata
  map<string, string> metadata = 7;
}
```

---

### value_dependency.proto {#value_dependency}

**Path**: `gcommon/v1/config/value_dependency.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `ValueDependency`

**Imports** (3):

- `gcommon/v1/common/dependency_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_dependency.proto
// version: 1.0.0
// guid: ceefe5a4-8fbf-4555-9535-c57437357bef

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/dependency_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueDependency {
  // Dependency type
  gcommon.v1.common.DependencyType type = 1;

  // Dependent value key
  string dependent_key = 2 [(buf.validate.field).string.min_len = 1];

  // Dependency key
  string dependency_key = 3 [(buf.validate.field).string.min_len = 1];

  // Dependency condition
  string condition = 4 [(buf.validate.field).string.min_len = 1];

  // Dependency metadata
  map<string, string> metadata = 5;
}
```

---

### value_history_entry.proto {#value_history_entry}

**Path**: `gcommon/v1/config/value_history_entry.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `ValueHistoryEntry`

**Imports** (4):

- `gcommon/v1/common/config_change_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_history_entry.proto
// version: 1.0.0
// guid: 842c89c0-e045-4b46-8c03-f19d4383edb0

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/config_change_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueHistoryEntry {
  // Entry ID
  string entry_id = 1 [(buf.validate.field).string.min_len = 1];

  // Previous value
  string previous_value = 2 [(buf.validate.field).string.min_len = 1];

  // New value
  string new_value = 3 [(buf.validate.field).string.min_len = 1];

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;

  // User who made the change
  string changed_by = 5 [(buf.validate.field).string.min_len = 1];

  // Change reason
  string reason = 6 [(buf.validate.field).string.min_len = 1];

  // Change type (using ChangeType from config_template.proto)
  gcommon.v1.common.TemplateChangeType change_type = 7;

  // Change metadata
  map<string, string> metadata = 8;
}
```

---

### value_reference.proto {#value_reference}

**Path**: `gcommon/v1/config/value_reference.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `ValueReference`

**Imports** (3):

- `gcommon/v1/common/reference_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_reference.proto
// version: 1.0.0
// guid: b56910e9-5a31-46b6-b2ac-3c854f87e332

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/reference_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueReference {
  // Reference type
  gcommon.v1.common.ReferenceType type = 1;

  // Referenced value key
  string referenced_key = 2 [(buf.validate.field).string.min_len = 1];

  // Reference path
  string path = 3 [(buf.validate.field).string.min_len = 1];

  // Reference metadata
  map<string, string> metadata = 4;
}
```

---

### value_usage_statistics.proto {#value_usage_statistics}

**Path**: `gcommon/v1/config/value_usage_statistics.proto` **Package**: `gcommon.v1.config` **Lines**: 51

**Messages** (1): `ValueUsageStatistics`

**Imports** (4):

- `gcommon/v1/config/value_usage_trend.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_usage_statistics.proto
// version: 1.0.0
// guid: 3e5f0d64-7329-474a-9bd9-17d7f8fdf4b5

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/value_usage_trend.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueUsageStatistics {
  // Total read count
  int64 read_count = 1 [(buf.validate.field).int64.gte = 0];

  // Total write count
  int64 write_count = 2 [(buf.validate.field).int64.gte = 0];

  // Last read timestamp
  google.protobuf.Timestamp last_read_at = 3;

  // Last write timestamp
  google.protobuf.Timestamp last_written_at = 4;

  // Read frequency (reads per day)
  double read_frequency = 5 [(buf.validate.field).double.gte = 0.0];

  // Write frequency (writes per day)
  double write_frequency = 6 [(buf.validate.field).double.gte = 0.0];

  // Unique readers count
  int64 unique_readers = 7 [(buf.validate.field).int64.gte = 0];

  // Unique writers count
  int64 unique_writers = 8 [(buf.validate.field).int64.gte = 0];

  // Peak usage timestamp
  google.protobuf.Timestamp peak_usage_at = 9;

  // Peak usage count
  int64 peak_usage_count = 10 [(buf.validate.field).int64.gte = 0];

  // Usage trends
  repeated gcommon.v1.config.ValueUsageTrend trends = 11 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### value_usage_trend.proto {#value_usage_trend}

**Path**: `gcommon/v1/config/value_usage_trend.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `ValueUsageTrend`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_usage_trend.proto
// version: 1.0.0
// guid: 77c2eae0-a102-4079-971c-4294d89bef5d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueUsageTrend {
  // Trend period
  string period = 1 [(buf.validate.field).string.min_len = 1];

  // Read count
  int64 read_count = 2 [(buf.validate.field).int64.gte = 0];

  // Write count
  int64 write_count = 3 [(buf.validate.field).int64.gte = 0];

  // Trend timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Trend metadata
  map<string, string> metadata = 5;
}
```

---

### value_validation_result.proto {#value_validation_result}

**Path**: `gcommon/v1/config/value_validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 45

**Messages** (1): `ValueValidationResult`

**Imports** (5):

- `gcommon/v1/common/value_validation_result_type.proto`
- `gcommon/v1/common/value_validation_severity.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_validation_result.proto
// version: 1.0.0
// guid: 01a83346-1423-44d3-a9c9-c97dc0cb3f4f

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/value_validation_result_type.proto";
import "gcommon/v1/common/value_validation_severity.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ValueValidationResult {
  // Validation name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Validation result
  gcommon.v1.common.ValueValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Validation severity
  gcommon.v1.common.ValueValidationSeverity severity = 4;

  // Validation timestamp
  google.protobuf.Timestamp timestamp = 5;

  // Validation details
  map<string, string> details = 6;

  // Validation rule
  string rule = 7;

  // Validation context
  string context = 8;
}
```

---

### version_artifact.proto {#version_artifact}

**Path**: `gcommon/v1/config/version_artifact.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `VersionArtifact`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_artifact.proto
// version: 1.0.0
// guid: 7cbe5a72-963f-4b03-b61e-7cd392e571c8

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionArtifact {
  // Artifact name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Artifact type
  string type = 2;

  // Artifact path
  string path = 3;

  // Artifact size
  int64 size = 4;

  // Artifact checksum
  string checksum = 5;

  // Artifact metadata
  map<string, string> metadata = 6;

  // Artifact timestamp
  google.protobuf.Timestamp timestamp = 7;
}
```

---

### version_compatibility_info.proto {#version_compatibility_info}

**Path**: `gcommon/v1/config/version_compatibility_info.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `VersionCompatibilityInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_compatibility_info.proto
// version: 1.0.0
// guid: bdb10c96-0338-4ab3-877b-f10ea821efe9

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionCompatibilityInfo {
  // Backward compatible
  bool backward_compatible = 1;

  // Forward compatible
  bool forward_compatible = 2;

  // Breaking changes
  repeated string breaking_changes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Compatibility notes
  string notes = 4 [(buf.validate.field).string.min_len = 1];

  // Minimum version
  string min_version = 5 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Maximum version
  string max_version = 6 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Deprecated features
  repeated string deprecated_features = 7 [(buf.validate.field).repeated.min_items = 1];

  // Migration guide
  string migration_guide = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### version_dependency.proto {#version_dependency}

**Path**: `gcommon/v1/config/version_dependency.proto` **Package**: `gcommon.v1.config` **Lines**: 39

**Messages** (1): `VersionDependency`

**Imports** (3):

- `gcommon/v1/common/version_dependency_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_dependency.proto
// version: 1.0.0
// guid: c6e48e5f-19bf-49eb-ae5b-2360c1e11fe1

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/version_dependency_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionDependency {
  // Dependency name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Dependency version
  string version = 2;

  // Dependency type
  gcommon.v1.common.VersionDependencyType type = 3;

  // Dependency scope
  string scope = 4;

  // Dependency bool optional = 5;

  // Dependency constraints
  repeated string constraints = 6;

  // Dependency metadata
  map<string, string> metadata = 7;
}
```

---

### version_deployment_info.proto {#version_deployment_info}

**Path**: `gcommon/v1/config/version_deployment_info.proto` **Package**: `gcommon.v1.config` **Lines**: 46

**Messages** (1): `VersionDeploymentInfo`

**Imports** (5):

- `gcommon/v1/common/version_deployment_status.proto`
- `gcommon/v1/common/version_health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_deployment_info.proto
// version: 1.0.0
// guid: 194328f1-30ba-459e-b106-f6b99ece3ee3

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/version_deployment_status.proto";
import "gcommon/v1/common/version_health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionDeploymentInfo {
  // Deployment status
  gcommon.v1.common.VersionDeploymentStatus status = 1;

  // Deployment timestamp
  google.protobuf.Timestamp deployed_at = 2;

  // Deployment environment
  string environment = 3 [(buf.validate.field).string.min_len = 1];

  // Deployment method
  string method = 4 [(buf.validate.field).string.min_len = 1];

  // Deployment user
  string deployed_by = 5 [(buf.validate.field).string.min_len = 1];

  // Deployment configuration
  map<string, string> config = 6;

  // Deployment artifacts
  repeated string artifacts = 7 [(buf.validate.field).repeated.min_items = 1];

  // Deployment health
  gcommon.v1.common.VersionHealthStatus health = 8;

  // Deployment metrics
  map<string, double> metrics = 9;
}
```

---

### version_quality_issue.proto {#version_quality_issue}

**Path**: `gcommon/v1/config/version_quality_issue.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `VersionQualityIssue`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_quality_issue.proto
// version: 1.0.0
// guid: 98aad520-640b-4663-a48a-ec3928c41c6a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionQualityIssue {
  // Issue type
  string type = 1;

  // Issue severity
  string severity = 2;

  // Issue description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Issue location
  string location = 4;

  // Issue rule
  string rule = 5;

  // Issue fix suggestion
  string fix_suggestion = 6;
}
```

---

### version_quality_metrics.proto {#version_quality_metrics}

**Path**: `gcommon/v1/config/version_quality_metrics.proto` **Package**: `gcommon.v1.config` **Lines**: 45

**Messages** (1): `VersionQualityMetrics`

**Imports** (4):

- `gcommon/v1/config/version_quality_issue.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_quality_metrics.proto
// version: 1.0.0
// guid: 2326770b-b97a-4a96-93aa-b093931437a7

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/config/version_quality_issue.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionQualityMetrics {
  // Code quality score
  double quality_score = 1 [(buf.validate.field).double.gte = 0.0];

  // Test coverage
  double test_coverage = 2 [(buf.validate.field).double.gte = 0.0];

  // Security score
  double security_score = 3 [(buf.validate.field).double.gte = 0.0];

  // Performance score
  double performance_score = 4 [(buf.validate.field).double.gte = 0.0];

  // Complexity score
  double complexity_score = 5 [(buf.validate.field).double.gte = 0.0];

  // Technical debt score
  double technical_debt_score = 6 [(buf.validate.field).double.gte = 0.0];

  // Quality gate status
  bool quality_gate_passed = 7;

  // Quality issues
  repeated VersionQualityIssue issues = 8 [(buf.validate.field).repeated.min_items = 1];

  // Quality metrics timestamp
  google.protobuf.Timestamp timestamp = 9;
}
```

---

### versioning_settings.proto {#versioning_settings}

**Path**: `gcommon/v1/config/versioning_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Messages** (1): `VersioningSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/versioning_settings.proto
// version: 1.0.0
// guid: 8ed86af7-67dd-4efb-abe6-bd383a4a4720

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersioningSettings {
  // Whether versioning is enabled
  bool enabled = 1;

  // Maximum number of versions to keep
  int32 max_versions = 2 [(buf.validate.field).int32.gte = 0];

  // Version retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Whether to create versions on change
  bool version_on_change = 4;

  // Whether to create versions on schedule
  bool version_on_schedule = 5;

  // Versioning schedule
  string schedule = 6 [(buf.validate.field).string.min_len = 1];

  // Version metadata
  map<string, string> metadata = 7;
}
```

---

### backup_policy.proto {#backup_policy}

**Path**: `gcommon/v1/config/backup_policy.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `BackupPolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/backup_policy.proto
// version: 1.0.0
// guid: 900e85e2-21f2-4656-84f5-61f198cb79c7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message BackupPolicy {
  // Backup enabled
  bool enabled = 1;

  // Backup schedule
  string schedule = 2 [(buf.validate.field).string.min_len = 1];

  // Backup retention
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup location
  string location = 4 [(buf.validate.field).string.min_len = 1];

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup verification
  bool verified = 7;

  // Backup metadata
  map<string, string> metadata = 8;
}
```

---

### backup_settings.proto {#backup_settings}

**Path**: `gcommon/v1/config/backup_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `BackupSettings`

**Imports** (3):

- `gcommon/v1/common/backup_frequency.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/backup_settings.proto
// version: 1.0.0
// guid: e9a07253-25f8-4306-ad78-31325ce9b271

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/backup_frequency.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message BackupSettings {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup frequency
  gcommon.v1.common.BackupFrequency frequency = 2;

  // Backup retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup storage location
  string storage_location = 4 [(buf.validate.field).string.min_len = 1];

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup metadata
  map<string, string> metadata = 7;
}
```

---

### get_schema_request.proto {#get_schema_request}

**Path**: `gcommon/v1/config/get_schema_request.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `GetSchemaRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/get_schema_request.proto
// version: 1.0.0
// guid: 418bff8d-7263-433a-84b5-c063a0a393fa
// file: proto/gcommon/v1/config/get_schema_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message GetSchemaRequest {
  // Schema name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_schema_response.proto {#get_schema_response}

**Path**: `gcommon/v1/config/get_schema_response.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Messages** (1): `GetSchemaResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/config/config_schema.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_schema_response.proto
// version: 1.0.1
// guid: 814082ea-43bd-4fe6-9f69-3e587af7e038
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/config/config_schema.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * GetSchemaResponse returns a configuration schema.
 */
message GetSchemaResponse {
  // Configuration schema
  ConfigSchema schema = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/config/health_check_request.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `ConfigHealthCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_request.proto
// version: 1.0.0
// guid: bb4a27ef-7b1e-4a20-937c-7366e3be5b6f
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

message ConfigHealthCheckRequest {
  // Target namespace to check
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/config/health_check_response.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Messages** (1): `ConfigHealthCheckResponse`

**Imports** (3):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_response.proto
// version: 1.0.0
// guid: 4f491273-ecd5-4d3c-b13d-b7ef6219a25d

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * HealthCheckResponse provides health status for the config service.
 */
message ConfigHealthCheckResponse {
  // Overall health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Optional human-readable message
  string message = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### rollback_info.proto {#rollback_info}

**Path**: `gcommon/v1/config/rollback_info.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `RollbackInfo`

**Imports** (3):

- `gcommon/v1/common/rollback_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rollback_info.proto
// version: 1.0.0
// guid: 20b0233a-770b-4484-a066-948c77afc78e

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/rollback_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RollbackInfo {
  // Original audit entry being rolled back
  string original_audit_id = 1 [(buf.validate.field).string.min_len = 1];

  // Rollback reason
  string reason = 2 [(buf.validate.field).string.min_len = 1];

  // Rollback method
  gcommon.v1.common.RollbackMethod method = 3;

  // Target version for rollback
  string target_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Whether rollback was automatic
  bool automatic = 5;
}
```

---

### config_watch_event.proto {#config_watch_event}

**Path**: `gcommon/v1/config/config_watch_event.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `ConfigWatchEvent`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_watch_event.proto
// version: 1.0.0
// guid: 218de9f4-02fd-4c68-acb9-0f549a1cfd06

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigWatchEvent {
  // Watch session identifier
  string watch_id = 1 [(buf.validate.field).string.min_len = 1];

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

  // Configuration namespace or section
  string namespace = 7 [(buf.validate.field).string.min_len = 1];

  // Additional event metadata
  map<string, string> metadata = 8;
}
```

---

### rotation_event.proto {#rotation_event}

**Path**: `gcommon/v1/config/rotation_event.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `RotationEvent`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rotation_event.proto
// version: 1.0.0
// guid: b7c8d9e0-1f23-4567-1234-789012345678

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RotationEvent {
  // Event ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Rotation timestamp
  google.protobuf.Timestamp timestamp = 2;

  // Previous value
  string previous_value = 3;

  // New value
  string new_value = 4;

  // Rotation reason
  string reason = 5;
}
```

---

### version_promotion_event.proto {#version_promotion_event}

**Path**: `gcommon/v1/config/version_promotion_event.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `VersionPromotionEvent`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_promotion_event.proto
// version: 1.0.0
// guid: d231a04f-95ab-4854-a15d-7992ab883362

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionPromotionEvent {
  // Source environment
  string source_environment = 1 [(buf.validate.field).string.min_len = 1];

  // Target environment
  string target_environment = 2 [(buf.validate.field).string.min_len = 1];

  // Promotion timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Promotion user
  string promoted_by = 4 [(buf.validate.field).string.min_len = 1];

  // Promotion reason
  string reason = 5 [(buf.validate.field).string.min_len = 1];

  // Promotion method
  string method = 6 [(buf.validate.field).string.min_len = 1];

  // Promotion success
  bool success = 7;

  // Promotion error
  string error = 8 [(buf.validate.field).string.min_len = 1];

  // Promotion metadata
  map<string, string> metadata = 9;
}
```

---

