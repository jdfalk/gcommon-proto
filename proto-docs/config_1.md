# config_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 14
- **Services**: 0
- **Enums**: 36

## Files in this Module

- [access_control.proto](#access_control)
- [access_restriction.proto](#access_restriction)
- [alert_severity.proto](#alert_severity)
- [alert_type.proto](#alert_type)
- [approval_info.proto](#approval_info)
- [approval_requirement.proto](#approval_requirement)
- [approval_status.proto](#approval_status)
- [backoff_strategy.proto](#backoff_strategy)
- [backup_frequency.proto](#backup_frequency)
- [cache_invalidation_trigger.proto](#cache_invalidation_trigger)
- [cache_refresh_strategy.proto](#cache_refresh_strategy)
- [change_type.proto](#change_type)
- [channel_type.proto](#channel_type)
- [compliance_reporting.proto](#compliance_reporting)
- [compression_type.proto](#compression_type)
- [conflict_resolution.proto](#conflict_resolution)
- [dependency_type.proto](#dependency_type)
- [deployment_status.proto](#deployment_status)
- [deprecation_info.proto](#deprecation_info)
- [deprecation_level.proto](#deprecation_level)
- [environment_status.proto](#environment_status)
- [environment_type.proto](#environment_type)
- [filter_action.proto](#filter_action)
- [filter_type.proto](#filter_type)
- [health_check_type.proto](#health_check_type)
- [health_state.proto](#health_state)
- [hook_error_handling.proto](#hook_error_handling)
- [hook_type.proto](#hook_type)
- [inheritance_filter.proto](#inheritance_filter)
- [inheritance_strategy.proto](#inheritance_strategy)
- [inheritance_transformation.proto](#inheritance_transformation)
- [merge_strategy.proto](#merge_strategy)
- [metadata_status.proto](#metadata_status)
- [monitoring_alert.proto](#monitoring_alert)
- [notification_channel.proto](#notification_channel)
- [notification_trigger.proto](#notification_trigger)
- [parameter_constraints.proto](#parameter_constraints)
- [parameter_type.proto](#parameter_type)
- [rate_limits.proto](#rate_limits)
- [reference_type.proto](#reference_type)
- [restore_point_status.proto](#restore_point_status)
- [restore_point_type.proto](#restore_point_type)
- [restriction_type.proto](#restriction_type)
- [rollback_info.proto](#rollback_info)
- [rollback_method.proto](#rollback_method)
- [rotation_frequency.proto](#rotation_frequency)
- [secret_backup_frequency.proto](#secret_backup_frequency)
- [secret_status.proto](#secret_status)
- [secret_type.proto](#secret_type)
- [secret_validation_result.proto](#secret_validation_result)

## Module Dependencies

**This module depends on**:

- [config_2](./config_2.md)
- [config_config_1](./config_config_1.md)
- [config_events](./config_events.md)
- [log](./log.md)

**Modules that depend on this one**:

- [config_2](./config_2.md)
- [config_config_1](./config_config_1.md)
- [config_config_2](./config_config_2.md)
- [metrics_1](./metrics_1.md)
- [metrics_config](./metrics_config.md)
- [queue_1](./queue_1.md)
- [queue_config](./queue_config.md)
- [web_config_1](./web_config_1.md)

---

## Detailed Documentation

### access_control.proto {#access_control}

**Path**: `pkg/config/proto/access_control.proto` **Package**: `gcommon.v1.config` **Lines**: 48

**Messages** (1): `AccessControl`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/access_restriction.proto`
- `pkg/config/proto/rate_limits.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/access_control.proto
// version: 1.0.0
// guid: 5707e31a-b72e-4cc1-b3ba-87269e99e05b

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/access_restriction.proto";
import "pkg/config/proto/rate_limits.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message AccessControl {
  // Access policy
  string policy = 1;

  // Allowed users
  repeated string allowed_users = 2;

  // Allowed roles
  repeated string allowed_roles = 3;

  // Allowed services
  repeated string allowed_services = 4;

  // Allowed environments
  repeated string allowed_environments = 5;

  // Access restrictions
  repeated AccessRestriction restrictions = 6;

  // Maximum access count
  int32 max_access_count = 7;

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

**Path**: `pkg/config/proto/access_restriction.proto` **Package**: `gcommon.v1.config` **Lines**: 29

**Messages** (1): `AccessRestriction`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/restriction_type.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/access_restriction.proto
// version: 1.0.0
// guid: cfdd7cdc-6bb3-4b8f-b3a9-fa8a84cc84ad

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/restriction_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message AccessRestriction {
  // Restriction type
  RestrictionType type = 1;

  // Restriction value
  string value = 2;

  // Restriction operator
  string operator = 3;

  // Restriction reason
  string reason = 4;
}

```

---

### alert_severity.proto {#alert_severity}

**Path**: `pkg/config/proto/alert_severity.proto` **Package**: `gcommon.v1.config` **Lines**: 21

**Enums** (1): `AlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/alert_severity.proto
// version: 1.0.0
// guid: e4538794-5759-4c3f-a3ed-b3794a014e86

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum AlertSeverity {
  ALERT_SEVERITY_UNSPECIFIED = 0;
  ALERT_SEVERITY_LOW = 1;
  ALERT_SEVERITY_MEDIUM = 2;
  ALERT_SEVERITY_HIGH = 3;
  ALERT_SEVERITY_CRITICAL = 4;
}

```

---

### alert_type.proto {#alert_type}

**Path**: `pkg/config/proto/alert_type.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `AlertType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/alert_type.proto
// version: 1.0.0
// guid: 54407766-3304-4e90-90d6-973ac6ff0fc3

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum AlertType {
  ALERT_TYPE_UNSPECIFIED = 0;
  ALERT_TYPE_EXPIRATION = 1;
  ALERT_TYPE_ACCESS_ANOMALY = 2;
  ALERT_TYPE_FAILED_ACCESS = 3;
  ALERT_TYPE_ROTATION_FAILURE = 4;
  ALERT_TYPE_BACKUP_FAILURE = 5;
  ALERT_TYPE_COMPLIANCE_VIOLATION = 6;
  ALERT_TYPE_SECURITY_INCIDENT = 7;
}

```

---

### approval_info.proto {#approval_info}

**Path**: `pkg/config/proto/approval_info.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `ApprovalInfo`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/approval_status.proto`
- `pkg/config/proto/audit_operation_type.proto` → [config_events](./config_events.md#audit_operation_type)
- `pkg/config/proto/rollback_method.proto`
- `pkg/config/proto/validation_result_type.proto` → [config_2](./config_2.md#validation_result_type)
- `pkg/config/proto/validation_severity.proto` → [config_2](./config_2.md#validation_severity)

#### Source Code

```protobuf
// file: pkg/config/proto/approval_info.proto
// version: 1.0.0
// guid: 28dbf45a-ffed-40b5-8bad-30879b48ddcd

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/approval_status.proto";
import "pkg/config/proto/audit_operation_type.proto";
import "pkg/config/proto/rollback_method.proto";
import "pkg/config/proto/validation_result_type.proto";
import "pkg/config/proto/validation_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ApprovalInfo {
  // Whether approval was required
  bool required = 1;

  // Approval status
  ApprovalStatus status = 2;

  // User who approved
  string approved_by = 3;

  // Approval timestamp
  google.protobuf.Timestamp approved_at = 4;

  // Approval comments
  string comments = 5;

  // Approval workflow ID
  string workflow_id = 6;

  // Approval policy applied
  string policy_name = 7;
}

```

---

### approval_requirement.proto {#approval_requirement}

**Path**: `pkg/config/proto/approval_requirement.proto` **Package**: `gcommon.v1.config` **Lines**: 47

**Messages** (1): `ApprovalRequirement`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` → [config_events](./config_events.md#audit_level)
- `pkg/config/proto/backup_frequency.proto`
- `pkg/config/proto/channel_type.proto`
- `pkg/config/proto/config_data_type.proto` → [config_config_1](./config_config_1.md#config_data_type)
- `pkg/config/proto/deprecation_level.proto`
- `pkg/config/proto/metadata_status.proto`
- `pkg/config/proto/notification_trigger.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/approval_requirement.proto
// version: 1.0.0
// guid: 54ae6b55-a574-4ad5-89ea-9cadf541517a

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

message ApprovalRequirement {
  // Whether approval is required
  bool required = 1;

  // Number of approvals required
  int32 approval_count = 2;

  // Required approver roles
  repeated string approver_roles = 3;

  // Required approver users
  repeated string approver_users = 4;

  // Approval policy
  string policy = 5;

  // Approval workflow
  string workflow = 6;

  // Auto-approval conditions
  repeated string auto_approval_conditions = 7;

  // Approval timeout
  int32 approval_timeout_hours = 8;
}

```

---

### approval_status.proto {#approval_status}

**Path**: `pkg/config/proto/approval_status.proto` **Package**: `gcommon.v1.config` **Lines**: 37

**Enums** (1): `ApprovalStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/approval_status.proto
// version: 1.0.0
// guid: a9b0c1d2-e3f4-5a6b-7c8d-9e0f1a2b3c4d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ApprovalStatus represents the approval status.
 * Specifies the current state of configuration change approval.
 */
enum ApprovalStatus {
  // Unspecified approval status
  APPROVAL_STATUS_UNSPECIFIED = 0;

  // Approval is pending
  APPROVAL_STATUS_PENDING = 1;

  // Change has been approved
  APPROVAL_STATUS_APPROVED = 2;

  // Change has been rejected
  APPROVAL_STATUS_REJECTED = 3;

  // Approval was cancelled
  APPROVAL_STATUS_CANCELLED = 4;

  // Approval request expired
  APPROVAL_STATUS_EXPIRED = 5;
}

```

---

### backoff_strategy.proto {#backoff_strategy}

**Path**: `pkg/config/proto/backoff_strategy.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `BackoffStrategy`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/backoff_strategy.proto
// version: 1.0.0
// guid: 5aec3abd-38af-4436-a59a-c4140f44a461

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum BackoffStrategy {
  BACKOFF_STRATEGY_UNSPECIFIED = 0;
  BACKOFF_STRATEGY_FIXED = 1;
  BACKOFF_STRATEGY_LINEAR = 2;
  BACKOFF_STRATEGY_EXPONENTIAL = 3;
  BACKOFF_STRATEGY_CUSTOM = 4;
}

```

---

### backup_frequency.proto {#backup_frequency}

**Path**: `pkg/config/proto/backup_frequency.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `BackupFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/backup_frequency.proto
// version: 1.0.0
// guid: 4efc5d0f-be87-47e1-8f01-f42fa2926368

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum BackupFrequency {
  BACKUP_FREQUENCY_UNSPECIFIED = 0;
  BACKUP_FREQUENCY_MANUAL = 1;
  BACKUP_FREQUENCY_HOURLY = 2;
  BACKUP_FREQUENCY_DAILY = 3;
  BACKUP_FREQUENCY_WEEKLY = 4;
  BACKUP_FREQUENCY_MONTHLY = 5;
  BACKUP_FREQUENCY_ON_CHANGE = 6;
}

```

---

### cache_invalidation_trigger.proto {#cache_invalidation_trigger}

**Path**: `pkg/config/proto/cache_invalidation_trigger.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `CacheInvalidationTrigger`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/cache_invalidation_trigger.proto
// version: 1.0.0
// guid: b09e744e-1475-4fcb-a8cc-0d121530e6b7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum CacheInvalidationTrigger {
  CACHE_INVALIDATION_TRIGGER_UNSPECIFIED = 0;
  CACHE_INVALIDATION_TRIGGER_CHANGE = 1;
  CACHE_INVALIDATION_TRIGGER_DELETE = 2;
  CACHE_INVALIDATION_TRIGGER_EXPIRE = 3;
  CACHE_INVALIDATION_TRIGGER_MANUAL = 4;
  CACHE_INVALIDATION_TRIGGER_SCHEDULE = 5;
}

```

---

### cache_refresh_strategy.proto {#cache_refresh_strategy}

**Path**: `pkg/config/proto/cache_refresh_strategy.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `CacheRefreshStrategy`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/cache_refresh_strategy.proto
// version: 1.0.0
// guid: c38dfb62-6d18-4f59-a901-6c4b5e659952

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum CacheRefreshStrategy {
  CACHE_REFRESH_STRATEGY_UNSPECIFIED = 0;
  CACHE_REFRESH_STRATEGY_TTL = 1;
  CACHE_REFRESH_STRATEGY_LAZY = 2;
  CACHE_REFRESH_STRATEGY_PROACTIVE = 3;
  CACHE_REFRESH_STRATEGY_BACKGROUND = 4;
}

```

---

### change_type.proto {#change_type}

**Path**: `pkg/config/proto/change_type.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `ChangeType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/change_type.proto
// version: 1.0.0
// guid: 0e330584-b155-45f0-8c79-0aa19e9aa30e

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ChangeType {
  CHANGE_TYPE_UNSPECIFIED = 0;
  CHANGE_TYPE_FEATURE = 1;
  CHANGE_TYPE_BUGFIX = 2;
  CHANGE_TYPE_ENHANCEMENT = 3;
  CHANGE_TYPE_DEPRECATED = 4;
  CHANGE_TYPE_SECURITY = 5;
  CHANGE_TYPE_BREAKING = 6;
}

```

---

### channel_type.proto {#channel_type}

**Path**: `pkg/config/proto/channel_type.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `ChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/channel_type.proto
// version: 1.0.0
// guid: 6f6a3985-1560-40b0-b6d5-b2985349b649

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ChannelType {
  CHANNEL_TYPE_UNSPECIFIED = 0;
  CHANNEL_TYPE_EMAIL = 1;
  CHANNEL_TYPE_SLACK = 2;
  CHANNEL_TYPE_WEBHOOK = 3;
  CHANNEL_TYPE_SMS = 4;
  CHANNEL_TYPE_PAGERDUTY = 5;
  CHANNEL_TYPE_TEAMS = 6;
  CHANNEL_TYPE_DISCORD = 7;
  CHANNEL_TYPE_JIRA = 8;
}

```

---

### compliance_reporting.proto {#compliance_reporting}

**Path**: `pkg/config/proto/compliance_reporting.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Messages** (1): `ComplianceReporting`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/compliance_reporting.proto
// version: 1.0.0
// guid: e4f5a6b7-8c9d-0123-ef01-456789012345

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceReporting {
  // Reporting enabled status
  bool enabled = 1;

  // Report frequency in hours
  int32 frequency_hours = 2;

  // Report recipients
  repeated string recipients = 3;
}

```

---

### compression_type.proto {#compression_type}

**Path**: `pkg/config/proto/compression_type.proto` **Package**: `gcommon.v1.config` **Lines**: 22

**Enums** (1): `CompressionType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/compression_type.proto
// version: 1.0.0
// guid: 78a4e05d-1bca-4728-ae76-18aba9fd52d8

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum CompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  COMPRESSION_TYPE_NONE = 1;
  COMPRESSION_TYPE_GZIP = 2;
  COMPRESSION_TYPE_LZ4 = 3;
  COMPRESSION_TYPE_ZSTD = 4;
}

```

---

### conflict_resolution.proto {#conflict_resolution}

**Path**: `pkg/config/proto/conflict_resolution.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `ConflictResolution`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/conflict_resolution.proto
// version: 1.0.0
// guid: 8535d30e-d232-4d73-9362-10e717955b66

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ConflictResolution {
  CONFLICT_RESOLUTION_UNSPECIFIED = 0;
  CONFLICT_RESOLUTION_SOURCE_WINS = 1;
  CONFLICT_RESOLUTION_TARGET_WINS = 2;
  CONFLICT_RESOLUTION_MERGE = 3;
  CONFLICT_RESOLUTION_MANUAL = 4;
  CONFLICT_RESOLUTION_TIMESTAMP = 5;
}

```

---

### dependency_type.proto {#dependency_type}

**Path**: `pkg/config/proto/dependency_type.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `DependencyType`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/dependency_type.proto
// version: 1.0.0
// guid: 0dbbaf99-12ad-49af-8747-0eb055671d35

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum DependencyType {
  DEPENDENCY_TYPE_UNSPECIFIED = 0;
  DEPENDENCY_TYPE_REQUIRED = 1;
  DEPENDENCY_TYPE_OPTIONAL = 2;
  DEPENDENCY_TYPE_CONDITIONAL = 3;
  DEPENDENCY_TYPE_DERIVED = 4;
  DEPENDENCY_TYPE_CONFLICT = 5;
}

```

---

### deployment_status.proto {#deployment_status}

**Path**: `pkg/config/proto/deployment_status.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Enums** (1): `DeploymentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/deployment_status.proto
// version: 1.0.0
// guid: e3f4a5b6-c7d8-9e0f-1a2b-3c4d5e6f7a8b

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * DeploymentStatus represents the status of a deployment.
 * Specifies the current state of configuration deployment operations.
 */
enum DeploymentStatus {
  // Unspecified deployment status
  DEPLOYMENT_STATUS_UNSPECIFIED = 0;

  // Deployment is pending
  DEPLOYMENT_STATUS_PENDING = 1;

  // Deployment is in progress
  DEPLOYMENT_STATUS_IN_PROGRESS = 2;

  // Deployment completed successfully
  DEPLOYMENT_STATUS_SUCCESS = 3;

  // Deployment failed
  DEPLOYMENT_STATUS_FAILED = 4;

  // Deployment was rolled back
  DEPLOYMENT_STATUS_ROLLED_BACK = 5;

  // Deployment was cancelled
  DEPLOYMENT_STATUS_CANCELLED = 6;
}

```

---

### deprecation_info.proto {#deprecation_info}

**Path**: `pkg/config/proto/deprecation_info.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `DeprecationInfo`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` → [config_events](./config_events.md#audit_level)
- `pkg/config/proto/backup_frequency.proto`
- `pkg/config/proto/channel_type.proto`
- `pkg/config/proto/config_data_type.proto` → [config_config_1](./config_config_1.md#config_data_type)
- `pkg/config/proto/deprecation_level.proto`
- `pkg/config/proto/metadata_status.proto`
- `pkg/config/proto/notification_trigger.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/deprecation_info.proto
// version: 1.0.0
// guid: 8431c848-ce8a-41cf-9848-ee052647463a

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

message DeprecationInfo {
  // Whether the configuration is deprecated
  bool deprecated = 1;

  // Deprecation reason
  string reason = 2;

  // Deprecation date
  google.protobuf.Timestamp deprecated_at = 3;

  // Replacement configuration key
  string replacement_key = 4;

  // Removal date
  google.protobuf.Timestamp removal_date = 5;

  // Migration guide
  string migration_guide = 6;

  // Deprecation level
  DeprecationLevel level = 7;
}

```

---

### deprecation_level.proto {#deprecation_level}

**Path**: `pkg/config/proto/deprecation_level.proto` **Package**: `gcommon.v1.config` **Lines**: 20

**Enums** (1): `DeprecationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/deprecation_level.proto
// version: 1.0.0
// guid: 0a330fa1-9f33-458b-a37e-aeed96ad7530

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum DeprecationLevel {
  DEPRECATION_LEVEL_UNSPECIFIED = 0;
  DEPRECATION_LEVEL_SOFT = 1; // Soft deprecation (warning)
  DEPRECATION_LEVEL_HARD = 2; // Hard deprecation (error)
  DEPRECATION_LEVEL_REMOVAL = 3; // Scheduled for removal
}

```

---

### environment_status.proto {#environment_status}

**Path**: `pkg/config/proto/environment_status.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Enums** (1): `EnvironmentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/environment_status.proto
// version: 1.0.0
// guid: d2e3f4a5-b6c7-8d9e-0f1a-2b3c4d5e6f7a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * EnvironmentStatus represents the status of an environment.
 * Specifies the current operational state of a configuration environment.
 */
enum EnvironmentStatus {
  // Unspecified environment status
  ENVIRONMENT_STATUS_UNSPECIFIED = 0;

  // Environment is active and operational
  ENVIRONMENT_STATUS_ACTIVE = 1;

  // Environment is inactive
  ENVIRONMENT_STATUS_INACTIVE = 2;

  // Environment is under maintenance
  ENVIRONMENT_STATUS_MAINTENANCE = 3;

  // Environment is deprecated
  ENVIRONMENT_STATUS_DEPRECATED = 4;

  // Environment is archived
  ENVIRONMENT_STATUS_ARCHIVED = 5;

  // Environment is in error state
  ENVIRONMENT_STATUS_ERROR = 6;
}

```

---

### environment_type.proto {#environment_type}

**Path**: `pkg/config/proto/environment_type.proto` **Package**: `gcommon.v1.config` **Lines**: 52

**Enums** (1): `EnvironmentType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/environment_type.proto
// version: 1.0.0
// guid: c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * EnvironmentType represents the type of environment.
 * Specifies the purpose and classification of configuration environments.
 */
enum EnvironmentType {
  // Unspecified environment type
  ENVIRONMENT_TYPE_UNSPECIFIED = 0;

  // Development environment
  ENVIRONMENT_TYPE_DEVELOPMENT = 1;

  // Testing environment
  ENVIRONMENT_TYPE_TESTING = 2;

  // Staging environment
  ENVIRONMENT_TYPE_STAGING = 3;

  // Production environment
  ENVIRONMENT_TYPE_PRODUCTION = 4;

  // Sandbox environment for experimentation
  ENVIRONMENT_TYPE_SANDBOX = 5;

  // Canary deployment environment
  ENVIRONMENT_TYPE_CANARY = 6;

  // Disaster recovery environment
  ENVIRONMENT_TYPE_DISASTER_RECOVERY = 7;

  // Integration testing environment
  ENVIRONMENT_TYPE_INTEGRATION = 8;

  // Performance testing environment
  ENVIRONMENT_TYPE_PERFORMANCE = 9;

  // Security testing environment
  ENVIRONMENT_TYPE_SECURITY = 10;
}

```

---

### filter_action.proto {#filter_action}

**Path**: `pkg/config/proto/filter_action.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `FilterAction`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/filter_action.proto
// version: 1.0.0
// guid: 733209f2-fa3d-471a-b3c3-260adaecd3a2

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum FilterAction {
  FILTER_ACTION_UNSPECIFIED = 0;
  FILTER_ACTION_INCLUDE = 1;
  FILTER_ACTION_EXCLUDE = 2;
  FILTER_ACTION_TRANSFORM = 3;
  FILTER_ACTION_VALIDATE = 4;
}

```

---

### filter_type.proto {#filter_type}

**Path**: `pkg/config/proto/filter_type.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Enums** (1): `FilterType`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/filter_type.proto
// version: 1.0.0
// guid: b6d065a7-715d-45d0-baa4-b09e53b470b5

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum FilterType {
  FILTER_TYPE_UNSPECIFIED = 0;
  FILTER_TYPE_KEY_PATTERN = 1;
  FILTER_TYPE_VALUE_PATTERN = 2;
  FILTER_TYPE_ENVIRONMENT = 3;
  FILTER_TYPE_SERVICE = 4;
  FILTER_TYPE_COMPONENT = 5;
  FILTER_TYPE_TAG = 6;
  FILTER_TYPE_CUSTOM = 7;
}

```

---

### health_check_type.proto {#health_check_type}

**Path**: `pkg/config/proto/health_check_type.proto` **Package**: `gcommon.v1.config` **Lines**: 43

**Enums** (1): `HealthCheckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/health_check_type.proto
// version: 1.0.0
// guid: f4a5b6c7-d8e9-0f1a-2b3c-4d5e6f7a8b9c

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * HealthCheckType represents the type of health check.
 * Specifies the protocol and method used for environment health checks.
 */
enum HealthCheckType {
  // Unspecified health check type
  HEALTH_CHECK_TYPE_UNSPECIFIED = 0;

  // HTTP health check
  HEALTH_CHECK_TYPE_HTTP = 1;

  // HTTPS health check
  HEALTH_CHECK_TYPE_HTTPS = 2;

  // TCP connection health check
  HEALTH_CHECK_TYPE_TCP = 3;

  // UDP connection health check
  HEALTH_CHECK_TYPE_UDP = 4;

  // gRPC health check
  HEALTH_CHECK_TYPE_GRPC = 5;

  // Database health check
  HEALTH_CHECK_TYPE_DATABASE = 6;

  // Custom health check
  HEALTH_CHECK_TYPE_CUSTOM = 7;
}

```

---

### health_state.proto {#health_state}

**Path**: `pkg/config/proto/health_state.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Enums** (1): `HealthState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/health_state.proto
// version: 1.0.0
// guid: a5b6c7d8-e9f0-1a2b-3c4d-5e6f7a8b9c0d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * HealthState represents the state of health.
 * Specifies the current health condition of environment components.
 */
enum HealthState {
  // Unspecified health state
  HEALTH_STATE_UNSPECIFIED = 0;

  // Component is healthy
  HEALTH_STATE_HEALTHY = 1;

  // Component is degraded but functional
  HEALTH_STATE_DEGRADED = 2;

  // Component is unhealthy
  HEALTH_STATE_UNHEALTHY = 3;

  // Health state is unknown
  HEALTH_STATE_UNKNOWN = 4;
}

```

---

### hook_error_handling.proto {#hook_error_handling}

**Path**: `pkg/config/proto/hook_error_handling.proto` **Package**: `gcommon.v1.config` **Lines**: 21

**Enums** (1): `HookErrorHandling`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/hook_error_handling.proto
// version: 1.0.0
// guid: f5c075fd-6a9f-4072-bea8-ee82bb35c1b5

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum HookErrorHandling {
  HOOK_ERROR_HANDLING_UNSPECIFIED = 0;
  HOOK_ERROR_HANDLING_IGNORE = 1;
  HOOK_ERROR_HANDLING_WARN = 2;
  HOOK_ERROR_HANDLING_FAIL = 3;
}

```

---

### hook_type.proto {#hook_type}

**Path**: `pkg/config/proto/hook_type.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `HookType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/hook_type.proto
// version: 1.0.0
// guid: a9982046-4cf7-4320-91ff-66f4b56b6258

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum HookType {
  HOOK_TYPE_UNSPECIFIED = 0;
  HOOK_TYPE_PRE_RENDER = 1;
  HOOK_TYPE_POST_RENDER = 2;
  HOOK_TYPE_PRE_APPLY = 3;
  HOOK_TYPE_POST_APPLY = 4;
  HOOK_TYPE_PRE_VALIDATE = 5;
  HOOK_TYPE_POST_VALIDATE = 6;
}

```

---

### inheritance_filter.proto {#inheritance_filter}

**Path**: `pkg/config/proto/inheritance_filter.proto` **Package**: `gcommon.v1.config` **Lines**: 31

**Messages** (1): `InheritanceFilter`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/filter_action.proto`
- `pkg/config/proto/filter_type.proto` → [log](./log.md#filter_type)

#### Source Code

```protobuf
// file: pkg/config/proto/inheritance_filter.proto
// version: 1.0.0
// guid: 0cda004b-8fb1-47de-a58b-fb17ec38d92f

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/filter_action.proto";
import "pkg/config/proto/filter_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message InheritanceFilter {
  // Filter type
  FilterType type = 1;

  // Filter expression
  string expression = 2;

  // Filter action
  FilterAction action = 3;

  // Filter metadata
  map<string, string> metadata = 4;
}

```

---

### inheritance_strategy.proto {#inheritance_strategy}

**Path**: `pkg/config/proto/inheritance_strategy.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `InheritanceStrategy`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/inheritance_strategy.proto
// version: 1.0.0
// guid: 8dc7386b-afe2-4d9d-804d-2286b8ae6cf7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum InheritanceStrategy {
  INHERITANCE_STRATEGY_UNSPECIFIED = 0;
  INHERITANCE_STRATEGY_OVERRIDE = 1;
  INHERITANCE_STRATEGY_MERGE = 2;
  INHERITANCE_STRATEGY_FALLBACK = 3;
  INHERITANCE_STRATEGY_PRIORITY = 4;
  INHERITANCE_STRATEGY_WEIGHTED = 5;
}

```

---

### inheritance_transformation.proto {#inheritance_transformation}

**Path**: `pkg/config/proto/inheritance_transformation.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `InheritanceTransformation`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/transformation_type.proto` → [config_2](./config_2.md#transformation_type)

#### Source Code

```protobuf
// file: pkg/config/proto/inheritance_transformation.proto
// version: 1.0.0
// guid: 9983db27-ce0c-4ed1-9433-20495b86b257

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/transformation_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message InheritanceTransformation {
  // Transformation type
  TransformationType type = 1;

  // Transformation expression
  string expression = 2;

  // Transformation parameters
  map<string, string> parameters = 3;

  // Transformation metadata
  map<string, string> metadata = 4;
}

```

---

### merge_strategy.proto {#merge_strategy}

**Path**: `pkg/config/proto/merge_strategy.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Enums** (1): `MergeStrategy`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/merge_strategy.proto
// version: 1.0.0
// guid: 559ca0d7-17d4-49ab-861d-febdc5862a47

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum MergeStrategy {
  MERGE_STRATEGY_UNSPECIFIED = 0;
  MERGE_STRATEGY_REPLACE = 1;
  MERGE_STRATEGY_MERGE_DEEP = 2;
  MERGE_STRATEGY_MERGE_SHALLOW = 3;
  MERGE_STRATEGY_ARRAY_CONCAT = 4;
  MERGE_STRATEGY_ARRAY_REPLACE = 5;
  MERGE_STRATEGY_ARRAY_MERGE = 6;
  MERGE_STRATEGY_CUSTOM = 7;
}

```

---

### metadata_status.proto {#metadata_status}

**Path**: `pkg/config/proto/metadata_status.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `MetadataStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/metadata_status.proto
// version: 1.0.0
// guid: b82301c8-c50d-454c-a434-ae44d4199677

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum MetadataStatus {
  METADATA_STATUS_UNSPECIFIED = 0;
  METADATA_STATUS_ACTIVE = 1;
  METADATA_STATUS_INACTIVE = 2;
  METADATA_STATUS_DRAFT = 3;
  METADATA_STATUS_DEPRECATED = 4;
  METADATA_STATUS_DELETED = 5;
  METADATA_STATUS_ERROR = 6;
}

```

---

### monitoring_alert.proto {#monitoring_alert}

**Path**: `pkg/config/proto/monitoring_alert.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `MonitoringAlert`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/monitoring_alert.proto
// version: 1.0.0
// guid: a6b7c8d9-0e1f-2345-0123-678901234567

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message MonitoringAlert {
  // Alert ID
  string id = 1;

  // Alert name
  string name = 2;

  // Alert condition
  string condition = 3;

  // Alert threshold
  double threshold = 4;

  // Alert enabled status
  bool enabled = 5;
}

```

---

### notification_channel.proto {#notification_channel}

**Path**: `pkg/config/proto/notification_channel.proto` **Package**: `gcommon.v1.config` **Lines**: 35

**Messages** (1): `NotificationChannel`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` → [config_events](./config_events.md#audit_level)
- `pkg/config/proto/backup_frequency.proto`
- `pkg/config/proto/channel_type.proto`
- `pkg/config/proto/config_data_type.proto` → [config_config_1](./config_config_1.md#config_data_type)
- `pkg/config/proto/deprecation_level.proto`
- `pkg/config/proto/metadata_status.proto`
- `pkg/config/proto/notification_trigger.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/notification_channel.proto
// version: 1.0.0
// guid: 81ed59c5-4e0f-499a-97c8-57a2a375fd75

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

message NotificationChannel {
  // Channel type
  ChannelType type = 1;

  // Channel configuration
  map<string, string> config = 2;

  // Whether channel is enabled
  bool enabled = 3;

  // Channel priority
  int32 priority = 4;
}

```

---

### notification_trigger.proto {#notification_trigger}

**Path**: `pkg/config/proto/notification_trigger.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `NotificationTrigger`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/notification_trigger.proto
// version: 1.0.0
// guid: e23c0d82-9395-4a27-840c-5765e4aaffbb

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum NotificationTrigger {
  NOTIFICATION_TRIGGER_UNSPECIFIED = 0;
  NOTIFICATION_TRIGGER_CHANGE = 1;
  NOTIFICATION_TRIGGER_DELETE = 2;
  NOTIFICATION_TRIGGER_ERROR = 3;
  NOTIFICATION_TRIGGER_APPROVAL = 4;
  NOTIFICATION_TRIGGER_DEPLOYMENT = 5;
  NOTIFICATION_TRIGGER_ROLLBACK = 6;
  NOTIFICATION_TRIGGER_SCHEDULE = 7;
}

```

---

### parameter_constraints.proto {#parameter_constraints}

**Path**: `pkg/config/proto/parameter_constraints.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `ParameterConstraints`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/parameter_constraints.proto
// version: 1.0.0
// guid: c8d9e0f1-2345-6789-2345-890123456789

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ParameterConstraints {
  // Minimum value
  string min_value = 1;

  // Maximum value
  string max_value = 2;

  // Pattern validation
  string pattern = 3;

  // Required flag
  bool required = 4;

  // Default value
  string default_value = 5;
}

```

---

### parameter_type.proto {#parameter_type}

**Path**: `pkg/config/proto/parameter_type.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Enums** (1): `ParameterType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/parameter_type.proto
// version: 1.0.0
// guid: ef891bab-fd5b-433d-9db4-42ff7a05b986

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ParameterType {
  PARAMETER_TYPE_UNSPECIFIED = 0;
  PARAMETER_TYPE_STRING = 1;
  PARAMETER_TYPE_INTEGER = 2;
  PARAMETER_TYPE_FLOAT = 3;
  PARAMETER_TYPE_BOOLEAN = 4;
  PARAMETER_TYPE_ENUM = 5;
  PARAMETER_TYPE_ARRAY = 6;
  PARAMETER_TYPE_OBJECT = 7;
  PARAMETER_TYPE_FILE = 8;
  PARAMETER_TYPE_URL = 9;
  PARAMETER_TYPE_EMAIL = 10;
  PARAMETER_TYPE_PASSWORD = 11;
  PARAMETER_TYPE_DATE = 12;
  PARAMETER_TYPE_TIME = 13;
  PARAMETER_TYPE_DATETIME = 14;
}

```

---

### rate_limits.proto {#rate_limits}

**Path**: `pkg/config/proto/rate_limits.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Messages** (1): `RateLimits`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/rate_limits.proto
// version: 1.0.0
// guid: c2d3e4f5-6a7b-8901-cdef-234567890123

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RateLimits {
  // Maximum requests per second
  int32 requests_per_second = 1;

  // Maximum burst size
  int32 burst_size = 2;

  // Rate limit window in seconds
  int32 window_seconds = 3;
}

```

---

### reference_type.proto {#reference_type}

**Path**: `pkg/config/proto/reference_type.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `ReferenceType`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/reference_type.proto
// version: 1.0.0
// guid: f7734726-4137-4441-b14d-c0c5479a50bd

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum ReferenceType {
  REFERENCE_TYPE_UNSPECIFIED = 0;
  REFERENCE_TYPE_TEMPLATE = 1;
  REFERENCE_TYPE_POINTER = 2;
  REFERENCE_TYPE_ALIAS = 3;
  REFERENCE_TYPE_COMPUTED = 4;
  REFERENCE_TYPE_DERIVED = 5;
}

```

---

### restore_point_status.proto {#restore_point_status}

**Path**: `pkg/config/proto/restore_point_status.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `RestorePointStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/restore_point_status.proto
// version: 1.0.0
// guid: 83838713-4e8f-494e-93ec-7bdf0b406982

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum RestorePointStatus {
  RESTORE_POINT_STATUS_UNSPECIFIED = 0;
  RESTORE_POINT_STATUS_CREATING = 1;
  RESTORE_POINT_STATUS_ACTIVE = 2;
  RESTORE_POINT_STATUS_EXPIRED = 3;
  RESTORE_POINT_STATUS_DELETED = 4;
  RESTORE_POINT_STATUS_ERROR = 5;
}

```

---

### restore_point_type.proto {#restore_point_type}

**Path**: `pkg/config/proto/restore_point_type.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `RestorePointType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/restore_point_type.proto
// version: 1.0.0
// guid: 2f531175-07c6-46a3-a5ab-01b240355ab8

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum RestorePointType {
  RESTORE_POINT_TYPE_UNSPECIFIED = 0;
  RESTORE_POINT_TYPE_MANUAL = 1; // Manually created restore point
  RESTORE_POINT_TYPE_AUTOMATIC = 2; // Automatically created restore point
  RESTORE_POINT_TYPE_SCHEDULED = 3; // Scheduled restore point
  RESTORE_POINT_TYPE_PRE_CHANGE = 4; // Created before configuration change
  RESTORE_POINT_TYPE_MILESTONE = 5; // Milestone restore point
  RESTORE_POINT_TYPE_BACKUP = 6; // Backup restore point
}

```

---

### restriction_type.proto {#restriction_type}

**Path**: `pkg/config/proto/restriction_type.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Enums** (1): `RestrictionType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/restriction_type.proto
// version: 1.0.0
// guid: 7444b7aa-6693-418e-ae6b-aa854f8c5400

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum RestrictionType {
  RESTRICTION_TYPE_UNSPECIFIED = 0;
  RESTRICTION_TYPE_IP_ADDRESS = 1;
  RESTRICTION_TYPE_TIME_RANGE = 2;
  RESTRICTION_TYPE_LOCATION = 3;
  RESTRICTION_TYPE_USER_AGENT = 4;
  RESTRICTION_TYPE_CUSTOM = 5;
}

```

---

### rollback_info.proto {#rollback_info}

**Path**: `pkg/config/proto/rollback_info.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `RollbackInfo`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/approval_status.proto`
- `pkg/config/proto/audit_operation_type.proto` → [config_events](./config_events.md#audit_operation_type)
- `pkg/config/proto/rollback_method.proto`
- `pkg/config/proto/validation_result_type.proto` → [config_2](./config_2.md#validation_result_type)
- `pkg/config/proto/validation_severity.proto` → [config_2](./config_2.md#validation_severity)

#### Source Code

```protobuf
// file: pkg/config/proto/rollback_info.proto
// version: 1.0.0
// guid: 20b0233a-770b-4484-a066-948c77afc78e

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/approval_status.proto";
import "pkg/config/proto/audit_operation_type.proto";
import "pkg/config/proto/rollback_method.proto";
import "pkg/config/proto/validation_result_type.proto";
import "pkg/config/proto/validation_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RollbackInfo {
  // Original audit entry being rolled back
  string original_audit_id = 1;

  // Rollback reason
  string reason = 2;

  // Rollback method
  RollbackMethod method = 3;

  // Target version for rollback
  string target_version = 4;

  // Whether rollback was automatic
  bool automatic = 5;
}

```

---

### rollback_method.proto {#rollback_method}

**Path**: `pkg/config/proto/rollback_method.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Enums** (1): `RollbackMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/rollback_method.proto
// version: 1.0.0
// guid: b0c1d2e3-f4a5-6b7c-8d9e-0f1a2b3c4d5e

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * RollbackMethod represents how the rollback was performed.
 * Specifies the technique used to revert configuration changes.
 */
enum RollbackMethod {
  // Unspecified rollback method
  ROLLBACK_METHOD_UNSPECIFIED = 0;

  // Restore individual values
  ROLLBACK_METHOD_VALUE_RESTORE = 1;

  // Restore from version history
  ROLLBACK_METHOD_VERSION_RESTORE = 2;

  // Restore from snapshot
  ROLLBACK_METHOD_SNAPSHOT_RESTORE = 3;

  // Manual rollback process
  ROLLBACK_METHOD_MANUAL = 4;
}

```

---

### rotation_frequency.proto {#rotation_frequency}

**Path**: `pkg/config/proto/rotation_frequency.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `RotationFrequency`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/rotation_frequency.proto
// version: 1.0.0
// guid: 4bb020d8-2763-4ac1-96fc-6210bade7050

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum RotationFrequency {
  ROTATION_FREQUENCY_UNSPECIFIED = 0;
  ROTATION_FREQUENCY_MANUAL = 1;
  ROTATION_FREQUENCY_DAILY = 2;
  ROTATION_FREQUENCY_WEEKLY = 3;
  ROTATION_FREQUENCY_MONTHLY = 4;
  ROTATION_FREQUENCY_QUARTERLY = 5;
  ROTATION_FREQUENCY_YEARLY = 6;
  ROTATION_FREQUENCY_ON_EXPIRY = 7;
}

```

---

### secret_backup_frequency.proto {#secret_backup_frequency}

**Path**: `pkg/config/proto/secret_backup_frequency.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Enums** (1): `SecretBackupFrequency`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/secret_backup_frequency.proto
// version: 1.0.0
// guid: d2ec4ba6-932e-4349-89f4-aa4af899c73f

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SecretBackupFrequency {
  SECRET_BACKUP_FREQUENCY_UNSPECIFIED = 0;
  SECRET_BACKUP_FREQUENCY_MANUAL = 1;
  SECRET_BACKUP_FREQUENCY_HOURLY = 2;
  SECRET_BACKUP_FREQUENCY_DAILY = 3;
  SECRET_BACKUP_FREQUENCY_WEEKLY = 4;
  SECRET_BACKUP_FREQUENCY_MONTHLY = 5;
  SECRET_BACKUP_FREQUENCY_ON_CHANGE = 6;
}

```

---

### secret_status.proto {#secret_status}

**Path**: `pkg/config/proto/secret_status.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Enums** (1): `SecretStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/secret_status.proto
// version: 1.0.0
// guid: 7fb6a7a0-ecc1-4dc0-b2a0-49c3e3fe88b9

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SecretStatus {
  SECRET_STATUS_UNSPECIFIED = 0;
  SECRET_STATUS_ACTIVE = 1;
  SECRET_STATUS_INACTIVE = 2;
  SECRET_STATUS_EXPIRED = 3;
  SECRET_STATUS_ROTATED = 4;
  SECRET_STATUS_COMPROMISED = 5;
  SECRET_STATUS_DELETED = 6;
  SECRET_STATUS_ERROR = 7;
}

```

---

### secret_type.proto {#secret_type}

**Path**: `pkg/config/proto/secret_type.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Enums** (1): `SecretType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/secret_type.proto
// version: 1.0.0
// guid: efadf8e9-2dc3-4ccc-8c9a-3a7f0a1c0895

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SecretType {
  SECRET_TYPE_UNSPECIFIED = 0;
  SECRET_TYPE_PASSWORD = 1;
  SECRET_TYPE_API_KEY = 2;
  SECRET_TYPE_TOKEN = 3;
  SECRET_TYPE_CERTIFICATE = 4;
  SECRET_TYPE_PRIVATE_KEY = 5;
  SECRET_TYPE_PUBLIC_KEY = 6;
  SECRET_TYPE_OAUTH_CLIENT_SECRET = 7;
  SECRET_TYPE_DATABASE_PASSWORD = 8;
  SECRET_TYPE_CONNECTION_STRING = 9;
  SECRET_TYPE_ENCRYPTION_KEY = 10;
  SECRET_TYPE_SIGNING_KEY = 11;
  SECRET_TYPE_SSH_KEY = 12;
  SECRET_TYPE_TLS_CERTIFICATE = 13;
  SECRET_TYPE_JWT_SECRET = 14;
  SECRET_TYPE_WEBHOOK_SECRET = 15;
  SECRET_TYPE_CUSTOM = 16;
}

```

---

### secret_validation_result.proto {#secret_validation_result}

**Path**: `pkg/config/proto/secret_validation_result.proto` **Package**: `gcommon.v1.config` **Lines**: 36

**Messages** (1): `SecretValidationResult`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/secret_validation_result_type.proto` → [config_2](./config_2.md#secret_validation_result_type)
- `pkg/config/proto/secret_validation_severity.proto` → [config_2](./config_2.md#secret_validation_severity)

#### Source Code

```protobuf
// file: pkg/config/proto/secret_validation_result.proto
// version: 1.0.0
// guid: 59941566-6573-4333-bf99-4652471115b0

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/secret_validation_result_type.proto";
import "pkg/config/proto/secret_validation_severity.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message SecretValidationResult {
  // Validation name
  string name = 1;

  // Validation result
  SecretValidationResultType result = 2;

  // Validation message
  string message = 3;

  // Validation severity
  SecretValidationSeverity severity = 4;

  // Validation timestamp
  google.protobuf.Timestamp timestamp = 5;

  // Validation details
  map<string, string> details = 6;
}

```

---
