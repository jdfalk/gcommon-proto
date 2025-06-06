#!/bin/bash
# file: create_all_protos.sh


# Base directory
BASE_DIR="/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg"

# Create all proto files for GCommon modules

# 1. Auth proto (comprehensive authentication and authorization)
cat > "${BASE_DIR}/auth/proto/auth.proto" << 'AUTH_PROTO'
// file: pkg/auth/proto/auth.proto
edition = "2023";

package gcommon.v1.auth;

import "pkg/common/proto/common.proto";
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/field_mask.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/auth/proto;authpb";
option features.(pb.go).api_level = API_HYBRID;

// AuthService provides comprehensive authentication capabilities
service AuthService {
  // Authenticate a user with various credential types
  rpc Authenticate(AuthenticateRequest) returns (AuthenticateResponse);

  // Verify user credentials without issuing tokens
  rpc VerifyCredentials(VerifyCredentialsRequest) returns (VerifyCredentialsResponse);

  // Validate an access token
  rpc ValidateToken(ValidateTokenRequest) returns (ValidateTokenResponse);

  // Refresh an access token using a refresh token
  rpc RefreshToken(RefreshTokenRequest) returns (RefreshTokenResponse);

  // Revoke a token (access or refresh)
  rpc RevokeToken(RevokeTokenRequest) returns (google.protobuf.Empty);

  // Get user information from a valid token
  rpc GetUserInfo(GetUserInfoRequest) returns (GetUserInfoResponse);

  // Initiate password reset flow
  rpc InitiatePasswordReset(InitiatePasswordResetRequest) returns (InitiatePasswordResetResponse);

  // Complete password reset with token
  rpc CompletePasswordReset(CompletePasswordResetRequest) returns (google.protobuf.Empty);

  // Change user password (authenticated)
  rpc ChangePassword(ChangePasswordRequest) returns (google.protobuf.Empty);
}

// AuthorizationService provides authorization and permission management
service AuthorizationService {
  // Check if a user is authorized for a specific action
  rpc Authorize(AuthorizeRequest) returns (AuthorizeResponse);

  // Get all permissions for a user
  rpc GetUserPermissions(GetUserPermissionsRequest) returns (GetUserPermissionsResponse);

  // Get user roles
  rpc GetUserRoles(GetUserRolesRequest) returns (GetUserRolesResponse);

  // Assign role to user
  rpc AssignRole(AssignRoleRequest) returns (google.protobuf.Empty);

  // Remove role from user
  rpc RemoveRole(RemoveRoleRequest) returns (google.protobuf.Empty);

  // Create a new role
  rpc CreateRole(CreateRoleRequest) returns (Role);

  // Update an existing role
  rpc UpdateRole(UpdateRoleRequest) returns (Role);

  // Delete a role
  rpc DeleteRole(DeleteRoleRequest) returns (google.protobuf.Empty);

  // List roles with filtering and pagination
  rpc ListRoles(ListRolesRequest) returns (ListRolesResponse);
}

// SessionService manages user sessions
service SessionService {
  // Create a new session
  rpc CreateSession(CreateSessionRequest) returns (Session);

  // Get session information
  rpc GetSession(GetSessionRequest) returns (Session);

  // Update session (e.g., refresh activity)
  rpc UpdateSession(UpdateSessionRequest) returns (Session);

  // Terminate a session
  rpc TerminateSession(TerminateSessionRequest) returns (google.protobuf.Empty);

  // List user sessions
  rpc ListUserSessions(ListUserSessionsRequest) returns (ListUserSessionsResponse);

  // Validate session token
  rpc ValidateSession(ValidateSessionRequest) returns (ValidateSessionResponse);
}

// Authentication request with multiple credential types
message AuthenticateRequest {
  // Request metadata for tracing and correlation
  gcommon.common.v1.RequestMetadata metadata = 1;

  // Authentication credentials (oneof ensures only one type is used)
  oneof credentials {
    // Username/password authentication
    PasswordCredentials password = 2;
    // API key authentication
    APIKeyCredentials api_key = 3;
    // OAuth2 authorization code
    OAuth2Credentials oauth2 = 4;
    // JWT bearer token
    JWTCredentials jwt = 5;
  }

  // Requested scopes
  repeated string scopes = 6;

  // Client information
  gcommon.common.v1.ClientInfo client_info = 7;
}

// Username/password credentials
message PasswordCredentials {
  // Username or email
  string username = 1;
  // Password
  string password = 2;
  // Remember me option for extended session
  bool remember_me = 3;
}

// API key credentials
message APIKeyCredentials {
  // API key value
  string key = 1;
  // API key ID (optional)
  string key_id = 2;
}

// OAuth2 credentials
message OAuth2Credentials {
  // Authorization code
  string code = 1;
  // Redirect URI used in authorization request
  string redirect_uri = 2;
  // Client ID
  string client_id = 3;
  // Client secret (for confidential clients)
  string client_secret = 4;
}

// JWT credentials
message JWTCredentials {
  // JWT token
  string token = 1;
  // Issuer (optional validation)
  string issuer = 2;
}

// Authentication response
message AuthenticateResponse {
  // Access token for API access
  string access_token = 1;
  // Refresh token for token renewal
  string refresh_token = 2;
  // Token type (always "Bearer")
  string token_type = 3;
  // Token expiration time in seconds
  int32 expires_in = 4;
  // Granted scopes
  repeated string scopes = 5;
  // User information
  UserInfo user_info = 6;
  // Session information
  Session session = 7;
  // Rate limit information
  gcommon.common.v1.RateLimit rate_limit = 8;
}

// User information
message UserInfo {
  // Unique user identifier
  string id = 1;
  // Username
  string username = 2;
  // Email address
  string email = 3;
  // Display name
  string display_name = 4;
  // User roles
  repeated string roles = 5;
  // Direct permissions
  repeated string permissions = 6;
  // User attributes/metadata
  map<string, string> attributes = 7;
  // Account creation timestamp
  google.protobuf.Timestamp created_at = 8;
  // Last login timestamp
  google.protobuf.Timestamp last_login_at = 9;
  // Account status
  UserStatus status = 10;
  // Email verification status
  bool email_verified = 11;
}

// User account status enumeration
enum UserStatus {
  USER_STATUS_UNSPECIFIED = 0;
  USER_STATUS_ACTIVE = 1;
  USER_STATUS_INACTIVE = 2;
  USER_STATUS_SUSPENDED = 3;
  USER_STATUS_PENDING_VERIFICATION = 4;
  USER_STATUS_LOCKED = 5;
  USER_STATUS_DELETED = 6;
}

// Session information
message Session {
  // Unique session identifier
  string id = 1;
  // User ID associated with the session
  string user_id = 2;
  // Session creation timestamp
  google.protobuf.Timestamp created_at = 3;
  // Last activity timestamp
  google.protobuf.Timestamp last_activity_at = 4;
  // Session expiration timestamp
  google.protobuf.Timestamp expires_at = 5;
  // Client information
  gcommon.common.v1.ClientInfo client_info = 6;
  // Session status
  SessionStatus status = 7;
  // Session metadata
  map<string, string> metadata = 8;
  // IP address when session was created
  string ip_address = 9;
  // User agent when session was created
  string user_agent = 10;
}

// Session status enumeration
enum SessionStatus {
  SESSION_STATUS_UNSPECIFIED = 0;
  SESSION_STATUS_ACTIVE = 1;
  SESSION_STATUS_EXPIRED = 2;
  SESSION_STATUS_TERMINATED = 3;
  SESSION_STATUS_INVALID = 4;
}

// Role definition
message Role {
  // Unique role identifier
  string id = 1;
  // Role name
  string name = 2;
  // Role description
  string description = 3;
  // Permissions granted by this role
  repeated string permissions = 4;
  // Role metadata
  map<string, string> metadata = 5;
  // Role creation timestamp
  google.protobuf.Timestamp created_at = 6;
  // Role status
  gcommon.common.v1.ResourceStatus status = 7;
}

// Additional request/response messages (abbreviated for space)
message VerifyCredentialsRequest {
  gcommon.common.v1.RequestMetadata metadata = 1;
  oneof credentials {
    PasswordCredentials password = 2;
    APIKeyCredentials api_key = 3;
  }
}

message VerifyCredentialsResponse {
  bool verified = 1;
  UserInfo user_info = 2;
  gcommon.common.v1.Error error = 3;
}

message ValidateTokenRequest {
  string token = 1;
  repeated string required_scopes = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message ValidateTokenResponse {
  bool valid = 1;
  string subject = 2;
  repeated string scopes = 3;
  google.protobuf.Timestamp expires_at = 4;
  UserInfo user_info = 5;
  gcommon.common.v1.Error error = 6;
}

message RefreshTokenRequest {
  string refresh_token = 1;
  repeated string scopes = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message RefreshTokenResponse {
  string access_token = 1;
  string refresh_token = 2;
  string token_type = 3;
  int32 expires_in = 4;
  repeated string scopes = 5;
}

message RevokeTokenRequest {
  string token = 1;
  string token_type_hint = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message GetUserInfoRequest {
  string token = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetUserInfoResponse {
  UserInfo user_info = 1;
  map<string, string> attributes = 2;
}

message AuthorizeRequest {
  string token = 1;
  string resource = 2;
  string action = 3;
  map<string, string> context = 4;
  gcommon.common.v1.RequestMetadata metadata = 5;
}

message AuthorizeResponse {
  bool authorized = 1;
  repeated string permissions = 2;
  string denial_reason = 3;
  gcommon.common.v1.Error error = 4;
}

message InitiatePasswordResetRequest {
  string identifier = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message InitiatePasswordResetResponse {
  string reset_token = 1;
  google.protobuf.Timestamp expires_at = 2;
  string message = 3;
}

message CompletePasswordResetRequest {
  string reset_token = 1;
  string new_password = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message ChangePasswordRequest {
  string current_password = 1;
  string new_password = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message GetUserPermissionsRequest {
  string user_id = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetUserPermissionsResponse {
  repeated string permissions = 1;
  repeated string role_permissions = 2;
  repeated string effective_permissions = 3;
  repeated Role roles = 4;
}

message GetUserRolesRequest {
  string user_id = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetUserRolesResponse {
  repeated Role roles = 1;
}

message AssignRoleRequest {
  string user_id = 1;
  string role_id = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message RemoveRoleRequest {
  string user_id = 1;
  string role_id = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message CreateRoleRequest {
  Role role = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message UpdateRoleRequest {
  Role role = 1;
  google.protobuf.FieldMask update_mask = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message DeleteRoleRequest {
  string role_id = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ListRolesRequest {
  gcommon.common.v1.Pagination pagination = 1;
  gcommon.common.v1.FilterOptions filter = 2;
  gcommon.common.v1.SortOptions sort = 3;
  gcommon.common.v1.RequestMetadata metadata = 4;
}

message ListRolesResponse {
  repeated Role roles = 1;
  gcommon.common.v1.PaginatedResponse pagination = 2;
}

message CreateSessionRequest {
  string user_id = 1;
  gcommon.common.v1.ClientInfo client_info = 2;
  repeated string scopes = 3;
  map<string, string> metadata = 4;
  bool remember_me = 5;
  gcommon.common.v1.RequestMetadata request_metadata = 6;
}

message GetSessionRequest {
  string session_id = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message UpdateSessionRequest {
  Session session = 1;
  google.protobuf.FieldMask update_mask = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message TerminateSessionRequest {
  string session_id = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ListUserSessionsRequest {
  string user_id = 1;
  gcommon.common.v1.Pagination pagination = 2;
  gcommon.common.v1.FilterOptions filter = 3;
  gcommon.common.v1.RequestMetadata metadata = 4;
}

message ListUserSessionsResponse {
  repeated Session sessions = 1;
  gcommon.common.v1.PaginatedResponse pagination = 2;
}

message ValidateSessionRequest {
  string session_token = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ValidateSessionResponse {
  bool valid = 1;
  Session session = 2;
  UserInfo user_info = 3;
  gcommon.common.v1.Error error = 4;
}
AUTH_PROTO

echo "Created auth.proto"

# 2. Cache proto (comprehensive caching operations)
cat > "${BASE_DIR}/cache/proto/cache.proto" << 'CACHE_PROTO'
// file: pkg/cache/proto/cache.proto
edition = "2023";

package gcommon.v1.cache;

import "pkg/common/proto/common.proto";
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/any.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto;cachepb";
option features.(pb.go).api_level = API_HYBRID;

// CacheService provides comprehensive caching capabilities
service CacheService {
  // Get retrieves a value from the cache
  rpc Get(GetRequest) returns (GetResponse);

  // Set stores a value in the cache
  rpc Set(SetRequest) returns (SetResponse);

  // Delete removes a value from the cache
  rpc Delete(DeleteRequest) returns (DeleteResponse);

  // Exists checks if a key exists in the cache
  rpc Exists(ExistsRequest) returns (ExistsResponse);

  // GetMultiple retrieves multiple values from the cache
  rpc GetMultiple(GetMultipleRequest) returns (GetMultipleResponse);

  // SetMultiple stores multiple values in the cache
  rpc SetMultiple(SetMultipleRequest) returns (SetMultipleResponse);

  // DeleteMultiple removes multiple values from the cache
  rpc DeleteMultiple(DeleteMultipleRequest) returns (DeleteMultipleResponse);

  // Increment atomically increments a numeric value
  rpc Increment(IncrementRequest) returns (IncrementResponse);

  // Decrement atomically decrements a numeric value
  rpc Decrement(DecrementRequest) returns (DecrementResponse);

  // Clear removes all entries from the cache or by pattern
  rpc Clear(ClearRequest) returns (ClearResponse);

  // Keys returns all keys matching a pattern
  rpc Keys(KeysRequest) returns (KeysResponse);

  // GetStats returns cache statistics and metrics
  rpc GetStats(GetStatsRequest) returns (GetStatsResponse);

  // Flush forces cache persistence if supported
  rpc Flush(FlushRequest) returns (FlushResponse);

  // TouchExpiration updates the expiration time of a key
  rpc TouchExpiration(TouchExpirationRequest) returns (TouchExpirationResponse);
}

// Cache management service for administrative operations
service CacheAdminService {
  // CreateNamespace creates a new cache namespace
  rpc CreateNamespace(CreateNamespaceRequest) returns (CreateNamespaceResponse);

  // DeleteNamespace removes a cache namespace
  rpc DeleteNamespace(DeleteNamespaceRequest) returns (google.protobuf.Empty);

  // ListNamespaces returns all available namespaces
  rpc ListNamespaces(ListNamespacesRequest) returns (ListNamespacesResponse);

  // GetNamespaceStats returns statistics for a namespace
  rpc GetNamespaceStats(GetNamespaceStatsRequest) returns (GetNamespaceStatsResponse);

  // ConfigurePolicy sets cache policies for a namespace
  rpc ConfigurePolicy(ConfigurePolicyRequest) returns (ConfigurePolicyResponse);
}

// Get request for retrieving a cached value
message GetRequest {
  // Cache key
  string key = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;

  // Whether to update access time (for LRU policies)
  bool update_access_time = 4;
}

// Get response containing cached value
message GetResponse {
  // The cached value
  CacheEntry entry = 1;

  // Whether the key was found
  bool found = 2;

  // Error information if retrieval failed
  gcommon.common.v1.Error error = 3;
}

// Set request for storing a value in cache
message SetRequest {
  // Cache key
  string key = 1;

  // Value to store
  google.protobuf.Any value = 2;

  // Time-to-live duration
  google.protobuf.Duration ttl = 3;

  // Optional namespace
  string namespace = 4;

  // Cache entry metadata
  map<string, string> metadata = 5;

  // Tags for categorization and bulk operations
  repeated string tags = 6;

  // Conditional set options
  SetOptions options = 7;

  // Request metadata
  gcommon.common.v1.RequestMetadata request_metadata = 8;
}

// Set response indicating success/failure
message SetResponse {
  // Whether the operation succeeded
  bool success = 1;

  // Previous value if it existed
  CacheEntry previous_entry = 2;

  // Error information if set failed
  gcommon.common.v1.Error error = 3;
}

// Delete request for removing a cached value
message DeleteRequest {
  // Cache key to delete
  string key = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Delete response indicating result
message DeleteResponse {
  // Whether a value was actually deleted
  bool deleted = 1;

  // The deleted entry if it existed
  CacheEntry deleted_entry = 2;

  // Error information if deletion failed
  gcommon.common.v1.Error error = 3;
}

// Cache entry representation
message CacheEntry {
  // The cache key
  string key = 1;

  // The cached value
  google.protobuf.Any value = 2;

  // Entry creation timestamp
  google.protobuf.Timestamp created_at = 3;

  // Entry last access timestamp
  google.protobuf.Timestamp accessed_at = 4;

  // Entry expiration timestamp
  google.protobuf.Timestamp expires_at = 5;

  // Time-to-live duration
  google.protobuf.Duration ttl = 6;

  // Entry metadata
  map<string, string> metadata = 7;

  // Entry tags
  repeated string tags = 8;

  // Access count for LFU policies
  int64 access_count = 9;

  // Entry size in bytes
  int64 size_bytes = 10;

  // Entry namespace
  string namespace = 11;

  // Entry version for optimistic concurrency
  int64 version = 12;
}

// Set operation options
message SetOptions {
  // Only set if key doesn't exist
  bool if_not_exists = 1;

  // Only set if key exists
  bool if_exists = 2;

  // Expected version for optimistic concurrency
  int64 expected_version = 3;

  // Whether to return previous value
  bool return_previous = 4;
}

// Exists request to check key presence
message ExistsRequest {
  // Cache key to check
  string key = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Exists response indicating presence
message ExistsResponse {
  // Whether the key exists
  bool exists = 1;

  // Key expiration information if it exists
  google.protobuf.Timestamp expires_at = 2;
}

// GetMultiple request for batch retrieval
message GetMultipleRequest {
  // Keys to retrieve
  repeated string keys = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// GetMultiple response with batch results
message GetMultipleResponse {
  // Retrieved entries mapped by key
  map<string, CacheEntry> entries = 1;

  // Keys that were not found
  repeated string not_found = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// SetMultiple request for batch storage
message SetMultipleRequest {
  // Key-value pairs to store
  map<string, google.protobuf.Any> items = 1;

  // Common TTL for all items
  google.protobuf.Duration ttl = 2;

  // Optional namespace
  string namespace = 3;

  // Common metadata for all items
  map<string, string> metadata = 4;

  // Common tags for all items
  repeated string tags = 5;

  // Request metadata
  gcommon.common.v1.RequestMetadata request_metadata = 6;
}

// SetMultiple response with batch results
message SetMultipleResponse {
  // Success status for each key
  map<string, bool> results = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// DeleteMultiple request for batch removal
message DeleteMultipleRequest {
  // Keys to delete
  repeated string keys = 1;

  // Optional namespace
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// DeleteMultiple response with batch results
message DeleteMultipleResponse {
  // Deletion status for each key
  map<string, bool> results = 1;

  // Count of actually deleted items
  int64 deleted_count = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Increment request for atomic counter operations
message IncrementRequest {
  // Counter key
  string key = 1;

  // Increment delta (can be negative)
  int64 delta = 2;

  // Initial value if key doesn't exist
  int64 initial_value = 3;

  // TTL for the counter
  google.protobuf.Duration ttl = 4;

  // Optional namespace
  string namespace = 5;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 6;
}

// Increment response with new value
message IncrementResponse {
  // New counter value
  int64 value = 1;

  // Whether the operation succeeded
  bool success = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Decrement request for atomic counter operations
message DecrementRequest {
  // Counter key
  string key = 1;

  // Decrement delta (can be negative)
  int64 delta = 2;

  // Initial value if key doesn't exist
  int64 initial_value = 3;

  // TTL for the counter
  google.protobuf.Duration ttl = 4;

  // Optional namespace
  string namespace = 5;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 6;
}

// Decrement response with new value
message DecrementResponse {
  // New counter value
  int64 value = 1;

  // Whether the operation succeeded
  bool success = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Clear request for bulk deletion
message ClearRequest {
  // Key pattern to match (supports wildcards)
  string pattern = 1;

  // Optional namespace
  string namespace = 2;

  // Optional tags to match
  repeated string tags = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Clear response with deletion count
message ClearResponse {
  // Number of entries deleted
  int64 deleted_count = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Keys request for key listing
message KeysRequest {
  // Key pattern to match (supports wildcards)
  string pattern = 1;

  // Optional namespace
  string namespace = 2;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Keys response with matching keys
message KeysResponse {
  // Matching keys
  repeated string keys = 1;

  // Pagination information
  gcommon.common.v1.PaginatedResponse pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Cache statistics request
message GetStatsRequest {
  // Optional namespace filter
  string namespace = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Cache statistics response
message GetStatsResponse {
  // Cache statistics
  CacheStats stats = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Cache statistics
message CacheStats {
  // Total number of cache hits
  int64 hits = 1;

  // Total number of cache misses
  int64 misses = 2;

  // Current number of entries
  int64 entry_count = 3;

  // Total cache size in bytes
  int64 size_bytes = 4;

  // Number of evictions
  int64 evictions = 5;

  // Number of expirations
  int64 expirations = 6;

  // Hit rate percentage
  double hit_rate = 7;

  // Average get latency in microseconds
  double avg_get_latency_us = 8;

  // Average set latency in microseconds
  double avg_set_latency_us = 9;

  // Memory usage statistics
  MemoryStats memory = 10;

  // Per-namespace statistics
  map<string, NamespaceStats> namespace_stats = 11;
}

// Memory usage statistics
message MemoryStats {
  // Total allocated memory in bytes
  int64 allocated_bytes = 1;

  // Memory in use in bytes
  int64 in_use_bytes = 2;

  // System memory in bytes
  int64 system_bytes = 3;

  // Number of garbage collections
  int64 gc_count = 4;
}

// Per-namespace statistics
message NamespaceStats {
  // Namespace name
  string namespace = 1;

  // Number of entries in namespace
  int64 entry_count = 2;

  // Size in bytes for namespace
  int64 size_bytes = 3;

  // Hits for namespace
  int64 hits = 4;

  // Misses for namespace
  int64 misses = 5;
}

// Flush request for persistence
message FlushRequest {
  // Optional namespace to flush
  string namespace = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Flush response
message FlushResponse {
  // Whether flush succeeded
  bool success = 1;

  // Number of entries flushed
  int64 flushed_count = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Touch expiration request
message TouchExpirationRequest {
  // Key to update
  string key = 1;

  // New TTL duration
  google.protobuf.Duration ttl = 2;

  // Optional namespace
  string namespace = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Touch expiration response
message TouchExpirationResponse {
  // Whether the operation succeeded
  bool success = 1;

  // New expiration timestamp
  google.protobuf.Timestamp expires_at = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Admin service messages
message CreateNamespaceRequest {
  // Namespace name
  string namespace = 1;

  // Namespace configuration
  NamespaceConfig config = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message CreateNamespaceResponse {
  // Created namespace information
  Namespace namespace = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Namespace configuration
message NamespaceConfig {
  // Cache policy for the namespace
  gcommon.common.v1.CachePolicy policy = 1;

  // Maximum size in bytes
  int64 max_size_bytes = 2;

  // Maximum number of entries
  int64 max_entries = 3;

  // Default TTL for entries
  google.protobuf.Duration default_ttl = 4;
}

// Namespace information
message Namespace {
  // Namespace name
  string name = 1;

  // Namespace configuration
  NamespaceConfig config = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3;

  // Current statistics
  NamespaceStats stats = 4;

  // Namespace status
  gcommon.common.v1.ResourceStatus status = 5;
}

message DeleteNamespaceRequest {
  string namespace = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ListNamespacesRequest {
  gcommon.common.v1.Pagination pagination = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ListNamespacesResponse {
  repeated Namespace namespaces = 1;
  gcommon.common.v1.PaginatedResponse pagination = 2;
}

message GetNamespaceStatsRequest {
  string namespace = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetNamespaceStatsResponse {
  NamespaceStats stats = 1;
  gcommon.common.v1.Error error = 2;
}

message ConfigurePolicyRequest {
  string namespace = 1;
  gcommon.common.v1.CachePolicy policy = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message ConfigurePolicyResponse {
  bool success = 1;
  gcommon.common.v1.Error error = 2;
}
CACHE_PROTO

echo "Created cache.proto"

# 3. Config proto (comprehensive configuration management)
cat > "${BASE_DIR}/config/proto/config.proto" << 'CONFIG_PROTO'
// file: pkg/config/proto/config.proto
edition = "2023";

package gcommon.v1.config;

import "pkg/common/proto/common.proto";
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/any.proto";
import "google/protobuf/field_mask.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/config/proto;configpb";
option features.(pb.go).api_level = API_HYBRID;

// ConfigService provides comprehensive configuration management
service ConfigService {
  // Get retrieves a configuration value
  rpc Get(GetConfigRequest) returns (GetConfigResponse);

  // Set stores a configuration value
  rpc Set(SetConfigRequest) returns (SetConfigResponse);

  // Delete removes a configuration value
  rpc Delete(DeleteConfigRequest) returns (google.protobuf.Empty);

  // List configuration keys with optional filtering
  rpc List(ListConfigRequest) returns (ListConfigResponse);

  // Watch for configuration changes
  rpc Watch(WatchConfigRequest) returns (stream WatchConfigResponse);

  // GetMultiple retrieves multiple configuration values
  rpc GetMultiple(GetMultipleConfigRequest) returns (GetMultipleConfigResponse);

  // SetMultiple stores multiple configuration values
  rpc SetMultiple(SetMultipleConfigRequest) returns (SetMultipleConfigResponse);

  // Validate configuration values
  rpc Validate(ValidateConfigRequest) returns (ValidateConfigResponse);

  // GetSchema retrieves configuration schema
  rpc GetSchema(GetSchemaRequest) returns (GetSchemaResponse);
}

// Request metadata for configuration operations
message RequestMetadata {
  // Unique request ID for tracing
  string request_id = 1;

  // Client IP address
  string client_ip = 2;

  // User agent string
  string user_agent = 3;

  // Timestamp of the request
  google.protobuf.Timestamp timestamp = 4;

  // Authenticated user ID (if available)
  string user_id = 5;

  // Session ID (if available)
  string session_id = 6;

  // Additional custom attributes
  map<string, string> attributes = 7;
}

// Configuration value request
message GetConfigRequest {
  // Configuration key
  string key = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;

  // Whether to decrypt encrypted values
  bool decrypt = 4;
}

// Configuration value response
message GetConfigResponse {
  // Configuration entry
  ConfigEntry entry = 1;

  // Whether the key was found
  bool found = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Set configuration request
message SetConfigRequest {
  // Configuration key
  string key = 1;

  // Configuration value
  gcommon.common.v1.ConfigValue value = 2;

  // Optional namespace/environment
  string namespace = 3;

  // Configuration metadata
  map<string, string> metadata = 4;

  // Whether to encrypt the value
  bool encrypt = 5;

  // Tags for categorization
  repeated string tags = 6;

  // Request metadata
  gcommon.common.v1.RequestMetadata request_metadata = 7;
}

// Set configuration response
message SetConfigResponse {
  // Whether the operation succeeded
  bool success = 1;

  // Previous value if it existed
  ConfigEntry previous_entry = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete configuration request
message DeleteConfigRequest {
  // Configuration key to delete
  string key = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// List configuration request
message ListConfigRequest {
  // Key prefix filter
  string prefix = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 3;

  // Filter options
  gcommon.common.v1.FilterOptions filter = 4;

  // Sort options
  gcommon.common.v1.SortOptions sort = 5;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 6;
}

// List configuration response
message ListConfigResponse {
  // Configuration entries
  repeated ConfigEntry entries = 1;

  // Pagination information
  gcommon.common.v1.PaginatedResponse pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Watch configuration request
message WatchConfigRequest {
  // Key or key pattern to watch
  string key_pattern = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Watch configuration response
message WatchConfigResponse {
  // Type of change
  ConfigChangeType change_type = 1;

  // Configuration entry
  ConfigEntry entry = 2;

  // Previous value for updates/deletes
  ConfigEntry previous_entry = 3;

  // Change timestamp
  google.protobuf.Timestamp timestamp = 4;
}

// Configuration change type
enum ConfigChangeType {
  CONFIG_CHANGE_TYPE_UNSPECIFIED = 0;
  CONFIG_CHANGE_TYPE_CREATED = 1;
  CONFIG_CHANGE_TYPE_UPDATED = 2;
  CONFIG_CHANGE_TYPE_DELETED = 3;
}

// Configuration entry
message ConfigEntry {
  // Configuration key
  string key = 1;

  // Configuration value
  gcommon.common.v1.ConfigValue value = 2;

  // Namespace/environment
  string namespace = 3;

  // Entry metadata
  map<string, string> metadata = 4;

  // Tags for categorization
  repeated string tags = 5;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 6;

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 7;

  // Entry version for optimistic concurrency
  int64 version = 8;

  // Entry status
  gcommon.common.v1.ResourceStatus status = 9;
}

// GetMultiple configuration request
message GetMultipleConfigRequest {
  // Configuration keys to retrieve
  repeated string keys = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Whether to decrypt encrypted values
  bool decrypt = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// GetMultiple configuration response
message GetMultipleConfigResponse {
  // Retrieved entries mapped by key
  map<string, ConfigEntry> entries = 1;

  // Keys that were not found
  repeated string not_found = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// SetMultiple configuration request
message SetMultipleConfigRequest {
  // Configuration entries to set
  map<string, gcommon.common.v1.ConfigValue> entries = 1;

  // Optional namespace/environment
  string namespace = 2;

  // Common metadata for all entries
  map<string, string> metadata = 3;

  // Whether to encrypt values
  bool encrypt = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata request_metadata = 5;
}

// SetMultiple configuration response
message SetMultipleConfigResponse {
  // Success status for each key
  map<string, bool> results = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Validate configuration request
message ValidateConfigRequest {
  // Configuration entries to validate
  repeated ConfigEntry entries = 1;

  // Schema to validate against
  string schema_name = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Validate configuration response
message ValidateConfigResponse {
  // Validation result
  bool valid = 1;

  // Validation errors
  repeated ConfigValidationError errors = 2;

  // Validation warnings
  repeated ConfigValidationWarning warnings = 3;
}

// Configuration validation error
message ConfigValidationError {
  // Configuration key with error
  string key = 1;

  // Error message
  string message = 2;

  // Error code
  string code = 3;
}

// Configuration validation warning
message ConfigValidationWarning {
  // Configuration key with warning
  string key = 1;

  // Warning message
  string message = 2;

  // Warning code
  string code = 3;
}

// Schema request
message GetSchemaRequest {
  // Schema name
  string name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Schema response
message GetSchemaResponse {
  // Configuration schema
  ConfigSchema schema = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Configuration schema
message ConfigSchema {
  // Schema name
  string name = 1;

  // Schema version
  string version = 2;

  // Schema definition (JSON Schema)
  string definition = 3;

  // Schema metadata
  map<string, string> metadata = 4;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 5;
}
CONFIG_PROTO

echo "Created config.proto"

# 4. Database proto (comprehensive database operations)
cat > "${BASE_DIR}/db/proto/database.proto" << 'DATABASE_PROTO'
// file: pkg/db/proto/database.proto
edition = "2023";

package gcommon.v1.database;

import "pkg/common/proto/common.proto";
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/any.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/struct.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/db/proto;dbpb";
option features.(pb.go).api_level = API_HYBRID;

// DatabaseService provides comprehensive database operations
service DatabaseService {
  // Query executes a read-only query
  rpc Query(QueryRequest) returns (QueryResponse);

  // Execute runs a write operation (INSERT, UPDATE, DELETE)
  rpc Execute(ExecuteRequest) returns (ExecuteResponse);

  // ExecuteBatch runs multiple operations in a batch
  rpc ExecuteBatch(ExecuteBatchRequest) returns (ExecuteBatchResponse);

  // BeginTransaction starts a new transaction
  rpc BeginTransaction(BeginTransactionRequest) returns (BeginTransactionResponse);

  // CommitTransaction commits a transaction
  rpc CommitTransaction(CommitTransactionRequest) returns (google.protobuf.Empty);

  // RollbackTransaction rolls back a transaction
  rpc RollbackTransaction(RollbackTransactionRequest) returns (google.protobuf.Empty);

  // GetConnectionInfo returns connection pool information
  rpc GetConnectionInfo(GetConnectionInfoRequest) returns (GetConnectionInfoResponse);

  // Health check for database connectivity
  rpc HealthCheck(HealthCheckRequest) returns (HealthCheckResponse);
}

// Database admin service for management operations
service DatabaseAdminService {
  // CreateDatabase creates a new database
  rpc CreateDatabase(CreateDatabaseRequest) returns (CreateDatabaseResponse);

  // DropDatabase removes a database
  rpc DropDatabase(DropDatabaseRequest) returns (google.protobuf.Empty);

  // ListDatabases returns available databases
  rpc ListDatabases(ListDatabasesRequest) returns (ListDatabasesResponse);

  // GetDatabaseInfo returns database metadata
  rpc GetDatabaseInfo(GetDatabaseInfoRequest) returns (GetDatabaseInfoResponse);

  // CreateSchema creates a new schema
  rpc CreateSchema(CreateSchemaRequest) returns (CreateSchemaResponse);

  // DropSchema removes a schema
  rpc DropSchema(DropSchemaRequest) returns (google.protobuf.Empty);

  // ListSchemas returns available schemas
  rpc ListSchemas(ListSchemasRequest) returns (ListSchemasResponse);

  // RunMigration executes database migrations
  rpc RunMigration(RunMigrationRequest) returns (RunMigrationResponse);

  // GetMigrationStatus returns migration status
  rpc GetMigrationStatus(GetMigrationStatusRequest) returns (GetMigrationStatusResponse);
}

// Query request for read operations
message QueryRequest {
  // SQL query or NoSQL query
  string query = 1;

  // Query parameters
  repeated QueryParameter parameters = 2;

  // Database name (optional)
  string database = 3;

  // Query options
  QueryOptions options = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;

  // Transaction ID if part of transaction
  string transaction_id = 6;
}

// Query response with results
message QueryResponse {
  // Query result set
  ResultSet result_set = 1;

  // Query execution statistics
  QueryStats stats = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Execute request for write operations
message ExecuteRequest {
  // SQL statement or NoSQL operation
  string statement = 1;

  // Statement parameters
  repeated QueryParameter parameters = 2;

  // Database name (optional)
  string database = 3;

  // Execution options
  ExecuteOptions options = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;

  // Transaction ID if part of transaction
  string transaction_id = 6;
}

// Execute response with operation result
message ExecuteResponse {
  // Number of affected rows
  int64 affected_rows = 1;

  // Generated keys (for INSERT operations)
  repeated google.protobuf.Any generated_keys = 2;

  // Execution statistics
  ExecuteStats stats = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Query parameter for parameterized queries
message QueryParameter {
  // Parameter name
  string name = 1;

  // Parameter value
  google.protobuf.Any value = 2;

  // Parameter type hint
  string type = 3;
}

// Query options
message QueryOptions {
  // Maximum number of rows to return
  int32 limit = 1;

  // Number of rows to skip
  int32 offset = 2;

  // Query timeout
  google.protobuf.Duration timeout = 3;

  // Whether to include column metadata
  bool include_metadata = 4;

  // Read consistency level
  ConsistencyLevel consistency = 5;
}

// Execute options
message ExecuteOptions {
  // Execution timeout
  google.protobuf.Duration timeout = 1;

  // Whether to return generated keys
  bool return_generated_keys = 2;

  // Isolation level for transaction
  IsolationLevel isolation = 3;
}

// Result set for query results
message ResultSet {
  // Column metadata
  repeated ColumnMetadata columns = 1;

  // Result rows
  repeated Row rows = 2;

  // Total row count (if known)
  int64 total_count = 3;

  // Whether more rows are available
  bool has_more = 4;
}

// Column metadata
message ColumnMetadata {
  // Column name
  string name = 1;

  // Column type
  string type = 2;

  // Whether column allows null values
  bool nullable = 3;

  // Column size/precision
  int32 size = 4;

  // Column scale (for decimal types)
  int32 scale = 5;

  // Additional metadata
  map<string, string> metadata = 6;
}

// Result row
message Row {
  // Column values in order
  repeated google.protobuf.Any values = 1;
}

// Query execution statistics
message QueryStats {
  // Execution time
  google.protobuf.Duration execution_time = 1;

  // Number of rows returned
  int64 row_count = 2;

  // Number of columns
  int32 column_count = 3;

  // Query plan (if available)
  string query_plan = 4;

  // Cost estimate
  double cost_estimate = 5;
}

// Execute operation statistics
message ExecuteStats {
  // Execution time
  google.protobuf.Duration execution_time = 1;

  // Number of affected rows
  int64 affected_rows = 2;

  // Cost estimate
  double cost_estimate = 3;
}

// Consistency level enumeration
enum ConsistencyLevel {
  CONSISTENCY_LEVEL_UNSPECIFIED = 0;
  CONSISTENCY_LEVEL_EVENTUAL = 1;
  CONSISTENCY_LEVEL_STRONG = 2;
  CONSISTENCY_LEVEL_BOUNDED_STALENESS = 3;
}

// Isolation level enumeration
enum IsolationLevel {
  ISOLATION_LEVEL_UNSPECIFIED = 0;
  ISOLATION_LEVEL_READ_UNCOMMITTED = 1;
  ISOLATION_LEVEL_READ_COMMITTED = 2;
  ISOLATION_LEVEL_REPEATABLE_READ = 3;
  ISOLATION_LEVEL_SERIALIZABLE = 4;
}

// Batch execute request
message ExecuteBatchRequest {
  // Batch operations
  repeated BatchOperation operations = 1;

  // Database name (optional)
  string database = 2;

  // Batch options
  BatchExecuteOptions options = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;

  // Transaction ID if part of transaction
  string transaction_id = 5;
}

// Batch operation
message BatchOperation {
  // SQL statement or operation
  string statement = 1;

  // Statement parameters
  repeated QueryParameter parameters = 2;
}

// Batch execute options
message BatchExecuteOptions {
  // Whether to stop on first error
  bool fail_fast = 1;

  // Execution timeout for entire batch
  google.protobuf.Duration timeout = 2;

  // Maximum parallel operations
  int32 max_parallel = 3;
}

// Batch execute response
message ExecuteBatchResponse {
  // Results for each operation
  repeated BatchOperationResult results = 1;

  // Overall batch statistics
  BatchStats stats = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Result for individual batch operation
message BatchOperationResult {
  // Whether operation succeeded
  bool success = 1;

  // Number of affected rows
  int64 affected_rows = 2;

  // Generated keys (for INSERT operations)
  repeated google.protobuf.Any generated_keys = 3;

  // Error if operation failed
  gcommon.common.v1.Error error = 4;
}

// Batch execution statistics
message BatchStats {
  // Total execution time
  google.protobuf.Duration total_time = 1;

  // Number of successful operations
  int32 successful_operations = 2;

  // Number of failed operations
  int32 failed_operations = 3;

  // Total affected rows
  int64 total_affected_rows = 4;
}

// Transaction management messages
message BeginTransactionRequest {
  // Database name (optional)
  string database = 1;

  // Transaction options
  TransactionOptions options = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message BeginTransactionResponse {
  // Transaction ID
  string transaction_id = 1;

  // Transaction timestamp
  google.protobuf.Timestamp started_at = 2;
}

// Transaction options
message TransactionOptions {
  // Isolation level
  IsolationLevel isolation = 1;

  // Transaction timeout
  google.protobuf.Duration timeout = 2;

  // Read-only transaction
  bool read_only = 3;
}

message CommitTransactionRequest {
  // Transaction ID
  string transaction_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message RollbackTransactionRequest {
  // Transaction ID
  string transaction_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Connection info messages
message GetConnectionInfoRequest {
  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 1;
}

message GetConnectionInfoResponse {
  // Connection pool information
  ConnectionPoolInfo pool_info = 1;

  // Database information
  DatabaseInfo database_info = 2;
}

// Connection pool information
message ConnectionPoolInfo {
  // Maximum connections
  int32 max_connections = 1;

  // Active connections
  int32 active_connections = 2;

  // Idle connections
  int32 idle_connections = 3;

  // Average connection lifetime
  google.protobuf.Duration avg_lifetime = 4;

  // Connection pool statistics
  PoolStats stats = 5;
}

// Pool statistics
message PoolStats {
  // Total connections created
  int64 total_created = 1;

  // Total connections closed
  int64 total_closed = 2;

  // Connection acquisition failures
  int64 acquisition_failures = 3;

  // Average acquisition time
  google.protobuf.Duration avg_acquisition_time = 4;
}

// Database information
message DatabaseInfo {
  // Database name
  string name = 1;

  // Database version
  string version = 2;

  // Database type/vendor
  string type = 3;

  // Connection string (sanitized)
  string connection_string = 4;

  // Database features
  repeated string features = 5;
}

// Health check messages
message HealthCheckRequest {
  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 1;
}

message HealthCheckResponse {
  // Health status
  gcommon.common.v1.HealthStatus status = 1;

  // Connection check result
  bool connection_ok = 2;

  // Response time
  google.protobuf.Duration response_time = 3;

  // Error information if unhealthy
  gcommon.common.v1.Error error = 4;
}

// Admin service messages (abbreviated for space)
message CreateDatabaseRequest {
  string name = 1;
  map<string, string> options = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message CreateDatabaseResponse {
  bool success = 1;
  gcommon.common.v1.Error error = 2;
}

message DropDatabaseRequest {
  string name = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ListDatabasesRequest {
  gcommon.common.v1.RequestMetadata metadata = 1;
}

message ListDatabasesResponse {
  repeated string databases = 1;
}

message GetDatabaseInfoRequest {
  string name = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetDatabaseInfoResponse {
  DatabaseInfo info = 1;
}

message CreateSchemaRequest {
  string database = 1;
  string schema = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message CreateSchemaResponse {
  bool success = 1;
  gcommon.common.v1.Error error = 2;
}

message DropSchemaRequest {
  string database = 1;
  string schema = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message ListSchemasRequest {
  string database = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message ListSchemasResponse {
  repeated string schemas = 1;
}

message RunMigrationRequest {
  string database = 1;
  repeated MigrationScript scripts = 2;
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message MigrationScript {
  string version = 1;
  string script = 2;
  string description = 3;
}

message RunMigrationResponse {
  bool success = 1;
  repeated string applied_versions = 2;
  gcommon.common.v1.Error error = 3;
}

message GetMigrationStatusRequest {
  string database = 1;
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetMigrationStatusResponse {
  string current_version = 1;
  repeated string applied_versions = 2;
  repeated string pending_versions = 3;
}
DATABASE_PROTO

echo "Created database.proto"

# 5. Health proto (comprehensive health checking)
cat > "${BASE_DIR}/health/proto/health.proto" << 'HEALTH_PROTO'
// file: pkg/health/proto/health.proto
edition = "2023";

package gcommon.v1.health;

import "pkg/common/proto/common.proto";
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/any.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/health/proto;healthpb";
option features.(pb.go).api_level = API_HYBRID;

// HealthService provides comprehensive health checking capabilities
service HealthService {
  // Check performs a health check for a specific service
  rpc Check(HealthCheckRequest) returns (HealthCheckResponse);

  // Watch returns a stream of health check results
  rpc Watch(WatchRequest) returns (stream HealthCheckResponse);

  // GetServiceHealth returns health status for a service
  rpc GetServiceHealth(GetServiceHealthRequest) returns (GetServiceHealthResponse);

  // ListServices returns all monitored services
  rpc ListServices(ListServicesRequest) returns (ListServicesResponse);

  // RegisterCheck registers a new health check
  rpc RegisterCheck(RegisterCheckRequest) returns (RegisterCheckResponse);

  // UnregisterCheck removes a health check
  rpc UnregisterCheck(UnregisterCheckRequest) returns (google.protobuf.Empty);

  // GetHealthMetrics returns health metrics and statistics
  rpc GetHealthMetrics(GetHealthMetricsRequest) returns (GetHealthMetricsResponse);
}

// Standard gRPC health checking service (for compatibility)
service HealthCheckService {
  rpc Check(HealthCheckRequest) returns (HealthCheckResponse);
  rpc Watch(WatchRequest) returns (stream HealthCheckResponse);
}

// Health check request
message HealthCheckRequest {
  // Service name to check (empty for overall health)
  string service = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;

  // Check timeout
  google.protobuf.Duration timeout = 3;

  // Include detailed check results
  bool include_details = 4;
}

// Health check response
message HealthCheckResponse {
  // Overall health status
  gcommon.common.v1.HealthStatus status = 1;

  // Service name
  string service = 2;

  // Check timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Response time
  google.protobuf.Duration response_time = 4;

  // Detailed check results
  repeated CheckResult check_results = 5;

  // Health message
  string message = 6;

  // Error information if unhealthy
  gcommon.common.v1.Error error = 7;

  // Health metrics
  HealthMetrics metrics = 8;
}

// Watch request for streaming health checks
message WatchRequest {
  // Service name to watch (empty for all services)
  string service = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Service health response
message GetServiceHealthRequest {
  // Service name
  string service = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

message GetServiceHealthResponse {
  // Health status
  gcommon.common.v1.HealthStatus status = 1;

  // Last check timestamp
  google.protobuf.Timestamp last_check = 2;

  // Error information if unhealthy
  gcommon.common.v1.Error error = 3;
}

// List services response
message ListServicesRequest {
  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 1;
}

message ListServicesResponse {
  // List of service names
  repeated string services = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Register health check request
message RegisterCheckRequest {
  // Service name
  string service = 1;

  // Check parameters
  HealthCheckRequest check = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

message RegisterCheckResponse {
  // Success status
  bool success = 1;

  // Registered check ID
  string check_id = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Unregister health check request
message UnregisterCheckRequest {
  // Check ID to unregister
  string check_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Health metrics request
message GetHealthMetricsRequest {
  // Service name (optional)
  string service = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Health metrics response
message GetHealthMetricsResponse {
  // Health metrics data
  repeated HealthMetricData metrics = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Health metric data
message HealthMetricData {
  // Metric name
  string name = 1;

  // Metric value
  double value = 2;

  // Timestamp of the metric
  google.protobuf.Timestamp timestamp = 3;

  // Labels for the metric
  map<string, string> labels = 4;
}
HEALTH_PROTO

echo "Created health.proto"

# 6. Log proto (comprehensive logging operations)
cat > "${BASE_DIR}/log/proto/log.proto" << 'LOG_PROTO'
// file: pkg/log/proto/log.proto
edition = "2023";

package gcommon.v1.log;

import "pkg/common/proto/common.proto";
import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/any.proto";
import "google/protobuf/field_mask.proto";

option go_package = "github.com/jdfalk/gcommon/pkg/log/proto;logpb";
option features.(pb.go).api_level = API_HYBRID;

// LogService provides comprehensive logging capabilities
service LogService {
  // Log writes a log entry
  rpc Log(LogRequest) returns (LogResponse);

  // LogBatch writes multiple log entries
  rpc LogBatch(LogBatchRequest) returns (LogBatchResponse);

  // Query searches and retrieves log entries
  rpc Query(QueryLogRequest) returns (QueryLogResponse);

  // Stream returns a real-time stream of log entries
  rpc Stream(StreamLogRequest) returns (stream LogEntry);

  // GetLogLevel returns the current log level
  rpc GetLogLevel(GetLogLevelRequest) returns (GetLogLevelResponse);

  // SetLogLevel changes the log level
  rpc SetLogLevel(SetLogLevelRequest) returns (SetLogLevelResponse);

  // GetLogStats returns logging statistics
  rpc GetLogStats(GetLogStatsRequest) returns (GetLogStatsResponse);
}

// LogAdminService provides administrative logging operations
service LogAdminService {
  // CreateLogger creates a new logger instance
  rpc CreateLogger(CreateLoggerRequest) returns (CreateLoggerResponse);

  // UpdateLogger updates logger configuration
  rpc UpdateLogger(UpdateLoggerRequest) returns (UpdateLoggerResponse);

  // DeleteLogger removes a logger instance
  rpc DeleteLogger(DeleteLoggerRequest) returns (google.protobuf.Empty);

  // ListLoggers returns all available loggers
  rpc ListLoggers(ListLoggersRequest) returns (ListLoggersResponse);

  // ConfigureAppender configures log output destinations
  rpc ConfigureAppender(ConfigureAppenderRequest) returns (ConfigureAppenderResponse);

  // RotateLogs forces log rotation
  rpc RotateLogs(RotateLogsRequest) returns (RotateLogsResponse);

  // ArchiveLogs archives old log files
  rpc ArchiveLogs(ArchiveLogsRequest) returns (ArchiveLogsResponse);
}

// Log level enumeration
enum LogLevel {
  LOG_LEVEL_UNSPECIFIED = 0;
  LOG_LEVEL_TRACE = 1;
  LOG_LEVEL_DEBUG = 2;
  LOG_LEVEL_INFO = 3;
  LOG_LEVEL_WARN = 4;
  LOG_LEVEL_ERROR = 5;
  LOG_LEVEL_FATAL = 6;
}

// Log request for writing a single entry
message LogRequest {
  // Log entry to write
  LogEntry entry = 1;

  // Logger name (optional)
  string logger = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Log response
message LogResponse {
  // Success status
  bool success = 1;

  // Entry ID (if supported)
  string entry_id = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Batch log request
message LogBatchRequest {
  // Log entries to write
  repeated LogEntry entries = 1;

  // Logger name (optional)
  string logger = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;

  // Batch options
  BatchLogOptions options = 4;
}

// Batch log options
message BatchLogOptions {
  // Whether to fail fast on first error
  bool fail_fast = 1;

  // Maximum batch size
  int32 max_batch_size = 2;

  // Batch timeout
  google.protobuf.Duration timeout = 3;
}

// Batch log response
message LogBatchResponse {
  // Number of successfully written entries
  int32 success_count = 1;

  // Number of failed entries
  int32 failure_count = 2;

  // Entry IDs (if supported)
  repeated string entry_ids = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Log entry representation
message LogEntry {
  // Log level
  LogLevel level = 1;

  // Log message
  string message = 2;

  // Timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Logger name
  string logger = 4;

  // Thread/goroutine information
  string thread = 5;

  // Source file information
  SourceLocation source = 6;

  // Structured fields
  map<string, google.protobuf.Any> fields = 7;

  // Tags for categorization
  repeated string tags = 8;

  // Trace ID for distributed tracing
  string trace_id = 9;

  // Span ID for distributed tracing
  string span_id = 10;

  // User ID associated with the log
  string user_id = 11;

  // Request ID
  string request_id = 12;

  // Error information (if log level is ERROR or FATAL)
  ErrorInfo error_info = 13;
}

// Source location information
message SourceLocation {
  // File name
  string file = 1;

  // Line number
  int32 line = 2;

  // Function name
  string function = 3;

  // Package/module name
  string package = 4;
}

// Error information for error/fatal logs
message ErrorInfo {
  // Error message
  string message = 1;

  // Error type/class
  string type = 2;

  // Stack trace
  string stack_trace = 3;

  // Error code
  string code = 4;

  // Additional error context
  map<string, string> context = 5;

  // Cause chain for error propagation
  repeated ErrorInfo causes = 6;
}

// Query log request
message QueryLogRequest {
  // Query filters
  LogFilter filter = 1;

  // Pagination
  gcommon.common.v1.Pagination pagination = 2;

  // Sorting options
  LogSort sort = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Log filter options
message LogFilter {
  // Log level filter
  repeated LogLevel levels = 1;

  // Logger name filter
  repeated string loggers = 2;

  // Message search (supports regex)
  string message_pattern = 3;

  // Time range filter
  TimeRange time_range = 4;

  // Tag filters
  repeated string tags = 5;

  // Trace ID filter
  string trace_id = 6;

  // User ID filter
  string user_id = 7;

  // Request ID filter
  string request_id = 8;

  // Field filters
  map<string, string> field_filters = 9;
}

// Time range for filtering
message TimeRange {
  // Start time (inclusive)
  google.protobuf.Timestamp start = 1;

  // End time (exclusive)
  google.protobuf.Timestamp end = 2;
}

// Log sorting options
message LogSort {
  // Sort field
  LogSortField field = 1;

  // Sort direction
  gcommon.common.v1.SortDirection direction = 2;
}

// Log sort fields
enum LogSortField {
  LOG_SORT_FIELD_UNSPECIFIED = 0;
  LOG_SORT_FIELD_TIMESTAMP = 1;
  LOG_SORT_FIELD_LEVEL = 2;
  LOG_SORT_FIELD_LOGGER = 3;
  LOG_SORT_FIELD_MESSAGE = 4;
}

// Query log response
message QueryLogResponse {
  // Found log entries
  repeated LogEntry entries = 1;

  // Pagination info
  gcommon.common.v1.Pagination pagination = 2;

  // Total count (if requested)
  int64 total_count = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Stream log request
message StreamLogRequest {
  // Stream filters
  LogFilter filter = 1;

  // Follow mode (tail -f style)
  bool follow = 2;

  // Buffer size
  int32 buffer_size = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Get log level request
message GetLogLevelRequest {
  // Logger name (optional, defaults to root)
  string logger = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get log level response
message GetLogLevelResponse {
  // Current log level
  LogLevel level = 1;

  // Logger name
  string logger = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Set log level request
message SetLogLevelRequest {
  // New log level
  LogLevel level = 1;

  // Logger name (optional, defaults to root)
  string logger = 2;

  // Whether to persist the change
  bool persist = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Set log level response
message SetLogLevelResponse {
  // Previous log level
  LogLevel previous_level = 1;

  // New log level
  LogLevel new_level = 2;

  // Logger name
  string logger = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Get log stats request
message GetLogStatsRequest {
  // Time range for statistics
  TimeRange time_range = 1;

  // Logger filter
  repeated string loggers = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Get log stats response
message GetLogStatsResponse {
  // Overall statistics
  LogStatistics stats = 1;

  // Per-level statistics
  map<string, int64> level_counts = 2;

  // Per-logger statistics
  map<string, LogStatistics> logger_stats = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Log statistics
message LogStatistics {
  // Total log entries
  int64 total_entries = 1;

  // Entries per second (rate)
  double entries_per_second = 2;

  // Average entry size
  int64 average_size = 3;

  // Total size
  int64 total_size = 4;

  // Error count
  int64 error_count = 5;

  // Warning count
  int64 warning_count = 6;
}

// Admin service messages

// Create logger request
message CreateLoggerRequest {
  // Logger name
  string name = 1;

  // Logger configuration
  LoggerConfig config = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Logger configuration
message LoggerConfig {
  // Log level
  LogLevel level = 1;

  // Output appenders
  repeated AppenderConfig appenders = 2;

  // Whether to inherit from parent
  bool inherit_appenders = 3;

  // Whether to propagate to parent logger
  bool propagate = 4;

  // Additional properties
  map<string, string> properties = 5;
}

// Appender configuration
message AppenderConfig {
  // Appender name
  string name = 1;

  // Appender type
  AppenderType type = 2;

  // Output configuration
  OutputConfig output = 3;

  // Formatter configuration
  FormatterConfig formatter = 4;

  // Filter configuration
  FilterConfig filter = 5;
}

// Appender types
enum AppenderType {
  APPENDER_TYPE_UNSPECIFIED = 0;
  APPENDER_TYPE_CONSOLE = 1;
  APPENDER_TYPE_FILE = 2;
  APPENDER_TYPE_ROLLING_FILE = 3;
  APPENDER_TYPE_SYSLOG = 4;
  APPENDER_TYPE_NETWORK = 5;
  APPENDER_TYPE_DATABASE = 6;
}

// Output configuration
message OutputConfig {
  // Output target (file path, network address, etc.)
  string target = 1;

  // Additional output options
  map<string, string> options = 2;
}

// Formatter configuration
message FormatterConfig {
  // Formatter type
  FormatterType type = 1;

  // Format pattern
  string pattern = 2;

  // Timestamp format
  string timestamp_format = 3;

  // Additional formatter options
  map<string, string> options = 4;
}

// Formatter type enumeration
enum FormatterType {
  FORMATTER_TYPE_UNSPECIFIED = 0;
  FORMATTER_TYPE_TEXT = 1;
  FORMATTER_TYPE_JSON = 2;
  FORMATTER_TYPE_XML = 3;
  FORMATTER_TYPE_CUSTOM = 4;
}

// Filter configuration
message FilterConfig {
  // Filter type
  FilterType type = 1;

  // Filter criteria
  map<string, string> criteria = 2;
}

// Filter type enumeration
enum FilterType {
  FILTER_TYPE_UNSPECIFIED = 0;
  FILTER_TYPE_LEVEL = 1;
  FILTER_TYPE_LOGGER = 2;
  FILTER_TYPE_MESSAGE = 3;
  FILTER_TYPE_FIELD = 4;
}

// Create logger response
message CreateLoggerResponse {
  // Created logger name
  string name = 1;

  // Success status
  bool success = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Update logger request
message UpdateLoggerRequest {
  // Logger name
  string name = 1;

  // Updated configuration
  LoggerConfig config = 2;

  // Update mask
  google.protobuf.FieldMask update_mask = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Update logger response
message UpdateLoggerResponse {
  // Updated logger name
  string name = 1;

  // Success status
  bool success = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete logger request
message DeleteLoggerRequest {
  // Logger name
  string name = 1;

  // Force deletion
  bool force = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// List loggers request
message ListLoggersRequest {
  // Name pattern filter
  string name_pattern = 1;

  // Level filter
  repeated LogLevel levels = 2;

  // Pagination
  gcommon.common.v1.Pagination pagination = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// List loggers response
message ListLoggersResponse {
  // Logger information
  repeated LoggerInfo loggers = 1;

  // Pagination info
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Logger information
message LoggerInfo {
  // Logger name
  string name = 1;

  // Current configuration
  LoggerConfig config = 2;

  // Parent logger
  string parent = 3;

  // Child loggers
  repeated string children = 4;

  // Statistics
  LogStatistics stats = 5;

  // Creation time
  google.protobuf.Timestamp created_at = 6;

  // Last modified time
  google.protobuf.Timestamp modified_at = 7;

  // Status
  LoggerStatus status = 8;
}

// Logger status enumeration
enum LoggerStatus {
  LOGGER_STATUS_UNSPECIFIED = 0;
  LOGGER_STATUS_ACTIVE = 1;
  LOGGER_STATUS_INACTIVE = 2;
  LOGGER_STATUS_ERROR = 3;
}

// Configure appender request
message ConfigureAppenderRequest {
  // Appender configuration
  AppenderConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Configure appender response
message ConfigureAppenderResponse {
  // Appender name
  string name = 1;

  // Success status
  bool success = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Rotate logs request
message RotateLogsRequest {
  // Logger pattern
  string logger_pattern = 1;

  // Force rotation
  bool force = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Rotate logs response
message RotateLogsResponse {
  // Number of rotated files
  int32 rotated_count = 1;

  // Rotated file paths
  repeated string rotated_files = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Archive logs request
message ArchiveLogsRequest {
  // Archive criteria
  ArchiveCriteria criteria = 1;

  // Archive destination
  string destination = 2;

  // Compression type
  CompressionType compression = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Archive criteria
message ArchiveCriteria {
  // Older than duration
  google.protobuf.Duration older_than = 1;

  // Size threshold
  int64 size_threshold_bytes = 2;

  // Logger pattern
  string logger_pattern = 3;

  // Date range
  google.protobuf.Timestamp start_time = 4;
  google.protobuf.Timestamp end_time = 5;
}

// Compression type enumeration
enum CompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  COMPRESSION_TYPE_NONE = 1;
  COMPRESSION_TYPE_GZIP = 2;
  COMPRESSION_TYPE_ZIP = 3;
  COMPRESSION_TYPE_BZIP2 = 4;
  COMPRESSION_TYPE_TAR_GZ = 5;
}

// Archive logs response
message ArchiveLogsResponse {
  // Number of archived files
  int32 archived_count = 1;

  // Archive file path
  string archive_path = 2;

  // Archive size
  int64 archive_size = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}
LOG_PROTO

echo "Created log.proto"

# Create metrics.proto
cat > pkg/metrics/proto/metrics.proto << 'METRICS_PROTO'
// file: pkg/metrics/proto/metrics.proto
edition = "2023";

package gcommon.v1.metrics;

option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto;metricspb";
option features.(pb.go).api_level = API_HYBRID;

import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/field_mask.proto";
import "pkg/common/proto/common.proto";

// MetricsService provides comprehensive metrics collection, aggregation, and querying
service MetricsService {
  // Record a metric value
  rpc RecordMetric(RecordMetricRequest) returns (RecordMetricResponse);

  // Record multiple metrics in batch
  rpc RecordMetrics(RecordMetricsRequest) returns (RecordMetricsResponse);

  // Increment a counter metric
  rpc IncrementCounter(IncrementCounterRequest) returns (IncrementCounterResponse);

  // Record a gauge metric
  rpc RecordGauge(RecordGaugeRequest) returns (RecordGaugeResponse);

  // Record a histogram metric
  rpc RecordHistogram(RecordHistogramRequest) returns (RecordHistogramResponse);

  // Record a timer metric
  rpc RecordTimer(RecordTimerRequest) returns (RecordTimerResponse);

  // Query metrics
  rpc QueryMetrics(QueryMetricsRequest) returns (QueryMetricsResponse);

  // Stream metrics in real-time
  rpc StreamMetrics(StreamMetricsRequest) returns (stream MetricData);

  // Get metric statistics
  rpc GetMetricStats(GetMetricStatsRequest) returns (GetMetricStatsResponse);

  // List available metrics
  rpc ListMetrics(ListMetricsRequest) returns (ListMetricsResponse);

  // Get metric metadata
  rpc GetMetricMetadata(GetMetricMetadataRequest) returns (GetMetricMetadataResponse);
}

// MetricsAdminService provides metrics administration and configuration
service MetricsAdminService {
  // Create a metric definition
  rpc CreateMetric(CreateMetricRequest) returns (CreateMetricResponse);

  // Update a metric definition
  rpc UpdateMetric(UpdateMetricRequest) returns (UpdateMetricResponse);

  // Delete a metric definition
  rpc DeleteMetric(DeleteMetricRequest) returns (DeleteMetricResponse);

  // Configure metric collection
  rpc ConfigureCollection(ConfigureCollectionRequest) returns (ConfigureCollectionResponse);

  // Create alert rules
  rpc CreateAlert(CreateAlertRequest) returns (CreateAlertResponse);

  // Update alert rules
  rpc UpdateAlert(UpdateAlertRequest) returns (UpdateAlertResponse);

  // Delete alert rules
  rpc DeleteAlert(DeleteAlertRequest) returns (DeleteAlertResponse);

  // List alert rules
  rpc ListAlerts(ListAlertsRequest) returns (ListAlertsResponse);

  // Get alert status
  rpc GetAlertStatus(GetAlertStatusRequest) returns (GetAlertStatusResponse);

  // Export metrics data
  rpc ExportMetrics(ExportMetricsRequest) returns (ExportMetricsResponse);

  // Import metrics data
  rpc ImportMetrics(ImportMetricsRequest) returns (ImportMetricsResponse);

  // Purge old metrics data
  rpc PurgeMetrics(PurgeMetricsRequest) returns (PurgeMetricsResponse);

  // Get system metrics
  rpc GetSystemMetrics(GetSystemMetricsRequest) returns (GetSystemMetricsResponse);
}

// Record metric request
message RecordMetricRequest {
  // Metric data
  MetricData metric = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Record metric response
message RecordMetricResponse {
  // Success status
  bool success = 1;

  // Metric ID
  string metric_id = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Record metrics request (batch)
message RecordMetricsRequest {
  // Multiple metric data
  repeated MetricData metrics = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Record metrics response (batch)
message RecordMetricsResponse {
  // Number of metrics recorded
  int32 recorded_count = 1;

  // Failed metrics with errors
  repeated MetricError failed_metrics = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Metric error information
message MetricError {
  // Metric name
  string metric_name = 1;

  // Error message
  string error_message = 2;

  // Error code
  string error_code = 3;
}

// Increment counter request
message IncrementCounterRequest {
  // Counter name
  string name = 1;

  // Increment value (default: 1)
  double value = 2;

  // Metric tags
  map<string, string> tags = 3;

  // Timestamp (optional, defaults to current time)
  google.protobuf.Timestamp timestamp = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Increment counter response
message IncrementCounterResponse {
  // Success status
  bool success = 1;

  // New counter value
  double new_value = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Record gauge request
message RecordGaugeRequest {
  // Gauge name
  string name = 1;

  // Gauge value
  double value = 2;

  // Metric tags
  map<string, string> tags = 3;

  // Timestamp (optional, defaults to current time)
  google.protobuf.Timestamp timestamp = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Record gauge response
message RecordGaugeResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Record histogram request
message RecordHistogramRequest {
  // Histogram name
  string name = 1;

  // Value to record
  double value = 2;

  // Metric tags
  map<string, string> tags = 3;

  // Timestamp (optional, defaults to current time)
  google.protobuf.Timestamp timestamp = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Record histogram response
message RecordHistogramResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Record timer request
message RecordTimerRequest {
  // Timer name
  string name = 1;

  // Duration to record
  google.protobuf.Duration duration = 2;

  // Metric tags
  map<string, string> tags = 3;

  // Timestamp (optional, defaults to current time)
  google.protobuf.Timestamp timestamp = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Record timer response
message RecordTimerResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Query metrics request
message QueryMetricsRequest {
  // Metric query
  MetricQuery query = 1;

  // Aggregation options
  AggregationOptions aggregation = 2;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Metric query parameters
message MetricQuery {
  // Metric name pattern
  string name_pattern = 1;

  // Time range
  google.protobuf.Timestamp start_time = 2;
  google.protobuf.Timestamp end_time = 3;

  // Metric types to include
  repeated MetricType types = 4;

  // Tag filters
  map<string, string> tag_filters = 5;

  // Value range filters
  ValueRange value_range = 6;

  // Sort order
  MetricSortOrder sort_order = 7;

  // Maximum results
  int32 limit = 8;
}

// Value range filter
message ValueRange {
  // Minimum value (optional)
  double min_value = 1;

  // Maximum value (optional)
  double max_value = 2;
}

// Metric sort order
enum MetricSortOrder {
  METRIC_SORT_ORDER_UNSPECIFIED = 0;
  METRIC_SORT_ORDER_TIMESTAMP_ASC = 1;
  METRIC_SORT_ORDER_TIMESTAMP_DESC = 2;
  METRIC_SORT_ORDER_VALUE_ASC = 3;
  METRIC_SORT_ORDER_VALUE_DESC = 4;
  METRIC_SORT_ORDER_NAME_ASC = 5;
  METRIC_SORT_ORDER_NAME_DESC = 6;
}

// Aggregation options
message AggregationOptions {
  // Aggregation function
  AggregationFunction function = 1;

  // Time window for aggregation
  google.protobuf.Duration time_window = 2;

  // Group by fields
  repeated string group_by = 3;

  // Having conditions for aggregated results
  map<string, double> having = 4;
}

// Aggregation function enumeration
enum AggregationFunction {
  AGGREGATION_FUNCTION_UNSPECIFIED = 0;
  AGGREGATION_FUNCTION_SUM = 1;
  AGGREGATION_FUNCTION_AVG = 2;
  AGGREGATION_FUNCTION_COUNT = 3;
  AGGREGATION_FUNCTION_MIN = 4;
  AGGREGATION_FUNCTION_MAX = 5;
  AGGREGATION_FUNCTION_STDDEV = 6;
  AGGREGATION_FUNCTION_PERCENTILE = 7;
}

// Query metrics response
message QueryMetricsResponse {
  // Metric data results
  repeated MetricData metrics = 1;

  // Aggregated results (if aggregation was requested)
  repeated AggregatedMetric aggregated_metrics = 2;

  // Total count
  int64 total_count = 3;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 4;

  // Error information
  gcommon.common.v1.Error error = 5;
}

// Aggregated metric data
message AggregatedMetric {
  // Metric name
  string name = 1;

  // Aggregated value
  double value = 2;

  // Aggregation function used
  AggregationFunction function = 3;

  // Time window
  google.protobuf.Timestamp window_start = 4;
  google.protobuf.Timestamp window_end = 5;

  // Group by values
  map<string, string> group_values = 6;

  // Sample count
  int64 sample_count = 7;
}

// Stream metrics request
message StreamMetricsRequest {
  // Query for filtering metrics
  MetricQuery query = 1;

  // Buffer size for streaming
  int32 buffer_size = 2;

  // Update interval
  google.protobuf.Duration update_interval = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Get metric stats request
message GetMetricStatsRequest {
  // Metric name
  string name = 1;

  // Time range
  google.protobuf.Timestamp start_time = 2;
  google.protobuf.Timestamp end_time = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Get metric stats response
message GetMetricStatsResponse {
  // Metric statistics
  MetricStats stats = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Metric statistics
message MetricStats {
  // Metric name
  string name = 1;

  // Total data points
  int64 total_points = 2;

  // Statistics by time period
  MetricStatsByPeriod hourly = 3;
  MetricStatsByPeriod daily = 4;
  MetricStatsByPeriod weekly = 5;

  // Value statistics
  ValueStats value_stats = 6;

  // Storage usage
  int64 storage_bytes = 7;
}

// Metric statistics by time period
message MetricStatsByPeriod {
  // Average value
  double avg_value = 1;

  // Minimum value
  double min_value = 2;

  // Maximum value
  double max_value = 3;

  // Total count
  int64 count = 4;

  // Standard deviation
  double std_dev = 5;
}

// Value statistics
message ValueStats {
  // Mean value
  double mean = 1;

  // Median value
  double median = 2;

  // 95th percentile
  double p95 = 3;

  // 99th percentile
  double p99 = 4;

  // Standard deviation
  double std_dev = 5;

  // Variance
  double variance = 6;
}

// List metrics request
message ListMetricsRequest {
  // Name pattern filter
  string name_pattern = 1;

  // Type filter
  MetricType type = 2;

  // Tag filters
  map<string, string> tag_filters = 3;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// List metrics response
message ListMetricsResponse {
  // Metric definitions
  repeated MetricDefinition metrics = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get metric metadata request
message GetMetricMetadataRequest {
  // Metric name
  string name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get metric metadata response
message GetMetricMetadataResponse {
  // Metric metadata
  MetricMetadata metadata = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Core metric data structure
message MetricData {
  // Metric name
  string name = 1;

  // Metric type
  MetricType type = 2;

  // Metric value(s)
  MetricValue value = 3;

  // Metric tags
  map<string, string> tags = 4;

  // Timestamp
  google.protobuf.Timestamp timestamp = 5;

  // Additional metadata
  map<string, string> metadata = 6;
}

// Metric type enumeration
enum MetricType {
  METRIC_TYPE_UNSPECIFIED = 0;
  METRIC_TYPE_COUNTER = 1;
  METRIC_TYPE_GAUGE = 2;
  METRIC_TYPE_HISTOGRAM = 3;
  METRIC_TYPE_SUMMARY = 4;
  METRIC_TYPE_TIMER = 5;
}

// Metric value union
message MetricValue {
  oneof value_type {
    // Simple numeric value
    double number_value = 1;

    // Histogram value
    HistogramValue histogram_value = 2;

    // Summary value
    SummaryValue summary_value = 3;

    // Timer value
    TimerValue timer_value = 4;
  }
}

// Histogram value data
message HistogramValue {
  // Sample count
  int64 sample_count = 1;

  // Sum of all samples
  double sample_sum = 2;

  // Histogram buckets
  repeated HistogramBucket buckets = 3;
}

// Histogram bucket
message HistogramBucket {
  // Upper bound (inclusive)
  double upper_bound = 1;

  // Cumulative count
  int64 cumulative_count = 2;
}

// Summary value data
message SummaryValue {
  // Sample count
  int64 sample_count = 1;

  // Sum of all samples
  double sample_sum = 2;

  // Quantiles
  repeated Quantile quantiles = 3;
}

// Quantile data
message Quantile {
  // Quantile (0.0 to 1.0)
  double quantile = 1;

  // Value at quantile
  double value = 2;
}

// Timer value data
message TimerValue {
  // Duration
  google.protobuf.Duration duration = 1;

  // Count of measurements
  int64 count = 2;

  // Rate (measurements per second)
  double rate = 3;
}

// Metric definition
message MetricDefinition {
  // Metric name
  string name = 1;

  // Metric type
  MetricType type = 2;

  // Description
  string description = 3;

  // Unit of measurement
  string unit = 4;

  // Default tags
  map<string, string> default_tags = 5;

  // Creation time
  google.protobuf.Timestamp created_at = 6;

  // Last updated time
  google.protobuf.Timestamp updated_at = 7;

  // Status
  MetricStatus status = 8;
}

// Metric status enumeration
enum MetricStatus {
  METRIC_STATUS_UNSPECIFIED = 0;
  METRIC_STATUS_ACTIVE = 1;
  METRIC_STATUS_INACTIVE = 2;
  METRIC_STATUS_DEPRECATED = 3;
}

// Metric metadata
message MetricMetadata {
  // Metric definition
  MetricDefinition definition = 1;

  // Statistics
  MetricStats stats = 2;

  // Collection configuration
  CollectionConfig collection_config = 3;

  // Alert rules
  repeated AlertRule alert_rules = 4;
}

// Collection configuration
message CollectionConfig {
  // Collection interval
  google.protobuf.Duration interval = 1;

  // Retention period
  google.protobuf.Duration retention = 2;

  // Sampling rate (0.0 to 1.0)
  double sampling_rate = 3;

  // Aggregation settings
  AggregationOptions aggregation = 4;

  // Storage settings
  StorageConfig storage = 5;
}

// Storage configuration
message StorageConfig {
  // Storage backend
  StorageBackend backend = 1;

  // Compression enabled
  bool compression_enabled = 2;

  // Batch size for writes
  int32 batch_size = 3;

  // Flush interval
  google.protobuf.Duration flush_interval = 4;
}

// Storage backend enumeration
enum StorageBackend {
  STORAGE_BACKEND_UNSPECIFIED = 0;
  STORAGE_BACKEND_MEMORY = 1;
  STORAGE_BACKEND_DISK = 2;
  STORAGE_BACKEND_DATABASE = 3;
  STORAGE_BACKEND_TIMESERIES = 4;
}

// Admin service messages
message CreateMetricRequest {
  // Metric definition
  MetricDefinition definition = 1;

  // Collection configuration
  CollectionConfig collection_config = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Create metric response
message CreateMetricResponse {
  // Success status
  bool success = 1;

  // Created metric definition
  MetricDefinition metric = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Update metric request
message UpdateMetricRequest {
  // Metric name
  string name = 1;

  // Updated definition
  MetricDefinition definition = 2;

  // Updated collection configuration
  CollectionConfig collection_config = 3;

  // Field mask for partial updates
  google.protobuf.FieldMask update_mask = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Update metric response
message UpdateMetricResponse {
  // Success status
  bool success = 1;

  // Updated metric definition
  MetricDefinition metric = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete metric request
message DeleteMetricRequest {
  // Metric name
  string name = 1;

  // Whether to delete associated data
  bool delete_data = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Configure collection request
message ConfigureCollectionRequest {
  // Global collection configuration
  GlobalCollectionConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Global collection configuration
message GlobalCollectionConfig {
  // Default collection interval
  google.protobuf.Duration default_interval = 1;

  // Default retention period
  google.protobuf.Duration default_retention = 2;

  // Maximum metrics limit
  int32 max_metrics = 3;

  // Storage configuration
  StorageConfig storage = 4;

  // Performance settings
  PerformanceConfig performance = 5;
}

// Performance configuration
message PerformanceConfig {
  // Worker pool size
  int32 worker_pool_size = 1;

  // Buffer size
  int32 buffer_size = 2;

  // Maximum batch size
  int32 max_batch_size = 3;

  // Flush timeout
  google.protobuf.Duration flush_timeout = 4;
}

// Configure collection response
message ConfigureCollectionResponse {
  // Success status
  bool success = 1;

  // Applied configuration
  GlobalCollectionConfig config = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Create alert request
message CreateAlertRequest {
  // Alert rule
  AlertRule rule = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Alert rule definition
message AlertRule {
  // Rule name
  string name = 1;

  // Description
  string description = 2;

  // Metric query
  MetricQuery query = 3;

  // Alert condition
  AlertCondition condition = 4;

  // Notification configuration
  NotificationConfig notification = 5;

  // Evaluation interval
  google.protobuf.Duration evaluation_interval = 6;

  // Grace period before firing
  google.protobuf.Duration grace_period = 7;

  // Severity level
  AlertSeverity severity = 8;

  // Tags
  map<string, string> tags = 9;

  // Enabled status
  bool enabled = 10;
}

// Alert condition
message AlertCondition {
  // Condition type
  AlertConditionType type = 1;

  // Threshold value
  double threshold = 2;

  // Comparison operator
  ComparisonOperator operator = 3;

  // Time window for evaluation
  google.protobuf.Duration time_window = 4;

  // Required consecutive violations
  int32 consecutive_violations = 5;
}

// Alert condition type enumeration
enum AlertConditionType {
  ALERT_CONDITION_TYPE_UNSPECIFIED = 0;
  ALERT_CONDITION_TYPE_THRESHOLD = 1;
  ALERT_CONDITION_TYPE_CHANGE = 2;
  ALERT_CONDITION_TYPE_ANOMALY = 3;
  ALERT_CONDITION_TYPE_ABSENCE = 4;
}

// Comparison operator enumeration
enum ComparisonOperator {
  COMPARISON_OPERATOR_UNSPECIFIED = 0;
  COMPARISON_OPERATOR_GREATER = 1;
  COMPARISON_OPERATOR_GREATER_EQUAL = 2;
  COMPARISON_OPERATOR_LESS = 3;
  COMPARISON_OPERATOR_LESS_EQUAL = 4;
  COMPARISON_OPERATOR_EQUAL = 5;
  COMPARISON_OPERATOR_NOT_EQUAL = 6;
}

// Notification configuration
message NotificationConfig {
  // Notification channels
  repeated NotificationChannel channels = 1;

  // Message template
  string message_template = 2;

  // Notification throttling
  google.protobuf.Duration throttle_duration = 3;

  // Escalation rules
  repeated EscalationRule escalation_rules = 4;
}

// Notification channel
message NotificationChannel {
  // Channel type
  NotificationChannelType type = 1;

  // Channel configuration
  map<string, string> config = 2;

  // Enabled status
  bool enabled = 3;
}

// Notification channel type enumeration
enum NotificationChannelType {
  NOTIFICATION_CHANNEL_TYPE_UNSPECIFIED = 0;
  NOTIFICATION_CHANNEL_TYPE_EMAIL = 1;
  NOTIFICATION_CHANNEL_TYPE_SLACK = 2;
  NOTIFICATION_CHANNEL_TYPE_WEBHOOK = 3;
  NOTIFICATION_CHANNEL_TYPE_SMS = 4;
  NOTIFICATION_CHANNEL_TYPE_PAGERDUTY = 5;
}

// Escalation rule
message EscalationRule {
  // Delay before escalation
  google.protobuf.Duration delay = 1;

  // Escalation channels
  repeated NotificationChannel channels = 2;

  // Condition for escalation
  string condition = 3;
}

// Alert severity enumeration
enum AlertSeverity {
  ALERT_SEVERITY_UNSPECIFIED = 0;
  ALERT_SEVERITY_INFO = 1;
  ALERT_SEVERITY_WARNING = 2;
  ALERT_SEVERITY_ERROR = 3;
  ALERT_SEVERITY_CRITICAL = 4;
}

// Create alert response
message CreateAlertResponse {
  // Success status
  bool success = 1;

  // Created alert rule
  AlertRule rule = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Update alert request
message UpdateAlertRequest {
  // Alert rule name
  string name = 1;

  // Updated alert rule
  AlertRule rule = 2;

  // Field mask for partial updates
  google.protobuf.FieldMask update_mask = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Update alert response
message UpdateAlertResponse {
  // Success status
  bool success = 1;

  // Updated alert rule
  AlertRule rule = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete alert request
message DeleteAlertRequest {
  // Alert rule name
  string name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// List alerts request
message ListAlertsRequest {
  // Name pattern filter
  string name_pattern = 1;

  // Severity filter
  AlertSeverity severity = 2;

  // Enabled status filter
  bool enabled = 3;

  // Tag filters
  map<string, string> tag_filters = 4;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 5;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 6;
}

// List alerts response
message ListAlertsResponse {
  // Alert rules
  repeated AlertRule rules = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get alert status request
message GetAlertStatusRequest {
  // Alert rule name
  string name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get alert status response
message GetAlertStatusResponse {
  // Alert status
  AlertStatus status = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Alert status
message AlertStatus {
  // Rule name
  string rule_name = 1;

  // Current state
  AlertState state = 2;

  // Last evaluation time
  google.protobuf.Timestamp last_evaluation = 3;

  // Last fired time
  google.protobuf.Timestamp last_fired = 4;

  // Current value
  double current_value = 5;

  // Threshold value
  double threshold_value = 6;

  // Consecutive violations
  int32 consecutive_violations = 7;

  // Active notifications
  repeated ActiveNotification active_notifications = 8;
}

// Alert state enumeration
enum AlertState {
  ALERT_STATE_UNSPECIFIED = 0;
  ALERT_STATE_OK = 1;
  ALERT_STATE_PENDING = 2;
  ALERT_STATE_FIRING = 3;
  ALERT_STATE_RESOLVED = 4;
}

// Active notification
message ActiveNotification {
  // Notification channel
  NotificationChannel channel = 1;

  // Sent time
  google.protobuf.Timestamp sent_at = 2;

  // Status
  NotificationStatus status = 3;
}

// Notification status enumeration
enum NotificationStatus {
  NOTIFICATION_STATUS_UNSPECIFIED = 0;
  NOTIFICATION_STATUS_PENDING = 1;
  NOTIFICATION_STATUS_SENT = 2;
  NOTIFICATION_STATUS_FAILED = 3;
  NOTIFICATION_STATUS_ACKNOWLEDGED = 4;
}

// Export metrics request
message ExportMetricsRequest {
  // Export query
  MetricQuery query = 1;

  // Export format
  ExportFormat format = 2;

  // Export destination
  string destination = 3;

  // Compression options
  CompressionOptions compression = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Export format enumeration
enum ExportFormat {
  EXPORT_FORMAT_UNSPECIFIED = 0;
  EXPORT_FORMAT_JSON = 1;
  EXPORT_FORMAT_CSV = 2;
  EXPORT_FORMAT_PROMETHEUS = 3;
  EXPORT_FORMAT_INFLUXDB = 4;
}

// Compression options
message CompressionOptions {
  // Compression type
  CompressionType type = 1;

  // Compression level (1-9)
  int32 level = 2;
}

// Compression type enumeration
enum CompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  COMPRESSION_TYPE_NONE = 1;
  COMPRESSION_TYPE_GZIP = 2;
  COMPRESSION_TYPE_BZIP2 = 3;
  COMPRESSION_TYPE_XZ = 4;
}

// Export metrics response
message ExportMetricsResponse {
  // Export job ID
  string job_id = 1;

  // Export status
  ExportStatus status = 2;

  // Export location
  string export_location = 3;

  // Number of metrics exported
  int64 metrics_count = 4;

  // Export size in bytes
  int64 export_size_bytes = 5;

  // Error information
  gcommon.common.v1.Error error = 6;
}

// Export status enumeration
enum ExportStatus {
  EXPORT_STATUS_UNSPECIFIED = 0;
  EXPORT_STATUS_PENDING = 1;
  EXPORT_STATUS_IN_PROGRESS = 2;
  EXPORT_STATUS_COMPLETED = 3;
  EXPORT_STATUS_FAILED = 4;
}

// Import metrics request
message ImportMetricsRequest {
  // Import source
  string source = 1;

  // Import format
  ExportFormat format = 2;

  // Import options
  ImportOptions options = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Import options
message ImportOptions {
  // Overwrite existing metrics
  bool overwrite_existing = 1;

  // Validate data before import
  bool validate_data = 2;

  // Batch size for import
  int32 batch_size = 3;

  // Dry run mode
  bool dry_run = 4;
}

// Import metrics response
message ImportMetricsResponse {
  // Import job ID
  string job_id = 1;

  // Import status
  ImportStatus status = 2;

  // Number of metrics imported
  int64 metrics_imported = 3;

  // Number of metrics skipped
  int64 metrics_skipped = 4;

  // Number of metrics failed
  int64 metrics_failed = 5;

  // Error information
  gcommon.common.v1.Error error = 6;
}

// Import status enumeration
enum ImportStatus {
  IMPORT_STATUS_UNSPECIFIED = 0;
  IMPORT_STATUS_PENDING = 1;
  IMPORT_STATUS_IN_PROGRESS = 2;
  IMPORT_STATUS_COMPLETED = 3;
  IMPORT_STATUS_FAILED = 4;
}

// Purge metrics request
message PurgeMetricsRequest {
  // Purge criteria
  PurgeCriteria criteria = 1;

  // Dry run mode
  bool dry_run = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Purge criteria
message PurgeCriteria {
  // Older than duration
  google.protobuf.Duration older_than = 1;

  // Metric name pattern
  string name_pattern = 2;

  // Metric types to purge
  repeated MetricType types = 3;

  // Tag filters
  map<string, string> tag_filters = 4;

  // Size threshold
  int64 size_threshold_bytes = 5;
}

// Purge metrics response
message PurgeMetricsResponse {
  // Number of metrics purged
  int64 metrics_purged = 1;

  // Number of data points purged
  int64 data_points_purged = 2;

  // Storage space freed in bytes
  int64 space_freed_bytes = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Get system metrics request
message GetSystemMetricsRequest {
  // System metric types to retrieve
  repeated SystemMetricType types = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// System metric type enumeration
enum SystemMetricType {
  SYSTEM_METRIC_TYPE_UNSPECIFIED = 0;
  SYSTEM_METRIC_TYPE_CPU = 1;
  SYSTEM_METRIC_TYPE_MEMORY = 2;
  SYSTEM_METRIC_TYPE_DISK = 3;
  SYSTEM_METRIC_TYPE_NETWORK = 4;
  SYSTEM_METRIC_TYPE_PROCESS = 5;
}

// Get system metrics response
message GetSystemMetricsResponse {
  // System metrics
  repeated SystemMetric metrics = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// System metric data
message SystemMetric {
  // Metric type
  SystemMetricType type = 1;

  // Metric data
  MetricData data = 2;

  // System information
  map<string, string> system_info = 3;
}
METRICS_PROTO

echo "Created metrics.proto"

# Create queue.proto
cat > pkg/queue/proto/queue.proto << 'QUEUE_PROTO'
// file: pkg/queue/proto/queue.proto
edition = "2023";

package gcommon.v1.queue;

option go_package = "github.com/jdfalk/gcommon/pkg/queue/proto;queuepb";
option features.(pb.go).api_level = API_HYBRID;

import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/any.proto";
import "google/protobuf/field_mask.proto";
import "pkg/common/proto/common.proto";

// QueueService provides message queuing and pub/sub functionality
service QueueService {
  // Send a message to a queue
  rpc SendMessage(SendMessageRequest) returns (SendMessageResponse);

  // Send multiple messages in batch
  rpc SendMessages(SendMessagesRequest) returns (SendMessagesResponse);

  // Receive a message from a queue
  rpc ReceiveMessage(ReceiveMessageRequest) returns (ReceiveMessageResponse);

  // Receive multiple messages in batch
  rpc ReceiveMessages(ReceiveMessagesRequest) returns (ReceiveMessagesResponse);

  // Acknowledge message processing
  rpc AckMessage(AckMessageRequest) returns (AckMessageResponse);

  // Negative acknowledge message (requeue)
  rpc NackMessage(NackMessageRequest) returns (NackMessageResponse);

  // Publish a message to a topic
  rpc Publish(PublishRequest) returns (PublishResponse);

  // Subscribe to a topic
  rpc Subscribe(SubscribeRequest) returns (stream MessageEvent);

  // Unsubscribe from a topic
  rpc Unsubscribe(UnsubscribeRequest) returns (UnsubscribeResponse);

  // Get message by ID
  rpc GetMessage(GetMessageRequest) returns (GetMessageResponse);

  // List messages in a queue
  rpc ListMessages(ListMessagesRequest) returns (ListMessagesResponse);

  // Get queue statistics
  rpc GetQueueStats(GetQueueStatsRequest) returns (GetQueueStatsResponse);

  // Get subscription statistics
  rpc GetSubscriptionStats(GetSubscriptionStatsRequest) returns (GetSubscriptionStatsResponse);
}

// QueueAdminService provides queue administration and management
service QueueAdminService {
  // Create a queue
  rpc CreateQueue(CreateQueueRequest) returns (CreateQueueResponse);

  // Update a queue
  rpc UpdateQueue(UpdateQueueRequest) returns (UpdateQueueResponse);

  // Delete a queue
  rpc DeleteQueue(DeleteQueueRequest) returns (DeleteQueueResponse);

  // List queues
  rpc ListQueues(ListQueuesRequest) returns (ListQueuesResponse);

  // Create a topic
  rpc CreateTopic(CreateTopicRequest) returns (CreateTopicResponse);

  // Update a topic
  rpc UpdateTopic(UpdateTopicRequest) returns (UpdateTopicResponse);

  // Delete a topic
  rpc DeleteTopic(DeleteTopicRequest) returns (DeleteTopicResponse);

  // List topics
  rpc ListTopics(ListTopicsRequest) returns (ListTopicsResponse);

  // Create a subscription
  rpc CreateSubscription(CreateSubscriptionRequest) returns (CreateSubscriptionResponse);

  // Update a subscription
  rpc UpdateSubscription(UpdateSubscriptionRequest) returns (UpdateSubscriptionResponse);

  // Delete a subscription
  rpc DeleteSubscription(DeleteSubscriptionRequest) returns (DeleteSubscriptionResponse);

  // List subscriptions
  rpc ListSubscriptions(ListSubscriptionsRequest) returns (ListSubscriptionsResponse);

  // Purge messages from a queue
  rpc PurgeQueue(PurgeQueueRequest) returns (PurgeQueueResponse);

  // Get dead letter queue messages
  rpc GetDeadLetterMessages(GetDeadLetterMessagesRequest) returns (GetDeadLetterMessagesResponse);

  // Requeue dead letter messages
  rpc RequeueDeadLetterMessages(RequeueDeadLetterMessagesRequest) returns (RequeueDeadLetterMessagesResponse);

  // Get system health
  rpc GetSystemHealth(GetSystemHealthRequest) returns (GetSystemHealthResponse);
}

// WorkflowService provides workflow orchestration functionality
service WorkflowService {
  // Start a workflow
  rpc StartWorkflow(StartWorkflowRequest) returns (StartWorkflowResponse);

  // Get workflow status
  rpc GetWorkflow(GetWorkflowRequest) returns (GetWorkflowResponse);

  // List workflows
  rpc ListWorkflows(ListWorkflowsRequest) returns (ListWorkflowsResponse);

  // Cancel a workflow
  rpc CancelWorkflow(CancelWorkflowRequest) returns (CancelWorkflowResponse);

  // Pause a workflow
  rpc PauseWorkflow(PauseWorkflowRequest) returns (PauseWorkflowResponse);

  // Resume a workflow
  rpc ResumeWorkflow(ResumeWorkflowRequest) returns (ResumeWorkflowResponse);

  // Complete a task
  rpc CompleteTask(CompleteTaskRequest) returns (CompleteTaskResponse);

  // Fail a task
  rpc FailTask(FailTaskRequest) returns (FailTaskResponse);

  // Get task status
  rpc GetTask(GetTaskRequest) returns (GetTaskResponse);

  // List tasks
  rpc ListTasks(ListTasksRequest) returns (ListTasksResponse);
}

// Send message request
message SendMessageRequest {
  // Queue name
  string queue_name = 1;

  // Message to send
  QueueMessage message = 2;

  // Delivery options
  DeliveryOptions delivery_options = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Queue message
message QueueMessage {
  // Message ID (auto-generated if not provided)
  string id = 1;

  // Message body
  google.protobuf.Any body = 2;

  // Message attributes
  map<string, string> attributes = 3;

  // Message headers
  map<string, string> headers = 4;

  // Message priority (0-255, higher is higher priority)
  int32 priority = 5;

  // Message expiration time
  google.protobuf.Timestamp expires_at = 6;

  // Correlation ID
  string correlation_id = 7;

  // Reply-to queue
  string reply_to = 8;

  // Content type
  string content_type = 9;

  // Content encoding
  string content_encoding = 10;

  // Timestamp when message was created
  google.protobuf.Timestamp created_at = 11;
}

// Delivery options
message DeliveryOptions {
  // Delay before delivery
  google.protobuf.Duration delay = 1;

  // Maximum retry attempts
  int32 max_retries = 2;

  // Retry delay
  google.protobuf.Duration retry_delay = 3;

  // Exponential backoff multiplier
  double backoff_multiplier = 4;

  // Maximum retry delay
  google.protobuf.Duration max_retry_delay = 5;

  // Dead letter queue name
  string dead_letter_queue = 6;

  // Require acknowledgment
  bool require_ack = 7;

  // Acknowledgment timeout
  google.protobuf.Duration ack_timeout = 8;
}

// Send message response
message SendMessageResponse {
  // Message ID
  string message_id = 1;

  // Success status
  bool success = 2;

  // Queue position (if applicable)
  int64 queue_position = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Send messages request (batch)
message SendMessagesRequest {
  // Queue name
  string queue_name = 1;

  // Messages to send
  repeated QueueMessage messages = 2;

  // Default delivery options
  DeliveryOptions delivery_options = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Send messages response (batch)
message SendMessagesResponse {
  // Successfully sent message IDs
  repeated string message_ids = 1;

  // Failed messages with errors
  repeated MessageError failed_messages = 2;

  // Total sent count
  int32 sent_count = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Message error information
message MessageError {
  // Message ID or index
  string message_id = 1;

  // Error message
  string error_message = 2;

  // Error code
  string error_code = 3;
}

// Receive message request
message ReceiveMessageRequest {
  // Queue name
  string queue_name = 1;

  // Receive options
  ReceiveOptions receive_options = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Receive options
message ReceiveOptions {
  // Maximum messages to receive
  int32 max_messages = 1;

  // Visibility timeout
  google.protobuf.Duration visibility_timeout = 2;

  // Wait time for long polling
  google.protobuf.Duration wait_time = 3;

  // Message attributes to include
  repeated string attribute_names = 4;

  // Auto-acknowledge messages
  bool auto_ack = 5;
}

// Receive message response
message ReceiveMessageResponse {
  // Received message
  ReceivedMessage message = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Received message
message ReceivedMessage {
  // Original message
  QueueMessage message = 1;

  // Receipt handle for acknowledgment
  string receipt_handle = 2;

  // Delivery count
  int32 delivery_count = 3;

  // First delivery time
  google.protobuf.Timestamp first_delivered_at = 4;

  // Current delivery time
  google.protobuf.Timestamp delivered_at = 5;

  // Message visibility timeout
  google.protobuf.Timestamp visible_after = 6;
}

// Receive messages request (batch)
message ReceiveMessagesRequest {
  // Queue name
  string queue_name = 1;

  // Receive options
  ReceiveOptions receive_options = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Receive messages response (batch)
message ReceiveMessagesResponse {
  // Received messages
  repeated ReceivedMessage messages = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Acknowledge message request
message AckMessageRequest {
  // Queue name
  string queue_name = 1;

  // Receipt handle
  string receipt_handle = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Acknowledge message response
message AckMessageResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Negative acknowledge message request
message NackMessageRequest {
  // Queue name
  string queue_name = 1;

  // Receipt handle
  string receipt_handle = 2;

  // Requeue delay
  google.protobuf.Duration requeue_delay = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Negative acknowledge message response
message NackMessageResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Publish request
message PublishRequest {
  // Topic name
  string topic_name = 1;

  // Message to publish
  PubSubMessage message = 2;

  // Publish options
  PublishOptions publish_options = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Pub/Sub message
message PubSubMessage {
  // Message ID (auto-generated if not provided)
  string id = 1;

  // Message data
  google.protobuf.Any data = 2;

  // Message attributes
  map<string, string> attributes = 3;

  // Ordering key for ordered delivery
  string ordering_key = 4;

  // Message timestamp
  google.protobuf.Timestamp published_at = 5;
}

// Publish options
message PublishOptions {
  // Ordering required
  bool ordering_required = 1;

  // Batch publish
  bool enable_batching = 2;

  // Batch size
  int32 batch_size = 3;

  // Batch timeout
  google.protobuf.Duration batch_timeout = 4;
}

// Publish response
message PublishResponse {
  // Message ID
  string message_id = 1;

  // Success status
  bool success = 2;

  // Publish timestamp
  google.protobuf.Timestamp published_at = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Subscribe request
message SubscribeRequest {
  // Subscription name
  string subscription_name = 1;

  // Subscribe options
  SubscribeOptions subscribe_options = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Subscribe options
message SubscribeOptions {
  // Maximum outstanding messages
  int32 max_outstanding_messages = 1;

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 2;

  // Flow control settings
  FlowControlSettings flow_control = 3;

  // Acknowledgment deadline
  google.protobuf.Duration ack_deadline = 4;

  // Auto-extend acknowledgment deadline
  bool auto_extend_ack_deadline = 5;
}

// Flow control settings
message FlowControlSettings {
  // Maximum outstanding messages per subscription
  int32 max_outstanding_messages = 1;

  // Maximum outstanding bytes per subscription
  int64 max_outstanding_bytes = 2;

  // Limit exceeded behavior
  FlowControlBehavior limit_exceeded_behavior = 3;
}

// Flow control behavior enumeration
enum FlowControlBehavior {
  FLOW_CONTROL_BEHAVIOR_UNSPECIFIED = 0;
  FLOW_CONTROL_BEHAVIOR_IGNORE = 1;
  FLOW_CONTROL_BEHAVIOR_BLOCK = 2;
  FLOW_CONTROL_BEHAVIOR_SIGNAL_ERROR = 3;
}

// Message event (streaming response)
message MessageEvent {
  // Event type
  MessageEventType event_type = 1;

  // Pub/Sub message (for MESSAGE event)
  ReceivedPubSubMessage message = 2;

  // Error information (for ERROR event)
  gcommon.common.v1.Error error = 3;

  // Status information (for STATUS event)
  SubscriptionStatus status = 4;
}

// Message event type enumeration
enum MessageEventType {
  MESSAGE_EVENT_TYPE_UNSPECIFIED = 0;
  MESSAGE_EVENT_TYPE_MESSAGE = 1;
  MESSAGE_EVENT_TYPE_ERROR = 2;
  MESSAGE_EVENT_TYPE_STATUS = 3;
  MESSAGE_EVENT_TYPE_HEARTBEAT = 4;
}

// Received pub/sub message
message ReceivedPubSubMessage {
  // Original message
  PubSubMessage message = 1;

  // Acknowledgment ID
  string ack_id = 2;

  // Delivery attempt
  int32 delivery_attempt = 3;

  // Delivery timestamp
  google.protobuf.Timestamp delivered_at = 4;

  // Acknowledgment deadline
  google.protobuf.Timestamp ack_deadline = 5;
}

// Subscription status
message SubscriptionStatus {
  // Subscription name
  string subscription_name = 1;

  // Connection status
  ConnectionStatus connection_status = 2;

  // Outstanding messages
  int32 outstanding_messages = 3;

  // Outstanding bytes
  int64 outstanding_bytes = 4;

  // Last activity timestamp
  google.protobuf.Timestamp last_activity = 5;
}

// Connection status enumeration
enum ConnectionStatus {
  CONNECTION_STATUS_UNSPECIFIED = 0;
  CONNECTION_STATUS_CONNECTING = 1;
  CONNECTION_STATUS_CONNECTED = 2;
  CONNECTION_STATUS_DISCONNECTED = 3;
  CONNECTION_STATUS_ERROR = 4;
}

// Unsubscribe request
message UnsubscribeRequest {
  // Subscription name
  string subscription_name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Unsubscribe response
message UnsubscribeResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Get message request
message GetMessageRequest {
  // Queue name
  string queue_name = 1;

  // Message ID
  string message_id = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Get message response
message GetMessageResponse {
  // Message
  QueueMessage message = 1;

  // Message status
  MessageStatus status = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Message status
message MessageStatus {
  // Current state
  MessageState state = 1;

  // Delivery count
  int32 delivery_count = 2;

  // Created timestamp
  google.protobuf.Timestamp created_at = 3;

  // Last delivery timestamp
  google.protobuf.Timestamp last_delivered_at = 4;

  // Visibility timeout
  google.protobuf.Timestamp visible_after = 5;

  // Retry information
  RetryInfo retry_info = 6;
}

// Message state enumeration
enum MessageState {
  MESSAGE_STATE_UNSPECIFIED = 0;
  MESSAGE_STATE_PENDING = 1;
  MESSAGE_STATE_DELIVERED = 2;
  MESSAGE_STATE_ACKNOWLEDGED = 3;
  MESSAGE_STATE_FAILED = 4;
  MESSAGE_STATE_DEAD_LETTER = 5;
  MESSAGE_STATE_EXPIRED = 6;
}

// Retry information
message RetryInfo {
  // Current retry attempt
  int32 current_attempt = 1;

  // Maximum retry attempts
  int32 max_attempts = 2;

  // Next retry time
  google.protobuf.Timestamp next_retry_at = 3;

  // Retry delay
  google.protobuf.Duration retry_delay = 4;

  // Last error message
  string last_error = 5;
}

// List messages request
message ListMessagesRequest {
  // Queue name
  string queue_name = 1;

  // Message state filter
  MessageState state = 2;

  // Time range filter
  google.protobuf.Timestamp start_time = 3;
  google.protobuf.Timestamp end_time = 4;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 5;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 6;
}

// List messages response
message ListMessagesResponse {
  // Messages
  repeated QueueMessage messages = 1;

  // Message statuses
  repeated MessageStatus statuses = 2;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Get queue stats request
message GetQueueStatsRequest {
  // Queue name
  string queue_name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get queue stats response
message GetQueueStatsResponse {
  // Queue statistics
  QueueStats stats = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Queue statistics
message QueueStats {
  // Queue name
  string queue_name = 1;

  // Message counts by state
  map<string, int64> message_counts = 2;

  // Total messages
  int64 total_messages = 3;

  // Messages in flight
  int64 messages_in_flight = 4;

  // Average message size
  int64 avg_message_size_bytes = 5;

  // Total queue size
  int64 total_size_bytes = 6;

  // Oldest message age
  google.protobuf.Duration oldest_message_age = 7;

  // Throughput statistics
  ThroughputStats throughput = 8;

  // Error statistics
  ErrorStats errors = 9;
}

// Throughput statistics
message ThroughputStats {
  // Messages per second (current)
  double messages_per_second = 1;

  // Bytes per second (current)
  double bytes_per_second = 2;

  // Average processing time
  google.protobuf.Duration avg_processing_time = 3;

  // Peak messages per second (last hour)
  double peak_messages_per_second = 4;

  // Peak bytes per second (last hour)
  double peak_bytes_per_second = 5;
}

// Error statistics
message ErrorStats {
  // Total errors
  int64 total_errors = 1;

  // Error rate (errors per second)
  double error_rate = 2;

  // Common error types
  map<string, int64> error_types = 3;

  // Recent errors
  repeated RecentError recent_errors = 4;
}

// Recent error information
message RecentError {
  // Error message
  string message = 1;

  // Error type
  string type = 2;

  // Occurrence count
  int32 count = 3;

  // Last occurrence
  google.protobuf.Timestamp last_occurrence = 4;
}

// Get subscription stats request
message GetSubscriptionStatsRequest {
  // Subscription name
  string subscription_name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get subscription stats response
message GetSubscriptionStatsResponse {
  // Subscription statistics
  SubscriptionStats stats = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Subscription statistics
message SubscriptionStats {
  // Subscription name
  string subscription_name = 1;

  // Topic name
  string topic_name = 2;

  // Active subscribers
  int32 active_subscribers = 3;

  // Total messages delivered
  int64 total_messages_delivered = 4;

  // Messages pending acknowledgment
  int64 messages_pending_ack = 5;

  // Average acknowledgment time
  google.protobuf.Duration avg_ack_time = 6;

  // Delivery statistics
  DeliveryStats delivery = 7;

  // Backlog information
  BacklogInfo backlog = 8;
}

// Delivery statistics
message DeliveryStats {
  // Successful deliveries
  int64 successful_deliveries = 1;

  // Failed deliveries
  int64 failed_deliveries = 2;

  // Duplicate deliveries
  int64 duplicate_deliveries = 3;

  // Average delivery latency
  google.protobuf.Duration avg_delivery_latency = 4;

  // Delivery rate (messages per second)
  double delivery_rate = 5;
}

// Backlog information
message BacklogInfo {
  // Total backlog size
  int64 total_messages = 1;

  // Backlog size in bytes
  int64 total_size_bytes = 2;

  // Oldest undelivered message age
  google.protobuf.Duration oldest_undelivered_age = 3;

  // Estimated processing time
  google.protobuf.Duration estimated_processing_time = 4;
}

// Admin service messages
message CreateQueueRequest {
  // Queue configuration
  QueueConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Queue configuration
message QueueConfig {
  // Queue name
  string name = 1;

  // Queue type
  QueueType type = 2;

  // Maximum message size
  int64 max_message_size_bytes = 3;

  // Message retention period
  google.protobuf.Duration message_retention = 4;

  // Visibility timeout
  google.protobuf.Duration visibility_timeout = 5;

  // Dead letter queue configuration
  DeadLetterQueueConfig dead_letter_queue = 6;

  // Queue attributes
  map<string, string> attributes = 7;

  // Access policy
  AccessPolicy access_policy = 8;
}

// Queue type enumeration
enum QueueType {
  QUEUE_TYPE_UNSPECIFIED = 0;
  QUEUE_TYPE_STANDARD = 1;
  QUEUE_TYPE_FIFO = 2;
  QUEUE_TYPE_PRIORITY = 3;
  QUEUE_TYPE_DELAY = 4;
}

// Dead letter queue configuration
message DeadLetterQueueConfig {
  // Target queue name
  string target_queue = 1;

  // Maximum receive count before moving to DLQ
  int32 max_receive_count = 2;

  // Enable dead letter queue
  bool enabled = 3;
}

// Access policy
message AccessPolicy {
  // Allowed operations
  repeated QueueOperation allowed_operations = 1;

  // Principal identifiers
  repeated string principals = 2;

  // Conditions
  map<string, string> conditions = 3;
}

// Queue operation enumeration
enum QueueOperation {
  QUEUE_OPERATION_UNSPECIFIED = 0;
  QUEUE_OPERATION_SEND_MESSAGE = 1;
  QUEUE_OPERATION_RECEIVE_MESSAGE = 2;
  QUEUE_OPERATION_DELETE_MESSAGE = 3;
  QUEUE_OPERATION_GET_QUEUE_ATTRIBUTES = 4;
  QUEUE_OPERATION_SET_QUEUE_ATTRIBUTES = 5;
}

// Create queue response
message CreateQueueResponse {
  // Success status
  bool success = 1;

  // Created queue information
  QueueInfo queue = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Queue information
message QueueInfo {
  // Queue configuration
  QueueConfig config = 1;

  // Queue statistics
  QueueStats stats = 2;

  // Creation time
  google.protobuf.Timestamp created_at = 3;

  // Last updated time
  google.protobuf.Timestamp updated_at = 4;

  // Queue status
  QueueStatus status = 5;
}

// Queue status enumeration
enum QueueStatus {
  QUEUE_STATUS_UNSPECIFIED = 0;
  QUEUE_STATUS_ACTIVE = 1;
  QUEUE_STATUS_INACTIVE = 2;
  QUEUE_STATUS_DELETING = 3;
  QUEUE_STATUS_ERROR = 4;
}

// Update queue request
message UpdateQueueRequest {
  // Queue name
  string name = 1;

  // Updated configuration
  QueueConfig config = 2;

  // Field mask for partial updates
  google.protobuf.FieldMask update_mask = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Update queue response
message UpdateQueueResponse {
  // Success status
  bool success = 1;

  // Updated queue information
  QueueInfo queue = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete queue request
message DeleteQueueRequest {
  // Queue name
  string name = 1;

  // Force delete even if not empty
  bool force = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// List queues request
message ListQueuesRequest {
  // Name pattern filter
  string name_pattern = 1;

  // Queue type filter
  QueueType type = 2;

  // Status filter
  QueueStatus status = 3;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// List queues response
message ListQueuesResponse {
  // Queue information
  repeated QueueInfo queues = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Create topic request
message CreateTopicRequest {
  // Topic configuration
  TopicConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Topic configuration
message TopicConfig {
  // Topic name
  string name = 1;

  // Message retention period
  google.protobuf.Duration message_retention = 2;

  // Partition count
  int32 partition_count = 3;

  // Replication factor
  int32 replication_factor = 4;

  // Topic attributes
  map<string, string> attributes = 5;

  // Schema configuration
  SchemaConfig schema = 6;

  // Access policy
  AccessPolicy access_policy = 7;
}

// Schema configuration
message SchemaConfig {
  // Schema type
  SchemaType type = 1;

  // Schema definition
  string definition = 2;

  // Schema version
  string version = 3;

  // Backward compatibility
  bool backward_compatible = 4;
}

// Schema type enumeration
enum SchemaType {
  SCHEMA_TYPE_UNSPECIFIED = 0;
  SCHEMA_TYPE_AVRO = 1;
  SCHEMA_TYPE_JSON = 2;
  SCHEMA_TYPE_PROTOBUF = 3;
}

// Create topic response
message CreateTopicResponse {
  // Success status
  bool success = 1;

  // Created topic information
  TopicInfo topic = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Topic information
message TopicInfo {
  // Topic configuration
  TopicConfig config = 1;

  // Topic statistics
  TopicStats stats = 2;

  // Creation time
  google.protobuf.Timestamp created_at = 3;

  // Last updated time
  google.protobuf.Timestamp updated_at = 4;

  // Topic status
  TopicStatus status = 5;
}

// Topic statistics
message TopicStats {
  // Total messages
  int64 total_messages = 1;

  // Total size in bytes
  int64 total_size_bytes = 2;

  // Messages per second
  double messages_per_second = 3;

  // Active subscriptions
  int32 active_subscriptions = 4;

  // Partition statistics
  repeated PartitionStats partitions = 5;
}

// Partition statistics
message PartitionStats {
  // Partition ID
  int32 partition_id = 1;

  // Message count
  int64 message_count = 2;

  // Size in bytes
  int64 size_bytes = 3;

  // Leader replica
  string leader_replica = 4;

  // Lag information
  int64 lag = 5;
}

// Topic status enumeration
enum TopicStatus {
  TOPIC_STATUS_UNSPECIFIED = 0;
  TOPIC_STATUS_ACTIVE = 1;
  TOPIC_STATUS_INACTIVE = 2;
  TOPIC_STATUS_DELETING = 3;
  TOPIC_STATUS_ERROR = 4;
}

// Update topic request
message UpdateTopicRequest {
  // Topic name
  string name = 1;

  // Updated configuration
  TopicConfig config = 2;

  // Field mask for partial updates
  google.protobuf.FieldMask update_mask = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Update topic response
message UpdateTopicResponse {
  // Success status
  bool success = 1;

  // Updated topic information
  TopicInfo topic = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete topic request
message DeleteTopicRequest {
  // Topic name
  string name = 1;

  // Force delete even with active subscriptions
  bool force = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// List topics request
message ListTopicsRequest {
  // Name pattern filter
  string name_pattern = 1;

  // Status filter
  TopicStatus status = 2;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// List topics response
message ListTopicsResponse {
  // Topic information
  repeated TopicInfo topics = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Create subscription request
message CreateSubscriptionRequest {
  // Subscription configuration
  SubscriptionConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Subscription configuration
message SubscriptionConfig {
  // Subscription name
  string name = 1;

  // Topic name
  string topic_name = 2;

  // Acknowledgment deadline
  google.protobuf.Duration ack_deadline = 3;

  // Message retention duration
  google.protobuf.Duration message_retention = 4;

  // Retry policy
  RetryPolicy retry_policy = 5;

  // Dead letter policy
  DeadLetterPolicy dead_letter_policy = 6;

  // Filter expression
  string filter = 7;

  // Push configuration
  PushConfig push_config = 8;

  // Subscription attributes
  map<string, string> attributes = 9;
}

// Retry policy
message RetryPolicy {
  // Minimum delay between retries
  google.protobuf.Duration minimum_backoff = 1;

  // Maximum delay between retries
  google.protobuf.Duration maximum_backoff = 2;

  // Maximum retry attempts
  int32 maximum_attempts = 3;

  // Backoff multiplier
  double backoff_multiplier = 4;
}

// Dead letter policy
message DeadLetterPolicy {
  // Dead letter topic
  string dead_letter_topic = 1;

  // Maximum delivery attempts
  int32 max_delivery_attempts = 2;
}

// Push configuration
message PushConfig {
  // Push endpoint URL
  string push_endpoint = 1;

  // Authentication configuration
  AuthConfig auth_config = 2;

  // Push attributes
  map<string, string> attributes = 3;
}

// Authentication configuration
message AuthConfig {
  // Authentication type
  AuthType auth_type = 1;

  // Token or credentials
  string token = 2;

  // Additional auth parameters
  map<string, string> parameters = 3;
}

// Authentication type enumeration
enum AuthType {
  AUTH_TYPE_UNSPECIFIED = 0;
  AUTH_TYPE_NONE = 1;
  AUTH_TYPE_BASIC = 2;
  AUTH_TYPE_BEARER = 3;
  AUTH_TYPE_OAUTH2 = 4;
}

// Create subscription response
message CreateSubscriptionResponse {
  // Success status
  bool success = 1;

  // Created subscription information
  SubscriptionInfo subscription = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Subscription information
message SubscriptionInfo {
  // Subscription configuration
  SubscriptionConfig config = 1;

  // Subscription statistics
  SubscriptionStats stats = 2;

  // Creation time
  google.protobuf.Timestamp created_at = 3;

  // Last updated time
  google.protobuf.Timestamp updated_at = 4;

  // Subscription status
  SubscriptionStatus status = 5;
}

// Update subscription request
message UpdateSubscriptionRequest {
  // Subscription name
  string name = 1;

  // Updated configuration
  SubscriptionConfig config = 2;

  // Field mask for partial updates
  google.protobuf.FieldMask update_mask = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Update subscription response
message UpdateSubscriptionResponse {
  // Success status
  bool success = 1;

  // Updated subscription information
  SubscriptionInfo subscription = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Delete subscription request
message DeleteSubscriptionRequest {
  // Subscription name
  string name = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// List subscriptions request
message ListSubscriptionsRequest {
  // Topic name filter
  string topic_name = 1;

  // Name pattern filter
  string name_pattern = 2;

  // Status filter
  SubscriptionStatus status = 3;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// List subscriptions response
message ListSubscriptionsResponse {
  // Subscription information
  repeated SubscriptionInfo subscriptions = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Purge queue request
message PurgeQueueRequest {
  // Queue name
  string queue_name = 1;

  // Purge criteria
  PurgeQueueCriteria criteria = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Purge queue criteria
message PurgeQueueCriteria {
  // Purge all messages
  bool purge_all = 1;

  // Purge messages older than
  google.protobuf.Duration older_than = 2;

  // Purge by message state
  repeated MessageState states = 3;

  // Purge by attributes
  map<string, string> attribute_filters = 4;
}

// Purge queue response
message PurgeQueueResponse {
  // Number of messages purged
  int64 messages_purged = 1;

  // Success status
  bool success = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get dead letter messages request
message GetDeadLetterMessagesRequest {
  // Dead letter queue name
  string queue_name = 1;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Get dead letter messages response
message GetDeadLetterMessagesResponse {
  // Dead letter messages
  repeated DeadLetterMessage messages = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Dead letter message
message DeadLetterMessage {
  // Original message
  QueueMessage message = 1;

  // Source queue
  string source_queue = 2;

  // Failure reason
  string failure_reason = 3;

  // Number of delivery attempts
  int32 delivery_attempts = 4;

  // First failure time
  google.protobuf.Timestamp first_failed_at = 5;

  // Last failure time
  google.protobuf.Timestamp last_failed_at = 6;
}

// Requeue dead letter messages request
message RequeueDeadLetterMessagesRequest {
  // Dead letter queue name
  string queue_name = 1;

  // Target queue (optional, defaults to original source queue)
  string target_queue = 2;

  // Message IDs to requeue (optional, defaults to all)
  repeated string message_ids = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Requeue dead letter messages response
message RequeueDeadLetterMessagesResponse {
  // Number of messages requeued
  int64 messages_requeued = 1;

  // Number of messages failed to requeue
  int64 messages_failed = 2;

  // Success status
  bool success = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Get system health request
message GetSystemHealthRequest {
  // Health check types to include
  repeated HealthCheckType check_types = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Health check type enumeration
enum HealthCheckType {
  HEALTH_CHECK_TYPE_UNSPECIFIED = 0;
  HEALTH_CHECK_TYPE_STORAGE = 1;
  HEALTH_CHECK_TYPE_NETWORK = 2;
  HEALTH_CHECK_TYPE_MEMORY = 3;
  HEALTH_CHECK_TYPE_CPU = 4;
  HEALTH_CHECK_TYPE_DISK = 5;
}

// Get system health response
message GetSystemHealthResponse {
  // Overall health status
  HealthStatus overall_status = 1;

  // Individual health checks
  repeated HealthCheck health_checks = 2;

  // System metrics
  SystemMetrics metrics = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Health status enumeration
enum HealthStatus {
  HEALTH_STATUS_UNSPECIFIED = 0;
  HEALTH_STATUS_HEALTHY = 1;
  HEALTH_STATUS_DEGRADED = 2;
  HEALTH_STATUS_UNHEALTHY = 3;
}

// Health check
message HealthCheck {
  // Check type
  HealthCheckType type = 1;

  // Check status
  HealthStatus status = 2;

  // Check message
  string message = 3;

  // Check timestamp
  google.protobuf.Timestamp timestamp = 4;

  // Check duration
  google.protobuf.Duration duration = 5;
}

// System metrics
message SystemMetrics {
  // CPU usage percentage
  double cpu_usage_percent = 1;

  // Memory usage percentage
  double memory_usage_percent = 2;

  // Disk usage percentage
  double disk_usage_percent = 3;

  // Network I/O statistics
  NetworkIOStats network_io = 4;

  // Queue system metrics
  QueueSystemMetrics queue_metrics = 5;
}

// Network I/O statistics
message NetworkIOStats {
  // Bytes received per second
  double bytes_received_per_sec = 1;

  // Bytes sent per second
  double bytes_sent_per_sec = 2;

  // Packets received per second
  double packets_received_per_sec = 3;

  // Packets sent per second
  double packets_sent_per_sec = 4;
}

// Queue system metrics
message QueueSystemMetrics {
  // Total active queues
  int32 total_queues = 1;

  // Total active topics
  int32 total_topics = 2;

  // Total active subscriptions
  int32 total_subscriptions = 3;

  // Total messages in system
  int64 total_messages = 4;

  // Messages per second
  double messages_per_second = 5;

  // Storage usage in bytes
  int64 storage_usage_bytes = 6;
}

// Workflow service messages
message StartWorkflowRequest {
  // Workflow definition
  WorkflowDefinition workflow = 1;

  // Workflow input data
  google.protobuf.Any input_data = 2;

  // Workflow options
  WorkflowOptions options = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Workflow definition
message WorkflowDefinition {
  // Workflow name
  string name = 1;

  // Workflow version
  string version = 2;

  // Workflow description
  string description = 3;

  // Workflow tasks
  repeated TaskDefinition tasks = 4;

  // Workflow configuration
  WorkflowConfig config = 5;
}

// Task definition
message TaskDefinition {
  // Task name
  string name = 1;

  // Task type
  TaskType type = 2;

  // Task configuration
  google.protobuf.Any config = 3;

  // Task dependencies
  repeated string dependencies = 4;

  // Task timeout
  google.protobuf.Duration timeout = 5;

  // Retry policy
  TaskRetryPolicy retry_policy = 6;
}

// Task type enumeration
enum TaskType {
  TASK_TYPE_UNSPECIFIED = 0;
  TASK_TYPE_HTTP = 1;
  TASK_TYPE_QUEUE = 2;
  TASK_TYPE_FUNCTION = 3;
  TASK_TYPE_CONDITION = 4;
  TASK_TYPE_LOOP = 5;
  TASK_TYPE_PARALLEL = 6;
}

// Task retry policy
message TaskRetryPolicy {
  // Maximum retry attempts
  int32 max_attempts = 1;

  // Initial retry delay
  google.protobuf.Duration initial_delay = 2;

  // Backoff multiplier
  double backoff_multiplier = 3;

  // Maximum retry delay
  google.protobuf.Duration max_delay = 4;
}

// Workflow configuration
message WorkflowConfig {
  // Workflow timeout
  google.protobuf.Duration timeout = 1;

  // Execution mode
  ExecutionMode execution_mode = 2;

  // Error handling strategy
  ErrorHandlingStrategy error_strategy = 3;

  // Workflow attributes
  map<string, string> attributes = 4;
}

// Execution mode enumeration
enum ExecutionMode {
  EXECUTION_MODE_UNSPECIFIED = 0;
  EXECUTION_MODE_SEQUENTIAL = 1;
  EXECUTION_MODE_PARALLEL = 2;
  EXECUTION_MODE_CONDITIONAL = 3;
}

// Error handling strategy enumeration
enum ErrorHandlingStrategy {
  ERROR_HANDLING_STRATEGY_UNSPECIFIED = 0;
  ERROR_HANDLING_STRATEGY_FAIL_FAST = 1;
  ERROR_HANDLING_STRATEGY_CONTINUE = 2;
  ERROR_HANDLING_STRATEGY_COMPENSATE = 3;
}

// Workflow options
message WorkflowOptions {
  // Workflow ID (auto-generated if not provided)
  string workflow_id = 1;

  // Priority
  int32 priority = 2;

  // Start delay
  google.protobuf.Duration start_delay = 3;

  // Scheduled start time
  google.protobuf.Timestamp scheduled_start = 4;

  // Workflow tags
  map<string, string> tags = 5;
}

// Start workflow response
message StartWorkflowResponse {
  // Workflow ID
  string workflow_id = 1;

  // Workflow status
  WorkflowStatus status = 2;

  // Success status
  bool success = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Get workflow request
message GetWorkflowRequest {
  // Workflow ID
  string workflow_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get workflow response
message GetWorkflowResponse {
  // Workflow information
  WorkflowInfo workflow = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Workflow information
message WorkflowInfo {
  // Workflow ID
  string workflow_id = 1;

  // Workflow definition
  WorkflowDefinition definition = 2;

  // Workflow status
  WorkflowStatus status = 3;

  // Input data
  google.protobuf.Any input_data = 4;

  // Output data
  google.protobuf.Any output_data = 5;

  // Execution history
  repeated TaskExecution task_executions = 6;

  // Created timestamp
  google.protobuf.Timestamp created_at = 7;

  // Started timestamp
  google.protobuf.Timestamp started_at = 8;

  // Completed timestamp
  google.protobuf.Timestamp completed_at = 9;
}

// Workflow status enumeration
enum WorkflowStatus {
  WORKFLOW_STATUS_UNSPECIFIED = 0;
  WORKFLOW_STATUS_PENDING = 1;
  WORKFLOW_STATUS_RUNNING = 2;
  WORKFLOW_STATUS_PAUSED = 3;
  WORKFLOW_STATUS_COMPLETED = 4;
  WORKFLOW_STATUS_FAILED = 5;
  WORKFLOW_STATUS_CANCELLED = 6;
}

// Task execution information
message TaskExecution {
  // Task name
  string task_name = 1;

  // Execution status
  TaskStatus status = 2;

  // Input data
  google.protobuf.Any input_data = 3;

  // Output data
  google.protobuf.Any output_data = 4;

  // Error information
  string error_message = 5;

  // Attempt number
  int32 attempt = 6;

  // Started timestamp
  google.protobuf.Timestamp started_at = 7;

  // Completed timestamp
  google.protobuf.Timestamp completed_at = 8;

  // Execution duration
  google.protobuf.Duration duration = 9;
}

// Task status enumeration
enum TaskStatus {
  TASK_STATUS_UNSPECIFIED = 0;
  TASK_STATUS_PENDING = 1;
  TASK_STATUS_RUNNING = 2;
  TASK_STATUS_COMPLETED = 3;
  TASK_STATUS_FAILED = 4;
  TASK_STATUS_SKIPPED = 5;
  TASK_STATUS_CANCELLED = 6;
}

// List workflows request
message ListWorkflowsRequest {
  // Status filter
  WorkflowStatus status = 1;

  // Name pattern filter
  string name_pattern = 2;

  // Tag filters
  map<string, string> tag_filters = 3;

  // Time range filter
  google.protobuf.Timestamp start_time = 4;
  google.protobuf.Timestamp end_time = 5;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 6;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 7;
}

// List workflows response
message ListWorkflowsResponse {
  // Workflow information
  repeated WorkflowInfo workflows = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Cancel workflow request
message CancelWorkflowRequest {
  // Workflow ID
  string workflow_id = 1;

  // Reason for cancellation
  string reason = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Cancel workflow response
message CancelWorkflowResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Pause workflow request
message PauseWorkflowRequest {
  // Workflow ID
  string workflow_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Pause workflow response
message PauseWorkflowResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Resume workflow request
message ResumeWorkflowRequest {
  // Workflow ID
  string workflow_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Resume workflow response
message ResumeWorkflowResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Complete task request
message CompleteTaskRequest {
  // Workflow ID
  string workflow_id = 1;

  // Task name
  string task_name = 2;

  // Task output data
  google.protobuf.Any output_data = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Complete task response
message CompleteTaskResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Fail task request
message FailTaskRequest {
  // Workflow ID
  string workflow_id = 1;

  // Task name
  string task_name = 2;

  // Error message
  string error_message = 3;

  // Whether to retry the task
  bool retry = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Fail task response
message FailTaskResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Get task request
message GetTaskRequest {
  // Workflow ID
  string workflow_id = 1;

  // Task name
  string task_name = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Get task response
message GetTaskResponse {
  // Task execution information
  TaskExecution task_execution = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// List tasks request
message ListTasksRequest {
  // Workflow ID
  string workflow_id = 1;

  // Status filter
  TaskStatus status = 2;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// List tasks response
message ListTasksResponse {
  // Task executions
  repeated TaskExecution task_executions = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}
QUEUE_PROTO

echo "Created queue.proto"

# Create web.proto
cat > pkg/web/proto/web.proto << 'WEB_PROTO'
// file: pkg/web/proto/web.proto
edition = "2023";

package gcommon.v1.web;

option go_package = "github.com/jdfalk/gcommon/pkg/web/proto;webpb";
option features.(pb.go).api_level = API_HYBRID;

import "google/protobuf/timestamp.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/any.proto";
import "google/protobuf/field_mask.proto";
import "pkg/common/proto/common.proto";

// WebService provides HTTP server and web framework functionality
service WebService {
  // Create an HTTP server
  rpc CreateServer(CreateServerRequest) returns (CreateServerResponse);

  // Start a server
  rpc StartServer(StartServerRequest) returns (StartServerResponse);

  // Stop a server
  rpc StopServer(StopServerRequest) returns (StopServerResponse);

  // Get server status
  rpc GetServerStatus(GetServerStatusRequest) returns (GetServerStatusResponse);

  // List servers
  rpc ListServers(ListServersRequest) returns (ListServersResponse);

  // Register a route
  rpc RegisterRoute(RegisterRouteRequest) returns (RegisterRouteResponse);

  // Unregister a route
  rpc UnregisterRoute(UnregisterRouteRequest) returns (UnregisterRouteResponse);

  // List routes
  rpc ListRoutes(ListRoutesRequest) returns (ListRoutesResponse);

  // Add middleware
  rpc AddMiddleware(AddMiddlewareRequest) returns (AddMiddlewareResponse);

  // Remove middleware
  rpc RemoveMiddleware(RemoveMiddlewareRequest) returns (RemoveMiddlewareResponse);

  // List middleware
  rpc ListMiddleware(ListMiddlewareRequest) returns (ListMiddlewareResponse);

  // Get server metrics
  rpc GetServerMetrics(GetServerMetricsRequest) returns (GetServerMetricsResponse);

  // Get route metrics
  rpc GetRouteMetrics(GetRouteMetricsRequest) returns (GetRouteMetricsResponse);

  // Handle HTTP request
  rpc HandleRequest(HandleRequestRequest) returns (HandleRequestResponse);

  // Stream server events
  rpc StreamServerEvents(StreamServerEventsRequest) returns (stream ServerEvent);
}

// WebAdminService provides web server administration
service WebAdminService {
  // Configure global settings
  rpc ConfigureGlobal(ConfigureGlobalRequest) returns (ConfigureGlobalResponse);

  // Update server configuration
  rpc UpdateServerConfig(UpdateServerConfigRequest) returns (UpdateServerConfigResponse);

  // Get server logs
  rpc GetServerLogs(GetServerLogsRequest) returns (GetServerLogsResponse);

  // Get access logs
  rpc GetAccessLogs(GetAccessLogsRequest) returns (GetAccessLogsResponse);

  // Reload server configuration
  rpc ReloadServerConfig(ReloadServerConfigRequest) returns (ReloadServerConfigResponse);

  // Get SSL certificate info
  rpc GetSSLCertificateInfo(GetSSLCertificateInfoRequest) returns (GetSSLCertificateInfoResponse);

  // Update SSL certificate
  rpc UpdateSSLCertificate(UpdateSSLCertificateRequest) returns (UpdateSSLCertificateResponse);

  // Get server health
  rpc GetServerHealth(GetServerHealthRequest) returns (GetServerHealthResponse);

  // Export server configuration
  rpc ExportServerConfig(ExportServerConfigRequest) returns (ExportServerConfigResponse);

  // Import server configuration
  rpc ImportServerConfig(ImportServerConfigRequest) returns (ImportServerConfigResponse);
}

// Create server request
message CreateServerRequest {
  // Server configuration
  ServerConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Server configuration
message ServerConfig {
  // Server name
  string name = 1;

  // Server address
  string address = 2;

  // Server port
  int32 port = 3;

  // TLS configuration
  TLSConfig tls_config = 4;

  // HTTP configuration
  HTTPConfig http_config = 5;

  // Timeout configuration
  TimeoutConfig timeout_config = 6;

  // Security configuration
  SecurityConfig security_config = 7;

  // Middleware configurations
  repeated MiddlewareConfig middleware = 8;

  // Static file serving
  StaticFileConfig static_config = 9;

  // Server attributes
  map<string, string> attributes = 10;
}

// TLS configuration
message TLSConfig {
  // Enable TLS
  bool enabled = 1;

  // Certificate file path
  string cert_file = 2;

  // Private key file path
  string key_file = 3;

  // CA certificate file path
  string ca_file = 4;

  // Minimum TLS version
  string min_version = 5;

  // Maximum TLS version
  string max_version = 6;

  // Cipher suites
  repeated string cipher_suites = 7;

  // Client certificate verification
  ClientCertVerification client_cert_verification = 8;

  // Certificate auto-renewal
  bool auto_renewal = 9;
}

// Client certificate verification enumeration
enum ClientCertVerification {
  CLIENT_CERT_VERIFICATION_UNSPECIFIED = 0;
  CLIENT_CERT_VERIFICATION_NONE = 1;
  CLIENT_CERT_VERIFICATION_REQUEST = 2;
  CLIENT_CERT_VERIFICATION_REQUIRE = 3;
}

// HTTP configuration
message HTTPConfig {
  // Maximum header size
  int32 max_header_size_bytes = 1;

  // Maximum body size
  int64 max_body_size_bytes = 2;

  // Enable HTTP/2
  bool enable_http2 = 3;

  // Enable compression
  bool enable_compression = 4;

  // Compression level
  int32 compression_level = 5;

  // Compression types
  repeated string compression_types = 6;

  // CORS configuration
  CORSConfig cors_config = 7;

  // Request ID header
  string request_id_header = 8;

  // Enable keep-alive
  bool enable_keep_alive = 9;

  // Keep-alive timeout
  google.protobuf.Duration keep_alive_timeout = 10;
}

// CORS configuration
message CORSConfig {
  // Enable CORS
  bool enabled = 1;

  // Allowed origins
  repeated string allowed_origins = 2;

  // Allowed methods
  repeated string allowed_methods = 3;

  // Allowed headers
  repeated string allowed_headers = 4;

  // Exposed headers
  repeated string exposed_headers = 5;

  // Allow credentials
  bool allow_credentials = 6;

  // Max age
  google.protobuf.Duration max_age = 7;
}

// Timeout configuration
message TimeoutConfig {
  // Read timeout
  google.protobuf.Duration read_timeout = 1;

  // Write timeout
  google.protobuf.Duration write_timeout = 2;

  // Idle timeout
  google.protobuf.Duration idle_timeout = 3;

  // Request timeout
  google.protobuf.Duration request_timeout = 4;

  // Shutdown timeout
  google.protobuf.Duration shutdown_timeout = 5;
}

// Security configuration
message SecurityConfig {
  // Rate limiting
  RateLimitConfig rate_limit = 1;

  // IP filtering
  IPFilterConfig ip_filter = 2;

  // Authentication configuration
  AuthenticationConfig authentication = 3;

  // Security headers
  SecurityHeadersConfig security_headers = 4;

  // Request validation
  RequestValidationConfig request_validation = 5;
}

// Rate limiting configuration
message RateLimitConfig {
  // Enable rate limiting
  bool enabled = 1;

  // Requests per second
  int32 requests_per_second = 2;

  // Burst size
  int32 burst_size = 3;

  // Rate limit strategy
  RateLimitStrategy strategy = 4;

  // Rate limit key extractor
  string key_extractor = 5;

  // Skip conditions
  repeated string skip_conditions = 6;
}

// Rate limit strategy enumeration
enum RateLimitStrategy {
  RATE_LIMIT_STRATEGY_UNSPECIFIED = 0;
  RATE_LIMIT_STRATEGY_TOKEN_BUCKET = 1;
  RATE_LIMIT_STRATEGY_FIXED_WINDOW = 2;
  RATE_LIMIT_STRATEGY_SLIDING_WINDOW = 3;
  RATE_LIMIT_STRATEGY_LEAKY_BUCKET = 4;
}

// IP filtering configuration
message IPFilterConfig {
  // Enable IP filtering
  bool enabled = 1;

  // Allowed IP addresses/ranges
  repeated string allowed_ips = 2;

  // Blocked IP addresses/ranges
  repeated string blocked_ips = 3;

  // Filter mode
  IPFilterMode mode = 4;

  // Trusted proxies
  repeated string trusted_proxies = 5;
}

// IP filter mode enumeration
enum IPFilterMode {
  IP_FILTER_MODE_UNSPECIFIED = 0;
  IP_FILTER_MODE_WHITELIST = 1;
  IP_FILTER_MODE_BLACKLIST = 2;
}

// Authentication configuration
message AuthenticationConfig {
  // Enable authentication
  bool enabled = 1;

  // Authentication schemes
  repeated AuthScheme schemes = 2;

  // Default scheme
  string default_scheme = 3;

  // Skip paths
  repeated string skip_paths = 4;

  // JWT configuration
  JWTConfig jwt_config = 5;

  // Basic auth configuration
  BasicAuthConfig basic_auth_config = 6;
}

// Authentication scheme
message AuthScheme {
  // Scheme name
  string name = 1;

  // Scheme type
  AuthSchemeType type = 2;

  // Scheme configuration
  google.protobuf.Any config = 3;

  // Enabled status
  bool enabled = 4;
}

// Authentication scheme type enumeration
enum AuthSchemeType {
  AUTH_SCHEME_TYPE_UNSPECIFIED = 0;
  AUTH_SCHEME_TYPE_BASIC = 1;
  AUTH_SCHEME_TYPE_BEARER = 2;
  AUTH_SCHEME_TYPE_JWT = 3;
  AUTH_SCHEME_TYPE_API_KEY = 4;
  AUTH_SCHEME_TYPE_OAUTH2 = 5;
}

// JWT configuration
message JWTConfig {
  // Secret key
  string secret = 1;

  // Public key
  string public_key = 2;

  // Algorithm
  string algorithm = 3;

  // Issuer
  string issuer = 4;

  // Audience
  repeated string audience = 5;

  // Token expiration
  google.protobuf.Duration expiration = 6;

  // Claims mapping
  map<string, string> claims_mapping = 7;
}

// Basic authentication configuration
message BasicAuthConfig {
  // Realm
  string realm = 1;

  // User credentials
  map<string, string> users = 2;

  // Password hash algorithm
  string hash_algorithm = 3;
}

// Security headers configuration
message SecurityHeadersConfig {
  // Enable security headers
  bool enabled = 1;

  // Content Security Policy
  string content_security_policy = 2;

  // X-Frame-Options
  string x_frame_options = 3;

  // X-Content-Type-Options
  string x_content_type_options = 4;

  // X-XSS-Protection
  string x_xss_protection = 5;

  // Strict-Transport-Security
  string strict_transport_security = 6;

  // Referrer-Policy
  string referrer_policy = 7;

  // Custom headers
  map<string, string> custom_headers = 8;
}

// Request validation configuration
message RequestValidationConfig {
  // Enable request validation
  bool enabled = 1;

  // Maximum request size
  int64 max_request_size_bytes = 2;

  // Allowed content types
  repeated string allowed_content_types = 3;

  // Validate JSON schema
  bool validate_json_schema = 4;

  // JSON schema definitions
  map<string, string> json_schemas = 5;

  // Custom validators
  repeated string custom_validators = 6;
}

// Middleware configuration
message MiddlewareConfig {
  // Middleware name
  string name = 1;

  // Middleware type
  MiddlewareType type = 2;

  // Middleware order/priority
  int32 order = 3;

  // Middleware configuration
  google.protobuf.Any config = 4;

  // Enabled status
  bool enabled = 5;

  // Apply to paths
  repeated string paths = 6;

  // Skip paths
  repeated string skip_paths = 7;
}

// Middleware type enumeration
enum MiddlewareType {
  MIDDLEWARE_TYPE_UNSPECIFIED = 0;
  MIDDLEWARE_TYPE_LOGGING = 1;
  MIDDLEWARE_TYPE_AUTHENTICATION = 2;
  MIDDLEWARE_TYPE_AUTHORIZATION = 3;
  MIDDLEWARE_TYPE_RATE_LIMITING = 4;
  MIDDLEWARE_TYPE_COMPRESSION = 5;
  MIDDLEWARE_TYPE_CORS = 6;
  MIDDLEWARE_TYPE_SECURITY_HEADERS = 7;
  MIDDLEWARE_TYPE_REQUEST_VALIDATION = 8;
  MIDDLEWARE_TYPE_RESPONSE_TRANSFORMATION = 9;
  MIDDLEWARE_TYPE_CUSTOM = 10;
}

// Static file configuration
message StaticFileConfig {
  // Enable static file serving
  bool enabled = 1;

  // Static file directory
  string directory = 2;

  // URL prefix
  string url_prefix = 3;

  // Index files
  repeated string index_files = 4;

  // Enable directory browsing
  bool enable_directory_browsing = 5;

  // Cache control header
  string cache_control = 6;

  // File compression
  bool enable_compression = 7;
}

// Create server response
message CreateServerResponse {
  // Success status
  bool success = 1;

  // Server information
  ServerInfo server = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Server information
message ServerInfo {
  // Server ID
  string server_id = 1;

  // Server configuration
  ServerConfig config = 2;

  // Server status
  ServerStatus status = 3;

  // Server statistics
  ServerStats stats = 4;

  // Creation time
  google.protobuf.Timestamp created_at = 5;

  // Last updated time
  google.protobuf.Timestamp updated_at = 6;
}

// Server status enumeration
enum ServerStatus {
  SERVER_STATUS_UNSPECIFIED = 0;
  SERVER_STATUS_CREATED = 1;
  SERVER_STATUS_STARTING = 2;
  SERVER_STATUS_RUNNING = 3;
  SERVER_STATUS_STOPPING = 4;
  SERVER_STATUS_STOPPED = 5;
  SERVER_STATUS_ERROR = 6;
}

// Server statistics
message ServerStats {
  // Total requests handled
  int64 total_requests = 1;

  // Active connections
  int32 active_connections = 2;

  // Requests per second
  double requests_per_second = 3;

  // Average response time
  google.protobuf.Duration avg_response_time = 4;

  // Error count
  int64 error_count = 5;

  // Bytes sent
  int64 bytes_sent = 6;

  // Bytes received
  int64 bytes_received = 7;

  // Uptime
  google.protobuf.Duration uptime = 8;
}

// Start server request
message StartServerRequest {
  // Server ID
  string server_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Start server response
message StartServerResponse {
  // Success status
  bool success = 1;

  // Server status
  ServerStatus status = 2;

  // Listen address
  string listen_address = 3;

  // Error information
  gcommon.common.v1.Error error = 4;
}

// Stop server request
message StopServerRequest {
  // Server ID
  string server_id = 1;

  // Graceful shutdown timeout
  google.protobuf.Duration graceful_timeout = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Stop server response
message StopServerResponse {
  // Success status
  bool success = 1;

  // Server status
  ServerStatus status = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get server status request
message GetServerStatusRequest {
  // Server ID
  string server_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get server status response
message GetServerStatusResponse {
  // Server information
  ServerInfo server = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// List servers request
message ListServersRequest {
  // Status filter
  ServerStatus status = 1;

  // Name pattern filter
  string name_pattern = 2;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// List servers response
message ListServersResponse {
  // Server information
  repeated ServerInfo servers = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Register route request
message RegisterRouteRequest {
  // Server ID
  string server_id = 1;

  // Route configuration
  RouteConfig route = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Route configuration
message RouteConfig {
  // Route name
  string name = 1;

  // HTTP method
  string method = 2;

  // Route path
  string path = 3;

  // Handler configuration
  HandlerConfig handler = 4;

  // Route middleware
  repeated MiddlewareConfig middleware = 5;

  // Route attributes
  map<string, string> attributes = 6;

  // Route timeout
  google.protobuf.Duration timeout = 7;

  // Enable caching
  bool enable_caching = 8;

  // Cache TTL
  google.protobuf.Duration cache_ttl = 9;
}

// Handler configuration
message HandlerConfig {
  // Handler type
  HandlerType type = 1;

  // Handler configuration
  google.protobuf.Any config = 2;

  // Handler target (URL, function name, etc.)
  string target = 3;

  // Handler options
  map<string, string> options = 4;
}

// Handler type enumeration
enum HandlerType {
  HANDLER_TYPE_UNSPECIFIED = 0;
  HANDLER_TYPE_STATIC = 1;
  HANDLER_TYPE_PROXY = 2;
  HANDLER_TYPE_FUNCTION = 3;
  HANDLER_TYPE_REDIRECT = 4;
  HANDLER_TYPE_TEMPLATE = 5;
  HANDLER_TYPE_WEBSOCKET = 6;
  HANDLER_TYPE_GRPC = 7;
}

// Register route response
message RegisterRouteResponse {
  // Success status
  bool success = 1;

  // Route information
  RouteInfo route = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Route information
message RouteInfo {
  // Route ID
  string route_id = 1;

  // Route configuration
  RouteConfig config = 2;

  // Route statistics
  RouteStats stats = 3;

  // Creation time
  google.protobuf.Timestamp created_at = 4;

  // Last updated time
  google.protobuf.Timestamp updated_at = 5;
}

// Route statistics
message RouteStats {
  // Total requests
  int64 total_requests = 1;

  // Success count
  int64 success_count = 2;

  // Error count
  int64 error_count = 3;

  // Average response time
  google.protobuf.Duration avg_response_time = 4;

  // Response time percentiles
  ResponseTimePercentiles response_time_percentiles = 5;

  // Status code distribution
  map<string, int64> status_codes = 6;

  // Last request time
  google.protobuf.Timestamp last_request_time = 7;
}

// Response time percentiles
message ResponseTimePercentiles {
  // 50th percentile
  google.protobuf.Duration p50 = 1;

  // 90th percentile
  google.protobuf.Duration p90 = 2;

  // 95th percentile
  google.protobuf.Duration p95 = 3;

  // 99th percentile
  google.protobuf.Duration p99 = 4;
}

// Unregister route request
message UnregisterRouteRequest {
  // Server ID
  string server_id = 1;

  // Route ID
  string route_id = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Unregister route response
message UnregisterRouteResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// List routes request
message ListRoutesRequest {
  // Server ID
  string server_id = 1;

  // Method filter
  string method = 2;

  // Path pattern filter
  string path_pattern = 3;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// List routes response
message ListRoutesResponse {
  // Route information
  repeated RouteInfo routes = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Add middleware request
message AddMiddlewareRequest {
  // Server ID
  string server_id = 1;

  // Middleware configuration
  MiddlewareConfig middleware = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Add middleware response
message AddMiddlewareResponse {
  // Success status
  bool success = 1;

  // Middleware information
  MiddlewareInfo middleware = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Middleware information
message MiddlewareInfo {
  // Middleware ID
  string middleware_id = 1;

  // Middleware configuration
  MiddlewareConfig config = 2;

  // Middleware statistics
  MiddlewareStats stats = 3;

  // Creation time
  google.protobuf.Timestamp created_at = 4;

  // Last updated time
  google.protobuf.Timestamp updated_at = 5;
}

// Middleware statistics
message MiddlewareStats {
  // Total executions
  int64 total_executions = 1;

  // Success count
  int64 success_count = 2;

  // Error count
  int64 error_count = 3;

  // Average execution time
  google.protobuf.Duration avg_execution_time = 4;

  // Last execution time
  google.protobuf.Timestamp last_execution_time = 5;
}

// Remove middleware request
message RemoveMiddlewareRequest {
  // Server ID
  string server_id = 1;

  // Middleware ID
  string middleware_id = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Remove middleware response
message RemoveMiddlewareResponse {
  // Success status
  bool success = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// List middleware request
message ListMiddlewareRequest {
  // Server ID
  string server_id = 1;

  // Type filter
  MiddlewareType type = 2;

  // Enabled status filter
  bool enabled = 3;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// List middleware response
message ListMiddlewareResponse {
  // Middleware information
  repeated MiddlewareInfo middleware = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get server metrics request
message GetServerMetricsRequest {
  // Server ID
  string server_id = 1;

  // Metric types to include
  repeated ServerMetricType metric_types = 2;

  // Time range
  google.protobuf.Timestamp start_time = 3;
  google.protobuf.Timestamp end_time = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Server metric type enumeration
enum ServerMetricType {
  SERVER_METRIC_TYPE_UNSPECIFIED = 0;
  SERVER_METRIC_TYPE_REQUESTS = 1;
  SERVER_METRIC_TYPE_RESPONSE_TIME = 2;
  SERVER_METRIC_TYPE_CONNECTIONS = 3;
  SERVER_METRIC_TYPE_ERRORS = 4;
  SERVER_METRIC_TYPE_THROUGHPUT = 5;
}

// Get server metrics response
message GetServerMetricsResponse {
  // Server metrics
  ServerMetrics metrics = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Server metrics
message ServerMetrics {
  // Server ID
  string server_id = 1;

  // Request metrics
  RequestMetrics request_metrics = 2;

  // Response metrics
  ResponseMetrics response_metrics = 3;

  // Connection metrics
  ConnectionMetrics connection_metrics = 4;

  // Error metrics
  ErrorMetrics error_metrics = 5;

  // Resource metrics
  ResourceMetrics resource_metrics = 6;
}

// Request metrics
message RequestMetrics {
  // Total requests
  int64 total_requests = 1;

  // Requests per second
  double requests_per_second = 2;

  // Request rate trend
  repeated DataPoint request_rate_trend = 3;

  // Request size distribution
  SizeDistribution request_size_distribution = 4;

  // HTTP method distribution
  map<string, int64> method_distribution = 5;
}

// Response metrics
message ResponseMetrics {
  // Average response time
  google.protobuf.Duration avg_response_time = 1;

  // Response time percentiles
  ResponseTimePercentiles response_time_percentiles = 2;

  // Response time trend
  repeated DataPoint response_time_trend = 3;

  // Response size distribution
  SizeDistribution response_size_distribution = 4;

  // Status code distribution
  map<string, int64> status_code_distribution = 5;
}

// Connection metrics
message ConnectionMetrics {
  // Active connections
  int32 active_connections = 1;

  // Total connections
  int64 total_connections = 2;

  // Connection rate
  double connections_per_second = 3;

  // Connection duration distribution
  DurationDistribution connection_duration_distribution = 4;

  // Connection state distribution
  map<string, int32> connection_state_distribution = 5;
}

// Error metrics
message ErrorMetrics {
  // Total errors
  int64 total_errors = 1;

  // Error rate
  double error_rate = 2;

  // Error trend
  repeated DataPoint error_trend = 3;

  // Error type distribution
  map<string, int64> error_type_distribution = 4;

  // Recent errors
  repeated RecentError recent_errors = 5;
}

// Resource metrics
message ResourceMetrics {
  // CPU usage percentage
  double cpu_usage_percent = 1;

  // Memory usage in bytes
  int64 memory_usage_bytes = 2;

  // Memory usage percentage
  double memory_usage_percent = 3;

  // Goroutine count
  int32 goroutine_count = 4;

  // GC statistics
  GCStats gc_stats = 5;
}

// GC statistics
message GCStats {
  // Number of GC cycles
  int64 num_gc = 1;

  // Total GC pause time
  google.protobuf.Duration total_pause_time = 2;

  // Average GC pause time
  google.protobuf.Duration avg_pause_time = 3;

  // Memory allocated
  int64 memory_allocated = 4;

  // Memory released
  int64 memory_released = 5;
}

// Data point for trends
message DataPoint {
  // Timestamp
  google.protobuf.Timestamp timestamp = 1;

  // Value
  double value = 2;
}

// Size distribution
message SizeDistribution {
  // Minimum size
  int64 min_size = 1;

  // Maximum size
  int64 max_size = 2;

  // Average size
  double avg_size = 3;

  // Size buckets
  repeated SizeBucket size_buckets = 4;
}

// Size bucket
message SizeBucket {
  // Upper bound
  int64 upper_bound = 1;

  // Count
  int64 count = 2;
}

// Duration distribution
message DurationDistribution {
  // Minimum duration
  google.protobuf.Duration min_duration = 1;

  // Maximum duration
  google.protobuf.Duration max_duration = 2;

  // Average duration
  google.protobuf.Duration avg_duration = 3;

  // Duration buckets
  repeated DurationBucket duration_buckets = 4;
}

// Duration bucket
message DurationBucket {
  // Upper bound
  google.protobuf.Duration upper_bound = 1;

  // Count
  int64 count = 2;
}

// Recent error
message RecentError {
  // Error message
  string message = 1;

  // Error type
  string type = 2;

  // Count
  int32 count = 3;

  // Last occurrence
  google.protobuf.Timestamp last_occurrence = 4;

  // Request path
  string request_path = 5;

  // Status code
  int32 status_code = 6;
}

// Get route metrics request
message GetRouteMetricsRequest {
  // Server ID
  string server_id = 1;

  // Route ID
  string route_id = 2;

  // Time range
  google.protobuf.Timestamp start_time = 3;
  google.protobuf.Timestamp end_time = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Get route metrics response
message GetRouteMetricsResponse {
  // Route metrics
  RouteMetrics metrics = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Route metrics
message RouteMetrics {
  // Route ID
  string route_id = 1;

  // Route path
  string route_path = 2;

  // Request metrics
  RequestMetrics request_metrics = 3;

  // Response metrics
  ResponseMetrics response_metrics = 4;

  // Error metrics
  ErrorMetrics error_metrics = 5;

  // Performance metrics
  PerformanceMetrics performance_metrics = 6;
}

// Performance metrics
message PerformanceMetrics {
  // Throughput (requests per second)
  double throughput = 1;

  // Latency percentiles
  ResponseTimePercentiles latency_percentiles = 2;

  // Cache hit rate
  double cache_hit_rate = 3;

  // Cache miss rate
  double cache_miss_rate = 4;

  // Database query time
  google.protobuf.Duration avg_db_query_time = 5;
}

// Handle request request
message HandleRequestRequest {
  // Server ID
  string server_id = 1;

  // HTTP request
  HTTPRequest request = 2;

  // Request context
  RequestContext context = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// HTTP request
message HTTPRequest {
  // HTTP method
  string method = 1;

  // Request URL
  string url = 2;

  // Request path
  string path = 3;

  // Query parameters
  map<string, string> query_params = 4;

  // HTTP headers
  map<string, string> headers = 5;

  // Request body
  bytes body = 6;

  // Content type
  string content_type = 7;

  // Content length
  int64 content_length = 8;

  // Remote address
  string remote_addr = 9;

  // User agent
  string user_agent = 10;

  // Request ID
  string request_id = 11;
}

// Request context
message RequestContext {
  // User information
  UserInfo user = 1;

  // Session information
  SessionInfo session = 2;

  // Request tracing
  TracingInfo tracing = 3;

  // Request attributes
  map<string, string> attributes = 4;

  // Request timestamp
  google.protobuf.Timestamp timestamp = 5;
}

// User information
message UserInfo {
  // User ID
  string user_id = 1;

  // Username
  string username = 2;

  // User roles
  repeated string roles = 3;

  // User permissions
  repeated string permissions = 4;

  // User attributes
  map<string, string> attributes = 5;
}

// Session information
message SessionInfo {
  // Session ID
  string session_id = 1;

  // Session data
  map<string, string> data = 2;

  // Session creation time
  google.protobuf.Timestamp created_at = 3;

  // Session expiration time
  google.protobuf.Timestamp expires_at = 4;
}

// Tracing information
message TracingInfo {
  // Trace ID
  string trace_id = 1;

  // Span ID
  string span_id = 2;

  // Parent span ID
  string parent_span_id = 3;

  // Sampling decision
  bool sampled = 4;

  // Trace flags
  int32 trace_flags = 5;
}

// Handle request response
message HandleRequestResponse {
  // HTTP response
  HTTPResponse response = 1;

  // Processing time
  google.protobuf.Duration processing_time = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// HTTP response
message HTTPResponse {
  // Status code
  int32 status_code = 1;

  // Status message
  string status_message = 2;

  // Response headers
  map<string, string> headers = 3;

  // Response body
  bytes body = 4;

  // Content type
  string content_type = 5;

  // Content length
  int64 content_length = 6;
}

// Stream server events request
message StreamServerEventsRequest {
  // Server ID
  string server_id = 1;

  // Event types to stream
  repeated ServerEventType event_types = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Server event type enumeration
enum ServerEventType {
  SERVER_EVENT_TYPE_UNSPECIFIED = 0;
  SERVER_EVENT_TYPE_REQUEST = 1;
  SERVER_EVENT_TYPE_RESPONSE = 2;
  SERVER_EVENT_TYPE_ERROR = 3;
  SERVER_EVENT_TYPE_CONNECTION = 4;
  SERVER_EVENT_TYPE_STATUS_CHANGE = 5;
}

// Server event
message ServerEvent {
  // Event ID
  string event_id = 1;

  // Event type
  ServerEventType event_type = 2;

  // Event timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Server ID
  string server_id = 4;

  // Event data
  google.protobuf.Any event_data = 5;

  // Event attributes
  map<string, string> attributes = 6;
}

// Admin service messages
message ConfigureGlobalRequest {
  // Global configuration
  GlobalConfig config = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Global configuration
message GlobalConfig {
  // Default server configuration
  ServerConfig default_server_config = 1;

  // Global security settings
  GlobalSecurityConfig security = 2;

  // Global logging settings
  GlobalLoggingConfig logging = 3;

  // Global monitoring settings
  GlobalMonitoringConfig monitoring = 4;

  // Resource limits
  ResourceLimits resource_limits = 5;
}

// Global security configuration
message GlobalSecurityConfig {
  // Default TLS settings
  TLSConfig default_tls = 1;

  // Security policy
  SecurityPolicy security_policy = 2;

  // Certificate management
  CertificateManagement certificate_management = 3;
}

// Security policy
message SecurityPolicy {
  // Minimum TLS version
  string min_tls_version = 1;

  // Required cipher suites
  repeated string required_cipher_suites = 2;

  // Security headers enforcement
  bool enforce_security_headers = 3;

  // Content type validation
  bool validate_content_types = 4;
}

// Certificate management
message CertificateManagement {
  // Auto-renewal enabled
  bool auto_renewal_enabled = 1;

  // Certificate authority
  string certificate_authority = 2;

  // Renewal threshold
  google.protobuf.Duration renewal_threshold = 3;

  // Certificate storage
  string certificate_storage = 4;
}

// Global logging configuration
message GlobalLoggingConfig {
  // Default log level
  string default_log_level = 1;

  // Access log format
  string access_log_format = 2;

  // Error log format
  string error_log_format = 3;

  // Log rotation
  LogRotationConfig log_rotation = 4;
}

// Log rotation configuration
message LogRotationConfig {
  // Rotation size
  int64 rotation_size_bytes = 1;

  // Rotation interval
  google.protobuf.Duration rotation_interval = 2;

  // Keep files
  int32 keep_files = 3;

  // Compression enabled
  bool compression_enabled = 4;
}

// Global monitoring configuration
message GlobalMonitoringConfig {
  // Metrics collection interval
  google.protobuf.Duration metrics_interval = 1;

  // Health check interval
  google.protobuf.Duration health_check_interval = 2;

  // Performance monitoring
  bool performance_monitoring_enabled = 3;

  // Distributed tracing
  bool distributed_tracing_enabled = 4;
}

// Resource limits
message ResourceLimits {
  // Maximum servers
  int32 max_servers = 1;

  // Maximum routes per server
  int32 max_routes_per_server = 2;

  // Maximum connections per server
  int32 max_connections_per_server = 3;

  // Memory limit per server
  int64 memory_limit_per_server_bytes = 4;

  // CPU limit per server
  double cpu_limit_per_server_cores = 5;
}

// Configure global response
message ConfigureGlobalResponse {
  // Success status
  bool success = 1;

  // Applied configuration
  GlobalConfig config = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Update server config request
message UpdateServerConfigRequest {
  // Server ID
  string server_id = 1;

  // Updated configuration
  ServerConfig config = 2;

  // Field mask for partial updates
  google.protobuf.FieldMask update_mask = 3;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 4;
}

// Update server config response
message UpdateServerConfigResponse {
  // Success status
  bool success = 1;

  // Updated server information
  ServerInfo server = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get server logs request
message GetServerLogsRequest {
  // Server ID
  string server_id = 1;

  // Log level filter
  string log_level = 2;

  // Time range
  google.protobuf.Timestamp start_time = 3;
  google.protobuf.Timestamp end_time = 4;

  // Log message filter
  string message_filter = 5;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 6;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 7;
}

// Get server logs response
message GetServerLogsResponse {
  // Log entries
  repeated LogEntry log_entries = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Log entry
message LogEntry {
  // Timestamp
  google.protobuf.Timestamp timestamp = 1;

  // Log level
  string level = 2;

  // Log message
  string message = 3;

  // Logger name
  string logger = 4;

  // Additional fields
  map<string, string> fields = 5;
}

// Get access logs request
message GetAccessLogsRequest {
  // Server ID
  string server_id = 1;

  // Time range
  google.protobuf.Timestamp start_time = 2;
  google.protobuf.Timestamp end_time = 3;

  // Status code filter
  int32 status_code = 4;

  // Path filter
  string path_filter = 5;

  // Method filter
  string method_filter = 6;

  // Pagination options
  gcommon.common.v1.Pagination pagination = 7;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 8;
}

// Get access logs response
message GetAccessLogsResponse {
  // Access log entries
  repeated AccessLogEntry access_logs = 1;

  // Pagination information
  gcommon.common.v1.Pagination pagination = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Access log entry
message AccessLogEntry {
  // Timestamp
  google.protobuf.Timestamp timestamp = 1;

  // Remote address
  string remote_addr = 2;

  // HTTP method
  string method = 3;

  // Request path
  string path = 4;

  // Status code
  int32 status_code = 5;

  // Response size
  int64 response_size = 6;

  // Response time
  google.protobuf.Duration response_time = 7;

  // User agent
  string user_agent = 8;

  // Referer
  string referer = 9;

  // Request ID
  string request_id = 10;
}

// Reload server config request
message ReloadServerConfigRequest {
  // Server ID
  string server_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Reload server config response
message ReloadServerConfigResponse {
  // Success status
  bool success = 1;

  // Reloaded configuration
  ServerConfig config = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get SSL certificate info request
message GetSSLCertificateInfoRequest {
  // Server ID
  string server_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get SSL certificate info response
message GetSSLCertificateInfoResponse {
  // Certificate information
  CertificateInfo certificate = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Certificate information
message CertificateInfo {
  // Certificate subject
  string subject = 1;

  // Certificate issuer
  string issuer = 2;

  // Not before date
  google.protobuf.Timestamp not_before = 3;

  // Not after date
  google.protobuf.Timestamp not_after = 4;

  // Serial number
  string serial_number = 5;

  // Subject alternative names
  repeated string san = 6;

  // Certificate fingerprint
  string fingerprint = 7;

  // Certificate chain length
  int32 chain_length = 8;
}

// Update SSL certificate request
message UpdateSSLCertificateRequest {
  // Server ID
  string server_id = 1;

  // Certificate data
  string certificate_data = 2;

  // Private key data
  string private_key_data = 3;

  // CA certificate data
  string ca_certificate_data = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Update SSL certificate response
message UpdateSSLCertificateResponse {
  // Success status
  bool success = 1;

  // Updated certificate information
  CertificateInfo certificate = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Get server health request
message GetServerHealthRequest {
  // Server ID
  string server_id = 1;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 2;
}

// Get server health response
message GetServerHealthResponse {
  // Server health status
  ServerHealthStatus health = 1;

  // Error information
  gcommon.common.v1.Error error = 2;
}

// Server health status
message ServerHealthStatus {
  // Overall health
  HealthStatus overall_health = 1;

  // Component health checks
  repeated ComponentHealth component_health = 2;

  // Last health check time
  google.protobuf.Timestamp last_check_time = 3;

  // Health check duration
  google.protobuf.Duration check_duration = 4;
}

// Component health
message ComponentHealth {
  // Component name
  string component = 1;

  // Health status
  HealthStatus status = 2;

  // Health message
  string message = 3;

  // Last check time
  google.protobuf.Timestamp last_check_time = 4;
}

// Health status enumeration
enum HealthStatus {
  HEALTH_STATUS_UNSPECIFIED = 0;
  HEALTH_STATUS_HEALTHY = 1;
  HEALTH_STATUS_DEGRADED = 2;
  HEALTH_STATUS_UNHEALTHY = 3;
}

// Export server config request
message ExportServerConfigRequest {
  // Server ID
  string server_id = 1;

  // Export format
  ConfigExportFormat format = 2;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 3;
}

// Config export format enumeration
enum ConfigExportFormat {
  CONFIG_EXPORT_FORMAT_UNSPECIFIED = 0;
  CONFIG_EXPORT_FORMAT_JSON = 1;
  CONFIG_EXPORT_FORMAT_YAML = 2;
  CONFIG_EXPORT_FORMAT_TOML = 3;
}

// Export server config response
message ExportServerConfigResponse {
  // Exported configuration data
  string config_data = 1;

  // Export format used
  ConfigExportFormat format = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}

// Import server config request
message ImportServerConfigRequest {
  // Server ID
  string server_id = 1;

  // Configuration data
  string config_data = 2;

  // Import format
  ConfigExportFormat format = 3;

  // Merge strategy
  ConfigMergeStrategy merge_strategy = 4;

  // Request metadata
  gcommon.common.v1.RequestMetadata metadata = 5;
}

// Config merge strategy enumeration
enum ConfigMergeStrategy {
  CONFIG_MERGE_STRATEGY_UNSPECIFIED = 0;
  CONFIG_MERGE_STRATEGY_REPLACE = 1;
  CONFIG_MERGE_STRATEGY_MERGE = 2;
  CONFIG_MERGE_STRATEGY_UPDATE = 3;
}

// Import server config response
message ImportServerConfigResponse {
  // Success status
  bool success = 1;

  // Imported server information
  ServerInfo server = 2;

  // Error information
  gcommon.common.v1.Error error = 3;
}
WEB_PROTO

echo "Created web.proto"

# Final completion message
echo ""
echo "✅ All protobuf files have been created successfully!"
echo ""
echo "Created files:"
echo "  - pkg/auth/proto/auth.proto"
echo "  - pkg/cache/proto/cache.proto"
echo "  - pkg/config/proto/config.proto"
echo "  - pkg/db/proto/database.proto"
echo "  - pkg/health/proto/health.proto"
echo "  - pkg/log/proto/log.proto"
echo "  - pkg/metrics/proto/metrics.proto"
echo "  - pkg/queue/proto/queue.proto"
echo "  - pkg/web/proto/web.proto"
echo ""
echo "All protobuf files use:"
echo "  - Edition 2023 syntax"
echo "  - gcommon.v1.{service_name} package naming"
echo "  - Hybrid API support (REST + gRPC)"
echo "  - Comprehensive service definitions"
echo "  - Common types from gcommon.common.v1"
echo ""
echo "Next steps:"
echo "  1. Run this script: bash create_all_protos.sh"
echo "  2. Update generate.sh to include new proto files"
echo "  3. Run generate.sh to compile protobuf files"
echo "  4. Implement service interfaces in Go"

