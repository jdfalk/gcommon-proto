# common_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [get_check_status_request.proto](#get_check_status_request)
- [get_health_history_request.proto](#get_health_history_request)
- [get_health_metrics_request.proto](#get_health_metrics_request)
- [get_health_metrics_response.proto](#get_health_metrics_response)
- [get_health_request.proto](#get_health_request)
- [get_permission_request.proto](#get_permission_request)
- [get_permission_response.proto](#get_permission_response)
- [get_preferences_request.proto](#get_preferences_request)
- [get_preferences_response.proto](#get_preferences_response)
- [get_role_request.proto](#get_role_request)
- [get_role_response.proto](#get_role_response)
- [get_session_request.proto](#get_session_request)
- [get_session_response.proto](#get_session_response)
- [get_system_stats_request.proto](#get_system_stats_request)
- [get_system_stats_response.proto](#get_system_stats_response)
- [get_template_request.proto](#get_template_request)
- [get_template_response.proto](#get_template_response)
- [get_user_info_request.proto](#get_user_info_request)
- [get_user_info_response.proto](#get_user_info_response)
- [get_user_permissions_request.proto](#get_user_permissions_request)
- [get_user_permissions_response.proto](#get_user_permissions_response)
- [get_user_request.proto](#get_user_request)
- [get_user_response.proto](#get_user_response)
- [get_user_roles_request.proto](#get_user_roles_request)
- [get_user_roles_response.proto](#get_user_roles_response)
- [grant_permission_request.proto](#grant_permission_request)
- [grant_permission_response.proto](#grant_permission_response)
- [health_check_all_request.proto](#health_check_all_request)
- [health_check_all_response.proto](#health_check_all_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [initiate_password_reset_request.proto](#initiate_password_reset_request)
- [initiate_password_reset_response.proto](#initiate_password_reset_response)
- [invalidate_user_sessions_request.proto](#invalidate_user_sessions_request)
- [list_api_keys_request.proto](#list_api_keys_request)
- [list_api_keys_response.proto](#list_api_keys_response)
- [list_checks_request.proto](#list_checks_request)
- [list_notifications_request.proto](#list_notifications_request)
- [list_notifications_response.proto](#list_notifications_response)
- [list_permissions_request.proto](#list_permissions_request)
- [list_permissions_response.proto](#list_permissions_response)
- [list_roles_request.proto](#list_roles_request)
- [list_roles_response.proto](#list_roles_response)
- [list_sessions_request.proto](#list_sessions_request)
- [list_sessions_response.proto](#list_sessions_response)
- [list_user_sessions_request.proto](#list_user_sessions_request)
- [list_user_sessions_response.proto](#list_user_sessions_response)
- [list_users_request.proto](#list_users_request)
- [list_users_response.proto](#list_users_response)
- [logout_request.proto](#logout_request)
---


## Detailed Documentation

### get_check_status_request.proto {#get_check_status_request}

**Path**: `gcommon/v1/common/get_check_status_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetCheckStatusRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_check_status_request.proto
// version: 1.0.0
// guid: b22eabcb-b556-4dd9-bd5b-4016956b8e69
// file: proto/gcommon/v1/common/get_check_status_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetCheckStatusRequest {
  // Name or ID of the check
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_health_history_request.proto {#get_health_history_request}

**Path**: `gcommon/v1/common/get_health_history_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `GetHealthHistoryRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_health_history_request.proto
// version: 1.0.0
// guid: b0eb3b6a-e7f2-454f-addf-e8c9a9d2313a
// file: proto/gcommon/v1/common/get_health_history_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthHistoryRequest {
  // Service name to query
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Optional start time for history records
  google.protobuf.Timestamp start_time = 2;

  // Optional end time for history records
  google.protobuf.Timestamp end_time = 3;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### get_health_metrics_request.proto {#get_health_metrics_request}

**Path**: `gcommon/v1/common/get_health_metrics_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `GetHealthMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_health_metrics_request.proto
// version: 1.0.0
// guid: 85ebb0e8-dd6f-4a2d-9e83-386b9d84d776
// file: proto/gcommon/v1/common/get_health_metrics_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthMetricsRequest {
  // Service name (optional)
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata used for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_health_metrics_response.proto {#get_health_metrics_response}

**Path**: `gcommon/v1/common/get_health_metrics_response.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `GetHealthMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/health_metric_data.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_health_metrics_response.proto
// version: 1.0.0
// guid: 53811a7b-91b9-44c9-8045-42ff44f502c2

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_metric_data.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthMetricsResponse {
  // Health metrics data
  repeated HealthMetricData metrics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_health_request.proto {#get_health_request}

**Path**: `gcommon/v1/common/get_health_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `GetHealthRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_health_request.proto
// version: 1.0.0
// guid: 9c9295ed-ade9-4dd4-843c-f8f78a380b7f
// file: proto/gcommon/v1/common/get_health_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthRequest {
  // Service name to query
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to include detailed check results
  bool include_details = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### get_permission_request.proto {#get_permission_request}

**Path**: `gcommon/v1/common/get_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `GetPermissionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_permission_request.proto
// version: 1.0.0
// guid: 0658829b-708a-480e-942d-42b7ce0e4fdd

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to fetch details about a permission entry.
 */
message GetPermissionRequest {
  // Permission identifier
  string permission_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_permission_response.proto {#get_permission_response}

**Path**: `gcommon/v1/common/get_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetPermissionResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/permission.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_permission_response.proto
// version: 1.0.1
// guid: fabb3420-290d-4f58-8be9-b363ef1adefd

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/permission.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### get_preferences_request.proto {#get_preferences_request}

**Path**: `gcommon/v1/common/get_preferences_request.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetPreferencesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_preferences_request.proto
// version: 1.0.0
// guid: fb16c45a-545c-4d05-b3fd-34dbc4a9d0c1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetPreferencesRequest {
  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier for the user whose preferences are being requested.
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### get_preferences_response.proto {#get_preferences_response}

**Path**: `gcommon/v1/common/get_preferences_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetPreferencesResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/common/subscription_preferences.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_preferences_response.proto
// version: 1.0.1
// guid: 3c2f540d-f827-4df1-9afe-6f31f6d73dd9

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/common/subscription_preferences.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GetPreferencesResponse returns a user's subscription preferences.
 */
message GetPreferencesResponse {
  // Current subscription preferences.
  SubscriptionPreferences preferences = 1;

  // Response metadata for rate limiting and tracing.
  gcommon.v1.common.ResponseMetadata metadata = 2;
}
```

---

### get_role_request.proto {#get_role_request}

**Path**: `gcommon/v1/common/get_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_role_request.proto
// version: 1.0.0
// guid: 554e7499-0070-40fe-a99c-3428bec2651f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to retrieve details about a specific role.
 */
message GetRoleRequest {
  // Unique identifier of the role
  string role_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include permissions in the response
  bool include_permissions = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### get_role_response.proto {#get_role_response}

**Path**: `gcommon/v1/common/get_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetRoleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_role_response.proto
// version: 1.0.1
// guid: 4da329f9-4bb7-4695-85e7-a7083ae930e1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/get_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `AuthGetSessionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_session_request.proto
// version: 1.1.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get session information.
 * Used to retrieve detailed session data by session ID.
 * Provides session status, metadata, and activity information.
 */
message AuthGetSessionRequest {
  // Session ID to retrieve (required)
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to include detailed session activity
  bool include_activity = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### get_session_response.proto {#get_session_response}

**Path**: `gcommon/v1/common/get_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `AuthGetSessionResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/session.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_session_response.proto
// version: 1.0.1
// guid: e2dfbf3c-a64b-4e03-8728-bb79288e0998
// file: proto/gcommon/v1/common/get_session_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/session.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for getting session information.
 * Contains session details if found, or error information if not found.
 */
message AuthGetSessionResponse {
  // Session information if found
  Session session = 1;

  // Error information if session not found or access denied
  gcommon.v1.common.Error error = 2;
}
```

---

### get_system_stats_request.proto {#get_system_stats_request}

**Path**: `gcommon/v1/common/get_system_stats_request.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `GetSystemStatsRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_system_stats_request.proto
// version: 1.0.1
// guid: 789eabcd-e1f2-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/get_system_stats_response.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `GetSystemStatsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_system_stats_response.proto
// version: 1.0.0
// guid: 8a9ebcde-f1a2-3b4c-5d6e-7f8a9b0c1d2e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing authentication system statistics.
 */
message GetSystemStatsResponse {
  // Total number of active users
  int64 active_users = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of roles
  int64 total_roles = 2 [(buf.validate.field).int64.gte = 0];

  // Total number of active sessions
  int64 active_sessions = 3 [(buf.validate.field).int64.gte = 0];

  // Total number of failed login attempts (last 24h)
  int64 failed_logins = 4 [(buf.validate.field).int64.gte = 0];

  // Authentication system uptime in seconds
  int64 uptime_seconds = 5 [(buf.validate.field).int64.gte = 0];

  // Error information if stats retrieval failed
  gcommon.v1.common.Error error = 6;
}
```

---

### get_template_request.proto {#get_template_request}

**Path**: `gcommon/v1/common/get_template_request.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetTemplateRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_template_request.proto
// version: 1.0.0
// guid: 4b8dae31-438b-4407-8f5e-25e99ebd347b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetTemplateRequest {
  // Template identifier to fetch
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_template_response.proto {#get_template_response}

**Path**: `gcommon/v1/common/get_template_response.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `GetTemplateResponse`

**Imports** (2):

- `gcommon/v1/common/template.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_template_response.proto
// version: 1.2.1
// guid: 525e0a4f-3e9f-4b1a-8d33-fa9c295964a0

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/template.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a requested notification template.
 */
message GetTemplateResponse {
  // Template data
  gcommon.v1.common.Template template = 1 [lazy = true];
}
```

---

### get_user_info_request.proto {#get_user_info_request}

**Path**: `gcommon/v1/common/get_user_info_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `GetUserInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_info_request.proto
// version: 1.0.0
// guid: 43e29c52-26b2-4a16-899e-5eb46029783d
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get user information from a valid token.
 * Extracts user profile data from an authenticated session.
 * Used for user profile display and authorization decisions.
 */
message GetUserInfoRequest {
  // Access token to extract user info from
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_user_info_response.proto {#get_user_info_response}

**Path**: `gcommon/v1/common/get_user_info_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetUserInfoResponse`

**Imports** (2):

- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_info_response.proto
// version: 1.0.1
// guid: b6270468-8ca0-4f87-9843-2528bd262254
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/get_user_permissions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetUserPermissionsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_permissions_request.proto
// version: 1.0.0
// guid: 38097153-2bce-47ac-ab8a-20605ee39939
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get all permissions for a user.
 * Returns direct permissions and role-based permissions.
 * Used for user permission auditing and UI authorization.
 */
message GetUserPermissionsRequest {
  // User ID to get permissions for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_user_permissions_response.proto {#get_user_permissions_response}

**Path**: `gcommon/v1/common/get_user_permissions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `GetUserPermissionsResponse`

**Imports** (3):

- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_permissions_response.proto
// version: 1.0.1
// guid: 732b72be-148e-459b-861f-220b83fc9903
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing all permissions for a user.
 * Includes direct permissions, role-based permissions, and effective permissions.
 * Provides comprehensive permission information for authorization decisions.
 */
message GetUserPermissionsResponse {
  // Direct permissions assigned to the user
  repeated string permissions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Permissions inherited from roles
  repeated string role_permissions = 2 [(buf.validate.field).repeated.min_items = 1];

  // All effective permissions (union of direct and role permissions)
  repeated string effective_permissions = 3 [(buf.validate.field).repeated.min_items = 1];

  // User's roles (includes permission details)
  repeated Role roles = 4 [lazy = true, (buf.validate.field).repeated.min_items = 1];
}
```

---

### get_user_request.proto {#get_user_request}

**Path**: `gcommon/v1/common/get_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `GetUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174008

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get a specific user's details.
 */
message GetUserRequest {
  // Unique identifier of the user to retrieve
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/get_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `GetUserResponse`

**Imports** (2):

- `gcommon/v1/common/user_details.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_response.proto
// version: 1.0.1
// guid: 3c135848-65ac-40ed-9e96-bab2045c4997

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_details.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetUserResponse {
  // User details
  gcommon.v1.common.UserDetails user = 1;

  // Whether the user was found
  bool found = 2;
}
```

---

### get_user_roles_request.proto {#get_user_roles_request}

**Path**: `gcommon/v1/common/get_user_roles_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetUserRolesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_roles_request.proto
// version: 1.0.0
// guid: b97cd079-474d-492b-a33e-8c35d42c445a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get all roles assigned to a user.
 * Used for user role management and authorization decisions.
 * Returns detailed role information including permissions.
 */
message GetUserRolesRequest {
  // User ID to get roles for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_user_roles_response.proto {#get_user_roles_response}

**Path**: `gcommon/v1/common/get_user_roles_response.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `GetUserRolesResponse`

**Imports** (3):

- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_roles_response.proto
// version: 1.0.0
// guid: c8a7e641-1fb8-46ee-9491-d3612c2c2400
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing all roles assigned to a user.
 * Provides complete role information including permissions and metadata.
 * Used for role management and authorization display.
 */
message GetUserRolesResponse {
  // All roles assigned to the user
  repeated Role roles = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### grant_permission_request.proto {#grant_permission_request}

**Path**: `gcommon/v1/common/grant_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `GrantPermissionRequest`

**Imports** (3):

- `gcommon/v1/common/subject_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/grant_permission_request.proto
// version: 1.0.0
// guid: f01c2811-f92f-4582-bfca-c77c277c3e12

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/subject_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GrantPermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subject type
  AuthSubjectType subject_type = 2;

  // Permission ID to grant
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### grant_permission_response.proto {#grant_permission_response}

**Path**: `gcommon/v1/common/grant_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `GrantPermissionResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/grant_permission_response.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for permission grant operations.
 * Indicates whether the permission was successfully granted.
 */
message GrantPermissionResponse {
  // Whether the permission grant was successful
  bool success = 1;

  // Error message if grant failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // The granted permission ID
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];

  // User or entity the permission was granted to
  string grantee_id = 4 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}
```

---

### health_check_all_request.proto {#health_check_all_request}

**Path**: `gcommon/v1/common/health_check_all_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `HealthCheckAllRequest`

**Imports** (3):

- `gcommon/v1/common/check_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_all_request.proto
// version: 1.0.0
// guid: 6e150288-20ca-4892-9582-6ca93070073b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthCheckAllRequest requests health status for all services or filtered by type
 */
message HealthCheckAllRequest {
  // Optional filter by check types
  repeated gcommon.v1.common.CheckType types = 1 [(buf.validate.field).repeated.min_items = 1];
  // Whether to include detailed component information
  bool include_details = 2;
  // Timeout for the overall check in seconds
  int32 timeout_seconds = 3 [(buf.validate.field).int32.gt = 0];
}
```

---

### health_check_all_response.proto {#health_check_all_response}

**Path**: `gcommon/v1/common/health_check_all_response.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `HealthCheckAllResponse`

**Imports** (4):

- `gcommon/v1/common/health_check_result.proto`
- `gcommon/v1/common/serving_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_all_response.proto
// version: 1.0.0
// guid: 64089a6a-9c0e-43db-a038-6e271809004e
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_check_result.proto";
import "gcommon/v1/common/serving_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthCheckAllResponse contains comprehensive health information for all services
 */
message HealthCheckAllResponse {
  // Overall system status
  ServingStatus overall_status = 1;
  // Individual service health results
  repeated HealthHealthCheckResult results = 2 [(buf.validate.field).repeated.min_items = 1];
  // Total number of services checked
  int32 total_services = 3 [(buf.validate.field).int32.gte = 0];
  // Number of healthy services
  int32 healthy_services = 4 [(buf.validate.field).int32.gte = 0];
  // Number of unhealthy services
  int32 unhealthy_services = 5 [(buf.validate.field).int32.gte = 0];
  // Total check duration in milliseconds
  int64 total_duration_ms = 6 [(buf.validate.field).int64.gt = 0];
  // Timestamp when the check was completed
  int64 timestamp = 7;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/common/health_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `HealthHealthCheckRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_request.proto
// version: 1.0.0
// guid: f260a75e-1b70-48df-a829-d4d53e277a16
//
// Health check request message definition
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message HealthHealthCheckRequest {
  // Service name to check (empty for overall health)
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;

  // Check timeout
  google.protobuf.Duration timeout = 3;

  // Include detailed check results
  bool include_details = 4;
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/common/health_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `HealthHealthCheckResponse`

**Imports** (8):

- `gcommon/v1/common/check_result.proto`
- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_metrics.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_response.proto
// version: 1.0.0
// guid: 2276a26b-e231-4da7-86b6-3cf35110b85f
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_result.proto";
import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_metrics.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for health check operations.
 * Contains comprehensive health status information including detailed results and metrics.
 */
message HealthHealthCheckResponse {
  // Overall health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Service name
  string service = 2 [(buf.validate.field).string.min_len = 1];

  // Check timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Response time
  google.protobuf.Duration response_time = 4;

  // Detailed check results
  repeated CheckResult check_results = 5 [(buf.validate.field).repeated.min_items = 1];

  // Health message
  string message = 6 [(buf.validate.field).string.min_len = 1];

  // Error information if unhealthy
  gcommon.v1.common.Error error = 7;

  // Health metrics
  HealthMetrics metrics = 8;
}
```

---

### initiate_password_reset_request.proto {#initiate_password_reset_request}

**Path**: `gcommon/v1/common/initiate_password_reset_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `InitiatePasswordResetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/initiate_password_reset_request.proto
// version: 1.0.0
// guid: 16ce7615-af01-41a5-b5be-86728f975870
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to initiate password reset flow.
 * Sends reset instructions to user's email or generates reset token.
 * Used for self-service password recovery.
 */
message InitiatePasswordResetRequest {
  // User identifier (username or email)
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### initiate_password_reset_response.proto {#initiate_password_reset_response}

**Path**: `gcommon/v1/common/initiate_password_reset_response.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `InitiatePasswordResetResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/initiate_password_reset_response.proto
// version: 1.0.0
// guid: 418382e8-da43-4470-a00c-41b8ad9d699b
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to password reset initiation request.
 * Contains reset token and expiration information.
 * May include additional instructions for the user.
 */
message InitiatePasswordResetResponse {
  // Password reset token (may be sent via email instead)
  string reset_token = 1 [(buf.validate.field).string.min_len = 1];

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 2;

  // Message to display to user (e.g., "Check your email")
  string message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### invalidate_user_sessions_request.proto {#invalidate_user_sessions_request}

**Path**: `gcommon/v1/common/invalidate_user_sessions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `InvalidateUserSessionsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/invalidate_user_sessions_request.proto
// version: 1.0.0
// guid: 678e9abc-d1e2-3f4a-5b6c-7d8e9f0a1b2c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to invalidate all sessions for a user.
 */
message InvalidateUserSessionsRequest {
  // User ID whose sessions should be invalidated
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### list_api_keys_request.proto {#list_api_keys_request}

**Path**: `gcommon/v1/common/list_api_keys_request.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `ListApiKeysRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_api_keys_request.proto
// version: 1.0.0
// guid: 978a16cb-4ec7-45ce-b762-c2a2b40a4e6f
// file: proto/gcommon/v1/common/list_api_keys_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListApiKeysRequest {
  // User ID to list API keys for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/list_api_keys_response.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `ListApiKeysResponse`

**Imports** (3):

- `gcommon/v1/common/api_key.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_api_keys_response.proto
// version: 1.0.0
// guid: 1c9b335d-ac56-4d22-aced-e1e6722e9247

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListApiKeysResponse {
  // List of API keys
  repeated gcommon.v1.common.APIKey api_keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Next page token
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total count
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### list_checks_request.proto {#list_checks_request}

**Path**: `gcommon/v1/common/list_checks_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `ListChecksRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_checks_request.proto
// version: 1.0.0
// guid: 15ac39bc-301a-4120-a333-5c07d417d4fb
// file: proto/gcommon/v1/common/list_checks_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListChecksRequest {
  // Optional service name to filter checks
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### list_notifications_request.proto {#list_notifications_request}

**Path**: `gcommon/v1/common/list_notifications_request.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `ListNotificationsRequest`

**Imports** (2):

- `gcommon/v1/common/pagination.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_notifications_request.proto
// version: 1.0.1
// guid: 34151d3e-f3cb-4445-a801-c9a44078e3cd

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/pagination.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to list previously sent notifications.
 */
message ListNotificationsRequest {
  // Pagination information for result set.
  gcommon.v1.common.Pagination pagination = 1;
}
```

---

### list_notifications_response.proto {#list_notifications_response}

**Path**: `gcommon/v1/common/list_notifications_response.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `ListNotificationsResponse`

**Imports** (3):

- `gcommon/v1/common/notification_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_notifications_response.proto
// version: 1.0.0
// guid: 7986e6b9-6a3e-4b7e-b093-5a87133742a3

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/notification_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a list of notifications.
 */
message ListNotificationsResponse {
  // Notifications sorted by creation time descending.
  repeated NotificationMessage notifications = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### list_permissions_request.proto {#list_permissions_request}

**Path**: `gcommon/v1/common/list_permissions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `ListPermissionsRequest`

**Imports** (3):

- `gcommon/v1/common/subject_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_permissions_request.proto
// version: 1.0.0
// guid: b28e318d-b0e8-41bb-9c90-d6b98f138e4f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/subject_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListPermissionsRequest {
  // User or role ID to list permissions for
  string subject_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subject type

  AuthSubjectType subject_type = 2;

  // Pagination
  int32 page_size = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
  string page_token = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_permissions_response.proto {#list_permissions_response}

**Path**: `gcommon/v1/common/list_permissions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `ListPermissionsResponse`

**Imports** (3):

- `gcommon/v1/common/permission.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_permissions_response.proto
// version: 1.0.0
// guid: 4aecc4bd-409d-4724-a679-a189e3390d5d
// file: proto/gcommon/v1/common/list_permissions_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/permission.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListPermissionsResponse {
  // List of permissions
  repeated Permission permissions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Next page token
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total count
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### list_roles_request.proto {#list_roles_request}

**Path**: `gcommon/v1/common/list_roles_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ListRolesRequest`

**Imports** (5):

- `gcommon/v1/common/filter_options.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/sort_options.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_roles_request.proto
// version: 1.0.1
// guid: 10d4a32a-06da-4751-965f-97c0d522d456
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/filter_options.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/sort_options.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/list_roles_response.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `ListRolesResponse`

**Imports** (4):

- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_roles_response.proto
// version: 1.0.0
// guid: b0d2291f-7911-45f0-94d1-6dee153b5841
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a list of roles.
 * Includes pagination information for large result sets.
 * Used for role management interfaces and administration.
 */
message ListRolesResponse {
  // List of roles matching the request criteria
  repeated Role roles = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information for the response
  gcommon.v1.common.PaginatedResponse pagination = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### list_sessions_request.proto {#list_sessions_request}

**Path**: `gcommon/v1/common/list_sessions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `AuthListSessionsRequest`

**Imports** (3):

- `gcommon/v1/common/pagination.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_sessions_request.proto
// version: 1.0.0
// guid: b293be7c-9588-4756-9429-52fe8a24a7b5
// file: proto/gcommon/v1/common/list_sessions_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/pagination.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to list all sessions (admin only).
 * Used for administrative monitoring and management.
 */
message AuthListSessionsRequest {
  // Pagination parameters
  gcommon.v1.common.Pagination pagination = 1;

  // Filter by user ID (optional)
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Filter by session status (optional)
  string status = 3;
}
```

---

### list_sessions_response.proto {#list_sessions_response}

**Path**: `gcommon/v1/common/list_sessions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `AuthListSessionsResponse`

**Imports** (4):

- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/common/session.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_sessions_response.proto
// version: 1.0.0
// guid: a07e1500-4f58-4fb0-9741-29e10c17d095
// file: proto/gcommon/v1/common/list_sessions_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/common/session.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a list of sessions.
 * Includes pagination information for large result sets.
 */
message AuthListSessionsResponse {
  // List of sessions
  repeated Session sessions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information
  gcommon.v1.common.PaginatedResponse pagination = 2;
}
```

---

### list_user_sessions_request.proto {#list_user_sessions_request}

**Path**: `gcommon/v1/common/list_user_sessions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 89

**Messages** (1): `ListUserSessionsRequest`

**Imports** (5):

- `gcommon/v1/common/pagination_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_user_sessions_request.proto
// version: 1.0.0
// guid: 8a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/pagination_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/list_user_sessions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 103

**Messages** (1): `ListUserSessionsResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/session_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_user_sessions_response.proto
// version: 1.0.0
// guid: ac4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/session_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports

// Common types

// Auth module types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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
  repeated SessionInfo sessions = 1;

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
  string user_id = 15 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/list_users_request.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Messages** (1): `ListUsersRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_users_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174004

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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
  string email_filter = 4 [ (buf.validate.field).string.email = true ];

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

**Path**: `gcommon/v1/common/list_users_response.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Messages** (1): `ListUsersResponse`

**Imports** (3):

- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_users_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174005

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for listing users.
 */
message ListUsersResponse {
  // List of users
  repeated UserInfo users = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of users (before pagination)
  int32 total_count = 2 [(buf.validate.field).int32.gte = 0];

  // Current page number
  int32 page = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items per page
  int32 page_size = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total number of pages
  int32 total_pages = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Whether there are more pages
  bool has_next_page = 6;

  // Whether this is not the first page
  bool has_previous_page = 7;
}
```

---

### logout_request.proto {#logout_request}

**Path**: `gcommon/v1/common/logout_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `LogoutRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logout_request.proto
// version: 1.0.0
// guid: b22adc38-523e-4fbf-8fae-d3f890525589

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogoutRequest ends a user session and invalidates tokens
message LogoutRequest {
  // ID of the session to terminate
  string session_id = 1;

  // Optional user ID for audit purposes
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

