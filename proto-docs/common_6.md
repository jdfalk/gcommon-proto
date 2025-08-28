# common_6 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 41
- **Messages**: 12
- **Services**: 0
- **Enums**: 29

## Files in this Module

- [template_status.proto](#template_status)
- [tenant_status.proto](#tenant_status)
- [time_range_metrics.proto](#time_range_metrics)
- [time_restriction.proto](#time_restriction)
- [time_unit.proto](#time_unit)
- [time_window.proto](#time_window)
- [token.proto](#token)
- [token_info.proto](#token_info)
- [token_metadata.proto](#token_metadata)
- [token_status.proto](#token_status)
- [token_type.proto](#token_type)
- [transformation_type.proto](#transformation_type)
- [two_fa_type.proto](#two_fa_type)
- [user.proto](#user)
- [user_details.proto](#user_details)
- [user_info.proto](#user_info)
- [user_metadata.proto](#user_metadata)
- [user_preferences.proto](#user_preferences)
- [user_profile.proto](#user_profile)
- [user_status.proto](#user_status)
- [validation_result_type.proto](#validation_result_type)
- [validation_rule_severity.proto](#validation_rule_severity)
- [validation_rule_type.proto](#validation_rule_type)
- [validation_severity.proto](#validation_severity)
- [value_source.proto](#value_source)
- [value_status.proto](#value_status)
- [value_type.proto](#value_type)
- [value_validation_result_type.proto](#value_validation_result_type)
- [value_validation_severity.proto](#value_validation_severity)
- [verification_status.proto](#verification_status)
- [verification_type.proto](#verification_type)
- [version_dependency_type.proto](#version_dependency_type)
- [version_deployment_status.proto](#version_deployment_status)
- [version_health_status.proto](#version_health_status)
- [version_status.proto](#version_status)
- [version_type.proto](#version_type)
- [visualization_type.proto](#visualization_type)
- [web_auth_method.proto](#web_auth_method)
- [web_session_state.proto](#web_session_state)
- [web_socket_state.proto](#web_socket_state)
- [write_level.proto](#write_level)
---


## Detailed Documentation

### template_status.proto {#template_status}

**Path**: `gcommon/v1/common/template_status.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `TemplateStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_status.proto
// version: 1.0.1
// guid: fcaf0275-1145-4c6c-af44-a4386dd4c2a7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TemplateStatus {
  TEMPLATE_STATUS_UNSPECIFIED = 0;
  TEMPLATE_STATUS_DRAFT = 1;
  TEMPLATE_STATUS_ACTIVE = 2;
  TEMPLATE_STATUS_DEPRECATED = 3;
  TEMPLATE_STATUS_ARCHIVED = 4;
  TEMPLATE_STATUS_DELETED = 5;
}
```

---

### tenant_status.proto {#tenant_status}

**Path**: `gcommon/v1/common/tenant_status.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Enums** (1): `TenantStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/tenant_status.proto
// version: 1.0.1
// guid: 180914cf-dfc6-4920-bf56-9a4b6972db9d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Tenant status enumeration defining the state of a tenant within an organization.
 * Used for multi-tenant architecture to control tenant access and operations.
 */
enum TenantStatus {
  // Default value indicating no status was specified
  TENANT_STATUS_UNSPECIFIED = 0;

  // Tenant is active and operational
  TENANT_STATUS_ACTIVE = 1;

  // Tenant is inactive (temporarily disabled)
  TENANT_STATUS_INACTIVE = 2;

  // Tenant is suspended due to policy violations or resource limits
  TENANT_STATUS_SUSPENDED = 3;

  // Tenant is pending setup or verification
  TENANT_STATUS_PENDING = 4;

  // Tenant has exceeded resource quotas and is throttled
  TENANT_STATUS_QUOTA_EXCEEDED = 5;

  // Tenant is in trial period with limited features
  TENANT_STATUS_TRIAL = 6;

  // Tenant is archived (read-only access)
  TENANT_STATUS_ARCHIVED = 7;

  // Tenant is marked for deletion
  TENANT_STATUS_DELETED = 8;
}
```

---

### time_range_metrics.proto {#time_range_metrics}

**Path**: `gcommon/v1/common/time_range_metrics.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `TimeRangeMetrics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_range.proto
// version: 1.0.0
// guid: d6e7f8a9-012d-467c-1234-789012345678

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TimeRangeMetrics {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;

  // Duration in seconds
  int64 duration_seconds = 3 [(buf.validate.field).int64.gt = 0];
}
```

---

### time_restriction.proto {#time_restriction}

**Path**: `gcommon/v1/common/time_restriction.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `TimeRestriction`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/time_restriction.proto
// version: 1.0.0
// guid: e1c0e36e-397a-42c1-a74a-e7aeca18ade2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TimeRestriction {
  // Day of week (0-6, 0=Sunday)
  int32 day_of_week = 1 [(buf.validate.field).int32.gte = 0];

  // Start time (24-hour format, e.g., "09:00")
  string start_time = 2 [(buf.validate.field).string.min_len = 1];

  // End time (24-hour format, e.g., "17:00")
  string end_time = 3 [(buf.validate.field).string.min_len = 1];

  // Timezone for this restriction
  string timezone = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### time_unit.proto {#time_unit}

**Path**: `gcommon/v1/common/time_unit.proto` **Package**: `gcommon.v1.common` **Lines**: 55

**Enums** (1): `TimeUnit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_unit.proto
// version: 1.0.1
// guid: a2bc1886-34e7-4229-93b2-c279f6d89b7a
// file: proto/gcommon/v1/metrics/v1/time_unit.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * TimeUnit defines the units of time for metric intervals, retention, and aggregation.
 * Used throughout the metrics system for temporal operations.
 */
enum TimeUnit {
  // Unspecified time unit (default)
  TIME_UNIT_UNSPECIFIED = 0;

  // Nanoseconds
  TIME_UNIT_NANOSECONDS = 1;

  // Microseconds
  TIME_UNIT_MICROSECONDS = 2;

  // Milliseconds
  TIME_UNIT_MILLISECONDS = 3;

  // Seconds
  TIME_UNIT_SECONDS = 4;

  // Minutes
  TIME_UNIT_MINUTES = 5;

  // Hours
  TIME_UNIT_HOURS = 6;

  // Days
  TIME_UNIT_DAYS = 7;

  // Weeks
  TIME_UNIT_WEEKS = 8;

  // Months
  TIME_UNIT_MONTHS = 9;

  // Years
  TIME_UNIT_YEARS = 10;
}
```

---

### time_window.proto {#time_window}

**Path**: `gcommon/v1/common/time_window.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `TimeWindow`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_window.proto
// version: 1.0.1
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// TimeWindow represents different time windows for metrics aggregation
enum TimeWindow {
  // Unspecified time window
  TIME_WINDOW_UNSPECIFIED = 0;

  // 1 minute window
  TIME_WINDOW_1_MINUTE = 1;

  // 5 minute window
  TIME_WINDOW_5_MINUTES = 2;

  // 15 minute window
  TIME_WINDOW_15_MINUTES = 3;

  // 30 minute window
  TIME_WINDOW_30_MINUTES = 4;

  // 1 hour window
  TIME_WINDOW_1_HOUR = 5;

  // 4 hour window
  TIME_WINDOW_4_HOURS = 6;

  // 12 hour window
  TIME_WINDOW_12_HOURS = 7;

  // 1 day window
  TIME_WINDOW_1_DAY = 8;

  // 1 week window
  TIME_WINDOW_1_WEEK = 9;

  // 1 month window
  TIME_WINDOW_1_MONTH = 10;

  // 1 year window
  TIME_WINDOW_1_YEAR = 11;

  // Custom time window
  TIME_WINDOW_CUSTOM = 12;
}
```

---

### token.proto {#token}

**Path**: `gcommon/v1/common/token.proto` **Package**: `gcommon.v1.common` **Lines**: 70

**Messages** (1): `Token`

**Imports** (5):

- `gcommon/v1/common/token_status.proto`
- `gcommon/v1/common/token_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token.proto
// version: 1.0.0
// guid: caf60cc1-beab-4119-bb01-f426fbb8b680
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/token_status.proto";
import "gcommon/v1/common/token_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Token entity representing authentication and authorization tokens.
 * Used for access tokens, refresh tokens, and other security tokens.
 * Contains token metadata and lifecycle information.
 */
message Token {
  // Unique token identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Token value (may be JWT or opaque)
  string value = 2;

  // Token type (access, refresh, etc.)
  gcommon.v1.common.TokenType type = 3;

  // Token status
  gcommon.v1.common.TokenStatus status = 4;

  // User ID associated with this token
  string user_id = 5 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Client ID that requested this token
  string client_id = 6;

  // Token scopes/permissions
  repeated string scopes = 7;

  // Token creation timestamp
  google.protobuf.Timestamp created_at = 8 [lazy = true, (buf.validate.field).required = true];

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

**Path**: `gcommon/v1/common/token_info.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Messages** (1): `TokenInfo`

**Imports** (4):

- `gcommon/v1/common/token_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_info.proto
// version: 1.0.0
// guid: 4c29c1f8-c076-4308-b035-5ac388999383
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/token_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Token information for lightweight token tracking.
 * Contains essential token data without sensitive information.
 * Used in responses where full token data is not needed.
 */
message TokenInfo {
  // Token identifier
  string token_id = 1;

  // Token type
  gcommon.v1.common.TokenType type = 2;

  // User ID associated with token
  string user_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Client ID that owns the token
  string client_id = 4;

  // Token scopes
  repeated string scopes = 5;

  // Token creation time
  google.protobuf.Timestamp created_at = 6 [ (buf.validate.field).required = true ];

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

**Path**: `gcommon/v1/common/token_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `TokenMetadata`

**Imports** (3):

- `gcommon/v1/common/token_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_metadata.proto
// version: 1.0.0
// guid: 038ee237-f0cb-43e1-95c5-5869754a969d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/token_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TokenMetadata {
  // Token ID
  string token_id = 1 [(buf.validate.field).string.min_len = 1];

  // Token type
  gcommon.v1.common.TokenType type = 2;

  // Subject (user ID)
  string subject = 3 [(buf.validate.field).string.min_len = 1];

  // Audience
  repeated string audience = 4 [(buf.validate.field).repeated.min_items = 1];

  // Scopes
  repeated string scopes = 5 [(buf.validate.field).repeated.min_items = 1];

  // Issued at timestamp
  int64 issued_at = 6 [(buf.validate.field).int64.gte = 0];

  // Expires at timestamp
  int64 expires_at = 7 [(buf.validate.field).int64.gte = 0];

  // Not before timestamp
  int64 not_before = 8 [(buf.validate.field).int64.gte = 0];

  // Issuer
  string issuer = 9 [(buf.validate.field).string.min_len = 1];
}
```

---

### token_status.proto {#token_status}

**Path**: `gcommon/v1/common/token_status.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `TokenStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_status.proto
// version: 1.0.1
// guid: 3d813f39-ef48-4c3e-b551-46ae673e7af1
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/token_type.proto` **Package**: `gcommon.v1.common` **Lines**: 50

**Enums** (1): `TokenType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_type.proto
// version: 1.0.1
// guid: fe1ca2c9-528e-4485-8890-6b151d7d47ae
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### transformation_type.proto {#transformation_type}

**Path**: `gcommon/v1/common/transformation_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `TransformationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/transformation_type.proto
// version: 1.0.1
// guid: 9c4d5ef1-c4a7-4f98-9315-43c2517e6f41

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TransformationType {
  TRANSFORMATION_TYPE_UNSPECIFIED = 0;
  TRANSFORMATION_TYPE_TEMPLATE = 1;
  TRANSFORMATION_TYPE_FUNCTION = 2;
  TRANSFORMATION_TYPE_SCRIPT = 3;
  TRANSFORMATION_TYPE_REGEX = 4;
  TRANSFORMATION_TYPE_JSONPATH = 5;
  TRANSFORMATION_TYPE_XPATH = 6;
  TRANSFORMATION_TYPE_CUSTOM = 7;
}
```

---

### two_fa_type.proto {#two_fa_type}

**Path**: `gcommon/v1/common/two_fa_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `AuthTwoFaType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/two_fa_type.proto
// version: 1.0.1
// guid: dcad7fe3-8803-479a-b205-bff3accb74d5

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthTwoFaType {
  TWO_FA_TYPE_UNSPECIFIED = 0;
  TWO_FA_TYPE_TOTP = 1; // Time-based One-Time Password
  TWO_FA_TYPE_SMS = 2; // SMS code
  TWO_FA_TYPE_BACKUP = 3; // Backup code
}
```

---

### user.proto {#user}

**Path**: `gcommon/v1/common/user.proto` **Package**: `gcommon.v1.common` **Lines**: 87

**Messages** (1): `User`

**Imports** (4):

- `gcommon/v1/common/user_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user.proto
// version: 1.0.0
// guid: 00ae1e1a-a2c9-4e7a-bd91-dda7967d8647
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * User entity representing a complete user account.
 * Contains comprehensive user data for account management.
 * Includes profile, security, and administrative information.
 */
message User {
  // Unique user identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username (may be mutable depending on system policy)
  string username = 2;

  // Primary email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Display name
  string display_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // First name
  string first_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Last name
  string last_name = 6 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // User account status
  gcommon.v1.common.UserStatus status = 7;

  // Account creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 8 [lazy = true, (buf.validate.field).required = true];

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
  string avatar_url = 16 [ (buf.validate.field).string.uri = true ];

  // User timezone
  string timezone = 17;

  // User locale/language preference
  string locale = 18;
}
```

---

### user_details.proto {#user_details}

**Path**: `gcommon/v1/common/user_details.proto` **Package**: `gcommon.v1.common` **Lines**: 70

**Messages** (1): `UserDetails`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_details.proto
// version: 1.0.0
// guid: 3dfa4bc7-c4c7-4c1c-89e9-e3e3d3219d52

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UserDetails {
  // Unique identifier for the user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username
  string username = 2;

  // Email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Full name
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account is enabled
  bool enabled = 5;

  // Assigned roles
  repeated string roles = 6;

  // User permissions
  repeated string permissions = 7;

  // Additional metadata
  map<string, string> metadata = 8;

  // When the account was created
  google.protobuf.Timestamp created_at = 9 [ (buf.validate.field).required = true ];

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
```

---

### user_info.proto {#user_info}

**Path**: `gcommon/v1/common/user_info.proto` **Package**: `gcommon.v1.common` **Lines**: 67

**Messages** (1): `UserInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_info.proto
// version: 1.0.0
// guid: a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * UserInfo contains information about a user.
 */
message UserInfo {
  // Unique user identifier
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username
  string username = 2;

  // User's email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // User's display name
  string display_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // User roles
  repeated string roles = 5;

  // User permissions
  repeated string permissions = 6;

  // User groups
  repeated string groups = 7;

  // User metadata
  map<string, string> metadata = 8;

  // When the user was created
  google.protobuf.Timestamp created_at = 9 [ (buf.validate.field).required = true ];

  // When the user was last updated
  google.protobuf.Timestamp updated_at = 10;

  // When the user last logged in
  google.protobuf.Timestamp last_login_at = 11;

  // Whether the user account is active
  bool active = 12;

  // Whether the user's email is verified
  bool email_verified = 13;

  // User's profile picture URL
  string avatar_url = 14 [ (buf.validate.field).string.uri = true ];
}
```

---

### user_metadata.proto {#user_metadata}

**Path**: `gcommon/v1/common/user_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 66

**Messages** (1): `UserMetadata`

**Imports** (5):

- `gcommon/v1/common/user_preferences.proto`
- `gcommon/v1/common/verification_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_metadata.proto
// version: 1.0.0
// guid: 18290eba-bd6e-4e3a-8aea-ffb79b9fa0f9

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_preferences.proto";
import "gcommon/v1/common/verification_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UserMetadata {
  // User's preferred display name
  string display_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // User's profile picture URL
  string avatar_url = 2 [ (buf.validate.field).string.uri = true ];

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
  gcommon.v1.common.UserPreferences preferences = 14;

  // Account verification status
  gcommon.v1.common.VerificationStatus verification = 15;
}
```

---

### user_preferences.proto {#user_preferences}

**Path**: `gcommon/v1/common/user_preferences.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `UserPreferences`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_preferences.proto
// version: 1.0.0
// guid: 484a49f6-ee77-4683-b2f7-3bb3f64107f9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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
  int32 session_timeout_minutes = 6 [(buf.validate.field).int32.gt = 0];

  // Theme preference (light, dark, auto)
  string theme = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### user_profile.proto {#user_profile}

**Path**: `gcommon/v1/common/user_profile.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Messages** (1): `UserProfile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_profile.proto
// version: 1.0.0
// guid: 9554454d-6823-42b3-aac9-341f375031ea

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Public profile information for a user.
 */
message UserProfile {
  // Unique identifier for the user.
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Display name for the user.
  string display_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Primary email address.
  string email = 3 [ (buf.validate.field).string.email = true ];

  // URL to the user's avatar image.
  string avatar_url = 4 [ (buf.validate.field).string.uri = true ];

  // Additional custom attributes for the profile.
  map<string, string> attributes = 5 [lazy = true];
}
```

---

### user_status.proto {#user_status}

**Path**: `gcommon/v1/common/user_status.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `UserStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_status.proto
// version: 1.0.1
// guid: 8cc7b811-529b-4c10-8615-1593d65d7c0d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### validation_result_type.proto {#validation_result_type}

**Path**: `gcommon/v1/common/validation_result_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `ValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_result_type.proto
// version: 1.0.1
// guid: e7f8a9b0-c1d2-3e4f-5a6b-7c8d9e0f1a2b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ValidationResultType represents the result of validation.
 * Specifies the outcome of configuration validation checks.
 */
enum ValidationResultType {
  // Unspecified validation result
  VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;

  // Validation passed
  VALIDATION_RESULT_TYPE_PASS = 1;

  // Validation failed
  VALIDATION_RESULT_TYPE_FAIL = 2;

  // Validation completed with warnings
  VALIDATION_RESULT_TYPE_WARNING = 3;

  // Validation was skipped
  VALIDATION_RESULT_TYPE_SKIP = 4;
}
```

---

### validation_rule_severity.proto {#validation_rule_severity}

**Path**: `gcommon/v1/common/validation_rule_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValidationRuleSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_rule_severity.proto
// version: 1.0.1
// guid: 49607ba0-0d79-4402-a891-1a5d80c4286f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValidationRuleSeverity {
  VALIDATION_RULE_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_RULE_SEVERITY_INFO = 1;
  VALIDATION_RULE_SEVERITY_WARNING = 2;
  VALIDATION_RULE_SEVERITY_ERROR = 3;
  VALIDATION_RULE_SEVERITY_CRITICAL = 4;
}
```

---

### validation_rule_type.proto {#validation_rule_type}

**Path**: `gcommon/v1/common/validation_rule_type.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `ValidationRuleType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_rule_type.proto
// version: 1.0.1
// guid: 604ea5f1-2b57-45ce-9711-be0f342bde10

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValidationRuleType {
  VALIDATION_RULE_TYPE_UNSPECIFIED = 0;
  VALIDATION_RULE_TYPE_REGEX = 1;
  VALIDATION_RULE_TYPE_RANGE = 2;
  VALIDATION_RULE_TYPE_LENGTH = 3;
  VALIDATION_RULE_TYPE_FORMAT = 4;
  VALIDATION_RULE_TYPE_ENUM = 5;
  VALIDATION_RULE_TYPE_CUSTOM = 6;
  VALIDATION_RULE_TYPE_FUNCTION = 7;
  VALIDATION_RULE_TYPE_SCHEMA = 8;
}
```

---

### validation_severity.proto {#validation_severity}

**Path**: `gcommon/v1/common/validation_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_severity.proto
// version: 1.0.1
// guid: e0f1a2b3-4567-890b-4567-012345678901

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValidationSeverity {
  VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_SEVERITY_INFO = 1;
  VALIDATION_SEVERITY_WARNING = 2;
  VALIDATION_SEVERITY_ERROR = 3;
  VALIDATION_SEVERITY_CRITICAL = 4;
}
```

---

### value_source.proto {#value_source}

**Path**: `gcommon/v1/common/value_source.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `ValueSource`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_source.proto
// version: 1.0.1
// guid: a06a0eb7-f579-4539-87e5-4f5bf9181601

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueSource {
  VALUE_SOURCE_UNSPECIFIED = 0;
  VALUE_SOURCE_DEFAULT = 1;
  VALUE_SOURCE_ENVIRONMENT = 2;
  VALUE_SOURCE_FILE = 3;
  VALUE_SOURCE_DATABASE = 4;
  VALUE_SOURCE_CONSUL = 5;
  VALUE_SOURCE_ETCD = 6;
  VALUE_SOURCE_KUBERNETES = 7;
  VALUE_SOURCE_VAULT = 8;
  VALUE_SOURCE_AWS_PARAMETER_STORE = 9;
  VALUE_SOURCE_AWS_SECRETS_MANAGER = 10;
  VALUE_SOURCE_AZURE_KEY_VAULT = 11;
  VALUE_SOURCE_GCP_SECRET_MANAGER = 12;
  VALUE_SOURCE_REDIS = 13;
  VALUE_SOURCE_API = 14;
  VALUE_SOURCE_COMMAND_LINE = 15;
  VALUE_SOURCE_REMOTE = 16;
  VALUE_SOURCE_COMPUTED = 17;
  VALUE_SOURCE_INHERITED = 18;
  VALUE_SOURCE_OVERRIDE = 19;
  VALUE_SOURCE_CUSTOM = 20;
}
```

---

### value_status.proto {#value_status}

**Path**: `gcommon/v1/common/value_status.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Enums** (1): `ValueStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_status.proto
// version: 1.0.1
// guid: cd97b900-15cf-474b-a899-146f0e687253

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueStatus {
  VALUE_STATUS_UNSPECIFIED = 0;
  VALUE_STATUS_ACTIVE = 1;
  VALUE_STATUS_INACTIVE = 2;
  VALUE_STATUS_DRAFT = 3;
  VALUE_STATUS_DEPRECATED = 4;
  VALUE_STATUS_DELETED = 5;
  VALUE_STATUS_ERROR = 6;
  VALUE_STATUS_PENDING = 7;
  VALUE_STATUS_SYNCING = 8;
  VALUE_STATUS_VALIDATING = 9;
}
```

---

### value_type.proto {#value_type}

**Path**: `gcommon/v1/common/value_type.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Enums** (1): `ValueType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/value_type.proto
// version: 1.0.1
// guid: ad79b2ed-884b-4399-84c0-f29aa53ca0a3
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Value type enumeration for configuration values and other typed data.
 * Provides type safety and validation hints for stored values across
 * all GCommon modules.
 */
enum ValueType {
  // Default value indicating no value type was specified
  VALUE_TYPE_UNSPECIFIED = 0;

  // UTF-8 encoded string value
  VALUE_TYPE_STRING = 1;

  // 64-bit signed integer value
  VALUE_TYPE_INT = 2;

  // Double precision floating point value
  VALUE_TYPE_DOUBLE = 3;

  // Boolean true/false value
  VALUE_TYPE_BOOL = 4;

  // Raw binary data
  VALUE_TYPE_BYTES = 5;

  // JSON-formatted string that should be parsed as JSON
  VALUE_TYPE_JSON = 6;

  // YAML-formatted string that should be parsed as YAML
  VALUE_TYPE_YAML = 7;
}
```

---

### value_validation_result_type.proto {#value_validation_result_type}

**Path**: `gcommon/v1/common/value_validation_result_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValueValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_validation_result_type.proto
// version: 1.0.1
// guid: 6558f48c-96da-4dc8-b0f1-691f0e0e8999

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueValidationResultType {
  VALUE_VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;
  VALUE_VALIDATION_RESULT_TYPE_PASS = 1;
  VALUE_VALIDATION_RESULT_TYPE_FAIL = 2;
  VALUE_VALIDATION_RESULT_TYPE_WARNING = 3;
  VALUE_VALIDATION_RESULT_TYPE_SKIP = 4;
}
```

---

### value_validation_severity.proto {#value_validation_severity}

**Path**: `gcommon/v1/common/value_validation_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValueValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_validation_severity.proto
// version: 1.0.1
// guid: 55cd1c6a-887d-49f5-b248-9025dc9f5084

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueValidationSeverity {
  VALUE_VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALUE_VALIDATION_SEVERITY_INFO = 1;
  VALUE_VALIDATION_SEVERITY_WARNING = 2;
  VALUE_VALIDATION_SEVERITY_ERROR = 3;
  VALUE_VALIDATION_SEVERITY_CRITICAL = 4;
}
```

---

### verification_status.proto {#verification_status}

**Path**: `gcommon/v1/common/verification_status.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `VerificationStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verification_status.proto
// version: 1.0.1
// guid: 2e8605fa-61b3-4b0c-8322-8e47f1d58d0e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### verification_type.proto {#verification_type}

**Path**: `gcommon/v1/common/verification_type.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `AuthVerificationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verification_type.proto
// version: 1.0.1
// guid: 0875b6fd-5225-43a7-a52d-fa98beee769d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthVerificationType {
  VERIFICATION_TYPE_UNSPECIFIED = 0;
  VERIFICATION_TYPE_EMAIL = 1;
  VERIFICATION_TYPE_SMS = 2;
}
```

---

### version_dependency_type.proto {#version_dependency_type}

**Path**: `gcommon/v1/common/version_dependency_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `VersionDependencyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_dependency_type.proto
// version: 1.0.1
// guid: 34850372-1489-45d0-9f83-e262d595215b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionDependencyType {
  VERSION_DEPENDENCY_TYPE_UNSPECIFIED = 0;
  VERSION_DEPENDENCY_TYPE_RUNTIME = 1;
  VERSION_DEPENDENCY_TYPE_BUILD = 2;
  VERSION_DEPENDENCY_TYPE_TEST = 3;
  VERSION_DEPENDENCY_TYPE_DEV = 4;
  VERSION_DEPENDENCY_TYPE_PEER = 5;
  VERSION_DEPENDENCY_TYPE_OPTIONAL = 6;
}
```

---

### version_deployment_status.proto {#version_deployment_status}

**Path**: `gcommon/v1/common/version_deployment_status.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `VersionDeploymentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_deployment_status.proto
// version: 1.0.1
// guid: ff99e66b-873a-415d-8f2e-df2a6b1a25c2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionDeploymentStatus {
  VERSION_DEPLOYMENT_STATUS_UNSPECIFIED = 0;
  VERSION_DEPLOYMENT_STATUS_PENDING = 1;
  VERSION_DEPLOYMENT_STATUS_IN_PROGRESS = 2;
  VERSION_DEPLOYMENT_STATUS_SUCCESS = 3;
  VERSION_DEPLOYMENT_STATUS_FAILED = 4;
  VERSION_DEPLOYMENT_STATUS_ROLLED_BACK = 5;
  VERSION_DEPLOYMENT_STATUS_CANCELLED = 6;
}
```

---

### version_health_status.proto {#version_health_status}

**Path**: `gcommon/v1/common/version_health_status.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `VersionHealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_health_status.proto
// version: 1.0.1
// guid: 71f9e59c-35f1-439c-9785-8149f061e4d9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionHealthStatus {
  VERSION_HEALTH_STATUS_UNSPECIFIED = 0;
  VERSION_HEALTH_STATUS_HEALTHY = 1;
  VERSION_HEALTH_STATUS_DEGRADED = 2;
  VERSION_HEALTH_STATUS_UNHEALTHY = 3;
  VERSION_HEALTH_STATUS_UNKNOWN = 4;
}
```

---

### version_status.proto {#version_status}

**Path**: `gcommon/v1/common/version_status.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `VersionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_status.proto
// version: 1.0.1
// guid: 55704401-46f6-4b87-94a8-11020525cfe4

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionStatus {
  VERSION_STATUS_UNSPECIFIED = 0;
  VERSION_STATUS_DRAFT = 1;
  VERSION_STATUS_PENDING = 2;
  VERSION_STATUS_ACTIVE = 3;
  VERSION_STATUS_DEPRECATED = 4;
  VERSION_STATUS_ARCHIVED = 5;
  VERSION_STATUS_DELETED = 6;
  VERSION_STATUS_FAILED = 7;
  VERSION_STATUS_CANCELLED = 8;
}
```

---

### version_type.proto {#version_type}

**Path**: `gcommon/v1/common/version_type.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `VersionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_type.proto
// version: 1.0.1
// guid: 38337d79-8f7d-4d84-bc08-cf277adfd568

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionType {
  VERSION_TYPE_UNSPECIFIED = 0;
  VERSION_TYPE_MAJOR = 1;
  VERSION_TYPE_MINOR = 2;
  VERSION_TYPE_PATCH = 3;
  VERSION_TYPE_HOTFIX = 4;
  VERSION_TYPE_PRERELEASE = 5;
  VERSION_TYPE_SNAPSHOT = 6;
  VERSION_TYPE_BRANCH = 7;
  VERSION_TYPE_TAG = 8;
}
```

---

### visualization_type.proto {#visualization_type}

**Path**: `gcommon/v1/common/visualization_type.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Enums** (1): `VisualizationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/visualization_type.proto
// version: 1.0.1
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// VisualizationType represents different types of data visualizations
enum VisualizationType {
  // Unspecified visualization type
  VISUALIZATION_TYPE_UNSPECIFIED = 0;

  // Line chart
  VISUALIZATION_TYPE_LINE_CHART = 1;

  // Bar chart
  VISUALIZATION_TYPE_BAR_CHART = 2;

  // Pie chart
  VISUALIZATION_TYPE_PIE_CHART = 3;

  // Area chart
  VISUALIZATION_TYPE_AREA_CHART = 4;

  // Scatter plot
  VISUALIZATION_TYPE_SCATTER_PLOT = 5;

  // Heatmap
  VISUALIZATION_TYPE_HEATMAP = 6;

  // Histogram
  VISUALIZATION_TYPE_HISTOGRAM = 7;

  // Gauge
  VISUALIZATION_TYPE_GAUGE = 8;

  // Table
  VISUALIZATION_TYPE_TABLE = 9;

  // Single stat
  VISUALIZATION_TYPE_SINGLE_STAT = 10;

  // Graph
  VISUALIZATION_TYPE_GRAPH = 11;

  // Worldmap
  VISUALIZATION_TYPE_WORLDMAP = 12;

  // Text panel
  VISUALIZATION_TYPE_TEXT = 13;

  // Custom visualization
  VISUALIZATION_TYPE_CUSTOM = 14;
}
```

---

### web_auth_method.proto {#web_auth_method}

**Path**: `gcommon/v1/common/web_auth_method.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `WebAuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/auth_method.proto
// version: 1.0.1
// guid: f8f4a7c2-b0ea-4b6f-8c70-8bd37e0615f9
//
// AuthMethod defines supported authentication mechanisms for the web module.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Supported authentication mechanisms for HTTP requests.
enum WebAuthMethod {
  WEB_AUTH_METHOD_UNSPECIFIED = 0;
  WEB_AUTH_METHOD_NONE = 1;
  // Token-based authentication (JWT, API keys, etc.)
  WEB_AUTH_METHOD_TOKEN = 2;
  // OAuth2 with various providers
  WEB_AUTH_METHOD_OAUTH2 = 3;
}
```

---

### web_session_state.proto {#web_session_state}

**Path**: `gcommon/v1/common/web_session_state.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `WebSessionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/session_state.proto
// version: 1.0.1
// guid: a34ac56d-96ba-4c3e-b36b-a60ba1e62d86
//
// SessionState describes the lifecycle of a user session.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum WebSessionState {
  WEB_SESSION_STATE_UNSPECIFIED = 0;
  WEB_SESSION_STATE_ACTIVE = 1;
  WEB_SESSION_STATE_EXPIRED = 2;
  WEB_SESSION_STATE_REVOKED = 3;
}
```

---

### web_socket_state.proto {#web_socket_state}

**Path**: `gcommon/v1/common/web_socket_state.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `WebSocketState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/web_socket_state.proto
// version: 1.0.1
// guid: 0d71bf70-328b-459b-8bc7-674138f22f92
//
// WebSocketState tracks connection lifecycle stages.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum WebSocketState {
  WEB_SOCKET_STATE_UNSPECIFIED = 0;
  WEB_SOCKET_STATE_CONNECTING = 1;
  WEB_SOCKET_STATE_OPEN = 2;
  WEB_SOCKET_STATE_CLOSING = 3;
  WEB_SOCKET_STATE_CLOSED = 4;
}
```

---

### write_level.proto {#write_level}

**Path**: `gcommon/v1/common/write_level.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `WriteLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/write_level.proto
// version: 1.0.1
// guid: 4d949bc0-a987-4e3f-b104-24538f7ae53e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum WriteLevel {
  WRITE_LEVEL_UNSPECIFIED = 0;
  WRITE_LEVEL_ASYNC = 1; // Asynchronous writes
  WRITE_LEVEL_SYNC_ONE = 2; // Synchronous to one replica
  WRITE_LEVEL_SYNC_QUORUM = 3; // Synchronous to quorum
  WRITE_LEVEL_SYNC_ALL = 4; // Synchronous to all replicas
}
```

---

