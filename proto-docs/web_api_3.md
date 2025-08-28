# web_api_3 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 30
- **Messages**: 30
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [render_template_request.proto](#render_template_request)
- [render_template_response.proto](#render_template_response)
- [reset_stats_request.proto](#reset_stats_request)
- [reset_stats_response.proto](#reset_stats_response)
- [restart_server_request.proto](#restart_server_request)
- [restart_server_response.proto](#restart_server_response)
- [send_websocket_message_request.proto](#send_websocket_message_request)
- [send_websocket_message_response.proto](#send_websocket_message_response)
- [serve_static_request.proto](#serve_static_request)
- [serve_static_response.proto](#serve_static_response)
- [start_server_request.proto](#start_server_request)
- [start_server_response.proto](#start_server_response)
- [stop_server_request.proto](#stop_server_request)
- [stop_server_response.proto](#stop_server_response)
- [unregister_handler_request.proto](#unregister_handler_request)
- [unregister_handler_response.proto](#unregister_handler_response)
- [unregister_middleware_request.proto](#unregister_middleware_request)
- [unregister_middleware_response.proto](#unregister_middleware_response)
- [unregister_route_request.proto](#unregister_route_request)
- [unregister_route_response.proto](#unregister_route_response)
- [update_cookie_request.proto](#update_cookie_request)
- [update_cookie_response.proto](#update_cookie_response)
- [update_session_request.proto](#update_session_request)
- [update_session_response.proto](#update_session_response)
- [update_ssl_certificate_request.proto](#update_ssl_certificate_request)
- [update_ssl_certificate_response.proto](#update_ssl_certificate_response)
- [upload_file_request.proto](#upload_file_request)
- [upload_file_response.proto](#upload_file_response)
- [validate_csrf_token_request.proto](#validate_csrf_token_request)
- [validate_csrf_token_response.proto](#validate_csrf_token_response)
---


## Detailed Documentation

### render_template_request.proto {#render_template_request}

**Path**: `gcommon/v1/web/render_template_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RenderTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/render_template_request.proto
// version: 1.0.0
// guid: 7af6bf58-6fbd-443a-a1b4-bbff1986136c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RenderTemplateRequest request definition.
message RenderTemplateRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### render_template_response.proto {#render_template_response}

**Path**: `gcommon/v1/web/render_template_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RenderTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/render_template_response.proto
// version: 1.0.0
// guid: 97e5b67b-3c0e-46dc-9e4b-66964408d78e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RenderTemplateResponse response definition.
message RenderTemplateResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### reset_stats_request.proto {#reset_stats_request}

**Path**: `gcommon/v1/web/reset_stats_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ResetStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reset_stats_request.proto
// version: 1.0.0
// guid: 489cfa57-6202-40a6-bdff-a76a1f55fa1d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ResetStatsRequest request definition.
message ResetStatsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### reset_stats_response.proto {#reset_stats_response}

**Path**: `gcommon/v1/web/reset_stats_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ResetStatsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/reset_stats_response.proto
// version: 1.0.0
// guid: 1d37d4bf-fa7b-4794-aa70-4d3b11142625

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ResetStatsResponse response definition.
message ResetStatsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### restart_server_request.proto {#restart_server_request}

**Path**: `gcommon/v1/web/restart_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RestartServerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/restart_server_request.proto
// version: 1.0.0
// guid: 9fc26a42-b6e1-4d63-a78a-24fa09be9abb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RestartServerRequest request definition.
message RestartServerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### restart_server_response.proto {#restart_server_response}

**Path**: `gcommon/v1/web/restart_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RestartServerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/restart_server_response.proto
// version: 1.0.0
// guid: a53bc58d-9a8b-490a-b3c7-f33025aad447

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RestartServerResponse response definition.
message RestartServerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### send_websocket_message_request.proto {#send_websocket_message_request}

**Path**: `gcommon/v1/web/send_websocket_message_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `SendWebsocketMessageRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/send_websocket_message_request.proto
// version: 1.0.0
// guid: 0f379368-5941-4e80-a7c6-3d66aafd5d54

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SendWebsocketMessageRequest request definition.
message SendWebsocketMessageRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### send_websocket_message_response.proto {#send_websocket_message_response}

**Path**: `gcommon/v1/web/send_websocket_message_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `SendWebsocketMessageResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/send_websocket_message_response.proto
// version: 1.0.0
// guid: 844cd4f0-f98b-4548-8b5a-fd4b1cc457ff

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SendWebsocketMessageResponse response definition.
message SendWebsocketMessageResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### serve_static_request.proto {#serve_static_request}

**Path**: `gcommon/v1/web/serve_static_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ServeStaticRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/serve_static_request.proto
// version: 1.0.0
// guid: ed014e20-4f0a-447b-8c14-ef6b0f967b36

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ServeStaticRequest request definition.
message ServeStaticRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### serve_static_response.proto {#serve_static_response}

**Path**: `gcommon/v1/web/serve_static_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ServeStaticResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/serve_static_response.proto
// version: 1.0.0
// guid: d3354a82-ddd1-48c8-956b-d715c8f9ac83

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ServeStaticResponse response definition.
message ServeStaticResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### start_server_request.proto {#start_server_request}

**Path**: `gcommon/v1/web/start_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 24

**Messages** (1): `StartServerRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/start_server_request.proto
// version: 1.0.1
// guid: 25892d63-79d6-4211-8d7e-aa4cdbf1fa99
// StartServerRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message StartServerRequest {
  // Server ID
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### start_server_response.proto {#start_server_response}

**Path**: `gcommon/v1/web/start_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `StartServerResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/server_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/start_server_response.proto
// version: 1.0.1
// guid: 0655b1fa-e5f9-419d-a4f1-dcd1a5b474b5

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/server_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StartServerResponse response definition.
message StartServerResponse {
  // Success status
  bool success = 1;

  // Server status
  gcommon.v1.common.ServerStatus status = 2;

  // Listen address
  string listen_address = 3 [(buf.validate.field).string.min_len = 1];

  // Error information
  gcommon.v1.common.Error error = 4;
}
```

---

### stop_server_request.proto {#stop_server_request}

**Path**: `gcommon/v1/web/stop_server_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `StopServerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/stop_server_request.proto
// version: 1.0.0
// guid: 400d2dd2-87fd-497d-99e3-a7c2470f7377

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StopServerRequest request definition.
message StopServerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_server_response.proto {#stop_server_response}

**Path**: `gcommon/v1/web/stop_server_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `StopServerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/stop_server_response.proto
// version: 1.0.0
// guid: 968f4a2e-5b03-4188-8c64-209017b813da

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// StopServerResponse response definition.
message StopServerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_handler_request.proto {#unregister_handler_request}

**Path**: `gcommon/v1/web/unregister_handler_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterHandlerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_handler_request.proto
// version: 1.0.0
// guid: b3a2283a-da75-498d-bcd6-73068020f71f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterHandlerRequest request definition.
message UnregisterHandlerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_handler_response.proto {#unregister_handler_response}

**Path**: `gcommon/v1/web/unregister_handler_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterHandlerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_handler_response.proto
// version: 1.0.0
// guid: 60c00ce0-2fa0-4af1-a7ab-48b4351a72cf

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterHandlerResponse response definition.
message UnregisterHandlerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_middleware_request.proto {#unregister_middleware_request}

**Path**: `gcommon/v1/web/unregister_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Messages** (1): `UnregisterMiddlewareRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_middleware_request.proto
// version: 1.1.0
// guid: 9123fb9b-ced5-4251-adb0-dcb9b453b8b5
// UnregisterMiddlewareRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message UnregisterMiddlewareRequest {
  // Server identifier
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Middleware identifier
  string middleware_id = 2 [(buf.validate.field).string.min_len = 1];

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### unregister_middleware_response.proto {#unregister_middleware_response}

**Path**: `gcommon/v1/web/unregister_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `UnregisterMiddlewareResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_middleware_response.proto
// version: 1.1.1
// guid: 008a5536-7226-40b2-8424-92dcc7075e14

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/unregister_route_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterRouteRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_route_request.proto
// version: 1.0.0
// guid: 6bd8df0c-0003-4464-b76f-837bb1a72af6

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterRouteRequest request definition.
message UnregisterRouteRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### unregister_route_response.proto {#unregister_route_response}

**Path**: `gcommon/v1/web/unregister_route_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UnregisterRouteResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/unregister_route_response.proto
// version: 1.0.0
// guid: 701eb2b6-d704-4e56-9ee0-ad1a1e244453

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UnregisterRouteResponse response definition.
message UnregisterRouteResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_cookie_request.proto {#update_cookie_request}

**Path**: `gcommon/v1/web/update_cookie_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCookieRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cookie_request.proto
// version: 1.0.0
// guid: 3762d335-0618-4954-be4c-297ba3a2ed8e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCookieRequest request definition.
message UpdateCookieRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_cookie_response.proto {#update_cookie_response}

**Path**: `gcommon/v1/web/update_cookie_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateCookieResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_cookie_response.proto
// version: 1.0.0
// guid: e817a298-f3a9-4451-bdc6-e8967ed8175e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateCookieResponse response definition.
message UpdateCookieResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_session_request.proto {#update_session_request}

**Path**: `gcommon/v1/web/update_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 23

**Messages** (1): `WebUpdateSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_session_request.proto
// version: 1.1.0
// guid: 4c543371-4882-4a5c-9fe2-481de3738e67

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSessionRequest request definition.
message WebUpdateSessionRequest {
  // Identifier of the session to update
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // New metadata to apply
  map<string, string> metadata = 2;
}
```

---

### update_session_response.proto {#update_session_response}

**Path**: `gcommon/v1/web/update_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebUpdateSessionResponse`

**Imports** (2):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_session_response.proto
// version: 1.1.1
// guid: f1b380a2-162b-44ad-a6c0-5fd39e3add91

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateSessionResponse response definition.
message WebUpdateSessionResponse {
  // Updated session data
  SessionData session = 1;
}
```

---

### update_ssl_certificate_request.proto {#update_ssl_certificate_request}

**Path**: `gcommon/v1/web/update_ssl_certificate_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `UpdateSSLCertificateRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_ssl_certificate_request.proto
// version: 1.0.1
// guid: eec70ef5-baf4-4799-ba2d-3b00ad4b2e32

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

**Path**: `gcommon/v1/web/update_ssl_certificate_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `UpdateSSLCertificateResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_ssl_certificate_response.proto
// version: 1.0.1
// guid: f2ee4b98-5830-4ea9-a968-5cf5c6216d5d

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

**Path**: `gcommon/v1/web/upload_file_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UploadFileRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/upload_file_request.proto
// version: 1.0.0
// guid: c341b4e3-de76-449b-93d0-fbb1fe4e1655

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UploadFileRequest request definition.
message UploadFileRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### upload_file_response.proto {#upload_file_response}

**Path**: `gcommon/v1/web/upload_file_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UploadFileResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/upload_file_response.proto
// version: 1.0.0
// guid: d6f9dad0-3449-4808-b710-f73253ba1b06

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UploadFileResponse response definition.
message UploadFileResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### validate_csrf_token_request.proto {#validate_csrf_token_request}

**Path**: `gcommon/v1/web/validate_csrf_token_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ValidateCsrfTokenRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/validate_csrf_token_request.proto
// version: 1.0.0
// guid: a28f712d-4b1c-417b-ad6c-eb154c429933

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ValidateCsrfTokenRequest request definition.
message ValidateCsrfTokenRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### validate_csrf_token_response.proto {#validate_csrf_token_response}

**Path**: `gcommon/v1/web/validate_csrf_token_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ValidateCsrfTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/validate_csrf_token_response.proto
// version: 1.0.0
// guid: d29634a2-4e04-442d-9de5-e11d1e300ed4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ValidateCsrfTokenResponse response definition.
message ValidateCsrfTokenResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

