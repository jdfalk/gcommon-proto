// file: pkg/db/grpc/server_test.go
package grpc

import (
	"context"
	"database/sql"
	"net"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/test/bufconn"

	"github.com/jdfalk/gcommon/pkg/db"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// Buffer size is declared in client_test.go
// const bufSize = 1024 * 1024

// mockDatabase implements the db.Database interface for testing
type mockDatabase struct {
	executeFunc     func(ctx context.Context, query string, args ...interface{}) (db.Result, error)
	queryFunc       func(ctx context.Context, query string, args ...interface{}) (db.Rows, error)
	queryRowFunc    func(ctx context.Context, query string, args ...interface{}) db.Row
	beginFunc       func(ctx context.Context) (db.Transaction, error)
	beginTxFunc     func(ctx context.Context, opts *db.TxOptions) (db.Transaction, error)
	statsFunc       func() db.Stats
	pingFunc        func(ctx context.Context) error
	closeFunc       func() error
	rawFunc         func() interface{}
	grpcServiceFunc func() db.DatabaseGRPCService
}

func (m *mockDatabase) Driver() db.DriverType {
	return db.DriverType("mock")
}

func (m *mockDatabase) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	if m.executeFunc != nil {
		return m.executeFunc(ctx, query, args...)
	}
	return &mockResult{}, nil
}

func (m *mockDatabase) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	if m.queryFunc != nil {
		return m.queryFunc(ctx, query, args...)
	}
	return &mockRows{}, nil
}

func (m *mockDatabase) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	if m.queryRowFunc != nil {
		return m.queryRowFunc(ctx, query, args...)
	}
	return &mockRow{}
}

func (m *mockDatabase) Begin(ctx context.Context) (db.Transaction, error) {
	if m.beginFunc != nil {
		return m.beginFunc(ctx)
	}
	return &mockTransaction{}, nil
}

func (m *mockDatabase) BeginTx(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
	if m.beginTxFunc != nil {
		return m.beginTxFunc(ctx, opts)
	}
	return &mockTransaction{}, nil
}

func (m *mockDatabase) Stats() db.Stats {
	if m.statsFunc != nil {
		return m.statsFunc()
	}
	return db.Stats{}
}

func (m *mockDatabase) Ping(ctx context.Context) error {
	if m.pingFunc != nil {
		return m.pingFunc(ctx)
	}
	return nil
}

func (m *mockDatabase) Close() error {
	if m.closeFunc != nil {
		return m.closeFunc()
	}
	return nil
}

func (m *mockDatabase) Raw() interface{} {
	if m.rawFunc != nil {
		return m.rawFunc()
	}
	return nil
}

func (m *mockDatabase) GRPCService() db.DatabaseGRPCService {
	if m.grpcServiceFunc != nil {
		return m.grpcServiceFunc()
	}
	return nil
}

// mockResult implements the db.Result interface for testing
type mockResult struct {
	lastInsertId int64
	rowsAffected int64
}

func (r *mockResult) LastInsertId() (int64, error) {
	return r.lastInsertId, nil
}

func (r *mockResult) RowsAffected() (int64, error) {
	return r.rowsAffected, nil
}

// mockRow implements the db.Row interface for testing
type mockRow struct {
	values  []interface{}
	columns []string
	err     error
}

func (r *mockRow) Scan(dest ...interface{}) error {
	if r.err != nil {
		return r.err
	}
	return nil
}

func (r *mockRow) Columns() ([]string, error) {
	if r.err != nil {
		return nil, r.err
	}
	return r.columns, nil
}

// mockRows implements the db.Rows interface for testing
type mockRows struct {
	data     [][]interface{}
	columns  []string
	pos      int
	err      error
	closed   bool
	scanFunc func(dest ...interface{}) error
}

func (r *mockRows) Next() bool {
	if r.err != nil || r.closed || r.pos >= len(r.data) {
		return false
	}
	r.pos++
	return true
}

func (r *mockRows) Scan(dest ...interface{}) error {
	if r.scanFunc != nil {
		return r.scanFunc(dest...)
	}
	if r.err != nil {
		return r.err
	}
	if r.closed {
		return sql.ErrNoRows
	}
	if r.pos == 0 || r.pos > len(r.data) {
		return sql.ErrNoRows
	}

	// Get the current row data based on position
	row := r.data[r.pos-1]

	// Copy data from the row to destination arguments
	for i, val := range row {
		if i < len(dest) {
			switch d := dest[i].(type) {
			case *interface{}:
				*d = val
			case *int:
				if v, ok := val.(int); ok {
					*d = v
				}
			case *int64:
				if v, ok := val.(int64); ok {
					*d = v
				} else if v, ok := val.(int); ok {
					*d = int64(v)
				}
			case *string:
				if v, ok := val.(string); ok {
					*d = v
				}
			case *bool:
				if v, ok := val.(bool); ok {
					*d = v
				}
			case *[]byte:
				if v, ok := val.([]byte); ok {
					*d = v
				}
			}
		}
	}

	return nil
}

func (r *mockRows) Close() error {
	r.closed = true
	return nil
}

func (r *mockRows) Err() error {
	return r.err
}

func (r *mockRows) Columns() ([]string, error) {
	if r.err != nil {
		return nil, r.err
	}
	return r.columns, nil
}

func (r *mockRows) ColumnTypes() ([]*sql.ColumnType, error) {
	return nil, nil
}

// mockTransaction implements the db.Transaction interface for testing
type mockTransaction struct {
	id         string
	committed  bool
	rolledBack bool
}

func (t *mockTransaction) Execute(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
	return &mockResult{}, nil
}

func (t *mockTransaction) Query(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
	return &mockRows{}, nil
}

func (t *mockTransaction) QueryRow(ctx context.Context, query string, args ...interface{}) db.Row {
	return &mockRow{}
}

func (t *mockTransaction) Commit() error {
	t.committed = true
	return nil
}

func (t *mockTransaction) Rollback() error {
	t.rolledBack = true
	return nil
}

func (t *mockTransaction) ID() string {
	return t.id
}

// setupGRPCServer creates a test gRPC server and client connection
func setupGRPCServer(database db.Database) (*grpc.Server, *grpc.ClientConn, error) {
	// Create a buffer-based network connection
	lis := bufconn.Listen(bufSize)

	// Create a gRPC server
	server := grpc.NewServer()

	// Register database service
	dbServer := NewDatabaseServer(database)
	dbServer.Register(server)

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

// TestDatabaseServerExecute tests the Execute RPC method
func TestDatabaseServerExecute(t *testing.T) {
	// Create a mock database that returns a predefined result for Execute
	mockDB := &mockDatabase{
		executeFunc: func(ctx context.Context, query string, args ...interface{}) (db.Result, error) {
			// Verify the query and args are passed correctly
			assert.Equal(t, "INSERT INTO test (name) VALUES (?)", query)
			assert.Equal(t, 1, len(args))
			assert.Equal(t, "test value", args[0])

			// Return a mock result
			return &mockResult{
				lastInsertId: 42,
				rowsAffected: 1,
			}, nil
		},
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockDB)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := dbpb.NewDatabaseServiceClient(conn)

	// Test Execute RPC
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Create request with a string parameter
	req := &dbpb.ExecuteRequest{
		Query: "INSERT INTO test (name) VALUES (?)",
		Parameters: []*dbpb.Value{
			{Value: &dbpb.Value_StringValue{StringValue: "test value"}},
		},
	}

	// Call Execute
	resp, err := client.Execute(ctx, req)
	require.NoError(t, err)
	require.NotNil(t, resp)

	// Verify response
	assert.Equal(t, int64(42), resp.LastInsertId)
	assert.Equal(t, int64(1), resp.RowsAffected)
}

// TestDatabaseServerQuery tests the Query RPC method
func TestDatabaseServerQuery(t *testing.T) {
	// Create mock rows with test data
	mockRowsData := [][]interface{}{
		{1, "Row 1"},
		{2, "Row 2"},
		{3, "Row 3"},
	}

	// Create a mock database that returns predefined rows for Query
	mockDB := &mockDatabase{
		queryFunc: func(ctx context.Context, query string, args ...interface{}) (db.Rows, error) {
			// Verify the query and args are passed correctly
			// Setup mock rows
			rows := &mockRows{
				columns: []string{"id", "name"},
				data:    mockRowsData,
				pos:     0,
			}

			// Override the Scan method using scanFunc
			rows.scanFunc = func(dest ...interface{}) error {
				if rows.pos == 0 || rows.pos > len(rows.data) {
					return sql.ErrNoRows
				}

				row := rows.data[rows.pos-1]
				for i, val := range row {
					if i < len(dest) {
						switch d := dest[i].(type) {
						case *interface{}:
							*d = val
						case *int:
							if v, ok := val.(int); ok {
								*d = v
							}
						case *string:
							if v, ok := val.(string); ok {
								*d = v
							}
						}
					}
				}
				return nil
			}

			return rows, nil
		},
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockDB)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := dbpb.NewDatabaseServiceClient(conn)

	// Test Query RPC
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Create request with an int64 parameter
	req := &dbpb.QueryRequest{
		Query: "SELECT id, name FROM test WHERE id > ?",
		Parameters: []*dbpb.Value{
			{Value: &dbpb.Value_Int64Value{Int64Value: 0}},
		},
	}

	// Call Query
	stream, err := client.Query(ctx, req)
	require.NoError(t, err)
	require.NotNil(t, stream)

	// Collect response rows
	var rows []*dbpb.QueryResponse
	for {
		row, err := stream.Recv()
		if err != nil {
			break
		}
		rows = append(rows, row)
	}

	// Verify we received the expected number of rows
	assert.Equal(t, len(mockRowsData), len(rows))

	// Verify column names
	for _, row := range rows {
		assert.Equal(t, []string{"id", "name"}, row.Columns)
	}
}

// TestDatabaseServerPing tests the Ping RPC method
func TestDatabaseServerPing(t *testing.T) {
	// Create a mock database
	mockDB := &mockDatabase{
		pingFunc: func(ctx context.Context) error {
			// Simulate ping delay
			time.Sleep(10 * time.Millisecond)
			return nil
		},
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockDB)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := dbpb.NewDatabaseServiceClient(conn)

	// Test Ping RPC
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Call Ping
	resp, err := client.Ping(ctx, &dbpb.PingRequest{})
	require.NoError(t, err)
	require.NotNil(t, resp)

	// Verify response
	assert.True(t, resp.Success)
	assert.True(t, resp.LatencyMs > 0, "Latency should be greater than 0")
	assert.Empty(t, resp.ErrorMessage)
}

// TestDatabaseServerGetStats tests the GetStats RPC method
func TestDatabaseServerGetStats(t *testing.T) {
	// Create a mock database
	mockDB := &mockDatabase{
		statsFunc: func() db.Stats {
			return db.Stats{
				OpenConnections:    10,
				InUse:              5,
				Idle:               5,
				WaitCount:          100,
				WaitDuration:       1 * time.Second,
				MaxOpenConnections: 20,
				MaxIdleConnections: 10,
				MaxLifetime:        10 * time.Minute,
				CustomStats: map[string]string{
					"test_stat": "test_value",
				},
			}
		},
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockDB)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := dbpb.NewDatabaseServiceClient(conn)

	// Test GetStats RPC
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Call GetStats
	resp, err := client.GetStats(ctx, &dbpb.StatsRequest{})
	require.NoError(t, err)
	require.NotNil(t, resp)

	// Verify response
	assert.Equal(t, int32(10), resp.OpenConnections)
	assert.Equal(t, int32(5), resp.InUse)
	assert.Equal(t, int32(5), resp.Idle)
	assert.Equal(t, int64(100), resp.WaitCount)
	assert.Equal(t, int64(1000), resp.WaitDurationMs)
	assert.Equal(t, int32(20), resp.MaxOpenConnections)
	assert.Equal(t, int32(10), resp.MaxIdleConnections)
	assert.Equal(t, int64(600000), resp.MaxLifetimeMs)
	assert.Equal(t, "test_value", resp.CustomStats["test_stat"])
}

// TestDatabaseServerBeginTransaction tests the BeginTransaction RPC method
func TestDatabaseServerBeginTransaction(t *testing.T) {
	// Create a mock database
	mockDB := &mockDatabase{
		beginTxFunc: func(ctx context.Context, opts *db.TxOptions) (db.Transaction, error) {
			// Verify transaction options
			require.NotNil(t, opts)
			assert.True(t, opts.ReadOnly)
			assert.Equal(t, db.IsolationLevelSerializable, opts.Isolation)

			// Return a mock transaction with a test ID
			return &mockTransaction{id: "test-transaction-id"}, nil
		},
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockDB)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := dbpb.NewDatabaseServiceClient(conn)

	// Test BeginTransaction RPC
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Call BeginTransaction with options
	resp, err := client.BeginTransaction(ctx, &dbpb.BeginTransactionRequest{
		ReadOnly:       true,
		IsolationLevel: dbpb.IsolationLevel_ISOLATION_LEVEL_SERIALIZABLE,
		TimeoutMs:      5000,
	})
	require.NoError(t, err)
	require.NotNil(t, resp)

	// Verify response
	assert.True(t, resp.Success)
	assert.Equal(t, "test-transaction-id", resp.TransactionId)
	assert.Empty(t, resp.ErrorMessage)
}
