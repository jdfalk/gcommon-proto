# database_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 4
- **Messages**: 0
- **Services**: 4
- **Enums**: 0

## Files in this Module

- [database_admin_service.proto](#database_admin_service)
- [database_service.proto](#database_service)
- [migration_service.proto](#migration_service)
- [transaction_service.proto](#transaction_service)

## Module Dependencies

**This module depends on**:

- [auth_api_2](./auth_api_2.md)
- [cache_api_1](./cache_api_1.md)
- [config_api](./config_api.md)
- [database_api](./database_api.md)
- [health](./health.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [web_api_2](./web_api_2.md)

---

## Detailed Documentation

### database_admin_service.proto {#database_admin_service}

**Path**: `pkg/db/proto/database_admin_service.proto` **Package**: `gcommon.v1.database` **Lines**: 50

**Services** (1): `DatabaseAdminService`

**Imports** (14):

- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`
- `pkg/db/proto/create_database_request.proto` → [database_api](./database_api.md#create_database_request)
- `pkg/db/proto/create_database_response.proto` → [database_api](./database_api.md#create_database_response)
- `pkg/db/proto/create_schema_request.proto` → [database_api](./database_api.md#create_schema_request)
- `pkg/db/proto/create_schema_response.proto` → [database_api](./database_api.md#create_schema_response)
- `pkg/db/proto/drop_database_request.proto` → [database_api](./database_api.md#drop_database_request)
- `pkg/db/proto/drop_schema_request.proto` → [database_api](./database_api.md#drop_schema_request)
- `pkg/db/proto/get_database_info_request.proto` → [database_api](./database_api.md#get_database_info_request)
- `pkg/db/proto/get_database_info_response.proto` → [database_api](./database_api.md#get_database_info_response)
- `pkg/db/proto/list_databases_request.proto` → [database_api](./database_api.md#list_databases_request)
- `pkg/db/proto/list_databases_response.proto` → [database_api](./database_api.md#list_databases_response)
- `pkg/db/proto/list_schemas_request.proto` → [database_api](./database_api.md#list_schemas_request)
- `pkg/db/proto/list_schemas_response.proto` → [database_api](./database_api.md#list_schemas_response)

#### Source Code

```protobuf
// file: pkg/db/proto/services/database_admin_service.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";
import "pkg/db/proto/create_database_request.proto";
import "pkg/db/proto/create_database_response.proto";
import "pkg/db/proto/create_schema_request.proto";
import "pkg/db/proto/create_schema_response.proto";
import "pkg/db/proto/drop_database_request.proto";
import "pkg/db/proto/drop_schema_request.proto";
import "pkg/db/proto/get_database_info_request.proto";
import "pkg/db/proto/get_database_info_response.proto";
import "pkg/db/proto/list_databases_request.proto";
import "pkg/db/proto/list_databases_response.proto";
import "pkg/db/proto/list_schemas_request.proto";
import "pkg/db/proto/list_schemas_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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

**Path**: `pkg/db/proto/database_service.proto` **Package**: `gcommon.v1.database` **Lines**: 46

**Services** (1): `DatabaseService`

**Imports** (13):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/execute_batch_request.proto` → [database_api](./database_api.md#execute_batch_request)
- `pkg/db/proto/execute_batch_response.proto` → [database_api](./database_api.md#execute_batch_response)
- `pkg/db/proto/execute_request.proto` → [database_api](./database_api.md#execute_request)
- `pkg/db/proto/execute_response.proto` → [database_api](./database_api.md#execute_response)
- `pkg/db/proto/get_connection_info_request.proto` → [database_api](./database_api.md#get_connection_info_request)
- `pkg/db/proto/get_connection_info_response.proto` → [database_api](./database_api.md#get_connection_info_response)
- `pkg/db/proto/health_check_request.proto` → [auth_api_2](./auth_api_2.md#health_check_request) → [cache_api_1](./cache_api_1.md#health_check_request) → [config_api](./config_api.md#health_check_request) →
  [database_api](./database_api.md#health_check_request) → [health](./health.md#health_check_request) → [metrics_api_1](./metrics_api_1.md#health_check_request) → [queue_api_2](./queue_api_2.md#health_check_request) →
  [web_api_2](./web_api_2.md#health_check_request)
- `pkg/db/proto/health_check_response.proto` → [auth_api_2](./auth_api_2.md#health_check_response) → [config_api](./config_api.md#health_check_response) → [database_api](./database_api.md#health_check_response) →
  [health](./health.md#health_check_response) → [metrics_api_1](./metrics_api_1.md#health_check_response) → [queue_api_2](./queue_api_2.md#health_check_response) → [web_api_2](./web_api_2.md#health_check_response)
- `pkg/db/proto/query_request.proto` → [database_api](./database_api.md#query_request)
- `pkg/db/proto/query_response.proto` → [database_api](./database_api.md#query_response)
- `pkg/db/proto/query_row_request.proto` → [database_api](./database_api.md#query_row_request)
- `pkg/db/proto/query_row_response.proto` → [database_api](./database_api.md#query_row_response)

#### Source Code

```protobuf
// file: pkg/db/proto/services/database_service.proto
edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/execute_batch_request.proto";
import "pkg/db/proto/execute_batch_response.proto";
import "pkg/db/proto/execute_request.proto";
import "pkg/db/proto/execute_response.proto";
import "pkg/db/proto/get_connection_info_request.proto";
import "pkg/db/proto/get_connection_info_response.proto";
import "pkg/db/proto/health_check_request.proto";
import "pkg/db/proto/health_check_response.proto";
import "pkg/db/proto/query_request.proto";
import "pkg/db/proto/query_response.proto";
import "pkg/db/proto/query_row_request.proto";
import "pkg/db/proto/query_row_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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
  rpc HealthCheck(HealthCheckRequest) returns (HealthCheckResponse);
}

```

---

### migration_service.proto {#migration_service}

**Path**: `pkg/db/proto/migration_service.proto` **Package**: `gcommon.v1.database` **Lines**: 38

**Services** (1): `MigrationService`

**Imports** (9):

- `google/protobuf/go_features.proto`
- `pkg/db/proto/get_migration_status_request.proto` → [database_api](./database_api.md#get_migration_status_request)
- `pkg/db/proto/get_migration_status_response.proto` → [database_api](./database_api.md#get_migration_status_response)
- `pkg/db/proto/list_migrations_request.proto` → [database_api](./database_api.md#list_migrations_request)
- `pkg/db/proto/list_migrations_response.proto` → [database_api](./database_api.md#list_migrations_response)
- `pkg/db/proto/revert_migration_request.proto` → [database_api](./database_api.md#revert_migration_request)
- `pkg/db/proto/revert_migration_response.proto` → [database_api](./database_api.md#revert_migration_response)
- `pkg/db/proto/run_migration_request.proto` → [database_api](./database_api.md#run_migration_request)
- `pkg/db/proto/run_migration_response.proto` → [database_api](./database_api.md#run_migration_response)

#### Source Code

```protobuf
// file: pkg/db/proto/services/migration_service.proto
// version: 1.0.0
// guid: e6a810ad-ad41-4afb-9340-84b009cfdd59

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/go_features.proto";
import "pkg/db/proto/get_migration_status_request.proto";
import "pkg/db/proto/get_migration_status_response.proto";
import "pkg/db/proto/list_migrations_request.proto";
import "pkg/db/proto/list_migrations_response.proto";
import "pkg/db/proto/revert_migration_request.proto";
import "pkg/db/proto/revert_migration_response.proto";
import "pkg/db/proto/run_migration_request.proto";
import "pkg/db/proto/run_migration_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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

**Path**: `pkg/db/proto/transaction_service.proto` **Package**: `gcommon.v1.database` **Lines**: 37

**Services** (1): `TransactionService`

**Imports** (8):

- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`
- `pkg/db/proto/begin_transaction_request.proto` → [database_api](./database_api.md#begin_transaction_request)
- `pkg/db/proto/begin_transaction_response.proto` → [database_api](./database_api.md#begin_transaction_response)
- `pkg/db/proto/commit_transaction_request.proto` → [database_api](./database_api.md#commit_transaction_request)
- `pkg/db/proto/rollback_transaction_request.proto` → [database_api](./database_api.md#rollback_transaction_request)
- `pkg/db/proto/transaction_status_request.proto` → [database_api](./database_api.md#transaction_status_request)
- `pkg/db/proto/transaction_status_response.proto` → [database_api](./database_api.md#transaction_status_response)

#### Source Code

```protobuf
// file: pkg/db/proto/services/transaction_service.proto
// version: 1.0.0
// guid: 48c127b3-f9fa-4a27-bdd8-a41127f3d449

edition = "2023";

package gcommon.v1.database;

import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";
import "pkg/db/proto/begin_transaction_request.proto";
import "pkg/db/proto/begin_transaction_response.proto";
import "pkg/db/proto/commit_transaction_request.proto";
import "pkg/db/proto/rollback_transaction_request.proto";
import "pkg/db/proto/transaction_status_request.proto";
import "pkg/db/proto/transaction_status_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/db/proto";

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
