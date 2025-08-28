# common_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 44
- **Services**: 0
- **Enums**: 6

## Files in this Module

- [ack_level.proto](#ack_level)
- [ack_mode.proto](#ack_mode)
- [ack_type.proto](#ack_type)
- [assign_role_request.proto](#assign_role_request)
- [assign_role_response.proto](#assign_role_response)
- [authenticate_request.proto](#authenticate_request)
- [authenticate_response.proto](#authenticate_response)
- [authorize_request.proto](#authorize_request)
- [authorize_response.proto](#authorize_response)
- [backup_frequency.proto](#backup_frequency)
- [batch_operation.proto](#batch_operation)
- [batch_options.proto](#batch_options)
- [batch_priority.proto](#batch_priority)
- [change_password_request.proto](#change_password_request)
- [change_password_response.proto](#change_password_response)
- [change_type.proto](#change_type)
- [check_permission_request.proto](#check_permission_request)
- [check_permission_response.proto](#check_permission_response)
- [complete_password_reset_request.proto](#complete_password_reset_request)
- [complete_password_reset_response.proto](#complete_password_reset_response)
- [create_permission_request.proto](#create_permission_request)
- [create_role_request.proto](#create_role_request)
- [create_role_response.proto](#create_role_response)
- [create_session_request.proto](#create_session_request)
- [create_session_response.proto](#create_session_response)
- [create_user_request.proto](#create_user_request)
- [create_user_response.proto](#create_user_response)
- [delete_notification_request.proto](#delete_notification_request)
- [delete_notification_response.proto](#delete_notification_response)
- [delete_permission_request.proto](#delete_permission_request)
- [delete_role_request.proto](#delete_role_request)
- [delete_role_response.proto](#delete_role_response)
- [delete_session_request.proto](#delete_session_request)
- [delete_session_response.proto](#delete_session_response)
- [delete_user_request.proto](#delete_user_request)
- [delete_user_response.proto](#delete_user_response)
- [disable2_fa_request.proto](#disable2_fa_request)
- [disable_check_request.proto](#disable_check_request)
- [disable_check_response.proto](#disable_check_response)
- [disable_mfa_request.proto](#disable_mfa_request)
- [disable_mfa_response.proto](#disable_mfa_response)
- [enable2_fa_request.proto](#enable2_fa_request)
- [enable_check_request.proto](#enable_check_request)
- [enable_check_response.proto](#enable_check_response)
- [enable_mfa_request.proto](#enable_mfa_request)
- [enable_mfa_response.proto](#enable_mfa_response)
- [generate_api_key_request.proto](#generate_api_key_request)
- [generate_api_key_response.proto](#generate_api_key_response)
- [get_api_key_request.proto](#get_api_key_request)
- [get_api_key_response.proto](#get_api_key_response)
---


## Detailed Documentation

### ack_level.proto {#ack_level}

**Path**: `gcommon/v1/common/ack_level.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `AckLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/ack_level.proto
// file: proto/gcommon/v1/queue/ack_level.proto
// version: 1.0.1
// guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Acknowledgment level for durability guarantees.
 */
enum AckLevel {
  // Default unspecified level
  ACK_LEVEL_UNSPECIFIED = 0;

  // No acknowledgment required (fire and forget)
  ACK_LEVEL_NONE = 1;

  // Wait for leader acknowledgment only
  ACK_LEVEL_LEADER = 2;

  // Wait for all replicas to acknowledge
  ACK_LEVEL_ALL = 3;

  // Wait for majority of replicas
  ACK_LEVEL_MAJORITY = 4;
}
```

---

### ack_mode.proto {#ack_mode}

**Path**: `gcommon/v1/common/ack_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Enums** (1): `AckMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/ack_mode.proto
// version: 1.0.1
// guid: 1ea916c3-cb02-4ad8-9ff0-03396568398a
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Acknowledgment mode enumeration for message processing.
 * Defines how message acknowledgments are handled in streaming operations,
 * queue processing, and event handling across all GCommon modules.
 */
enum AckMode {
  // Default value indicating no acknowledgment mode was specified
  ACK_MODE_UNSPECIFIED = 0;

  // Manual acknowledgment - client must explicitly acknowledge messages
  ACK_MODE_MANUAL = 1;

  // Automatic acknowledgment - messages are acknowledged upon delivery
  ACK_MODE_AUTO = 2;

  // Client-side acknowledgment - acknowledgment is handled by client logic
  ACK_MODE_CLIENT = 3;
}
```

---

### ack_type.proto {#ack_type}

**Path**: `gcommon/v1/common/ack_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `AckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ack_type.proto
// version: 1.0.1
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Types of acknowledgments.
 * Defines how a consumed message was processed.
 */
enum AckType {
  // Unspecified acknowledgment type
  ACK_TYPE_UNSPECIFIED = 0;

  // Successful processing acknowledgment
  ACK_TYPE_SUCCESS = 1;

  // Failed processing - retry message
  ACK_TYPE_RETRY = 2;

  // Failed processing - reject message (dead letter)
  ACK_TYPE_REJECT = 3;

  // Processing timeout
  ACK_TYPE_TIMEOUT = 4;
}
```

---

### assign_role_request.proto {#assign_role_request}

**Path**: `gcommon/v1/common/assign_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 59

**Messages** (1): `AssignRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/assign_role_request.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID to assign (required)
  // Must be a valid role identifier in the system
  string role_id = 2;

  // Optional organization context for scoped role assignment
  // If not provided, role is assigned globally
  string organization_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/assign_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `AssignRoleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/assign_role_response.proto
// version: 1.0.0
// guid: 71268c4b-6cea-4997-9b67-ce60cc72de2b
// file: proto/gcommon/v1/common/assign_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message AssignRoleResponse {
  // Assignment success
  bool success = 1;

  // Error message if assignment failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Effective permissions after assignment
  repeated string effective_permissions = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### authenticate_request.proto {#authenticate_request}

**Path**: `gcommon/v1/common/authenticate_request.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Messages** (1): `AuthAuthenticateRequest`

**Imports** (7):

- `gcommon/v1/common/api_key_credentials.proto`
- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/jwt_credentials.proto`
- `gcommon/v1/common/o_auth2_credentials.proto`
- `gcommon/v1/common/password_credentials.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authenticate_request.proto
// version: 1.0.1
// guid: 3662d31f-ad12-4066-be86-6a74f4e4a884
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key_credentials.proto";
import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/jwt_credentials.proto";
import "gcommon/v1/common/o_auth2_credentials.proto";
import "gcommon/v1/common/password_credentials.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Authentication request supporting multiple credential types.
 * Uses oneof to ensure only one authentication method is provided per request.
 * Supports comprehensive metadata and client information for security and auditing.
 */
message AuthAuthenticateRequest {
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

**Path**: `gcommon/v1/common/authenticate_response.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Messages** (1): `AuthAuthenticateResponse`

**Imports** (5):

- `gcommon/v1/common/rate_limit.proto`
- `gcommon/v1/common/session.proto`
- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authenticate_response.proto
// version: 1.0.0
// guid: c28da8ae-a463-4446-83b2-50a947fd8826
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/rate_limit.proto";
import "gcommon/v1/common/session.proto";
import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Authentication response containing access tokens and user information.
 * Follows OAuth2 token response format with additional session and user data.
 * Includes rate limiting information for client throttling.
 */
message AuthAuthenticateResponse {
  // Access token for API authentication (JWT format)
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // Refresh token for token renewal (opaque format)
  string refresh_token = 2 [(buf.validate.field).string.min_len = 1];

  // Token type (always "Bearer" for OAuth2 compliance)
  string token_type = 3 [(buf.validate.field).string.min_len = 1];

  // Access token expiration time in seconds
  int32 expires_in = 4 [(buf.validate.field).int32.gte = 0];

  // Granted authorization scopes
  repeated string scopes = 5 [(buf.validate.field).repeated.min_items = 1];

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

**Path**: `gcommon/v1/common/authorize_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `AuthAuthorizeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authorize_request.proto
// version: 1.0.0
// guid: 06edf238-40f2-4d28-a7dc-0b6a972bf7b2
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to check if a user is authorized for a specific action.
 * Used for fine-grained access control and permission validation.
 * Supports contextual authorization with additional metadata.
 */
message AuthAuthorizeRequest {
  // Access token for the user being authorized
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Resource being accessed (e.g., "user:123", "project:456")
  string resource = 2 [(buf.validate.field).string.min_len = 1];

  // Action being performed (e.g., "read", "write", "delete")
  string action = 3 [(buf.validate.field).string.min_len = 1];

  // Additional context for authorization decision
  map<string, string> context = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### authorize_response.proto {#authorize_response}

**Path**: `gcommon/v1/common/authorize_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `AuthAuthorizeResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authorize_response.proto
// version: 1.0.0
// guid: 698cde09-444b-45ef-abbd-239e622ddc4f
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to authorization request.
 * Contains authorization decision and relevant permission information.
 * Includes denial reason if authorization fails.
 */
message AuthAuthorizeResponse {
  // Whether the user is authorized for the requested action
  bool authorized = 1;

  // Permissions that granted this authorization (if any)
  repeated string permissions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Reason for denial if authorization failed
  string denial_reason = 3 [(buf.validate.field).string.min_len = 1];

  // Error information if authorization check failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### backup_frequency.proto {#backup_frequency}

**Path**: `gcommon/v1/common/backup_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `BackupFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/backup_frequency.proto
// version: 1.0.1
// guid: 4efc5d0f-be87-47e1-8f01-f42fa2926368

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### batch_operation.proto {#batch_operation}

**Path**: `gcommon/v1/common/batch_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `CommonBatchOperation`

**Imports** (5):

- `buf/validate/validate.proto`
- `gcommon/v1/common/batch_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/batch_operation.proto
// version: 1.0.1
// guid: 5671d63f-77bd-4415-a7ec-3c22d3557b37
edition = "2023";

package gcommon.v1.common;

import "buf/validate/validate.proto";
import "gcommon/v1/common/batch_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Batch operation wrapper for bulk request processing.
 * Enables efficient processing of multiple operations with
 * configurable parallelism, error handling, and timeout policies.
 */
message CommonBatchOperation {
  // Unique identifier for this batch operation
  string batch_id = 1 [(buf.validate.field).string.min_len = 1];

  // Type of operation being performed in batch
  string operation_type = 2 [(buf.validate.field).string.min_len = 1];

  // Individual operations within the batch (type-specific)
  repeated google.protobuf.Any operations = 3 [
    lazy = true,
    (buf.validate.field).repeated.min_items = 1
  ];

  // Batch processing configuration options
  CommonBatchOptions options = 4 [lazy = true];

  // Request metadata for tracing and correlation
  RequestMetadata metadata = 5 [lazy = true];
}
```

---

### batch_options.proto {#batch_options}

**Path**: `gcommon/v1/common/batch_options.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `CommonBatchOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/batch_options.proto
// version: 1.0.0
// guid: 66c5dc7e-add8-44b2-8bde-bf1845acbd3f
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Batch processing options for configuring bulk operation behavior.
 * Controls parallelism, error handling, timeout policies, and
 * result handling for efficient batch processing.
 */
message CommonBatchOptions {
  // Maximum number of operations to process in parallel
  int32 max_parallel = 1 [(buf.validate.field).int32.gte = 0];

  // Whether to stop processing on the first error encountered
  bool fail_fast = 2;

  // Total timeout for the entire batch operation
  google.protobuf.Duration timeout = 3;

  // Whether to return partial results if timeout is reached
  bool return_partial = 4;
}
```

---

### batch_priority.proto {#batch_priority}

**Path**: `gcommon/v1/common/batch_priority.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `BatchPriority`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_priority.proto
// version: 1.0.1
// guid: f9429991-ff0a-4c70-a6e5-7d639281f030

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * BatchPriority defines the processing priority for batch operations.
 */
enum BatchPriority {
  BATCH_PRIORITY_UNSPECIFIED = 0;
  BATCH_PRIORITY_LOW = 1;
  BATCH_PRIORITY_NORMAL = 2;
  BATCH_PRIORITY_HIGH = 3;
  BATCH_PRIORITY_URGENT = 4;
}
```

---

### change_password_request.proto {#change_password_request}

**Path**: `gcommon/v1/common/change_password_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `ChangePasswordRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/change_password_request.proto
// version: 1.0.0
// guid: a3ff57ec-81fd-4ed4-89ab-1d804175aabd
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to change user password (authenticated).
 * Requires current password for security validation.
 * Used for authenticated password change operations.
 */
message ChangePasswordRequest {
  // Current password for verification
  string current_password = 1 [(buf.validate.field).string.min_len = 8];

  // New password to set
  string new_password = 2 [(buf.validate.field).string.min_len = 8];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### change_password_response.proto {#change_password_response}

**Path**: `gcommon/v1/common/change_password_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ChangePasswordResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/change_password_response.proto
// version: 1.0.0
// guid: 0b8b2b05-a63d-43c6-abd4-49e3fb0c7409
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to password change request.
 * Contains confirmation of password change and any relevant metadata.
 * Provides feedback to the user about the operation status.
 */
message ChangePasswordResponse {
  // Whether the password change was successful
  bool success = 1;

  // Confirmation message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if password change failed
  gcommon.v1.common.Error error = 3 [lazy = true];

  // Whether all existing sessions should be terminated
  bool sessions_terminated = 4;

  // Number of sessions that were terminated
  int32 terminated_session_count = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### change_type.proto {#change_type}

**Path**: `gcommon/v1/common/change_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `MetricsChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/change_type.proto
// version: 1.0.1
// guid: 43b77608-77cc-40ad-97ae-4055d556fe1f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ChangeType defines the type of configuration change.
 */
enum MetricsChangeType {
  CHANGE_TYPE_UNSPECIFIED = 0;
  CHANGE_TYPE_ADDED = 1;
  CHANGE_TYPE_UPDATED = 2;
  CHANGE_TYPE_REMOVED = 3;
  CHANGE_TYPE_REPLACED = 4;
}
```

---

### check_permission_request.proto {#check_permission_request}

**Path**: `gcommon/v1/common/check_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `CheckPermissionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_permission_request.proto
// version: 1.0.0
// guid: db7aca7d-742a-443b-b641-448ddf4a8518

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to verify that a user possesses a specific permission.
 */
message CheckPermissionRequest {
  // Metadata for tracing and audit purposes
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // User ID being verified
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Permission ID to check
  string permission_id = 3;
}
```

---

### check_permission_response.proto {#check_permission_response}

**Path**: `gcommon/v1/common/check_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `CheckPermissionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_permission_response.proto
// version: 1.0.1
// guid: 909a647b-cd2d-44d1-b612-5ea1e54bda39

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/complete_password_reset_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `CompletePasswordResetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/complete_password_reset_request.proto
// version: 1.0.0
// guid: 66afc3ec-b304-45c8-ad75-7dff63410987
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to complete password reset with token.
 * Validates reset token and sets new password.
 * Completes the password recovery flow.
 */
message CompletePasswordResetRequest {
  // Password reset token from initiate request
  string reset_token = 1 [(buf.validate.field).string.min_len = 1];

  // New password to set
  string new_password = 2 [(buf.validate.field).string.min_len = 8];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### complete_password_reset_response.proto {#complete_password_reset_response}

**Path**: `gcommon/v1/common/complete_password_reset_response.proto` **Package**: `gcommon.v1.common` **Lines**: 50

**Messages** (1): `CompletePasswordResetResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/complete_password_reset_response.proto
// version: 1.0.0
// guid: abe29553-64dd-4743-bf15-c3f35155de70
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * CompletePasswordResetResponse confirms successful password reset completion.
 * Provides confirmation and security information about the password reset
 * operation for audit logging and user notification.
 */
message CompletePasswordResetResponse {
  // User ID whose password was reset
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/create_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `CreatePermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/create_permission_request.proto
// version: 1.0.0
// guid: dee162c4-dfc6-4ebf-94f8-7f7871349e23
// file: proto/gcommon/v1/common/create_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message CreatePermissionRequest {
  // Permission name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Permission description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Actions this permission grants
  repeated string actions = 3;

  // Resources this permission applies to
  repeated string resources = 4;
}
```

---

### create_role_request.proto {#create_role_request}

**Path**: `gcommon/v1/common/create_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `CreateRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_role_request.proto
// version: 1.0.1
// guid: f08ba415-9259-4f93-a889-7405b082f9cd
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/create_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `CreateRoleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/create_role_response.proto
// file: proto/gcommon/v1/common/create_role_response.proto
// version: 1.0.1
// guid: 345e6789-a1b2-3c4d-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for creating a new role.
 * Returns the created role with its assigned ID.
 */
message CreateRoleResponse {
  // The created role
  Role role = 1;

  // Error information if creation failed
  gcommon.v1.common.Error error = 2;
}
```

---

### create_session_request.proto {#create_session_request}

**Path**: `gcommon/v1/common/create_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Messages** (1): `AuthCreateSessionRequest`

**Imports** (4):

- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_session_request.proto
// version: 1.0.0
// guid: 4e2786c7-f3d0-442e-bb3b-c88772e7aece
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to create a new user session.
 * Used after successful authentication to establish a session
 * with specific duration and metadata tracking.
 */
message AuthCreateSessionRequest {
  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // User ID for which to create the session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/create_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Messages** (1): `AuthCreateSessionResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_session_response.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-1234-567890abcdef

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for session creation operations.
 * Contains session token, expiration details, and user context.
 */
message AuthCreateSessionResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Created session details
  string session_id = 2;
  string access_token = 3;
  string refresh_token = 4;
  google.protobuf.Timestamp expires_at = 5;
  google.protobuf.Timestamp refresh_expires_at = 6;

  // User context
  string user_id = 7 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
  repeated string roles = 8;
  repeated string permissions = 9;
}
```

---

### create_user_request.proto {#create_user_request}

**Path**: `gcommon/v1/common/create_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `CreateUserRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to create a new user account.
 */
message CreateUserRequest {
  // Username for the new account
  string username = 1;

  // Email address for the new account
  string email = 2 [ (buf.validate.field).string.email = true ];

  // Password for the new account (should be hashed)
  string password = 3;

  // Full name of the user
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/common/create_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 55

**Messages** (1): `CreateUserResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174002

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for creating a new user account.
 */
message CreateUserResponse {
  // Unique identifier for the created user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username of the created account
  string username = 2;

  // Email address of the created account
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Full name of the user
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account is enabled
  bool enabled = 5;

  // Assigned roles
  repeated string roles = 6;

  // When the account was created
  google.protobuf.Timestamp created_at = 7 [ (buf.validate.field).required = true ];

  // Whether email verification is required
  bool email_verification_required = 8;

  // Email verification token (if required)
  string verification_token = 9;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 10;
}
```

---

### delete_notification_request.proto {#delete_notification_request}

**Path**: `gcommon/v1/common/delete_notification_request.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `DeleteNotificationRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_notification_request.proto
// version: 1.0.0
// guid: 20a32413-3de3-416f-a3ad-23c2172121c9

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeleteNotificationRequest {
  // Identifier of the notification to delete.
  string notification_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### delete_notification_response.proto {#delete_notification_response}

**Path**: `gcommon/v1/common/delete_notification_response.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `DeleteNotificationResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_notification_response.proto
// version: 1.0.1
// guid: d7f015d6-70a1-4fcd-82b3-560a134d7a45

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response after deleting a notification.
 */
message DeleteNotificationResponse {
  // True if the deletion succeeded.
  bool success = 1;
}
```

---

### delete_permission_request.proto {#delete_permission_request}

**Path**: `gcommon/v1/common/delete_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `DeletePermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_permission_request.proto
// version: 1.0.0
// guid: e40a5914-c7d8-41e0-bb7d-07495308e638
// file: proto/gcommon/v1/common/delete_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeletePermissionRequest {
  // Permission ID to delete
  string permission_id = 1 [(buf.validate.field).string.min_len = 1];

  // Force deletion even if assigned
  bool force = 2;
}
```

---

### delete_role_request.proto {#delete_role_request}

**Path**: `gcommon/v1/common/delete_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeleteRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_role_request.proto
// version: 1.0.0
// guid: c6fef1ce-1633-4607-967d-1b42b93dcf8c
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to delete a role.
 * Used for role management and cleanup.
 * Role must not be assigned to any users before deletion.
 */
message DeleteRoleRequest {
  // Role ID to delete
  string role_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### delete_role_response.proto {#delete_role_response}

**Path**: `gcommon/v1/common/delete_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeleteRoleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_role_response.proto
// version: 1.0.0
// guid: d7a5181a-727d-4f09-85fb-70407122b1eb
// file: proto/gcommon/v1/common/delete_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeleteRoleResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Number of users/entities that lost this role
  int32 affected_subjects = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### delete_session_request.proto {#delete_session_request}

**Path**: `gcommon/v1/common/delete_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `AuthDeleteSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_session_request.proto
// version: 1.0.0
// guid: 81f54c30-c375-4c15-a847-2a7296c9741c
// file: proto/gcommon/v1/common/delete_session_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to delete a session.
 * Used for session cleanup and administrative purposes.
 */
message AuthDeleteSessionRequest {
  // Session ID to delete
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // Force delete even if session is active (admin only)
  bool force = 2;
}
```

---

### delete_session_response.proto {#delete_session_response}

**Path**: `gcommon/v1/common/delete_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `AuthDeleteSessionResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_session_response.proto
// version: 1.0.1
// guid: e99771c5-4060-4cd9-a8f5-7919d9b8cb61
// file: proto/gcommon/v1/common/delete_session_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for session deletion request.
 * Confirms successful deletion or provides error information.
 */
message AuthDeleteSessionResponse {
  // Whether the session was successfully deleted
  bool deleted = 1;

  // Error information if deletion failed
  gcommon.v1.common.Error error = 2;
}
```

---

### delete_user_request.proto {#delete_user_request}

**Path**: `gcommon/v1/common/delete_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `DeleteUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174003

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to delete a user account.
 */
message DeleteUserRequest {
  // Unique identifier of the user to delete
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/delete_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeleteUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_user_response.proto
// version: 1.0.0
// guid: 1c98d374-f744-4078-bb80-826832a42620
// file: proto/gcommon/v1/common/delete_user_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeleteUserResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Data retention information
  string data_retention_info = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### disable2_fa_request.proto {#disable2_fa_request}

**Path**: `gcommon/v1/common/disable2_fa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `Disable2FaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable2_fa_request.proto
// version: 1.0.0
// guid: 00c046b6-37b9-4a79-a9a4-05f73d7c0d7f
// file: proto/gcommon/v1/common/disable2_fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Disable2FaRequest {
  // User ID requesting 2FA disable
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Current password for verification
  string password = 2;

  // 2FA code for verification
  string verification_code = 3;
}
```

---

### disable_check_request.proto {#disable_check_request}

**Path**: `gcommon/v1/common/disable_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DisableCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable_check_request.proto
// version: 1.0.0
// guid: 57c84c2e-3f48-4a3d-a2c3-a910d1956773
// file: proto/gcommon/v1/common/disable_check_request.proto
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

message DisableCheckRequest {
  // Name or ID of the check to disable
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### disable_check_response.proto {#disable_check_response}

**Path**: `gcommon/v1/common/disable_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `DisableCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/disable_check_response.proto
// version: 1.0.0
// guid: 0cba0a9a-f486-48cc-b449-1245a11558c4
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for disabling a health check.
 * Contains the result of disabling an active check.
 */
message DisableCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was disabled
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if disabling failed
  gcommon.v1.common.Error error = 3;

  // Reason for disabling (if provided)
  string reason = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### disable_mfa_request.proto {#disable_mfa_request}

**Path**: `gcommon/v1/common/disable_mfa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `DisableMfaRequest`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable_mfa_request.proto
// version: 1.0.0
// guid: 69fe90b5-14de-44b2-a3dc-8768c27f6617
// file: proto/gcommon/v1/common/disable_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DisableMfaRequest {
  // User ID requesting MFA disable
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Current password for verification
  string password = 2;

  // MFA verification code
  string verification_code = 3;

  // Specific methods to disable (empty = all)
  repeated gcommon.v1.common.MfaMethod methods = 4;
}
```

---

### disable_mfa_response.proto {#disable_mfa_response}

**Path**: `gcommon/v1/common/disable_mfa_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `DisableMfaResponse`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable_mfa_response.proto
// version: 1.0.0
// guid: 8fa6daf5-aee9-414d-95a0-ed59c3c11334
// file: proto/gcommon/v1/common/disable_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DisableMfaResponse {
  // Success status
  bool success = 1;

  // Methods that were disabled
  repeated gcommon.v1.common.MfaMethod disabled_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error message if operation failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### enable2_fa_request.proto {#enable2_fa_request}

**Path**: `gcommon/v1/common/enable2_fa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `Enable2FaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/enable2_fa_request.proto
// version: 1.0.0
// guid: 2f270251-6e96-4864-9c75-1e9a381549d6
// file: proto/gcommon/v1/common/enable2_fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Enable2FaRequest {
  // User ID requesting 2FA enablement
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

### enable_check_request.proto {#enable_check_request}

**Path**: `gcommon/v1/common/enable_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `EnableCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/enable_check_request.proto
// version: 1.0.0
// guid: 0377eaa7-a0d8-46c3-b427-2743c1062111
// file: proto/gcommon/v1/common/enable_check_request.proto
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

message EnableCheckRequest {
  // Name or ID of the check to enable
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### enable_check_response.proto {#enable_check_response}

**Path**: `gcommon/v1/common/enable_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `EnableCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/enable_check_response.proto
// version: 1.0.0
// guid: e785b271-7a1a-42e8-add6-deda8ce9f5b1
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for enabling a health check.
 * Contains the result of enabling a previously disabled check.
 */
message EnableCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was enabled
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if enabling failed
  gcommon.v1.common.Error error = 3;

  // Check status after enabling
  string status = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### enable_mfa_request.proto {#enable_mfa_request}

**Path**: `gcommon/v1/common/enable_mfa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `EnableMfaRequest`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/enable_mfa_request.proto
// version: 1.0.0
// guid: 1277fc9b-bcd3-49c3-9c5d-2596a743c594
// file: proto/gcommon/v1/common/enable_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EnableMfaRequest {
  // User ID requesting MFA enablement
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // MFA methods to enable
  repeated gcommon.v1.common.MfaMethod methods = 2;

  // Primary contact method
  string primary_contact = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### enable_mfa_response.proto {#enable_mfa_response}

**Path**: `gcommon/v1/common/enable_mfa_response.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `EnableMfaResponse`

**Imports** (3):

- `gcommon/v1/common/mfa_setup_instruction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/enable_mfa_response.proto
// version: 1.0.0
// guid: 7fe3c97f-1a88-419f-b2f9-9f699a13b78c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_setup_instruction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EnableMfaResponse {
  // Success status
  bool success = 1;

  // Setup instructions for each method
  repeated MfaSetupInstruction setup_instructions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error message if operation failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### generate_api_key_request.proto {#generate_api_key_request}

**Path**: `gcommon/v1/common/generate_api_key_request.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `GenerateAPIKeyRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/generate_api_key_request.proto
// version: 1.0.0
// guid: 5590365e-02f0-4a3d-96eb-15bc615c14ef

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GenerateAPIKeyRequest requests creation of a new API key for a user.
 */
message GenerateAPIKeyRequest {
  // User ID for whom to generate the key
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional name/description for the key
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional expiration in seconds
  int32 expires_in = 3;

  // Metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### generate_api_key_response.proto {#generate_api_key_response}

**Path**: `gcommon/v1/common/generate_api_key_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GenerateAPIKeyResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/generate_api_key_response.proto
// version: 1.0.0
// guid: 026770a4-919a-4111-818f-ab932e8523ea

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GenerateAPIKeyResponse returns the newly created API key.
 */
message GenerateAPIKeyResponse {
  // Generated API key value
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional key identifier
  string key_id = 2 [(buf.validate.field).string.min_len = 1];

  // Response metadata for rate limiting and tracing
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### get_api_key_request.proto {#get_api_key_request}

**Path**: `gcommon/v1/common/get_api_key_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetApiKeyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_api_key_request.proto
// version: 1.0.0
// guid: 942d4a7c-b73d-43e7-a95d-bcd51091d1be
// file: proto/gcommon/v1/common/get_api_key_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetApiKeyRequest {
  // API key ID
  string key_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include usage statistics
  bool include_stats = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### get_api_key_response.proto {#get_api_key_response}

**Path**: `gcommon/v1/common/get_api_key_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `GetApiKeyResponse`

**Imports** (4):

- `gcommon/v1/common/api_key.proto`
- `gcommon/v1/common/api_key_stats.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_api_key_response.proto
// version: 1.0.0
// guid: 584574e5-3a49-4346-ada5-78a7454f921e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key.proto";
import "gcommon/v1/common/api_key_stats.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetApiKeyResponse {
  // API key details
  gcommon.v1.common.APIKey api_key = 1;

  // Usage statistics if requested
  gcommon.v1.common.ApiKeyStats stats = 2;

  // Error message if not found
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

