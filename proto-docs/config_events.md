# config_events Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 6
- **Messages**: 3
- **Services**: 0
- **Enums**: 3

## Files in this Module

- [audit_level.proto](#audit_level)
- [audit_operation_type.proto](#audit_operation_type)
- [compliance_audit.proto](#compliance_audit)
- [rotation_event.proto](#rotation_event)
- [secret_audit_level.proto](#secret_audit_level)
- [version_promotion_event.proto](#version_promotion_event)

## Module Dependencies

**This module depends on**:

- [auth_events](./auth_events.md)
- [common](./common.md)

**Modules that depend on this one**:

- [config_1](./config_1.md)
- [config_2](./config_2.md)
- [config_config_1](./config_config_1.md)
- [config_config_2](./config_config_2.md)

---

## Detailed Documentation

### audit_level.proto {#audit_level}

**Path**: `pkg/config/proto/audit_level.proto` **Package**: `gcommon.v1.config`
**Lines**: 22

**Enums** (1): `AuditLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/audit_level.proto
// version: 1.0.0
// guid: 8576474b-84f1-4a99-ab88-a865fb4e28ca

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum AuditLevel {
  AUDIT_LEVEL_UNSPECIFIED = 0;
  AUDIT_LEVEL_NONE = 1;
  AUDIT_LEVEL_MINIMAL = 2;
  AUDIT_LEVEL_STANDARD = 3;
  AUDIT_LEVEL_DETAILED = 4;
  AUDIT_LEVEL_VERBOSE = 5;
}

```

---

### audit_operation_type.proto {#audit_operation_type}

**Path**: `pkg/config/proto/audit_operation_type.proto` **Package**:
`gcommon.v1.config` **Lines**: 61

**Enums** (1): `AuditOperationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/audit_operation_type.proto
// version: 1.0.0
// guid: d6e7f8a9-b0c1-2d3e-4f5a-6b7c8d9e0f1a

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * AuditOperationType represents the type of configuration operation.
 * Specifies the category of configuration change being audited.
 */
enum AuditOperationType {
  // Unspecified operation type
  AUDIT_OPERATION_TYPE_UNSPECIFIED = 0;

  // Create new configuration
  AUDIT_OPERATION_TYPE_CREATE = 1;

  // Update existing configuration
  AUDIT_OPERATION_TYPE_UPDATE = 2;

  // Delete configuration
  AUDIT_OPERATION_TYPE_DELETE = 3;

  // Bulk create multiple configurations
  AUDIT_OPERATION_TYPE_BULK_CREATE = 4;

  // Bulk update multiple configurations
  AUDIT_OPERATION_TYPE_BULK_UPDATE = 5;

  // Bulk delete multiple configurations
  AUDIT_OPERATION_TYPE_BULK_DELETE = 6;

  // Import configuration data
  AUDIT_OPERATION_TYPE_IMPORT = 7;

  // Export configuration data
  AUDIT_OPERATION_TYPE_EXPORT = 8;

  // Backup configuration
  AUDIT_OPERATION_TYPE_BACKUP = 9;

  // Restore configuration from backup
  AUDIT_OPERATION_TYPE_RESTORE = 10;

  // Rollback configuration changes
  AUDIT_OPERATION_TYPE_ROLLBACK = 11;

  // Validate configuration
  AUDIT_OPERATION_TYPE_VALIDATE = 12;

  // Synchronize configuration
  AUDIT_OPERATION_TYPE_SYNC = 13;
}

```

---

### compliance_audit.proto {#compliance_audit}

**Path**: `pkg/config/proto/compliance_audit.proto` **Package**:
`gcommon.v1.config` **Lines**: 27

**Messages** (1): `ComplianceAudit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/compliance_audit.proto
// version: 1.0.0
// guid: d3e4f5a6-7b8c-9012-def0-345678901234

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ComplianceAudit {
  // Audit ID
  string id = 1;

  // Audit name
  string name = 2;

  // Audit type
  string type = 3;

  // Audit enabled status
  bool enabled = 4;
}

```

---

### rotation_event.proto {#rotation_event}

**Path**: `pkg/config/proto/rotation_event.proto` **Package**:
`gcommon.v1.config` **Lines**: 31

**Messages** (1): `RotationEvent`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/rotation_event.proto
// version: 1.0.0
// guid: b7c8d9e0-1f23-4567-1234-789012345678

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message RotationEvent {
  // Event ID
  string id = 1;

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

### secret_audit_level.proto {#secret_audit_level}

**Path**: `pkg/config/proto/secret_audit_level.proto` **Package**:
`gcommon.v1.config` **Lines**: 23

**Enums** (1): `SecretAuditLevel`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/config/proto/secret_audit_level.proto
// version: 1.0.0
// guid: bc307b1b-aa5d-4b26-8724-6f1e537132c5

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

enum SecretAuditLevel {
  SECRET_AUDIT_LEVEL_UNSPECIFIED = 0;
  SECRET_AUDIT_LEVEL_NONE = 1;
  SECRET_AUDIT_LEVEL_MINIMAL = 2;
  SECRET_AUDIT_LEVEL_STANDARD = 3;
  SECRET_AUDIT_LEVEL_DETAILED = 4;
  SECRET_AUDIT_LEVEL_VERBOSE = 5;
}

```

---

### version_promotion_event.proto {#version_promotion_event}

**Path**: `pkg/config/proto/version_promotion_event.proto` **Package**:
`gcommon.v1.config` **Lines**: 44

**Messages** (1): `VersionPromotionEvent`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/audit_log.proto` → [auth_events](./auth_events.md#audit_log)
  → [common](./common.md#audit_log)

#### Source Code

```protobuf
// file: pkg/config/proto/version_promotion_event.proto
// version: 1.0.0
// guid: d231a04f-95ab-4854-a15d-7992ab883362

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/audit_log.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersionPromotionEvent {
  // Source environment
  string source_environment = 1;

  // Target environment
  string target_environment = 2;

  // Promotion timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Promotion user
  string promoted_by = 4;

  // Promotion reason
  string reason = 5;

  // Promotion method
  string method = 6;

  // Promotion success
  bool success = 7;

  // Promotion error
  string error = 8;

  // Promotion metadata
  map<string, string> metadata = 9;
}

```

---
