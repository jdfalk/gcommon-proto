# common_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 15
- **Services**: 0
- **Enums**: 35

## Files in this Module

- [dashboard_type.proto](#dashboard_type)
- [database_isolation_level.proto](#database_isolation_level)
- [database_status_code.proto](#database_status_code)
- [debug_info.proto](#debug_info)
- [delivery_channel.proto](#delivery_channel)
- [delivery_channel_type.proto](#delivery_channel_type)
- [delivery_mode.proto](#delivery_mode)
- [delivery_status.proto](#delivery_status)
- [dependency_type.proto](#dependency_type)
- [deployment_status.proto](#deployment_status)
- [deprecation_level.proto](#deprecation_level)
- [device_info.proto](#device_info)
- [durability_level.proto](#durability_level)
- [email_template.proto](#email_template)
- [environment_status.proto](#environment_status)
- [environment_type.proto](#environment_type)
- [error.proto](#error)
- [error_code.proto](#error_code)
- [error_info.proto](#error_info)
- [error_type_count.proto](#error_type_count)
- [eviction_policy.proto](#eviction_policy)
- [expiration_policy.proto](#expiration_policy)
- [export_format.proto](#export_format)
- [file_sort_order.proto](#file_sort_order)
- [filter_action.proto](#filter_action)
- [filter_operation.proto](#filter_operation)
- [filter_options.proto](#filter_options)
- [filter_type.proto](#filter_type)
- [filter_value.proto](#filter_value)
- [flush_policy.proto](#flush_policy)
- [formatter_type.proto](#formatter_type)
- [gauge_operation.proto](#gauge_operation)
- [grant_type.proto](#grant_type)
- [group.proto](#group)
- [handler_type.proto](#handler_type)
- [health_check_result.proto](#health_check_result)
- [health_check_type.proto](#health_check_type)
- [health_metric_data.proto](#health_metric_data)
- [health_metrics.proto](#health_metrics)
- [health_state.proto](#health_state)
- [health_status.proto](#health_status)
- [hierarchy_type.proto](#hierarchy_type)
- [hook_error_handling.proto](#hook_error_handling)
- [hook_type.proto](#hook_type)
- [http_method.proto](#http_method)
- [http_status.proto](#http_status)
- [inheritance_strategy.proto](#inheritance_strategy)
- [int64_array.proto](#int64_array)
- [isolation_level.proto](#isolation_level)
- [jwt_credentials.proto](#jwt_credentials)
---


## Detailed Documentation

### dashboard_type.proto {#dashboard_type}

**Path**: `gcommon/v1/common/dashboard_type.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `DashboardType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/dashboard_type.proto
// version: 1.0.1
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// DashboardType represents different types of dashboards
enum DashboardType {
  // Unspecified dashboard type
  DASHBOARD_TYPE_UNSPECIFIED = 0;

  // System overview dashboard
  DASHBOARD_TYPE_SYSTEM_OVERVIEW = 1;

  // Application performance dashboard
  DASHBOARD_TYPE_APPLICATION_PERFORMANCE = 2;

  // Infrastructure monitoring dashboard
  DASHBOARD_TYPE_INFRASTRUCTURE = 3;

  // Business metrics dashboard
  DASHBOARD_TYPE_BUSINESS_METRICS = 4;

  // Security monitoring dashboard
  DASHBOARD_TYPE_SECURITY = 5;

  // Custom dashboard
  DASHBOARD_TYPE_CUSTOM = 6;

  // Real-time monitoring dashboard
  DASHBOARD_TYPE_REAL_TIME = 7;

  // Historical analysis dashboard
  DASHBOARD_TYPE_HISTORICAL = 8;

  // Alert summary dashboard
  DASHBOARD_TYPE_ALERT_SUMMARY = 9;

  // Service health dashboard
  DASHBOARD_TYPE_SERVICE_HEALTH = 10;

  // Capacity planning dashboard
  DASHBOARD_TYPE_CAPACITY_PLANNING = 11;

  // SLA/SLO tracking dashboard
  DASHBOARD_TYPE_SLA_SLO = 12;
}
```

---

### database_isolation_level.proto {#database_isolation_level}

**Path**: `gcommon/v1/common/database_isolation_level.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `DatabaseIsolationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/isolation_level.proto
// version: 1.0.1
// guid: 004cde4c-f6bc-40ff-b341-1408e58e37b6
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * IsolationLevel defines transaction isolation levels controlling concurrent access.
 * Balances data consistency with concurrency performance.
 */
enum DatabaseIsolationLevel {
  // Default unspecified isolation level
  DATABASE_ISOLATION_LEVEL_UNSPECIFIED = 0;

  // Read uncommitted - allows dirty reads, lowest isolation
  DATABASE_ISOLATION_LEVEL_READ_UNCOMMITTED = 1;

  // Read committed - prevents dirty reads, allows non-repeatable reads
  DATABASE_ISOLATION_LEVEL_READ_COMMITTED = 2;

  // Repeatable read - prevents dirty and non-repeatable reads
  DATABASE_ISOLATION_LEVEL_REPEATABLE_READ = 3;

  // Serializable - highest isolation, prevents all phenomena
  DATABASE_ISOLATION_LEVEL_SERIALIZABLE = 4;
}
```

---

### database_status_code.proto {#database_status_code}

**Path**: `gcommon/v1/common/database_status_code.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `DatabaseStatusCode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/database_status_code.proto
// version: 1.0.1
// guid: 9849ce1c-df0e-418d-9de6-27b7b1b99d99

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * DatabaseStatusCode represents the health state of a database
 * connection or service.
 */
enum DatabaseStatusCode {
  // Default unspecified status
  DATABASE_STATUS_CODE_UNSPECIFIED = 0;

  // Database is reachable and operational
  DATABASE_STATUS_CODE_OK = 1;

  // Database is unreachable or returned an error
  DATABASE_STATUS_CODE_ERROR = 2;
}
```

---

### debug_info.proto {#debug_info}

**Path**: `gcommon/v1/common/debug_info.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `DebugInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/debug_info.proto
// version: 1.0.0
// guid: 5cfc62b5-b458-4d97-bf91-b5a1c3eccadf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * DebugInfo provides supplemental debugging information
 * that can be included in request or response messages.
 * It captures contextual details useful for tracing and
 * troubleshooting complex issues.
 */
message DebugInfo {
  // Service or component name emitting this debug info
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Optional method or operation identifier
  string method = 2 [(buf.validate.field).string.min_len = 1];

  // Time when this debug info was generated
  google.protobuf.Timestamp timestamp = 3;

  // Arbitrary key/value details for debugging
  map<string, string> details = 4;

  // Additional tags to categorize or filter debug entries
  repeated string tags = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### delivery_channel.proto {#delivery_channel}

**Path**: `gcommon/v1/common/delivery_channel.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeliveryChannel`

**Imports** (3):

- `gcommon/v1/common/delivery_channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delivery_channel.proto
// version: 1.1.0
// guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Delivery channel specifying how a notification is sent.
 */
message DeliveryChannel {
  // Channel type such as email or SMS
  gcommon.v1.common.DeliveryChannelType type = 1;

  // Destination address (email, phone number, webhook URL, etc.)
  string target = 2 [(buf.validate.field).string.min_len = 1];

  // Optional channel specific configuration
  map<string, string> config = 3 [lazy = true];
}
```

---

### delivery_channel_type.proto {#delivery_channel_type}

**Path**: `gcommon/v1/common/delivery_channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `DeliveryChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delivery_channel_type.proto
// version: 1.0.1
// guid: c5d6e7f8-a9b0-1c2d-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Delivery channel type enumeration.
 * Specifies the communication channel for notification delivery.
 */
enum DeliveryChannelType {
  // Unspecified delivery channel
  DELIVERY_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email delivery
  DELIVERY_CHANNEL_TYPE_EMAIL = 1;

  // SMS delivery
  DELIVERY_CHANNEL_TYPE_SMS = 2;

  // Slack message delivery
  DELIVERY_CHANNEL_TYPE_SLACK = 3;

  // Webhook delivery
  DELIVERY_CHANNEL_TYPE_WEBHOOK = 4;
}
```

---

### delivery_mode.proto {#delivery_mode}

**Path**: `gcommon/v1/common/delivery_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `DeliveryMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/delivery_mode.proto
// file: proto/gcommon/v1/queue/delivery_mode.proto
// version: 1.0.1
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Message delivery mode for queue operations.
 */
enum DeliveryMode {
  // Default unspecified delivery mode
  DELIVERY_MODE_UNSPECIFIED = 0;

  // At most once delivery (may lose messages, no duplicates)
  DELIVERY_MODE_AT_MOST_ONCE = 1;

  // At least once delivery (no message loss, may have duplicates)
  DELIVERY_MODE_AT_LEAST_ONCE = 2;

  // Exactly once delivery (no loss, no duplicates - when supported)
  DELIVERY_MODE_EXACTLY_ONCE = 3;

  // Best effort delivery (no guarantees)
  DELIVERY_MODE_BEST_EFFORT = 4;
}
```

---

### delivery_status.proto {#delivery_status}

**Path**: `gcommon/v1/common/delivery_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `DeliveryStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delivery_status.proto
// version: 1.0.1
// guid: 6548d52a-11c5-44c0-bbf8-269fecf8eab3
// file: proto/gcommon/v1/common/delivery_status.proto
//
// Delivery status enumeration for tracking notification outcomes.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Notification delivery status
enum DeliveryStatus {
  DELIVERY_STATUS_UNSPECIFIED = 0;
  DELIVERY_STATUS_PENDING = 1;
  DELIVERY_STATUS_SENT = 2;
  DELIVERY_STATUS_FAILED = 3;
  DELIVERY_STATUS_ACKNOWLEDGED = 4;
}
```

---

### dependency_type.proto {#dependency_type}

**Path**: `gcommon/v1/common/dependency_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `DependencyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/dependency_type.proto
// version: 1.0.1
// guid: 0dbbaf99-12ad-49af-8747-0eb055671d35

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum DependencyType {
  DEPENDENCY_TYPE_UNSPECIFIED = 0;
  DEPENDENCY_TYPE_REQUIRED = 1;
  DEPENDENCY_TYPE_OPTIONAL = 2;
  DEPENDENCY_TYPE_CONDITIONAL = 3;
  DEPENDENCY_TYPE_DERIVED = 4;
  DEPENDENCY_TYPE_CONFLICT = 5;
}
```

---

### deployment_status.proto {#deployment_status}

**Path**: `gcommon/v1/common/deployment_status.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `DeploymentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deployment_status.proto
// version: 1.0.1
// guid: e3f4a5b6-c7d8-9e0f-1a2b-3c4d5e6f7a8b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * DeploymentStatus represents the status of a deployment.
 * Specifies the current state of configuration deployment operations.
 */
enum DeploymentStatus {
  // Unspecified deployment status
  DEPLOYMENT_STATUS_UNSPECIFIED = 0;

  // Deployment is pending
  DEPLOYMENT_STATUS_PENDING = 1;

  // Deployment is in progress
  DEPLOYMENT_STATUS_IN_PROGRESS = 2;

  // Deployment completed successfully
  DEPLOYMENT_STATUS_SUCCESS = 3;

  // Deployment failed
  DEPLOYMENT_STATUS_FAILED = 4;

  // Deployment was rolled back
  DEPLOYMENT_STATUS_ROLLED_BACK = 5;

  // Deployment was cancelled
  DEPLOYMENT_STATUS_CANCELLED = 6;
}
```

---

### deprecation_level.proto {#deprecation_level}

**Path**: `gcommon/v1/common/deprecation_level.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `DeprecationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deprecation_level.proto
// version: 1.0.1
// guid: 0a330fa1-9f33-458b-a37e-aeed96ad7530

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum DeprecationLevel {
  DEPRECATION_LEVEL_UNSPECIFIED = 0;
  DEPRECATION_LEVEL_SOFT = 1; // Soft deprecation (warning)
  DEPRECATION_LEVEL_HARD = 2; // Hard deprecation (error)
  DEPRECATION_LEVEL_REMOVAL = 3; // Scheduled for removal
}
```

---

### device_info.proto {#device_info}

**Path**: `gcommon/v1/common/device_info.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `DeviceInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/device_info.proto
// version: 1.0.0
// guid: 3c9b9c62-c45a-4919-bbf2-88ae536fc5e6

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeviceInfo {
  string device_id = 1 [(buf.validate.field).string.min_len = 1];
  string device_type = 2; // mobile, desktop, tablet
  string os = 3 [(buf.validate.field).string.min_len = 1];
  string browser = 4 [(buf.validate.field).string.min_len = 1];
  bool is_trusted = 5;
}
```

---

### durability_level.proto {#durability_level}

**Path**: `gcommon/v1/common/durability_level.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `DurabilityLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/durability_level.proto
// file: proto/gcommon/v1/queue/durability_level.proto
// version: 1.0.1
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Durability levels for message persistence guarantees.
 */
enum DurabilityLevel {
  // Default unspecified level
  DURABILITY_LEVEL_UNSPECIFIED = 0;

  // No durability - messages may be lost on restart
  DURABILITY_LEVEL_NONE = 1;

  // Memory-only persistence with periodic snapshots
  DURABILITY_LEVEL_MEMORY = 2;

  // Synchronous disk persistence for each message
  DURABILITY_LEVEL_DISK_SYNC = 3;

  // Asynchronous disk persistence with batching
  DURABILITY_LEVEL_DISK_ASYNC = 4;

  // Replicated across multiple nodes with disk persistence
  DURABILITY_LEVEL_REPLICATED = 5;
}
```

---

### email_template.proto {#email_template}

**Path**: `gcommon/v1/common/email_template.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `EmailTemplate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/email_template.proto
// version: 1.0.0
// guid: 03debb46-12b4-4099-9c8f-99523c435029

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EmailTemplate {
  // Template name/type (e.g., "welcome", "password_reset")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Email subject template
  string subject = 2;

  // Email body template (HTML)
  string body_html = 3;

  // Email body template (plain text)
  string body_text = 4;
}
```

---

### environment_status.proto {#environment_status}

**Path**: `gcommon/v1/common/environment_status.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `EnvironmentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/environment_status.proto
// version: 1.0.1
// guid: d2e3f4a5-b6c7-8d9e-0f1a-2b3c4d5e6f7a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * EnvironmentStatus represents the status of an environment.
 * Specifies the current operational state of a configuration environment.
 */
enum EnvironmentStatus {
  // Unspecified environment status
  ENVIRONMENT_STATUS_UNSPECIFIED = 0;

  // Environment is active and operational
  ENVIRONMENT_STATUS_ACTIVE = 1;

  // Environment is inactive
  ENVIRONMENT_STATUS_INACTIVE = 2;

  // Environment is under maintenance
  ENVIRONMENT_STATUS_MAINTENANCE = 3;

  // Environment is deprecated
  ENVIRONMENT_STATUS_DEPRECATED = 4;

  // Environment is archived
  ENVIRONMENT_STATUS_ARCHIVED = 5;

  // Environment is in error state
  ENVIRONMENT_STATUS_ERROR = 6;
}
```

---

### environment_type.proto {#environment_type}

**Path**: `gcommon/v1/common/environment_type.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Enums** (1): `EnvironmentType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/environment_type.proto
// version: 1.0.1
// guid: c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * EnvironmentType represents the type of environment.
 * Specifies the purpose and classification of configuration environments.
 */
enum EnvironmentType {
  // Unspecified environment type
  ENVIRONMENT_TYPE_UNSPECIFIED = 0;

  // Development environment
  ENVIRONMENT_TYPE_DEVELOPMENT = 1;

  // Testing environment
  ENVIRONMENT_TYPE_TESTING = 2;

  // Staging environment
  ENVIRONMENT_TYPE_STAGING = 3;

  // Production environment
  ENVIRONMENT_TYPE_PRODUCTION = 4;

  // Sandbox environment for experimentation
  ENVIRONMENT_TYPE_SANDBOX = 5;

  // Canary deployment environment
  ENVIRONMENT_TYPE_CANARY = 6;

  // Disaster recovery environment
  ENVIRONMENT_TYPE_DISASTER_RECOVERY = 7;

  // Integration testing environment
  ENVIRONMENT_TYPE_INTEGRATION = 8;

  // Performance testing environment
  ENVIRONMENT_TYPE_PERFORMANCE = 9;

  // Security testing environment
  ENVIRONMENT_TYPE_SECURITY = 10;
}
```

---

### error.proto {#error}

**Path**: `gcommon/v1/common/error.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `Error`

**Imports** (4):

- `gcommon/v1/common/error_code.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error.proto
// version: 1.0.0
// guid: 6998154e-e6c6-4156-b1d8-3633dc509d8a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_code.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common error message structure for standardized error handling.
 * Provides comprehensive error information including code, message,
 * debugging details, and traceability across all GCommon modules.
 */
message Error {
  // Standardized error code for programmatic handling
  gcommon.v1.common.ErrorCode code = 1;

  // Human-readable error message describing what went wrong
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Additional error details for debugging and troubleshooting
  map<string, string> details = 3;

  // Distributed trace ID for request correlation across services
  string trace_id = 4 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the error occurred
  google.protobuf.Timestamp timestamp = 5;

  // Source module or component that generated the error
  string source = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### error_code.proto {#error_code}

**Path**: `gcommon/v1/common/error_code.proto` **Package**: `gcommon.v1.common` **Lines**: 64

**Enums** (1): `ErrorCode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error_code.proto
// version: 1.0.1
// guid: 6177a6c6-ea53-448e-8ec8-b526bb86a53f
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Standardized error codes following gRPC conventions.
 * These codes provide consistent error handling across all GCommon modules.
 *
 * Each error code maps to standard gRPC status codes for cross-language compatibility.
 */
enum ErrorCode {
  // Default value indicating no error code was specified
  ERROR_CODE_UNSPECIFIED = 0;

  // Client specified an invalid argument. Request should not be retried without modification
  ERROR_CODE_INVALID_ARGUMENT = 1;

  // Some requested entity was not found
  ERROR_CODE_NOT_FOUND = 2;

  // The entity that a client attempted to create already exists
  ERROR_CODE_ALREADY_EXISTS = 3;

  // The caller does not have permission to execute the specified operation
  ERROR_CODE_PERMISSION_DENIED = 4;

  // The request does not have valid authentication credentials
  ERROR_CODE_UNAUTHENTICATED = 5;

  // Internal server error. Client should not retry
  ERROR_CODE_INTERNAL = 6;

  // The service is currently unavailable. Client may retry
  ERROR_CODE_UNAVAILABLE = 7;

  // Deadline expired before operation could complete
  ERROR_CODE_TIMEOUT = 8;

  // Resource has been exhausted (e.g., quota exceeded)
  ERROR_CODE_RESOURCE_EXHAUSTED = 9;

  // Operation was rejected because the system is not in required state
  ERROR_CODE_FAILED_PRECONDITION = 10;

  // The operation was aborted, typically due to concurrency issue
  ERROR_CODE_ABORTED = 11;

  // Operation was attempted past the valid range
  ERROR_CODE_OUT_OF_RANGE = 12;

  // Operation is not implemented or not supported
  ERROR_CODE_UNIMPLEMENTED = 13;

  // Unrecoverable data loss or corruption
  ERROR_CODE_DATA_LOSS = 14;
}
```

---

### error_info.proto {#error_info}

**Path**: `gcommon/v1/common/error_info.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `ErrorInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error_info.proto
// version: 1.0.0
// guid: ba36f77a-0141-43fc-a77e-fde479168a40

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ErrorInfo provides structured error details for log entries
message ErrorInfo {
  // Error message
  string message = 1 [(buf.validate.field).string.min_len = 1];

  // Error type or class name
  string type = 2 [(buf.validate.field).string.min_len = 1];

  // Full stack trace if available
  string stack_trace = 3 [(buf.validate.field).string.min_len = 1];

  // Application-specific error code
  string code = 4 [(buf.validate.field).string.min_len = 1];

  // Arbitrary key/value context information
  map<string, string> context = 5;

  // Nested causes for error propagation
  repeated ErrorInfo causes = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### error_type_count.proto {#error_type_count}

**Path**: `gcommon/v1/common/error_type_count.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `ErrorTypeCount`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error_type_count.proto
// version: 1.0.0
// guid: 8116a2bc-950e-407c-9db8-2f3985e9394d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ErrorTypeCount {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double percentage = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### eviction_policy.proto {#eviction_policy}

**Path**: `gcommon/v1/common/eviction_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `EvictionPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/eviction_policy.proto
// version: 1.0.1
// guid: 53ad7b97-17b7-45fc-b834-31d09296f358
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Cache eviction policy enumeration for cache management.
 * Defines which cached items should be removed when cache capacity
 * is reached across all GCommon modules.
 */
enum EvictionPolicy {
  // Default value indicating no eviction policy was specified
  EVICTION_POLICY_UNSPECIFIED = 0;

  // Least Recently Used - evict items that haven't been accessed recently
  EVICTION_POLICY_LRU = 1;

  // Least Frequently Used - evict items that are accessed least often
  EVICTION_POLICY_LFU = 2;

  // First In, First Out - evict items in order they were added
  EVICTION_POLICY_FIFO = 3;

  // Random eviction - evict randomly selected items
  EVICTION_POLICY_RANDOM = 4;
}
```

---

### expiration_policy.proto {#expiration_policy}

**Path**: `gcommon/v1/common/expiration_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `ExpirationPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/expiration_policy.proto
// version: 1.0.1
// guid: 788be552-a444-4860-9db6-1004f1f1fabf
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Cache expiration policy enumeration for cache management.
 * Defines how cached items expire and when they should be evicted
 * from cache storage across all GCommon modules.
 */
enum ExpirationPolicy {
  // Default value indicating no expiration policy was specified
  EXPIRATION_POLICY_UNSPECIFIED = 0;

  // Time-to-live based expiration - items expire after a fixed duration
  EXPIRATION_POLICY_TTL = 1;

  // Idle time expiration - items expire after being unused for a duration
  EXPIRATION_POLICY_IDLE = 2;

  // Write time expiration - items expire after a duration from last write
  EXPIRATION_POLICY_WRITE = 3;

  // Never expire - items remain in cache until explicitly removed
  EXPIRATION_POLICY_NEVER = 4;
}
```

---

### export_format.proto {#export_format}

**Path**: `gcommon/v1/common/export_format.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `CommonExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/export_format.proto
// version: 1.0.1
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ExportFormat enumerates data export formats used across all systems
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonExportFormat {
  EXPORT_FORMAT_UNSPECIFIED = 0;
  EXPORT_FORMAT_PROMETHEUS = 1;
  EXPORT_FORMAT_JSON = 2;
  EXPORT_FORMAT_CSV = 3;
  EXPORT_FORMAT_OPENTELEMETRY = 4;
}
```

---

### file_sort_order.proto {#file_sort_order}

**Path**: `gcommon/v1/common/file_sort_order.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `FileSortOrder`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_sort_order.proto
// version: 1.0.1
// guid: f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * File sorting options.
 * Defines how files should be ordered in directory listings.
 */
enum FileSortOrder {
  // Default sorting (name ascending)
  FILE_SORT_ORDER_UNSPECIFIED = 0;

  // Sort by name ascending
  FILE_SORT_ORDER_NAME_ASC = 1;

  // Sort by name descending
  FILE_SORT_ORDER_NAME_DESC = 2;

  // Sort by size ascending
  FILE_SORT_ORDER_SIZE_ASC = 3;

  // Sort by size descending
  FILE_SORT_ORDER_SIZE_DESC = 4;

  // Sort by modification time ascending
  FILE_SORT_ORDER_MODIFIED_ASC = 5;

  // Sort by modification time descending
  FILE_SORT_ORDER_MODIFIED_DESC = 6;
}
```

---

### filter_action.proto {#filter_action}

**Path**: `gcommon/v1/common/filter_action.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `FilterAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/filter_action.proto
// version: 1.0.1
// guid: 733209f2-fa3d-471a-b3c3-260adaecd3a2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum FilterAction {
  FILTER_ACTION_UNSPECIFIED = 0;
  FILTER_ACTION_INCLUDE = 1;
  FILTER_ACTION_EXCLUDE = 2;
  FILTER_ACTION_TRANSFORM = 3;
  FILTER_ACTION_VALIDATE = 4;
}
```

---

### filter_operation.proto {#filter_operation}

**Path**: `gcommon/v1/common/filter_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `FilterOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_operation.proto
// version: 1.0.1
// guid: 792c2366-c261-43b4-8647-d776a7245cc2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Filter operation types for query filtering across all GCommon modules.
 * Provides standardized filtering operations for database queries, search,
 * and other filtering requirements.
 */
enum FilterOperation {
  // Default value indicating no filter operation was specified
  FILTER_OPERATION_UNSPECIFIED = 0;

  // Exact equality match
  FILTER_OPERATION_EQUALS = 1;

  // Not equal to the specified value
  FILTER_OPERATION_NOT_EQUALS = 2;

  // Greater than the specified value (numeric/date comparison)
  FILTER_OPERATION_GREATER_THAN = 3;

  // Less than the specified value (numeric/date comparison)
  FILTER_OPERATION_LESS_THAN = 4;

  // Greater than or equal to the specified value
  FILTER_OPERATION_GREATER_THAN_OR_EQUAL = 5;

  // Less than or equal to the specified value
  FILTER_OPERATION_LESS_THAN_OR_EQUAL = 6;

  // Contains the specified substring (case-sensitive)
  FILTER_OPERATION_CONTAINS = 7;

  // Starts with the specified prefix
  FILTER_OPERATION_STARTS_WITH = 8;

  // Ends with the specified suffix
  FILTER_OPERATION_ENDS_WITH = 9;

  // Value is contained in the specified list
  FILTER_OPERATION_IN = 10;

  // Value is not contained in the specified list
  FILTER_OPERATION_NOT_IN = 11;
}
```

---

### filter_options.proto {#filter_options}

**Path**: `gcommon/v1/common/filter_options.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `FilterOptions`

**Imports** (4):

- `gcommon/v1/common/filter_value.proto`
- `gcommon/v1/common/metrics_time_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_options.proto
// version: 1.0.0
// guid: 1c91c5f0-6774-405a-bb94-4a646e1e859d
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/filter_value.proto";
import "gcommon/v1/common/metrics_time_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common filtering options for search and query operations.
 * Provides a unified interface for filtering data across all GCommon modules.
 *
 * Supports field-based filters, text search, and time range filtering,
 * enabling flexible and powerful query capabilities.
 */
message FilterOptions {
  // Field-based filters with typed values and operations
  map<string, FilterValue> filters = 1;

  // Full-text search query for text-based filtering
  string search_query = 2 [(buf.validate.field).string.min_len = 1];

  // Time range filter for temporal data
  CommonTimeRange time_range = 3;
}
```

---

### filter_type.proto {#filter_type}

**Path**: `gcommon/v1/common/filter_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `LogFilterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_type.proto
// version: 1.0.1
// guid: eb317c45-0d04-48fb-ab44-ab82262f995b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// FilterType enumerates log filter strategies
// buf:lint:ignore ENUM_VALUE_PREFIX
enum LogFilterType {
  FILTER_TYPE_UNSPECIFIED = 0;
  FILTER_TYPE_LEVEL = 1;
  FILTER_TYPE_LOGGER = 2;
  FILTER_TYPE_MESSAGE = 3;
  FILTER_TYPE_FIELD = 4;
}
```

---

### filter_value.proto {#filter_value}

**Path**: `gcommon/v1/common/filter_value.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `FilterValue`

**Imports** (5):

- `gcommon/v1/common/filter_operation.proto`
- `gcommon/v1/common/int64_array.proto`
- `gcommon/v1/common/string_array.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_value.proto
// version: 1.0.0
// guid: e873017a-bb7e-4509-bb4b-ba7a2d08bb2b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/filter_operation.proto";
import "gcommon/v1/common/int64_array.proto";
import "gcommon/v1/common/string_array.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Filter value with multiple type support and operation specification.
 * Enables type-safe filtering with various data types and comparison operations.
 *
 * Supports scalar values (string, int, double, bool) and array values
 * for IN/NOT_IN operations, with explicit operation specification.
 */
message FilterValue {
  // The value to filter by (one of the supported types)
  oneof value {
    // String value for text-based filtering
    string string_value = 1 [(buf.validate.field).string.min_len = 1];

    // Integer value for numeric filtering
    int64 int_value = 2 [(buf.validate.field).int64.gte = 0];

    // Double value for floating-point filtering
    double double_value = 3 [(buf.validate.field).double.gte = 0.0];

    // Boolean value for true/false filtering
    bool bool_value = 4;

    // Array of strings for multi-value filtering
    gcommon.v1.common.StringArray string_array = 5 [lazy = true];

    // Array of integers for multi-value filtering
    gcommon.v1.common.Int64Array int_array = 6 [lazy = true];
  }

  // Filter operation type (equals, contains, greater than, etc.)
  gcommon.v1.common.FilterOperation operation = 7;
}
```

---

### flush_policy.proto {#flush_policy}

**Path**: `gcommon/v1/common/flush_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `FlushPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/flush_policy.proto
// file: proto/gcommon/v1/queue/flush_policy.proto
// version: 1.0.1
// guid: 0a9b8c7d-6e5f-4a3b-2c1d-0e9f8a7b6c5d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Policy for when to flush messages to persistent storage.
 */
enum FlushPolicy {
  // Default unspecified policy
  FLUSH_POLICY_UNSPECIFIED = 0;

  // Flush immediately after each message
  FLUSH_POLICY_IMMEDIATE = 1;

  // Flush after a certain number of messages
  FLUSH_POLICY_BATCH = 2;

  // Flush after a time interval
  FLUSH_POLICY_TIMED = 3;

  // Flush when buffer is full
  FLUSH_POLICY_BUFFER_FULL = 4;

  // Manual flush only
  FLUSH_POLICY_MANUAL = 5;
}
```

---

### formatter_type.proto {#formatter_type}

**Path**: `gcommon/v1/common/formatter_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `FormatterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/formatter_type.proto
// version: 1.0.1
// guid: 0d49c8f5-9abd-4a9e-8d96-ddab6f45249b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// FormatterType enumerates log formatting strategies
enum FormatterType {
  FORMATTER_TYPE_UNSPECIFIED = 0;
  FORMATTER_TYPE_TEXT = 1;
  FORMATTER_TYPE_JSON = 2;
  FORMATTER_TYPE_XML = 3;
  FORMATTER_TYPE_CUSTOM = 4;
}
```

---

### gauge_operation.proto {#gauge_operation}

**Path**: `gcommon/v1/common/gauge_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `GaugeOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/gauge_operation.proto
// version: 1.0.1
// guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GaugeOperation defines how to update the gauge value.
 * Specifies the operation to perform on a gauge metric.
 */
enum GaugeOperation {
  // Unspecified operation (defaults to SET)
  GAUGE_OPERATION_UNSPECIFIED = 0;

  // Set the gauge to the specified value
  GAUGE_OPERATION_SET = 1;

  // Add the value to the current gauge value
  GAUGE_OPERATION_ADD = 2;

  // Subtract the value from the current gauge value
  GAUGE_OPERATION_SUBTRACT = 3;

  // Increment the gauge by 1
  GAUGE_OPERATION_INCREMENT = 4;

  // Decrement the gauge by 1
  GAUGE_OPERATION_DECREMENT = 5;
}
```

---

### grant_type.proto {#grant_type}

**Path**: `gcommon/v1/common/grant_type.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Enums** (1): `GrantType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/grant_type.proto
// version: 1.0.1
// guid: 75a43fdc-3d73-410d-80b1-00ca7583f150
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth 2.0 grant types supported by the authentication system.
 */
enum GrantType {
  // Unspecified grant type.
  GRANT_TYPE_UNSPECIFIED = 0;

  // Authorization code grant.
  GRANT_TYPE_AUTHORIZATION_CODE = 1;

  // Implicit grant (legacy).
  GRANT_TYPE_IMPLICIT = 2;

  // Resource owner password credentials grant.
  GRANT_TYPE_PASSWORD = 3;

  // Client credentials grant.
  GRANT_TYPE_CLIENT_CREDENTIALS = 4;

  // Refresh token grant.
  GRANT_TYPE_REFRESH_TOKEN = 5;

  // Device code grant for device authorization flows.
  GRANT_TYPE_DEVICE_CODE = 6;

  // SAML2 bearer assertion grant.
  GRANT_TYPE_SAML2_BEARER = 7;
}
```

---

### group.proto {#group}

**Path**: `gcommon/v1/common/group.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Messages** (1): `Group`

**Imports** (4):

- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/group.proto
// version: 1.0.0
// guid: 3d1addaa-66d2-4768-9214-6f57d3dea222
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Group entity for organizing users into collections.
 * Used for bulk permission management and organizational structure.
 * Supports hierarchical group relationships.
 */
message Group {
  // Unique group identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Group name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Group description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Parent group ID (for hierarchical groups)
  string parent_group_id = 4;

  // Group permissions
  repeated string permissions = 5;

  // Group metadata for extensibility
  map<string, string> metadata = 6 [lazy = true];

  // Group creation timestamp
  google.protobuf.Timestamp created_at = 7 [lazy = true, (buf.validate.field).required = true];

  // Group status
  gcommon.v1.common.ResourceStatus status = 8;

  // Group member count
  int32 member_count = 9;

  // Group administrator user IDs
  repeated string admin_user_ids = 10;
}
```

---

### handler_type.proto {#handler_type}

**Path**: `gcommon/v1/common/handler_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `HandlerType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handler_type.proto
// version: 1.0.1
// guid: 38fcdb5d-d9f0-4109-b909-c1da72c74948
//
// HandlerType categorizes incoming request handlers.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HandlerType {
  HANDLER_TYPE_UNSPECIFIED = 0;
  HANDLER_TYPE_HTTP = 1;
  HANDLER_TYPE_GRPC = 2;
  HANDLER_TYPE_WEBSOCKET = 3;
}
```

---

### health_check_result.proto {#health_check_result}

**Path**: `gcommon/v1/common/health_check_result.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `HealthHealthCheckResult`

**Imports** (5):

- `gcommon/v1/common/check_type.proto`
- `gcommon/v1/common/component_health.proto`
- `gcommon/v1/common/serving_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_result.proto
// version: 1.0.0
// guid: f29a3085-ffb9-4d33-8e60-ee52f8ff4570

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_type.proto";
import "gcommon/v1/common/component_health.proto";
import "gcommon/v1/common/serving_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message HealthHealthCheckResult {
  // Service name being checked
  string service = 1 [(buf.validate.field).string.min_len = 1];
  // Overall status of the health check
  ServingStatus status = 2;
  // Type of health check performed
  CheckType check_type = 3;
  // Timestamp when the check was performed
  int64 timestamp = 4;
  // Duration of the check in milliseconds
  int64 duration_ms = 5 [(buf.validate.field).int64.gt = 0];
  // Human-readable message about the check result
  string message = 6 [(buf.validate.field).string.min_len = 1];
  // Error details if the check failed
  string error = 7 [(buf.validate.field).string.min_len = 1];
  // Additional metadata about the check
  map<string, string> metadata = 8;
  // Component-specific health details
  repeated ComponentHealth components = 9 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### health_check_type.proto {#health_check_type}

**Path**: `gcommon/v1/common/health_check_type.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Enums** (1): `HealthCheckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_type.proto
// version: 1.0.1
// guid: f4a5b6c7-d8e9-0f1a-2b3c-4d5e6f7a8b9c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthCheckType represents the type of health check.
 * Specifies the protocol and method used for environment health checks.
 */
enum HealthCheckType {
  // Unspecified health check type
  HEALTH_CHECK_TYPE_UNSPECIFIED = 0;

  // HTTP health check
  HEALTH_CHECK_TYPE_HTTP = 1;

  // HTTPS health check
  HEALTH_CHECK_TYPE_HTTPS = 2;

  // TCP connection health check
  HEALTH_CHECK_TYPE_TCP = 3;

  // UDP connection health check
  HEALTH_CHECK_TYPE_UDP = 4;

  // gRPC health check
  HEALTH_CHECK_TYPE_GRPC = 5;

  // Database health check
  HEALTH_CHECK_TYPE_DATABASE = 6;

  // Custom health check
  HEALTH_CHECK_TYPE_CUSTOM = 7;
}
```

---

### health_metric_data.proto {#health_metric_data}

**Path**: `gcommon/v1/common/health_metric_data.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `HealthMetricData`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_metric_data.proto
// version: 1.0.0
// guid: 2d079e14-0602-4a9a-9b6b-dc8bbf629fe8
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Individual health metric data point.
 * Represents a single metric measurement with associated metadata.
 */
message HealthMetricData {
  // Metric name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Metric value
  double value = 2;

  // Timestamp of the metric
  google.protobuf.Timestamp timestamp = 3;

  // Labels for the metric
  map<string, string> labels = 4;

  // Unit of measurement (e.g., "ms", "count", "percentage")
  string unit = 5;

  // Description of what this metric measures
  string description = 6 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### health_metrics.proto {#health_metrics}

**Path**: `gcommon/v1/common/health_metrics.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `HealthMetrics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_metrics.proto
// version: 1.0.0
// guid: 5abc1dde-0895-4d4d-b970-d9784a116f26
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Health metrics aggregation containing overall system health statistics.
 * Provides quantitative data about health check performance and system status.
 */
message HealthMetrics {
  // Total number of health checks
  int32 total_checks = 1 [(buf.validate.field).int32.gte = 0];

  // Number of healthy checks
  int32 healthy_checks = 2 [(buf.validate.field).int32.gte = 0];

  // Number of unhealthy checks
  int32 unhealthy_checks = 3 [(buf.validate.field).int32.gte = 0];

  // Number of unknown status checks
  int32 unknown_checks = 4 [(buf.validate.field).int32.gte = 0];

  // Average response time across all checks
  double average_response_time_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // Last update timestamp
  google.protobuf.Timestamp last_updated = 6;

  // System uptime
  double uptime_seconds = 7 [(buf.validate.field).double.gte = 0.0];

  // Additional custom metrics
  map<string, double> custom_metrics = 8;
}
```

---

### health_state.proto {#health_state}

**Path**: `gcommon/v1/common/health_state.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `HealthState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_state.proto
// version: 1.0.1
// guid: a5b6c7d8-e9f0-1a2b-3c4d-5e6f7a8b9c0d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthState represents the state of health.
 * Specifies the current health condition of environment components.
 */
enum HealthState {
  // Unspecified health state
  HEALTH_STATE_UNSPECIFIED = 0;

  // Component is healthy
  HEALTH_STATE_HEALTHY = 1;

  // Component is degraded but functional
  HEALTH_STATE_DEGRADED = 2;

  // Component is unhealthy
  HEALTH_STATE_UNHEALTHY = 3;

  // Health state is unknown
  HEALTH_STATE_UNKNOWN = 4;
}
```

---

### health_status.proto {#health_status}

**Path**: `gcommon/v1/common/health_status.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `CommonHealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_status.proto
// version: 1.0.1
// guid: f5b71864-058c-43b1-8500-dd1845802068
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common health status enumeration used across all GCommon modules.
 * Provides consistent health reporting for services, components, and resources.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonHealthStatus {
  // Default value indicating health status was not specified
  HEALTH_STATUS_UNSPECIFIED = 0;

  // Service/component is operating normally
  HEALTH_STATUS_HEALTHY = 1;

  // Service/component is not functioning properly
  HEALTH_STATUS_UNHEALTHY = 2;

  // Service/component is partially functioning with degraded performance
  HEALTH_STATUS_DEGRADED = 3;

  // Service/component is in the process of starting up
  HEALTH_STATUS_STARTING = 4;

  // Service/component is in the process of shutting down
  HEALTH_STATUS_STOPPING = 5;
}
```

---

### hierarchy_type.proto {#hierarchy_type}

**Path**: `gcommon/v1/common/hierarchy_type.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `HierarchyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/hierarchy_type.proto
// version: 1.0.1
// guid: 4618131c-f81c-417c-ba7a-46d3f5a9a06b
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Hierarchy type enumeration defining the type of organizational structure.
 * Used to categorize different organizational units and their relationships.
 */
enum HierarchyType {
  // Default value indicating no hierarchy type was specified
  HIERARCHY_TYPE_UNSPECIFIED = 0;

  // Department-based hierarchical structure
  HIERARCHY_TYPE_DEPARTMENT = 1;

  // Team-based organizational structure
  HIERARCHY_TYPE_TEAM = 2;

  // Project-based organizational structure
  HIERARCHY_TYPE_PROJECT = 3;

  // Geographic/location-based structure
  HIERARCHY_TYPE_GEOGRAPHIC = 4;

  // Functional role-based structure
  HIERARCHY_TYPE_FUNCTIONAL = 5;

  // Matrix organizational structure (multi-dimensional)
  HIERARCHY_TYPE_MATRIX = 6;

  // Flat organizational structure (minimal hierarchy)
  HIERARCHY_TYPE_FLAT = 7;
}
```

---

### hook_error_handling.proto {#hook_error_handling}

**Path**: `gcommon/v1/common/hook_error_handling.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `HookErrorHandling`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/hook_error_handling.proto
// version: 1.0.1
// guid: f5c075fd-6a9f-4072-bea8-ee82bb35c1b5

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HookErrorHandling {
  HOOK_ERROR_HANDLING_UNSPECIFIED = 0;
  HOOK_ERROR_HANDLING_IGNORE = 1;
  HOOK_ERROR_HANDLING_WARN = 2;
  HOOK_ERROR_HANDLING_FAIL = 3;
}
```

---

### hook_type.proto {#hook_type}

**Path**: `gcommon/v1/common/hook_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `HookType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/hook_type.proto
// version: 1.0.1
// guid: a9982046-4cf7-4320-91ff-66f4b56b6258

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HookType {
  HOOK_TYPE_UNSPECIFIED = 0;
  HOOK_TYPE_PRE_RENDER = 1;
  HOOK_TYPE_POST_RENDER = 2;
  HOOK_TYPE_PRE_APPLY = 3;
  HOOK_TYPE_POST_APPLY = 4;
  HOOK_TYPE_PRE_VALIDATE = 5;
  HOOK_TYPE_POST_VALIDATE = 6;
}
```

---

### http_method.proto {#http_method}

**Path**: `gcommon/v1/common/http_method.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `HTTPMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_method.proto
// version: 1.0.1
// guid: 91d1cc0e-2cad-460c-81e9-236116f31e05
//
// HTTPMethod enumerates supported request verbs.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HTTPMethod {
  HTTP_METHOD_UNSPECIFIED = 0;
  HTTP_METHOD_GET = 1;
  HTTP_METHOD_POST = 2;
  HTTP_METHOD_PUT = 3;
  HTTP_METHOD_DELETE = 4;
  HTTP_METHOD_PATCH = 5;
  HTTP_METHOD_OPTIONS = 6;
  HTTP_METHOD_HEAD = 7;
}
```

---

### http_status.proto {#http_status}

**Path**: `gcommon/v1/common/http_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `HTTPStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_status.proto
// version: 1.0.1
// guid: 8e7253f5-0453-42e2-b55a-336dd5c9b589
//
// HTTPStatus enumerates common response status codes.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HTTPStatus {
  HTTP_STATUS_UNSPECIFIED = 0;
  HTTP_STATUS_OK = 200;
  HTTP_STATUS_BAD_REQUEST = 400;
  HTTP_STATUS_UNAUTHORIZED = 401;
  HTTP_STATUS_FORBIDDEN = 403;
  HTTP_STATUS_NOT_FOUND = 404;
  HTTP_STATUS_INTERNAL_ERROR = 500;
}
```

---

### inheritance_strategy.proto {#inheritance_strategy}

**Path**: `gcommon/v1/common/inheritance_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `InheritanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/inheritance_strategy.proto
// version: 1.0.1
// guid: 8dc7386b-afe2-4d9d-804d-2286b8ae6cf7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum InheritanceStrategy {
  INHERITANCE_STRATEGY_UNSPECIFIED = 0;
  INHERITANCE_STRATEGY_OVERRIDE = 1;
  INHERITANCE_STRATEGY_MERGE = 2;
  INHERITANCE_STRATEGY_FALLBACK = 3;
  INHERITANCE_STRATEGY_PRIORITY = 4;
  INHERITANCE_STRATEGY_WEIGHTED = 5;
}
```

---

### int64_array.proto {#int64_array}

**Path**: `gcommon/v1/common/int64_array.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `Int64Array`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/int64_array.proto
// version: 1.0.0
// guid: 319f8be8-1a6c-4543-b1fe-14beb5e83c0c
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Int64 array wrapper for oneof usage in filter values and other contexts.
 * Required because oneof fields cannot directly contain repeated types,
 * so arrays must be wrapped in a message.
 */
message Int64Array {
  // Array of 64-bit signed integer values
  repeated int64 values = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### isolation_level.proto {#isolation_level}

**Path**: `gcommon/v1/common/isolation_level.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `OrganizationIsolationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/isolation_level.proto
// version: 1.0.1
// guid: a922822f-aac2-4d39-ab9c-546cfae195e4
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Isolation level enumeration defining the degree of tenant isolation.
 * Used in multi-tenant architectures to control data and resource separation.
 */
enum OrganizationIsolationLevel {
  // Default value indicating no isolation level was specified
  ISOLATION_LEVEL_UNSPECIFIED = 0;

  // Shared infrastructure with logical separation (lowest cost, shared resources)
  ISOLATION_LEVEL_SHARED = 1;

  // Dedicated database/schema per tenant (medium isolation)
  ISOLATION_LEVEL_DATABASE = 2;

  // Dedicated infrastructure per tenant (highest isolation)
  ISOLATION_LEVEL_INFRASTRUCTURE = 3;

  // Virtual private cloud isolation (network-level separation)
  ISOLATION_LEVEL_NETWORK = 4;

  // Physical server isolation (hardware-level separation)
  ISOLATION_LEVEL_PHYSICAL = 5;
}
```

---

### jwt_credentials.proto {#jwt_credentials}

**Path**: `gcommon/v1/common/jwt_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `JWTCredentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/jwt_credentials.proto
// version: 1.0.0
// guid: f1c445cd-2b3d-49ec-bc9e-80e3ed12e215
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * JWT (JSON Web Token) credentials for token-based authentication.
 * Supports validation of externally issued JWTs with optional issuer verification.
 */
message JWTCredentials {
  // JWT token string (header.payload.signature format)
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Expected issuer for JWT validation (optional)
  // When provided, the JWT's 'iss' claim must match this value
  string issuer = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

