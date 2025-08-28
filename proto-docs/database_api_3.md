# database_api_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 3
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [unsubscribe_request.proto](#unsubscribe_request)
- [unwatch_request.proto](#unwatch_request)
- [watch_request.proto](#watch_request)
---


## Detailed Documentation

### unsubscribe_request.proto {#unsubscribe_request}

**Path**: `gcommon/v1/database/unsubscribe_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `CacheUnsubscribeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/unsubscribe_request.proto
// version: 1.0.0
// guid: ab8ca5f1-cb63-41bc-88d5-0aef5bd4f76a
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to unsubscribe from cache events.
 */
message CacheUnsubscribeRequest {
  // Topic or channel name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### unwatch_request.proto {#unwatch_request}

**Path**: `gcommon/v1/database/unwatch_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `UnwatchRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/unwatch_request.proto
// version: 1.0.0
// guid: d369ada8-e4ff-4d62-98c8-97e1d767763e
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to stop watching a cache key for changes.
 */
message UnwatchRequest {
  // Key being watched
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### watch_request.proto {#watch_request}

**Path**: `gcommon/v1/database/watch_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `CacheWatchRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/watch_request.proto
// version: 1.0.0
// guid: ec773ec9-0060-4165-a6a0-7d33894d0f75
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to watch a cache key for changes.
 */
message CacheWatchRequest {
  // Key to watch
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

