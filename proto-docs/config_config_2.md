# config_config_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 8
- **Messages**: 8
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [transformation_settings.proto](#transformation_settings)
- [unwatch_config_request.proto](#unwatch_config_request)
- [validate_config_request.proto](#validate_config_request)
- [validate_config_response.proto](#validate_config_response)
- [validation_settings.proto](#validation_settings)
- [versioning_settings.proto](#versioning_settings)
- [watch_config_request.proto](#watch_config_request)
- [watch_config_response.proto](#watch_config_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [config_1](./config_1.md)
- [config_2](./config_2.md)
- [config_config_1](./config_config_1.md)
- [config_events](./config_events.md)

**Modules that depend on this one**:

- [config_services](./config_services.md)

---

## Detailed Documentation

### transformation_settings.proto {#transformation_settings}

**Path**: `pkg/config/proto/transformation_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 33

**Messages** (1): `TransformationSettings`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/transformation_step.proto` → [config_2](./config_2.md#transformation_step)

#### Source Code

```protobuf
// file: pkg/config/proto/transformation_settings.proto
// version: 1.0.0
// guid: aadcd103-6f7c-4b6c-a58a-5c4ee2500cbf

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/transformation_step.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message TransformationSettings {
  // Whether transformation is enabled
  bool enabled = 1;

  // Transformation pipeline
  repeated TransformationStep pipeline = 2;

  // Transformation on read
  bool transform_on_read = 3;

  // Transformation on write
  bool transform_on_write = 4;

  // Transformation metadata
  map<string, string> metadata = 5;
}

```

---

### unwatch_config_request.proto {#unwatch_config_request}

**Path**: `pkg/config/proto/unwatch_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Messages** (1): `UnwatchConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/unwatch_config_request.proto
// file: config/proto/requests/unwatch_config_request.proto
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

message UnwatchConfigRequest {
  // Watch identifier returned by WatchConfigRequest
  string watch_id = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### validate_config_request.proto {#validate_config_request}

**Path**: `pkg/config/proto/validate_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Messages** (1): `ValidateConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/config/proto/config_entry.proto` → [config_config_1](./config_config_1.md#config_entry)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/validate_config_request.proto
// file: config/proto/requests/validate_config_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/config/proto/config_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValidateConfigRequest {
  // Configuration entries to validate
  repeated ConfigEntry entries = 1;

  // Schema to validate against
  string schema_name = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### validate_config_response.proto {#validate_config_response}

**Path**: `pkg/config/proto/validate_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 26

**Messages** (1): `ValidateConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/config/proto/config_validation_error.proto` → [config_config_1](./config_config_1.md#config_validation_error)
- `pkg/config/proto/config_validation_warning.proto` → [config_config_1](./config_config_1.md#config_validation_warning)

#### Source Code

```protobuf
// file: pkg/config/proto/responses/validate_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/config/proto/config_validation_error.proto";
import "pkg/config/proto/config_validation_warning.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * ValidateConfigResponse contains validation results for configuration entries.
 */
message ValidateConfigResponse {
  // Validation result
  bool valid = 1;

  // Validation errors
  repeated ConfigValidationError errors = 2;

  // Validation warnings
  repeated ConfigValidationWarning warnings = 3;
}

```

---

### validation_settings.proto {#validation_settings}

**Path**: `pkg/config/proto/validation_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 40

**Messages** (1): `ValidationSettings`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/retry_settings.proto` → [config_config_1](./config_config_1.md#retry_settings)
- `pkg/config/proto/validation_rule.proto` → [config_2](./config_2.md#validation_rule)

#### Source Code

```protobuf
// file: pkg/config/proto/validation_settings.proto
// version: 1.0.0
// guid: b6a8294f-3f5c-4bcc-95ad-9369bd1addd5

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/retry_settings.proto";
import "pkg/config/proto/validation_rule.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message ValidationSettings {
  // Whether validation is enabled
  bool enabled = 1;

  // Validation rules (using ValidationRule from config_template.proto)
  repeated ValidationRule rules = 2;

  // Validation on change
  bool validate_on_change = 3;

  // Validation on access
  bool validate_on_access = 4;

  // Validation timeout in seconds
  int32 timeout_seconds = 5;

  // Validation retry settings
  RetrySettings retry = 6;

  // Validation metadata
  map<string, string> metadata = 7;
}

```

---

### versioning_settings.proto {#versioning_settings}

**Path**: `pkg/config/proto/versioning_settings.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `VersioningSettings`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/audit_level.proto` → [config_events](./config_events.md#audit_level)
- `pkg/config/proto/backup_frequency.proto` → [config_1](./config_1.md#backup_frequency)
- `pkg/config/proto/channel_type.proto` → [config_1](./config_1.md#channel_type)
- `pkg/config/proto/config_data_type.proto` → [config_config_1](./config_config_1.md#config_data_type)
- `pkg/config/proto/deprecation_level.proto` → [config_1](./config_1.md#deprecation_level)
- `pkg/config/proto/metadata_status.proto` → [config_1](./config_1.md#metadata_status)
- `pkg/config/proto/notification_trigger.proto` → [config_1](./config_1.md#notification_trigger)

#### Source Code

```protobuf
// file: pkg/config/proto/versioning_settings.proto
// version: 1.0.0
// guid: 8ed86af7-67dd-4efb-abe6-bd383a4a4720

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/audit_level.proto";
import "pkg/config/proto/backup_frequency.proto";
import "pkg/config/proto/channel_type.proto";
import "pkg/config/proto/config_data_type.proto";
import "pkg/config/proto/deprecation_level.proto";
import "pkg/config/proto/metadata_status.proto";
import "pkg/config/proto/notification_trigger.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message VersioningSettings {
  // Whether versioning is enabled
  bool enabled = 1;

  // Maximum number of versions to keep
  int32 max_versions = 2;

  // Version retention period in days
  int32 retention_days = 3;

  // Whether to create versions on change
  bool version_on_change = 4;

  // Whether to create versions on schedule
  bool version_on_schedule = 5;

  // Versioning schedule
  string schedule = 6;

  // Version metadata
  map<string, string> metadata = 7;
}

```

---

### watch_config_request.proto {#watch_config_request}

**Path**: `pkg/config/proto/watch_config_request.proto` **Package**: `gcommon.v1.config` **Lines**: 25

**Messages** (1): `WatchConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/config/proto/requests/watch_config_request.proto
// file: config/proto/requests/watch_config_request.proto
//

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

message WatchConfigRequest {
  // Key or key pattern to watch
  string key_pattern = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### watch_config_response.proto {#watch_config_response}

**Path**: `pkg/config/proto/watch_config_response.proto` **Package**: `gcommon.v1.config` **Lines**: 30

**Messages** (1): `WatchConfigResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/config/proto/config_change_type.proto` → [config_config_1](./config_config_1.md#config_change_type)
- `pkg/config/proto/config_entry.proto` → [config_config_1](./config_config_1.md#config_entry)

#### Source Code

```protobuf
// file: pkg/config/proto/responses/watch_config_response.proto
edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/config/proto/config_change_type.proto";
import "pkg/config/proto/config_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/config/proto";

/**
 * WatchConfigResponse describes a configuration change event.
 */
message WatchConfigResponse {
  // Type of change
  ConfigChangeType change_type = 1;

  // Configuration entry
  ConfigEntry entry = 2;

  // Previous value for updates/deletes
  ConfigEntry previous_entry = 3;

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;
}

```

---
