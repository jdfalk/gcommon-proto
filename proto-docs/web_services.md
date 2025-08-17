# web_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 2
- **Messages**: 0
- **Services**: 2
- **Enums**: 0

## Files in this Module

- [web_admin_service.proto](#web_admin_service)
- [web_service.proto](#web_service)

## Module Dependencies

**This module depends on**:

- [web_api_1](./web_api_1.md)
- [web_config_1](./web_config_1.md)

---

## Detailed Documentation

### web_admin_service.proto {#web_admin_service}

**Path**: `pkg/web/proto/web_admin_service.proto` **Package**: `gcommon.v1.web` **Lines**: 35

**Services** (1): `WebAdminService`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `pkg/web/proto/flush_cache_request.proto` → [web_api_1](./web_api_1.md#flush_cache_request)
- `pkg/web/proto/flush_cache_response.proto` → [web_api_1](./web_api_1.md#flush_cache_response)
- `pkg/web/proto/get_cache_config_request.proto` → [web_config_1](./web_config_1.md#get_cache_config_request)
- `pkg/web/proto/get_cache_config_response.proto` → [web_config_1](./web_config_1.md#get_cache_config_response)
- `pkg/web/proto/update_cache_config_request.proto` → [web_config_1](./web_config_1.md#update_cache_config_request)
- `pkg/web/proto/update_cache_config_response.proto` → [web_config_1](./web_config_1.md#update_cache_config_response)

#### Source Code

```protobuf
// file: pkg/web/proto/services/web_admin_service.proto
// file: pkg/web/proto/services/web_admin_service.proto
//
// Administrative service for managing web server cache settings.
//
edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "pkg/web/proto/flush_cache_request.proto";
import "pkg/web/proto/flush_cache_response.proto";
import "pkg/web/proto/get_cache_config_request.proto";
import "pkg/web/proto/get_cache_config_response.proto";
import "pkg/web/proto/update_cache_config_request.proto";
import "pkg/web/proto/update_cache_config_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

/**
 * WebAdminService provides cache administration endpoints
 * for web server management tools.
 */
service WebAdminService {
  // Retrieve current cache configuration
  rpc GetCacheConfig(GetCacheConfigRequest) returns (GetCacheConfigResponse);

  // Update cache configuration
  rpc UpdateCacheConfig(UpdateCacheConfigRequest) returns (UpdateCacheConfigResponse);

  // Flush all cached entries
  rpc FlushCache(FlushCacheRequest) returns (FlushCacheResponse);
}

```

---

### web_service.proto {#web_service}

**Path**: `pkg/web/proto/web_service.proto` **Package**: `gcommon.v1.web` **Lines**: 33

**Services** (1): `HTTPGatewayService`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/web/proto/services/web_service.proto
// version: 1.0.0
// guid: 7c9e0f1a-6d8b-5f4e-0a9f-8e7d6c5b4a3f

// WebService definition
//
// This file implements the 1-1-1 pattern for service definitions.
// NOTE: The main WebService is defined in pkg/web/proto/web.proto
// This file is reserved for future additional web services or service extensions.

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/web/proto";

// Future web service extensions can be defined here
// The main WebService is defined in web.proto to avoid duplication

// Example additional service for HTTP handling:
/*
   service HTTPGatewayService {
     // Handle HTTP request
     rpc HandleRequest(HTTPRequest) returns (HTTPResponse);

     // Process REST API calls
     rpc ProcessRESTCall(RESTRequest) returns (RESTResponse);
   }
*/

```

---
