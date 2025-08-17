# auth_events Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 2
- **Services**: 0
- **Enums**: 1

## Files in this Module

- [audit_action.proto](#audit_action)
- [audit_event.proto](#audit_event)
- [audit_log.proto](#audit_log)

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)

**Modules that depend on this one**:

- [config_2](./config_2.md)
- [config_events](./config_events.md)

---

## Detailed Documentation

### audit_action.proto {#audit_action}

**Path**: `pkg/auth/proto/audit_action.proto` **Package**: `gcommon.v1.auth` **Lines**: 57

**Enums** (1): `AuditAction`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/audit_action.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Audit action enumeration for tracking user and system actions.
 * Used for security auditing and compliance logging.
 */
enum AuditAction {
  // Unspecified audit action
  AUDIT_ACTION_UNSPECIFIED = 0;

  // Authentication actions
  AUDIT_ACTION_LOGIN = 1;
  AUDIT_ACTION_LOGOUT = 2;
  AUDIT_ACTION_LOGIN_FAILED = 3;

  // Authorization actions
  AUDIT_ACTION_ACCESS_GRANTED = 4;
  AUDIT_ACTION_ACCESS_DENIED = 5;

  // User management actions
  AUDIT_ACTION_USER_CREATED = 6;
  AUDIT_ACTION_USER_UPDATED = 7;
  AUDIT_ACTION_USER_DELETED = 8;
  AUDIT_ACTION_USER_SUSPENDED = 9;

  // Role management actions
  AUDIT_ACTION_ROLE_ASSIGNED = 10;
  AUDIT_ACTION_ROLE_REMOVED = 11;
  AUDIT_ACTION_ROLE_CREATED = 12;
  AUDIT_ACTION_ROLE_UPDATED = 13;
  AUDIT_ACTION_ROLE_DELETED = 14;

  // Permission actions
  AUDIT_ACTION_PERMISSION_GRANTED = 15;
  AUDIT_ACTION_PERMISSION_REVOKED = 16;

  // Session actions
  AUDIT_ACTION_SESSION_CREATED = 17;
  AUDIT_ACTION_SESSION_TERMINATED = 18;

  // Configuration changes
  AUDIT_ACTION_CONFIG_UPDATED = 19;

  // System actions
  AUDIT_ACTION_SYSTEM_BACKUP = 20;
  AUDIT_ACTION_SYSTEM_RESTORE = 21;
}

```

---

### audit_event.proto {#audit_event}

**Path**: `pkg/auth/proto/audit_event.proto` **Package**: `gcommon.v1.auth` **Lines**: 31

**Messages** (1): `AuditEvent`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/audit_event.proto
// version: 1.0.0
// guid: 07442bc2-38fe-42b3-aecd-0ffda724fa86

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuditEvent records authentication-related actions for auditing.
 */
message AuditEvent {
  // Type of event (e.g., LOGIN, LOGOUT)
  string event_type = 1;

  // User ID associated with the event
  string user_id = 2;

  // Time event occurred
  google.protobuf.Timestamp timestamp = 3 [lazy = true];

  // Additional metadata about the event
  map<string, string> metadata = 4;
}

```

---

### audit_log.proto {#audit_log}

**Path**: `pkg/auth/proto/audit_log.proto` **Package**: `gcommon.v1.auth` **Lines**: 32

**Messages** (1): `AuditLog`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/audit_log.proto
// version: 1.0.0
// guid: 404a4fba-327e-4ad8-a144-f337dd511f36

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

// AuditLog captures security-relevant user actions for auditing purposes
message AuditLog {
  // Unique identifier of the user performing the action
  string user_id = 1;

  // Action performed (e.g., LOGIN, LOGOUT, UPDATE_PROFILE)
  string action = 2;

  // Time the action occurred
  google.protobuf.Timestamp timestamp = 3;

  // IP address of the client
  string ip_address = 4;

  // Additional metadata for the audit entry
  map<string, string> metadata = 5;
}

```

---
