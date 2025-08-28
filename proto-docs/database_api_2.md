# database_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [get_request.proto](#get_request)
- [get_response.proto](#get_response)
- [get_stats_request.proto](#get_stats_request)
- [get_stats_response.proto](#get_stats_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [import_request.proto](#import_request)
- [increment_request.proto](#increment_request)
- [increment_response.proto](#increment_response)
- [info_request.proto](#info_request)
- [keys_request.proto](#keys_request)
- [keys_response.proto](#keys_response)
- [list_databases_request.proto](#list_databases_request)
- [list_databases_response.proto](#list_databases_response)
- [list_migrations_request.proto](#list_migrations_request)
- [list_migrations_response.proto](#list_migrations_response)
- [list_namespaces_request.proto](#list_namespaces_request)
- [list_namespaces_response.proto](#list_namespaces_response)
- [list_schemas_request.proto](#list_schemas_request)
- [list_schemas_response.proto](#list_schemas_response)
- [list_subscriptions_request.proto](#list_subscriptions_request)
- [lock_request.proto](#lock_request)
- [m_get_request.proto](#m_get_request)
- [optimize_request.proto](#optimize_request)
- [pipeline_request.proto](#pipeline_request)
- [prepend_request.proto](#prepend_request)
- [publish_request.proto](#publish_request)
- [query_request.proto](#query_request)
- [query_response.proto](#query_response)
- [query_row_request.proto](#query_row_request)
- [query_row_response.proto](#query_row_response)
- [restore_request.proto](#restore_request)
- [revert_migration_request.proto](#revert_migration_request)
- [revert_migration_response.proto](#revert_migration_response)
- [rollback_transaction_request.proto](#rollback_transaction_request)
- [run_migration_request.proto](#run_migration_request)
- [run_migration_response.proto](#run_migration_response)
- [scan_request.proto](#scan_request)
- [set_multiple_request.proto](#set_multiple_request)
- [set_multiple_response.proto](#set_multiple_response)
- [set_options.proto](#set_options)
- [set_request.proto](#set_request)
- [set_response.proto](#set_response)
- [subscribe_request.proto](#subscribe_request)
- [touch_expiration_request.proto](#touch_expiration_request)
- [touch_expiration_response.proto](#touch_expiration_response)
- [transaction_request.proto](#transaction_request)
- [transaction_status_request.proto](#transaction_status_request)
- [transaction_status_response.proto](#transaction_status_response)
- [unlock_request.proto](#unlock_request)
---


## Detailed Documentation

### get_request.proto {#get_request}

**Path**: `gcommon/v1/database/get_request.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `GetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_request.proto
// version: 1.0.0
// guid: 5277ac94-ab80-4548-a6ca-3a8b98e038c4
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to retrieve a cached value by key.
 * Supports namespace isolation and access time tracking
 * for LRU cache policies.
 */
message GetRequest {
  // Cache key to retrieve
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace for cache isolation
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];

  // Whether to update access time (for LRU policies)
  bool update_access_time = 4;
}
```

---

### get_response.proto {#get_response}

**Path**: `gcommon/v1/database/get_response.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `GetResponse`

**Imports** (2):

- `gcommon/v1/database/cache_entry.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_response.proto
// version: 1.0.1
// guid: d92e32a6-96eb-4e6c-a56b-6b9a9c54ba6a
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/cache_entry.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

### get_stats_request.proto {#get_stats_request}

**Path**: `gcommon/v1/database/get_stats_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `CacheGetStatsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_stats_request.proto
// version: 1.0.0
// guid: 58717dfd-f988-42e8-8720-ecfdb5ab542c
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to retrieve cache statistics.
 */
message CacheGetStatsRequest {
  // Optional namespace filter
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_stats_response.proto {#get_stats_response}

**Path**: `gcommon/v1/database/get_stats_response.proto` **Package**: `gcommon.v1.database` **Lines**: 48

**Messages** (1): `CacheGetStatsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_stats_response.proto
// version: 1.0.0
// guid: hi8jklmn-90o1-2p3q-4r5s-6t7u8v9w0x1y

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache statistics operations.
 * Provides detailed cache performance metrics.
 */
message CacheGetStatsResponse {
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

  // Whether the operation was successful
  bool success = 8;

  // Error details if stats retrieval failed
  gcommon.v1.common.Error error = 9;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/database/health_check_request.proto` **Package**: `gcommon.v1.database` **Lines**: 18

**Messages** (1): `DatabaseHealthCheckRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/health_check_request.proto
// version: 1.0.1
// guid: ad313d88-e21f-4b72-8844-1e5fdafefd4e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message DatabaseHealthCheckRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/database/health_check_response.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `DatabaseHealthCheckResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/health_check_response.proto
// version: 1.0.1
// guid: e1d2c65f-544c-4adf-b3cd-949e155bed14
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * HealthCheckResponse contains the result of a database health check.
 * Provides connection status, response time, and error details.
 */
message DatabaseHealthCheckResponse {
  // Overall health status of the database
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Whether the database connection is operational
  bool connection_ok = 2;

  // Time taken to perform the health check
  google.protobuf.Duration response_time = 3 [lazy = true];

  // Error information if the health check failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### import_request.proto {#import_request}

**Path**: `gcommon/v1/database/import_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `ImportRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/import_request.proto
// version: 1.0.0
// guid: 97a06666-8fd5-4e65-b830-1f8b94bd2a50
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to import cache contents from an external source.
 */
message ImportRequest {
  // Source location of the data
  string source = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace to import into
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### increment_request.proto {#increment_request}

**Path**: `gcommon/v1/database/increment_request.proto` **Package**: `gcommon.v1.database` **Lines**: 38

**Messages** (1): `IncrementRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/increment_request.proto
// version: 1.0.0
// guid: f128cf36-e0d8-40e0-894b-ae3339e9bd7f
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to increment a cached counter atomically.
 */
message IncrementRequest {
  // Counter key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Increment delta (can be negative)
  int64 delta = 2 [(buf.validate.field).int64.gte = 0];

  // Initial value if key doesn't exist
  int64 initial_value = 3 [(buf.validate.field).int64.gte = 0];

  // TTL for the counter
  google.protobuf.Duration ttl = 4 [lazy = true];

  // Optional namespace
  string namespace = 5 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 6 [lazy = true];
}
```

---

### increment_response.proto {#increment_response}

**Path**: `gcommon/v1/database/increment_response.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `IncrementResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/increment_response.proto
// version: 1.0.0
// guid: bc2defgh-34i5-6j7k-8l9m-0n1o2p3q4r5s

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache increment operations.
 * Returns the new value after incrementing.
 */
message IncrementResponse {
  // The new value after incrementing
  int64 new_value = 1 [(buf.validate.field).int64.gte = 0];

  // Whether the operation was successful
  bool success = 2;

  // Error details if increment failed
  gcommon.v1.common.Error error = 3;
}
```

---

### info_request.proto {#info_request}

**Path**: `gcommon/v1/database/info_request.proto` **Package**: `gcommon.v1.database` **Lines**: 20

**Messages** (1): `InfoRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/info_request.proto
// version: 1.0.1
// guid: ab9ee789-34ee-4b13-9a9e-ab0fbed3f5f2
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

**Path**: `gcommon/v1/database/keys_request.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `KeysRequest`

**Imports** (4):

- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/keys_request.proto
// version: 1.0.0
// guid: 52aedf5e-c6a7-42f0-8d7c-8ebc4d679a3b
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to list cache keys matching a pattern.
 */
message KeysRequest {
  // Key pattern to match (supports wildcards)
  string pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Pagination options
  gcommon.v1.common.Pagination pagination = 3 [lazy = true];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### keys_response.proto {#keys_response}

**Path**: `gcommon/v1/database/keys_response.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `KeysResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/keys_response.proto
// version: 1.0.0
// guid: fg6hijkl-78m9-0n1o-2p3q-4r5s6t7u8v9w

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache keys listing operations.
 * Returns all matching keys from the cache.
 */
message KeysResponse {
  // List of keys matching the pattern
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of keys found
  int64 total_count = 2 [(buf.validate.field).int64.gte = 0];

  // Whether the operation was successful
  bool success = 3;

  // Error details if keys retrieval failed
  gcommon.v1.common.Error error = 4;
}
```

---

### list_databases_request.proto {#list_databases_request}

**Path**: `gcommon/v1/database/list_databases_request.proto` **Package**: `gcommon.v1.database` **Lines**: 18

**Messages** (1): `ListDatabasesRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/list_databases_request.proto
// version: 1.0.1
// guid: d893dba4-db7c-410b-bdf0-94c27a7dc1ee

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message ListDatabasesRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### list_databases_response.proto {#list_databases_response}

**Path**: `gcommon/v1/database/list_databases_response.proto` **Package**: `gcommon.v1.database` **Lines**: 22

**Messages** (1): `ListDatabasesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/list_databases_response.proto
// version: 1.0.0
// guid: 36e09c07-048c-463e-bd22-902a4dbed6a9
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ListDatabasesResponse contains the list of available databases.
 * Provides database names accessible to the authenticated user.
 */
message ListDatabasesResponse {
  // List of database names
  repeated string databases = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### list_migrations_request.proto {#list_migrations_request}

**Path**: `gcommon/v1/database/list_migrations_request.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `ListMigrationsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/list_migrations_request.proto
// version: 1.0.0
// guid: e09ee131-1388-41e5-973c-3c7eb4308349

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message ListMigrationsRequest {
  // Database name to list migrations for
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Return only applied or pending migrations (optional)
  string status_filter = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### list_migrations_response.proto {#list_migrations_response}

**Path**: `gcommon/v1/database/list_migrations_response.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `ListMigrationsResponse`

**Imports** (3):

- `gcommon/v1/database/migration_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/list_migrations_response.proto
// version: 1.0.1
// guid: 2d1040e2-056b-4264-8f84-d731b345d924

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/migration_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ListMigrationsResponse returns a list of migrations for a database.
 */
message ListMigrationsResponse {
  // List of migration metadata entries
  repeated MigrationInfo migrations = 1 [lazy = true, (buf.validate.field).repeated.min_items = 1];
}
```

---

### list_namespaces_request.proto {#list_namespaces_request}

**Path**: `gcommon/v1/database/list_namespaces_request.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `ListNamespacesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/list_namespaces_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174015

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to list cache namespaces.
 */
message ListNamespacesRequest {
  // Page number (starting from 1)
  int32 page = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items per page
  int32 page_size = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Filter by name pattern
  string name_filter = 3 [(buf.validate.field).string.min_len = 1];

  // Include detailed statistics
  bool include_stats = 4;
}
```

---

### list_namespaces_response.proto {#list_namespaces_response}

**Path**: `gcommon/v1/database/list_namespaces_response.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `ListNamespacesResponse`

**Imports** (3):

- `gcommon/v1/database/namespace_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/list_namespaces_response.proto
// version: 1.0.0
// guid: 4b616806-7b7b-4186-94bf-981b0e229c1c

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/namespace_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message ListNamespacesResponse {
  // List of namespaces
  repeated NamespaceInfo namespaces = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count
  int32 total_count = 2 [(buf.validate.field).int32.gte = 0];

  // Current page
  int32 page = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Page size
  int32 page_size = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total pages
  int32 total_pages = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
}
```

---

### list_schemas_request.proto {#list_schemas_request}

**Path**: `gcommon/v1/database/list_schemas_request.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `ListSchemasRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/list_schemas_request.proto
// version: 1.0.0
// guid: 98a59d16-8985-401b-96a8-07c9f542435d

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message ListSchemasRequest {
  // Database name to list schemas from
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### list_schemas_response.proto {#list_schemas_response}

**Path**: `gcommon/v1/database/list_schemas_response.proto` **Package**: `gcommon.v1.database` **Lines**: 22

**Messages** (1): `ListSchemasResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/list_schemas_response.proto
// version: 1.0.0
// guid: c25c875d-b542-4abd-8778-17d88c9d22cc
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ListSchemasResponse contains the list of schemas within a database.
 * Provides schema names available in the specified database.
 */
message ListSchemasResponse {
  // List of schema names in the database
  repeated string schemas = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### list_subscriptions_request.proto {#list_subscriptions_request}

**Path**: `gcommon/v1/database/list_subscriptions_request.proto` **Package**: `gcommon.v1.database` **Lines**: 20

**Messages** (1): `CacheListSubscriptionsRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/list_subscriptions_request.proto
// version: 1.0.1
// guid: c49e8f0c-687d-4f5f-8261-7550969111d9
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to list active cache subscriptions.
 */
message CacheListSubscriptionsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### lock_request.proto {#lock_request}

**Path**: `gcommon/v1/database/lock_request.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `LockRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/lock_request.proto
// version: 1.0.0
// guid: 53613615-702b-470a-b522-8173cb458d12
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to acquire a cache lock.
 */
message LockRequest {
  // Lock key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Lock expiration
  google.protobuf.Duration ttl = 2 [lazy = true];

  // Optional namespace
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### m_get_request.proto {#m_get_request}

**Path**: `gcommon/v1/database/m_get_request.proto` **Package**: `gcommon.v1.database` **Lines**: 39

**Messages** (1): `MGetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/config/m_get_request.proto
// version: 1.0.0
// guid: e61074f0-5ce0-44d1-b0e5-b8eb49bc97a3
// file: proto/gcommon/v1/database/m_get_request.proto
//
// Multi-get request definitions for cache module
//
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * MGetRequest is used to retrieve multiple cache entries in a single operation.
 * This is more efficient than multiple individual Get operations.
 */
message MGetRequest {
  // List of keys to retrieve
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Namespace to search in (optional)
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

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

**Path**: `gcommon/v1/database/optimize_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `OptimizeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/optimize_request.proto
// version: 1.0.0
// guid: 3dfdfacc-5cc8-48f5-9df4-adb442034b47
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to optimize cache storage layout.
 */
message OptimizeRequest {
  // Optional namespace to optimize
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### pipeline_request.proto {#pipeline_request}

**Path**: `gcommon/v1/database/pipeline_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `PipelineRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/pipeline_request.proto
// version: 1.0.0
// guid: c4ed1ac6-29fd-4359-851f-e9f73d6926c5
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to execute a batch of cache operations atomically.
 */
message PipelineRequest {
  // Encoded operations in execution order
  bytes operations = 1;

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### prepend_request.proto {#prepend_request}

**Path**: `gcommon/v1/database/prepend_request.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `PrependRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/prepend_request.proto
// version: 1.0.0
// guid: 5dff4515-b826-40e9-be87-fcc208e45acc
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to prepend data to an existing cache entry.
 */
message PrependRequest {
  // Cache key to modify
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Value to prepend
  google.protobuf.Any value = 2 [lazy = true];

  // Optional namespace
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### publish_request.proto {#publish_request}

**Path**: `gcommon/v1/database/publish_request.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `CachePublishRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/publish_request.proto
// version: 1.0.0
// guid: 90c22d73-f181-473b-9344-04cedb5afbbe
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to publish a value to cache subscribers.
 */
message CachePublishRequest {
  // Topic or channel name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Payload to publish
  google.protobuf.Any payload = 2 [lazy = true];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### query_request.proto {#query_request}

**Path**: `gcommon/v1/database/query_request.proto` **Package**: `gcommon.v1.database` **Lines**: 37

**Messages** (1): `QueryRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/database/query_options.proto`
- `gcommon/v1/database/query_parameter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_request.proto
// version: 1.0.1
// guid: 7c121670-ec19-444d-8042-91074225644d

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/database/query_options.proto";
import "gcommon/v1/database/query_parameter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message QueryRequest {
  // SQL query or NoSQL query string
  string query = 1 [(buf.validate.field).string.min_len = 1];

  // Query parameters for parameterized queries
  repeated QueryParameter parameters = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Database name (optional, uses default if not specified)
  string database = 3 [(buf.validate.field).string.min_len = 1];

  // Query execution options
  QueryOptions options = 4 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 5 [lazy = true];

  // Transaction ID if this query is part of a transaction
  string transaction_id = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### query_response.proto {#query_response}

**Path**: `gcommon/v1/database/query_response.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `QueryResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/database/query_stats.proto`
- `gcommon/v1/database/result_set.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_response.proto
// version: 1.0.1
// guid: 2dfa79e3-f38e-4708-b131-0f941eb755f8
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/database/query_stats.proto";
import "gcommon/v1/database/result_set.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * QueryResponse contains the results of a database query operation.
 * Includes result data, execution statistics, and error information.
 */
message QueryResponse {
  // Query result set with data and metadata
  ResultSet result_set = 1 [lazy = true];

  // Query execution statistics and performance metrics
  DatabaseQueryStats stats = 2 [lazy = true];

  // Error information if the query failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### query_row_request.proto {#query_row_request}

**Path**: `gcommon/v1/database/query_row_request.proto` **Package**: `gcommon.v1.database` **Lines**: 37

**Messages** (1): `QueryRowRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/database/query_options.proto`
- `gcommon/v1/database/query_parameter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_row_request.proto
// version: 1.0.1
// guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/database/query_options.proto";
import "gcommon/v1/database/query_parameter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message QueryRowRequest {
  // SQL query or NoSQL query string (should return at most one row)
  string query = 1 [(buf.validate.field).string.min_len = 1];

  // Query parameters for parameterized queries
  repeated QueryParameter parameters = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Database name (optional, uses default if not specified)
  string database = 3 [(buf.validate.field).string.min_len = 1];

  // Query execution options
  QueryOptions options = 4 [lazy = true];

  // Transaction ID if this query should be executed within a transaction
  string transaction_id = 5 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}
```

---

### query_row_response.proto {#query_row_response}

**Path**: `gcommon/v1/database/query_row_response.proto` **Package**: `gcommon.v1.database` **Lines**: 38

**Messages** (1): `QueryRowResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/database/query_stats.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/query_row_response.proto
// version: 1.0.1
// guid: dff9c212-0d7d-4f0a-bcca-8a0a641a29f9

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/database/query_stats.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * QueryRowResponse contains the result of a single-row query.
 * If no row was found, `found` will be false and `values` will be empty.
 */
message QueryRowResponse {
  // Indicates whether a row was found
  bool found = 1;

  // Column names matching the returned values
  repeated string columns = 2 [(buf.validate.field).repeated.min_items = 1];

  // Row values encoded as generic Any values
  repeated google.protobuf.Any values = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Query execution statistics
  DatabaseQueryStats stats = 4 [lazy = true];

  // Error information if the query failed
  gcommon.v1.common.Error error = 5 [lazy = true];
}
```

---

### restore_request.proto {#restore_request}

**Path**: `gcommon/v1/database/restore_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `RestoreRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/restore_request.proto
// version: 1.0.0
// guid: cd942141-18b5-4a0d-88b2-9c5fdf4f3cb0
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to restore cache contents from a backup.
 */
message RestoreRequest {
  // Source backup identifier
  string source = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace to restore
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### revert_migration_request.proto {#revert_migration_request}

**Path**: `gcommon/v1/database/revert_migration_request.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `RevertMigrationRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/revert_migration_request.proto
// version: 1.0.0
// guid: 02d407f4-a362-4009-b8be-dc47f6588d24

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message RevertMigrationRequest {
  // Database name to apply the reversion to
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Target migration version to revert to
  string target_version = 2 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### revert_migration_response.proto {#revert_migration_response}

**Path**: `gcommon/v1/database/revert_migration_response.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `RevertMigrationResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/revert_migration_response.proto
// version: 1.0.0
// guid: 93e7bf68-8691-4063-91b7-247a1dad6e67

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * RevertMigrationResponse indicates the result of a migration reversion.
 */
message RevertMigrationResponse {
  // Whether the migration was reverted successfully
  bool success = 1;

  // Version that the database was reverted to
  string reverted_to = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if the revert failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### rollback_transaction_request.proto {#rollback_transaction_request}

**Path**: `gcommon/v1/database/rollback_transaction_request.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `RollbackTransactionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/rollback_transaction_request.proto
// version: 1.0.0
// guid: 922f9d84-62b4-4428-b44b-443dfd8d3693

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message RollbackTransactionRequest {
  // Transaction ID to rollback
  string transaction_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### run_migration_request.proto {#run_migration_request}

**Path**: `gcommon/v1/database/run_migration_request.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `RunMigrationRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/database/migration_script.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/run_migration_request.proto
// version: 1.0.1
// guid: 666b0a89-7fc5-48ce-ac8a-9a886d9d039a

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/database/migration_script.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message RunMigrationRequest {
  // Database name to run migrations against
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // List of migration scripts to execute
  repeated MigrationScript scripts = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### run_migration_response.proto {#run_migration_response}

**Path**: `gcommon/v1/database/run_migration_response.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `RunMigrationResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/run_migration_response.proto
// version: 1.0.0
// guid: 661b4f25-d546-44b6-b066-0838d3631589
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * RunMigrationResponse contains the result of executing database migrations.
 * Indicates success status and lists applied migration versions.
 */
message RunMigrationResponse {
  // Whether all migrations were applied successfully
  bool success = 1;

  // List of migration versions that were successfully applied
  repeated string applied_versions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error information if any migration failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### scan_request.proto {#scan_request}

**Path**: `gcommon/v1/database/scan_request.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `ScanRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/scan_request.proto
// version: 1.0.0
// guid: a7bf4302-713a-4025-b81f-63984c540e21
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to scan cache keys with a cursor.
 */
message ScanRequest {
  // Scan cursor position
  string cursor = 1 [(buf.validate.field).string.min_len = 1];

  // Match pattern for keys
  string pattern = 2 [(buf.validate.field).string.min_len = 1];

  // Optional namespace
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### set_multiple_request.proto {#set_multiple_request}

**Path**: `gcommon/v1/database/set_multiple_request.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `SetMultipleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/set_multiple_request.proto
// version: 1.0.1
// guid: de4f5678-678a-9b0c-1d2e-3f4a5b6c7d8e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

**Path**: `gcommon/v1/database/set_multiple_response.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `SetMultipleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/set_multiple_response.proto
// version: 1.0.0
// guid: ef5g6789-789a-0b1c-2d3e-4f5a6b7c8d9e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for multiple cache value set operations.
 * Indicates success/failure of batch set operation.
 */
message SetMultipleResponse {
  // Whether all values were successfully set
  bool success = 1;

  // List of keys that failed to be set
  repeated string failed_keys = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error details if operation failed
  gcommon.v1.common.Error error = 3;

  // Number of keys that were successfully set
  int32 set_count = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### set_options.proto {#set_options}

**Path**: `gcommon/v1/database/set_options.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `SetOptions`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/set_options.proto
// version: 1.0.1
// guid: e38b21c6-45d8-4a4b-9f7d-5f6a93484ee9

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

### set_request.proto {#set_request}

**Path**: `gcommon/v1/database/set_request.proto` **Package**: `gcommon.v1.database` **Lines**: 43

**Messages** (1): `SetRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/set_request.proto
// version: 1.0.0
// guid: 47c2c3b4-b463-42e9-a479-8e4ac8debd4c
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to store a value in the cache.
 * Supports flexible expiration policies and namespace isolation.
 */
message SetRequest {
  // Cache key to store
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Value to store (supports any type)
  google.protobuf.Any value = 2 [lazy = true];

  // Optional namespace for cache isolation
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

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

**Path**: `gcommon/v1/database/set_response.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `SetResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/set_response.proto
// version: 1.0.0
// guid: 2c28ae26-1591-4248-baff-82cf800c5349
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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
  int64 size_bytes = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### subscribe_request.proto {#subscribe_request}

**Path**: `gcommon/v1/database/subscribe_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `CacheSubscribeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/subscribe_request.proto
// version: 1.0.0
// guid: 420c972d-4190-4144-b565-04d629a644f0
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to subscribe to cache events.
 */
message CacheSubscribeRequest {
  // Topic or channel name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### touch_expiration_request.proto {#touch_expiration_request}

**Path**: `gcommon/v1/database/touch_expiration_request.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `TouchExpirationRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/touch_expiration_request.proto
// version: 1.0.0
// guid: bb0056c3-6eb4-4476-a508-c6789653b1f5
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to update the TTL of an existing cache key.
 */
message TouchExpirationRequest {
  // Key to update
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // New TTL duration
  google.protobuf.Duration ttl = 2 [lazy = true];

  // Optional namespace
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### touch_expiration_response.proto {#touch_expiration_response}

**Path**: `gcommon/v1/database/touch_expiration_response.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `TouchExpirationResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/touch_expiration_response.proto
// version: 1.0.1
// guid: kl1mnopq-23r4-5s6t-7u8v-9w0x1y2z3a4b

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

**Path**: `gcommon/v1/database/transaction_request.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `TransactionRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/transaction_request.proto
// version: 1.0.1
// guid: 6f47375b-c8cf-45cb-a270-71538e8ae9fd
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

### transaction_status_request.proto {#transaction_status_request}

**Path**: `gcommon/v1/database/transaction_status_request.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `TransactionStatusRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/transaction_status_request.proto
// version: 1.0.0
// guid: 8934c096-ef4b-455b-b318-20395a6b4962

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message TransactionStatusRequest {
  // Identifier of the transaction
  string transaction_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### transaction_status_response.proto {#transaction_status_response}

**Path**: `gcommon/v1/database/transaction_status_response.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `TransactionStatusResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/transaction_status_response.proto
// version: 1.0.0
// guid: 9cba586d-35b2-48c1-a923-dc28fcc06359

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * TransactionStatusResponse returns the current status of a transaction.
 */
message TransactionStatusResponse {
  // Current status of the transaction (e.g., ACTIVE, COMMITTED, ROLLED_BACK)
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Error information if the transaction encountered an issue
  gcommon.v1.common.Error error = 2 [lazy = true];
}
```

---

### unlock_request.proto {#unlock_request}

**Path**: `gcommon/v1/database/unlock_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `UnlockRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/unlock_request.proto
// version: 1.0.0
// guid: b4f680d7-0b7f-41ff-99aa-6333bd7e7709
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to release a previously acquired cache lock.
 */
message UnlockRequest {
  // Lock key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

