// file: pkg/db/interfaces.go
package db

import (
	"context"
	"database/sql"
	"time"
)

// DriverType represents the type of database driver
type DriverType string

const (
	// DriverSQLite represents the SQLite driver
	DriverSQLite DriverType = "sqlite"

	// DriverPostgres represents the PostgreSQL driver
	DriverPostgres DriverType = "postgres"

	// DriverCockroachDB represents the CockroachDB driver
	DriverCockroachDB DriverType = "cockroachdb"

	// DriverPebble represents the Pebble key-value store driver
	DriverPebble DriverType = "pebble"

	// DriverMock represents a mock driver for testing
	DriverMock DriverType = "mock"
)

// IsolationLevel represents the transaction isolation level
type IsolationLevel int

const (
	// IsolationLevelDefault uses the default isolation level for the database
	IsolationLevelDefault IsolationLevel = iota

	// IsolationLevelReadUncommitted corresponds to SQL standard READ UNCOMMITTED
	IsolationLevelReadUncommitted

	// IsolationLevelReadCommitted corresponds to SQL standard READ COMMITTED
	IsolationLevelReadCommitted

	// IsolationLevelRepeatableRead corresponds to SQL standard REPEATABLE READ
	IsolationLevelRepeatableRead

	// IsolationLevelSerializable corresponds to SQL standard SERIALIZABLE
	IsolationLevelSerializable
)

// Database is the central interface for database interactions
type Database interface {
	// Driver returns the database driver type
	Driver() DriverType

	// Execute runs a query without returning any rows
	Execute(ctx context.Context, query string, args ...interface{}) (Result, error)

	// Query executes a query that returns rows
	Query(ctx context.Context, query string, args ...interface{}) (Rows, error)

	// QueryRow executes a query that is expected to return at most one row
	QueryRow(ctx context.Context, query string, args ...interface{}) Row

	// BeginTx starts a transaction with specified options
	BeginTx(ctx context.Context, opts *TxOptions) (Transaction, error)

	// Begin starts a transaction with default options
	Begin(ctx context.Context) (Transaction, error)

	// Stats returns database statistics
	Stats() Stats

	// Ping checks if the database is accessible
	Ping(ctx context.Context) error

	// Close closes the database, releasing any open resources
	Close() error

	// Raw returns the underlying database driver implementation
	// This could be *sql.DB for SQL databases or a client specific to key-value stores
	Raw() interface{}

	// GRPCService returns the database as a gRPC service
	GRPCService() DatabaseGRPCService
}

// DatabaseGRPCService represents the gRPC service interface for a database
type DatabaseGRPCService interface {
	// Must implement the generated gRPC service interface
}

// Result represents the result of a database operation that doesn't return rows
type Result interface {
	// LastInsertId returns the ID of the last inserted row
	LastInsertId() (int64, error)

	// RowsAffected returns the number of rows affected by the operation
	RowsAffected() (int64, error)
}

// Row represents a single row returned from a query
type Row interface {
	// Scan copies the columns from the row into the provided variables
	Scan(dest ...interface{}) error

	// Columns returns the column names
	Columns() ([]string, error)
}

// Rows represents multiple rows returned from a query
type Rows interface {
	// Next prepares the next row for reading with Scan
	// It returns false when there are no more rows or an error occurred
	Next() bool

	// Scan copies the columns from the current row into the provided variables
	Scan(dest ...interface{}) error

	// Close closes the rows, releasing any resources
	Close() error

	// Err returns any error encountered during iteration
	Err() error

	// Columns returns the column names
	Columns() ([]string, error)

	// ColumnTypes returns column type information
	ColumnTypes() ([]*sql.ColumnType, error)
}

// Transaction represents a database transaction
type Transaction interface {
	// Execute runs a query without returning any rows within the transaction
	Execute(ctx context.Context, query string, args ...interface{}) (Result, error)

	// Query executes a query that returns rows within the transaction
	Query(ctx context.Context, query string, args ...interface{}) (Rows, error)

	// QueryRow executes a query that is expected to return at most one row within the transaction
	QueryRow(ctx context.Context, query string, args ...interface{}) Row

	// Commit commits the transaction
	Commit() error

	// Rollback aborts the transaction
	Rollback() error

	// ID returns a unique identifier for the transaction
	ID() string
}

// TxOptions represents transaction options
type TxOptions struct {
	// Isolation represents the isolation level for the transaction
	Isolation IsolationLevel

	// ReadOnly specifies if the transaction is read-only
	ReadOnly bool

	// Timeout specifies a timeout for the transaction
	Timeout time.Duration
}

// Stats represents database statistics
type Stats struct {
	// OpenConnections is the number of established connections both idle and in use
	OpenConnections int

	// InUse is the number of connections currently in use
	InUse int

	// Idle is the number of idle connections
	Idle int

	// WaitCount is the total number of connections waited for
	WaitCount int64

	// WaitDuration is the total time blocked waiting for a new connection
	WaitDuration time.Duration

	// MaxOpenConnections is the maximum number of open connections to the database
	MaxOpenConnections int

	// MaxIdleConnections is the maximum number of idle connections to the database
	MaxIdleConnections int

	// MaxLifetime is the maximum amount of time a connection may be reused
	MaxLifetime time.Duration

	// CustomStats contains database-specific statistics
	CustomStats map[string]string
}

// Config is the interface for database configuration
type Config interface {
	// Driver returns the database driver type
	Driver() DriverType

	// ConnectionString returns the connection string for the database
	ConnectionString() string

	// ConnectionTimeout returns the connection timeout
	ConnectionTimeout() time.Duration

	// MaxOpenConnections returns the maximum number of open connections
	MaxOpenConnections() int

	// MaxIdleConnections returns the maximum number of idle connections
	MaxIdleConnections() int

	// ConnMaxLifetime returns the maximum lifetime of a connection
	ConnMaxLifetime() time.Duration

	// Options returns additional driver-specific options
	Options() map[string]interface{}
}

// Factory is used to create database instances
type Factory interface {
	// Create creates a new database instance with the provided configuration
	Create(cfg Config) (Database, error)

	// CreateWithURI creates a new database instance from a connection URI
	CreateWithURI(driverType DriverType, uri string) (Database, error)
}

// DefaultFactory returns a new default database factory
func DefaultFactory() Factory {
	return &defaultFactory{}
}

// defaultFactory is the default implementation of Factory
type defaultFactory struct{}

// Create creates a new database instance with the provided configuration
func (f *defaultFactory) Create(cfg Config) (Database, error) {
	// Implementation to be added
	return nil, nil
}

// CreateWithURI creates a new database instance from a connection URI
func (f *defaultFactory) CreateWithURI(driverType DriverType, uri string) (Database, error) {
	// Implementation to be added
	return nil, nil
}
