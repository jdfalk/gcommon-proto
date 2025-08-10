# web_config_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 23

## Files in this Module

- [auth_config.proto](#auth_config)
- [cache_config.proto](#cache_config)
- [compression_config.proto](#compression_config)
- [configure_global_request.proto](#configure_global_request) ⚠️ 1 issues
- [configure_global_response.proto](#configure_global_response) ⚠️ 1 issues
- [cookie_config.proto](#cookie_config)
- [cors_config.proto](#cors_config)
- [csrf_config.proto](#csrf_config)
- [export_server_config_request.proto](#export_server_config_request) ⚠️ 1
  issues
- [export_server_config_response.proto](#export_server_config_response) ⚠️ 1
  issues
- [get_cache_config_request.proto](#get_cache_config_request)
- [get_cache_config_response.proto](#get_cache_config_response)
- [get_cors_config_request.proto](#get_cors_config_request) ⚠️ 1 issues
- [get_cors_config_response.proto](#get_cors_config_response) ⚠️ 1 issues
- [get_security_config_request.proto](#get_security_config_request) ⚠️ 1 issues
- [get_security_config_response.proto](#get_security_config_response) ⚠️ 1
  issues
- [get_server_config_request.proto](#get_server_config_request) ⚠️ 1 issues
- [get_server_config_response.proto](#get_server_config_response) ⚠️ 1 issues
- [handler_config.proto](#handler_config)
- [health_check_config.proto](#health_check_config)
- [import_server_config_request.proto](#import_server_config_request) ⚠️ 1
  issues
- [import_server_config_response.proto](#import_server_config_response) ⚠️ 1
  issues
- [load_balancer_config.proto](#load_balancer_config)
- [middleware_config.proto](#middleware_config)
- [proxy_config.proto](#proxy_config)
- [rate_limit_config.proto](#rate_limit_config)
- [reload_server_config_request.proto](#reload_server_config_request) ⚠️ 1
  issues
- [reload_server_config_response.proto](#reload_server_config_response) ⚠️ 1
  issues
- [route_config.proto](#route_config)
- [security_config.proto](#security_config)
- [server_config.proto](#server_config)
- [session_config.proto](#session_config)
- [ssl_config.proto](#ssl_config)
- [static_config.proto](#static_config)
- [template_config.proto](#template_config)
- [timeout_config.proto](#timeout_config)
- [tls_config.proto](#tls_config)
- [update_cache_config_request.proto](#update_cache_config_request)
- [update_cache_config_response.proto](#update_cache_config_response)
- [update_cors_config_request.proto](#update_cors_config_request) ⚠️ 1 issues
- [update_cors_config_response.proto](#update_cors_config_response) ⚠️ 1 issues
- [update_handler_config_request.proto](#update_handler_config_request) ⚠️ 1
  issues
- [update_handler_config_response.proto](#update_handler_config_response) ⚠️ 1
  issues
- [update_middleware_config_request.proto](#update_middleware_config_request)
- [update_middleware_config_response.proto](#update_middleware_config_response)
- [update_route_config_request.proto](#update_route_config_request) ⚠️ 1 issues
- [update_route_config_response.proto](#update_route_config_response) ⚠️ 1
  issues
- [update_security_config_request.proto](#update_security_config_request) ⚠️ 1
  issues
- [update_security_config_response.proto](#update_security_config_response) ⚠️ 1
  issues
- [update_server_config_request.proto](#update_server_config_request) ⚠️ 1
  issues

## Module Dependencies

**This module depends on**:

- [cache_config](./cache_config.md)
- [common](./common.md)
- [config_1](./config_1.md)
- [log](./log.md)
- [metrics_1](./metrics_1.md)
- [web](./web.md)

**Modules that depend on this one**:

- [web](./web.md)
- [web_api_2](./web_api_2.md)
- [web_services](./web_services.md)

---

## Detailed Documentation

### auth_config.proto {#auth_config}

**Path**: `pkg/web/proto/auth_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 29

**Messages** (1): `AuthConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/auth_config.proto
// version: 1.0.0
// guid: 01c8f7e0-20a4-4ffe-81ba-5e0aede462e0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// AuthConfig message definition.
// AuthConfig defines authentication settings for a web server.
message AuthConfig {
  // Enable authentication middleware
  bool enable_auth = 1;

  // Allowed roles for access control
  repeated string allowed_roles = 2;

  // Required scopes for authorization
  repeated string required_scopes = 3;

  // Additional auth options
  map<string, string> options = 4;
}

```

---

### cache_config.proto {#cache_config}

**Path**: `pkg/web/proto/cache_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 34

**Messages** (1): `CacheConfig`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/cache_policy.proto` → [common](./common.md#cache_policy)
- `pkg/web/proto/cache_strategy.proto` → [web](./web.md#cache_strategy)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/cache_config.proto
// version: 1.1.0
// guid: 21e9abdf-bf09-4c22-b45b-eb9c092d9664

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/cache_policy.proto";
import "pkg/web/proto/cache_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// CacheConfig defines caching behavior for web responses.
message CacheConfig {
  // Selected cache strategy for responses
  CacheStrategy strategy = 1;

  // Detailed cache policy settings
  gcommon.v1.common.CachePolicy policy = 2 [lazy = true];

  // Override time to live for web resources
  google.protobuf.Duration ttl = 3;

  // Whether caching is enabled for this server
  bool enabled = 4;

  // Optional namespace or cache name
  string cache_name = 5;
}

```

---

### compression_config.proto {#compression_config}

**Path**: `pkg/web/proto/compression_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 26

**Messages** (1): `CompressionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/compression_type.proto` →
  [config_1](./config_1.md#compression_type) → [log](./log.md#compression_type)
  → [metrics_1](./metrics_1.md#compression_type) →
  [web](./web.md#compression_type)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/compression_config.proto
// version: 1.1.0
// guid: e4d9d1fd-7180-432c-a64b-5b6f24858928

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/compression_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// CompressionConfig message definition.
message CompressionConfig {
  // Compression algorithm to use for HTTP responses
  CompressionType compression_type = 1;

  // Minimum content length in bytes before compression is applied
  int32 min_length = 2;

  // Compression level (implementation specific)
  int32 level = 3;
}

```

---

### configure_global_request.proto {#configure_global_request}

**Path**: `pkg/web/proto/configure_global_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `ConfigureGlobalRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 20: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/requests/configure_global_request.proto
// version: 1.0.0
// guid: 53f1a181-4823-4590-977d-dcd614b74421

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ConfigureGlobalRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ConfigureGlobalRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}

```

---

### configure_global_response.proto {#configure_global_response}

**Path**: `pkg/web/proto/configure_global_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `ConfigureGlobalResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 21: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/responses/configure_global_response.proto
// version: 1.0.0
// guid: 0719dc91-a213-44de-817e-6f26efe9dc68

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ConfigureGlobalResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ConfigureGlobalResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}

```

---

### cookie_config.proto {#cookie_config}

**Path**: `pkg/web/proto/cookie_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 39

**Messages** (1): `CookieConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/web/proto/cookie_same_site.proto` → [web](./web.md#cookie_same_site)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/cookie_config.proto
// version: 1.1.0
// guid: 57c9187b-fa13-46bb-9840-d7a2515e7ff1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/web/proto/cookie_same_site.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// CookieConfig message definition.
message CookieConfig {
  // Cookie name
  string name = 1;

  // Cookie domain
  string domain = 2;

  // Cookie path
  string path = 3;

  // Set Secure flag
  bool secure = 4;

  // Set HttpOnly flag
  bool http_only = 5;

  // SameSite policy
  CookieSameSite same_site = 6;

  // Max age of the cookie
  google.protobuf.Duration max_age = 7;
}

```

---

### cors_config.proto {#cors_config}

**Path**: `pkg/web/proto/cors_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 38

**Messages** (1): `CORSConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/cors_config.proto
// version: 1.0.1
// guid: a30ac136-585a-4ceb-becf-9ca8beef5e86

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// CorsConfig message definition.
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

```

---

### csrf_config.proto {#csrf_config}

**Path**: `pkg/web/proto/csrf_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 32

**Messages** (1): `CsrfConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/csrf_config.proto
// version: 1.1.0
// guid: b3eaed64-1234-45b9-86c4-e348b91cdbe9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// CsrfConfig message definition.
message CsrfConfig {
  // Name of the HTTP header containing the CSRF token
  string header_name = 1;

  // Name of the cookie used to store the token
  string cookie_name = 2;

  // Length of generated tokens
  int32 token_length = 3;

  // Token expiration duration
  google.protobuf.Duration token_ttl = 4;

  // Require secure cookies
  bool secure = 5;
}

```

---

### export_server_config_request.proto {#export_server_config_request}

**Path**: `pkg/web/proto/export_server_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `ExportServerConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 20: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/requests/export_server_config_request.proto
// version: 1.0.0
// guid: f5105c4f-0736-4a4a-a9c6-004a43fbbd9b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ExportServerConfigRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ExportServerConfigRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}

```

---

### export_server_config_response.proto {#export_server_config_response}

**Path**: `pkg/web/proto/export_server_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `ExportServerConfigResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 21: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/responses/export_server_config_response.proto
// version: 1.0.0
// guid: b7274c09-ff07-4507-8c91-b7bfc995a64b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ExportServerConfigResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ExportServerConfigResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}

```

---

### get_cache_config_request.proto {#get_cache_config_request}

**Path**: `pkg/web/proto/get_cache_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCacheConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_cache_config_request.proto
// version: 1.0.0
// guid: abc12345-6789-0def-1234-567890abcdef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message GetCacheConfigRequest {
  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 1;
}

```

---

### get_cache_config_response.proto {#get_cache_config_response}

**Path**: `pkg/web/proto/get_cache_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 23

**Messages** (1): `GetCacheConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/web/proto/cache_config.proto` →
  [cache_config](./cache_config.md#cache_config)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_cache_config_response.proto
// version: 1.0.0
// guid: def67890-abcd-1234-5678-90abcdef1234

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/web/proto/cache_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message GetCacheConfigResponse {
  // The current cache configuration
  CacheConfig config = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### get_cors_config_request.proto {#get_cors_config_request}

**Path**: `pkg/web/proto/get_cors_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetCorsConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_cors_config_request.proto
// version: 1.0.0
// guid: c22a2431-29be-4eb5-8ed8-40b2840f03ae

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetCorsConfigRequest request definition.
message GetCorsConfigRequest {
  string placeholder = 1;
}

```

---

### get_cors_config_response.proto {#get_cors_config_response}

**Path**: `pkg/web/proto/get_cors_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetCorsConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_cors_config_response.proto
// version: 1.0.0
// guid: 15367ee2-9586-4b6b-a32f-69bf3a2f3310

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetCorsConfigResponse response definition.
message GetCorsConfigResponse {
  string placeholder = 1;
}

```

---

### get_security_config_request.proto {#get_security_config_request}

**Path**: `pkg/web/proto/get_security_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetSecurityConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_security_config_request.proto
// version: 1.0.0
// guid: a5853c6e-88c2-4c4c-962b-c7fc36d4bdef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetSecurityConfigRequest request definition.
message GetSecurityConfigRequest {
  string placeholder = 1;
}

```

---

### get_security_config_response.proto {#get_security_config_response}

**Path**: `pkg/web/proto/get_security_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetSecurityConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_security_config_response.proto
// version: 1.0.0
// guid: ad8fcfc2-e9a0-4a3c-8f15-eddc7235c96f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetSecurityConfigResponse response definition.
message GetSecurityConfigResponse {
  string placeholder = 1;
}

```

---

### get_server_config_request.proto {#get_server_config_request}

**Path**: `pkg/web/proto/get_server_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetServerConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_server_config_request.proto
// version: 1.0.0
// guid: 78c28db0-b087-4225-b72d-babf47e86db3

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetServerConfigRequest request definition.
message GetServerConfigRequest {
  string placeholder = 1;
}

```

---

### get_server_config_response.proto {#get_server_config_response}

**Path**: `pkg/web/proto/get_server_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetServerConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_server_config_response.proto
// version: 1.0.0
// guid: 3f909fa5-4f36-4285-8b01-fe1bc5b01fd7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetServerConfigResponse response definition.
message GetServerConfigResponse {
  string placeholder = 1;
}

```

---

### handler_config.proto {#handler_config}

**Path**: `pkg/web/proto/handler_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 30

**Messages** (1): `HandlerConfig`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `pkg/web/proto/handler_type.proto` → [web](./web.md#handler_type)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/handler_config.proto
// version: 1.1.0
// guid: 68d30216-8b75-4c02-88ca-9c39d70d4c4c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "pkg/web/proto/handler_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HandlerConfig message definition.
message HandlerConfig {
  // Handler type
  HandlerType type = 1;

  // Handler-specific configuration
  google.protobuf.Any config = 2;

  // Target for the handler (URL, function name, etc.)
  string target = 3;

  // Additional handler options
  map<string, string> options = 4;
}

```

---

### health_check_config.proto {#health_check_config}

**Path**: `pkg/web/proto/health_check_config.proto` **Package**:
`gcommon.v1.web` **Lines**: 34

**Messages** (1): `HealthCheckConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/health_check_config.proto
// version: 1.1.0
// guid: 7aea6b7c-133f-4443-b7b6-c1cdeb194f0b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HealthCheckConfig defines parameters for performing HTTP health checks.
message HealthCheckConfig {
  // HTTP path used for the health check request.
  string path = 1;

  // Interval between health checks in seconds.
  double interval_seconds = 2;

  // Timeout for a single health check in seconds.
  double timeout_seconds = 3;

  // Expected HTTP status code indicating a healthy response.
  int32 expected_status = 4;

  // Additional headers to include with the request.
  map<string, string> headers = 5;

  // Whether the health check is enabled.
  bool enabled = 6;
}

```

---

### import_server_config_request.proto {#import_server_config_request}

**Path**: `pkg/web/proto/import_server_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `ImportServerConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 20: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/requests/import_server_config_request.proto
// version: 1.0.0
// guid: 60a97ec8-a4f9-4606-844c-774a208ca62a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ImportServerConfigRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ImportServerConfigRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}

```

---

### import_server_config_response.proto {#import_server_config_response}

**Path**: `pkg/web/proto/import_server_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `ImportServerConfigResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 21: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/responses/import_server_config_response.proto
// version: 1.0.0
// guid: 5cf8e464-8b8e-487d-86a0-0707a9490356

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ImportServerConfigResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ImportServerConfigResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}

```

---

### load_balancer_config.proto {#load_balancer_config}

**Path**: `pkg/web/proto/load_balancer_config.proto` **Package**:
`gcommon.v1.web` **Lines**: 30

**Messages** (1): `LoadBalancerConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/web/proto/load_balance_strategy.proto` →
  [web](./web.md#load_balance_strategy)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/load_balancer_config.proto
// version: 1.1.0
// guid: 773a3c4c-d370-4416-b0d8-bf270ea7d2de

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/web/proto/load_balance_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// LoadBalancerConfig message definition.
message LoadBalancerConfig {
  // Load balancing strategy
  LoadBalanceStrategy strategy = 1;

  // Upstream server addresses
  repeated string upstreams = 2;

  // Health check path
  string health_check_path = 3;

  // Timeout for proxy requests
  google.protobuf.Duration timeout = 4;
}

```

---

### middleware_config.proto {#middleware_config}

**Path**: `pkg/web/proto/middleware_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 30

**Messages** (1): `MiddlewareConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/middleware_type.proto` → [web](./web.md#middleware_type)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/middleware_config.proto
// version: 1.0.0
// guid: e9b024e1-e72c-48e4-b1c4-5df34ed3e3ac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/middleware_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// MiddlewareConfig message definition.
// MiddlewareConfig represents a single middleware's configuration.
message MiddlewareConfig {
  // Middleware type
  MiddlewareType type = 1;

  // Whether the middleware is enabled
  bool enabled = 2;

  // Execution priority (lower runs first)
  int32 priority = 3;

  // Additional middleware options
  map<string, string> options = 4;
}

```

---

### proxy_config.proto {#proxy_config}

**Path**: `pkg/web/proto/proxy_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 34

**Messages** (1): `ProxyConfig`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/web/proto/http_header.proto` → [web](./web.md#http_header)
- `pkg/web/proto/proxy_type.proto` → [web](./web.md#proxy_type)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/proxy_config.proto
// version: 1.1.0
// guid: 44849c54-6bf7-4211-a8c0-0be1e0c98add

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/web/proto/http_header.proto";
import "pkg/web/proto/proxy_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ProxyConfig message definition.
message ProxyConfig {
  // Type of proxy
  ProxyType proxy_type = 1;

  // Target backend URL
  string target_url = 2;

  // Headers to forward to the backend
  repeated HttpHeader forward_headers = 3;

  // Connect timeout duration
  google.protobuf.Duration connect_timeout = 4;

  // Whether to trust X-Forwarded headers
  bool trust_forward_headers = 5;
}

```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `pkg/web/proto/rate_limit_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 35

**Messages** (1): `RateLimitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/rate_limit_strategy.proto` →
  [web](./web.md#rate_limit_strategy)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/rate_limit_config.proto
// version: 1.0.1
// guid: 180cb5f4-1064-4b88-bbe6-dbc6934ec21e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/rate_limit_strategy.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RateLimitConfig message definition.
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

```

---

### reload_server_config_request.proto {#reload_server_config_request}

**Path**: `pkg/web/proto/reload_server_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `ReloadServerConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 20: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/requests/reload_server_config_request.proto
// version: 1.0.0
// guid: abeb1b6f-6a94-4044-b27e-a91c1c9e6042

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ReloadServerConfigRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ReloadServerConfigRequest {
  // Required fields (1-10)

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Timestamps (51-60)

  /**
   * Timestamp when this request was created.
   */
  google.protobuf.Timestamp requested_at = 51;
}

```

---

### reload_server_config_response.proto {#reload_server_config_response}

**Path**: `pkg/web/proto/reload_server_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `ReloadServerConfigResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### ⚠️ Issues Found (1)

- Line 21: Implementation needed - \* Auto-generated placeholder - implement
  specific fields as needed.

#### Source Code

```protobuf
// file: pkg/web/proto/responses/reload_server_config_response.proto
// version: 1.0.0
// guid: a6f6a4cf-253b-4759-a0a7-f699c4cf8463

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * ReloadServerConfigResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ReloadServerConfigResponse {
  // Required fields (1-10)

  /**
   * Indicates whether the operation was successful.
   */
  bool success = 1;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Status and error fields (61-70)

  /**
   * Error information if the operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 51;
}

```

---

### route_config.proto {#route_config}

**Path**: `pkg/web/proto/route_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 36

**Messages** (1): `RouteConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/handler_type.proto` → [web](./web.md#handler_type)
- `pkg/web/proto/http_method.proto` → [web](./web.md#http_method)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/route_config.proto
// version: 1.1.0
// guid: ce3f0233-7da2-4e81-8460-b1bf3a6fba53

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/handler_type.proto";
import "pkg/web/proto/http_method.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RouteConfig message definition.
message RouteConfig {
  // URL path pattern
  string path = 1;

  // Allowed HTTP methods
  repeated HTTPMethod methods = 2;

  // Handler name or identifier
  string handler = 3;

  // Handler type implementation
  HandlerType handler_type = 4;

  // Middleware IDs applied to this route
  repeated string middleware_ids = 5;

  // Require authentication for route
  bool auth_required = 6;
}

```

---

### security_config.proto {#security_config}

**Path**: `pkg/web/proto/security_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 30

**Messages** (1): `SecurityConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/tls_config.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/security_config.proto
// version: 1.1.0
// guid: 2d5231ca-5b58-4b11-8448-a87d4ae0154e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// Import TLS config
import "pkg/web/proto/tls_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// SecurityConfig message definition.
message SecurityConfig {
  // Enable TLS security
  bool enable_tls = 1;

  // TLS configuration details
  TLSConfig tls = 2;

  // Allowed host patterns
  repeated string allowed_hosts = 3;

  // Additional security options
  map<string, string> options = 4;
}

```

---

### server_config.proto {#server_config}

**Path**: `pkg/web/proto/server_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 38

**Messages** (1): `ServerConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/server_config.proto
// version: 1.0.0
// guid: f4e56c59-17af-4da2-8a92-e1a619fe9fba

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ServerConfig message definition.
// ServerConfig defines basic web server settings.
message ServerConfig {
  // Hostname or IP address to bind
  string host = 1;

  // Listening port number
  int32 port = 2;

  // Enable TLS for secure communication
  bool enable_tls = 3;

  // Path to TLS certificate
  string tls_cert_path = 4;

  // Path to TLS key
  string tls_key_path = 5;

  // Trusted proxy addresses
  repeated string trusted_proxies = 6;

  // Additional server options
  map<string, string> options = 7;
}

```

---

### session_config.proto {#session_config}

**Path**: `pkg/web/proto/session_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 36

**Messages** (1): `SessionConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/web/proto/cookie_same_site.proto` → [web](./web.md#cookie_same_site)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/session_config.proto
// version: 1.1.0
// guid: 78ffbac0-1dba-4e18-85e1-ecce179da015

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/web/proto/cookie_same_site.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// SessionConfig message definition.
message SessionConfig {
  // Session idle timeout before automatic expiration
  google.protobuf.Duration idle_timeout = 1;

  // Absolute session lifetime regardless of activity
  google.protobuf.Duration absolute_timeout = 2;

  // Name of the session cookie
  string cookie_name = 3;

  // Use secure cookies (HTTPS only)
  bool secure_cookies = 4;

  // Restrict cookie to HTTP only
  bool http_only = 5;

  // Cookie SameSite policy
  CookieSameSite same_site = 6;
}

```

---

### ssl_config.proto {#ssl_config}

**Path**: `pkg/web/proto/ssl_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 32

**Messages** (1): `SslConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/ssl_protocol.proto` → [web](./web.md#ssl_protocol)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/ssl_config.proto
// version: 1.1.0
// guid: 4d5ec783-ec4b-4ffc-a7e6-28df5382a594

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/ssl_protocol.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// SslConfig message definition.
message SslConfig {
  // TLS protocol version
  SSLProtocol protocol = 1;

  // Path to certificate file
  string cert_file = 2;

  // Path to key file
  string key_file = 3;

  // Optional CA bundle path
  string ca_file = 4;

  // Require client certificates
  bool require_client_auth = 5;
}

```

---

### static_config.proto {#static_config}

**Path**: `pkg/web/proto/static_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 25

**Messages** (1): `StaticConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/static_config.proto
// version: 1.1.0
// guid: e2d0d32a-6b50-42ec-b728-ef60869cf5ac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// StaticConfig message definition.
message StaticConfig {
  // Root directory for static files
  string directory = 1;

  // Default index files
  repeated string index_files = 2;

  // Enable directory listing
  bool enable_listing = 3;
}

```

---

### template_config.proto {#template_config}

**Path**: `pkg/web/proto/template_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 28

**Messages** (1): `TemplateConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/template_config.proto
// version: 1.1.0
// guid: 02942f54-029c-468f-85df-cdf3042e8ee6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// TemplateConfig message definition.
message TemplateConfig {
  // Directory containing template files
  string directory = 1;

  // Default file extension
  string extension = 2;

  // Reload templates on change
  bool reload = 3;

  // Custom template function names
  repeated string functions = 4;
}

```

---

### timeout_config.proto {#timeout_config}

**Path**: `pkg/web/proto/timeout_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 32

**Messages** (1): `TimeoutConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/timeout_config.proto
// version: 1.0.0
// guid: e3a21e33-e66f-47e7-b7ff-6c6df8a0e9a1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// TimeoutConfig specifies various timeout settings for the server.
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

```

---

### tls_config.proto {#tls_config}

**Path**: `pkg/web/proto/tls_config.proto` **Package**: `gcommon.v1.web`
**Lines**: 68

**Messages** (1): `TLSConfig`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/tls_config.proto
// version: 1.0.0
// guid: 9f8e7d6c-5b4a-3928-1706-f5e4d3c2b1a0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
// Standard imports
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * TLSConfig defines TLS/SSL configuration for web servers.
 */
message TLSConfig {
  // Required fields (1-10)

  /**
   * Certificate file path or content.
   */
  string cert_file = 1;

  /**
   * Private key file path or content.
   */
  string key_file = 2;

  // Optional fields (11-50)

  /**
   * CA certificate file path for client verification.
   */
  string ca_file = 11;

  /**
   * Minimum TLS version (e.g., "1.2", "1.3").
   */
  string min_version = 12;

  /**
   * Maximum TLS version (e.g., "1.2", "1.3").
   */
  string max_version = 13;

  /**
   * List of supported cipher suites.
   */
  repeated string cipher_suites = 14;

  /**
   * Whether to require client certificates.
   */
  bool require_client_cert = 15;

  /**
   * Whether to verify client certificates.
   */
  bool verify_client_cert = 16;

  /**
   * Server name for SNI (Server Name Indication).
   */
  string server_name = 17;
}

```

---

### update_cache_config_request.proto {#update_cache_config_request}

**Path**: `pkg/web/proto/update_cache_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 23

**Messages** (1): `UpdateCacheConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/web/proto/cache_config.proto` →
  [cache_config](./cache_config.md#cache_config)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_cache_config_request.proto
// version: 1.0.0
// guid: ghi12345-6789-0abc-def1-234567890123

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/web/proto/cache_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message UpdateCacheConfigRequest {
  // The new cache configuration to apply
  CacheConfig config = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### update_cache_config_response.proto {#update_cache_config_response}

**Path**: `pkg/web/proto/update_cache_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 22

**Messages** (1): `UpdateCacheConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_cache_config_response.proto
// version: 1.0.0
// guid: jkl45678-90ab-cdef-1234-567890abcdef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message UpdateCacheConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### update_cors_config_request.proto {#update_cors_config_request}

**Path**: `pkg/web/proto/update_cors_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateCorsConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_cors_config_request.proto
// version: 1.0.0
// guid: 00b7b190-69c5-49c8-8b50-ca9c0e68e231

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateCorsConfigRequest request definition.
message UpdateCorsConfigRequest {
  string placeholder = 1;
}

```

---

### update_cors_config_response.proto {#update_cors_config_response}

**Path**: `pkg/web/proto/update_cors_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateCorsConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_cors_config_response.proto
// version: 1.0.0
// guid: 44e8600c-ebb5-45be-851d-41f41c810996

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateCorsConfigResponse response definition.
message UpdateCorsConfigResponse {
  string placeholder = 1;
}

```

---

### update_handler_config_request.proto {#update_handler_config_request}

**Path**: `pkg/web/proto/update_handler_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateHandlerConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_handler_config_request.proto
// version: 1.0.0
// guid: 6241c28b-b274-4d3e-afb4-2c2a65fa5e96

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateHandlerConfigRequest request definition.
message UpdateHandlerConfigRequest {
  string placeholder = 1;
}

```

---

### update_handler_config_response.proto {#update_handler_config_response}

**Path**: `pkg/web/proto/update_handler_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateHandlerConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_handler_config_response.proto
// version: 1.0.0
// guid: f5dc02ec-1a36-4fcd-ae1e-352189358ea7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateHandlerConfigResponse response definition.
message UpdateHandlerConfigResponse {
  string placeholder = 1;
}

```

---

### update_middleware_config_request.proto {#update_middleware_config_request}

**Path**: `pkg/web/proto/update_middleware_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 25

**Messages** (1): `UpdateMiddlewareConfigRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/web/proto/middleware_config.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_middleware_config_request.proto
// version: 1.0.0
// guid: 30e082c9-2bd6-4472-ae4a-f71e481f04a3
// UpdateMiddlewareConfigRequest request definition.
// UpdateMiddlewareConfigRequest updates an existing middleware configuration.

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/web/proto/middleware_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message UpdateMiddlewareConfigRequest {
  // Request metadata for tracing and auth
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Updated middleware configuration
  MiddlewareConfig config = 2;
}

```

---

### update_middleware_config_response.proto {#update_middleware_config_response}

**Path**: `pkg/web/proto/update_middleware_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 24

**Messages** (1): `UpdateMiddlewareConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_middleware_config_response.proto
// version: 1.0.0
// guid: e8328b61-1bdf-487b-b874-01de9424625e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateMiddlewareConfigResponse response definition.
// UpdateMiddlewareConfigResponse returns the result of updating middleware config.
message UpdateMiddlewareConfigResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Whether the middleware was updated
  bool updated = 2;
}

```

---

### update_route_config_request.proto {#update_route_config_request}

**Path**: `pkg/web/proto/update_route_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateRouteConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_route_config_request.proto
// version: 1.0.0
// guid: 65c64e7e-be8d-4fa3-9bd1-e0c9b752fef9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateRouteConfigRequest request definition.
message UpdateRouteConfigRequest {
  string placeholder = 1;
}

```

---

### update_route_config_response.proto {#update_route_config_response}

**Path**: `pkg/web/proto/update_route_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateRouteConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_route_config_response.proto
// version: 1.0.0
// guid: 07ee551d-a9ae-4d39-995c-3442717c934b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateRouteConfigResponse response definition.
message UpdateRouteConfigResponse {
  string placeholder = 1;
}

```

---

### update_security_config_request.proto {#update_security_config_request}

**Path**: `pkg/web/proto/update_security_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateSecurityConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_security_config_request.proto
// version: 1.0.0
// guid: 69e8edc6-5475-4f71-9753-26c412daab0e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateSecurityConfigRequest request definition.
message UpdateSecurityConfigRequest {
  string placeholder = 1;
}

```

---

### update_security_config_response.proto {#update_security_config_response}

**Path**: `pkg/web/proto/update_security_config_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateSecurityConfigResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_security_config_response.proto
// version: 1.0.0
// guid: 63689787-044d-4302-8175-9745ac688e61

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateSecurityConfigResponse response definition.
message UpdateSecurityConfigResponse {
  string placeholder = 1;
}

```

---

### update_server_config_request.proto {#update_server_config_request}

**Path**: `pkg/web/proto/update_server_config_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateServerConfigRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_server_config_request.proto
// version: 1.0.0
// guid: 6a2b47b4-af5e-4e51-9807-18898846cb4a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateServerConfigRequest request definition.
message UpdateServerConfigRequest {
  string placeholder = 1;
}

```

---
