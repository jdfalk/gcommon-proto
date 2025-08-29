# Common Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 9
- **Services**: 9

## Table of Contents

### Services

- [`AuthAdminService`](#auth_admin_service) - from auth_admin_service.proto
- [`AuthService`](#auth_service) - from auth_service.proto
- [`AuthorizationService`](#authorization_service) - from authorization_service.proto
- [`HealthAdminService`](#health_admin_service) - from health_admin_service.proto
- [`HealthService`](#health_service) - from health_service.proto
- [`LogAdminService`](#log_admin_service) - from log_admin_service.proto
- [`LogService`](#log_service) - from log_service.proto
- [`NotificationService`](#notification_service) - from notification_service.proto
- [`SessionService`](#session_service) - from session_service.proto

### Files in this Module

- [auth_admin_service.proto](#auth_admin_service)
- [auth_service.proto](#auth_service)
- [authorization_service.proto](#authorization_service)
- [health_admin_service.proto](#health_admin_service)
- [health_service.proto](#health_service)
- [log_admin_service.proto](#log_admin_service)
- [log_service.proto](#log_service)
- [notification_service.proto](#notification_service)
- [session_service.proto](#session_service)

---


## Services Documentation

### auth_admin_service.proto {#auth_admin_service}

**Path**: `gcommon/v1/common/auth_admin_service.proto` **Package**: `gcommon.v1.common` **Lines**: 78

**Services** (1): `AuthAdminService`

**Imports** (23):

- `gcommon/v1/common/assign_role_request.proto`
- `gcommon/v1/common/create_role_request.proto`
- `gcommon/v1/common/create_role_response.proto`
- `gcommon/v1/common/create_user_request.proto`
- `gcommon/v1/common/create_user_response.proto`
- `gcommon/v1/common/delete_role_request.proto`
- `gcommon/v1/common/delete_user_request.proto`
- `gcommon/v1/common/get_system_stats_request.proto`
- `gcommon/v1/common/get_system_stats_response.proto`
- `gcommon/v1/common/get_user_request.proto`
- `gcommon/v1/common/get_user_response.proto`
- `gcommon/v1/common/invalidate_user_sessions_request.proto`
- `gcommon/v1/common/list_roles_request.proto`
- `gcommon/v1/common/list_roles_response.proto`
- `gcommon/v1/common/list_users_request.proto`
- `gcommon/v1/common/list_users_response.proto`
- `gcommon/v1/common/remove_role_request.proto`
- `gcommon/v1/common/update_role_request.proto`
- `gcommon/v1/common/update_role_response.proto`
- `gcommon/v1/common/update_user_request.proto`
- `gcommon/v1/common/update_user_response.proto`
- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_admin_service.proto
// version: 1.0.1
// guid: 253654c0-690d-48e1-b4fd-24d978958200
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/assign_role_request.proto";
import "gcommon/v1/common/create_role_request.proto";
import "gcommon/v1/common/create_role_response.proto";
import "gcommon/v1/common/create_user_request.proto";
import "gcommon/v1/common/create_user_response.proto";
import "gcommon/v1/common/delete_role_request.proto";
import "gcommon/v1/common/delete_user_request.proto";
import "gcommon/v1/common/get_system_stats_request.proto";
import "gcommon/v1/common/get_system_stats_response.proto";
import "gcommon/v1/common/get_user_request.proto";
import "gcommon/v1/common/get_user_response.proto";
import "gcommon/v1/common/invalidate_user_sessions_request.proto";
import "gcommon/v1/common/list_roles_request.proto";
import "gcommon/v1/common/list_roles_response.proto";
import "gcommon/v1/common/list_users_request.proto";
import "gcommon/v1/common/list_users_response.proto";
import "gcommon/v1/common/remove_role_request.proto";
import "gcommon/v1/common/update_role_request.proto";
import "gcommon/v1/common/update_role_response.proto";
import "gcommon/v1/common/update_user_request.proto";
import "gcommon/v1/common/update_user_response.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/auth_service.proto` **Package**: `gcommon.v1.common` **Lines**: 63

**Services** (1): `AuthService`

**Imports** (19):

- `gcommon/v1/common/authenticate_request.proto`
- `gcommon/v1/common/authenticate_response.proto`
- `gcommon/v1/common/change_password_request.proto`
- `gcommon/v1/common/change_password_response.proto`
- `gcommon/v1/common/complete_password_reset_request.proto`
- `gcommon/v1/common/complete_password_reset_response.proto`
- `gcommon/v1/common/get_user_info_request.proto`
- `gcommon/v1/common/get_user_info_response.proto`
- `gcommon/v1/common/initiate_password_reset_request.proto`
- `gcommon/v1/common/initiate_password_reset_response.proto`
- `gcommon/v1/common/refresh_token_request.proto`
- `gcommon/v1/common/refresh_token_response.proto`
- `gcommon/v1/common/revoke_token_request.proto`
- `gcommon/v1/common/revoke_token_response.proto`
- `gcommon/v1/common/validate_token_request.proto`
- `gcommon/v1/common/validate_token_response.proto`
- `gcommon/v1/common/verify_credentials_request.proto`
- `gcommon/v1/common/verify_credentials_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_service.proto
// version: 1.0.1
// guid: 9f3ae39c-bbe9-4615-b0ce-944a7b3fbe86
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/authenticate_request.proto";
import "gcommon/v1/common/authenticate_response.proto";
import "gcommon/v1/common/change_password_request.proto";
import "gcommon/v1/common/change_password_response.proto";
import "gcommon/v1/common/complete_password_reset_request.proto";
import "gcommon/v1/common/complete_password_reset_response.proto";
import "gcommon/v1/common/get_user_info_request.proto";
import "gcommon/v1/common/get_user_info_response.proto";
import "gcommon/v1/common/initiate_password_reset_request.proto";
import "gcommon/v1/common/initiate_password_reset_response.proto";
import "gcommon/v1/common/refresh_token_request.proto";
import "gcommon/v1/common/refresh_token_response.proto";
import "gcommon/v1/common/revoke_token_request.proto";
import "gcommon/v1/common/revoke_token_response.proto";
import "gcommon/v1/common/validate_token_request.proto";
import "gcommon/v1/common/validate_token_response.proto";
import "gcommon/v1/common/verify_credentials_request.proto";
import "gcommon/v1/common/verify_credentials_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthService provides comprehensive authentication capabilities.
 * Handles user authentication, token validation, password management,
 * and credential verification for secure access control.
 */
service AuthService {
  // Authenticate a user with various credential types (password, OAuth, etc.)
  rpc Authenticate(AuthAuthenticateRequest) returns (AuthAuthenticateResponse);

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

**Path**: `gcommon/v1/common/authorization_service.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Services** (1): `AuthorizationService`

**Imports** (7):

- `gcommon/v1/common/authorize_request.proto`
- `gcommon/v1/common/authorize_response.proto`
- `gcommon/v1/common/get_user_permissions_request.proto`
- `gcommon/v1/common/get_user_permissions_response.proto`
- `gcommon/v1/common/get_user_roles_request.proto`
- `gcommon/v1/common/get_user_roles_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authorization_service.proto
// version: 1.0.1
// guid: b686e721-a0f4-4ad1-8bfb-b6c773d0d9eb
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/authorize_request.proto";
import "gcommon/v1/common/authorize_response.proto";
import "gcommon/v1/common/get_user_permissions_request.proto";
import "gcommon/v1/common/get_user_permissions_response.proto";
import "gcommon/v1/common/get_user_roles_request.proto";
import "gcommon/v1/common/get_user_roles_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthorizationService provides authorization and permission management.
 * Handles role-based access control (RBAC), permission checking,
 * and role lifecycle management for fine-grained access control.
 */
service AuthorizationService {
  // Check if a user is authorized for a specific action on a resource
  rpc Authorize(AuthAuthorizeRequest) returns (AuthAuthorizeResponse);

  // Get all permissions granted to a user (direct and via roles)
  rpc GetUserPermissions(GetUserPermissionsRequest) returns (GetUserPermissionsResponse);

  // Get all roles assigned to a user
  rpc GetUserRoles(GetUserRolesRequest) returns (GetUserRolesResponse);
}
```

---

### health_admin_service.proto {#health_admin_service}

**Path**: `gcommon/v1/common/health_admin_service.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Services** (1): `HealthAdminService`

**Imports** (13):

- `gcommon/v1/common/configure_alerting_request.proto`
- `gcommon/v1/common/configure_alerting_response.proto`
- `gcommon/v1/common/disable_check_request.proto`
- `gcommon/v1/common/disable_check_response.proto`
- `gcommon/v1/common/enable_check_request.proto`
- `gcommon/v1/common/enable_check_response.proto`
- `gcommon/v1/common/reset_health_stats_request.proto`
- `gcommon/v1/common/reset_health_stats_response.proto`
- `gcommon/v1/common/run_check_request.proto`
- `gcommon/v1/common/run_check_response.proto`
- `gcommon/v1/common/set_health_request.proto`
- `gcommon/v1/common/set_health_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_admin_service.proto
// version: 1.0.1
// guid: 852f060f-cb4f-4a6c-9eb5-1a8cbdf34351
// file: proto/gcommon/v1/common/health_admin_service.proto
//
// Administrative service definitions for health module
//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/configure_alerting_request.proto";
import "gcommon/v1/common/configure_alerting_response.proto";
import "gcommon/v1/common/disable_check_request.proto";
import "gcommon/v1/common/disable_check_response.proto";
import "gcommon/v1/common/enable_check_request.proto";
import "gcommon/v1/common/enable_check_response.proto";
import "gcommon/v1/common/reset_health_stats_request.proto";
import "gcommon/v1/common/reset_health_stats_response.proto";
import "gcommon/v1/common/run_check_request.proto";
import "gcommon/v1/common/run_check_response.proto";
import "gcommon/v1/common/set_health_request.proto";
import "gcommon/v1/common/set_health_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthAdminService provides administrative health operations
 * such as enabling or disabling checks and configuring alerting.
 */
service HealthAdminService {
  // Configure alerting for a check or service
  rpc ConfigureAlerting(ConfigureAlertingRequest) returns (ConfigureAlertingResponse);

  // Enable a previously disabled check
  rpc EnableCheck(EnableCheckRequest) returns (EnableCheckResponse);

  // Disable an existing check
  rpc DisableCheck(DisableCheckRequest) returns (DisableCheckResponse);

  // Manually run a health check
  rpc RunCheck(RunCheckRequest) returns (RunCheckResponse);

  // Reset stored health statistics
  rpc ResetHealthStats(ResetHealthStatsRequest) returns (ResetHealthStatsResponse);

  // Manually set the overall health status
  rpc SetHealth(SetHealthRequest) returns (SetHealthResponse);
}
```

---

### health_service.proto {#health_service}

**Path**: `gcommon/v1/common/health_service.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Services** (1): `HealthService`

**Imports** (17):

- `gcommon/v1/common/get_health_metrics_request.proto`
- `gcommon/v1/common/get_health_metrics_response.proto`
- `gcommon/v1/common/get_service_health_request.proto`
- `gcommon/v1/common/get_service_health_response.proto`
- `gcommon/v1/common/health_check_all_request.proto`
- `gcommon/v1/common/health_check_all_response.proto`
- `gcommon/v1/common/health_check_request.proto`
- `gcommon/v1/common/health_check_response.proto`
- `gcommon/v1/common/list_services_request.proto`
- `gcommon/v1/common/list_services_response.proto`
- `gcommon/v1/common/register_check_request.proto`
- `gcommon/v1/common/register_check_response.proto`
- `gcommon/v1/common/unregister_check_request.proto`
- `gcommon/v1/common/unregister_check_response.proto`
- `gcommon/v1/common/watch_request.proto`
- `gcommon/v1/common/watch_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_service.proto
// version: 1.0.1
// guid: 81fada90-f4d6-4bfc-9756-b7b144fcbdf6
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/get_health_metrics_request.proto";
import "gcommon/v1/common/get_health_metrics_response.proto";
import "gcommon/v1/common/get_service_health_request.proto";
import "gcommon/v1/common/get_service_health_response.proto";
import "gcommon/v1/common/health_check_all_request.proto";
import "gcommon/v1/common/health_check_all_response.proto";
import "gcommon/v1/common/health_check_request.proto";
import "gcommon/v1/common/health_check_response.proto";
import "gcommon/v1/common/list_services_request.proto";
import "gcommon/v1/common/list_services_response.proto";
import "gcommon/v1/common/register_check_request.proto";
import "gcommon/v1/common/register_check_response.proto";
import "gcommon/v1/common/unregister_check_request.proto";
import "gcommon/v1/common/unregister_check_response.proto";
import "gcommon/v1/common/watch_request.proto";
import "gcommon/v1/common/watch_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthService provides comprehensive health checking capabilities.
 * Supports individual check status, system-wide health, and health monitoring.
 */
service HealthService {
  // Check performs a health check for a specific service
  rpc Check(HealthHealthCheckRequest) returns (HealthHealthCheckResponse);

  // CheckAll performs comprehensive health checks for all services
  rpc CheckAll(HealthCheckAllRequest) returns (HealthCheckAllResponse);

  // Watch returns a stream of health check results
  rpc Watch(HealthWatchRequest) returns (stream WatchResponse);

  // GetServiceHealth returns health status for a service
  rpc GetServiceHealth(GetServiceHealthRequest) returns (GetServiceHealthResponse);

  // ListServices returns all monitored services
  rpc ListServices(ListServicesRequest) returns (ListServicesResponse);

  // RegisterCheck registers a new health check
  rpc RegisterCheck(RegisterCheckRequest) returns (RegisterCheckResponse);

  // UnregisterCheck removes a health check
  rpc UnregisterCheck(UnregisterCheckRequest) returns (UnregisterCheckResponse);

  // GetHealthMetrics returns health metrics and statistics
  rpc GetHealthMetrics(GetHealthMetricsRequest) returns (GetHealthMetricsResponse);
}
```

---

### log_admin_service.proto {#log_admin_service}

**Path**: `gcommon/v1/common/log_admin_service.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Services** (1): `LogAdminService`

**Imports** (3):

- `gcommon/v1/common/configure_logger_request.proto`
- `gcommon/v1/common/configure_logger_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_admin_service.proto
// version: 1.0.1
// guid: 4f5e6d7c-8b9a-0312-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/configure_logger_request.proto";
import "gcommon/v1/common/configure_logger_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * LogAdminService provides log administration operations for
 * managing logger configurations and settings.
 */
service LogAdminService {
  // Configure logger settings
  rpc ConfigureLogger(gcommon.v1.common.ConfigureLoggerRequest) returns (gcommon.v1.common.ConfigureLoggerResponse);
}
```

---

### log_service.proto {#log_service}

**Path**: `gcommon/v1/common/log_service.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Services** (1): `LogService`

**Imports** (5):

- `gcommon/v1/common/read_logs_request.proto`
- `gcommon/v1/common/read_logs_response.proto`
- `gcommon/v1/common/write_log_request.proto`
- `gcommon/v1/common/write_log_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_service.proto
// version: 1.0.1
// guid: 1f2e3d4c-5b6a-7089-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/read_logs_request.proto";
import "gcommon/v1/common/read_logs_response.proto";
import "gcommon/v1/common/write_log_request.proto";
import "gcommon/v1/common/write_log_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * LogService provides log management operations for
 * centralized logging and log retrieval.
 */
service LogService {
  // Write a log entry
  rpc WriteLog(WriteLogRequest) returns (WriteLogResponse);

  // Read log entries
  rpc ReadLogs(ReadLogsRequest) returns (ReadLogsResponse);
}
```

---

### notification_service.proto {#notification_service}

**Path**: `gcommon/v1/common/notification_service.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Services** (1): `NotificationService`

**Imports** (13):

- `gcommon/v1/common/delete_notification_request.proto`
- `gcommon/v1/common/delete_notification_response.proto`
- `gcommon/v1/common/get_template_request.proto`
- `gcommon/v1/common/get_template_response.proto`
- `gcommon/v1/common/list_notifications_request.proto`
- `gcommon/v1/common/list_notifications_response.proto`
- `gcommon/v1/common/mark_as_read_request.proto`
- `gcommon/v1/common/mark_as_read_response.proto`
- `gcommon/v1/common/send_notification_request.proto`
- `gcommon/v1/common/send_notification_response.proto`
- `gcommon/v1/common/update_preferences_request.proto`
- `gcommon/v1/common/update_preferences_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/notification_service.proto
// version: 1.0.1
// guid: e9327023-1377-4f3c-8fed-77a4c7e40b1b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delete_notification_request.proto";
import "gcommon/v1/common/delete_notification_response.proto";
import "gcommon/v1/common/get_template_request.proto";
import "gcommon/v1/common/get_template_response.proto";
import "gcommon/v1/common/list_notifications_request.proto";
import "gcommon/v1/common/list_notifications_response.proto";
import "gcommon/v1/common/mark_as_read_request.proto";
import "gcommon/v1/common/mark_as_read_response.proto";
import "gcommon/v1/common/send_notification_request.proto";
import "gcommon/v1/common/send_notification_response.proto";
import "gcommon/v1/common/update_preferences_request.proto";
import "gcommon/v1/common/update_preferences_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * NotificationService handles delivery, retrieval, and management of notifications.
 */
service NotificationService {
  // Send delivers a notification through configured channels.
  rpc Send(SendNotificationRequest) returns (SendNotificationResponse);

  // List returns previously sent notifications.
  rpc List(ListNotificationsRequest) returns (ListNotificationsResponse);

  // Update subscription preferences for a user
  rpc UpdatePreferences(UpdatePreferencesRequest) returns (UpdatePreferencesResponse);

  // Retrieve a notification template by ID
  rpc GetTemplate(GetTemplateRequest) returns (GetTemplateResponse);

  // Mark a notification as read
  rpc MarkAsRead(MarkAsReadRequest) returns (MarkAsReadResponse);

  // Delete a notification
  rpc Delete(DeleteNotificationRequest) returns (DeleteNotificationResponse);
}
```

---

### session_service.proto {#session_service}

**Path**: `gcommon/v1/common/session_service.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Services** (1): `SessionService`

**Imports** (17):

- `gcommon/v1/common/create_session_request.proto`
- `gcommon/v1/common/create_session_response.proto`
- `gcommon/v1/common/delete_session_request.proto`
- `gcommon/v1/common/delete_session_response.proto`
- `gcommon/v1/common/get_session_request.proto`
- `gcommon/v1/common/get_session_response.proto`
- `gcommon/v1/common/list_sessions_request.proto`
- `gcommon/v1/common/list_sessions_response.proto`
- `gcommon/v1/common/list_user_sessions_request.proto`
- `gcommon/v1/common/list_user_sessions_response.proto`
- `gcommon/v1/common/terminate_session_request.proto`
- `gcommon/v1/common/terminate_session_response.proto`
- `gcommon/v1/common/update_session_request.proto`
- `gcommon/v1/common/update_session_response.proto`
- `gcommon/v1/common/validate_session_request.proto`
- `gcommon/v1/common/validate_session_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_service.proto
// version: 1.0.1
// guid: cdb77963-bfe4-405f-86a2-e3d6ba7fb232
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/create_session_request.proto";
import "gcommon/v1/common/create_session_response.proto";
import "gcommon/v1/common/delete_session_request.proto";
import "gcommon/v1/common/delete_session_response.proto";
import "gcommon/v1/common/get_session_request.proto";
import "gcommon/v1/common/get_session_response.proto";
import "gcommon/v1/common/list_sessions_request.proto";
import "gcommon/v1/common/list_sessions_response.proto";
import "gcommon/v1/common/list_user_sessions_request.proto";
import "gcommon/v1/common/list_user_sessions_response.proto";
import "gcommon/v1/common/terminate_session_request.proto";
import "gcommon/v1/common/terminate_session_response.proto";
import "gcommon/v1/common/update_session_request.proto";
import "gcommon/v1/common/update_session_response.proto";
import "gcommon/v1/common/validate_session_request.proto";
import "gcommon/v1/common/validate_session_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SessionService manages user sessions and session lifecycle.
 * Provides session creation, validation, tracking, and termination
 * for stateful authentication and user activity monitoring.
 */
service SessionService {
  // Create a new session for an authenticated user
  rpc CreateSession(AuthCreateSessionRequest) returns (AuthCreateSessionResponse);

  // Get detailed information about a specific session
  rpc GetSession(AuthGetSessionRequest) returns (AuthGetSessionResponse);

  // Update session information (e.g., refresh activity timestamp)
  rpc UpdateSession(AuthUpdateSessionRequest) returns (AuthUpdateSessionResponse);

  // Validate a session and return session information
  rpc ValidateSession(ValidateSessionRequest) returns (ValidateSessionResponse);

  // Terminate a session (logout)
  rpc TerminateSession(TerminateSessionRequest) returns (TerminateSessionResponse);

  // Delete a specific session
  rpc DeleteSession(AuthDeleteSessionRequest) returns (AuthDeleteSessionResponse);

  // List all active sessions for a user
  rpc ListUserSessions(ListUserSessionsRequest) returns (ListUserSessionsResponse);

  // List all sessions (admin only)
  rpc ListSessions(AuthListSessionsRequest) returns (AuthListSessionsResponse);
}
```

---

