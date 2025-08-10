# cache_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 3
- **Messages**: 3
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [cache_config.proto](#cache_config)
- [configure_policy_request.proto](#configure_policy_request)
- [configure_policy_response.proto](#configure_policy_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)

**Modules that depend on this one**:

- [cache_services](./cache_services.md)
- [web_config_1](./web_config_1.md)

---

## Detailed Documentation

### cache_config.proto {#cache_config}

**Path**: `pkg/cache/proto/cache_config.proto` **Package**: `gcommon.v1.cache`
**Lines**: 45

**Messages** (1): `CacheConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/eviction_policy.proto` →
  [common](./common.md#eviction_policy)

#### Source Code

```protobuf
// file: pkg/cache/proto/messages/cache_config.proto
// version: 1.0.0
// guid: lm2nopqr-34s5-6t7u-8v9w-0x1y2z3a4b5c

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/eviction_policy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Configuration settings for cache behavior.
 * Defines cache policies, limits, and operational parameters.
 */
message CacheConfig {
  // Maximum number of entries in cache
  int64 max_entries = 1;

  // Maximum memory usage in bytes
  int64 max_memory_bytes = 2;

  // Default time-to-live for entries
  google.protobuf.Duration default_ttl = 3;

  // Eviction policy when cache is full
  gcommon.v1.common.EvictionPolicy eviction_policy = 4;

  // Whether to enable cache statistics
  bool enable_stats = 5;

  // Whether to enable cache persistence
  bool enable_persistence = 6;

  // Persistence file path (if persistence enabled)
  string persistence_file = 7;

  // Cache name/identifier
  string name = 8;
}

```

---

### configure_policy_request.proto {#configure_policy_request}

**Path**: `pkg/cache/proto/configure_policy_request.proto` **Package**:
`gcommon.v1.cache` **Lines**: 33

**Messages** (1): `ConfigurePolicyRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/requests/configure_policy_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174019

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Request to configure cache policies.
 */
message ConfigurePolicyRequest {
  // Namespace ID to configure
  string namespace_id = 1;

  // Eviction policy (LRU, LFU, FIFO, etc.)
  string eviction_policy = 2;

  // Maximum TTL in seconds
  int32 max_ttl_seconds = 3;

  // Memory threshold for eviction (percentage)
  double memory_threshold_percent = 4;

  // Additional policy configuration
  map<string, string> policy_config = 5;
}

```

---

### configure_policy_response.proto {#configure_policy_response}

**Path**: `pkg/cache/proto/configure_policy_response.proto` **Package**:
`gcommon.v1.cache` **Lines**: 40

**Messages** (1): `ConfigurePolicyResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/cache/proto/responses/configure_policy_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174020

edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Response for configuring cache policies.
 */
message ConfigurePolicyResponse {
  // Namespace ID that was configured
  string namespace_id = 1;

  // Applied eviction policy
  string eviction_policy = 2;

  // Applied maximum TTL
  int32 max_ttl_seconds = 3;

  // Applied memory threshold
  double memory_threshold_percent = 4;

  // When the policy was applied
  google.protobuf.Timestamp applied_at = 5;

  // Previous policy configuration
  map<string, string> previous_config = 6;

  // New policy configuration
  map<string, string> new_config = 7;
}

```

---
