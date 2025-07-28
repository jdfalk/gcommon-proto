// file: pkg/db/pebble/driver.go
package pebble

import (
	"context"
	"encoding/json"
	"fmt"
	"reflect"
	"sync"
	"time"

	"github.com/cockroachdb/pebble"
	"github.com/jdfalk/gcommon/pkg/db"
)

// Default configuration constants for Pebble
const (
	DefaultCacheSize       = 64 << 20 // 64MB
	DefaultWriteBufferSize = 32 << 20 // 32MB
)

// Config represents the configuration for a Pebble key-value store.
// It implements the db.Config interface and provides Pebble-specific settings.
type Config struct {
	// Path is the directory path where the database files will be stored
	Path string

	// CacheSize is the size of the block cache in bytes
	CacheSize int64

	// WriteBufferSize is the size of the write buffer in bytes
	WriteBufferSize int64

	// Sync specifies whether to sync writes to disk
	Sync bool

	// ReadOnly opens the database in read-only mode
	ReadOnly bool

	// AdditionalOptions contains driver-specific options
	AdditionalOptions map[string]interface{}
}

// NewConfig creates a new Pebble configuration with default values.
//
// Parameters:
//   - path: Directory path for the database files
//
// Returns:
//   - *Config: A new Pebble configuration with sensible defaults
func NewConfig(path string) *Config {
	return &Config{
		Path:              path,
		CacheSize:         DefaultCacheSize,
		WriteBufferSize:   DefaultWriteBufferSize,
		Sync:              true,
		ReadOnly:          false,
		AdditionalOptions: make(map[string]interface{}),
	}
}

// Driver returns the database driver type
func (c *Config) Driver() db.DriverType {
	return db.DriverPebble
}

// ConnectionString returns the path for the Pebble database
func (c *Config) ConnectionString() string {
	return c.Path
}

// ConnectionTimeout returns zero since Pebble doesn't use network connections
func (c *Config) ConnectionTimeout() time.Duration {
	return 0
}

// MaxOpenConnections returns 1 since Pebble doesn't use connection pools
func (c *Config) MaxOpenConnections() int {
	return 1
}

// MaxIdleConnections returns 1 since Pebble doesn't use connection pools
func (c *Config) MaxIdleConnections() int {
	return 1
}

// ConnMaxLifetime returns zero since Pebble doesn't use connection pools
func (c *Config) ConnMaxLifetime() time.Duration {
	return 0
}

// Options returns additional driver-specific options
func (c *Config) Options() map[string]interface{} {
	return c.AdditionalOptions
}

// Driver implements the Pebble key-value store driver.
type Driver struct {
	db     *pebble.DB
	config *Config
	mutex  sync.RWMutex
	closed bool
}

// NewDriver creates a new Pebble driver instance with the provided configuration.
//
// Parameters:
//   - cfg: Database configuration
//
// Returns:
//   - *Driver: A new Pebble driver instance
//   - error: Error if driver creation fails
func NewDriver(cfg *Config) (*Driver, error) {
	if cfg == nil {
		return nil, fmt.Errorf("configuration cannot be nil")
	}

	if cfg.Path == "" {
		return nil, fmt.Errorf("database path cannot be empty")
	}

	opts := &pebble.Options{
		Cache:        pebble.NewCache(cfg.CacheSize),
		MemTableSize: uint64(cfg.WriteBufferSize),
		DisableWAL:   !cfg.Sync,
		ReadOnly:     cfg.ReadOnly,
	}

	db, err := pebble.Open(cfg.Path, opts)
	if err != nil {
		return nil, fmt.Errorf("failed to open Pebble database: %w", err)
	}

	return &Driver{
		db:     db,
		config: cfg,
	}, nil
}

// Driver returns the database driver type
func (d *Driver) Driver() db.DriverType {
	return db.DriverPebble
}

// Execute runs a key-value operation (Set, Delete)
func (d *Driver) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return nil, fmt.Errorf("database connection is closed")
	}

	// Parse the query to determine operation type
	switch query {
	case "SET":
		if len(args) != 2 {
			return nil, fmt.Errorf("SET operation requires exactly 2 arguments (key, value)")
		}
		key, ok := args[0].(string)
		if !ok {
			return nil, fmt.Errorf("key must be a string")
		}

		// Convert value to JSON for storage
		valueBytes, err := json.Marshal(args[1])
		if err != nil {
			return nil, fmt.Errorf("failed to marshal value: %w", err)
		}

		err = d.db.Set([]byte(key), valueBytes, pebble.Sync)
		if err != nil {
			return nil, fmt.Errorf("failed to set key-value: %w", err)
		}

		return &kvResult{affectedRows: 1}, nil

	case "DELETE":
		if len(args) != 1 {
			return nil, fmt.Errorf("DELETE operation requires exactly 1 argument (key)")
		}
		key, ok := args[0].(string)
		if !ok {
			return nil, fmt.Errorf("key must be a string")
		}

		err := d.db.Delete([]byte(key), pebble.Sync)
		if err != nil {
			return nil, fmt.Errorf("failed to delete key: %w", err)
		}

		return &kvResult{affectedRows: 1}, nil

	default:
		return nil, fmt.Errorf("unsupported operation: %s", query)
	}
}

// Query executes a key-value query operation (GET, SCAN)
func (d *Driver) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return nil, fmt.Errorf("database connection is closed")
	}

	switch query {
	case "SCAN":
		// Return an iterator over all keys
		iter, err := d.db.NewIter(nil)
		if err != nil {
			return nil, fmt.Errorf("failed to create iterator: %w", err)
		}
		return &kvRows{iter: iter}, nil

	case "SCAN_PREFIX":
		if len(args) != 1 {
			return nil, fmt.Errorf("SCAN_PREFIX operation requires exactly 1 argument (prefix)")
		}
		prefix, ok := args[0].(string)
		if !ok {
			return nil, fmt.Errorf("prefix must be a string")
		}

		prefixBytes := []byte(prefix)
		iter, err := d.db.NewIter(&pebble.IterOptions{
			LowerBound: prefixBytes,
			UpperBound: prefixUpperBound(prefixBytes),
		})
		if err != nil {
			return nil, fmt.Errorf("failed to create prefix iterator: %w", err)
		}
		return &kvRows{iter: iter}, nil

	default:
		return nil, fmt.Errorf("unsupported query operation: %s", query)
	}
}

// QueryRow executes a single key lookup
func (d *Driver) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return &kvRow{err: fmt.Errorf("database connection is closed")}
	}

	if query != "GET" {
		return &kvRow{err: fmt.Errorf("unsupported row operation: %s", query)}
	}

	if len(args) != 1 {
		return &kvRow{err: fmt.Errorf("GET operation requires exactly 1 argument (key)")}
	}

	key, ok := args[0].(string)
	if !ok {
		return &kvRow{err: fmt.Errorf("key must be a string")}
	}

	value, closer, err := d.db.Get([]byte(key))
	if err != nil {
		if err == pebble.ErrNotFound {
			return &kvRow{err: fmt.Errorf("key not found: %s", key)}
		}
		return &kvRow{err: fmt.Errorf("failed to get key: %w", err)}
	}

	// Make a copy of the value before closing
	valueCopy := make([]byte, len(value))
	copy(valueCopy, value)
	closer.Close()

	return &kvRow{key: key, value: valueCopy}
}

// BeginTx returns an error since Pebble doesn't support transactions in the SQL sense
func (d *Driver) BeginTx(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
	return nil, fmt.Errorf("transactions not supported by Pebble driver")
}

// Begin returns an error since Pebble doesn't support transactions in the SQL sense
func (d *Driver) Begin(ctx context.Context) (db.Transaction, error) {
	return nil, fmt.Errorf("transactions not supported by Pebble driver")
}

// Prepare returns an error since Pebble doesn't support prepared statements
func (d *Driver) Prepare(ctx context.Context, query string) (db.Stmt, error) {
	return nil, fmt.Errorf("prepared statements not supported by Pebble driver")
}

// Stats returns database statistics
func (d *Driver) Stats() db.Stats {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	metrics := d.db.Metrics()
	customStats := map[string]string{
		"level_count":      fmt.Sprintf("%d", len(metrics.Levels)),
		"mem_table_count":  fmt.Sprintf("%d", metrics.MemTable.Count),
		"mem_table_size":   fmt.Sprintf("%d", metrics.MemTable.Size),
		"disk_space_usage": fmt.Sprintf("%d", metrics.DiskSpaceUsage()),
	}

	return db.Stats{
		OpenConnections:    1, // Pebble uses a single connection
		InUse:              1,
		Idle:               0,
		MaxOpenConnections: 1,
		MaxIdleConnections: 1,
		CustomStats:        customStats,
	}
}

// Ping checks if the database is accessible
func (d *Driver) Ping(ctx context.Context) error {
	d.mutex.RLock()
	defer d.mutex.RUnlock()

	if d.closed {
		return fmt.Errorf("database connection is closed")
	}

	// Try a simple operation to verify the database is working
	_, closer, err := d.db.Get([]byte("__ping__"))
	if closer != nil {
		closer.Close()
	}
	if err != nil && err != pebble.ErrNotFound {
		return fmt.Errorf("database ping failed: %w", err)
	}

	return nil
}

// Close closes the database, releasing any open resources
func (d *Driver) Close() error {
	d.mutex.Lock()
	defer d.mutex.Unlock()

	if d.closed {
		return nil
	}

	d.closed = true
	return d.db.Close()
}

// Raw returns the underlying Pebble database instance
func (d *Driver) Raw() interface{} {
	return d.db
}

// GRPCService returns the database as a gRPC service (not implemented for Pebble)
func (d *Driver) GRPCService() db.DatabaseGRPCService {
	return nil // Not implemented for key-value stores
}

// Helper types for Pebble operations

// kvResult implements the db.Result interface for key-value operations
type kvResult struct {
	affectedRows int64
}

func (r *kvResult) LastInsertId() (int64, error) {
	return 0, fmt.Errorf("LastInsertId not supported for key-value operations")
}

func (r *kvResult) RowsAffected() (int64, error) {
	return r.affectedRows, nil
}

// kvRow implements the db.Row interface for single key lookups
type kvRow struct {
	key   string
	value []byte
	err   error
}

func (r *kvRow) Scan(dest ...interface{}) error {
	if r.err != nil {
		return r.err
	}

	if len(dest) == 0 {
		return fmt.Errorf("no destination provided for scan")
	}

	// For key-value stores, we can scan the key and/or value
	if len(dest) == 1 {
		// Scan just the value
		return json.Unmarshal(r.value, dest[0])
	}

	if len(dest) == 2 {
		// Scan key and value
		if keyPtr, ok := dest[0].(*string); ok {
			*keyPtr = r.key
		} else {
			return fmt.Errorf("first destination must be *string for key")
		}
		return json.Unmarshal(r.value, dest[1])
	}

	return fmt.Errorf("too many destinations for key-value scan")
}

func (r *kvRow) Columns() ([]string, error) {
	if r.err != nil {
		return nil, r.err
	}
	return []string{"key", "value"}, nil
}

// kvRows implements the db.Rows interface for key-value iterations
type kvRows struct {
	iter   *pebble.Iterator
	valid  bool
	closed bool
}

func (r *kvRows) Next() bool {
	if r.closed {
		return false
	}

	if !r.valid {
		r.valid = r.iter.First()
	} else {
		r.valid = r.iter.Next()
	}

	return r.valid
}

func (r *kvRows) Scan(dest ...interface{}) error {
	if !r.valid {
		return fmt.Errorf("no current row")
	}

	if len(dest) == 0 {
		return fmt.Errorf("no destination provided for scan")
	}

	key := string(r.iter.Key())
	value := r.iter.Value()

	if len(dest) == 1 {
		// Scan just the value
		return json.Unmarshal(value, dest[0])
	}

	if len(dest) == 2 {
		// Scan key and value
		if keyPtr, ok := dest[0].(*string); ok {
			*keyPtr = key
		} else {
			return fmt.Errorf("first destination must be *string for key")
		}
		return json.Unmarshal(value, dest[1])
	}

	return fmt.Errorf("too many destinations for key-value scan")
}

func (r *kvRows) Close() error {
	if r.closed {
		return nil
	}
	r.closed = true
	return r.iter.Close()
}

func (r *kvRows) Err() error {
	return r.iter.Error()
}

func (r *kvRows) Columns() ([]string, error) {
	return []string{"key", "value"}, nil
}

func (r *kvRows) ColumnTypes() ([]db.ColumnType, error) {
	return []db.ColumnType{
		&kvColumnType{name: "key", typeName: "TEXT"},
		&kvColumnType{name: "value", typeName: "BLOB"},
	}, nil
}

// kvColumnType implements the db.ColumnType interface
type kvColumnType struct {
	name     string
	typeName string
}

func (c *kvColumnType) Name() string {
	return c.name
}

func (c *kvColumnType) DatabaseTypeName() string {
	return c.typeName
}

func (c *kvColumnType) Length() (length int64, ok bool) {
	return 0, false
}

func (c *kvColumnType) DecimalSize() (precision, scale int64, ok bool) {
	return 0, 0, false
}

func (c *kvColumnType) Nullable() (nullable, ok bool) {
	return false, true
}

func (c *kvColumnType) ScanType() reflect.Type {
	if c.name == "key" {
		return reflect.TypeOf("")
	}
	return reflect.TypeOf([]byte{})
}

// Helper function to create upper bound for prefix scanning
func prefixUpperBound(prefix []byte) []byte {
	if len(prefix) == 0 {
		return nil
	}

	// Create a copy and increment the last byte
	upper := make([]byte, len(prefix))
	copy(upper, prefix)

	for i := len(upper) - 1; i >= 0; i-- {
		if upper[i] < 0xff {
			upper[i]++
			return upper[:i+1]
		}
	}

	// All bytes are 0xff, no upper bound
	return nil
}
