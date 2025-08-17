# gRPC and Protocol Buffers Integration Guide

## Introduction

This guide explains how gcommon uses Protocol Buffers (protobuf) and gRPC to provide powerful, language-agnostic APIs for microservices. Whether you're building a new microservice or integrating with existing systems, this guide will help
you leverage these technologies effectively.

## What Are Protocol Buffers and gRPC?

**Protocol Buffers** are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data. They're smaller, faster, and simpler than formats like JSON or XML.

**gRPC** is a modern, high-performance RPC framework that works across languages and platforms. It uses Protocol Buffers for service definitions and message serialization.

## Benefits for Microservices

Using Protocol Buffers and gRPC in your microservices provides numerous advantages:

1. **Strong Typing**: Service contracts are explicit and enforced at compile time
2. **High Performance**: Faster serialization/deserialization and HTTP/2-based transport
3. **Language Agnostic**: Services can be implemented and consumed in different languages
4. **Streaming Support**: Built-in support for bidirectional streaming
5. **Code Generation**: Automatic client and server code generation
6. **Schema Evolution**: Backward compatible schema updates

## How gcommon Integrates gRPC

gcommon provides:

1. **Dual Interfaces**: Every module supports both traditional Go methods and gRPC services
2. **Consistent Patterns**: Standard patterns for all modules make learning and usage easier
3. **Configuration Options**: Flexible configuration for both server and client components
4. **Ready-to-Use Examples**: Complete examples showing gRPC integration

## Getting Started

### 1. Using Existing gRPC Services

To use a gcommon module via gRPC:

```go
import (
    "google.golang.org/grpc"
    "github.com/jdfalk/gcommon/pkg/health/grpc"
)

// Create a connection
conn, err := grpc.Dial("localhost:9090", grpc.WithInsecure())
if err != nil {
    log.Fatalf("Failed to connect: %v", err)
}
defer conn.Close()

// Create a client
healthClient := grpc.NewHealthClient(conn)

// Use the client
status, err := healthClient.Check(context.Background(), "database")
```

### 2. Exposing gRPC Services

To expose a gcommon module as a gRPC service:

```go
import (
    "google.golang.org/grpc"
    "github.com/jdfalk/gcommon/pkg/health"
    healthgrpc "github.com/jdfalk/gcommon/pkg/health/grpc"
)

// Create the module instance
healthProvider, err := health.NewProvider(health.DefaultConfig())
if err != nil {
    log.Fatalf("Failed to create health provider: %v", err)
}

// Register health checks
// ...

// Create a gRPC server
grpcServer := grpc.NewServer()

// Create and register the gRPC service
healthService := healthgrpc.NewServer(healthProvider)
healthService.Register(grpcServer)

// Start the server
lis, err := net.Listen("tcp", ":9090")
if err != nil {
    log.Fatalf("Failed to listen: %v", err)
}
grpcServer.Serve(lis)
```

## Module-Specific Usage

### Health Module

The health module provides a gRPC service for querying health status:

```protobuf
service HealthService {
  rpc Check(CheckRequest) returns (CheckResponse);
  rpc CheckAll(CheckAllRequest) returns (CheckAllResponse);
  rpc Watch(WatchRequest) returns (stream HealthEvent);
}
```

Example usage:

```go
// Client code
client := healthgrpc.NewHealthClient(conn)
resp, err := client.Check(ctx, &healthpb.CheckRequest{Name: "database"})
if err != nil {
    log.Fatalf("Health check failed: %v", err)
}
fmt.Printf("Health status: %s\n", resp.Status)
```

### Database Module

The database module provides a gRPC service for database operations:

```protobuf
service DatabaseService {
  rpc Execute(ExecuteRequest) returns (ExecuteResponse);
  rpc Query(QueryRequest) returns (stream QueryResponse);
  // ...
}
```

Example usage:

```go
// Client code
client := dbgrpc.NewDatabaseClient(conn)
resp, err := client.Execute(ctx, &dbpb.ExecuteRequest{
    Query: "INSERT INTO users (name, email) VALUES (?, ?)",
    Parameters: []*dbpb.Value{
        {Value: &dbpb.Value_StringValue{StringValue: "John Doe"}},
        {Value: &dbpb.Value_StringValue{StringValue: "john@example.com"}},
    },
})
```

### Other Modules

Each module in gcommon provides similar gRPC integration. Refer to module-specific documentation for details.

## Advanced Usage

### Streaming

gRPC supports streaming, which is particularly useful for:

1. **Real-time updates**: Subscribe to health status changes
2. **Large result sets**: Stream database query results
3. **Event processing**: Process log or metric events as they occur

Example of streaming health events:

```go
stream, err := client.Watch(ctx, &healthpb.WatchRequest{
    Names: []string{"database", "redis", "api"},
})
if err != nil {
    log.Fatalf("Watch failed: %v", err)
}

for {
    event, err := stream.Recv()
    if err == io.EOF {
        break
    }
    if err != nil {
        log.Fatalf("Watch error: %v", err)
    }
    fmt.Printf("Health event: %s changed to %s\n",
        event.Name, event.Status)
}
```

### Authentication and Security

For secure gRPC communication:

1. **TLS**: Use transport security

```go
// Server
creds, err := credentials.NewServerTLSFromFile("server.crt", "server.key")
if err != nil {
    log.Fatalf("Failed to generate credentials: %v", err)
}
grpcServer := grpc.NewServer(grpc.Creds(creds))

// Client
creds, err := credentials.NewClientTLSFromFile("server.crt", "")
if err != nil {
    log.Fatalf("Failed to generate credentials: %v", err)
}
conn, err := grpc.Dial("localhost:9090", grpc.WithTransportCredentials(creds))
```

2. **Authentication**: Use interceptors for authentication

```go
// Auth interceptor example
func authInterceptor(ctx context.Context, req interface{},
    info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {

    // Extract token from metadata
    md, ok := metadata.FromIncomingContext(ctx)
    if !ok {
        return nil, status.Error(codes.Unauthenticated, "missing metadata")
    }

    // Validate token
    token := md.Get("authorization")
    if !validateToken(token) {
        return nil, status.Error(codes.Unauthenticated, "invalid token")
    }

    // Proceed with the request
    return handler(ctx, req)
}

// Use interceptor
grpcServer := grpc.NewServer(
    grpc.UnaryInterceptor(authInterceptor),
)
```

## Compatibility with REST APIs

For environments that require REST APIs, you can use gRPC Gateway to expose your gRPC services as RESTful JSON APIs:

1. Add gateway annotations to your proto files:

```protobuf
import "google/api/annotations.proto";

service HealthService {
  rpc Check(CheckRequest) returns (CheckResponse) {
    option (google.api.http) = {
      get: "/api/v1/health/{name}"
    };
  }
}
```

2. Generate and use the gateway proxy:

```go
import (
    "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
)

// Create gRPC server
// ...

// Create gateway server
mux := runtime.NewServeMux()
err := healthpb.RegisterHealthServiceHandlerFromEndpoint(
    ctx, mux, "localhost:9090", []grpc.DialOption{grpc.WithInsecure()},
)
if err != nil {
    log.Fatalf("Failed to register gateway: %v", err)
}

// Serve HTTP
http.ListenAndServe(":8080", mux)
```

## Testing gRPC Services

gcommon provides tools for testing gRPC services:

1. **In-memory testing**: Test without network overhead

```go
// Create server and client without network
server := grpc.NewServer()
healthService := healthgrpc.NewServer(healthProvider)
healthService.Register(server)

// Create in-memory connection
clientConn, serverConn := net.Pipe()
go server.Serve(serverConn)

// Create client using the in-memory connection
client := healthgrpc.NewHealthClient(clientConn)

// Test
resp, err := client.Check(ctx, &healthpb.CheckRequest{Name: "test"})
```

2. **Mock services**: Use generated mock clients for unit testing

## Best Practices

1. **Define Service Boundaries Carefully**: Each service should represent a cohesive capability
2. **Version Your APIs**: Use protobuf versioning to maintain backward compatibility
3. **Handle Errors Consistently**: Use standard error codes and include detailed error messages
4. **Document Your Services**: Add detailed comments to your proto files
5. **Monitor Your Services**: Track metrics like request count, error rate, and latency
6. **Test Thoroughly**: Test both happy path and error conditions

## Conclusion

By integrating Protocol Buffers and gRPC, gcommon provides a powerful foundation for building robust, high-performance microservices. This integration enables language-agnostic communication, strong typing, and high efficiency while
maintaining compatibility with traditional development patterns.

For detailed protocol definitions and implementation specifics, refer to the [Protocol Buffers and gRPC Technical Design](../technical/protobuf-grpc-design.md) document.
