// file: pkg/db/postgres/driver.go
package postgres

import (
	"context"
	"database/sql"
	"fmt"
	"net/url"
	"reflect"
	"strings"
	"sync"
	"time"

	// Import PostgreSQL driver
	_ "github.com/jackc/pgx/v4/stdlib"

	"github.com/jdfalk/gcommon/pkg/db"
)

// Default configuration constants for PostgreSQL
const (
	DefaultMaxOpenConns    = 25
	DefaultMaxIdleConns    = 25
	DefaultConnMaxLifetime = time.Hour
	DefaultConnTimeout     = 5 * time.Second
)

// Config represents the configuration for a PostgreSQL database.
// It implements the db.Config interface and provides PostgreSQL-specific settings.
type Config struct {
	// Host is the database server hostname or IP address
	Host string

	// Port is the database server port (default: 5432)
	Port int

	// Database is the name of the database to connect to
	Database string

	// Username for authentication
	Username string

	// Password for authentication
	Password string

	// SSLMode defines the SSL connection mode (disable, require, verify-ca, verify-full)
	SSLMode string

	// Timezone for the connection
	Timezone string

	// ConnectionTimeout specifies how long to wait for a connection
	connTimeout time.Duration

	// MaxOpenConns is the maximum number of open connections
	MaxOpenConns int

	// MaxIdleConns is the maximum number of idle connections
	MaxIdleConns int

	// ConnMaxLifetime is the maximum amount of time a connection may be reused
	connMaxLifetime time.Duration

	// AdditionalOptions contains driver-specific connection parameters
	AdditionalOptions map[string]string
}

// NewConfig creates a new PostgreSQL configuration with default values.
//
// Parameters:
//   - host: Database server hostname
//   - port: Database server port
//   - database: Database name
//   - username: Username for authentication
//   - password: Password for authentication
//
// Returns:
//   - *Config: A new PostgreSQL configuration with sensible defaults
func NewConfig(host string, port int, database, username, password string) *Config {
	return &Config{
		Host:              host,
		Port:              port,
		Database:          database,
		Username:          username,
		Password:          password,
		SSLMode:           "require",
		Timezone:          "UTC",
		connTimeout:       DefaultConnTimeout,
		MaxOpenConns:      DefaultMaxOpenConns,
		MaxIdleConns:      DefaultMaxIdleConns,
		connMaxLifetime:   DefaultConnMaxLifetime,
		AdditionalOptions: make(map[string]string),
	}
}

// NewConfigFromDSN creates a configuration from a PostgreSQL DSN string.
//
// Parameters:
//   - dsn: PostgreSQL connection string (DSN)
//
// Returns:
//   - *Config: A new PostgreSQL configuration parsed from the DSN
//   - error: Error if DSN parsing fails
func NewConfigFromDSN(dsn string) (*Config, error) {
	u, err := url.Parse(dsn)
	if err != nil {
		return nil, fmt.Errorf("failed to parse DSN: %w", err)
	}

	config := &Config{
		Host:              u.Hostname(),
		Database:          strings.TrimPrefix(u.Path, "/"),
		connTimeout:       DefaultConnTimeout,
		MaxOpenConns:      DefaultMaxOpenConns,
		MaxIdleConns:      DefaultMaxIdleConns,
		connMaxLifetime:   DefaultConnMaxLifetime,
		AdditionalOptions: make(map[string]string),
	}

	// Parse port
	if u.Port() != "" {
		if _, err := fmt.Sscanf(u.Port(), "%d", &config.Port); err != nil {
			return nil, fmt.Errorf("invalid port in DSN: %w", err)
		}
	} else {
		config.Port = 5432 // Default PostgreSQL port
	}

	// Parse user info
	if u.User != nil {
		config.Username = u.User.Username()
		if password, ok := u.User.Password(); ok {
			config.Password = password
		}
	}

	// Parse query parameters
	for key, values := range u.Query() {
		if len(values) > 0 {
			switch key {
			case "sslmode":
				config.SSLMode = values[0]
			case "timezone":
				config.Timezone = values[0]
			default:
				config.AdditionalOptions[key] = values[0]
			}
		}
	}

	return config, nil
}

// Driver returns the database driver type.
//
// Returns:
//   - db.DriverType: Always returns db.DriverPostgres
func (c *Config) Driver() db.DriverType {
	return db.DriverPostgres
}

// ConnectionString builds and returns the PostgreSQL connection string.
//
// Returns:
//   - string: A complete PostgreSQL connection string
func (c *Config) ConnectionString() string {
	var parts []string

	if c.Host != "" {
		parts = append(parts, fmt.Sprintf("host=%s", c.Host))
	}

	if c.Port > 0 {
		parts = append(parts, fmt.Sprintf("port=%d", c.Port))
	}

	if c.Database != "" {
		parts = append(parts, fmt.Sprintf("dbname=%s", c.Database))
	}

	if c.Username != "" {
		parts = append(parts, fmt.Sprintf("user=%s", c.Username))
	}

	if c.Password != "" {
		parts = append(parts, fmt.Sprintf("password=%s", c.Password))
	}

	if c.SSLMode != "" {
		parts = append(parts, fmt.Sprintf("sslmode=%s", c.SSLMode))
	}

	if c.Timezone != "" {
		parts = append(parts, fmt.Sprintf("timezone=%s", c.Timezone))
	}

	// Add additional options
	for key, value := range c.AdditionalOptions {
		parts = append(parts, fmt.Sprintf("%s=%s", key, value))
	}

	return strings.Join(parts, " ")
}

// ConnectionTimeout returns the connection timeout duration.
//
// Returns:
//   - time.Duration: The timeout for establishing connections
func (c *Config) ConnectionTimeout() time.Duration {
	return c.connTimeout
}

// MaxOpenConnections returns the maximum number of open connections.
//
// Returns:
//   - int: Maximum number of open connections to the database
func (c *Config) MaxOpenConnections() int {
	return c.MaxOpenConns
}

// MaxIdleConnections returns the maximum number of idle connections.
//
// Returns:
//   - int: Maximum number of idle connections in the pool
func (c *Config) MaxIdleConnections() int {
	return c.MaxIdleConns
}

// ConnectionMaxLifetime returns the maximum lifetime for connections.
//
// Returns:
//   - time.Duration: Maximum amount of time a connection may be reused
func (c *Config) ConnectionMaxLifetime() time.Duration {
	return c.connMaxLifetime
}

// DriverOptions returns additional driver-specific options.
//
// Returns:
//   - map[string]interface{}: Additional configuration options
func (c *Config) DriverOptions() map[string]interface{} {
	options := make(map[string]interface{})
	for k, v := range c.AdditionalOptions {
		options[k] = v
	}
	return options
}

// Driver is the PostgreSQL implementation of the db.Database interface.
// It provides comprehensive database operations including CRUD operations,
// transaction management, and connection pooling.
type Driver struct {
	db     *sql.DB
	name   string
	config *Config
	mutex  sync.RWMutex
	closed bool
}

// NewDriver creates a new PostgreSQL driver instance.
//
// Parameters:
//   - config: PostgreSQL configuration
//
// Returns:
//   - *Driver: A new PostgreSQL driver instance
//   - error: Error if driver creation fails
func NewDriver(config *Config) (*Driver, error) {
	if config == nil {
		return nil, fmt.Errorf("config cannot be nil")
	}

	// Build connection string
	connStr := config.ConnectionString()
	if connStr == "" {
		return nil, fmt.Errorf("connection string cannot be empty")
	}

	// Create database connection
	database, err := sql.Open("pgx", connStr)
	if err != nil {
		return nil, fmt.Errorf("failed to open PostgreSQL connection: %w", err)
	}

	// Configure connection pool
	database.SetMaxOpenConns(config.MaxOpenConnections())
	database.SetMaxIdleConns(config.MaxIdleConnections())
	database.SetConnMaxLifetime(config.ConnectionMaxLifetime())

	// Test the connection
	ctx, cancel := context.WithTimeout(context.Background(), config.ConnectionTimeout())
	defer cancel()

	if err := database.PingContext(ctx); err != nil {
		database.Close()
		return nil, fmt.Errorf("failed to ping PostgreSQL database: %w", err)
	}

	name := "postgres"
	if config.Database != "" {
		name = config.Database
	}

	return &Driver{
		db:     database,
		name:   name,
		config: config,
	}, nil
}

// Name returns the name of the database connection.
//
// Returns:
//   - string: The database connection name
func (d *Driver) Name() string {
	d.mutex.RLock()
	defer d.mutex.RUnlock()
	return d.name
}

// Driver returns the database driver type.
//
// Returns:
//   - db.DriverType: Always returns db.DriverPostgres
func (d *Driver) Driver() db.DriverType {
	return db.DriverPostgres
}

// Ping tests the database connection.
//
// Parameters:
//   - ctx: Context for the operation
//
// Returns:
//   - error: Error if ping fails, nil if successful
func (d *Driver) Ping(ctx context.Context) error {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return fmt.Errorf("database connection is closed")
	}

	return d.db.PingContext(ctx)
}

// Close closes the database connection and releases all resources.
//
// Returns:
//   - error: Error if closing fails, nil if successful
func (d *Driver) Close() error {
	d.mutex.Lock()
	defer d.mutex.Unlock()

	if d.closed {
		return nil
	}

	d.closed = true
	return d.db.Close()
}

// BeginTx starts a new database transaction with the specified options.
//
// Parameters:
//   - ctx: Context for the transaction
//   - opts: Transaction options including isolation level
//
// Returns:
//   - db.Tx: A new transaction instance
//   - error: Error if transaction creation fails
func (d *Driver) BeginTx(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return nil, fmt.Errorf("database connection is closed")
	}

	var sqlOpts *sql.TxOptions
	if opts != nil {
		sqlOpts = &sql.TxOptions{
			Isolation: sql.IsolationLevel(opts.Isolation),
			ReadOnly:  opts.ReadOnly,
		}
	}

	sqlTx, err := d.db.BeginTx(ctx, sqlOpts)
	if err != nil {
		return nil, fmt.Errorf("failed to begin transaction: %w", err)
	}

	return &transaction{
		tx:     sqlTx,
		driver: d,
	}, nil
}

// Exec executes a query without returning any rows.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query arguments
//
// Returns:
//   - db.Result: Result containing affected rows and last insert ID
//   - error: Error if execution fails
func (d *Driver) Exec(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return nil, fmt.Errorf("database connection is closed")
	}

	result, err := d.db.ExecContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query: %w", err)
	}

	return &queryResult{result: result}, nil
}

// Query executes a query that returns rows.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query arguments
//
// Returns:
//   - db.Rows: Query result rows
//   - error: Error if query execution fails
func (d *Driver) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return nil, fmt.Errorf("database connection is closed")
	}

	rows, err := d.db.QueryContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query: %w", err)
	}

	return &queryRows{rows: rows}, nil
}

// QueryRow executes a query that is expected to return at most one row.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to execute
//   - args: Query arguments
//
// Returns:
//   - db.Row: Single query result row
func (d *Driver) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return &queryRow{err: fmt.Errorf("database connection is closed")}
	}

	sqlRow := d.db.QueryRowContext(ctx, query, args...)
	return &queryRow{row: sqlRow}
}

// Prepare creates a prepared statement for later queries or executions.
//
// Parameters:
//   - ctx: Context for the operation
//   - query: SQL query to prepare
//
// Returns:
//   - db.Stmt: Prepared statement
//   - error: Error if preparation fails
func (d *Driver) Prepare(ctx context.Context, query string) (db.Stmt, error) {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return nil, fmt.Errorf("database connection is closed")
	}

	stmt, err := d.db.PrepareContext(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("failed to prepare statement: %w", err)
	}

	return &preparedStatement{stmt: stmt}, nil
}

// transaction implements the db.Tx interface for PostgreSQL transactions.
type transaction struct {
	tx     *sql.Tx
	driver *Driver
	mutex  sync.RWMutex
	closed bool
}

// Execute executes a query without returning any rows within the transaction.
// This method implements the db.Transaction interface.
func (t *transaction) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	return t.Exec(ctx, query, args...)
}

// Exec executes a query without returning any rows within the transaction.
func (t *transaction) Exec(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	t.mutex.RLock()
	defer t.mutex.RUnlock()

	if t.closed {
		return nil, fmt.Errorf("transaction is closed")
	}

	result, err := t.tx.ExecContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query in transaction: %w", err)
	}

	return &queryResult{result: result}, nil
}

// Query executes a query that returns rows within the transaction.
func (t *transaction) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	t.mutex.RLock()
	defer t.mutex.RUnlock()

	if t.closed {
		return nil, fmt.Errorf("transaction is closed")
	}

	rows, err := t.tx.QueryContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query in transaction: %w", err)
	}

	return &queryRows{rows: rows}, nil
}

// QueryRow executes a query that returns at most one row within the transaction.
func (t *transaction) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	t.mutex.RLock()
	defer t.mutex.RUnlock()

	if t.closed {
		return &queryRow{err: fmt.Errorf("transaction is closed")}
	}

	sqlRow := t.tx.QueryRowContext(ctx, query, args...)
	return &queryRow{row: sqlRow}
}

// Prepare creates a prepared statement within the transaction.
func (t *transaction) Prepare(ctx context.Context, query string) (db.Stmt, error) {
	t.mutex.RLock()
	defer t.mutex.RUnlock()

	if t.closed {
		return nil, fmt.Errorf("transaction is closed")
	}

	stmt, err := t.tx.PrepareContext(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("failed to prepare statement in transaction: %w", err)
	}

	return &preparedStatement{stmt: stmt}, nil
}

// Commit commits the transaction.
func (t *transaction) Commit() error {
	t.mutex.Lock()
	defer t.mutex.Unlock()

	if t.closed {
		return fmt.Errorf("transaction is already closed")
	}

	t.closed = true
	return t.tx.Commit()
}

// Rollback aborts the transaction.
func (t *transaction) Rollback() error {
	t.mutex.Lock()
	defer t.mutex.Unlock()

	if t.closed {
		return nil // Already closed, rollback is a no-op
	}

	t.closed = true
	return t.tx.Rollback()
}

// ID returns a unique identifier for the transaction.
func (t *transaction) ID() string {
	// Generate a simple ID based on the transaction pointer
	return fmt.Sprintf("tx_%p", t.tx)
}

// queryResult implements the db.Result interface.
type queryResult struct {
	result sql.Result
}

// LastInsertId returns the last inserted ID.
func (r *queryResult) LastInsertId() (int64, error) {
	return r.result.LastInsertId()
}

// RowsAffected returns the number of rows affected.
func (r *queryResult) RowsAffected() (int64, error) {
	return r.result.RowsAffected()
}

// queryRows implements the db.Rows interface.
type queryRows struct {
	rows *sql.Rows
}

// Next advances to the next row.
func (r *queryRows) Next() bool {
	return r.rows.Next()
}

// Scan copies the columns in the current row into the values pointed at by dest.
func (r *queryRows) Scan(dest ...interface{}) error {
	return r.rows.Scan(dest...)
}

// Close closes the rows iterator.
func (r *queryRows) Close() error {
	return r.rows.Close()
}

// Err returns the error, if any, that was encountered during iteration.
func (r *queryRows) Err() error {
	return r.rows.Err()
}

// Columns returns the column names.
func (r *queryRows) Columns() ([]string, error) {
	return r.rows.Columns()
}

// ColumnTypes returns column information.
func (r *queryRows) ColumnTypes() ([]db.ColumnType, error) {
	colTypes, err := r.rows.ColumnTypes()
	if err != nil {
		return nil, err
	}

	result := make([]db.ColumnType, len(colTypes))
	for i, ct := range colTypes {
		result[i] = &columnType{ct}
	}

	return result, nil
}

// queryRow implements the db.Row interface.
type queryRow struct {
	row *sql.Row
	err error
}

// Scan copies the columns from the matched row into the values pointed at by dest.
func (r *queryRow) Scan(dest ...interface{}) error {
	if r.err != nil {
		return r.err
	}
	return r.row.Scan(dest...)
}

// Columns returns the column names for the row.
// Note: sql.Row doesn't provide column information, so this is a limitation.
func (r *queryRow) Columns() ([]string, error) {
	if r.err != nil {
		return nil, r.err
	}
	// sql.Row doesn't expose column information
	// This is a limitation of the database/sql package
	return nil, fmt.Errorf("column information not available for single row queries")
}

// preparedStatement implements the db.Stmt interface.
type preparedStatement struct {
	stmt *sql.Stmt
}

// Execute executes the prepared statement.
func (s *preparedStatement) Execute(ctx context.Context, args ...interface{}) (db.Result, error) {
	result, err := s.stmt.ExecContext(ctx, args...)
	if err != nil {
		return nil, err
	}
	return &queryResult{result: result}, nil
}

// Query executes the prepared query statement.
func (s *preparedStatement) Query(ctx context.Context, args ...interface{}) (db.Rows, error) {
	rows, err := s.stmt.QueryContext(ctx, args...)
	if err != nil {
		return nil, err
	}
	return &queryRows{rows: rows}, nil
}

// QueryRow executes the prepared query statement that returns at most one row.
func (s *preparedStatement) QueryRow(ctx context.Context, args ...interface{}) db.Row {
	sqlRow := s.stmt.QueryRowContext(ctx, args...)
	return &queryRow{row: sqlRow}
}

// Close closes the prepared statement.
func (s *preparedStatement) Close() error {
	return s.stmt.Close()
}

// columnType implements the db.ColumnType interface.
type columnType struct {
	*sql.ColumnType
}

// Name returns the name of the column.
func (c *columnType) Name() string {
	return c.ColumnType.Name()
}

// DatabaseTypeName returns the database system type name.
func (c *columnType) DatabaseTypeName() string {
	return c.ColumnType.DatabaseTypeName()
}

// DecimalSize returns the scale and precision of a decimal type.
func (c *columnType) DecimalSize() (precision, scale int64, ok bool) {
	return c.ColumnType.DecimalSize()
}

// Length returns the column type length for variable length column types.
func (c *columnType) Length() (length int64, ok bool) {
	return c.ColumnType.Length()
}

// Nullable reports whether the column may be null.
func (c *columnType) Nullable() (nullable, ok bool) {
	return c.ColumnType.Nullable()
}

// ScanType returns a Go type suitable for scanning into using Rows.Scan.
func (c *columnType) ScanType() reflect.Type {
	return c.ColumnType.ScanType()
}
