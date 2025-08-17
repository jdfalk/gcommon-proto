# cache_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 11
- **Messages**: 11
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [set_request.proto](#set_request)
- [set_response.proto](#set_response)
- [stats_request.proto](#stats_request)
- [subscribe_request.proto](#subscribe_request)
- [touch_expiration_response.proto](#touch_expiration_response)
- [transaction_request.proto](#transaction_request)
- [ttl_request.proto](#ttl_request)
- [unlock_request.proto](#unlock_request)
- [unsubscribe_request.proto](#unsubscribe_request)
- [unwatch_request.proto](#unwatch_request)
- [watch_request.proto](#watch_request)

## Module Dependencies

**This module depends on**:

- [common](./common.md)

**Modules that depend on this one**:

- [cache_services](./cache_services.md)
- [health](./health.md)
- [queue_1](./queue_1.md)

---

## Detailed Documentation

### set_request.proto {#set_request}

**Path**: `pkg/cache/proto/set_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 40

**Messages** (1): `SetRequest`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/set_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/any.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to store a value in the cache.
 * Supports flexible expiration policies and namespace isolation.
 */
message SetRequest {
  // Cache key to store
  string key = 1;

  // Value to store (supports any type)
  google.protobuf.Any value = 2 [lazy = true];

  // Optional namespace for cache isolation
  string namespace = 3;

  // Time-to-live for the cache entry (0 for no expiration)
  google.protobuf.Duration ttl = 4 [lazy = true];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5 [lazy = true];

  // Whether to overwrite existing value
  bool overwrite = 6;

  // Entry metadata for extensibility
  map<string, string> entry_metadata = 7 [lazy = true];
}

```

---

### set_response.proto {#set_response}

**Path**: `pkg/cache/proto/set_response.proto` **Package**: `gcommon.v1.cache` **Lines**: 25

**Messages** (1): `SetResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: cache/proto/responses/set_response.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache set operation.
 * Indicates success and provides operation metadata.
 */
message SetResponse {
  // Whether the operation was successful
  bool success = 1;

  // Whether an existing value was overwritten
  bool overwritten = 2;

  // Size of the stored value in bytes
  int64 size_bytes = 3;
}

```

---

### stats_request.proto {#stats_request}

**Path**: `pkg/cache/proto/stats_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 22

**Messages** (1): `GetStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/stats_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to retrieve cache statistics.
 */
message GetStatsRequest {
  // Optional namespace filter
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### subscribe_request.proto {#subscribe_request}

**Path**: `pkg/cache/proto/subscribe_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 22

**Messages** (1): `SubscribeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/subscribe_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to subscribe to cache events.
 */
message SubscribeRequest {
  // Topic or channel name
  string topic = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### touch_expiration_response.proto {#touch_expiration_response}

**Path**: `pkg/cache/proto/touch_expiration_response.proto` **Package**: `gcommon.v1.cache` **Lines**: 29

**Messages** (1): `TouchExpirationResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/touch_expiration_response.proto
// version: 1.0.0
// guid: kl1mnopq-23r4-5s6t-7u8v-9w0x1y2z3a4b

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache touch expiration operations.
 * Indicates success/failure of TTL update.
 */
message TouchExpirationResponse {
  // Whether the key's TTL was successfully updated
  bool success = 1;

  // Whether the key existed before the touch operation
  bool key_existed = 2;

  // Error details if touch failed
  gcommon.v1.common.Error error = 3;
}

```

---

### transaction_request.proto {#transaction_request}

**Path**: `pkg/cache/proto/transaction_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 22

**Messages** (1): `TransactionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/transaction_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to execute multiple cache operations in a transaction.
 */
message TransactionRequest {
  // Encoded operations in transaction
  bytes operations = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### ttl_request.proto {#ttl_request}

**Path**: `pkg/cache/proto/ttl_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 29

**Messages** (1): `TouchExpirationRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/ttl_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to update the TTL of an existing cache key.
 */
message TouchExpirationRequest {
  // Key to update
  string key = 1;

  // New TTL duration
  google.protobuf.Duration ttl = 2 [lazy = true];

  // Optional namespace
  string namespace = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}

```

---

### unlock_request.proto {#unlock_request}

**Path**: `pkg/cache/proto/unlock_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 25

**Messages** (1): `UnlockRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/unlock_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to release a previously acquired cache lock.
 */
message UnlockRequest {
  // Lock key
  string key = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### unsubscribe_request.proto {#unsubscribe_request}

**Path**: `pkg/cache/proto/unsubscribe_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 22

**Messages** (1): `UnsubscribeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/unsubscribe_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to unsubscribe from cache events.
 */
message UnsubscribeRequest {
  // Topic or channel name
  string topic = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### unwatch_request.proto {#unwatch_request}

**Path**: `pkg/cache/proto/unwatch_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 22

**Messages** (1): `UnwatchRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/unwatch_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to stop watching a cache key for changes.
 */
message UnwatchRequest {
  // Key being watched
  string key = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### watch_request.proto {#watch_request}

**Path**: `pkg/cache/proto/watch_request.proto` **Package**: `gcommon.v1.cache` **Lines**: 22

**Messages** (1): `WatchRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/watch_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to watch a cache key for changes.
 */
message WatchRequest {
  // Key to watch
  string key = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---
