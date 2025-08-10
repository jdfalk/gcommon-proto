# auth_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 52
- **Services**: 0
- **Enums**: 4
- ⚠️ **Issues**: 4

## Files in this Module

- [get_user_request.proto](#get_user_request)
- [get_user_response.proto](#get_user_response)
- [get_user_roles_request.proto](#get_user_roles_request)
- [get_user_roles_response.proto](#get_user_roles_response)
- [grant_permission_request.proto](#grant_permission_request)
- [grant_permission_response.proto](#grant_permission_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [initiate_password_reset_request.proto](#initiate_password_reset_request)
- [initiate_password_reset_response.proto](#initiate_password_reset_response)
- [invalidate_user_sessions_request.proto](#invalidate_user_sessions_request)
- [list_api_keys_request.proto](#list_api_keys_request)
- [list_api_keys_response.proto](#list_api_keys_response)
- [list_permissions_request.proto](#list_permissions_request)
- [list_permissions_response.proto](#list_permissions_response)
- [list_roles_request.proto](#list_roles_request) ⚠️ 1 issues
- [list_roles_response.proto](#list_roles_response) ⚠️ 1 issues
- [list_sessions_request.proto](#list_sessions_request)
- [list_sessions_response.proto](#list_sessions_response)
- [list_user_sessions_request.proto](#list_user_sessions_request)
- [list_user_sessions_response.proto](#list_user_sessions_response)
- [list_users_request.proto](#list_users_request)
- [list_users_response.proto](#list_users_response)
- [logout_request.proto](#logout_request)
- [logout_response.proto](#logout_response)
- [refresh_token_request.proto](#refresh_token_request)
- [refresh_token_response.proto](#refresh_token_response) ⚠️ 1 issues
- [register_user_request.proto](#register_user_request)
- [register_user_response.proto](#register_user_response)
- [remove_role_request.proto](#remove_role_request)
- [remove_role_response.proto](#remove_role_response)
- [resend_verification_request.proto](#resend_verification_request)
- [reset_password_request.proto](#reset_password_request)
- [reset_password_response.proto](#reset_password_response)
- [revoke_api_key_request.proto](#revoke_api_key_request)
- [revoke_api_key_response.proto](#revoke_api_key_response)
- [revoke_permission_request.proto](#revoke_permission_request)
- [revoke_permission_response.proto](#revoke_permission_response)
- [revoke_role_request.proto](#revoke_role_request)
- [revoke_role_response.proto](#revoke_role_response)
- [revoke_token_request.proto](#revoke_token_request)
- [revoke_token_response.proto](#revoke_token_response)
- [send_verification_email_request.proto](#send_verification_email_request)
- [send_verification_email_response.proto](#send_verification_email_response)
- [terminate_session_request.proto](#terminate_session_request)
- [terminate_session_response.proto](#terminate_session_response)
- [update_permission_request.proto](#update_permission_request)
- [update_role_request.proto](#update_role_request) ⚠️ 1 issues
- [update_role_response.proto](#update_role_response)
- [update_session_request.proto](#update_session_request)

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)
- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [queue_1](./queue_1.md)
- [web](./web.md)

**Modules that depend on this one**:

- [auth_services](./auth_services.md)
- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)

---

## Detailed Documentation

### get_user_request.proto {#get_user_request}

**Path**: `pkg/auth/proto/get_user_request.proto` **Package**: `gcommon.v1.auth`
**Lines**: 30

**Messages** (1): `GetUserRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174008

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to get a specific user's details.
 */
message GetUserRequest {
  // Unique identifier of the user to retrieve
  string user_id = 1;

  // Include detailed information (roles, permissions, etc.)
  bool include_details = 2;

  // Include deleted users in search
  bool include_deleted = 3;

  // Specific fields to return (if empty, all fields returned)
  repeated string fields = 4;
}

```

---

### get_user_response.proto {#get_user_response}

**Path**: `pkg/auth/proto/get_user_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 78

**Messages** (2): `UserDetails`, `GetUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174009

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Detailed user information.
 */
message UserDetails {
  // Unique identifier for the user
  string user_id = 1;

  // Username
  string username = 2;

  // Email address
  string email = 3;

  // Full name
  string full_name = 4;

  // Whether the account is enabled
  bool enabled = 5;

  // Assigned roles
  repeated string roles = 6;

  // User permissions
  repeated string permissions = 7;

  // Additional metadata
  map<string, string> metadata = 8;

  // When the account was created
  google.protobuf.Timestamp created_at = 9;

  // When the account was last updated
  google.protobuf.Timestamp updated_at = 10;

  // Last login time
  google.protobuf.Timestamp last_login_at = 11;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 12;

  // Whether the account is deleted
  bool deleted = 13;

  // Email verification status
  bool email_verified = 14;

  // Multi-factor authentication enabled
  bool mfa_enabled = 15;

  // Number of active sessions
  int32 active_sessions = 16;
}

/**
 * Response for getting user details.
 */
message GetUserResponse {
  // User details
  UserDetails user = 1;

  // Whether the user was found
  bool found = 2;
}

```

---

### get_user_roles_request.proto {#get_user_roles_request}

**Path**: `pkg/auth/proto/get_user_roles_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 25

**Messages** (1): `GetUserRolesRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_user_roles_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to get all roles assigned to a user.
 * Used for user role management and authorization decisions.
 * Returns detailed role information including permissions.
 */
message GetUserRolesRequest {
  // User ID to get roles for
  string user_id = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_user_roles_response.proto {#get_user_roles_response}

**Path**: `pkg/auth/proto/get_user_roles_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 21

**Messages** (1): `GetUserRolesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_user_roles_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing all roles assigned to a user.
 * Provides complete role information including permissions and metadata.
 * Used for role management and authorization display.
 */
message GetUserRolesResponse {
  // All roles assigned to the user
  repeated Role roles = 1;
}

```

---

### grant_permission_request.proto {#grant_permission_request}

**Path**: `pkg/auth/proto/grant_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 34

**Messages** (1): `GrantPermissionRequest`

**Enums** (1): `SubjectType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/grant_permission_request.proto
// file: auth/proto/requests/grant_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message GrantPermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1;

  // Subject type
  enum SubjectType {
    SUBJECT_TYPE_UNSPECIFIED = 0;
    SUBJECT_TYPE_USER = 1;
    SUBJECT_TYPE_ROLE = 2;
  }
  SubjectType subject_type = 2;

  // Permission ID to grant
  string permission_id = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### grant_permission_response.proto {#grant_permission_response}

**Path**: `pkg/auth/proto/grant_permission_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 35

**Messages** (1): `GrantPermissionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/grant_permission_response.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for permission grant operations.
 * Indicates whether the permission was successfully granted.
 */
message GrantPermissionResponse {
  // Whether the permission grant was successful
  bool success = 1;

  // Error message if grant failed
  string error_message = 2;

  // The granted permission ID
  string permission_id = 3;

  // User or entity the permission was granted to
  string grantee_id = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/auth/proto/health_check_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/health_check_request.proto
// version: 1.0.0
// guid: 6fb9b4a2-72b2-4e24-8f41-5611a6f6217b
//
// HealthCheckRequest for the auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * HealthCheckRequest verifies the health of the authentication subsystem.
 */
message HealthCheckRequest {
  // Optional target auth provider.
  string provider = 1;

  // Metadata for tracing.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### health_check_response.proto {#health_check_response}

**Path**: `pkg/auth/proto/health_check_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 32

**Messages** (1): `HealthCheckResponse`

**Imports** (5):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/health_check_response.proto
// version: 1.0.0
// guid: fef90e32-7ccd-4a2d-bcc8-7c86a5f15d36
//
// HealthCheckResponse for the auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * HealthCheckResponse conveys the authentication service health status.
 */
message HealthCheckResponse {
  // Overall health status.
  gcommon.v1.common.HealthStatus status = 1;

  // Response time for the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Error information if unhealthy.
  gcommon.v1.common.Error error = 3 [lazy = true];
}

```

---

### initiate_password_reset_request.proto {#initiate_password_reset_request}

**Path**: `pkg/auth/proto/initiate_password_reset_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 24

**Messages** (1): `InitiatePasswordResetRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/initiate_password_reset_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to initiate password reset flow.
 * Sends reset instructions to user's email or generates reset token.
 * Used for self-service password recovery.
 */
message InitiatePasswordResetRequest {
  // User identifier (username or email)
  string identifier = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### initiate_password_reset_response.proto {#initiate_password_reset_response}

**Path**: `pkg/auth/proto/initiate_password_reset_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `InitiatePasswordResetResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/initiate_password_reset_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response to password reset initiation request.
 * Contains reset token and expiration information.
 * May include additional instructions for the user.
 */
message InitiatePasswordResetResponse {
  // Password reset token (may be sent via email instead)
  string reset_token = 1;

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 2;

  // Message to display to user (e.g., "Check your email")
  string message = 3;
}

```

---

### invalidate_user_sessions_request.proto {#invalidate_user_sessions_request}

**Path**: `pkg/auth/proto/invalidate_user_sessions_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 25

**Messages** (1): `InvalidateUserSessionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/invalidate_user_sessions_request.proto
// version: 1.0.0
// guid: 678e9abc-d1e2-3f4a-5b6c-7d8e9f0a1b2c

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to invalidate all sessions for a user.
 */
message InvalidateUserSessionsRequest {
  // User ID whose sessions should be invalidated
  string user_id = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### list_api_keys_request.proto {#list_api_keys_request}

**Path**: `pkg/auth/proto/list_api_keys_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `ListApiKeysRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/list_api_keys_request.proto
// file: auth/proto/requests/list_api_keys_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message ListApiKeysRequest {
  // User ID to list API keys for
  string user_id = 1;

  // Include expired keys
  bool include_expired = 2;

  // Pagination
  int32 page_size = 3;
  string page_token = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### list_api_keys_response.proto {#list_api_keys_response}

**Path**: `pkg/auth/proto/list_api_keys_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 40

**Messages** (2): `ListApiKeysResponse`, `ApiKey`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/list_api_keys_response.proto
// file: auth/proto/responses/list_api_keys_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message ListApiKeysResponse {
  // List of API keys
  repeated ApiKey api_keys = 1;

  // Next page token
  string next_page_token = 2;

  // Total count
  int32 total_count = 3;
}

message ApiKey {
  string id = 1;
  string name = 2;
  string key_prefix = 3; // Only show prefix for security
  repeated string scopes = 4;
  int64 created_at = 5;
  int64 expires_at = 6;
  int64 last_used_at = 7;
  bool is_active = 8;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### list_permissions_request.proto {#list_permissions_request}

**Path**: `pkg/auth/proto/list_permissions_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 35

**Messages** (1): `ListPermissionsRequest`

**Enums** (1): `SubjectType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/list_permissions_request.proto
// file: auth/proto/requests/list_permissions_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message ListPermissionsRequest {
  // User or role ID to list permissions for
  string subject_id = 1;

  // Subject type
  enum SubjectType {
    SUBJECT_TYPE_UNSPECIFIED = 0;
    SUBJECT_TYPE_USER = 1;
    SUBJECT_TYPE_ROLE = 2;
  }
  SubjectType subject_type = 2;

  // Pagination
  int32 page_size = 3;
  string page_token = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### list_permissions_response.proto {#list_permissions_response}

**Path**: `pkg/auth/proto/list_permissions_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `ListPermissionsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/permission.proto` → [auth](./auth.md#permission)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/list_permissions_response.proto
// file: auth/proto/responses/list_permissions_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/permission.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message ListPermissionsResponse {
  // List of permissions
  repeated Permission permissions = 1;

  // Next page token
  string next_page_token = 2;

  // Total count
  int32 total_count = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### list_roles_request.proto {#list_roles_request}

**Path**: `pkg/auth/proto/list_roles_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 36

**Messages** (1): `ListRolesRequest`

**Imports** (6):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/filter_options.proto` → [common](./common.md#filter_options)
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/sort.proto` → [common](./common.md#sort)

#### ⚠️ Issues Found (1)

- Line 34: Implementation needed - // This is a placeholder file created during
  1-1-1 migration

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/list_roles_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/filter_options.proto";
import "pkg/common/proto/pagination.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/sort.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to list roles with filtering and pagination.
 * Used for role management interfaces and administration.
 * Supports filtering, sorting, and pagination.
 */
message ListRolesRequest {
  // Pagination parameters
  gcommon.v1.common.Pagination pagination = 1;

  // Filter options for role selection
  gcommon.v1.common.FilterOptions filter = 2;

  // Sort options for result ordering
  gcommon.v1.common.SortOptions sort = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements

```

---

### list_roles_response.proto {#list_roles_response}

**Path**: `pkg/auth/proto/list_roles_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 28

**Messages** (1): `ListRolesResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 26: Implementation needed - // This is a placeholder file created during
  1-1-1 migration

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/list_roles_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/paginated_response.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing a list of roles.
 * Includes pagination information for large result sets.
 * Used for role management interfaces and administration.
 */
message ListRolesResponse {
  // List of roles matching the request criteria
  repeated Role roles = 1;

  // Pagination information for the response
  gcommon.v1.common.PaginatedResponse pagination = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements

```

---

### list_sessions_request.proto {#list_sessions_request}

**Path**: `pkg/auth/proto/list_sessions_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `ListSessionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/list_sessions_request.proto
// file: auth/proto/requests/list_sessions_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to list all sessions (admin only).
 * Used for administrative monitoring and management.
 */
message ListSessionsRequest {
  // Pagination parameters
  gcommon.v1.common.Pagination pagination = 1;

  // Filter by user ID (optional)
  string user_id = 2;

  // Filter by session status (optional)
  string status = 3;
}

```

---

### list_sessions_response.proto {#list_sessions_response}

**Path**: `pkg/auth/proto/list_sessions_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `ListSessionsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/session.proto` → [auth](./auth.md#session)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/list_sessions_response.proto
// file: auth/proto/responses/list_sessions_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/session.proto";
import "pkg/common/proto/paginated_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing a list of sessions.
 * Includes pagination information for large result sets.
 */
message ListSessionsResponse {
  // List of sessions
  repeated Session sessions = 1;

  // Pagination information
  gcommon.v1.common.PaginatedResponse pagination = 2;
}

```

---

### list_user_sessions_request.proto {#list_user_sessions_request}

**Path**: `pkg/auth/proto/list_user_sessions_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 86

**Messages** (1): `ListUserSessionsRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/pagination_options.proto` →
  [common](./common.md#pagination_options)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/list_user_sessions_request.proto
// version: 1.0.0
// guid: 8a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/pagination_options.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * ListUserSessionsRequest requests a list of active sessions for a user.
 * Used by administrators to monitor user sessions and by users to view
 * their own active sessions across devices.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListUserSessionsRequest {
  // Required fields (1-10)

  /**
   * The ID of the user whose sessions should be listed.
   * This can be the requesting user's own ID or another user's ID
   * if the requester has appropriate permissions.
   */
  string user_id = 1;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Pagination options for large result sets.
   * Defaults to first 50 sessions if not specified.
   */
  gcommon.v1.common.PaginationOptions pagination = 12;

  /**
   * Filter sessions by status (active, expired, terminated).
   * If not specified, returns all sessions.
   */
  string status_filter = 13;

  /**
   * Filter sessions by device type (web, mobile, api, etc.).
   * If not specified, returns sessions from all device types.
   */
  string device_type_filter = 14;

  /**
   * Only return sessions created after this timestamp.
   * Useful for finding recent sessions.
   */
  google.protobuf.Timestamp created_after = 15;

  /**
   * Only return sessions created before this timestamp.
   * Useful for historical analysis.
   */
  google.protobuf.Timestamp created_before = 16;

  /**
   * Include detailed session information (IP addresses, user agents, etc.).
   * May require additional permissions. Defaults to false.
   */
  bool include_details = 17;

  /**
   * Sort order for results. Valid values: "created_asc", "created_desc",
   * "last_activity_asc", "last_activity_desc". Defaults to "created_desc".
   */
  string sort_order = 18;
}

```

---

### list_user_sessions_response.proto {#list_user_sessions_response}

**Path**: `pkg/auth/proto/list_user_sessions_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 98

**Messages** (1): `ListUserSessionsResponse`

**Imports** (6):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/session_info.proto` → [auth](./auth.md#session_info)
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/paginated_response.proto` →
  [common](./common.md#paginated_response)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/list_user_sessions_response.proto
// version: 1.0.0
// guid: ac4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Auth module types
import "pkg/auth/proto/session_info.proto";
import "pkg/common/proto/error.proto";
// Common types
import "pkg/common/proto/paginated_response.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * ListUserSessionsResponse returns a list of user sessions.
 * Contains session details, pagination information, and metadata
 * for administrative session management and user self-service.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListUserSessionsResponse {
  // Required fields (1-10)

  /**
   * List of session information for the requested user.
   * Empty if no sessions match the filters.
   */
  repeated gcommon.v1.auth.SessionInfo sessions = 1;

  /**
   * Total number of sessions that match the query filters,
   * regardless of pagination. Useful for calculating page counts.
   */
  int32 total_count = 2;

  // Optional fields (11-50)

  /**
   * Pagination information for navigating through large result sets.
   * Contains next_page_token for retrieving additional results.
   */
  gcommon.v1.common.PaginatedResponse pagination = 11;

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 12;

  /**
   * Indicates if the current request's session is included
   * in the results. Useful for UI highlighting.
   */
  bool includes_current_session = 13;

  /**
   * Number of active sessions (not expired/terminated).
   * Subset of total_count for quick status information.
   */
  int32 active_session_count = 14;

  /**
   * User ID for which sessions were retrieved.
   * Echoed from the request for verification.
   */
  string user_id = 15;

  // Status and error fields (61-70)

  /**
   * Error information if the request failed partially
   * or if there were issues retrieving some session data.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   * Useful for caching and staleness detection.
   */
  google.protobuf.Timestamp generated_at = 51;

  /**
   * Timestamp when the session data was last refreshed
   * from the authoritative source.
   */
  google.protobuf.Timestamp data_refreshed_at = 52;
}

```

---

### list_users_request.proto {#list_users_request}

**Path**: `pkg/auth/proto/list_users_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 45

**Messages** (1): `ListUsersRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/list_users_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174004

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to list users with pagination and filtering.
 */
message ListUsersRequest {
  // Page number (starting from 1)
  int32 page = 1;

  // Number of items per page
  int32 page_size = 2;

  // Filter by username (partial match)
  string username_filter = 3;

  // Filter by email (partial match)
  string email_filter = 4;

  // Filter by enabled status
  bool enabled_filter = 5;

  // Filter by role
  string role_filter = 6;

  // Sort field (username, email, created_at, etc.)
  string sort_by = 7;

  // Sort direction (asc or desc)
  string sort_direction = 8;

  // Include deleted users in results
  bool include_deleted = 9;
}

```

---

### list_users_response.proto {#list_users_response}

**Path**: `pkg/auth/proto/list_users_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 41

**Messages** (1): `ListUsersResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/user_info.proto` → [auth](./auth.md#user_info)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/list_users_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174005

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/user_info.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for listing users.
 */
message ListUsersResponse {
  // List of users
  repeated UserInfo users = 1;

  // Total number of users (before pagination)
  int32 total_count = 2;

  // Current page number
  int32 page = 3;

  // Number of items per page
  int32 page_size = 4;

  // Total number of pages
  int32 total_pages = 5;

  // Whether there are more pages
  bool has_next_page = 6;

  // Whether this is not the first page
  bool has_previous_page = 7;
}

```

---

### logout_request.proto {#logout_request}

**Path**: `pkg/auth/proto/logout_request.proto` **Package**: `gcommon.v1.auth`
**Lines**: 26

**Messages** (1): `LogoutRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/logout_request.proto
// version: 1.0.0
// guid: b22adc38-523e-4fbf-8fae-d3f890525589

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

// LogoutRequest ends a user session and invalidates tokens
message LogoutRequest {
  // ID of the session to terminate
  string session_id = 1;

  // Optional user ID for audit purposes
  string user_id = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### logout_response.proto {#logout_response}

**Path**: `pkg/auth/proto/logout_response.proto` **Package**: `gcommon.v1.auth`
**Lines**: 24

**Messages** (1): `LogoutResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/logout_response.proto
// version: 1.0.0
// guid: 96821169-cc26-45e4-a7e3-b81f44ddeb99

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

// LogoutResponse provides the result of a logout request
message LogoutResponse {
  // Whether the logout was successful
  bool success = 1;

  // Optional error information if logout failed
  gcommon.v1.common.Error error = 2;
}

```

---

### refresh_token_request.proto {#refresh_token_request}

**Path**: `pkg/auth/proto/refresh_token_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `RefreshTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/refresh_token_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to refresh an access token using a refresh token.
 * Exchanges a valid refresh token for a new access token.
 * Optionally requests new scopes for the refreshed token.
 */
message RefreshTokenRequest {
  // Refresh token to exchange for new access token
  string refresh_token = 1;

  // Requested scopes for the new access token
  repeated string scopes = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### refresh_token_response.proto {#refresh_token_response}

**Path**: `pkg/auth/proto/refresh_token_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 34

**Messages** (1): `RefreshTokenResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 32: Implementation needed - // This is a placeholder file created during
  1-1-1 migration

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/refresh_token_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response to token refresh request.
 * Contains new access token and potentially new refresh token.
 * Follows OAuth2 token response format.
 */
message RefreshTokenResponse {
  // New access token for API authentication
  string access_token = 1;

  // New refresh token (may be the same as input)
  string refresh_token = 2;

  // Token type (always "Bearer")
  string token_type = 3;

  // Access token expiration time in seconds
  int32 expires_in = 4;

  // Granted scopes for the new access token
  repeated string scopes = 5;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements

```

---

### register_user_request.proto {#register_user_request}

**Path**: `pkg/auth/proto/register_user_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 59

**Messages** (1): `RegisterUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/register_user_request.proto
// version: 1.0.0
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to register a new user account.
 * Creates a new user with the provided credentials and profile information.
 */
message RegisterUserRequest {
  // Username for the new account (required)
  string username = 1;

  // Email address for the new account (required)
  string email = 2;

  // Password for the new account (required)
  string password = 3;

  // First name of the user
  string first_name = 4;

  // Last name of the user
  string last_name = 5;

  // Phone number (optional)
  string phone_number = 6;

  // Initial organization to associate user with (optional)
  string organization_id = 7;

  // Whether email verification is required
  bool require_email_verification = 8;

  // Invitation token (if registering via invitation)
  string invitation_token = 9;

  // Additional user metadata
  map<string, string> metadata = 10;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Terms of service acceptance timestamp
  int64 tos_accepted_at = 12;

  // Privacy policy acceptance timestamp
  int64 privacy_accepted_at = 13;
}

```

---

### register_user_response.proto {#register_user_response}

**Path**: `pkg/auth/proto/register_user_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 35

**Messages** (1): `RegisterUserResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/register_user_response.proto
// file: auth/proto/responses/register_user_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message RegisterUserResponse {
  // Registration success
  bool success = 1;

  // User ID of created user
  string user_id = 2;

  // Whether email verification is required
  bool email_verification_required = 3;

  // Error message if registration failed
  string error_message = 4;

  // Session token if immediate login is allowed
  string session_token = 5;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### remove_role_request.proto {#remove_role_request}

**Path**: `pkg/auth/proto/remove_role_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 28

**Messages** (1): `RemoveRoleRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/remove_role_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to remove a role from a user.
 * Used for role-based access control management.
 * Removes the specified role assignment from the user.
 */
message RemoveRoleRequest {
  // User ID to remove role from
  string user_id = 1;

  // Role ID to remove
  string role_id = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### remove_role_response.proto {#remove_role_response}

**Path**: `pkg/auth/proto/remove_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 50

**Messages** (1): `RemoveRoleResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/remove_role_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * RemoveRoleResponse confirms successful role removal from a user.
 * Provides information about the removal operation including
 * the removed role and removal metadata for audit purposes.
 */
message RemoveRoleResponse {
  // User ID from whom the role was removed
  string user_id = 1;

  // Username of the user
  string username = 2;

  // Role that was removed from the user
  Role role = 3;

  // Timestamp when the role was removed
  google.protobuf.Timestamp removed_at = 4;

  // ID of the admin user who performed the removal
  string removed_by_user_id = 5;

  // Username of the admin who performed the removal
  string removed_by_username = 6;

  // Whether this removal was effective immediately
  bool effective_immediately = 7;

  // Whether the user still has other roles assigned
  bool has_remaining_roles = 8;

  // Count of remaining roles for the user
  int32 remaining_role_count = 9;

  // Success message describing the removal
  string message = 10;
}

```

---

### resend_verification_request.proto {#resend_verification_request}

**Path**: `pkg/auth/proto/resend_verification_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 31

**Messages** (1): `ResendVerificationRequest`

**Enums** (1): `VerificationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/resend_verification_request.proto
// file: auth/proto/requests/resend_verification_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message ResendVerificationRequest {
  // User ID or email address
  string identifier = 1;

  // Verification type
  enum VerificationType {
    VERIFICATION_TYPE_UNSPECIFIED = 0;
    VERIFICATION_TYPE_EMAIL = 1;
    VERIFICATION_TYPE_SMS = 2;
  }
  VerificationType type = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### reset_password_request.proto {#reset_password_request}

**Path**: `pkg/auth/proto/reset_password_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 31

**Messages** (1): `ResetPasswordRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/reset_password_request.proto
// version: 1.0.0
// guid: 79c62bc6-23ed-4b2e-9bb4-4e3091880b22

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * ResetPasswordRequest triggers a password reset for a user.
 */
message ResetPasswordRequest {
  // User ID to reset password for
  string user_id = 1;

  // Temporary reset token provided to the user
  string token = 2;

  // New password to set
  string new_password = 3;

  // Metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### reset_password_response.proto {#reset_password_response}

**Path**: `pkg/auth/proto/reset_password_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `ResetPasswordResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/reset_password_response.proto
// version: 1.0.0
// guid: 9de139b4-5d77-49c3-b18b-7cf12ea5c132

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * ResetPasswordResponse indicates success or failure of password reset.
 */
message ResetPasswordResponse {
  // Whether the reset was successful
  bool success = 1;

  // Optional message describing the result
  string message = 2;

  // Response metadata for rate limiting and tracing
  gcommon.v1.common.ResponseMetadata metadata = 3;
}

```

---

### revoke_api_key_request.proto {#revoke_api_key_request}

**Path**: `pkg/auth/proto/revoke_api_key_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `RevokeApiKeyRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/revoke_api_key_request.proto
// file: auth/proto/requests/revoke_api_key_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message RevokeApiKeyRequest {
  // API key ID to revoke
  string key_id = 1;

  // Reason for revocation
  string reason = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### revoke_api_key_response.proto {#revoke_api_key_response}

**Path**: `pkg/auth/proto/revoke_api_key_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `RevokeApiKeyResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/revoke_api_key_response.proto
// file: auth/proto/responses/revoke_api_key_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message RevokeApiKeyResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2;

  // Revocation timestamp
  int64 revoked_at = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### revoke_permission_request.proto {#revoke_permission_request}

**Path**: `pkg/auth/proto/revoke_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 34

**Messages** (1): `RevokePermissionRequest`

**Enums** (1): `SubjectType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/revoke_permission_request.proto
// file: auth/proto/requests/revoke_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message RevokePermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1;

  // Subject type
  enum SubjectType {
    SUBJECT_TYPE_UNSPECIFIED = 0;
    SUBJECT_TYPE_USER = 1;
    SUBJECT_TYPE_ROLE = 2;
  }
  SubjectType subject_type = 2;

  // Permission ID to revoke
  string permission_id = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### revoke_permission_response.proto {#revoke_permission_response}

**Path**: `pkg/auth/proto/revoke_permission_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 35

**Messages** (1): `RevokePermissionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/revoke_permission_response.proto
// version: 1.0.0
// guid: f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for permission revocation operations.
 * Indicates whether the permission was successfully revoked.
 */
message RevokePermissionResponse {
  // Whether the permission revocation was successful
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2;

  // The revoked permission ID
  string permission_id = 3;

  // User or entity the permission was revoked from
  string revokee_id = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}

```

---

### revoke_role_request.proto {#revoke_role_request}

**Path**: `pkg/auth/proto/revoke_role_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 43

**Messages** (1): `RevokeRoleRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/revoke_role_request.proto
// version: 1.0.0
// guid: a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to revoke a role from a user.
 * Used for role-based access control management.
 * Removes the specified role permissions from the user.
 */
message RevokeRoleRequest {
  // User ID to revoke role from (required)
  string user_id = 1;

  // Role ID to revoke (required)
  string role_id = 2;

  // Optional organization context for scoped role revocation
  string organization_id = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Audit information for tracking who made the revocation
  string revoked_by = 5;

  // Reason for role revocation (optional)
  string reason = 6;

  // Whether to force revocation even if user has dependencies
  bool force = 7;
}

```

---

### revoke_role_response.proto {#revoke_role_response}

**Path**: `pkg/auth/proto/revoke_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `RevokeRoleResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/revoke_role_response.proto
// file: auth/proto/responses/revoke_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message RevokeRoleResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2;

  // Remaining permissions after revocation
  repeated string remaining_permissions = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### revoke_token_request.proto {#revoke_token_request}

**Path**: `pkg/auth/proto/revoke_token_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `RevokeTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/revoke_token_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to revoke a token (access or refresh).
 * Invalidates the specified token and prevents further use.
 * Used for logout operations and security revocation.
 */
message RevokeTokenRequest {
  // Token to revoke (access or refresh token)
  string token = 1;

  // Token type hint ("access_token" or "refresh_token")
  string token_type_hint = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### revoke_token_response.proto {#revoke_token_response}

**Path**: `pkg/auth/proto/revoke_token_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 36

**Messages** (1): `RevokeTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/revoke_token_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * RevokeTokenResponse confirms successful token revocation.
 * Provides information about the revoked token and revocation timestamp
 * for audit logging and confirmation purposes.
 */
message RevokeTokenResponse {
  // Token ID that was revoked
  string token_id = 1;

  // Type of token that was revoked (access, refresh, etc.)
  string token_type = 2;

  // Timestamp when the token was revoked
  google.protobuf.Timestamp revoked_at = 3;

  // User ID associated with the revoked token
  string user_id = 4;

  // Reason for revocation (logout, security, expiry, etc.)
  string revocation_reason = 5;

  // Whether this was the last token for the user session
  bool last_token_in_session = 6;
}

```

---

### send_verification_email_request.proto {#send_verification_email_request}

**Path**: `pkg/auth/proto/send_verification_email_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `SendVerificationEmailRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/send_verification_email_request.proto
// file: auth/proto/requests/send_verification_email_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message SendVerificationEmailRequest {
  // User ID or email address
  string identifier = 1;

  // Template to use for email
  string template = 2;

  // Additional context data
  map<string, string> context = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### send_verification_email_response.proto {#send_verification_email_response}

**Path**: `pkg/auth/proto/send_verification_email_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `SendVerificationEmailResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/send_verification_email_response.proto
// file: auth/proto/responses/send_verification_email_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message SendVerificationEmailResponse {
  // Send success
  bool sent = 1;

  // Error message if send failed
  string error_message = 2;

  // Token expiry time
  int64 expires_at = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### terminate_session_request.proto {#terminate_session_request}

**Path**: `pkg/auth/proto/terminate_session_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 99

**Messages** (1): `TerminateSessionRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/terminate_session_request.proto
// version: 1.0.0
// guid: 9b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * TerminateSessionRequest terminates one or more user sessions.
 * Used by administrators to forcibly terminate user sessions,
 * or by users to terminate their own sessions (e.g., "log out all devices").
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message TerminateSessionRequest {
  // Required fields (1-10)

  /**
   * The ID of the user whose session(s) should be terminated.
   * This can be the requesting user's own ID or another user's ID
   * if the requester has appropriate permissions.
   */
  string user_id = 1;

  /**
   * Specific session IDs to terminate. If empty, the termination
   * scope is determined by other filters.
   */
  repeated string session_ids = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Terminate all sessions for this user. When true, ignores
   * session_ids and other filters. Requires admin permissions
   * unless user is terminating their own sessions.
   */
  bool terminate_all = 12;

  /**
   * Only terminate sessions matching this device type filter.
   * Valid values: "web", "mobile", "api", "desktop".
   * If not specified, applies to all device types.
   */
  string device_type_filter = 13;

  /**
   * Only terminate sessions created before this timestamp.
   * Useful for terminating old/stale sessions.
   */
  google.protobuf.Timestamp created_before = 14;

  /**
   * Only terminate sessions with last activity before this timestamp.
   * Useful for terminating inactive sessions.
   */
  google.protobuf.Timestamp last_activity_before = 15;

  /**
   * Exclude the current session (the one making this request)
   * from termination. Defaults to true to prevent self-logout.
   */
  bool exclude_current_session = 16;

  /**
   * Reason for termination (for audit logging).
   * Examples: "user_logout", "admin_action", "security_breach", "policy_violation".
   */
  string termination_reason = 17;

  /**
   * Send notification to user about session termination.
   * May include email, push notification, etc. Defaults to true.
   */
  bool send_notification = 18;

  /**
   * Force immediate termination without graceful cleanup.
   * Use with caution as it may result in data loss. Defaults to false.
   */
  bool force_immediate = 19;
}

```

---

### terminate_session_response.proto {#terminate_session_response}

**Path**: `pkg/auth/proto/terminate_session_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 48

**Messages** (1): `TerminateSessionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/terminate_session_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * TerminateSessionResponse confirms successful session termination.
 * Provides information about the terminated session and cleanup operations
 * for audit logging and confirmation purposes.
 */
message TerminateSessionResponse {
  // Session ID that was terminated
  string session_id = 1;

  // User ID whose session was terminated
  string user_id = 2;

  // Username of the user
  string username = 3;

  // Timestamp when the session was terminated
  google.protobuf.Timestamp terminated_at = 4;

  // Reason for termination (logout, timeout, security, admin, etc.)
  string termination_reason = 5;

  // Whether any associated tokens were revoked
  bool tokens_revoked = 6;

  // Number of tokens that were revoked
  int32 revoked_token_count = 7;

  // Whether this was a forced termination (by admin or security)
  bool forced_termination = 8;

  // Number of remaining active sessions for this user
  int32 remaining_session_count = 9;

  // Success message describing the termination
  string message = 10;
}

```

---

### update_permission_request.proto {#update_permission_request}

**Path**: `pkg/auth/proto/update_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 50

**Messages** (1): `UpdatePermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/update_permission_request.proto
// version: 1.0.0
// guid: e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to update an existing permission.
 * Allows modification of permission properties and constraints.
 */
message UpdatePermissionRequest {
  // Permission ID to update (required)
  string permission_id = 1;

  // New permission name (optional)
  string name = 2;

  // New permission description (optional)
  string description = 3;

  // New resource this permission applies to (optional)
  string resource = 4;

  // New action this permission allows (optional)
  string action = 5;

  // New conditions for the permission (optional)
  repeated string conditions = 6;

  // Whether the permission should be active (optional)
  bool active = 7;

  // Fields to update (field mask)
  repeated string update_mask = 8;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 9;

  // Reason for the update
  string reason = 10;
}

```

---

### update_role_request.proto {#update_role_request}

**Path**: `pkg/auth/proto/update_role_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 31

**Messages** (1): `UpdateRoleRequest`

**Imports** (4):

- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 29: Implementation needed - // This is a placeholder file created during
  1-1-1 migration

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/update_role_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to update an existing role.
 * Used for role management and permission modification.
 * Supports partial updates using field mask.
 */
message UpdateRoleRequest {
  // Role data with updates
  Role role = 1;

  // Field mask specifying which fields to update
  google.protobuf.FieldMask update_mask = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements

```

---

### update_role_response.proto {#update_role_response}

**Path**: `pkg/auth/proto/update_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `UpdateRoleResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/update_role_response.proto
// file: auth/proto/responses/update_role_response.proto
// version: 1.0.0
// guid: 567e89ab-c1d2-3e4f-5a6b-7c8d9e0f1a2b

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for updating a role.
 * Returns the updated role.
 */
message UpdateRoleResponse {
  // The updated role
  gcommon.v1.auth.Role role = 1;

  // Error information if update failed
  gcommon.v1.common.Error error = 2;
}

```

---

### update_session_request.proto {#update_session_request}

**Path**: `pkg/auth/proto/update_session_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `UpdateSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/update_session_request.proto
// file: auth/proto/requests/update_session_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to update session information.
 * Used to refresh session activity or update session metadata.
 */
message UpdateSessionRequest {
  // Session ID to update
  string session_id = 1;

  // Updated session metadata
  map<string, string> metadata = 2;

  // New expiration time (optional)
  google.protobuf.Timestamp expires_at = 3;
}

```

---
