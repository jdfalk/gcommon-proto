# auth Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 43
- **Messages**: 34
- **Services**: 0
- **Enums**: 16
- ⚠️ **Issues**: 8

## Files in this Module

- [auth_context.proto](#auth_context)
- [auth_method.proto](#auth_method)
- [auth_provider.proto](#auth_provider)
- [auth_token.proto](#auth_token) ⚠️ 2 issues
- [claims.proto](#claims)
- [grant_type.proto](#grant_type) ⚠️ 1 issues
- [group.proto](#group)
- [jwt_credentials.proto](#jwt_credentials)
- [mfa_method.proto](#mfa_method)
- [mfa_type.proto](#mfa_type)
- [oauth2_credentials.proto](#oauth2_credentials)
- [oauth2_flow_type.proto](#oauth2_flow_type)
- [oauth_client.proto](#oauth_client)
- [password_credentials.proto](#password_credentials)
- [password_policy.proto](#password_policy) ⚠️ 2 issues
- [permission.proto](#permission)
- [permission_grant.proto](#permission_grant)
- [permission_metadata.proto](#permission_metadata)
- [permission_scope.proto](#permission_scope)
- [permission_type.proto](#permission_type) ⚠️ 1 issues
- [provider_type.proto](#provider_type)
- [refresh_token.proto](#refresh_token)
- [role.proto](#role)
- [role_assignment.proto](#role_assignment)
- [role_metadata.proto](#role_metadata)
- [role_scope.proto](#role_scope)
- [scope_type.proto](#scope_type)
- [security_context.proto](#security_context)
- [security_policy.proto](#security_policy)
- [session.proto](#session)
- [session_info.proto](#session_info)
- [session_metadata.proto](#session_metadata)
- [session_status.proto](#session_status)
- [token.proto](#token)
- [token_info.proto](#token_info)
- [token_metadata.proto](#token_metadata)
- [token_status.proto](#token_status)
- [token_type.proto](#token_type)
- [user.proto](#user)
- [user_info.proto](#user_info)
- [user_metadata.proto](#user_metadata)
- [user_profile.proto](#user_profile) ⚠️ 2 issues
- [user_status.proto](#user_status)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_2](./metrics_2.md)

**Modules that depend on this one**:

- [auth_api_1](./auth_api_1.md)
- [auth_api_2](./auth_api_2.md)
- [auth_api_3](./auth_api_3.md)
- [auth_config](./auth_config.md)
- [auth_events](./auth_events.md)
- [auth_services](./auth_services.md)
- [metrics_api_1](./metrics_api_1.md)

---

## Detailed Documentation

### auth_context.proto {#auth_context}

**Path**: `pkg/auth/proto/auth_context.proto` **Package**: `gcommon.v1.auth` **Lines**: 36

**Messages** (1): `AuthContext`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/role.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/auth_context.proto
// version: 1.0.0
// guid: 70848c6a-eeb6-46ee-b108-9159435b2475

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuthContext carries user identity and authorization details
 * generated during authentication.
 */
message AuthContext {
  // ID of the authenticated user
  string user_id = 1;

  // Roles assigned to the user
  repeated string roles = 2;

  // Permissions granted to the user
  repeated string permissions = 3;

  // When this context was generated
  google.protobuf.Timestamp issued_at = 4 [lazy = true];

  // Arbitrary metadata passed between services
  map<string, string> metadata = 5;
}

```

---

### auth_method.proto {#auth_method}

**Path**: `pkg/auth/proto/auth_method.proto` **Package**: `gcommon.v1.auth` **Lines**: 39

**Enums** (1): `AuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/auth_method.proto
// version: 1.0.0
// guid: 815bb886-5864-44fd-ae07-c6102c110fd7

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuthMethod enumerates the supported authentication mechanisms.
 */
enum AuthMethod {
  // Default unknown method
  AUTH_METHOD_UNSPECIFIED = 0;

  // Traditional username and password authentication
  AUTH_METHOD_PASSWORD = 1;

  // API key based authentication
  AUTH_METHOD_API_KEY = 2;

  // OAuth2 or OpenID Connect authentication
  AUTH_METHOD_OAUTH2 = 3;

  // SAML identity provider authentication
  AUTH_METHOD_SAML = 4;

  // LDAP directory authentication
  AUTH_METHOD_LDAP = 5;

  // Multi-factor authentication method
  AUTH_METHOD_MFA = 6;
}

```

---

### auth_provider.proto {#auth_provider}

**Path**: `pkg/auth/proto/auth_provider.proto` **Package**: `gcommon.v1.auth` **Lines**: 32

**Messages** (1): `AuthProvider`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/provider_type.proto` → [metrics_2](./metrics_2.md#provider_type)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/auth_provider.proto
// version: 1.0.0
// guid: 7293f6cc-7049-493d-9e7c-b17f00dd8a76

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/provider_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * AuthProvider represents an external authentication provider configuration.
 * It defines the provider type and connection details used for authentication.
 */
message AuthProvider {
  // Unique provider identifier
  string id = 1;

  // Human readable provider name
  string name = 2;

  // Provider type (e.g., LDAP, OAUTH2, SAML)
  ProviderType type = 3;

  // Provider-specific configuration reference or JSON blob
  string config = 4;
}

```

---

### auth_token.proto {#auth_token}

**Path**: `pkg/auth/proto/auth_token.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `AuthToken`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message AuthToken {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/auth_token.proto
// version: 1.0.0
// guid: 61671511-e4c8-4e25-a0a6-5f82f7e45002

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing auth token.
 */
message AuthToken {
  // TODO: Add message fields
}

```

---

### claims.proto {#claims}

**Path**: `pkg/auth/proto/claims.proto` **Package**: `gcommon.v1.auth` **Lines**: 46

**Messages** (1): `Claims`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/claims.proto
// file: auth/proto/types/claims.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message Claims {
  // Standard JWT claims
  string issuer = 1; // iss
  string subject = 2; // sub
  repeated string audience = 3; // aud
  int64 expires_at = 4; // exp
  int64 not_before = 5; // nbf
  int64 issued_at = 6; // iat
  string jwt_id = 7; // jti

  // Custom claims
  string user_id = 8;
  string username = 9;
  string email = 10;
  bool email_verified = 11;
  repeated string roles = 12;
  repeated string permissions = 13;
  repeated string scopes = 14;

  // MFA claims
  bool mfa_verified = 15;
  string mfa_method = 16;

  // Session claims
  string session_id = 17;
  bool is_refresh_token = 18;

  // Additional metadata
  map<string, string> metadata = 19;
}

```

---

### grant_type.proto {#grant_type}

**Path**: `pkg/auth/proto/grant_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 19

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: TODO - // TODO: Add enum definitions here

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/grant_type.proto
// file: auth/proto/enums/grant_type.proto
//
// Enum definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

// TODO: Add enum definitions here

// Implement the actual protobuf definitions according to the auth module requirements

```

---

### group.proto {#group}

**Path**: `pkg/auth/proto/group.proto` **Package**: `gcommon.v1.auth` **Lines**: 50

**Messages** (1): `Group`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/common/proto/resource_status.proto` → [common](./common.md#resource_status)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/group.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/resource_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Group entity for organizing users into collections.
 * Used for bulk permission management and organizational structure.
 * Supports hierarchical group relationships.
 */
message Group {
  // Unique group identifier
  string id = 1;

  // Group name
  string name = 2;

  // Group description
  string description = 3;

  // Parent group ID (for hierarchical groups)
  string parent_group_id = 4;

  // Group permissions
  repeated string permissions = 5;

  // Group metadata for extensibility
  map<string, string> metadata = 6 [lazy = true];

  // Group creation timestamp
  google.protobuf.Timestamp created_at = 7 [lazy = true];

  // Group status
  gcommon.v1.common.ResourceStatus status = 8;

  // Group member count
  int32 member_count = 9;

  // Group administrator user IDs
  repeated string admin_user_ids = 10;
}

```

---

### jwt_credentials.proto {#jwt_credentials}

**Path**: `pkg/auth/proto/jwt_credentials.proto` **Package**: `gcommon.v1.auth` **Lines**: 23

**Messages** (1): `JWTCredentials`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/jwt_credentials.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * JWT (JSON Web Token) credentials for token-based authentication.
 * Supports validation of externally issued JWTs with optional issuer verification.
 */
message JWTCredentials {
  // JWT token string (header.payload.signature format)
  string token = 1;

  // Expected issuer for JWT validation (optional)
  // When provided, the JWT's 'iss' claim must match this value
  string issuer = 2;
}

```

---

### mfa_method.proto {#mfa_method}

**Path**: `pkg/auth/proto/mfa_method.proto` **Package**: `gcommon.v1.auth` **Lines**: 33

**Enums** (1): `MfaMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/mfa_method.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174123

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Multi-factor authentication methods supported by the system.
 */
enum MfaMethod {
  // Unspecified MFA method
  MFA_METHOD_UNSPECIFIED = 0;

  // SMS-based verification
  MFA_METHOD_SMS = 1;

  // Email-based verification
  MFA_METHOD_EMAIL = 2;

  // Time-based one-time password (TOTP)
  MFA_METHOD_TOTP = 3;

  // Hardware security key
  MFA_METHOD_HARDWARE_KEY = 4;
}

```

---

### mfa_type.proto {#mfa_type}

**Path**: `pkg/auth/proto/mfa_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 33

**Enums** (1): `MFAType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/mfa_type.proto
// version: 1.0.0
// guid: a5e413ea-00e3-4585-9e9d-30348138c407

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * MFAType enumerates supported multi-factor authentication methods.
 */
enum MFAType {
  // Unknown or unspecified MFA method
  MFA_TYPE_UNSPECIFIED = 0;

  // Time-based one-time password via authenticator apps
  MFA_TYPE_TOTP = 1;

  // One-time code delivered via SMS
  MFA_TYPE_SMS = 2;

  // One-time code delivered via email
  MFA_TYPE_EMAIL = 3;

  // Push notification to a trusted device
  MFA_TYPE_PUSH = 4;
}

```

---

### oauth2_credentials.proto {#oauth2_credentials}

**Path**: `pkg/auth/proto/oauth2_credentials.proto` **Package**: `gcommon.v1.auth` **Lines**: 30

**Messages** (1): `OAuth2Credentials`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/oauth2_credentials.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * OAuth2 credentials for authorization code flow authentication.
 * Implements standard OAuth2 authorization code exchange for tokens.
 */
message OAuth2Credentials {
  // Authorization code received from OAuth2 provider
  string code = 1;

  // Redirect URI that was used in the authorization request
  // Must match the URI registered with the OAuth2 provider
  string redirect_uri = 2;

  // OAuth2 client identifier
  string client_id = 3;

  // OAuth2 client secret (for confidential clients only)
  // Should be omitted for public clients (e.g., mobile apps, SPAs)
  string client_secret = 4;
}

```

---

### oauth2_flow_type.proto {#oauth2_flow_type}

**Path**: `pkg/auth/proto/oauth2_flow_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 34

**Enums** (1): `OAuth2FlowType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/oauth2_flow_type.proto
// version: 1.0.0
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * OAuth2 flow types.
 * Defines the different OAuth2 authentication flows supported.
 */
enum OAuth2FlowType {
  // Unspecified flow type
  OAUTH2_FLOW_TYPE_UNSPECIFIED = 0;

  // Authorization code flow
  OAUTH2_FLOW_TYPE_AUTHORIZATION_CODE = 1;

  // Implicit flow
  OAUTH2_FLOW_TYPE_IMPLICIT = 2;

  // Client credentials flow
  OAUTH2_FLOW_TYPE_CLIENT_CREDENTIALS = 3;

  // Device code flow
  OAUTH2_FLOW_TYPE_DEVICE_CODE = 4;
}

```

---

### oauth_client.proto {#oauth_client}

**Path**: `pkg/auth/proto/oauth_client.proto` **Package**: `gcommon.v1.auth` **Lines**: 65

**Messages** (1): `OAuthClient`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/common/proto/resource_status.proto` → [common](./common.md#resource_status)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/oauth_client.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/common/proto/resource_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * OAuth2 client configuration for third-party integrations.
 * Used for OAuth2 authorization code and implicit flows.
 * Contains client credentials and configuration.
 */
message OAuthClient {
  // Unique client identifier
  string client_id = 1;

  // Client secret (for confidential clients)
  string client_secret = 2;

  // Client name
  string name = 3;

  // Client description
  string description = 4;

  // Client type ("public" or "confidential")
  string client_type = 5;

  // Allowed redirect URIs
  repeated string redirect_uris = 6;

  // Allowed grant types
  repeated string grant_types = 7;

  // Allowed response types
  repeated string response_types = 8;

  // Allowed scopes
  repeated string scopes = 9;

  // Client creation timestamp
  google.protobuf.Timestamp created_at = 10 [lazy = true];

  // Client status
  gcommon.v1.common.ResourceStatus status = 11;

  // Client metadata
  map<string, string> metadata = 12 [lazy = true];

  // Client logo URL
  string logo_url = 13;

  // Client website URL
  string website_url = 14;

  // Client owner user ID
  string owner_user_id = 15;
}

```

---

### password_credentials.proto {#password_credentials}

**Path**: `pkg/auth/proto/password_credentials.proto` **Package**: `gcommon.v1.auth` **Lines**: 27

**Messages** (1): `PasswordCredentials`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/password_credentials.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Username/password credentials for traditional authentication.
 * Supports both username and email-based authentication with optional
 * remember-me functionality for extended session duration.
 */
message PasswordCredentials {
  // Username or email address for authentication
  string username = 1;

  // User's password (should be transmitted over secure channels only)
  string password = 2;

  // Remember me option for extended session duration
  // When true, session may have longer expiration time
  bool remember_me = 3;
}

```

---

### password_policy.proto {#password_policy}

**Path**: `pkg/auth/proto/password_policy.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `PasswordPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message PasswordPolicy {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/password_policy.proto
// version: 1.0.0
// guid: d19b7fa7-bd0d-4d6c-bc5b-2453bd250890

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing password policy.
 */
message PasswordPolicy {
  // TODO: Add message fields
}

```

---

### permission.proto {#permission}

**Path**: `pkg/auth/proto/permission.proto` **Package**: `gcommon.v1.auth` **Lines**: 36

**Messages** (1): `Permission`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/scope_type.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/permission.proto
// version: 1.0.0
// guid: 38e2195b-8510-48b4-9c7c-2f87ab8e9a1a

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/scope_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Permission represents a specific action that can be granted
 * to a user or role within the authentication system.
 */
message Permission {
  // Unique identifier for the permission
  string id = 1;

  // Short machine friendly permission name
  string name = 2;

  // Human readable description of what the permission allows
  string description = 3;

  // Scope at which this permission applies
  ScopeType scope = 4;

  // Timestamp when the permission was created
  google.protobuf.Timestamp created_at = 5 [lazy = true];
}

```

---

### permission_grant.proto {#permission_grant}

**Path**: `pkg/auth/proto/permission_grant.proto` **Package**: `gcommon.v1.auth` **Lines**: 50

**Messages** (1): `PermissionGrant`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/permission_scope.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/permission_grant.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/permission_scope.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Permission grant entity representing granted permissions.
 * Used for tracking direct permission assignments to users.
 * Supports scoped permissions and expiration.
 */
message PermissionGrant {
  // Unique grant identifier
  string id = 1;

  // User ID receiving the permission
  string user_id = 2;

  // Permission being granted
  string permission = 3;

  // Resource the permission applies to (optional)
  string resource = 4;

  // Permission scope
  PermissionScope scope = 5;

  // Grant creation timestamp
  google.protobuf.Timestamp created_at = 6 [lazy = true];

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

### permission_metadata.proto {#permission_metadata}

**Path**: `pkg/auth/proto/permission_metadata.proto` **Package**: `gcommon.v1.auth` **Lines**: 55

**Messages** (2): `PermissionMetadata`, `PermissionCondition`

**Enums** (1): `PermissionLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/permission_metadata.proto
// file: auth/proto/types/permission_metadata.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message PermissionMetadata {
  // Permission ID
  string permission_id = 1;

  // Permission name
  string name = 2;

  // Resource types this permission applies to
  repeated string resource_types = 3;

  // Actions allowed by this permission
  repeated string actions = 4;

  // Conditions or constraints
  repeated PermissionCondition conditions = 5;

  // Permission level (system, organization, project, etc.)
  enum PermissionLevel {
    PERMISSION_LEVEL_UNSPECIFIED = 0;
    PERMISSION_LEVEL_SYSTEM = 1;
    PERMISSION_LEVEL_ORGANIZATION = 2;
    PERMISSION_LEVEL_PROJECT = 3;
    PERMISSION_LEVEL_RESOURCE = 4;
  }
  PermissionLevel level = 6;

  // Creation metadata
  int64 created_at = 7;
  string created_by = 8;
}

message PermissionCondition {
  string key = 1;
  string operator = 2; // eq, ne, in, not_in, etc.
  repeated string values = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### permission_scope.proto {#permission_scope}

**Path**: `pkg/auth/proto/permission_scope.proto` **Package**: `gcommon.v1.auth` **Lines**: 34

**Enums** (1): `PermissionScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/permission_scope.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

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

**Path**: `pkg/auth/proto/permission_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 19

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: TODO - // TODO: Add enum definitions here

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/permission_type.proto
// file: auth/proto/enums/permission_type.proto
//
// Enum definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

// TODO: Add enum definitions here

// Implement the actual protobuf definitions according to the auth module requirements

```

---

### provider_type.proto {#provider_type}

**Path**: `pkg/auth/proto/provider_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 33

**Enums** (1): `ProviderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/provider_type.proto
// version: 1.0.0
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f90

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * ProviderType enumerates the supported authentication provider backends.
 */
enum ProviderType {
  // Default unspecified provider type
  PROVIDER_TYPE_UNSPECIFIED = 0;

  // Built-in local provider
  PROVIDER_TYPE_LOCAL = 1;

  // LDAP directory provider
  PROVIDER_TYPE_LDAP = 2;

  // SAML identity provider
  PROVIDER_TYPE_SAML = 3;

  // OAuth2 or OpenID Connect provider
  PROVIDER_TYPE_OAUTH2 = 4;
}

```

---

### refresh_token.proto {#refresh_token}

**Path**: `pkg/auth/proto/refresh_token.proto` **Package**: `gcommon.v1.auth` **Lines**: 28

**Messages** (1): `RefreshToken`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/refresh_token.proto
// version: 1.0.0
// guid: 19426e54-07ed-40a6-bb1a-739ec97c225f

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Refresh token details for token renewal workflows.
 */
message RefreshToken {
  // Refresh token string
  string value = 1;

  // Associated user ID
  string user_id = 2;

  // When the refresh token expires
  google.protobuf.Timestamp expires_at = 3 [lazy = true];
}

```

---

### role.proto {#role}

**Path**: `pkg/auth/proto/role.proto` **Package**: `gcommon.v1.auth` **Lines**: 43

**Messages** (1): `Role`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/resource_status.proto` → [common](./common.md#resource_status)

#### Source Code

```protobuf
// file: pkg/auth/proto/types/role.proto
// version: 1.0.0
// guid: 456e789a-b1c2-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/resource_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Role definition for role-based access control (RBAC).
 * Represents a collection of permissions that can be assigned to users.
 * Supports hierarchical roles and metadata for extensibility.
 */
message Role {
  // Unique role identifier (immutable)
  string id = 1;

  // Human-readable role name
  string name = 2;

  // Role description explaining its purpose
  string description = 3;

  // Permissions granted by this role
  repeated string permissions = 4;

  // Role metadata for extensibility
  map<string, string> metadata = 5 [lazy = true];

  // Role creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 6 [lazy = true];

  // Role status (active, inactive, etc.)
  gcommon.v1.common.ResourceStatus status = 7;
}

```

---

### role_assignment.proto {#role_assignment}

**Path**: `pkg/auth/proto/role_assignment.proto` **Package**: `gcommon.v1.auth` **Lines**: 51

**Messages** (1): `RoleAssignment`

**Imports** (5):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/role.proto`
- `pkg/auth/proto/role_scope.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/role_assignment.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/role.proto";
import "pkg/auth/proto/role_scope.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Role assignment entity representing role grants to users.
 * Used for tracking role-based access control assignments.
 * Supports scoped roles and expiration.
 */
message RoleAssignment {
  // Unique assignment identifier
  string id = 1;

  // User ID receiving the role
  string user_id = 2;

  // Role ID being assigned
  string role_id = 3;

  // Resource the role applies to (optional, for scoped roles)
  string resource = 4;

  // Role scope
  RoleScope scope = 5;

  // Assignment creation timestamp
  google.protobuf.Timestamp created_at = 6 [lazy = true];

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

**Path**: `pkg/auth/proto/role_metadata.proto` **Package**: `gcommon.v1.auth` **Lines**: 29

**Messages** (1): `RoleMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/role.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/role_metadata.proto
// version: 1.0.0
// guid: 1b935f51-d35c-4113-aa68-03457b4294db

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * RoleMetadata provides metadata about role creation and updates.
 */
message RoleMetadata {
  // Timestamp when the role was created
  google.protobuf.Timestamp created_at = 1 [lazy = true];

  // Timestamp of the last update to the role
  google.protobuf.Timestamp updated_at = 2 [lazy = true];

  // User ID that created the role
  string created_by = 3;
}

```

---

### role_scope.proto {#role_scope}

**Path**: `pkg/auth/proto/role_scope.proto` **Package**: `gcommon.v1.auth` **Lines**: 35

**Enums** (1): `RoleScope`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/auth/proto/role.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/role_scope.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "pkg/auth/proto/role.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

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

### scope_type.proto {#scope_type}

**Path**: `pkg/auth/proto/scope_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 34

**Enums** (1): `ScopeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/scope_type.proto
// file: auth/proto/enums/scope_type.proto
//
// Enum definitions for auth module
//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * ScopeType defines the scope at which a permission can be applied
 */
enum ScopeType {
  // Unspecified scope type
  SCOPE_TYPE_UNSPECIFIED = 0;

  // Global scope - applies across the entire system
  SCOPE_TYPE_GLOBAL = 1;

  // Organization scope - applies within a specific organization
  SCOPE_TYPE_ORGANIZATION = 2;

  // Project scope - applies within a specific project
  SCOPE_TYPE_PROJECT = 3;

  // Resource scope - applies to a specific resource
  SCOPE_TYPE_RESOURCE = 4;
}

```

---

### security_context.proto {#security_context}

**Path**: `pkg/auth/proto/security_context.proto` **Package**: `gcommon.v1.auth` **Lines**: 58

**Messages** (1): `SecurityContext`

**Enums** (1): `AuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/security_context.proto
// file: auth/proto/types/security_context.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message SecurityContext {
  // User ID
  string user_id = 1;

  // Session ID
  string session_id = 2;

  // User roles
  repeated string roles = 3;

  // User permissions
  repeated string permissions = 4;

  // Authentication method used
  enum AuthMethod {
    AUTH_METHOD_UNSPECIFIED = 0;
    AUTH_METHOD_PASSWORD = 1;
    AUTH_METHOD_MFA = 2;
    AUTH_METHOD_API_KEY = 3;
    AUTH_METHOD_OAUTH = 4;
    AUTH_METHOD_SSO = 5;
  }
  AuthMethod auth_method = 5;

  // MFA verified
  bool mfa_verified = 6;

  // IP address
  string ip_address = 7;

  // User agent
  string user_agent = 8;

  // Authentication timestamp
  int64 auth_timestamp = 9;

  // Context metadata
  map<string, string> metadata = 10;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### security_policy.proto {#security_policy}

**Path**: `pkg/auth/proto/security_policy.proto` **Package**: `gcommon.v1.auth` **Lines**: 28

**Messages** (1): `SecurityPolicy`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/security_policy.proto
// version: 1.0.0
// guid: 1d12dbb5-c796-48b9-beab-f89a58a4d115

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * SecurityPolicy defines account and token security requirements.
 */
message SecurityPolicy {
  // Minimum password length requirement
  uint32 min_password_length = 1;

  // Password expiration duration
  google.protobuf.Duration password_ttl = 2;

  // Maximum failed login attempts before lockout
  uint32 max_failed_attempts = 3;
}

```

---

### session.proto {#session}

**Path**: `pkg/auth/proto/session.proto` **Package**: `gcommon.v1.auth` **Lines**: 50

**Messages** (1): `Session`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/session_status.proto`
- `pkg/common/proto/client_info.proto` → [common](./common.md#client_info)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/session.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/session_status.proto";
import "pkg/common/proto/client_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Session information representing an authenticated user session.
 * Contains session lifecycle data, client information, and metadata
 * for session management and security tracking.
 */
message Session {
  // Unique session identifier (immutable)
  string id = 1;

  // User ID associated with this session
  string user_id = 2;

  // Session creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 3 [lazy = true];

  // Last activity timestamp (updated on each request)
  google.protobuf.Timestamp last_activity_at = 4 [lazy = true];

  // Session expiration timestamp
  google.protobuf.Timestamp expires_at = 5 [lazy = true];

  // Client information from session creation
  gcommon.v1.common.ClientInfo client_info = 6 [lazy = true];

  // Current session status
  SessionStatus status = 7;

  // Session metadata for extensibility and tracking
  map<string, string> metadata = 8 [lazy = true];

  // IP address when session was created
  string ip_address = 9;

  // User agent when session was created
  string user_agent = 10;
}

```

---

### session_info.proto {#session_info}

**Path**: `pkg/auth/proto/session_info.proto` **Package**: `gcommon.v1.auth` **Lines**: 42

**Messages** (1): `SessionInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/session_info.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Session information for lightweight session tracking.
 * Contains essential session data without full session details.
 * Used in responses where full session data is not needed.
 */
message SessionInfo {
  // Session identifier
  string session_id = 1;

  // User ID associated with session
  string user_id = 2;

  // Session creation time
  google.protobuf.Timestamp created_at = 3;

  // Session expiration time
  google.protobuf.Timestamp expires_at = 4;

  // Last activity time
  google.protobuf.Timestamp last_activity_at = 5;

  // IP address
  string ip_address = 6;

  // User agent
  string user_agent = 7;

  // Session active flag
  bool active = 8;
}

```

---

### session_metadata.proto {#session_metadata}

**Path**: `pkg/auth/proto/session_metadata.proto` **Package**: `gcommon.v1.auth` **Lines**: 73

**Messages** (3): `SessionMetadata`, `DeviceInfo`, `LocationInfo`

**Enums** (1): `SessionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/session_metadata.proto
// file: auth/proto/types/session_metadata.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message SessionMetadata {
  // Session ID
  string session_id = 1;

  // User ID
  string user_id = 2;

  // Session start time
  int64 started_at = 3;

  // Last activity time
  int64 last_activity = 4;

  // Session expiry time
  int64 expires_at = 5;

  // IP address
  string ip_address = 6;

  // User agent
  string user_agent = 7;

  // Device information
  DeviceInfo device_info = 8;

  // Location information
  LocationInfo location_info = 9;

  // Session state
  enum SessionState {
    SESSION_STATE_UNSPECIFIED = 0;
    SESSION_STATE_ACTIVE = 1;
    SESSION_STATE_IDLE = 2;
    SESSION_STATE_EXPIRED = 3;
    SESSION_STATE_TERMINATED = 4;
  }
  SessionState state = 10;
}

message DeviceInfo {
  string device_id = 1;
  string device_type = 2; // mobile, desktop, tablet
  string os = 3;
  string browser = 4;
  bool is_trusted = 5;
}

message LocationInfo {
  string country = 1;
  string region = 2;
  string city = 3;
  double latitude = 4;
  double longitude = 5;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### session_status.proto {#session_status}

**Path**: `pkg/auth/proto/session_status.proto` **Package**: `gcommon.v1.auth` **Lines**: 31

**Enums** (1): `SessionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/session_status.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Session status enumeration defining the current state of a user session.
 * Used for session lifecycle management and security validation.
 */
enum SessionStatus {
  // Default value indicating no status was specified
  SESSION_STATUS_UNSPECIFIED = 0;

  // Session is active and valid for authentication
  SESSION_STATUS_ACTIVE = 1;

  // Session has expired based on time-based expiration
  SESSION_STATUS_EXPIRED = 2;

  // Session was explicitly terminated (logout)
  SESSION_STATUS_TERMINATED = 3;

  // Session is invalid due to security concerns or corruption
  SESSION_STATUS_INVALID = 4;
}

```

---

### token.proto {#token}

**Path**: `pkg/auth/proto/token.proto` **Package**: `gcommon.v1.auth` **Lines**: 62

**Messages** (1): `Token`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/token_status.proto`
- `pkg/auth/proto/token_type.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/token.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/token_status.proto";
import "pkg/auth/proto/token_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Token entity representing authentication and authorization tokens.
 * Used for access tokens, refresh tokens, and other security tokens.
 * Contains token metadata and lifecycle information.
 */
message Token {
  // Unique token identifier
  string id = 1;

  // Token value (may be JWT or opaque)
  string value = 2;

  // Token type (access, refresh, etc.)
  TokenType type = 3;

  // Token status
  TokenStatus status = 4;

  // User ID associated with this token
  string user_id = 5;

  // Client ID that requested this token
  string client_id = 6;

  // Token scopes/permissions
  repeated string scopes = 7;

  // Token creation timestamp
  google.protobuf.Timestamp created_at = 8 [lazy = true];

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 9 [lazy = true];

  // Last time token was used
  google.protobuf.Timestamp last_used_at = 10 [lazy = true];

  // Token metadata for extensibility
  map<string, string> metadata = 11 [lazy = true];

  // IP address when token was created
  string ip_address = 12;

  // User agent when token was created
  string user_agent = 13;

  // Refresh token ID (for access tokens)
  string refresh_token_id = 14;
}

```

---

### token_info.proto {#token_info}

**Path**: `pkg/auth/proto/token_info.proto` **Package**: `gcommon.v1.auth` **Lines**: 47

**Messages** (1): `TokenInfo`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/token_type.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/token_info.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/token_type.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Token information for lightweight token tracking.
 * Contains essential token data without sensitive information.
 * Used in responses where full token data is not needed.
 */
message TokenInfo {
  // Token identifier
  string token_id = 1;

  // Token type
  TokenType type = 2;

  // User ID associated with token
  string user_id = 3;

  // Client ID that owns the token
  string client_id = 4;

  // Token scopes
  repeated string scopes = 5;

  // Token creation time
  google.protobuf.Timestamp created_at = 6;

  // Token expiration time
  google.protobuf.Timestamp expires_at = 7;

  // Token active flag
  bool active = 8;

  // Time until expiration (seconds)
  int64 expires_in = 9;
}

```

---

### token_metadata.proto {#token_metadata}

**Path**: `pkg/auth/proto/token_metadata.proto` **Package**: `gcommon.v1.auth` **Lines**: 54

**Messages** (1): `TokenMetadata`

**Enums** (1): `TokenType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/types/token_metadata.proto
// file: auth/proto/types/token_metadata.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

message TokenMetadata {
  // Token ID
  string token_id = 1;

  // Token type
  enum TokenType {
    TOKEN_TYPE_UNSPECIFIED = 0;
    TOKEN_TYPE_ACCESS = 1;
    TOKEN_TYPE_REFRESH = 2;
    TOKEN_TYPE_ID = 3;
    TOKEN_TYPE_API_KEY = 4;
  }
  TokenType type = 2;

  // Subject (user ID)
  string subject = 3;

  // Audience
  repeated string audience = 4;

  // Scopes
  repeated string scopes = 5;

  // Issued at timestamp
  int64 issued_at = 6;

  // Expires at timestamp
  int64 expires_at = 7;

  // Not before timestamp
  int64 not_before = 8;

  // Issuer
  string issuer = 9;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation

```

---

### token_status.proto {#token_status}

**Path**: `pkg/auth/proto/token_status.proto` **Package**: `gcommon.v1.auth` **Lines**: 37

**Enums** (1): `TokenStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/token_status.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Token status enumeration for tracking token lifecycle.
 * Used for token management and security validation.
 */
enum TokenStatus {
  // Unspecified token status
  TOKEN_STATUS_UNSPECIFIED = 0;

  // Token is active and valid
  TOKEN_STATUS_ACTIVE = 1;

  // Token has expired
  TOKEN_STATUS_EXPIRED = 2;

  // Token has been revoked
  TOKEN_STATUS_REVOKED = 3;

  // Token is suspended (temporarily inactive)
  TOKEN_STATUS_SUSPENDED = 4;

  // Token is pending activation
  TOKEN_STATUS_PENDING = 5;

  // Token is invalid (malformed or corrupted)
  TOKEN_STATUS_INVALID = 6;
}

```

---

### token_type.proto {#token_type}

**Path**: `pkg/auth/proto/token_type.proto` **Package**: `gcommon.v1.auth` **Lines**: 49

**Enums** (1): `TokenType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/token_type.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Token type enumeration for different kinds of authentication tokens.
 * Used to distinguish between access tokens, refresh tokens, and other token types.
 */
enum TokenType {
  // Unspecified token type
  TOKEN_TYPE_UNSPECIFIED = 0;

  // Access token for API authentication
  TOKEN_TYPE_ACCESS = 1;

  // Refresh token for token renewal
  TOKEN_TYPE_REFRESH = 2;

  // ID token for user identity (OpenID Connect)
  TOKEN_TYPE_ID = 3;

  // Authorization code for OAuth2 flows
  TOKEN_TYPE_AUTHORIZATION_CODE = 4;

  // API key token for service authentication
  TOKEN_TYPE_API_KEY = 5;

  // Session token for web sessions
  TOKEN_TYPE_SESSION = 6;

  // Password reset token
  TOKEN_TYPE_PASSWORD_RESET = 7;

  // Email verification token
  TOKEN_TYPE_EMAIL_VERIFICATION = 8;

  // Phone verification token
  TOKEN_TYPE_PHONE_VERIFICATION = 9;

  // Invitation token
  TOKEN_TYPE_INVITATION = 10;
}

```

---

### user.proto {#user}

**Path**: `pkg/auth/proto/user.proto` **Package**: `gcommon.v1.auth` **Lines**: 73

**Messages** (1): `User`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/auth/proto/user_status.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/user.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/auth/proto/user_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * User entity representing a complete user account.
 * Contains comprehensive user data for account management.
 * Includes profile, security, and administrative information.
 */
message User {
  // Unique user identifier (immutable)
  string id = 1;

  // Username (may be mutable depending on system policy)
  string username = 2;

  // Primary email address
  string email = 3;

  // Display name
  string display_name = 4;

  // First name
  string first_name = 5;

  // Last name
  string last_name = 6;

  // User account status
  UserStatus status = 7;

  // Account creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 8 [lazy = true];

  // Last account update timestamp
  google.protobuf.Timestamp updated_at = 9 [lazy = true];

  // Last successful login timestamp
  google.protobuf.Timestamp last_login_at = 10 [lazy = true];

  // Email verification status
  bool email_verified = 11;

  // Phone number (optional)
  string phone_number = 12;

  // Phone verification status
  bool phone_verified = 13;

  // User preferences and settings
  map<string, string> preferences = 14 [lazy = true];

  // User metadata for extensibility
  map<string, string> metadata = 15 [lazy = true];

  // Avatar/profile image URL
  string avatar_url = 16;

  // User timezone
  string timezone = 17;

  // User locale/language preference
  string locale = 18;
}

```

---

### user_info.proto {#user_info}

**Path**: `pkg/auth/proto/user_info.proto` **Package**: `gcommon.v1.auth` **Lines**: 61

**Messages** (1): `UserInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/messages/user_info.proto
// version: 1.0.0
// guid: a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * UserInfo contains information about a user.
 */
message UserInfo {
  // Unique user identifier
  string user_id = 1;

  // Username
  string username = 2;

  // User's email address
  string email = 3;

  // User's display name
  string display_name = 4;

  // User roles
  repeated string roles = 5;

  // User permissions
  repeated string permissions = 6;

  // User groups
  repeated string groups = 7;

  // User metadata
  map<string, string> metadata = 8;

  // When the user was created
  google.protobuf.Timestamp created_at = 9;

  // When the user was last updated
  google.protobuf.Timestamp updated_at = 10;

  // When the user last logged in
  google.protobuf.Timestamp last_login_at = 11;

  // Whether the user account is active
  bool active = 12;

  // Whether the user's email is verified
  bool email_verified = 13;

  // User's profile picture URL
  string avatar_url = 14;
}

```

---

### user_metadata.proto {#user_metadata}

**Path**: `pkg/auth/proto/user_metadata.proto` **Package**: `gcommon.v1.auth` **Lines**: 114

**Messages** (3): `UserMetadata`, `UserPreferences`, `VerificationStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/user_metadata.proto
// version: 1.0.0
// guid: c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * User metadata containing profile and preference information.
 * Stores additional user data beyond basic authentication credentials.
 */
message UserMetadata {
  // User's preferred display name
  string display_name = 1;

  // User's profile picture URL
  string avatar_url = 2;

  // User's timezone
  string timezone = 3;

  // User's preferred language
  string language = 4;

  // User's locale
  string locale = 5;

  // User's profile bio/description
  string bio = 6;

  // User's website URL
  string website = 7;

  // User's location/address
  string location = 8;

  // Date of birth for age verification purposes
  google.protobuf.Timestamp birth_date = 9;

  // User's gender
  string gender = 10;

  // User's occupation/job title
  string occupation = 11;

  // User's company/organization
  string company = 12;

  // Additional custom metadata
  map<string, string> custom_fields = 13;

  // User preferences
  UserPreferences preferences = 14;

  // Account verification status
  VerificationStatus verification = 15;
}

/**
 * User preferences and settings.
 */
message UserPreferences {
  // Email notification preferences
  bool email_notifications = 1;

  // SMS notification preferences
  bool sms_notifications = 2;

  // Push notification preferences
  bool push_notifications = 3;

  // Marketing email preferences
  bool marketing_emails = 4;

  // Two-factor authentication enabled
  bool two_factor_enabled = 5;

  // Session timeout preference (minutes)
  int32 session_timeout_minutes = 6;

  // Theme preference (light, dark, auto)
  string theme = 7;
}

/**
 * Account verification status information.
 */
message VerificationStatus {
  // Email verification status
  bool email_verified = 1;

  // Phone number verification status
  bool phone_verified = 2;

  // Identity verification status
  bool identity_verified = 3;

  // When email was verified
  google.protobuf.Timestamp email_verified_at = 4;

  // When phone was verified
  google.protobuf.Timestamp phone_verified_at = 5;

  // When identity was verified
  google.protobuf.Timestamp identity_verified_at = 6;
}

```

---

### user_profile.proto {#user_profile}

**Path**: `pkg/auth/proto/user_profile.proto` **Package**: `gcommon.v1.auth` **Lines**: 20

**Messages** (1): `UserProfile`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (2)

- Line 17: Empty message - message UserProfile {
- Line 18: TODO - // TODO: Add message fields

#### Source Code

```protobuf
// file: pkg/auth/proto/user_profile.proto
// version: 1.0.0
// guid: 9554454d-6823-42b3-aac9-341f375031ea

edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * Message representing user profile.
 */
message UserProfile {
  // TODO: Add message fields
}

```

---

### user_status.proto {#user_status}

**Path**: `pkg/auth/proto/user_status.proto` **Package**: `gcommon.v1.auth` **Lines**: 37

**Enums** (1): `UserStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/auth/proto/enums/user_status.proto
edition = "2023";

package gcommon.v1.auth;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto";

/**
 * User account status enumeration defining the state of a user account.
 * Used to track account lifecycle, security status, and access permissions.
 */
enum UserStatus {
  // Default value indicating no status was specified
  USER_STATUS_UNSPECIFIED = 0;

  // User account is active and in good standing
  USER_STATUS_ACTIVE = 1;

  // User account is inactive (user-initiated or policy-based)
  USER_STATUS_INACTIVE = 2;

  // User account is suspended due to policy violations or security concerns
  USER_STATUS_SUSPENDED = 3;

  // User account is pending email or identity verification
  USER_STATUS_PENDING_VERIFICATION = 4;

  // User account is locked due to security concerns (e.g., too many failed login attempts)
  USER_STATUS_LOCKED = 5;

  // User account has been soft-deleted and marked for cleanup
  USER_STATUS_DELETED = 6;
}

```

---
