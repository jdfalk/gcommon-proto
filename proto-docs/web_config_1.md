# web_config_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [auth_config.proto](#auth_config)
- [cache_config.proto](#cache_config)
- [compression_config.proto](#compression_config)
- [configure_global_request.proto](#configure_global_request)
- [configure_global_response.proto](#configure_global_response)
- [cookie_config.proto](#cookie_config)
- [cors_config.proto](#cors_config)
- [csrf_config.proto](#csrf_config)
- [export_server_config_request.proto](#export_server_config_request)
- [export_server_config_response.proto](#export_server_config_response)
- [get_cache_config_request.proto](#get_cache_config_request)
- [get_cache_config_response.proto](#get_cache_config_response)
- [get_cors_config_request.proto](#get_cors_config_request)
- [get_cors_config_response.proto](#get_cors_config_response)
- [get_security_config_request.proto](#get_security_config_request)
- [get_security_config_response.proto](#get_security_config_response)
- [get_server_config_request.proto](#get_server_config_request)
- [get_server_config_response.proto](#get_server_config_response)
- [handler_config.proto](#handler_config)
- [health_check_config.proto](#health_check_config)
- [import_server_config_request.proto](#import_server_config_request)
- [import_server_config_response.proto](#import_server_config_response)
- [load_balancer_config.proto](#load_balancer_config)
- [middleware_config.proto](#middleware_config)
- [proxy_config.proto](#proxy_config)
- [rate_limit_config.proto](#rate_limit_config)
- [reload_server_config_request.proto](#reload_server_config_request)
- [reload_server_config_response.proto](#reload_server_config_response)
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
- [update_cors_config_request.proto](#update_cors_config_request)
- [update_cors_config_response.proto](#update_cors_config_response)
- [update_handler_config_request.proto](#update_handler_config_request)
- [update_handler_config_response.proto](#update_handler_config_response)
- [update_middleware_config_request.proto](#update_middleware_config_request)
- [update_middleware_config_response.proto](#update_middleware_config_response)
- [update_route_config_request.proto](#update_route_config_request)
- [update_route_config_response.proto](#update_route_config_response)
- [update_security_config_request.proto](#update_security_config_request)
- [update_security_config_response.proto](#update_security_config_response)
- [update_server_config_request.proto](#update_server_config_request)
---


## Detailed Documentation

### auth_config.proto {#auth_config}

**Path**: `gcommon/v1/web/auth_config.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebAuthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/auth_config.proto
// version: 1.0.0
// guid: 01c8f7e0-20a4-4ffe-81ba-5e0aede462e0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthConfig message definition.
// AuthConfig defines authentication settings for a web server.
message WebAuthConfig {
  // Enable authentication middleware
  bool enable_auth = 1;

  // Allowed roles for access control
  repeated string allowed_roles = 2 [(buf.validate.field).repeated.min_items = 1];

  // Required scopes for authorization
  repeated string required_scopes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Additional auth options
  map<string, string> options = 4;
}
```

---

### cache_config.proto {#cache_config}

**Path**: `gcommon/v1/web/cache_config.proto` **Package**: `gcommon.v1.web` **Lines**: 37

**Messages** (1): `WebCacheConfig`

**Imports** (5):

- `gcommon/v1/common/cache_policy.proto`
- `gcommon/v1/common/cache_strategy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cache_config.proto
// version: 1.1.0
// guid: 21e9abdf-bf09-4c22-b45b-eb9c092d9664

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cache_policy.proto";
import "gcommon/v1/common/cache_strategy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CacheConfig defines caching behavior for web responses.
message WebCacheConfig {
  // Selected cache strategy for responses
  gcommon.v1.common.CacheStrategy strategy = 1;

  // Detailed cache policy settings
  gcommon.v1.common.CachePolicy policy = 2 [lazy = true];

  // Override time to live for web resources
  google.protobuf.Duration ttl = 3;

  // Whether caching is enabled for this server
  bool enabled = 4;

  // Optional namespace or cache name
  string cache_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### compression_config.proto {#compression_config}

**Path**: `gcommon/v1/web/compression_config.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Messages** (1): `WebCompressionConfig`

**Imports** (3):

- `gcommon/v1/common/compression_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/compression_config.proto
// version: 1.1.0
// guid: e4d9d1fd-7180-432c-a64b-5b6f24858928

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/compression_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CompressionConfig message definition.
message WebCompressionConfig {
  // Compression algorithm to use for HTTP responses
  // Compression type to use for responses
  gcommon.v1.common.LogCompressionType compression_type = 1;

  // Minimum content length in bytes before compression is applied
  int32 min_length = 2 [(buf.validate.field).int32.gte = 0];

  // Compression level (implementation specific)
  int32 level = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### configure_global_request.proto {#configure_global_request}

**Path**: `gcommon/v1/web/configure_global_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ConfigureGlobalRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/configure_global_request.proto
// version: 1.0.1
// guid: 53f1a181-4823-4590-977d-dcd614b74421

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/configure_global_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ConfigureGlobalResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/configure_global_response.proto
// version: 1.0.1
// guid: 0719dc91-a213-44de-817e-6f26efe9dc68

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/cookie_config.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `CookieConfig`

**Imports** (4):

- `gcommon/v1/common/cookie_same_site.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cookie_config.proto
// version: 1.1.0
// guid: 57c9187b-fa13-46bb-9840-d7a2515e7ff1

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cookie_same_site.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CookieConfig message definition.
message CookieConfig {
  // Cookie name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cookie domain
  string domain = 2;

  // Cookie path
  string path = 3;

  // Set Secure flag
  bool secure = 4;

  // Set HttpOnly flag
  bool http_only = 5;

  // SameSite policy
  gcommon.v1.common.CookieSameSite same_site = 6;

  // Max age of the cookie
  google.protobuf.Duration max_age = 7;
}
```

---

### cors_config.proto {#cors_config}

**Path**: `gcommon/v1/web/cors_config.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `CORSConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cors_config.proto
// version: 1.0.1
// guid: a30ac136-585a-4ceb-becf-9ca8beef5e86

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CorsConfig message definition.
message CORSConfig {
  // Enable CORS
  bool enabled = 1;

  // Allowed origins
  repeated string allowed_origins = 2 [(buf.validate.field).repeated.min_items = 1];

  // Allowed methods
  repeated string allowed_methods = 3 [(buf.validate.field).repeated.min_items = 1];

  // Allowed headers
  repeated string allowed_headers = 4 [(buf.validate.field).repeated.min_items = 1];

  // Exposed headers
  repeated string exposed_headers = 5 [(buf.validate.field).repeated.min_items = 1];

  // Allow credentials
  bool allow_credentials = 6;

  // Max age
  google.protobuf.Duration max_age = 7;
}
```

---

### csrf_config.proto {#csrf_config}

**Path**: `gcommon/v1/web/csrf_config.proto` **Package**: `gcommon.v1.web` **Lines**: 38

**Messages** (1): `CsrfConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/csrf_config.proto
// version: 1.1.0
// guid: b3eaed64-1234-45b9-86c4-e348b91cdbe9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CsrfConfig message definition.
message CsrfConfig {
  // Name of the HTTP header containing the CSRF token
  string header_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Name of the cookie used to store the token
  string cookie_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/web/export_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ExportServerConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/export_server_config_request.proto
// version: 1.0.1
// guid: f5105c4f-0736-4a4a-a9c6-004a43fbbd9b

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/export_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ExportServerConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/export_server_config_response.proto
// version: 1.0.1
// guid: b7274c09-ff07-4507-8c91-b7bfc995a64b

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/get_cache_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetCacheConfigRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cache_config_request.proto
// version: 1.0.1
// guid: abc12345-6789-0def-1234-567890abcdef

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message GetCacheConfigRequest {
  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 1;
}
```

---

### get_cache_config_response.proto {#get_cache_config_response}

**Path**: `gcommon/v1/web/get_cache_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `GetCacheConfigResponse`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/cache_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cache_config_response.proto
// version: 1.0.1
// guid: def67890-abcd-1234-5678-90abcdef1234

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/cache_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message GetCacheConfigResponse {
  // The current cache configuration
  WebCacheConfig config = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_cors_config_request.proto {#get_cors_config_request}

**Path**: `gcommon/v1/web/get_cors_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCorsConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cors_config_request.proto
// version: 1.0.0
// guid: c22a2431-29be-4eb5-8ed8-40b2840f03ae

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCorsConfigRequest request definition.
message GetCorsConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_cors_config_response.proto {#get_cors_config_response}

**Path**: `gcommon/v1/web/get_cors_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCorsConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cors_config_response.proto
// version: 1.0.0
// guid: 15367ee2-9586-4b6b-a32f-69bf3a2f3310

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCorsConfigResponse response definition.
message GetCorsConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_security_config_request.proto {#get_security_config_request}

**Path**: `gcommon/v1/web/get_security_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetSecurityConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_security_config_request.proto
// version: 1.0.0
// guid: a5853c6e-88c2-4c4c-962b-c7fc36d4bdef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSecurityConfigRequest request definition.
message GetSecurityConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_security_config_response.proto {#get_security_config_response}

**Path**: `gcommon/v1/web/get_security_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetSecurityConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_security_config_response.proto
// version: 1.0.0
// guid: ad8fcfc2-e9a0-4a3c-8f15-eddc7235c96f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSecurityConfigResponse response definition.
message GetSecurityConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_server_config_request.proto {#get_server_config_request}

**Path**: `gcommon/v1/web/get_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_config_request.proto
// version: 1.0.0
// guid: 78c28db0-b087-4225-b72d-babf47e86db3

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerConfigRequest request definition.
message GetServerConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_server_config_response.proto {#get_server_config_response}

**Path**: `gcommon/v1/web/get_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_config_response.proto
// version: 1.0.0
// guid: 3f909fa5-4f36-4285-8b01-fe1bc5b01fd7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerConfigResponse response definition.
message GetServerConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### handler_config.proto {#handler_config}

**Path**: `gcommon/v1/web/handler_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `HandlerConfig`

**Imports** (4):

- `gcommon/v1/common/handler_type.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handler_config.proto
// version: 1.1.0
// guid: 68d30216-8b75-4c02-88ca-9c39d70d4c4c

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/handler_type.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandlerConfig message definition.
message HandlerConfig {
  // Handler type
  gcommon.v1.common.HandlerType type = 1;

  // Handler-specific configuration
  google.protobuf.Any config = 2;

  // Target for the handler (URL, function name, etc.)
  string target = 3 [(buf.validate.field).string.min_len = 1];

  // Additional handler options
  map<string, string> options = 4;
}
```

---

### health_check_config.proto {#health_check_config}

**Path**: `gcommon/v1/web/health_check_config.proto` **Package**: `gcommon.v1.web` **Lines**: 35

**Messages** (1): `WebHealthCheckConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/health_check_config.proto
// version: 1.1.0
// guid: 7aea6b7c-133f-4443-b7b6-c1cdeb194f0b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HealthCheckConfig defines parameters for performing HTTP health checks.
message WebHealthCheckConfig {
  // HTTP path used for the health check request.
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // Interval between health checks in seconds.
  double interval_seconds = 2 [(buf.validate.field).double.gte = 0.0];

  // Timeout for a single health check in seconds.
  double timeout_seconds = 3 [(buf.validate.field).double.gte = 0.0];

  // Expected HTTP status code indicating a healthy response.
  int32 expected_status = 4 [(buf.validate.field).int32.gte = 0];

  // Additional headers to include with the request.
  map<string, string> headers = 5;

  // Whether the health check is enabled.
  bool enabled = 6;
}
```

---

### import_server_config_request.proto {#import_server_config_request}

**Path**: `gcommon/v1/web/import_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ImportServerConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/import_server_config_request.proto
// version: 1.0.1
// guid: 60a97ec8-a4f9-4606-844c-774a208ca62a

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/import_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ImportServerConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/import_server_config_response.proto
// version: 1.0.1
// guid: 5cf8e464-8b8e-487d-86a0-0707a9490356

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/load_balancer_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `WebLoadBalancerConfig`

**Imports** (4):

- `gcommon/v1/common/load_balance_strategy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/load_balancer_config.proto
// version: 1.1.0
// guid: 773a3c4c-d370-4416-b0d8-bf270ea7d2de

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/load_balance_strategy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// LoadBalancerConfig message definition.
message WebLoadBalancerConfig {
  // Load balancing strategy
  gcommon.v1.common.LoadBalanceStrategy strategy = 1;

  // Upstream server addresses
  repeated string upstreams = 2 [(buf.validate.field).repeated.min_items = 1];

  // Health check path
  string health_check_path = 3 [(buf.validate.field).string.min_len = 1];

  // Timeout for proxy requests
  google.protobuf.Duration timeout = 4;
}
```

---

### middleware_config.proto {#middleware_config}

**Path**: `gcommon/v1/web/middleware_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `MiddlewareConfig`

**Imports** (3):

- `gcommon/v1/common/middleware_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/middleware_config.proto
// version: 1.0.0
// guid: e9b024e1-e72c-48e4-b1c4-5df34ed3e3ac

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/middleware_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// MiddlewareConfig message definition.
// MiddlewareConfig represents a single middleware's configuration.
message MiddlewareConfig {
  // Middleware type
  gcommon.v1.common.MiddlewareType type = 1;

  // Whether the middleware is enabled
  bool enabled = 2;

  // Execution priority (lower runs first)
  int32 priority = 3 [(buf.validate.field).int32.gte = 0];

  // Additional middleware options
  map<string, string> options = 4;
}
```

---

### proxy_config.proto {#proxy_config}

**Path**: `gcommon/v1/web/proxy_config.proto` **Package**: `gcommon.v1.web` **Lines**: 34

**Messages** (1): `ProxyConfig`

**Imports** (5):

- `gcommon/v1/common/proxy_type.proto`
- `gcommon/v1/web/http_header.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/proxy_config.proto
// version: 1.1.0
// guid: 44849c54-6bf7-4211-a8c0-0be1e0c98add

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/proxy_type.proto";
import "gcommon/v1/web/http_header.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ProxyConfig message definition.
message ProxyConfig {
  // Type of proxy
  gcommon.v1.common.ProxyType proxy_type = 1;

  // Target backend URL
  string target_url = 2 [ (buf.validate.field).string.uri = true ];

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

**Path**: `gcommon/v1/web/rate_limit_config.proto` **Package**: `gcommon.v1.web` **Lines**: 36

**Messages** (1): `WebRateLimitConfig`

**Imports** (3):

- `gcommon/v1/common/rate_limit_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/rate_limit_config.proto
// version: 1.0.1
// guid: 180cb5f4-1064-4b88-bbe6-dbc6934ec21e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/rate_limit_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RateLimitConfig message definition.
message WebRateLimitConfig {
  // Enable rate limiting
  bool enabled = 1;

  // Requests per second
  int32 requests_per_second = 2 [(buf.validate.field).int32.gte = 0];

  // Burst size
  int32 burst_size = 3 [(buf.validate.field).int32.gte = 0];

  // Rate limit strategy
  gcommon.v1.common.RateLimitStrategy strategy = 4;

  // Rate limit key extractor
  string key_extractor = 5 [(buf.validate.field).string.min_len = 1];

  // Skip conditions
  repeated string skip_conditions = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### reload_server_config_request.proto {#reload_server_config_request}

**Path**: `gcommon/v1/web/reload_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ReloadServerConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reload_server_config_request.proto
// version: 1.0.1
// guid: abeb1b6f-6a94-4044-b27e-a91c1c9e6042

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/reload_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ReloadServerConfigResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reload_server_config_response.proto
// version: 1.0.1
// guid: a6f6a4cf-253b-4759-a0a7-f699c4cf8463

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/route_config.proto` **Package**: `gcommon.v1.web` **Lines**: 37

**Messages** (1): `RouteConfig`

**Imports** (4):

- `gcommon/v1/common/handler_type.proto`
- `gcommon/v1/common/http_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/route_config.proto
// version: 1.1.0
// guid: ce3f0233-7da2-4e81-8460-b1bf3a6fba53

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/handler_type.proto";
import "gcommon/v1/common/http_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RouteConfig message definition.
message RouteConfig {
  // URL path pattern
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // Allowed HTTP methods
  repeated gcommon.v1.common.HTTPMethod methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Handler name or identifier
  string handler = 3 [(buf.validate.field).string.min_len = 1];

  // Handler type implementation
  gcommon.v1.common.HandlerType handler_type = 4;

  // Middleware IDs applied to this route
  repeated string middleware_ids = 5 [(buf.validate.field).repeated.min_items = 1];

  // Require authentication for route
  bool auth_required = 6;
}
```

---

### security_config.proto {#security_config}

**Path**: `gcommon/v1/web/security_config.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebSecurityConfig`

**Imports** (3):

- `gcommon/v1/web/tls_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/security_config.proto
// version: 1.1.0
// guid: 2d5231ca-5b58-4b11-8448-a87d4ae0154e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/tls_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SecurityConfig message definition.
message WebSecurityConfig {
  // Enable TLS security
  bool enable_tls = 1;

  // TLS configuration details
  WebTLSConfig tls = 2;

  // Allowed host patterns
  repeated string allowed_hosts = 3 [(buf.validate.field).repeated.min_items = 1];

  // Additional security options
  map<string, string> options = 4;
}
```

---

### server_config.proto {#server_config}

**Path**: `gcommon/v1/web/server_config.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `ServerConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_config.proto
// version: 1.0.0
// guid: f4e56c59-17af-4da2-8a92-e1a619fe9fba

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ServerConfig message definition.
// ServerConfig defines basic web server settings.
message ServerConfig {
  // Hostname or IP address to bind
  string host = 1 [(buf.validate.field).string.min_len = 1];

  // Listening port number
  int32 port = 2 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Enable TLS for secure communication
  bool enable_tls = 3;

  // Path to TLS certificate
  string tls_cert_path = 4 [(buf.validate.field).string.min_len = 1];

  // Path to TLS key
  string tls_key_path = 5 [(buf.validate.field).string.min_len = 1];

  // Trusted proxy addresses
  repeated string trusted_proxies = 6 [(buf.validate.field).repeated.min_items = 1];

  // Additional server options
  map<string, string> options = 7;
}
```

---

### session_config.proto {#session_config}

**Path**: `gcommon/v1/web/session_config.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `WebSessionConfig`

**Imports** (4):

- `gcommon/v1/common/cookie_same_site.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/session_config.proto
// version: 1.1.0
// guid: 78ffbac0-1dba-4e18-85e1-ecce179da015

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cookie_same_site.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SessionConfig message definition.
message WebSessionConfig {
  // Session idle timeout before automatic expiration
  google.protobuf.Duration idle_timeout = 1;

  // Absolute session lifetime regardless of activity
  google.protobuf.Duration absolute_timeout = 2;

  // Name of the session cookie
  string cookie_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Use secure cookies (HTTPS only)
  bool secure_cookies = 4;

  // Restrict cookie to HTTP only
  bool http_only = 5;

  // Cookie SameSite policy
  gcommon.v1.common.CookieSameSite same_site = 6;
}
```

---

### ssl_config.proto {#ssl_config}

**Path**: `gcommon/v1/web/ssl_config.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Messages** (1): `SslConfig`

**Imports** (3):

- `gcommon/v1/common/ssl_protocol.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/ssl_config.proto
// version: 1.1.0
// guid: 4d5ec783-ec4b-4ffc-a7e6-28df5382a594

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/ssl_protocol.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SslConfig message definition.
message SslConfig {
  // TLS protocol version
  gcommon.v1.common.SSLProtocol protocol = 1;

  // Path to certificate file
  string cert_file = 2 [(buf.validate.field).string.min_len = 1];

  // Path to key file
  string key_file = 3 [(buf.validate.field).string.min_len = 1];

  // Optional CA bundle path
  string ca_file = 4 [(buf.validate.field).string.min_len = 1];

  // Require client certificates
  bool require_client_auth = 5;
}
```

---

### static_config.proto {#static_config}

**Path**: `gcommon/v1/web/static_config.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `StaticConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/static_config.proto
// version: 1.1.0
// guid: e2d0d32a-6b50-42ec-b728-ef60869cf5ac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StaticConfig message definition.
message StaticConfig {
  // Root directory for static files
  string directory = 1 [(buf.validate.field).string.min_len = 1];

  // Default index files
  repeated string index_files = 2 [(buf.validate.field).repeated.min_items = 1];

  // Enable directory listing
  bool enable_listing = 3;
}
```

---

### template_config.proto {#template_config}

**Path**: `gcommon/v1/web/template_config.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `TemplateConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/template_config.proto
// version: 1.1.0
// guid: 02942f54-029c-468f-85df-cdf3042e8ee6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// TemplateConfig message definition.
message TemplateConfig {
  // Directory containing template files
  string directory = 1 [(buf.validate.field).string.min_len = 1];

  // Default file extension
  string extension = 2 [(buf.validate.field).string.min_len = 1];

  // Reload templates on change
  bool reload = 3;

  // Custom template function names
  repeated string functions = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### timeout_config.proto {#timeout_config}

**Path**: `gcommon/v1/web/timeout_config.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `WebTimeoutConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/timeout_config.proto
// version: 1.0.1
// guid: e3a21e33-e66f-47e7-b7ff-6c6df8a0e9a1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// TimeoutConfig specifies various timeout settings for the server.
message WebTimeoutConfig {
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

**Path**: `gcommon/v1/web/tls_config.proto` **Package**: `gcommon.v1.web` **Lines**: 71

**Messages** (1): `WebTLSConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/tls_config.proto
// version: 1.0.0
// guid: 9f8e7d6c-5b4a-3928-1706-f5e4d3c2b1a0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
// Standard imports
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * TLSConfig defines TLS/SSL configuration for web servers.
 */
message WebTLSConfig {
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
  string server_name = 17 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
}
```

---

### update_cache_config_request.proto {#update_cache_config_request}

**Path**: `gcommon/v1/web/update_cache_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `UpdateCacheConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/cache_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cache_config_request.proto
// version: 1.0.1
// guid: ghi12345-6789-0abc-def1-234567890123

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/cache_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UpdateCacheConfigRequest {
  // The new cache configuration to apply
  WebCacheConfig config = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### update_cache_config_response.proto {#update_cache_config_response}

**Path**: `gcommon/v1/web/update_cache_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Messages** (1): `UpdateCacheConfigResponse`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cache_config_response.proto
// version: 1.0.1
// guid: jkl45678-90ab-cdef-1234-567890abcdef

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UpdateCacheConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### update_cors_config_request.proto {#update_cors_config_request}

**Path**: `gcommon/v1/web/update_cors_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCorsConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cors_config_request.proto
// version: 1.0.0
// guid: 00b7b190-69c5-49c8-8b50-ca9c0e68e231

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCorsConfigRequest request definition.
message UpdateCorsConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_cors_config_response.proto {#update_cors_config_response}

**Path**: `gcommon/v1/web/update_cors_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCorsConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cors_config_response.proto
// version: 1.0.0
// guid: 44e8600c-ebb5-45be-851d-41f41c810996

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCorsConfigResponse response definition.
message UpdateCorsConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_handler_config_request.proto {#update_handler_config_request}

**Path**: `gcommon/v1/web/update_handler_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateHandlerConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_handler_config_request.proto
// version: 1.0.0
// guid: 6241c28b-b274-4d3e-afb4-2c2a65fa5e96

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateHandlerConfigRequest request definition.
message UpdateHandlerConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_handler_config_response.proto {#update_handler_config_response}

**Path**: `gcommon/v1/web/update_handler_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateHandlerConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_handler_config_response.proto
// version: 1.0.0
// guid: f5dc02ec-1a36-4fcd-ae1e-352189358ea7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateHandlerConfigResponse response definition.
message UpdateHandlerConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_middleware_config_request.proto {#update_middleware_config_request}

**Path**: `gcommon/v1/web/update_middleware_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Messages** (1): `UpdateMiddlewareConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/middleware_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_middleware_config_request.proto
// version: 1.0.1
// guid: 30e082c9-2bd6-4472-ae4a-f71e481f04a3
// UpdateMiddlewareConfigRequest request definition.
// UpdateMiddlewareConfigRequest updates an existing middleware configuration.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/middleware_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UpdateMiddlewareConfigRequest {
  // Request metadata for tracing and auth
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Updated middleware configuration
  MiddlewareConfig config = 2;
}
```

---

### update_middleware_config_response.proto {#update_middleware_config_response}

**Path**: `gcommon/v1/web/update_middleware_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `UpdateMiddlewareConfigResponse`

**Imports** (2):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_middleware_config_response.proto
// version: 1.0.1
// guid: e8328b61-1bdf-487b-b874-01de9424625e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/update_route_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateRouteConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_route_config_request.proto
// version: 1.0.0
// guid: 65c64e7e-be8d-4fa3-9bd1-e0c9b752fef9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateRouteConfigRequest request definition.
message UpdateRouteConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_route_config_response.proto {#update_route_config_response}

**Path**: `gcommon/v1/web/update_route_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateRouteConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_route_config_response.proto
// version: 1.0.0
// guid: 07ee551d-a9ae-4d39-995c-3442717c934b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateRouteConfigResponse response definition.
message UpdateRouteConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_security_config_request.proto {#update_security_config_request}

**Path**: `gcommon/v1/web/update_security_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateSecurityConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_security_config_request.proto
// version: 1.0.0
// guid: 69e8edc6-5475-4f71-9753-26c412daab0e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSecurityConfigRequest request definition.
message UpdateSecurityConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_security_config_response.proto {#update_security_config_response}

**Path**: `gcommon/v1/web/update_security_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateSecurityConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_security_config_response.proto
// version: 1.0.0
// guid: 63689787-044d-4302-8175-9745ac688e61

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSecurityConfigResponse response definition.
message UpdateSecurityConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_server_config_request.proto {#update_server_config_request}

**Path**: `gcommon/v1/web/update_server_config_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateServerConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_server_config_request.proto
// version: 1.0.0
// guid: 6a2b47b4-af5e-4e51-9807-18898846cb4a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateServerConfigRequest request definition.
message UpdateServerConfigRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

