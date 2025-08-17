# database Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 23
- **Messages**: 20
- **Services**: 0
- **Enums**: 3

## Files in this Module

- [batch_execute_options.proto](#batch_execute_options)
- [batch_operation.proto](#batch_operation)
- [batch_operation_result.proto](#batch_operation_result)
- [batch_stats.proto](#batch_stats)
- [column_metadata.proto](#column_metadata)
- [connection_pool_info.proto](#connection_pool_info)
- [consistency_level.proto](#consistency_level)
- [database_info.proto](#database_info)
- [database_status.proto](#database_status)
- [database_status_code.proto](#database_status_code)
- [execute_options.proto](#execute_options)
- [execute_stats.proto](#execute_stats)
- [isolation_level.proto](#isolation_level)
- [migration_info.proto](#migration_info)
- [migration_script.proto](#migration_script)
- [mysql_status.proto](#mysql_status)
- [pool_stats.proto](#pool_stats)
- [query_options.proto](#query_options)
- [query_parameter.proto](#query_parameter)
- [query_stats.proto](#query_stats)
- [result_set.proto](#result_set)
- [row.proto](#row)
- [transaction_options.proto](#transaction_options)

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [organization](./organization.md)
- [queue_1](./queue_1.md)

**Modules that depend on this one**:

- [database_api](./database_api.md)
- [metrics_api_1](./metrics_api_1.md)
- [organization](./organization.md)
- [queue_1](./queue_1.md)

---

## Detailed Documentation

### batch_execute_options.proto {#batch_execute_options}

**Path**: `pkg/db/proto/batch_execute_options.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `BatchExecuteOptions`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/batch_execute_options.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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
  int32 max_parallel = 3;
}

```

---

### batch_operation.proto {#batch_operation}

**Path**: `pkg/db/proto/batch_operation.proto` **Package**: `gcommon.v1.database` **Lines**: 23

**Messages** (1): `BatchOperation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/query_parameter.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/batch_operation.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/query_parameter.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * BatchOperation represents a single operation within a batch execution.
 * Contains the SQL statement and its parameters for batch processing.
 */
message BatchOperation {
  // SQL statement or database operation to execute
  string statement = 1;

  // Parameters for the statement
  repeated QueryParameter parameters = 2 [lazy = true];
}

```

---

### batch_operation_result.proto {#batch_operation_result}

**Path**: `pkg/db/proto/batch_operation_result.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `BatchOperationResult`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/db/proto/messages/batch_operation_result.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * BatchOperationResult contains the result of a single operation in a batch.
 * Provides success status, affected rows, and error information.
 */
message BatchOperationResult {
  // Whether the operation completed successfully
  bool success = 1;

  // Number of rows affected by this operation
  int64 affected_rows = 2;

  // Generated keys for INSERT operations
  repeated google.protobuf.Any generated_keys = 3 [lazy = true];

  // Error information if the operation failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}

```

---

### batch_stats.proto {#batch_stats}

**Path**: `pkg/db/proto/batch_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `BatchStats`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/batch_stats.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * BatchStats provides execution statistics for batch database operations.
 * Used for monitoring batch performance and operation success rates.
 */
message BatchStats {
  // Total execution time for the entire batch
  google.protobuf.Duration total_time = 1 [lazy = true];

  // Number of operations that completed successfully
  int32 successful_operations = 2;

  // Number of operations that failed
  int32 failed_operations = 3;

  // Total number of rows affected across all operations
  int64 total_affected_rows = 4;
}

```

---

### column_metadata.proto {#column_metadata}

**Path**: `pkg/db/proto/column_metadata.proto` **Package**: `gcommon.v1.database` **Lines**: 34

**Messages** (1): `ColumnMetadata`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/types/column_metadata.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ColumnMetadata describes the structure and properties of a database column.
 * Used in result sets to provide type information for proper data handling.
 */
message ColumnMetadata {
  // Column name as defined in the database
  string name = 1;

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

**Path**: `pkg/db/proto/connection_pool_info.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `ConnectionPoolInfo`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/db/proto/pool_stats.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/connection_pool_info.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/db/proto/pool_stats.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ConnectionPoolInfo provides information about database connection pool status.
 * Used for monitoring connection health and pool performance.
 */
message ConnectionPoolInfo {
  // Maximum number of connections allowed in the pool
  int32 max_connections = 1;

  // Number of currently active connections
  int32 active_connections = 2;

  // Number of idle connections in the pool
  int32 idle_connections = 3;

  // Average lifetime of connections in the pool
  google.protobuf.Duration avg_lifetime = 4 [lazy = true];

  // Detailed connection pool statistics
  PoolStats stats = 5 [lazy = true];
}

```

---

### consistency_level.proto {#consistency_level}

**Path**: `pkg/db/proto/consistency_level.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Enums** (1): `ConsistencyLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/enums/consistency_level.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ConsistencyLevel defines the data consistency requirements for database operations.
 * Controls the trade-off between consistency, availability, and partition tolerance.
 */
enum ConsistencyLevel {
  // Default unspecified consistency level
  CONSISTENCY_LEVEL_UNSPECIFIED = 0;

  // Eventual consistency - may read stale data but eventually consistent
  CONSISTENCY_LEVEL_EVENTUAL = 1;

  // Strong consistency - always reads most recent committed data
  CONSISTENCY_LEVEL_STRONG = 2;

  // Bounded staleness - reads data within specified time bounds
  CONSISTENCY_LEVEL_BOUNDED_STALENESS = 3;
}

```

---

### database_info.proto {#database_info}

**Path**: `pkg/db/proto/database_info.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Messages** (1): `DatabaseInfo`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/database_info.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * DatabaseInfo provides metadata about a database instance.
 * Used for identifying database capabilities and connection details.
 */
message DatabaseInfo {
  // Database name
  string name = 1;

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

**Path**: `pkg/db/proto/database_status.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `DatabaseStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/database_status_code.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/database_status.proto
// version: 1.0.0
// guid: 67bfa96b-764e-4290-adc8-2387c9b456b4

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/database_status_code.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * DatabaseStatus reports the current connection status for a
 * database driver or service.
 */
message DatabaseStatus {
  // Code indicates the health state of the database
  DatabaseStatusCode code = 1;

  // Human readable status details
  string message = 2;
}

```

---

### database_status_code.proto {#database_status_code}

**Path**: `pkg/db/proto/database_status_code.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Enums** (1): `DatabaseStatusCode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/enums/database_status_code.proto
// version: 1.0.0
// guid: 9849ce1c-df0e-418d-9de6-27b7b1b99d99

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * DatabaseStatusCode represents the health state of a database
 * connection or service.
 */
enum DatabaseStatusCode {
  // Default unspecified status
  DATABASE_STATUS_CODE_UNSPECIFIED = 0;

  // Database is reachable and operational
  DATABASE_STATUS_CODE_OK = 1;

  // Database is unreachable or returned an error
  DATABASE_STATUS_CODE_ERROR = 2;
}

```

---

### execute_options.proto {#execute_options}

**Path**: `pkg/db/proto/execute_options.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `ExecuteOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/db/proto/isolation_level.proto` → [organization](./organization.md#isolation_level)

#### Source Code

```protobuf
// file: pkg/db/proto/messages/execute_options.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/db/proto/isolation_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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
  IsolationLevel isolation = 3;
}

```

---

### execute_stats.proto {#execute_stats}

**Path**: `pkg/db/proto/execute_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `ExecuteStats`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/execute_stats.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ExecuteStats provides execution statistics for database operations.
 * Used for performance monitoring and operation optimization.
 */
message ExecuteStats {
  // Total execution time for the operation
  google.protobuf.Duration execution_time = 1 [lazy = true];

  // Number of rows affected by the operation
  int64 affected_rows = 2;

  // Estimated cost of operation execution
  double cost_estimate = 3;
}

```

---

### isolation_level.proto {#isolation_level}

**Path**: `pkg/db/proto/isolation_level.proto` **Package**: `gcommon.v1.database` **Lines**: 31

**Enums** (1): `IsolationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/enums/isolation_level.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * IsolationLevel defines transaction isolation levels controlling concurrent access.
 * Balances data consistency with concurrency performance.
 */
enum IsolationLevel {
  // Default unspecified isolation level
  ISOLATION_LEVEL_UNSPECIFIED = 0;

  // Read uncommitted - allows dirty reads, lowest isolation
  ISOLATION_LEVEL_READ_UNCOMMITTED = 1;

  // Read committed - prevents dirty reads, allows non-repeatable reads
  ISOLATION_LEVEL_READ_COMMITTED = 2;

  // Repeatable read - prevents dirty and non-repeatable reads
  ISOLATION_LEVEL_REPEATABLE_READ = 3;

  // Serializable - highest isolation, prevents all phenomena
  ISOLATION_LEVEL_SERIALIZABLE = 4;
}

```

---

### migration_info.proto {#migration_info}

**Path**: `pkg/db/proto/migration_info.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `MigrationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/migration_info.proto
// version: 1.0.0
// guid: 4b59457d-20d4-4134-af01-340fe289787e

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * MigrationInfo provides metadata about an applied or pending migration.
 */
message MigrationInfo {
  // Version identifier of the migration
  string version = 1;

  // Descriptive name of the migration
  string description = 2;

  // Timestamp when the migration was applied
  google.protobuf.Timestamp applied_at = 3;
}

```

---

### migration_script.proto {#migration_script}

**Path**: `pkg/db/proto/migration_script.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `MigrationScript`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/types/migration_script.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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
  string description = 3;
}

```

---

### mysql_status.proto {#mysql_status}

**Path**: `pkg/db/proto/mysql_status.proto` **Package**: `gcommon.v1.database` **Lines**: 28

**Messages** (1): `MySQLStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/mysql_status.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * MySQLStatus provides runtime metrics and server version information.
 */
message MySQLStatus {
  // Server version string
  string version = 1;

  // Server start time
  google.protobuf.Timestamp started_at = 2;

  // Number of open connections
  int32 open_connections = 3;

  // Replication role (e.g., master, replica)
  string role = 4;
}

```

---

### pool_stats.proto {#pool_stats}

**Path**: `pkg/db/proto/pool_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 29

**Messages** (1): `PoolStats`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/pool_stats.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * PoolStats provides detailed statistics about connection pool usage.
 * Used for monitoring pool efficiency and connection management.
 */
message PoolStats {
  // Total number of connections created since pool initialization
  int64 total_created = 1;

  // Total number of connections closed since pool initialization
  int64 total_closed = 2;

  // Number of failed attempts to acquire connections
  int64 acquisition_failures = 3;

  // Average time to acquire a connection from the pool
  google.protobuf.Duration avg_acquisition_time = 4 [lazy = true];
}

```

---

### query_options.proto {#query_options}

**Path**: `pkg/db/proto/query_options.proto` **Package**: `gcommon.v1.database` **Lines**: 33

**Messages** (1): `QueryOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/db/proto/consistency_level.proto` → [queue_1](./queue_1.md#consistency_level)

#### Source Code

```protobuf
// file: pkg/db/proto/messages/query_options.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/db/proto/consistency_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * QueryOptions configures behavior for database query operations.
 * Controls result limits, timeouts, and consistency requirements.
 */
message QueryOptions {
  // Maximum number of rows to return
  int32 limit = 1;

  // Number of rows to skip for pagination
  int32 offset = 2;

  // Query execution timeout
  google.protobuf.Duration timeout = 3 [lazy = true];

  // Whether to include column metadata in response
  bool include_metadata = 4;

  // Read consistency level for the query
  ConsistencyLevel consistency = 5;
}

```

---

### query_parameter.proto {#query_parameter}

**Path**: `pkg/db/proto/query_parameter.proto` **Package**: `gcommon.v1.database` **Lines**: 26

**Messages** (1): `QueryParameter`

**Imports** (2):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/types/query_parameter.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * QueryParameter represents a parameter for parameterized queries.
 * Supports typed parameters to prevent SQL injection and improve performance.
 */
message QueryParameter {
  // Parameter name for named parameters
  string name = 1;

  // Parameter value as Any type for flexibility
  google.protobuf.Any value = 2 [lazy = true];

  // Optional type hint for better query optimization
  string type = 3;
}

```

---

### query_stats.proto {#query_stats}

**Path**: `pkg/db/proto/query_stats.proto` **Package**: `gcommon.v1.database` **Lines**: 32

**Messages** (1): `QueryStats`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/query_stats.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * QueryStats provides execution statistics for database queries.
 * Used for performance monitoring and query optimization.
 */
message QueryStats {
  // Total execution time for the query
  google.protobuf.Duration execution_time = 1 [lazy = true];

  // Number of rows returned by the query
  int64 row_count = 2;

  // Number of columns in the result set
  int32 column_count = 3;

  // Query execution plan (if available)
  string query_plan = 4;

  // Estimated cost of query execution
  double cost_estimate = 5;
}

```

---

### result_set.proto {#result_set}

**Path**: `pkg/db/proto/result_set.proto` **Package**: `gcommon.v1.database` **Lines**: 30

**Messages** (1): `ResultSet`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/column_metadata.proto`
- `pkg/db/proto/row.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/messages/result_set.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/column_metadata.proto";
import "pkg/db/proto/row.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * ResultSet contains the results of a database query operation.
 * Includes column metadata, data rows, and pagination information.
 */
message ResultSet {
  // Metadata for each column in the result set
  repeated ColumnMetadata columns = 1 [lazy = true];

  // Data rows matching the query
  repeated Row rows = 2 [lazy = true];

  // Total row count if known (for pagination)
  int64 total_count = 3;

  // Whether more rows are available beyond this result set
  bool has_more = 4;
}

```

---

### row.proto {#row}

**Path**: `pkg/db/proto/row.proto` **Package**: `gcommon.v1.database` **Lines**: 20

**Messages** (1): `Row`

**Imports** (2):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/db/proto/types/row.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * Row represents a single row of data from a database result set.
 * Contains column values in the same order as defined in ColumnMetadata.
 */
message Row {
  // Column values in order matching the column metadata
  repeated google.protobuf.Any values = 1 [lazy = true];
}

```

---

### transaction_options.proto {#transaction_options}

**Path**: `pkg/db/proto/transaction_options.proto` **Package**: `gcommon.v1.database` **Lines**: 27

**Messages** (1): `TransactionOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/db/proto/isolation_level.proto` → [organization](./organization.md#isolation_level)

#### Source Code

```protobuf
// file: pkg/db/proto/messages/transaction_options.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/db/proto/isolation_level.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

/**
 * TransactionOptions configures behavior for database transactions.
 * Controls isolation level, timeout, and read-only mode.
 */
message TransactionOptions {
  // Isolation level for the transaction
  IsolationLevel isolation = 1;

  // Transaction timeout before automatic rollback
  google.protobuf.Duration timeout = 2 [lazy = true];

  // Whether this is a read-only transaction
  bool read_only = 3;
}

```

---
