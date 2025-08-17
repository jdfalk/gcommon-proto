# config_api Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 4
- **Messages**: 4
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [get_schema_request.proto](#get_schema_request)
- [get_schema_response.proto](#get_schema_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_config_1](./config_config_1.md)
- [metrics_1](./metrics_1.md)
- [queue_1](./queue_1.md)
- [web](./web.md)

**Modules that depend on this one**:

- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)

---

## Detailed Documentation

### get_schema_request.proto {#get_schema_request}

**Path**: `pkg/config/proto/get_schema_request.proto` **Package**: `gcommon.v1.config` **Lines**: 22

**Messages** (1): `GetSchemaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/get_config_schema_request.proto
// file: config/proto/requests/get_config_schema_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message GetSchemaRequest {
  // Schema name
  string name = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_schema_response.proto {#get_schema_response}

**Path**: `pkg/config/proto/get_schema_response.proto` **Package**: `gcommon.v1.config` **Lines**: 23

**Messages** (1): `GetSchemaResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/config/proto/config_schema.proto` → [config_config_1](./config_config_1.md#config_schema)

#### Source Code

```protobuf
// file: pkg/config/proto/responses/get_schema_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/config/proto/config_schema.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * GetSchemaResponse returns a configuration schema.
 */
message GetSchemaResponse {
  // Configuration schema
  ConfigSchema schema = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/config/proto/health_check_request.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/health_check_request.proto
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message HealthCheckRequest {
  // Target namespace to check
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### health_check_response.proto {#health_check_response}

**Path**: `pkg/config/proto/health_check_response.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Messages** (1): `HealthCheckResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) → [metrics_1](./metrics_1.md#health_status) → [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/config/proto/responses/health_check_response.proto
// version: 1.0.0
// guid: 4f491273-ecd5-4d3c-b13d-b7ef6219a25d

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * HealthCheckResponse provides health status for the config service.
 */
message HealthCheckResponse {
  // Overall health status
  gcommon.v1.common.HealthStatus status = 1;

  // Optional human-readable message
  string message = 2;
}

```

---
