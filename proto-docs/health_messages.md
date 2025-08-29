# Health Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 32
- **Messages**: 37

## Table of Contents

### Messages

- [`CheckConfig`](#check_config) - from check_config.proto
- [`CheckRegistry`](#check_registry) - from check_registry.proto
- [`ComponentHealth`](#component_health) - from component_health.proto
- [`CpuUsage`](#resource_usage) - from resource_usage.proto
- [`DependencyCheck`](#dependency_check) - from dependency_check.proto
- [`DependencyCheckRequest`](#dependency_check_request) - from dependency_check_request.proto
- [`DependencyCheckResponse`](#dependency_check_response) - from dependency_check_response.proto
- [`DependencyResult`](#dependency_result) - from dependency_result.proto
- [`DiskUsage`](#resource_usage) - from resource_usage.proto
- [`HealthCheck`](#health_check) - from health_check.proto
- [`HealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`HealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`HealthEvent`](#health_event) - from health_event.proto
- [`HealthMetrics`](#health_metrics) - from health_metrics.proto
- [`HealthResult`](#health_result) - from health_result.proto
- [`ListChecksRequest`](#list_checks_request) - from list_checks_request.proto
- [`ListChecksResponse`](#list_checks_response) - from list_checks_response.proto
- [`LivenessCheck`](#liveness_check) - from liveness_check.proto
- [`LivenessCheckRequest`](#liveness_check_request) - from liveness_check_request.proto
- [`LivenessCheckResponse`](#liveness_check_response) - from liveness_check_response.proto
- [`LivenessResult`](#liveness_result) - from liveness_result.proto
- [`MemoryUsage`](#resource_usage) - from resource_usage.proto
- [`NetworkUsage`](#resource_usage) - from resource_usage.proto
- [`ReadinessCheck`](#readiness_check) - from readiness_check.proto
- [`ReadinessCheckRequest`](#readiness_check_request) - from readiness_check_request.proto
- [`ReadinessCheckResponse`](#readiness_check_response) - from readiness_check_response.proto
- [`ReadinessResult`](#readiness_result) - from readiness_result.proto
- [`RegisterCheckRequest`](#register_check_request) - from register_check_request.proto
- [`RegisterCheckResponse`](#register_check_response) - from register_check_response.proto
- [`ResourceUsage`](#resource_usage) - from resource_usage.proto
- [`ServiceHealthMetrics`](#health_metrics) - from health_metrics.proto
- [`ServiceInfo`](#service_info) - from service_info.proto
- [`SystemMetrics`](#system_metrics) - from system_metrics.proto
- [`UnregisterCheckRequest`](#unregister_check_request) - from unregister_check_request.proto
- [`UnregisterCheckResponse`](#unregister_check_response) - from unregister_check_response.proto
- [`WatchHealthRequest`](#watch_health_request) - from watch_health_request.proto
- [`WatchHealthResponse`](#watch_health_response) - from watch_health_response.proto

### Files in this Module

- [check_registry.proto](#check_registry)
- [component_health.proto](#component_health)
- [dependency_check.proto](#dependency_check)
- [dependency_result.proto](#dependency_result)
- [health_check.proto](#health_check)
- [health_metrics.proto](#health_metrics)
- [health_result.proto](#health_result)
- [liveness_check.proto](#liveness_check)
- [liveness_result.proto](#liveness_result)
- [readiness_check.proto](#readiness_check)
- [readiness_result.proto](#readiness_result)
- [resource_usage.proto](#resource_usage)
- [system_metrics.proto](#system_metrics)
- [service_info.proto](#service_info)
- [health_event.proto](#health_event)
- [check_config.proto](#check_config)
- [dependency_check_request.proto](#dependency_check_request)
- [health_check_request.proto](#health_check_request)
- [list_checks_request.proto](#list_checks_request)
- [liveness_check_request.proto](#liveness_check_request)
- [readiness_check_request.proto](#readiness_check_request)
- [register_check_request.proto](#register_check_request)
- [unregister_check_request.proto](#unregister_check_request)
- [watch_health_request.proto](#watch_health_request)
- [dependency_check_response.proto](#dependency_check_response)
- [health_check_response.proto](#health_check_response)
- [list_checks_response.proto](#list_checks_response)
- [liveness_check_response.proto](#liveness_check_response)
- [readiness_check_response.proto](#readiness_check_response)
- [register_check_response.proto](#register_check_response)
- [unregister_check_response.proto](#unregister_check_response)
- [watch_health_response.proto](#watch_health_response)

---

## Messages Documentation

### check_registry.proto {#check_registry}

**Path**: `gcommon/v1/health/messages/check_registry.proto` **Package**: `gcommon.v1.health` **Lines**: 39

**Messages** (1): `CheckRegistry`

**Imports** (3):

- `gcommon/v1/health/messages/health_check.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/check_registry.proto
// version: 1.0.0
// guid: 5d6e7f80-9ca2-7890-4567-123456789012

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/messages/health_check.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * CheckRegistry represents a registry of all health checks in the system.
 * Maintains the authoritative list of configured health checks.
 * Follows 1-1-1 pattern: one message per file.
 */
message CheckRegistry {
  // All registered health checks indexed by check ID
  map<string, HealthCheck> checks = 1;

  // Total number of registered checks
  int32 total_checks = 2;

  // Number of enabled checks
  int32 enabled_checks = 3;

  // When this registry was last updated
  google.protobuf.Timestamp last_updated = 4;

  // Registry version for optimistic locking
  int64 version = 5;

  // Services currently being monitored
  repeated string monitored_services = 6;
}
```

---

### component_health.proto {#component_health}

**Path**: `gcommon/v1/health/messages/component_health.proto` **Package**: `gcommon.v1.health` **Lines**: 57

**Messages** (1): `ComponentHealth`

**Imports** (3):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/component_health.proto
// version: 1.0.0
// guid: 3c4d5e6f-7081-9012-cdef-345678901234

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ComponentHealth represents the health status of a system component.
 * Used for aggregating health information across multiple checks.
 * Follows 1-1-1 pattern: one message per file.
 */
message ComponentHealth {
  // Component name or identifier
  string component_name = 1;

  // Overall health status of the component
  HealthStatus status = 2;

  // Human-readable status description
  string description = 3;

  // When this component's health was last updated
  google.protobuf.Timestamp last_updated = 4;

  // List of individual check IDs that contribute to this component's health
  repeated string check_ids = 5;

  // Number of healthy checks
  int32 healthy_checks = 6;

  // Number of unhealthy checks
  int32 unhealthy_checks = 7;

  // Total number of checks for this component
  int32 total_checks = 8;

  // Component-specific metadata
  map<string, string> metadata = 9;

  // Version of the component
  string version = 10;

  // Component dependencies
  repeated string dependencies = 11;

  // When this component was last restarted
  google.protobuf.Timestamp last_restart = 12;
}
```

---

### dependency_check.proto {#dependency_check}

**Path**: `gcommon/v1/health/messages/dependency_check.proto` **Package**: `gcommon.v1.health` **Lines**: 55

**Messages** (1): `DependencyCheck`

**Imports** (4):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/dependency_check.proto
// version: 1.0.0
// guid: 607182a3-adb4-2345-9012-678901234567

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * DependencyCheck represents a health check for external dependencies.
 * Monitors the health and availability of services this component depends on.
 * Follows 1-1-1 pattern: one message per file.
 */
message DependencyCheck {
  // Unique identifier for this dependency check
  string id = 1;

  // Name of the dependency being checked
  string dependency_name = 2;

  // Type of dependency (database, service, cache, etc.)
  string dependency_type = 3;

  // Connection string or endpoint
  string endpoint = 4;

  // Current status of the dependency
  HealthStatus status = 5;

  // How critical this dependency is (1-10, 10 being most critical)
  int32 criticality = 6;

  // Check timeout
  google.protobuf.Duration timeout = 7;

  // Check interval
  google.protobuf.Duration check_interval = 8;

  // When this dependency was last checked
  google.protobuf.Timestamp last_checked = 9;

  // When this dependency check was configured
  google.protobuf.Timestamp configured_at = 10;

  // Additional metadata about the dependency
  map<string, string> metadata = 11;
}
```

---

### dependency_result.proto {#dependency_result}

**Path**: `gcommon/v1/health/messages/dependency_result.proto` **Package**: `gcommon.v1.health` **Lines**: 49

**Messages** (1): `DependencyResult`

**Imports** (4):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/dependency_result.proto
// version: 1.0.0
// guid: 4c5d6e7f-8b91-6789-3456-012345678901

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * DependencyResult represents the result of a dependency check execution.
 * Contains detailed dependency health assessment information.
 * Follows 1-1-1 pattern: one message per file.
 */
message DependencyResult {
  // ID of the dependency check that generated this result
  string check_id = 1;

  // Name of the dependency
  string dependency_name = 2;

  // Dependency health status
  HealthStatus status = 3;

  // When this dependency check was performed
  google.protobuf.Timestamp checked_at = 4;

  // How long the dependency check took
  google.protobuf.Duration duration = 5;

  // Error message if dependency is unhealthy
  string error_message = 6;

  // Response time for the dependency
  google.protobuf.Duration response_time = 7;

  // Whether the dependency is reachable
  bool reachable = 8;

  // Additional dependency metadata
  map<string, string> details = 9;
}
```

---

### health_check.proto {#health_check}

**Path**: `gcommon/v1/health/messages/health_check.proto` **Package**: `gcommon.v1.health` **Lines**: 65

**Messages** (1): `HealthCheck`

**Imports** (5):

- `gcommon/v1/health/enums/check_type.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/health_check.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7890-abcd-123456789012

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/check_type.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthCheck represents a configuration for a health check.
 * Defines how and when a health check should be performed.
 * Follows 1-1-1 pattern: one message per file.
 */
message HealthCheck {
  // Unique identifier for this health check
  string id = 1 [(buf.validate.field).string.min_len = 1];

  // Human-readable name for the check
  string name = 2 [(buf.validate.field).string.min_len = 1];

  // Type of health check to perform
  CheckType check_type = 3;

  // Service or component name being checked
  string service_name = 4 [(buf.validate.field).string.min_len = 1];

  // Endpoint or resource to check (URL, database connection string, etc.)
  string endpoint = 5;

  // How often to perform this check
  google.protobuf.Duration interval = 6;

  // Maximum time to wait for check completion
  google.protobuf.Duration timeout = 7;

  // Number of consecutive failures before marking as unhealthy
  int32 failure_threshold = 8;

  // Number of consecutive successes before marking as healthy
  int32 success_threshold = 9;

  // Whether this check is currently enabled
  bool enabled = 10;

  // When this check was created
  google.protobuf.Timestamp created_at = 11;

  // When this check was last updated
  google.protobuf.Timestamp updated_at = 12;

  // Additional configuration for the specific check type
  map<string, string> config = 13;

  // Tags for categorizing and filtering checks
  repeated string tags = 14;
}
```

---

### health_metrics.proto {#health_metrics}

**Path**: `gcommon/v1/health/messages/health_metrics.proto` **Package**: `gcommon.v1.health` **Lines**: 73

**Messages** (2): `HealthMetrics`, `ServiceHealthMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/health_metrics.proto
// version: 1.0.0
// guid: 9a3b4c5d-d0e7-5678-2345-901234567890

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthMetrics represents aggregated health metrics and statistics.
 * Provides insight into system health trends and performance.
 * Follows 1-1-1 pattern: one message per file.
 */
message HealthMetrics {
  // When these metrics were collected
  google.protobuf.Timestamp collected_at = 1;

  // Total number of registered health checks
  int32 total_checks = 2;

  // Number of currently healthy checks
  int32 healthy_checks = 3;

  // Number of currently unhealthy checks
  int32 unhealthy_checks = 4;

  // Number of checks in unknown state
  int32 unknown_checks = 5;

  // Average check execution time in milliseconds
  double avg_check_duration_ms = 6;

  // Check success rate percentage (0-100)
  double success_rate_percent = 7;

  // Number of status changes in the last hour
  int32 status_changes_last_hour = 8;

  // Most recent check failure timestamp
  google.protobuf.Timestamp last_failure = 9;

  // System uptime percentage (0-100)
  double uptime_percent = 10;

  // Service-specific metrics
  map<string, ServiceHealthMetrics> service_metrics = 11;
}

/**
 * ServiceHealthMetrics represents health metrics for a specific service.
 */
message ServiceHealthMetrics {
  // Service name
  string service_name = 1;

  // Number of checks for this service
  int32 check_count = 2;

  // Service health score (0-100)
  int32 health_score = 3;

  // Service uptime percentage
  double uptime_percent = 4;

  // Average response time in milliseconds
  double avg_response_time_ms = 5;
}
```

---

### health_result.proto {#health_result}

**Path**: `gcommon/v1/health/messages/health_result.proto` **Package**: `gcommon.v1.health` **Lines**: 58

**Messages** (1): `HealthResult`

**Imports** (4):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/health_result.proto
// version: 1.0.0
// guid: 2b3c4d5e-6f70-8901-bcde-234567890123

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthResult represents the result of a health check execution.
 * Contains status, timing, and diagnostic information.
 * Follows 1-1-1 pattern: one message per file.
 */
message HealthResult {
  // ID of the health check that generated this result
  string check_id = 1;

  // Current health status
  HealthStatus status = 2;

  // When this check was performed
  google.protobuf.Timestamp checked_at = 3;

  // How long the check took to complete
  google.protobuf.Duration duration = 4;

  // Human-readable status message
  string message = 5;

  // Detailed error information if check failed
  string error = 6;

  // Additional diagnostic data
  map<string, string> details = 7;

  // Sequence number for this check result
  int64 sequence = 8;

  // Whether this result represents a status change
  bool status_changed = 9;

  // Previous status before this check (if status_changed is true)
  HealthStatus previous_status = 10;

  // Number of consecutive results with the same status
  int32 consecutive_count = 11;

  // Performance metrics for the check
  map<string, double> metrics = 12;
}
```

---

### liveness_check.proto {#liveness_check}

**Path**: `gcommon/v1/health/messages/liveness_check.proto` **Package**: `gcommon.v1.health` **Lines**: 48

**Messages** (1): `LivenessCheck`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/liveness_check.proto
// version: 1.0.0
// guid: 5f607182-9ca3-1234-8901-567890123456

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * LivenessCheck represents a liveness check configuration.
 * Defines criteria for determining if a service is alive and responsive.
 * Follows 1-1-1 pattern: one message per file.
 */
message LivenessCheck {
  // Unique identifier for this liveness check
  string id = 1;

  // Service name this check applies to
  string service_name = 2;

  // Probe endpoint or method
  string probe_endpoint = 3;

  // Check interval
  google.protobuf.Duration interval = 4;

  // Timeout for each check
  google.protobuf.Duration timeout = 5;

  // Number of failures before considering service dead
  int32 failure_threshold = 6;

  // Initial delay before starting checks
  google.protobuf.Duration initial_delay = 7;

  // When this check was created
  google.protobuf.Timestamp created_at = 8;

  // Whether this check is currently active
  bool active = 9;
}
```

---

### liveness_result.proto {#liveness_result}

**Path**: `gcommon/v1/health/messages/liveness_result.proto` **Package**: `gcommon.v1.health` **Lines**: 46

**Messages** (1): `LivenessResult`

**Imports** (4):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/liveness_result.proto
// version: 1.0.0
// guid: 3b4c5d6e-7a80-5678-2345-901234567890

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * LivenessResult represents the result of a liveness check execution.
 * Contains detailed liveness assessment information.
 * Follows 1-1-1 pattern: one message per file.
 */
message LivenessResult {
  // ID of the liveness check that generated this result
  string check_id = 1;

  // Liveness status
  HealthStatus status = 2;

  // Whether the service is alive
  bool alive = 3;

  // When this liveness check was performed
  google.protobuf.Timestamp checked_at = 4;

  // How long the liveness check took
  google.protobuf.Duration duration = 5;

  // Uptime since last restart
  google.protobuf.Timestamp started_at = 6;

  // Response message from the liveness probe
  string response_message = 7;

  // Additional liveness details
  map<string, string> details = 8;
}
```

---

### readiness_check.proto {#readiness_check}

**Path**: `gcommon/v1/health/messages/readiness_check.proto` **Package**: `gcommon.v1.health` **Lines**: 46

**Messages** (1): `ReadinessCheck`

**Imports** (4):

- `gcommon/v1/health/enums/check_type.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/readiness_check.proto
// version: 1.0.0
// guid: 4e5f6071-8b92-0123-7890-456789012345

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/check_type.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ReadinessCheck represents a readiness check configuration.
 * Defines criteria for determining if a service is ready to handle requests.
 * Follows 1-1-1 pattern: one message per file.
 */
message ReadinessCheck {
  // Unique identifier for this readiness check
  string id = 1;

  // Service name this check applies to
  string service_name = 2;

  // Dependencies that must be ready
  repeated string dependencies = 3;

  // Minimum required health score (0-100)
  int32 min_health_score = 4;

  // Maximum acceptable response time
  google.protobuf.Duration max_response_time = 5;

  // Grace period after startup before checks begin
  google.protobuf.Duration startup_grace_period = 6;

  // When this check was last modified
  google.protobuf.Timestamp updated_at = 7;

  // Whether this check is currently enabled
  bool enabled = 8;
}
```

---

### readiness_result.proto {#readiness_result}

**Path**: `gcommon/v1/health/messages/readiness_result.proto` **Package**: `gcommon.v1.health` **Lines**: 49

**Messages** (1): `ReadinessResult`

**Imports** (4):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/readiness_result.proto
// version: 1.0.0
// guid: 2a3b4c5d-697f-4567-1234-890123456789

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ReadinessResult represents the result of a readiness check execution.
 * Contains detailed readiness assessment information.
 * Follows 1-1-1 pattern: one message per file.
 */
message ReadinessResult {
  // ID of the readiness check that generated this result
  string check_id = 1;

  // Readiness status
  HealthStatus status = 2;

  // Whether the service is ready
  bool ready = 3;

  // When this readiness check was performed
  google.protobuf.Timestamp checked_at = 4;

  // How long the readiness check took
  google.protobuf.Duration duration = 5;

  // Reason if not ready
  string reason = 6;

  // Health score (0-100)
  int32 health_score = 7;

  // Dependency readiness status
  map<string, bool> dependency_readiness = 8;

  // Additional readiness details
  map<string, string> details = 9;
}
```

---

### resource_usage.proto {#resource_usage}

**Path**: `gcommon/v1/health/messages/resource_usage.proto` **Package**: `gcommon.v1.health` **Lines**: 94

**Messages** (5): `ResourceUsage`, `CpuUsage`, `MemoryUsage`, `DiskUsage`, `NetworkUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/resource_usage.proto
// version: 1.0.0
// guid: 6e7f8091-adb3-8901-5678-234567890123

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ResourceUsage represents resource consumption metrics for health monitoring.
 * Tracks system resource utilization for capacity planning and health assessment.
 * Follows 1-1-1 pattern: one message per file.
 */
message ResourceUsage {
  // When these metrics were collected
  google.protobuf.Timestamp collected_at = 1;

  // Service or component name
  string component_name = 2;

  // CPU usage metrics
  CpuUsage cpu = 3;

  // Memory usage metrics
  MemoryUsage memory = 4;

  // Disk usage metrics
  DiskUsage disk = 5;

  // Network usage metrics
  NetworkUsage network = 6;
}

/**
 * CpuUsage represents CPU utilization metrics.
 */
message CpuUsage {
  // CPU usage percentage (0-100)
  double usage_percent = 1;

  // Number of CPU cores
  int32 cores = 2;

  // Load average
  double load_average = 3;
}

/**
 * MemoryUsage represents memory utilization metrics.
 */
message MemoryUsage {
  // Used memory in bytes
  int64 used_bytes = 1;

  // Total available memory in bytes
  int64 total_bytes = 2;

  // Usage percentage (0-100)
  double usage_percent = 3;
}

/**
 * DiskUsage represents disk utilization metrics.
 */
message DiskUsage {
  // Used disk space in bytes
  int64 used_bytes = 1;

  // Total disk space in bytes
  int64 total_bytes = 2;

  // Usage percentage (0-100)
  double usage_percent = 3;
}

/**
 * NetworkUsage represents network utilization metrics.
 */
message NetworkUsage {
  // Bytes received
  int64 bytes_received = 1;

  // Bytes sent
  int64 bytes_sent = 2;

  // Active connections
  int32 active_connections = 3;
}
```

---

### system_metrics.proto {#system_metrics}

**Path**: `gcommon/v1/health/messages/system_metrics.proto` **Package**: `gcommon.v1.health` **Lines**: 62

**Messages** (1): `SystemMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/system_metrics.proto
// version: 1.0.0
// guid: 1b2c3d4e-5869-7890-4567-123456789012

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * SystemMetrics represents system-level performance and resource metrics.
 * Used for health monitoring and capacity planning.
 * Follows 1-1-1 pattern: one message per file.
 */
message SystemMetrics {
  // When these metrics were collected
  google.protobuf.Timestamp collected_at = 1;

  // CPU usage percentage (0-100)
  double cpu_usage_percent = 2;

  // Memory usage in bytes
  int64 memory_used_bytes = 3;

  // Total available memory in bytes
  int64 memory_total_bytes = 4;

  // Disk usage in bytes
  int64 disk_used_bytes = 5;

  // Total disk space in bytes
  int64 disk_total_bytes = 6;

  // Network bytes received
  int64 network_bytes_received = 7;

  // Network bytes sent
  int64 network_bytes_sent = 8;

  // Number of active connections
  int32 active_connections = 9;

  // System load average (1 minute)
  double load_average_1m = 10;

  // System load average (5 minutes)
  double load_average_5m = 11;

  // System load average (15 minutes)
  double load_average_15m = 12;

  // Process count
  int32 process_count = 13;

  // Uptime in seconds
  int64 uptime_seconds = 14;
}
```

---

### service_info.proto {#service_info}

**Path**: `gcommon/v1/health/messages/service_info.proto` **Package**: `gcommon.v1.health` **Lines**: 57

**Messages** (1): `ServiceInfo`

**Imports** (3):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/service_info.proto
// version: 1.0.0
// guid: a3b4c5d6-e1f8-6789-3456-012345678901

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ServiceInfo represents information about a monitored service.
 * Contains metadata and current status for health monitoring.
 * Follows 1-1-1 pattern: one message per file.
 */
message ServiceInfo {
  // Service name
  string name = 1;

  // Service version
  string version = 2;

  // Current overall health status
  HealthStatus status = 3;

  // Service description
  string description = 4;

  // When this service was registered for monitoring
  google.protobuf.Timestamp registered_at = 5;

  // When the service was last updated
  google.protobuf.Timestamp last_updated = 6;

  // Service endpoints
  repeated string endpoints = 7;

  // Service tags for categorization
  repeated string tags = 8;

  // Service metadata
  map<string, string> metadata = 9;

  // Health check IDs associated with this service
  repeated string check_ids = 10;

  // Whether this service is currently being monitored
  bool monitoring_enabled = 11;

  // Service owner or team
  string owner = 12;
}
```

---

### health_event.proto {#health_event}

**Path**: `gcommon/v1/health/messages/health_event.proto` **Package**: `gcommon.v1.health` **Lines**: 54

**Messages** (1): `HealthEvent`

**Imports** (3):

- `gcommon/v1/health/enums/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/health_event.proto
// version: 1.0.0
// guid: 82a3b4c5-cfd6-4567-1234-890123456789

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthEvent represents a significant health-related event.
 * Used for notifications, alerts, and audit trails.
 * Follows 1-1-1 pattern: one message per file.
 */
message HealthEvent {
  // Unique identifier for this event
  string event_id = 1;

  // Type of event (status_change, check_failure, recovery, etc.)
  string event_type = 2;

  // Service or component this event relates to
  string service_name = 3;

  // Check ID that generated this event (if applicable)
  string check_id = 4;

  // Event timestamp
  google.protobuf.Timestamp timestamp = 5;

  // Previous status (for status change events)
  HealthStatus previous_status = 6;

  // Current status
  HealthStatus current_status = 7;

  // Human-readable event message
  string message = 8;

  // Event severity level (info, warning, error, critical)
  string severity = 9;

  // Additional event metadata
  map<string, string> metadata = 10;

  // Source that generated this event
  string source = 11;
}
```

---

### check_config.proto {#check_config}

**Path**: `gcommon/v1/health/messages/check_config.proto` **Package**: `gcommon.v1.health` **Lines**: 50

**Messages** (1): `CheckConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/messages/check_config.proto
// version: 1.0.0
// guid: 7182a3b4-bec5-3456-0123-789012345678

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * CheckConfig represents global configuration for health checks.
 * Defines default behaviors and system-wide health check settings.
 * Follows 1-1-1 pattern: one message per file.
 */
message CheckConfig {
  // Default check interval for new health checks
  google.protobuf.Duration default_interval = 1;

  // Default timeout for health checks
  google.protobuf.Duration default_timeout = 2;

  // Default failure threshold before marking unhealthy
  int32 default_failure_threshold = 3;

  // Default success threshold before marking healthy
  int32 default_success_threshold = 4;

  // Whether to enable health check metrics collection
  bool enable_metrics = 5;

  // Whether to enable health check logging
  bool enable_logging = 6;

  // Maximum number of concurrent health checks
  int32 max_concurrent_checks = 7;

  // Global tags to apply to all health checks
  repeated string global_tags = 8;

  // Health check result retention period
  google.protobuf.Duration retention_period = 9;

  // Whether to automatically retry failed checks
  bool auto_retry = 10;
}
```

---

### dependency_check_request.proto {#dependency_check_request}

**Path**: `gcommon/v1/health/requests/dependency_check_request.proto` **Package**: `gcommon.v1.health` **Lines**: 39

**Messages** (1): `DependencyCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/dependency_check_request.proto
// version: 1.0.0
// guid: b4c5d6e7-f209-7890-4567-123456789012

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * DependencyCheckRequest requests a check of external dependencies.
 * Verifies connectivity and health of services this component depends on.
 * Follows 1-1-1 pattern: one message per file.
 */
message DependencyCheckRequest {
  // Service name to check dependencies for
  string service_name = 1;

  // Specific dependency to check (optional, checks all if empty)
  string dependency_name = 2;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 3;

  // Maximum time to wait for dependency checks
  google.protobuf.Duration timeout = 4;

  // Include only critical dependencies
  bool critical_only = 5;

  // Minimum criticality level to include (1-10)
  int32 min_criticality = 6;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/health/requests/health_check_request.proto` **Package**: `gcommon.v1.health` **Lines**: 46

**Messages** (1): `HealthCheckRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/health_check_request.proto
// version: 1.0.0
// guid: 4d5e6f70-8192-0123-def0-456789012345

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthCheckRequest requests a health check for a specific service or component.
 * Can be used for on-demand health verification.
 * Follows 1-1-1 pattern: one message per file.
 */
message HealthCheckRequest {
  // Service name to check (empty for overall system health)
  string service_name = 1;

  // Component name within the service (optional)
  string component_name = 2;

  // Specific check ID to execute (optional, defaults to all checks for service)
  string check_id = 3;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Maximum time to wait for the check to complete
  google.protobuf.Duration timeout = 5;

  // Whether to include detailed diagnostic information in the response
  bool include_details = 6;

  // Whether to force a fresh check (bypass cache)
  bool force_refresh = 7;

  // Tags to filter which checks to run
  repeated string tags = 8;
}
```

---

### list_checks_request.proto {#list_checks_request}

**Path**: `gcommon/v1/health/requests/list_checks_request.proto` **Package**: `gcommon.v1.health` **Lines**: 41

**Messages** (1): `ListChecksRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/list_checks_request.proto
// version: 1.0.0
// guid: f809192a-364c-1234-8901-567890123456

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ListChecksRequest requests a list of registered health checks.
 * Supports filtering and pagination.
 * Follows 1-1-1 pattern: one message per file.
 */
message ListChecksRequest {
  // Filter by service name (optional)
  string service_name = 1;

  // Filter by check type (optional)
  string check_type = 2;

  // Filter by tags (optional)
  repeated string tags = 3;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Include only enabled checks
  bool enabled_only = 5;

  // Maximum number of results to return
  int32 limit = 6;

  // Pagination offset
  int32 offset = 7;
}
```

---

### liveness_check_request.proto {#liveness_check_request}

**Path**: `gcommon/v1/health/requests/liveness_check_request.proto` **Package**: `gcommon.v1.health` **Lines**: 33

**Messages** (1): `LivenessCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/liveness_check_request.proto
// version: 1.0.0
// guid: 920a1b2c-3647-5678-2345-901234567890

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * LivenessCheckRequest requests a liveness check for a service.
 * Liveness checks verify that a service is alive and responsive.
 * Follows 1-1-1 pattern: one message per file.
 */
message LivenessCheckRequest {
  // Service name to check liveness for
  string service_name = 1;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 2;

  // Maximum time to wait for the liveness check
  google.protobuf.Duration timeout = 3;

  // Specific probe endpoint to check (optional)
  string probe_endpoint = 4;
}
```

---

### readiness_check_request.proto {#readiness_check_request}

**Path**: `gcommon/v1/health/requests/readiness_check_request.proto` **Package**: `gcommon.v1.health` **Lines**: 36

**Messages** (1): `ReadinessCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/readiness_check_request.proto
// version: 1.0.0
// guid: 5e6f7081-9203-1234-ef01-567890123456

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ReadinessCheckRequest requests a readiness check for a service.
 * Readiness checks verify that a service is ready to handle requests.
 * Follows 1-1-1 pattern: one message per file.
 */
message ReadinessCheckRequest {
  // Service name to check readiness for
  string service_name = 1;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 2;

  // Maximum time to wait for the readiness check
  google.protobuf.Duration timeout = 3;

  // Include dependency readiness checks
  bool include_dependencies = 4;

  // Minimum required health score (0-100) to consider ready
  int32 min_health_score = 5;
}
```

---

### register_check_request.proto {#register_check_request}

**Path**: `gcommon/v1/health/requests/register_check_request.proto` **Package**: `gcommon.v1.health` **Lines**: 30

**Messages** (1): `RegisterCheckRequest`

**Imports** (3):

- `gcommon/v1/health/messages/health_check.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/register_check_request.proto
// version: 1.0.0
// guid: 2c3d4e5f-6970-8901-5678-234567890123

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/messages/health_check.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * RegisterCheckRequest registers a new health check with the system.
 * Allows dynamic addition of health checks at runtime.
 * Follows 1-1-1 pattern: one message per file.
 */
message RegisterCheckRequest {
  // Health check configuration to register
  HealthCheck health_check = 1;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 2;

  // Whether to replace existing check with same ID
  bool replace_existing = 3;
}
```

---

### unregister_check_request.proto {#unregister_check_request}

**Path**: `gcommon/v1/health/requests/unregister_check_request.proto` **Package**: `gcommon.v1.health` **Lines**: 29

**Messages** (1): `UnregisterCheckRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/unregister_check_request.proto
// version: 1.0.0
// guid: d6e7f809-142a-9012-6789-345678901234

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * UnregisterCheckRequest removes a health check from the system.
 * Allows dynamic removal of health checks at runtime.
 * Follows 1-1-1 pattern: one message per file.
 */
message UnregisterCheckRequest {
  // ID of the health check to unregister
  string check_id = 1;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 2;

  // Whether to force removal even if check is running
  bool force = 3;
}
```

---

### watch_health_request.proto {#watch_health_request}

**Path**: `gcommon/v1/health/requests/watch_health_request.proto` **Package**: `gcommon.v1.health` **Lines**: 35

**Messages** (1): `WatchHealthRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/requests/watch_health_request.proto
// version: 1.0.0
// guid: 7f809192-bec4-9012-6789-345678901234

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * WatchHealthRequest requests a stream of health status updates.
 * Allows real-time monitoring of health check results.
 * Follows 1-1-1 pattern: one message per file.
 */
message WatchHealthRequest {
  // Service name to watch (empty for all services)
  string service_name = 1;

  // Specific check ID to watch (optional)
  string check_id = 2;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 3;

  // Only send updates for status changes
  bool status_changes_only = 4;

  // Filter by tags
  repeated string tags = 5;
}
```

---

### dependency_check_response.proto {#dependency_check_response}

**Path**: `gcommon/v1/health/responses/dependency_check_response.proto` **Package**: `gcommon.v1.health` **Lines**: 39

**Messages** (1): `DependencyCheckResponse`

**Imports** (3):

- `gcommon/v1/health/messages/dependency_check.proto`
- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/dependency_check_response.proto
// version: 1.0.0
// guid: c5d6e7f8-0319-8901-5678-234567890123

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/messages/dependency_check.proto";
import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * DependencyCheckResponse returns the results of dependency health checks.
 * Contains status and details for all checked dependencies.
 * Follows 1-1-1 pattern: one message per file.
 */
message DependencyCheckResponse {
  // Results for each dependency checked
  repeated DependencyCheck dependencies = 1;

  // Overall dependency health status
  bool all_dependencies_healthy = 2;

  // Number of healthy dependencies
  int32 healthy_count = 3;

  // Number of unhealthy dependencies
  int32 unhealthy_count = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;

  // Any issues encountered during checks
  repeated string issues = 6;
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/health/responses/health_check_response.proto` **Package**: `gcommon.v1.health` **Lines**: 45

**Messages** (1): `HealthCheckResponse`

**Imports** (3):

- `gcommon/v1/health/messages/health_result.proto`
- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/health_check_response.proto
// version: 1.0.0
// guid: 6f708192-0314-2345-f012-678901234567

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/messages/health_result.proto";
import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthCheckResponse returns the result of a health check request.
 * Contains health status and diagnostic information.
 * Follows 1-1-1 pattern: one message per file.
 */
message HealthCheckResponse {
  // Results of the health checks performed
  repeated HealthResult results = 1;

  // Overall health summary
  string summary = 2;

  // Total number of checks performed
  int32 total_checks = 3;

  // Number of healthy checks
  int32 healthy_checks = 4;

  // Number of unhealthy checks
  int32 unhealthy_checks = 5;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 6;

  // Whether all requested checks completed successfully
  bool all_checks_completed = 7;

  // Any warnings or notices about the health check process
  repeated string warnings = 8;
}
```

---

### list_checks_response.proto {#list_checks_response}

**Path**: `gcommon/v1/health/responses/list_checks_response.proto` **Package**: `gcommon.v1.health` **Lines**: 30

**Messages** (1): `ListChecksResponse`

**Imports** (3):

- `gcommon/v1/health/messages/health_check.proto`
- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/list_checks_response.proto
// version: 1.0.0
// guid: 09192a3b-475d-2345-9012-678901234567

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/messages/health_check.proto";
import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ListChecksResponse returns a list of registered health checks.
 * Contains health check configurations and metadata.
 * Follows 1-1-1 pattern: one message per file.
 */
message ListChecksResponse {
  // List of health checks
  repeated HealthCheck checks = 1;

  // Total number of checks available (for pagination)
  int32 total_count = 2;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### liveness_check_response.proto {#liveness_check_response}

**Path**: `gcommon/v1/health/responses/liveness_check_response.proto` **Package**: `gcommon.v1.health` **Lines**: 37

**Messages** (1): `LivenessCheckResponse`

**Imports** (4):

- `gcommon/v1/health/enums/health_status.proto`
- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/liveness_check_response.proto
// version: 1.0.0
// guid: 0a1b2c3d-4758-6789-3456-012345678901

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * LivenessCheckResponse returns the result of a liveness check.
 * Indicates whether a service is alive and responsive.
 * Follows 1-1-1 pattern: one message per file.
 */
message LivenessCheckResponse {
  // Overall liveness status
  HealthStatus status = 1;

  // Whether the service is alive
  bool alive = 2;

  // Uptime since last restart
  google.protobuf.Timestamp started_at = 3;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 4;

  // Additional liveness details
  string details = 5;
}
```

---

### readiness_check_response.proto {#readiness_check_response}

**Path**: `gcommon/v1/health/responses/readiness_check_response.proto` **Package**: `gcommon.v1.health` **Lines**: 42

**Messages** (1): `ReadinessCheckResponse`

**Imports** (3):

- `gcommon/v1/health/enums/health_status.proto`
- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/readiness_check_response.proto
// version: 1.0.0
// guid: 7081920a-1425-3456-0123-789012345678

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/enums/health_status.proto";
import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * ReadinessCheckResponse returns the result of a readiness check.
 * Indicates whether a service is ready to handle requests.
 * Follows 1-1-1 pattern: one message per file.
 */
message ReadinessCheckResponse {
  // Overall readiness status
  HealthStatus status = 1;

  // Whether the service is ready to handle requests
  bool ready = 2;

  // Reason if not ready
  string reason = 3;

  // Health score (0-100)
  int32 health_score = 4;

  // Dependency readiness status
  map<string, HealthStatus> dependency_status = 5;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 6;

  // Additional readiness details
  map<string, string> details = 7;
}
```

---

### register_check_response.proto {#register_check_response}

**Path**: `gcommon/v1/health/responses/register_check_response.proto` **Package**: `gcommon.v1.health` **Lines**: 35

**Messages** (1): `RegisterCheckResponse`

**Imports** (2):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/register_check_response.proto
// version: 1.0.0
// guid: 3d4e5f60-7a81-9012-6789-345678901234

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * RegisterCheckResponse confirms registration of a health check.
 * Returns success status and any relevant information.
 * Follows 1-1-1 pattern: one message per file.
 */
message RegisterCheckResponse {
  // Whether the registration was successful
  bool success = 1;

  // The ID assigned to the registered check
  string check_id = 2;

  // Human-readable message about the registration
  string message = 3;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 4;

  // Any warnings about the registration
  repeated string warnings = 5;
}
```

---

### unregister_check_response.proto {#unregister_check_response}

**Path**: `gcommon/v1/health/responses/unregister_check_response.proto` **Package**: `gcommon.v1.health` **Lines**: 29

**Messages** (1): `UnregisterCheckResponse`

**Imports** (2):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/unregister_check_response.proto
// version: 1.0.0
// guid: e7f8091a-253b-0123-7890-456789012345

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * UnregisterCheckResponse confirms removal of a health check.
 * Returns success status and any relevant information.
 * Follows 1-1-1 pattern: one message per file.
 */
message UnregisterCheckResponse {
  // Whether the unregistration was successful
  bool success = 1;

  // Human-readable message about the unregistration
  string message = 2;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### watch_health_response.proto {#watch_health_response}

**Path**: `gcommon/v1/health/responses/watch_health_response.proto` **Package**: `gcommon.v1.health` **Lines**: 34

**Messages** (1): `WatchHealthResponse`

**Imports** (4):

- `gcommon/v1/health/messages/health_result.proto`
- `gcommon/v1/health/messages/health_event.proto`
- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/responses/watch_health_response.proto
// version: 1.0.0
// guid: 80919203-cfd5-0123-7890-456789012345

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/messages/health_result.proto";
import "gcommon/v1/health/messages/health_event.proto";
import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * WatchHealthResponse streams health status updates.
 * Provides real-time health monitoring data.
 * Follows 1-1-1 pattern: one message per file.
 */
message WatchHealthResponse {
  // Type of update (result, event, heartbeat)
  string update_type = 1;

  // Health check result (for result updates)
  HealthResult result = 2;

  // Health event (for event updates)
  HealthEvent event = 3;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 4;
}
```

---
