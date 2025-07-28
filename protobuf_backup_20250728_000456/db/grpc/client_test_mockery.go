// file: pkg/db/grpc/client_test_mockery.go
package grpc

import (
	"context"
	"errors"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
	"github.com/stretchr/testify/require"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	"github.com/jdfalk/gcommon/pkg/db"
	dbmock "github.com/jdfalk/gcommon/pkg/db/mock"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// streamMock is a test helper for mocking gRPC streams
type streamMock struct {
	mock.Mock
	responses []*dbpb.QueryResponse
	index     int
}

// Recv implements the Recv method for the gRPC stream interface
func (s *streamMock) Recv() (*dbpb.QueryResponse, error) {
	if s.index >= len(s.responses) {
		return nil, errors.New("EOF")
	}
	response := s.responses[s.index]
	s.index++
	return response, nil
}

// Header implements the Header method for the gRPC stream interface
func (s *streamMock) Header() (grpc.Header, error) {
	args := s.Called()
	return args.Get(0).(grpc.Header), args.Error(1)
}

// Trailer implements the Trailer method for the gRPC stream interface
func (s *streamMock) Trailer() grpc.Trailer {
	args := s.Called()
	return args.Get(0).(grpc.Trailer)
}

// CloseSend implements the CloseSend method for the gRPC stream interface
func (s *streamMock) CloseSend() error {
	args := s.Called()
	return args.Error(0)
}

// Context implements the Context method for the gRPC stream interface
func (s *streamMock) Context() context.Context {
	args := s.Called()
	return args.Get(0).(context.Context)
}

// SendMsg implements the SendMsg method for the gRPC stream interface
func (s *streamMock) SendMsg(m interface{}) error {
	args := s.Called(m)
	return args.Error(0)
}

// RecvMsg implements the RecvMsg method for the gRPC stream interface
func (s *streamMock) RecvMsg(m interface{}) error {
	args := s.Called(m)
	return args.Error(0)
}

// TestClientQueryWithMockery demonstrates how to use the mockery-generated mocks
// to test the Query method with proper stream simulation
func TestClientQueryWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the responses for the query stream
	responses := []*dbpb.QueryResponse{
		// First response with column information
		{
			Columns: []string{"id", "name"},
		},
		// Row 1
		{
			Values: []*dbpb.Value{
				{Value: &dbpb.Value_Int64Value{Int64Value: 1}},
				{Value: &dbpb.Value_StringValue{StringValue: "Row A"}},
			},
		},
		// Row 2
		{
			Values: []*dbpb.Value{
				{Value: &dbpb.Value_Int64Value{Int64Value: 2}},
				{Value: &dbpb.Value_StringValue{StringValue: "Row B"}},
			},
		},
		// Row 3
		{
			Values: []*dbpb.Value{
				{Value: &dbpb.Value_Int64Value{Int64Value: 3}},
				{Value: &dbpb.Value_StringValue{StringValue: "Row C"}},
			},
		},
	}

	// Create a mock stream with our prepared responses
	stream := &streamMock{
		responses: responses,
	}

	// Set expectations for the Context and CloseSend methods
	stream.On("Context").Return(context.Background())
	stream.On("CloseSend").Return(nil)

	// Configure the mock client to return our stream
	mockClient.On("Query", mock.Anything, mock.MatchedBy(func(req *dbpb.QueryRequest) bool {
		return req.Query == "SELECT * FROM test WHERE id = ?" &&
			len(req.Parameters) == 1 &&
			req.Parameters[0].GetInt64Value() == 1
	})).Return(stream, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test Query method
	ctx := context.Background()
	rows, err := client.Query(ctx, "SELECT * FROM test WHERE id = ?", 1)
	require.NoError(t, err)
	require.NotNil(t, rows)
	defer rows.Close()

	// First get the column information
	columns, err := rows.Columns()
	require.NoError(t, err)
	require.Equal(t, []string{"id", "name"}, columns)

	// Process all rows
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
	assert.Equal(t, 1, rowData[0][0])
	assert.Equal(t, "Row A", rowData[0][1])
	assert.Equal(t, 2, rowData[1][0])
	assert.Equal(t, "Row B", rowData[1][1])
	assert.Equal(t, 3, rowData[2][0])
	assert.Equal(t, "Row C", rowData[2][1])

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientQueryErrorWithMockery demonstrates how to use mockery-generated mocks
// to test the error handling in the Query method
func TestClientQueryErrorWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return an error for the Query call
	mockClient.On("Query", mock.Anything, mock.Anything).
		Return(nil, status.Error(codes.Internal, "query error"))

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test Query method with error
	ctx := context.Background()
	rows, err := client.Query(ctx, "SELECT * FROM test", 1)

	// Verify that we got the expected error
	assert.Error(t, err)
	assert.Nil(t, rows)
	assert.Contains(t, err.Error(), "database internal error: query error")

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientExecuteWithMockery demonstrates how to use mockery-generated mocks
// to test the Execute method
func TestClientExecuteWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return a success response for Execute
	mockClient.On("Execute", mock.Anything, mock.MatchedBy(func(req *dbpb.ExecuteRequest) bool {
		// Verify request parameters
		return req.Query == "INSERT INTO test VALUES (?)" &&
			len(req.Parameters) == 1 &&
			req.Parameters[0].GetStringValue() == "test-value"
	}), mock.Anything).Return(&dbpb.ExecuteResponse{
		LastInsertId: 42,
		RowsAffected: 1,
	}, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test Execute method
	ctx := context.Background()
	result, err := client.Execute(ctx, "INSERT INTO test VALUES (?)", "test-value")
	assert.NoError(t, err)
	assert.NotNil(t, result)

	// Verify result data
	lastID, err := result.LastInsertId()
	assert.NoError(t, err)
	assert.Equal(t, int64(42), lastID)

	rowsAffected, err := result.RowsAffected()
	assert.NoError(t, err)
	assert.Equal(t, int64(1), rowsAffected)

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientQueryRowWithMockery demonstrates how to use mockery-generated mocks
// to test the QueryRow method
func TestClientQueryRowWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return a row for QueryRow
	mockClient.On("QueryRow", mock.Anything, mock.MatchedBy(func(req *dbpb.QueryRequest) bool {
		return req.Query == "SELECT * FROM test WHERE id = ?" &&
			len(req.Parameters) == 1 &&
			req.Parameters[0].GetInt64Value() == 1
	}), mock.Anything).Return(&dbpb.QueryRowResponse{
		Found:   true,
		Columns: []string{"id", "name"},
		Values: []*dbpb.Value{
			{Value: &dbpb.Value_Int64Value{Int64Value: 1}},
			{Value: &dbpb.Value_StringValue{StringValue: "Test Row"}},
		},
	}, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test QueryRow method
	ctx := context.Background()
	row := client.QueryRow(ctx, "SELECT * FROM test WHERE id = ?", 1)
	assert.NotNil(t, row)

	// Scan the row values
	var id int
	var name string
	err := row.Scan(&id, &name)
	assert.NoError(t, err)
	assert.Equal(t, 1, id)
	assert.Equal(t, "Test Row", name)

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientQueryRowNotFoundWithMockery tests the behavior when no row is found
func TestClientQueryRowNotFoundWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return no row for QueryRow
	mockClient.On("QueryRow", mock.Anything, mock.Anything, mock.Anything).Return(&dbpb.QueryRowResponse{
		Found:   false,
		Columns: []string{"id", "name"},
	}, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test QueryRow method with no result
	ctx := context.Background()
	row := client.QueryRow(ctx, "SELECT * FROM test WHERE id = ?", 999)

	// Scan should return an error
	var id int
	var name string
	err := row.Scan(&id, &name)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "no rows in result set")

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientBeginTransactionWithMockery tests the BeginTx method
func TestClientBeginTransactionWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return a transaction response
	mockClient.On("BeginTransaction", mock.Anything, mock.MatchedBy(func(req *dbpb.BeginTransactionRequest) bool {
		return req.IsolationLevel == dbpb.IsolationLevel_ISOLATION_LEVEL_SERIALIZABLE &&
			req.ReadOnly == true &&
			req.TimeoutMs == 5000
	}), mock.Anything).Return(&dbpb.TransactionResponse{
		TransactionId: "test-tx-id",
		Success:       true,
	}, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test BeginTx method with options
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

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientPingWithMockery tests the Ping method
func TestClientPingWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return a successful ping response
	mockClient.On("Ping", mock.Anything, mock.MatchedBy(func(req *dbpb.PingRequest) bool {
		return req.TimeoutMs == 0
	}), mock.Anything).Return(&dbpb.PingResponse{
		Success:   true,
		LatencyMs: 15,
	}, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

	// Test Ping method
	ctx := context.Background()
	err := client.Ping(ctx)
	assert.NoError(t, err)

	// Test with error response
	mockClient.On("Ping", mock.Anything, mock.Anything, mock.Anything).Return(&dbpb.PingResponse{
		Success:      false,
		ErrorMessage: "database unavailable",
	}, nil)

	err = client.Ping(ctx)
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "database unavailable")

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}

// TestClientStatsWithMockery tests the Stats method
func TestClientStatsWithMockery(t *testing.T) {
	// Create a mock DatabaseServiceClient
	mockClient := &dbmock.DatabaseServiceClient{}

	// Set up the mock client to return stats
	mockClient.On("GetStats", mock.Anything, mock.Anything, mock.Anything).Return(&dbpb.StatsResponse{
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
	}, nil)

	// Create client with our mock client
	client := &Client{
		client:       mockClient,
		transactions: make(map[string]*Transaction),
	}

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

	// Verify that all expected mock calls were made
	mockClient.AssertExpectations(t)
}
