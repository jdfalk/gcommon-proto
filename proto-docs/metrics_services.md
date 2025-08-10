# metrics_services Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 2
- **Messages**: 0
- **Services**: 2
- **Enums**: 0

## Files in this Module

- [metrics_admin_service.proto](#metrics_admin_service)
- [metrics_service.proto](#metrics_service)

## Module Dependencies

**This module depends on**:

- [metrics_1](./metrics_1.md)
- [metrics_api_1](./metrics_api_1.md)
- [metrics_api_2](./metrics_api_2.md)
- [web_api_1](./web_api_1.md)

---

## Detailed Documentation

### metrics_admin_service.proto {#metrics_admin_service}

**Path**: `pkg/metrics/proto/metrics_admin_service.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 45

**Services** (1): `MetricsManagementService`

**Imports** (11):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/create_provider_request.proto` →
  [metrics_api_1](./metrics_api_1.md#create_provider_request)
- `pkg/metrics/proto/create_provider_response.proto` →
  [metrics_api_1](./metrics_api_1.md#create_provider_response)
- `pkg/metrics/proto/delete_provider_request.proto` →
  [metrics_api_1](./metrics_api_1.md#delete_provider_request)
- `pkg/metrics/proto/delete_provider_response.proto` →
  [metrics_api_1](./metrics_api_1.md#delete_provider_response)
- `pkg/metrics/proto/get_provider_stats_request.proto` →
  [metrics_api_1](./metrics_api_1.md#get_provider_stats_request)
- `pkg/metrics/proto/get_provider_stats_response.proto` →
  [metrics_api_1](./metrics_api_1.md#get_provider_stats_response)
- `pkg/metrics/proto/list_providers_request.proto` →
  [metrics_api_1](./metrics_api_1.md#list_providers_request)
- `pkg/metrics/proto/list_providers_response.proto` →
  [metrics_api_1](./metrics_api_1.md#list_providers_response)
- `pkg/metrics/proto/update_provider_request.proto` →
  [metrics_api_2](./metrics_api_2.md#update_provider_request)
- `pkg/metrics/proto/update_provider_response.proto` →
  [metrics_api_2](./metrics_api_2.md#update_provider_response)

#### Source Code

```protobuf
// file: pkg/metrics/proto/metrics_admin_service.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-7890-abcd-1234567890ab

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
// Import all required request and response messages
import "pkg/metrics/proto/create_provider_request.proto";
import "pkg/metrics/proto/create_provider_response.proto";
import "pkg/metrics/proto/delete_provider_request.proto";
import "pkg/metrics/proto/delete_provider_response.proto";
import "pkg/metrics/proto/get_provider_stats_request.proto";
import "pkg/metrics/proto/get_provider_stats_response.proto";
import "pkg/metrics/proto/list_providers_request.proto";
import "pkg/metrics/proto/list_providers_response.proto";
import "pkg/metrics/proto/update_provider_request.proto";
import "pkg/metrics/proto/update_provider_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricsManagementService provides administrative capabilities for metrics providers.
 * This service handles provider lifecycle, configuration, and monitoring.
 */
service MetricsManagementService {
  // Create a new metrics provider
  rpc CreateMetricsProvider(CreateProviderRequest) returns (CreateProviderResponse);

  // Update an existing metrics provider configuration
  rpc UpdateMetricsProvider(UpdateProviderRequest) returns (UpdateProviderResponse);

  // Delete a metrics provider and optionally its data
  rpc DeleteMetricsProvider(DeleteProviderRequest) returns (DeleteProviderResponse);

  // List all configured metrics providers
  rpc ListMetricsProviders(ListProvidersRequest) returns (ListProvidersResponse);

  // Get statistics and status for a specific provider
  rpc GetProviderStats(GetProviderStatsRequest) returns (GetProviderStatsResponse);
}

```

---

### metrics_service.proto {#metrics_service}

**Path**: `pkg/metrics/proto/metrics_service.proto` **Package**:
`gcommon.v1.metrics` **Lines**: 65

**Services** (1): `MetricsService`

**Imports** (19):

- `google/protobuf/go_features.proto`
- `pkg/metrics/proto/get_metric_metadata_request.proto` →
  [metrics_api_1](./metrics_api_1.md#get_metric_metadata_request)
- `pkg/metrics/proto/get_metric_metadata_response.proto` →
  [metrics_api_1](./metrics_api_1.md#get_metric_metadata_response)
- `pkg/metrics/proto/get_metrics_request.proto` →
  [metrics_api_1](./metrics_api_1.md#get_metrics_request) →
  [web_api_1](./web_api_1.md#get_metrics_request)
- `pkg/metrics/proto/get_metrics_response.proto` →
  [metrics_api_1](./metrics_api_1.md#get_metrics_response) →
  [web_api_1](./web_api_1.md#get_metrics_response)
- `pkg/metrics/proto/get_metrics_summary_request.proto` →
  [metrics_api_1](./metrics_api_1.md#get_metrics_summary_request)
- `pkg/metrics/proto/get_metrics_summary_response.proto` →
  [metrics_api_1](./metrics_api_1.md#get_metrics_summary_response)
- `pkg/metrics/proto/metric_data.proto` →
  [metrics_1](./metrics_1.md#metric_data)
- `pkg/metrics/proto/query_metrics_request.proto` →
  [metrics_api_1](./metrics_api_1.md#query_metrics_request)
- `pkg/metrics/proto/query_metrics_response.proto` →
  [metrics_api_1](./metrics_api_1.md#query_metrics_response)
- `pkg/metrics/proto/record_metric_request.proto` →
  [metrics_api_1](./metrics_api_1.md#record_metric_request)
- `pkg/metrics/proto/record_metric_response.proto` →
  [metrics_api_1](./metrics_api_1.md#record_metric_response)
- `pkg/metrics/proto/record_metrics_request.proto` →
  [metrics_api_1](./metrics_api_1.md#record_metrics_request)
- `pkg/metrics/proto/record_metrics_response.proto` →
  [metrics_api_1](./metrics_api_1.md#record_metrics_response)
- `pkg/metrics/proto/register_metric_request.proto` →
  [metrics_api_1](./metrics_api_1.md#register_metric_request)
- `pkg/metrics/proto/register_metric_response.proto` →
  [metrics_api_1](./metrics_api_1.md#register_metric_response)
- `pkg/metrics/proto/stream_metrics_request.proto` →
  [metrics_api_2](./metrics_api_2.md#stream_metrics_request)
- `pkg/metrics/proto/unregister_metric_request.proto` →
  [metrics_api_2](./metrics_api_2.md#unregister_metric_request)
- `pkg/metrics/proto/unregister_metric_response.proto` →
  [metrics_api_2](./metrics_api_2.md#unregister_metric_response)

#### Source Code

```protobuf
// file: pkg/metrics/proto/metrics_service.proto
// version: 1.1.0
// guid: f1g2h3i4-j5k6-7890-l1m2-n3o4p5q6r7s8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "pkg/metrics/proto/get_metric_metadata_request.proto";
import "pkg/metrics/proto/get_metric_metadata_response.proto";
import "pkg/metrics/proto/get_metrics_request.proto";
import "pkg/metrics/proto/get_metrics_response.proto";
import "pkg/metrics/proto/get_metrics_summary_request.proto";
import "pkg/metrics/proto/get_metrics_summary_response.proto";
import "pkg/metrics/proto/metric_data.proto";
import "pkg/metrics/proto/query_metrics_request.proto";
import "pkg/metrics/proto/query_metrics_response.proto";
import "pkg/metrics/proto/record_metric_request.proto";
// Import response messages
import "pkg/metrics/proto/record_metric_response.proto";
import "pkg/metrics/proto/record_metrics_request.proto";
import "pkg/metrics/proto/record_metrics_response.proto";
import "pkg/metrics/proto/register_metric_request.proto";
import "pkg/metrics/proto/register_metric_response.proto";
import "pkg/metrics/proto/stream_metrics_request.proto";
import "pkg/metrics/proto/unregister_metric_request.proto";
import "pkg/metrics/proto/unregister_metric_response.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/metrics/proto";

/**
 * MetricsService provides comprehensive metrics collection and querying capabilities.
 * Supports counters, gauges, histograms, streaming, and custom metrics aggregation.
 */
service MetricsService {
  // Record a single metric data point
  rpc RecordMetric(RecordMetricRequest) returns (RecordMetricResponse);

  // Record multiple metrics in batch for efficiency
  rpc RecordBatchMetrics(RecordMetricsRequest) returns (RecordMetricsResponse);

  // Retrieve metrics data with filtering and aggregation
  rpc GetMetrics(GetMetricsRequest) returns (GetMetricsResponse);

  // Stream metrics data in real-time
  rpc StreamMetrics(StreamMetricsRequest) returns (stream MetricData);

  // Register a new metric definition
  rpc RegisterMetric(RegisterMetricRequest) returns (RegisterMetricResponse);

  // Unregister an existing metric
  rpc UnregisterMetric(UnregisterMetricRequest) returns (UnregisterMetricResponse);

  // Get metadata for a specific metric
  rpc GetMetricMetadata(GetMetricMetadataRequest) returns (GetMetricMetadataResponse);

  // Query metrics data using complex query expressions
  rpc QueryMetrics(QueryMetricsRequest) returns (QueryMetricsResponse);

  // Get summary statistics about metrics
  rpc GetMetricsSummary(GetMetricsSummaryRequest) returns (GetMetricsSummaryResponse);
}

```

---
