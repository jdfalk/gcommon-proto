# Complete Protobuf Mapping for GCommon

## Overview

This document provides a 100% complete mapping of all protobuf messages and
services required for the GCommon project. Each module is analyzed based on the
technical design documents and project goals to ensure comprehensive coverage.

## Common Types Module

**File**: `pkg/common/proto/common.proto` **Package**: `gcommon.common.v1`

### Core Messages

✅ **Implemented** - These are already defined in the common.proto file:

1. `Error` - Standardized error handling
2. `ErrorCode` (enum) - Standard error codes
3. `Pagination` - Common pagination parameters
4. `PaginatedResponse` - Standard pagination response
5. `RequestMetadata` - Request context and observability
6. `ClientInfo` - Client identification
7. `TimeRange` - Time-based filtering
8. `SortOptions` - Sorting parameters
9. `FilterOptions` - Filtering parameters
10. `FilterValue` - Multi-type filter values
11. `FilterOperation` (enum) - Filter operations
12. `HealthStatus` (enum) - Common health status
13. `ResourceStatus` (enum) - Resource lifecycle status
14. `KeyValue` - Generic key-value pairs
15. `ResourceReference` - Cross-module resource references
16. `MetricPoint` - Common metrics data
17. `ConfigValue` - Configuration value with types
18. `ValueType` (enum) - Value type definitions
19. `RateLimit` - Rate limiting information
20. `ServiceVersion` - Service version metadata

### Additional Common Messages Needed

🔄 **To Be Added**:

21. `AuditLog` - For tracking operations across modules
22. `BatchOperation` - For batch request patterns
23. `SubscriptionInfo` - For streaming subscriptions
24. `CachePolicy` - Common cache policies
25. `RetryPolicy` - Retry configuration
26. `CircuitBreakerConfig` - Circuit breaker settings

---

## 1. Health Module

**File**: `pkg/health/proto/health.proto` **Package**: `gcommon.health.v1`

### Services Required

#### HealthService

1. `Check(HealthCheckRequest) → HealthCheckResponse`
2. `Watch(HealthCheckRequest) → stream HealthCheckResponse`
3. `CheckAll(HealthCheckAllRequest) → HealthCheckAllResponse`
4. `GetHistory(HealthHistoryRequest) → HealthHistoryResponse`
5. `RegisterCheck(RegisterCheckRequest) → RegisterCheckResponse`
6. `UnregisterCheck(UnregisterCheckRequest) → UnregisterCheckResponse`
7. `UpdateCheck(UpdateCheckRequest) → UpdateCheckResponse`
8. `TriggerRemediation(RemediationRequest) → RemediationResponse`
9. `GetRemediationHistory(RemediationHistoryRequest) → RemediationHistoryResponse`
10. `GetMetrics(HealthMetricsRequest) → HealthMetricsResponse`

### Messages Required

#### Request Messages

1. `HealthCheckRequest` ✅ (service name, options)
2. `HealthCheckAllRequest` ✅ (include details, filter types)
3. `HealthHistoryRequest` (time range, service filter)
4. `RegisterCheckRequest` (check definition, config)
5. `UnregisterCheckRequest` (check ID/name)
6. `UpdateCheckRequest` (check ID, new config)
7. `RemediationRequest` (service, action type, parameters)
8. `RemediationHistoryRequest` (time range, service filter)
9. `HealthMetricsRequest` (time range, metric types)

#### Response Messages

1. `HealthCheckResponse` ✅ (status, timestamp, details)
2. `HealthCheckAllResponse` ✅ (overall status, individual results)
3. `HealthHistoryResponse` (history entries, pagination)
4. `RegisterCheckResponse` (check ID, success status)
5. `UnregisterCheckResponse` (success status)
6. `UpdateCheckResponse` (success status)
7. `RemediationResponse` (action taken, success, details)
8. `RemediationHistoryResponse` (remediation entries)
9. `HealthMetricsResponse` (metrics data)

#### Core Messages

1. `HealthCheck` - Check definition with config
2. `HealthResult` - Individual check result
3. `HealthConfig` - Check configuration
4. `RemediationAction` - Remediation definition
5. `RemediationResult` - Remediation execution result
6. `HealthMetric` - Health-specific metrics
7. `CheckType` (enum) - Types of health checks
8. `ServingStatus` (enum) ✅ - Health status values
9. `RemediationType` (enum) - Types of remediation

---

## 2. Authentication Module

**File**: `pkg/auth/proto/auth.proto` **Package**: `gcommon.auth.v1`

### Services Required

#### AuthService

1. `Authenticate(AuthenticateRequest) → AuthenticateResponse`
2. `ValidateToken(ValidateTokenRequest) → ValidateTokenResponse`
3. `RefreshToken(RefreshTokenRequest) → RefreshTokenResponse`
4. `RevokeToken(RevokeTokenRequest) → RevokeTokenResponse`
5. `GenerateToken(GenerateTokenRequest) → GenerateTokenResponse`
6. `GetUserInfo(UserInfoRequest) → UserInfoResponse`
7. `UpdateUserInfo(UpdateUserInfoRequest) → UpdateUserInfoResponse`
8. `ChangePassword(ChangePasswordRequest) → ChangePasswordResponse`

#### AuthorizationService

1. `Authorize(AuthorizeRequest) → AuthorizeResponse`
2. `HasRole(HasRoleRequest) → HasRoleResponse`
3. `HasPermission(HasPermissionRequest) → HasPermissionResponse`
4. `ListRoles(ListRolesRequest) → ListRolesResponse`
5. `ListPermissions(ListPermissionsRequest) → ListPermissionsResponse`
6. `CreateRole(CreateRoleRequest) → CreateRoleResponse`
7. `UpdateRole(UpdateRoleRequest) → UpdateRoleResponse`
8. `DeleteRole(DeleteRoleRequest) → DeleteRoleResponse`
9. `AssignRole(AssignRoleRequest) → AssignRoleResponse`
10. `RevokeRole(RevokeRoleRequest) → RevokeRoleResponse`

#### SessionService

1. `CreateSession(CreateSessionRequest) → CreateSessionResponse`
2. `GetSession(GetSessionRequest) → GetSessionResponse`
3. `UpdateSession(UpdateSessionRequest) → UpdateSessionResponse`
4. `DeleteSession(DeleteSessionRequest) → DeleteSessionResponse`
5. `ListSessions(ListSessionsRequest) → ListSessionsResponse`

### Messages Required

#### Authentication Messages

1. `AuthenticateRequest` ✅ (credentials, auth type)
2. `AuthenticateResponse` ✅ (identity, token, success)
3. `ValidateTokenRequest` ✅ (token)
4. `ValidateTokenResponse` ✅ (valid, identity, claims)
5. `RefreshTokenRequest` ✅ (refresh token)
6. `RefreshTokenResponse` ✅ (new tokens)
7. `RevokeTokenRequest` (token to revoke)
8. `RevokeTokenResponse` (success status)
9. `GenerateTokenRequest` (identity, claims, options)
10. `GenerateTokenResponse` (token, expiry)

#### User Management Messages

1. `UserInfoRequest` (user ID or token)
2. `UserInfoResponse` (user profile, roles, permissions)
3. `UpdateUserInfoRequest` (user ID, field updates)
4. `UpdateUserInfoResponse` (success, updated user)
5. `ChangePasswordRequest` (user ID, old/new password)
6. `ChangePasswordResponse` (success status)

#### Authorization Messages

1. `AuthorizeRequest` ✅ (identity, resource, action)
2. `AuthorizeResponse` ✅ (allowed, reason)
3. `HasRoleRequest` ✅ (identity, role)
4. `HasRoleResponse` ✅ (has role)
5. `HasPermissionRequest` (identity, permission, resource)
6. `HasPermissionResponse` (has permission)
7. `ListRolesRequest` (user filter, pagination)
8. `ListRolesResponse` (roles, pagination)
9. `ListPermissionsRequest` (role filter, pagination)
10. `ListPermissionsResponse` (permissions, pagination)

#### Role Management Messages

1. `CreateRoleRequest` (role definition)
2. `CreateRoleResponse` (created role)
3. `UpdateRoleRequest` (role ID, updates)
4. `UpdateRoleResponse` (updated role)
5. `DeleteRoleRequest` (role ID)
6. `DeleteRoleResponse` (success status)
7. `AssignRoleRequest` (user ID, role ID)
8. `AssignRoleResponse` (success status)
9. `RevokeRoleRequest` (user ID, role ID)
10. `RevokeRoleResponse` (success status)

#### Session Messages

1. `CreateSessionRequest` (user ID, session data)
2. `CreateSessionResponse` (session ID, expiry)
3. `GetSessionRequest` (session ID)
4. `GetSessionResponse` (session data)
5. `UpdateSessionRequest` (session ID, updates)
6. `UpdateSessionResponse` (success status)
7. `DeleteSessionRequest` (session ID)
8. `DeleteSessionResponse` (success status)
9. `ListSessionsRequest` (user filter, pagination)
10. `ListSessionsResponse` (sessions, pagination)

#### Core Types

1. `Identity` ✅ - User identity information
2. `AuthToken` ✅ - Token with metadata
3. `Credentials` - Authentication credentials
4. `Role` - Role definition with permissions
5. `Permission` - Permission definition
6. `Session` - Session data
7. `AuthMethod` (enum) ✅ - Authentication methods
8. `TokenType` (enum) - Token types (access, refresh, etc.)
9. `AuthStatus` (enum) - Authentication status

---

## 3. Database Module

**File**: `pkg/db/proto/database.proto` **Package**: `gcommon.database.v1`

### Services Required

#### DatabaseService

1. `Get(GetRequest) → GetResponse`
2. `Set(SetRequest) → SetResponse`
3. `Delete(DeleteRequest) → DeleteResponse`
4. `List(ListRequest) → ListResponse`
5. `Query(QueryRequest) → QueryResponse`
6. `Execute(ExecuteRequest) → ExecuteResponse`
7. `BatchExecute(BatchRequest) → BatchResponse`

#### TransactionService

1. `BeginTransaction(BeginTransactionRequest) → BeginTransactionResponse`
2. `CommitTransaction(CommitTransactionRequest) → CommitTransactionResponse`
3. `RollbackTransaction(RollbackTransactionRequest) → RollbackTransactionResponse`
4. `GetTransactionStatus(TransactionStatusRequest) → TransactionStatusResponse`

#### SchemaService

1. `CreateTable(CreateTableRequest) → CreateTableResponse`
2. `AlterTable(AlterTableRequest) → AlterTableResponse`
3. `DropTable(DropTableRequest) → DropTableResponse`
4. `ListTables(ListTablesRequest) → ListTablesResponse`
5. `DescribeTable(DescribeTableRequest) → DescribeTableResponse`
6. `CreateIndex(CreateIndexRequest) → CreateIndexResponse`
7. `DropIndex(DropIndexRequest) → DropIndexResponse`

#### MigrationService

1. `ApplyMigration(ApplyMigrationRequest) → ApplyMigrationResponse`
2. `RevertMigration(RevertMigrationRequest) → RevertMigrationResponse`
3. `GetMigrationStatus(MigrationStatusRequest) → MigrationStatusResponse`
4. `ListMigrations(ListMigrationsRequest) → ListMigrationsResponse`

### Messages Required

#### Core Operation Messages

1. `GetRequest` ✅ (key, table, options)
2. `GetResponse` ✅ (value, found, metadata)
3. `SetRequest` ✅ (key, value, table, options)
4. `SetResponse` ✅ (success, metadata)
5. `DeleteRequest` ✅ (key, table, options)
6. `DeleteResponse` ✅ (success, found)
7. `ListRequest` ✅ (table, filter, pagination)
8. `ListResponse` ✅ (values, pagination)
9. `QueryRequest` (SQL query, parameters, options)
10. `QueryResponse` (rows, metadata)
11. `ExecuteRequest` (SQL statement, parameters)
12. `ExecuteResponse` (affected rows, metadata)
13. `BatchRequest` ✅ (operations list)
14. `BatchResponse` ✅ (results list)

#### Transaction Messages

1. `BeginTransactionRequest` ✅ (isolation level, timeout)
2. `BeginTransactionResponse` ✅ (transaction ID)
3. `CommitTransactionRequest` ✅ (transaction ID)
4. `CommitTransactionResponse` ✅ (success status)
5. `RollbackTransactionRequest` ✅ (transaction ID)
6. `RollbackTransactionResponse` ✅ (success status)
7. `TransactionStatusRequest` (transaction ID)
8. `TransactionStatusResponse` (status, metadata)

#### Schema Messages

1. `CreateTableRequest` (table definition)
2. `CreateTableResponse` (success status)
3. `AlterTableRequest` (table name, alterations)
4. `AlterTableResponse` (success status)
5. `DropTableRequest` (table name, cascade)
6. `DropTableResponse` (success status)
7. `ListTablesRequest` (schema filter)
8. `ListTablesResponse` (table names, metadata)
9. `DescribeTableRequest` (table name)
10. `DescribeTableResponse` (table schema)
11. `CreateIndexRequest` (index definition)
12. `CreateIndexResponse` (success status)
13. `DropIndexRequest` (index name)
14. `DropIndexResponse` (success status)

#### Migration Messages

1. `ApplyMigrationRequest` (migration definition)
2. `ApplyMigrationResponse` (success, applied version)
3. `RevertMigrationRequest` (target version)
4. `RevertMigrationResponse` (success, reverted to)
5. `MigrationStatusRequest` (empty or version filter)
6. `MigrationStatusResponse` (current version, pending)
7. `ListMigrationsRequest` (status filter)
8. `ListMigrationsResponse` (migration list)

#### Core Types

1. `DatabaseValue` ✅ - Flexible value container
2. `TransactionContext` ✅ - Transaction metadata
3. `QueryOptions` ✅ - Query configuration
4. `DatabaseError` ✅ - Database-specific errors
5. `TableSchema` - Table definition
6. `ColumnDefinition` - Column schema
7. `IndexDefinition` - Index schema
8. `Migration` - Migration definition
9. `IsolationLevel` (enum) - Transaction isolation
10. `DatabaseOperation` (enum) - Operation types

---

## 4. Cache Module

**File**: `pkg/cache/proto/cache.proto` **Package**: `gcommon.cache.v1`

### Services Required

#### CacheService

1. `Get(CacheGetRequest) → CacheGetResponse`
2. `Set(CacheSetRequest) → CacheSetResponse`
3. `Delete(CacheDeleteRequest) → CacheDeleteResponse`
4. `Clear(CacheClearRequest) → CacheClearResponse`
5. `Exists(CacheExistsRequest) → CacheExistsResponse`
6. `TTL(CacheTTLRequest) → CacheTTLResponse`
7. `Expire(CacheExpireRequest) → CacheExpireResponse`
8. `BatchGet(CacheBatchGetRequest) → CacheBatchGetResponse`
9. `BatchSet(CacheBatchSetRequest) → CacheBatchSetResponse`
10. `BatchDelete(CacheBatchDeleteRequest) → CacheBatchDeleteResponse`
11. `ListKeys(CacheListRequest) → CacheListResponse`
12. `GetStats(CacheStatsRequest) → CacheStatsResponse`
13. `FlushAll(CacheFlushRequest) → CacheFlushResponse`

#### CacheManagementService

1. `CreateCache(CreateCacheRequest) → CreateCacheResponse`
2. `DeleteCache(DeleteCacheRequest) → DeleteCacheResponse`
3. `ListCaches(ListCachesRequest) → ListCachesResponse`
4. `GetCacheInfo(CacheInfoRequest) → CacheInfoResponse`
5. `UpdateCacheConfig(UpdateCacheConfigRequest) → UpdateCacheConfigResponse`

### Messages Required

#### Core Operation Messages

1. `CacheGetRequest` ✅ (key, cache name)
2. `CacheGetResponse` ✅ (value, found, TTL)
3. `CacheSetRequest` ✅ (key, value, TTL, cache name)
4. `CacheSetResponse` ✅ (success status)
5. `CacheDeleteRequest` ✅ (key, cache name)
6. `CacheDeleteResponse` ✅ (success, found)
7. `CacheClearRequest` ✅ (cache name, pattern)
8. `CacheClearResponse` ✅ (cleared count)
9. `CacheExistsRequest` (key, cache name)
10. `CacheExistsResponse` (exists)
11. `CacheTTLRequest` (key, cache name)
12. `CacheTTLResponse` (TTL, exists)
13. `CacheExpireRequest` (key, TTL, cache name)
14. `CacheExpireResponse` (success)

#### Batch Operation Messages

1. `CacheBatchGetRequest` (keys list, cache name)
2. `CacheBatchGetResponse` (values map, found keys)
3. `CacheBatchSetRequest` (key-value pairs, TTL, cache name)
4. `CacheBatchSetResponse` (success count, failed keys)
5. `CacheBatchDeleteRequest` (keys list, cache name)
6. `CacheBatchDeleteResponse` (deleted count, failed keys)

#### Management Messages

1. `CacheListRequest` ✅ (cache name, pattern, pagination)
2. `CacheListResponse` ✅ (keys, pagination)
3. `CacheStatsRequest` ✅ (cache name)
4. `CacheStatsResponse` ✅ (statistics)
5. `CacheFlushRequest` (cache name)
6. `CacheFlushResponse` (success)
7. `CreateCacheRequest` (cache config)
8. `CreateCacheResponse` (success, cache info)
9. `DeleteCacheRequest` (cache name)
10. `DeleteCacheResponse` (success)
11. `ListCachesRequest` (filter, pagination)
12. `ListCachesResponse` (cache list, pagination)
13. `CacheInfoRequest` (cache name)
14. `CacheInfoResponse` (cache configuration, stats)
15. `UpdateCacheConfigRequest` (cache name, new config)
16. `UpdateCacheConfigResponse` (success)

#### Core Types

1. `CacheValue` ✅ - Value with TTL and metadata
2. `CacheStats` ✅ - Cache statistics
3. `CachePolicy` ✅ - Cache policies and settings
4. `CacheConfig` - Cache configuration
5. `CacheInfo` - Cache information and metadata
6. `EvictionPolicy` (enum) - Eviction strategies
7. `CacheType` (enum) - Cache backend types

---

## 5. Configuration Module

**File**: `pkg/config/proto/config.proto` **Package**: `gcommon.config.v1`

### Services Required

#### ConfigService

1. `GetConfig(ConfigRequest) → ConfigResponse`
2. `SetConfig(SetConfigRequest) → SetConfigResponse`
3. `DeleteConfig(DeleteConfigRequest) → DeleteConfigResponse`
4. `ListConfigs(ListConfigRequest) → ListConfigResponse`
5. `WatchConfig(WatchConfigRequest) → stream ConfigChangeEvent`
6. `ValidateConfig(ValidateConfigRequest) → ValidateConfigResponse`
7. `GetConfigHistory(ConfigHistoryRequest) → ConfigHistoryResponse`
8. `ReloadConfig(ReloadConfigRequest) → ReloadConfigResponse`

#### ConfigSchemaService

1. `RegisterSchema(RegisterSchemaRequest) → RegisterSchemaResponse`
2. `GetSchema(GetSchemaRequest) → GetSchemaResponse`
3. `UpdateSchema(UpdateSchemaRequest) → UpdateSchemaResponse`
4. `DeleteSchema(DeleteSchemaRequest) → DeleteSchemaResponse`
5. `ListSchemas(ListSchemasRequest) → ListSchemasResponse`

### Messages Required

#### Core Operation Messages

1. `ConfigRequest` ✅ (key, environment, version)
2. `ConfigResponse` ✅ (value, metadata, found)
3. `SetConfigRequest` ✅ (key, value, metadata)
4. `SetConfigResponse` ✅ (success, version)
5. `DeleteConfigRequest` ✅ (key, environment)
6. `DeleteConfigResponse` ✅ (success, found)
7. `ListConfigRequest` ✅ (prefix, environment, pagination)
8. `ListConfigResponse` ✅ (configs, pagination)
9. `WatchConfigRequest` ✅ (key pattern, environment)
10. `ConfigChangeEvent` ✅ (key, old/new values, change type)
11. `ValidateConfigRequest` ✅ (key, value, schema)
12. `ValidateConfigResponse` ✅ (valid, errors)
13. `ConfigHistoryRequest` (key, time range)
14. `ConfigHistoryResponse` (history entries)
15. `ReloadConfigRequest` (source filter)
16. `ReloadConfigResponse` (reloaded count, errors)

#### Schema Messages

1. `RegisterSchemaRequest` (schema definition)
2. `RegisterSchemaResponse` (success, schema ID)
3. `GetSchemaRequest` (schema ID or key pattern)
4. `GetSchemaResponse` (schema definition)
5. `UpdateSchemaRequest` (schema ID, new definition)
6. `UpdateSchemaResponse` (success)
7. `DeleteSchemaRequest` (schema ID)
8. `DeleteSchemaResponse` (success)
9. `ListSchemasRequest` (filter, pagination)
10. `ListSchemasResponse` (schemas, pagination)

#### Core Types

1. `ConfigValue` ✅ - Configuration with validation
2. `ConfigChangeEvent` ✅ - Change notifications
3. `ConfigValidation` ✅ - Schema validation
4. `ConfigSource` ✅ - Source tracking
5. `ConfigSchema` - Schema definition
6. `ConfigHistory` - Historical change record
7. `ConfigMetadata` - Configuration metadata
8. `ChangeType` (enum) - Types of changes
9. `ConfigEnvironment` (enum) - Environment types
10. `ValidationRule` - Validation rules

---

## 6. Logging Module

**File**: `pkg/log/proto/log.proto` **Package**: `gcommon.log.v1`

### Services Required

#### LogService

1. `WriteLog(LogRequest) → LogResponse`
2. `WriteBatchLogs(BatchLogRequest) → BatchLogResponse`
3. `GetLogs(GetLogsRequest) → GetLogsResponse`
4. `StreamLogs(StreamLogsRequest) → stream LogEntry`
5. `SetLogLevel(SetLogLevelRequest) → SetLogLevelResponse`
6. `GetLogLevel(GetLogLevelRequest) → GetLogLevelResponse`
7. `SearchLogs(SearchLogsRequest) → SearchLogsResponse`
8. `GetLogStats(LogStatsRequest) → LogStatsResponse`

#### LogManagementService

1. `CreateLogger(CreateLoggerRequest) → CreateLoggerResponse`
2. `UpdateLogger(UpdateLoggerRequest) → UpdateLoggerResponse`
3. `DeleteLogger(DeleteLoggerRequest) → DeleteLoggerResponse`
4. `ListLoggers(ListLoggersRequest) → ListLoggersResponse`
5. `GetLoggerConfig(LoggerConfigRequest) → LoggerConfigResponse`

### Messages Required

#### Core Operation Messages

1. `LogRequest` ✅ (entry, logger name)
2. `LogResponse` ✅ (success, entry ID)
3. `BatchLogRequest` (entries list, logger name)
4. `BatchLogResponse` (success count, failed entries)
5. `GetLogsRequest` ✅ (filter, time range, pagination)
6. `GetLogsResponse` ✅ (entries, pagination)
7. `StreamLogsRequest` ✅ (filter, follow mode)
8. `LogEntry` ✅ - Structured log entry
9. `SetLogLevelRequest` ✅ (logger, level)
10. `SetLogLevelResponse` ✅ (success)
11. `GetLogLevelRequest` ✅ (logger name)
12. `GetLogLevelResponse` ✅ (current level)
13. `SearchLogsRequest` (query, time range, pagination)
14. `SearchLogsResponse` (matching entries, pagination)
15. `LogStatsRequest` (time range, grouping)
16. `LogStatsResponse` (statistics)

#### Management Messages

1. `CreateLoggerRequest` (logger config)
2. `CreateLoggerResponse` (success, logger info)
3. `UpdateLoggerRequest` (logger name, new config)
4. `UpdateLoggerResponse` (success)
5. `DeleteLoggerRequest` (logger name)
6. `DeleteLoggerResponse` (success)
7. `ListLoggersRequest` (filter, pagination)
8. `ListLoggersResponse` (logger list, pagination)
9. `LoggerConfigRequest` (logger name)
10. `LoggerConfigResponse` (configuration)

#### Core Types

1. `LogEntry` ✅ - Structured log with fields
2. `LogFilter` ✅ - Filtering criteria
3. `LogLevel` (enum) ✅ - Log levels
4. `LogMetadata` ✅ - Context information
5. `LoggerConfig` - Logger configuration
6. `LogStats` - Log statistics
7. `LogFormat` (enum) - Output formats
8. `LogOutput` (enum) - Output destinations

---

## 7. Metrics Module

**File**: `pkg/metrics/proto/metrics.proto` **Package**: `gcommon.metrics.v1`

### Services Required

#### MetricsService

1. `RecordMetric(MetricRequest) → MetricResponse`
2. `RecordBatchMetrics(BatchMetricRequest) → BatchMetricResponse`
3. `GetMetrics(GetMetricsRequest) → GetMetricsResponse`
4. `StreamMetrics(StreamMetricsRequest) → stream MetricData`
5. `RegisterMetric(RegisterMetricRequest) → RegisterMetricResponse`
6. `UnregisterMetric(UnregisterMetricRequest) → UnregisterMetricResponse`
7. `GetMetricMetadata(MetricMetadataRequest) → MetricMetadataResponse`
8. `QueryMetrics(QueryMetricsRequest) → QueryMetricsResponse`

#### MetricsManagementService

1. `CreateMetricsProvider(CreateProviderRequest) → CreateProviderResponse`
2. `UpdateMetricsProvider(UpdateProviderRequest) → UpdateProviderResponse`
3. `DeleteMetricsProvider(DeleteProviderRequest) → DeleteProviderResponse`
4. `ListMetricsProviders(ListProvidersRequest) → ListProvidersResponse`
5. `GetProviderStats(ProviderStatsRequest) → ProviderStatsResponse`

### Messages Required

#### Core Operation Messages

1. `MetricRequest` ✅ (metric data, provider)
2. `MetricResponse` ✅ (success status)
3. `BatchMetricRequest` (metrics list, provider)
4. `BatchMetricResponse` (success count, failed metrics)
5. `GetMetricsRequest` ✅ (filter, time range, aggregation)
6. `GetMetricsResponse` ✅ (metrics data, metadata)
7. `StreamMetricsRequest` ✅ (filter, real-time mode)
8. `MetricData` ✅ - Individual metric point
9. `RegisterMetricRequest` ✅ (metric definition)
10. `RegisterMetricResponse` ✅ (success, metric ID)
11. `UnregisterMetricRequest` (metric ID/name)
12. `UnregisterMetricResponse` (success)
13. `MetricMetadataRequest` ✅ (metric ID/name)
14. `MetricMetadataResponse` ✅ (metadata, definition)
15. `QueryMetricsRequest` (PromQL/query, time range)
16. `QueryMetricsResponse` (query results)

#### Management Messages

1. `CreateProviderRequest` (provider config)
2. `CreateProviderResponse` (success, provider info)
3. `UpdateProviderRequest` (provider ID, new config)
4. `UpdateProviderResponse` (success)
5. `DeleteProviderRequest` (provider ID)
6. `DeleteProviderResponse` (success)
7. `ListProvidersRequest` (filter, pagination)
8. `ListProvidersResponse` (provider list, pagination)
9. `ProviderStatsRequest` (provider ID)
10. `ProviderStatsResponse` (statistics)

#### Core Types

1. `MetricData` ✅ - Metric with labels and timestamp
2. `MetricType` (enum) ✅ - Counter, gauge, histogram, etc.
3. `MetricFilter` ✅ - Filtering by name/labels/time
4. `MetricAggregation` ✅ - Aggregation functions
5. `MetricDefinition` - Metric schema definition
6. `MetricProvider` - Provider configuration
7. `MetricStats` - Provider statistics
8. `AggregationFunction` (enum) - Sum, avg, max, etc.
9. `MetricUnit` (enum) - Units of measurement

---

## 8. Queue Module

**File**: `pkg/queue/proto/queue.proto` **Package**: `gcommon.queue.v1`

### Services Required

#### QueueService

1. `Publish(PublishRequest) → PublishResponse`
2. `BatchPublish(BatchPublishRequest) → BatchPublishResponse`
3. `Subscribe(SubscribeRequest) → stream QueueMessage`
4. `Acknowledge(AckRequest) → AckResponse`
5. `Reject(RejectRequest) → RejectResponse`
6. `GetMessage(GetMessageRequest) → GetMessageResponse`
7. `GetQueueInfo(QueueInfoRequest) → QueueInfoResponse`
8. `GetQueueStats(QueueStatsRequest) → QueueStatsResponse`
9. `PurgeQueue(PurgeQueueRequest) → PurgeQueueResponse`

#### QueueManagementService

1. `CreateQueue(CreateQueueRequest) → CreateQueueResponse`
2. `UpdateQueue(UpdateQueueRequest) → UpdateQueueResponse`
3. `DeleteQueue(DeleteQueueRequest) → DeleteQueueResponse`
4. `ListQueues(ListQueuesRequest) → ListQueuesResponse`
5. `PauseQueue(PauseQueueRequest) → PauseQueueResponse`
6. `ResumeQueue(ResumeQueueRequest) → ResumeQueueResponse`

### Messages Required

#### Core Operation Messages

1. `PublishRequest` ✅ (message, queue, options)
2. `PublishResponse` ✅ (success, message ID)
3. `BatchPublishRequest` ✅ (messages list, queue)
4. `BatchPublishResponse` ✅ (success count, failed messages)
5. `SubscribeRequest` (queue, consumer config)
6. `QueueMessage` ✅ - Message with headers and metadata
7. `AckRequest` ✅ (message ID, consumer)
8. `AckResponse` ✅ (success)
9. `RejectRequest` (message ID, consumer, requeue)
10. `RejectResponse` (success)
11. `GetMessageRequest` (queue, consumer options)
12. `GetMessageResponse` (message, available)
13. `QueueInfoRequest` ✅ (queue name)
14. `QueueInfoResponse` ✅ (queue configuration, status)
15. `QueueStatsRequest` ✅ (queue name, time range)
16. `QueueStatsResponse` ✅ (statistics)
17. `PurgeQueueRequest` (queue name, filter)
18. `PurgeQueueResponse` (purged count)

#### Management Messages

1. `CreateQueueRequest` ✅ (queue config)
2. `CreateQueueResponse` ✅ (success, queue info)
3. `UpdateQueueRequest` (queue name, new config)
4. `UpdateQueueResponse` (success)
5. `DeleteQueueRequest` ✅ (queue name, force)
6. `DeleteQueueResponse` ✅ (success)
7. `ListQueuesRequest` (filter, pagination)
8. `ListQueuesResponse` (queue list, pagination)
9. `PauseQueueRequest` (queue name)
10. `PauseQueueResponse` (success)
11. `ResumeQueueRequest` (queue name)
12. `ResumeQueueResponse` (success)

#### Core Types

1. `QueueMessage` ✅ - Message with metadata
2. `QueueConfig` ✅ - Queue configuration
3. `DeliveryOptions` ✅ - Delivery settings
4. `QueueStats` ✅ - Queue statistics
5. `ConsumerConfig` - Consumer configuration
6. `MessageFilter` - Message filtering
7. `QueueStatus` (enum) - Queue state
8. `DeliveryMode` (enum) - Delivery guarantees
9. `AckMode` (enum) - Acknowledgment modes

---

## 9. Web Module

**File**: `pkg/web/proto/web.proto` **Package**: `gcommon.web.v1`

### Services Required

#### WebService

1. `HandleRequest(WebRequest) → WebResponse`
2. `RegisterHandler(RegisterHandlerRequest) → RegisterHandlerResponse`
3. `UnregisterHandler(UnregisterHandlerRequest) → UnregisterHandlerResponse`
4. `GetServerInfo(ServerInfoRequest) → ServerInfoResponse`
5. `GetServerStats(ServerStatsRequest) → ServerStatsResponse`
6. `CheckSecurity(SecurityCheckRequest) → SecurityCheckResponse`
7. `GetMetrics(WebMetricsRequest) → WebMetricsResponse`

#### MiddlewareService

1. `RegisterMiddleware(RegisterMiddlewareRequest) → RegisterMiddlewareResponse`
2. `UnregisterMiddleware(UnregisterMiddlewareRequest) → UnregisterMiddlewareResponse`
3. `ListMiddleware(ListMiddlewareRequest) → ListMiddlewareResponse`
4. `UpdateMiddleware(UpdateMiddlewareRequest) → UpdateMiddlewareResponse`

#### WebSocketService

1. `Connect(WebSocketConnectRequest) → stream WebSocketMessage`
2. `Send(WebSocketSendRequest) → WebSocketSendResponse`
3. `Broadcast(WebSocketBroadcastRequest) → WebSocketBroadcastResponse`
4. `GetConnections(WebSocketConnectionsRequest) → WebSocketConnectionsResponse`

### Messages Required

#### Core Operation Messages

1. `WebRequest` ✅ - HTTP request abstraction
2. `WebResponse` ✅ - HTTP response with headers
3. `RegisterHandlerRequest` ✅ (route, handler config)
4. `RegisterHandlerResponse` ✅ (success, handler ID)
5. `UnregisterHandlerRequest` (handler ID or route)
6. `UnregisterHandlerResponse` (success)
7. `ServerInfoRequest` ✅ (include stats)
8. `ServerInfoResponse` ✅ (server configuration, status)
9. `ServerStatsRequest` (time range, metric types)
10. `ServerStatsResponse` (server statistics)
11. `SecurityCheckRequest` ✅ (request context, checks)
12. `SecurityCheckResponse` ✅ (passed, violations)
13. `WebMetricsRequest` ✅ (time range, metric filter)
14. `WebMetricsResponse` ✅ (metrics data)

#### Middleware Messages

1. `RegisterMiddlewareRequest` (middleware config, priority)
2. `RegisterMiddlewareResponse` (success, middleware ID)
3. `UnregisterMiddlewareRequest` (middleware ID)
4. `UnregisterMiddlewareResponse` (success)
5. `ListMiddlewareRequest` (filter, pagination)
6. `ListMiddlewareResponse` (middleware list, pagination)
7. `UpdateMiddlewareRequest` (middleware ID, new config)
8. `UpdateMiddlewareResponse` (success)

#### WebSocket Messages

1. `WebSocketConnectRequest` (connection config, auth)
2. `WebSocketMessage` (message data, connection ID)
3. `WebSocketSendRequest` (connection ID, message)
4. `WebSocketSendResponse` (success)
5. `WebSocketBroadcastRequest` (message, room filter)
6. `WebSocketBroadcastResponse` (sent count)
7. `WebSocketConnectionsRequest` (filter, pagination)
8. `WebSocketConnectionsResponse` (connections, pagination)

#### Core Types

1. `WebRequest` ✅ - HTTP request representation
2. `WebResponse` ✅ - HTTP response with metadata
3. `SecurityCheck` ✅ - Security validation
4. `HandlerConfig` ✅ - Route configuration
5. `MiddlewareConfig` - Middleware configuration
6. `WebSocketConnection` - WebSocket connection info
7. `ServerConfig` - Server configuration
8. `ServerStats` - Server statistics
9. `HTTPMethod` (enum) - HTTP methods
10. `SecurityViolation` (enum) - Security violation types

---

## Summary Statistics

### Total Services Required: **18 Services**

1. HealthService
2. AuthService
3. AuthorizationService
4. SessionService
5. DatabaseService
6. TransactionService
7. SchemaService
8. MigrationService
9. CacheService
10. CacheManagementService
11. ConfigService
12. ConfigSchemaService
13. LogService
14. LogManagementService
15. MetricsService
16. MetricsManagementService
17. QueueService
18. QueueManagementService
19. WebService
20. MiddlewareService
21. WebSocketService

### Total Messages Required: **400+ Messages**

- **Common Types**: ~25 messages (base foundation)
- **Health Module**: ~25 messages
- **Auth Module**: ~60 messages (most complex due to 3 services)
- **Database Module**: ~50 messages (4 services)
- **Cache Module**: ~35 messages
- **Config Module**: ~30 messages
- **Logging Module**: ~30 messages
- **Metrics Module**: ~35 messages
- **Queue Module**: ~30 messages
- **Web Module**: ~40 messages

### Implementation Priority

1. **Phase 1** (Foundation): Common types, Health, Auth basics
2. **Phase 2** (Core Services): Database, Cache, Config, Logging
3. **Phase 3** (Advanced): Metrics, Queue, Web services
4. **Phase 4** (Management): All management services and advanced features

This represents a **complete mapping** of all protobuf services and messages
needed to achieve 100% functionality across all GCommon modules.
