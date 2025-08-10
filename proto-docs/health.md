# health Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 35
- **Messages**: 33
- **Services**: 2
- **Enums**: 0

## Files in this Module

- [check_result.proto](#check_result)
- [configure_alerting_request.proto](#configure_alerting_request)
- [configure_alerting_response.proto](#configure_alerting_response)
- [disable_check_request.proto](#disable_check_request)
- [disable_check_response.proto](#disable_check_response)
- [enable_check_request.proto](#enable_check_request)
- [enable_check_response.proto](#enable_check_response)
- [get_check_status_request.proto](#get_check_status_request)
- [get_health_history_request.proto](#get_health_history_request)
- [get_health_metrics_request.proto](#get_health_metrics_request)
- [get_health_metrics_response.proto](#get_health_metrics_response)
- [get_health_request.proto](#get_health_request)
- [get_service_health_request.proto](#get_service_health_request)
- [get_service_health_response.proto](#get_service_health_response)
- [health_admin_service.proto](#health_admin_service)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [health_metric_data.proto](#health_metric_data)
- [health_metrics.proto](#health_metrics)
- [health_service.proto](#health_service)
- [list_checks_request.proto](#list_checks_request)
- [list_services_request.proto](#list_services_request)
- [list_services_response.proto](#list_services_response)
- [register_check_request.proto](#register_check_request)
- [register_check_response.proto](#register_check_response)
- [reset_health_stats_request.proto](#reset_health_stats_request)
- [reset_health_stats_response.proto](#reset_health_stats_response)
- [run_check_request.proto](#run_check_request)
- [run_check_response.proto](#run_check_response)
- [set_health_request.proto](#set_health_request)
- [set_health_response.proto](#set_health_response)
- [unregister_check_request.proto](#unregister_check_request)
- [unregister_check_response.proto](#unregister_check_response)
- [watch_request.proto](#watch_request)
- [watch_response.proto](#watch_response)

## Module Dependencies

**This module depends on**:

- [auth_api_2](./auth_api_2.md)
- [cache_api_1](./cache_api_1.md)
- [cache_api_2](./cache_api_2.md)
- [common](./common.md)
- [config_api](./config_api.md)
- [database_api](./database_api.md)
- [metrics_1](./metrics_1.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_1](./queue_1.md)
- [queue_api_2](./queue_api_2.md)
- [web](./web.md)
- [web_api_2](./web_api_2.md)

**Modules that depend on this one**:

- [config_services](./config_services.md)
- [database_services](./database_services.md)

---

## Detailed Documentation

### check_result.proto {#check_result}

**Path**: `pkg/health/proto/check_result.proto` **Package**: `gcommon.v1.health`
**Lines**: 41

**Messages** (1): `CheckResult`

**Imports** (5):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/health/proto/messages/check_result.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Individual health check result for a specific component or subsystem.
 * Provides detailed information about the health status of a single check.
 */
message CheckResult {
  // Check name or identifier
  string name = 1;

  // Health status of this specific check
  gcommon.v1.common.HealthStatus status = 2;

  // Check execution timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Time taken to execute this check
  google.protobuf.Duration execution_time = 4;

  // Human-readable message about the check result
  string message = 5;

  // Error details if the check failed
  gcommon.v1.common.Error error = 6;

  // Additional metadata for this check
  map<string, string> metadata = 7;
}

```

---

### configure_alerting_request.proto {#configure_alerting_request}

**Path**: `pkg/health/proto/configure_alerting_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 33

**Messages** (1): `ConfigureAlertingRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/configure_alerting_request.proto
// file: health/proto/requests/configure_alerting_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message ConfigureAlertingRequest {
  // Name of the service or check to configure
  string target = 1;

  // Whether alerting is enabled for this check
  bool enabled = 2;

  // Number of consecutive failures required before alerting
  int32 failure_threshold = 3;

  // Optional notification channels (email, slack, etc.)
  repeated string channels = 4;

  // Standard request metadata for tracing and auth
  gcommon.v1.common.RequestMetadata metadata = 5;
}

```

---

### configure_alerting_response.proto {#configure_alerting_response}

**Path**: `pkg/health/proto/configure_alerting_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 29

**Messages** (1): `ConfigureAlertingResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/configure_alerting_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for configuring alerting settings.
 * Contains the result of alerting configuration changes.
 */
message ConfigureAlertingResponse {
  // Success status
  bool success = 1;

  // Configuration ID
  string config_id = 2;

  // Error information if configuration failed
  gcommon.v1.common.Error error = 3;

  // Applied alerting rules
  repeated string applied_rules = 4;
}

```

---

### disable_check_request.proto {#disable_check_request}

**Path**: `pkg/health/proto/disable_check_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `DisableCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/disable_check_request.proto
// file: health/proto/requests/disable_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message DisableCheckRequest {
  // Name or ID of the check to disable
  string name = 1;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### disable_check_response.proto {#disable_check_response}

**Path**: `pkg/health/proto/disable_check_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 29

**Messages** (1): `DisableCheckResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/disable_check_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for disabling a health check.
 * Contains the result of disabling an active check.
 */
message DisableCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was disabled
  string check_id = 2;

  // Error information if disabling failed
  gcommon.v1.common.Error error = 3;

  // Reason for disabling (if provided)
  string reason = 4;
}

```

---

### enable_check_request.proto {#enable_check_request}

**Path**: `pkg/health/proto/enable_check_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `EnableCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/enable_check_request.proto
// file: health/proto/requests/enable_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message EnableCheckRequest {
  // Name or ID of the check to enable
  string name = 1;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### enable_check_response.proto {#enable_check_response}

**Path**: `pkg/health/proto/enable_check_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 29

**Messages** (1): `EnableCheckResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/enable_check_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for enabling a health check.
 * Contains the result of enabling a previously disabled check.
 */
message EnableCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was enabled
  string check_id = 2;

  // Error information if enabling failed
  gcommon.v1.common.Error error = 3;

  // Check status after enabling
  string status = 4;
}

```

---

### get_check_status_request.proto {#get_check_status_request}

**Path**: `pkg/health/proto/get_check_status_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `GetCheckStatusRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/get_check_status_request.proto
// file: health/proto/requests/get_check_status_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message GetCheckStatusRequest {
  // Name or ID of the check
  string name = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_health_history_request.proto {#get_health_history_request}

**Path**: `pkg/health/proto/get_health_history_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 31

**Messages** (1): `GetHealthHistoryRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/get_health_history_request.proto
// file: health/proto/requests/get_health_history_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message GetHealthHistoryRequest {
  // Service name to query
  string service = 1;

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

**Path**: `pkg/health/proto/get_health_metrics_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `GetHealthMetricsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/get_health_metrics_request.proto
// file: health/proto/requests/get_health_metrics_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message GetHealthMetricsRequest {
  // Service name (optional)
  string service = 1;

  // Request metadata used for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_health_metrics_response.proto {#get_health_metrics_response}

**Path**: `pkg/health/proto/get_health_metrics_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 21

**Messages** (1): `GetHealthMetricsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/health/proto/health_metric_data.proto`

#### Source Code

```protobuf
// file: pkg/health/proto/responses/get_health_metrics_response.proto

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/health/proto/health_metric_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message GetHealthMetricsResponse {
  // Health metrics data
  repeated HealthMetricData metrics = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_health_request.proto {#get_health_request}

**Path**: `pkg/health/proto/get_health_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 27

**Messages** (1): `GetHealthRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/get_health_request.proto
// file: health/proto/requests/get_health_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message GetHealthRequest {
  // Service name to query
  string service = 1;

  // Whether to include detailed check results
  bool include_details = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### get_service_health_request.proto {#get_service_health_request}

**Path**: `pkg/health/proto/get_service_health_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 23

**Messages** (1): `GetServiceHealthRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: health/proto/requests/get_service_health_request.proto
//
// Get service health request message definition
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message GetServiceHealthRequest {
  // Service name
  string service = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_service_health_response.proto {#get_service_health_response}

**Path**: `pkg/health/proto/get_service_health_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 28

**Messages** (1): `GetServiceHealthResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/get_service_health_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for service health status requests.
 * Provides health status for a specific service.
 */
message GetServiceHealthResponse {
  // Health status
  gcommon.v1.common.HealthStatus status = 1;

  // Last check timestamp
  google.protobuf.Timestamp last_check = 2;

  // Error information if unhealthy
  gcommon.v1.common.Error error = 3;
}

```

---

### health_admin_service.proto {#health_admin_service}

**Path**: `pkg/health/proto/health_admin_service.proto` **Package**:
`gcommon.v1.health` **Lines**: 50

**Services** (1): `HealthAdminService`

**Imports** (13):

- `google/protobuf/go_features.proto`
- `pkg/health/proto/configure_alerting_request.proto`
- `pkg/health/proto/configure_alerting_response.proto`
- `pkg/health/proto/disable_check_request.proto`
- `pkg/health/proto/disable_check_response.proto`
- `pkg/health/proto/enable_check_request.proto`
- `pkg/health/proto/enable_check_response.proto`
- `pkg/health/proto/reset_health_stats_request.proto`
- `pkg/health/proto/reset_health_stats_response.proto`
- `pkg/health/proto/run_check_request.proto`
- `pkg/health/proto/run_check_response.proto`
- `pkg/health/proto/set_health_request.proto`
- `pkg/health/proto/set_health_response.proto`

#### Source Code

```protobuf
// file: pkg/health/proto/services/health_admin_service.proto
// file: health/proto/services/health_admin_service.proto
//
// Administrative service definitions for health module
//
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/health/proto/configure_alerting_request.proto";
import "pkg/health/proto/configure_alerting_response.proto";
import "pkg/health/proto/disable_check_request.proto";
import "pkg/health/proto/disable_check_response.proto";
import "pkg/health/proto/enable_check_request.proto";
import "pkg/health/proto/enable_check_response.proto";
import "pkg/health/proto/reset_health_stats_request.proto";
import "pkg/health/proto/reset_health_stats_response.proto";
import "pkg/health/proto/run_check_request.proto";
import "pkg/health/proto/run_check_response.proto";
import "pkg/health/proto/set_health_request.proto";
import "pkg/health/proto/set_health_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * HealthAdminService provides administrative health operations
 * such as enabling or disabling checks and configuring alerting.
 */
service HealthAdminService {
  // Configure alerting for a check or service
  rpc ConfigureAlerting(ConfigureAlertingRequest) returns (ConfigureAlertingResponse);

  // Enable a previously disabled check
  rpc EnableCheck(EnableCheckRequest) returns (EnableCheckResponse);

  // Disable an existing check
  rpc DisableCheck(DisableCheckRequest) returns (DisableCheckResponse);

  // Manually run a health check
  rpc RunCheck(RunCheckRequest) returns (RunCheckResponse);

  // Reset stored health statistics
  rpc ResetHealthStats(ResetHealthStatsRequest) returns (ResetHealthStatsResponse);

  // Manually set the overall health status
  rpc SetHealth(SetHealthRequest) returns (SetHealthResponse);
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/health/proto/health_check_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 30

**Messages** (1): `HealthCheckRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: health/proto/requests/health_check_request.proto
//
// Health check request message definition
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message HealthCheckRequest {
  // Service name to check (empty for overall health)
  string service = 1;

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

**Path**: `pkg/health/proto/health_check_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 46

**Messages** (1): `HealthCheckResponse`

**Imports** (7):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)
- `pkg/health/proto/check_result.proto`
- `pkg/health/proto/health_metrics.proto`

#### Source Code

```protobuf
// file: pkg/health/proto/responses/health_check_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";
import "pkg/health/proto/check_result.proto";
import "pkg/health/proto/health_metrics.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for health check operations.
 * Contains comprehensive health status information including detailed results and metrics.
 */
message HealthCheckResponse {
  // Overall health status
  gcommon.v1.common.HealthStatus status = 1;

  // Service name
  string service = 2;

  // Check timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Response time
  google.protobuf.Duration response_time = 4;

  // Detailed check results
  repeated CheckResult check_results = 5;

  // Health message
  string message = 6;

  // Error information if unhealthy
  gcommon.v1.common.Error error = 7;

  // Health metrics
  HealthMetrics metrics = 8;
}

```

---

### health_metric_data.proto {#health_metric_data}

**Path**: `pkg/health/proto/health_metric_data.proto` **Package**:
`gcommon.v1.health` **Lines**: 35

**Messages** (1): `HealthMetricData`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/health/proto/messages/health_metric_data.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Individual health metric data point.
 * Represents a single metric measurement with associated metadata.
 */
message HealthMetricData {
  // Metric name
  string name = 1;

  // Metric value
  double value = 2;

  // Timestamp of the metric
  google.protobuf.Timestamp timestamp = 3;

  // Labels for the metric
  map<string, string> labels = 4;

  // Unit of measurement (e.g., "ms", "count", "percentage")
  string unit = 5;

  // Description of what this metric measures
  string description = 6;
}

```

---

### health_metrics.proto {#health_metrics}

**Path**: `pkg/health/proto/health_metrics.proto` **Package**:
`gcommon.v1.health` **Lines**: 41

**Messages** (1): `HealthMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/health/proto/messages/health_metrics.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Health metrics aggregation containing overall system health statistics.
 * Provides quantitative data about health check performance and system status.
 */
message HealthMetrics {
  // Total number of health checks
  int32 total_checks = 1;

  // Number of healthy checks
  int32 healthy_checks = 2;

  // Number of unhealthy checks
  int32 unhealthy_checks = 3;

  // Number of unknown status checks
  int32 unknown_checks = 4;

  // Average response time across all checks
  double average_response_time_ms = 5;

  // Last update timestamp
  google.protobuf.Timestamp last_updated = 6;

  // System uptime
  double uptime_seconds = 7;

  // Additional custom metrics
  map<string, double> custom_metrics = 8;
}

```

---

### health_service.proto {#health_service}

**Path**: `pkg/health/proto/health_service.proto` **Package**:
`gcommon.v1.health` **Lines**: 51

**Services** (1): `HealthService`

**Imports** (15):

- `google/protobuf/go_features.proto`
- `pkg/health/proto/get_health_metrics_request.proto`
- `pkg/health/proto/get_health_metrics_response.proto`
- `pkg/health/proto/get_service_health_request.proto`
- `pkg/health/proto/get_service_health_response.proto`
- `pkg/health/proto/health_check_request.proto` →
  [auth_api_2](./auth_api_2.md#health_check_request) →
  [cache_api_1](./cache_api_1.md#health_check_request) →
  [config_api](./config_api.md#health_check_request) →
  [database_api](./database_api.md#health_check_request) →
  [metrics_api_1](./metrics_api_1.md#health_check_request) →
  [queue_api_2](./queue_api_2.md#health_check_request) →
  [web_api_2](./web_api_2.md#health_check_request)
- `pkg/health/proto/health_check_response.proto` →
  [auth_api_2](./auth_api_2.md#health_check_response) →
  [config_api](./config_api.md#health_check_response) →
  [database_api](./database_api.md#health_check_response) →
  [metrics_api_1](./metrics_api_1.md#health_check_response) →
  [queue_api_2](./queue_api_2.md#health_check_response) →
  [web_api_2](./web_api_2.md#health_check_response)
- `pkg/health/proto/list_services_request.proto`
- `pkg/health/proto/list_services_response.proto`
- `pkg/health/proto/register_check_request.proto`
- `pkg/health/proto/register_check_response.proto`
- `pkg/health/proto/unregister_check_request.proto`
- `pkg/health/proto/unregister_check_response.proto`
- `pkg/health/proto/watch_request.proto` →
  [cache_api_2](./cache_api_2.md#watch_request)
- `pkg/health/proto/watch_response.proto`

#### Source Code

```protobuf
// file: health/proto/services/health_service.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/health/proto/get_health_metrics_request.proto";
import "pkg/health/proto/get_health_metrics_response.proto";
import "pkg/health/proto/get_service_health_request.proto";
import "pkg/health/proto/get_service_health_response.proto";
import "pkg/health/proto/health_check_request.proto";
import "pkg/health/proto/health_check_response.proto";
import "pkg/health/proto/list_services_request.proto";
import "pkg/health/proto/list_services_response.proto";
import "pkg/health/proto/register_check_request.proto";
import "pkg/health/proto/register_check_response.proto";
import "pkg/health/proto/unregister_check_request.proto";
import "pkg/health/proto/unregister_check_response.proto";
import "pkg/health/proto/watch_request.proto";
import "pkg/health/proto/watch_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * HealthService provides comprehensive health checking capabilities.
 * Supports individual check status, system-wide health, and health monitoring.
 */
service HealthService {
  // Check performs a health check for a specific service
  rpc Check(HealthCheckRequest) returns (HealthCheckResponse);

  // Watch returns a stream of health check results
  rpc Watch(WatchRequest) returns (stream WatchResponse);

  // GetServiceHealth returns health status for a service
  rpc GetServiceHealth(GetServiceHealthRequest) returns (GetServiceHealthResponse);

  // ListServices returns all monitored services
  rpc ListServices(ListServicesRequest) returns (ListServicesResponse);

  // RegisterCheck registers a new health check
  rpc RegisterCheck(RegisterCheckRequest) returns (RegisterCheckResponse);

  // UnregisterCheck removes a health check
  rpc UnregisterCheck(UnregisterCheckRequest) returns (UnregisterCheckResponse);

  // GetHealthMetrics returns health metrics and statistics
  rpc GetHealthMetrics(GetHealthMetricsRequest) returns (GetHealthMetricsResponse);
}

```

---

### list_checks_request.proto {#list_checks_request}

**Path**: `pkg/health/proto/list_checks_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `ListChecksRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/list_checks_request.proto
// file: health/proto/requests/list_checks_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message ListChecksRequest {
  // Optional service name to filter checks
  string service = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### list_services_request.proto {#list_services_request}

**Path**: `pkg/health/proto/list_services_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 20

**Messages** (1): `ListServicesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: health/proto/requests/list_services_request.proto
//
// List services request message definition
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message ListServicesRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;
}

```

---

### list_services_response.proto {#list_services_response}

**Path**: `pkg/health/proto/list_services_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 20

**Messages** (1): `ListServicesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/list_services_response.proto

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message ListServicesResponse {
  // List of service names
  repeated string services = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### register_check_request.proto {#register_check_request}

**Path**: `pkg/health/proto/register_check_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 28

**Messages** (1): `RegisterCheckRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/health/proto/health_check_request.proto` →
  [auth_api_2](./auth_api_2.md#health_check_request) →
  [cache_api_1](./cache_api_1.md#health_check_request) →
  [config_api](./config_api.md#health_check_request) →
  [database_api](./database_api.md#health_check_request) →
  [metrics_api_1](./metrics_api_1.md#health_check_request) →
  [queue_api_2](./queue_api_2.md#health_check_request) →
  [web_api_2](./web_api_2.md#health_check_request)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/register_check_request.proto
// file: health/proto/requests/register_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/health/proto/health_check_request.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message RegisterCheckRequest {
  // Service name this check belongs to
  string service = 1;

  // Parameters describing the check to execute
  HealthCheckRequest check = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### register_check_response.proto {#register_check_response}

**Path**: `pkg/health/proto/register_check_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 26

**Messages** (1): `RegisterCheckResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/register_check_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for health check registration.
 * Contains the result of registering a new health check.
 */
message RegisterCheckResponse {
  // Success status
  bool success = 1;

  // Registered check ID
  string check_id = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}

```

---

### reset_health_stats_request.proto {#reset_health_stats_request}

**Path**: `pkg/health/proto/reset_health_stats_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `ResetHealthStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/reset_health_stats_request.proto
// file: health/proto/requests/reset_health_stats_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message ResetHealthStatsRequest {
  // Service name whose stats should be reset
  string service = 1;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### reset_health_stats_response.proto {#reset_health_stats_response}

**Path**: `pkg/health/proto/reset_health_stats_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 33

**Messages** (1): `ResetHealthStatsResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/reset_health_stats_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for resetting health statistics.
 * Contains the result of clearing stored health metrics and statistics.
 */
message ResetHealthStatsResponse {
  // Success status
  bool success = 1;

  // Number of statistics entries cleared
  int32 cleared_entries = 2;

  // Reset timestamp
  google.protobuf.Timestamp reset_at = 3;

  // Error information if reset failed
  gcommon.v1.common.Error error = 4;

  // Statistics categories that were reset
  repeated string reset_categories = 5;
}

```

---

### run_check_request.proto {#run_check_request}

**Path**: `pkg/health/proto/run_check_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `RunCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/run_check_request.proto
// file: health/proto/requests/run_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message RunCheckRequest {
  // Name or ID of the check to run
  string name = 1;

  // Request metadata used for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### run_check_response.proto {#run_check_response}

**Path**: `pkg/health/proto/run_check_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 41

**Messages** (1): `RunCheckResponse`

**Imports** (5):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/run_check_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for manually running a health check.
 * Contains the result of executing a health check on demand.
 */
message RunCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was executed
  string check_id = 2;

  // Health status result
  gcommon.v1.common.HealthStatus status = 3;

  // Execution timestamp
  google.protobuf.Timestamp executed_at = 4;

  // Execution duration
  google.protobuf.Duration execution_time = 5;

  // Check result message
  string message = 6;

  // Error information if check failed
  gcommon.v1.common.Error error = 7;
}

```

---

### set_health_request.proto {#set_health_request}

**Path**: `pkg/health/proto/set_health_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 28

**Messages** (1): `SetHealthRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/set_health_request.proto
// file: health/proto/requests/set_health_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/health_status.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message SetHealthRequest {
  // Service name to update
  string service = 1;

  // Desired health status
  gcommon.v1.common.HealthStatus status = 2;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### set_health_response.proto {#set_health_response}

**Path**: `pkg/health/proto/set_health_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 37

**Messages** (1): `SetHealthResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/set_health_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for manually setting health status.
 * Contains the result of administratively setting the health status.
 */
message SetHealthResponse {
  // Success status
  bool success = 1;

  // Previous health status
  gcommon.v1.common.HealthStatus previous_status = 2;

  // New health status
  gcommon.v1.common.HealthStatus new_status = 3;

  // Timestamp when status was changed
  google.protobuf.Timestamp changed_at = 4;

  // Error information if setting failed
  gcommon.v1.common.Error error = 5;

  // Reason for the manual status change
  string reason = 6;
}

```

---

### unregister_check_request.proto {#unregister_check_request}

**Path**: `pkg/health/proto/unregister_check_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 24

**Messages** (1): `UnregisterCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/health/proto/requests/unregister_check_request.proto
// file: health/proto/requests/unregister_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message UnregisterCheckRequest {
  // ID of the check to unregister
  string check_id = 1;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### unregister_check_response.proto {#unregister_check_response}

**Path**: `pkg/health/proto/unregister_check_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 29

**Messages** (1): `UnregisterCheckResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/health/proto/responses/unregister_check_response.proto
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

/**
 * Response message for unregistering a health check.
 * Contains the result of removing a health check from the system.
 */
message UnregisterCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was unregistered
  string check_id = 2;

  // Error information if unregistration failed
  gcommon.v1.common.Error error = 3;

  // Confirmation message
  string message = 4;
}

```

---

### watch_request.proto {#watch_request}

**Path**: `pkg/health/proto/watch_request.proto` **Package**:
`gcommon.v1.health` **Lines**: 23

**Messages** (1): `WatchRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: health/proto/requests/watch_request.proto
//
// Watch request message definition for streaming health updates
//

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

message WatchRequest {
  // Service name to watch (empty for all services)
  string service = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### watch_response.proto {#watch_response}

**Path**: `pkg/health/proto/watch_response.proto` **Package**:
`gcommon.v1.health` **Lines**: 55

**Messages** (1): `WatchResponse`

**Imports** (7):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)
- `pkg/health/proto/check_result.proto`
- `pkg/health/proto/health_metrics.proto`

#### Source Code

```protobuf
// file: health/proto/responses/watch_response.proto
//
// Watch response message definition for streaming health updates
//
edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";
import "pkg/health/proto/check_result.proto";
import "pkg/health/proto/health_metrics.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/health/proto";

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
  gcommon.v1.common.HealthStatus status = 1;

  // Service name
  string service = 2;

  // Check timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Response time
  google.protobuf.Duration response_time = 4;

  // Detailed check results
  repeated CheckResult check_results = 5;

  // Health message
  string message = 6;

  // Error information if unhealthy
  gcommon.v1.common.Error error = 7;

  // Health metrics
  HealthMetrics metrics = 8;
}

```

---
