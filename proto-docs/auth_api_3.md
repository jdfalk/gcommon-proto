# auth_api_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 14
- **Messages**: 14
- **Services**: 0
- **Enums**: 1

## Files in this Module

- [update_session_response.proto](#update_session_response)
- [update_user_request.proto](#update_user_request)
- [update_user_response.proto](#update_user_response)
- [validate_session_request.proto](#validate_session_request)
- [validate_session_response.proto](#validate_session_response)
- [validate_token_request.proto](#validate_token_request)
- [validate_token_response.proto](#validate_token_response)
- [verify_2fa_request.proto](#verify_2fa_request)
- [verify_credentials_request.proto](#verify_credentials_request)
- [verify_credentials_response.proto](#verify_credentials_response)
- [verify_email_request.proto](#verify_email_request)
- [verify_email_response.proto](#verify_email_response)
- [verify_mfa_request.proto](#verify_mfa_request)
- [verify_mfa_response.proto](#verify_mfa_response)

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)
- [auth_api_1](./auth_api_1.md)
- [common](./common.md)

**Modules that depend on this one**:

- [auth_services](./auth_services.md)

---

## Detailed Documentation

### update_session_response.proto {#update_session_response}

**Path**: `pkg/auth/proto/update_session_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 33

**Messages** (1): `UpdateSessionResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/session_info.proto` → [auth](./auth.md#session_info)
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/update_session_response.proto
// version: 1.0.0
// guid: f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/session_info.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for session update operations.
 * Contains the updated session information.
 */
message UpdateSessionResponse {
  // Whether the update was successful
  bool success = 1;

  // Updated session information
  gcommon.v1.auth.SessionInfo session = 2;

  // Error message if update failed
  string error_message = 3;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 4;
}

```

---

### update_user_request.proto {#update_user_request}

**Path**: `pkg/auth/proto/update_user_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 46

**Messages** (1): `UpdateUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/update_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174006

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to update an existing user account.
 */
message UpdateUserRequest {
  // Unique identifier of the user to update
  string user_id = 1;

  // New email address (optional)
  string email = 2;

  // New password (should be hashed, optional)
  string password = 3;

  // New full name (optional)
  string full_name = 4;

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

**Path**: `pkg/auth/proto/update_user_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 46

**Messages** (1): `UpdateUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/update_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174007

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Response for updating a user account.
 */
message UpdateUserResponse {
  // Unique identifier for the updated user
  string user_id = 1;

  // Updated username
  string username = 2;

  // Updated email address
  string email = 3;

  // Updated full name
  string full_name = 4;

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

**Path**: `pkg/auth/proto/validate_session_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 24

**Messages** (1): `ValidateSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/validate_session_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to validate a session token.
 * Used to verify session validity and retrieve session information.
 * Returns session and user data if token is valid.
 */
message ValidateSessionRequest {
  // Session token to validate
  string session_token = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### validate_session_response.proto {#validate_session_response}

**Path**: `pkg/auth/proto/validate_session_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 32

**Messages** (1): `ValidateSessionResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/session.proto` → [auth](./auth.md#session)
- `pkg/auth/proto/user_info.proto` → [auth](./auth.md#user_info)
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/validate_session_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/session.proto";
import "pkg/auth/proto/user_info.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

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

**Path**: `pkg/auth/proto/validate_token_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 29

**Messages** (1): `ValidateTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/validate_token_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Request to validate an access token.
 * Used to verify token authenticity, expiration, and extract user information.
 */
message ValidateTokenRequest {
  // Access token to validate (Bearer token format)
  string access_token = 1;

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

**Path**: `pkg/auth/proto/validate_token_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 40

**Messages** (1): `ValidateTokenResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/user_info.proto` → [auth](./auth.md#user_info)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/validate_token_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/user_info.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

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
  repeated string scopes = 4;

  // Token subject (user ID)
  string subject = 5;

  // Token issuer
  string issuer = 6;

  // Time until token expires (in seconds)
  int32 expires_in = 7;
}

```

---

### verify_2fa_request.proto {#verify_2fa_request}

**Path**: `pkg/auth/proto/verify_2fa_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 35

**Messages** (1): `Verify2FaRequest`

**Enums** (1): `TwoFaType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/verify_2fa_request.proto
// file: auth/proto/requests/verify_2fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message Verify2FaRequest {
  // User ID
  string user_id = 1;

  // 2FA verification code
  string code = 2;

  // Type of 2FA being verified
  enum TwoFaType {
    TWO_FA_TYPE_UNSPECIFIED = 0;
    TWO_FA_TYPE_TOTP = 1; // Time-based One-Time Password
    TWO_FA_TYPE_SMS = 2; // SMS code
    TWO_FA_TYPE_BACKUP = 3; // Backup code
  }
  TwoFaType type = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### verify_credentials_request.proto {#verify_credentials_request}

**Path**: `pkg/auth/proto/verify_credentials_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 31

**Messages** (1): `VerifyCredentialsRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/api_key_credentials.proto` → [auth_api_1](./auth_api_1.md#api_key_credentials)
- `pkg/auth/proto/password_credentials.proto` → [auth](./auth.md#password_credentials)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/verify_credentials_request.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/api_key_credentials.proto";
import "pkg/auth/proto/password_credentials.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

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

**Path**: `pkg/auth/proto/verify_credentials_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 29

**Messages** (1): `VerifyCredentialsResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/user_info.proto` → [auth](./auth.md#user_info)
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/verify_credentials_response.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/user_info.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

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

**Path**: `pkg/auth/proto/verify_email_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 26

**Messages** (1): `VerifyEmailRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/verify_email_request.proto
// file: auth/proto/requests/verify_email_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message VerifyEmailRequest {
  // User ID or email to verify
  string identifier = 1;

  // Verification token from email
  string verification_token = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### verify_email_response.proto {#verify_email_response}

**Path**: `pkg/auth/proto/verify_email_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 29

**Messages** (1): `VerifyEmailResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/verify_email_response.proto
// file: auth/proto/responses/verify_email_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message VerifyEmailResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  string error_message = 2;

  // User ID that was verified
  string user_id = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### verify_mfa_request.proto {#verify_mfa_request}

**Path**: `pkg/auth/proto/verify_mfa_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 33

**Messages** (1): `VerifyMfaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/mfa_method.proto` → [auth](./auth.md#mfa_method)

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/verify_mfa_request.proto
// file: auth/proto/requests/verify_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/mfa_method.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message VerifyMfaRequest {
  // User ID
  string user_id = 1;

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

**Path**: `pkg/auth/proto/verify_mfa_response.proto` **Package**: `gcommon.v1.auth` **Lines**: 32

**Messages** (1): `VerifyMfaResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/responses/verify_mfa_response.proto
// file: auth/proto/responses/verify_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message VerifyMfaResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  string error_message = 2;

  // Remaining attempts (for rate limiting)
  int32 remaining_attempts = 3;

  // Session token if successful
  string session_token = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---
