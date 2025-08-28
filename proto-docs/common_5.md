# common_5 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 13
- **Services**: 0
- **Enums**: 37

## Files in this Module

- [routing_pattern.proto](#routing_pattern)
- [routing_strategy.proto](#routing_strategy)
- [same_site_policy.proto](#same_site_policy)
- [sample_rate.proto](#sample_rate)
- [schema_compatibility_mode.proto](#schema_compatibility_mode)
- [schema_evolution_strategy.proto](#schema_evolution_strategy)
- [schema_format.proto](#schema_format)
- [scope_type.proto](#scope_type)
- [scrape_status.proto](#scrape_status)
- [secret_audit_level.proto](#secret_audit_level)
- [secret_backup_frequency.proto](#secret_backup_frequency)
- [secret_status.proto](#secret_status)
- [secret_type.proto](#secret_type)
- [secret_validation_result_type.proto](#secret_validation_result_type)
- [secret_validation_severity.proto](#secret_validation_severity)
- [security_context.proto](#security_context)
- [security_policy.proto](#security_policy)
- [serialization_format.proto](#serialization_format)
- [server_state.proto](#server_state)
- [server_status.proto](#server_status)
- [serving_status.proto](#serving_status)
- [session.proto](#session)
- [session_info.proto](#session_info)
- [session_metadata.proto](#session_metadata)
- [session_state.proto](#session_state)
- [session_status.proto](#session_status)
- [sort_direction.proto](#sort_direction)
- [sort_field.proto](#sort_field)
- [sort_options.proto](#sort_options)
- [source_location.proto](#source_location)
- [ssl_protocol.proto](#ssl_protocol)
- [statistic_grouping.proto](#statistic_grouping)
- [statistic_type.proto](#statistic_type)
- [stats_granularity.proto](#stats_granularity)
- [storage_backend.proto](#storage_backend)
- [stream_compression.proto](#stream_compression)
- [stream_qos.proto](#stream_qos)
- [stream_restart_policy.proto](#stream_restart_policy)
- [string_array.proto](#string_array)
- [subject_type.proto](#subject_type)
- [subscription_info.proto](#subscription_info)
- [subscription_options.proto](#subscription_options)
- [subscription_preferences.proto](#subscription_preferences)
- [subscription_state.proto](#subscription_state)
- [subscription_status.proto](#subscription_status)
- [subtitle_format.proto](#subtitle_format)
- [synchronization_frequency.proto](#synchronization_frequency)
- [template.proto](#template)
- [template_format.proto](#template_format)
- [template_parameter.proto](#template_parameter)
---


## Detailed Documentation

### routing_pattern.proto {#routing_pattern}

**Path**: `gcommon/v1/common/routing_pattern.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `RoutingPattern`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_pattern.proto
// version: 1.0.1
// guid: f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Routing pattern types for key matching.
 * Specifies how routing keys are matched against patterns.
 */
enum RoutingPattern {
  // Exact string match
  ROUTING_PATTERN_UNSPECIFIED = 0;

  // Wildcard pattern (* and ?)
  ROUTING_PATTERN_WILDCARD = 1;

  // Regular expression pattern
  ROUTING_PATTERN_REGEX = 2;

  // Topic-style pattern (dot separated, # and * wildcards)
  ROUTING_PATTERN_TOPIC = 3;

  // Prefix match
  ROUTING_PATTERN_PREFIX = 4;

  // Suffix match
  ROUTING_PATTERN_SUFFIX = 5;
}
```

---

### routing_strategy.proto {#routing_strategy}

**Path**: `gcommon/v1/common/routing_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `RoutingStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_strategy.proto
// version: 1.0.1
// guid: c0da3188-9710-4555-bbda-9632f6b3f29b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Routing strategies.
 */
enum RoutingStrategy {
  // Default unspecified strategy
  ROUTING_STRATEGY_UNSPECIFIED = 0;

  // Direct routing based on destination name
  ROUTING_STRATEGY_DIRECT = 1;

  // Topic-based routing using routing key
  ROUTING_STRATEGY_TOPIC = 2;

  // Fanout routing to all bound queues
  ROUTING_STRATEGY_FANOUT = 3;

  // Header-based routing using message headers
  ROUTING_STRATEGY_HEADER = 4;

  // Content-based routing using message content
  ROUTING_STRATEGY_CONTENT = 5;

  // Hash-based routing for load distribution
  ROUTING_STRATEGY_HASH = 6;
}
```

---

### same_site_policy.proto {#same_site_policy}

**Path**: `gcommon/v1/common/same_site_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `SameSitePolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/same_site_policy.proto
// version: 1.0.1
// guid: a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SameSite cookie policy options.
 * Controls when cookies are sent with cross-site requests.
 */
enum SameSitePolicy {
  // Default SameSite policy
  SAME_SITE_POLICY_UNSPECIFIED = 0;

  // No SameSite restriction
  SAME_SITE_POLICY_NONE = 1;

  // Lax SameSite policy
  SAME_SITE_POLICY_LAX = 2;

  // Strict SameSite policy
  SAME_SITE_POLICY_STRICT = 3;
}
```

---

### sample_rate.proto {#sample_rate}

**Path**: `gcommon/v1/common/sample_rate.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Enums** (1): `SampleRate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/sample_rate.proto
// version: 1.0.1
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// SampleRate represents different sampling rates for metrics collection
enum SampleRate {
  // Unspecified sample rate
  SAMPLE_RATE_UNSPECIFIED = 0;

  // Collect every sample (100%)
  SAMPLE_RATE_FULL = 1;

  // Sample at 50% rate
  SAMPLE_RATE_HALF = 2;

  // Sample at 25% rate
  SAMPLE_RATE_QUARTER = 3;

  // Sample at 10% rate
  SAMPLE_RATE_TENTH = 4;

  // Sample at 5% rate
  SAMPLE_RATE_TWENTIETH = 5;

  // Sample at 1% rate
  SAMPLE_RATE_HUNDREDTH = 6;

  // Sample at 0.1% rate
  SAMPLE_RATE_THOUSANDTH = 7;

  // Adaptive sampling (dynamic rate)
  SAMPLE_RATE_ADAPTIVE = 8;

  // Custom sampling rate
  SAMPLE_RATE_CUSTOM = 9;
}
```

---

### schema_compatibility_mode.proto {#schema_compatibility_mode}

**Path**: `gcommon/v1/common/schema_compatibility_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Enums** (1): `SchemaCompatibilityMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_compatibility_mode.proto
// version: 1.0.1
// guid: 6c24f62f-1d37-4098-b5d4-a49e4a58d05e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Schema compatibility modes.
 */
enum SchemaCompatibilityMode {
  // Default unspecified mode
  SCHEMA_COMPATIBILITY_MODE_UNSPECIFIED = 0;

  // Strict compatibility checking
  SCHEMA_COMPATIBILITY_MODE_STRICT = 1;

  // Lenient compatibility checking
  SCHEMA_COMPATIBILITY_MODE_LENIENT = 2;

  // No compatibility checking
  SCHEMA_COMPATIBILITY_MODE_NONE = 3;
}
```

---

### schema_evolution_strategy.proto {#schema_evolution_strategy}

**Path**: `gcommon/v1/common/schema_evolution_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `SchemaEvolutionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_evolution_strategy.proto
// version: 1.0.1
// guid: ef5f0572-3b2c-44c1-8e1c-247b8fad9c9c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Schema evolution strategies.
 */
enum SchemaEvolutionStrategy {
  // Default unspecified strategy
  SCHEMA_EVOLUTION_STRATEGY_UNSPECIFIED = 0;

  // No evolution allowed
  SCHEMA_EVOLUTION_STRATEGY_NONE = 1;

  // Forward compatibility (new schema can read old data)
  SCHEMA_EVOLUTION_STRATEGY_FORWARD = 2;

  // Backward compatibility (old schema can read new data)
  SCHEMA_EVOLUTION_STRATEGY_BACKWARD = 3;

  // Full compatibility (bidirectional)
  SCHEMA_EVOLUTION_STRATEGY_FULL = 4;

  // No compatibility checks
  SCHEMA_EVOLUTION_STRATEGY_NONE_CHECK = 5;
}
```

---

### schema_format.proto {#schema_format}

**Path**: `gcommon/v1/common/schema_format.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `SchemaFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_format.proto
// version: 1.0.1
// guid: 8dbf53aa-e92d-4de4-84a8-ec3fb37ce521

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Schema format types.
 */
enum SchemaFormat {
  // Default unspecified format
  SCHEMA_FORMAT_UNSPECIFIED = 0;

  // JSON Schema format
  SCHEMA_FORMAT_JSON_SCHEMA = 1;

  // Apache Avro schema
  SCHEMA_FORMAT_AVRO = 2;

  // Protocol Buffers schema
  SCHEMA_FORMAT_PROTOBUF = 3;

  // XML Schema (XSD)
  SCHEMA_FORMAT_XML_SCHEMA = 4;

  // Custom schema format
  SCHEMA_FORMAT_CUSTOM = 5;
}
```

---

### scope_type.proto {#scope_type}

**Path**: `gcommon/v1/common/scope_type.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `ScopeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/scope_type.proto
// version: 1.0.1
// guid: f8bce9e5-500a-40e6-aca9-4ce5c58d2d04
// file: proto/gcommon/v1/common/scope_type.proto
//
// Enum definitions for auth module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### scrape_status.proto {#scrape_status}

**Path**: `gcommon/v1/common/scrape_status.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Enums** (1): `ScrapeStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/types/scrape_status.proto
// version: 1.0.1
// guid: 8c8f682b-16a6-490f-84ce-c96e566d5fba
// file: proto/gcommon/v1/metrics/scrape_status.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ScrapeStatus defines the status of metric scraping operations.
 * Used to track the health and success of metric collection from targets.
 */
enum ScrapeStatus {
  // Unspecified scrape status (default)
  SCRAPE_STATUS_UNSPECIFIED = 0;

  // Scrape completed successfully
  SCRAPE_STATUS_SUCCESS = 1;

  // Scrape failed due to network/connection issues
  SCRAPE_STATUS_NETWORK_ERROR = 2;

  // Scrape failed due to authentication/authorization issues
  SCRAPE_STATUS_AUTH_ERROR = 3;

  // Scrape failed due to timeout
  SCRAPE_STATUS_TIMEOUT = 4;

  // Scrape failed due to invalid/malformed response
  SCRAPE_STATUS_PARSE_ERROR = 5;

  // Target is unreachable/down
  SCRAPE_STATUS_TARGET_DOWN = 6;

  // Target returned HTTP error status
  SCRAPE_STATUS_HTTP_ERROR = 7;

  // Scrape was cancelled/aborted
  SCRAPE_STATUS_CANCELLED = 8;

  // Rate limited by target
  SCRAPE_STATUS_RATE_LIMITED = 9;

  // Target configuration is invalid
  SCRAPE_STATUS_CONFIG_ERROR = 10;

  // Scrape is currently in progress
  SCRAPE_STATUS_IN_PROGRESS = 11;
}
```

---

### secret_audit_level.proto {#secret_audit_level}

**Path**: `gcommon/v1/common/secret_audit_level.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `SecretAuditLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_audit_level.proto
// version: 1.0.1
// guid: bc307b1b-aa5d-4b26-8724-6f1e537132c5

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretAuditLevel {
  SECRET_AUDIT_LEVEL_UNSPECIFIED = 0;
  SECRET_AUDIT_LEVEL_NONE = 1;
  SECRET_AUDIT_LEVEL_MINIMAL = 2;
  SECRET_AUDIT_LEVEL_STANDARD = 3;
  SECRET_AUDIT_LEVEL_DETAILED = 4;
  SECRET_AUDIT_LEVEL_VERBOSE = 5;
}
```

---

### secret_backup_frequency.proto {#secret_backup_frequency}

**Path**: `gcommon/v1/common/secret_backup_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `SecretBackupFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_backup_frequency.proto
// version: 1.0.1
// guid: d2ec4ba6-932e-4349-89f4-aa4af899c73f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretBackupFrequency {
  SECRET_BACKUP_FREQUENCY_UNSPECIFIED = 0;
  SECRET_BACKUP_FREQUENCY_MANUAL = 1;
  SECRET_BACKUP_FREQUENCY_HOURLY = 2;
  SECRET_BACKUP_FREQUENCY_DAILY = 3;
  SECRET_BACKUP_FREQUENCY_WEEKLY = 4;
  SECRET_BACKUP_FREQUENCY_MONTHLY = 5;
  SECRET_BACKUP_FREQUENCY_ON_CHANGE = 6;
}
```

---

### secret_status.proto {#secret_status}

**Path**: `gcommon/v1/common/secret_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `SecretStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_status.proto
// version: 1.0.1
// guid: 7fb6a7a0-ecc1-4dc0-b2a0-49c3e3fe88b9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretStatus {
  SECRET_STATUS_UNSPECIFIED = 0;
  SECRET_STATUS_ACTIVE = 1;
  SECRET_STATUS_INACTIVE = 2;
  SECRET_STATUS_EXPIRED = 3;
  SECRET_STATUS_ROTATED = 4;
  SECRET_STATUS_COMPROMISED = 5;
  SECRET_STATUS_DELETED = 6;
  SECRET_STATUS_ERROR = 7;
}
```

---

### secret_type.proto {#secret_type}

**Path**: `gcommon/v1/common/secret_type.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `SecretType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_type.proto
// version: 1.0.1
// guid: efadf8e9-2dc3-4ccc-8c9a-3a7f0a1c0895

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretType {
  SECRET_TYPE_UNSPECIFIED = 0;
  SECRET_TYPE_PASSWORD = 1;
  SECRET_TYPE_API_KEY = 2;
  SECRET_TYPE_TOKEN = 3;
  SECRET_TYPE_CERTIFICATE = 4;
  SECRET_TYPE_PRIVATE_KEY = 5;
  SECRET_TYPE_PUBLIC_KEY = 6;
  SECRET_TYPE_OAUTH_CLIENT_SECRET = 7;
  SECRET_TYPE_DATABASE_PASSWORD = 8;
  SECRET_TYPE_CONNECTION_STRING = 9;
  SECRET_TYPE_ENCRYPTION_KEY = 10;
  SECRET_TYPE_SIGNING_KEY = 11;
  SECRET_TYPE_SSH_KEY = 12;
  SECRET_TYPE_TLS_CERTIFICATE = 13;
  SECRET_TYPE_JWT_SECRET = 14;
  SECRET_TYPE_WEBHOOK_SECRET = 15;
  SECRET_TYPE_CUSTOM = 16;
}
```

---

### secret_validation_result_type.proto {#secret_validation_result_type}

**Path**: `gcommon/v1/common/secret_validation_result_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `SecretValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_validation_result_type.proto
// version: 1.0.1
// guid: b6bb65eb-d0bd-40b2-ad57-22253970cb05

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretValidationResultType {
  SECRET_VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;
  SECRET_VALIDATION_RESULT_TYPE_PASS = 1;
  SECRET_VALIDATION_RESULT_TYPE_FAIL = 2;
  SECRET_VALIDATION_RESULT_TYPE_WARNING = 3;
  SECRET_VALIDATION_RESULT_TYPE_SKIP = 4;
}
```

---

### secret_validation_severity.proto {#secret_validation_severity}

**Path**: `gcommon/v1/common/secret_validation_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `SecretValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_validation_severity.proto
// version: 1.0.1
// guid: 8dc44dbd-dedb-4dfd-b5f9-ad2256d6a6c6

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretValidationSeverity {
  SECRET_VALIDATION_SEVERITY_UNSPECIFIED = 0;
  SECRET_VALIDATION_SEVERITY_INFO = 1;
  SECRET_VALIDATION_SEVERITY_WARNING = 2;
  SECRET_VALIDATION_SEVERITY_ERROR = 3;
  SECRET_VALIDATION_SEVERITY_CRITICAL = 4;
}
```

---

### security_context.proto {#security_context}

**Path**: `gcommon/v1/common/security_context.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `SecurityContext`

**Imports** (3):

- `gcommon/v1/common/auth_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/security_context.proto
// version: 1.0.0
// guid: 80402f15-2486-4290-92b0-77a7f38f1820

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/auth_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SecurityContext {
  // User ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session ID
  string session_id = 2;

  // User roles
  repeated string roles = 3;

  // User permissions
  repeated string permissions = 4;

  // Authentication method used
  gcommon.v1.common.AuthAuthMethod auth_method = 5;

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
```

---

### security_policy.proto {#security_policy}

**Path**: `gcommon/v1/common/security_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `SecurityPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/security_policy.proto
// version: 1.0.0
// guid: 1d12dbb5-c796-48b9-beab-f89a58a4d115

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SecurityPolicy defines account and token security requirements.
 */
message SecurityPolicy {
  // Minimum password length requirement
  uint32 min_password_length = 1 [(buf.validate.field).uint32.gte = 0];

  // Password expiration duration
  google.protobuf.Duration password_ttl = 2;

  // Maximum failed login attempts before lockout
  uint32 max_failed_attempts = 3 [(buf.validate.field).uint32.gte = 0];
}
```

---

### serialization_format.proto {#serialization_format}

**Path**: `gcommon/v1/common/serialization_format.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Enums** (1): `SerializationFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/serialization_format.proto
// file: proto/gcommon/v1/queue/serialization_format.proto
// version: 1.0.1
// guid: 7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Supported message serialization formats for queue messages.
 */
enum SerializationFormat {
  // Default unspecified format
  SERIALIZATION_FORMAT_UNSPECIFIED = 0;

  // Protocol Buffers binary format
  SERIALIZATION_FORMAT_PROTOBUF = 1;

  // JSON text format
  SERIALIZATION_FORMAT_JSON = 2;

  // MessagePack binary format
  SERIALIZATION_FORMAT_MSGPACK = 3;

  // Apache Avro binary format
  SERIALIZATION_FORMAT_AVRO = 4;

  // Raw binary data (no specific format)
  SERIALIZATION_FORMAT_BINARY = 5;

  // Plain text format
  SERIALIZATION_FORMAT_TEXT = 6;

  // XML format
  SERIALIZATION_FORMAT_XML = 7;
}
```

---

### server_state.proto {#server_state}

**Path**: `gcommon/v1/common/server_state.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ServerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_state.proto
// version: 1.0.1
// guid: edc8f45d-5db0-4b28-b04a-c6eedc98b19b
//
// ServerState represents lifecycle states of the server.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ServerState {
  SERVER_STATE_UNSPECIFIED = 0;
  SERVER_STATE_STARTING = 1;
  SERVER_STATE_RUNNING = 2;
  SERVER_STATE_STOPPING = 3;
  SERVER_STATE_STOPPED = 4;
}
```

---

### server_status.proto {#server_status}

**Path**: `gcommon/v1/common/server_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `ServerStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_status.proto
// version: 1.0.2
// guid: 1846bf32-3652-4e52-a6fc-333db4886d5c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ServerStatus enumeration describing server lifecycle states.
enum ServerStatus {
  SERVER_STATUS_UNSPECIFIED = 0;
  SERVER_STATUS_CREATED = 1;
  SERVER_STATUS_STARTING = 2;
  SERVER_STATUS_RUNNING = 3;
  SERVER_STATUS_STOPPING = 4;
  SERVER_STATUS_STOPPED = 5;
  SERVER_STATUS_ERROR = 6;
}
```

---

### serving_status.proto {#serving_status}

**Path**: `gcommon/v1/common/serving_status.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Enums** (1): `ServingStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/serving_status.proto
// version: 1.0.1
// guid: 61568d14-42ce-4cc7-b55e-a2fedc98db5f
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ServingStatus indicates the current serving status of a service
 */
enum ServingStatus {
  // Unknown status
  SERVING_STATUS_UNSPECIFIED = 0;
  // Service is serving
  SERVING_STATUS_SERVING = 1;
  // Service is not serving
  SERVING_STATUS_NOT_SERVING = 2;
  // Service is serving but degraded
  SERVING_STATUS_SERVING_DEGRADED = 3;
}
```

---

### session.proto {#session}

**Path**: `gcommon/v1/common/session.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Messages** (1): `Session`

**Imports** (5):

- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/session_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session.proto
// version: 1.0.0
// guid: 9f1dffb9-b42d-48ad-a0df-25008ed44303
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/session_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Session information representing an authenticated user session.
 * Contains session lifecycle data, client information, and metadata
 * for session management and security tracking.
 */
message Session {
  // Unique session identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User ID associated with this session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 3 [lazy = true, (buf.validate.field).required = true];

  // Last activity timestamp (updated on each request)
  google.protobuf.Timestamp last_activity_at = 4 [lazy = true];

  // Session expiration timestamp
  google.protobuf.Timestamp expires_at = 5 [lazy = true];

  // Client information from session creation
  ClientInfo client_info = 6 [lazy = true];

  // Current session status
  gcommon.v1.common.SessionStatus status = 7;

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

**Path**: `gcommon/v1/common/session_info.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Messages** (1): `SessionInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_info.proto
// version: 1.0.0
// guid: 805af1d3-ee56-4be2-9807-baeedd9fc6d3
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Session information for lightweight session tracking.
 * Contains essential session data without full session details.
 * Used in responses where full session data is not needed.
 */
message SessionInfo {
  // Session identifier
  string session_id = 1;

  // User ID associated with session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session creation time
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

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

**Path**: `gcommon/v1/common/session_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `SessionMetadata`

**Imports** (5):

- `gcommon/v1/common/device_info.proto`
- `gcommon/v1/common/location_info.proto`
- `gcommon/v1/common/session_state.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_metadata.proto
// version: 1.0.0
// guid: 01cd27dc-f07e-4fe5-805f-ff4fc49ef91b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/device_info.proto";
import "gcommon/v1/common/location_info.proto";
import "gcommon/v1/common/session_state.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SessionMetadata {
  // Session ID
  string session_id = 1;

  // User ID
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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
  gcommon.v1.common.DeviceInfo device_info = 8;

  // Location information
  gcommon.v1.common.LocationInfo location_info = 9;

  // Session state

  gcommon.v1.common.SessionState state = 10;
}
```

---

### session_state.proto {#session_state}

**Path**: `gcommon/v1/common/session_state.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `SessionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_state.proto
// version: 1.0.1
// guid: 1a1dfd90-4426-4329-a9ab-e7c705fb4f74

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum SessionState {
  COMMON_SESSION_STATE_UNSPECIFIED = 0;
  COMMON_SESSION_STATE_ACTIVE = 1;
  COMMON_SESSION_STATE_EXPIRED = 2;
}
```

---

### session_status.proto {#session_status}

**Path**: `gcommon/v1/common/session_status.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `SessionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_status.proto
// version: 1.0.1
// guid: df65ccac-c72e-48cf-ba09-e50b76276d9e
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### sort_direction.proto {#sort_direction}

**Path**: `gcommon/v1/common/sort_direction.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `SortDirection`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/sort_direction.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Sort direction enumeration.
 * Defines ascending or descending order for sorting operations.
 */
enum SortDirection {
  // Unspecified sort direction
  SORT_DIRECTION_UNSPECIFIED = 0;

  // Ascending order (A-Z, 0-9, oldest-newest)
  SORT_DIRECTION_ASC = 1;

  // Descending order (Z-A, 9-0, newest-oldest)
  SORT_DIRECTION_DESC = 2;
}
```

---

### sort_field.proto {#sort_field}

**Path**: `gcommon/v1/common/sort_field.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `SortField`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/sort_field.proto
// version: 1.0.1
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SortField defines fields that can be used for sorting providers.
 * Specifies available fields for provider list sorting.
 */
enum SortField {
  // Unspecified sort field
  SORT_FIELD_UNSPECIFIED = 0;

  // Sort by provider name
  SORT_FIELD_NAME = 1;

  // Sort by provider type
  SORT_FIELD_TYPE = 2;

  // Sort by creation timestamp
  SORT_FIELD_CREATED_AT = 3;

  // Sort by provider state
  SORT_FIELD_STATE = 4;

  // Sort by health status
  SORT_FIELD_HEALTH = 5;
}
```

---

### sort_options.proto {#sort_options}

**Path**: `gcommon/v1/common/sort_options.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `SortOptions`

**Imports** (3):

- `gcommon/v1/common/sort_direction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/sort_options.proto
// version: 1.1.0
// guid: 34507f56-8bd2-4dd8-af7e-c9045ddbf029

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/sort_direction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Sort options for configuring list sorting.
 * Defines field and direction for sorting operations.
 */
message SortOptions {
  // Field to sort by
  string sort_field = 1 [(buf.validate.field).string.min_len = 1];

  // Sort direction
  gcommon.v1.common.SortDirection direction = 2;
}
```

---

### source_location.proto {#source_location}

**Path**: `gcommon/v1/common/source_location.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `SourceLocation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/source_location.proto
// version: 1.0.0
// guid: b529bc13-5c0e-4b3e-9d64-5025a5889fa2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// SourceLocation describes the origin of a log entry
message SourceLocation {
  // File name where the log occurred
  string file = 1 [(buf.validate.field).string.min_len = 1];

  // Line number in the source file
  int32 line = 2 [(buf.validate.field).int32.gte = 0];

  // Function name
  string function = 3 [(buf.validate.field).string.min_len = 1];

  // Package or module name
  string package = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### ssl_protocol.proto {#ssl_protocol}

**Path**: `gcommon/v1/common/ssl_protocol.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `SSLProtocol`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/ssl_protocol.proto
// version: 1.0.1
// guid: 2f6af5d4-4f52-42cd-9ae8-9c6506e0da5e
//
// SSLProtocol lists supported TLS protocol versions.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SSLProtocol {
  SSL_PROTOCOL_UNSPECIFIED = 0;
  SSL_PROTOCOL_TLS1_0 = 1;
  SSL_PROTOCOL_TLS1_1 = 2;
  SSL_PROTOCOL_TLS1_2 = 3;
  SSL_PROTOCOL_TLS1_3 = 4;
}
```

---

### statistic_grouping.proto {#statistic_grouping}

**Path**: `gcommon/v1/common/statistic_grouping.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `StatisticGrouping`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/statistic_grouping.proto
// version: 1.0.1
// guid: a8a72b1a-cc3a-46d1-a1ab-87af3535faac

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum StatisticGrouping {
  STATISTIC_GROUPING_UNSPECIFIED = 0;
  STATISTIC_GROUPING_NONE = 1; // No grouping, flat statistics
  STATISTIC_GROUPING_BY_QUEUE = 2; // Group by queue name
  STATISTIC_GROUPING_BY_CONSUMER = 3; // Group by consumer
  STATISTIC_GROUPING_BY_TIME_PERIOD = 4; // Group by time periods
  STATISTIC_GROUPING_BY_MESSAGE_TYPE = 5; // Group by message type
}
```

---

### statistic_type.proto {#statistic_type}

**Path**: `gcommon/v1/common/statistic_type.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `StatisticType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/statistic_type.proto
// version: 1.0.1
// guid: cb4f227d-f3e9-4698-aa3e-776544976e01

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum StatisticType {
  STATISTIC_TYPE_UNSPECIFIED = 0;
  STATISTIC_TYPE_MESSAGE_COUNT = 1;
  STATISTIC_TYPE_THROUGHPUT = 2;
  STATISTIC_TYPE_LATENCY = 3;
  STATISTIC_TYPE_ERROR_RATE = 4;
  STATISTIC_TYPE_QUEUE_DEPTH = 5;
  STATISTIC_TYPE_PROCESSING_TIME = 6;
  STATISTIC_TYPE_CONSUMER_COUNT = 7;
  STATISTIC_TYPE_MESSAGE_SIZE = 8;
  STATISTIC_TYPE_AGE_DISTRIBUTION = 9;
  STATISTIC_TYPE_SUCCESS_RATE = 10;
}
```

---

### stats_granularity.proto {#stats_granularity}

**Path**: `gcommon/v1/common/stats_granularity.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `StatsGranularity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stats_granularity.proto
// version: 1.0.1
// guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StatsGranularity represents the granularity for statistics.
 * Specifies the time interval granularity for statistical data collection and aggregation.
 */
enum StatsGranularity {
  // Default unspecified granularity
  STATS_GRANULARITY_UNSPECIFIED = 0;

  // Minute-level granularity
  STATS_GRANULARITY_MINUTE = 1;

  // Hour-level granularity
  STATS_GRANULARITY_HOUR = 2;

  // Day-level granularity
  STATS_GRANULARITY_DAY = 3;

  // Week-level granularity
  STATS_GRANULARITY_WEEK = 4;
}
```

---

### storage_backend.proto {#storage_backend}

**Path**: `gcommon/v1/common/storage_backend.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Enums** (1): `StorageBackend`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/storage_backend.proto
// version: 1.0.1
// guid: 5ee72796-5fec-4f25-8894-b75050c9f18e
// file: proto/gcommon/v1/metrics/v1/storage_backend.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StorageBackend defines the types of storage systems available for metrics.
 * Used to specify where metrics should be stored and retrieved from.
 */
enum StorageBackend {
  // Unspecified storage backend (default)
  STORAGE_BACKEND_UNSPECIFIED = 0;

  // In-memory storage (non-persistent, for testing/development)
  STORAGE_BACKEND_MEMORY = 1;

  // Prometheus time-series database
  STORAGE_BACKEND_PROMETHEUS = 2;

  // InfluxDB time-series database
  STORAGE_BACKEND_INFLUXDB = 3;

  // TimescaleDB (PostgreSQL extension for time-series)
  STORAGE_BACKEND_TIMESCALEDB = 4;

  // OpenTelemetry backend (various implementations)
  STORAGE_BACKEND_OPENTELEMETRY = 5;

  // Graphite time-series database
  STORAGE_BACKEND_GRAPHITE = 6;

  // ElasticSearch for metrics storage
  STORAGE_BACKEND_ELASTICSEARCH = 7;

  // CloudWatch (AWS managed metrics)
  STORAGE_BACKEND_CLOUDWATCH = 8;

  // Google Cloud Monitoring
  STORAGE_BACKEND_GCP_MONITORING = 9;

  // Azure Monitor
  STORAGE_BACKEND_AZURE_MONITOR = 10;

  // VictoriaMetrics time-series database
  STORAGE_BACKEND_VICTORIAMETRICS = 11;
}
```

---

### stream_compression.proto {#stream_compression}

**Path**: `gcommon/v1/common/stream_compression.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `StreamCompression`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_compression.proto
// version: 1.0.1
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StreamCompression defines compression options for streaming.
 * Specifies how metrics data should be compressed during streaming.
 */
enum StreamCompression {
  // Unspecified compression
  STREAM_COMPRESSION_UNSPECIFIED = 0;

  // No compression
  STREAM_COMPRESSION_NONE = 1;

  // GZIP compression
  STREAM_COMPRESSION_GZIP = 2;

  // Snappy compression
  STREAM_COMPRESSION_SNAPPY = 3;

  // LZ4 compression
  STREAM_COMPRESSION_LZ4 = 4;
}
```

---

### stream_qos.proto {#stream_qos}

**Path**: `gcommon/v1/common/stream_qos.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `StreamQOS`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_qos.proto
// version: 1.0.1
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StreamQOS defines quality of service levels for streaming.
 * Specifies delivery guarantees for streaming metrics.
 */
enum StreamQOS {
  // Unspecified QOS level
  STREAM_QOS_UNSPECIFIED = 0;

  // Best effort delivery (fire and forget)
  STREAM_QOS_BEST_EFFORT = 1;

  // At least once delivery guarantee
  STREAM_QOS_AT_LEAST_ONCE = 2;

  // Exactly once delivery guarantee
  STREAM_QOS_EXACTLY_ONCE = 3;
}
```

---

### stream_restart_policy.proto {#stream_restart_policy}

**Path**: `gcommon/v1/common/stream_restart_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `StreamRestartPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/stream_restart_policy.proto
// file: proto/gcommon/v1/queue/stream_restart_policy.proto
// version: 1.0.1
// guid: 6a5b4c3d-2e1f-0a9b-8c7d-6e5f4a3b2c1d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Stream restart behavior on failures.
 */
enum StreamRestartPolicy {
  // Default unspecified policy
  STREAM_RESTART_POLICY_UNSPECIFIED = 0;

  // Never restart streams automatically
  STREAM_RESTART_POLICY_NEVER = 1;

  // Restart immediately on failure
  STREAM_RESTART_POLICY_IMMEDIATE = 2;

  // Restart with exponential backoff
  STREAM_RESTART_POLICY_EXPONENTIAL_BACKOFF = 3;

  // Restart with fixed delay
  STREAM_RESTART_POLICY_FIXED_DELAY = 4;
}
```

---

### string_array.proto {#string_array}

**Path**: `gcommon/v1/common/string_array.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `StringArray`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/string_array.proto
// version: 1.0.0
// guid: 5ff69d27-5bdf-4475-a029-e9f948b8a078
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * String array wrapper for oneof usage in filter values and other contexts.
 * Required because oneof fields cannot directly contain repeated types,
 * so arrays must be wrapped in a message.
 */
message StringArray {
  // Array of string values
  repeated string values = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### subject_type.proto {#subject_type}

**Path**: `gcommon/v1/common/subject_type.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `AuthSubjectType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subject_type.proto
// version: 1.0.1
// guid: d89bcd75-cade-444b-a4de-35078c41a269

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthSubjectType {
  SUBJECT_TYPE_UNSPECIFIED = 0;
  SUBJECT_TYPE_USER = 1;
  SUBJECT_TYPE_ROLE = 2;
}
```

---

### subscription_info.proto {#subscription_info}

**Path**: `gcommon/v1/common/subscription_info.proto` **Package**: `gcommon.v1.common` **Lines**: 46

**Messages** (1): `CommonSubscriptionInfo`

**Imports** (7):

- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/filter_options.proto`
- `gcommon/v1/common/subscription_options.proto`
- `gcommon/v1/common/subscription_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_info.proto
// version: 1.0.0
// guid: 890b3e39-196c-4fe4-8153-4f73bdf677e6
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/filter_options.proto";
import "gcommon/v1/common/subscription_options.proto";
import "gcommon/v1/common/subscription_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Subscription information for streaming and event-driven operations.
 * Manages long-lived subscriptions with filtering, time ranges,
 * and client-specific configuration for real-time data streaming.
 */
message CommonSubscriptionInfo {
  // Unique identifier for this subscription
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Filter criteria for subscription events
  FilterOptions filter = 2;

  // When the subscription started
  google.protobuf.Timestamp start_time = 3;

  // Optional end time for the subscription (null for indefinite)
  google.protobuf.Timestamp end_time = 4;

  // Information about the subscribing client
  ClientInfo subscriber = 5;

  // Subscription configuration options
  SubscriptionOptions options = 6;

  // Current status of the subscription
  SubscriptionStatus status = 7;
}
```

---

### subscription_options.proto {#subscription_options}

**Path**: `gcommon/v1/common/subscription_options.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `SubscriptionOptions`

**Imports** (4):

- `gcommon/v1/common/ack_mode.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_options.proto
// version: 1.0.0
// guid: 8c54ce21-f38c-48cb-8631-3f92c91cbd67
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/ack_mode.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Subscription options for configuring streaming behavior.
 * Controls historical data inclusion, batching, acknowledgment,
 * and keep-alive settings for optimal streaming performance.
 */
message SubscriptionOptions {
  // Whether to include historical data in the subscription
  bool include_history = 1;

  // Maximum number of events to batch together
  int32 max_batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Acknowledgment mode for message delivery
  gcommon.v1.common.AckMode ack_mode = 3;

  // Keep-alive interval to maintain connection
  google.protobuf.Duration keep_alive = 4;
}
```

---

### subscription_preferences.proto {#subscription_preferences}

**Path**: `gcommon/v1/common/subscription_preferences.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `SubscriptionPreferences`

**Imports** (3):

- `gcommon/v1/common/delivery_channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_preferences.proto
// version: 1.2.0
// guid: e1f2g3h4-i5j6-7890-k1l2-m3n4o5p6q7r8

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * User subscription preferences for event notifications.
 */
message SubscriptionPreferences {
  // User or entity identifier
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Enabled delivery channels
  repeated DeliveryChannelType channels = 2;

  // Subscribed event types
  repeated string events = 3;

  // Additional arbitrary preferences
  map<string, string> metadata = 4 [lazy = true];
}
```

---

### subscription_state.proto {#subscription_state}

**Path**: `gcommon/v1/common/subscription_state.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `SubscriptionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_state.proto
// version: 1.0.1
// guid: ddd7bd85-a329-4347-be1d-18983916cd3e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// SubscriptionState describes the lifecycle state of a subscription.
enum SubscriptionState {
  // Default state. Server decides behavior.
  SUBSCRIPTION_STATE_UNSPECIFIED = 0;
  // Actively receiving messages.
  SUBSCRIPTION_STATE_ACTIVE = 1;
  // Temporarily paused from delivering messages.
  SUBSCRIPTION_STATE_PAUSED = 2;
  // Permanently closed and cannot be resumed.
  SUBSCRIPTION_STATE_CLOSED = 3;
}
```

---

### subscription_status.proto {#subscription_status}

**Path**: `gcommon/v1/common/subscription_status.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `SubscriptionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_status.proto
// version: 1.0.1
// guid: 2b701f36-27a4-4a02-a1a8-d30ef84d277c
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Subscription status enumeration for streaming operations.
 * Provides consistent status tracking for event subscriptions, data streams,
 * and real-time updates across all GCommon modules.
 */
enum SubscriptionStatus {
  // Default value indicating no subscription status was specified
  SUBSCRIPTION_STATUS_UNSPECIFIED = 0;

  // Subscription is active and receiving events
  SUBSCRIPTION_STATUS_ACTIVE = 1;

  // Subscription is temporarily paused
  SUBSCRIPTION_STATUS_PAUSED = 2;

  // Subscription has been cancelled by client or system
  SUBSCRIPTION_STATUS_CANCELLED = 3;

  // Subscription is in an error state
  SUBSCRIPTION_STATUS_ERROR = 4;
}
```

---

### subtitle_format.proto {#subtitle_format}

**Path**: `gcommon/v1/common/subtitle_format.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `SubtitleFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/subtitle_format.proto
// version: 1.0.1
// guid: f012345-6789-abcd-d6e7-f8a9b0c1d2e3

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Supported subtitle formats.
enum SubtitleFormat {
  SUBTITLE_FORMAT_UNSPECIFIED = 0;
  SUBTITLE_FORMAT_SRT = 1; // SubRip
  SUBTITLE_FORMAT_VTT = 2; // WebVTT
  SUBTITLE_FORMAT_ASS = 3; // Advanced SubStation Alpha
  SUBTITLE_FORMAT_SSA = 4; // SubStation Alpha
  SUBTITLE_FORMAT_TTML = 5; // Timed Text Markup Language
  SUBTITLE_FORMAT_SCC = 6; // Scenarist Closed Caption
  SUBTITLE_FORMAT_SBV = 7; // YouTube subtitle format
}
```

---

### synchronization_frequency.proto {#synchronization_frequency}

**Path**: `gcommon/v1/common/synchronization_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `SynchronizationFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/synchronization_frequency.proto
// version: 1.0.1
// guid: 939438cc-2704-4ba7-ab8a-8ed45e882d94

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SynchronizationFrequency {
  SYNCHRONIZATION_FREQUENCY_UNSPECIFIED = 0;
  SYNCHRONIZATION_FREQUENCY_REAL_TIME = 1;
  SYNCHRONIZATION_FREQUENCY_HOURLY = 2;
  SYNCHRONIZATION_FREQUENCY_DAILY = 3;
  SYNCHRONIZATION_FREQUENCY_WEEKLY = 4;
  SYNCHRONIZATION_FREQUENCY_ON_CHANGE = 5;
}
```

---

### template.proto {#template}

**Path**: `gcommon/v1/common/template.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `Template`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/template.proto
// version: 1.0.0
// guid: b40be0b3-2832-4999-be82-78423c52b4d3
// file: proto/gcommon/v1/common/template.proto
//
// Notification template definition for reusable messages.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Template for rendering notification content.
 */
message Template {
  // Template identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human readable name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Template body using placeholders
  string body = 3;

  // Time the template was created
  google.protobuf.Timestamp created_at = 4 [lazy = true, (buf.validate.field).required = true];

  // Time the template was last updated
  google.protobuf.Timestamp updated_at = 5 [lazy = true];
}
```

---

### template_format.proto {#template_format}

**Path**: `gcommon/v1/common/template_format.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `TemplateFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_format.proto
// version: 1.0.1
// guid: 5633815c-6ddb-47f1-b36e-a761ce96bd90

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TemplateFormat {
  TEMPLATE_FORMAT_UNSPECIFIED = 0;
  TEMPLATE_FORMAT_JSON = 1;
  TEMPLATE_FORMAT_YAML = 2;
  TEMPLATE_FORMAT_TOML = 3;
  TEMPLATE_FORMAT_XML = 4;
  TEMPLATE_FORMAT_PROPERTIES = 5;
  TEMPLATE_FORMAT_INI = 6;
  TEMPLATE_FORMAT_CUSTOM = 7;
}
```

---

### template_parameter.proto {#template_parameter}

**Path**: `gcommon/v1/common/template_parameter.proto` **Package**: `gcommon.v1.common` **Lines**: 68

**Messages** (1): `TemplateParameter`

**Imports** (4):

- `gcommon/v1/common/parameter_constraints.proto`
- `gcommon/v1/common/parameter_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/template_parameter.proto
// version: 1.1.0
// guid: 800be7b5-ca05-4137-a8d2-7d1a3fe5cc97

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/parameter_constraints.proto";
import "gcommon/v1/common/parameter_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TemplateParameter {
  // Parameter name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Parameter description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Parameter type
  gcommon.v1.common.ParameterType type = 3;

  // Whether parameter is required
  bool required = 4;

  // Default value
  string default_value = 5;

  // Allowed values (for enum types)
  repeated string allowed_values = 6;

  // Parameter constraints
  gcommon.v1.common.ParameterConstraints constraints = 7;

  // Parameter group
  string group = 8;

  // Display order
  int32 order = 9;

  // Whether parameter is sensitive
  bool sensitive = 10;

  // Parameter validation pattern
  string validation_pattern = 11;

  // Parameter examples
  repeated string examples = 12;

  // Parameter documentation
  string documentation = 13;

  // Parameter display name
  string display_name = 14 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Parameter placeholder text
  string placeholder = 15;
}
```

---

