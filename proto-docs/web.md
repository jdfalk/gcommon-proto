# web Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 36
- **Messages**: 15
- **Services**: 0
- **Enums**: 21

## Files in this Module

- [auth_method.proto](#auth_method)
- [cache_strategy.proto](#cache_strategy)
- [compression_type.proto](#compression_type)
- [content_type.proto](#content_type)
- [cookie_data.proto](#cookie_data)
- [cookie_same_site.proto](#cookie_same_site)
- [file_info.proto](#file_info)
- [file_metadata.proto](#file_metadata)
- [file_sort_order.proto](#file_sort_order)
- [file_upload.proto](#file_upload)
- [handler_info.proto](#handler_info)
- [handler_type.proto](#handler_type)
- [health_status.proto](#health_status)
- [http_header.proto](#http_header)
- [http_method.proto](#http_method)
- [http_status.proto](#http_status)
- [load_balance_strategy.proto](#load_balance_strategy)
- [middleware_info.proto](#middleware_info)
- [middleware_type.proto](#middleware_type)
- [mime_type.proto](#mime_type)
- [performance_stats.proto](#performance_stats)
- [proxy_type.proto](#proxy_type)
- [rate_limit_strategy.proto](#rate_limit_strategy)
- [route_info.proto](#route_info)
- [route_type.proto](#route_type)
- [same_site_policy.proto](#same_site_policy)
- [server_state.proto](#server_state)
- [server_status.proto](#server_status)
- [session_data.proto](#session_data)
- [session_state.proto](#session_state)
- [ssl_protocol.proto](#ssl_protocol)
- [template_data.proto](#template_data)
- [url_path.proto](#url_path)
- [websocket_info.proto](#websocket_info)
- [websocket_message.proto](#websocket_message)
- [websocket_state.proto](#websocket_state)

## Module Dependencies

**This module depends on**:

- [web_config_1](./web_config_1.md)

**Modules that depend on this one**:

- [auth_api_2](./auth_api_2.md)
- [cache](./cache.md)
- [config_api](./config_api.md)
- [database_api](./database_api.md)
- [health](./health.md)
- [metrics_1](./metrics_1.md)
- [metrics_api_1](./metrics_api_1.md)
- [queue_api_2](./queue_api_2.md)
- [queue_services](./queue_services.md)
- [web_api_1](./web_api_1.md)
- [web_api_2](./web_api_2.md)
- [web_api_3](./web_api_3.md)
- [web_config_1](./web_config_1.md)

---

## Detailed Documentation

### auth_method.proto {#auth_method}

**Path**: `pkg/web/proto/auth_method.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Enums** (1): `AuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/auth_method.proto
// version: 1.0.0
// guid: f8f4a7c2-b0ea-4b6f-8c70-8bd37e0615f9
//
// AuthMethod defines supported authentication mechanisms for the web module.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// Supported authentication mechanisms for HTTP requests.
enum AuthMethod {
  // Default unspecified value.
  AUTH_METHOD_UNSPECIFIED = 0;
  // No authentication required.
  AUTH_METHOD_NONE = 1;
  // HTTP Basic authentication.
  AUTH_METHOD_BASIC = 2;
  // Token-based authentication via Authorization header.
  AUTH_METHOD_TOKEN = 3;
  // OAuth2 based authentication.
  AUTH_METHOD_OAUTH2 = 4;
}

```

---

### cache_strategy.proto {#cache_strategy}

**Path**: `pkg/web/proto/cache_strategy.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Enums** (1): `CacheStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/cache_strategy.proto
// version: 1.0.0
// guid: a2c186e6-9e1e-402b-802f-39fc7b4dfc0d
//
// CacheStrategy defines caching policies for HTTP handlers.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// Available caching policies for responses.
enum CacheStrategy {
  CACHE_STRATEGY_UNSPECIFIED = 0;
  // Do not cache responses.
  CACHE_STRATEGY_NONE = 1;
  // Use in-memory caching only.
  CACHE_STRATEGY_MEMORY = 2;
  // Use distributed cache (e.g., Redis).
  CACHE_STRATEGY_DISTRIBUTED = 3;
  // Use external CDN cache.
  CACHE_STRATEGY_CDN = 4;
}

```

---

### compression_type.proto {#compression_type}

**Path**: `pkg/web/proto/compression_type.proto` **Package**: `gcommon.v1.web` **Lines**: 25

**Enums** (1): `CompressionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/compression_type.proto
// version: 1.0.0
// guid: 0f9ae4d2-05d3-4a49-92e4-3c902a4b8c3e
//
// CompressionType enumerates supported HTTP compression algorithms.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// Supported compression algorithms for responses.
enum CompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  // No compression.
  COMPRESSION_TYPE_NONE = 1;
  // gzip compression.
  COMPRESSION_TYPE_GZIP = 2;
  // brotli compression.
  COMPRESSION_TYPE_BROTLI = 3;
}

```

---

### content_type.proto {#content_type}

**Path**: `pkg/web/proto/content_type.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Enums** (1): `ContentType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/content_type.proto
// version: 1.0.0
// guid: 8bb9871c-690b-4fb4-83e1-735d6815a620
//
// ContentType enumerates common MIME types.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// Well-known MIME types supported by the server.
enum ContentType {
  CONTENT_TYPE_UNSPECIFIED = 0;
  CONTENT_TYPE_HTML = 1;
  CONTENT_TYPE_JSON = 2;
  CONTENT_TYPE_XML = 3;
  CONTENT_TYPE_TEXT = 4;
  CONTENT_TYPE_BINARY = 5;
}

```

---

### cookie_data.proto {#cookie_data}

**Path**: `pkg/web/proto/cookie_data.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `CookieData`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/web/proto/cookie_same_site.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/cookie_data.proto
// version: 1.1.0
// guid: a3854557-84b7-4173-8481-d69bf32fcbd0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
// CookieData message definition.
import "google/protobuf/timestamp.proto";
import "pkg/web/proto/cookie_same_site.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message CookieData {
  // Cookie name
  string name = 1;

  // Cookie value
  string value = 2;

  // Cookie path
  string path = 3;

  // Cookie domain
  string domain = 4;

  // Expiration timestamp
  google.protobuf.Timestamp expires_at = 5;

  // Whether cookie is HTTP only
  bool http_only = 6;

  // Whether cookie is Secure
  bool secure = 7;

  // SameSite policy
  CookieSameSite same_site = 8;
}

```

---

### cookie_same_site.proto {#cookie_same_site}

**Path**: `pkg/web/proto/cookie_same_site.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Enums** (1): `CookieSameSite`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/cookie_same_site.proto
// version: 1.0.0
// guid: b38945ee-58e0-4d5a-9637-f2c57a5a9b31
//
// CookieSameSite defines SameSite settings for cookies.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum CookieSameSite {
  COOKIE_SAME_SITE_UNSPECIFIED = 0;
  COOKIE_SAME_SITE_DEFAULT = 1;
  COOKIE_SAME_SITE_LAX = 2;
  COOKIE_SAME_SITE_STRICT = 3;
  COOKIE_SAME_SITE_NONE = 4;
}

```

---

### file_info.proto {#file_info}

**Path**: `pkg/web/proto/file_info.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Messages** (1): `FileInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/web/proto/mime_type.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/file_info.proto
// version: 1.1.0
// guid: ee525bfe-ed87-4698-bf47-41bff85db277

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/web/proto/mime_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// FileInfo message definition.
message FileInfo {
  // Full file path
  string path = 1;

  // File size in bytes
  int64 size_bytes = 2;

  // MIME type information
  MimeType mime_type = 3;

  // Last modified timestamp
  google.protobuf.Timestamp modified_at = 4;

  // Optional checksum of the file contents
  string checksum = 5;
}

```

---

### file_metadata.proto {#file_metadata}

**Path**: `pkg/web/proto/file_metadata.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Messages** (1): `FileMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/web/proto/mime_type.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/types/file_metadata.proto
// version: 1.1.0
// guid: ac289d4b-2cc8-4cfb-a360-36eef7dba093

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/web/proto/mime_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// FileMetadata message definition.
message FileMetadata {
  // File name
  string name = 1;

  // File size in bytes
  int64 size_bytes = 2;

  // MIME type of the file
  MimeType mime_type = 3;

  // Optional checksum string
  string checksum = 4;

  // Last modification time
  google.protobuf.Timestamp modified_at = 5;
}

```

---

### file_sort_order.proto {#file_sort_order}

**Path**: `pkg/web/proto/file_sort_order.proto` **Package**: `gcommon.v1.web` **Lines**: 40

**Enums** (1): `FileSortOrder`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/file_sort_order.proto
// version: 1.0.0
// guid: f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * File sorting options.
 * Defines how files should be ordered in directory listings.
 */
enum FileSortOrder {
  // Default sorting (name ascending)
  FILE_SORT_ORDER_UNSPECIFIED = 0;

  // Sort by name ascending
  FILE_SORT_ORDER_NAME_ASC = 1;

  // Sort by name descending
  FILE_SORT_ORDER_NAME_DESC = 2;

  // Sort by size ascending
  FILE_SORT_ORDER_SIZE_ASC = 3;

  // Sort by size descending
  FILE_SORT_ORDER_SIZE_DESC = 4;

  // Sort by modification time ascending
  FILE_SORT_ORDER_MODIFIED_ASC = 5;

  // Sort by modification time descending
  FILE_SORT_ORDER_MODIFIED_DESC = 6;
}

```

---

### file_upload.proto {#file_upload}

**Path**: `pkg/web/proto/file_upload.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `FileUpload`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/mime_type.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/file_upload.proto
// version: 1.1.0
// guid: 47f22269-7456-4237-b463-c287580f662d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/mime_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// FileUpload message definition.
message FileUpload {
  // Name of the uploaded file
  string file_name = 1;

  // MIME type of the file
  MimeType content_type = 2;

  // Raw file bytes
  bytes data = 3;

  // Destination path on server
  string destination = 4;
}

```

---

### handler_info.proto {#handler_info}

**Path**: `pkg/web/proto/handler_info.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `HandlerInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/web/proto/handler_config.proto` → [web_config_1](./web_config_1.md#handler_config)

#### Source Code

```protobuf
// file: pkg/web/proto/messages/handler_info.proto
// version: 1.1.0
// guid: ce840d82-a0a7-451a-ace7-062820511c9a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/web/proto/handler_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HandlerInfo message definition.
message HandlerInfo {
  // Handler identifier
  string handler_id = 1;

  // Configuration for the handler
  HandlerConfig config = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3;

  // Last updated timestamp
  google.protobuf.Timestamp updated_at = 4;
}

```

---

### handler_type.proto {#handler_type}

**Path**: `pkg/web/proto/handler_type.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Enums** (1): `HandlerType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/handler_type.proto
// version: 1.0.0
// guid: 38fcdb5d-d9f0-4109-b909-c1da72c74948
//
// HandlerType categorizes incoming request handlers.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum HandlerType {
  HANDLER_TYPE_UNSPECIFIED = 0;
  HANDLER_TYPE_HTTP = 1;
  HANDLER_TYPE_GRPC = 2;
  HANDLER_TYPE_WEBSOCKET = 3;
}

```

---

### health_status.proto {#health_status}

**Path**: `pkg/web/proto/health_status.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Enums** (1): `HealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/health_status.proto
// version: 1.0.0
// guid: c72e470c-79c0-4a29-95b3-10dd038637ef
//
// HealthStatus indicates the operational state of the server.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum HealthStatus {
  HEALTH_STATUS_UNSPECIFIED = 0;
  HEALTH_STATUS_HEALTHY = 1;
  HEALTH_STATUS_DEGRADED = 2;
  HEALTH_STATUS_UNHEALTHY = 3;
}

```

---

### http_header.proto {#http_header}

**Path**: `pkg/web/proto/http_header.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `HttpHeader`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/types/http_header.proto
// version: 1.0.0
// guid: 6a2d7cae-9978-46b7-951c-094945b969f9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HttpHeader message definition.
// HttpHeader represents a single HTTP header field.
message HttpHeader {
  // Header name
  string name = 1;

  // One or more values for the header
  repeated string values = 2;
}

```

---

### http_method.proto {#http_method}

**Path**: `pkg/web/proto/http_method.proto` **Package**: `gcommon.v1.web` **Lines**: 25

**Enums** (1): `HTTPMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/http_method.proto
// version: 1.0.0
// guid: 91d1cc0e-2cad-460c-81e9-236116f31e05
//
// HTTPMethod enumerates supported request verbs.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum HTTPMethod {
  HTTP_METHOD_UNSPECIFIED = 0;
  HTTP_METHOD_GET = 1;
  HTTP_METHOD_POST = 2;
  HTTP_METHOD_PUT = 3;
  HTTP_METHOD_DELETE = 4;
  HTTP_METHOD_PATCH = 5;
  HTTP_METHOD_OPTIONS = 6;
  HTTP_METHOD_HEAD = 7;
}

```

---

### http_status.proto {#http_status}

**Path**: `pkg/web/proto/http_status.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Enums** (1): `HTTPStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/http_status.proto
// version: 1.0.0
// guid: 8e7253f5-0453-42e2-b55a-336dd5c9b589
//
// HTTPStatus enumerates common response status codes.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum HTTPStatus {
  HTTP_STATUS_UNSPECIFIED = 0;
  HTTP_STATUS_OK = 200;
  HTTP_STATUS_BAD_REQUEST = 400;
  HTTP_STATUS_UNAUTHORIZED = 401;
  HTTP_STATUS_FORBIDDEN = 403;
  HTTP_STATUS_NOT_FOUND = 404;
  HTTP_STATUS_INTERNAL_ERROR = 500;
}

```

---

### load_balance_strategy.proto {#load_balance_strategy}

**Path**: `pkg/web/proto/load_balance_strategy.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Enums** (1): `LoadBalanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/load_balance_strategy.proto
// version: 1.0.0
// guid: d147b3b5-5e20-4bf9-9cfe-467e528f59a7
//
// LoadBalanceStrategy lists supported balancing algorithms.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum LoadBalanceStrategy {
  LOAD_BALANCE_STRATEGY_UNSPECIFIED = 0;
  LOAD_BALANCE_STRATEGY_ROUND_ROBIN = 1;
  LOAD_BALANCE_STRATEGY_LEAST_CONNECTIONS = 2;
  LOAD_BALANCE_STRATEGY_IP_HASH = 3;
}

```

---

### middleware_info.proto {#middleware_info}

**Path**: `pkg/web/proto/middleware_info.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `MiddlewareInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/middleware_type.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/middleware_info.proto
// version: 1.1.0
// guid: ddae7421-009f-4275-806a-9ff6d3270232

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/middleware_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// MiddlewareInfo message definition.
message MiddlewareInfo {
  // Middleware identifier
  string id = 1;

  // Middleware type
  MiddlewareType type = 2;

  // Execution order priority
  int32 order = 3;

  // Arbitrary metadata for middleware
  map<string, string> metadata = 4;
}

```

---

### middleware_type.proto {#middleware_type}

**Path**: `pkg/web/proto/middleware_type.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Enums** (1): `MiddlewareType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/middleware_type.proto
// version: 1.0.0
// guid: e6a7b5cb-240b-4636-bb49-9615874e9f9d
//
// MiddlewareType represents categories of HTTP middleware.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum MiddlewareType {
  MIDDLEWARE_TYPE_UNSPECIFIED = 0;
  MIDDLEWARE_TYPE_LOGGING = 1;
  MIDDLEWARE_TYPE_AUTHENTICATION = 2;
  MIDDLEWARE_TYPE_METRICS = 3;
  MIDDLEWARE_TYPE_COMPRESSION = 4;
  MIDDLEWARE_TYPE_CORS = 5;
  MIDDLEWARE_TYPE_RATE_LIMIT = 6;
}

```

---

### mime_type.proto {#mime_type}

**Path**: `pkg/web/proto/mime_type.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `MimeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/types/mime_type.proto
// version: 1.0.0
// guid: b600b818-5782-4f9d-ba1e-e6d3f0f23159

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// MimeType message definition.
// MimeType represents a content type with optional parameters.
message MimeType {
  // Primary type, e.g. "text"
  string type = 1;

  // Subtype, e.g. "html"
  string subtype = 2;

  // Optional parameters such as charset
  map<string, string> parameters = 3;
}

```

---

### performance_stats.proto {#performance_stats}

**Path**: `pkg/web/proto/performance_stats.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Messages** (1): `PerformanceStats`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/performance_stats.proto
// version: 1.1.0
// guid: 2ea24441-9142-4f94-b30e-9d8d07afa209

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// PerformanceStats message definition.
message PerformanceStats {
  // Total number of requests handled
  int64 request_count = 1;

  // Average latency in milliseconds
  double average_latency_ms = 2;

  // Current active connections
  int32 active_connections = 3;

  // Error rate percentage (0-100)
  double error_rate = 4;
}

```

---

### proxy_type.proto {#proxy_type}

**Path**: `pkg/web/proto/proxy_type.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Enums** (1): `ProxyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/proxy_type.proto
// version: 1.0.0
// guid: 9b6f5494-a0d0-4832-a3f3-9d91dbf2c200
//
// ProxyType lists supported proxy configurations.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum ProxyType {
  PROXY_TYPE_UNSPECIFIED = 0;
  PROXY_TYPE_FORWARD = 1;
  PROXY_TYPE_REVERSE = 2;
  PROXY_TYPE_TRANSPARENT = 3;
}

```

---

### rate_limit_strategy.proto {#rate_limit_strategy}

**Path**: `pkg/web/proto/rate_limit_strategy.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Enums** (1): `RateLimitStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/rate_limit_strategy.proto
// version: 1.0.0
// guid: dcc25ed5-f313-4ae4-8be6-bfbc050afb57

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RateLimitStrategy enumeration defines available algorithms for rate limiting.
enum RateLimitStrategy {
  RATE_LIMIT_STRATEGY_UNSPECIFIED = 0;
  RATE_LIMIT_STRATEGY_TOKEN_BUCKET = 1;
  RATE_LIMIT_STRATEGY_FIXED_WINDOW = 2;
  RATE_LIMIT_STRATEGY_SLIDING_WINDOW = 3;
  RATE_LIMIT_STRATEGY_LEAKY_BUCKET = 4;
}

```

---

### route_info.proto {#route_info}

**Path**: `pkg/web/proto/route_info.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `RouteInfo`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/web/proto/route_config.proto` → [web_config_1](./web_config_1.md#route_config)
- `pkg/web/proto/route_type.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/route_info.proto
// version: 1.1.0
// guid: 8154bd31-51b0-4043-9a14-f0614adcd523

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/web/proto/route_config.proto";
import "pkg/web/proto/route_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RouteInfo message definition.
message RouteInfo {
  // Route configuration
  RouteConfig config = 1;

  // Type of route
  RouteType route_type = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3;

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 4;
}

```

---

### route_type.proto {#route_type}

**Path**: `pkg/web/proto/route_type.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Enums** (1): `RouteType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/route_type.proto
// version: 1.0.0
// guid: a655dd19-273c-4cb4-a5ea-71ce983e16cd
//
// RouteType distinguishes different route behaviors.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum RouteType {
  ROUTE_TYPE_UNSPECIFIED = 0;
  ROUTE_TYPE_STATIC_FILE = 1;
  ROUTE_TYPE_API = 2;
  ROUTE_TYPE_REDIRECT = 3;
}

```

---

### same_site_policy.proto {#same_site_policy}

**Path**: `pkg/web/proto/same_site_policy.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Enums** (1): `SameSitePolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/same_site_policy.proto
// version: 1.0.0
// guid: a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * SameSite cookie policy options.
 * Controls when cookies are sent with cross-site requests.
 */
enum SameSitePolicy {
  // Default SameSite policy
  SAME_SITE_POLICY_UNSPECIFIED = 0;

  // No SameSite restriction
  SAME_SITE_POLICY_NONE = 1;

  // Lax SameSite policy
  SAME_SITE_POLICY_LAX = 2;

  // Strict SameSite policy
  SAME_SITE_POLICY_STRICT = 3;
}

```

---

### server_state.proto {#server_state}

**Path**: `pkg/web/proto/server_state.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Enums** (1): `ServerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/server_state.proto
// version: 1.0.0
// guid: edc8f45d-5db0-4b28-b04a-c6eedc98b19b
//
// ServerState represents lifecycle states of the server.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum ServerState {
  SERVER_STATE_UNSPECIFIED = 0;
  SERVER_STATE_STARTING = 1;
  SERVER_STATE_RUNNING = 2;
  SERVER_STATE_STOPPING = 3;
  SERVER_STATE_STOPPED = 4;
}

```

---

### server_status.proto {#server_status}

**Path**: `pkg/web/proto/server_status.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Enums** (1): `ServerStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/server_status.proto
// version: 1.0.1
// guid: 1846bf32-3652-4e52-a6fc-333db4886d5c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ServerStatus enumeration describing server lifecycle states.
enum ServerStatus {
  SERVER_STATUS_UNSPECIFIED = 0;
  SERVER_STATUS_CREATED = 1;
  SERVER_STATUS_STARTING = 2;
  SERVER_STATUS_RUNNING = 3;
  SERVER_STATUS_STOPPING = 4;
  SERVER_STATUS_STOPPED = 5;
  SERVER_STATUS_ERROR = 6;
}

```

---

### session_data.proto {#session_data}

**Path**: `pkg/web/proto/session_data.proto` **Package**: `gcommon.v1.web` **Lines**: 45

**Messages** (1): `SessionData`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/web/proto/session_state.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/session_data.proto
// version: 1.1.0
// guid: f93f7cc5-48c6-4b64-98d2-35549cf19b02

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/web/proto/session_state.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// SessionData message definition.
message SessionData {
  // Unique session identifier
  string session_id = 1;

  // User ID associated with the session
  string user_id = 2;

  // Current session state
  SessionState state = 3;

  // Session creation timestamp
  google.protobuf.Timestamp created_at = 4 [lazy = true];

  // Last access timestamp
  google.protobuf.Timestamp last_access_at = 5 [lazy = true];

  // Session expiration timestamp
  google.protobuf.Timestamp expires_at = 6 [lazy = true];

  // Client IP address
  string ip_address = 7;

  // Client user agent
  string user_agent = 8;

  // Custom session metadata
  map<string, string> metadata = 9;
}

```

---

### session_state.proto {#session_state}

**Path**: `pkg/web/proto/session_state.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Enums** (1): `SessionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/session_state.proto
// version: 1.0.0
// guid: a34ac56d-96ba-4c3e-b36b-a60ba1e62d86
//
// SessionState describes the lifecycle of a user session.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum SessionState {
  SESSION_STATE_UNSPECIFIED = 0;
  SESSION_STATE_ACTIVE = 1;
  SESSION_STATE_EXPIRED = 2;
  SESSION_STATE_REVOKED = 3;
}

```

---

### ssl_protocol.proto {#ssl_protocol}

**Path**: `pkg/web/proto/ssl_protocol.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Enums** (1): `SSLProtocol`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/ssl_protocol.proto
// version: 1.0.0
// guid: 2f6af5d4-4f52-42cd-9ae8-9c6506e0da5e
//
// SSLProtocol lists supported TLS protocol versions.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum SSLProtocol {
  SSL_PROTOCOL_UNSPECIFIED = 0;
  SSL_PROTOCOL_TLS1_0 = 1;
  SSL_PROTOCOL_TLS1_1 = 2;
  SSL_PROTOCOL_TLS1_2 = 3;
  SSL_PROTOCOL_TLS1_3 = 4;
}

```

---

### template_data.proto {#template_data}

**Path**: `pkg/web/proto/template_data.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `TemplateData`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/template_data.proto
// version: 1.1.0
// guid: 31c5d8ac-caa3-4a45-816d-b831995e1757

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// TemplateData message definition.
message TemplateData {
  // Template name
  string name = 1;

  // Arbitrary context data
  google.protobuf.Any context = 2;

  // Template body source
  string template_body = 3;

  // Last compilation timestamp
  google.protobuf.Timestamp compiled_at = 4;
}

```

---

### url_path.proto {#url_path}

**Path**: `pkg/web/proto/url_path.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UrlPath`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/types/url_path.proto
// version: 1.1.0
// guid: 265bd840-fba9-4930-ac69-55c9d3d55210

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UrlPath message definition.
message UrlPath {
  // Individual path segments
  repeated string segments = 1;
}

```

---

### websocket_info.proto {#websocket_info}

**Path**: `pkg/web/proto/websocket_info.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `WebsocketInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/websocket_info.proto
// version: 1.1.0
// guid: 3ebae9bb-41c1-42db-aa71-8ef0660759d4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// WebsocketInfo message definition.
message WebsocketInfo {
  // Connection identifier
  string connection_id = 1;

  // Client IP address
  string client_ip = 2;

  // User agent string
  string user_agent = 3;

  // Connection established timestamp
  google.protobuf.Timestamp connected_at = 4;
}

```

---

### websocket_message.proto {#websocket_message}

**Path**: `pkg/web/proto/websocket_message.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `WebsocketMessage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/websocket_message.proto
// version: 1.1.0
// guid: cba98cf1-43c2-4026-bcc0-779111b41ec1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// WebsocketMessage message definition.
message WebsocketMessage {
  // Connection identifier
  string connection_id = 1;

  // Payload data
  bytes data = 2;

  // Optional message type label
  string message_type = 3;

  // Timestamp when the message was sent
  google.protobuf.Timestamp sent_at = 4;
}

```

---

### websocket_state.proto {#websocket_state}

**Path**: `pkg/web/proto/websocket_state.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Enums** (1): `WebSocketState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/enums/websocket_state.proto
// version: 1.0.0
// guid: 0d71bf70-328b-459b-8bc7-674138f22f92
//
// WebSocketState tracks connection lifecycle stages.
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

enum WebSocketState {
  WEB_SOCKET_STATE_UNSPECIFIED = 0;
  WEB_SOCKET_STATE_CONNECTING = 1;
  WEB_SOCKET_STATE_OPEN = 2;
  WEB_SOCKET_STATE_CLOSING = 3;
  WEB_SOCKET_STATE_CLOSED = 4;
}

```

---
