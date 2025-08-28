# database_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [append_request.proto](#append_request)
- [backup_request.proto](#backup_request)
- [batch_execute_options.proto](#batch_execute_options)
- [batch_operation.proto](#batch_operation)
- [batch_operation_result.proto](#batch_operation_result)
- [batch_stats.proto](#batch_stats)
- [begin_transaction_request.proto](#begin_transaction_request)
- [begin_transaction_response.proto](#begin_transaction_response)
- [clear_request.proto](#clear_request)
- [clear_response.proto](#clear_response)
- [commit_transaction_request.proto](#commit_transaction_request)
- [create_database_request.proto](#create_database_request)
- [create_database_response.proto](#create_database_response)
- [create_namespace_request.proto](#create_namespace_request)
- [create_namespace_response.proto](#create_namespace_response)
- [create_schema_request.proto](#create_schema_request)
- [create_schema_response.proto](#create_schema_response)
- [decrement_request.proto](#decrement_request)
- [decrement_response.proto](#decrement_response)
- [defrag_request.proto](#defrag_request)
- [delete_multiple_request.proto](#delete_multiple_request)
- [delete_multiple_response.proto](#delete_multiple_response)
- [delete_namespace_request.proto](#delete_namespace_request)
- [delete_request.proto](#delete_request)
- [delete_response.proto](#delete_response)
- [drop_database_request.proto](#drop_database_request)
- [drop_schema_request.proto](#drop_schema_request)
- [execute_batch_request.proto](#execute_batch_request)
- [execute_batch_response.proto](#execute_batch_response)
- [execute_request.proto](#execute_request)
- [execute_response.proto](#execute_response)
- [exists_request.proto](#exists_request)
- [exists_response.proto](#exists_response)
- [expire_request.proto](#expire_request)
- [export_request.proto](#export_request)
- [flush_request.proto](#flush_request)
- [flush_response.proto](#flush_response)
- [gc_request.proto](#gc_request)
- [get_connection_info_request.proto](#get_connection_info_request)
- [get_connection_info_response.proto](#get_connection_info_response)
- [get_database_info_request.proto](#get_database_info_request)
- [get_database_info_response.proto](#get_database_info_response)
- [get_memory_usage_request.proto](#get_memory_usage_request)
- [get_memory_usage_response.proto](#get_memory_usage_response)
- [get_migration_status_request.proto](#get_migration_status_request)
- [get_migration_status_response.proto](#get_migration_status_response)
- [get_multiple_request.proto](#get_multiple_request)
- [get_multiple_response.proto](#get_multiple_response)
- [get_namespace_stats_request.proto](#get_namespace_stats_request)
- [get_namespace_stats_response.proto](#get_namespace_stats_response)
---


## Detailed Documentation

### append_request.proto {#append_request}

**Path**: `gcommon/v1/database/append_request.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `AppendRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/append_request.proto
// version: 1.0.0
// guid: 8d45a433-b73c-484a-b3ec-7b28da214561
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to append data to an existing cache entry.
 */
message AppendRequest {
  // Cache key to modify
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Value to append
  google.protobuf.Any value = 2 [lazy = true];

  // Optional namespace for cache isolation
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### backup_request.proto {#backup_request}

**Path**: `gcommon/v1/database/backup_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `BackupRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/backup_request.proto
// version: 1.0.0
// guid: 86d919cd-de08-4ada-813a-e950b0ad8640
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to create a backup of the cache contents.
 */
message BackupRequest {
  // Destination path or identifier for the backup
  string destination = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace to back up
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### batch_execute_options.proto {#batch_execute_options}

**Path**: `gcommon/v1/database/batch_execute_options.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `BatchExecuteOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/batch_execute_options.proto
// version: 1.0.0
// guid: 7d1e1868-699a-432f-ab30-ba90462e683a
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * BatchExecuteOptions configures behavior for batch database operations.
 * Controls error handling, timeouts, and parallelism for batch execution.
 */
message BatchExecuteOptions {
  // Whether to stop execution on the first error
  bool fail_fast = 1;

  // Timeout for the entire batch operation
  google.protobuf.Duration timeout = 2 [lazy = true];

  // Maximum number of operations to execute in parallel
  int32 max_parallel = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### batch_operation.proto {#batch_operation}

**Path**: `gcommon/v1/database/batch_operation.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `DatabaseBatchOperation`

**Imports** (3):

- `gcommon/v1/database/query_parameter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/batch_operation.proto
// version: 1.0.1
// guid: 5d1d11c4-d351-47d7-afeb-48167f63e928
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/query_parameter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * BatchOperation represents a single operation within a batch execution.
 * Contains the SQL statement and its parameters for batch processing.
 */
message DatabaseBatchOperation {
  // SQL statement or database operation to execute
  string statement = 1 [(buf.validate.field).string.min_len = 1];

  // Parameters for the statement
  repeated QueryParameter parameters = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];
}
```

---

### batch_operation_result.proto {#batch_operation_result}

**Path**: `gcommon/v1/database/batch_operation_result.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `BatchOperationResult`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/batch_operation_result.proto
// version: 1.0.1
// guid: ac8d0f0b-4515-44a4-9978-0fba3e8ad463
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * BatchOperationResult contains the result of a single operation in a batch.
 * Provides success status, affected rows, and error information.
 */
message BatchOperationResult {
  // Whether the operation completed successfully
  bool success = 1;

  // Number of rows affected by this operation
  int64 affected_rows = 2 [(buf.validate.field).int64.gte = 0];

  // Generated keys for INSERT operations
  repeated google.protobuf.Any generated_keys = 3 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Error information if the operation failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### batch_stats.proto {#batch_stats}

**Path**: `gcommon/v1/database/batch_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `DatabaseBatchStats`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/batch_stats.proto
// version: 1.0.0
// guid: 0bb234e6-f7a8-4767-ac4a-1c9a0ad6ffa7
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * BatchStats provides execution statistics for batch database operations.
 * Used for monitoring batch performance and operation success rates.
 */
message DatabaseBatchStats {
  // Total execution time for the entire batch
  google.protobuf.Duration total_time = 1 [lazy = true];

  // Number of operations that completed successfully
  int32 successful_operations = 2 [(buf.validate.field).int32.gte = 0];

  // Number of operations that failed
  int32 failed_operations = 3 [(buf.validate.field).int32.gte = 0];

  // Total number of rows affected across all operations
  int64 total_affected_rows = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### begin_transaction_request.proto {#begin_transaction_request}

**Path**: `gcommon/v1/database/begin_transaction_request.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `BeginTransactionRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/database/transaction_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/begin_transaction_request.proto
// version: 1.0.0
// guid: 32a5d984-3a6f-4a66-a8c8-903a3d8c9bb3

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/database/transaction_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message BeginTransactionRequest {
  // Database name (optional, uses default if not specified)
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Transaction configuration options
  TransactionOptions options = 2 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### begin_transaction_response.proto {#begin_transaction_response}

**Path**: `gcommon/v1/database/begin_transaction_response.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `BeginTransactionResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/begin_transaction_response.proto
// version: 1.0.0
// guid: 438f9345-ddb5-4696-9238-03275c33eb39
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * BeginTransactionResponse contains the result of starting a new transaction.
 * Provides the transaction ID and timestamp for tracking.
 */
message BeginTransactionResponse {
  // Unique identifier for the new transaction
  string transaction_id = 1 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the transaction was started
  google.protobuf.Timestamp started_at = 2 [lazy = true];
}
```

---

### clear_request.proto {#clear_request}

**Path**: `gcommon/v1/database/clear_request.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `ClearRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/clear_request.proto
// version: 1.0.0
// guid: de4fghij-56k7-8l9m-0n1o-2p3q4r5s6t7u

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to clear all cache entries.
 * Optionally clear only a specific namespace.
 */
message ClearRequest {
  // Optional namespace to clear (if empty, clears all)
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### clear_response.proto {#clear_response}

**Path**: `gcommon/v1/database/clear_response.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `ClearResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/clear_response.proto
// version: 1.0.0
// guid: ef5ghijk-67l8-9m0n-1o2p-3q4r5s6t7u8v

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache clear operations.
 * Indicates success/failure of clearing cache entries.
 */
message ClearResponse {
  // Number of entries that were cleared
  int64 cleared_count = 1 [(buf.validate.field).int64.gte = 0];

  // Whether the operation was successful
  bool success = 2;

  // Error details if clear failed
  gcommon.v1.common.Error error = 3;
}
```

---

### commit_transaction_request.proto {#commit_transaction_request}

**Path**: `gcommon/v1/database/commit_transaction_request.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `CommitTransactionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/commit_transaction_request.proto
// version: 1.0.0
// guid: 398b751d-7d5a-4624-b844-e7ea289486e6

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message CommitTransactionRequest {
  // Transaction ID to commit
  string transaction_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### create_database_request.proto {#create_database_request}

**Path**: `gcommon/v1/database/create_database_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `CreateDatabaseRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/create_database_request.proto
// version: 1.0.0
// guid: 03802a98-5909-4ba7-9f75-94fc7d2b5071

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message CreateDatabaseRequest {
  // Name of the database to create
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Database creation options and configuration
  map<string, string> options = 2 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### create_database_response.proto {#create_database_response}

**Path**: `gcommon/v1/database/create_database_response.proto` **Package**: `gcommon.v1.database` **Lines**: 24

**Messages** (1): `CreateDatabaseResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/create_database_response.proto
// version: 1.0.1
// guid: 7c2169d7-9306-4a69-8060-e5c5dc1b4dee
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * CreateDatabaseResponse contains the result of a database creation operation.
 * Indicates success status and provides error details if creation failed.
 */
message CreateDatabaseResponse {
  // Whether the database was created successfully
  bool success = 1;

  // Error information if the creation failed
  gcommon.v1.common.Error error = 2 [lazy = true];
}
```

---

### create_namespace_request.proto {#create_namespace_request}

**Path**: `gcommon/v1/database/create_namespace_request.proto` **Package**: `gcommon.v1.database` **Lines**: 39

**Messages** (1): `CreateNamespaceRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/create_namespace_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174012

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to create a new cache namespace.
 */
message CreateNamespaceRequest {
  // Name of the namespace to create
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of the namespace
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

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

**Path**: `gcommon/v1/database/create_namespace_response.proto` **Package**: `gcommon.v1.database` **Lines**: 46

**Messages** (1): `CreateNamespaceResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/create_namespace_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174013

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for creating a cache namespace.
 */
message CreateNamespaceResponse {
  // ID of the created namespace
  string namespace_id = 1;

  // Name of the created namespace
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of the namespace
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // When the namespace was created
  google.protobuf.Timestamp created_at = 4 [ (buf.validate.field).required = true ];

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

### create_schema_request.proto {#create_schema_request}

**Path**: `gcommon/v1/database/create_schema_request.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `CreateSchemaRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/create_schema_request.proto
// version: 1.0.0
// guid: a765b5cd-f14d-4cc1-9aea-8f0c6d372040

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message CreateSchemaRequest {
  // Database name where the schema will be created
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Name of the schema to create
  string schema = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### create_schema_response.proto {#create_schema_response}

**Path**: `gcommon/v1/database/create_schema_response.proto` **Package**: `gcommon.v1.database` **Lines**: 24

**Messages** (1): `CreateSchemaResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/create_schema_response.proto
// version: 1.0.1
// guid: 1c068bcd-cb00-4a27-9dad-0e1a7d938da4
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * CreateSchemaResponse contains the result of a schema creation operation.
 * Indicates success status and provides error details if creation failed.
 */
message CreateSchemaResponse {
  // Whether the schema was created successfully
  bool success = 1;

  // Error information if the creation failed
  gcommon.v1.common.Error error = 2 [lazy = true];
}
```

---

### decrement_request.proto {#decrement_request}

**Path**: `gcommon/v1/database/decrement_request.proto` **Package**: `gcommon.v1.database` **Lines**: 38

**Messages** (1): `DecrementRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/decrement_request.proto
// version: 1.0.0
// guid: 288b113d-b76e-4309-9c5b-207cb4061a73
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to decrement a cached counter atomically.
 */
message DecrementRequest {
  // Counter key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Decrement delta (can be negative)
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

### decrement_response.proto {#decrement_response}

**Path**: `gcommon/v1/database/decrement_response.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `DecrementResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/decrement_response.proto
// version: 1.0.0
// guid: cd3efghi-45j6-7k8l-9m0n-1o2p3q4r5s6t

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache decrement operations.
 * Returns the new value after decrementing.
 */
message DecrementResponse {
  // The new value after decrementing
  int64 new_value = 1 [(buf.validate.field).int64.gte = 0];

  // Whether the operation was successful
  bool success = 2;

  // Error details if decrement failed
  gcommon.v1.common.Error error = 3;
}
```

---

### defrag_request.proto {#defrag_request}

**Path**: `gcommon/v1/database/defrag_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `DefragRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/defrag_request.proto
// version: 1.0.0
// guid: 6a8126b1-18c6-4308-ac2b-07653d79d506
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to defragment the cache storage.
 */
message DefragRequest {
  // Optional namespace to defragment
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### delete_multiple_request.proto {#delete_multiple_request}

**Path**: `gcommon/v1/database/delete_multiple_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `DeleteMultipleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/delete_multiple_request.proto
// version: 1.0.0
// guid: d0edcc55-46c6-4059-927f-4cfabbed653a
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to delete multiple cache keys.
 */
message DeleteMultipleRequest {
  // Keys to delete
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### delete_multiple_response.proto {#delete_multiple_response}

**Path**: `gcommon/v1/database/delete_multiple_response.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `DeleteMultipleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/delete_multiple_response.proto
// version: 1.0.0
// guid: ab1cdefg-23h4-5i6j-7k8l-9m0n1o2p3q4r

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache delete multiple operations.
 * Indicates success/failure of multiple key deletions.
 */
message DeleteMultipleResponse {
  // Number of keys that were successfully deleted
  int32 deleted_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of keys that failed to delete
  int32 failed_count = 2 [(buf.validate.field).int32.gte = 0];

  // List of keys that failed to delete
  repeated string failed_keys = 3 [(buf.validate.field).repeated.min_items = 1];

  // Error details if any deletions failed
  gcommon.v1.common.Error error = 4;
}
```

---

### delete_namespace_request.proto {#delete_namespace_request}

**Path**: `gcommon/v1/database/delete_namespace_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `DeleteNamespaceRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/delete_namespace_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174014

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to delete a cache namespace.
 */
message DeleteNamespaceRequest {
  // ID of the namespace to delete
  string namespace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Force deletion even if namespace contains data
  bool force = 2;

  // Create backup before deletion
  bool backup = 3;
}
```

---

### delete_request.proto {#delete_request}

**Path**: `gcommon/v1/database/delete_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `CacheDeleteRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/delete_request.proto
// version: 1.0.0
// guid: 91c53d9d-7973-470c-b0c7-b04aedadec17
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to delete a cached value by key.
 */
message CacheDeleteRequest {
  // Cache key to delete
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace for cache isolation
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### delete_response.proto {#delete_response}

**Path**: `gcommon/v1/database/delete_response.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `CacheDeleteResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/delete_response.proto
// version: 1.0.0
// guid: 9a0bcdef-12a3-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache delete operations.
 * Indicates success/failure of key deletion.
 */
message CacheDeleteResponse {
  // Whether the key was successfully deleted
  bool success = 1;

  // Error details if deletion failed
  gcommon.v1.common.Error error = 2;

  // Number of keys that were actually deleted
  int32 deleted_count = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### drop_database_request.proto {#drop_database_request}

**Path**: `gcommon/v1/database/drop_database_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `DropDatabaseRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/drop_database_request.proto
// version: 1.0.0
// guid: ed581d88-2b08-4716-9ad4-62e491029bde

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message DropDatabaseRequest {
  // Name of the database to drop
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### drop_schema_request.proto {#drop_schema_request}

**Path**: `gcommon/v1/database/drop_schema_request.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `DropSchemaRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/drop_schema_request.proto
// version: 1.0.0
// guid: f4442e10-50d1-43f9-bc1b-468fb7e6bf3f

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message DropSchemaRequest {
  // Database name containing the schema
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Name of the schema to drop
  string schema = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### execute_batch_request.proto {#execute_batch_request}

**Path**: `gcommon/v1/database/execute_batch_request.proto` **Package**: `gcommon.v1.database` **Lines**: 35

**Messages** (1): `ExecuteBatchRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/database/batch_execute_options.proto`
- `gcommon/v1/database/batch_operation.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/execute_batch_request.proto
// version: 1.0.1
// guid: 2b4354c4-f03a-4317-86b9-57babf767494

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/database/batch_execute_options.proto";
import "gcommon/v1/database/batch_operation.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

// Use DB-specific batch operation definitions

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message ExecuteBatchRequest {
  // List of operations to execute in the batch
  repeated DatabaseBatchOperation operations = 1 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Database name (optional, uses default if not specified)
  string database = 2 [(buf.validate.field).string.min_len = 1];

  // Batch execution options and configuration
  BatchExecuteOptions options = 3 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];

  // Transaction ID if this batch is part of a transaction
  string transaction_id = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### execute_batch_response.proto {#execute_batch_response}

**Path**: `gcommon/v1/database/execute_batch_response.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `ExecuteBatchResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/database/batch_operation_result.proto`
- `gcommon/v1/database/batch_stats.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/execute_batch_response.proto
// version: 1.0.1
// guid: 963b8126-4c56-42c0-a78c-6079e70987ed
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/database/batch_operation_result.proto";
import "gcommon/v1/database/batch_stats.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ExecuteBatchResponse contains the results of a batch database operation.
 * Includes individual operation results and overall batch statistics.
 */
message ExecuteBatchResponse {
  // Results for each operation in the batch
  repeated BatchOperationResult results = 1 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Overall batch execution statistics
  DatabaseBatchStats stats = 2 [lazy = true];

  // Error information if the batch failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### execute_request.proto {#execute_request}

**Path**: `gcommon/v1/database/execute_request.proto` **Package**: `gcommon.v1.database` **Lines**: 37

**Messages** (1): `ExecuteRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/database/execute_options.proto`
- `gcommon/v1/database/query_parameter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/execute_request.proto
// version: 1.0.1
// guid: c2d8bf6f-1805-4fbe-8c00-77c616083610

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/database/execute_options.proto";
import "gcommon/v1/database/query_parameter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message ExecuteRequest {
  // SQL statement or NoSQL operation
  string statement = 1 [(buf.validate.field).string.min_len = 1];

  // Statement parameters for parameterized operations
  repeated QueryParameter parameters = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Database name (optional, uses default if not specified)
  string database = 3 [(buf.validate.field).string.min_len = 1];

  // Execution options and configuration
  ExecuteOptions options = 4 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 5 [lazy = true];

  // Transaction ID if this operation is part of a transaction
  string transaction_id = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### execute_response.proto {#execute_response}

**Path**: `gcommon/v1/database/execute_response.proto` **Package**: `gcommon.v1.database` **Lines**: 34

**Messages** (1): `ExecuteResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/database/execute_stats.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/execute_response.proto
// version: 1.0.1
// guid: d8b5ff82-aa9b-4a8d-a4fb-ef485e3d076d
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/database/execute_stats.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * ExecuteResponse contains the results of a database execute operation.
 * Includes affected row count, generated keys, and execution statistics.
 */
message ExecuteResponse {
  // Number of rows affected by the operation
  int64 affected_rows = 1 [(buf.validate.field).int64.gte = 0];

  // Generated keys from INSERT operations
  repeated google.protobuf.Any generated_keys = 2 [lazy = true, (buf.validate.field).repeated.min_items = 1];

  // Execution statistics and performance metrics
  ExecuteStats stats = 3 [lazy = true];

  // Error information if the operation failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### exists_request.proto {#exists_request}

**Path**: `gcommon/v1/database/exists_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `ExistsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/exists_request.proto
// version: 1.0.0
// guid: 2d1a7b7e-3d9a-44f8-9904-9ed1d77b2ac7
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to check for the existence of a cache key.
 */
message ExistsRequest {
  // Cache key to check
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### exists_response.proto {#exists_response}

**Path**: `gcommon/v1/database/exists_response.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `ExistsResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/exists_response.proto
// version: 1.0.1
// guid: ab1cdef2-23a4-5b6c-7d8e-9f0a1b2c3d4e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

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

**Path**: `gcommon/v1/database/expire_request.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `ExpireRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/expire_request.proto
// version: 1.0.0
// guid: 1ae9e0b1-c430-4d0b-9abd-f6d12cb342bb
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to expire a cache key after a specified duration.
 */
message ExpireRequest {
  // Key to expire
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

### export_request.proto {#export_request}

**Path**: `gcommon/v1/database/export_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `ExportRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/export_request.proto
// version: 1.0.0
// guid: 7c9c11a2-50f9-4b6d-9165-f060cb136a1a
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to export cache contents to an external system.
 */
message ExportRequest {
  // Destination identifier for export
  string destination = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace filter
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### flush_request.proto {#flush_request}

**Path**: `gcommon/v1/database/flush_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `FlushRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/flush_request.proto
// version: 1.0.0
// guid: dcd310f0-3d3c-4b26-a89a-7d46f912f346
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to flush the cache to persistent storage.
 */
message FlushRequest {
  // Optional namespace to flush
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### flush_response.proto {#flush_response}

**Path**: `gcommon/v1/database/flush_response.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `FlushResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/flush_response.proto
// version: 1.0.0
// guid: ij9klmno-01p2-3q4r-5s6t-7u8v9w0x1y2z

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for cache flush operations.
 * Indicates success/failure of cache flushing.
 */
message FlushResponse {
  // Number of items that were flushed
  int64 flushed_count = 1 [(buf.validate.field).int64.gte = 0];

  // Whether the operation was successful
  bool success = 2;

  // Error details if flush failed
  gcommon.v1.common.Error error = 3;
}
```

---

### gc_request.proto {#gc_request}

**Path**: `gcommon/v1/database/gc_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `GcRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/gc_request.proto
// version: 1.0.0
// guid: cf3c56d0-e033-482e-9c7e-2c72782267b7
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to trigger cache garbage collection.
 */
message GcRequest {
  // Optional namespace to clean
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_connection_info_request.proto {#get_connection_info_request}

**Path**: `gcommon/v1/database/get_connection_info_request.proto` **Package**: `gcommon.v1.database` **Lines**: 18

**Messages** (1): `GetConnectionInfoRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_connection_info_request.proto
// version: 1.0.1
// guid: 32ff391a-940f-4051-84f4-22936a48e124

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message GetConnectionInfoRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### get_connection_info_response.proto {#get_connection_info_response}

**Path**: `gcommon/v1/database/get_connection_info_response.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `GetConnectionInfoResponse`

**Imports** (3):

- `gcommon/v1/database/connection_pool_info.proto`
- `gcommon/v1/database/database_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_connection_info_response.proto
// version: 1.0.1
// guid: aeb84786-b800-4de9-bf70-e9e9eda20820
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/connection_pool_info.proto";
import "gcommon/v1/database/database_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * GetConnectionInfoResponse contains database connection and pool information.
 * Provides details about connection health and database capabilities.
 */
message GetConnectionInfoResponse {
  // Database connection pool information and statistics
  ConnectionPoolInfo pool_info = 1 [lazy = true];

  // Database instance information and metadata
  DatabaseInfo database_info = 2 [lazy = true];
}
```

---

### get_database_info_request.proto {#get_database_info_request}

**Path**: `gcommon/v1/database/get_database_info_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `GetDatabaseInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_database_info_request.proto
// version: 1.0.0
// guid: 5ccf29d5-d416-4ca3-881f-f28b652a626c

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message GetDatabaseInfoRequest {
  // Name of the database to get information about
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_database_info_response.proto {#get_database_info_response}

**Path**: `gcommon/v1/database/get_database_info_response.proto` **Package**: `gcommon.v1.database` **Lines**: 21

**Messages** (1): `GetDatabaseInfoResponse`

**Imports** (2):

- `gcommon/v1/database/database_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_database_info_response.proto
// version: 1.0.1
// guid: 82b01a11-1af8-4919-9361-f49aa8b3f822
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/database_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * GetDatabaseInfoResponse contains detailed metadata about a database.
 * Includes version, type, capabilities, and connection information.
 */
message GetDatabaseInfoResponse {
  // Detailed database information and metadata
  DatabaseInfo info = 1 [lazy = true];
}
```

---

### get_memory_usage_request.proto {#get_memory_usage_request}

**Path**: `gcommon/v1/database/get_memory_usage_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `GetMemoryUsageRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_memory_usage_request.proto
// version: 1.0.0
// guid: 97d985af-123a-4048-ae7e-bb36a97c9069
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to retrieve cache memory usage statistics.
 */
message GetMemoryUsageRequest {
  // Optional namespace filter
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_memory_usage_response.proto {#get_memory_usage_response}

**Path**: `gcommon/v1/database/get_memory_usage_response.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `GetMemoryUsageResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_memory_usage_response.proto
// version: 1.0.0
// guid: 4bd2a1f2-5469-4fc5-9bdb-e0691a1bbaa9
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for GetMemoryUsage operations.
 */
message GetMemoryUsageResponse {
  // Memory usage in bytes
  int64 memory_usage_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Memory usage as a percentage of total capacity
  double memory_usage_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}
```

---

### get_migration_status_request.proto {#get_migration_status_request}

**Path**: `gcommon/v1/database/get_migration_status_request.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `GetMigrationStatusRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/get_migration_status_request.proto
// version: 1.0.0
// guid: 3fca70ce-04de-482f-979e-f1a51d118b0e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message GetMigrationStatusRequest {
  // Database name to check migration status for
  string database = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_migration_status_response.proto {#get_migration_status_response}

**Path**: `gcommon/v1/database/get_migration_status_response.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `GetMigrationStatusResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/schema/get_migration_status_response.proto
// version: 1.0.0
// guid: 1659e56b-2105-471e-8b9a-270425e3ac31
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * GetMigrationStatusResponse contains the current migration status for a database.
 * Shows current version, applied migrations, and pending migrations.
 */
message GetMigrationStatusResponse {
  // Current migration version of the database
  string current_version = 1 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // List of migration versions that have been applied
  repeated string applied_versions = 2 [(buf.validate.field).repeated.min_items = 1];

  // List of migration versions that are pending application
  repeated string pending_versions = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### get_multiple_request.proto {#get_multiple_request}

**Path**: `gcommon/v1/database/get_multiple_request.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `GetMultipleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_multiple_request.proto
// version: 1.0.0
// guid: bc2def34-45a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to get multiple cache values by keys.
 * Supports batch retrieval for performance optimization.
 */
message GetMultipleRequest {
  // List of keys to retrieve
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_multiple_response.proto {#get_multiple_response}

**Path**: `gcommon/v1/database/get_multiple_response.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `GetMultipleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_multiple_response.proto
// version: 1.0.0
// guid: cd3ef456-567a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Response for multiple cache value retrieval.
 * Contains a map of keys to their values or error information.
 */
message GetMultipleResponse {
  // Map of key to value for successful retrievals
  map<string, bytes> values = 1;

  // List of keys that were not found
  repeated string missing_keys = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error details if operation failed
  gcommon.v1.common.Error error = 3;
}
```

---

### get_namespace_stats_request.proto {#get_namespace_stats_request}

**Path**: `gcommon/v1/database/get_namespace_stats_request.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `GetNamespaceStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_namespace_stats_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174017

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to get namespace statistics.
 */
message GetNamespaceStatsRequest {
  // ID of the namespace
  string namespace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include detailed metrics
  bool include_detailed_metrics = 2;

  // Include key distribution stats
  bool include_key_distribution = 3;
}
```

---

### get_namespace_stats_response.proto {#get_namespace_stats_response}

**Path**: `gcommon/v1/database/get_namespace_stats_response.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `GetNamespaceStatsResponse`

**Imports** (4):

- `gcommon/v1/database/namespace_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/get_namespace_stats_response.proto
// version: 1.0.0
// guid: c59d03a0-bea0-440a-a4d1-6008ef5a0958

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/namespace_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

message GetNamespaceStatsResponse {
  // Namespace ID
  string namespace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Statistics
  // Statistics for the requested namespace
  NamespaceStats stats = 2;

  // When stats were collected
  google.protobuf.Timestamp collected_at = 3;
}
```

---

