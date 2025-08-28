# config_events Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 3
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [config_watch_event.proto](#config_watch_event)
- [rotation_event.proto](#rotation_event)
- [version_promotion_event.proto](#version_promotion_event)
---


## Detailed Documentation

### config_watch_event.proto {#config_watch_event}

**Path**: `gcommon/v1/config/config_watch_event.proto` **Package**: `gcommon.v1.config` **Lines**: 42

**Messages** (1): `ConfigWatchEvent`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_watch_event.proto
// version: 1.0.0
// guid: 218de9f4-02fd-4c68-acb9-0f549a1cfd06

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message ConfigWatchEvent {
  // Watch session identifier
  string watch_id = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration key that changed
  string key = 2 [(buf.validate.field).string.min_len = 1];

  // Previous value (if any)
  google.protobuf.Any old_value = 3;

  // New value
  google.protobuf.Any new_value = 4;

  // Type of change (CREATE, UPDATE, DELETE)
  string change_type = 5 [(buf.validate.field).string.min_len = 1];

  // Timestamp of the change
  google.protobuf.Timestamp timestamp = 6;

  // Configuration namespace or section
  string namespace = 7 [(buf.validate.field).string.min_len = 1];

  // Additional event metadata
  map<string, string> metadata = 8;
}
```

---

### rotation_event.proto {#rotation_event}

**Path**: `gcommon/v1/config/rotation_event.proto` **Package**: `gcommon.v1.config` **Lines**: 34

**Messages** (1): `RotationEvent`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rotation_event.proto
// version: 1.0.0
// guid: b7c8d9e0-1f23-4567-1234-789012345678

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message RotationEvent {
  // Event ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Rotation timestamp
  google.protobuf.Timestamp timestamp = 2;

  // Previous value
  string previous_value = 3;

  // New value
  string new_value = 4;

  // Rotation reason
  string reason = 5;
}
```

---

### version_promotion_event.proto {#version_promotion_event}

**Path**: `gcommon/v1/config/version_promotion_event.proto` **Package**: `gcommon.v1.config` **Lines**: 44

**Messages** (1): `VersionPromotionEvent`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_promotion_event.proto
// version: 1.0.0
// guid: d231a04f-95ab-4854-a15d-7992ab883362

edition = "2023";

package gcommon.v1.config;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/config";

message VersionPromotionEvent {
  // Source environment
  string source_environment = 1 [(buf.validate.field).string.min_len = 1];

  // Target environment
  string target_environment = 2 [(buf.validate.field).string.min_len = 1];

  // Promotion timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Promotion user
  string promoted_by = 4 [(buf.validate.field).string.min_len = 1];

  // Promotion reason
  string reason = 5 [(buf.validate.field).string.min_len = 1];

  // Promotion method
  string method = 6 [(buf.validate.field).string.min_len = 1];

  // Promotion success
  bool success = 7;

  // Promotion error
  string error = 8 [(buf.validate.field).string.min_len = 1];

  // Promotion metadata
  map<string, string> metadata = 9;
}
```

---

