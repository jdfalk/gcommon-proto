# cache_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 2
- **Messages**: 0
- **Services**: 2
- **Enums**: 0

## Files in this Module

- [cache_admin_service.proto](#cache_admin_service)
- [cache_service.proto](#cache_service)

## Module Dependencies

**This module depends on**:

- [cache_api_1](./cache_api_1.md)
- [cache_api_2](./cache_api_2.md)
- [cache_config](./cache_config.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_api_1](./queue_api_1.md)

---

## Detailed Documentation

### cache_admin_service.proto {#cache_admin_service}

**Path**: `pkg/cache/proto/cache_admin_service.proto` **Package**: `gcommon.v1.cache` **Lines**: 42

**Services** (1): `CacheAdminService`

**Imports** (11):

- `google/protobuf/empty.proto`
- `google/protobuf/go_features.proto`
- `pkg/cache/proto/configure_policy_request.proto` → [cache_config](./cache_config.md#configure_policy_request)
- `pkg/cache/proto/configure_policy_response.proto` → [cache_config](./cache_config.md#configure_policy_response)
- `pkg/cache/proto/create_namespace_request.proto` → [cache_api_1](./cache_api_1.md#create_namespace_request)
- `pkg/cache/proto/create_namespace_response.proto` → [cache_api_1](./cache_api_1.md#create_namespace_response)
- `pkg/cache/proto/delete_namespace_request.proto` → [cache_api_1](./cache_api_1.md#delete_namespace_request)
- `pkg/cache/proto/get_namespace_stats_request.proto` → [cache_api_1](./cache_api_1.md#get_namespace_stats_request)
- `pkg/cache/proto/get_namespace_stats_response.proto` → [cache_api_1](./cache_api_1.md#get_namespace_stats_response)
- `pkg/cache/proto/list_namespaces_request.proto` → [cache_api_1](./cache_api_1.md#list_namespaces_request)
- `pkg/cache/proto/list_namespaces_response.proto` → [cache_api_1](./cache_api_1.md#list_namespaces_response)

#### Source Code

```protobuf
// file: pkg/cache/proto/services/cache_admin_service.proto
// version: 1.0.1
// guid: d7b6285b-2286-46f8-a2aa-5ef8715919f9
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/empty.proto";
import "google/protobuf/go_features.proto";
import "pkg/cache/proto/configure_policy_request.proto";
import "pkg/cache/proto/configure_policy_response.proto";
import "pkg/cache/proto/create_namespace_request.proto";
import "pkg/cache/proto/create_namespace_response.proto";
import "pkg/cache/proto/delete_namespace_request.proto";
import "pkg/cache/proto/get_namespace_stats_request.proto";
import "pkg/cache/proto/get_namespace_stats_response.proto";
import "pkg/cache/proto/list_namespaces_request.proto";
import "pkg/cache/proto/list_namespaces_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * Administrative cache management operations.
 */
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

```

---

### cache_service.proto {#cache_service}

**Path**: `pkg/cache/proto/cache_service.proto` **Package**: `gcommon.v1.cache` **Lines**: 87

**Services** (1): `CacheService`

**Imports** (29):

- `google/protobuf/go_features.proto`
- `pkg/cache/proto/clear_request.proto` → [cache_api_1](./cache_api_1.md#clear_request)
- `pkg/cache/proto/clear_response.proto` → [cache_api_1](./cache_api_1.md#clear_response)
- `pkg/cache/proto/decrement_request.proto` → [cache_api_1](./cache_api_1.md#decrement_request)
- `pkg/cache/proto/decrement_response.proto` → [cache_api_1](./cache_api_1.md#decrement_response)
- `pkg/cache/proto/delete_multiple_request.proto` → [cache_api_1](./cache_api_1.md#delete_multiple_request)
- `pkg/cache/proto/delete_multiple_response.proto` → [cache_api_1](./cache_api_1.md#delete_multiple_response)
- `pkg/cache/proto/delete_request.proto` → [cache_api_1](./cache_api_1.md#delete_request) → [queue_api_1](./queue_api_1.md#delete_request)
- `pkg/cache/proto/delete_response.proto` → [cache_api_1](./cache_api_1.md#delete_response) → [queue_api_1](./queue_api_1.md#delete_response)
- `pkg/cache/proto/exists_request.proto` → [cache_api_1](./cache_api_1.md#exists_request)
- `pkg/cache/proto/exists_response.proto` → [cache_api_1](./cache_api_1.md#exists_response)
- `pkg/cache/proto/flush_request.proto` → [cache_api_1](./cache_api_1.md#flush_request)
- `pkg/cache/proto/flush_response.proto` → [cache_api_1](./cache_api_1.md#flush_response)
- `pkg/cache/proto/get_multiple_request.proto` → [cache_api_1](./cache_api_1.md#get_multiple_request)
- `pkg/cache/proto/get_multiple_response.proto` → [cache_api_1](./cache_api_1.md#get_multiple_response)
- `pkg/cache/proto/get_request.proto` → [cache_api_1](./cache_api_1.md#get_request)
- `pkg/cache/proto/get_response.proto` → [cache_api_1](./cache_api_1.md#get_response)
- `pkg/cache/proto/get_stats_response.proto` → [cache_api_1](./cache_api_1.md#get_stats_response) → [metrics_api_1](./metrics_api_1.md#get_stats_response)
- `pkg/cache/proto/increment_request.proto` → [cache_api_1](./cache_api_1.md#increment_request)
- `pkg/cache/proto/increment_response.proto` → [cache_api_1](./cache_api_1.md#increment_response)
- `pkg/cache/proto/keys_request.proto` → [cache_api_1](./cache_api_1.md#keys_request)
- `pkg/cache/proto/keys_response.proto` → [cache_api_1](./cache_api_1.md#keys_response)
- `pkg/cache/proto/set_multiple_request.proto` → [cache_api_1](./cache_api_1.md#set_multiple_request)
- `pkg/cache/proto/set_multiple_response.proto` → [cache_api_1](./cache_api_1.md#set_multiple_response)
- `pkg/cache/proto/set_request.proto` → [cache_api_2](./cache_api_2.md#set_request)
- `pkg/cache/proto/set_response.proto` → [cache_api_2](./cache_api_2.md#set_response)
- `pkg/cache/proto/stats_request.proto` → [cache_api_2](./cache_api_2.md#stats_request)
- `pkg/cache/proto/touch_expiration_response.proto` → [cache_api_2](./cache_api_2.md#touch_expiration_response)
- `pkg/cache/proto/ttl_request.proto` → [cache_api_2](./cache_api_2.md#ttl_request)

#### Source Code

```protobuf
// file: pkg/cache/proto/services/cache_service.proto
edition = "2023";

package gcommon.v1.cache;

import "google/protobuf/go_features.proto";
import "pkg/cache/proto/clear_request.proto";
import "pkg/cache/proto/clear_response.proto";
import "pkg/cache/proto/decrement_request.proto";
import "pkg/cache/proto/decrement_response.proto";
import "pkg/cache/proto/delete_multiple_request.proto";
import "pkg/cache/proto/delete_multiple_response.proto";
import "pkg/cache/proto/delete_request.proto";
import "pkg/cache/proto/delete_response.proto";
import "pkg/cache/proto/exists_request.proto";
import "pkg/cache/proto/exists_response.proto";
import "pkg/cache/proto/flush_request.proto";
import "pkg/cache/proto/flush_response.proto";
import "pkg/cache/proto/get_multiple_request.proto";
import "pkg/cache/proto/get_multiple_response.proto";
import "pkg/cache/proto/get_request.proto";
import "pkg/cache/proto/get_response.proto";
import "pkg/cache/proto/get_stats_response.proto";
import "pkg/cache/proto/increment_request.proto";
import "pkg/cache/proto/increment_response.proto";
import "pkg/cache/proto/keys_request.proto";
import "pkg/cache/proto/keys_response.proto";
import "pkg/cache/proto/set_multiple_request.proto";
import "pkg/cache/proto/set_multiple_response.proto";
import "pkg/cache/proto/set_request.proto";
import "pkg/cache/proto/set_response.proto";
import "pkg/cache/proto/stats_request.proto";
import "pkg/cache/proto/touch_expiration_response.proto";
import "pkg/cache/proto/ttl_request.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/cache/proto";

/**
 * CacheService provides comprehensive caching capabilities.
 * Supports CRUD operations, batch operations, atomic operations,
 * and cache management with flexible expiration policies.
 */
service CacheService {
  // Get retrieves a value from the cache by key
  rpc Get(GetRequest) returns (GetResponse);

  // Set stores a value in the cache with optional expiration
  rpc Set(SetRequest) returns (SetResponse);

  // Delete removes a value from the cache
  rpc Delete(DeleteRequest) returns (DeleteResponse);

  // Exists checks if a key exists in the cache
  rpc Exists(ExistsRequest) returns (ExistsResponse);

  // GetMultiple retrieves multiple values from the cache in a single operation
  rpc GetMultiple(GetMultipleRequest) returns (GetMultipleResponse);

  // SetMultiple stores multiple values in the cache atomically
  rpc SetMultiple(SetMultipleRequest) returns (SetMultipleResponse);

  // DeleteMultiple removes multiple values from the cache atomically
  rpc DeleteMultiple(DeleteMultipleRequest) returns (DeleteMultipleResponse);

  // Increment atomically increments a numeric value
  rpc Increment(IncrementRequest) returns (IncrementResponse);

  // Decrement atomically decrements a numeric value
  rpc Decrement(DecrementRequest) returns (DecrementResponse);

  // Clear removes all entries from the cache or by pattern
  rpc Clear(ClearRequest) returns (ClearResponse);

  // Keys returns all keys matching a pattern
  rpc Keys(KeysRequest) returns (KeysResponse);

  // GetStats returns cache statistics and performance metrics
  rpc GetStats(GetStatsRequest) returns (GetStatsResponse);

  // Flush forces cache persistence if supported by the backend
  rpc Flush(FlushRequest) returns (FlushResponse);

  // TouchExpiration updates the expiration time of an existing key
  rpc TouchExpiration(TouchExpirationRequest) returns (TouchExpirationResponse);
}

```

---
