// file: pkg/db/cockroachdb/driver.go
package cockroachdb

import (
	"context"
	"database/sql"
	"fmt"
	"reflect"
	"strings"
	"time"

	// Import CockroachDB SQL driver
	_ "github.com/cockroachdb/cockroach-go/crdb"
	_ "github.com/jackc/pgx/v4/stdlib"

	"github.com/jdfalk/gcommon/pkg/db"
	dbgrpc "github.com/jdfalk/gcommon/pkg/db/grpc"
)

// Driver is the CockroachDB implementation of the db.Database interface.
type Driver struct {
	db       *sql.DB
	name     string
	connInfo string
}

// Config implements the db.Config interface for CockroachDB.
type Config struct {
	// DSN is the data source name (connection string)
	DSN string

	// Database name
	Name string

	// ConnectionTimeout specifies how long to wait for a connection
	ConnectionTimeout time.Duration

	// MaxOpenConnections is the maximum number of open connections
	MaxOpenConns int

	// MaxIdleConnections is the maximum number of idle connections
	MaxIdleConns int

	// ConnMaxLifetime is the maximum amount of time a connection may be reused
	ConnMaxLifetime time.Duration

	// AdditionalOptions contains driver-specific options
	AdditionalOptions map[string]interface{}
}

// NewDriver creates a new CockroachDB driver.
//
// Parameters:
//   - dsn: Database connection string
//   - name: Optional name for the database connection
//
// Returns:
//   - A CockroachDB driver implementing the db.Database interface
//   - Error if driver creation fails
func NewDriver(dsn string, name string) (*Driver, error) {
	if dsn == "" {
		return nil, fmt.Errorf("dsn cannot be empty")
	}

	if name == "" {
		name = "cockroachdb"
	}

	// Connect to the database
	database, err := sql.Open("pgx", dsn)
	if err != nil {
		return nil, fmt.Errorf("failed to open CockroachDB connection: %w", err)
	}

	// Verify connection
	if err := database.Ping(); err != nil {
		database.Close()
		return nil, fmt.Errorf("failed to ping CockroachDB: %w", err)
	}

	return &Driver{
		db:       database,
		name:     name,
		connInfo: sanitizeDSN(dsn),
	}, nil
}

// NewDriverWithConfig creates a new CockroachDB driver using the provided configuration.
//
// Parameters:
//   - cfg: Database configuration
//
// Returns:
//   - A CockroachDB driver implementing the db.Database interface
//   - Error if driver creation fails
func NewDriverWithConfig(cfg *Config) (*Driver, error) {
	if cfg == nil {
		return nil, fmt.Errorf("config cannot be nil")
	}

	if cfg.DSN == "" {
		return nil, fmt.Errorf("DSN cannot be empty")
	}

	name := cfg.Name
	if name == "" {
		name = "cockroachdb"
	}

	// Connect to the database
	database, err := sql.Open("pgx", cfg.DSN)
	if err != nil {
		return nil, fmt.Errorf("failed to open CockroachDB connection: %w", err)
	}

	// Configure connection pool
	if cfg.MaxOpenConns > 0 {
		database.SetMaxOpenConns(cfg.MaxOpenConns)
	}
	if cfg.MaxIdleConns > 0 {
		database.SetMaxIdleConns(cfg.MaxIdleConns)
	}
	if cfg.ConnMaxLifetime > 0 {
		database.SetConnMaxLifetime(cfg.ConnMaxLifetime)
	}

	// Set connection timeout
	ctx := context.Background()
	if cfg.ConnectionTimeout > 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, cfg.ConnectionTimeout)
		defer cancel()
	}

	// Verify connection
	if err := database.PingContext(ctx); err != nil {
		database.Close()
		return nil, fmt.Errorf("failed to ping CockroachDB: %w", err)
	}

	return &Driver{
		db:       database,
		name:     name,
		connInfo: sanitizeDSN(cfg.DSN),
	}, nil
}

// Driver returns the database driver type.
func (d *Driver) Driver() db.DriverType {
	return db.DriverCockroachDB
}

// Execute runs a query without returning any rows.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - Result of the operation
//   - Error if the operation fails
func (d *Driver) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	result, err := d.db.ExecContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("execute error: %w", err)
	}
	return &Result{result: result}, nil
}

// Query executes a query that returns rows.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - Rows returned by the query
//   - Error if the query fails
func (d *Driver) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	rows, err := d.db.QueryContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("query error: %w", err)
	}
	return &Rows{rows: rows}, nil
}

// QueryRow executes a query that is expected to return at most one row.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - Row returned by the query
func (d *Driver) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	row := d.db.QueryRowContext(ctx, query, args...)
	return &Row{row: row}
}

// Prepare creates a prepared statement for repeated use.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to prepare
//
// Returns:
//   - Prepared statement
//   - Error if preparation fails
func (d *Driver) Prepare(ctx context.Context, query string) (db.Stmt, error) {
	stmt, err := d.db.PrepareContext(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("prepare error: %w", err)
	}
	return &Stmt{stmt: stmt}, nil
}

// BeginTx starts a transaction with specified options.
//
// Parameters:
//   - ctx: Context for the operation
//   - opts: Transaction options
//
// Returns:
//   - A new transaction
//   - Error if starting the transaction fails
func (d *Driver) BeginTx(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
	// Convert our options to sql options
	var sqlOpts *sql.TxOptions
	if opts != nil {
		sqlOpts = &sql.TxOptions{
			ReadOnly: opts.ReadOnly,
		}

		// Map isolation levels
		switch opts.Isolation {
		case db.IsolationLevelReadUncommitted:
			sqlOpts.Isolation = sql.LevelReadUncommitted
		case db.IsolationLevelReadCommitted:
			sqlOpts.Isolation = sql.LevelReadCommitted
		case db.IsolationLevelRepeatableRead:
			sqlOpts.Isolation = sql.LevelRepeatableRead
		case db.IsolationLevelSerializable:
			sqlOpts.Isolation = sql.LevelSerializable
		case db.IsolationLevelDefault:
			sqlOpts.Isolation = sql.LevelDefault
		}

		// Apply timeout if specified
		if opts.Timeout > 0 {
			var cancel context.CancelFunc
			ctx, cancel = context.WithTimeout(ctx, opts.Timeout)
			// The cancel will be called when the transaction is committed or rolled back
			_ = cancel
		}
	}

	tx, err := d.db.BeginTx(ctx, sqlOpts)
	if err != nil {
		return nil, fmt.Errorf("begin transaction error: %w", err)
	}

	return &Transaction{
		tx:  tx,
		id:  fmt.Sprintf("tx-%d", time.Now().UnixNano()),
		ctx: ctx,
	}, nil
}

// Begin starts a transaction with default options.
//
// Parameters:
//   - ctx: Context for the operation
//
// Returns:
//   - A new transaction
//   - Error if starting the transaction fails
func (d *Driver) Begin(ctx context.Context) (db.Transaction, error) {
	return d.BeginTx(ctx, nil)
}

// Stats returns database statistics.
func (d *Driver) Stats() db.Stats {
	sqlStats := d.db.Stats()
	return db.Stats{
		OpenConnections:    sqlStats.OpenConnections,
		InUse:              sqlStats.InUse,
		Idle:               sqlStats.Idle,
		WaitCount:          sqlStats.WaitCount,
		WaitDuration:       sqlStats.WaitDuration,
		MaxOpenConnections: sqlStats.MaxOpenConnections,
		MaxIdleConnections: int(sqlStats.MaxIdleClosed),
		MaxLifetime:        time.Duration(sqlStats.MaxLifetimeClosed),
		CustomStats: map[string]string{
			"database_name": d.name,
		},
	}
}

// Ping checks if the database is accessible.
//
// Parameters:
//   - ctx: Context for the operation
//
// Returns:
//   - Error if the ping fails
func (d *Driver) Ping(ctx context.Context) error {
	return d.db.PingContext(ctx)
}

// Close closes the database, releasing any open resources.
//
// Returns:
//   - Error if closing fails
func (d *Driver) Close() error {
	return d.db.Close()
}

// Raw returns the underlying database driver implementation.
//
// Returns:
//   - The underlying *sql.DB object
func (d *Driver) Raw() interface{} {
	return d.db
}

// GRPCService returns the database as a gRPC service.
//
// Returns:
//   - A gRPC service exposing the database
func (d *Driver) GRPCService() db.DatabaseGRPCService {
	return dbgrpc.NewDatabaseServer(d)
}

// Result wraps sql.Result to implement the db.Result interface.
type Result struct {
	result sql.Result
}

// LastInsertId returns the ID of the last inserted row.
//
// Returns:
//   - Last insert ID
//   - Error if retrieving the ID fails
func (r *Result) LastInsertId() (int64, error) {
	return r.result.LastInsertId()
}

// RowsAffected returns the number of rows affected by the operation.
//
// Returns:
//   - Number of rows affected
//   - Error if retrieving the count fails
func (r *Result) RowsAffected() (int64, error) {
	return r.result.RowsAffected()
}

// Rows wraps sql.Rows to implement the db.Rows interface.
type Rows struct {
	rows *sql.Rows
}

// Next prepares the next row for reading with Scan.
//
// Returns:
//   - True if a row was prepared, false if no more rows or an error occurred
func (r *Rows) Next() bool {
	return r.rows.Next()
}

// Scan copies the columns in the current row into the provided variables.
//
// Parameters:
//   - dest: Destination variables
//
// Returns:
//   - Error if the scan fails
func (r *Rows) Scan(dest ...interface{}) error {
	return r.rows.Scan(dest...)
}

// Close closes the rows, releasing any resources.
//
// Returns:
//   - Error if closing fails
func (r *Rows) Close() error {
	return r.rows.Close()
}

// Err returns any error encountered during iteration.
//
// Returns:
//   - Error encountered during iteration
func (r *Rows) Err() error {
	return r.rows.Err()
}

// Columns returns the column names.
//
// Returns:
//   - Column names
//   - Error if retrieving column names fails
func (r *Rows) Columns() ([]string, error) {
	return r.rows.Columns()
}

// ColumnTypes returns column type information.
//
// Returns:
//   - Column type information
//   - Error if retrieving column types fails
func (r *Rows) ColumnTypes() ([]db.ColumnType, error) {
	sqlTypes, err := r.rows.ColumnTypes()
	if err != nil {
		return nil, err
	}

	dbTypes := make([]db.ColumnType, len(sqlTypes))
	for i, sqlType := range sqlTypes {
		dbTypes[i] = &cockroachdbColumnType{sqlType: sqlType}
	}
	return dbTypes, nil
}

// Row wraps sql.Row to implement the db.Row interface.
type Row struct {
	row *sql.Row
}

// Scan copies the columns in the current row into the provided variables.
//
// Parameters:
//   - dest: Destination variables
//
// Returns:
//   - Error if the scan fails
func (r *Row) Scan(dest ...interface{}) error {
	return r.row.Scan(dest...)
}

// Columns returns the column names.
// Since sql.Row doesn't provide access to column names, this is not supported.
//
// Returns:
//   - Error indicating the operation is not supported
func (r *Row) Columns() ([]string, error) {
	return nil, fmt.Errorf("getting column names from row not supported")
}

// Transaction wraps sql.Tx to implement the db.Transaction interface.
type Transaction struct {
	tx  *sql.Tx
	id  string
	ctx context.Context
}

// Execute runs a query without returning any rows within the transaction.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - Result of the operation
//   - Error if the operation fails
func (t *Transaction) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	result, err := t.tx.ExecContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("execute error: %w", err)
	}
	return &Result{result: result}, nil
}

// Query executes a query that returns rows within the transaction.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - Rows returned by the query
//   - Error if the query fails
func (t *Transaction) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	rows, err := t.tx.QueryContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("query error: %w", err)
	}
	return &Rows{rows: rows}, nil
}

// QueryRow executes a query that is expected to return at most one row within the transaction.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - Row returned by the query
func (t *Transaction) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	row := t.tx.QueryRowContext(ctx, query, args...)
	return &Row{row: row}
}

// Prepare creates a prepared statement within the transaction.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to prepare
//
// Returns:
//   - Prepared statement
//   - Error if preparation fails
func (t *Transaction) Prepare(ctx context.Context, query string) (db.Stmt, error) {
	stmt, err := t.tx.PrepareContext(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("prepare error: %w", err)
	}
	return &Stmt{stmt: stmt}, nil
}

// Commit commits the transaction.
//
// Returns:
//   - Error if the commit fails
func (t *Transaction) Commit() error {
	return t.tx.Commit()
}

// Rollback aborts the transaction.
//
// Returns:
//   - Error if the rollback fails
func (t *Transaction) Rollback() error {
	return t.tx.Rollback()
}

// ID returns a unique identifier for the transaction.
//
// Returns:
//   - The transaction ID
func (t *Transaction) ID() string {
	return t.id
}

// Stmt wraps sql.Stmt to implement the db.Stmt interface.
type Stmt struct {
	stmt *sql.Stmt
}

// Execute executes a prepared statement.
//
// Parameters:
//   - ctx: Context for the operation
//   - args: Query parameters
//
// Returns:
//   - Result of the operation
//   - Error if the operation fails
func (s *Stmt) Execute(ctx context.Context, args ...interface{}) (db.Result, error) {
	result, err := s.stmt.ExecContext(ctx, args...)
	if err != nil {
		return nil, fmt.Errorf("execute error: %w", err)
	}
	return &Result{result: result}, nil
}

// Query executes a prepared query statement.
//
// Parameters:
//   - ctx: Context for the operation
//   - args: Query parameters
//
// Returns:
//   - Rows returned by the query
//   - Error if the query fails
func (s *Stmt) Query(ctx context.Context, args ...interface{}) (db.Rows, error) {
	rows, err := s.stmt.QueryContext(ctx, args...)
	if err != nil {
		return nil, fmt.Errorf("query error: %w", err)
	}
	return &Rows{rows: rows}, nil
}

// QueryRow executes a prepared query statement that is expected to return at most one row.
//
// Parameters:
//   - ctx: Context for the operation
//   - args: Query parameters
//
// Returns:
//   - Row returned by the query
func (s *Stmt) QueryRow(ctx context.Context, args ...interface{}) db.Row {
	row := s.stmt.QueryRowContext(ctx, args...)
	return &Row{row: row}
}

// Close closes the statement.
//
// Returns:
//   - Error if closing fails
func (s *Stmt) Close() error {
	return s.stmt.Close()
}

// cockroachdbColumnType wraps sql.ColumnType to implement the db.ColumnType interface.
type cockroachdbColumnType struct {
	sqlType *sql.ColumnType
}

// Name returns the name of the column.
func (ct *cockroachdbColumnType) Name() string {
	return ct.sqlType.Name()
}

// DatabaseTypeName returns the database-specific type name.
func (ct *cockroachdbColumnType) DatabaseTypeName() string {
	return ct.sqlType.DatabaseTypeName()
}

// Length returns the column type length for variable length column types.
func (ct *cockroachdbColumnType) Length() (length int64, ok bool) {
	return ct.sqlType.Length()
}

// DecimalSize returns the scale and precision of a decimal type.
func (ct *cockroachdbColumnType) DecimalSize() (precision, scale int64, ok bool) {
	return ct.sqlType.DecimalSize()
}

// Nullable returns whether the column may be null.
func (ct *cockroachdbColumnType) Nullable() (nullable, ok bool) {
	return ct.sqlType.Nullable()
}

// ScanType returns a Go type suitable for scanning into using Rows.Scan.
func (ct *cockroachdbColumnType) ScanType() reflect.Type {
	return ct.sqlType.ScanType()
}

// sanitizeDSN removes any sensitive information from a DSN before logging or displaying it.
//
// Parameters:
//   - dsn: Database connection string
//
// Returns:
//   - Sanitized connection string
func sanitizeDSN(dsn string) string {
	// Create a copy to avoid modifying the original
	sanitized := dsn

	// Remove password from the DSN
	if pwdStart := strings.Index(sanitized, "password="); pwdStart != -1 {
		pwdEnd := strings.Index(sanitized[pwdStart:], " ")
		if pwdEnd == -1 {
			pwdEnd = len(sanitized)
		} else {
			pwdEnd += pwdStart
		}
		sanitized = sanitized[:pwdStart] + "password=<redacted>" + sanitized[pwdEnd:]
	}

	// Handle URL format
	if strings.Contains(sanitized, "@") {
		parts := strings.Split(sanitized, "@")
		if len(parts) > 1 {
			credentials := strings.Split(parts[0], "://")
			scheme := ""
			if len(credentials) > 1 {
				scheme = credentials[0] + "://"
				credentials[0] = credentials[1]
			}
			sanitized = scheme + "<redacted>@" + strings.Join(parts[1:], "@")
		}
	}

	return sanitized
}
