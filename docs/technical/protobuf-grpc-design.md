# Protocol Buffers and gRPC Integration Strategy

## Overview

This document outlines the strategy for integrating Protocol Buffers (protobuf) and gRPC across all modules of the gcommon library. This integration will enable language-agnostic service definitions, efficient serialization, standardized
API contracts, and streamlined microservices architecture.

## Core Principles

1. **Protocol-First Design**: All modules should be designed with Protocol Buffers as the primary data exchange format.
2. **Dual Interface Support**: Each module should support both traditional Go interfaces and gRPC interfaces.
3. **Consistent Versioning**: All proto files should follow a consistent versioning strategy.
4. **Backward Compatibility**: Changes to proto definitions should maintain backward compatibility.
5. **Cross-Language Support**: Proto definitions should be designed to work well across multiple languages.

## Directory Structure

```
pkg/<module>/
  ├── interfaces.go       # Go interfaces
  ├── implementations/    # Go implementations
  ├── proto/              # Protocol Buffer definitions
  │   ├── <module>.proto  # Main proto file
  │   ├── v1/             # Version 1 API
  │   ├── generate.sh     # Code generation script
  │   └── README.md       # Proto documentation
  └── grpc/               # gRPC server implementations
      ├── server.go       # gRPC server implementation
      └── client.go       # gRPC client
```

## Protocol Buffer Standards

### File Structure

Each proto file should follow this template:

```protobuf
edition = "2023";

package <module>.v1;

option go_package = "github.com/jdfalk/gcommon/pkg/<module>/proto/v1";

// Import common definitions
import "google/protobuf/timestamp.proto";
import "google/protobuf/empty.proto";

// Service definition
service <Module>Service {
  // Methods...
}

// Message definitions
message Request {
  // Fields...
}

message Response {
  // Fields...
}
```

### Naming Conventions

- **Services**: `<Module>Service` (e.g., `DatabaseService`, `CacheService`)
- **Methods**: Use verb-noun format (e.g., `GetConfig`, `StoreValue`)
- **Messages**: Use purpose-based names (e.g., `StoreValueRequest`, `ConfigResponse`)
- **Fields**: Use snake_case (e.g., `connection_string`, `max_connections`)
- **Enums**: Use PascalCase for type names and SCREAMING_SNAKE_CASE for values

### Common Types

Define common types in a shared proto package:

```protobuf
// common/types.proto
edition = "2023";

package common.v1;

option go_package = "github.com/jdfalk/gcommon/pkg/common/proto/v1";

message Error {
  int32 code = 1;
  string message = 2;
  string details = 3;
}

message Status {
  enum StatusCode {
    STATUS_CODE_UNSPECIFIED = 0;
    STATUS_CODE_OK = 1;
    STATUS_CODE_ERROR = 2;
    // ...
  }
  StatusCode code = 1;
  string message = 2;
}
```

## gRPC Service Implementation

### Server Implementation

Each module should provide a gRPC server implementation that:

1. Wraps the standard Go implementation
2. Implements the generated gRPC service interface
3. Translates between protobuf and Go native types

Example server implementation pattern:

```go
type MyModuleGRPCServer struct {
  pb.UnimplementedMyModuleServiceServer
  implementation MyModule // Standard Go implementation
}

func NewGRPCServer(impl MyModule) *MyModuleGRPCServer {
  return &MyModuleGRPCServer{implementation: impl}
}

func (s *MyModuleGRPCServer) DoSomething(ctx context.Context, req *pb.DoSomethingRequest) (*pb.DoSomethingResponse, error) {
  // Convert request
  nativeReq := convertRequest(req)

  // Call implementation
  result, err := s.implementation.DoSomething(ctx, nativeReq)
  if err != nil {
    return nil, statusFromError(err)
  }

  // Convert response
  return convertResponse(result), nil
}
```

### Client Implementation

Each module should provide a client implementation that:

1. Implements the standard Go interface
2. Uses the generated gRPC client
3. Translates between protobuf and Go native types

Example client implementation pattern:

```go
type MyModuleGRPCClient struct {
  client pb.MyModuleServiceClient
}

func NewGRPCClient(conn *grpc.ClientConn) MyModule {
  return &MyModuleGRPCClient{client: pb.NewMyModuleServiceClient(conn)}
}

func (c *MyModuleGRPCClient) DoSomething(ctx context.Context, req MyRequest) (MyResponse, error) {
  // Convert request
  pbReq := convertToPBRequest(req)

  // Call gRPC
  pbResp, err := c.client.DoSomething(ctx, pbReq)
  if err != nil {
    return MyResponse{}, errorFromStatus(err)
  }

  // Convert response
  return convertFromPBResponse(pbResp), nil
}
```

## Module-Specific Integrations

### Database Module

The database module will provide:

1. Protocol Buffer definitions for queries, results, and transactions
2. gRPC services for executing queries and managing transactions
3. Support for streaming query results

Example proto:

```protobuf
service DatabaseService {
  rpc Execute(ExecuteRequest) returns (ExecuteResponse);
  rpc Query(QueryRequest) returns (stream QueryResponse);
  rpc BeginTransaction(BeginTransactionRequest) returns (TransactionResponse);
  // ...
}
```

### Cache Module

The cache module will provide:

1. Protocol Buffer definitions for cache operations
2. gRPC services for getting, setting, and invalidating cached items

Example proto:

```protobuf
service CacheService {
  rpc Get(GetRequest) returns (GetResponse);
  rpc Set(SetRequest) returns (SetResponse);
  rpc Delete(DeleteRequest) returns (DeleteResponse);
  // ...
}
```

### Config Module

The config module will provide:

1. Protocol Buffer definitions for configuration
2. gRPC services for retrieving and updating configuration
3. Support for config change notifications via streaming

Example proto:

```protobuf
service ConfigService {
  rpc GetConfig(GetConfigRequest) returns (GetConfigResponse);
  rpc UpdateConfig(UpdateConfigRequest) returns (UpdateConfigResponse);
  rpc WatchConfig(WatchConfigRequest) returns (stream ConfigChangeEvent);
  // ...
}
```

### Logging Module

The logging module will provide:

1. Protocol Buffer definitions for log entries
2. gRPC services for remote logging
3. Support for log streaming and filtering

Example proto:

```protobuf
service LoggingService {
  rpc Log(LogRequest) returns (LogResponse);
  rpc StreamLogs(StreamLogsRequest) returns (stream LogEntry);
  // ...
}
```

### Metrics Module

The metrics module will provide:

1. Protocol Buffer definitions for metrics data
2. gRPC services for reporting and retrieving metrics
3. Support for metrics streaming

Example proto:

```protobuf
service MetricsService {
  rpc ReportMetrics(ReportMetricsRequest) returns (ReportMetricsResponse);
  rpc GetMetrics(GetMetricsRequest) returns (GetMetricsResponse);
  rpc WatchMetrics(WatchMetricsRequest) returns (stream MetricUpdate);
  // ...
}
```

### Auth Module

The auth module will provide:

1. Protocol Buffer definitions for authentication and authorization
2. gRPC services for authentication, token validation, and permission checking

Example proto:

```protobuf
service AuthService {
  rpc Authenticate(AuthenticateRequest) returns (AuthenticateResponse);
  rpc ValidateToken(ValidateTokenRequest) returns (ValidateTokenResponse);
  rpc CheckPermission(CheckPermissionRequest) returns (CheckPermissionResponse);
  // ...
}
```

### Queue Module

The queue module will provide:

1. Protocol Buffer definitions for queue operations
2. gRPC services for enqueueing, dequeueing, and managing queues
3. Support for message streaming

Example proto:

```protobuf
service QueueService {
  rpc Enqueue(EnqueueRequest) returns (EnqueueResponse);
  rpc Dequeue(DequeueRequest) returns (DequeueResponse);
  rpc Subscribe(SubscribeRequest) returns (stream Message);
  // ...
}
```

## Cross-Cutting Concerns

### Error Handling

Define a consistent error model:

1. Use gRPC status codes appropriately
2. Include error details in a structured format
3. Provide a mechanism to convert between Go errors and gRPC errors

### Security

Implement standard security patterns:

1. TLS for all gRPC connections
2. Authentication via interceptors
3. Token-based authorization
4. Security for streaming connections

### Versioning

Maintain API versioning:

1. Use directory-based versioning for proto files (v1, v2, etc.)
2. Include version in package name
3. Never remove or change the semantics of fields in existing messages
4. Follow semantic versioning principles

### Documentation

Each proto file should be well-documented:

1. Service-level documentation explaining the service's purpose
2. Method-level documentation explaining each operation
3. Message-level documentation explaining the data structure
4. Field-level documentation explaining the meaning of each field

## Implementation Roadmap

1. **Define Common Types**: Create shared proto definitions for common types
2. **Create Proto Templates**: Define templates for each module
3. **Implement Health Module**: Complete protobuf/gRPC for health module (already done)
4. **Database Module**: Implement database protobufs and gRPC service
5. **Extend Incrementally**: Add protobuf/gRPC support to each module
6. **Integration Testing**: Create comprehensive tests for gRPC services
7. **Documentation**: Document all proto definitions and gRPC APIs

## Conclusion

This strategy provides a comprehensive approach to integrating Protocol Buffers and gRPC throughout the gcommon library. By following these guidelines, we'll create a powerful, consistent, and interoperable foundation for microservices
development.
