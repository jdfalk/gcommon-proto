# cache Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 7
- **Messages**: 7
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [cache_entry.proto](#cache_entry)
- [cache_info.proto](#cache_info)
- [cache_metrics.proto](#cache_metrics)
- [cache_operation_result.proto](#cache_operation_result)
- [cache_stats.proto](#cache_stats)
- [eviction_result.proto](#eviction_result)
- [set_options.proto](#set_options)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [queue_1](./queue_1.md)
- [web](./web.md)

**Modules that depend on this one**:

- [cache_api_1](./cache_api_1.md)

---

## Detailed Documentation

### cache_entry.proto {#cache_entry}

**Path**: `pkg/cache/proto/cache_entry.proto` **Package**: `gcommon.v1.cache`
**Lines**: 46

**Messages** (1): `CacheEntry`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/cache_entry.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Cache entry containing the cached value and metadata.
 * Supports multiple value types with comprehensive expiration
 * and access tracking for cache policies.
 */
message CacheEntry {
  // Cache key (immutable)
  string key = 1;

  // The cached value (flexible type support)
  google.protobuf.Any value = 2 [lazy = true];

  // When the entry was created
  google.protobuf.Timestamp created_at = 3 [lazy = true];

  // When the entry was last accessed
  google.protobuf.Timestamp last_accessed_at = 4 [lazy = true];

  // When the entry expires (optional)
  google.protobuf.Timestamp expires_at = 5 [lazy = true];

  // Number of times the entry has been accessed
  int64 access_count = 6;

  // Size of the entry in bytes
  int64 size_bytes = 7;

  // Entry metadata for extensibility
  map<string, string> metadata = 8 [lazy = true];

  // Cache namespace this entry belongs to
  string namespace = 9;
}

```

---

### cache_info.proto {#cache_info}

**Path**: `pkg/cache/proto/cache_info.proto` **Package**: `gcommon.v1.cache`
**Lines**: 48

**Messages** (1): `CacheInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/cache_info.proto
// version: 1.0.0
// guid: no4pqrst-56u7-8v9w-0x1y-2z3a4b5c6d7e

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * General cache information and metadata.
 * Provides cache instance details and operational status.
 */
message CacheInfo {
  // Cache instance name
  string name = 1;

  // Cache version
  string version = 2;

  // Cache type (e.g., "memory", "redis", "memcached")
  string cache_type = 3;

  // Current health status
  gcommon.v1.common.HealthStatus health_status = 4;

  // Cache creation timestamp
  google.protobuf.Timestamp created_at = 5;

  // Last access timestamp
  google.protobuf.Timestamp last_accessed = 6;

  // Cache instance ID
  string instance_id = 7;

  // Cache description
  string description = 8;

  // Additional metadata
  map<string, string> metadata = 9;
}

```

---

### cache_metrics.proto {#cache_metrics}

**Path**: `pkg/cache/proto/cache_metrics.proto` **Package**: `gcommon.v1.cache`
**Lines**: 60

**Messages** (1): `CacheMetrics`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/cache_metrics.proto
// version: 1.0.0
// guid: pq6rstuv-78w9-0x1y-2z3a-4b5c6d7e8f9g

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Detailed cache performance metrics.
 * Provides comprehensive metrics for cache monitoring and optimization.
 */
message CacheMetrics {
  // Operations per second
  double ops_per_second = 1;

  // Read operations per second
  double reads_per_second = 2;

  // Write operations per second
  double writes_per_second = 3;

  // Average response time
  google.protobuf.Duration avg_response_time = 4;

  // 95th percentile response time
  google.protobuf.Duration p95_response_time = 5;

  // 99th percentile response time
  google.protobuf.Duration p99_response_time = 6;

  // Total number of connections
  int64 total_connections = 7;

  // Active connections
  int64 active_connections = 8;

  // Network bytes received
  int64 network_bytes_in = 9;

  // Network bytes sent
  int64 network_bytes_out = 10;

  // CPU usage percentage
  double cpu_usage_percent = 11;

  // Memory usage percentage
  double memory_usage_percent = 12;

  // Timestamp of metrics collection
  google.protobuf.Timestamp collected_at = 13;
}

```

---

### cache_operation_result.proto {#cache_operation_result}

**Path**: `pkg/cache/proto/cache_operation_result.proto` **Package**:
`gcommon.v1.cache` **Lines**: 48

**Messages** (1): `CacheOperationResult`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/cache_operation_result.proto
// version: 1.0.0
// guid: qr7stuvw-89x0-1y2z-3a4b-5c6d7e8f9g0h

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Result of cache operations.
 * Provides detailed outcome information for cache operations.
 */
message CacheOperationResult {
  // Whether the operation was successful
  bool success = 1;

  // Operation type (e.g., "GET", "SET", "DELETE")
  string operation_type = 2;

  // Key involved in the operation
  string key = 3;

  // Namespace (if applicable)
  string namespace = 4;

  // Operation duration
  int64 duration_microseconds = 5;

  // Timestamp of operation
  google.protobuf.Timestamp timestamp = 6;

  // Number of items affected
  int64 items_affected = 7;

  // Error details if operation failed
  gcommon.v1.common.Error error = 8;

  // Additional operation metadata
  map<string, string> metadata = 9;
}

```

---

### cache_stats.proto {#cache_stats}

**Path**: `pkg/cache/proto/cache_stats.proto` **Package**: `gcommon.v1.cache`
**Lines**: 53

**Messages** (1): `CacheStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/cache_stats.proto
// version: 1.0.0
// guid: mn3opqrs-45t6-7u8v-9w0x-1y2z3a4b5c6d

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Cache statistics and performance metrics.
 * Provides detailed information about cache usage and performance.
 */
message CacheStats {
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

  // Number of expired items
  int64 expired_items = 8;

  // Average access time in milliseconds
  double avg_access_time_ms = 9;

  // Last reset timestamp
  google.protobuf.Timestamp last_reset = 10;

  // Cache uptime in seconds
  int64 uptime_seconds = 11;
}

```

---

### eviction_result.proto {#eviction_result}

**Path**: `pkg/cache/proto/eviction_result.proto` **Package**:
`gcommon.v1.cache` **Lines**: 42

**Messages** (1): `EvictionResult`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/eviction_policy.proto` →
  [common](./common.md#eviction_policy)

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/eviction_result.proto
// version: 1.0.0
// guid: op5qrstu-67v8-9w0x-1y2z-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/common/proto/eviction_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Result of cache eviction operations.
 * Provides details about items removed from cache.
 */
message EvictionResult {
  // Number of items evicted
  int64 evicted_count = 1;

  // List of evicted keys
  repeated string evicted_keys = 2;

  // Eviction policy used
  gcommon.v1.common.EvictionPolicy policy_used = 3;

  // Reason for eviction
  string eviction_reason = 4;

  // Timestamp of eviction
  google.protobuf.Timestamp evicted_at = 5;

  // Memory freed by eviction (bytes)
  int64 memory_freed = 6;

  // Whether eviction was successful
  bool success = 7;
}

```

---

### set_options.proto {#set_options}

**Path**: `pkg/cache/proto/set_options.proto` **Package**: `gcommon.v1.cache`
**Lines**: 32

**Messages** (1): `SetOptions`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/set_options.proto
// version: 1.0.0
// guid: e38b21c6-45d8-4a4b-9f7d-5f6a93484ee9

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Options for advanced cache set operations.
 * Allows conditional writes and flexible expiration policies.
 */
message SetOptions {
  // Only set the value if the key does not already exist
  bool only_if_absent = 1;

  // Only set the value if the key already exists
  bool only_if_present = 2;

  // Time-to-live for the entry
  google.protobuf.Duration ttl = 3 [lazy = true];

  // Return the previous value if overwritten
  bool return_previous = 4;
}

```

---
