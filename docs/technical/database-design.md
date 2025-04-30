# Database Module Technical Design

## Overview

The database module provides a unified interface for database operations with support for multiple database backends. This design document outlines the architecture, interfaces, and implementation details for the database module.

## Goals

- Provide a consistent API for database operations across applications
- Support multiple database backends (SQLite, PostgreSQL, CockroachDB, Pebble)
- Enable efficient connection pooling and management
- Support transactions and atomic operations
- Provide migration capabilities for schema evolution
- Enable query building and execution
- Support prepared statements and parameter binding
- Offer efficient batch operations
- Enable context-aware database operations
- Support both SQL and key-value storage models

## Architecture

### Core Components

```
                     +------------------+
                     |    Interfaces    |
                     +--------+---------+
                              |
          +------------------+-------------------+
          |                  |                   |
     +----+-----+      +-----+------+      +-----+------+
     |    DB    |      | Transaction|      |   Query    |
     +----+-----+      +-----+------+      +-----+------+
          |                  |                   |
          |                  |                   |
+---------+---------+--------+---------+---------+---------+
|                                                          |
|                      Implementations                     |
|                                                          |
+--+-------+-------+--------+--------+-------+------------+
   |       |       |        |        |       |
+--+--+ +--+--+ +--+--+ +---+---+ +--+--+ +--+--+
|SQLite| |Postgres| |Cockroach| |Pebble| |Mock | |In-Memory|
+-----+ +-------+ +--------+ +-------+ +-----+ +---------+
```

### Component Design

#### DB Interface

The core of the module is the `DB` interface, which defines the common operations for database access.

#### Transaction Interface

The `Transaction` interface defines the operations for transaction management.

#### Query Interface

The `Query` interface provides operations for building and executing queries.

#### Driver Implementation

Each database backend has a specific driver implementation that adapts the backend-specific APIs to the common interfaces.

## Interface Design

### DB

```go
// DB represents a database connection.
type DB interface {
    // Exec executes a query without returning any rows.
    Exec(ctx context.Context, query string, args ...interface{}) (Result, error)

    // Query executes a query that returns rows.
    Query(ctx context.Context, query string, args ...interface{}) (Rows, error)

    // QueryRow executes a query that returns at most one row.
    QueryRow(ctx context.Context, query string, args ...interface{}) Row

    // Prepare prepares a statement for later execution.
    Prepare(ctx context.Context, query string) (Stmt, error)

    // Begin starts a new transaction.
    Begin(ctx context.Context) (Tx, error)

    // BeginTx starts a new transaction with the given options.
    BeginTx(ctx context.Context, opts *TxOptions) (Tx, error)

    // Close closes the database connection.
    Close() error

    // Stats returns database statistics.
    Stats() DBStats

    // Ping verifies the connection to the database is still alive.
    Ping(ctx context.Context) error

    // Driver returns the database driver.
    Driver() Driver

    // SetMaxOpenConns sets the maximum number of open connections.
    SetMaxOpenConns(n int)

    // SetMaxIdleConns sets the maximum number of idle connections.
    SetMaxIdleConns(n int)

    // SetConnMaxLifetime sets the maximum connection lifetime.
    SetConnMaxLifetime(d time.Duration)

    // SetConnMaxIdleTime sets the maximum connection idle time.
    SetConnMaxIdleTime(d time.Duration)

    // KV returns a key-value store if supported by the driver.
    KV() (KVStore, error)

    // Migrate runs the given migrations.
    Migrate(ctx context.Context, migrations []Migration) error

    // Schema returns the database schema.
    Schema(ctx context.Context) (*Schema, error)

    // WithLogger sets the logger for the database.
    WithLogger(logger log.Logger) DB
}
```

### Tx (Transaction)

```go
// Tx represents a database transaction.
type Tx interface {
    // Exec executes a query within the transaction.
    Exec(ctx context.Context, query string, args ...interface{}) (Result, error)

    // Query executes a query within the transaction.
    Query(ctx context.Context, query string, args ...interface{}) (Rows, error)

    // QueryRow executes a query that returns at most one row.
    QueryRow(ctx context.Context, query string, args ...interface{}) Row

    // Prepare prepares a statement for execution within the transaction.
    Prepare(ctx context.Context, query string) (Stmt, error)

    // Commit commits the transaction.
    Commit() error

    // Rollback aborts the transaction.
    Rollback() error
}
```

### Stmt (Prepared Statement)

```go
// Stmt represents a prepared statement.
type Stmt interface {
    // Exec executes the statement.
    Exec(ctx context.Context, args ...interface{}) (Result, error)

    // Query executes the statement and returns rows.
    Query(ctx context.Context, args ...interface{}) (Rows, error)

    // QueryRow executes the statement and returns at most one row.
    QueryRow(ctx context.Context, args ...interface{}) Row

    // Close closes the statement.
    Close() error
}
```

### Row

```go
// Row represents a single row returned from a query.
type Row interface {
    // Scan copies the columns from the row into the given values.
    Scan(dest ...interface{}) error

    // Columns returns the column names.
    Columns() ([]string, error)

    // Err returns any error that occurred while reading.
    Err() error

    // ScanStruct scans the row into the given struct.
    ScanStruct(dest interface{}) error
}
```

### Rows

```go
// Rows represents multiple rows returned from a query.
type Rows interface {
    // Next advances to the next row.
    Next() bool

    // Scan copies the columns in the current row into the given values.
    Scan(dest ...interface{}) error

    // Columns returns the column names.
    Columns() ([]string, error)

    // ColumnTypes returns the column types.
    ColumnTypes() ([]*ColumnType, error)

    // Err returns any error that occurred while reading.
    Err() error

    // Close closes the rows.
    Close() error

    // ScanStruct scans the current row into the given struct.
    ScanStruct(dest interface{}) error
}
```

### Result

```go
// Result represents the result of a database operation.
type Result interface {
    // LastInsertId returns the ID of the last inserted row.
    LastInsertId() (int64, error)

    // RowsAffected returns the number of rows affected.
    RowsAffected() (int64, error)
}
```

### KVStore (Key-Value Store)

```go
// KVStore represents a key-value store.
type KVStore interface {
    // Get gets the value for the given key.
    Get(ctx context.Context, key []byte) ([]byte, error)

    // Set sets the value for the given key.
    Set(ctx context.Context, key, value []byte) error

    // Delete deletes the value for the given key.
    Delete(ctx context.Context, key []byte) error

    // Has checks if the given key exists.
    Has(ctx context.Context, key []byte) (bool, error)

    // Scan scans keys with the given prefix.
    Scan(ctx context.Context, prefix []byte, limit int) (Iterator, error)

    // Batch returns a new batch operation.
    Batch() Batch

    // Close closes the store.
    Close() error
}
```

### Batch

```go
// Batch represents a batch operation.
type Batch interface {
    // Set sets the value for the given key.
    Set(key, value []byte)

    // Delete deletes the value for the given key.
    Delete(key []byte)

    // Write applies the batch operations.
    Write(ctx context.Context) error

    // Reset resets the batch.
    Reset()
}
```

### Iterator

```go
// Iterator represents a key-value iterator.
type Iterator interface {
    // Next advances to the next key.
    Next() bool

    // Key returns the current key.
    Key() []byte

    // Value returns the current value.
    Value() []byte

    // Error returns any error that occurred during iteration.
    Error() error

    // Close closes the iterator.
    Close() error
}
```

### Migration

```go
// Migration represents a database migration.
type Migration struct {
    // ID is the migration ID.
    ID string

    // Description is the migration description.
    Description string

    // Up is the migration up function.
    Up func(ctx context.Context, tx Tx) error

    // Down is the migration down function.
    Down func(ctx context.Context, tx Tx) error
}
```

### Schema

```go
// Schema represents a database schema.
type Schema struct {
    // Tables are the database tables.
    Tables []*Table

    // Views are the database views.
    Views []*View

    // Indexes are the database indexes.
    Indexes []*Index
}

// Table represents a database table.
type Table struct {
    // Name is the table name.
    Name string

    // Columns are the table columns.
    Columns []*Column

    // PrimaryKey is the primary key constraint.
    PrimaryKey *Constraint

    // Constraints are the table constraints.
    Constraints []*Constraint
}

// Column represents a database column.
type Column struct {
    // Name is the column name.
    Name string

    // Type is the column type.
    Type string

    // Nullable indicates if the column can be null.
    Nullable bool

    // DefaultValue is the default value.
    DefaultValue interface{}
}

// Constraint represents a database constraint.
type Constraint struct {
    // Name is the constraint name.
    Name string

    // Type is the constraint type.
    Type ConstraintType

    // Columns are the constraint columns.
    Columns []string

    // ReferencesTable is the referenced table.
    ReferencesTable string

    // ReferencesColumns are the referenced columns.
    ReferencesColumns []string

    // OnDelete is the on delete action.
    OnDelete ReferenceAction

    // OnUpdate is the on update action.
    OnUpdate ReferenceAction
}
```

## Configuration

### Config Structure

```go
// Config represents the database configuration.
type Config struct {
    // Driver specifies the database driver to use.
    // Supported values: "sqlite", "postgres", "cockroach", "pebble", "memory"
    Driver string

    // DSN is the data source name.
    DSN string

    // MaxOpenConns is the maximum number of open connections.
    MaxOpenConns int

    // MaxIdleConns is the maximum number of idle connections.
    MaxIdleConns int

    // ConnMaxLifetime is the maximum connection lifetime.
    ConnMaxLifetime time.Duration

    // ConnMaxIdleTime is the maximum connection idle time.
    ConnMaxIdleTime time.Duration

    // SQLiteConfig contains SQLite-specific configuration.
    SQLiteConfig *SQLiteConfig

    // PostgresConfig contains PostgreSQL-specific configuration.
    PostgresConfig *PostgresConfig

    // CockroachConfig contains CockroachDB-specific configuration.
    CockroachConfig *CockroachConfig

    // PebbleConfig contains Pebble-specific configuration.
    PebbleConfig *PebbleConfig
}

// SQLiteConfig represents SQLite-specific configuration.
type SQLiteConfig struct {
    // JournalMode is the journal mode.
    JournalMode string

    // SynchronousMode is the synchronous mode.
    SynchronousMode string

    // ForeignKeys enables foreign key constraints.
    ForeignKeys bool

    // Memory indicates if the database should be in-memory.
    Memory bool

    // CacheSize is the cache size in pages.
    CacheSize int
}

// PostgresConfig represents PostgreSQL-specific configuration.
type PostgresConfig struct {
    // Host is the database host.
    Host string

    // Port is the database port.
    Port int

    // User is the database user.
    User string

    // Password is the database password.
    Password string

    // Database is the database name.
    Database string

    // SSLMode is the SSL mode.
    SSLMode string

    // ApplicationName is the application name.
    ApplicationName string

    // ConnectTimeout is the connection timeout.
    ConnectTimeout time.Duration

    // StatementTimeout is the statement timeout.
    StatementTimeout time.Duration
}

// CockroachConfig represents CockroachDB-specific configuration.
type CockroachConfig struct {
    // Host is the database host.
    Host string

    // Port is the database port.
    Port int

    // User is the database user.
    User string

    // Password is the database password.
    Password string

    // Database is the database name.
    Database string

    // SSLMode is the SSL mode.
    SSLMode string

    // ApplicationName is the application name.
    ApplicationName string

    // RetryBackoffFactor is the retry backoff factor.
    RetryBackoffFactor float64

    // MaxRetries is the maximum number of retries.
    MaxRetries int
}

// PebbleConfig represents Pebble-specific configuration.
type PebbleConfig struct {
    // Path is the database path.
    Path string

    // CacheSize is the cache size in bytes.
    CacheSize int64

    // MemtableSize is the memtable size in bytes.
    MemtableSize int64

    // MaxOpenFiles is the maximum number of open files.
    MaxOpenFiles int

    // Compression enables compression.
    Compression bool
}
```

## Implementation Details

### SQLite Implementation

The SQLite implementation uses the `github.com/mattn/go-sqlite3` package and provides a lightweight, file-based database solution.

### PostgreSQL Implementation

The PostgreSQL implementation uses the `github.com/jackc/pgx/v4` package and provides a robust, server-based database solution.

### CockroachDB Implementation

The CockroachDB implementation builds on the PostgreSQL driver with additional features specific to CockroachDB, such as automatic retry for serialization errors.

### Pebble Implementation

The Pebble implementation uses the `github.com/cockroachdb/pebble` package and provides a high-performance, local key-value store.

### Migration System

The migration system supports both SQL and key-value migrations with versioning and rollback capabilities.

### Query Building

The module includes a query builder to help construct SQL queries safely and efficiently.

## Usage Examples

### Basic Usage

```go
// Configure the database
config := db.Config{
    Driver:         "postgres",
    DSN:            "postgres://user:password@localhost/mydb?sslmode=disable",
    MaxOpenConns:   10,
    MaxIdleConns:   5,
    ConnMaxLifetime: time.Minute * 5,
    PostgresConfig: &db.PostgresConfig{
        ApplicationName: "myapp",
        StatementTimeout: time.Second * 30,
    },
}

// Open the database
database, err := db.Open(config)
if err != nil {
    log.Fatal(err)
}
defer database.Close()

// Set a logger
database = database.WithLogger(logger)

// Execute a simple query
result, err := database.Exec(
    context.Background(),
    "INSERT INTO users (name, email) VALUES ($1, $2)",
    "John Doe",
    "john@example.com",
)
if err != nil {
    log.Error("Failed to insert user", log.Error(err))
    return
}

// Get the last insert ID
id, err := result.LastInsertId()
if err != nil {
    log.Error("Failed to get last insert ID", log.Error(err))
    return
}

log.Info("Inserted user", log.Int64("id", id))

// Query a single row
var user struct {
    ID    int64
    Name  string
    Email string
}

row := database.QueryRow(
    context.Background(),
    "SELECT id, name, email FROM users WHERE id = $1",
    id,
)

err = row.ScanStruct(&user)
if err != nil {
    log.Error("Failed to query user", log.Error(err))
    return
}

log.Info("Found user", log.String("name", user.Name))
```

### Transactions

```go
// Start a transaction
tx, err := database.Begin(context.Background())
if err != nil {
    log.Error("Failed to start transaction", log.Error(err))
    return
}

// Always ensure the transaction is finished
defer func() {
    if err != nil {
        tx.Rollback()
    }
}()

// Execute multiple operations in the transaction
_, err = tx.Exec(
    context.Background(),
    "INSERT INTO accounts (user_id, balance) VALUES ($1, $2)",
    1,
    1000.00,
)
if err != nil {
    log.Error("Failed to insert account", log.Error(err))
    return
}

_, err = tx.Exec(
    context.Background(),
    "INSERT INTO transactions (account_id, amount, description) VALUES ($1, $2, $3)",
    1,
    1000.00,
    "Initial deposit",
)
if err != nil {
    log.Error("Failed to insert transaction", log.Error(err))
    return
}

// Commit the transaction
err = tx.Commit()
if err != nil {
    log.Error("Failed to commit transaction", log.Error(err))
    return
}
```

### Query Multiple Rows

```go
// Query multiple rows
rows, err := database.Query(
    context.Background(),
    "SELECT id, name, email FROM users WHERE active = $1",
    true,
)
if err != nil {
    log.Error("Failed to query users", log.Error(err))
    return
}
defer rows.Close()

// Process the rows
var users []struct {
    ID    int64
    Name  string
    Email string
}

for rows.Next() {
    var user struct {
        ID    int64
        Name  string
        Email string
    }

    err = rows.ScanStruct(&user)
    if err != nil {
        log.Error("Failed to scan user", log.Error(err))
        return
    }

    users = append(users, user)
}

if err = rows.Err(); err != nil {
    log.Error("Error during rows iteration", log.Error(err))
    return
}

log.Info("Found users", log.Int("count", len(users)))
```

### Prepared Statements

```go
// Prepare a statement
stmt, err := database.Prepare(
    context.Background(),
    "SELECT id, name, email FROM users WHERE id = $1",
)
if err != nil {
    log.Error("Failed to prepare statement", log.Error(err))
    return
}
defer stmt.Close()

// Execute the statement multiple times
for _, id := range []int64{1, 2, 3} {
    var user struct {
        ID    int64
        Name  string
        Email string
    }

    row := stmt.QueryRow(context.Background(), id)
    err = row.ScanStruct(&user)
    if err != nil {
        if err == sql.ErrNoRows {
            log.Info("User not found", log.Int64("id", id))
            continue
        }
        log.Error("Failed to query user", log.Error(err))
        return
    }

    log.Info("Found user", log.Int64("id", user.ID), log.String("name", user.Name))
}
```

### Key-Value Store

```go
// Get the key-value store
kv, err := database.KV()
if err != nil {
    log.Error("Key-value store not supported", log.Error(err))
    return
}
defer kv.Close()

// Set a value
err = kv.Set(context.Background(), []byte("key1"), []byte("value1"))
if err != nil {
    log.Error("Failed to set value", log.Error(err))
    return
}

// Get a value
value, err := kv.Get(context.Background(), []byte("key1"))
if err != nil {
    log.Error("Failed to get value", log.Error(err))
    return
}

log.Info("Got value", log.String("value", string(value)))

// Use a batch operation
batch := kv.Batch()
batch.Set([]byte("key2"), []byte("value2"))
batch.Set([]byte("key3"), []byte("value3"))
batch.Delete([]byte("key1"))

err = batch.Write(context.Background())
if err != nil {
    log.Error("Failed to write batch", log.Error(err))
    return
}

// Scan for keys with a prefix
iter, err := kv.Scan(context.Background(), []byte("key"), 10)
if err != nil {
    log.Error("Failed to scan keys", log.Error(err))
    return
}
defer iter.Close()

for iter.Next() {
    key := iter.Key()
    value := iter.Value()
    log.Info("Found key-value pair",
        log.String("key", string(key)),
        log.String("value", string(value)),
    )
}

if err = iter.Error(); err != nil {
    log.Error("Error during iteration", log.Error(err))
    return
}
```

### Migrations

```go
// Define migrations
migrations := []db.Migration{
    {
        ID:          "001_create_users",
        Description: "Create users table",
        Up: func(ctx context.Context, tx db.Tx) error {
            _, err := tx.Exec(ctx, `
                CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            `)
            return err
        },
        Down: func(ctx context.Context, tx db.Tx) error {
            _, err := tx.Exec(ctx, "DROP TABLE users")
            return err
        },
    },
    {
        ID:          "002_create_posts",
        Description: "Create posts table",
        Up: func(ctx context.Context, tx db.Tx) error {
            _, err := tx.Exec(ctx, `
                CREATE TABLE posts (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL REFERENCES users(id),
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            `)
            return err
        },
        Down: func(ctx context.Context, tx db.Tx) error {
            _, err := tx.Exec(ctx, "DROP TABLE posts")
            return err
        },
    },
}

// Run migrations
err = database.Migrate(context.Background(), migrations)
if err != nil {
    log.Error("Failed to run migrations", log.Error(err))
    return
}
```

### Schema Introspection

```go
// Get the database schema
schema, err := database.Schema(context.Background())
if err != nil {
    log.Error("Failed to get schema", log.Error(err))
    return
}

// Print the tables
for _, table := range schema.Tables {
    log.Info("Table", log.String("name", table.Name))

    for _, column := range table.Columns {
        log.Info("Column",
            log.String("name", column.Name),
            log.String("type", column.Type),
            log.Bool("nullable", column.Nullable),
        )
    }

    for _, constraint := range table.Constraints {
        log.Info("Constraint",
            log.String("name", constraint.Name),
            log.String("type", string(constraint.Type)),
            log.Strings("columns", constraint.Columns),
        )
    }
}
```

## Testing Strategy

- Unit tests for each database driver
- Integration tests with actual databases
- Mock database for higher-level tests
- Performance benchmarks for commonly used operations
- Test coverage for edge cases and error conditions

## Security Considerations

- Parameter binding to prevent SQL injection
- Connection pool limits to prevent resource exhaustion
- Properly managed credentials
- TLS for database connections
- Proper error handling to prevent information leakage
- Sanitization of inputs and outputs
- Prepared statements for repetitive queries

## Performance Considerations

- Connection pooling
- Efficient query building
- Batch operations
- Query caching when appropriate
- Index usage optimization
- Minimizing round trips to the database
- Prepared statements for repeated queries
