# cache_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 52
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [append_request.proto](#append_request)
- [backup_request.proto](#backup_request)
- [clear_request.proto](#clear_request)
- [clear_response.proto](#clear_response)
- [create_namespace_request.proto](#create_namespace_request)
- [create_namespace_response.proto](#create_namespace_response)
- [decrement_request.proto](#decrement_request)
- [decrement_response.proto](#decrement_response)
- [defrag_request.proto](#defrag_request)
- [delete_multiple_request.proto](#delete_multiple_request)
- [delete_multiple_response.proto](#delete_multiple_response)
- [delete_namespace_request.proto](#delete_namespace_request)
- [delete_request.proto](#delete_request)
- [delete_response.proto](#delete_response)
- [exists_request.proto](#exists_request)
- [exists_response.proto](#exists_response)
- [expire_request.proto](#expire_request)
- [export_request.proto](#export_request)
- [flush_request.proto](#flush_request)
- [flush_response.proto](#flush_response)
- [gc_request.proto](#gc_request)
- [get_memory_usage_request.proto](#get_memory_usage_request)
- [get_memory_usage_response.proto](#get_memory_usage_response)
- [get_multiple_request.proto](#get_multiple_request)
- [get_multiple_response.proto](#get_multiple_response)
- [get_namespace_stats_request.proto](#get_namespace_stats_request)
- [get_namespace_stats_response.proto](#get_namespace_stats_response)
- [get_request.proto](#get_request)
- [get_response.proto](#get_response)
- [get_stats_response.proto](#get_stats_response)
- [health_check_request.proto](#health_check_request)
- [import_request.proto](#import_request)
- [increment_request.proto](#increment_request)
- [increment_response.proto](#increment_response)
- [info_request.proto](#info_request)
- [keys_request.proto](#keys_request)
- [keys_response.proto](#keys_response)
- [list_namespaces_request.proto](#list_namespaces_request)
- [list_namespaces_response.proto](#list_namespaces_response)
- [list_subscriptions_request.proto](#list_subscriptions_request)
- [lock_request.proto](#lock_request)
- [mget_request.proto](#mget_request)
- [optimize_request.proto](#optimize_request)
- [pipeline_request.proto](#pipeline_request)
- [prepend_request.proto](#prepend_request)
- [publish_request.proto](#publish_request)
- [restore_request.proto](#restore_request)
- [scan_request.proto](#scan_request)
- [set_multiple_request.proto](#set_multiple_request)
- [set_multiple_response.proto](#set_multiple_response)

## Module Dependencies

**This module depends on**:

- [cache](./cache.md)
- [common](./common.md)

**Modules that depend on this one**:

- [cache_services](./cache_services.md)
- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)

---

## Detailed Documentation

### append_request.proto {#append_request}

**Path**: `pkg/cache/proto/append_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 29

**Messages** (1): `AppendRequest`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/append_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to append data to an existing cache entry.
 */
message AppendRequest {
  // Cache key to modify
  string key = 1;

  // Value to append
  google.protobuf.Any value = 2 [lazy = true];

  // Optional namespace for cache isolation
  string namespace = 3;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}

```

---

### backup_request.proto {#backup_request}

**Path**: `pkg/cache/proto/backup_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 25

**Messages** (1): `BackupRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/backup_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to create a backup of the cache contents.
 */
message BackupRequest {
  // Destination path or identifier for the backup
  string destination = 1;

  // Optional namespace to back up
  string namespace = 2;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### clear_request.proto {#clear_request}

**Path**: `pkg/cache/proto/clear_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 26

**Messages** (1): `ClearRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/clear_request.proto
// version: 1.0.0
// guid: de4fghij-56k7-8l9m-0n1o-2p3q4r5s6t7u

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to clear all cache entries.
 * Optionally clear only a specific namespace.
 */
message ClearRequest {
  // Optional namespace to clear (if empty, clears all)
  string namespace = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### clear_response.proto {#clear_response}

**Path**: `pkg/cache/proto/clear_response.proto` **Package**: `gcommon.v1.cache`
**Lines**: 29

**Messages** (1): `ClearResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/clear_response.proto
// version: 1.0.0
// guid: ef5ghijk-67l8-9m0n-1o2p-3q4r5s6t7u8v

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache clear operations.
 * Indicates success/failure of clearing cache entries.
 */
message ClearResponse {
  // Number of entries that were cleared
  int64 cleared_count = 1;

  // Whether the operation was successful
  bool success = 2;

  // Error details if clear failed
  gcommon.v1.common.Error error = 3;
}

```

---

### create_namespace_request.proto {#create_namespace_request}

**Path**: `pkg/cache/proto/create_namespace_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 36

**Messages** (1): `CreateNamespaceRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/create_namespace_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174012

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to create a new cache namespace.
 */
message CreateNamespaceRequest {
  // Name of the namespace to create
  string name = 1;

  // Description of the namespace
  string description = 2;

  // Maximum number of keys allowed in this namespace
  int64 max_keys = 3;

  // Maximum memory usage for this namespace (in bytes)
  int64 max_memory_bytes = 4;

  // Default TTL for keys in this namespace (in seconds)
  int32 default_ttl_seconds = 5;

  // Configuration options for the namespace
  map<string, string> config = 6;
}

```

---

### create_namespace_response.proto {#create_namespace_response}

**Path**: `pkg/cache/proto/create_namespace_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 43

**Messages** (1): `CreateNamespaceResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/create_namespace_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174013

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for creating a cache namespace.
 */
message CreateNamespaceResponse {
  // ID of the created namespace
  string namespace_id = 1;

  // Name of the created namespace
  string name = 2;

  // Description of the namespace
  string description = 3;

  // When the namespace was created
  google.protobuf.Timestamp created_at = 4;

  // Maximum number of keys allowed
  int64 max_keys = 5;

  // Maximum memory usage (in bytes)
  int64 max_memory_bytes = 6;

  // Default TTL for keys (in seconds)
  int32 default_ttl_seconds = 7;

  // Current configuration
  map<string, string> config = 8;
}

```

---

### decrement_request.proto {#decrement_request}

**Path**: `pkg/cache/proto/decrement_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 35

**Messages** (1): `DecrementRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/decrement_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to decrement a cached counter atomically.
 */
message DecrementRequest {
  // Counter key
  string key = 1;

  // Decrement delta (can be negative)
  int64 delta = 2;

  // Initial value if key doesn't exist
  int64 initial_value = 3;

  // TTL for the counter
  google.protobuf.Duration ttl = 4 [lazy = true];

  // Optional namespace
  string namespace = 5;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 6 [lazy = true];
}

```

---

### decrement_response.proto {#decrement_response}

**Path**: `pkg/cache/proto/decrement_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 29

**Messages** (1): `DecrementResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/decrement_response.proto
// version: 1.0.0
// guid: cd3efghi-45j6-7k8l-9m0n-1o2p3q4r5s6t

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache decrement operations.
 * Returns the new value after decrementing.
 */
message DecrementResponse {
  // The new value after decrementing
  int64 new_value = 1;

  // Whether the operation was successful
  bool success = 2;

  // Error details if decrement failed
  gcommon.v1.common.Error error = 3;
}

```

---

### defrag_request.proto {#defrag_request}

**Path**: `pkg/cache/proto/defrag_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 22

**Messages** (1): `DefragRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/defrag_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to defragment the cache storage.
 */
message DefragRequest {
  // Optional namespace to defragment
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### delete_multiple_request.proto {#delete_multiple_request}

**Path**: `pkg/cache/proto/delete_multiple_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 25

**Messages** (1): `DeleteMultipleRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/delete_multiple_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to delete multiple cache keys.
 */
message DeleteMultipleRequest {
  // Keys to delete
  repeated string keys = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### delete_multiple_response.proto {#delete_multiple_response}

**Path**: `pkg/cache/proto/delete_multiple_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 32

**Messages** (1): `DeleteMultipleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/delete_multiple_response.proto
// version: 1.0.0
// guid: ab1cdefg-23h4-5i6j-7k8l-9m0n1o2p3q4r

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache delete multiple operations.
 * Indicates success/failure of multiple key deletions.
 */
message DeleteMultipleResponse {
  // Number of keys that were successfully deleted
  int32 deleted_count = 1;

  // Number of keys that failed to delete
  int32 failed_count = 2;

  // List of keys that failed to delete
  repeated string failed_keys = 3;

  // Error details if any deletions failed
  gcommon.v1.common.Error error = 4;
}

```

---

### delete_namespace_request.proto {#delete_namespace_request}

**Path**: `pkg/cache/proto/delete_namespace_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 27

**Messages** (1): `DeleteNamespaceRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/delete_namespace_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174014

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to delete a cache namespace.
 */
message DeleteNamespaceRequest {
  // ID of the namespace to delete
  string namespace_id = 1;

  // Force deletion even if namespace contains data
  bool force = 2;

  // Create backup before deletion
  bool backup = 3;
}

```

---

### delete_request.proto {#delete_request}

**Path**: `pkg/cache/proto/delete_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 25

**Messages** (1): `DeleteRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: cache/proto/requests/delete_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to delete a cached value by key.
 */
message DeleteRequest {
  // Cache key to delete
  string key = 1;

  // Optional namespace for cache isolation
  string namespace = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### delete_response.proto {#delete_response}

**Path**: `pkg/cache/proto/delete_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 29

**Messages** (1): `DeleteResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/delete_response.proto
// version: 1.0.0
// guid: 9a0bcdef-12a3-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache delete operations.
 * Indicates success/failure of key deletion.
 */
message DeleteResponse {
  // Whether the key was successfully deleted
  bool success = 1;

  // Error details if deletion failed
  gcommon.v1.common.Error error = 2;

  // Number of keys that were actually deleted
  int32 deleted_count = 3;
}

```

---

### exists_request.proto {#exists_request}

**Path**: `pkg/cache/proto/exists_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 25

**Messages** (1): `ExistsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/exists_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to check for the existence of a cache key.
 */
message ExistsRequest {
  // Cache key to check
  string key = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### exists_response.proto {#exists_response}

**Path**: `pkg/cache/proto/exists_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 26

**Messages** (1): `ExistsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/exists_response.proto
// version: 1.0.0
// guid: ab1cdef2-23a4-5b6c-7d8e-9f0a1b2c3d4e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache key existence checks.
 * Indicates whether a key exists in the cache.
 */
message ExistsResponse {
  // Whether the key exists in the cache
  bool exists = 1;

  // Error details if check failed
  gcommon.v1.common.Error error = 2;
}

```

---

### expire_request.proto {#expire_request}

**Path**: `pkg/cache/proto/expire_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 29

**Messages** (1): `ExpireRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/expire_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to expire a cache key after a specified duration.
 */
message ExpireRequest {
  // Key to expire
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

### export_request.proto {#export_request}

**Path**: `pkg/cache/proto/export_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 25

**Messages** (1): `ExportRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/export_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to export cache contents to an external system.
 */
message ExportRequest {
  // Destination identifier for export
  string destination = 1;

  // Optional namespace filter
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### flush_request.proto {#flush_request}

**Path**: `pkg/cache/proto/flush_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 22

**Messages** (1): `FlushRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/flush_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to flush the cache to persistent storage.
 */
message FlushRequest {
  // Optional namespace to flush
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### flush_response.proto {#flush_response}

**Path**: `pkg/cache/proto/flush_response.proto` **Package**: `gcommon.v1.cache`
**Lines**: 29

**Messages** (1): `FlushResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/flush_response.proto
// version: 1.0.0
// guid: ij9klmno-01p2-3q4r-5s6t-7u8v9w0x1y2z

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache flush operations.
 * Indicates success/failure of cache flushing.
 */
message FlushResponse {
  // Number of items that were flushed
  int64 flushed_count = 1;

  // Whether the operation was successful
  bool success = 2;

  // Error details if flush failed
  gcommon.v1.common.Error error = 3;
}

```

---

### gc_request.proto {#gc_request}

**Path**: `pkg/cache/proto/gc_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 22

**Messages** (1): `GcRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/gc_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to trigger cache garbage collection.
 */
message GcRequest {
  // Optional namespace to clean
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_memory_usage_request.proto {#get_memory_usage_request}

**Path**: `pkg/cache/proto/get_memory_usage_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 22

**Messages** (1): `GetMemoryUsageRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/get_memory_usage_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to retrieve cache memory usage statistics.
 */
message GetMemoryUsageRequest {
  // Optional namespace filter
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_memory_usage_response.proto {#get_memory_usage_response}

**Path**: `pkg/cache/proto/get_memory_usage_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 27

**Messages** (1): `GetMemoryUsageResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/get_memory_usage_response.proto
// version: 1.0.0
// guid: 4bd2a1f2-5469-4fc5-9bdb-e0691a1bbaa9
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for GetMemoryUsage operations.
 */
message GetMemoryUsageResponse {
  // Memory usage in bytes
  int64 memory_usage_bytes = 1;

  // Memory usage as a percentage of total capacity
  double memory_usage_percent = 2;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}

```

---

### get_multiple_request.proto {#get_multiple_request}

**Path**: `pkg/cache/proto/get_multiple_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 26

**Messages** (1): `GetMultipleRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/get_multiple_request.proto
// version: 1.0.0
// guid: bc2def34-45a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to get multiple cache values by keys.
 * Supports batch retrieval for performance optimization.
 */
message GetMultipleRequest {
  // List of keys to retrieve
  repeated string keys = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_multiple_response.proto {#get_multiple_response}

**Path**: `pkg/cache/proto/get_multiple_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 29

**Messages** (1): `GetMultipleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/get_multiple_response.proto
// version: 1.0.0
// guid: cd3ef456-567a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for multiple cache value retrieval.
 * Contains a map of keys to their values or error information.
 */
message GetMultipleResponse {
  // Map of key to value for successful retrievals
  map<string, bytes> values = 1;

  // List of keys that were not found
  repeated string missing_keys = 2;

  // Error details if operation failed
  gcommon.v1.common.Error error = 3;
}

```

---

### get_namespace_stats_request.proto {#get_namespace_stats_request}

**Path**: `pkg/cache/proto/get_namespace_stats_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 27

**Messages** (1): `GetNamespaceStatsRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/get_namespace_stats_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174017

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to get namespace statistics.
 */
message GetNamespaceStatsRequest {
  // ID of the namespace
  string namespace_id = 1;

  // Include detailed metrics
  bool include_detailed_metrics = 2;

  // Include key distribution stats
  bool include_key_distribution = 3;
}

```

---

### get_namespace_stats_response.proto {#get_namespace_stats_response}

**Path**: `pkg/cache/proto/get_namespace_stats_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 60

**Messages** (2): `NamespaceStats`, `GetNamespaceStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/get_namespace_stats_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174018

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Statistics for a cache namespace.
 */
message NamespaceStats {
  // Total keys in namespace
  int64 total_keys = 1;

  // Memory usage in bytes
  int64 memory_usage_bytes = 2;

  // Hit rate percentage
  double hit_rate_percent = 3;

  // Cache hits
  int64 cache_hits = 4;

  // Cache misses
  int64 cache_misses = 5;

  // Evictions
  int64 evictions = 6;

  // Average key size
  double avg_key_size_bytes = 7;

  // Average value size
  double avg_value_size_bytes = 8;

  // Last access time
  google.protobuf.Timestamp last_access_time = 9;
}

/**
 * Response for namespace statistics.
 */
message GetNamespaceStatsResponse {
  // Namespace ID
  string namespace_id = 1;

  // Statistics
  NamespaceStats stats = 2;

  // When stats were collected
  google.protobuf.Timestamp collected_at = 3;
}

```

---

### get_request.proto {#get_request}

**Path**: `pkg/cache/proto/get_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 30

**Messages** (1): `GetRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/get_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to retrieve a cached value by key.
 * Supports namespace isolation and access time tracking
 * for LRU cache policies.
 */
message GetRequest {
  // Cache key to retrieve
  string key = 1;

  // Optional namespace for cache isolation
  string namespace = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];

  // Whether to update access time (for LRU policies)
  bool update_access_time = 4;
}

```

---

### get_response.proto {#get_response}

**Path**: `pkg/cache/proto/get_response.proto` **Package**: `gcommon.v1.cache`
**Lines**: 26

**Messages** (1): `GetResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/cache/proto/cache_entry.proto` → [cache](./cache.md#cache_entry)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/get_response.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/cache/proto/cache_entry.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response containing a cached value and metadata.
 * Includes cache hit/miss information and entry details.
 */
message GetResponse {
  // The cached entry (only present if found)
  CacheEntry entry = 1 [lazy = true];

  // Whether the key was found in the cache
  bool found = 2;

  // Cache hit/miss information for metrics
  bool cache_hit = 3;
}

```

---

### get_stats_response.proto {#get_stats_response}

**Path**: `pkg/cache/proto/get_stats_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 47

**Messages** (1): `GetStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/get_stats_response.proto
// version: 1.0.0
// guid: hi8jklmn-90o1-2p3q-4r5s-6t7u8v9w0x1y

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache statistics operations.
 * Provides detailed cache performance metrics.
 */
message GetStatsResponse {
  // Total number of cached items
  int64 total_items = 1;

  // Total cache hits
  int64 cache_hits = 2;

  // Total cache misses
  int64 cache_misses = 3;

  // Cache hit ratio (0.0 to 1.0)
  double hit_ratio = 4;

  // Memory usage in bytes
  int64 memory_usage = 5;

  // Maximum memory limit in bytes
  int64 memory_limit = 6;

  // Number of evicted items
  int64 evicted_items = 7;

  // Whether the operation was successful
  bool success = 8;

  // Error details if stats retrieval failed
  gcommon.v1.common.Error error = 9;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/cache/proto/health_check_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 22

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/health_check_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to perform a cache health check.
 */
message HealthCheckRequest {
  // Optional namespace to check
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### import_request.proto {#import_request}

**Path**: `pkg/cache/proto/import_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 25

**Messages** (1): `ImportRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/import_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to import cache contents from an external source.
 */
message ImportRequest {
  // Source location of the data
  string source = 1;

  // Optional namespace to import into
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### increment_request.proto {#increment_request}

**Path**: `pkg/cache/proto/increment_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 35

**Messages** (1): `IncrementRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/increment_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to increment a cached counter atomically.
 */
message IncrementRequest {
  // Counter key
  string key = 1;

  // Increment delta (can be negative)
  int64 delta = 2;

  // Initial value if key doesn't exist
  int64 initial_value = 3;

  // TTL for the counter
  google.protobuf.Duration ttl = 4 [lazy = true];

  // Optional namespace
  string namespace = 5;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 6 [lazy = true];
}

```

---

### increment_response.proto {#increment_response}

**Path**: `pkg/cache/proto/increment_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 29

**Messages** (1): `IncrementResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/increment_response.proto
// version: 1.0.0
// guid: bc2defgh-34i5-6j7k-8l9m-0n1o2p3q4r5s

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache increment operations.
 * Returns the new value after incrementing.
 */
message IncrementResponse {
  // The new value after incrementing
  int64 new_value = 1;

  // Whether the operation was successful
  bool success = 2;

  // Error details if increment failed
  gcommon.v1.common.Error error = 3;
}

```

---

### info_request.proto {#info_request}

**Path**: `pkg/cache/proto/info_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 19

**Messages** (1): `InfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/info_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to retrieve cache server information.
 */
message InfoRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### keys_request.proto {#keys_request}

**Path**: `pkg/cache/proto/keys_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 29

**Messages** (1): `KeysRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/keys_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to list cache keys matching a pattern.
 */
message KeysRequest {
  // Key pattern to match (supports wildcards)
  string pattern = 1;

  // Optional namespace
  string namespace = 2;

  // Pagination options
  gcommon.v1.common.Pagination pagination = 3 [lazy = true];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}

```

---

### keys_response.proto {#keys_response}

**Path**: `pkg/cache/proto/keys_response.proto` **Package**: `gcommon.v1.cache`
**Lines**: 32

**Messages** (1): `KeysResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/keys_response.proto
// version: 1.0.0
// guid: fg6hijkl-78m9-0n1o-2p3q-4r5s6t7u8v9w

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for cache keys listing operations.
 * Returns all matching keys from the cache.
 */
message KeysResponse {
  // List of keys matching the pattern
  repeated string keys = 1;

  // Total number of keys found
  int64 total_count = 2;

  // Whether the operation was successful
  bool success = 3;

  // Error details if keys retrieval failed
  gcommon.v1.common.Error error = 4;
}

```

---

### list_namespaces_request.proto {#list_namespaces_request}

**Path**: `pkg/cache/proto/list_namespaces_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 30

**Messages** (1): `ListNamespacesRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/list_namespaces_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174015

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to list cache namespaces.
 */
message ListNamespacesRequest {
  // Page number (starting from 1)
  int32 page = 1;

  // Number of items per page
  int32 page_size = 2;

  // Filter by name pattern
  string name_filter = 3;

  // Include detailed statistics
  bool include_stats = 4;
}

```

---

### list_namespaces_response.proto {#list_namespaces_response}

**Path**: `pkg/cache/proto/list_namespaces_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 60

**Messages** (2): `NamespaceInfo`, `ListNamespacesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/list_namespaces_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174016

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Namespace information.
 */
message NamespaceInfo {
  // ID of the namespace
  string namespace_id = 1;

  // Name of the namespace
  string name = 2;

  // Description
  string description = 3;

  // When created
  google.protobuf.Timestamp created_at = 4;

  // Current key count
  int64 current_keys = 5;

  // Current memory usage (bytes)
  int64 current_memory_bytes = 6;

  // Configuration
  map<string, string> config = 7;
}

/**
 * Response for listing namespaces.
 */
message ListNamespacesResponse {
  // List of namespaces
  repeated NamespaceInfo namespaces = 1;

  // Total count
  int32 total_count = 2;

  // Current page
  int32 page = 3;

  // Page size
  int32 page_size = 4;

  // Total pages
  int32 total_pages = 5;
}

```

---

### list_subscriptions_request.proto {#list_subscriptions_request}

**Path**: `pkg/cache/proto/list_subscriptions_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 19

**Messages** (1): `ListSubscriptionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/list_subscriptions_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to list active cache subscriptions.
 */
message ListSubscriptionsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### lock_request.proto {#lock_request}

**Path**: `pkg/cache/proto/lock_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 29

**Messages** (1): `LockRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/lock_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to acquire a cache lock.
 */
message LockRequest {
  // Lock key
  string key = 1;

  // Lock expiration
  google.protobuf.Duration ttl = 2 [lazy = true];

  // Optional namespace
  string namespace = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}

```

---

### mget_request.proto {#mget_request}

**Path**: `pkg/cache/proto/mget_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 36

**Messages** (1): `MGetRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/mget_request.proto
// file: cache/proto/requests/mget_request.proto
//
// Multi-get request definitions for cache module
//
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * MGetRequest is used to retrieve multiple cache entries in a single operation.
 * This is more efficient than multiple individual Get operations.
 */
message MGetRequest {
  // List of keys to retrieve
  repeated string keys = 1;

  // Namespace to search in (optional)
  string namespace = 2;

  // Whether to return expired entries
  bool include_expired = 3;

  // Whether to update access time for retrieved entries
  bool update_access_time = 4;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 5;
}

```

---

### optimize_request.proto {#optimize_request}

**Path**: `pkg/cache/proto/optimize_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 22

**Messages** (1): `OptimizeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/optimize_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to optimize cache storage layout.
 */
message OptimizeRequest {
  // Optional namespace to optimize
  string namespace = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### pipeline_request.proto {#pipeline_request}

**Path**: `pkg/cache/proto/pipeline_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 25

**Messages** (1): `PipelineRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/pipeline_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to execute a batch of cache operations atomically.
 */
message PipelineRequest {
  // Encoded operations in execution order
  bytes operations = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### prepend_request.proto {#prepend_request}

**Path**: `pkg/cache/proto/prepend_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 29

**Messages** (1): `PrependRequest`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/prepend_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to prepend data to an existing cache entry.
 */
message PrependRequest {
  // Cache key to modify
  string key = 1;

  // Value to prepend
  google.protobuf.Any value = 2 [lazy = true];

  // Optional namespace
  string namespace = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}

```

---

### publish_request.proto {#publish_request}

**Path**: `pkg/cache/proto/publish_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 26

**Messages** (1): `PublishRequest`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/publish_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to publish a value to cache subscribers.
 */
message PublishRequest {
  // Topic or channel name
  string topic = 1;

  // Payload to publish
  google.protobuf.Any payload = 2 [lazy = true];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### restore_request.proto {#restore_request}

**Path**: `pkg/cache/proto/restore_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 25

**Messages** (1): `RestoreRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/restore_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to restore cache contents from a backup.
 */
message RestoreRequest {
  // Source backup identifier
  string source = 1;

  // Optional namespace to restore
  string namespace = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### scan_request.proto {#scan_request}

**Path**: `pkg/cache/proto/scan_request.proto` **Package**: `gcommon.v1.cache`
**Lines**: 28

**Messages** (1): `ScanRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/scan_request.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to scan cache keys with a cursor.
 */
message ScanRequest {
  // Scan cursor position
  string cursor = 1;

  // Match pattern for keys
  string pattern = 2;

  // Optional namespace
  string namespace = 3;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}

```

---

### set_multiple_request.proto {#set_multiple_request}

**Path**: `pkg/cache/proto/set_multiple_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 30

**Messages** (1): `SetMultipleRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/set_multiple_request.proto
// version: 1.0.0
// guid: de4f5678-678a-9b0c-1d2e-3f4a5b6c7d8e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to set multiple cache key-value pairs.
 * Supports batch operations for performance optimization.
 */
message SetMultipleRequest {
  // Map of key-value pairs to set
  map<string, bytes> values = 1;

  // TTL for the cache entries (optional)
  google.protobuf.Duration ttl = 2 [lazy = true];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### set_multiple_response.proto {#set_multiple_response}

**Path**: `pkg/cache/proto/set_multiple_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 32

**Messages** (1): `SetMultipleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/set_multiple_response.proto
// version: 1.0.0
// guid: ef5g6789-789a-0b1c-2d3e-4f5a6b7c8d9e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for multiple cache value set operations.
 * Indicates success/failure of batch set operation.
 */
message SetMultipleResponse {
  // Whether all values were successfully set
  bool success = 1;

  // List of keys that failed to be set
  repeated string failed_keys = 2;

  // Error details if operation failed
  gcommon.v1.common.Error error = 3;

  // Number of keys that were successfully set
  int32 set_count = 4;
}

```

---
