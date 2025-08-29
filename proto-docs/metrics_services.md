# Metrics Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 2
- **Services**: 2

## Table of Contents

### Services

- [`MetricsManagementService`](#metrics_management_service) - from metrics_management_service.proto
- [`MetricsService`](#metrics_service) - from metrics_service.proto

### Files in this Module

- [metrics_management_service.proto](#metrics_management_service)
- [metrics_service.proto](#metrics_service)

---

## Services Documentation

### metrics_management_service.proto {#metrics_management_service}

**Path**: `gcommon/v1/metrics/metrics_management_service.proto` **Package**: `gcommon.v1.metrics` **Lines**: 45

**Services** (1): `MetricsManagementService`

**Imports** (11):

- `gcommon/v1/metrics/create_provider_request.proto`
- `gcommon/v1/metrics/create_provider_response.proto`
- `gcommon/v1/metrics/delete_provider_request.proto`
- `gcommon/v1/metrics/delete_provider_response.proto`
- `gcommon/v1/metrics/get_provider_stats_request.proto`
- `gcommon/v1/metrics/get_provider_stats_response.proto`
- `gcommon/v1/metrics/list_providers_request.proto`
- `gcommon/v1/metrics/list_providers_response.proto`
- `gcommon/v1/metrics/update_provider_request.proto`
- `gcommon/v1/metrics/update_provider_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metrics_management_service.proto
// version: 1.1.1
// guid: a1b2c3d4-e5f6-7890-abcd-1234567890ab

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/create_provider_request.proto";
import "gcommon/v1/metrics/create_provider_response.proto";
import "gcommon/v1/metrics/delete_provider_request.proto";
import "gcommon/v1/metrics/delete_provider_response.proto";
import "gcommon/v1/metrics/get_provider_stats_request.proto";
import "gcommon/v1/metrics/get_provider_stats_response.proto";
import "gcommon/v1/metrics/list_providers_request.proto";
import "gcommon/v1/metrics/list_providers_response.proto";
import "gcommon/v1/metrics/update_provider_request.proto";
import "gcommon/v1/metrics/update_provider_response.proto";
import "google/protobuf/go_features.proto";

// Import all required request and response messages

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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

**Path**: `gcommon/v1/metrics/metrics_service.proto` **Package**: `gcommon.v1.metrics` **Lines**: 65

**Services** (1): `MetricsService`

**Imports** (19):

- `gcommon/v1/metrics/get_metric_metadata_request.proto`
- `gcommon/v1/metrics/get_metric_metadata_response.proto`
- `gcommon/v1/metrics/get_metrics_request.proto`
- `gcommon/v1/metrics/get_metrics_response.proto`
- `gcommon/v1/metrics/get_metrics_summary_request.proto`
- `gcommon/v1/metrics/get_metrics_summary_response.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `gcommon/v1/metrics/query_metrics_request.proto`
- `gcommon/v1/metrics/query_metrics_response.proto`
- `gcommon/v1/metrics/record_metric_request.proto`
- `gcommon/v1/metrics/record_metric_response.proto`
- `gcommon/v1/metrics/record_metrics_request.proto`
- `gcommon/v1/metrics/record_metrics_response.proto`
- `gcommon/v1/metrics/register_metric_request.proto`
- `gcommon/v1/metrics/register_metric_response.proto`
- `gcommon/v1/metrics/stream_metrics_request.proto`
- `gcommon/v1/metrics/unregister_metric_request.proto`
- `gcommon/v1/metrics/unregister_metric_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metrics_service.proto
// version: 1.1.1
// guid: f1g2h3i4-j5k6-7890-l1m2-n3o4p5q6r7s8

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/get_metric_metadata_request.proto";
import "gcommon/v1/metrics/get_metric_metadata_response.proto";
import "gcommon/v1/metrics/get_metrics_request.proto";
import "gcommon/v1/metrics/get_metrics_response.proto";
import "gcommon/v1/metrics/get_metrics_summary_request.proto";
import "gcommon/v1/metrics/get_metrics_summary_response.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "gcommon/v1/metrics/query_metrics_request.proto";
import "gcommon/v1/metrics/query_metrics_response.proto";
import "gcommon/v1/metrics/record_metric_request.proto";
import "gcommon/v1/metrics/record_metric_response.proto";
import "gcommon/v1/metrics/record_metrics_request.proto";
import "gcommon/v1/metrics/record_metrics_response.proto";
import "gcommon/v1/metrics/register_metric_request.proto";
import "gcommon/v1/metrics/register_metric_response.proto";
import "gcommon/v1/metrics/stream_metrics_request.proto";
import "gcommon/v1/metrics/unregister_metric_request.proto";
import "gcommon/v1/metrics/unregister_metric_response.proto";
import "google/protobuf/go_features.proto";

// Import response messages

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

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
  rpc GetMetrics(MetricsGetMetricsRequest) returns (MetricsGetMetricsResponse);

  // Stream real-time metrics data with configurable filters and options
  rpc StreamMetrics(MetricsStreamMetricsRequest) returns (stream MetricData);

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
