# database Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 24
- **Messages**: 24
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [cache_entry.proto](#cache_entry)
- [cache_info.proto](#cache_info)
- [cache_metrics.proto](#cache_metrics)
- [cache_operation_result.proto](#cache_operation_result)
- [cache_stats.proto](#cache_stats)
- [column_metadata.proto](#column_metadata)
- [connection_pool_info.proto](#connection_pool_info)
- [database_info.proto](#database_info)
- [database_status.proto](#database_status)
- [eviction_result.proto](#eviction_result)
- [execute_options.proto](#execute_options)
- [execute_stats.proto](#execute_stats)
- [migration_info.proto](#migration_info)
- [migration_script.proto](#migration_script)
- [my_sql_status.proto](#my_sql_status)
- [namespace_info.proto](#namespace_info)
- [namespace_stats.proto](#namespace_stats)
- [pool_stats.proto](#pool_stats)
- [query_options.proto](#query_options)
- [query_parameter.proto](#query_parameter)
- [query_stats.proto](#query_stats)
- [result_set.proto](#result_set)
- [row.proto](#row)
- [transaction_options.proto](#transaction_options)
---


## Detailed Documentation

### cache_entry.proto {#cache_entry}

**Path**: `gcommon/v1/database/cache_entry.proto` **Package**: `gcommon.v1.database` **Lines**: 48

**Messages** (1): `CacheEntry`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_entry.proto
// version: 1.0.0
// guid: c95add2b-ab62-455e-99d1-100c51e3a325
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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
  google.protobuf.Timestamp created_at = 3 [lazy = true, (buf.validate.field).required = true];

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

**Path**: `gcommon/v1/database/cache_info.proto` **Package**: `gcommon.v1.database` **Lines**: 51

**Messages** (1): `CacheInfo`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_info.proto
// version: 1.0.0
// guid: no4pqrst-56u7-8v9w-0x1y-2z3a4b5c6d7e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * General cache information and metadata.
 * Provides cache instance details and operational status.
 */
message CacheInfo {
  // Cache instance name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cache version
  string version = 2;

  // Cache type (e.g., "memory", "redis", "memcached")
  string cache_type = 3;

  // Current health status
  gcommon.v1.common.CommonHealthStatus health_status = 4;

  // Cache creation timestamp
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // Last access timestamp
  google.protobuf.Timestamp last_accessed = 6;

  // Cache instance ID
  string instance_id = 7;

  // Cache description
  string description = 8 [ (buf.validate.field).string.max_len = 1000 ];

  // Additional metadata
  map<string, string> metadata = 9;
}
```

---

### cache_metrics.proto {#cache_metrics}

**Path**: `gcommon/v1/database/cache_metrics.proto` **Package**: `gcommon.v1.database` **Lines**: 61

**Messages** (1): `CacheMetrics`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_metrics.proto
// version: 1.0.0
// guid: pq6rstuv-78w9-0x1y-2z3a-4b5c6d7e8f9g

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Detailed cache performance metrics.
 * Provides comprehensive metrics for cache monitoring and optimization.
 */
message CacheMetrics {
  // Operations per second
  double ops_per_second = 1 [(buf.validate.field).double.gte = 0.0];

  // Read operations per second
  double reads_per_second = 2 [(buf.validate.field).double.gte = 0.0];

  // Write operations per second
  double writes_per_second = 3 [(buf.validate.field).double.gte = 0.0];

  // Average response time
  google.protobuf.Duration avg_response_time = 4;

  // 95th percentile response time
  google.protobuf.Duration p95_response_time = 5;

  // 99th percentile response time
  google.protobuf.Duration p99_response_time = 6;

  // Total number of connections
  int64 total_connections = 7 [(buf.validate.field).int64.gte = 0];

  // Active connections
  int64 active_connections = 8 [(buf.validate.field).int64.gte = 0];

  // Network bytes received
  int64 network_bytes_in = 9 [(buf.validate.field).int64.gte = 0];

  // Network bytes sent
  int64 network_bytes_out = 10 [(buf.validate.field).int64.gte = 0];

  // CPU usage percentage
  double cpu_usage_percent = 11 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Memory usage percentage
  double memory_usage_percent = 12 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Timestamp of metrics collection
  google.protobuf.Timestamp collected_at = 13;
}
```

---

### cache_operation_result.proto {#cache_operation_result}

**Path**: `gcommon/v1/database/cache_operation_result.proto` **Package**: `gcommon.v1.database` **Lines**: 49

**Messages** (1): `CacheOperationResult`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_operation_result.proto
// version: 1.0.0
// guid: qr7stuvw-89x0-1y2z-3a4b-5c6d7e8f9g0h

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Result of cache operations.
 * Provides detailed outcome information for cache operations.
 */
message CacheOperationResult {
  // Whether the operation was successful
  bool success = 1;

  // Operation type (e.g., "GET", "SET", "DELETE")
  string operation_type = 2 [(buf.validate.field).string.min_len = 1];

  // Key involved in the operation
  string key = 3 [(buf.validate.field).string.min_len = 1];

  // Namespace (if applicable)
  string namespace = 4 [(buf.validate.field).string.min_len = 1];

  // Operation duration
  int64 duration_microseconds = 5 [(buf.validate.field).int64.gt = 0];

  // Timestamp of operation
  google.protobuf.Timestamp timestamp = 6;

  // Number of items affected
  int64 items_affected = 7 [(buf.validate.field).int64.gte = 0];

  // Error details if operation failed
  gcommon.v1.common.Error error = 8;

  // Additional operation metadata
  map<string, string> metadata = 9;
}
```

---

### cache_stats.proto {#cache_stats}

**Path**: `gcommon/v1/database/cache_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 54

**Messages** (1): `CacheStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_stats.proto
// version: 1.0.0
// guid: mn3opqrs-45t6-7u8v-9w0x-1y2z3a4b5c6d

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Cache statistics and performance metrics.
 * Provides detailed information about cache usage and performance.
 */
message CacheStats {
  // Total number of cached items
  int64 total_items = 1 [(buf.validate.field).int64.gte = 0];

  // Total cache hits
  int64 cache_hits = 2 [(buf.validate.field).int64.gte = 0];

  // Total cache misses
  int64 cache_misses = 3 [(buf.validate.field).int64.gte = 0];

  // Cache hit ratio (0.0 to 1.0)
  double hit_ratio = 4 [(buf.validate.field).double.gte = 0.0];

  // Memory usage in bytes
  int64 memory_usage = 5 [(buf.validate.field).int64.gte = 0];

  // Maximum memory limit in bytes
  int64 memory_limit = 6 [(buf.validate.field).int64.gte = 0];

  // Number of evicted items
  int64 evicted_items = 7 [(buf.validate.field).int64.gte = 0];

  // Number of expired items
  int64 expired_items = 8 [(buf.validate.field).int64.gte = 0];

  // Average access time in milliseconds
  double avg_access_time_ms = 9 [(buf.validate.field).double.gte = 0.0];

  // Last reset timestamp
  google.protobuf.Timestamp last_reset = 10;

  // Cache uptime in seconds
  int64 uptime_seconds = 11 [(buf.validate.field).int64.gte = 0];
}
```

---

### column_metadata.proto {#column_metadata}

**Path**: `gcommon/v1/database/column_metadata.proto` **Package**: `gcommon.v1.database` **Lines**: 39

**Messages** (1): `ColumnMetadata`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/column_metadata.proto
// version: 1.0.0
// guid: d06d164a-51bd-4f22-b1db-15171a8dd72d
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ColumnMetadata describes the structure and properties of a database column.
 * Used in result sets to provide type information for proper data handling.
 */
message ColumnMetadata {
  // Column name as defined in the database
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Column data type (database-specific)
  string type = 2;

  // Whether the column allows NULL values
  bool nullable = 3;

  // Column size/precision for numeric and string types
  int32 size = 4;

  // Column scale for decimal/numeric types
  int32 scale = 5;

  // Additional column-specific metadata
  map<string, string> metadata = 6 [lazy = true];
}
```

---

### connection_pool_info.proto {#connection_pool_info}

**Path**: `gcommon/v1/database/connection_pool_info.proto` **Package**: `gcommon.v1.database` **Lines**: 36

**Messages** (1): `ConnectionPoolInfo`

**Imports** (4):

- `gcommon/v1/database/pool_stats.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/connection_pool_info.proto
// version: 1.0.0
// guid: 96aea9f8-77e8-4342-87af-6a00947ef1b0
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/pool_stats.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ConnectionPoolInfo provides information about database connection pool status.
 * Used for monitoring connection health and pool performance.
 */
message ConnectionPoolInfo {
  // Maximum number of connections allowed in the pool
  int32 max_connections = 1 [(buf.validate.field).int32.gte = 0];

  // Number of currently active connections
  int32 active_connections = 2 [(buf.validate.field).int32.gte = 0];

  // Number of idle connections in the pool
  int32 idle_connections = 3 [(buf.validate.field).int32.gte = 0];

  // Average lifetime of connections in the pool
  google.protobuf.Duration avg_lifetime = 4 [lazy = true];

  // Detailed connection pool statistics
  PoolStats stats = 5 [lazy = true];
}
```

---

### database_info.proto {#database_info}

**Path**: `gcommon/v1/database/database_info.proto` **Package**: `gcommon.v1.database` **Lines**: 36

**Messages** (1): `DatabaseInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/database_info.proto
// version: 1.0.0
// guid: 4bce9e15-4221-4e32-97a0-664f1f5fc777
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * DatabaseInfo provides metadata about a database instance.
 * Used for identifying database capabilities and connection details.
 */
message DatabaseInfo {
  // Database name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Database version information
  string version = 2;

  // Database type/vendor (e.g., PostgreSQL, MySQL, CockroachDB)
  string type = 3;

  // Sanitized connection string (credentials removed)
  string connection_string = 4;

  // List of supported database features
  repeated string features = 5;
}
```

---

### database_status.proto {#database_status}

**Path**: `gcommon/v1/database/database_status.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `DatabaseStatus`

**Imports** (3):

- `gcommon/v1/common/database_status_code.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/database_status.proto
// version: 1.0.0
// guid: 67bfa96b-764e-4290-adc8-2387c9b456b4

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/database_status_code.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * DatabaseStatus reports the current connection status for a
 * database driver or service.
 */
message DatabaseStatus {
  // Code indicates the health state of the database
  gcommon.v1.common.DatabaseStatusCode code = 1;

  // Human readable status details
  string message = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### eviction_result.proto {#eviction_result}

**Path**: `gcommon/v1/database/eviction_result.proto` **Package**: `gcommon.v1.database` **Lines**: 43

**Messages** (1): `EvictionResult`

**Imports** (4):

- `gcommon/v1/common/eviction_policy.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/eviction_result.proto
// version: 1.0.0
// guid: op5qrstu-67v8-9w0x-1y2z-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/eviction_policy.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Result of cache eviction operations.
 * Provides details about items removed from cache.
 */
message EvictionResult {
  // Number of items evicted
  int64 evicted_count = 1 [(buf.validate.field).int64.gte = 0];

  // List of evicted keys
  repeated string evicted_keys = 2 [(buf.validate.field).repeated.min_items = 1];

  // Eviction policy used
  gcommon.v1.common.EvictionPolicy policy_used = 3;

  // Reason for eviction
  string eviction_reason = 4 [(buf.validate.field).string.min_len = 1];

  // Timestamp of eviction
  google.protobuf.Timestamp evicted_at = 5;

  // Memory freed by eviction (bytes)
  int64 memory_freed = 6 [(buf.validate.field).int64.gte = 0];

  // Whether eviction was successful
  bool success = 7;
}
```

---

### execute_options.proto {#execute_options}

**Path**: `gcommon/v1/database/execute_options.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `ExecuteOptions`

**Imports** (3):

- `gcommon/v1/common/database_isolation_level.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/execute_options.proto
// version: 1.0.1
// guid: 8442b047-87bf-4004-a060-60b8ca1da578
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/database_isolation_level.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ExecuteOptions configures behavior for database execute operations.
 * Controls timeouts, transaction isolation, and result handling.
 */
message ExecuteOptions {
  // Execution timeout for the operation
  google.protobuf.Duration timeout = 1 [lazy = true];

  // Whether to return generated keys (for INSERT operations)
  bool return_generated_keys = 2;

  // Isolation level for transaction operations
  gcommon.v1.common.DatabaseIsolationLevel isolation = 3;
}
```

---

### execute_stats.proto {#execute_stats}

**Path**: `gcommon/v1/database/execute_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `ExecuteStats`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/execute_stats.proto
// version: 1.0.0
// guid: f5aa4c14-0881-4b49-ac30-21e7699e68be
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ExecuteStats provides execution statistics for database operations.
 * Used for performance monitoring and operation optimization.
 */
message ExecuteStats {
  // Total execution time for the operation
  google.protobuf.Duration execution_time = 1 [lazy = true];

  // Number of rows affected by the operation
  int64 affected_rows = 2 [(buf.validate.field).int64.gte = 0];

  // Estimated cost of operation execution
  double cost_estimate = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### migration_info.proto {#migration_info}

**Path**: `gcommon/v1/database/migration_info.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `MigrationInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/migration_info.proto
// version: 1.0.0
// guid: 4b59457d-20d4-4134-af01-340fe289787e

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * MigrationInfo provides metadata about an applied or pending migration.
 */
message MigrationInfo {
  // Version identifier of the migration
  string version = 1;

  // Descriptive name of the migration
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Timestamp when the migration was applied
  google.protobuf.Timestamp applied_at = 3;
}
```

---

### migration_script.proto {#migration_script}

**Path**: `gcommon/v1/database/migration_script.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `MigrationScript`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/migration_script.proto
// version: 1.0.0
// guid: 29854789-0235-4d1e-9031-989570ae161d
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * MigrationScript represents a database migration script with version control.
 * Used for managing database schema changes and data migrations.
 */
message MigrationScript {
  // Migration version identifier
  string version = 1;

  // SQL script or migration commands
  string script = 2;

  // Human-readable description of the migration
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### my_sql_status.proto {#my_sql_status}

**Path**: `gcommon/v1/database/my_sql_status.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `MySQLStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/my_sql_status.proto
// version: 1.0.0
// guid: 41592093-2b89-4742-af88-e1590168c2ee
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * MySQLStatus provides runtime metrics and server version information.
 */
message MySQLStatus {
  // Server version string
  string version = 1 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Server start time
  google.protobuf.Timestamp started_at = 2;

  // Number of open connections
  int32 open_connections = 3 [(buf.validate.field).int32.gte = 0];

  // Replication role (e.g., master, replica)
  string role = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### namespace_info.proto {#namespace_info}

**Path**: `gcommon/v1/database/namespace_info.proto` **Package**: `gcommon.v1.database` **Lines**: 40

**Messages** (1): `NamespaceInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/namespace_info.proto
// version: 1.0.0
// guid: 99ca4ced-3db8-4b4d-a745-b9f6a699357d

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message NamespaceInfo {
  // ID of the namespace
  string namespace_id = 1;

  // Name of the namespace
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // When created
  google.protobuf.Timestamp created_at = 4 [ (buf.validate.field).required = true ];

  // Current key count
  int64 current_keys = 5;

  // Current memory usage (bytes)
  int64 current_memory_bytes = 6;

  // Configuration
  map<string, string> config = 7;
}
```

---

### namespace_stats.proto {#namespace_stats}

**Path**: `gcommon/v1/database/namespace_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 44

**Messages** (1): `NamespaceStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/namespace_stats.proto
// version: 1.0.0
// guid: 17ab825b-e172-494b-a8b3-a410bf866ed3

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message NamespaceStats {
  // Total keys in namespace
  int64 total_keys = 1 [(buf.validate.field).int64.gte = 0];

  // Memory usage in bytes
  int64 memory_usage_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Hit rate percentage
  double hit_rate_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Cache hits
  int64 cache_hits = 4 [(buf.validate.field).int64.gte = 0];

  // Cache misses
  int64 cache_misses = 5 [(buf.validate.field).int64.gte = 0];

  // Evictions
  int64 evictions = 6 [(buf.validate.field).int64.gte = 0];

  // Average key size
  double avg_key_size_bytes = 7 [(buf.validate.field).double.gte = 0.0];

  // Average value size
  double avg_value_size_bytes = 8 [(buf.validate.field).double.gte = 0.0];

  // Last access time
  google.protobuf.Timestamp last_access_time = 9;
}
```

---

### pool_stats.proto {#pool_stats}

**Path**: `gcommon/v1/database/pool_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `PoolStats`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/pool_stats.proto
// version: 1.0.0
// guid: aa9c4de3-12a9-4aa4-a381-051dab476fa1
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * PoolStats provides detailed statistics about connection pool usage.
 * Used for monitoring pool efficiency and connection management.
 */
message PoolStats {
  // Total number of connections created since pool initialization
  int64 total_created = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of connections closed since pool initialization
  int64 total_closed = 2 [(buf.validate.field).int64.gte = 0];

  // Number of failed attempts to acquire connections
  int64 acquisition_failures = 3 [(buf.validate.field).int64.gte = 0];

  // Average time to acquire a connection from the pool
  google.protobuf.Duration avg_acquisition_time = 4 [lazy = true];
}
```

---

### query_options.proto {#query_options}

**Path**: `gcommon/v1/database/query_options.proto` **Package**: `gcommon.v1.database` **Lines**: 36

**Messages** (1): `QueryOptions`

**Imports** (4):

- `gcommon/v1/common/consistency_level.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_options.proto
// version: 1.0.0
// guid: 0370003e-a0f1-4704-a267-885654ec1dd8
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/consistency_level.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * QueryOptions configures behavior for database query operations.
 * Controls result limits, timeouts, and consistency requirements.
 */
message QueryOptions {
  // Maximum number of rows to return
  int32 limit = 1 [(buf.validate.field).int32.gte = 0];

  // Number of rows to skip for pagination
  int32 offset = 2 [(buf.validate.field).int32.gte = 0];

  // Query execution timeout
  google.protobuf.Duration timeout = 3 [lazy = true];

  // Whether to include column metadata in response
  bool include_metadata = 4;

  // Read consistency level for the query
  gcommon.v1.common.DatabaseConsistencyLevel consistency = 5;
}
```

---

### query_parameter.proto {#query_parameter}

**Path**: `gcommon/v1/database/query_parameter.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `QueryParameter`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_parameter.proto
// version: 1.0.0
// guid: 1b5e1d5c-6969-439e-ac9a-7130cfe0d560
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * QueryParameter represents a parameter for parameterized queries.
 * Supports typed parameters to prevent SQL injection and improve performance.
 */
message QueryParameter {
  // Parameter name for named parameters
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Parameter value as Any type for flexibility
  google.protobuf.Any value = 2 [lazy = true];

  // Optional type hint for better query optimization
  string type = 3;
}
```

---

### query_stats.proto {#query_stats}

**Path**: `gcommon/v1/database/query_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 35

**Messages** (1): `DatabaseQueryStats`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_stats.proto
// version: 1.0.0
// guid: 910cc013-78cc-4062-b329-3b767b0516b2
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * QueryStats provides execution statistics for database queries.
 * Used for performance monitoring and query optimization.
 */
message DatabaseQueryStats {
  // Total execution time for the query
  google.protobuf.Duration execution_time = 1 [lazy = true];

  // Number of rows returned by the query
  int64 row_count = 2 [(buf.validate.field).int64.gte = 0];

  // Number of columns in the result set
  int32 column_count = 3 [(buf.validate.field).int32.gte = 0];

  // Query execution plan (if available)
  string query_plan = 4 [(buf.validate.field).string.min_len = 1];

  // Estimated cost of query execution
  double cost_estimate = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### result_set.proto {#result_set}

**Path**: `gcommon/v1/database/result_set.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `ResultSet`

**Imports** (4):

- `gcommon/v1/database/column_metadata.proto`
- `gcommon/v1/database/row.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/result_set.proto
// version: 1.0.1
// guid: b4dc4847-4e57-46b9-bcf0-f74e86882c0a
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/column_metadata.proto";
import "gcommon/v1/database/row.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ResultSet contains the results of a database query operation.
 * Includes column metadata, data rows, and pagination information.
 */
message ResultSet {
  // Metadata for each column in the result set
  repeated ColumnMetadata columns = 1 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Data rows matching the query
  repeated Row rows = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Total row count if known (for pagination)
  int64 total_count = 3 [(buf.validate.field).int64.gte = 0];

  // Whether more rows are available beyond this result set
  bool has_more = 4;
}
```

---

### row.proto {#row}

**Path**: `gcommon/v1/database/row.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `Row`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/row.proto
// version: 1.0.1
// guid: b3495bf9-4671-40b0-8d44-3fe8f9aac6ca
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Row represents a single row of data from a database result set.
 * Contains column values in the same order as defined in ColumnMetadata.
 */
message Row {
  // Column values in order matching the column metadata
  repeated google.protobuf.Any values = 1 [lazy = true, (buf.validate.field).repeated.min_items = 1];
}
```

---

### transaction_options.proto {#transaction_options}

**Path**: `gcommon/v1/database/transaction_options.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `TransactionOptions`

**Imports** (3):

- `gcommon/v1/common/database_isolation_level.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/transaction_options.proto
// version: 1.0.1
// guid: 6e13a9a6-2870-4e4c-91c0-a16cee8a0b50
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/database_isolation_level.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * TransactionOptions configures behavior for database transactions.
 * Controls isolation level, timeout, and read-only mode.
 */
message TransactionOptions {
  // Isolation level for the transaction
  gcommon.v1.common.DatabaseIsolationLevel isolation = 1;

  // Transaction timeout before automatic rollback
  google.protobuf.Duration timeout = 2 [lazy = true];

  // Whether this is a read-only transaction
  bool read_only = 3;
}
```

---

