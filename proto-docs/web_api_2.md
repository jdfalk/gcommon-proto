# web_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [get_server_health_request.proto](#get_server_health_request)
- [get_server_health_response.proto](#get_server_health_response)
- [get_server_logs_request.proto](#get_server_logs_request)
- [get_server_logs_response.proto](#get_server_logs_response)
- [get_server_metrics_request.proto](#get_server_metrics_request)
- [get_server_metrics_response.proto](#get_server_metrics_response)
- [get_server_status_request.proto](#get_server_status_request)
- [get_server_status_response.proto](#get_server_status_response)
- [get_session_request.proto](#get_session_request)
- [get_session_response.proto](#get_session_response)
- [get_ssl_certificate_info_request.proto](#get_ssl_certificate_info_request)
- [get_ssl_certificate_info_response.proto](#get_ssl_certificate_info_response)
- [get_template_info_request.proto](#get_template_info_request)
- [get_template_info_response.proto](#get_template_info_response)
- [get_websocket_info_request.proto](#get_websocket_info_request)
- [get_websocket_info_response.proto](#get_websocket_info_response)
- [handle_request.proto](#handle_request)
- [handle_request_request.proto](#handle_request_request)
- [handle_request_response.proto](#handle_request_response)
- [handle_response.proto](#handle_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [http_request.proto](#http_request)
- [http_response.proto](#http_response)
- [list_cookies_request.proto](#list_cookies_request)
- [list_cookies_response.proto](#list_cookies_response)
- [list_files_request.proto](#list_files_request)
- [list_files_response.proto](#list_files_response)
- [list_handlers_request.proto](#list_handlers_request)
- [list_handlers_response.proto](#list_handlers_response)
- [list_middleware_request.proto](#list_middleware_request)
- [list_middleware_response.proto](#list_middleware_response)
- [list_routes_request.proto](#list_routes_request)
- [list_routes_response.proto](#list_routes_response)
- [list_servers_request.proto](#list_servers_request)
- [list_servers_response.proto](#list_servers_response)
- [list_sessions_request.proto](#list_sessions_request)
- [list_sessions_response.proto](#list_sessions_response)
- [list_templates_request.proto](#list_templates_request)
- [list_templates_response.proto](#list_templates_response)
- [list_websockets_request.proto](#list_websockets_request)
- [list_websockets_response.proto](#list_websockets_response)
- [register_handler_request.proto](#register_handler_request)
- [register_handler_response.proto](#register_handler_response)
- [register_middleware_request.proto](#register_middleware_request)
- [register_middleware_response.proto](#register_middleware_response)
- [register_route_request.proto](#register_route_request)
- [register_route_response.proto](#register_route_response)
- [remove_middleware_request.proto](#remove_middleware_request)
- [remove_middleware_response.proto](#remove_middleware_response)
---


## Detailed Documentation

### get_server_health_request.proto {#get_server_health_request}

**Path**: `gcommon/v1/web/get_server_health_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerHealthRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_health_request.proto
// version: 1.0.1
// guid: 150fcfd0-33d0-453e-a628-70235d0d760d

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
 * GetServerHealthRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerHealthRequest {
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

### get_server_health_response.proto {#get_server_health_response}

**Path**: `gcommon/v1/web/get_server_health_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerHealthResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_health_response.proto
// version: 1.0.1
// guid: 3b792629-d4ac-4821-8ab0-badba4ad3aea

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
 * GetServerHealthResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerHealthResponse {
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

### get_server_logs_request.proto {#get_server_logs_request}

**Path**: `gcommon/v1/web/get_server_logs_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerLogsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_logs_request.proto
// version: 1.0.1
// guid: 8e8d56e9-af3b-4205-bab3-d528f6528104

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
 * GetServerLogsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerLogsRequest {
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

### get_server_logs_response.proto {#get_server_logs_response}

**Path**: `gcommon/v1/web/get_server_logs_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerLogsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_logs_response.proto
// version: 1.0.1
// guid: 2bece2cb-e346-41b9-8e2b-2bdbbbe4c94f

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
 * GetServerLogsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerLogsResponse {
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

### get_server_metrics_request.proto {#get_server_metrics_request}

**Path**: `gcommon/v1/web/get_server_metrics_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_metrics_request.proto
// version: 1.0.1
// guid: 3f87be3d-9370-43a0-88fc-13d5eb9eb37a

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
 * GetServerMetricsRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerMetricsRequest {
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

### get_server_metrics_response.proto {#get_server_metrics_response}

**Path**: `gcommon/v1/web/get_server_metrics_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_metrics_response.proto
// version: 1.0.1
// guid: c7d26642-5c77-4ba5-b891-5876066cfaba

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
 * GetServerMetricsResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetServerMetricsResponse {
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

### get_server_status_request.proto {#get_server_status_request}

**Path**: `gcommon/v1/web/get_server_status_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerStatusRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_status_request.proto
// version: 1.0.0
// guid: 589c81b7-a311-4da5-9604-ece349fc6e55

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerStatusRequest request definition.
message GetServerStatusRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_server_status_response.proto {#get_server_status_response}

**Path**: `gcommon/v1/web/get_server_status_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetServerStatusResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_server_status_response.proto
// version: 1.0.0
// guid: 3cb9f0ee-d816-469a-89f1-0486c03c9f3a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetServerStatusResponse response definition.
message GetServerStatusResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_session_request.proto {#get_session_request}

**Path**: `gcommon/v1/web/get_session_request.proto` **Package**: `gcommon.v1.web` **Lines**: 20

**Messages** (1): `WebGetSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_session_request.proto
// version: 1.1.0
// guid: 5ab16058-a2a8-463c-b101-b1f24df275ef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSessionRequest request definition.
message WebGetSessionRequest {
  // Identifier of the session to retrieve
  string session_id = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_session_response.proto {#get_session_response}

**Path**: `gcommon/v1/web/get_session_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebGetSessionResponse`

**Imports** (2):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_session_response.proto
// version: 1.1.1
// guid: 97fcede8-5243-4901-b423-41a0723fb0c7

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetSessionResponse response definition.
message WebGetSessionResponse {
  // Retrieved session data
  SessionData session = 1;
}
```

---

### get_ssl_certificate_info_request.proto {#get_ssl_certificate_info_request}

**Path**: `gcommon/v1/web/get_ssl_certificate_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetSSLCertificateInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_ssl_certificate_info_request.proto
// version: 1.0.1
// guid: dc573011-0a3c-48ac-9de4-3a7718171101

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
 * GetSSLCertificateInfoRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetSSLCertificateInfoRequest {
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

### get_ssl_certificate_info_response.proto {#get_ssl_certificate_info_response}

**Path**: `gcommon/v1/web/get_ssl_certificate_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetSSLCertificateInfoResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_ssl_certificate_info_response.proto
// version: 1.0.1
// guid: 9ffed0bc-f94b-47a9-8a07-7e01d998e746

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
 * GetSSLCertificateInfoResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message GetSSLCertificateInfoResponse {
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

### get_template_info_request.proto {#get_template_info_request}

**Path**: `gcommon/v1/web/get_template_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetTemplateInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_template_info_request.proto
// version: 1.0.0
// guid: 0660a509-2a17-4efb-be93-9712e8b2c84e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetTemplateInfoRequest request definition.
message GetTemplateInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_template_info_response.proto {#get_template_info_response}

**Path**: `gcommon/v1/web/get_template_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetTemplateInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_template_info_response.proto
// version: 1.0.0
// guid: e1cc4547-9204-48a5-84a3-3c7526d71494

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetTemplateInfoResponse response definition.
message GetTemplateInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_websocket_info_request.proto {#get_websocket_info_request}

**Path**: `gcommon/v1/web/get_websocket_info_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetWebsocketInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_websocket_info_request.proto
// version: 1.0.0
// guid: 48f87988-451a-453b-9f51-2c7175112c25

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetWebsocketInfoRequest request definition.
message GetWebsocketInfoRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_websocket_info_response.proto {#get_websocket_info_response}

**Path**: `gcommon/v1/web/get_websocket_info_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetWebsocketInfoResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/get_websocket_info_response.proto
// version: 1.0.0
// guid: 147168a6-ba00-4881-8ddd-dd52c3af7198

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// GetWebsocketInfoResponse response definition.
message GetWebsocketInfoResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### handle_request.proto {#handle_request}

**Path**: `gcommon/v1/web/handle_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `HandleRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_request.proto
// version: 1.0.0
// guid: 50315b83-99de-4058-b883-61ebfa2b47a8

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandleRequest request definition.
message HandleRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### handle_request_request.proto {#handle_request_request}

**Path**: `gcommon/v1/web/handle_request_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `HandleRequestRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_request_request.proto
// version: 1.0.1
// guid: 0af45f43-528e-4f14-a668-eebf5ae2d975

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
 * HandleRequestRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HandleRequestRequest {
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

### handle_request_response.proto {#handle_request_response}

**Path**: `gcommon/v1/web/handle_request_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `HandleRequestResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_request_response.proto
// version: 1.0.1
// guid: c75ed356-c467-40db-ac2c-529e7b956802

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
 * HandleRequestResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HandleRequestResponse {
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

### handle_response.proto {#handle_response}

**Path**: `gcommon/v1/web/handle_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `HandleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handle_response.proto
// version: 1.0.0
// guid: 54494647-eae8-4100-9c64-809b55fe043a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HandleResponse response definition.
message HandleResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/web/health_check_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `WebHealthCheckRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/health_check_request.proto
// version: 1.0.1
// guid: 08748b61-ccf0-4bfe-bfc6-ad2778f3959c
// HealthCheckRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message WebHealthCheckRequest {
  // Request metadata for the HTTP server.
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/web/health_check_response.proto` **Package**: `gcommon.v1.web` **Lines**: 27

**Messages** (1): `WebHealthCheckResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/health_check_response.proto
// version: 1.0.1
// guid: abec6322-3426-4dde-8a30-3afe453d1650

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// HealthCheckResponse response definition.
message WebHealthCheckResponse {
  // Web server health status.
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Time taken to respond to the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Error details if the server is unhealthy.
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### http_request.proto {#http_request}

**Path**: `gcommon/v1/web/http_request.proto` **Package**: `gcommon.v1.web` **Lines**: 175

**Messages** (1): `HttpRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_request.proto
// version: 1.0.0
// guid: fb9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * HttpRequest represents an HTTP request for processing by web services.
 * Captures all essential HTTP request information including headers,
 * body, and metadata for service mesh and proxy use cases.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HttpRequest {
  // Required fields (1-10)

  /**
   * HTTP method (GET, POST, PUT, DELETE, etc.).
   */
  string method = 1;

  /**
   * Request URL including scheme, host, path, and query parameters.
   * Example: "https://api.example.com/v1/users?limit=10"
   */
  string url = 2;

  /**
   * HTTP protocol version (e.g., "HTTP/1.1", "HTTP/2", "HTTP/3").
   */
  string protocol_version = 3;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * HTTP headers as key-value pairs.
   * Includes standard headers like Content-Type, Authorization, etc.
   */
  map<string, string> headers = 12;

  /**
   * Request body/payload data.
   * Can contain any content type (JSON, XML, binary, etc.).
   */
  google.protobuf.Any body = 13;

  /**
   * Query parameters extracted from the URL.
   * Provided separately for easier access.
   */
  map<string, string> query_params = 14;

  /**
   * Path parameters extracted from the URL pattern.
   * Example: For /users/{user_id}, would contain {"user_id": "123"}
   */
  map<string, string> path_params = 15;

  /**
   * Cookies sent with the request.
   */
  map<string, string> cookies = 16;

  /**
   * Client IP address (original or from proxy headers).
   */
  string client_ip = 17;

  /**
   * User agent string from the client.
   */
  string user_agent = 18;

  /**
   * Referrer URL (if present).
   */
  string referrer = 19;

  /**
   * Content length in bytes.
   */
  int64 content_length = 20;

  /**
   * Content type of the request body.
   */
  string content_type = 21;

  /**
   * Accept header value indicating preferred response types.
   */
  string accept = 22;

  /**
   * Accept-Language header for internationalization.
   */
  string accept_language = 23;

  /**
   * Accept-Encoding header for compression negotiation.
   */
  string accept_encoding = 24;

  /**
   * Authorization header value.
   */
  string authorization = 25;

  /**
   * Request ID for tracking and correlation.
   * May be generated by load balancers or API gateways.
   */
  string request_id = 26;

  /**
   * Session ID if the request is part of a user session.
   */
  string session_id = 27;

  /**
   * Target service name for routing in service mesh.
   */
  string target_service = 28;

  /**
   * Target service version for version-specific routing.
   */
  string target_version = 29;

  /**
   * Request timeout in milliseconds.
   */
  int64 timeout_ms = 30;

  /**
   * Whether the request expects a streaming response.
   */
  bool streaming = 31;

  /**
   * Whether the connection should be kept alive.
   */
  bool keep_alive = 32;

  // Timestamps (51-60)

  /**
   * When the request was received by the first proxy/gateway.
   */
  google.protobuf.Timestamp received_at = 51;

  /**
   * When the request was created/initiated by the client.
   */
  google.protobuf.Timestamp created_at = 52 [ (buf.validate.field).required = true ];
}
```

---

### http_response.proto {#http_response}

**Path**: `gcommon/v1/web/http_response.proto` **Package**: `gcommon.v1.web` **Lines**: 193

**Messages** (1): `HttpResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_response.proto
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * HttpResponse represents an HTTP response from web services.
 * Captures all essential HTTP response information including status,
 * headers, body, and metadata for service mesh and proxy use cases.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message HttpResponse {
  // Required fields (1-10)

  /**
   * HTTP status code (200, 404, 500, etc.).
   */
  int32 status_code = 1;

  /**
   * HTTP status message/reason phrase (OK, Not Found, Internal Server Error, etc.).
   */
  string status_message = 2;

  /**
   * HTTP protocol version used for the response.
   */
  string protocol_version = 3;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * HTTP response headers as key-value pairs.
   * Includes standard headers like Content-Type, Cache-Control, etc.
   */
  map<string, string> headers = 12;

  /**
   * Response body/payload data.
   * Can contain any content type (JSON, XML, HTML, binary, etc.).
   */
  google.protobuf.Any body = 13;

  /**
   * Cookies to be set in the client.
   */
  map<string, string> cookies = 14;

  /**
   * Content length in bytes.
   */
  int64 content_length = 15;

  /**
   * Content type of the response body.
   */
  string content_type = 16;

  /**
   * Content encoding (gzip, deflate, etc.).
   */
  string content_encoding = 17;

  /**
   * Cache-Control header value.
   */
  string cache_control = 18;

  /**
   * ETag header for caching and conditional requests.
   */
  string etag = 19;

  /**
   * Location header for redirects.
   */
  string location = 20;

  /**
   * Server header identifying the server software.
   */
  string server = 21;

  /**
   * CORS Access-Control-Allow-Origin header.
   */
  string access_control_allow_origin = 22;

  /**
   * CORS Access-Control-Allow-Methods header.
   */
  string access_control_allow_methods = 23;

  /**
   * CORS Access-Control-Allow-Headers header.
   */
  string access_control_allow_headers = 24;

  /**
   * Request ID that was processed (for correlation).
   */
  string request_id = 25;

  /**
   * Service name that generated this response.
   */
  string service_name = 26 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * Service version that generated this response.
   */
  string service_version = 27;

  /**
   * Response processing time in milliseconds.
   */
  int64 processing_time_ms = 28;

  /**
   * Whether the response was served from cache.
   */
  bool served_from_cache = 29;

  /**
   * Whether the response is being streamed.
   */
  bool streaming = 30;

  /**
   * Whether the connection will be kept alive.
   */
  bool keep_alive = 31;

  /**
   * Whether the response was compressed.
   */
  bool compressed = 32;

  /**
   * Compression ratio if compressed (0.0-1.0).
   */
  float compression_ratio = 33;

  // Status and error fields (61-70)

  /**
   * Error information if the response represents an error
   * or if there were issues generating the response.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * When response generation started.
   */
  google.protobuf.Timestamp processing_started_at = 51;

  /**
   * When the response was generated.
   */
  google.protobuf.Timestamp generated_at = 52;

  /**
   * When the response was sent to the client.
   */
  google.protobuf.Timestamp sent_at = 53;
}
```

---

### list_cookies_request.proto {#list_cookies_request}

**Path**: `gcommon/v1/web/list_cookies_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListCookiesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_cookies_request.proto
// version: 1.0.0
// guid: b31f8f02-8e3b-4c2c-8094-5e991dabb601

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListCookiesRequest request definition.
message ListCookiesRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_cookies_response.proto {#list_cookies_response}

**Path**: `gcommon/v1/web/list_cookies_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListCookiesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_cookies_response.proto
// version: 1.0.0
// guid: af6c455c-4937-4d9b-a355-2124c8e24b91

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListCookiesResponse response definition.
message ListCookiesResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_files_request.proto {#list_files_request}

**Path**: `gcommon/v1/web/list_files_request.proto` **Package**: `gcommon.v1.web` **Lines**: 46

**Messages** (1): `ListFilesRequest`

**Imports** (4):

- `gcommon/v1/common/file_sort_order.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_files_request.proto
// version: 1.2.0
// guid: 69d44c54-6e03-4313-a56c-2df3041206f8

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/file_sort_order.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Request to list files in a directory.
 * Used for static file serving and directory browsing.
 */
message ListFilesRequest {
  // Directory path to list files from
  string directory_path = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to include subdirectories recursively
  bool recursive = 2;

  // File pattern filter (glob-style)
  string pattern = 3 [(buf.validate.field).string.min_len = 1];

  // Maximum number of files to return
  int32 limit = 4 [(buf.validate.field).int32.gte = 0];

  // Pagination offset
  int32 offset = 5 [(buf.validate.field).int32.gte = 0];

  // Whether to include hidden files (starting with .)
  bool include_hidden = 6;

  // Sort order for the files
  gcommon.v1.common.FileSortOrder sort_order = 7;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 8;
}
```

---

### list_files_response.proto {#list_files_response}

**Path**: `gcommon/v1/web/list_files_response.proto` **Package**: `gcommon.v1.web` **Lines**: 37

**Messages** (1): `ListFilesResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/web/file_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_files_response.proto
// version: 1.1.0
// guid: 0ee5d62d-df69-4b40-a4ea-a36fb6e16147

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/web/file_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Response containing a list of files from a directory or file system.
 * Used for file browsing and management operations.
 */
message ListFilesResponse {
  // List of files and directories
  repeated FileInfo files = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of files (may be larger than returned list if paginated)
  int64 total_count = 2 [(buf.validate.field).int64.gte = 0];

  // Token for next page (if paginated)
  string next_page_token = 3 [(buf.validate.field).string.min_len = 1];

  // Whether there are more results
  bool has_more = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}
```

---

### list_handlers_request.proto {#list_handlers_request}

**Path**: `gcommon/v1/web/list_handlers_request.proto` **Package**: `gcommon.v1.web` **Lines**: 39

**Messages** (1): `ListHandlersRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_handlers_request.proto
// version: 1.1.0
// guid: 5141d082-9a7d-4518-bc9a-3bdf2aca716c

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * Request to list registered HTTP handlers.
 * Used for route discovery and management.
 */
message ListHandlersRequest {
  // Filter by HTTP method (GET, POST, etc.)
  string method_filter = 1 [(buf.validate.field).string.min_len = 1];

  // Filter by path pattern
  string path_filter = 2 [(buf.validate.field).string.min_len = 1];

  // Whether to include middleware information
  bool include_middleware = 3;

  // Maximum number of handlers to return
  int32 limit = 4 [(buf.validate.field).int32.gte = 0];

  // Pagination offset
  int32 offset = 5 [(buf.validate.field).int32.gte = 0];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}
```

---

### list_handlers_response.proto {#list_handlers_response}

**Path**: `gcommon/v1/web/list_handlers_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListHandlersResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_handlers_response.proto
// version: 1.0.0
// guid: 0dafdb52-5ffd-4e3f-a17a-9527935385b0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListHandlersResponse response definition.
message ListHandlersResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_middleware_request.proto {#list_middleware_request}

**Path**: `gcommon/v1/web/list_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 35

**Messages** (1): `ListMiddlewareRequest`

**Imports** (5):

- `gcommon/v1/common/middleware_type.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_middleware_request.proto
// version: 1.1.0
// guid: 0717a6fd-6194-47c2-a17e-4cb18eac5bba

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/middleware_type.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListMiddlewareRequest request definition.
message ListMiddlewareRequest {
  // Server identifier
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Filter by middleware type
  gcommon.v1.common.MiddlewareType type = 2;

  // Filter by enabled state
  bool enabled = 3;

  // Pagination options
  gcommon.v1.common.Pagination pagination = 4;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### list_middleware_response.proto {#list_middleware_response}

**Path**: `gcommon/v1/web/list_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 29

**Messages** (1): `ListMiddlewareResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/web/middleware_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_middleware_response.proto
// version: 1.1.0
// guid: 340d48d9-09d3-4bef-bafb-c16741471339

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/web/middleware_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListMiddlewareResponse response definition.
message ListMiddlewareResponse {
  // Middleware information
  repeated MiddlewareInfo middleware = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination details
  gcommon.v1.common.Pagination pagination = 2;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}
```

---

### list_routes_request.proto {#list_routes_request}

**Path**: `gcommon/v1/web/list_routes_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListRoutesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_routes_request.proto
// version: 1.0.0
// guid: aae7a362-705b-4f59-b285-58b5df10536d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListRoutesRequest request definition.
message ListRoutesRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_routes_response.proto {#list_routes_response}

**Path**: `gcommon/v1/web/list_routes_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListRoutesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_routes_response.proto
// version: 1.0.0
// guid: 47f1c54d-cebd-43eb-a358-7c79ccffcbf3

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListRoutesResponse response definition.
message ListRoutesResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_servers_request.proto {#list_servers_request}

**Path**: `gcommon/v1/web/list_servers_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `ListServersRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_servers_request.proto
// version: 1.0.1
// guid: 1b601e51-740d-448e-b1cf-ca06a0180bee

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
 * ListServersRequest message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListServersRequest {
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

### list_servers_response.proto {#list_servers_response}

**Path**: `gcommon/v1/web/list_servers_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `ListServersResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_servers_response.proto
// version: 1.0.1
// guid: 794ce93d-bcc4-4324-a6d6-867f13442500

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
 * ListServersResponse message for web service operations.
 * Auto-generated placeholder - implement specific fields as needed.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListServersResponse {
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

### list_sessions_request.proto {#list_sessions_request}

**Path**: `gcommon/v1/web/list_sessions_request.proto` **Package**: `gcommon.v1.web` **Lines**: 22

**Messages** (1): `WebListSessionsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_sessions_request.proto
// version: 1.1.0
// guid: a6c1c53c-e5dd-4cbc-9a88-357c8c22e179

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListSessionsRequest request definition.
message WebListSessionsRequest {
  // Filter sessions by user ID (optional)
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### list_sessions_response.proto {#list_sessions_response}

**Path**: `gcommon/v1/web/list_sessions_response.proto` **Package**: `gcommon.v1.web` **Lines**: 21

**Messages** (1): `WebListSessionsResponse`

**Imports** (3):

- `gcommon/v1/web/session_data.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_sessions_response.proto
// version: 1.1.0
// guid: f9b7c78a-576f-4603-9a83-de8d0abb2341

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/session_data.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListSessionsResponse response definition.
message WebListSessionsResponse {
  // List of active sessions
  repeated SessionData sessions = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### list_templates_request.proto {#list_templates_request}

**Path**: `gcommon/v1/web/list_templates_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListTemplatesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_templates_request.proto
// version: 1.0.0
// guid: 17a404df-9dc4-4ee0-b848-9acd1d114fac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListTemplatesRequest request definition.
message ListTemplatesRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_templates_response.proto {#list_templates_response}

**Path**: `gcommon/v1/web/list_templates_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListTemplatesResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_templates_response.proto
// version: 1.0.0
// guid: f71c982a-072a-4971-b28b-8aa39775d4cc

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListTemplatesResponse response definition.
message ListTemplatesResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_websockets_request.proto {#list_websockets_request}

**Path**: `gcommon/v1/web/list_websockets_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListWebsocketsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_websockets_request.proto
// version: 1.0.0
// guid: 4e624d8b-c0a8-4db1-a31a-1b7edabb3b76

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListWebsocketsRequest request definition.
message ListWebsocketsRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_websockets_response.proto {#list_websockets_response}

**Path**: `gcommon/v1/web/list_websockets_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListWebsocketsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/list_websockets_response.proto
// version: 1.0.0
// guid: 1dd3b983-0837-4026-bca1-57e896d2d1fb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// ListWebsocketsResponse response definition.
message ListWebsocketsResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_handler_request.proto {#register_handler_request}

**Path**: `gcommon/v1/web/register_handler_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterHandlerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_handler_request.proto
// version: 1.0.0
// guid: 808ab079-268c-49db-be80-37f91f8c9f7e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterHandlerRequest request definition.
message RegisterHandlerRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_handler_response.proto {#register_handler_response}

**Path**: `gcommon/v1/web/register_handler_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterHandlerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_handler_response.proto
// version: 1.0.0
// guid: a59897f6-9cf0-48f8-8117-621aea3b60e0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterHandlerResponse response definition.
message RegisterHandlerResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_middleware_request.proto {#register_middleware_request}

**Path**: `gcommon/v1/web/register_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Messages** (1): `RegisterMiddlewareRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/web/middleware_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_middleware_request.proto
// version: 1.1.0
// guid: c136f229-3eee-476f-87b9-6417ec8bb8b0
// RegisterMiddlewareRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/web/middleware_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

message RegisterMiddlewareRequest {
  // Target server identifier
  string server_id = 1 [(buf.validate.field).string.min_len = 1];

  // Middleware configuration
  MiddlewareConfig middleware = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### register_middleware_response.proto {#register_middleware_response}

**Path**: `gcommon/v1/web/register_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 26

**Messages** (1): `RegisterMiddlewareResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/web/middleware_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_middleware_response.proto
// version: 1.1.1
// guid: 759e7f49-492f-4cf6-ae71-bfcc4f96aa83

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/web/middleware_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterMiddlewareResponse response definition.
message RegisterMiddlewareResponse {
  // Operation success flag
  bool success = 1;

  // Details about the registered middleware
  MiddlewareInfo middleware = 2;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}
```

---

### register_route_request.proto {#register_route_request}

**Path**: `gcommon/v1/web/register_route_request.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterRouteRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_route_request.proto
// version: 1.0.0
// guid: 0c8be2b5-29b4-4207-a6a3-91d9c03312fe

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterRouteRequest request definition.
message RegisterRouteRequest {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### register_route_response.proto {#register_route_response}

**Path**: `gcommon/v1/web/register_route_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `RegisterRouteResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/register_route_response.proto
// version: 1.0.0
// guid: d4348084-2633-450e-b54d-876af3f04908

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// RegisterRouteResponse response definition.
message RegisterRouteResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### remove_middleware_request.proto {#remove_middleware_request}

**Path**: `gcommon/v1/web/remove_middleware_request.proto` **Package**: `gcommon.v1.web` **Lines**: 42

**Messages** (1): `RemoveMiddlewareRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/remove_middleware_request.proto
// version: 1.0.1
// guid: 8a7398c4-58cc-47b4-a4db-e53da72f74d5

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

**Path**: `gcommon/v1/web/remove_middleware_response.proto` **Package**: `gcommon.v1.web` **Lines**: 56

**Messages** (1): `RemoveMiddlewareResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/remove_middleware_response.proto
// version: 1.0.1
// guid: 6b5a3ac2-61d8-478d-874b-c0fcbb4eceed

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

