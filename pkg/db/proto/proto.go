// file: pkg/db/proto/proto.go

// Package dbpb provides consolidated exports for database protobuf types
package dbpb

// Re-export types from various database protobuf packages for backwards compatibility
import (
	dbpb_messages "github.com/jdfalk/gcommon/pkg/db/proto/messages"
	dbpb_requests "github.com/jdfalk/gcommon/pkg/db/proto/requests"
	dbpb_responses "github.com/jdfalk/gcommon/pkg/db/proto/responses"
	dbpb_services "github.com/jdfalk/gcommon/pkg/db/proto/services"
	dbpb_types "github.com/jdfalk/gcommon/pkg/db/proto/types"
)

// Service interfaces
type (
	DatabaseServiceClient      = dbpb_services.DatabaseServiceClient
	DatabaseServiceServer      = dbpb_services.DatabaseServiceServer
	DatabaseAdminServiceClient = dbpb_services.DatabaseAdminServiceClient
	DatabaseAdminServiceServer = dbpb_services.DatabaseAdminServiceServer
)

// Request types
type (
	QueryRequest               = dbpb_requests.QueryRequest
	ExecuteRequest             = dbpb_requests.ExecuteRequest
	ExecuteBatchRequest        = dbpb_requests.ExecuteBatchRequest
	BeginTransactionRequest    = dbpb_requests.BeginTransactionRequest
	CommitTransactionRequest   = dbpb_requests.CommitTransactionRequest
	RollbackTransactionRequest = dbpb_requests.RollbackTransactionRequest
	CreateDatabaseRequest      = dbpb_requests.CreateDatabaseRequest
	DropDatabaseRequest        = dbpb_requests.DropDatabaseRequest
	CreateSchemaRequest        = dbpb_requests.CreateSchemaRequest
	DropSchemaRequest          = dbpb_requests.DropSchemaRequest
	ListSchemasRequest         = dbpb_requests.ListSchemasRequest
	GetDatabaseInfoRequest     = dbpb_requests.GetDatabaseInfoRequest
	RunMigrationRequest        = dbpb_requests.RunMigrationRequest
	GetMigrationStatusRequest  = dbpb_requests.GetMigrationStatusRequest
	HealthCheckRequest         = dbpb_requests.HealthCheckRequest
)

// Response types
type (
	QueryResponse               = dbpb_responses.QueryResponse
	ExecuteResponse             = dbpb_responses.ExecuteResponse
	ExecuteBatchResponse        = dbpb_responses.ExecuteBatchResponse
	BeginTransactionResponse    = dbpb_responses.BeginTransactionResponse
	CommitTransactionResponse   = dbpb_responses.CommitTransactionResponse
	RollbackTransactionResponse = dbpb_responses.RollbackTransactionResponse
	CreateDatabaseResponse      = dbpb_responses.CreateDatabaseResponse
	DropDatabaseResponse        = dbpb_responses.DropDatabaseResponse
	CreateSchemaResponse        = dbpb_responses.CreateSchemaResponse
	DropSchemaResponse          = dbpb_responses.DropSchemaResponse
	ListSchemasResponse         = dbpb_responses.ListSchemasResponse
	GetDatabaseInfoResponse     = dbpb_responses.GetDatabaseInfoResponse
	RunMigrationResponse        = dbpb_responses.RunMigrationResponse
	GetMigrationStatusResponse  = dbpb_responses.GetMigrationStatusResponse
	HealthCheckResponse         = dbpb_responses.HealthCheckResponse
)

// Type definitions
type (
	DatabaseInfo = dbpb_types.DatabaseInfo
	SchemaInfo   = dbpb_types.SchemaInfo
	TableInfo    = dbpb_types.TableInfo
	ColumnInfo   = dbpb_types.ColumnInfo
	IndexInfo    = dbpb_types.IndexInfo
)

// Message types
type (
	ResultSet      = dbpb_messages.ResultSet
	Row            = dbpb_messages.Row
	Field          = dbpb_messages.Field
	Transaction    = dbpb_messages.Transaction
	BatchOperation = dbpb_messages.BatchOperation
)
