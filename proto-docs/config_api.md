# config_api Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 7
- **Messages**: 7
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [backup_policy.proto](#backup_policy)
- [backup_settings.proto](#backup_settings)
- [get_schema_request.proto](#get_schema_request)
- [get_schema_response.proto](#get_schema_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [rollback_info.proto](#rollback_info)
---


## Detailed Documentation

### backup_policy.proto {#backup_policy}

**Path**: `gcommon/v1/config/backup_policy.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `BackupPolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/backup_policy.proto
// version: 1.0.0
// guid: 900e85e2-21f2-4656-84f5-61f198cb79c7

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message BackupPolicy {
  // Backup enabled
  bool enabled = 1;

  // Backup schedule
  string schedule = 2 [(buf.validate.field).string.min_len = 1];

  // Backup retention
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup location
  string location = 4 [(buf.validate.field).string.min_len = 1];

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup verification
  bool verified = 7;

  // Backup metadata
  map<string, string> metadata = 8;
}
```

---

### backup_settings.proto {#backup_settings}

**Path**: `gcommon/v1/config/backup_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 38

**Messages** (1): `BackupSettings`

**Imports** (3):

- `gcommon/v1/common/backup_frequency.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/backup_settings.proto
// version: 1.0.0
// guid: e9a07253-25f8-4306-ad78-31325ce9b271

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/backup_frequency.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message BackupSettings {
  // Whether backup is enabled
  bool enabled = 1;

  // Backup frequency
  gcommon.v1.common.BackupFrequency frequency = 2;

  // Backup retention period in days
  int32 retention_days = 3 [(buf.validate.field).int32.gte = 0];

  // Backup storage location
  string storage_location = 4 [(buf.validate.field).string.min_len = 1];

  // Backup encryption
  bool encrypted = 5;

  // Backup compression
  bool compressed = 6;

  // Backup metadata
  map<string, string> metadata = 7;
}
```

---

### get_schema_request.proto {#get_schema_request}

**Path**: `gcommon/v1/config/get_schema_request.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `GetSchemaRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/api/get_schema_request.proto
// version: 1.0.0
// guid: 418bff8d-7263-433a-84b5-c063a0a393fa
// file: proto/gcommon/v1/config/get_schema_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message GetSchemaRequest {
  // Schema name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_schema_response.proto {#get_schema_response}

**Path**: `gcommon/v1/config/get_schema_response.proto` **Package**: `gcommon.v1.config` **Lines**: 24

**Messages** (1): `GetSchemaResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/config/config_schema.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/get_schema_response.proto
// version: 1.0.1
// guid: 814082ea-43bd-4fe6-9f69-3e587af7e038
edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/config/config_schema.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

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

**Path**: `gcommon/v1/config/health_check_request.proto` **Package**: `gcommon.v1.config` **Lines**: 27

**Messages** (1): `ConfigHealthCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_request.proto
// version: 1.0.0
// guid: bb4a27ef-7b1e-4a20-937c-7366e3be5b6f
//
// Request definitions for config module
// Generated as part of protobuf implementation
//

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigHealthCheckRequest {
  // Target namespace to check
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/config/health_check_response.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Messages** (1): `ConfigHealthCheckResponse`

**Imports** (3):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_response.proto
// version: 1.0.0
// guid: 4f491273-ecd5-4d3c-b13d-b7ef6219a25d

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

/**
 * HealthCheckResponse provides health status for the config service.
 */
message ConfigHealthCheckResponse {
  // Overall health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Optional human-readable message
  string message = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### rollback_info.proto {#rollback_info}

**Path**: `gcommon/v1/config/rollback_info.proto` **Package**: `gcommon.v1.config` **Lines**: 32

**Messages** (1): `RollbackInfo`

**Imports** (3):

- `gcommon/v1/common/rollback_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rollback_info.proto
// version: 1.0.0
// guid: 20b0233a-770b-4484-a066-948c77afc78e

edition = "2023";

package gcommon.v1.config;

import "gcommon/v1/common/rollback_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RollbackInfo {
  // Original audit entry being rolled back
  string original_audit_id = 1 [(buf.validate.field).string.min_len = 1];

  // Rollback reason
  string reason = 2 [(buf.validate.field).string.min_len = 1];

  // Rollback method
  gcommon.v1.common.RollbackMethod method = 3;

  // Target version for rollback
  string target_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Whether rollback was automatic
  bool automatic = 5;
}
```

---

