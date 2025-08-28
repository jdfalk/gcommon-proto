# web_api_1 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [add_middleware_request.proto](#add_middleware_request)
- [add_middleware_response.proto](#add_middleware_response)
- [authenticate_request.proto](#authenticate_request)
- [authenticate_response.proto](#authenticate_response)
- [authorize_request.proto](#authorize_request)
- [authorize_response.proto](#authorize_response)
- [close_websocket_request.proto](#close_websocket_request)
- [close_websocket_response.proto](#close_websocket_response)
- [create_cookie_request.proto](#create_cookie_request)
- [create_cookie_response.proto](#create_cookie_response)
- [create_server_request.proto](#create_server_request)
- [create_server_response.proto](#create_server_response)
- [create_session_request.proto](#create_session_request)
- [create_session_response.proto](#create_session_response)
- [create_template_request.proto](#create_template_request)
- [create_template_response.proto](#create_template_response)
- [create_websocket_request.proto](#create_websocket_request)
- [create_websocket_response.proto](#create_websocket_response)
- [delete_cookie_request.proto](#delete_cookie_request)
- [delete_cookie_response.proto](#delete_cookie_response)
- [delete_file_request.proto](#delete_file_request)
- [delete_file_response.proto](#delete_file_response)
- [delete_session_request.proto](#delete_session_request)
- [delete_session_response.proto](#delete_session_response)
- [delete_template_request.proto](#delete_template_request)
- [delete_template_response.proto](#delete_template_response)
- [download_file_request.proto](#download_file_request)
- [download_file_response.proto](#download_file_response)
- [flush_cache_request.proto](#flush_cache_request)
- [flush_cache_response.proto](#flush_cache_response)
- [generate_csrf_token_request.proto](#generate_csrf_token_request)
- [generate_csrf_token_response.proto](#generate_csrf_token_response)
- [get_access_logs_request.proto](#get_access_logs_request)
- [get_access_logs_response.proto](#get_access_logs_response)
- [get_cookie_request.proto](#get_cookie_request)
- [get_cookie_response.proto](#get_cookie_response)
- [get_file_info_request.proto](#get_file_info_request)
- [get_file_info_response.proto](#get_file_info_response)
- [get_handler_info_request.proto](#get_handler_info_request)
- [get_handler_info_response.proto](#get_handler_info_response)
- [get_metrics_request.proto](#get_metrics_request)
- [get_metrics_response.proto](#get_metrics_response)
- [get_middleware_info_request.proto](#get_middleware_info_request)
- [get_middleware_info_response.proto](#get_middleware_info_response)
- [get_performance_stats_request.proto](#get_performance_stats_request)
- [get_performance_stats_response.proto](#get_performance_stats_response)
- [get_route_info_request.proto](#get_route_info_request)
- [get_route_info_response.proto](#get_route_info_response)
- [get_route_metrics_request.proto](#get_route_metrics_request)
- [get_route_metrics_response.proto](#get_route_metrics_response)
---


## Detailed Documentation

### add_middleware_request.proto {#add_middleware_request}

**Path**: `gcommon/v1/web/add_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `AddMiddlewareRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/add_middleware_request.proto
// version: 1.0.1
// guid: f3eee777-6416-43d6-9c51-7d0857359e6b

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
 * AddMiddlewareRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AddMiddlewareRequest {
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

### add_middleware_response.proto {#add_middleware_response}

**Path**: `gcommon/v1/web/add_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `AddMiddlewareResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/add_middleware_response.proto
// version: 1.0.1
// guid: 7630a43f-ad62-483e-8e6e-3a8b8a24a8ee

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
 * AddMiddlewareResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AddMiddlewareResponse {
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

### authenticate_request.proto {#authenticate_request}

**Path**: `gcommon/v1/web/authenticate_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthenticateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authenticate_request.proto
// version: 1.0.0
// guid: 94442c59-c156-4b84-b389-9423724c6635

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthenticateRequest request definition.
message WebAuthenticateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### authenticate_response.proto {#authenticate_response}

**Path**: `gcommon/v1/web/authenticate_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthenticateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authenticate_response.proto
// version: 1.0.0
// guid: f058366e-3b22-4c95-8be7-0ddf15eec85f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthenticateResponse response definition.
message WebAuthenticateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### authorize_request.proto {#authorize_request}

**Path**: `gcommon/v1/web/authorize_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthorizeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authorize_request.proto
// version: 1.0.0
// guid: 1582f475-35f6-43c9-ac19-74b29568fa64

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthorizeRequest request definition.
message WebAuthorizeRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### authorize_response.proto {#authorize_response}

**Path**: `gcommon/v1/web/authorize_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebAuthorizeResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/authorize_response.proto
// version: 1.0.0
// guid: df7cdfcb-6b3a-4991-a9e2-1b08a908570b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// AuthorizeResponse response definition.
message WebAuthorizeResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### close_websocket_request.proto {#close_websocket_request}

**Path**: `gcommon/v1/web/close_websocket_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CloseWebsocketRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/close_websocket_request.proto
// version: 1.0.0
// guid: 43005508-aedc-4d2d-9b42-6fce6bd32ad9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CloseWebsocketRequest request definition.
message CloseWebsocketRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### close_websocket_response.proto {#close_websocket_response}

**Path**: `gcommon/v1/web/close_websocket_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CloseWebsocketResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/close_websocket_response.proto
// version: 1.0.0
// guid: eca486b9-3dd5-4720-9813-30a5b343bd8a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CloseWebsocketResponse response definition.
message CloseWebsocketResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_cookie_request.proto {#create_cookie_request}

**Path**: `gcommon/v1/web/create_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 55

**Messages** (1): `CreateCookieRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/same_site_policy.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_cookie_request.proto
// version: 1.2.0
// guid: 44838568-f1f6-44f1-b4a5-2299a815ccad

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/same_site_policy.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Request to create an HTTP cookie.
 * Used for session management and client state storage.
 */
message CreateCookieRequest {
  // Cookie name (required)
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cookie value
  string value = 2;

  // Cookie domain
  string domain = 3;

  // Cookie path
  string path = 4;

  // Cookie expiration time
  google.protobuf.Timestamp expires = 5;

  // Maximum age in seconds
  int32 max_age = 6;

  // Whether cookie is secure (HTTPS only)
  bool secure = 7;

  // Whether cookie is HTTP only
  bool http_only = 8;

  // Cookie SameSite attribute
  gcommon.v1.common.SameSitePolicy same_site = 9;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 10;
}
```

---

### create_cookie_response.proto {#create_cookie_response}

**Path**: `gcommon/v1/web/create_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_cookie_response.proto
// version: 1.0.0
// guid: 0d0254f8-1e8f-4646-817d-7ec57f25c88c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateCookieResponse response definition.
message CreateCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_server_request.proto {#create_server_request}

**Path**: `gcommon/v1/web/create_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `CreateServerRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_server_request.proto
// version: 1.0.1
// guid: a071056d-f27f-4932-aff8-57a2344955f2

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
 * CreateServerRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message CreateServerRequest {
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

### create_server_response.proto {#create_server_response}

**Path**: `gcommon/v1/web/create_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `CreateServerResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_server_response.proto
// version: 1.0.1
// guid: e65e4983-3fb2-4098-b293-efc34aee92d8

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
 * CreateServerResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message CreateServerResponse {
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

### create_session_request.proto {#create_session_request}

**Path**: `gcommon/v1/web/create_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 25

**Messages** (1): `WebCreateSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_session_request.proto
// version: 1.1.0
// guid: 1022341d-b551-43d4-b090-2354a82b624c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateSessionRequest request definition.
message WebCreateSessionRequest {
  // User ID for the new session
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional initial metadata
  map<string, string> metadata = 2;
}
```

---

### create_session_response.proto {#create_session_response}

**Path**: `gcommon/v1/web/create_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebCreateSessionResponse`

**Imports** (2):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_session_response.proto
// version: 1.1.1
// guid: 5b7bc14e-bb7d-4d0d-bd5b-c35bc5fb7bda

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateSessionResponse response definition.
message WebCreateSessionResponse {
  // Newly created session details
  SessionData session = 1;
}
```

---

### create_template_request.proto {#create_template_request}

**Path**: `gcommon/v1/web/create_template_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_template_request.proto
// version: 1.0.0
// guid: 0cb8a2eb-9d24-4b5c-9b3a-b66164b5ab50

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateTemplateRequest request definition.
message CreateTemplateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_template_response.proto {#create_template_response}

**Path**: `gcommon/v1/web/create_template_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_template_response.proto
// version: 1.0.0
// guid: 294f4744-3238-404c-94ec-85cb4b77bfbe

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateTemplateResponse response definition.
message CreateTemplateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_websocket_request.proto {#create_websocket_request}

**Path**: `gcommon/v1/web/create_websocket_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateWebsocketRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_websocket_request.proto
// version: 1.0.0
// guid: df288e0f-57af-4326-a2a7-91ff6b3ed38b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateWebsocketRequest request definition.
message CreateWebsocketRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### create_websocket_response.proto {#create_websocket_response}

**Path**: `gcommon/v1/web/create_websocket_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `CreateWebsocketResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/create_websocket_response.proto
// version: 1.0.0
// guid: e46f3fe0-b2cb-4d13-982a-4a28a59a2025

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// CreateWebsocketResponse response definition.
message CreateWebsocketResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_cookie_request.proto {#delete_cookie_request}

**Path**: `gcommon/v1/web/delete_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteCookieRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_cookie_request.proto
// version: 1.0.0
// guid: 704e1ea8-b8a8-4c45-9a2f-3571aa92021e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteCookieRequest request definition.
message DeleteCookieRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_cookie_response.proto {#delete_cookie_response}

**Path**: `gcommon/v1/web/delete_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_cookie_response.proto
// version: 1.0.0
// guid: 2b9f0298-3825-4e48-8606-dae4d44c0b9c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteCookieResponse response definition.
message DeleteCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_file_request.proto {#delete_file_request}

**Path**: `gcommon/v1/web/delete_file_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_file_request.proto
// version: 1.0.0
// guid: d13d91f6-e28f-4932-bd69-254f9ab926cf

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteFileRequest request definition.
message DeleteFileRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_file_response.proto {#delete_file_response}

**Path**: `gcommon/v1/web/delete_file_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteFileResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_file_response.proto
// version: 1.0.0
// guid: ece03faf-72a0-4c28-9084-8636a30178d0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteFileResponse response definition.
message DeleteFileResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_session_request.proto {#delete_session_request}

**Path**: `gcommon/v1/web/delete_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 20

**Messages** (1): `WebDeleteSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_session_request.proto
// version: 1.1.0
// guid: 90ce1e00-4c38-47bf-b246-fba60817030a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteSessionRequest request definition.
message WebDeleteSessionRequest {
  // Identifier of the session to delete
  string session_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_session_response.proto {#delete_session_response}

**Path**: `gcommon/v1/web/delete_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 18

**Messages** (1): `WebDeleteSessionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_session_response.proto
// version: 1.1.1
// guid: 4115c974-f373-4e67-aeb0-fff852ec685a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteSessionResponse response definition.
message WebDeleteSessionResponse {
  // Indicates if the session was deleted
  bool success = 1;
}
```

---

### delete_template_request.proto {#delete_template_request}

**Path**: `gcommon/v1/web/delete_template_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_template_request.proto
// version: 1.0.0
// guid: 77e6e070-8d45-407c-bf0d-4fa8e59286c9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteTemplateRequest request definition.
message DeleteTemplateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_template_response.proto {#delete_template_response}

**Path**: `gcommon/v1/web/delete_template_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DeleteTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/delete_template_response.proto
// version: 1.0.0
// guid: 694ea8d5-14d0-4199-ba28-c703229f2782

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DeleteTemplateResponse response definition.
message DeleteTemplateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### download_file_request.proto {#download_file_request}

**Path**: `gcommon/v1/web/download_file_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DownloadFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/download_file_request.proto
// version: 1.0.0
// guid: 9505fac6-9597-4f3f-9adf-caff8184f860

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DownloadFileRequest request definition.
message DownloadFileRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### download_file_response.proto {#download_file_response}

**Path**: `gcommon/v1/web/download_file_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `DownloadFileResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/download_file_response.proto
// version: 1.0.0
// guid: ad823437-e5e1-4b0c-afb4-9eea7f74a97f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// DownloadFileResponse response definition.
message DownloadFileResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### flush_cache_request.proto {#flush_cache_request}

**Path**: `gcommon/v1/web/flush_cache_request.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `FlushCacheRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/flush_cache_request.proto
// version: 1.0.0
// guid: mno78901-2345-6789-abcd-ef1234567890

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message FlushCacheRequest {
  // Optional namespace to flush (if empty, flushes all)
  string namespace = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### flush_cache_response.proto {#flush_cache_response}

**Path**: `gcommon/v1/web/flush_cache_response.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `FlushCacheResponse`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/flush_cache_response.proto
// version: 1.0.0
// guid: pqr01234-5678-9abc-def0-123456789012

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message FlushCacheResponse {
  // Whether the flush was successful
  bool success = 1;

  // Number of entries flushed
  int64 entries_flushed = 2 [(buf.validate.field).int64.gte = 0];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### generate_csrf_token_request.proto {#generate_csrf_token_request}

**Path**: `gcommon/v1/web/generate_csrf_token_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GenerateCsrfTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/generate_csrf_token_request.proto
// version: 1.0.0
// guid: b05fa822-c009-4975-ac54-ef39dbdcaa7e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GenerateCsrfTokenRequest request definition.
message GenerateCsrfTokenRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### generate_csrf_token_response.proto {#generate_csrf_token_response}

**Path**: `gcommon/v1/web/generate_csrf_token_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GenerateCsrfTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/generate_csrf_token_response.proto
// version: 1.0.0
// guid: 2883e71c-133f-4b82-aadf-9883eb41bb68

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GenerateCsrfTokenResponse response definition.
message GenerateCsrfTokenResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_access_logs_request.proto {#get_access_logs_request}

**Path**: `gcommon/v1/web/get_access_logs_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetAccessLogsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_access_logs_request.proto
// version: 1.0.1
// guid: b1ae7686-f402-48c3-a4cf-a89cf32e9fe3

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
 * GetAccessLogsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetAccessLogsRequest {
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

### get_access_logs_response.proto {#get_access_logs_response}

**Path**: `gcommon/v1/web/get_access_logs_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetAccessLogsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_access_logs_response.proto
// version: 1.0.1
// guid: d3a99c97-12b6-4158-b9b9-339b0aaa8d87

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
 * GetAccessLogsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetAccessLogsResponse {
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

### get_cookie_request.proto {#get_cookie_request}

**Path**: `gcommon/v1/web/get_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCookieRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cookie_request.proto
// version: 1.0.0
// guid: c813599e-921b-4476-a0ce-e43beac01bdb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCookieRequest request definition.
message GetCookieRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_cookie_response.proto {#get_cookie_response}

**Path**: `gcommon/v1/web/get_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_cookie_response.proto
// version: 1.0.0
// guid: 9408a9d0-e0d9-4b42-97c3-bb662f1a5990

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetCookieResponse response definition.
message GetCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_file_info_request.proto {#get_file_info_request}

**Path**: `gcommon/v1/web/get_file_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetFileInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_file_info_request.proto
// version: 1.0.0
// guid: cf3df7e0-3738-456e-9082-d5ccd898b372

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetFileInfoRequest request definition.
message GetFileInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_file_info_response.proto {#get_file_info_response}

**Path**: `gcommon/v1/web/get_file_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetFileInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_file_info_response.proto
// version: 1.0.0
// guid: c49bbb1e-7f94-4a6d-84e5-e9517b988719

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetFileInfoResponse response definition.
message GetFileInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_handler_info_request.proto {#get_handler_info_request}

**Path**: `gcommon/v1/web/get_handler_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetHandlerInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_handler_info_request.proto
// version: 1.0.0
// guid: 8e46bc43-d8f7-4053-bb73-4e458022efb6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetHandlerInfoRequest request definition.
message GetHandlerInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_handler_info_response.proto {#get_handler_info_response}

**Path**: `gcommon/v1/web/get_handler_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetHandlerInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_handler_info_response.proto
// version: 1.0.0
// guid: d6203aa9-40d1-47d9-8c6d-ea2d7cf3c76e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetHandlerInfoResponse response definition.
message GetHandlerInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_metrics_request.proto {#get_metrics_request}

**Path**: `gcommon/v1/web/get_metrics_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebGetMetricsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_metrics_request.proto
// version: 1.0.0
// guid: 21aad446-24e7-442f-a61f-0287b7742589

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMetricsRequest request definition.
message WebGetMetricsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_metrics_response.proto {#get_metrics_response}

**Path**: `gcommon/v1/web/get_metrics_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebGetMetricsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_metrics_response.proto
// version: 1.0.0
// guid: d42faed3-d602-4066-a445-01c6f1bf8448

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMetricsResponse response definition.
message WebGetMetricsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_middleware_info_request.proto {#get_middleware_info_request}

**Path**: `gcommon/v1/web/get_middleware_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetMiddlewareInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_middleware_info_request.proto
// version: 1.0.0
// guid: c8c3314e-63ab-46b2-a217-5c81a2f55eb0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMiddlewareInfoRequest request definition.
message GetMiddlewareInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_middleware_info_response.proto {#get_middleware_info_response}

**Path**: `gcommon/v1/web/get_middleware_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetMiddlewareInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_middleware_info_response.proto
// version: 1.0.0
// guid: 46941911-33dc-4735-8f43-e834fa94e935

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetMiddlewareInfoResponse response definition.
message GetMiddlewareInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_performance_stats_request.proto {#get_performance_stats_request}

**Path**: `gcommon/v1/web/get_performance_stats_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetPerformanceStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_performance_stats_request.proto
// version: 1.0.0
// guid: 2858eba1-31b0-47f0-9d29-91c78943323b

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetPerformanceStatsRequest request definition.
message GetPerformanceStatsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_performance_stats_response.proto {#get_performance_stats_response}

**Path**: `gcommon/v1/web/get_performance_stats_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetPerformanceStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_performance_stats_response.proto
// version: 1.0.0
// guid: ecadd1ec-a5eb-4813-a0c7-055cfc58c7be

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetPerformanceStatsResponse response definition.
message GetPerformanceStatsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_route_info_request.proto {#get_route_info_request}

**Path**: `gcommon/v1/web/get_route_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetRouteInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_info_request.proto
// version: 1.0.0
// guid: bc9c9890-0ee4-4a5f-b0e9-1f06ae76801c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetRouteInfoRequest request definition.
message GetRouteInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_route_info_response.proto {#get_route_info_response}

**Path**: `gcommon/v1/web/get_route_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetRouteInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_info_response.proto
// version: 1.0.0
// guid: 8717580f-b835-4cf1-97f8-afc41daf8ed4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetRouteInfoResponse response definition.
message GetRouteInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_route_metrics_request.proto {#get_route_metrics_request}

**Path**: `gcommon/v1/web/get_route_metrics_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetRouteMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_metrics_request.proto
// version: 1.0.1
// guid: fd25fe7a-1f87-4979-8502-8ff4b7022e24

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
 * GetRouteMetricsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetRouteMetricsRequest {
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

### get_route_metrics_response.proto {#get_route_metrics_response}

**Path**: `gcommon/v1/web/get_route_metrics_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetRouteMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_route_metrics_response.proto
// version: 1.0.1
// guid: a14b318a-9397-452e-8f29-201aa145aa19

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
 * GetRouteMetricsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetRouteMetricsResponse {
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

