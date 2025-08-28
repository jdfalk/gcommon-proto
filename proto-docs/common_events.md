# common_events Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 2
- **Messages**: 2
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [audit_event.proto](#audit_event)
- [event_notification.proto](#event_notification)
---


## Detailed Documentation

### audit_event.proto {#audit_event}

**Path**: `gcommon/v1/common/audit_event.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `AuditEvent`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_event.proto
// version: 1.0.0
// guid: 07442bc2-38fe-42b3-aecd-0ffda724fa86

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuditEvent records authentication-related actions for auditing.
 */
message AuditEvent {
  // Type of event (e.g., LOGIN, LOGOUT)
  string event_type = 1;

  // User ID associated with the event
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Time event occurred
  google.protobuf.Timestamp timestamp = 3 [lazy = true];

  // Additional metadata about the event
  map<string, string> metadata = 4;
}
```

---

### event_notification.proto {#event_notification}

**Path**: `gcommon/v1/common/event_notification.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `EventNotification`

**Imports** (5):

- `gcommon/v1/common/notification_message.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/event_notification.proto
// version: 1.2.0
// guid: d1e2f3g4-h5i6-7890-j1k2-l3m4n5o6p7q8

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/notification_message.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Notification generated from an event.
 */
message EventNotification {
  // Associated event identifier
  string event_id = 1 [(buf.validate.field).string.min_len = 1];

  // Event type or name
  string event_type = 2 [(buf.validate.field).string.min_len = 1];

  // Event payload data
  google.protobuf.Any event_payload = 3 [lazy = true];

  // Notification details
  NotificationMessage notification = 4 [lazy = true];

  // Time the event occurred
  google.protobuf.Timestamp event_time = 5 [lazy = true];
}
```

---

