# web_api_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 33
- **Messages**: 33
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 27

## Files in this Module

- [remove_middleware_request.proto](#remove_middleware_request) ⚠️ 1 issues
- [remove_middleware_response.proto](#remove_middleware_response) ⚠️ 1 issues
- [render_template_request.proto](#render_template_request) ⚠️ 1 issues
- [render_template_response.proto](#render_template_response) ⚠️ 1 issues
- [reset_stats_request.proto](#reset_stats_request) ⚠️ 1 issues
- [reset_stats_response.proto](#reset_stats_response) ⚠️ 1 issues
- [restart_server_request.proto](#restart_server_request) ⚠️ 1 issues
- [restart_server_response.proto](#restart_server_response) ⚠️ 1 issues
- [send_websocket_message_request.proto](#send_websocket_message_request) ⚠️ 1
  issues
- [send_websocket_message_response.proto](#send_websocket_message_response) ⚠️ 1
  issues
- [serve_static_request.proto](#serve_static_request) ⚠️ 1 issues
- [serve_static_response.proto](#serve_static_response) ⚠️ 1 issues
- [start_server_request.proto](#start_server_request)
- [start_server_response.proto](#start_server_response)
- [stop_server_request.proto](#stop_server_request) ⚠️ 1 issues
- [stop_server_response.proto](#stop_server_response) ⚠️ 1 issues
- [stream_server_events_request.proto](#stream_server_events_request) ⚠️ 1
  issues
- [unregister_handler_request.proto](#unregister_handler_request) ⚠️ 1 issues
- [unregister_handler_response.proto](#unregister_handler_response) ⚠️ 1 issues
- [unregister_middleware_request.proto](#unregister_middleware_request)
- [unregister_middleware_response.proto](#unregister_middleware_response)
- [unregister_route_request.proto](#unregister_route_request) ⚠️ 1 issues
- [unregister_route_response.proto](#unregister_route_response) ⚠️ 1 issues
- [update_cookie_request.proto](#update_cookie_request) ⚠️ 1 issues
- [update_cookie_response.proto](#update_cookie_response) ⚠️ 1 issues
- [update_session_request.proto](#update_session_request)
- [update_session_response.proto](#update_session_response)
- [update_ssl_certificate_request.proto](#update_ssl_certificate_request) ⚠️ 1
  issues
- [update_ssl_certificate_response.proto](#update_ssl_certificate_response) ⚠️ 1
  issues
- [upload_file_request.proto](#upload_file_request) ⚠️ 1 issues
- [upload_file_response.proto](#upload_file_response) ⚠️ 1 issues
- [validate_csrf_token_request.proto](#validate_csrf_token_request) ⚠️ 1 issues
- [validate_csrf_token_response.proto](#validate_csrf_token_response) ⚠️ 1
  issues

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [web](./web.md)

**Modules that depend on this one**:

- [auth_services](./auth_services.md)

---

## Detailed Documentation

### remove_middleware_request.proto {#remove_middleware_request}

**Path**: `pkg/web/proto/remove_middleware_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `RemoveMiddlewareRequest`

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
// file: pkg/web/proto/requests/remove_middleware_request.proto
// version: 1.0.0
// guid: 8a7398c4-58cc-47b4-a4db-e53da72f74d5

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
 * RemoveMiddlewareRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message RemoveMiddlewareRequest {
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

### remove_middleware_response.proto {#remove_middleware_response}

**Path**: `pkg/web/proto/remove_middleware_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `RemoveMiddlewareResponse`

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
// file: pkg/web/proto/responses/remove_middleware_response.proto
// version: 1.0.0
// guid: 6b5a3ac2-61d8-478d-874b-c0fcbb4eceed

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
 * RemoveMiddlewareResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message RemoveMiddlewareResponse {
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

### render_template_request.proto {#render_template_request}

**Path**: `pkg/web/proto/render_template_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RenderTemplateRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/render_template_request.proto
// version: 1.0.0
// guid: 7af6bf58-6fbd-443a-a1b4-bbff1986136c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RenderTemplateRequest request definition.
message RenderTemplateRequest {
  string placeholder = 1;
}

```

---

### render_template_response.proto {#render_template_response}

**Path**: `pkg/web/proto/render_template_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RenderTemplateResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/render_template_response.proto
// version: 1.0.0
// guid: 97e5b67b-3c0e-46dc-9e4b-66964408d78e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RenderTemplateResponse response definition.
message RenderTemplateResponse {
  string placeholder = 1;
}

```

---

### reset_stats_request.proto {#reset_stats_request}

**Path**: `pkg/web/proto/reset_stats_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ResetStatsRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/reset_stats_request.proto
// version: 1.0.0
// guid: 489cfa57-6202-40a6-bdff-a76a1f55fa1d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ResetStatsRequest request definition.
message ResetStatsRequest {
  string placeholder = 1;
}

```

---

### reset_stats_response.proto {#reset_stats_response}

**Path**: `pkg/web/proto/reset_stats_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ResetStatsResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/reset_stats_response.proto
// version: 1.0.0
// guid: 1d37d4bf-fa7b-4794-aa70-4d3b11142625

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ResetStatsResponse response definition.
message ResetStatsResponse {
  string placeholder = 1;
}

```

---

### restart_server_request.proto {#restart_server_request}

**Path**: `pkg/web/proto/restart_server_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RestartServerRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/restart_server_request.proto
// version: 1.0.0
// guid: 9fc26a42-b6e1-4d63-a78a-24fa09be9abb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RestartServerRequest request definition.
message RestartServerRequest {
  string placeholder = 1;
}

```

---

### restart_server_response.proto {#restart_server_response}

**Path**: `pkg/web/proto/restart_server_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RestartServerResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/restart_server_response.proto
// version: 1.0.0
// guid: a53bc58d-9a8b-490a-b3c7-f33025aad447

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RestartServerResponse response definition.
message RestartServerResponse {
  string placeholder = 1;
}

```

---

### send_websocket_message_request.proto {#send_websocket_message_request}

**Path**: `pkg/web/proto/send_websocket_message_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `SendWebsocketMessageRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/send_websocket_message_request.proto
// version: 1.0.0
// guid: 0f379368-5941-4e80-a7c6-3d66aafd5d54

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// SendWebsocketMessageRequest request definition.
message SendWebsocketMessageRequest {
  string placeholder = 1;
}

```

---

### send_websocket_message_response.proto {#send_websocket_message_response}

**Path**: `pkg/web/proto/send_websocket_message_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `SendWebsocketMessageResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/send_websocket_message_response.proto
// version: 1.0.0
// guid: 844cd4f0-f98b-4548-8b5a-fd4b1cc457ff

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// SendWebsocketMessageResponse response definition.
message SendWebsocketMessageResponse {
  string placeholder = 1;
}

```

---

### serve_static_request.proto {#serve_static_request}

**Path**: `pkg/web/proto/serve_static_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ServeStaticRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/serve_static_request.proto
// version: 1.0.0
// guid: ed014e20-4f0a-447b-8c14-ef6b0f967b36

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ServeStaticRequest request definition.
message ServeStaticRequest {
  string placeholder = 1;
}

```

---

### serve_static_response.proto {#serve_static_response}

**Path**: `pkg/web/proto/serve_static_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ServeStaticResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/serve_static_response.proto
// version: 1.0.0
// guid: d3354a82-ddd1-48c8-956b-d715c8f9ac83

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ServeStaticResponse response definition.
message ServeStaticResponse {
  string placeholder = 1;
}

```

---

### start_server_request.proto {#start_server_request}

**Path**: `pkg/web/proto/start_server_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 23

**Messages** (1): `StartServerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/start_server_request.proto
// version: 1.0.1
// guid: 25892d63-79d6-4211-8d7e-aa4cdbf1fa99
// StartServerRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message StartServerRequest {
  // Server ID
  string server_id = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}

```

---

### start_server_response.proto {#start_server_response}

**Path**: `pkg/web/proto/start_server_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 30

**Messages** (1): `StartServerResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/web/proto/server_status.proto` → [web](./web.md#server_status)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/start_server_response.proto
// version: 1.0.1
// guid: 0655b1fa-e5f9-419d-a4f1-dcd1a5b474b5

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/web/proto/server_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// StartServerResponse response definition.
message StartServerResponse {
  // Success status
  bool success = 1;

  // Server status
  ServerStatus status = 2;

  // Listen address
  string listen_address = 3;

  // Error information
  gcommon.v1.common.Error error = 4;
}

```

---

### stop_server_request.proto {#stop_server_request}

**Path**: `pkg/web/proto/stop_server_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `StopServerRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/stop_server_request.proto
// version: 1.0.0
// guid: 400d2dd2-87fd-497d-99e3-a7c2470f7377

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// StopServerRequest request definition.
message StopServerRequest {
  string placeholder = 1;
}

```

---

### stop_server_response.proto {#stop_server_response}

**Path**: `pkg/web/proto/stop_server_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `StopServerResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/stop_server_response.proto
// version: 1.0.0
// guid: 968f4a2e-5b03-4188-8c64-209017b813da

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// StopServerResponse response definition.
message StopServerResponse {
  string placeholder = 1;
}

```

---

### stream_server_events_request.proto {#stream_server_events_request}

**Path**: `pkg/web/proto/stream_server_events_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `StreamServerEventsRequest`

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
// file: pkg/web/proto/requests/stream_server_events_request.proto
// version: 1.0.0
// guid: 0316e0ad-e7e2-4a26-82d6-0a4b3d92c9ec

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
 * StreamServerEventsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message StreamServerEventsRequest {
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

### unregister_handler_request.proto {#unregister_handler_request}

**Path**: `pkg/web/proto/unregister_handler_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UnregisterHandlerRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/unregister_handler_request.proto
// version: 1.0.0
// guid: b3a2283a-da75-498d-bcd6-73068020f71f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UnregisterHandlerRequest request definition.
message UnregisterHandlerRequest {
  string placeholder = 1;
}

```

---

### unregister_handler_response.proto {#unregister_handler_response}

**Path**: `pkg/web/proto/unregister_handler_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UnregisterHandlerResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/unregister_handler_response.proto
// version: 1.0.0
// guid: 60c00ce0-2fa0-4af1-a7ab-48b4351a72cf

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UnregisterHandlerResponse response definition.
message UnregisterHandlerResponse {
  string placeholder = 1;
}

```

---

### unregister_middleware_request.proto {#unregister_middleware_request}

**Path**: `pkg/web/proto/unregister_middleware_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 26

**Messages** (1): `UnregisterMiddlewareRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/unregister_middleware_request.proto
// version: 1.1.0
// guid: 9123fb9b-ced5-4251-adb0-dcb9b453b8b5
// UnregisterMiddlewareRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message UnregisterMiddlewareRequest {
  // Server identifier
  string server_id = 1;

  // Middleware identifier
  string middleware_id = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### unregister_middleware_response.proto {#unregister_middleware_response}

**Path**: `pkg/web/proto/unregister_middleware_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 23

**Messages** (1): `UnregisterMiddlewareResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/unregister_middleware_response.proto
// version: 1.1.0
// guid: 008a5536-7226-40b2-8424-92dcc7075e14

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UnregisterMiddlewareResponse response definition.
message UnregisterMiddlewareResponse {
  // Operation success flag
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;
}

```

---

### unregister_route_request.proto {#unregister_route_request}

**Path**: `pkg/web/proto/unregister_route_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UnregisterRouteRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/unregister_route_request.proto
// version: 1.0.0
// guid: 6bd8df0c-0003-4464-b76f-837bb1a72af6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UnregisterRouteRequest request definition.
message UnregisterRouteRequest {
  string placeholder = 1;
}

```

---

### unregister_route_response.proto {#unregister_route_response}

**Path**: `pkg/web/proto/unregister_route_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UnregisterRouteResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/unregister_route_response.proto
// version: 1.0.0
// guid: 701eb2b6-d704-4e56-9ee0-ad1a1e244453

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UnregisterRouteResponse response definition.
message UnregisterRouteResponse {
  string placeholder = 1;
}

```

---

### update_cookie_request.proto {#update_cookie_request}

**Path**: `pkg/web/proto/update_cookie_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateCookieRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_cookie_request.proto
// version: 1.0.0
// guid: 3762d335-0618-4954-be4c-297ba3a2ed8e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateCookieRequest request definition.
message UpdateCookieRequest {
  string placeholder = 1;
}

```

---

### update_cookie_response.proto {#update_cookie_response}

**Path**: `pkg/web/proto/update_cookie_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UpdateCookieResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_cookie_response.proto
// version: 1.0.0
// guid: e817a298-f3a9-4451-bdc6-e8967ed8175e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateCookieResponse response definition.
message UpdateCookieResponse {
  string placeholder = 1;
}

```

---

### update_session_request.proto {#update_session_request}

**Path**: `pkg/web/proto/update_session_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 22

**Messages** (1): `UpdateSessionRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/requests/update_session_request.proto
// version: 1.1.0
// guid: 4c543371-4882-4a5c-9fe2-481de3738e67

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateSessionRequest request definition.
message UpdateSessionRequest {
  // Identifier of the session to update
  string session_id = 1;

  // New metadata to apply
  map<string, string> metadata = 2;
}

```

---

### update_session_response.proto {#update_session_response}

**Path**: `pkg/web/proto/update_session_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 20

**Messages** (1): `UpdateSessionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/session_data.proto` → [web](./web.md#session_data)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/update_session_response.proto
// version: 1.1.0
// guid: f1b380a2-162b-44ad-a6c0-5fd39e3add91

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/session_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UpdateSessionResponse response definition.
message UpdateSessionResponse {
  // Updated session data
  SessionData session = 1;
}

```

---

### update_ssl_certificate_request.proto {#update_ssl_certificate_request}

**Path**: `pkg/web/proto/update_ssl_certificate_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `UpdateSSLCertificateRequest`

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
// file: pkg/web/proto/requests/update_s_s_l_certificate_request.proto
// version: 1.0.0
// guid: eec70ef5-baf4-4799-ba2d-3b00ad4b2e32

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
 * UpdateSSLCertificateRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message UpdateSSLCertificateRequest {
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

### update_ssl_certificate_response.proto {#update_ssl_certificate_response}

**Path**: `pkg/web/proto/update_ssl_certificate_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `UpdateSSLCertificateResponse`

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
// file: pkg/web/proto/responses/update_s_s_l_certificate_response.proto
// version: 1.0.0
// guid: f2ee4b98-5830-4ea9-a968-5cf5c6216d5d

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
 * UpdateSSLCertificateResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message UpdateSSLCertificateResponse {
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

### upload_file_request.proto {#upload_file_request}

**Path**: `pkg/web/proto/upload_file_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UploadFileRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/upload_file_request.proto
// version: 1.0.0
// guid: c341b4e3-de76-449b-93d0-fbb1fe4e1655

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UploadFileRequest request definition.
message UploadFileRequest {
  string placeholder = 1;
}

```

---

### upload_file_response.proto {#upload_file_response}

**Path**: `pkg/web/proto/upload_file_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `UploadFileResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/upload_file_response.proto
// version: 1.0.0
// guid: d6f9dad0-3449-4808-b710-f73253ba1b06

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// UploadFileResponse response definition.
message UploadFileResponse {
  string placeholder = 1;
}

```

---

### validate_csrf_token_request.proto {#validate_csrf_token_request}

**Path**: `pkg/web/proto/validate_csrf_token_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ValidateCsrfTokenRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/validate_csrf_token_request.proto
// version: 1.0.0
// guid: a28f712d-4b1c-417b-ad6c-eb154c429933

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ValidateCsrfTokenRequest request definition.
message ValidateCsrfTokenRequest {
  string placeholder = 1;
}

```

---

### validate_csrf_token_response.proto {#validate_csrf_token_response}

**Path**: `pkg/web/proto/validate_csrf_token_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ValidateCsrfTokenResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/validate_csrf_token_response.proto
// version: 1.0.0
// guid: d29634a2-4e04-442d-9de5-e11d1e300ed4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ValidateCsrfTokenResponse response definition.
message ValidateCsrfTokenResponse {
  string placeholder = 1;
}

```

---
