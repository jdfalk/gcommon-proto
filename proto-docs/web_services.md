# Web Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 2
- **Services**: 2

## Table of Contents

### Services

- [`WebAdminService`](#web_admin_service) - from web_admin_service.proto
- [`WebService`](#web_service) - from web_service.proto

### Files in this Module

- [web_admin_service.proto](#web_admin_service)
- [web_service.proto](#web_service)

---


## Services Documentation

### web_admin_service.proto {#web_admin_service}

**Path**: `gcommon/v1/web/web_admin_service.proto` **Package**: `gcommon.v1.web` **Lines**: 36

**Services** (1): `WebAdminService`

**Imports** (7):

- `gcommon/v1/web/flush_cache_request.proto`
- `gcommon/v1/web/flush_cache_response.proto`
- `gcommon/v1/web/get_cache_config_request.proto`
- `gcommon/v1/web/get_cache_config_response.proto`
- `gcommon/v1/web/update_cache_config_request.proto`
- `gcommon/v1/web/update_cache_config_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/web_admin_service.proto
// version: 1.0.1
// guid: 1419b30a-cf4d-4cd5-80ab-8bdd18381d02
// file: proto/gcommon/v1/web/web_admin_service.proto
//
// Administrative service for managing web server cache settings.
//
edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/flush_cache_request.proto";
import "gcommon/v1/web/flush_cache_response.proto";
import "gcommon/v1/web/get_cache_config_request.proto";
import "gcommon/v1/web/get_cache_config_response.proto";
import "gcommon/v1/web/update_cache_config_request.proto";
import "gcommon/v1/web/update_cache_config_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

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

**Path**: `gcommon/v1/web/web_service.proto` **Package**: `gcommon.v1.web` **Lines**: 28

**Services** (1): `WebService`

**Imports** (5):

- `gcommon/v1/web/handle_request_request.proto`
- `gcommon/v1/web/handle_request_response.proto`
- `gcommon/v1/web/health_check_request.proto`
- `gcommon/v1/web/health_check_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/web_service.proto
// version: 1.0.1
// guid: 5f6e7d8c-9b0a-1423-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.web;

import "gcommon/v1/web/handle_request_request.proto";
import "gcommon/v1/web/handle_request_response.proto";
import "gcommon/v1/web/health_check_request.proto";
import "gcommon/v1/web/health_check_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

/**
 * WebService provides core web server operations for
 * handling HTTP requests and managing web services.
 */
service WebService {
  // Handle an incoming web request
  rpc HandleRequest(HandleRequestRequest) returns (HandleRequestResponse);

  // Check health of web service
  rpc HealthCheck(WebHealthCheckRequest) returns (WebHealthCheckResponse);
}
```

---

