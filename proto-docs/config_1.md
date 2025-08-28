# config_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

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
---


## Detailed Documentation

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

