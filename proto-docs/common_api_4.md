# common_api_4 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 24
- **Messages**: 23
- **Services**: 0
- **Enums**: 1

## Files in this Module

- [update_preferences_request.proto](#update_preferences_request)
- [update_preferences_response.proto](#update_preferences_response)
- [update_role_request.proto](#update_role_request)
- [update_role_response.proto](#update_role_response)
- [update_session_request.proto](#update_session_request)
- [update_session_response.proto](#update_session_response)
- [update_strategy.proto](#update_strategy)
- [update_user_request.proto](#update_user_request)
- [update_user_response.proto](#update_user_response)
- [validate_session_request.proto](#validate_session_request)
- [validate_session_response.proto](#validate_session_response)
- [validate_token_request.proto](#validate_token_request)
- [validate_token_response.proto](#validate_token_response)
- [verify2_fa_request.proto](#verify2_fa_request)
- [verify_credentials_request.proto](#verify_credentials_request)
- [verify_credentials_response.proto](#verify_credentials_response)
- [verify_email_request.proto](#verify_email_request)
- [verify_email_response.proto](#verify_email_response)
- [verify_mfa_request.proto](#verify_mfa_request)
- [verify_mfa_response.proto](#verify_mfa_response)
- [watch_request.proto](#watch_request)
- [watch_response.proto](#watch_response)
- [write_log_request.proto](#write_log_request)
- [write_log_response.proto](#write_log_response)
---


## Detailed Documentation

### update_preferences_request.proto {#update_preferences_request}

**Path**: `gcommon/v1/common/update_preferences_request.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `UpdatePreferencesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/subscription_preferences.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_preferences_request.proto
// version: 1.0.1
// guid: c74c733f-1a03-4b74-b5f1-cfa062e66475

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/subscription_preferences.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UpdatePreferencesRequest {
  // Subscription preferences to apply
  SubscriptionPreferences preferences = 1 [lazy = true];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### update_preferences_response.proto {#update_preferences_response}

**Path**: `gcommon/v1/common/update_preferences_response.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Messages** (1): `UpdatePreferencesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_preferences_response.proto
// version: 1.0.1
// guid: 3eb0a369-6ebb-48fb-b5a1-8e7e3d5d7f39
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for updating subscription preferences.
 */
message UpdatePreferencesResponse {
  // Whether the update succeeded
  bool success = 1;
}
```

---

### update_role_request.proto {#update_role_request}

**Path**: `gcommon/v1/common/update_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `UpdateRoleRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_role_request.proto
// version: 1.0.1
// guid: b5502816-55e0-4610-93d1-c0d0d470d118
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/update_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `UpdateRoleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/update_role_response.proto
// file: proto/gcommon/v1/common/update_role_response.proto
// version: 1.0.1
// guid: 567e89ab-c1d2-3e4f-5a6b-7c8d9e0f1a2b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for updating a role.
 * Returns the updated role.
 */
message UpdateRoleResponse {
  // The updated role
  Role role = 1;

  // Error information if update failed
  gcommon.v1.common.Error error = 2;
}
```

---

### update_session_request.proto {#update_session_request}

**Path**: `gcommon/v1/common/update_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `AuthUpdateSessionRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/update_session_request.proto
// version: 1.0.0
// guid: 7e7565ed-c945-498a-8b56-705b4e113e51
// file: proto/gcommon/v1/common/update_session_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update session information.
 * Used to refresh session activity or update session metadata.
 */
message AuthUpdateSessionRequest {
  // Session ID to update
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // Updated session metadata
  map<string, string> metadata = 2;

  // New expiration time (optional)
  google.protobuf.Timestamp expires_at = 3;
}
```

---

### update_session_response.proto {#update_session_response}

**Path**: `gcommon/v1/common/update_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `AuthUpdateSessionResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/common/session_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_session_response.proto
// version: 1.0.0
// guid: f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/common/session_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for session update operations.
 * Contains the updated session information.
 */
message AuthUpdateSessionResponse {
  // Whether the update was successful
  bool success = 1;

  // Updated session information
  SessionInfo session = 2;

  // Error message if update failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 4;
}
```

---

### update_strategy.proto {#update_strategy}

**Path**: `gcommon/v1/common/update_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `UpdateStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_strategy.proto
// version: 1.0.1
// guid: 33aabd04-d32c-4267-94a4-dca8e8c580ad

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * UpdateStrategy defines how updates should be applied.
 */
enum UpdateStrategy {
  UPDATE_STRATEGY_UNSPECIFIED = 0;
  UPDATE_STRATEGY_ROLLING = 1;
  UPDATE_STRATEGY_BLUE_GREEN = 2;
  UPDATE_STRATEGY_IMMEDIATE = 3;
  UPDATE_STRATEGY_SCHEDULED = 4;
}
```

---

### update_user_request.proto {#update_user_request}

**Path**: `gcommon/v1/common/update_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `UpdateUserRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174006

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update an existing user account.
 */
message UpdateUserRequest {
  // Unique identifier of the user to update
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // New email address (optional)
  string email = 2 [ (buf.validate.field).string.email = true ];

  // New password (should be hashed, optional)
  string password = 3;

  // New full name (optional)
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether to enable/disable the account (optional)
  bool enabled = 5;

  // New roles to assign (replaces existing roles)
  repeated string roles = 6;

  // Additional metadata updates
  map<string, string> metadata = 7;

  // New account expiration time (optional)
  google.protobuf.Timestamp expires_at = 8;

  // Fields to update (if empty, all provided fields are updated)
  repeated string update_mask = 9;
}
```

---

### update_user_response.proto {#update_user_response}

**Path**: `gcommon/v1/common/update_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `UpdateUserResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174007

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for updating a user account.
 */
message UpdateUserResponse {
  // Unique identifier for the updated user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Updated username
  string username = 2;

  // Updated email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Updated full name
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account is enabled
  bool enabled = 5;

  // Updated roles
  repeated string roles = 6;

  // When the account was last updated
  google.protobuf.Timestamp updated_at = 7;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 8;

  // List of fields that were actually updated
  repeated string updated_fields = 9;
}
```

---

### validate_session_request.proto {#validate_session_request}

**Path**: `gcommon/v1/common/validate_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `ValidateSessionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_session_request.proto
// version: 1.0.0
// guid: 0100439d-a620-4991-9d73-231ae604bf9a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to validate a session token.
 * Used to verify session validity and retrieve session information.
 * Returns session and user data if token is valid.
 */
message ValidateSessionRequest {
  // Session token to validate
  string session_token = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### validate_session_response.proto {#validate_session_response}

**Path**: `gcommon/v1/common/validate_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `ValidateSessionResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/session.proto`
- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_session_response.proto
// version: 1.0.1
// guid: 53da0a29-4520-4990-9822-6b18b3dedc2a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/session.proto";
import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to session validation request.
 * Contains session validity status and associated user/session information.
 * Includes error information if validation fails.
 */
message ValidateSessionResponse {
  // Whether the session is valid
  bool valid = 1;

  // Session information if valid
  Session session = 2 [lazy = true];

  // User information associated with the session
  UserInfo user_info = 3 [lazy = true];

  // Error information if validation fails
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### validate_token_request.proto {#validate_token_request}

**Path**: `gcommon/v1/common/validate_token_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `ValidateTokenRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_token_request.proto
// version: 1.0.0
// guid: 337bc0eb-8b0a-4a0c-b173-506f0eae4f52
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to validate an access token.
 * Used to verify token authenticity, expiration, and extract user information.
 */
message ValidateTokenRequest {
  // Access token to validate (Bearer token format)
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];

  // Whether to include user information in response
  bool include_user_info = 3;

  // Whether to include permissions in response
  bool include_permissions = 4;
}
```

---

### validate_token_response.proto {#validate_token_response}

**Path**: `gcommon/v1/common/validate_token_response.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `ValidateTokenResponse`

**Imports** (4):

- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_token_response.proto
// version: 1.0.0
// guid: b1fc9b36-9860-473f-b59b-a7b9ffbe218b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for token validation requests.
 * Contains token validity status and associated user information.
 */
message ValidateTokenResponse {
  // Whether the token is valid
  bool valid = 1;

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 2 [lazy = true];

  // User information associated with the token
  UserInfo user_info = 3 [lazy = true];

  // Token scopes/permissions
  repeated string scopes = 4 [(buf.validate.field).repeated.min_items = 1];

  // Token subject (user ID)
  string subject = 5 [(buf.validate.field).string.min_len = 1];

  // Token issuer
  string issuer = 6 [(buf.validate.field).string.min_len = 1];

  // Time until token expires (in seconds)
  int32 expires_in = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### verify2_fa_request.proto {#verify2_fa_request}

**Path**: `gcommon/v1/common/verify2_fa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `Verify2FaRequest`

**Imports** (3):

- `gcommon/v1/common/two_fa_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verify2_fa_request.proto
// version: 1.0.0
// guid: fa64bc16-24a7-4b50-ba76-fc8fdd7079de

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/two_fa_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Verify2FaRequest {
  // User ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // 2FA verification code
  string code = 2;

  // Type of 2FA being verified

  AuthTwoFaType type = 3;
}
```

---

### verify_credentials_request.proto {#verify_credentials_request}

**Path**: `gcommon/v1/common/verify_credentials_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `VerifyCredentialsRequest`

**Imports** (4):

- `gcommon/v1/common/api_key_credentials.proto`
- `gcommon/v1/common/password_credentials.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verify_credentials_request.proto
// version: 1.0.1
// guid: 11047805-0f53-4b8a-b2b5-355b1abfea63
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key_credentials.proto";
import "gcommon/v1/common/password_credentials.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to verify user credentials without issuing tokens.
 * Used for credential validation without creating an authenticated session.
 * Supports password and API key credential verification.
 */
message VerifyCredentialsRequest {
  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Credentials to verify (oneof ensures only one type is used)
  oneof credentials {
    // Username/password credentials
    PasswordCredentials password = 2;
    // API key credentials
    APIKeyCredentials api_key = 3;
  }
}
```

---

### verify_credentials_response.proto {#verify_credentials_response}

**Path**: `gcommon/v1/common/verify_credentials_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `VerifyCredentialsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verify_credentials_response.proto
// version: 1.0.1
// guid: e7457cd0-baf1-4e73-a64c-ac0a8ed7946f
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to credential verification request.
 * Contains verification result and user information if credentials are valid.
 * Includes error information if verification fails.
 */
message VerifyCredentialsResponse {
  // Whether the credentials are valid
  bool verified = 1;

  // User information if credentials are verified
  UserInfo user_info = 2 [lazy = true];

  // Error information if verification fails
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### verify_email_request.proto {#verify_email_request}

**Path**: `gcommon/v1/common/verify_email_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `VerifyEmailRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_email_request.proto
// version: 1.0.0
// guid: 8f68392c-3cc1-408c-a8ac-4c48d08a70a0
// file: proto/gcommon/v1/common/verify_email_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyEmailRequest {
  // User ID or email to verify
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Verification token from email
  string verification_token = 2 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### verify_email_response.proto {#verify_email_response}

**Path**: `gcommon/v1/common/verify_email_response.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `VerifyEmailResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_email_response.proto
// version: 1.0.0
// guid: 93319a70-2b96-4a96-8bfd-c8412437d883
// file: proto/gcommon/v1/common/verify_email_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyEmailResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  string error_message = 2;

  // User ID that was verified
  string user_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### verify_mfa_request.proto {#verify_mfa_request}

**Path**: `gcommon/v1/common/verify_mfa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `VerifyMfaRequest`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_mfa_request.proto
// version: 1.0.0
// guid: a628ba55-dd40-4025-bd1b-a634add55417
// file: proto/gcommon/v1/common/verify_mfa_request.proto
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

message VerifyMfaRequest {
  // User ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // MFA verification code
  string code = 2;

  // Method being verified
  MfaMethod method = 3;

  // Context for the verification (login, transaction, etc.)
  string context = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### verify_mfa_response.proto {#verify_mfa_response}

**Path**: `gcommon/v1/common/verify_mfa_response.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `VerifyMfaResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_mfa_response.proto
// version: 1.0.0
// guid: 352b7b8d-1237-45ac-89b7-63228d94c5d0
// file: proto/gcommon/v1/common/verify_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyMfaResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Remaining attempts (for rate limiting)
  int32 remaining_attempts = 3 [(buf.validate.field).int32.gte = 0];

  // Session token if successful
  string session_token = 4 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### watch_request.proto {#watch_request}

**Path**: `gcommon/v1/common/watch_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `HealthWatchRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/watch_request.proto
// version: 1.0.0
// guid: dc2cc626-d629-4419-8765-3f7cd4010a51
//
// Watch request message definition for streaming health updates
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message HealthWatchRequest {
  // Service name to watch (empty for all services)
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### watch_response.proto {#watch_response}

**Path**: `gcommon/v1/common/watch_response.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Messages** (1): `WatchResponse`

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
// file: proto/gcommon/v1/common/watch_response.proto
// version: 1.0.0
// guid: 63859080-ce23-4630-b180-012a9c86ae1f
//
// Watch response message definition for streaming health updates
//
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
 * WatchResponse represents a streaming health status update
 * containing real-time health information for services.
 *
 * This message provides:
 * - Real-time health status changes
 * - Service-specific health updates
 * - Detailed check results and metrics
 * - Error information for unhealthy services
 */
message WatchResponse {
  // Overall health status
  CommonHealthStatus status = 1;

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

### write_log_request.proto {#write_log_request}

**Path**: `gcommon/v1/common/write_log_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `WriteLogRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/write_log_request.proto
// version: 1.0.0
// guid: 7f8e9d0c-1b2a-3645-7e8f-9a0b1c2d3e4f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * WriteLogRequest defines the request for writing a log entry.
 */
message WriteLogRequest {
  // Log level (e.g., "INFO", "ERROR", "DEBUG")
  string level = 1 [(buf.validate.field).string.min_len = 1];

  // Log message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Source component or service
  string source = 3 [(buf.validate.field).string.min_len = 1];

  // Additional metadata
  map<string, string> metadata = 4;
}
```

---

### write_log_response.proto {#write_log_response}

**Path**: `gcommon/v1/common/write_log_response.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `WriteLogResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/write_log_response.proto
// version: 1.0.0
// guid: 8f9e0d1c-2b3a-4756-8e9f-0a1b2c3d4e5f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * WriteLogResponse defines the response from writing a log entry.
 */
message WriteLogResponse {
  // Status of the write operation
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Log entry ID if applicable
  string log_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

