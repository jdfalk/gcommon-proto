// file: pkg/db/sqlite/driver.go
package sqlite

import (
	"context"
	"database/sql"
	"fmt"
	"reflect"
	"sync"
	"time"

	// Import SQLite driver
	"github.com/google/uuid"
	_ "github.com/mattn/go-sqlite3"

	"github.com/jdfalk/gcommon/pkg/db"
	dbgrpc "github.com/jdfalk/gcommon/pkg/db/grpc"
)

// DefaultMaxOpenConns is the default maximum number of open connections for SQLite
const DefaultMaxOpenConns = 1 // SQLite works best with a single connection

// DefaultMaxIdleConns is the default maximum number of idle connections for SQLite
const DefaultMaxIdleConns = 1

// DefaultConnMaxLifetime is the default maximum lifetime of a connection for SQLite
const DefaultConnMaxLifetime = time.Hour

// Config represents the configuration for an SQLite database
type Config struct {
	// Path is the path to the SQLite database file
	Path string

	// Memory indicates if the database should be in-memory
	Memory bool

	// connTimeout is the timeout for establishing a connection
	connTimeout time.Duration

	// MaxOpenConns is the maximum number of open connections
	MaxOpenConns int

	// MaxIdleConns is the maximum number of idle connections
	MaxIdleConns int

	// connMaxLifetime is the maximum lifetime of a connection
	connMaxLifetime time.Duration

	// DriverOptions contains additional driver-specific options
	DriverOptions map[string]interface{}
}

// NewConfig creates a new SQLite configuration with default values
func NewConfig(path string) *Config {
	return &Config{
		Path:            path,
		Memory:          false,
		connTimeout:     5 * time.Second,
		MaxOpenConns:    DefaultMaxOpenConns,
		MaxIdleConns:    DefaultMaxIdleConns,
		connMaxLifetime: DefaultConnMaxLifetime,
		DriverOptions:   make(map[string]interface{}),
	}
}

// NewMemoryConfig creates a new in-memory SQLite configuration
func NewMemoryConfig() *Config {
	return &Config{
		Path:            ":memory:",
		Memory:          true,
		connTimeout:     5 * time.Second,
		MaxOpenConns:    DefaultMaxOpenConns,
		MaxIdleConns:    DefaultMaxIdleConns,
		connMaxLifetime: DefaultConnMaxLifetime,
		DriverOptions:   make(map[string]interface{}),
	}
}

// Driver returns the database driver type
func (c *Config) Driver() db.DriverType {
	return db.DriverSQLite
}

// ConnectionString returns the connection string for the database
func (c *Config) ConnectionString() string {
	if c.Memory {
		return "file::memory:?cache=shared"
	}
	return fmt.Sprintf("file:%s?_busy_timeout=5000", c.Path)
}

// ConnectionTimeout returns the connection timeout
func (c *Config) ConnectionTimeout() time.Duration {
	return c.connTimeout
}

// MaxOpenConnections returns the maximum number of open connections
func (c *Config) MaxOpenConnections() int {
	return c.MaxOpenConns
}

// MaxIdleConnections returns the maximum number of idle connections
func (c *Config) MaxIdleConnections() int {
	return c.MaxIdleConns
}

// ConnMaxLifetime returns the maximum lifetime of a connection
func (c *Config) ConnMaxLifetime() time.Duration {
	return c.connMaxLifetime
}

// Options returns additional driver-specific options
func (c *Config) Options() map[string]interface{} {
	return c.DriverOptions
}

// Database represents an SQLite database
type Database struct {
	db     *sql.DB
	config *Config
	mu     sync.RWMutex
}

// New creates a new SQLite database instance
func New(cfg *Config) (*Database, error) {
	if cfg == nil {
		cfg = NewMemoryConfig()
	}

	connectionString := cfg.ConnectionString()
	db, err := sql.Open("sqlite3", connectionString)
	if err != nil {
		return nil, fmt.Errorf("failed to open SQLite database: %w", err)
	}

	// Set connection pool parameters
	db.SetMaxOpenConns(cfg.MaxOpenConns)
	db.SetMaxIdleConns(cfg.MaxIdleConns)
	db.SetConnMaxLifetime(cfg.ConnMaxLifetime())

	// Set pragmas for better performance
	if _, err := db.Exec("PRAGMA journal_mode=WAL"); err != nil {
		db.Close()
		return nil, fmt.Errorf("failed to set journal_mode pragma: %w", err)
	}

	if _, err := db.Exec("PRAGMA synchronous=NORMAL"); err != nil {
		db.Close()
		return nil, fmt.Errorf("failed to set synchronous pragma: %w", err)
	}

	if _, err := db.Exec("PRAGMA foreign_keys=ON"); err != nil {
		db.Close()
		return nil, fmt.Errorf("failed to set foreign_keys pragma: %w", err)
	}

	// Apply custom pragmas from options
	for key, value := range cfg.DriverOptions {
		if key == "pragma" {
			// If the option is specified as a pragma map
			if pragmas, ok := value.(map[string]interface{}); ok {
				for pragma, pragmaVal := range pragmas {
					if _, err := db.Exec(fmt.Sprintf("PRAGMA %s=%v", pragma, pragmaVal)); err != nil {
						db.Close()
						return nil, fmt.Errorf("failed to set custom pragma %s: %w", pragma, err)
					}
				}
			}
		}
	}

	// Verify the connection
	ctx, cancel := context.WithTimeout(context.Background(), cfg.connTimeout)
	defer cancel()

	if err := db.PingContext(ctx); err != nil {
		db.Close()
		return nil, fmt.Errorf("failed to ping SQLite database: %w", err)
	}

	return &Database{
		db:     db,
		config: cfg,
	}, nil
}

// Driver returns the database driver type
func (d *Database) Driver() db.DriverType {
	return db.DriverSQLite
}

// Execute runs a query without returning any rows
func (d *Database) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	d.mu.RLock()
	defer d.mu.RUnlock()

	result, err := d.db.ExecContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query: %w", err)
	}

	return &sqliteResult{result: result}, nil
}

// Query executes a query that returns rows
func (d *Database) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	d.mu.RLock()
	defer d.mu.RUnlock()

	rows, err := d.db.QueryContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query: %w", err)
	}

	return &sqliteRows{rows: rows}, nil
}

// QueryRow executes a query that is expected to return at most one row
func (d *Database) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	d.mu.RLock()
	defer d.mu.RUnlock()

	row := d.db.QueryRowContext(ctx, query, args...)
	return &sqliteRow{row: row}
}

// Begin starts a transaction with default options
func (d *Database) Begin(ctx context.Context) (db.Transaction, error) {
	return d.BeginTx(ctx, nil)
}

// BeginTx starts a transaction with specified options
func (d *Database) BeginTx(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
	d.mu.Lock()
	defer d.mu.Unlock()

	var txOpts *sql.TxOptions
	if opts != nil {
		txOpts = &sql.TxOptions{
			ReadOnly: opts.ReadOnly,
		}

		// Map isolation levels to SQL standard
		switch opts.Isolation {
		case db.IsolationLevelReadUncommitted:
			txOpts.Isolation = sql.LevelReadUncommitted
		case db.IsolationLevelReadCommitted:
			txOpts.Isolation = sql.LevelReadCommitted
		case db.IsolationLevelRepeatableRead:
			txOpts.Isolation = sql.LevelRepeatableRead
		case db.IsolationLevelSerializable:
			txOpts.Isolation = sql.LevelSerializable
		}
	}

	tx, err := d.db.BeginTx(ctx, txOpts)
	if err != nil {
		return nil, fmt.Errorf("failed to begin transaction: %w", err)
	}

	return &sqliteTransaction{
		tx: tx,
		id: uuid.New().String(),
	}, nil
}

// Stats returns database statistics
func (d *Database) Stats() db.Stats {
	d.mu.RLock()
	defer d.mu.RUnlock()

	sqlStats := d.db.Stats()
	return db.Stats{
		OpenConnections:    sqlStats.OpenConnections,
		InUse:              sqlStats.InUse,
		Idle:               sqlStats.Idle,
		WaitCount:          sqlStats.WaitCount,
		WaitDuration:       sqlStats.WaitDuration,
		MaxOpenConnections: d.config.MaxOpenConns,
		MaxIdleConnections: d.config.MaxIdleConns,
		MaxLifetime:        d.config.connMaxLifetime,
		CustomStats:        make(map[string]string),
	}
}

// Ping checks if the database is accessible
func (d *Database) Ping(ctx context.Context) error {
	d.mu.RLock()
	defer d.mu.RUnlock()

	return d.db.PingContext(ctx)
}

// Close closes the database, releasing any open resources
func (d *Database) Close() error {
	d.mu.Lock()
	defer d.mu.Unlock()

	return d.db.Close()
}

// Raw returns the underlying database driver implementation
func (d *Database) Raw() interface{} {
	return d.db
}

// GRPCService returns the database as a gRPC service
func (d *Database) GRPCService() db.DatabaseGRPCService {
	return dbgrpc.NewDatabaseServer(d)
}

// SQLite-specific result type
type sqliteResult struct {
	result sql.Result
}

// LastInsertId returns the ID of the last inserted row
func (r *sqliteResult) LastInsertId() (int64, error) {
	return r.result.LastInsertId()
}

// RowsAffected returns the number of rows affected by the operation
func (r *sqliteResult) RowsAffected() (int64, error) {
	return r.result.RowsAffected()
}

// SQLite-specific row type
type sqliteRow struct {
	row *sql.Row
}

// Scan copies the columns from the row into the provided variables
func (r *sqliteRow) Scan(dest ...interface{}) error {
	return r.row.Scan(dest...)
}

// Columns returns the column names
func (r *sqliteRow) Columns() ([]string, error) {
	// Standard sql.Row doesn't expose column names, so this is a limitation
	return nil, fmt.Errorf("column names not available for sql.Row")
}

// SQLite-specific rows type
type sqliteRows struct {
	rows *sql.Rows
}

// Next prepares the next row for reading with Scan
func (r *sqliteRows) Next() bool {
	return r.rows.Next()
}

// Scan copies the columns from the current row into the provided variables
func (r *sqliteRows) Scan(dest ...interface{}) error {
	return r.rows.Scan(dest...)
}

// Close closes the rows, releasing any resources
func (r *sqliteRows) Close() error {
	return r.rows.Close()
}

// Err returns any error encountered during iteration
func (r *sqliteRows) Err() error {
	return r.rows.Err()
}

// Columns returns the column names
func (r *sqliteRows) Columns() ([]string, error) {
	return r.rows.Columns()
}

// ColumnTypes returns column type information
func (r *sqliteRows) ColumnTypes() ([]db.ColumnType, error) {
	sqlTypes, err := r.rows.ColumnTypes()
	if err != nil {
		return nil, err
	}

	result := make([]db.ColumnType, len(sqlTypes))
	for i, sqlType := range sqlTypes {
		result[i] = &sqliteColumnType{sqlType: sqlType}
	}
	return result, nil
}

// SQLite-specific transaction type
type sqliteTransaction struct {
	tx *sql.Tx
	id string
}

// Execute runs a query without returning any rows within the transaction
func (t *sqliteTransaction) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	result, err := t.tx.ExecContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query in transaction: %w", err)
	}

	return &sqliteResult{result: result}, nil
}

// Query executes a query that returns rows within the transaction
func (t *sqliteTransaction) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	rows, err := t.tx.QueryContext(ctx, query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query in transaction: %w", err)
	}

	return &sqliteRows{rows: rows}, nil
}

// QueryRow executes a query that is expected to return at most one row within the transaction
func (t *sqliteTransaction) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	row := t.tx.QueryRowContext(ctx, query, args...)
	return &sqliteRow{row: row}
}

// Commit commits the transaction
func (t *sqliteTransaction) Commit() error {
	return t.tx.Commit()
}

// Rollback aborts the transaction
func (t *sqliteTransaction) Rollback() error {
	return t.tx.Rollback()
}

// ID returns a unique identifier for the transaction
func (t *sqliteTransaction) ID() string {
	return t.id
}

// Prepare creates a prepared statement within the transaction
func (t *sqliteTransaction) Prepare(ctx context.Context, query string) (db.Stmt, error) {
	stmt, err := t.tx.PrepareContext(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("failed to prepare statement in transaction: %w", err)
	}
	return &sqlitePreparedStatement{stmt: stmt}, nil
}

// sqliteColumnType wraps sql.ColumnType to implement db.ColumnType
type sqliteColumnType struct {
	sqlType *sql.ColumnType
}

func (c *sqliteColumnType) Name() string {
	return c.sqlType.Name()
}

func (c *sqliteColumnType) DatabaseTypeName() string {
	return c.sqlType.DatabaseTypeName()
}

func (c *sqliteColumnType) Length() (length int64, ok bool) {
	return c.sqlType.Length()
}

func (c *sqliteColumnType) DecimalSize() (precision, scale int64, ok bool) {
	return c.sqlType.DecimalSize()
}

func (c *sqliteColumnType) Nullable() (nullable, ok bool) {
	return c.sqlType.Nullable()
}

func (c *sqliteColumnType) ScanType() reflect.Type {
	return c.sqlType.ScanType()
}

// sqlitePreparedStatement implements db.Stmt for SQLite
type sqlitePreparedStatement struct {
	stmt *sql.Stmt
}

func (s *sqlitePreparedStatement) Execute(ctx context.Context, args ...interface{}) (db.Result, error) {
	result, err := s.stmt.ExecContext(ctx, args...)
	if err != nil {
		return nil, err
	}
	return &sqliteResult{result: result}, nil
}

func (s *sqlitePreparedStatement) Query(ctx context.Context, args ...interface{}) (db.Rows, error) {
	rows, err := s.stmt.QueryContext(ctx, args...)
	if err != nil {
		return nil, err
	}
	return &sqliteRows{rows: rows}, nil
}

func (s *sqlitePreparedStatement) QueryRow(ctx context.Context, args ...interface{}) db.Row {
	row := s.stmt.QueryRowContext(ctx, args...)
	return &sqliteRow{row: row}
}

func (s *sqlitePreparedStatement) Close() error {
	return s.stmt.Close()
}
