# database_config Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 6
- **Messages**: 6
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [cache_config.proto](#cache_config)
- [cockroach_config.proto](#cockroach_config)
- [configure_policy_request.proto](#configure_policy_request)
- [configure_policy_response.proto](#configure_policy_response)
- [my_sql_config.proto](#my_sql_config)
- [pebble_config.proto](#pebble_config)
---


## Detailed Documentation

### cache_config.proto {#cache_config}

**Path**: `gcommon/v1/database/cache_config.proto` **Package**: `gcommon.v1.database` **Lines**: 48

**Messages** (1): `CacheCacheConfig`

**Imports** (4):

- `gcommon/v1/common/eviction_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_config.proto
// version: 1.0.0
// guid: lm2nopqr-34s5-6t7u-8v9w-0x1y2z3a4b5c

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/eviction_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Configuration settings for cache behavior.
 * Defines cache policies, limits, and operational parameters.
 */
message CacheCacheConfig {
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
  string name = 8 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### cockroach_config.proto {#cockroach_config}

**Path**: `gcommon/v1/database/cockroach_config.proto` **Package**: `gcommon.v1.database` **Lines**: 49

**Messages** (1): `CockroachConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cockroach_config.proto
// version: 1.0.0
// guid: a505881e-946a-4a19-9fd5-1e81405e1f73

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * CockroachConfig provides CockroachDB-specific connection configuration.
 * Includes retry behavior and identification options for robust connections.
 */
message CockroachConfig {
  // Host is the database host.
  string host = 1;

  // Port is the database port.
  int32 port = 2;

  // User is the database user.
  string user = 3;

  // Password is the database password.
  string password = 4;

  // Database is the database name.
  string database = 5;

  // SSLMode is the SSL mode.
  string ssl_mode = 6;

  // ApplicationName is the application name.
  string application_name = 7 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // RetryBackoffFactor is the retry backoff factor.
  float retry_backoff_factor = 8;

  // MaxRetries is the maximum number of retries.
  int32 max_retries = 9;
}
```

---

### configure_policy_request.proto {#configure_policy_request}

**Path**: `gcommon/v1/database/configure_policy_request.proto` **Package**: `gcommon.v1.database` **Lines**: 34

**Messages** (1): `ConfigurePolicyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/configure_policy_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174019

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to configure cache policies.
 */
message ConfigurePolicyRequest {
  // Namespace ID to configure
  string namespace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Eviction policy (LRU, LFU, FIFO, etc.)
  string eviction_policy = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum TTL in seconds
  int32 max_ttl_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Memory threshold for eviction (percentage)
  double memory_threshold_percent = 4 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Additional policy configuration
  map<string, string> policy_config = 5;
}
```

---

### configure_policy_response.proto {#configure_policy_response}

**Path**: `gcommon/v1/database/configure_policy_response.proto` **Package**: `gcommon.v1.database` **Lines**: 41

**Messages** (1): `ConfigurePolicyResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/configure_policy_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174020

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for configuring cache policies.
 */
message ConfigurePolicyResponse {
  // Namespace ID that was configured
  string namespace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Applied eviction policy
  string eviction_policy = 2 [(buf.validate.field).string.min_len = 1];

  // Applied maximum TTL
  int32 max_ttl_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Applied memory threshold
  double memory_threshold_percent = 4 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // When the policy was applied
  google.protobuf.Timestamp applied_at = 5;

  // Previous policy configuration
  map<string, string> previous_config = 6;

  // New policy configuration
  map<string, string> new_config = 7;
}
```

---

### my_sql_config.proto {#my_sql_config}

**Path**: `gcommon/v1/database/my_sql_config.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `MySQLConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/my_sql_config.proto
// version: 1.0.0
// guid: 7950ed79-355d-451e-a539-59a2306f882a
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * MySQLConfig defines connection parameters for MySQL databases.
 */
message MySQLConfig {
  // MySQL connection DSN string
  string dsn = 1 [(buf.validate.field).string.min_len = 1];

  // Maximum number of open connections
  int32 max_open_conns = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum number of idle connections
  int32 max_idle_conns = 3 [(buf.validate.field).int32.gte = 0];

  // Connection timeout in seconds
  int32 connect_timeout_seconds = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### pebble_config.proto {#pebble_config}

**Path**: `gcommon/v1/database/pebble_config.proto` **Package**: `gcommon.v1.database` **Lines**: 35

**Messages** (1): `PebbleConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/pebble_config.proto
// version: 1.0.0
// guid: 3d548f91-9c4d-4fe7-b610-fd2cafd073ef

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * PebbleConfig represents Pebble-specific configuration options
 * for the embedded key-value store driver.
 */
message PebbleConfig {
  // Path is the directory where the database files are stored
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // CacheSize is the size of the block cache in bytes
  int64 cache_size = 2 [(buf.validate.field).int64.gte = 0];

  // MemtableSize is the memtable size in bytes
  int64 memtable_size = 3 [(buf.validate.field).int64.gte = 0];

  // MaxOpenFiles is the maximum number of open files
  int32 max_open_files = 4 [(buf.validate.field).int32.gte = 0];

  // Compression enables on-disk compression when true
  bool compression = 5;
}
```

---

