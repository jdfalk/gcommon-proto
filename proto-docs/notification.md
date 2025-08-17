# notification Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 22
- **Messages**: 19
- **Services**: 1
- **Enums**: 2
- ⚠️ **Issues**: 1

## Files in this Module

- [delete_notification_request.proto](#delete_notification_request)
- [delete_notification_response.proto](#delete_notification_response)
- [delivery_channel.proto](#delivery_channel)
- [delivery_channel_type.proto](#delivery_channel_type)
- [delivery_status.proto](#delivery_status)
- [event_notification.proto](#event_notification)
- [get_preferences_request.proto](#get_preferences_request)
- [get_preferences_response.proto](#get_preferences_response)
- [get_template_request.proto](#get_template_request)
- [get_template_response.proto](#get_template_response)
- [list_notifications_request.proto](#list_notifications_request)
- [list_notifications_response.proto](#list_notifications_response)
- [mark_as_read_request.proto](#mark_as_read_request)
- [mark_as_read_response.proto](#mark_as_read_response)
- [notification_message.proto](#notification_message)
- [notification_service.proto](#notification_service)
- [send_notification_request.proto](#send_notification_request)
- [send_notification_response.proto](#send_notification_response)
- [subscription_preferences.proto](#subscription_preferences)
- [template.proto](#template) ⚠️ 1 issues
- [update_preferences_request.proto](#update_preferences_request)
- [update_preferences_response.proto](#update_preferences_response)

## Module Dependencies

**This module depends on**:

- [common](./common.md)

---

## Detailed Documentation

### delete_notification_request.proto {#delete_notification_request}

**Path**: `pkg/notification/proto/delete_notification_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `DeleteNotificationRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/delete_notification_request.proto
// version: 1.0.0
// guid: 20a32413-3de3-416f-a3ad-23c2172121c9

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message DeleteNotificationRequest {
  // Identifier of the notification to delete.
  string notification_id = 1;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### delete_notification_response.proto {#delete_notification_response}

**Path**: `pkg/notification/proto/delete_notification_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 21

**Messages** (1): `DeleteNotificationResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/responses/delete_notification_response.proto
// version: 1.0.0
// guid: d7f015d6-70a1-4fcd-82b3-560a134d7a45

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Response after deleting a notification.
 */
message DeleteNotificationResponse {
  // True if the deletion succeeded.
  bool success = 1;
}

```

---

### delivery_channel.proto {#delivery_channel}

**Path**: `pkg/notification/proto/delivery_channel.proto` **Package**: `gcommon.v1.notification` **Lines**: 28

**Messages** (1): `DeliveryChannel`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/notification/proto/delivery_channel_type.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/delivery_channel.proto
// version: 1.1.0
// guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/notification/proto/delivery_channel_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Delivery channel specifying how a notification is sent.
 */
message DeliveryChannel {
  // Channel type such as email or SMS
  DeliveryChannelType type = 1;

  // Destination address (email, phone number, webhook URL, etc.)
  string target = 2;

  // Optional channel specific configuration
  map<string, string> config = 3 [lazy = true];
}

```

---

### delivery_channel_type.proto {#delivery_channel_type}

**Path**: `pkg/notification/proto/delivery_channel_type.proto` **Package**: `gcommon.v1.notification` **Lines**: 34

**Enums** (1): `DeliveryChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/delivery_channel_type.proto
// version: 1.0.0
// guid: c5d6e7f8-a9b0-1c2d-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Delivery channel type enumeration.
 * Specifies the communication channel for notification delivery.
 */
enum DeliveryChannelType {
  // Unspecified delivery channel
  DELIVERY_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email delivery
  DELIVERY_CHANNEL_TYPE_EMAIL = 1;

  // SMS delivery
  DELIVERY_CHANNEL_TYPE_SMS = 2;

  // Slack message delivery
  DELIVERY_CHANNEL_TYPE_SLACK = 3;

  // Webhook delivery
  DELIVERY_CHANNEL_TYPE_WEBHOOK = 4;
}

```

---

### delivery_status.proto {#delivery_status}

**Path**: `pkg/notification/proto/delivery_status.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Enums** (1): `DeliveryStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/enums/delivery_status.proto
// file: notification/proto/enums/delivery_status.proto
//
// Delivery status enumeration for tracking notification outcomes.
edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

// Notification delivery status
enum DeliveryStatus {
  DELIVERY_STATUS_UNSPECIFIED = 0;
  DELIVERY_STATUS_PENDING = 1;
  DELIVERY_STATUS_SENT = 2;
  DELIVERY_STATUS_FAILED = 3;
  DELIVERY_STATUS_ACKNOWLEDGED = 4;
}

```

---

### event_notification.proto {#event_notification}

**Path**: `pkg/notification/proto/event_notification.proto` **Package**: `gcommon.v1.notification` **Lines**: 36

**Messages** (1): `EventNotification`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/notification/proto/notification_message.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/event_notification.proto
// version: 1.2.0
// guid: d1e2f3g4-h5i6-7890-j1k2-l3m4n5o6p7q8

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/notification/proto/notification_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Notification generated from an event.
 */
message EventNotification {
  // Associated event identifier
  string event_id = 1;

  // Event type or name
  string event_type = 2;

  // Event payload data
  google.protobuf.Any event_payload = 3 [lazy = true];

  // Notification details
  NotificationMessage notification = 4 [lazy = true];

  // Time the event occurred
  google.protobuf.Timestamp event_time = 5 [lazy = true];
}

```

---

### get_preferences_request.proto {#get_preferences_request}

**Path**: `pkg/notification/proto/get_preferences_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `GetPreferencesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/get_preferences_request.proto
// version: 1.0.0
// guid: fb16c45a-545c-4d05-b3fd-34dbc4a9d0c1

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message GetPreferencesRequest {
  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier for the user whose preferences are being requested.
  string user_id = 2;
}

```

---

### get_preferences_response.proto {#get_preferences_response}

**Path**: `pkg/notification/proto/get_preferences_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 26

**Messages** (1): `GetPreferencesResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/response_metadata.proto` → [common](./common.md#response_metadata)
- `pkg/notification/proto/subscription_preferences.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/responses/get_preferences_response.proto
// version: 1.0.0
// guid: 3c2f540d-f827-4df1-9afe-6f31f6d73dd9

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/response_metadata.proto";
import "pkg/notification/proto/subscription_preferences.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * GetPreferencesResponse returns a user's subscription preferences.
 */
message GetPreferencesResponse {
  // Current subscription preferences.
  SubscriptionPreferences preferences = 1;

  // Response metadata for rate limiting and tracing.
  gcommon.v1.common.ResponseMetadata metadata = 2;
}

```

---

### get_template_request.proto {#get_template_request}

**Path**: `pkg/notification/proto/get_template_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `GetTemplateRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/get_template_request.proto
// version: 1.0.0
// guid: 4b8dae31-438b-4407-8f5e-25e99ebd347b

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message GetTemplateRequest {
  // Template identifier to fetch
  string id = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### get_template_response.proto {#get_template_response}

**Path**: `pkg/notification/proto/get_template_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `GetTemplateResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/notification/proto/template.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/get_template_response.proto
// version: 1.2.0
// guid: 525e0a4f-3e9f-4b1a-8d33-fa9c295964a0

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/notification/proto/template.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Response containing a requested notification template.
 */
message GetTemplateResponse {
  // Template data
  Template template = 1 [lazy = true];
}

```

---

### list_notifications_request.proto {#list_notifications_request}

**Path**: `pkg/notification/proto/list_notifications_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `ListNotificationsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/pagination.proto` → [common](./common.md#pagination)

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/list_notifications_request.proto
// version: 1.0.0
// guid: 34151d3e-f3cb-4445-a801-c9a44078e3cd

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/pagination.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Request to list previously sent notifications.
 */
message ListNotificationsRequest {
  // Pagination information for result set.
  gcommon.v1.common.Pagination pagination = 1;
}

```

---

### list_notifications_response.proto {#list_notifications_response}

**Path**: `pkg/notification/proto/list_notifications_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `ListNotificationsResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/notification/proto/notification_message.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/responses/list_notifications_response.proto
// version: 1.0.0
// guid: 7986e6b9-6a3e-4b7e-b093-5a87133742a3

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/notification/proto/notification_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Response containing a list of notifications.
 */
message ListNotificationsResponse {
  // Notifications sorted by creation time descending.
  repeated NotificationMessage notifications = 1;
}

```

---

### mark_as_read_request.proto {#mark_as_read_request}

**Path**: `pkg/notification/proto/mark_as_read_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 22

**Messages** (1): `MarkAsReadRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/mark_as_read_request.proto
// version: 1.0.0
// guid: 106b287f-61f9-4551-8526-53a606fbd0d1

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message MarkAsReadRequest {
  // Identifier of the notification to mark as read.
  string notification_id = 1;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### mark_as_read_response.proto {#mark_as_read_response}

**Path**: `pkg/notification/proto/mark_as_read_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 21

**Messages** (1): `MarkAsReadResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/responses/mark_as_read_response.proto
// version: 1.0.0
// guid: 1fd2817b-1b04-474f-ba5b-190ee82693bd

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Response for marking a notification as read.
 */
message MarkAsReadResponse {
  // True if the operation succeeded.
  bool success = 1;
}

```

---

### notification_message.proto {#notification_message}

**Path**: `pkg/notification/proto/notification_message.proto` **Package**: `gcommon.v1.notification` **Lines**: 47

**Messages** (1): `NotificationMessage`

**Imports** (5):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/notification/proto/delivery_channel.proto`
- `pkg/notification/proto/delivery_status.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/messages/notification_message.proto
// file: notification/proto/messages/notification_message.proto
//
// Message definitions for notification module
edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/notification/proto/delivery_channel.proto";
import "pkg/notification/proto/delivery_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Notification message containing content and delivery details.
 * Supports scheduling, multi-channel delivery, and custom data.
 */
message NotificationMessage {
  // Unique notification identifier
  string id = 1;

  // Subject or title of the notification
  string subject = 2;

  // Body text or formatted content
  string body = 3;

  // Structured data payload for templating
  google.protobuf.Any data = 4 [lazy = true];

  // Delivery channels for this notification
  repeated DeliveryChannel channels = 5;

  // Desired send time (defaults to immediate)
  google.protobuf.Timestamp send_at = 6 [lazy = true];

  // Current delivery status
  DeliveryStatus status = 7;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 8 [lazy = true];
}

```

---

### notification_service.proto {#notification_service}

**Path**: `pkg/notification/proto/notification_service.proto` **Package**: `gcommon.v1.notification` **Lines**: 48

**Services** (1): `NotificationService`

**Imports** (13):

- `google/protobuf/go_features.proto`
- `pkg/notification/proto/delete_notification_request.proto`
- `pkg/notification/proto/delete_notification_response.proto`
- `pkg/notification/proto/get_template_request.proto`
- `pkg/notification/proto/get_template_response.proto`
- `pkg/notification/proto/list_notifications_request.proto`
- `pkg/notification/proto/list_notifications_response.proto`
- `pkg/notification/proto/mark_as_read_request.proto`
- `pkg/notification/proto/mark_as_read_response.proto`
- `pkg/notification/proto/send_notification_request.proto`
- `pkg/notification/proto/send_notification_response.proto`
- `pkg/notification/proto/update_preferences_request.proto`
- `pkg/notification/proto/update_preferences_response.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/services/notification_service.proto
// version: 1.0.0
// guid: e9327023-1377-4f3c-8fed-77a4c7e40b1b

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/notification/proto/delete_notification_request.proto";
import "pkg/notification/proto/delete_notification_response.proto";
import "pkg/notification/proto/get_template_request.proto";
import "pkg/notification/proto/get_template_response.proto";
import "pkg/notification/proto/list_notifications_request.proto";
import "pkg/notification/proto/list_notifications_response.proto";
import "pkg/notification/proto/mark_as_read_request.proto";
import "pkg/notification/proto/mark_as_read_response.proto";
import "pkg/notification/proto/send_notification_request.proto";
import "pkg/notification/proto/send_notification_response.proto";
import "pkg/notification/proto/update_preferences_request.proto";
import "pkg/notification/proto/update_preferences_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * NotificationService handles delivery, retrieval, and management of notifications.
 */
service NotificationService {
  // Send delivers a notification through configured channels.
  rpc Send(SendNotificationRequest) returns (SendNotificationResponse);

  // List returns previously sent notifications.
  rpc List(ListNotificationsRequest) returns (ListNotificationsResponse);

  // Update subscription preferences for a user
  rpc UpdatePreferences(UpdatePreferencesRequest) returns (UpdatePreferencesResponse);

  // Retrieve a notification template by ID
  rpc GetTemplate(GetTemplateRequest) returns (GetTemplateResponse);

  // Mark a notification as read
  rpc MarkAsRead(MarkAsReadRequest) returns (MarkAsReadResponse);

  // Delete a notification
  rpc Delete(DeleteNotificationRequest) returns (DeleteNotificationResponse);
}

```

---

### send_notification_request.proto {#send_notification_request}

**Path**: `pkg/notification/proto/send_notification_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 23

**Messages** (1): `SendNotificationRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/notification/proto/notification_message.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/send_notification_request.proto
// version: 1.0.0
// guid: 42b9620e-9388-4ee6-be25-e4a3a0928211

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/notification/proto/notification_message.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message SendNotificationRequest {
  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Notification to be delivered.
  NotificationMessage notification = 2;
}

```

---

### send_notification_response.proto {#send_notification_response}

**Path**: `pkg/notification/proto/send_notification_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 28

**Messages** (1): `SendNotificationResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/notification/proto/delivery_status.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/responses/send_notification_response.proto
// version: 1.0.0
// guid: 4c4e1ac6-1393-496b-80b5-cb0bd7ef41f1

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/notification/proto/delivery_status.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Response returned after sending a notification.
 */
message SendNotificationResponse {
  // Unique identifier for the queued notification.
  string notification_id = 1;

  // Whether the notification was accepted for delivery
  bool accepted = 2;

  // Current delivery status of the notification
  DeliveryStatus status = 3;
}

```

---

### subscription_preferences.proto {#subscription_preferences}

**Path**: `pkg/notification/proto/subscription_preferences.proto` **Package**: `gcommon.v1.notification` **Lines**: 31

**Messages** (1): `SubscriptionPreferences`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `pkg/notification/proto/delivery_channel_type.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/subscription_preferences.proto
// version: 1.2.0
// guid: e1f2g3h4-i5j6-7890-k1l2-m3n4o5p6q7r8

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/notification/proto/delivery_channel_type.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * User subscription preferences for event notifications.
 */
message SubscriptionPreferences {
  // User or entity identifier
  string user_id = 1;

  // Enabled delivery channels
  repeated DeliveryChannelType channels = 2;

  // Subscribed event types
  repeated string events = 3;

  // Additional arbitrary preferences
  map<string, string> metadata = 4 [lazy = true];
}

```

---

### template.proto {#template}

**Path**: `pkg/notification/proto/template.proto` **Package**: `gcommon.v1.notification` **Lines**: 34

**Messages** (1): `Template`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### ⚠️ Issues Found (1)

- Line 25: Implementation needed - // Template body using placeholders

#### Source Code

```protobuf
// file: pkg/notification/proto/messages/template.proto
// file: notification/proto/messages/template.proto
//
// Notification template definition for reusable messages.
edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Template for rendering notification content.
 */
message Template {
  // Template identifier
  string id = 1;

  // Human readable name
  string name = 2;

  // Template body using placeholders
  string body = 3;

  // Time the template was created
  google.protobuf.Timestamp created_at = 4 [lazy = true];

  // Time the template was last updated
  google.protobuf.Timestamp updated_at = 5 [lazy = true];
}

```

---

### update_preferences_request.proto {#update_preferences_request}

**Path**: `pkg/notification/proto/update_preferences_request.proto` **Package**: `gcommon.v1.notification` **Lines**: 23

**Messages** (1): `UpdatePreferencesRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/common/proto/request_metadata.proto` → [common](./common.md#request_metadata)
- `pkg/notification/proto/subscription_preferences.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/requests/update_preferences_request.proto
// version: 1.0.0
// guid: c74c733f-1a03-4b74-b5f1-cfa062e66475

edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";
import "pkg/common/proto/request_metadata.proto";
import "pkg/notification/proto/subscription_preferences.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

message UpdatePreferencesRequest {
  // Subscription preferences to apply
  SubscriptionPreferences preferences = 1 [lazy = true];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}

```

---

### update_preferences_response.proto {#update_preferences_response}

**Path**: `pkg/notification/proto/update_preferences_response.proto` **Package**: `gcommon.v1.notification` **Lines**: 20

**Messages** (1): `UpdatePreferencesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/notification/proto/responses/update_preferences_response.proto
// version: 1.0.0
// guid: 3eb0a369-6ebb-48fb-b5a1-8e7e3d5d7f39
edition = "2023";

package gcommon.v1.notification;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/notification/proto";

/**
 * Response for updating subscription preferences.
 */
message UpdatePreferencesResponse {
  // Whether the update succeeded
  bool success = 1;
}

```

---
