# auth_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 53
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 2

## Files in this Module

- [api_key.proto](#api_key)
- [api_key_credentials.proto](#api_key_credentials)
- [assign_role_request.proto](#assign_role_request)
- [assign_role_response.proto](#assign_role_response)
- [authenticate_request.proto](#authenticate_request)
- [authenticate_response.proto](#authenticate_response)
- [authorize_request.proto](#authorize_request)
- [authorize_response.proto](#authorize_response)
- [change_password_request.proto](#change_password_request)
- [change_password_response.proto](#change_password_response)
- [check_permission_request.proto](#check_permission_request)
- [check_permission_response.proto](#check_permission_response)
- [complete_password_reset_request.proto](#complete_password_reset_request)
- [complete_password_reset_response.proto](#complete_password_reset_response)
- [create_permission_request.proto](#create_permission_request)
- [create_role_request.proto](#create_role_request) ⚠️ 1 issues
- [create_role_response.proto](#create_role_response)
- [create_session_request.proto](#create_session_request)
- [create_session_response.proto](#create_session_response)
- [create_user_request.proto](#create_user_request)
- [create_user_response.proto](#create_user_response)
- [delete_permission_request.proto](#delete_permission_request)
- [delete_role_request.proto](#delete_role_request) ⚠️ 1 issues
- [delete_role_response.proto](#delete_role_response)
- [delete_session_request.proto](#delete_session_request)
- [delete_session_response.proto](#delete_session_response)
- [delete_user_request.proto](#delete_user_request)
- [delete_user_response.proto](#delete_user_response)
- [disable_2fa_request.proto](#disable_2fa_request)
- [disable_mfa_request.proto](#disable_mfa_request)
- [disable_mfa_response.proto](#disable_mfa_response)
- [enable_2fa_request.proto](#enable_2fa_request)
- [enable_mfa_request.proto](#enable_mfa_request)
- [enable_mfa_response.proto](#enable_mfa_response)
- [generate_api_key_request.proto](#generate_api_key_request)
- [generate_api_key_response.proto](#generate_api_key_response)
- [get_api_key_request.proto](#get_api_key_request)
- [get_api_key_response.proto](#get_api_key_response)
- [get_permission_request.proto](#get_permission_request)
- [get_permission_response.proto](#get_permission_response)
- [get_role_request.proto](#get_role_request)
- [get_role_response.proto](#get_role_response)
- [get_session_request.proto](#get_session_request)
- [get_session_response.proto](#get_session_response)
- [get_system_stats_request.proto](#get_system_stats_request)
- [get_system_stats_response.proto](#get_system_stats_response)
- [get_user_info_request.proto](#get_user_info_request)
- [get_user_info_response.proto](#get_user_info_response)
- [get_user_permissions_request.proto](#get_user_permissions_request)
- [get_user_permissions_response.proto](#get_user_permissions_response)

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)
- [common](./common.md)

**Modules that depend on this one**:

- [auth_api_3](./auth_api_3.md)
- [auth_services](./auth_services.md)

---

## Detailed Documentation

### api_key.proto {#api_key}

**Path**: `pkg/auth/proto/api_key.proto` **Package**: `gcommon.v1.auth`
**Lines**: 42

**Messages** (1): `APIKey`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/api_key.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-789a-b0c1-d2e3f4a5b6c7

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * APIKey represents a user-issued API key used for authenticating
 * programmatic access. The key value itself should be stored securely
 * and only the hashed form transmitted.
 */
message APIKey {
  // Unique identifier for the API key
  string id = 1;

  // ID of the user this key belongs to
  string user_id = 2;

  // Human readable description for the key
  string description = 3;

  // Hash of the API key value
  string key_hash = 4;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 5 [lazy = true];

  // Optional expiration timestamp
  google.protobuf.Timestamp expires_at = 6 [lazy = true];

  // Whether the key is currently active
  bool active = 7;
}

```

---

### api_key_credentials.proto {#api_key_credentials}

**Path**: `pkg/auth/proto/api_key_credentials.proto` **Package**:
`gcommon.v1.auth` **Lines**: 23

**Messages** (1): `APIKeyCredentials`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/api_key_credentials.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * API key credentials for programmatic authentication.
 * Supports both simple API key and key-pair authentication schemes.
 */
message APIKeyCredentials {
  // API key value used for authentication
  string key = 1;

  // Optional API key ID for key-pair authentication schemes
  // Used when the API key is associated with a specific key identifier
  string key_id = 2;
}

```

---

### assign_role_request.proto {#assign_role_request}

**Path**: `pkg/auth/proto/assign_role_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 54

**Messages** (1): `AssignRoleRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/assign_role_request.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to assign a role to a user.
 * Used for role-based access control management.
 * Grants the specified role permissions to the user.
 *
 * Example usage:
 * - Assigning admin role to a user
 * - Granting specific permissions through role assignment
 * - Managing user access control in the system
 */
message AssignRoleRequest {
  // User ID to assign role to (required)
  // Must be a valid user identifier in the system
  string user_id = 1;

  // Role ID to assign (required)
  // Must be a valid role identifier in the system
  string role_id = 2;

  // Optional organization context for scoped role assignment
  // If not provided, role is assigned globally
  string organization_id = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Audit information for tracking who made the assignment
  string assigned_by = 5;

  // Reason for role assignment (optional)
  string reason = 6;

  // Whether the assignment should be temporary
  bool temporary = 7;

  // Expiration time for temporary assignments
  int64 expires_at = 8;
}

```

---

### assign_role_response.proto {#assign_role_response}

**Path**: `pkg/auth/proto/assign_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `AssignRoleResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/assign_role_response.proto
// file: auth/proto/responses/assign_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message AssignRoleResponse {
  // Assignment success
  bool success = 1;

  // Error message if assignment failed
  string error_message = 2;

  // Effective permissions after assignment
  repeated string effective_permissions = 3;
}

```

---

### authenticate_request.proto {#authenticate_request}

**Path**: `pkg/auth/proto/authenticate_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 44

**Messages** (1): `AuthenticateRequest`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/api_key_credentials.proto`
- `pkg/auth/proto/jwt_credentials.proto` → [auth](./auth.md#jwt_credentials)
- `pkg/auth/proto/oauth2_credentials.proto` →
  [auth](./auth.md#oauth2_credentials)
- `pkg/auth/proto/password_credentials.proto` →
  [auth](./auth.md#password_credentials)
- `pkg/common/proto/client_info.proto` → [common](./common.md#client_info)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/authenticate_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/api_key_credentials.proto";
import "pkg/auth/proto/jwt_credentials.proto";
import "pkg/auth/proto/oauth2_credentials.proto";
import "pkg/auth/proto/password_credentials.proto";
import "pkg/common/proto/client_info.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Authentication request supporting multiple credential types.
 * Uses oneof to ensure only one authentication method is provided per request.
 * Supports comprehensive metadata and client information for security and auditing.
 */
message AuthenticateRequest {
  // Request metadata for tracing, correlation, and auditing
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // Authentication credentials (oneof ensures only one type is used)
  oneof credentials {
    // Username/password authentication
    PasswordCredentials password = 2;
    // API key authentication
    APIKeyCredentials api_key = 3;
    // OAuth2 authorization code flow
    OAuth2Credentials oauth2 = 4;
    // JWT bearer token authentication
    JWTCredentials jwt = 5;
  }

  // Requested authorization scopes
  repeated string scopes = 6;

  // Client information for security and session management
  gcommon.v1.common.ClientInfo client_info = 7 [lazy = true];
}

```

---

### authenticate_response.proto {#authenticate_response}

**Path**: `pkg/auth/proto/authenticate_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 45

**Messages** (1): `AuthenticateResponse`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/session.proto` → [auth](./auth.md#session)
- `pkg/auth/proto/user_info.proto` → [auth](./auth.md#user_info)
- `pkg/common/proto/rate_limit.proto` → [common](./common.md#rate_limit)
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/authenticate_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/session.proto";
import "pkg/auth/proto/user_info.proto";
import "pkg/common/proto/rate_limit.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Authentication response containing access tokens and user information.
 * Follows OAuth2 token response format with additional session and user data.
 * Includes rate limiting information for client throttling.
 */
message AuthenticateResponse {
  // Access token for API authentication (JWT format)
  string access_token = 1;

  // Refresh token for token renewal (opaque format)
  string refresh_token = 2;

  // Token type (always "Bearer" for OAuth2 compliance)
  string token_type = 3;

  // Access token expiration time in seconds
  int32 expires_in = 4;

  // Granted authorization scopes
  repeated string scopes = 5;

  // Complete user information
  UserInfo user_info = 6 [lazy = true];

  // Session information for session management
  Session session = 7 [lazy = true];

  // Rate limiting information for client throttling
  gcommon.v1.common.RateLimit rate_limit = 8 [lazy = true];
}

```

---

### authorize_request.proto {#authorize_request}

**Path**: `pkg/auth/proto/authorize_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 33

**Messages** (1): `AuthorizeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/authorize_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to check if a user is authorized for a specific action.
 * Used for fine-grained access control and permission validation.
 * Supports contextual authorization with additional metadata.
 */
message AuthorizeRequest {
  // Access token for the user being authorized
  string token = 1;

  // Resource being accessed (e.g., "user:123", "project:456")
  string resource = 2;

  // Action being performed (e.g., "read", "write", "delete")
  string action = 3;

  // Additional context for authorization decision
  map<string, string> context = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;
}

```

---

### authorize_response.proto {#authorize_response}

**Path**: `pkg/auth/proto/authorize_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `AuthorizeResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/authorize_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response to authorization request.
 * Contains authorization decision and relevant permission information.
 * Includes denial reason if authorization fails.
 */
message AuthorizeResponse {
  // Whether the user is authorized for the requested action
  bool authorized = 1;

  // Permissions that granted this authorization (if any)
  repeated string permissions = 2;

  // Reason for denial if authorization failed
  string denial_reason = 3;

  // Error information if authorization check failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}

```

---

### change_password_request.proto {#change_password_request}

**Path**: `pkg/auth/proto/change_password_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `ChangePasswordRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/change_password_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to change user password (authenticated).
 * Requires current password for security validation.
 * Used for authenticated password change operations.
 */
message ChangePasswordRequest {
  // Current password for verification
  string current_password = 1;

  // New password to set
  string new_password = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### change_password_response.proto {#change_password_response}

**Path**: `pkg/auth/proto/change_password_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 34

**Messages** (1): `ChangePasswordResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/change_password_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response to password change request.
 * Contains confirmation of password change and any relevant metadata.
 * Provides feedback to the user about the operation status.
 */
message ChangePasswordResponse {
  // Whether the password change was successful
  bool success = 1;

  // Confirmation message
  string message = 2;

  // Error information if password change failed
  gcommon.v1.common.Error error = 3 [lazy = true];

  // Whether all existing sessions should be terminated
  bool sessions_terminated = 4;

  // Number of sessions that were terminated
  int32 terminated_session_count = 5;
}

```

---

### check_permission_request.proto {#check_permission_request}

**Path**: `pkg/auth/proto/check_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 28

**Messages** (1): `CheckPermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/check_permission_request.proto
// version: 1.0.0
// guid: db7aca7d-742a-443b-b641-448ddf4a8518

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to verify that a user possesses a specific permission.
 */
message CheckPermissionRequest {
  // Metadata for tracing and audit purposes
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // User ID being verified
  string user_id = 2;

  // Permission ID to check
  string permission_id = 3;
}

```

---

### check_permission_response.proto {#check_permission_response}

**Path**: `pkg/auth/proto/check_permission_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 21

**Messages** (1): `CheckPermissionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/check_permission_response.proto
// version: 1.0.0
// guid: 909a647b-cd2d-44d1-b612-5ea1e54bda39

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response indicating whether the user has the requested permission.
 */
message CheckPermissionResponse {
  // True if the user possesses the permission
  bool allowed = 1;
}

```

---

### complete_password_reset_request.proto {#complete_password_reset_request}

**Path**: `pkg/auth/proto/complete_password_reset_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `CompletePasswordResetRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/complete_password_reset_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to complete password reset with token.
 * Validates reset token and sets new password.
 * Completes the password recovery flow.
 */
message CompletePasswordResetRequest {
  // Password reset token from initiate request
  string reset_token = 1;

  // New password to set
  string new_password = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### complete_password_reset_response.proto {#complete_password_reset_response}

**Path**: `pkg/auth/proto/complete_password_reset_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 45

**Messages** (1): `CompletePasswordResetResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/complete_password_reset_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * CompletePasswordResetResponse confirms successful password reset completion.
 * Provides confirmation and security information about the password reset
 * operation for audit logging and user notification.
 */
message CompletePasswordResetResponse {
  // User ID whose password was reset
  string user_id = 1;

  // Username or email of the user
  string username = 2;

  // Timestamp when the password was successfully reset
  google.protobuf.Timestamp reset_completed_at = 3;

  // Whether all existing sessions were terminated
  bool sessions_terminated = 4;

  // Number of sessions that were terminated
  int32 terminated_session_count = 5;

  // Whether all tokens for this user were revoked
  bool tokens_revoked = 6;

  // Number of tokens that were revoked
  int32 revoked_token_count = 7;

  // Security notice: next login will require additional verification
  bool requires_additional_verification = 8;

  // Success message for user display
  string message = 9;
}

```

---

### create_permission_request.proto {#create_permission_request}

**Path**: `pkg/auth/proto/create_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `CreatePermissionRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/create_permission_request.proto
// file: auth/proto/requests/create_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message CreatePermissionRequest {
  // Permission name
  string name = 1;

  // Permission description
  string description = 2;

  // Actions this permission grants
  repeated string actions = 3;

  // Resources this permission applies to
  repeated string resources = 4;
}

```

---

### create_role_request.proto {#create_role_request}

**Path**: `pkg/auth/proto/create_role_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `CreateRoleRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 25: Implementation needed - // This is a placeholder file created during
  1-1-1 migration

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/create_role_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to create a new role.
 * Used for role management and access control setup.
 * Creates a role with specified permissions and metadata.
 */
message CreateRoleRequest {
  // Role data to create
  Role role = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements

```

---

### create_role_response.proto {#create_role_response}

**Path**: `pkg/auth/proto/create_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 28

**Messages** (1): `CreateRoleResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/create_role_response.proto
// file: auth/proto/responses/create_role_response.proto
// version: 1.0.0
// guid: 345e6789-a1b2-3c4d-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for creating a new role.
 * Returns the created role with its assigned ID.
 */
message CreateRoleResponse {
  // The created role
  gcommon.v1.auth.Role role = 1;

  // Error information if creation failed
  gcommon.v1.common.Error error = 2;
}

```

---

### create_session_request.proto {#create_session_request}

**Path**: `pkg/auth/proto/create_session_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 34

**Messages** (1): `CreateSessionRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/client_info.proto` → [common](./common.md#client_info)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/create_session_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/client_info.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to create a new user session.
 * Used after successful authentication to establish a session
 * with specific duration and metadata tracking.
 */
message CreateSessionRequest {
  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // User ID for which to create the session
  string user_id = 2;

  // Client information for session tracking
  gcommon.v1.common.ClientInfo client_info = 3 [lazy = true];

  // Session duration in seconds (0 for system default)
  int32 duration_seconds = 4;

  // Additional session metadata
  map<string, string> session_metadata = 5 [lazy = true];
}

```

---

### create_session_response.proto {#create_session_response}

**Path**: `pkg/auth/proto/create_session_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 37

**Messages** (1): `CreateSessionResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/create_session_response.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-1234-567890abcdef

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for session creation operations.
 * Contains session token, expiration details, and user context.
 */
message CreateSessionResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Created session details
  string session_id = 2;
  string access_token = 3;
  string refresh_token = 4;
  google.protobuf.Timestamp expires_at = 5;
  google.protobuf.Timestamp refresh_expires_at = 6;

  // User context
  string user_id = 7;
  repeated string roles = 8;
  repeated string permissions = 9;
}

```

---

### create_user_request.proto {#create_user_request}

**Path**: `pkg/auth/proto/create_user_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 46

**Messages** (1): `CreateUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/create_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to create a new user account.
 */
message CreateUserRequest {
  // Username for the new account
  string username = 1;

  // Email address for the new account
  string email = 2;

  // Password for the new account (should be hashed)
  string password = 3;

  // Full name of the user
  string full_name = 4;

  // Whether the account should be enabled immediately
  bool enabled = 5;

  // Initial roles to assign to the user
  repeated string roles = 6;

  // Additional metadata for the user
  map<string, string> metadata = 7;

  // Whether to require email verification
  bool require_email_verification = 8;

  // Account expiration time (optional)
  google.protobuf.Timestamp expires_at = 9;
}

```

---

### create_user_response.proto {#create_user_response}

**Path**: `pkg/auth/proto/create_user_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 49

**Messages** (1): `CreateUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/create_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174002

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for creating a new user account.
 */
message CreateUserResponse {
  // Unique identifier for the created user
  string user_id = 1;

  // Username of the created account
  string username = 2;

  // Email address of the created account
  string email = 3;

  // Full name of the user
  string full_name = 4;

  // Whether the account is enabled
  bool enabled = 5;

  // Assigned roles
  repeated string roles = 6;

  // When the account was created
  google.protobuf.Timestamp created_at = 7;

  // Whether email verification is required
  bool email_verification_required = 8;

  // Email verification token (if required)
  string verification_token = 9;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 10;
}

```

---

### delete_permission_request.proto {#delete_permission_request}

**Path**: `pkg/auth/proto/delete_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 23

**Messages** (1): `DeletePermissionRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/delete_permission_request.proto
// file: auth/proto/requests/delete_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message DeletePermissionRequest {
  // Permission ID to delete
  string permission_id = 1;

  // Force deletion even if assigned
  bool force = 2;
}

```

---

### delete_role_request.proto {#delete_role_request}

**Path**: `pkg/auth/proto/delete_role_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `DeleteRoleRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 25: Implementation needed - // This is a placeholder file created during
  1-1-1 migration

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/delete_role_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to delete a role.
 * Used for role management and cleanup.
 * Role must not be assigned to any users before deletion.
 */
message DeleteRoleRequest {
  // Role ID to delete
  string role_id = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements

```

---

### delete_role_response.proto {#delete_role_response}

**Path**: `pkg/auth/proto/delete_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `DeleteRoleResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/delete_role_response.proto
// file: auth/proto/responses/delete_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message DeleteRoleResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  string error_message = 2;

  // Number of users/entities that lost this role
  int32 affected_subjects = 3;
}

```

---

### delete_session_request.proto {#delete_session_request}

**Path**: `pkg/auth/proto/delete_session_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 25

**Messages** (1): `DeleteSessionRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/delete_session_request.proto
// file: auth/proto/requests/delete_session_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to delete a session.
 * Used for session cleanup and administrative purposes.
 */
message DeleteSessionRequest {
  // Session ID to delete
  string session_id = 1;

  // Force delete even if session is active (admin only)
  bool force = 2;
}

```

---

### delete_session_response.proto {#delete_session_response}

**Path**: `pkg/auth/proto/delete_session_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `DeleteSessionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/delete_session_response.proto
// file: auth/proto/responses/delete_session_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for session deletion request.
 * Confirms successful deletion or provides error information.
 */
message DeleteSessionResponse {
  // Whether the session was successfully deleted
  bool deleted = 1;

  // Error information if deletion failed
  gcommon.v1.common.Error error = 2;
}

```

---

### delete_user_request.proto {#delete_user_request}

**Path**: `pkg/auth/proto/delete_user_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 33

**Messages** (1): `DeleteUserRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/delete_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174003

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to delete a user account.
 */
message DeleteUserRequest {
  // Unique identifier of the user to delete
  string user_id = 1;

  // Whether to perform a soft delete (mark as deleted) or hard delete
  bool soft_delete = 2;

  // Reason for deletion (optional, for audit purposes)
  string reason = 3;

  // Whether to transfer ownership of resources to another user
  string transfer_to_user_id = 4;

  // Whether to immediately revoke all active sessions
  bool revoke_sessions = 5;
}

```

---

### delete_user_response.proto {#delete_user_response}

**Path**: `pkg/auth/proto/delete_user_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `DeleteUserResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/delete_user_response.proto
// file: auth/proto/responses/delete_user_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message DeleteUserResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  string error_message = 2;

  // Data retention information
  string data_retention_info = 3;
}

```

---

### disable_2fa_request.proto {#disable_2fa_request}

**Path**: `pkg/auth/proto/disable_2fa_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `Disable2FaRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/disable_2fa_request.proto
// file: auth/proto/requests/disable_2fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message Disable2FaRequest {
  // User ID requesting 2FA disable
  string user_id = 1;

  // Current password for verification
  string password = 2;

  // 2FA code for verification
  string verification_code = 3;
}

```

---

### disable_mfa_request.proto {#disable_mfa_request}

**Path**: `pkg/auth/proto/disable_mfa_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `DisableMfaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/mfa_method.proto` → [auth](./auth.md#mfa_method)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/disable_mfa_request.proto
// file: auth/proto/requests/disable_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/mfa_method.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message DisableMfaRequest {
  // User ID requesting MFA disable
  string user_id = 1;

  // Current password for verification
  string password = 2;

  // MFA verification code
  string verification_code = 3;

  // Specific methods to disable (empty = all)
  repeated MfaMethod methods = 4;
}

```

---

### disable_mfa_response.proto {#disable_mfa_response}

**Path**: `pkg/auth/proto/disable_mfa_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `DisableMfaResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/mfa_method.proto` → [auth](./auth.md#mfa_method)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/disable_mfa_response.proto
// file: auth/proto/responses/disable_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/mfa_method.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message DisableMfaResponse {
  // Success status
  bool success = 1;

  // Methods that were disabled
  repeated MfaMethod disabled_methods = 2;

  // Error message if operation failed
  string error_message = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### enable_2fa_request.proto {#enable_2fa_request}

**Path**: `pkg/auth/proto/enable_2fa_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 32

**Messages** (1): `Enable2FaRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/enable_2fa_request.proto
// file: auth/proto/requests/enable_2fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message Enable2FaRequest {
  // User ID requesting 2FA enablement
  string user_id = 1;

  // Phone number for SMS-based 2FA
  string phone_number = 2;

  // Whether to use authenticator app
  bool use_authenticator = 3;

  // Backup codes preference
  bool generate_backup_codes = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### enable_mfa_request.proto {#enable_mfa_request}

**Path**: `pkg/auth/proto/enable_mfa_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `EnableMfaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/mfa_method.proto` → [auth](./auth.md#mfa_method)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/enable_mfa_request.proto
// file: auth/proto/requests/enable_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/mfa_method.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message EnableMfaRequest {
  // User ID requesting MFA enablement
  string user_id = 1;

  // MFA methods to enable
  repeated MfaMethod methods = 2;

  // Primary contact method
  string primary_contact = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### enable_mfa_response.proto {#enable_mfa_response}

**Path**: `pkg/auth/proto/enable_mfa_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 37

**Messages** (2): `EnableMfaResponse`, `MfaSetupInstruction`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/mfa_method.proto` → [auth](./auth.md#mfa_method)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/enable_mfa_response.proto
// file: auth/proto/responses/enable_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/mfa_method.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message EnableMfaResponse {
  // Success status
  bool success = 1;

  // Setup instructions for each method
  repeated MfaSetupInstruction setup_instructions = 2;

  // Error message if operation failed
  string error_message = 3;
}

message MfaSetupInstruction {
  MfaMethod method = 1;
  string instruction = 2;
  string qr_code = 3;
  string secret_key = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### generate_api_key_request.proto {#generate_api_key_request}

**Path**: `pkg/auth/proto/generate_api_key_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 31

**Messages** (1): `GenerateAPIKeyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/generate_api_key_request.proto
// version: 1.0.0
// guid: 5590365e-02f0-4a3d-96eb-15bc615c14ef

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * GenerateAPIKeyRequest requests creation of a new API key for a user.
 */
message GenerateAPIKeyRequest {
  // User ID for whom to generate the key
  string user_id = 1;

  // Optional name/description for the key
  string name = 2;

  // Optional expiration in seconds
  int32 expires_in = 3;

  // Metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}

```

---

### generate_api_key_response.proto {#generate_api_key_response}

**Path**: `pkg/auth/proto/generate_api_key_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 29

**Messages** (1): `GenerateAPIKeyResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/generate_api_key_response.proto
// version: 1.0.0
// guid: 026770a4-919a-4111-818f-ab932e8523ea

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * GenerateAPIKeyResponse returns the newly created API key.
 */
message GenerateAPIKeyResponse {
  // Generated API key value
  string key = 1;

  // Optional key identifier
  string key_id = 2;

  // Response metadata for rate limiting and tracing
  gcommon.v1.common.ResponseMetadata metadata = 3;
}

```

---

### get_api_key_request.proto {#get_api_key_request}

**Path**: `pkg/auth/proto/get_api_key_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `GetApiKeyRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_api_key_request.proto
// file: auth/proto/requests/get_api_key_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message GetApiKeyRequest {
  // API key ID
  string key_id = 1;

  // Include usage statistics
  bool include_stats = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### get_api_key_response.proto {#get_api_key_response}

**Path**: `pkg/auth/proto/get_api_key_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 43

**Messages** (3): `GetApiKeyResponse`, `ApiKeyStats`, `DailyUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/api_key.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_api_key_response.proto
// file: auth/proto/responses/get_api_key_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/api_key.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message GetApiKeyResponse {
  // API key details
  APIKey api_key = 1;

  // Usage statistics if requested
  ApiKeyStats stats = 2;

  // Error message if not found
  string error_message = 3;
}

message ApiKeyStats {
  int32 total_requests = 1;
  int32 successful_requests = 2;
  int32 failed_requests = 3;
  int64 last_used_at = 4;
  repeated DailyUsage daily_usage = 5;
}

message DailyUsage {
  string date = 1; // YYYY-MM-DD format
  int32 request_count = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### get_permission_request.proto {#get_permission_request}

**Path**: `pkg/auth/proto/get_permission_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 25

**Messages** (1): `GetPermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_permission_request.proto
// version: 1.0.0
// guid: 0658829b-708a-480e-942d-42b7ce0e4fdd

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to fetch details about a permission entry.
 */
message GetPermissionRequest {
  // Permission identifier
  string permission_id = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_permission_response.proto {#get_permission_response}

**Path**: `pkg/auth/proto/get_permission_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `GetPermissionResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/permission.proto` → [auth](./auth.md#permission)
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_permission_response.proto
// version: 1.0.0
// guid: fabb3420-290d-4f58-8be9-b363ef1adefd

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/permission.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for a permission retrieval request.
 */
message GetPermissionResponse {
  // Permission details if found
  Permission permission = 1 [lazy = true];

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2 [lazy = true];
}

```

---

### get_role_request.proto {#get_role_request}

**Path**: `pkg/auth/proto/get_role_request.proto` **Package**: `gcommon.v1.auth`
**Lines**: 29

**Messages** (1): `GetRoleRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_role_request.proto
// version: 1.0.0
// guid: 554e7499-0070-40fe-a99c-3428bec2651f

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to retrieve details about a specific role.
 */
message GetRoleRequest {
  // Unique identifier of the role
  string role_id = 1;

  // Include permissions in the response
  bool include_permissions = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### get_role_response.proto {#get_role_response}

**Path**: `pkg/auth/proto/get_role_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `GetRoleResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_role_response.proto
// version: 1.0.0
// guid: 4da329f9-4bb7-4695-85e7-a7083ae930e1

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing role information or an error.
 */
message GetRoleResponse {
  // Role details if found
  Role role = 1 [lazy = true];

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2 [lazy = true];
}

```

---

### get_session_request.proto {#get_session_request}

**Path**: `pkg/auth/proto/get_session_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `GetSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/get_session_request.proto
// version: 1.1.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to get session information.
 * Used to retrieve detailed session data by session ID.
 * Provides session status, metadata, and activity information.
 */
message GetSessionRequest {
  // Session ID to retrieve (required)
  string session_id = 1;

  // Whether to include detailed session activity
  bool include_activity = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### get_session_response.proto {#get_session_response}

**Path**: `pkg/auth/proto/get_session_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 27

**Messages** (1): `GetSessionResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/session.proto` → [auth](./auth.md#session)
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_session_response.proto
// file: auth/proto/responses/get_session_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/session.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for getting session information.
 * Contains session details if found, or error information if not found.
 */
message GetSessionResponse {
  // Session information if found
  Session session = 1;

  // Error information if session not found or access denied
  gcommon.v1.common.Error error = 2;
}

```

---

### get_system_stats_request.proto {#get_system_stats_request}

**Path**: `pkg/auth/proto/get_system_stats_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 22

**Messages** (1): `GetSystemStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_system_stats_request.proto
// version: 1.0.0
// guid: 789eabcd-e1f2-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to get authentication system statistics.
 */
message GetSystemStatsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### get_system_stats_response.proto {#get_system_stats_response}

**Path**: `pkg/auth/proto/get_system_stats_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 38

**Messages** (1): `GetSystemStatsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_system_stats_response.proto
// version: 1.0.0
// guid: 8a9ebcde-f1a2-3b4c-5d6e-7f8a9b0c1d2e

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing authentication system statistics.
 */
message GetSystemStatsResponse {
  // Total number of active users
  int64 active_users = 1;

  // Total number of roles
  int64 total_roles = 2;

  // Total number of active sessions
  int64 active_sessions = 3;

  // Total number of failed login attempts (last 24h)
  int64 failed_logins = 4;

  // Authentication system uptime in seconds
  int64 uptime_seconds = 5;

  // Error information if stats retrieval failed
  gcommon.v1.common.Error error = 6;
}

```

---

### get_user_info_request.proto {#get_user_info_request}

**Path**: `pkg/auth/proto/get_user_info_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 24

**Messages** (1): `GetUserInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_user_info_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to get user information from a valid token.
 * Extracts user profile data from an authenticated session.
 * Used for user profile display and authorization decisions.
 */
message GetUserInfoRequest {
  // Access token to extract user info from
  string token = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_user_info_response.proto {#get_user_info_response}

**Path**: `pkg/auth/proto/get_user_info_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 26

**Messages** (1): `GetUserInfoResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/user.proto` → [auth](./auth.md#user)
- `pkg/auth/proto/user_info.proto` → [auth](./auth.md#user_info)
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_user_info_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/user.proto";
import "pkg/auth/proto/user_info.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing user information from token validation.
 * Provides comprehensive user profile and metadata.
 * Used for user profile display and application authorization.
 */
message GetUserInfoResponse {
  // Complete user information
  UserInfo user_info = 1;

  // Additional user attributes/metadata
  map<string, string> attributes = 2 [lazy = true];
}

```

---

### get_user_permissions_request.proto {#get_user_permissions_request}

**Path**: `pkg/auth/proto/get_user_permissions_request.proto` **Package**:
`gcommon.v1.auth` **Lines**: 24

**Messages** (1): `GetUserPermissionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_user_permissions_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to get all permissions for a user.
 * Returns direct permissions and role-based permissions.
 * Used for user permission auditing and UI authorization.
 */
message GetUserPermissionsRequest {
  // User ID to get permissions for
  string user_id = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_user_permissions_response.proto {#get_user_permissions_response}

**Path**: `pkg/auth/proto/get_user_permissions_response.proto` **Package**:
`gcommon.v1.auth` **Lines**: 30

**Messages** (1): `GetUserPermissionsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/get_user_permissions_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response containing all permissions for a user.
 * Includes direct permissions, role-based permissions, and effective permissions.
 * Provides comprehensive permission information for authorization decisions.
 */
message GetUserPermissionsResponse {
  // Direct permissions assigned to the user
  repeated string permissions = 1;

  // Permissions inherited from roles
  repeated string role_permissions = 2;

  // All effective permissions (union of direct and role permissions)
  repeated string effective_permissions = 3;

  // User's roles (includes permission details)
  repeated Role roles = 4 [lazy = true];
}

```

---
