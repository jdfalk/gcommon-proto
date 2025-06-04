// file: pkg/db/grpc/client.go
package grpc

import (
	"context"
	"database/sql"
	"fmt"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	"github.com/jdfalk/gcommon/pkg/db"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// Client implements the db.Database interface using a gRPC client.
// It forwards database operations to a remote database service via gRPC.
type Client struct {
	conn   *grpc.ClientConn
	client dbpb.DatabaseServiceClient
	// Active transactions keyed by transaction ID
	transactions map[string]*Transaction
}

// ClientConfig defines the configuration for a database gRPC client.
type ClientConfig struct {
	// Target is the address of the gRPC server in the format "host:port"
	Target string

	// Timeout is the default timeout for operations
	Timeout time.Duration

	// DialOptions contains additional gRPC dial options
	DialOptions []grpc.DialOption
}

// NewClient creates a new database gRPC client.
//
// Parameters:
//   - conn: An existing gRPC client connection
//
// Returns:
//   - A database client implementing the db.Database interface
//   - Error if client creation fails
func NewClient(conn *grpc.ClientConn) (*Client, error) {
	if conn == nil {
		return nil, fmt.Errorf("connection cannot be nil")
	}

	client := dbpb.NewDatabaseServiceClient(conn)
	return &Client{
		conn:         conn,
		client:       client,
		transactions: make(map[string]*Transaction),
	}, nil
}

// NewClientWithConfig creates a new database gRPC client with the provided configuration.
//
// Parameters:
//   - config: Client configuration including target address and dial options
//
// Returns:
//   - A database client implementing the db.Database interface
//   - Error if client creation fails
func NewClientWithConfig(config *ClientConfig) (*Client, error) {
	if config == nil {
		return nil, fmt.Errorf("config cannot be nil")
	}

	if config.Target == "" {
		return nil, fmt.Errorf("target address cannot be empty")
	}

	// Set default timeout if not provided
	if config.Timeout == 0 {
		config.Timeout = 10 * time.Second
	}

	// Create a connection to the gRPC server
	conn, err := grpc.Dial(config.Target, config.DialOptions...)
	if err != nil {
		return nil, fmt.Errorf("failed to dial gRPC server: %w", err)
	}

	// Create a client using the connection
	return NewClient(conn)
}

// Driver returns the database driver type.
func (c *Client) Driver() db.DriverType {
	// This is a gRPC client, so the actual driver is on the server side
	return db.DriverType("grpc")
}

// Execute runs a query without returning any rows.
//
// Parameters:
//   - ctx: The context for the operation
//   - query: The SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - The result of the execution
//   - Error if the execution fails
func (c *Client) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	// Convert Go values to proto values
	protoArgs, err := argsToProtoValues(args)
	if err != nil {
		return nil, fmt.Errorf("failed to convert arguments: %w", err)
	}

	// Create the execute request
	req := &dbpb.ExecuteRequest{
		Query:      query,
		Parameters: protoArgs,
	}

	// Execute the query via gRPC
	resp, err := c.client.Execute(ctx, req)
	if err != nil {
		return nil, convertGRPCError(err)
	}

	// Return a result object that wraps the response
	return &ExecuteResult{
		rowsAffected: resp.RowsAffected,
		lastInsertId: resp.LastInsertId,
	}, nil
}

// Query executes a query that returns rows.
//
// Parameters:
//   - ctx: The context for the operation
//   - query: The SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - The result rows
//   - Error if the query fails
func (c *Client) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	// Convert Go values to proto values
	protoArgs, err := argsToProtoValues(args)
	if err != nil {
		return nil, fmt.Errorf("failed to convert arguments: %w", err)
	}

	// Create the query request
	req := &dbpb.QueryRequest{
		Query:      query,
		Parameters: protoArgs,
	}

	// Execute the query via gRPC
	stream, err := c.client.Query(ctx, req)
	if err != nil {
		return nil, convertGRPCError(err)
	}

	// Return a rows object that wraps the stream
	return &Rows{
		stream:  stream,
		current: nil,
		columns: nil,
		err:     nil,
	}, nil
}

// QueryRow executes a query that is expected to return at most one row.
//
// Parameters:
//   - ctx: The context for the operation
//   - query: The SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - The result row
func (c *Client) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	// Convert Go values to proto values
	protoArgs, err := argsToProtoValues(args)
	if err != nil {
		return &Row{err: fmt.Errorf("failed to convert arguments: %w", err)}
	}

	// Create the query request
	req := &dbpb.QueryRequest{
		Query:      query,
		Parameters: protoArgs,
	}

	// Execute the query via gRPC
	resp, err := c.client.QueryRow(ctx, req)
	if err != nil {
		return &Row{err: convertGRPCError(err)}
	}

	// If no row was found, return a row with no values
	if !resp.Found {
		return &Row{err: nil, found: false, columns: resp.Columns, values: nil}
	}

	// Return a row object that wraps the response
	return &Row{
		err:     nil,
		found:   true,
		columns: resp.Columns,
		values:  resp.Values,
	}
}

// Begin starts a transaction with default options.
//
// Parameters:
//   - ctx: The context for the operation
//
// Returns:
//   - A transaction
//   - Error if beginning the transaction fails
func (c *Client) Begin(ctx context.Context) (db.Transaction, error) {
	return c.BeginTx(ctx, nil)
}

// BeginTx starts a transaction with specified options.
//
// Parameters:
//   - ctx: The context for the operation
//   - opts: Transaction options
//
// Returns:
//   - A transaction
//   - Error if beginning the transaction fails
func (c *Client) BeginTx(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
	var isolationLevel dbpb.IsolationLevel
	var readOnly bool
	var timeoutMs int64

	// Set options if provided
	if opts != nil {
		// Convert isolation level
		switch opts.Isolation {
		case db.IsolationLevelDefault:
			isolationLevel = dbpb.IsolationLevel_ISOLATION_LEVEL_DEFAULT
		case db.IsolationLevelReadUncommitted:
			isolationLevel = dbpb.IsolationLevel_ISOLATION_LEVEL_READ_UNCOMMITTED
		case db.IsolationLevelReadCommitted:
			isolationLevel = dbpb.IsolationLevel_ISOLATION_LEVEL_READ_COMMITTED
		case db.IsolationLevelRepeatableRead:
			isolationLevel = dbpb.IsolationLevel_ISOLATION_LEVEL_REPEATABLE_READ
		case db.IsolationLevelSerializable:
			isolationLevel = dbpb.IsolationLevel_ISOLATION_LEVEL_SERIALIZABLE
		}

		readOnly = opts.ReadOnly
		if opts.Timeout > 0 {
			timeoutMs = opts.Timeout.Milliseconds()
		}
	}

	// Create begin transaction request
	req := &dbpb.BeginTransactionRequest{
		IsolationLevel: isolationLevel,
		ReadOnly:       readOnly,
		TimeoutMs:      timeoutMs,
	}

	// Begin the transaction via gRPC
	resp, err := c.client.BeginTransaction(ctx, req)
	if err != nil {
		return nil, convertGRPCError(err)
	}

	// Create a transaction object
	tx := &Transaction{
		client:        c.client,
		transactionId: resp.TransactionId,
		committed:     false,
		rolledBack:    false,
	}

	// Store the transaction
	c.transactions[resp.TransactionId] = tx

	return tx, nil
}

// Stats returns database statistics.
//
// Returns:
//   - Database statistics
func (c *Client) Stats() db.Stats {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Get stats via gRPC
	resp, err := c.client.GetStats(ctx, &dbpb.StatsRequest{})
	if err != nil {
		// Return empty stats on error
		return db.Stats{}
	}

	// Convert proto stats to db.Stats
	return db.Stats{
		OpenConnections:    int(resp.OpenConnections),
		InUse:              int(resp.InUse),
		Idle:               int(resp.Idle),
		WaitCount:          resp.WaitCount,
		WaitDuration:       time.Duration(resp.WaitDurationMs) * time.Millisecond,
		MaxOpenConnections: int(resp.MaxOpenConnections),
		MaxIdleConnections: int(resp.MaxIdleConnections),
		MaxLifetime:        time.Duration(resp.MaxLifetimeMs) * time.Millisecond,
		CustomStats:        resp.CustomStats,
	}
}

// Ping checks if the database is accessible.
//
// Parameters:
//   - ctx: The context for the operation
//
// Returns:
//   - Error if the ping fails
func (c *Client) Ping(ctx context.Context) error {
	// Create ping request
	req := &dbpb.PingRequest{
		TimeoutMs: 0, // Use context timeout
	}

	// Ping via gRPC
	resp, err := c.client.Ping(ctx, req)
	if err != nil {
		return convertGRPCError(err)
	}

	// Check if ping was successful
	if !resp.Success {
		return fmt.Errorf("ping failed: %s", resp.ErrorMessage)
	}

	return nil
}

// Close closes the database, releasing any open resources.
//
// Returns:
//   - Error if closing fails
func (c *Client) Close() error {
	return c.conn.Close()
}

// Raw returns the underlying database driver implementation.
//
// Returns:
//   - The underlying gRPC client
func (c *Client) Raw() interface{} {
	return c.client
}

// GRPCService returns the database as a gRPC service.
// For a client, this always returns nil.
//
// Returns:
//   - Always nil for a client
func (c *Client) GRPCService() db.DatabaseGRPCService {
	return nil
}

// ExecuteResult implements the db.Result interface.
type ExecuteResult struct {
	rowsAffected int64
	lastInsertId int64
}

// LastInsertId returns the ID of the last inserted row.
//
// Returns:
//   - Last insert ID
//   - Error if retrieving the ID fails
func (r *ExecuteResult) LastInsertId() (int64, error) {
	return r.lastInsertId, nil
}

// RowsAffected returns the number of rows affected by the operation.
//
// Returns:
//   - Number of rows affected
//   - Error if retrieving the count fails
func (r *ExecuteResult) RowsAffected() (int64, error) {
	return r.rowsAffected, nil
}

// Rows implements the db.Rows interface using a gRPC stream.
type Rows struct {
	stream  dbpb.DatabaseService_QueryClient
	current *dbpb.QueryResponse
	columns []string
	err     error
}

// Next prepares the next row for reading with Scan.
// It returns false when there are no more rows or an error occurred.
//
// Returns:
//   - true if there is a next row, false otherwise
func (r *Rows) Next() bool {
	// Return false if there was a previous error
	if r.err != nil {
		return false
	}

	// Receive the next row from the stream
	resp, err := r.stream.Recv()
	if err != nil {
		if err != context.Canceled && err != context.DeadlineExceeded {
			r.err = convertGRPCError(err)
		} else {
			r.err = err
		}
		return false
	}

	// Store the current row and column names
	r.current = resp

	// If we received column names, store them
	if len(resp.Columns) > 0 {
		r.columns = resp.Columns
	}

	// If this is just a column info message with no values, fetch the next row
	if resp.Values == nil || len(resp.Values) == 0 {
		return r.Next()
	}

	return true
}

// Scan copies the columns from the current row into the provided variables.
//
// Parameters:
//   - dest: Destination variables to scan into
//
// Returns:
//   - Error if scanning fails
func (r *Rows) Scan(dest ...interface{}) error {
	if r.current == nil {
		return fmt.Errorf("no row to scan")
	}

	if len(dest) != len(r.current.Values) {
		return fmt.Errorf("expected %d destination arguments in Scan, got %d", len(r.current.Values), len(dest))
	}

	// Convert proto values to native values and assign to dest
	for i, val := range r.current.Values {
		if val == nil {
			dest[i] = nil
			continue
		}

		nativeVal, err := protoValueToNative(val)
		if err != nil {
			return fmt.Errorf("failed to convert column %d: %w", i, err)
		}

		// Convert the native type to the expected type
		if err := assignValue(dest[i], nativeVal); err != nil {
			return fmt.Errorf("failed to assign column %d: %w", i, err)
		}
	}

	return nil
}

// Close closes the rows, releasing any resources.
//
// Returns:
//   - Error if closing fails
func (r *Rows) Close() error {
	// For gRPC streams, we don't need to explicitly close,
	// but we should cancel the stream context if possible
	return nil
}

// Err returns any error encountered during iteration.
//
// Returns:
//   - Error encountered during iteration
func (r *Rows) Err() error {
	return r.err
}

// Columns returns the column names.
//
// Returns:
//   - Column names
//   - Error if retrieving column names fails
func (r *Rows) Columns() ([]string, error) {
	if r.columns == nil {
		// Attempt to fetch the first row to populate columns
		if !r.Next() {
			if r.err != nil {
				return nil, r.err
			}
			return nil, fmt.Errorf("no columns available")
		}
	}
	return r.columns, nil
}

// ColumnTypes returns column type information.
// This is not supported with gRPC, as detailed type information is lost.
//
// Returns:
//   - nil column types
//   - Error indicating the operation is not supported
func (r *Rows) ColumnTypes() ([]*sql.ColumnType, error) {
	return nil, fmt.Errorf("column types not supported with gRPC client")
}

// Row implements the db.Row interface.
type Row struct {
	err     error
	found   bool
	columns []string
	values  []*dbpb.Value
}

// Scan copies the columns from the row into the provided variables.
//
// Parameters:
//   - dest: Destination variables to scan into
//
// Returns:
//   - Error if scanning fails
func (r *Row) Scan(dest ...interface{}) error {
	if r.err != nil {
		return r.err
	}

	if !r.found {
		return fmt.Errorf("no rows in result set")
	}

	if len(dest) != len(r.values) {
		return fmt.Errorf("expected %d destination arguments in Scan, got %d", len(r.values), len(dest))
	}

	// Convert proto values to native values and assign to dest
	for i, val := range r.values {
		if val == nil {
			dest[i] = nil
			continue
		}

		nativeVal, err := protoValueToNative(val)
		if err != nil {
			return fmt.Errorf("failed to convert column %d: %w", i, err)
		}

		// Convert the native type to the expected type
		if err := assignValue(dest[i], nativeVal); err != nil {
			return fmt.Errorf("failed to assign column %d: %w", i, err)
		}
	}

	return nil
}

// Columns returns the column names.
//
// Returns:
//   - Column names
//   - Error if retrieving column names fails
func (r *Row) Columns() ([]string, error) {
	if r.err != nil {
		return nil, r.err
	}

	if !r.found {
		return nil, fmt.Errorf("no rows in result set")
	}

	return r.columns, nil
}

// Transaction implements the db.Transaction interface.
type Transaction struct {
	client        dbpb.DatabaseServiceClient
	transactionId string
	committed     bool
	rolledBack    bool
}

// Execute runs a query without returning any rows within the transaction.
//
// Parameters:
//   - ctx: The context for the operation
//   - query: The SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - The result of the execution
//   - Error if the execution fails
func (t *Transaction) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	if t.committed || t.rolledBack {
		return nil, fmt.Errorf("transaction has already been committed or rolled back")
	}

	// Convert Go values to proto values
	protoArgs, err := argsToProtoValues(args)
	if err != nil {
		return nil, fmt.Errorf("failed to convert arguments: %w", err)
	}

	// Create the execute request with transaction ID
	req := &dbpb.ExecuteRequest{
		Query:         query,
		Parameters:    protoArgs,
		TransactionId: t.transactionId,
	}

	// Execute the query via gRPC
	resp, err := t.client.Execute(ctx, req)
	if err != nil {
		return nil, convertGRPCError(err)
	}

	// Return a result object that wraps the response
	return &ExecuteResult{
		rowsAffected: resp.RowsAffected,
		lastInsertId: resp.LastInsertId,
	}, nil
}

// Query executes a query that returns rows within the transaction.
//
// Parameters:
//   - ctx: The context for the operation
//   - query: The SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - The result rows
//   - Error if the query fails
func (t *Transaction) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	if t.committed || t.rolledBack {
		return nil, fmt.Errorf("transaction has already been committed or rolled back")
	}

	// Convert Go values to proto values
	protoArgs, err := argsToProtoValues(args)
	if err != nil {
		return nil, fmt.Errorf("failed to convert arguments: %w", err)
	}

	// Create the query request with transaction ID
	req := &dbpb.QueryRequest{
		Query:         query,
		Parameters:    protoArgs,
		TransactionId: t.transactionId,
	}

	// Execute the query via gRPC
	stream, err := t.client.Query(ctx, req)
	if err != nil {
		return nil, convertGRPCError(err)
	}

	// Return a rows object that wraps the stream
	return &Rows{
		stream:  stream,
		current: nil,
		columns: nil,
		err:     nil,
	}, nil
}

// QueryRow executes a query that is expected to return at most one row within the transaction.
//
// Parameters:
//   - ctx: The context for the operation
//   - query: The SQL query to execute
//   - args: Query parameters
//
// Returns:
//   - The result row
func (t *Transaction) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	if t.committed || t.rolledBack {
		return &Row{err: fmt.Errorf("transaction has already been committed or rolled back")}
	}

	// Convert Go values to proto values
	protoArgs, err := argsToProtoValues(args)
	if err != nil {
		return &Row{err: fmt.Errorf("failed to convert arguments: %w", err)}
	}

	// Create the query request with transaction ID
	req := &dbpb.QueryRequest{
		Query:         query,
		Parameters:    protoArgs,
		TransactionId: t.transactionId,
	}

	// Execute the query via gRPC
	resp, err := t.client.QueryRow(ctx, req)
	if err != nil {
		return &Row{err: convertGRPCError(err)}
	}

	// If no row was found, return a row with no values
	if !resp.Found {
		return &Row{err: nil, found: false, columns: resp.Columns, values: nil}
	}

	// Return a row object that wraps the response
	return &Row{
		err:     nil,
		found:   true,
		columns: resp.Columns,
		values:  resp.Values,
	}
}

// Commit commits the transaction.
//
// Returns:
//   - Error if the commit fails
func (t *Transaction) Commit() error {
	if t.committed || t.rolledBack {
		return fmt.Errorf("transaction has already been committed or rolled back")
	}

	// Create commit request
	req := &dbpb.TransactionRequest{
		TransactionId: t.transactionId,
	}

	// Use a short timeout for commit
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	// Commit the transaction via gRPC
	resp, err := t.client.CommitTransaction(ctx, req)
	if err != nil {
		return convertGRPCError(err)
	}

	// Check if commit was successful
	if !resp.Success {
		return fmt.Errorf("commit failed: %s", resp.ErrorMessage)
	}

	t.committed = true
	return nil
}

// Rollback aborts the transaction.
//
// Returns:
//   - Error if the rollback fails
func (t *Transaction) Rollback() error {
	if t.committed || t.rolledBack {
		return fmt.Errorf("transaction has already been committed or rolled back")
	}

	// Create rollback request
	req := &dbpb.TransactionRequest{
		TransactionId: t.transactionId,
	}

	// Use a short timeout for rollback
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	// Rollback the transaction via gRPC
	resp, err := t.client.RollbackTransaction(ctx, req)
	if err != nil {
		return convertGRPCError(err)
	}

	// Check if rollback was successful
	if !resp.Success {
		return fmt.Errorf("rollback failed: %s", resp.ErrorMessage)
	}

	t.rolledBack = true
	return nil
}

// ID returns a unique identifier for the transaction.
//
// Returns:
//   - The transaction ID
func (t *Transaction) ID() string {
	return t.transactionId
}

// argsToProtoValues converts a slice of Go values to Protocol Buffer Value messages.
//
// Parameters:
//   - args: Slice of Go values
//
// Returns:
//   - Slice of Protocol Buffer Value messages
//   - Error if conversion fails
func argsToProtoValues(args []interface{}) ([]*dbpb.Value, error) {
	protoValues := make([]*dbpb.Value, len(args))

	for i, arg := range args {
		switch v := arg.(type) {
		case nil:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_NullValue{NullValue: true}}
		case string:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_StringValue{StringValue: v}}
		case int:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_Int64Value{Int64Value: int64(v)}}
		case int32:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_Int64Value{Int64Value: int64(v)}}
		case int64:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_Int64Value{Int64Value: v}}
		case float32:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_DoubleValue{DoubleValue: float64(v)}}
		case float64:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_DoubleValue{DoubleValue: v}}
		case bool:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_BoolValue{BoolValue: v}}
		case []byte:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_BytesValue{BytesValue: v}}
		case time.Time:
			protoValues[i] = &dbpb.Value{Value: &dbpb.Value_TimestampValue{TimestampValue: v.Format(time.RFC3339)}}
		default:
			return nil, fmt.Errorf("unsupported argument type for arg %d: %T", i, arg)
		}
	}

	return protoValues, nil
}

// protoValueToNative converts a Protocol Buffer Value message to a native Go value.
//
// Parameters:
//   - protoValue: Protocol Buffer Value message
//
// Returns:
//   - Native Go value
//   - Error if conversion fails
func protoValueToNative(protoValue *dbpb.Value) (interface{}, error) {
	if protoValue == nil {
		return nil, nil
	}

	switch v := protoValue.Value.(type) {
	case *dbpb.Value_NullValue:
		return nil, nil
	case *dbpb.Value_StringValue:
		return v.StringValue, nil
	case *dbpb.Value_Int64Value:
		return v.Int64Value, nil
	case *dbpb.Value_DoubleValue:
		return v.DoubleValue, nil
	case *dbpb.Value_BoolValue:
		return v.BoolValue, nil
	case *dbpb.Value_BytesValue:
		return v.BytesValue, nil
	case *dbpb.Value_TimestampValue:
		// Parse RFC3339 timestamp
		t, err := time.Parse(time.RFC3339, v.TimestampValue)
		if err != nil {
			return nil, fmt.Errorf("invalid timestamp value: %w", err)
		}
		return t, nil
	default:
		return nil, fmt.Errorf("unsupported value type: %T", v)
	}
}

// assignValue assigns a native value to a destination pointer.
//
// Parameters:
//   - dest: Destination pointer
//   - src: Source value
//
// Returns:
//   - Error if assignment fails
func assignValue(dest interface{}, src interface{}) error {
	if src == nil {
		// Handle nil specially
		switch d := dest.(type) {
		case *interface{}:
			*d = nil
			return nil
		case *string:
			*d = ""
			return nil
		case *int:
			*d = 0
			return nil
		case *int64:
			*d = 0
			return nil
		case *float64:
			*d = 0
			return nil
		case *bool:
			*d = false
			return nil
		case *[]byte:
			*d = nil
			return nil
		case *time.Time:
			*d = time.Time{}
			return nil
		default:
			return fmt.Errorf("unsupported destination type for nil value: %T", dest)
		}
	}

	// Handle non-nil values
	switch d := dest.(type) {
	case *interface{}:
		*d = src
		return nil
	case *string:
		if s, ok := src.(string); ok {
			*d = s
			return nil
		}
	case *int:
		switch s := src.(type) {
		case int64:
			*d = int(s)
			return nil
		case int:
			*d = s
			return nil
		}
	case *int64:
		if s, ok := src.(int64); ok {
			*d = s
			return nil
		}
	case *float64:
		switch s := src.(type) {
		case float64:
			*d = s
			return nil
		case int64:
			*d = float64(s)
			return nil
		}
	case *bool:
		if s, ok := src.(bool); ok {
			*d = s
			return nil
		}
	case *[]byte:
		if s, ok := src.([]byte); ok {
			*d = s
			return nil
		}
	case *time.Time:
		if s, ok := src.(time.Time); ok {
			*d = s
			return nil
		}
	}

	return fmt.Errorf("cannot assign %T to %T", src, dest)
}

// convertGRPCError converts a gRPC error to a more meaningful database error.
//
// Parameters:
//   - err: gRPC error
//
// Returns:
//   - Converted error
func convertGRPCError(err error) error {
	if err == nil {
		return nil
	}

	// Get the gRPC status
	s, ok := status.FromError(err)
	if !ok {
		return err
	}

	// Convert based on status code
	switch s.Code() {
	case codes.NotFound:
		return fmt.Errorf("database resource not found: %s", s.Message())
	case codes.AlreadyExists:
		return fmt.Errorf("database resource already exists: %s", s.Message())
	case codes.InvalidArgument:
		return fmt.Errorf("invalid argument: %s", s.Message())
	case codes.Aborted:
		return fmt.Errorf("transaction aborted: %s", s.Message())
	case codes.DeadlineExceeded:
		return fmt.Errorf("database operation timed out: %s", s.Message())
	case codes.Internal:
		return fmt.Errorf("database internal error: %s", s.Message())
	case codes.Unavailable:
		return fmt.Errorf("database service unavailable: %s", s.Message())
	default:
		return fmt.Errorf("database error: %s", s.Message())
	}
}
