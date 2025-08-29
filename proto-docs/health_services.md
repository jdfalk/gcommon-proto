# Health Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 2
- **Services**: 2

## Table of Contents

### Services

- [`HealthCheckService`](#health_check_service) - from health_check_service.proto
- [`HealthService`](#health_service) - from health_service.proto

### Files in this Module

- [health_check_service.proto](#health_check_service)
- [health_service.proto](#health_service)

---

## Services Documentation

### health_check_service.proto {#health_check_service}

**Path**: `gcommon/v1/health/services/health_check_service.proto` **Package**: `gcommon.v1.health` **Lines**: 39

**Services** (1): `HealthCheckService`

**Imports** (9):

- `gcommon/v1/health/requests/dependency_check_request.proto`
- `gcommon/v1/health/requests/list_checks_request.proto`
- `gcommon/v1/health/requests/register_check_request.proto`
- `gcommon/v1/health/requests/unregister_check_request.proto`
- `gcommon/v1/health/responses/dependency_check_response.proto`
- `gcommon/v1/health/responses/list_checks_response.proto`
- `gcommon/v1/health/responses/register_check_response.proto`
- `gcommon/v1/health/responses/unregister_check_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/services/health_check_service.proto
// version: 1.0.0
// guid: 192a3b4c-586e-3456-0123-789012345678

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/requests/dependency_check_request.proto";
import "gcommon/v1/health/requests/list_checks_request.proto";
import "gcommon/v1/health/requests/register_check_request.proto";
import "gcommon/v1/health/requests/unregister_check_request.proto";
import "gcommon/v1/health/responses/dependency_check_response.proto";
import "gcommon/v1/health/responses/list_checks_response.proto";
import "gcommon/v1/health/responses/register_check_response.proto";
import "gcommon/v1/health/responses/unregister_check_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthCheckService provides health check management capabilities.
 * Allows registration, configuration, and management of health checks.
 * Follows 1-1-1 pattern: one service per file.
 */
service HealthCheckService {
  // RegisterCheck registers a new health check
  rpc RegisterCheck(RegisterCheckRequest) returns (RegisterCheckResponse);

  // UnregisterCheck removes a health check
  rpc UnregisterCheck(UnregisterCheckRequest) returns (UnregisterCheckResponse);

  // ListChecks returns all registered health checks
  rpc ListChecks(ListChecksRequest) returns (ListChecksResponse);

  // CheckDependencies verifies external dependencies
  rpc CheckDependencies(DependencyCheckRequest) returns (DependencyCheckResponse);
}
```

---

### health_service.proto {#health_service}

**Path**: `gcommon/v1/health/services/health_service.proto` **Package**: `gcommon.v1.health` **Lines**: 34

**Services** (1): `HealthService`

**Imports** (7):

- `gcommon/v1/health/requests/health_check_request.proto`
- `gcommon/v1/health/requests/readiness_check_request.proto`
- `gcommon/v1/health/requests/watch_health_request.proto`
- `gcommon/v1/health/responses/health_check_response.proto`
- `gcommon/v1/health/responses/readiness_check_response.proto`
- `gcommon/v1/health/responses/watch_health_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/services/health_service.proto
// version: 1.0.0
// guid: 8192031a-2536-4567-1234-890123456789

edition = "2023";

package gcommon.v1.health;

import "gcommon/v1/health/requests/health_check_request.proto";
import "gcommon/v1/health/requests/readiness_check_request.proto";
import "gcommon/v1/health/requests/watch_health_request.proto";
import "gcommon/v1/health/responses/health_check_response.proto";
import "gcommon/v1/health/responses/readiness_check_response.proto";
import "gcommon/v1/health/responses/watch_health_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * HealthService provides health checking capabilities for services and components.
 * Supports various types of health checks including basic health, readiness, and liveness.
 * Follows 1-1-1 pattern: one service per file.
 */
service HealthService {
  // Check performs a health check for a specific service or component
  rpc Check(HealthCheckRequest) returns (HealthCheckResponse);

  // CheckReadiness verifies if a service is ready to handle requests
  rpc CheckReadiness(ReadinessCheckRequest) returns (ReadinessCheckResponse);

  // WatchHealth returns a stream of health check results
  rpc WatchHealth(WatchHealthRequest) returns (stream WatchHealthResponse);
}
```

---
