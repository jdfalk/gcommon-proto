# web_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 50
- **Messages**: 50
- **Services**: 0
- **Enums**: 0
- ⚠️ **Issues**: 33

## Files in this Module

- [get_server_health_request.proto](#get_server_health_request) ⚠️ 1 issues
- [get_server_health_response.proto](#get_server_health_response) ⚠️ 1 issues
- [get_server_logs_request.proto](#get_server_logs_request) ⚠️ 1 issues
- [get_server_logs_response.proto](#get_server_logs_response) ⚠️ 1 issues
- [get_server_metrics_request.proto](#get_server_metrics_request) ⚠️ 1 issues
- [get_server_metrics_response.proto](#get_server_metrics_response) ⚠️ 1 issues
- [get_server_status_request.proto](#get_server_status_request) ⚠️ 1 issues
- [get_server_status_response.proto](#get_server_status_response) ⚠️ 1 issues
- [get_session_request.proto](#get_session_request)
- [get_session_response.proto](#get_session_response)
- [get_ssl_certificate_info_request.proto](#get_ssl_certificate_info_request) ⚠️
  1 issues
- [get_ssl_certificate_info_response.proto](#get_ssl_certificate_info_response)
  ⚠️ 1 issues
- [get_template_info_request.proto](#get_template_info_request) ⚠️ 1 issues
- [get_template_info_response.proto](#get_template_info_response) ⚠️ 1 issues
- [get_websocket_info_request.proto](#get_websocket_info_request) ⚠️ 1 issues
- [get_websocket_info_response.proto](#get_websocket_info_response) ⚠️ 1 issues
- [handle_request.proto](#handle_request) ⚠️ 1 issues
- [handle_request_request.proto](#handle_request_request) ⚠️ 1 issues
- [handle_request_response.proto](#handle_request_response) ⚠️ 1 issues
- [handle_response.proto](#handle_response) ⚠️ 1 issues
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [http_request.proto](#http_request)
- [http_request_per.proto](#http_request_per)
- [http_response.proto](#http_response)
- [http_response_per.proto](#http_response_per)
- [list_cookies_request.proto](#list_cookies_request) ⚠️ 1 issues
- [list_cookies_response.proto](#list_cookies_response) ⚠️ 1 issues
- [list_files_request.proto](#list_files_request)
- [list_files_response.proto](#list_files_response)
- [list_handlers_request.proto](#list_handlers_request)
- [list_handlers_response.proto](#list_handlers_response) ⚠️ 1 issues
- [list_middleware_request.proto](#list_middleware_request)
- [list_middleware_response.proto](#list_middleware_response)
- [list_routes_request.proto](#list_routes_request) ⚠️ 1 issues
- [list_routes_response.proto](#list_routes_response) ⚠️ 1 issues
- [list_servers_request.proto](#list_servers_request) ⚠️ 1 issues
- [list_servers_response.proto](#list_servers_response) ⚠️ 1 issues
- [list_sessions_request.proto](#list_sessions_request)
- [list_sessions_response.proto](#list_sessions_response)
- [list_templates_request.proto](#list_templates_request) ⚠️ 1 issues
- [list_templates_response.proto](#list_templates_response) ⚠️ 1 issues
- [list_websockets_request.proto](#list_websockets_request) ⚠️ 1 issues
- [list_websockets_response.proto](#list_websockets_response) ⚠️ 1 issues
- [register_handler_request.proto](#register_handler_request) ⚠️ 1 issues
- [register_handler_response.proto](#register_handler_response) ⚠️ 1 issues
- [register_middleware_request.proto](#register_middleware_request)
- [register_middleware_response.proto](#register_middleware_response)
- [register_route_request.proto](#register_route_request) ⚠️ 1 issues
- [register_route_response.proto](#register_route_response) ⚠️ 1 issues

## Module Dependencies

**This module depends on**:

- [common](./common.md)
- [metrics_1](./metrics_1.md)
- [queue_1](./queue_1.md)
- [web](./web.md)
- [web_config_1](./web_config_1.md)

**Modules that depend on this one**:

- [auth_services](./auth_services.md)
- [config_services](./config_services.md)
- [database_services](./database_services.md)
- [health](./health.md)

---

## Detailed Documentation

### get_server_health_request.proto {#get_server_health_request}

**Path**: `pkg/web/proto/get_server_health_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerHealthRequest`

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
// file: pkg/web/proto/requests/get_server_health_request.proto
// version: 1.0.0
// guid: 150fcfd0-33d0-453e-a628-70235d0d760d

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

**Path**: `pkg/web/proto/get_server_health_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerHealthResponse`

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
// file: pkg/web/proto/responses/get_server_health_response.proto
// version: 1.0.0
// guid: 3b792629-d4ac-4821-8ab0-badba4ad3aea

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

**Path**: `pkg/web/proto/get_server_logs_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerLogsRequest`

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
// file: pkg/web/proto/requests/get_server_logs_request.proto
// version: 1.0.0
// guid: 8e8d56e9-af3b-4205-bab3-d528f6528104

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

**Path**: `pkg/web/proto/get_server_logs_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerLogsResponse`

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
// file: pkg/web/proto/responses/get_server_logs_response.proto
// version: 1.0.0
// guid: 2bece2cb-e346-41b9-8e2b-2bdbbbe4c94f

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

**Path**: `pkg/web/proto/get_server_metrics_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetServerMetricsRequest`

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
// file: pkg/web/proto/requests/get_server_metrics_request.proto
// version: 1.0.0
// guid: 3f87be3d-9370-43a0-88fc-13d5eb9eb37a

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

**Path**: `pkg/web/proto/get_server_metrics_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetServerMetricsResponse`

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
// file: pkg/web/proto/responses/get_server_metrics_response.proto
// version: 1.0.0
// guid: c7d26642-5c77-4ba5-b891-5876066cfaba

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

**Path**: `pkg/web/proto/get_server_status_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetServerStatusRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_server_status_request.proto
// version: 1.0.0
// guid: 589c81b7-a311-4da5-9604-ece349fc6e55

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetServerStatusRequest request definition.
message GetServerStatusRequest {
  string placeholder = 1;
}

```

---

### get_server_status_response.proto {#get_server_status_response}

**Path**: `pkg/web/proto/get_server_status_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetServerStatusResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_server_status_response.proto
// version: 1.0.0
// guid: 3cb9f0ee-d816-469a-89f1-0486c03c9f3a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetServerStatusResponse response definition.
message GetServerStatusResponse {
  string placeholder = 1;
}

```

---

### get_session_request.proto {#get_session_request}

**Path**: `pkg/web/proto/get_session_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 19

**Messages** (1): `GetSessionRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_session_request.proto
// version: 1.1.0
// guid: 5ab16058-a2a8-463c-b101-b1f24df275ef

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetSessionRequest request definition.
message GetSessionRequest {
  // Identifier of the session to retrieve
  string session_id = 1;
}

```

---

### get_session_response.proto {#get_session_response}

**Path**: `pkg/web/proto/get_session_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 20

**Messages** (1): `GetSessionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/session_data.proto` → [web](./web.md#session_data)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_session_response.proto
// version: 1.1.0
// guid: 97fcede8-5243-4901-b423-41a0723fb0c7

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/session_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetSessionResponse response definition.
message GetSessionResponse {
  // Retrieved session data
  SessionData session = 1;
}

```

---

### get_ssl_certificate_info_request.proto {#get_ssl_certificate_info_request}

**Path**: `pkg/web/proto/get_ssl_certificate_info_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `GetSSLCertificateInfoRequest`

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
// file: pkg/web/proto/requests/get_s_s_l_certificate_info_request.proto
// version: 1.0.0
// guid: dc573011-0a3c-48ac-9de4-3a7718171101

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

**Path**: `pkg/web/proto/get_ssl_certificate_info_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `GetSSLCertificateInfoResponse`

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
// file: pkg/web/proto/responses/get_s_s_l_certificate_info_response.proto
// version: 1.0.0
// guid: 9ffed0bc-f94b-47a9-8a07-7e01d998e746

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

**Path**: `pkg/web/proto/get_template_info_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetTemplateInfoRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_template_info_request.proto
// version: 1.0.0
// guid: 0660a509-2a17-4efb-be93-9712e8b2c84e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetTemplateInfoRequest request definition.
message GetTemplateInfoRequest {
  string placeholder = 1;
}

```

---

### get_template_info_response.proto {#get_template_info_response}

**Path**: `pkg/web/proto/get_template_info_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetTemplateInfoResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_template_info_response.proto
// version: 1.0.0
// guid: e1cc4547-9204-48a5-84a3-3c7526d71494

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetTemplateInfoResponse response definition.
message GetTemplateInfoResponse {
  string placeholder = 1;
}

```

---

### get_websocket_info_request.proto {#get_websocket_info_request}

**Path**: `pkg/web/proto/get_websocket_info_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetWebsocketInfoRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/get_websocket_info_request.proto
// version: 1.0.0
// guid: 48f87988-451a-453b-9f51-2c7175112c25

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetWebsocketInfoRequest request definition.
message GetWebsocketInfoRequest {
  string placeholder = 1;
}

```

---

### get_websocket_info_response.proto {#get_websocket_info_response}

**Path**: `pkg/web/proto/get_websocket_info_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `GetWebsocketInfoResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/get_websocket_info_response.proto
// version: 1.0.0
// guid: 147168a6-ba00-4881-8ddd-dd52c3af7198

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// GetWebsocketInfoResponse response definition.
message GetWebsocketInfoResponse {
  string placeholder = 1;
}

```

---

### handle_request.proto {#handle_request}

**Path**: `pkg/web/proto/handle_request.proto` **Package**: `gcommon.v1.web`
**Lines**: 18

**Messages** (1): `HandleRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/handle_request.proto
// version: 1.0.0
// guid: 50315b83-99de-4058-b883-61ebfa2b47a8

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HandleRequest request definition.
message HandleRequest {
  string placeholder = 1;
}

```

---

### handle_request_request.proto {#handle_request_request}

**Path**: `pkg/web/proto/handle_request_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `HandleRequestRequest`

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
// file: pkg/web/proto/requests/handle_request_request.proto
// version: 1.0.0
// guid: 0af45f43-528e-4f14-a668-eebf5ae2d975

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

**Path**: `pkg/web/proto/handle_request_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `HandleRequestResponse`

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
// file: pkg/web/proto/responses/handle_request_response.proto
// version: 1.0.0
// guid: c75ed356-c467-40db-ac2c-529e7b956802

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

**Path**: `pkg/web/proto/handle_response.proto` **Package**: `gcommon.v1.web`
**Lines**: 18

**Messages** (1): `HandleResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/handle_response.proto
// version: 1.0.0
// guid: 54494647-eae8-4100-9c64-809b55fe043a

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HandleResponse response definition.
message HandleResponse {
  string placeholder = 1;
}

```

---

### health_check_request.proto {#health_check_request}

**Path**: `pkg/web/proto/health_check_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 20

**Messages** (1): `HealthCheckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/health_check_request.proto
// version: 1.0.0
// guid: 08748b61-ccf0-4bfe-bfc6-ad2778f3959c
// HealthCheckRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message HealthCheckRequest {
  // Request metadata for the HTTP server.
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}

```

---

### health_check_response.proto {#health_check_response}

**Path**: `pkg/web/proto/health_check_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 28

**Messages** (1): `HealthCheckResponse`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/health_status.proto` → [common](./common.md#health_status) →
  [metrics_1](./metrics_1.md#health_status) →
  [queue_1](./queue_1.md#health_status) → [web](./web.md#health_status)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/health_check_response.proto
// version: 1.0.0
// guid: abec6322-3426-4dde-8a30-3afe453d1650

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/health_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HealthCheckResponse response definition.
message HealthCheckResponse {
  // Web server health status.
  gcommon.v1.common.HealthStatus status = 1;

  // Time taken to respond to the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Error details if the server is unhealthy.
  gcommon.v1.common.Error error = 3 [lazy = true];
}

```

---

### http_request.proto {#http_request}

**Path**: `pkg/web/proto/http_request.proto` **Package**: `gcommon.v1.web`
**Lines**: 49

**Messages** (1): `HTTPRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/http_request.proto
// version: 1.0.1
// guid: 01f1be0e-353e-4d6b-9cbc-d47f6c09fd89

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HttpRequest message definition.
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

```

---

### http_request_per.proto {#http_request_per}

**Path**: `pkg/web/proto/http_request_per.proto` **Package**: `gcommon.v1.web`
**Lines**: 175

**Messages** (1): `HttpRequest`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/http_request_per.proto
// version: 1.0.0
// guid: fb9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

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
  google.protobuf.Timestamp created_at = 52;
}

```

---

### http_response.proto {#http_response}

**Path**: `pkg/web/proto/http_response.proto` **Package**: `gcommon.v1.web`
**Lines**: 34

**Messages** (1): `HTTPResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/messages/http_response.proto
// version: 1.0.1
// guid: e9b0fcee-3b0a-4b04-b8f5-68aa199c7d6f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// HttpResponse message definition.
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

```

---

### http_response_per.proto {#http_response_per}

**Path**: `pkg/web/proto/http_response_per.proto` **Package**: `gcommon.v1.web`
**Lines**: 190

**Messages** (1): `HttpResponse`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/http_response_per.proto
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
// Standard imports
import "google/protobuf/timestamp.proto";
// Common types
import "pkg/common/proto/error.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

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
  string service_name = 26;

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

**Path**: `pkg/web/proto/list_cookies_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListCookiesRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/list_cookies_request.proto
// version: 1.0.0
// guid: b31f8f02-8e3b-4c2c-8094-5e991dabb601

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListCookiesRequest request definition.
message ListCookiesRequest {
  string placeholder = 1;
}

```

---

### list_cookies_response.proto {#list_cookies_response}

**Path**: `pkg/web/proto/list_cookies_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListCookiesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_cookies_response.proto
// version: 1.0.0
// guid: af6c455c-4937-4d9b-a355-2124c8e24b91

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListCookiesResponse response definition.
message ListCookiesResponse {
  string placeholder = 1;
}

```

---

### list_files_request.proto {#list_files_request}

**Path**: `pkg/web/proto/list_files_request.proto` **Package**: `gcommon.v1.web`
**Lines**: 45

**Messages** (1): `ListFilesRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/web/proto/file_sort_order.proto` → [web](./web.md#file_sort_order)

#### Source Code

```protobuf
// file: pkg/web/proto/list_files_request.proto
// version: 1.2.0
// guid: 69d44c54-6e03-4313-a56c-2df3041206f8

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/web/proto/file_sort_order.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * Request to list files in a directory.
 * Used for static file serving and directory browsing.
 */
message ListFilesRequest {
  // Directory path to list files from
  string directory_path = 1;

  // Whether to include subdirectories recursively
  bool recursive = 2;

  // File pattern filter (glob-style)
  string pattern = 3;

  // Maximum number of files to return
  int32 limit = 4;

  // Pagination offset
  int32 offset = 5;

  // Whether to include hidden files (starting with .)
  bool include_hidden = 6;

  // Sort order for the files
  FileSortOrder sort_order = 7;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 8;
}

```

---

### list_files_response.proto {#list_files_response}

**Path**: `pkg/web/proto/list_files_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 36

**Messages** (1): `ListFilesResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` →
  [common](./common.md#response_metadata)
- `pkg/web/proto/file_info.proto` → [web](./web.md#file_info)

#### Source Code

```protobuf
// file: pkg/web/proto/list_files_response.proto
// version: 1.1.0
// guid: 0ee5d62d-df69-4b40-a4ea-a36fb6e16147

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";
import "pkg/web/proto/file_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * Response containing a list of files from a directory or file system.
 * Used for file browsing and management operations.
 */
message ListFilesResponse {
  // List of files and directories
  repeated gcommon.v1.web.FileInfo files = 1;

  // Total number of files (may be larger than returned list if paginated)
  int64 total_count = 2;

  // Token for next page (if paginated)
  string next_page_token = 3;

  // Whether there are more results
  bool has_more = 4;

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}

```

---

### list_handlers_request.proto {#list_handlers_request}

**Path**: `pkg/web/proto/list_handlers_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 38

**Messages** (1): `ListHandlersRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/web/proto/list_handlers_request.proto
// version: 1.1.0
// guid: 5141d082-9a7d-4518-bc9a-3bdf2aca716c

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * Request to list registered HTTP handlers.
 * Used for route discovery and management.
 */
message ListHandlersRequest {
  // Filter by HTTP method (GET, POST, etc.)
  string method_filter = 1;

  // Filter by path pattern
  string path_filter = 2;

  // Whether to include middleware information
  bool include_middleware = 3;

  // Maximum number of handlers to return
  int32 limit = 4;

  // Pagination offset
  int32 offset = 5;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}

```

---

### list_handlers_response.proto {#list_handlers_response}

**Path**: `pkg/web/proto/list_handlers_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListHandlersResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_handlers_response.proto
// version: 1.0.0
// guid: 0dafdb52-5ffd-4e3f-a17a-9527935385b0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListHandlersResponse response definition.
message ListHandlersResponse {
  string placeholder = 1;
}

```

---

### list_middleware_request.proto {#list_middleware_request}

**Path**: `pkg/web/proto/list_middleware_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 34

**Messages** (1): `ListMiddlewareRequest`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/web/proto/middleware_type.proto` → [web](./web.md#middleware_type)

#### Source Code

```protobuf
// file: pkg/web/proto/list_middleware_request.proto
// version: 1.1.0
// guid: 0717a6fd-6194-47c2-a17e-4cb18eac5bba

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/web/proto/middleware_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListMiddlewareRequest request definition.
message ListMiddlewareRequest {
  // Server identifier
  string server_id = 1;

  // Filter by middleware type
  MiddlewareType type = 2;

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

**Path**: `pkg/web/proto/list_middleware_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 28

**Messages** (1): `ListMiddlewareResponse`

**Imports** (4):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)
- `pkg/web/proto/middleware_info.proto` → [web](./web.md#middleware_info)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_middleware_response.proto
// version: 1.1.0
// guid: 340d48d9-09d3-4bef-bafb-c16741471339

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/common/proto/pagination.proto";
import "pkg/web/proto/middleware_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListMiddlewareResponse response definition.
message ListMiddlewareResponse {
  // Middleware information
  repeated MiddlewareInfo middleware = 1;

  // Pagination details
  gcommon.v1.common.Pagination pagination = 2;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 3;
}

```

---

### list_routes_request.proto {#list_routes_request}

**Path**: `pkg/web/proto/list_routes_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListRoutesRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/list_routes_request.proto
// version: 1.0.0
// guid: aae7a362-705b-4f59-b285-58b5df10536d

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListRoutesRequest request definition.
message ListRoutesRequest {
  string placeholder = 1;
}

```

---

### list_routes_response.proto {#list_routes_response}

**Path**: `pkg/web/proto/list_routes_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListRoutesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_routes_response.proto
// version: 1.0.0
// guid: 47f1c54d-cebd-43eb-a358-7c79ccffcbf3

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListRoutesResponse response definition.
message ListRoutesResponse {
  string placeholder = 1;
}

```

---

### list_servers_request.proto {#list_servers_request}

**Path**: `pkg/web/proto/list_servers_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 42

**Messages** (1): `ListServersRequest`

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
// file: pkg/web/proto/requests/list_servers_request.proto
// version: 1.0.0
// guid: 1b601e51-740d-448e-b1cf-ca06a0180bee

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

**Path**: `pkg/web/proto/list_servers_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 56

**Messages** (1): `ListServersResponse`

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
// file: pkg/web/proto/responses/list_servers_response.proto
// version: 1.0.0
// guid: 794ce93d-bcc4-4324-a6d6-867f13442500

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

**Path**: `pkg/web/proto/list_sessions_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 19

**Messages** (1): `ListSessionsRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/requests/list_sessions_request.proto
// version: 1.1.0
// guid: a6c1c53c-e5dd-4cbc-9a88-357c8c22e179

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListSessionsRequest request definition.
message ListSessionsRequest {
  // Filter sessions by user ID (optional)
  string user_id = 1;
}

```

---

### list_sessions_response.proto {#list_sessions_response}

**Path**: `pkg/web/proto/list_sessions_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 20

**Messages** (1): `ListSessionsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/session_data.proto` → [web](./web.md#session_data)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_sessions_response.proto
// version: 1.1.0
// guid: f9b7c78a-576f-4603-9a83-de8d0abb2341

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/session_data.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListSessionsResponse response definition.
message ListSessionsResponse {
  // List of active sessions
  repeated SessionData sessions = 1;
}

```

---

### list_templates_request.proto {#list_templates_request}

**Path**: `pkg/web/proto/list_templates_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListTemplatesRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/list_templates_request.proto
// version: 1.0.0
// guid: 17a404df-9dc4-4ee0-b848-9acd1d114fac

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListTemplatesRequest request definition.
message ListTemplatesRequest {
  string placeholder = 1;
}

```

---

### list_templates_response.proto {#list_templates_response}

**Path**: `pkg/web/proto/list_templates_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListTemplatesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_templates_response.proto
// version: 1.0.0
// guid: f71c982a-072a-4971-b28b-8aa39775d4cc

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListTemplatesResponse response definition.
message ListTemplatesResponse {
  string placeholder = 1;
}

```

---

### list_websockets_request.proto {#list_websockets_request}

**Path**: `pkg/web/proto/list_websockets_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListWebsocketsRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/list_websockets_request.proto
// version: 1.0.0
// guid: 4e624d8b-c0a8-4db1-a31a-1b7edabb3b76

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListWebsocketsRequest request definition.
message ListWebsocketsRequest {
  string placeholder = 1;
}

```

---

### list_websockets_response.proto {#list_websockets_response}

**Path**: `pkg/web/proto/list_websockets_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `ListWebsocketsResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/list_websockets_response.proto
// version: 1.0.0
// guid: 1dd3b983-0837-4026-bca1-57e896d2d1fb

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// ListWebsocketsResponse response definition.
message ListWebsocketsResponse {
  string placeholder = 1;
}

```

---

### register_handler_request.proto {#register_handler_request}

**Path**: `pkg/web/proto/register_handler_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RegisterHandlerRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/register_handler_request.proto
// version: 1.0.0
// guid: 808ab079-268c-49db-be80-37f91f8c9f7e

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RegisterHandlerRequest request definition.
message RegisterHandlerRequest {
  string placeholder = 1;
}

```

---

### register_handler_response.proto {#register_handler_response}

**Path**: `pkg/web/proto/register_handler_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RegisterHandlerResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/register_handler_response.proto
// version: 1.0.0
// guid: a59897f6-9cf0-48f8-8117-621aea3b60e0

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RegisterHandlerResponse response definition.
message RegisterHandlerResponse {
  string placeholder = 1;
}

```

---

### register_middleware_request.proto {#register_middleware_request}

**Path**: `pkg/web/proto/register_middleware_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 27

**Messages** (1): `RegisterMiddlewareRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` →
  [common](./common.md#request_metadata)
- `pkg/web/proto/middleware_config.proto` →
  [web_config_1](./web_config_1.md#middleware_config)

#### Source Code

```protobuf
// file: pkg/web/proto/requests/register_middleware_request.proto
// version: 1.1.0
// guid: c136f229-3eee-476f-87b9-6417ec8bb8b0
// RegisterMiddlewareRequest request definition.

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/web/proto/middleware_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

message RegisterMiddlewareRequest {
  // Target server identifier
  string server_id = 1;

  // Middleware configuration
  MiddlewareConfig middleware = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3;
}

```

---

### register_middleware_response.proto {#register_middleware_response}

**Path**: `pkg/web/proto/register_middleware_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 27

**Messages** (1): `RegisterMiddlewareResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/error.proto` → [common](./common.md#error)
- `pkg/web/proto/middleware_info.proto` → [web](./web.md#middleware_info)

#### Source Code

```protobuf
// file: pkg/web/proto/responses/register_middleware_response.proto
// version: 1.1.0
// guid: 759e7f49-492f-4cf6-ae71-bfcc4f96aa83

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/error.proto";
import "pkg/web/proto/middleware_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

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

**Path**: `pkg/web/proto/register_route_request.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RegisterRouteRequest`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/requests/register_route_request.proto
// version: 1.0.0
// guid: 0c8be2b5-29b4-4207-a6a3-91d9c03312fe

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RegisterRouteRequest request definition.
message RegisterRouteRequest {
  string placeholder = 1;
}

```

---

### register_route_response.proto {#register_route_response}

**Path**: `pkg/web/proto/register_route_response.proto` **Package**:
`gcommon.v1.web` **Lines**: 18

**Messages** (1): `RegisterRouteResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### ⚠️ Issues Found (1)

- Line 16: Implementation needed - string placeholder = 1;

#### Source Code

```protobuf
// file: pkg/web/proto/responses/register_route_response.proto
// version: 1.0.0
// guid: d4348084-2633-450e-b54d-876af3f04908

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// RegisterRouteResponse response definition.
message RegisterRouteResponse {
  string placeholder = 1;
}

```

---
