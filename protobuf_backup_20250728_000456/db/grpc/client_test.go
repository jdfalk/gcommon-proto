package grpc

import (
	"context"
	"fmt" // Add fmt package for string formatting
	"net"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/test/bufconn"

	"github.com/jdfalk/gcommon/pkg/db"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// Buffer size for testing
const bufSize = 1024 * 1024

// MockDatabaseService implements the DatabaseService gRPC service for testing
type MockDatabaseService struct {
	dbpb.UnimplementedDatabaseServiceServer
	executeFunc             func(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error)
	queryFunc               func(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error
	queryRowFunc            func(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error)
	beginTransactionFunc    func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error)
	commitTransactionFunc   func(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error)
	rollbackTransactionFunc func(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error)
	pingFunc                func(ctx context.Context, req *dbpb.PingRequest) (*dbpb.PingResponse, error)
	getStatsFunc            func(ctx context.Context, req *dbpb.StatsRequest) (*dbpb.StatsResponse, error)
}

// Execute handles execute requests for the mock service
func (m *MockDatabaseService) Execute(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error) {
	if m.executeFunc != nil {
		return m.executeFunc(ctx, req)
	}
	return &dbpb.ExecuteResponse{}, nil
}

// Query handles query requests for the mock service
func (m *MockDatabaseService) Query(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error {
	if m.queryFunc != nil {
		return m.queryFunc(req, stream)
	}
	return nil
}

// QueryRow handles query row requests for the mock service
func (m *MockDatabaseService) QueryRow(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
	if m.queryRowFunc != nil {
		return m.queryRowFunc(ctx, req)
	}
	return &dbpb.QueryRowResponse{Found: false}, nil
}

// BeginTransaction handles transaction start requests for the mock service
func (m *MockDatabaseService) BeginTransaction(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
	if m.beginTransactionFunc != nil {
		return m.beginTransactionFunc(ctx, req)
	}
	return &dbpb.TransactionResponse{TransactionId: "test-tx-id", Success: true}, nil
}

// CommitTransaction handles transaction commit requests for the mock service
func (m *MockDatabaseService) CommitTransaction(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
	if m.commitTransactionFunc != nil {
		return m.commitTransactionFunc(ctx, req)
	}
	return &dbpb.TransactionResponse{Success: true}, nil
}

// RollbackTransaction handles transaction rollback requests for the mock service
func (m *MockDatabaseService) RollbackTransaction(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
	if m.rollbackTransactionFunc != nil {
		return m.rollbackTransactionFunc(ctx, req)
	}
	return &dbpb.TransactionResponse{Success: true}, nil
}

// Ping handles ping requests for the mock service
func (m *MockDatabaseService) Ping(ctx context.Context, req *dbpb.PingRequest) (*dbpb.PingResponse, error) {
	if m.pingFunc != nil {
		return m.pingFunc(ctx, req)
	}
	return &dbpb.PingResponse{Success: true}, nil
}

// GetStats handles stats requests for the mock service
func (m *MockDatabaseService) GetStats(ctx context.Context, req *dbpb.StatsRequest) (*dbpb.StatsResponse, error) {
	if m.getStatsFunc != nil {
		return m.getStatsFunc(ctx, req)
	}
	return &dbpb.StatsResponse{}, nil
}

// setupGRPCClient creates a test gRPC server with the mock service and returns a client connection
//
// Parameters:
//   - mockService: The mock DatabaseService implementation to use
//
// Returns:
//   - gRPC server instance
//   - Client connection to the server
//   - Error if setup fails
func setupGRPCClient(mockService *MockDatabaseService) (*grpc.Server, *grpc.ClientConn, error) {
	// Create a buffer-based network connection for in-memory testing
	lis := bufconn.Listen(bufSize)

	// Create a gRPC server
	server := grpc.NewServer()

	// Register the mock service
	dbpb.RegisterDatabaseServiceServer(server, mockService)

	// Start server
	go func() {
		if err := server.Serve(lis); err != nil {
			panic(err)
		}
	}()

	// Create a custom dialer using the buffer connection
	bufDialer := func(context.Context, string) (net.Conn, error) {
		return lis.Dial()
	}

	// Create client connection
	ctx := context.Background()
	conn, err := grpc.DialContext(
		ctx,
		"bufnet",
		grpc.WithContextDialer(bufDialer),
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)

	return server, conn, err
}

// TestNewClient tests the NewClient constructor
func TestNewClient(t *testing.T) {
	// Create a mock service
	mockService := &MockDatabaseService{}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Test with valid connection
	client, err := NewClient(conn)
	assert.NoError(t, err)
	assert.NotNil(t, client)
	assert.Equal(t, conn, client.conn)
	assert.NotNil(t, client.client)
	assert.NotNil(t, client.transactions)

	// Test with nil connection
	client, err = NewClient(nil)
	assert.Error(t, err)
	assert.Nil(t, client)
	assert.Contains(t, err.Error(), "connection cannot be nil")
}

// TestNewClientWithConfig tests the NewClientWithConfig constructor
func TestNewClientWithConfig(t *testing.T) {
	// Skip connecting to an actual server - just test validation logic

	// Test with nil config
	client, err := NewClientWithConfig(nil)
	assert.Error(t, err)
	assert.Nil(t, client)
	assert.Contains(t, err.Error(), "config cannot be nil")

	// Test with empty target
	client, err = NewClientWithConfig(&ClientConfig{
		Target: "",
	})
	assert.Error(t, err)
	assert.Nil(t, client)
	assert.Contains(t, err.Error(), "target address cannot be empty")
}

// TestClientDriver tests the Driver method
func TestClientDriver(t *testing.T) {
	// Create a mock service
	mockService := &MockDatabaseService{}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Driver method
	driver := client.Driver()
	assert.Equal(t, db.DriverType("grpc"), driver)
}

// TestClientExecute tests the Execute method
func TestClientExecute(t *testing.T) {
	// Create a mock service with Execute implementation
	mockService := &MockDatabaseService{
		executeFunc: func(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error) {
			// Verify request
			assert.Equal(t, "INSERT INTO test VALUES (?)", req.Query)
			assert.Equal(t, 1, len(req.Parameters))
			assert.Equal(t, "test-value", req.Parameters[0].GetStringValue())

			// Return result
			return &dbpb.ExecuteResponse{
				LastInsertId: 42,
				RowsAffected: 1,
			}, nil
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Execute method
	ctx := context.Background()
	result, err := client.Execute(ctx, "INSERT INTO test VALUES (?)", "test-value")
	assert.NoError(t, err)
	assert.NotNil(t, result)

	// Verify result
	lastID, err := result.LastInsertId()
	assert.NoError(t, err)
	assert.Equal(t, int64(42), lastID)

	rowsAffected, err := result.RowsAffected()
	assert.NoError(t, err)
	assert.Equal(t, int64(1), rowsAffected)

	// Test error handling
	mockService.executeFunc = func(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error) {
		return nil, status.Error(codes.InvalidArgument, "invalid query")
	}

	result, err = client.Execute(ctx, "INVALID", "test-value")
	assert.Error(t, err)
	assert.Nil(t, result)
	assert.Contains(t, err.Error(), "invalid argument")
}

// TestClientQuery tests the Query method
func TestClientQuery(t *testing.T) {
	mockService := &MockDatabaseService{
		queryFunc: func(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error {
			// Verify request parameters
			assert.Equal(t, "SELECT * FROM test WHERE id = ?", req.Query)
			assert.Equal(t, 1, len(req.Parameters))
			assert.Equal(t, int64(1), req.Parameters[0].GetInt64Value())

			// First send a response with column information only
			if err := stream.Send(&dbpb.QueryResponse{
				Columns: []string{"id", "name"},
			}); err != nil {
				return err
			}

			// Then send row data with values
			for i := 0; i < 3; i++ {
				if err := stream.Send(&dbpb.QueryResponse{
					Values: []*dbpb.Value{
						{Value: &dbpb.Value_Int64Value{Int64Value: int64(i + 1)}},
						{Value: &dbpb.Value_StringValue{StringValue: fmt.Sprintf("Row %c", 'A'+i)}},
					},
				}); err != nil {
					return err
				}
			}

			// Return nil to complete streaming successfully
			return nil
		},
	}

	// Set up gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Query method
	ctx := context.Background()
	rows, err := client.Query(ctx, "SELECT * FROM test WHERE id = ?", 1)
	require.NoError(t, err)
	require.NotNil(t, rows)
	defer rows.Close()

	// Get columns first
	columns, err := rows.Columns()
	require.NoError(t, err)
	require.Equal(t, []string{"id", "name"}, columns)

	// Read all rows
	var rowData [][]interface{}
	for rows.Next() {
		var id int
		var name string
		err := rows.Scan(&id, &name)
		require.NoError(t, err)
		rowData = append(rowData, []interface{}{id, name})
	}
	require.NoError(t, rows.Err())

	// Verify the correct number of rows and values
	require.Equal(t, 3, len(rowData))
	for i, row := range rowData {
		require.Equal(t, i+1, row[0])
		require.Equal(t, fmt.Sprintf("Row %c", 'A'+i), row[1])
	}
}

// TestClientQueryError tests error handling in the Query method
func TestClientQueryError(t *testing.T) {
	// Create a mock service that returns an error for Query
	mockService := &MockDatabaseService{
		queryFunc: func(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error {
			// Return an error immediately without sending any data
			return status.Error(codes.Internal, "query error")
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Query method with error
	ctx := context.Background()
	rows, err := client.Query(ctx, "SELECT * FROM test", 1)

	// The client.Query should return the error from the server
	require.Error(t, err)
	require.Nil(t, rows)
	require.Contains(t, err.Error(), "database internal error: query error")
}

// TestClientQueryRow tests the QueryRow method
func TestClientQueryRow(t *testing.T) {
	// Create a mock service with QueryRow implementation
	mockService := &MockDatabaseService{
		queryRowFunc: func(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
			// Verify request
			assert.Equal(t, "SELECT * FROM test WHERE id = ?", req.Query)
			assert.Equal(t, 1, len(req.Parameters))
			assert.Equal(t, int64(1), req.Parameters[0].GetInt64Value())

			// Return a row
			return &dbpb.QueryRowResponse{
				Found:   true,
				Columns: []string{"id", "name"},
				Values: []*dbpb.Value{
					{Value: &dbpb.Value_Int64Value{Int64Value: 1}},
					{Value: &dbpb.Value_StringValue{StringValue: "Test Row"}},
				},
			}, nil
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test QueryRow method with result
	ctx := context.Background()
	row := client.QueryRow(ctx, "SELECT * FROM test WHERE id = ?", 1)
	assert.NotNil(t, row)

	// Scan values
	var id int
	var name string
	err = row.Scan(&id, &name)
	assert.NoError(t, err)
	assert.Equal(t, 1, id)
	assert.Equal(t, "Test Row", name)

	// Test QueryRow with no result
	mockService.queryRowFunc = func(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
		return &dbpb.QueryRowResponse{
			Found:   false,
			Columns: []string{"id", "name"},
		}, nil
	}

	row = client.QueryRow(ctx, "SELECT * FROM test WHERE id = ?", 999)
	err = row.Scan(&id, &name)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "no rows in result set")

	// Test error handling
	mockService.queryRowFunc = func(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
		return nil, status.Error(codes.Internal, "query error")
	}

	row = client.QueryRow(ctx, "SELECT * FROM test WHERE id = ?", 1)
	err = row.Scan(&id, &name)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "database internal error")
}

// TestClientBeginTransaction tests the Begin and BeginTx methods
func TestClientBeginTransaction(t *testing.T) {
	// Create a mock service with BeginTransaction implementation
	mockService := &MockDatabaseService{
		beginTransactionFunc: func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
			// Verify request - isolation level, read-only, and timeout
			assert.Equal(t, dbpb.IsolationLevel_ISOLATION_LEVEL_SERIALIZABLE, req.IsolationLevel)
			assert.True(t, req.ReadOnly)
			assert.Equal(t, int64(5000), req.TimeoutMs)

			return &dbpb.TransactionResponse{
				TransactionId: "test-tx-id",
				Success:       true,
			}, nil
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test BeginTx with options
	ctx := context.Background()
	txOpts := &db.TxOptions{
		Isolation: db.IsolationLevelSerializable,
		ReadOnly:  true,
		Timeout:   5 * time.Second,
	}
	tx, err := client.BeginTx(ctx, txOpts)
	assert.NoError(t, err)
	assert.NotNil(t, tx)
	assert.Equal(t, "test-tx-id", tx.ID())

	// Test Begin with default options
	mockService.beginTransactionFunc = func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
		// Default settings
		assert.Equal(t, dbpb.IsolationLevel_ISOLATION_LEVEL_DEFAULT, req.IsolationLevel)
		assert.False(t, req.ReadOnly)
		assert.Equal(t, int64(0), req.TimeoutMs)

		return &dbpb.TransactionResponse{
			TransactionId: "default-tx-id",
			Success:       true,
		}, nil
	}

	tx, err = client.Begin(ctx)
	assert.NoError(t, err)
	assert.NotNil(t, tx)
	assert.Equal(t, "default-tx-id", tx.ID())

	// Test error handling
	mockService.beginTransactionFunc = func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
		return nil, status.Error(codes.Internal, "transaction error")
	}

	tx, err = client.Begin(ctx)
	assert.Error(t, err)
	assert.Nil(t, tx)
	assert.Contains(t, err.Error(), "database internal error")
}

// TestClientTransaction tests transaction operations (Execute, Query, QueryRow, Commit, Rollback)
func TestClientTransaction(t *testing.T) {
	// Create a mock service with transaction operations
	mockService := &MockDatabaseService{
		executeFunc: func(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error) {
			// Normal execution shouldn't have transaction ID
			assert.Empty(t, req.TransactionId)
			return &dbpb.ExecuteResponse{}, nil
		},
		queryFunc: func(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error {
			// Normal query shouldn't have transaction ID
			assert.Empty(t, req.TransactionId)
			return nil
		},
		queryRowFunc: func(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
			// Normal query row shouldn't have transaction ID
			assert.Empty(t, req.TransactionId)
			return &dbpb.QueryRowResponse{Found: false}, nil
		},
		beginTransactionFunc: func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
			return &dbpb.TransactionResponse{
				TransactionId: "tx-id-123",
				Success:       true,
			}, nil
		},
		commitTransactionFunc: func(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
			assert.Equal(t, "tx-id-123", req.TransactionId)
			return &dbpb.TransactionResponse{
				TransactionId: req.TransactionId,
				Success:       true,
			}, nil
		},
		rollbackTransactionFunc: func(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
			assert.Equal(t, "tx-id-456", req.TransactionId)
			return &dbpb.TransactionResponse{
				TransactionId: req.TransactionId,
				Success:       true,
			}, nil
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Begin a transaction
	ctx := context.Background()
	tx, err := client.Begin(ctx)
	assert.NoError(t, err)
	assert.NotNil(t, tx)

	// Test transaction ID
	assert.Equal(t, "tx-id-123", tx.ID())

	// Setup execute in transaction
	mockService.executeFunc = func(ctx context.Context, req *dbpb.ExecuteRequest) (*dbpb.ExecuteResponse, error) {
		assert.Equal(t, "tx-id-123", req.TransactionId)
		assert.Equal(t, "INSERT INTO test VALUES (?)", req.Query)
		return &dbpb.ExecuteResponse{
			LastInsertId: 42,
			RowsAffected: 1,
		}, nil
	}

	// Test Execute in transaction
	result, err := tx.Execute(ctx, "INSERT INTO test VALUES (?)", "test-value")
	assert.NoError(t, err)
	assert.NotNil(t, result)

	lastID, err := result.LastInsertId()
	assert.NoError(t, err)
	assert.Equal(t, int64(42), lastID)

	// Setup query in transaction
	mockService.queryFunc = func(req *dbpb.QueryRequest, stream dbpb.DatabaseService_QueryServer) error {
		assert.Equal(t, "tx-id-123", req.TransactionId)
		assert.Equal(t, "SELECT * FROM test", req.Query)

		// Send a sample row
		err := stream.Send(&dbpb.QueryResponse{
			Columns: []string{"id"},
			Values: []*dbpb.Value{
				{Value: &dbpb.Value_Int64Value{Int64Value: 1}},
			},
		})
		return err
	}

	// Test Query in transaction
	rows, err := tx.Query(ctx, "SELECT * FROM test")
	assert.NoError(t, err)
	assert.NotNil(t, rows)
	defer rows.Close()

	// Setup query row in transaction
	mockService.queryRowFunc = func(ctx context.Context, req *dbpb.QueryRequest) (*dbpb.QueryRowResponse, error) {
		assert.Equal(t, "tx-id-123", req.TransactionId)
		assert.Equal(t, "SELECT * FROM test WHERE id = ?", req.Query)

		return &dbpb.QueryRowResponse{
			Found:   true,
			Columns: []string{"id"},
			Values: []*dbpb.Value{
				{Value: &dbpb.Value_Int64Value{Int64Value: 1}},
			},
		}, nil
	}

	// Test QueryRow in transaction
	row := tx.QueryRow(ctx, "SELECT * FROM test WHERE id = ?", 1)
	assert.NotNil(t, row)

	// Test Commit
	err = tx.Commit()
	assert.NoError(t, err)

	// Create another transaction for rollback test
	mockService.beginTransactionFunc = func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
		return &dbpb.TransactionResponse{
			TransactionId: "tx-id-456",
			Success:       true,
		}, nil
	}

	tx, err = client.Begin(ctx)
	assert.NoError(t, err)
	assert.NotNil(t, tx)

	// Test Rollback
	err = tx.Rollback()
	assert.NoError(t, err)

	// Test error handling for transaction operations
	mockService.commitTransactionFunc = func(ctx context.Context, req *dbpb.TransactionRequest) (*dbpb.TransactionResponse, error) {
		return nil, status.Error(codes.Internal, "commit error")
	}

	// Create new transaction for error testing
	mockService.beginTransactionFunc = func(ctx context.Context, req *dbpb.BeginTransactionRequest) (*dbpb.TransactionResponse, error) {
		return &dbpb.TransactionResponse{
			TransactionId: "tx-id-error",
			Success:       true,
		}, nil
	}

	tx, err = client.Begin(ctx)
	assert.NoError(t, err)

	// Test commit error
	err = tx.Commit()
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "database internal error")
}

// TestClientStats tests the Stats method
func TestClientStats(t *testing.T) {
	// Create a mock service with GetStats implementation
	mockService := &MockDatabaseService{
		getStatsFunc: func(ctx context.Context, req *dbpb.StatsRequest) (*dbpb.StatsResponse, error) {
			return &dbpb.StatsResponse{
				OpenConnections:    10,
				InUse:              5,
				Idle:               5,
				WaitCount:          100,
				WaitDurationMs:     5000,
				MaxOpenConnections: 20,
				MaxIdleConnections: 10,
				MaxLifetimeMs:      3600000,
				CustomStats: map[string]string{
					"test_stat": "test_value",
				},
			}, nil
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Stats method
	stats := client.Stats()
	assert.Equal(t, 10, stats.OpenConnections)
	assert.Equal(t, 5, stats.InUse)
	assert.Equal(t, 5, stats.Idle)
	assert.Equal(t, int64(100), stats.WaitCount)
	assert.Equal(t, time.Duration(5000)*time.Millisecond, stats.WaitDuration)
	assert.Equal(t, 20, stats.MaxOpenConnections)
	assert.Equal(t, 10, stats.MaxIdleConnections)
	assert.Equal(t, time.Duration(3600000)*time.Millisecond, stats.MaxLifetime)
	assert.Equal(t, "test_value", stats.CustomStats["test_stat"])

	// Test error handling - should return empty stats
	mockService.getStatsFunc = func(ctx context.Context, req *dbpb.StatsRequest) (*dbpb.StatsResponse, error) {
		return nil, status.Error(codes.Internal, "stats error")
	}

	stats = client.Stats()
	assert.Equal(t, 0, stats.OpenConnections)
	assert.Equal(t, 0, stats.InUse)
	assert.Equal(t, 0, stats.Idle)
}

// TestClientPing tests the Ping method
func TestClientPing(t *testing.T) {
	// Create a mock service with Ping implementation
	mockService := &MockDatabaseService{
		pingFunc: func(ctx context.Context, req *dbpb.PingRequest) (*dbpb.PingResponse, error) {
			return &dbpb.PingResponse{
				Success: true,
			}, nil
		},
	}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test successful ping
	ctx := context.Background()
	err = client.Ping(ctx)
	assert.NoError(t, err)

	// Test ping error
	mockService.pingFunc = func(ctx context.Context, req *dbpb.PingRequest) (*dbpb.PingResponse, error) {
		return nil, status.Error(codes.Unavailable, "database unavailable")
	}

	err = client.Ping(ctx)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "database unavailable")
}

// TestClientClose tests the Close method
func TestClientClose(t *testing.T) {
	// Create a mock service
	mockService := &MockDatabaseService{}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Close method
	err = client.Close()
	assert.NoError(t, err)

	// Connection should be closed, so operations should fail
	err = conn.Close() // This should fail since conn is already closed
	assert.Error(t, err)
}

// TestClientRaw tests the Raw method
func TestClientRaw(t *testing.T) {
	// Create a mock service
	mockService := &MockDatabaseService{}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test Raw method
	raw := client.Raw()
	assert.NotNil(t, raw)
	assert.Equal(t, client.client, raw)
}

// TestClientGRPCService tests the GRPCService method
func TestClientGRPCService(t *testing.T) {
	// Create a mock service
	mockService := &MockDatabaseService{}

	// Setup gRPC server and client connection
	server, conn, err := setupGRPCClient(mockService)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client, err := NewClient(conn)
	require.NoError(t, err)

	// Test GRPCService method - should return nil for a client
	service := client.GRPCService()
	assert.Nil(t, service)
}
