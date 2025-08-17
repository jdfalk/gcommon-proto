# auth_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 9
- **Messages**: 9
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 8

## Files in this Module

- [auth_config.proto](#auth_config)
- [get_auth_config_request.proto](#get_auth_config_request)
- [jwt_config.proto](#jwt_config)
- [ldap_config.proto](#ldap_config) ⚠️ 2 issues
- [mfa_config.proto](#mfa_config) ⚠️ 2 issues
- [oauth2_config.proto](#oauth2_config)
- [rate_limit_config.proto](#rate_limit_config)
- [saml_config.proto](#saml_config) ⚠️ 2 issues
- [session_config.proto](#session_config) ⚠️ 2 issues

## Module Dependencies

**This module depends on**:

- [auth](./auth.md)

---

## Detailed Documentation

### auth_config.proto {#auth_config}

**Path**: `pkg/auth/proto/auth_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 29

**Messages** (1): `AuthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/auth_config.proto
// version: 1.0.0
// guid: b2c3d4e5-f6a7-890b-c1d2-e3f4a5b6c7d8

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuthConfig defines authentication configuration for the application
 * including token lifetimes and password requirements.
 */
message AuthConfig {
  // How long issued access tokens remain valid
  google.protobuf.Timestamp access_token_ttl = 1;

  // How long refresh tokens remain valid
  google.protobuf.Timestamp refresh_token_ttl = 2;

  // Whether multi-factor authentication is required
  bool require_mfa = 3;
}

```

---

### get_auth_config_request.proto {#get_auth_config_request}

**Path**: `pkg/auth/proto/get_auth_config_request.proto` **Package**: `gcommon.v1.auth` **Lines**: 26

**Messages** (1): `GetAuthConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/requests/get_auth_config_request.proto
// file: auth/proto/requests/get_auth_config_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message GetAuthConfigRequest {
  // Optional specific config keys to retrieve
  repeated string keys = 1;

  // Include sensitive configuration
  bool include_sensitive = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### jwt_config.proto {#jwt_config}

**Path**: `pkg/auth/proto/jwt_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 28

**Messages** (1): `JWTConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/jwt_config.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-90c1-d2e3-f4a5b6c7d8e9

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * JWTConfig defines parameters for JWT token generation and validation.
 */
message JWTConfig {
  // Signing algorithm used for tokens (e.g., HS256, RS256)
  string signing_algorithm = 1;

  // Duration access tokens remain valid
  google.protobuf.Duration access_token_ttl = 2;

  // Duration refresh tokens remain valid
  google.protobuf.Duration refresh_token_ttl = 3;
}

```

---

### ldap_config.proto {#ldap_config}

**Path**: `pkg/auth/proto/ldap_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `LdapConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message LdapConfig {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/ldap_config.proto
// version: 1.0.0
// guid: de3eeaac-ad85-4f66-a525-670864c5815d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing ldap config.
 */
message LdapConfig {
  // TODO: Add message fields
}

```

---

### mfa_config.proto {#mfa_config}

**Path**: `pkg/auth/proto/mfa_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `MfaConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message MfaConfig {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/mfa_config.proto
// version: 1.0.0
// guid: ae560b06-340b-4dca-9a42-dc0eb623fbb1

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing mfa config.
 */
message MfaConfig {
  // TODO: Add message fields
}

```

---

### oauth2_config.proto {#oauth2_config}

**Path**: `pkg/auth/proto/oauth2_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 57

**Messages** (1): `OAuth2Config`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/jwt_config.proto`
- `pkg/auth/proto/oauth2_flow_type.proto` → [auth](./auth.md#oauth2_flow_type)

#### Source Code

```protobuf
// file: pkg/auth/proto/oauth2_config.proto
// version: 1.1.0
// guid: a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/jwt_config.proto";
import "pkg/auth/proto/oauth2_flow_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * OAuth2 configuration for authentication providers.
 * Supports various OAuth2 flows and provider configurations.
 */
message OAuth2Config {
  // OAuth2 provider name
  string provider_name = 1;

  // Client ID for OAuth2 application
  string client_id = 2;

  // Client secret for OAuth2 application
  string client_secret = 3;

  // Authorization endpoint URL
  string authorization_endpoint = 4;

  // Token endpoint URL
  string token_endpoint = 5;

  // User info endpoint URL
  string userinfo_endpoint = 6;

  // Redirect URI after authorization
  string redirect_uri = 7;

  // Requested scopes
  repeated string scopes = 8;

  // OAuth2 flow type
  OAuth2FlowType flow_type = 9;

  // Additional provider-specific parameters
  map<string, string> additional_params = 10;

  // Whether PKCE is required
  bool require_pkce = 11;

  // JWT configuration for token validation
  gcommon.v1.auth.JWTConfig jwt_config = 12;
}

```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `pkg/auth/proto/rate_limit_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 39

**Messages** (1): `RateLimitConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/rate_limit_config.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Rate limiting configuration for authentication operations.
 * Used to prevent abuse and enforce security policies.
 * Supports various rate limiting strategies.
 */
message RateLimitConfig {
  // Maximum number of requests allowed
  int32 max_requests = 1;

  // Time window for rate limiting
  google.protobuf.Duration time_window = 2;

  // Burst allowance (max requests in short burst)
  int32 burst_allowance = 3;

  // Rate limit scope (per user, per IP, etc.)
  string scope = 4;

  // Action to take when rate limit is exceeded
  string action = 5; // "block", "delay", "throttle"

  // Rate limit enabled flag
  bool enabled = 6;

  // Rate limit metadata
  map<string, string> metadata = 7 [lazy = true];
}

```

---

### saml_config.proto {#saml_config}

**Path**: `pkg/auth/proto/saml_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `SamlConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message SamlConfig {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/saml_config.proto
// version: 1.0.0
// guid: b1088674-0c17-45db-8c6d-3022ce0a629b

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing saml config.
 */
message SamlConfig {
  // TODO: Add message fields
}

```

---

### session_config.proto {#session_config}

**Path**: `pkg/auth/proto/session_config.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `SessionConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message SessionConfig {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/session_config.proto
// version: 1.0.0
// guid: cf31dcbd-ba1f-402c-a37c-c1a2afe2dba8

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing session config.
 */
message SessionConfig {
  // TODO: Add message fields
}

```

---
