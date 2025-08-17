# auth_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 4
- **Messages**: 0
- **Services**: 4
- **Enums**: 0

## Files in this Module

- [auth_admin_service.proto](#auth_admin_service)
- [auth_service.proto](#auth_service)
- [authorization_service.proto](#authorization_service)
- [session_service.proto](#session_service)

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)
- [auth_api_1](./auth_api_1.md)
- [auth_api_2](./auth_api_2.md)
- [auth_api_3](./auth_api_3.md)
- [web_api_1](./web_api_1.md)
- [web_api_2](./web_api_2.md)
- [web_api_3](./web_api_3.md)

---

## Detailed Documentation

### auth_admin_service.proto {#auth_admin_service}

**Path**: `pkg/auth/proto/auth_admin_service.proto` **Package**: `gcommon.v1.auth` **Lines**: 78

**Services** (1): `AuthAdminService`

**Imports** (24):

- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`
- `pkg/auth/proto/assign_role_request.proto` → [auth_api_1](./auth_api_1.md#assign_role_request)
- `pkg/auth/proto/create_role_request.proto` → [auth_api_1](./auth_api_1.md#create_role_request)
- `pkg/auth/proto/create_role_response.proto` → [auth_api_1](./auth_api_1.md#create_role_response)
- `pkg/auth/proto/create_user_request.proto` → [auth_api_1](./auth_api_1.md#create_user_request)
- `pkg/auth/proto/create_user_response.proto` → [auth_api_1](./auth_api_1.md#create_user_response)
- `pkg/auth/proto/delete_role_request.proto` → [auth_api_1](./auth_api_1.md#delete_role_request)
- `pkg/auth/proto/delete_user_request.proto` → [auth_api_1](./auth_api_1.md#delete_user_request)
- `pkg/auth/proto/get_system_stats_request.proto` → [auth_api_1](./auth_api_1.md#get_system_stats_request)
- `pkg/auth/proto/get_system_stats_response.proto` → [auth_api_1](./auth_api_1.md#get_system_stats_response)
- `pkg/auth/proto/get_user_request.proto` → [auth_api_2](./auth_api_2.md#get_user_request)
- `pkg/auth/proto/get_user_response.proto` → [auth_api_2](./auth_api_2.md#get_user_response)
- `pkg/auth/proto/invalidate_user_sessions_request.proto` → [auth_api_2](./auth_api_2.md#invalidate_user_sessions_request)
- `pkg/auth/proto/list_roles_request.proto` → [auth_api_2](./auth_api_2.md#list_roles_request)
- `pkg/auth/proto/list_roles_response.proto` → [auth_api_2](./auth_api_2.md#list_roles_response)
- `pkg/auth/proto/list_users_request.proto` → [auth_api_2](./auth_api_2.md#list_users_request)
- `pkg/auth/proto/list_users_response.proto` → [auth_api_2](./auth_api_2.md#list_users_response)
- `pkg/auth/proto/remove_role_request.proto` → [auth_api_2](./auth_api_2.md#remove_role_request)
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)
- `pkg/auth/proto/update_role_request.proto` → [auth_api_2](./auth_api_2.md#update_role_request)
- `pkg/auth/proto/update_role_response.proto` → [auth_api_2](./auth_api_2.md#update_role_response)
- `pkg/auth/proto/update_user_request.proto` → [auth_api_3](./auth_api_3.md#update_user_request)
- `pkg/auth/proto/update_user_response.proto` → [auth_api_3](./auth_api_3.md#update_user_response)

#### Source Code

```protobuf
// file: pkg/auth/proto/services/auth_admin_service.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";
import "pkg/auth/proto/assign_role_request.proto";
import "pkg/auth/proto/create_role_request.proto";
import "pkg/auth/proto/create_role_response.proto";
import "pkg/auth/proto/create_user_request.proto";
import "pkg/auth/proto/create_user_response.proto";
import "pkg/auth/proto/delete_role_request.proto";
import "pkg/auth/proto/delete_user_request.proto";
import "pkg/auth/proto/get_system_stats_request.proto";
import "pkg/auth/proto/get_system_stats_response.proto";
import "pkg/auth/proto/get_user_request.proto";
import "pkg/auth/proto/get_user_response.proto";
import "pkg/auth/proto/invalidate_user_sessions_request.proto";
import "pkg/auth/proto/list_roles_request.proto";
import "pkg/auth/proto/list_roles_response.proto";
import "pkg/auth/proto/list_users_request.proto";
import "pkg/auth/proto/list_users_response.proto";
import "pkg/auth/proto/remove_role_request.proto";
import "pkg/auth/proto/role.proto";
import "pkg/auth/proto/update_role_request.proto";
import "pkg/auth/proto/update_role_response.proto";
import "pkg/auth/proto/update_user_request.proto";
import "pkg/auth/proto/update_user_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Administrative authentication management operations.
 * Provides user management, role assignment, and system configuration.
 */
service AuthAdminService {
  // CreateUser creates a new user account
  rpc CreateUser(CreateUserRequest) returns (CreateUserResponse);

  // UpdateUser updates an existing user account
  rpc UpdateUser(UpdateUserRequest) returns (UpdateUserResponse);

  // DeleteUser removes a user account
  rpc DeleteUser(DeleteUserRequest) returns (google.protobuf.Empty);

  // ListUsers returns paginated list of users
  rpc ListUsers(ListUsersRequest) returns (ListUsersResponse);

  // GetUserDetails returns detailed user information
  rpc GetUser(GetUserRequest) returns (GetUserResponse);

  // AssignRole assigns a role to a user
  rpc AssignRole(AssignRoleRequest) returns (google.protobuf.Empty);

  // RemoveRole removes a role from a user
  rpc RemoveRole(RemoveRoleRequest) returns (google.protobuf.Empty);

  // CreateRole creates a new role
  rpc CreateRole(CreateRoleRequest) returns (CreateRoleResponse);

  // UpdateRole updates an existing role
  rpc UpdateRole(UpdateRoleRequest) returns (UpdateRoleResponse);

  // DeleteRole removes a role
  rpc DeleteRole(DeleteRoleRequest) returns (google.protobuf.Empty);

  // ListRoles returns all available roles
  rpc ListRoles(ListRolesRequest) returns (ListRolesResponse);

  // InvalidateUserSessions invalidates all sessions for a user
  rpc InvalidateUserSessions(InvalidateUserSessionsRequest) returns (google.protobuf.Empty);

  // GetSystemStats returns authentication system statistics
  rpc GetSystemStats(GetSystemStatsRequest) returns (GetSystemStatsResponse);
}

```

---

### auth_service.proto {#auth_service}

**Path**: `pkg/auth/proto/auth_service.proto` **Package**: `gcommon.v1.auth` **Lines**: 62

**Services** (1): `AuthService`

**Imports** (19):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/authenticate_request.proto` → [auth_api_1](./auth_api_1.md#authenticate_request) → [web_api_1](./web_api_1.md#authenticate_request)
- `pkg/auth/proto/authenticate_response.proto` → [auth_api_1](./auth_api_1.md#authenticate_response) → [web_api_1](./web_api_1.md#authenticate_response)
- `pkg/auth/proto/change_password_request.proto` → [auth_api_1](./auth_api_1.md#change_password_request)
- `pkg/auth/proto/change_password_response.proto` → [auth_api_1](./auth_api_1.md#change_password_response)
- `pkg/auth/proto/complete_password_reset_request.proto` → [auth_api_1](./auth_api_1.md#complete_password_reset_request)
- `pkg/auth/proto/complete_password_reset_response.proto` → [auth_api_1](./auth_api_1.md#complete_password_reset_response)
- `pkg/auth/proto/get_user_info_request.proto` → [auth_api_1](./auth_api_1.md#get_user_info_request)
- `pkg/auth/proto/get_user_info_response.proto` → [auth_api_1](./auth_api_1.md#get_user_info_response)
- `pkg/auth/proto/initiate_password_reset_request.proto` → [auth_api_2](./auth_api_2.md#initiate_password_reset_request)
- `pkg/auth/proto/initiate_password_reset_response.proto` → [auth_api_2](./auth_api_2.md#initiate_password_reset_response)
- `pkg/auth/proto/refresh_token_request.proto` → [auth_api_2](./auth_api_2.md#refresh_token_request)
- `pkg/auth/proto/refresh_token_response.proto` → [auth_api_2](./auth_api_2.md#refresh_token_response)
- `pkg/auth/proto/revoke_token_request.proto` → [auth_api_2](./auth_api_2.md#revoke_token_request)
- `pkg/auth/proto/revoke_token_response.proto` → [auth_api_2](./auth_api_2.md#revoke_token_response)
- `pkg/auth/proto/validate_token_request.proto` → [auth_api_3](./auth_api_3.md#validate_token_request)
- `pkg/auth/proto/validate_token_response.proto` → [auth_api_3](./auth_api_3.md#validate_token_response)
- `pkg/auth/proto/verify_credentials_request.proto` → [auth_api_3](./auth_api_3.md#verify_credentials_request)
- `pkg/auth/proto/verify_credentials_response.proto` → [auth_api_3](./auth_api_3.md#verify_credentials_response)

#### Source Code

```protobuf
// file: pkg/auth/proto/services/auth_service.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/authenticate_request.proto";
import "pkg/auth/proto/authenticate_response.proto";
import "pkg/auth/proto/change_password_request.proto";
import "pkg/auth/proto/change_password_response.proto";
import "pkg/auth/proto/complete_password_reset_request.proto";
import "pkg/auth/proto/complete_password_reset_response.proto";
import "pkg/auth/proto/get_user_info_request.proto";
import "pkg/auth/proto/get_user_info_response.proto";
import "pkg/auth/proto/initiate_password_reset_request.proto";
import "pkg/auth/proto/initiate_password_reset_response.proto";
import "pkg/auth/proto/refresh_token_request.proto";
import "pkg/auth/proto/refresh_token_response.proto";
import "pkg/auth/proto/revoke_token_request.proto";
import "pkg/auth/proto/revoke_token_response.proto";
import "pkg/auth/proto/validate_token_request.proto";
import "pkg/auth/proto/validate_token_response.proto";
import "pkg/auth/proto/verify_credentials_request.proto";
import "pkg/auth/proto/verify_credentials_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuthService provides comprehensive authentication capabilities.
 * Handles user authentication, token validation, password management,
 * and credential verification for secure access control.
 */
service AuthService {
  // Authenticate a user with various credential types (password, OAuth, etc.)
  rpc Authenticate(AuthenticateRequest) returns (AuthenticateResponse);

  // Validate an access token and return token information
  rpc ValidateToken(ValidateTokenRequest) returns (ValidateTokenResponse);

  // Verify user credentials without issuing tokens (for validation only)
  rpc VerifyCredentials(VerifyCredentialsRequest) returns (VerifyCredentialsResponse);

  // Refresh an access token using a valid refresh token
  rpc RefreshToken(RefreshTokenRequest) returns (RefreshTokenResponse);

  // Revoke a token (access or refresh) to invalidate it
  rpc RevokeToken(RevokeTokenRequest) returns (RevokeTokenResponse);

  // Get user information from a valid token
  rpc GetUserInfo(GetUserInfoRequest) returns (GetUserInfoResponse);

  // Initiate password reset flow (send reset email/token)
  rpc InitiatePasswordReset(InitiatePasswordResetRequest) returns (InitiatePasswordResetResponse);

  // Complete password reset with validation token
  rpc CompletePasswordReset(CompletePasswordResetRequest) returns (CompletePasswordResetResponse);

  // Change user password (requires current password authentication)
  rpc ChangePassword(ChangePasswordRequest) returns (ChangePasswordResponse);
}

```

---

### authorization_service.proto {#authorization_service}

**Path**: `pkg/auth/proto/authorization_service.proto` **Package**: `gcommon.v1.auth` **Lines**: 33

**Services** (1): `AuthorizationService`

**Imports** (8):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/authorize_request.proto` → [auth_api_1](./auth_api_1.md#authorize_request) → [web_api_1](./web_api_1.md#authorize_request)
- `pkg/auth/proto/authorize_response.proto` → [auth_api_1](./auth_api_1.md#authorize_response) → [web_api_1](./web_api_1.md#authorize_response)
- `pkg/auth/proto/get_user_permissions_request.proto` → [auth_api_1](./auth_api_1.md#get_user_permissions_request)
- `pkg/auth/proto/get_user_permissions_response.proto` → [auth_api_1](./auth_api_1.md#get_user_permissions_response)
- `pkg/auth/proto/get_user_roles_request.proto` → [auth_api_2](./auth_api_2.md#get_user_roles_request)
- `pkg/auth/proto/get_user_roles_response.proto` → [auth_api_2](./auth_api_2.md#get_user_roles_response)
- `pkg/auth/proto/role.proto` → [auth](./auth.md#role)

#### Source Code

```protobuf
// file: pkg/auth/proto/services/authorization_service.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/authorize_request.proto";
import "pkg/auth/proto/authorize_response.proto";
import "pkg/auth/proto/get_user_permissions_request.proto";
import "pkg/auth/proto/get_user_permissions_response.proto";
import "pkg/auth/proto/get_user_roles_request.proto";
import "pkg/auth/proto/get_user_roles_response.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuthorizationService provides authorization and permission management.
 * Handles role-based access control (RBAC), permission checking,
 * and role lifecycle management for fine-grained access control.
 */
service AuthorizationService {
  // Check if a user is authorized for a specific action on a resource
  rpc Authorize(AuthorizeRequest) returns (AuthorizeResponse);

  // Get all permissions granted to a user (direct and via roles)
  rpc GetUserPermissions(GetUserPermissionsRequest) returns (GetUserPermissionsResponse);

  // Get all roles assigned to a user
  rpc GetUserRoles(GetUserRolesRequest) returns (GetUserRolesResponse);
}

```

---

### session_service.proto {#session_service}

**Path**: `pkg/auth/proto/session_service.proto` **Package**: `gcommon.v1.auth` **Lines**: 58

**Services** (1): `SessionService`

**Imports** (18):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/create_session_request.proto` → [auth_api_1](./auth_api_1.md#create_session_request) → [web_api_1](./web_api_1.md#create_session_request)
- `pkg/auth/proto/create_session_response.proto` → [auth_api_1](./auth_api_1.md#create_session_response) → [web_api_1](./web_api_1.md#create_session_response)
- `pkg/auth/proto/delete_session_request.proto` → [auth_api_1](./auth_api_1.md#delete_session_request) → [web_api_1](./web_api_1.md#delete_session_request)
- `pkg/auth/proto/delete_session_response.proto` → [auth_api_1](./auth_api_1.md#delete_session_response) → [web_api_1](./web_api_1.md#delete_session_response)
- `pkg/auth/proto/get_session_request.proto` → [auth_api_1](./auth_api_1.md#get_session_request) → [web_api_2](./web_api_2.md#get_session_request)
- `pkg/auth/proto/get_session_response.proto` → [auth_api_1](./auth_api_1.md#get_session_response) → [web_api_2](./web_api_2.md#get_session_response)
- `pkg/auth/proto/list_sessions_request.proto` → [auth_api_2](./auth_api_2.md#list_sessions_request) → [web_api_2](./web_api_2.md#list_sessions_request)
- `pkg/auth/proto/list_sessions_response.proto` → [auth_api_2](./auth_api_2.md#list_sessions_response) → [web_api_2](./web_api_2.md#list_sessions_response)
- `pkg/auth/proto/list_user_sessions_request.proto` → [auth_api_2](./auth_api_2.md#list_user_sessions_request)
- `pkg/auth/proto/list_user_sessions_response.proto` → [auth_api_2](./auth_api_2.md#list_user_sessions_response)
- `pkg/auth/proto/session.proto` → [auth](./auth.md#session)
- `pkg/auth/proto/terminate_session_request.proto` → [auth_api_2](./auth_api_2.md#terminate_session_request)
- `pkg/auth/proto/terminate_session_response.proto` → [auth_api_2](./auth_api_2.md#terminate_session_response)
- `pkg/auth/proto/update_session_request.proto` → [auth_api_2](./auth_api_2.md#update_session_request) → [web_api_3](./web_api_3.md#update_session_request)
- `pkg/auth/proto/update_session_response.proto` → [auth_api_3](./auth_api_3.md#update_session_response) → [web_api_3](./web_api_3.md#update_session_response)
- `pkg/auth/proto/validate_session_request.proto` → [auth_api_3](./auth_api_3.md#validate_session_request)
- `pkg/auth/proto/validate_session_response.proto` → [auth_api_3](./auth_api_3.md#validate_session_response)

#### Source Code

```protobuf
// file: pkg/auth/proto/services/session_service.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/create_session_request.proto";
import "pkg/auth/proto/create_session_response.proto";
import "pkg/auth/proto/delete_session_request.proto";
import "pkg/auth/proto/delete_session_response.proto";
import "pkg/auth/proto/get_session_request.proto";
import "pkg/auth/proto/get_session_response.proto";
import "pkg/auth/proto/list_sessions_request.proto";
import "pkg/auth/proto/list_sessions_response.proto";
import "pkg/auth/proto/list_user_sessions_request.proto";
import "pkg/auth/proto/list_user_sessions_response.proto";
import "pkg/auth/proto/session.proto";
import "pkg/auth/proto/terminate_session_request.proto";
import "pkg/auth/proto/terminate_session_response.proto";
import "pkg/auth/proto/update_session_request.proto";
import "pkg/auth/proto/update_session_response.proto";
import "pkg/auth/proto/validate_session_request.proto";
import "pkg/auth/proto/validate_session_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * SessionService manages user sessions and session lifecycle.
 * Provides session creation, validation, tracking, and termination
 * for stateful authentication and user activity monitoring.
 */
service SessionService {
  // Create a new session for an authenticated user
  rpc CreateSession(CreateSessionRequest) returns (CreateSessionResponse);

  // Get detailed information about a specific session
  rpc GetSession(GetSessionRequest) returns (GetSessionResponse);

  // Update session information (e.g., refresh activity timestamp)
  rpc UpdateSession(UpdateSessionRequest) returns (UpdateSessionResponse);

  // Validate a session and return session information
  rpc ValidateSession(ValidateSessionRequest) returns (ValidateSessionResponse);

  // Terminate a session (logout)
  rpc TerminateSession(TerminateSessionRequest) returns (TerminateSessionResponse);

  // Delete a specific session
  rpc DeleteSession(DeleteSessionRequest) returns (DeleteSessionResponse);

  // List all active sessions for a user
  rpc ListUserSessions(ListUserSessionsRequest) returns (ListUserSessionsResponse);

  // List all sessions (admin only)
  rpc ListSessions(ListSessionsRequest) returns (ListSessionsResponse);
}

```

---
