# Health Enums Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 2
- **Enums**: 2

## Table of Contents

### Enums

- [`CheckType`](#check_type) - from check_type.proto
- [`HealthStatus`](#health_status) - from health_status.proto

### Files in this Module

- [check_type.proto](#check_type)
- [health_status.proto](#health_status)

---


## Enums Documentation

### check_type.proto {#check_type}

**Path**: `gcommon/v1/health/enums/check_type.proto` **Package**: `gcommon.v1.health` **Lines**: 45

**Enums** (1): `CheckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/enums/check_type.proto
// version: 1.0.0
// guid: 9b2c3d4e-5f67-8901-bcd2-345678901efa

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * Types of health checks that can be performed.
 * Each type represents a different aspect or method of health verification.
 */
enum CheckType {
  // Default unspecified check type
  CHECK_TYPE_UNSPECIFIED = 0;

  // Basic health check - simple alive/dead status
  CHECK_TYPE_HEALTH = 1;

  // Readiness check - service is ready to handle requests
  CHECK_TYPE_READINESS = 2;

  // Liveness check - service is alive and responsive
  CHECK_TYPE_LIVENESS = 3;

  // Dependency check - external dependencies are available
  CHECK_TYPE_DEPENDENCY = 4;

  // Resource check - system resources (CPU, memory, disk)
  CHECK_TYPE_RESOURCE = 5;

  // Network check - network connectivity and latency
  CHECK_TYPE_NETWORK = 6;

  // Database check - database connectivity and performance
  CHECK_TYPE_DATABASE = 7;

  // Custom application-specific check
  CHECK_TYPE_CUSTOM = 8;
}
```

---

### health_status.proto {#health_status}

**Path**: `gcommon/v1/health/enums/health_status.proto` **Package**: `gcommon.v1.health` **Lines**: 42

**Enums** (1): `HealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/health/enums/health_status.proto
// version: 1.0.0
// guid: 8a1b2c3d-4e5f-6789-abc1-234567890def

edition = "2023";

package gcommon.v1.health;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/health";

/**
 * Health status enumeration for the health module.
 * Provides detailed health states for services and components.
 */
enum HealthStatus {
  // Default unspecified state
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

  // Service/component status is unknown or cannot be determined
  HEALTH_STATUS_UNKNOWN = 6;

  // Service/component is in maintenance mode
  HEALTH_STATUS_MAINTENANCE = 7;
}
```

---

