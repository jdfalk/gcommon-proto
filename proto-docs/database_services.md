# database_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 6
- **Messages**: 0
- **Services**: 6
- **Enums**: 0

## Files in this Module

- [cache_admin_service.proto](#cache_admin_service)
- [cache_service.proto](#cache_service)
- [database_admin_service.proto](#database_admin_service)
- [database_service.proto](#database_service)
- [migration_service.proto](#migration_service)
- [transaction_service.proto](#transaction_service)
---


## Detailed Documentation

### cache_admin_service.proto {#cache_admin_service}

**Path**: `gcommon/v1/database/cache_admin_service.proto` **Package**: `gcommon.v1.database` **Lines**: 43

**Services** (1): `CacheAdminService`

**Imports** (11):

- `gcommon/v1/database/configure_policy_request.proto`
- `gcommon/v1/database/configure_policy_response.proto`
- `gcommon/v1/database/create_namespace_request.proto`
- `gcommon/v1/database/create_namespace_response.proto`
- `gcommon/v1/database/delete_namespace_request.proto`
- `gcommon/v1/database/get_namespace_stats_request.proto`
- `gcommon/v1/database/get_namespace_stats_response.proto`
- `gcommon/v1/database/list_namespaces_request.proto`
- `gcommon/v1/database/list_namespaces_response.proto`
- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_admin_service.proto
// version: 1.0.2
// guid: d7b6285b-2286-46f8-a2aa-5ef8715919f9
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/configure_policy_request.proto";
import "gcommon/v1/database/configure_policy_response.proto";
import "gcommon/v1/database/create_namespace_request.proto";
import "gcommon/v1/database/create_namespace_response.proto";
import "gcommon/v1/database/delete_namespace_request.proto";
import "gcommon/v1/database/get_namespace_stats_request.proto";
import "gcommon/v1/database/get_namespace_stats_response.proto";
import "gcommon/v1/database/list_namespaces_request.proto";
import "gcommon/v1/database/list_namespaces_response.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";

// (duplicates removed)

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * Administrative cache management operations.
 */
service CacheAdminService {
  // CreateNamespace creates a new cache namespace
  rpc CreateNamespace(CreateNamespaceRequest) returns (CreateNamespaceResponse);

  // DeleteNamespace removes a cache namespace
  rpc DeleteNamespace(DeleteNamespaceRequest) returns (google.protobuf.Empty);

  // ListNamespaces returns all available namespaces
  rpc ListNamespaces(ListNamespacesRequest) returns (ListNamespacesResponse);

  // GetNamespaceStats returns statistics for a namespace
  rpc GetNamespaceStats(GetNamespaceStatsRequest) returns (GetNamespaceStatsResponse);

  // ConfigurePolicy sets cache policies for a namespace
  rpc ConfigurePolicy(ConfigurePolicyRequest) returns (ConfigurePolicyResponse);
}
```

---

### cache_service.proto {#cache_service}

**Path**: `gcommon/v1/database/cache_service.proto` **Package**: `gcommon.v1.database` **Lines**: 88

**Services** (1): `CacheService`

**Imports** (29):

- `gcommon/v1/database/clear_request.proto`
- `gcommon/v1/database/clear_response.proto`
- `gcommon/v1/database/decrement_request.proto`
- `gcommon/v1/database/decrement_response.proto`
- `gcommon/v1/database/delete_multiple_request.proto`
- `gcommon/v1/database/delete_multiple_response.proto`
- `gcommon/v1/database/delete_request.proto`
- `gcommon/v1/database/delete_response.proto`
- `gcommon/v1/database/exists_request.proto`
- `gcommon/v1/database/exists_response.proto`
- `gcommon/v1/database/flush_request.proto`
- `gcommon/v1/database/flush_response.proto`
- `gcommon/v1/database/get_multiple_request.proto`
- `gcommon/v1/database/get_multiple_response.proto`
- `gcommon/v1/database/get_request.proto`
- `gcommon/v1/database/get_response.proto`
- `gcommon/v1/database/get_stats_request.proto`
- `gcommon/v1/database/get_stats_response.proto`
- `gcommon/v1/database/increment_request.proto`
- `gcommon/v1/database/increment_response.proto`
- `gcommon/v1/database/keys_request.proto`
- `gcommon/v1/database/keys_response.proto`
- `gcommon/v1/database/set_multiple_request.proto`
- `gcommon/v1/database/set_multiple_response.proto`
- `gcommon/v1/database/set_request.proto`
- `gcommon/v1/database/set_response.proto`
- `gcommon/v1/database/touch_expiration_request.proto`
- `gcommon/v1/database/touch_expiration_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/cache_service.proto
// version: 1.0.1
// guid: 3f067d2a-5942-4a2c-adcf-14b8ac93813b
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/clear_request.proto";
import "gcommon/v1/database/clear_response.proto";
import "gcommon/v1/database/decrement_request.proto";
import "gcommon/v1/database/decrement_response.proto";
import "gcommon/v1/database/delete_multiple_request.proto";
import "gcommon/v1/database/delete_multiple_response.proto";
import "gcommon/v1/database/delete_request.proto";
import "gcommon/v1/database/delete_response.proto";
import "gcommon/v1/database/exists_request.proto";
import "gcommon/v1/database/exists_response.proto";
import "gcommon/v1/database/flush_request.proto";
import "gcommon/v1/database/flush_response.proto";
import "gcommon/v1/database/get_multiple_request.proto";
import "gcommon/v1/database/get_multiple_response.proto";
import "gcommon/v1/database/get_request.proto";
import "gcommon/v1/database/get_response.proto";
import "gcommon/v1/database/get_stats_request.proto";
import "gcommon/v1/database/get_stats_response.proto";
import "gcommon/v1/database/increment_request.proto";
import "gcommon/v1/database/increment_response.proto";
import "gcommon/v1/database/keys_request.proto";
import "gcommon/v1/database/keys_response.proto";
import "gcommon/v1/database/set_multiple_request.proto";
import "gcommon/v1/database/set_multiple_response.proto";
import "gcommon/v1/database/set_request.proto";
import "gcommon/v1/database/set_response.proto";
import "gcommon/v1/database/touch_expiration_request.proto";
import "gcommon/v1/database/touch_expiration_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * CacheService provides comprehensive caching capabilities.
 * Supports CRUD operations, batch operations, atomic operations,
 * and cache management with flexible expiration policies.
 */
service CacheService {
  // Get retrieves a value from the cache by key
  rpc Get(GetRequest) returns (GetResponse);

  // Set stores a value in the cache with optional expiration
  rpc Set(SetRequest) returns (SetResponse);

  // Delete removes a value from the cache
  rpc Delete(CacheDeleteRequest) returns (CacheDeleteResponse);

  // Exists checks if a key exists in the cache
  rpc Exists(ExistsRequest) returns (ExistsResponse);

  // GetMultiple retrieves multiple values from the cache in a single operation
  rpc GetMultiple(GetMultipleRequest) returns (GetMultipleResponse);

  // SetMultiple stores multiple values in the cache atomically
  rpc SetMultiple(SetMultipleRequest) returns (SetMultipleResponse);

  // DeleteMultiple removes multiple values from the cache atomically
  rpc DeleteMultiple(DeleteMultipleRequest) returns (DeleteMultipleResponse);

  // Increment atomically increments a numeric value
  rpc Increment(IncrementRequest) returns (IncrementResponse);

  // Decrement atomically decrements a numeric value
  rpc Decrement(DecrementRequest) returns (DecrementResponse);

  // Clear removes all entries from the cache or by pattern
  rpc Clear(ClearRequest) returns (ClearResponse);

  // Keys returns all keys matching a pattern
  rpc Keys(KeysRequest) returns (KeysResponse);

  // GetStats returns cache statistics and performance metrics
  rpc GetStats(CacheGetStatsRequest) returns (CacheGetStatsResponse);

  // Flush forces cache persistence if supported by the backend
  rpc Flush(FlushRequest) returns (FlushResponse);

  // TouchExpiration updates the expiration time of an existing key
  rpc TouchExpiration(TouchExpirationRequest) returns (TouchExpirationResponse);
}
```

---

### database_admin_service.proto {#database_admin_service}

**Path**: `gcommon/v1/database/database_admin_service.proto` **Package**: `gcommon.v1.database` **Lines**: 51

**Services** (1): `DatabaseAdminService`

**Imports** (14):

- `gcommon/v1/database/create_database_request.proto`
- `gcommon/v1/database/create_database_response.proto`
- `gcommon/v1/database/create_schema_request.proto`
- `gcommon/v1/database/create_schema_response.proto`
- `gcommon/v1/database/drop_database_request.proto`
- `gcommon/v1/database/drop_schema_request.proto`
- `gcommon/v1/database/get_database_info_request.proto`
- `gcommon/v1/database/get_database_info_response.proto`
- `gcommon/v1/database/list_databases_request.proto`
- `gcommon/v1/database/list_databases_response.proto`
- `gcommon/v1/database/list_schemas_request.proto`
- `gcommon/v1/database/list_schemas_response.proto`
- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/database_admin_service.proto
// version: 1.0.1
// guid: 7f0b5d31-549f-466f-ac8e-e1a8339824cc
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/create_database_request.proto";
import "gcommon/v1/database/create_database_response.proto";
import "gcommon/v1/database/create_schema_request.proto";
import "gcommon/v1/database/create_schema_response.proto";
import "gcommon/v1/database/drop_database_request.proto";
import "gcommon/v1/database/drop_schema_request.proto";
import "gcommon/v1/database/get_database_info_request.proto";
import "gcommon/v1/database/get_database_info_response.proto";
import "gcommon/v1/database/list_databases_request.proto";
import "gcommon/v1/database/list_databases_response.proto";
import "gcommon/v1/database/list_schemas_request.proto";
import "gcommon/v1/database/list_schemas_response.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * DatabaseAdminService provides administrative operations for database
 * management including schema operations and migrations.
 */
service DatabaseAdminService {
  // Create a new database
  rpc CreateDatabase(CreateDatabaseRequest) returns (CreateDatabaseResponse);

  // Remove an existing database
  rpc DropDatabase(DropDatabaseRequest) returns (google.protobuf.Empty);

  // List all available databases
  rpc ListDatabases(ListDatabasesRequest) returns (ListDatabasesResponse);

  // Get metadata about a specific database
  rpc GetDatabaseInfo(GetDatabaseInfoRequest) returns (GetDatabaseInfoResponse);

  // Create a new schema within a database
  rpc CreateSchema(CreateSchemaRequest) returns (CreateSchemaResponse);

  // Remove a schema from a database
  rpc DropSchema(DropSchemaRequest) returns (google.protobuf.Empty);

  // List all schemas in a database
  rpc ListSchemas(ListSchemasRequest) returns (ListSchemasResponse);
}
```

---

### database_service.proto {#database_service}

**Path**: `gcommon/v1/database/database_service.proto` **Package**: `gcommon.v1.database` **Lines**: 47

**Services** (1): `DatabaseService`

**Imports** (13):

- `gcommon/v1/database/execute_batch_request.proto`
- `gcommon/v1/database/execute_batch_response.proto`
- `gcommon/v1/database/execute_request.proto`
- `gcommon/v1/database/execute_response.proto`
- `gcommon/v1/database/get_connection_info_request.proto`
- `gcommon/v1/database/get_connection_info_response.proto`
- `gcommon/v1/database/health_check_request.proto`
- `gcommon/v1/database/health_check_response.proto`
- `gcommon/v1/database/query_request.proto`
- `gcommon/v1/database/query_response.proto`
- `gcommon/v1/database/query_row_request.proto`
- `gcommon/v1/database/query_row_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/database_service.proto
// version: 1.0.1
// guid: 29fba4b4-7bdc-4792-b145-968271984ce0
edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/execute_batch_request.proto";
import "gcommon/v1/database/execute_batch_response.proto";
import "gcommon/v1/database/execute_request.proto";
import "gcommon/v1/database/execute_response.proto";
import "gcommon/v1/database/get_connection_info_request.proto";
import "gcommon/v1/database/get_connection_info_response.proto";
import "gcommon/v1/database/health_check_request.proto";
import "gcommon/v1/database/health_check_response.proto";
import "gcommon/v1/database/query_request.proto";
import "gcommon/v1/database/query_response.proto";
import "gcommon/v1/database/query_row_request.proto";
import "gcommon/v1/database/query_row_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * DatabaseService provides comprehensive database operations including
 * queries, transactions, batch operations, and health monitoring.
 */
service DatabaseService {
  // Execute a read-only query and return results
  rpc Query(QueryRequest) returns (QueryResponse);

  // Execute a query expected to return at most one row
  rpc QueryRow(QueryRowRequest) returns (QueryRowResponse);

  // Execute a write operation (INSERT, UPDATE, DELETE)
  rpc Execute(ExecuteRequest) returns (ExecuteResponse);

  // Execute multiple operations in a single batch
  rpc ExecuteBatch(ExecuteBatchRequest) returns (ExecuteBatchResponse);

  // Get information about database connection pool
  rpc GetConnectionInfo(GetConnectionInfoRequest) returns (GetConnectionInfoResponse);

  // Check database connectivity and health
  rpc HealthCheck(DatabaseHealthCheckRequest) returns (DatabaseHealthCheckResponse);
}
```

---

### migration_service.proto {#migration_service}

**Path**: `gcommon/v1/database/migration_service.proto` **Package**: `gcommon.v1.database` **Lines**: 37

**Services** (1): `MigrationService`

**Imports** (9):

- `gcommon/v1/database/get_migration_status_request.proto`
- `gcommon/v1/database/get_migration_status_response.proto`
- `gcommon/v1/database/list_migrations_request.proto`
- `gcommon/v1/database/list_migrations_response.proto`
- `gcommon/v1/database/revert_migration_request.proto`
- `gcommon/v1/database/revert_migration_response.proto`
- `gcommon/v1/database/run_migration_request.proto`
- `gcommon/v1/database/run_migration_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/migration_service.proto
// version: 1.0.1
// guid: e6a810ad-ad41-4afb-9340-84b009cfdd59

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/get_migration_status_request.proto";
import "gcommon/v1/database/get_migration_status_response.proto";
import "gcommon/v1/database/list_migrations_request.proto";
import "gcommon/v1/database/list_migrations_response.proto";
import "gcommon/v1/database/revert_migration_request.proto";
import "gcommon/v1/database/revert_migration_response.proto";
import "gcommon/v1/database/run_migration_request.proto";
import "gcommon/v1/database/run_migration_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * MigrationService manages database schema migrations.
 */
service MigrationService {
  // Apply one or more migration scripts
  rpc ApplyMigration(RunMigrationRequest) returns (RunMigrationResponse);

  // Revert to a previous migration version
  rpc RevertMigration(RevertMigrationRequest) returns (RevertMigrationResponse);

  // Retrieve migration status for a database
  rpc GetMigrationStatus(GetMigrationStatusRequest) returns (GetMigrationStatusResponse);

  // List migrations and their status
  rpc ListMigrations(ListMigrationsRequest) returns (ListMigrationsResponse);
}
```

---

### transaction_service.proto {#transaction_service}

**Path**: `gcommon/v1/database/transaction_service.proto` **Package**: `gcommon.v1.database` **Lines**: 36

**Services** (1): `TransactionService`

**Imports** (8):

- `gcommon/v1/database/begin_transaction_request.proto`
- `gcommon/v1/database/begin_transaction_response.proto`
- `gcommon/v1/database/commit_transaction_request.proto`
- `gcommon/v1/database/rollback_transaction_request.proto`
- `gcommon/v1/database/transaction_status_request.proto`
- `gcommon/v1/database/transaction_status_response.proto`
- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/transaction_service.proto
// version: 1.0.1
// guid: 48c127b3-f9fa-4a27-bdd8-a41127f3d449

edition = "2023";

package gcommon.v1.database;

import "gcommon/v1/database/begin_transaction_request.proto";
import "gcommon/v1/database/begin_transaction_response.proto";
import "gcommon/v1/database/commit_transaction_request.proto";
import "gcommon/v1/database/rollback_transaction_request.proto";
import "gcommon/v1/database/transaction_status_request.proto";
import "gcommon/v1/database/transaction_status_response.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/database";

/**
 * TransactionService manages database transactions.
 */
service TransactionService {
  // Begin a new transaction
  rpc BeginTransaction(BeginTransactionRequest) returns (BeginTransactionResponse);

  // Commit the specified transaction
  rpc CommitTransaction(CommitTransactionRequest) returns (google.protobuf.Empty);

  // Roll back the specified transaction
  rpc RollbackTransaction(RollbackTransactionRequest) returns (google.protobuf.Empty);

  // Retrieve status information for a transaction
  rpc GetTransactionStatus(TransactionStatusRequest) returns (TransactionStatusResponse);
}
```

---

