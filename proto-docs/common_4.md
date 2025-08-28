# common_4 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 20
- **Services**: 0
- **Enums**: 30

## Files in this Module

- [pagination_options.proto](#pagination_options)
- [parameter_constraints.proto](#parameter_constraints)
- [parameter_type.proto](#parameter_type)
- [partition_strategy.proto](#partition_strategy)
- [password_credentials.proto](#password_credentials)
- [password_policy.proto](#password_policy)
- [permission.proto](#permission)
- [permission_condition.proto](#permission_condition)
- [permission_grant.proto](#permission_grant)
- [permission_level.proto](#permission_level)
- [permission_metadata.proto](#permission_metadata)
- [permission_scope.proto](#permission_scope)
- [permission_type.proto](#permission_type)
- [priority_level.proto](#priority_level)
- [processing_status.proto](#processing_status)
- [provider_state.proto](#provider_state)
- [provider_type.proto](#provider_type)
- [proxy_type.proto](#proxy_type)
- [quality_score.proto](#quality_score)
- [query_operation.proto](#query_operation)
- [rate_limit.proto](#rate_limit)
- [rate_limit_info.proto](#rate_limit_info)
- [rate_limit_strategy.proto](#rate_limit_strategy)
- [read_level.proto](#read_level)
- [rebalance_strategy.proto](#rebalance_strategy)
- [reference_type.proto](#reference_type)
- [refresh_token.proto](#refresh_token)
- [registration_action.proto](#registration_action)
- [remediation_details.proto](#remediation_details)
- [replication_level.proto](#replication_level)
- [replication_mode.proto](#replication_mode)
- [request_metadata.proto](#request_metadata)
- [resolution.proto](#resolution)
- [resolution_strategy.proto](#resolution_strategy)
- [resource_reference.proto](#resource_reference)
- [resource_status.proto](#resource_status)
- [response_compression.proto](#response_compression)
- [response_metadata.proto](#response_metadata)
- [restriction_type.proto](#restriction_type)
- [retention_policy.proto](#retention_policy)
- [retention_policy_info.proto](#retention_policy_info)
- [retention_unit.proto](#retention_unit)
- [retry_delay_strategy.proto](#retry_delay_strategy)
- [retry_policy.proto](#retry_policy)
- [role.proto](#role)
- [role_assignment.proto](#role_assignment)
- [role_metadata.proto](#role_metadata)
- [role_scope.proto](#role_scope)
- [rotation_frequency.proto](#rotation_frequency)
- [route_type.proto](#route_type)
---


## Detailed Documentation

### pagination_options.proto {#pagination_options}

**Path**: `gcommon/v1/common/pagination_options.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `PaginationOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/pagination_options.proto
// version: 1.1.0
// guid: 5c1c9ffd-3554-4f8b-91d6-82d7a453683f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// PaginationOptions defines standard paging parameters.
message PaginationOptions {
  // Maximum number of items to return.
  int32 page_size = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Opaque token representing the next page.
  string page_token = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### parameter_constraints.proto {#parameter_constraints}

**Path**: `gcommon/v1/common/parameter_constraints.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `ParameterConstraints`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/parameter_constraints.proto
// version: 1.0.0
// guid: c8d9e0f1-2345-6789-2345-890123456789

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ParameterConstraints {
  // Minimum value
  string min_value = 1 [(buf.validate.field).string.min_len = 1];

  // Maximum value
  string max_value = 2 [(buf.validate.field).string.min_len = 1];

  // Pattern validation
  string pattern = 3 [(buf.validate.field).string.min_len = 1];

  // Required flag
  bool required = 4;

  // Default value
  string default_value = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### parameter_type.proto {#parameter_type}

**Path**: `gcommon/v1/common/parameter_type.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `ParameterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/parameter_type.proto
// version: 1.0.1
// guid: ef891bab-fd5b-433d-9db4-42ff7a05b986

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### partition_strategy.proto {#partition_strategy}

**Path**: `gcommon/v1/common/partition_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `PartitionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_strategy.proto
// version: 1.0.1
// guid: f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Partitioning strategies for queue messages.
 * Determines how messages are distributed across partitions.
 */
enum PartitionStrategy {
  // Default partitioning strategy
  PARTITION_STRATEGY_UNSPECIFIED = 0;

  // Round-robin distribution across partitions
  PARTITION_STRATEGY_ROUND_ROBIN = 1;

  // Hash-based partitioning using message key
  PARTITION_STRATEGY_HASH = 2;

  // Random partition assignment
  PARTITION_STRATEGY_RANDOM = 3;

  // Manual partition specification
  PARTITION_STRATEGY_MANUAL = 4;

  // Sticky partitioning (same producer uses same partition)
  PARTITION_STRATEGY_STICKY = 5;

  // Load-based partitioning (least loaded partition)
  PARTITION_STRATEGY_LOAD_BALANCED = 6;
}
```

---

### password_credentials.proto {#password_credentials}

**Path**: `gcommon/v1/common/password_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `PasswordCredentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/password_credentials.proto
// version: 1.0.0
// guid: 1ebf6a98-d3d5-4921-9d97-59280e8ba216
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Username/password credentials for traditional authentication.
 * Supports both username and email-based authentication with optional
 * remember-me functionality for extended session duration.
 */
message PasswordCredentials {
  // Username or email address for authentication
  string username = 1 [(buf.validate.field).string.min_len = 1];

  // User's password (should be transmitted over secure channels only)
  string password = 2 [(buf.validate.field).string.min_len = 8];

  // Remember me option for extended session duration
  // When true, session may have longer expiration time
  bool remember_me = 3;
}
```

---

### password_policy.proto {#password_policy}

**Path**: `gcommon/v1/common/password_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Messages** (1): `PasswordPolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/password_policy.proto
// version: 1.0.0
// guid: d19b7fa7-bd0d-4d6c-bc5b-2453bd250890

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Requirements and restrictions for user passwords.
 */
message PasswordPolicy {
  // Minimum required length for passwords.
  int32 min_length = 1 [(buf.validate.field).int32.gte = 0];

  // Require at least one uppercase letter.
  bool require_uppercase = 2;

  // Require at least one lowercase letter.
  bool require_lowercase = 3;

  // Require at least one numeric digit.
  bool require_number = 4;

  // Require at least one symbol character.
  bool require_symbol = 5;

  // Maximum password age in days before expiration.
  int32 max_age_days = 6 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of previous passwords disallowed for reuse.
  int32 history = 7 [(buf.validate.field).int32.gte = 0];

  // Whether password reuse is permitted after history is exhausted.
  bool allow_reuse = 8;
}
```

---

### permission.proto {#permission}

**Path**: `gcommon/v1/common/permission.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `Permission`

**Imports** (4):

- `gcommon/v1/common/scope_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission.proto
// version: 1.0.0
// guid: 38e2195b-8510-48b4-9c7c-2f87ab8e9a1a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/scope_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission represents a specific action that can be granted
 * to a user or role within the authentication system.
 */
message Permission {
  // Unique identifier for the permission
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Short machine friendly permission name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Human readable description of what the permission allows
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Scope at which this permission applies
  gcommon.v1.common.ScopeType scope = 4;

  // Timestamp when the permission was created
  google.protobuf.Timestamp created_at = 5 [lazy = true, (buf.validate.field).required = true];
}
```

---

### permission_condition.proto {#permission_condition}

**Path**: `gcommon/v1/common/permission_condition.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `PermissionCondition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_condition.proto
// version: 1.0.0
// guid: 54038d4d-21ce-4ccb-a735-255fae2bcd86

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message PermissionCondition {
  string key = 1 [(buf.validate.field).string.min_len = 1];
  string operator = 2; // eq, ne, in, not_in, etc.
  repeated string values = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### permission_grant.proto {#permission_grant}

**Path**: `gcommon/v1/common/permission_grant.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Messages** (1): `PermissionGrant`

**Imports** (4):

- `gcommon/v1/common/permission_scope.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_grant.proto
// version: 1.0.0
// guid: c33e6d90-d966-45f1-ad79-4b6142211caf
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/permission_scope.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission grant entity representing granted permissions.
 * Used for tracking direct permission assignments to users.
 * Supports scoped permissions and expiration.
 */
message PermissionGrant {
  // Unique grant identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User ID receiving the permission
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Permission being granted
  string permission = 3;

  // Resource the permission applies to (optional)
  string resource = 4;

  // Permission scope
  PermissionScope scope = 5;

  // Grant creation timestamp
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];

  // Grant expiration timestamp (optional)
  google.protobuf.Timestamp expires_at = 7 [lazy = true];

  // User who granted the permission
  string granted_by_user_id = 8;

  // Grant metadata
  map<string, string> metadata = 9 [lazy = true];

  // Grant active flag
  bool active = 10;
}
```

---

### permission_level.proto {#permission_level}

**Path**: `gcommon/v1/common/permission_level.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `AuthPermissionLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_level.proto
// version: 1.0.1
// guid: 776ae326-7f13-4a07-9c1d-255140b0f83b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthPermissionLevel {
  PERMISSION_LEVEL_UNSPECIFIED = 0;
  PERMISSION_LEVEL_SYSTEM = 1;
  PERMISSION_LEVEL_ORGANIZATION = 2;
  PERMISSION_LEVEL_PROJECT = 3;
  PERMISSION_LEVEL_RESOURCE = 4;
}
```

---

### permission_metadata.proto {#permission_metadata}

**Path**: `gcommon/v1/common/permission_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Messages** (1): `PermissionMetadata`

**Imports** (4):

- `gcommon/v1/common/permission_condition.proto`
- `gcommon/v1/common/permission_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_metadata.proto
// version: 1.0.0
// guid: e953942b-bd06-424a-8c5a-2b2b9f60d4ab

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/permission_condition.proto";
import "gcommon/v1/common/permission_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message PermissionMetadata {
  // Permission ID
  string permission_id = 1;

  // Permission name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Resource types this permission applies to
  repeated string resource_types = 3;

  // Actions allowed by this permission
  repeated string actions = 4;

  // Conditions or constraints
  repeated gcommon.v1.common.PermissionCondition conditions = 5;

  // Permission level (system, organization, project, etc.)

  AuthPermissionLevel level = 6;

  // Creation metadata
  int64 created_at = 7;
  string created_by = 8 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];
}
```

---

### permission_scope.proto {#permission_scope}

**Path**: `gcommon/v1/common/permission_scope.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `PermissionScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_scope.proto
// version: 1.0.1
// guid: 223f7d62-a27f-4724-8f07-6c99d1afaa17
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission scope enumeration defining the level at which permissions apply.
 * Used for fine-grained access control and permission inheritance.
 */
enum PermissionScope {
  // Unspecified permission scope
  PERMISSION_SCOPE_UNSPECIFIED = 0;

  // Global system-wide permission
  PERMISSION_SCOPE_GLOBAL = 1;

  // Organization-level permission
  PERMISSION_SCOPE_ORGANIZATION = 2;

  // Project-level permission
  PERMISSION_SCOPE_PROJECT = 3;

  // Resource-level permission
  PERMISSION_SCOPE_RESOURCE = 4;

  // User-level permission
  PERMISSION_SCOPE_USER = 5;
}
```

---

### permission_type.proto {#permission_type}

**Path**: `gcommon/v1/common/permission_type.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Enums** (1): `PermissionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_type.proto
// version: 1.0.1
// guid: 2e23ed6f-5620-4c13-a485-eaeb2d0edf25
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission categories for authorization decisions.
 */
enum PermissionType {
  // Unspecified permission type.
  PERMISSION_TYPE_UNSPECIFIED = 0;

  // Read-only access.
  PERMISSION_TYPE_READ = 1;

  // Write access.
  PERMISSION_TYPE_WRITE = 2;

  // Delete access.
  PERMISSION_TYPE_DELETE = 3;

  // Administrative privileges.
  PERMISSION_TYPE_ADMIN = 4;

  // Execute or run operations.
  PERMISSION_TYPE_EXECUTE = 5;
}
```

---

### priority_level.proto {#priority_level}

**Path**: `gcommon/v1/common/priority_level.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `PriorityLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/priority_level.proto
// version: 1.0.1
// guid: e13c77fc-1bf7-42ed-947a-6e1ed4914bb2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// PriorityLevel defines generic priority classes for queue messages.
// buf:lint:ignore ENUM_VALUE_PREFIX
enum PriorityLevel {
  // Default unspecified priority.
  QUEUE_PRIORITY_LEVEL_UNSPECIFIED = 0;
  // Low priority messages are processed after normal traffic.
  QUEUE_PRIORITY_LEVEL_LOW = 1;
  // Normal priority for standard workload.
  QUEUE_PRIORITY_LEVEL_MEDIUM = 2;
  // High priority messages are processed before others.
  QUEUE_PRIORITY_LEVEL_HIGH = 3;
  // Critical messages are processed immediately with highest importance.
  QUEUE_PRIORITY_LEVEL_CRITICAL = 4;
}
```

---

### processing_status.proto {#processing_status}

**Path**: `gcommon/v1/common/processing_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `ProcessingStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/processing_status.proto
// version: 1.0.1
// guid: ef01234-5678-9abc-c5d6-e7f8a9b0c1d2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Status of media processing jobs.
enum ProcessingStatus {
  PROCESSING_STATUS_UNSPECIFIED = 0;
  PROCESSING_STATUS_PENDING = 1;
  PROCESSING_STATUS_PROCESSING = 2;
  PROCESSING_STATUS_COMPLETED = 3;
  PROCESSING_STATUS_FAILED = 4;
  PROCESSING_STATUS_CANCELLED = 5;
  PROCESSING_STATUS_PAUSED = 6;
}
```

---

### provider_state.proto {#provider_state}

**Path**: `gcommon/v1/common/provider_state.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `ProviderState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_state.proto
// version: 1.0.1
// guid: 123e4567-e89b-12d3-a456-426614174024

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ProviderState defines the possible states of a provider.
 */
enum ProviderState {
  PROVIDER_STATE_UNSPECIFIED = 0;
  PROVIDER_STATE_CREATING = 1;
  PROVIDER_STATE_STARTING = 2;
  PROVIDER_STATE_RUNNING = 3;
  PROVIDER_STATE_STOPPING = 4;
  PROVIDER_STATE_STOPPED = 5;
  PROVIDER_STATE_ERROR = 6;
  PROVIDER_STATE_UNKNOWN = 7;
}
```

---

### provider_type.proto {#provider_type}

**Path**: `gcommon/v1/common/provider_type.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `AuthProviderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/provider_type.proto
// version: 1.0.1
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f90

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ProviderType enumerates the supported authentication provider backends.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthProviderType {
  // Default unspecified provider type
  AUTH_PROVIDER_TYPE_UNSPECIFIED = 0;

  // Built-in local provider
  AUTH_PROVIDER_TYPE_LOCAL = 1;

  // LDAP directory provider
  AUTH_PROVIDER_TYPE_LDAP = 2;

  // Active Directory provider
  AUTH_PROVIDER_TYPE_ACTIVE_DIRECTORY = 3;

  // OAuth2 provider (generic)
  AUTH_PROVIDER_TYPE_OAUTH2 = 4;

  // SAML provider
  AUTH_PROVIDER_TYPE_SAML = 5;
}
```

---

### proxy_type.proto {#proxy_type}

**Path**: `gcommon/v1/common/proxy_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ProxyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/proxy_type.proto
// version: 1.0.1
// guid: 9b6f5494-a0d0-4832-a3f3-9d91dbf2c200
//
// ProxyType lists supported proxy configurations.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ProxyType {
  PROXY_TYPE_UNSPECIFIED = 0;
  PROXY_TYPE_FORWARD = 1;
  PROXY_TYPE_REVERSE = 2;
  PROXY_TYPE_TRANSPARENT = 3;
}
```

---

### quality_score.proto {#quality_score}

**Path**: `gcommon/v1/common/quality_score.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `QualityScore`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/quality_score.proto
// version: 1.0.1
// guid: 3d37a954-484a-4beb-acc4-7ec2fd05bf7d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Overall media quality rating.
enum QualityScore {
  QUALITY_SCORE_UNSPECIFIED = 0;
  QUALITY_SCORE_LOW = 1;
  QUALITY_SCORE_MEDIUM = 2;
  QUALITY_SCORE_HIGH = 3;
  QUALITY_SCORE_EXCELLENT = 4;
}
```

---

### query_operation.proto {#query_operation}

**Path**: `gcommon/v1/common/query_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 61

**Enums** (1): `QueryOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_operation.proto
// version: 1.0.1
// guid: dcbbcb0c-451b-40d4-a928-ebe7659c8e66
// file: proto/gcommon/v1/metrics/v1/query_operation.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * QueryOperation defines the types of operations that can be performed on metrics queries.
 * Used for aggregating, filtering, and transforming metric data.
 */
enum QueryOperation {
  // Unspecified operation (default)
  QUERY_OPERATION_UNSPECIFIED = 0;

  // Select/filter metrics by criteria
  QUERY_OPERATION_SELECT = 1;

  // Group metrics by labels
  QUERY_OPERATION_GROUP_BY = 2;

  // Sum values across time or series
  QUERY_OPERATION_SUM = 3;

  // Average values across time or series
  QUERY_OPERATION_AVG = 4;

  // Find minimum value
  QUERY_OPERATION_MIN = 5;

  // Find maximum value
  QUERY_OPERATION_MAX = 6;

  // Count number of samples
  QUERY_OPERATION_COUNT = 7;

  // Calculate rate of change
  QUERY_OPERATION_RATE = 8;

  // Calculate increase over time
  QUERY_OPERATION_INCREASE = 9;

  // Sort results
  QUERY_OPERATION_SORT = 10;

  // Limit number of results
  QUERY_OPERATION_LIMIT = 11;

  // Join multiple metric series
  QUERY_OPERATION_JOIN = 12;
}
```

---

### rate_limit.proto {#rate_limit}

**Path**: `gcommon/v1/common/rate_limit.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `RateLimit`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/rate_limit.proto
// version: 1.0.0
// guid: ba20cc02-8ef6-4de0-9c0a-30ddcb8c7b14
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Rate limiting information for API throttling and quota management.
 * Provides current rate limit status and reset timing information
 * for client-side rate limit handling and backoff strategies.
 */
message RateLimit {
  // Maximum number of requests allowed per time window
  int32 limit = 1 [(buf.validate.field).int32.gte = 0];

  // Duration of the time window for rate limiting
  google.protobuf.Duration window = 2;

  // Number of requests remaining in the current window
  int32 remaining = 3 [(buf.validate.field).int32.gte = 0];

  // Time until the rate limit window resets
  google.protobuf.Duration reset_time = 4;
}
```

---

### rate_limit_info.proto {#rate_limit_info}

**Path**: `gcommon/v1/common/rate_limit_info.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `RateLimitInfo`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/rate_limit_info.proto
// version: 1.0.0
// guid: f124ed67-fd26-47d4-a6f7-c318a926d5f2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RateLimitInfo {
  // Number of requests remaining in the current window
  int64 remaining = 1 [(buf.validate.field).int64.gte = 0];

  // Total requests allowed in the current window
  int64 limit = 2 [(buf.validate.field).int64.gte = 0];

  // Time when the current rate limit window resets
  google.protobuf.Timestamp reset_time = 3;

  // Duration until the rate limit resets
  google.protobuf.Duration retry_after = 4;
}
```

---

### rate_limit_strategy.proto {#rate_limit_strategy}

**Path**: `gcommon/v1/common/rate_limit_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `RateLimitStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/rate_limit_strategy.proto
// version: 1.0.1
// guid: dcc25ed5-f313-4ae4-8be6-bfbc050afb57

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// RateLimitStrategy enumeration defines available algorithms for rate limiting.
enum RateLimitStrategy {
  RATE_LIMIT_STRATEGY_UNSPECIFIED = 0;
  RATE_LIMIT_STRATEGY_TOKEN_BUCKET = 1;
  RATE_LIMIT_STRATEGY_FIXED_WINDOW = 2;
  RATE_LIMIT_STRATEGY_SLIDING_WINDOW = 3;
  RATE_LIMIT_STRATEGY_LEAKY_BUCKET = 4;
}
```

---

### read_level.proto {#read_level}

**Path**: `gcommon/v1/common/read_level.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ReadLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/read_level.proto
// version: 1.0.1
// guid: 955b2f22-8c91-4d05-98f4-0348ba5bf327

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ReadLevel {
  READ_LEVEL_UNSPECIFIED = 0;
  READ_LEVEL_EVENTUAL = 1; // Eventually consistent reads
  READ_LEVEL_STRONG = 2; // Strongly consistent reads
  READ_LEVEL_BOUNDED_STALENESS = 3; // Bounded staleness reads
  READ_LEVEL_SESSION = 4; // Session consistency
}
```

---

### rebalance_strategy.proto {#rebalance_strategy}

**Path**: `gcommon/v1/common/rebalance_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `RebalanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/rebalance_strategy.proto
// version: 1.0.1
// guid: def27fd7-f689-4591-b5ed-452ee9ca34ea

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RebalanceStrategy {
  REBALANCE_STRATEGY_UNSPECIFIED = 0;
  REBALANCE_STRATEGY_EAGER = 1; // Stop all consumers, then reassign
  REBALANCE_STRATEGY_COOPERATIVE = 2; // Incremental cooperative rebalancing
  REBALANCE_STRATEGY_STATIC = 3; // Static assignment (no rebalancing)
}
```

---

### reference_type.proto {#reference_type}

**Path**: `gcommon/v1/common/reference_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ReferenceType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/reference_type.proto
// version: 1.0.1
// guid: f7734726-4137-4441-b14d-c0c5479a50bd

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### refresh_token.proto {#refresh_token}

**Path**: `gcommon/v1/common/refresh_token.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `RefreshToken`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/refresh_token.proto
// version: 1.0.0
// guid: 19426e54-07ed-40a6-bb1a-739ec97c225f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Refresh token details for token renewal workflows.
 */
message RefreshToken {
  // Refresh token string
  string value = 1;

  // Associated user ID
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // When the refresh token expires
  google.protobuf.Timestamp expires_at = 3 [lazy = true];
}
```

---

### registration_action.proto {#registration_action}

**Path**: `gcommon/v1/common/registration_action.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `RegistrationAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_action.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RegistrationAction indicates what action was taken during registration.
 */
enum RegistrationAction {
  REGISTRATION_ACTION_UNSPECIFIED = 0;
  REGISTRATION_ACTION_CREATED = 1;
  REGISTRATION_ACTION_UPDATED = 2;
  REGISTRATION_ACTION_REPLACED = 3;
  REGISTRATION_ACTION_NO_CHANGE = 4;
}
```

---

### remediation_details.proto {#remediation_details}

**Path**: `gcommon/v1/common/remediation_details.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `RemediationDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/remediation_details.proto
// version: 1.0.0
// guid: 6c9c153d-ad84-44c3-978c-b045473b6345
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RemediationDetails provides information about health remediation actions
 */
message RemediationDetails {
  // Type of remediation action
  string action_type = 1;
  // Description of the remediation action
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];
  // Whether automatic remediation is enabled
  bool auto_remediation_enabled = 3;
  // Maximum number of remediation attempts
  int32 max_attempts = 4;
  // Current attempt count
  int32 current_attempts = 5;
  // Last remediation timestamp
  int64 last_attempt_timestamp = 6;
  // Whether remediation was successful
  bool success = 7;
  // Error message if remediation failed
  string error_message = 8;
}
```

---

### replication_level.proto {#replication_level}

**Path**: `gcommon/v1/common/replication_level.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `ReplicationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/replication_level.proto
// version: 1.0.1
// guid: 3cf5a48e-2f5f-48ed-a2a9-6322f6010c4c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ReplicationLevel {
  REPLICATION_LEVEL_UNSPECIFIED = 0;
  REPLICATION_LEVEL_ONE = 1; // At least one replica
  REPLICATION_LEVEL_QUORUM = 2; // Majority of replicas
  REPLICATION_LEVEL_ALL = 3; // All replicas
}
```

---

### replication_mode.proto {#replication_mode}

**Path**: `gcommon/v1/common/replication_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `ReplicationMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/replication_mode.proto
// file: proto/gcommon/v1/queue/replication_mode.proto
// version: 1.0.1
// guid: 6d7e8f9a-0b1c-2d3e-4f5a-6b7c8d9e0f1a
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Replication mode for queue data across multiple nodes.
 */
enum ReplicationMode {
  // Default unspecified replication mode
  REPLICATION_MODE_UNSPECIFIED = 0;

  // No replication - single node only
  REPLICATION_MODE_NONE = 1;

  // Synchronous replication - wait for all replicas
  REPLICATION_MODE_SYNC = 2;

  // Asynchronous replication - don't wait for replicas
  REPLICATION_MODE_ASYNC = 3;

  // Quorum-based replication - wait for majority
  REPLICATION_MODE_QUORUM = 4;

  // Leader-follower replication
  REPLICATION_MODE_LEADER_FOLLOWER = 5;

  // Master-slave replication (legacy term)
  REPLICATION_MODE_MASTER_SLAVE = 6;
}
```

---

### request_metadata.proto {#request_metadata}

**Path**: `gcommon/v1/common/request_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Messages** (1): `RequestMetadata`

**Imports** (4):

- `gcommon/v1/common/client_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/request_metadata.proto
// version: 1.0.0
// guid: 04acf7f8-db07-4855-a3c6-ec7145088149
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common request metadata for observability and security.
 * Provides standardized metadata that should be included with all
 * requests for distributed tracing, monitoring, and security auditing.
 */
message RequestMetadata {
  // Distributed tracing ID for correlating requests across services
  string trace_id = 1;

  // User ID of the authenticated user making the request
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Correlation ID for grouping related requests in a workflow
  string correlation_id = 3;

  // HTTP headers or gRPC metadata from the original request
  map<string, string> headers = 4;

  // Client application information
  gcommon.v1.common.ClientInfo client = 5;

  // Timestamp when the request was initiated
  google.protobuf.Timestamp timestamp = 6;

  // Session ID if the request is part of a user session
  string session_id = 7;
}
```

---

### resolution.proto {#resolution}

**Path**: `gcommon/v1/common/resolution.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `Resolution`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/resolution.proto
// version: 1.0.1
// guid: 2901b257-89ea-43db-8650-a3b6b48acfdb

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Media resolution enumeration.
enum Resolution {
  RESOLUTION_UNSPECIFIED = 0;
  RESOLUTION_480P = 1;
  RESOLUTION_720P = 2;
  RESOLUTION_1080P = 3;
  RESOLUTION_4K = 4;
}
```

---

### resolution_strategy.proto {#resolution_strategy}

**Path**: `gcommon/v1/common/resolution_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ResolutionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resolution_strategy.proto
// version: 1.0.1
// guid: 2c802dfc-d9ae-4cc2-81ea-ebbb90394cff

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ResolutionStrategy {
  RESOLUTION_STRATEGY_UNSPECIFIED = 0;
  RESOLUTION_STRATEGY_LAST_WRITER_WINS = 1; // Last writer wins
  RESOLUTION_STRATEGY_FIRST_WRITER_WINS = 2; // First writer wins
  RESOLUTION_STRATEGY_MERGE = 3; // Automatic merge
  RESOLUTION_STRATEGY_CUSTOM = 4; // Custom resolution function
  RESOLUTION_STRATEGY_MULTI_VALUE = 5; // Keep all conflicting values
}
```

---

### resource_reference.proto {#resource_reference}

**Path**: `gcommon/v1/common/resource_reference.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `ResourceReference`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/resource_reference.proto
// version: 1.0.0
// guid: 3be67606-1200-41ca-ab13-9197830e75c2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Resource reference for cross-module operations and relationships.
 * Provides a standardized way to reference resources across different
 * GCommon modules with consistent identification and ownership tracking.
 */
message ResourceReference {
  // Resource type identifier (e.g., "user", "config", "queue", "metric")
  string type = 1;

  // Unique resource identifier within the module
  string id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human-readable resource name for display purposes
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Module that owns and manages this resource
  string module = 4;
}
```

---

### resource_status.proto {#resource_status}

**Path**: `gcommon/v1/common/resource_status.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Enums** (1): `ResourceStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/resource_status.proto
// version: 1.0.2
// guid: 789abc12-3456-7890-abcd-ef1234567890

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common resource status enumeration used across all GCommon modules.
 * Provides consistent status reporting for various resources like configurations,
 * cache entries, database connections, etc.
 */
enum ResourceStatus {
  // Default value indicating resource status was not specified
  RESOURCE_STATUS_UNSPECIFIED = 0;

  // Resource is active and available for use
  RESOURCE_STATUS_ACTIVE = 1;

  // Resource is inactive but can be activated
  RESOURCE_STATUS_INACTIVE = 2;

  // Resource is pending activation or processing
  RESOURCE_STATUS_PENDING = 3;

  // Resource has been marked for deletion or is deleted
  RESOURCE_STATUS_DELETED = 4;

  // Resource is in an error state and requires attention
  RESOURCE_STATUS_ERROR = 5;
}
```

---

### response_compression.proto {#response_compression}

**Path**: `gcommon/v1/common/response_compression.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `ResponseCompression`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/response_compression.proto
// version: 1.0.1
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ResponseCompression defines compression options for responses.
 * Specifies compression algorithms for metric response data.
 */
enum ResponseCompression {
  // Unspecified compression
  RESPONSE_COMPRESSION_UNSPECIFIED = 0;

  // No compression
  RESPONSE_COMPRESSION_NONE = 1;

  // GZIP compression
  RESPONSE_COMPRESSION_GZIP = 2;

  // Snappy compression
  RESPONSE_COMPRESSION_SNAPPY = 3;
}
```

---

### response_metadata.proto {#response_metadata}

**Path**: `gcommon/v1/common/response_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Messages** (1): `ResponseMetadata`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/pagination_info.proto`
- `gcommon/v1/common/rate_limit_info.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/response_metadata.proto
// version: 1.0.0
// guid: ef32bc34-15e2-49e7-82a9-0c0577f76c38

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/pagination_info.proto";
import "gcommon/v1/common/rate_limit_info.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ResponseMetadata {
  // Trace ID from the corresponding request for correlation
  string trace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request ID for unique identification of this specific request
  string request_id = 2 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the response was generated
  google.protobuf.Timestamp timestamp = 3;

  // Total processing time for the request
  google.protobuf.Duration processing_time = 4;

  // Service version that processed the request
  string service_version = 5 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Success indicator (true if operation succeeded)
  bool success = 6;

  // Error information if the operation failed
  Error error = 7;

  // Additional metadata specific to the response
  map<string, string> metadata = 8;

  // Rate limiting information
  RateLimitInfo rate_limit = 9;

  // Pagination information for list responses
  CommonPaginationInfo pagination = 10;
}
```

---

### restriction_type.proto {#restriction_type}

**Path**: `gcommon/v1/common/restriction_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `RestrictionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/restriction_type.proto
// version: 1.0.1
// guid: 7444b7aa-6693-418e-ae6b-aa854f8c5400

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### retention_policy.proto {#retention_policy}

**Path**: `gcommon/v1/common/retention_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 48

**Enums** (1): `MetricsRetentionPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_policy.proto
// version: 1.0.1
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// RetentionPolicy represents different retention policies for metrics data
enum MetricsRetentionPolicy {
  // Unspecified retention policy
  RETENTION_POLICY_UNSPECIFIED = 0;

  // Short-term retention (minutes to hours)
  RETENTION_POLICY_SHORT_TERM = 1;

  // Medium-term retention (days to weeks)
  RETENTION_POLICY_MEDIUM_TERM = 2;

  // Long-term retention (months to years)
  RETENTION_POLICY_LONG_TERM = 3;

  // Archive retention (permanent storage)
  RETENTION_POLICY_ARCHIVE = 4;

  // Custom retention policy
  RETENTION_POLICY_CUSTOM = 5;

  // High-frequency data retention (seconds to minutes)
  RETENTION_POLICY_HIGH_FREQUENCY = 6;

  // Low-frequency data retention (hours to days)
  RETENTION_POLICY_LOW_FREQUENCY = 7;

  // Compliance retention (regulatory requirements)
  RETENTION_POLICY_COMPLIANCE = 8;

  // Real-time retention (immediate processing, no storage)
  RETENTION_POLICY_REAL_TIME = 9;

  // Aggregate retention (summary data only)
  RETENTION_POLICY_AGGREGATE = 10;
}
```

---

### retention_policy_info.proto {#retention_policy_info}

**Path**: `gcommon/v1/common/retention_policy_info.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `RetentionPolicyInfo`

**Imports** (3):

- `gcommon/v1/common/metrics_retention_policy_config.proto`
- `gcommon/v1/common/retention_policy.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_policy_info.proto
// version: 1.0.1
// guid: 9b18ea2c-8470-4b90-93e1-437821fdd7f8

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/metrics_retention_policy_config.proto";
import "gcommon/v1/common/retention_policy.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RetentionPolicyInfo combines a retention policy enum with
 * optional configuration details.
 */
message RetentionPolicyInfo {
  // Predefined policy selection
  gcommon.v1.common.MetricsRetentionPolicy policy = 1;

  // Detailed configuration for custom policies
  gcommon.v1.common.MetricsRetentionPolicyConfig config = 2;
}
```

---

### retention_unit.proto {#retention_unit}

**Path**: `gcommon/v1/common/retention_unit.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Enums** (1): `RetentionUnit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_unit.proto
// version: 1.0.1
// guid: a5ffd419-c490-4f14-8c87-dd43c36de9ec
// file: proto/gcommon/v1/metrics/v1/retention_unit.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RetentionUnit defines the units for data retention policies.
 * Used to specify how long metric data should be kept in storage.
 */
enum RetentionUnit {
  // Unspecified retention unit (default)
  RETENTION_UNIT_UNSPECIFIED = 0;

  // Minutes
  RETENTION_UNIT_MINUTES = 1;

  // Hours
  RETENTION_UNIT_HOURS = 2;

  // Days
  RETENTION_UNIT_DAYS = 3;

  // Weeks
  RETENTION_UNIT_WEEKS = 4;

  // Months
  RETENTION_UNIT_MONTHS = 5;

  // Years
  RETENTION_UNIT_YEARS = 6;

  // Forever (no expiration)
  RETENTION_UNIT_FOREVER = 7;

  // Custom duration (specify in seconds)
  RETENTION_UNIT_CUSTOM = 8;
}
```

---

### retry_delay_strategy.proto {#retry_delay_strategy}

**Path**: `gcommon/v1/common/retry_delay_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `RetryDelayStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_delay_strategy.proto
// version: 1.0.1
// guid: e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Strategy for calculating retry delays.
 * Specifies how delays between retry attempts are computed.
 */
enum RetryDelayStrategy {
  // Default unspecified strategy
  RETRY_DELAY_STRATEGY_UNSPECIFIED = 0;

  // Fixed delay between retries
  RETRY_DELAY_STRATEGY_FIXED = 1;

  // Linear backoff (delay increases linearly)
  RETRY_DELAY_STRATEGY_LINEAR = 2;

  // Exponential backoff (delay doubles each time)
  RETRY_DELAY_STRATEGY_EXPONENTIAL = 3;

  // Custom backoff strategy
  RETRY_DELAY_STRATEGY_CUSTOM = 4;
}
```

---

### retry_policy.proto {#retry_policy}

**Path**: `gcommon/v1/common/retry_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Messages** (1): `CommonRetryPolicy`

**Imports** (4):

- `gcommon/v1/common/error_code.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/retry_policy.proto
// version: 1.0.0
// guid: 8377a6ed-7891-46dd-9cc3-88fabf03ddf8
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_code.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Retry policy configuration for resilient operation handling.
 * Defines retry behavior with exponential backoff, jitter,
 * and configurable error handling for robust service interactions.
 */
message CommonRetryPolicy {
  // Maximum number of retry attempts (including initial attempt)
  int32 max_attempts = 1 [(buf.validate.field).int32.gte = 0];

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 2;

  // Maximum delay between retry attempts
  google.protobuf.Duration max_delay = 3;

  // Multiplier for exponential backoff (e.g., 2.0 for doubling)
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Whether to add random jitter to retry timing
  bool enable_jitter = 5;

  // List of error codes that should trigger retries
  repeated ErrorCode retryable_errors = 6 [(buf.validate.field).repeated.min_items = 1];

  // Total timeout for all retry attempts combined
  google.protobuf.Duration total_timeout = 7;
}
```

---

### role.proto {#role}

**Path**: `gcommon/v1/common/role.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `Role`

**Imports** (4):

- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role.proto
// version: 1.0.1
// guid: 456e789a-b1c2-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Role definition for role-based access control (RBAC).
 * Represents a collection of permissions that can be assigned to users.
 * Supports hierarchical roles and metadata for extensibility.
 */
message Role {
  // Unique role identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human-readable role name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Role description explaining its purpose
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Permissions granted by this role
  repeated string permissions = 4;

  // Role metadata for extensibility
  map<string, string> metadata = 5 [lazy = true];

  // Role creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];

  // Role status (active, inactive, etc.)
  ResourceStatus status = 7;
}
```

---

### role_assignment.proto {#role_assignment}

**Path**: `gcommon/v1/common/role_assignment.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Messages** (1): `RoleAssignment`

**Imports** (4):

- `gcommon/v1/common/role_scope.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role_assignment.proto
// version: 1.0.0
// guid: 91143e0d-5e46-40b4-bf89-ab8d51c7be38
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role_scope.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Role assignment entity representing role grants to users.
 * Used for tracking role-based access control assignments.
 * Supports scoped roles and expiration.
 */
message RoleAssignment {
  // Unique assignment identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User ID receiving the role
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID being assigned
  string role_id = 3;

  // Resource the role applies to (optional, for scoped roles)
  string resource = 4;

  // Role scope
  RoleScope scope = 5;

  // Assignment creation timestamp
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];

  // Assignment expiration timestamp (optional)
  google.protobuf.Timestamp expires_at = 7 [lazy = true];

  // User who assigned the role
  string assigned_by_user_id = 8;

  // Assignment metadata
  map<string, string> metadata = 9 [lazy = true];

  // Assignment active flag
  bool active = 10;
}
```

---

### role_metadata.proto {#role_metadata}

**Path**: `gcommon/v1/common/role_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `RoleMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role_metadata.proto
// version: 1.0.0
// guid: 1b935f51-d35c-4113-aa68-03457b4294db

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RoleMetadata provides metadata about role creation and updates.
 */
message RoleMetadata {
  // Timestamp when the role was created
  google.protobuf.Timestamp created_at = 1 [lazy = true, (buf.validate.field).required = true];

  // Timestamp of the last update to the role
  google.protobuf.Timestamp updated_at = 2 [lazy = true];

  // User ID that created the role
  string created_by = 3 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];
}
```

---

### role_scope.proto {#role_scope}

**Path**: `gcommon/v1/common/role_scope.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `RoleScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role_scope.proto
// version: 1.0.1
// guid: d731d279-8c61-4854-ae41-17da08e62494
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Role scope enumeration defining the level at which roles apply.
 * Used for hierarchical role-based access control.
 */
enum RoleScope {
  // Unspecified role scope
  ROLE_SCOPE_UNSPECIFIED = 0;

  // Global system-wide role
  ROLE_SCOPE_GLOBAL = 1;

  // Organization-level role
  ROLE_SCOPE_ORGANIZATION = 2;

  // Project-level role
  ROLE_SCOPE_PROJECT = 3;

  // Team-level role
  ROLE_SCOPE_TEAM = 4;

  // Resource-level role
  ROLE_SCOPE_RESOURCE = 5;
}
```

---

### rotation_frequency.proto {#rotation_frequency}

**Path**: `gcommon/v1/common/rotation_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `RotationFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rotation_frequency.proto
// version: 1.0.1
// guid: 4bb020d8-2763-4ac1-96fc-6210bade7050

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### route_type.proto {#route_type}

**Path**: `gcommon/v1/common/route_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `RouteType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/route_type.proto
// version: 1.0.1
// guid: a655dd19-273c-4cb4-a5ea-71ce983e16cd
//
// RouteType distinguishes different route behaviors.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RouteType {
  ROUTE_TYPE_UNSPECIFIED = 0;
  ROUTE_TYPE_STATIC_FILE = 1;
  ROUTE_TYPE_API = 2;
  ROUTE_TYPE_REDIRECT = 3;
}
```

---

