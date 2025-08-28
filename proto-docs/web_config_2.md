# web_config_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 2
- **Messages**: 2
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [update_server_config_response.proto](#update_server_config_response)
- [websocket_config.proto](#websocket_config)
---


## Detailed Documentation

### update_server_config_response.proto {#update_server_config_response}

**Path**: `gcommon/v1/web/update_server_config_response.proto` **Package**: `gcommon.v1.web` **Lines**: 19

**Messages** (1): `UpdateServerConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/update_server_config_response.proto
// version: 1.0.0
// guid: db0184f3-c771-45f7-946e-aaadcf2ba967

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// UpdateServerConfigResponse response definition.
message UpdateServerConfigResponse {
  string placeholder = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### websocket_config.proto {#websocket_config}

**Path**: `gcommon/v1/web/websocket_config.proto` **Package**: `gcommon.v1.web` **Lines**: 32

**Messages** (1): `WebsocketConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/websocket_config.proto
// version: 1.1.0
// guid: b746de14-1e1e-4faf-812f-0bf9fa38c201

edition = "2023";

package gcommon.v1.web;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/web";

// WebsocketConfig message definition.
message WebsocketConfig {
  // Endpoint path for websocket connections
  string endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Allowed origin hosts
  repeated string allowed_origins = 2 [(buf.validate.field).repeated.min_items = 1];

  // Enable per-message compression
  bool enable_compression = 3;

  // Read buffer size in bytes
  int32 read_buffer_size = 4 [(buf.validate.field).int32.gte = 0];

  // Write buffer size in bytes
  int32 write_buffer_size = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

