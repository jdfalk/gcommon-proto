// file: pkg/db/grpc/server.go
package grpc

import (
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	"github.com/jdfalk/gcommon/pkg/db"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// DatabaseServer implements the DatabaseService gRPC service interface.
// It wraps a db.Database implementation and exposes it via gRPC.
type DatabaseServer struct {
	dbpb.UnimplementedDatabaseServiceServer
	database db.Database
}

// NewDatabaseServer creates a new DatabaseServer instance.
// It wraps the provided database implementation and exposes it as a gRPC service.
//
// Parameters:
//   - database: A db.Database implementation to be exposed via gRPC
//
// Returns:
//   - A new DatabaseServer that implements the DatabaseService gRPC interface
func NewDatabaseServer(database db.Database) *DatabaseServer {
	return &DatabaseServer{
		database: database,
	}
}

// Register registers the DatabaseService with the provided gRPC server.
//
// Parameters:
//   - server: The gRPC server to register the service with
func (s *DatabaseServer) Register(server *grpc.Server) {
	dbpb.RegisterDatabaseServiceServer(server, s)
}

// Execute implements the Execute RPC method.
// It executes a SQL statement that doesn't return rows (like INSERT, UPDATE, DELETE).
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The execution request containing the query and parameters
//
// Returns:
//   - The execution result with rows affected and last insert ID
//   - Error if the execution fails
func (s *DatabaseServer) Execute(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error) {
	// Convert parameters from proto to native types
	params, err := protoValuesToNative(req.Parameters)
	if err != nil {
		return nil, status.Errorf(codes.InvalidArgument, "invalid parameters: %v", err)
	}

	var result db.Result
	var execErr error

	// Check if this is part of a transaction
	if req.TransactionId != "" {
		// Not implemented yet - transaction handling will be added in a separate PR
		return nil, status.Errorf(codes.Unimplemented, "transaction support not yet implemented")
	} else {
		// Execute the query directly on the database
		result, execErr = s.database.Execute(ctx, req.Query, params...)
	}

	if execErr != nil {
		return nil, status.Errorf(codes.Internal, "database execution error: %v", execErr)
	}

	// Get result metadata
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to get rows affected: %v", err)
	}

	lastInsertId, err := result.LastInsertId()
	if err != nil {
		// Some databases don't support last insert ID, so we'll just log and continue
		lastInsertId = 0
	}

	return &dbpb.ExecuteResponse{
		RowsAffected: rowsAffected,
		LastInsertId: lastInsertId,
	}, nil
}

// Query implements the Query RPC method.
// It executes a query and streams the resulting rows back to the client.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The query request containing the SQL query and parameters
//
// Returns:
//   - Error if the query fails
func (s *DatabaseServer) Query(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error {
	ctx := stream.Context()

	// Convert parameters from proto to native types
	params, err := protoValuesToNative(req.Parameters)
	if err != nil {
		return status.Errorf(codes.InvalidArgument, "invalid parameters: %v", err)
	}

	var rows db.Rows
	var queryErr error

	// Check if this is part of a transaction
	if req.TransactionId != "" {
		// Not implemented yet - transaction handling will be added in a separate PR
		return status.Errorf(codes.Unimplemented, "transaction support not yet implemented")
	} else {
		// Execute the query directly on the database
		rows, queryErr = s.database.Query(ctx, req.Query, params...)
	}

	if queryErr != nil {
		return status.Errorf(codes.Internal, "database query error: %v", queryErr)
	}
	defer rows.Close()

	// Get column names
	columns, err := rows.Columns()
	if err != nil {
		return status.Errorf(codes.Internal, "failed to get column names: %v", err)
	}

	// Process rows
	for rows.Next() {
		// Create a slice of interface{} to hold the row values
		values := make([]interface{}, len(columns))
		valuePtrs := make([]interface{}, len(columns))

		// Set up pointers to each element in values
		for i := range values {
			valuePtrs[i] = &values[i]
		}

		// Scan the row into valuePtrs
		if err := rows.Scan(valuePtrs...); err != nil {
			return status.Errorf(codes.Internal, "failed to scan row: %v", err)
		}

		// Convert native values to proto values
		protoValues, err := nativeToProtoValues(values)
		if err != nil {
			return status.Errorf(codes.Internal, "failed to convert values: %v", err)
		}

		// Send the row to the client
		if err := stream.Send(&dbpb.QueryResponse{
			Values:  protoValues,
			Columns: columns,
		}); err != nil {
			return status.Errorf(codes.Internal, "failed to send row: %v", err)
		}
	}

	// Check for errors during iteration
	if err := rows.Err(); err != nil {
		return status.Errorf(codes.Internal, "error during row iteration: %v", err)
	}

	return nil
}

// QueryRow implements the QueryRow RPC method.
// It executes a query expected to return at most one row.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The query request containing the SQL query and parameters
//
// Returns:
//   - The row or an indication that no row was found
//   - Error if the query fails
func (s *DatabaseServer) QueryRow(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
	// Convert parameters from proto to native types
	params, err := protoValuesToNative(req.Parameters)
	if err != nil {
		return nil, status.Errorf(codes.InvalidArgument, "invalid parameters: %v", err)
	}

	var rows db.Rows
	var queryErr error

	// Check if this is part of a transaction
	if req.TransactionId != "" {
		// Not implemented yet - transaction handling will be added in a separate PR
		return nil, status.Errorf(codes.Unimplemented, "transaction support not yet implemented")
	} else {
		// Execute the query directly on the database
		// We'll use Query instead of QueryRow to get column names
		rows, queryErr = s.database.Query(ctx, req.Query, params...)
	}

	if queryErr != nil {
		return nil, status.Errorf(codes.Internal, "database query error: %v", queryErr)
	}
	defer rows.Close()

	// Get column names
	columns, err := rows.Columns()
	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to get column names: %v", err)
	}

	// Check if there's a row
	if !rows.Next() {
		// No row found
		return &dbpb.QueryRowResponse{
			Found:   false,
			Columns: columns,
			Values:  nil,
		}, nil
	}

	// Create a slice of interface{} to hold the row values
	values := make([]interface{}, len(columns))
	valuePtrs := make([]interface{}, len(columns))

	// Set up pointers to each element in values
	for i := range values {
		valuePtrs[i] = &values[i]
	}

	// Scan the row into valuePtrs
	if err := rows.Scan(valuePtrs...); err != nil {
		return nil, status.Errorf(codes.Internal, "failed to scan row: %v", err)
	}

	// Convert native values to proto values
	protoValues, err := nativeToProtoValues(values)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to convert values: %v", err)
	}

	return &dbpb.QueryRowResponse{
		Found:   true,
		Columns: columns,
		Values:  protoValues,
	}, nil
}

// BeginTransaction implements the BeginTransaction RPC method.
// It starts a new database transaction.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The transaction request with isolation level and read-only flag
//
// Returns:
//   - A transaction ID that can be used for subsequent operations
//   - Error if the transaction fails to start
func (s *DatabaseServer) BeginTransaction(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
	// Convert isolation level from proto to native
	var isolation db.IsolationLevel
	switch req.IsolationLevel {
	case dbpb.IsolationLevel_ISOLATION_LEVEL_DEFAULT:
		isolation = db.IsolationLevelDefault
	case dbpb.IsolationLevel_ISOLATION_LEVEL_READ_UNCOMMITTED:
		isolation = db.IsolationLevelReadUncommitted
	case dbpb.IsolationLevel_ISOLATION_LEVEL_READ_COMMITTED:
		isolation = db.IsolationLevelReadCommitted
	case dbpb.IsolationLevel_ISOLATION_LEVEL_REPEATABLE_READ:
		isolation = db.IsolationLevelRepeatableRead
	case dbpb.IsolationLevel_ISOLATION_LEVEL_SERIALIZABLE:
		isolation = db.IsolationLevelSerializable
	default:
		return nil, status.Errorf(codes.InvalidArgument, "invalid isolation level: %v", req.IsolationLevel)
	}

	// Set up transaction options
	opts := &db.TxOptions{
		ReadOnly:  req.ReadOnly,
		Isolation: isolation,
	}

	// Set timeout if specified
	if req.TimeoutMs > 0 {
		opts.Timeout = time.Duration(req.TimeoutMs) * time.Millisecond
	}

	// Begin the transaction
	tx, err := s.database.BeginTx(ctx, opts)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to begin transaction: %v", err)
	}

	// Return the transaction ID
	return &dbpb.TransactionResponse{
		TransactionId: tx.ID(),
		Success:       true,
	}, nil
}

// CommitTransaction implements the CommitTransaction RPC method.
// It commits a transaction identified by the transaction ID.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The transaction request with the transaction ID
//
// Returns:
//   - A response indicating if the commit was successful
//   - Error if the commit fails
func (s *DatabaseServer) CommitTransaction(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
	// Transaction handling will be implemented in a separate PR
	return nil, status.Errorf(codes.Unimplemented, "transaction support not yet implemented")
}

// RollbackTransaction implements the RollbackTransaction RPC method.
// It rolls back a transaction identified by the transaction ID.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The transaction request with the transaction ID
//
// Returns:
//   - A response indicating if the rollback was successful
//   - Error if the rollback fails
func (s *DatabaseServer) RollbackTransaction(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
	// Transaction handling will be implemented in a separate PR
	return nil, status.Errorf(codes.Unimplemented, "transaction support not yet implemented")
}

// Ping implements the Ping RPC method.
// It checks if the database is accessible.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The ping request with optional timeout
//
// Returns:
//   - A response indicating if the ping was successful
//   - Error if the ping fails
func (s *DatabaseServer) Ping(ctx context.Context, req *dbpb.PingRequest) (*dbpb.PingResponse, error) {
	// Apply timeout if specified
	if req.TimeoutMs > 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, time.Duration(req.TimeoutMs)*time.Millisecond)
		defer cancel()
	}

	// Measure ping time
	startTime := time.Now()
	err := s.database.Ping(ctx)
	latency := time.Since(startTime)

	if err != nil {
		return &dbpb.PingResponse{
			Success:      false,
			LatencyMs:    latency.Milliseconds(),
			ErrorMessage: err.Error(),
		}, nil
	}

	return &dbpb.PingResponse{
		Success:   true,
		LatencyMs: latency.Milliseconds(),
	}, nil
}

// GetStats implements the GetStats RPC method.
// It returns database statistics.
//
// Parameters:
//   - ctx: The context for the operation
//   - req: The stats request
//
// Returns:
//   - Database statistics
//   - Error if retrieving stats fails
func (s *DatabaseServer) GetStats(ctx context.Context, req *dbpb.StatsRequest) (*dbpb.StatsResponse, error) {
	stats := s.database.Stats()

	return &dbpb.StatsResponse{
		OpenConnections:    int32(stats.OpenConnections),
		InUse:              int32(stats.InUse),
		Idle:               int32(stats.Idle),
		WaitCount:          stats.WaitCount,
		WaitDurationMs:     stats.WaitDuration.Milliseconds(),
		MaxOpenConnections: int32(stats.MaxOpenConnections),
		MaxIdleConnections: int32(stats.MaxIdleConnections),
		MaxLifetimeMs:      stats.MaxLifetime.Milliseconds(),
		CustomStats:        stats.CustomStats,
	}, nil
}

// protoValuesToNative converts a slice of Protocol Buffer Value messages to native Go values.
//
// Parameters:
//   - protoValues: Slice of Protocol Buffer Value messages
//
// Returns:
//   - Slice of native Go values
//   - Error if conversion fails
func protoValuesToNative(protoValues []*dbpb.Value) ([]interface{}, error) {
	result := make([]interface{}, len(protoValues))

	for i, pv := range protoValues {
		if pv == nil {
			result[i] = nil
			continue
		}

		switch v := pv.Value.(type) {
		case *dbpb.Value_NullValue:
			result[i] = nil
		case *dbpb.Value_StringValue:
			result[i] = v.StringValue
		case *dbpb.Value_Int64Value:
			result[i] = v.Int64Value
		case *dbpb.Value_DoubleValue:
			result[i] = v.DoubleValue
		case *dbpb.Value_BoolValue:
			result[i] = v.BoolValue
		case *dbpb.Value_BytesValue:
			result[i] = v.BytesValue
		case *dbpb.Value_TimestampValue:
			// Parse RFC3339 timestamp
			t, err := time.Parse(time.RFC3339, v.TimestampValue)
			if err != nil {
				return nil, fmt.Errorf("invalid timestamp value: %v", err)
			}
			result[i] = t
		default:
			return nil, fmt.Errorf("unsupported value type: %T", v)
		}
	}

	return result, nil
}

// nativeToProtoValues converts a slice of native Go values to Protocol Buffer Value messages.
//
// Parameters:
//   - nativeValues: Slice of native Go values
//
// Returns:
//   - Slice of Protocol Buffer Value messages
//   - Error if conversion fails
func nativeToProtoValues(nativeValues []interface{}) ([]*dbpb.Value, error) {
	result := make([]*dbpb.Value, len(nativeValues))

	for i, nv := range nativeValues {
		if nv == nil {
			result[i] = &dbpb.Value{Value: &dbpb.Value_NullValue{NullValue: true}}
			continue
		}

		switch v := nv.(type) {
		case string:
			result[i] = &dbpb.Value{Value: &dbpb.Value_StringValue{StringValue: v}}
		case int:
			result[i] = &dbpb.Value{Value: &dbpb.Value_Int64Value{Int64Value: int64(v)}}
		case int32:
			result[i] = &dbpb.Value{Value: &dbpb.Value_Int64Value{Int64Value: int64(v)}}
		case int64:
			result[i] = &dbpb.Value{Value: &dbpb.Value_Int64Value{Int64Value: v}}
		case float32:
			result[i] = &dbpb.Value{Value: &dbpb.Value_DoubleValue{DoubleValue: float64(v)}}
		case float64:
			result[i] = &dbpb.Value{Value: &dbpb.Value_DoubleValue{DoubleValue: v}}
		case bool:
			result[i] = &dbpb.Value{Value: &dbpb.Value_BoolValue{BoolValue: v}}
		case []byte:
			result[i] = &dbpb.Value{Value: &dbpb.Value_BytesValue{BytesValue: v}}
		case time.Time:
			result[i] = &dbpb.Value{Value: &dbpb.Value_TimestampValue{TimestampValue: v.Format(time.RFC3339)}}
		default:
			// Try to convert to string for types we don't directly support
			result[i] = &dbpb.Value{Value: &dbpb.Value_StringValue{StringValue: fmt.Sprintf("%v", v)}}
		}
	}

	return result, nil
}
