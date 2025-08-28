# metrics_api_2 Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 21
- **Messages**: 21
- **Services**: 0
- **Enums**: 0

## Files in this Module

- [register_metric_request.proto](#register_metric_request)
- [register_metric_response.proto](#register_metric_response)
- [reset_metrics_request.proto](#reset_metrics_request)
- [reset_metrics_response.proto](#reset_metrics_response)
- [set_alerting_rules_request.proto](#set_alerting_rules_request)
- [set_alerting_rules_response.proto](#set_alerting_rules_response)
- [set_metric_metadata_request.proto](#set_metric_metadata_request)
- [set_metric_metadata_response.proto](#set_metric_metadata_response)
- [start_scraping_request.proto](#start_scraping_request)
- [start_scraping_response.proto](#start_scraping_response)
- [stop_scraping_request.proto](#stop_scraping_request)
- [stop_scraping_response.proto](#stop_scraping_response)
- [stream_metrics_request.proto](#stream_metrics_request)
- [unregister_metric_request.proto](#unregister_metric_request)
- [unregister_metric_response.proto](#unregister_metric_response)
- [update_metric_request.proto](#update_metric_request)
- [update_metric_response.proto](#update_metric_response)
- [update_options.proto](#update_options)
- [update_provider_request.proto](#update_provider_request)
- [update_provider_response.proto](#update_provider_response)
- [update_result.proto](#update_result)
---


## Detailed Documentation

### register_metric_request.proto {#register_metric_request}

**Path**: `gcommon/v1/metrics/register_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `RegisterMetricRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_definition.proto`
- `gcommon/v1/metrics/registration_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/register_metric_request.proto
// version: 1.0.0
// guid: bcf2d82b-2ffe-4608-acf1-e58abf98e4d2

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_definition.proto";
import "gcommon/v1/metrics/registration_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegisterMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metric definition to register
  MetricDefinition definition = 2;

  // Optional provider ID to register with
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to replace an existing metric with the same name
  bool replace_existing = 4;

  // Validation options for the registration
  RegistrationOptions options = 5;
}
```

---

### register_metric_response.proto {#register_metric_response}

**Path**: `gcommon/v1/metrics/register_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 52

**Messages** (1): `RegisterMetricResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/registration_result.proto`
- `gcommon/v1/metrics/registration_validation.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/register_metric_response.proto
// version: 1.0.0
// guid: 9cd957ab-069a-4d91-bd48-c466a7a29eb0

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/registration_result.proto";
import "gcommon/v1/metrics/registration_validation.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegisterMetricResponse {
  // Success status of the registration
  bool success = 1;

  // Error information if registration failed
  gcommon.v1.common.Error error = 2;

  // Unique ID assigned to the registered metric
  string metric_id = 3;

  // Name of the registered metric
  string metric_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // When the metric was registered
  google.protobuf.Timestamp registered_at = 5;

  // Provider that handled the registration
  string provider_id = 6;

  // Validation results from the registration process
  RegistrationValidation validation = 7;

  // Information about what was created/updated
  RegistrationResult result = 8;

  // Warnings or informational messages
  repeated string warnings = 9;

  // Whether this replaced an existing metric
  bool replaced_existing = 10;
}
```

---

### reset_metrics_request.proto {#reset_metrics_request}

**Path**: `gcommon/v1/metrics/reset_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `ResetMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/reset_metrics_request.proto
// version: 1.0.0
// guid: 16c1ba58-926f-4a1a-adbe-fe25ec131ea9
// file: proto/gcommon/v1/metrics/v1/reset_metrics_request.proto
//
// Request message for resetting stored metric data.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResetMetricsRequest {
  // Metric name or ID to reset
  string metric = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### reset_metrics_response.proto {#reset_metrics_response}

**Path**: `gcommon/v1/metrics/reset_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `ResetMetricsResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/reset_metrics_response.proto
// version: 1.0.1
// guid: 00510bc8-5a91-49a9-b6ef-49d624b3d846
// file: proto/gcommon/v1/metrics/v1/reset_metrics_response.proto
//
// Response after resetting metric data.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ResetMetricsResponse reports reset status.
 */
message ResetMetricsResponse {
  // Whether the reset succeeded
  bool success = 1;

  // Error information if reset failed
  gcommon.v1.common.Error error = 2;
}
```

---

### set_alerting_rules_request.proto {#set_alerting_rules_request}

**Path**: `gcommon/v1/metrics/set_alerting_rules_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `SetAlertingRulesRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/alerting_rule.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_alerting_rules_request.proto
// version: 1.0.0
// guid: 797328c8-f7f2-498b-9224-8ef45c3dcba8
// file: proto/gcommon/v1/metrics/v1/set_alerting_rules_request.proto
//
// Request message for configuring alerting rules for a metric.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/alerting_rule.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SetAlertingRulesRequest {
  // Metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Rules to set
  repeated AlertingRule rules = 2 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### set_alerting_rules_response.proto {#set_alerting_rules_response}

**Path**: `gcommon/v1/metrics/set_alerting_rules_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `SetAlertingRulesResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_alerting_rules_response.proto
// version: 1.0.1
// guid: 976aa24f-b19c-4700-b14c-3eaec3f9fab4
// file: proto/gcommon/v1/metrics/v1/set_alerting_rules_response.proto
//
// Response after setting alerting rules.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetAlertingRulesResponse confirms alert rule configuration.
 */
message SetAlertingRulesResponse {
  // Whether the operation succeeded
  bool success = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### set_metric_metadata_request.proto {#set_metric_metadata_request}

**Path**: `gcommon/v1/metrics/set_metric_metadata_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `SetMetricMetadataRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_metric_metadata_request.proto
// version: 1.0.1
// guid: d5a7a998-dd17-44a3-97d5-89144b904ee3
// file: proto/gcommon/v1/metrics/v1/set_metric_metadata_request.proto
//
// Request message for updating metric metadata.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SetMetricMetadataRequest {
  // Metric metadata to apply
  MetricMetadata metadata = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata request_meta = 2 [lazy = true];
}
```

---

### set_metric_metadata_response.proto {#set_metric_metadata_response}

**Path**: `gcommon/v1/metrics/set_metric_metadata_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `SetMetricMetadataResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_metric_metadata_response.proto
// version: 1.0.1
// guid: 2594ce5a-5795-4689-b2f9-433919c5cc67
// file: proto/gcommon/v1/metrics/v1/set_metric_metadata_response.proto
//
// Response after updating metric metadata.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetMetricMetadataResponse returns updated metadata.
 */
message SetMetricMetadataResponse {
  // Updated metadata
  MetricMetadata metadata = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### start_scraping_request.proto {#start_scraping_request}

**Path**: `gcommon/v1/metrics/start_scraping_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `StartScrapingRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/start_scraping_request.proto
// version: 1.1.0
// guid: 3bf09215-7dbf-4f23-97b5-911aeb40f125

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StartScrapingRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metrics provider identifier
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Scrape configuration to use
  ScrapeConfig config = 3;
}
```

---

### start_scraping_response.proto {#start_scraping_response}

**Path**: `gcommon/v1/metrics/start_scraping_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `StartScrapingResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/scrape_job.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/start_scraping_response.proto
// version: 1.1.1
// guid: 83543cf4-50e7-4161-9c5f-5ddca3a0655f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/scrape_job.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * StartScrapingResponse returns the result of starting a scrape job.
 */
message StartScrapingResponse {
  // Whether the job was started successfully
  bool success = 1;

  // Error information if unsuccessful
  gcommon.v1.common.Error error = 2;

  // Details of the started scrape job
  ScrapeJob job = 3;

  // Timestamp when the job started
  google.protobuf.Timestamp started_at = 4;
}
```

---

### stop_scraping_request.proto {#stop_scraping_request}

**Path**: `gcommon/v1/metrics/stop_scraping_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `StopScrapingRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stop_scraping_request.proto
// version: 1.1.0
// guid: 4fac5447-f3bb-4627-94d7-4d6115c265f1

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StopScrapingRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier of the job to stop
  string job_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_scraping_response.proto {#stop_scraping_response}

**Path**: `gcommon/v1/metrics/stop_scraping_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `StopScrapingResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/scrape_job.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stop_scraping_response.proto
// version: 1.1.1
// guid: 7d2eb263-b398-4b98-af07-c9950ab73d05

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/scrape_job.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * StopScrapingResponse returns the result of stopping a scrape job.
 */
message StopScrapingResponse {
  // Whether the job was stopped successfully
  bool success = 1;

  // Error information if unsuccessful
  gcommon.v1.common.Error error = 2;

  // Details of the stopped job
  ScrapeJob job = 3;

  // Timestamp when the job stopped
  google.protobuf.Timestamp stopped_at = 4;
}
```

---

### stream_metrics_request.proto {#stream_metrics_request}

**Path**: `gcommon/v1/metrics/stream_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricsStreamMetricsRequest`

**Imports** (7):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/buffer_config.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `gcommon/v1/metrics/stream_options.proto`
- `gcommon/v1/metrics/stream_start.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_metrics_request.proto
// version: 1.0.0
// guid: e3a862c4-9279-4574-baf6-5eb6c9317d19

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/buffer_config.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "gcommon/v1/metrics/stream_options.proto";
import "gcommon/v1/metrics/stream_start.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsStreamMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter to determine which metrics to stream
  MetricFilter filter = 2;

  // Streaming configuration options
  StreamOptions options = 3;

  // Optional provider ID to stream from
  string provider_id = 4 [(buf.validate.field).string.min_len = 1];

  // Starting point for the stream
  StreamStart start = 5;

  // Buffer configuration for the stream
  BufferConfig buffer_config = 6;
}
```

---

### unregister_metric_request.proto {#unregister_metric_request}

**Path**: `gcommon/v1/metrics/unregister_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 38

**Messages** (1): `UnregisterMetricRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/unregistration_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/unregister_metric_request.proto
// version: 1.0.0
// guid: 4beff2f2-e6cd-44fc-9d0e-58e5dbd3afff

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/unregistration_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UnregisterMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metric identifier (either name or ID)
  oneof metric_identifier {
    // Metric name to unregister
    string metric_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

    // Metric ID to unregister
    string metric_id = 3;
  }

  // Optional provider ID to unregister from
  string provider_id = 4;

  // Options for the unregistration process
  UnregistrationOptions options = 5;
}
```

---

### unregister_metric_response.proto {#unregister_metric_response}

**Path**: `gcommon/v1/metrics/unregister_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `UnregisterMetricResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/backup_info.proto`
- `gcommon/v1/metrics/unregistration_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/unregister_metric_response.proto
// version: 1.0.0
// guid: 28148796-f454-44f3-bb31-6352cfaf3755

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/backup_info.proto";
import "gcommon/v1/metrics/unregistration_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UnregisterMetricResponse {
  // Success status of the unregistration
  bool success = 1;

  // Error information if unregistration failed
  gcommon.v1.common.Error error = 2;

  // ID of the metric that was unregistered
  string metric_id = 3;

  // Name of the metric that was unregistered
  string metric_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // When the metric was unregistered
  google.protobuf.Timestamp unregistered_at = 5;

  // Provider that handled the unregistration
  string provider_id = 6;

  // Information about what was deleted/cleaned up
  UnregistrationResult result = 7;

  // Warnings or informational messages
  repeated string warnings = 8;

  // Backup information (if backup was created)
  MetricsBackupInfo backup_info = 9;
}
```

---

### update_metric_request.proto {#update_metric_request}

**Path**: `gcommon/v1/metrics/update_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `UpdateMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_metric_request.proto
// version: 1.0.1
// guid: 552e73bb-8b74-4132-a524-46d64cf01d78
// file: proto/gcommon/v1/metrics/v1/update_metric_request.proto
//
// Request message to update an existing metric definition.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UpdateMetricRequest {
  // Updated metric data
  MetricData metric = 1;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### update_metric_response.proto {#update_metric_response}

**Path**: `gcommon/v1/metrics/update_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `UpdateMetricResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_metric_response.proto
// version: 1.0.1
// guid: 018b666e-d5e2-4c95-ab4f-f525d01cc6b1
// file: proto/gcommon/v1/metrics/v1/update_metric_response.proto
//
// Response returned after updating a metric definition.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * UpdateMetricResponse returns updated metadata.
 */
message UpdateMetricResponse {
  // Updated metric metadata
  MetricMetadata metadata = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### update_options.proto {#update_options}

**Path**: `gcommon/v1/metrics/update_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `UpdateOptions`

**Imports** (2):

- `gcommon/v1/common/update_strategy.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_options.proto
// version: 1.0.1
// guid: 5725505d-38a1-4c4b-861e-d159e74202ce

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/update_strategy.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * UpdateOptions configure the update process.
 */
message UpdateOptions {
  // Whether to validate the configuration before updating
  bool validate_config = 1;

  // Whether to perform a dry run
  bool dry_run = 2;

  // Whether to restart the provider after update (if needed)
  bool restart_if_needed = 3;

  // Whether to backup current configuration before update
  bool backup_config = 4;

  // Update strategy
  gcommon.v1.common.UpdateStrategy strategy = 5;
}
```

---

### update_provider_request.proto {#update_provider_request}

**Path**: `gcommon/v1/metrics/update_provider_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `UpdateProviderRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_provider_request.proto
// version: 1.0.0
// guid: b2c3d4e5-f6a7-8901-2345-6789abcdef01

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UpdateProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to update
  string provider_id = 2;

  // Updated configuration
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  string type = 4;
  map<string, string> config = 5;
  string description = 6 [ (buf.validate.field).string.max_len = 1000 ];
  bool enabled = 7;
}
```

---

### update_provider_response.proto {#update_provider_response}

**Path**: `gcommon/v1/metrics/update_provider_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `UpdateProviderResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_provider_response.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d

// Update provider response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * UpdateProviderResponse contains the result of updating a metrics provider.
 */
message UpdateProviderResponse {
  // Success status of the update
  bool success = 1;

  // Provider ID that was updated
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Updated provider status
  ProviderStatus status = 3;

  // Validation results from the update operation
  repeated gcommon.v1.common.MetricsValidationResult validation_results = 4 [(buf.validate.field).repeated.min_items = 1];

  // Error information if update failed
  gcommon.v1.common.Error error = 5;

  // Timestamp when the update was processed
  google.protobuf.Timestamp updated_at = 6;

  // Configuration changes that were applied
  repeated string applied_changes = 7 [(buf.validate.field).repeated.min_items = 1];

  // Warning messages about the update
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### update_result.proto {#update_result}

**Path**: `gcommon/v1/metrics/update_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `UpdateResult`

**Imports** (4):

- `gcommon/v1/common/metrics_config_change.proto`
- `gcommon/v1/common/update_action.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_result.proto
// version: 1.1.0
// guid: cd6fac61-b122-455b-a74b-34935efa71b0

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_config_change.proto";
import "gcommon/v1/common/update_action.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * UpdateResult contains information about what was changed.
 */
message UpdateResult {
  // What update action was taken
  gcommon.v1.common.UpdateAction action = 1;

  // Configuration changes that were applied
  repeated gcommon.v1.common.MetricsConfigChange config_changes = 2 [(buf.validate.field).repeated.min_items = 1];

  // Settings that were updated
  repeated string updated_settings = 3 [(buf.validate.field).repeated.min_items = 1];

  // Settings that were removed
  repeated string removed_settings = 4 [(buf.validate.field).repeated.min_items = 1];

  // Whether a restart occurred
  bool restarted = 5;

  // Update strategy that was used
  string strategy_used = 6 [(buf.validate.field).string.min_len = 1];

  // Time taken for the update
  string update_duration = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

