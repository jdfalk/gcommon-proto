# queue_events Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 1
- **Messages**: 1
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [metrics_event.proto](#metrics_event)
---


## Detailed Documentation

### metrics_event.proto {#metrics_event}

**Path**: `gcommon/v1/queue/metrics_event.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `MetricsEvent`

**Imports** (4):

- `gcommon/v1/common/metric_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/metrics_event.proto
// version: 1.0.0
// guid: 3d754283-08ab-451e-ad1d-c72c8da71fa4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metric_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MetricsEvent {
  // Timestamp of the event
  google.protobuf.Timestamp timestamp = 1;

  // Queue name
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of metric
  gcommon.v1.common.MetricsMetricType metric_type = 3;

  // Metric value
  double value = 4;

  // Additional metadata
  map<string, string> labels = 5;
}
```

---

