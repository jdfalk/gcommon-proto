# web Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 16
- **Messages**: 16
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [cookie_data.proto](#cookie_data)
- [file_info.proto](#file_info)
- [file_metadata.proto](#file_metadata)
- [file_upload.proto](#file_upload)
- [handler_info.proto](#handler_info)
- [http_header.proto](#http_header)
- [middleware_info.proto](#middleware_info)
- [mime_type.proto](#mime_type)
- [performance_stats.proto](#performance_stats)
- [route_info.proto](#route_info)
- [session_data.proto](#session_data)
- [template_data.proto](#template_data)
- [url_path.proto](#url_path)
- [web.proto](#web)
- [websocket_info.proto](#websocket_info)
- [websocket_message.proto](#websocket_message)
---


## Detailed Documentation

### cookie_data.proto {#cookie_data}

**Path**: `gcommon/v1/web/cookie_data.proto` **Package**: `gcommon.v1.web` **Lines**: 45

**Messages** (1): `CookieData`

**Imports** (4):

- `gcommon/v1/common/cookie_same_site.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cookie_data.proto
// version: 1.1.0
// guid: a3854557-84b7-4173-8481-d69bf32fcbd0

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/cookie_same_site.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// CookieData message definition.

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message CookieData {
  // Cookie name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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
  gcommon.v1.common.CookieSameSite same_site = 8;
}
```

---

### file_info.proto {#file_info}

**Path**: `gcommon/v1/web/file_info.proto` **Package**: `gcommon.v1.web` **Lines**: 34

**Messages** (1): `FileInfo`

**Imports** (4):

- `gcommon/v1/web/mime_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_info.proto
// version: 1.1.0
// guid: ee525bfe-ed87-4698-bf47-41bff85db277

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/mime_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// FileInfo message definition.
message FileInfo {
  // Full file path
  string path = 1 [(buf.validate.field).string.min_len = 1];

  // File size in bytes
  int64 size_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // MIME type information
  MimeType mime_type = 3;

  // Last modified timestamp
  google.protobuf.Timestamp modified_at = 4;

  // Optional checksum of the file contents
  string checksum = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### file_metadata.proto {#file_metadata}

**Path**: `gcommon/v1/web/file_metadata.proto` **Package**: `gcommon.v1.web` **Lines**: 36

**Messages** (1): `FileMetadata`

**Imports** (4):

- `gcommon/v1/web/mime_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_metadata.proto
// version: 1.1.0
// guid: ac289d4b-2cc8-4cfb-a360-36eef7dba093

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/mime_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// FileMetadata message definition.
message FileMetadata {
  // File name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

### file_upload.proto {#file_upload}

**Path**: `gcommon/v1/web/file_upload.proto` **Package**: `gcommon.v1.web` **Lines**: 32

**Messages** (1): `FileUpload`

**Imports** (3):

- `gcommon/v1/web/mime_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_upload.proto
// version: 1.1.0
// guid: 47f22269-7456-4237-b463-c287580f662d

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/mime_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// FileUpload message definition.
message FileUpload {
  // Name of the uploaded file
  string file_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Content type validation
  MimeType content_type = 2;

  // Raw file bytes
  bytes data = 3;

  // Destination path on server
  string destination = 4;
}
```

---

### handler_info.proto {#handler_info}

**Path**: `gcommon/v1/web/handler_info.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `HandlerInfo`

**Imports** (4):

- `gcommon/v1/web/handler_config.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handler_info.proto
// version: 1.1.0
// guid: ce840d82-a0a7-451a-ace7-062820511c9a

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/handler_config.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandlerInfo message definition.
message HandlerInfo {
  // Handler identifier
  string handler_id = 1;

  // Configuration for the handler
  HandlerConfig config = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

  // Last updated timestamp
  google.protobuf.Timestamp updated_at = 4;
}
```

---

### http_header.proto {#http_header}

**Path**: `gcommon/v1/web/http_header.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `HttpHeader`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_header.proto
// version: 1.0.0
// guid: 6a2d7cae-9978-46b7-951c-094945b969f9

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HttpHeader message definition.
// HttpHeader represents a single HTTP header field.
message HttpHeader {
  // Header name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // One or more values for the header
  repeated string values = 2;
}
```

---

### middleware_info.proto {#middleware_info}

**Path**: `gcommon/v1/web/middleware_info.proto` **Package**: `gcommon.v1.web` **Lines**: 32

**Messages** (1): `MiddlewareInfo`

**Imports** (3):

- `gcommon/v1/common/middleware_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/middleware_info.proto
// version: 1.1.0
// guid: ddae7421-009f-4275-806a-9ff6d3270232

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/middleware_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// MiddlewareInfo message definition.
message MiddlewareInfo {
  // Middleware identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Middleware type
  gcommon.v1.common.MiddlewareType type = 2;

  // Execution order priority
  int32 order = 3;

  // Arbitrary metadata for middleware
  map<string, string> metadata = 4;
}
```

---

### mime_type.proto {#mime_type}

**Path**: `gcommon/v1/web/mime_type.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Messages** (1): `MimeType`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/mime_type.proto
// version: 1.0.0
// guid: b600b818-5782-4f9d-ba1e-e6d3f0f23159

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// MimeType message definition.
// MimeType represents a content type with optional parameters.
message MimeType {
  // Primary type, e.g. "text"
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Subtype, e.g. "html"
  string subtype = 2 [(buf.validate.field).string.min_len = 1];

  // Optional parameters such as charset
  map<string, string> parameters = 3;
}
```

---

### performance_stats.proto {#performance_stats}

**Path**: `gcommon/v1/web/performance_stats.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `WebPerformanceStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/performance_stats.proto
// version: 1.1.0
// guid: 2ea24441-9142-4f94-b30e-9d8d07afa209

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// PerformanceStats message definition.
message WebPerformanceStats {
  // Total number of requests handled
  int64 request_count = 1 [(buf.validate.field).int64.gte = 0];

  // Average latency in milliseconds
  double average_latency_ms = 2 [(buf.validate.field).double.gte = 0.0];

  // Current active connections
  int32 active_connections = 3 [(buf.validate.field).int32.gte = 0];

  // Error rate percentage (0-100)
  double error_rate = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### route_info.proto {#route_info}

**Path**: `gcommon/v1/web/route_info.proto` **Package**: `gcommon.v1.web` **Lines**: 31

**Messages** (1): `RouteInfo`

**Imports** (5):

- `gcommon/v1/common/route_type.proto`
- `gcommon/v1/web/route_config.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/route_info.proto
// version: 1.1.0
// guid: 8154bd31-51b0-4043-9a14-f0614adcd523

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/route_type.proto";
import "gcommon/v1/web/route_config.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RouteInfo message definition.
message RouteInfo {
  // Route configuration
  RouteConfig config = 1;

  // Type of route
  gcommon.v1.common.RouteType route_type = 2;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

  // Last update timestamp
  google.protobuf.Timestamp updated_at = 4;
}
```

---

### session_data.proto {#session_data}

**Path**: `gcommon/v1/web/session_data.proto` **Package**: `gcommon.v1.web` **Lines**: 48

**Messages** (1): `SessionData`

**Imports** (4):

- `gcommon/v1/common/web_session_state.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/session_data.proto
// version: 1.1.0
// guid: f93f7cc5-48c6-4b64-98d2-35549cf19b02

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/web_session_state.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// SessionData message definition.
message SessionData {
  // Unique session identifier
  string session_id = 1;

  // User ID associated with the session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Current session state
  gcommon.v1.common.WebSessionState state = 3;

  // Session creation timestamp
  google.protobuf.Timestamp created_at = 4 [lazy = true, (buf.validate.field).required = true];

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

### template_data.proto {#template_data}

**Path**: `gcommon/v1/web/template_data.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Messages** (1): `TemplateData`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/template_data.proto
// version: 1.1.0
// guid: 31c5d8ac-caa3-4a45-816d-b831995e1757

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// TemplateData message definition.
message TemplateData {
  // Template name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

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

**Path**: `gcommon/v1/web/url_path.proto` **Package**: `gcommon.v1.web` **Lines**: 20

**Messages** (1): `UrlPath`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/url_path.proto
// version: 1.1.0
// guid: 265bd840-fba9-4930-ac69-55c9d3d55210

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UrlPath message definition.
message UrlPath {
  // Individual path segments
  repeated string segments = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### web.proto {#web}

**Path**: `gcommon/v1/web/web.proto` **Package**: `gcommon.v1.web` **Lines**: 38

**Messages** (1): `WebInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/web.proto
// version: 1.0.0
// guid: 5f6e7d8c-9b0a-1423-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Web represents basic web server information and metadata.
 * Contains fundamental web service configuration and status.
 */
message WebInfo {
  // Web server name/identifier
  string server_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Server version
  string version = 2;

  // Server start time
  google.protobuf.Timestamp started_at = 3;

  // Whether the server is accepting requests
  bool accepting_requests = 4;

  // Server port number
  int32 port = 5;
}
```

---

### websocket_info.proto {#websocket_info}

**Path**: `gcommon/v1/web/websocket_info.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebsocketInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/websocket_info.proto
// version: 1.1.0
// guid: 3ebae9bb-41c1-42db-aa71-8ef0660759d4

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// WebsocketInfo message definition.
message WebsocketInfo {
  // Connection identifier
  string connection_id = 1 [(buf.validate.field).string.min_len = 1];

  // Client IP address
  string client_ip = 2 [(buf.validate.field).string.min_len = 1];

  // User agent string
  string user_agent = 3 [(buf.validate.field).string.min_len = 1];

  // Connection established timestamp
  google.protobuf.Timestamp connected_at = 4;
}
```

---

### websocket_message.proto {#websocket_message}

**Path**: `gcommon/v1/web/websocket_message.proto` **Package**: `gcommon.v1.web` **Lines**: 30

**Messages** (1): `WebsocketMessage`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/websocket_message.proto
// version: 1.1.0
// guid: cba98cf1-43c2-4026-bcc0-779111b41ec1

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// WebsocketMessage message definition.
message WebsocketMessage {
  // Connection identifier
  string connection_id = 1 [(buf.validate.field).string.min_len = 1];

  // Payload data
  bytes data = 2;

  // Optional message type label
  string message_type = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the message was sent
  google.protobuf.Timestamp sent_at = 4;
}
```

---

