# common_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 28
- **Messages**: 26
- **Services**: 0
- **Enums**: 4

## Files in this Module

- [appender_config.proto](#appender_config)
- [auth_config.proto](#auth_config)
- [circuit_breaker_config.proto](#circuit_breaker_config)
- [config_alert_severity.proto](#config_alert_severity)
- [config_change_type.proto](#config_change_type)
- [config_config_change_type.proto](#config_config_change_type)
- [config_data_type.proto](#config_data_type)
- [config_retry_settings.proto](#config_retry_settings)
- [config_value.proto](#config_value)
- [configure_alerting_request.proto](#configure_alerting_request)
- [configure_alerting_response.proto](#configure_alerting_response)
- [configure_logger_request.proto](#configure_logger_request)
- [configure_logger_response.proto](#configure_logger_response)
- [formatter_config.proto](#formatter_config)
- [get_auth_config_request.proto](#get_auth_config_request)
- [health_config.proto](#health_config)
- [jwt_config.proto](#jwt_config)
- [ldap_config.proto](#ldap_config)
- [logger_config.proto](#logger_config)
- [metrics_api_key_config.proto](#metrics_api_key_config)
- [metrics_config_change.proto](#metrics_config_change)
- [metrics_retention_policy_config.proto](#metrics_retention_policy_config)
- [mfa_config.proto](#mfa_config)
- [o_auth2_config.proto](#o_auth2_config)
- [output_config.proto](#output_config)
- [rate_limit_config.proto](#rate_limit_config)
- [saml_config.proto](#saml_config)
- [session_config.proto](#session_config)
---


## Detailed Documentation

### appender_config.proto {#appender_config}

**Path**: `gcommon/v1/common/appender_config.proto` **Package**: `gcommon.v1.common` **Lines**: 53

**Messages** (3): `AppenderConfig`, `OutputConfig`, `LogFormatterConfig`

**Imports** (4):

- `gcommon/v1/common/appender_type.proto`
- `gcommon/v1/common/formatter_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/appender_config.proto
// version: 1.0.0
// guid: 1423b6a1-54da-4a63-8427-4225cd81621a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/appender_type.proto";
import "gcommon/v1/common/formatter_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message AppenderConfig {
  // Unique appender name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Appender backend type
  AppenderType type = 2;

  // Output destination details
  OutputConfig output = 3;

  // Formatting configuration
  LogFormatterConfig formatter = 4;

  // Arbitrary appender properties
  map<string, string> properties = 5;

  // OutputConfig defines the destination for log entries
  message OutputConfig {
    // Output target (file path, network address, etc.)
    string target = 1;

    // Additional output options
    map<string, string> options = 2;
  }

  // FormatterConfig defines how log entries are formatted
  message LogFormatterConfig {
    // Formatting strategy
    FormatterType type = 1;

    // Optional format pattern
    string pattern = 2;
  }
}
```

---

### auth_config.proto {#auth_config}

**Path**: `gcommon/v1/common/auth_config.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `AuthAuthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_config.proto
// version: 1.0.1
// guid: b2c3d4e5-f6a7-890b-c1d2-e3f4a5b6c7d8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthConfig defines authentication configuration for the application
 * including token lifetimes and password requirements.
 */
message AuthAuthConfig {
  // How long issued access tokens remain valid
  google.protobuf.Timestamp access_token_ttl = 1;

  // How long refresh tokens remain valid
  google.protobuf.Timestamp refresh_token_ttl = 2;

  // Whether multi-factor authentication is required
  bool require_mfa = 3;
}
```

---

### circuit_breaker_config.proto {#circuit_breaker_config}

**Path**: `gcommon/v1/common/circuit_breaker_config.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `CommonCircuitBreakerConfig`

**Imports** (4):

- `gcommon/v1/common/circuit_breaker_state.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/circuit_breaker_config.proto
// version: 1.0.0
// guid: 2fa42a3e-78ac-439f-ab85-af2587126423
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/circuit_breaker_state.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Circuit breaker configuration for fault tolerance and system protection.
 * Implements the circuit breaker pattern with configurable thresholds,
 * timeouts, and state management for preventing cascade failures.
 */
message CommonCircuitBreakerConfig {
  // Number of consecutive failures to trigger circuit opening
  int32 failure_threshold = 1 [(buf.validate.field).int32.gte = 0];

  // Number of consecutive successes to close the circuit
  int32 success_threshold = 2 [(buf.validate.field).int32.gte = 0];

  // Duration to keep circuit open before attempting half-open
  google.protobuf.Duration timeout = 3;

  // Maximum concurrent requests allowed in half-open state
  int32 max_requests = 4 [(buf.validate.field).int32.gte = 0];

  // Time window for counting failures and successes
  google.protobuf.Duration window_size = 5;

  // Current state of the circuit breaker
  CircuitBreakerState state = 6;
}
```

---

### config_alert_severity.proto {#config_alert_severity}

**Path**: `gcommon/v1/common/config_alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ConfigAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/alert_severity.proto
// version: 1.0.1
// guid: e4538794-5759-4c3f-a3ed-b3794a014e86

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConfigAlertSeverity {
  CONFIG_ALERT_SEVERITY_UNSPECIFIED = 0;
  CONFIG_ALERT_SEVERITY_LOW = 1;
  CONFIG_ALERT_SEVERITY_MEDIUM = 2;
  CONFIG_ALERT_SEVERITY_HIGH = 3;
  CONFIG_ALERT_SEVERITY_CRITICAL = 4;
}
```

---

### config_change_type.proto {#config_change_type}

**Path**: `gcommon/v1/common/config_change_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `TemplateChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/change_type.proto
// version: 1.0.1
// guid: 0e330584-b155-45f0-8c79-0aa19e9aa30e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TemplateChangeType {
  TEMPLATE_CHANGE_TYPE_UNSPECIFIED = 0;
  TEMPLATE_CHANGE_TYPE_FEATURE = 1;
  TEMPLATE_CHANGE_TYPE_BUGFIX = 2;
  TEMPLATE_CHANGE_TYPE_ENHANCEMENT = 3;
  TEMPLATE_CHANGE_TYPE_DEPRECATED = 4;
  TEMPLATE_CHANGE_TYPE_SECURITY = 5;
  CHANGE_TYPE_BREAKING = 6;
}
```

---

### config_config_change_type.proto {#config_config_change_type}

**Path**: `gcommon/v1/common/config_config_change_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ConfigChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_change_type.proto
// version: 1.0.1
// guid: 0d47edd3-705c-42cb-a851-afe79bc2973d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigChangeType enumerates configuration change events.
 */
enum ConfigChangeType {
  CONFIG_CHANGE_TYPE_UNSPECIFIED = 0;
  CONFIG_CHANGE_TYPE_CREATED = 1;
  CONFIG_CHANGE_TYPE_UPDATED = 2;
  CONFIG_CHANGE_TYPE_DELETED = 3;
}
```

---

### config_data_type.proto {#config_data_type}

**Path**: `gcommon/v1/common/config_data_type.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `ConfigDataType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_data_type.proto
// version: 1.0.1
// guid: f619e4df-f067-46db-a813-30458f7fd517

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConfigDataType {
  CONFIG_DATA_TYPE_UNSPECIFIED = 0;
  CONFIG_DATA_TYPE_STRING = 1;
  CONFIG_DATA_TYPE_INTEGER = 2;
  CONFIG_DATA_TYPE_FLOAT = 3;
  CONFIG_DATA_TYPE_BOOLEAN = 4;
  CONFIG_DATA_TYPE_ENUM = 5;
  CONFIG_DATA_TYPE_LIST = 6;
  CONFIG_DATA_TYPE_MAP = 7;
  CONFIG_DATA_TYPE_JSON = 8;
  CONFIG_DATA_TYPE_YAML = 9;
  CONFIG_DATA_TYPE_URL = 10;
  CONFIG_DATA_TYPE_EMAIL = 11;
  CONFIG_DATA_TYPE_PASSWORD = 12;
  CONFIG_DATA_TYPE_CERTIFICATE = 13;
  CONFIG_DATA_TYPE_PRIVATE_KEY = 14;
  CONFIG_DATA_TYPE_PUBLIC_KEY = 15;
  CONFIG_DATA_TYPE_DURATION = 16;
  CONFIG_DATA_TYPE_TIMESTAMP = 17;
  CONFIG_DATA_TYPE_REGEX = 18;
  CONFIG_DATA_TYPE_IPV4 = 19;
  CONFIG_DATA_TYPE_IPV6 = 20;
  CONFIG_DATA_TYPE_CIDR = 21;
  CONFIG_DATA_TYPE_PORT = 22;
  CONFIG_DATA_TYPE_UUID = 23;
  CONFIG_DATA_TYPE_BASE64 = 24;
  CONFIG_DATA_TYPE_HEX = 25;
}
```

---

### config_retry_settings.proto {#config_retry_settings}

**Path**: `gcommon/v1/common/config_retry_settings.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `ConfigRetrySettings`

**Imports** (3):

- `gcommon/v1/common/backoff_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/retry_settings.proto
// version: 1.0.0
// guid: 97d15dc6-ddeb-4e88-a455-16bb8fb5c292

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/backoff_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ConfigRetrySettings {
  // Whether retry is enabled
  bool enabled = 1;

  // Maximum retry count
  int32 max_retries = 2 [(buf.validate.field).int32.gte = 0];

  // Retry delay in seconds
  int32 delay_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Retry backoff strategy
  gcommon.v1.common.BackoffStrategy backoff_strategy = 4;

  // Retry conditions
  repeated string conditions = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### config_value.proto {#config_value}

**Path**: `gcommon/v1/common/config_value.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `ConfigValue`

**Imports** (4):

- `gcommon/v1/common/value_type.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/config_value.proto
// version: 1.0.0
// guid: 343ca568-969b-4136-953b-7eac76c64553
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/value_type.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration value with type information and metadata.
 * Supports multiple value types with encryption and validation capabilities
 * for secure and type-safe configuration management.
 */
message ConfigValue {
  // The configuration value (one of the supported types)
  oneof value {
    // String value for text configuration
    string string_value = 1 [(buf.validate.field).string.min_len = 1];

    // Integer value for numeric configuration
    int64 int_value = 2 [(buf.validate.field).int64.gte = 0];

    // Double value for floating-point configuration
    double double_value = 3 [(buf.validate.field).double.gte = 0.0];

    // Boolean value for true/false configuration
    bool bool_value = 4;

    // Binary data for complex configuration
    bytes bytes_value = 5;

    // Any protobuf message for structured configuration
    google.protobuf.Any any_value = 6 [lazy = true];
  }

  // Value type for validation and serialization
  gcommon.v1.common.ValueType type = 7;

  // Whether the value is encrypted at rest
  bool encrypted = 8;

  // Additional metadata about the configuration value
  map<string, string> metadata = 9 [lazy = true];
}
```

---

### configure_alerting_request.proto {#configure_alerting_request}

**Path**: `gcommon/v1/common/configure_alerting_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ConfigureAlertingRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/configure_alerting_request.proto
// version: 1.0.0
// guid: 760eeee5-189e-489d-b385-42e80f43726f
// file: proto/gcommon/v1/common/configure_alerting_request.proto
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

message ConfigureAlertingRequest {
  // Name of the service or check to configure
  string target = 1 [(buf.validate.field).string.min_len = 1];

  // Whether alerting is enabled for this check
  bool enabled = 2;

  // Number of consecutive failures required before alerting
  int32 failure_threshold = 3 [(buf.validate.field).int32.gte = 0];

  // Optional notification channels (email, slack, etc.)
  repeated string channels = 4 [(buf.validate.field).repeated.min_items = 1];

  // Standard request metadata for tracing and auth
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### configure_alerting_response.proto {#configure_alerting_response}

**Path**: `gcommon/v1/common/configure_alerting_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `ConfigureAlertingResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/configure_alerting_response.proto
// version: 1.0.0
// guid: f996c2ec-cfc9-45c8-8d78-97eef22d2df4
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for configuring alerting settings.
 * Contains the result of alerting configuration changes.
 */
message ConfigureAlertingResponse {
  // Success status
  bool success = 1;

  // Configuration ID
  string config_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if configuration failed
  gcommon.v1.common.Error error = 3;

  // Applied alerting rules
  repeated string applied_rules = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### configure_logger_request.proto {#configure_logger_request}

**Path**: `gcommon/v1/common/configure_logger_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `ConfigureLoggerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/configure_logger_request.proto
// version: 1.0.0
// guid: 2f3e4d5c-6b7a-8190-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigureLoggerRequest defines the request for configuring logger settings.
 */
message ConfigureLoggerRequest {
  // Logger name or identifier
  string logger_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Log level to set
  string level = 2;

  // Output configuration
  string output_config = 3;
}
```

---

### configure_logger_response.proto {#configure_logger_response}

**Path**: `gcommon/v1/common/configure_logger_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `ConfigureLoggerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/configure_logger_response.proto
// version: 1.0.0
// guid: 3f4e5d6c-7b8a-9201-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigureLoggerResponse defines the response from configuring logger settings.
 */
message ConfigureLoggerResponse {
  // Status of the configuration
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### formatter_config.proto {#formatter_config}

**Path**: `gcommon/v1/common/formatter_config.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `LogFormatterConfig`

**Imports** (3):

- `gcommon/v1/common/formatter_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/formatter_config.proto
// version: 1.0.0
// guid: d4e8088a-7b07-48cf-b572-0d850b7218e4

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/formatter_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message LogFormatterConfig {
  // Formatting strategy
  gcommon.v1.common.FormatterType type = 1;

  // Optional format pattern
  string pattern = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_auth_config_request.proto {#get_auth_config_request}

**Path**: `gcommon/v1/common/get_auth_config_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetAuthConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_auth_config_request.proto
// version: 1.0.0
// guid: 8931da09-15df-4c40-a4c1-6be6ad1806f5
// file: proto/gcommon/v1/common/get_auth_config_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetAuthConfigRequest {
  // Optional specific config keys to retrieve
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Include sensitive configuration
  bool include_sensitive = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### health_config.proto {#health_config}

**Path**: `gcommon/v1/common/health_config.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `HealthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_config.proto
// version: 1.0.0
// guid: ebed5c7e-06be-4527-8d87-41afd0b1320d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthConfig represents health configuration
 */
message HealthConfig {
  // Whether health checking is enabled
  bool enabled = 1;
  // Health endpoint path
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];
  // Liveness check path
  string liveness_path = 3 [(buf.validate.field).string.min_len = 1];
  // Readiness check path
  string readiness_path = 4 [(buf.validate.field).string.min_len = 1];
  // Startup check path
  string startup_path = 5 [(buf.validate.field).string.min_len = 1];
  // Check timeout in seconds
  int32 timeout_seconds = 6 [(buf.validate.field).int32.gt = 0];
  // Check interval in seconds
  int32 interval_seconds = 7 [(buf.validate.field).int32.gte = 0];
  // Grace period in seconds
  int32 grace_period_seconds = 8 [(buf.validate.field).int32.gte = 0];
  // Number of retries
  int32 retries = 9 [(buf.validate.field).int32.gte = 0];
}
```

---

### jwt_config.proto {#jwt_config}

**Path**: `gcommon/v1/common/jwt_config.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `JWTConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/jwt_config.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-90c1-d2e3-f4a5b6c7d8e9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * JWTConfig defines parameters for JWT token generation and validation.
 */
message JWTConfig {
  // Signing algorithm used for tokens (e.g., HS256, RS256)
  string signing_algorithm = 1 [(buf.validate.field).string.min_len = 1];

  // Duration access tokens remain valid
  google.protobuf.Duration access_token_ttl = 2;

  // Duration refresh tokens remain valid
  google.protobuf.Duration refresh_token_ttl = 3;
}
```

---

### ldap_config.proto {#ldap_config}

**Path**: `gcommon/v1/common/ldap_config.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `LdapConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/ldap_config.proto
// version: 1.0.0
// guid: de3eeaac-ad85-4f66-a525-670864c5815d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration options for LDAP authentication providers.
 */
message LdapConfig {
  // Hostname or IP address of the LDAP server.
  string host = 1 [(buf.validate.field).string.min_len = 1];

  // Port number for the LDAP server.
  int32 port = 2 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Whether to use TLS for connections.
  bool use_tls = 3;

  // Distinguished name used to bind to the server.
  string bind_dn = 4 [(buf.validate.field).string.min_len = 1];

  // Password for the bind DN.
  string bind_password = 5 [(buf.validate.field).string.min_len = 8];

  // Base DN for searches.
  string base_dn = 6 [(buf.validate.field).string.min_len = 1];

  // LDAP filter used to locate user records.
  string user_filter = 7 [(buf.validate.field).string.min_len = 1];

  // LDAP filter used to locate group records.
  string group_filter = 8 [(buf.validate.field).string.min_len = 1];

  // Connection timeout in seconds.
  int32 timeout_seconds = 9 [(buf.validate.field).int32.gt = 0];

  // Additional provider-specific attributes.
  map<string, string> attributes = 10 [lazy = true];
}
```

---

### logger_config.proto {#logger_config}

**Path**: `gcommon/v1/common/logger_config.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `LoggerConfig`

**Imports** (4):

- `gcommon/v1/common/appender_config.proto`
- `gcommon/v1/common/log_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logger_config.proto
// version: 1.0.0
// guid: 37c6c755-fc97-46c2-8116-248fc5a0ce3c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/appender_config.proto";
import "gcommon/v1/common/log_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LoggerConfig defines configuration for a logger instance
message LoggerConfig {
  // Minimum log level for this logger
  LogLevel level = 1;

  // Output appenders used by this logger
  repeated AppenderConfig appenders = 2 [(buf.validate.field).repeated.min_items = 1];

  // Inherit appenders from parent logger
  bool inherit_appenders = 3;

  // Propagate log entries to parent logger
  bool propagate = 4;

  // Additional logger properties
  map<string, string> properties = 5;
}
```

---

### metrics_api_key_config.proto {#metrics_api_key_config}

**Path**: `gcommon/v1/common/metrics_api_key_config.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `MetricsAPIKeyConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/api_key_config.proto
// version: 1.0.0
// guid: af9b891a-1959-43c2-a287-891b402b4cdf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MetricsAPIKeyConfig {
  // Header name for API key
  string header_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether API key is required
  bool required = 2;

  // Allowed API keys (for validation)
  repeated string allowed_keys = 3;
}
```

---

### metrics_config_change.proto {#metrics_config_change}

**Path**: `gcommon/v1/common/metrics_config_change.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `MetricsConfigChange`

**Imports** (3):

- `gcommon/v1/common/change_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/config_change.proto
// version: 1.1.0
// guid: 29bbb593-9903-43ef-a25e-1c3c7c0a4e64

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/change_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigChange describes a configuration change that was made.
 */
message MetricsConfigChange {
  // Type of change
  gcommon.v1.common.MetricsChangeType change_type = 1;

  // Setting that was changed
  string setting_path = 2;

  // Old value (if applicable)
  string old_value = 3;

  // New value
  string new_value = 4;

  // Description of the change
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### metrics_retention_policy_config.proto {#metrics_retention_policy_config}

**Path**: `gcommon/v1/common/metrics_retention_policy_config.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `MetricsRetentionPolicyConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_policy_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174024

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Retention policy configuration for metric data.
 */
message MetricsRetentionPolicyConfig {
  // How long to retain data
  google.protobuf.Duration duration = 1;

  // Storage tier configuration
  string storage_tier = 2 [(buf.validate.field).string.min_len = 1];

  // Compression settings
  string compression = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### mfa_config.proto {#mfa_config}

**Path**: `gcommon/v1/common/mfa_config.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `MfaConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_config.proto
// version: 1.0.0
// guid: ae560b06-340b-4dca-9a42-dc0eb623fbb1

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Multi-factor authentication configuration settings.
 */
message MfaConfig {
  // Whether MFA is enabled.
  bool enabled = 1;

  // Supported MFA methods (e.g., "totp", "sms", "email").
  repeated string methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Time-based one-time password period in seconds.
  int32 totp_period = 3 [(buf.validate.field).int32.gte = 0];

  // Number of digits for TOTP codes.
  int32 totp_digits = 4 [(buf.validate.field).int32.gte = 0];

  // Whether SMS delivery is enabled.
  bool sms_enabled = 5;

  // Whether email delivery is enabled.
  bool email_enabled = 6;
}
```

---

### o_auth2_config.proto {#o_auth2_config}

**Path**: `gcommon/v1/common/o_auth2_config.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Messages** (1): `OAuth2Config`

**Imports** (4):

- `gcommon/v1/common/jwt_config.proto`
- `gcommon/v1/common/oauth2_flow_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/o_auth2_config.proto
// version: 1.1.0
// guid: a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/jwt_config.proto";
import "gcommon/v1/common/oauth2_flow_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 configuration for authentication providers.
 * Supports various OAuth2 flows and provider configurations.
 */
message OAuth2Config {
  // OAuth2 provider name
  string provider_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
  string redirect_uri = 7 [ (buf.validate.field).string.uri = true ];

  // Requested scopes
  repeated string scopes = 8;

  // OAuth2 flow type
  gcommon.v1.common.OAuth2FlowType flow_type = 9;

  // Additional provider-specific parameters
  map<string, string> additional_params = 10;

  // Whether PKCE is required
  bool require_pkce = 11;

  // JWT configuration for token validation
  JWTConfig jwt_config = 12;
}
```

---

### output_config.proto {#output_config}

**Path**: `gcommon/v1/common/output_config.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `OutputConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/output_config.proto
// version: 1.0.0
// guid: 0ee0198f-adab-435c-b8b9-0d67f7c06af0

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OutputConfig {
  // Output target (file path, network address, etc.)
  string target = 1 [(buf.validate.field).string.min_len = 1];

  // Additional output options
  map<string, string> options = 2;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/common/rate_limit_config.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `AuthRateLimitConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/rate_limit_config.proto
// version: 1.0.0
// guid: 5769fd20-09d6-4038-bf86-8087ee0374a0
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Rate limiting configuration for authentication operations.
 * Used to prevent abuse and enforce security policies.
 * Supports various rate limiting strategies.
 */
message AuthRateLimitConfig {
  // Maximum number of requests allowed
  int32 max_requests = 1 [(buf.validate.field).int32.gte = 0];

  // Time window for rate limiting
  google.protobuf.Duration time_window = 2;

  // Burst allowance (max requests in short burst)
  int32 burst_allowance = 3 [(buf.validate.field).int32.gte = 0];

  // Rate limit scope (per user, per IP, etc.)
  string scope = 4 [(buf.validate.field).string.min_len = 1];

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

**Path**: `gcommon/v1/common/saml_config.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `SamlConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/saml_config.proto
// version: 1.0.0
// guid: b1088674-0c17-45db-8c6d-3022ce0a629b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration options for SAML authentication.
 */
message SamlConfig {
  // URL for the identity provider metadata.
  string idp_metadata_url = 1 [ (buf.validate.field).string.uri = true ];

  // Service provider entity ID.
  string sp_entity_id = 2;

  // Service provider assertion consumer service URL.
  string sp_acs_url = 3 [ (buf.validate.field).string.uri = true ];

  // X.509 certificate for the service provider.
  string certificate = 4;

  // Private key for the service provider certificate.
  string private_key = 5;

  // Allowed domains for SAML assertions.
  repeated string allowed_domains = 6;
}
```

---

### session_config.proto {#session_config}

**Path**: `gcommon/v1/common/session_config.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `AuthSessionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_config.proto
// version: 1.0.0
// guid: cf31dcbd-ba1f-402c-a37c-c1a2afe2dba8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration parameters for user sessions.
 */
message AuthSessionConfig {
  // Idle timeout in seconds before session expiration.
  int32 idle_timeout_seconds = 1;

  // Absolute lifetime of a session in seconds.
  int32 absolute_lifetime_seconds = 2;

  // Whether sessions persist across server restarts.
  bool persist_across_restarts = 3;

  // Name of the session cookie.
  string cookie_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether to mark the cookie as secure.
  bool secure_cookie = 5;
}
```

---

