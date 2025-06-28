# GCommon Protobuf Implementation Guide

## Overview

This guide provides step-by-step instructions for implementing the recommendations from the [Protobuf Comprehensive Breakdown](./protobuf-comprehensive-breakdown.md). It focuses on practical implementation steps to standardize and improve the existing protobuf definitions.

## Phase 1: Foundation Implementation

### Step 1: Integrate Common Types

1. **Update generate.sh script** to include the new common proto:

   ```bash
   # Add to generate.sh after the existing protoc commands
   protoc --go_out=. --go_opt=paths=source_relative \
          --go-grpc_out=. --go-grpc_opt=paths=source_relative \
          pkg/common/proto/common.proto
   ```

2. **Update all existing proto files** to import common types:
   ```protobuf
   import "pkg/common/proto/common.proto";
   ```

### Step 2: Standardize Error Handling

#### Health Module Example Implementation

**Before**:

```protobuf
message HealthCheckResponse {
  HealthStatus status = 1;
  string message = 2;
  map<string, string> details = 3;
  google.protobuf.Timestamp timestamp = 4;
}
```

**After**:

```protobuf
import "pkg/common/proto/common.proto";

message HealthCheckResponse {
  gcommon.common.v1.HealthStatus status = 1;
  string message = 2;
  map<string, string> details = 3;
  google.protobuf.Timestamp timestamp = 4;
  // Add standardized error for failure cases
  gcommon.common.v1.Error error = 5;
  // Add request metadata for tracing
  gcommon.common.v1.RequestMetadata metadata = 6;
}
```

#### Database Module Example Implementation

**Before**:

```protobuf
message GetResponse {
  DatabaseValue value = 1;
  bool found = 2;
  string error = 3;
}
```

**After**:

```protobuf
import "pkg/common/proto/common.proto";

message GetResponse {
  DatabaseValue value = 1;
  bool found = 2;
  // Replace string error with standardized error
  gcommon.common.v1.Error error = 3;
  // Add metadata for observability
  gcommon.common.v1.RequestMetadata metadata = 4;
}
```

### Step 3: Standardize Pagination

#### Example: Config Module List Operation

**Before**:

```protobuf
message ListConfigRequest {
  string prefix = 1;
  int32 limit = 2;
  string cursor = 3;
}

message ListConfigResponse {
  repeated ConfigValue configs = 1;
  string next_cursor = 2;
  bool has_more = 3;
}
```

**After**:

```protobuf
import "pkg/common/proto/common.proto";

message ListConfigRequest {
  string prefix = 1;
  // Use standardized pagination
  gcommon.common.v1.Pagination pagination = 2;
  // Add standardized filtering
  gcommon.common.v1.FilterOptions filter = 3;
  // Add standardized sorting
  gcommon.common.v1.SortOptions sort = 4;
}

message ListConfigResponse {
  repeated ConfigValue configs = 1;
  // Use standardized pagination response
  gcommon.common.v1.PaginatedResponse pagination = 2;
  // Add standardized error handling
  gcommon.common.v1.Error error = 3;
}
```

### Step 4: Add Request Metadata to All Services

Update all service methods to include request metadata:

```protobuf
import "pkg/common/proto/common.proto";

message HealthCheckRequest {
  string component = 1;
  HealthCheckOptions options = 2;
  // Add metadata to all requests
  gcommon.common.v1.RequestMetadata metadata = 3;
}
```

## Phase 2: Cross-Module Integration

### Step 1: Add Authentication Context

Create an authentication interceptor message:

```protobuf
// Add to common.proto
message AuthContext {
  string user_id = 1;
  repeated string roles = 2;
  repeated string permissions = 3;
  string token = 4;
  google.protobuf.Timestamp expires_at = 5;
}

// Update RequestMetadata to include auth
message RequestMetadata {
  // ... existing fields ...
  AuthContext auth = 8;
}
```

### Step 2: Enhance Observability Integration

Add observability fields to all responses:

```protobuf
// Add to common.proto
message ObservabilityInfo {
  // Processing duration
  google.protobuf.Duration duration = 1;

  // Resource usage metrics
  map<string, double> metrics = 2;

  // Related trace spans
  repeated string span_ids = 3;

  // Performance warnings
  repeated string warnings = 4;
}

// Add to all response messages
message ExampleResponse {
  // ... existing fields ...
  gcommon.common.v1.ObservabilityInfo observability = 10;
}
```

### Step 3: Standardize Configuration Integration

Add module-specific configuration that references the common config service:

```protobuf
// Add to each module's proto
message ModuleConfig {
  // Reference to config service
  string config_key = 1;

  // Local overrides
  map<string, gcommon.common.v1.ConfigValue> overrides = 2;

  // Update notifications
  bool watch_changes = 3;
}
```

## Phase 3: Advanced Features

### Step 1: Add Validation Rules

Extend common types with validation:

```protobuf
// Add to common.proto
message ValidationRule {
  string field = 1;
  ValidationConstraint constraint = 2;
  string message = 3;
}

message ValidationConstraint {
  oneof constraint {
    StringConstraint string_constraint = 1;
    NumberConstraint number_constraint = 2;
    ArrayConstraint array_constraint = 3;
  }
}

message StringConstraint {
  int32 min_length = 1;
  int32 max_length = 2;
  string pattern = 3;
  repeated string allowed_values = 4;
}

message NumberConstraint {
  double min_value = 1;
  double max_value = 2;
  bool integer_only = 3;
}

message ArrayConstraint {
  int32 min_items = 1;
  int32 max_items = 2;
  bool unique_items = 3;
}
```

### Step 2: Add API Versioning Support

Create versioning headers:

```protobuf
// Add to common.proto
message ApiVersion {
  string version = 1;
  google.protobuf.Timestamp deprecated_at = 2;
  google.protobuf.Timestamp sunset_at = 3;
  repeated string breaking_changes = 4;
}

// Add to RequestMetadata
message RequestMetadata {
  // ... existing fields ...
  ApiVersion api_version = 9;
}
```

### Step 3: Add Cross-Module Operations

Create cross-module operation types:

```protobuf
// Add to common.proto
message CrossModuleOperation {
  string operation_id = 1;
  repeated ResourceReference resources = 2;
  CrossModuleOperationType type = 3;
  map<string, google.protobuf.Any> parameters = 4;
}

enum CrossModuleOperationType {
  CROSS_MODULE_OPERATION_TYPE_UNSPECIFIED = 0;
  CROSS_MODULE_OPERATION_TYPE_BACKUP = 1;
  CROSS_MODULE_OPERATION_TYPE_RESTORE = 2;
  CROSS_MODULE_OPERATION_TYPE_MIGRATE = 3;
  CROSS_MODULE_OPERATION_TYPE_SYNC = 4;
}
```

## Implementation Checklist

### Phase 1: Foundation (Week 1-2)

- [ ] Create `pkg/common/proto/common.proto`
- [ ] Update `generate.sh` to include common proto
- [ ] Update all 9 existing proto files to import common types
- [ ] Replace custom error handling with standardized errors
- [ ] Add RequestMetadata to all service methods
- [ ] Standardize pagination across all list operations
- [ ] Generate and test all protobuf code
- [ ] Update documentation with new patterns

### Phase 2: Integration (Week 3-4)

- [ ] Add AuthContext to RequestMetadata
- [ ] Implement authentication interceptors
- [ ] Add ObservabilityInfo to all responses
- [ ] Integrate with existing metrics and logging
- [ ] Standardize configuration references
- [ ] Update service implementations to use new types
- [ ] Add integration tests
- [ ] Update gRPC client examples

### Phase 3: Enhancement (Week 5-6)

- [ ] Add validation rules to all message types
- [ ] Implement API versioning headers
- [ ] Create cross-module operation framework
- [ ] Add advanced filtering and sorting
- [ ] Implement rate limiting headers
- [ ] Add performance monitoring
- [ ] Create migration guide for existing clients
- [ ] Update comprehensive documentation

## Testing Strategy

### Unit Tests

- Test protobuf serialization/deserialization
- Validate message construction with common types
- Test error handling standardization

### Integration Tests

- Test cross-module operations
- Validate authentication flow
- Test observability data collection

### Performance Tests

- Measure impact of additional metadata
- Test pagination performance
- Validate streaming operations

## Migration Guide for Existing Clients

### Breaking Changes

1. Error responses now use structured `Error` type instead of string
2. Pagination parameters standardized across all services
3. Request metadata required for all operations

### Non-Breaking Changes

1. Additional observability fields in responses
2. Enhanced filtering and sorting options
3. Cross-module operation support

### Migration Steps

1. Update client code to handle new error format
2. Migrate pagination logic to use new types
3. Add request metadata population
4. Update error handling to use error codes
5. Test all existing functionality

## Monitoring and Metrics

### Key Metrics to Track

- Proto compilation time
- Message size impact
- Service latency changes
- Error rate changes
- Client adoption of new features

### Alerts

- Proto compilation failures
- Significant latency increases
- High error rates during migration
- Client compatibility issues

## Conclusion

This implementation guide provides a structured approach to modernizing the GCommon protobuf definitions. By following these steps in phases, the project can achieve better consistency, improved observability, and enhanced developer experience while minimizing disruption to existing clients.

The key to success is incremental implementation with thorough testing at each phase, ensuring that improvements don't break existing functionality while adding valuable new capabilities.
