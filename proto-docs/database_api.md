# database_api Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 38
- **Messages**: 38
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [begin_transaction_request.proto](#begin_transaction_request)
- [begin_transaction_response.proto](#begin_transaction_response)
- [commit_transaction_request.proto](#commit_transaction_request)
- [create_database_request.proto](#create_database_request)
- [create_database_response.proto](#create_database_response)
- [create_schema_request.proto](#create_schema_request)
- [create_schema_response.proto](#create_schema_response)
- [drop_database_request.proto](#drop_database_request)
- [drop_schema_request.proto](#drop_schema_request)
- [execute_batch_request.proto](#execute_batch_request)
- [execute_batch_response.proto](#execute_batch_response)
- [execute_request.proto](#execute_request)
- [execute_response.proto](#execute_response)
- [get_connection_info_request.proto](#get_connection_info_request)
- [get_connection_info_response.proto](#get_connection_info_response)
- [get_database_info_request.proto](#get_database_info_request)
- [get_database_info_response.proto](#get_database_info_response)
- [get_migration_status_request.proto](#get_migration_status_request)
- [get_migration_status_response.proto](#get_migration_status_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [list_databases_request.proto](#list_databases_request)
- [list_databases_response.proto](#list_databases_response)
- [list_migrations_request.proto](#list_migrations_request)
- [list_migrations_response.proto](#list_migrations_response)
- [list_schemas_request.proto](#list_schemas_request)
- [list_schemas_response.proto](#list_schemas_response)
- [query_request.proto](#query_request)
- [query_response.proto](#query_response)
- [query_row_request.proto](#query_row_request)
- [query_row_response.proto](#query_row_response)
- [revert_migration_request.proto](#revert_migration_request)
- [revert_migration_response.proto](#revert_migration_response)
- [rollback_transaction_request.proto](#rollback_transaction_request)
- [run_migration_request.proto](#run_migration_request)
- [run_migration_response.proto](#run_migration_response)
- [transaction_status_request.proto](#transaction_status_request)
- [transaction_status_response.proto](#transaction_status_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [database](./database.md)
- [metrics_1](./metrics_1.md)
- [metrics_2](./metrics_2.md)
- [queue_1](./queue_1.md)
- [web](./web.md)

**Modules that depend on this one**:

- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)

---

## Detailed Documentation

### begin_transaction_request.proto {#begin_transaction_request}

**Path**: `pkg/db/proto/begin_transaction_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 24

**Messages** (1): `BeginTransactionRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/db/proto/transaction_options.proto` →
  [database](./database.md#transaction_options)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/begin_transaction_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/db/proto/transaction_options.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message BeginTransactionRequest {
  // Database name (optional, uses default if not specified)
  string database = 1;

  // Transaction configuration options
  TransactionOptions options = 2 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### begin_transaction_response.proto {#begin_transaction_response}

**Path**: `pkg/db/proto/begin_transaction_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 23

**Messages** (1): `BeginTransactionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/responses/begin_transaction_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * BeginTransactionResponse contains the result of starting a new transaction.
 * Provides the transaction ID and timestamp for tracking.
 */
message BeginTransactionResponse {
  // Unique identifier for the new transaction
  string transaction_id = 1;

  // Timestamp when the transaction was started
  google.protobuf.Timestamp started_at = 2 [lazy = true];
}

```

---

### commit_transaction_request.proto {#commit_transaction_request}

**Path**: `pkg/db/proto/commit_transaction_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `CommitTransactionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/commit_transaction_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message CommitTransactionRequest {
  // Transaction ID to commit
  string transaction_id = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### create_database_request.proto {#create_database_request}

**Path**: `pkg/db/proto/create_database_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 23

**Messages** (1): `CreateDatabaseRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/create_database_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message CreateDatabaseRequest {
  // Name of the database to create
  string name = 1;

  // Database creation options and configuration
  map<string, string> options = 2 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### create_database_response.proto {#create_database_response}

**Path**: `pkg/db/proto/create_database_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 23

**Messages** (1): `CreateDatabaseResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/create_database_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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

### create_schema_request.proto {#create_schema_request}

**Path**: `pkg/db/proto/create_schema_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 23

**Messages** (1): `CreateSchemaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/create_schema_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message CreateSchemaRequest {
  // Database name where the schema will be created
  string database = 1;

  // Name of the schema to create
  string schema = 2;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### create_schema_response.proto {#create_schema_response}

**Path**: `pkg/db/proto/create_schema_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 23

**Messages** (1): `CreateSchemaResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/create_schema_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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

### drop_database_request.proto {#drop_database_request}

**Path**: `pkg/db/proto/drop_database_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `DropDatabaseRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/drop_database_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message DropDatabaseRequest {
  // Name of the database to drop
  string name = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### drop_schema_request.proto {#drop_schema_request}

**Path**: `pkg/db/proto/drop_schema_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 23

**Messages** (1): `DropSchemaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/drop_schema_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message DropSchemaRequest {
  // Database name containing the schema
  string database = 1;

  // Name of the schema to drop
  string schema = 2;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### execute_batch_request.proto {#execute_batch_request}

**Path**: `pkg/db/proto/execute_batch_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 31

**Messages** (1): `ExecuteBatchRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/db/proto/batch_execute_options.proto` →
  [database](./database.md#batch_execute_options)
- `pkg/db/proto/batch_operation.proto` → [common](./common.md#batch_operation) →
  [database](./database.md#batch_operation)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/execute_batch_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/db/proto/batch_execute_options.proto";
import "pkg/db/proto/batch_operation.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message ExecuteBatchRequest {
  // List of operations to execute in the batch
  repeated BatchOperation operations = 1 [lazy = true];

  // Database name (optional, uses default if not specified)
  string database = 2;

  // Batch execution options and configuration
  BatchExecuteOptions options = 3 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];

  // Transaction ID if this batch is part of a transaction
  string transaction_id = 5;
}

```

---

### execute_batch_response.proto {#execute_batch_response}

**Path**: `pkg/db/proto/execute_batch_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 28

**Messages** (1): `ExecuteBatchResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/db/proto/batch_operation_result.proto` →
  [database](./database.md#batch_operation_result)
- `pkg/db/proto/batch_stats.proto` → [database](./database.md#batch_stats)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/execute_batch_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/db/proto/batch_operation_result.proto";
import "pkg/db/proto/batch_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ExecuteBatchResponse contains the results of a batch database operation.
 * Includes individual operation results and overall batch statistics.
 */
message ExecuteBatchResponse {
  // Results for each operation in the batch
  repeated BatchOperationResult results = 1 [lazy = true];

  // Overall batch execution statistics
  BatchStats stats = 2 [lazy = true];

  // Error information if the batch failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}

```

---

### execute_request.proto {#execute_request}

**Path**: `pkg/db/proto/execute_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 34

**Messages** (1): `ExecuteRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/db/proto/execute_options.proto` →
  [database](./database.md#execute_options)
- `pkg/db/proto/query_parameter.proto` →
  [database](./database.md#query_parameter)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/execute_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/db/proto/execute_options.proto";
import "pkg/db/proto/query_parameter.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message ExecuteRequest {
  // SQL statement or NoSQL operation
  string statement = 1;

  // Statement parameters for parameterized operations
  repeated QueryParameter parameters = 2 [lazy = true];

  // Database name (optional, uses default if not specified)
  string database = 3;

  // Execution options and configuration
  ExecuteOptions options = 4 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 5 [lazy = true];

  // Transaction ID if this operation is part of a transaction
  string transaction_id = 6;
}

```

---

### execute_response.proto {#execute_response}

**Path**: `pkg/db/proto/execute_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 31

**Messages** (1): `ExecuteResponse`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/db/proto/execute_stats.proto` → [database](./database.md#execute_stats)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/execute_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/db/proto/execute_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ExecuteResponse contains the results of a database execute operation.
 * Includes affected row count, generated keys, and execution statistics.
 */
message ExecuteResponse {
  // Number of rows affected by the operation
  int64 affected_rows = 1;

  // Generated keys from INSERT operations
  repeated google.protobuf.Any generated_keys = 2 [lazy = true];

  // Execution statistics and performance metrics
  ExecuteStats stats = 3 [lazy = true];

  // Error information if the operation failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}

```

---

### get_connection_info_request.proto {#get_connection_info_request}

**Path**: `pkg/db/proto/get_connection_info_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 17

**Messages** (1): `GetConnectionInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/get_connection_info_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message GetConnectionInfoRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### get_connection_info_response.proto {#get_connection_info_response}

**Path**: `pkg/db/proto/get_connection_info_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 24

**Messages** (1): `GetConnectionInfoResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/connection_pool_info.proto` →
  [database](./database.md#connection_pool_info)
- `pkg/db/proto/database_info.proto` → [database](./database.md#database_info)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/get_connection_info_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/connection_pool_info.proto";
import "pkg/db/proto/database_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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

**Path**: `pkg/db/proto/get_database_info_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `GetDatabaseInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/get_database_info_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message GetDatabaseInfoRequest {
  // Name of the database to get information about
  string name = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_database_info_response.proto {#get_database_info_response}

**Path**: `pkg/db/proto/get_database_info_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `GetDatabaseInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/database_info.proto` → [database](./database.md#database_info)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/get_database_info_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/database_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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

### get_migration_status_request.proto {#get_migration_status_request}

**Path**: `pkg/db/proto/get_migration_status_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `GetMigrationStatusRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/get_migration_status_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message GetMigrationStatusRequest {
  // Database name to check migration status for
  string database = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_migration_status_response.proto {#get_migration_status_response}

**Path**: `pkg/db/proto/get_migration_status_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 25

**Messages** (1): `GetMigrationStatusResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/responses/get_migration_status_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * GetMigrationStatusResponse contains the current migration status for a database.
 * Shows current version, applied migrations, and pending migrations.
 */
message GetMigrationStatusResponse {
  // Current migration version of the database
  string current_version = 1;

  // List of migration versions that have been applied
  repeated string applied_versions = 2;

  // List of migration versions that are pending application
  repeated string pending_versions = 3;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/db/proto/health_check_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 17

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/health_check_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message HealthCheckRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### health_check_response.proto {#health_check_response}

**Path**: `pkg/db/proto/health_check_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 31

**Messages** (1): `HealthCheckResponse`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/health_check_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * HealthCheckResponse contains the result of a database health check.
 * Provides connection status, response time, and error details.
 */
message HealthCheckResponse {
  // Overall health status of the database
  gcommon.v1.common.HealthStatus status = 1;

  // Whether the database connection is operational
  bool connection_ok = 2;

  // Time taken to perform the health check
  google.protobuf.Duration response_time = 3 [lazy = true];

  // Error information if the health check failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}

```

---

### list_databases_request.proto {#list_databases_request}

**Path**: `pkg/db/proto/list_databases_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 17

**Messages** (1): `ListDatabasesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/list_databases_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message ListDatabasesRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### list_databases_response.proto {#list_databases_response}

**Path**: `pkg/db/proto/list_databases_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 19

**Messages** (1): `ListDatabasesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/responses/list_databases_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ListDatabasesResponse contains the list of available databases.
 * Provides database names accessible to the authenticated user.
 */
message ListDatabasesResponse {
  // List of database names
  repeated string databases = 1;
}

```

---

### list_migrations_request.proto {#list_migrations_request}

**Path**: `pkg/db/proto/list_migrations_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 25

**Messages** (1): `ListMigrationsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/list_migrations_request.proto
// version: 1.0.0
// guid: e09ee131-1388-41e5-973c-3c7eb4308349

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message ListMigrationsRequest {
  // Database name to list migrations for
  string database = 1;

  // Return only applied or pending migrations (optional)
  string status_filter = 2;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### list_migrations_response.proto {#list_migrations_response}

**Path**: `pkg/db/proto/list_migrations_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 22

**Messages** (1): `ListMigrationsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/migration_info.proto` → [database](./database.md#migration_info)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/list_migrations_response.proto
// version: 1.0.0
// guid: 2d1040e2-056b-4264-8f84-d731b345d924

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/migration_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ListMigrationsResponse returns a list of migrations for a database.
 */
message ListMigrationsResponse {
  // List of migration metadata entries
  repeated MigrationInfo migrations = 1 [lazy = true];
}

```

---

### list_schemas_request.proto {#list_schemas_request}

**Path**: `pkg/db/proto/list_schemas_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `ListSchemasRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/list_schemas_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message ListSchemasRequest {
  // Database name to list schemas from
  string database = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### list_schemas_response.proto {#list_schemas_response}

**Path**: `pkg/db/proto/list_schemas_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 19

**Messages** (1): `ListSchemasResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/responses/list_schemas_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ListSchemasResponse contains the list of schemas within a database.
 * Provides schema names available in the specified database.
 */
message ListSchemasResponse {
  // List of schema names in the database
  repeated string schemas = 1;
}

```

---

### query_request.proto {#query_request}

**Path**: `pkg/db/proto/query_request.proto` **Package**: `gcommon.v1.database`
**Lines**: 34

**Messages** (1): `QueryRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/db/proto/query_options.proto` → [database](./database.md#query_options)
- `pkg/db/proto/query_parameter.proto` →
  [database](./database.md#query_parameter)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/query_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/db/proto/query_options.proto";
import "pkg/db/proto/query_parameter.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message QueryRequest {
  // SQL query or NoSQL query string
  string query = 1;

  // Query parameters for parameterized queries
  repeated QueryParameter parameters = 2 [lazy = true];

  // Database name (optional, uses default if not specified)
  string database = 3;

  // Query execution options
  QueryOptions options = 4 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 5 [lazy = true];

  // Transaction ID if this query is part of a transaction
  string transaction_id = 6;
}

```

---

### query_response.proto {#query_response}

**Path**: `pkg/db/proto/query_response.proto` **Package**: `gcommon.v1.database`
**Lines**: 28

**Messages** (1): `QueryResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/db/proto/query_stats.proto` → [database](./database.md#query_stats) →
  [metrics_2](./metrics_2.md#query_stats)
- `pkg/db/proto/result_set.proto` → [database](./database.md#result_set)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/query_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/db/proto/query_stats.proto";
import "pkg/db/proto/result_set.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * QueryResponse contains the results of a database query operation.
 * Includes result data, execution statistics, and error information.
 */
message QueryResponse {
  // Query result set with data and metadata
  ResultSet result_set = 1 [lazy = true];

  // Query execution statistics and performance metrics
  QueryStats stats = 2 [lazy = true];

  // Error information if the query failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}

```

---

### query_row_request.proto {#query_row_request}

**Path**: `pkg/db/proto/query_row_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 36

**Messages** (1): `QueryRowRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/db/proto/query_options.proto` → [database](./database.md#query_options)
- `pkg/db/proto/query_parameter.proto` →
  [database](./database.md#query_parameter)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/query_row_request.proto
// version: 1.0.0
// guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/db/proto/query_options.proto";
import "pkg/db/proto/query_parameter.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message QueryRowRequest {
  // SQL query or NoSQL query string (should return at most one row)
  string query = 1;

  // Query parameters for parameterized queries
  repeated QueryParameter parameters = 2 [lazy = true];

  // Database name (optional, uses default if not specified)
  string database = 3;

  // Query execution options
  QueryOptions options = 4 [lazy = true];

  // Transaction ID if this query should be executed within a transaction
  string transaction_id = 5;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}

```

---

### query_row_response.proto {#query_row_response}

**Path**: `pkg/db/proto/query_row_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 37

**Messages** (1): `QueryRowResponse`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/db/proto/query_stats.proto` → [database](./database.md#query_stats) →
  [metrics_2](./metrics_2.md#query_stats)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/query_row_response.proto
// version: 1.0.0
// guid: dff9c212-0d7d-4f0a-bcca-8a0a641a29f9

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/db/proto/query_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * QueryRowResponse contains the result of a single-row query.
 * If no row was found, `found` will be false and `values` will be empty.
 */
message QueryRowResponse {
  // Indicates whether a row was found
  bool found = 1;

  // Column names matching the returned values
  repeated string columns = 2;

  // Row values encoded as generic Any values
  repeated google.protobuf.Any values = 3 [lazy = true];

  // Query execution statistics
  QueryStats stats = 4 [lazy = true];

  // Error information if the query failed
  gcommon.v1.common.Error error = 5 [lazy = true];
}

```

---

### revert_migration_request.proto {#revert_migration_request}

**Path**: `pkg/db/proto/revert_migration_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 25

**Messages** (1): `RevertMigrationRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/revert_migration_request.proto
// version: 1.0.0
// guid: 02d407f4-a362-4009-b8be-dc47f6588d24

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message RevertMigrationRequest {
  // Database name to apply the reversion to
  string database = 1;

  // Target migration version to revert to
  string target_version = 2;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### revert_migration_response.proto {#revert_migration_response}

**Path**: `pkg/db/proto/revert_migration_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 28

**Messages** (1): `RevertMigrationResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/revert_migration_response.proto
// version: 1.0.0
// guid: 93e7bf68-8691-4063-91b7-247a1dad6e67

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * RevertMigrationResponse indicates the result of a migration reversion.
 */
message RevertMigrationResponse {
  // Whether the migration was reverted successfully
  bool success = 1;

  // Version that the database was reverted to
  string reverted_to = 2;

  // Error information if the revert failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}

```

---

### rollback_transaction_request.proto {#rollback_transaction_request}

**Path**: `pkg/db/proto/rollback_transaction_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 20

**Messages** (1): `RollbackTransactionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/rollback_transaction_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message RollbackTransactionRequest {
  // Transaction ID to rollback
  string transaction_id = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### run_migration_request.proto {#run_migration_request}

**Path**: `pkg/db/proto/run_migration_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 24

**Messages** (1): `RunMigrationRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/db/proto/migration_script.proto` →
  [database](./database.md#migration_script)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/run_migration_request.proto

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/db/proto/migration_script.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message RunMigrationRequest {
  // Database name to run migrations against
  string database = 1;

  // List of migration scripts to execute
  repeated MigrationScript scripts = 2 [lazy = true];

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}

```

---

### run_migration_response.proto {#run_migration_response}

**Path**: `pkg/db/proto/run_migration_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 26

**Messages** (1): `RunMigrationResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/run_migration_response.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * RunMigrationResponse contains the result of executing database migrations.
 * Indicates success status and lists applied migration versions.
 */
message RunMigrationResponse {
  // Whether all migrations were applied successfully
  bool success = 1;

  // List of migration versions that were successfully applied
  repeated string applied_versions = 2;

  // Error information if any migration failed
  gcommon.v1.common.Error error = 3 [lazy = true];
}

```

---

### transaction_status_request.proto {#transaction_status_request}

**Path**: `pkg/db/proto/transaction_status_request.proto` **Package**:
`gcommon.v1.database` **Lines**: 22

**Messages** (1): `TransactionStatusRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/db/proto/requests/transaction_status_request.proto
// version: 1.0.0
// guid: 8934c096-ef4b-455b-b318-20395a6b4962

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

message TransactionStatusRequest {
  // Identifier of the transaction
  string transaction_id = 1;

  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### transaction_status_response.proto {#transaction_status_response}

**Path**: `pkg/db/proto/transaction_status_response.proto` **Package**:
`gcommon.v1.database` **Lines**: 25

**Messages** (1): `TransactionStatusResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/db/proto/responses/transaction_status_response.proto
// version: 1.0.0
// guid: 9cba586d-35b2-48c1-a923-dc28fcc06359

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * TransactionStatusResponse returns the current status of a transaction.
 */
message TransactionStatusResponse {
  // Current status of the transaction (e.g., ACTIVE, COMMITTED, ROLLED_BACK)
  string status = 1;

  // Error information if the transaction encountered an issue
  gcommon.v1.common.Error error = 2 [lazy = true];
}

```

---
