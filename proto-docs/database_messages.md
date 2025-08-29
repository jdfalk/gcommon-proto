# Database Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 133
- **Messages**: 133

## Table of Contents

### Messages

- [`AppendRequest`](#append_request) - from append_request.proto
- [`BackupRequest`](#backup_request) - from backup_request.proto
- [`BatchExecuteOptions`](#batch_execute_options) - from batch_execute_options.proto
- [`BatchOperationResult`](#batch_operation_result) - from batch_operation_result.proto
- [`BeginTransactionRequest`](#begin_transaction_request) - from begin_transaction_request.proto
- [`BeginTransactionResponse`](#begin_transaction_response) - from begin_transaction_response.proto
- [`CacheCacheConfig`](#cache_config) - from cache_config.proto
- [`CacheDeleteRequest`](#delete_request) - from delete_request.proto
- [`CacheDeleteResponse`](#delete_response) - from delete_response.proto
- [`CacheEntry`](#cache_entry) - from cache_entry.proto
- [`CacheGetStatsRequest`](#get_stats_request) - from get_stats_request.proto
- [`CacheGetStatsResponse`](#get_stats_response) - from get_stats_response.proto
- [`CacheInfo`](#cache_info) - from cache_info.proto
- [`CacheListSubscriptionsRequest`](#list_subscriptions_request) - from list_subscriptions_request.proto
- [`CacheMetrics`](#cache_metrics) - from cache_metrics.proto
- [`CacheOperationResult`](#cache_operation_result) - from cache_operation_result.proto
- [`CachePublishRequest`](#publish_request) - from publish_request.proto
- [`CacheStats`](#cache_stats) - from cache_stats.proto
- [`CacheSubscribeRequest`](#subscribe_request) - from subscribe_request.proto
- [`CacheUnsubscribeRequest`](#unsubscribe_request) - from unsubscribe_request.proto
- [`CacheWatchRequest`](#watch_request) - from watch_request.proto
- [`ClearRequest`](#clear_request) - from clear_request.proto
- [`ClearResponse`](#clear_response) - from clear_response.proto
- [`CockroachConfig`](#cockroach_config) - from cockroach_config.proto
- [`ColumnMetadata`](#column_metadata) - from column_metadata.proto
- [`CommitTransactionRequest`](#commit_transaction_request) - from commit_transaction_request.proto
- [`ConfigurePolicyRequest`](#configure_policy_request) - from configure_policy_request.proto
- [`ConfigurePolicyResponse`](#configure_policy_response) - from configure_policy_response.proto
- [`ConnectionPoolInfo`](#connection_pool_info) - from connection_pool_info.proto
- [`CreateDatabaseRequest`](#create_database_request) - from create_database_request.proto
- [`CreateDatabaseResponse`](#create_database_response) - from create_database_response.proto
- [`CreateNamespaceRequest`](#create_namespace_request) - from create_namespace_request.proto
- [`CreateNamespaceResponse`](#create_namespace_response) - from create_namespace_response.proto
- [`CreateSchemaRequest`](#create_schema_request) - from create_schema_request.proto
- [`CreateSchemaResponse`](#create_schema_response) - from create_schema_response.proto
- [`DatabaseBatchOperation`](#batch_operation) - from batch_operation.proto
- [`DatabaseBatchStats`](#batch_stats) - from batch_stats.proto
- [`DatabaseHealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`DatabaseHealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`DatabaseInfo`](#database_info) - from database_info.proto
- [`DatabaseQueryStats`](#query_stats) - from query_stats.proto
- [`DatabaseStatus`](#database_status) - from database_status.proto
- [`DecrementRequest`](#decrement_request) - from decrement_request.proto
- [`DecrementResponse`](#decrement_response) - from decrement_response.proto
- [`DefragRequest`](#defrag_request) - from defrag_request.proto
- [`DeleteMultipleRequest`](#delete_multiple_request) - from delete_multiple_request.proto
- [`DeleteMultipleResponse`](#delete_multiple_response) - from delete_multiple_response.proto
- [`DeleteNamespaceRequest`](#delete_namespace_request) - from delete_namespace_request.proto
- [`DropDatabaseRequest`](#drop_database_request) - from drop_database_request.proto
- [`DropSchemaRequest`](#drop_schema_request) - from drop_schema_request.proto
- [`EvictionResult`](#eviction_result) - from eviction_result.proto
- [`ExecuteBatchRequest`](#execute_batch_request) - from execute_batch_request.proto
- [`ExecuteBatchResponse`](#execute_batch_response) - from execute_batch_response.proto
- [`ExecuteOptions`](#execute_options) - from execute_options.proto
- [`ExecuteRequest`](#execute_request) - from execute_request.proto
- [`ExecuteResponse`](#execute_response) - from execute_response.proto
- [`ExecuteStats`](#execute_stats) - from execute_stats.proto
- [`ExistsRequest`](#exists_request) - from exists_request.proto
- [`ExistsResponse`](#exists_response) - from exists_response.proto
- [`ExpireRequest`](#expire_request) - from expire_request.proto
- [`ExportRequest`](#export_request) - from export_request.proto
- [`FlushRequest`](#flush_request) - from flush_request.proto
- [`FlushResponse`](#flush_response) - from flush_response.proto
- [`GcRequest`](#gc_request) - from gc_request.proto
- [`GetConnectionInfoRequest`](#get_connection_info_request) - from get_connection_info_request.proto
- [`GetConnectionInfoResponse`](#get_connection_info_response) - from get_connection_info_response.proto
- [`GetDatabaseInfoRequest`](#get_database_info_request) - from get_database_info_request.proto
- [`GetDatabaseInfoResponse`](#get_database_info_response) - from get_database_info_response.proto
- [`GetMemoryUsageRequest`](#get_memory_usage_request) - from get_memory_usage_request.proto
- [`GetMemoryUsageResponse`](#get_memory_usage_response) - from get_memory_usage_response.proto
- [`GetMigrationStatusRequest`](#get_migration_status_request) - from get_migration_status_request.proto
- [`GetMigrationStatusResponse`](#get_migration_status_response) - from get_migration_status_response.proto
- [`GetMultipleRequest`](#get_multiple_request) - from get_multiple_request.proto
- [`GetMultipleResponse`](#get_multiple_response) - from get_multiple_response.proto
- [`GetNamespaceStatsRequest`](#get_namespace_stats_request) - from get_namespace_stats_request.proto
- [`GetNamespaceStatsResponse`](#get_namespace_stats_response) - from get_namespace_stats_response.proto
- [`GetRequest`](#get_request) - from get_request.proto
- [`GetResponse`](#get_response) - from get_response.proto
- [`ImportRequest`](#import_request) - from import_request.proto
- [`IncrementRequest`](#increment_request) - from increment_request.proto
- [`IncrementResponse`](#increment_response) - from increment_response.proto
- [`InfoRequest`](#info_request) - from info_request.proto
- [`KeysRequest`](#keys_request) - from keys_request.proto
- [`KeysResponse`](#keys_response) - from keys_response.proto
- [`ListDatabasesRequest`](#list_databases_request) - from list_databases_request.proto
- [`ListDatabasesResponse`](#list_databases_response) - from list_databases_response.proto
- [`ListMigrationsRequest`](#list_migrations_request) - from list_migrations_request.proto
- [`ListMigrationsResponse`](#list_migrations_response) - from list_migrations_response.proto
- [`ListNamespacesRequest`](#list_namespaces_request) - from list_namespaces_request.proto
- [`ListNamespacesResponse`](#list_namespaces_response) - from list_namespaces_response.proto
- [`ListSchemasRequest`](#list_schemas_request) - from list_schemas_request.proto
- [`ListSchemasResponse`](#list_schemas_response) - from list_schemas_response.proto
- [`LockRequest`](#lock_request) - from lock_request.proto
- [`MGetRequest`](#m_get_request) - from m_get_request.proto
- [`MigrationInfo`](#migration_info) - from migration_info.proto
- [`MigrationScript`](#migration_script) - from migration_script.proto
- [`MySQLConfig`](#my_sql_config) - from my_sql_config.proto
- [`MySQLStatus`](#my_sql_status) - from my_sql_status.proto
- [`NamespaceInfo`](#namespace_info) - from namespace_info.proto
- [`NamespaceStats`](#namespace_stats) - from namespace_stats.proto
- [`OptimizeRequest`](#optimize_request) - from optimize_request.proto
- [`PebbleConfig`](#pebble_config) - from pebble_config.proto
- [`PipelineRequest`](#pipeline_request) - from pipeline_request.proto
- [`PoolStats`](#pool_stats) - from pool_stats.proto
- [`PrependRequest`](#prepend_request) - from prepend_request.proto
- [`QueryOptions`](#query_options) - from query_options.proto
- [`QueryParameter`](#query_parameter) - from query_parameter.proto
- [`QueryRequest`](#query_request) - from query_request.proto
- [`QueryResponse`](#query_response) - from query_response.proto
- [`QueryRowRequest`](#query_row_request) - from query_row_request.proto
- [`QueryRowResponse`](#query_row_response) - from query_row_response.proto
- [`RestoreRequest`](#restore_request) - from restore_request.proto
- [`ResultSet`](#result_set) - from result_set.proto
- [`RevertMigrationRequest`](#revert_migration_request) - from revert_migration_request.proto
- [`RevertMigrationResponse`](#revert_migration_response) - from revert_migration_response.proto
- [`RollbackTransactionRequest`](#rollback_transaction_request) - from rollback_transaction_request.proto
- [`Row`](#row) - from row.proto
- [`RunMigrationRequest`](#run_migration_request) - from run_migration_request.proto
- [`RunMigrationResponse`](#run_migration_response) - from run_migration_response.proto
- [`ScanRequest`](#scan_request) - from scan_request.proto
- [`SetMultipleRequest`](#set_multiple_request) - from set_multiple_request.proto
- [`SetMultipleResponse`](#set_multiple_response) - from set_multiple_response.proto
- [`SetOptions`](#set_options) - from set_options.proto
- [`SetRequest`](#set_request) - from set_request.proto
- [`SetResponse`](#set_response) - from set_response.proto
- [`TouchExpirationRequest`](#touch_expiration_request) - from touch_expiration_request.proto
- [`TouchExpirationResponse`](#touch_expiration_response) - from touch_expiration_response.proto
- [`TransactionOptions`](#transaction_options) - from transaction_options.proto
- [`TransactionRequest`](#transaction_request) - from transaction_request.proto
- [`TransactionStatusRequest`](#transaction_status_request) - from transaction_status_request.proto
- [`TransactionStatusResponse`](#transaction_status_response) - from transaction_status_response.proto
- [`UnlockRequest`](#unlock_request) - from unlock_request.proto
- [`UnwatchRequest`](#unwatch_request) - from unwatch_request.proto

### Files in this Module

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
- [unsubscribe_request.proto](#unsubscribe_request)
- [unwatch_request.proto](#unwatch_request)
- [watch_request.proto](#watch_request)
- [cache_config.proto](#cache_config)
- [cockroach_config.proto](#cockroach_config)
- [configure_policy_request.proto](#configure_policy_request)
- [configure_policy_response.proto](#configure_policy_response)
- [my_sql_config.proto](#my_sql_config)
- [pebble_config.proto](#pebble_config)
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


## Messages Documentation

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

### unsubscribe_request.proto {#unsubscribe_request}

**Path**: `gcommon/v1/database/unsubscribe_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `CacheUnsubscribeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/unsubscribe_request.proto
// version: 1.0.0
// guid: ab8ca5f1-cb63-41bc-88d5-0aef5bd4f76a
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to unsubscribe from cache events.
 */
message CacheUnsubscribeRequest {
  // Topic or channel name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### unwatch_request.proto {#unwatch_request}

**Path**: `gcommon/v1/database/unwatch_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `UnwatchRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/unwatch_request.proto
// version: 1.0.0
// guid: d369ada8-e4ff-4d62-98c8-97e1d767763e
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to stop watching a cache key for changes.
 */
message UnwatchRequest {
  // Key being watched
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### watch_request.proto {#watch_request}

**Path**: `gcommon/v1/database/watch_request.proto` **Package**: `gcommon.v1.database` **Lines**: 25

**Messages** (1): `CacheWatchRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/watch_request.proto
// version: 1.0.0
// guid: ec773ec9-0060-4165-a6a0-7d33894d0f75
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Request to watch a cache key for changes.
 */
message CacheWatchRequest {
  // Key to watch
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

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

