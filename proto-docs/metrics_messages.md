# Metrics Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 218
- **Messages**: 218

## Table of Contents

### Messages

- [`APIKeyConfigUpdate`](#api_key_config_update) - from api_key_config_update.proto
- [`AggregationSpec`](#aggregation_spec) - from aggregation_spec.proto
- [`AlertNotification`](#alert_notification) - from alert_notification.proto
- [`AlertingCondition`](#alerting_condition) - from alerting_condition.proto
- [`AlertingRule`](#alerting_rule) - from alerting_rule.proto
- [`AppliedConfig`](#applied_config) - from applied_config.proto
- [`BatchContext`](#batch_context) - from batch_context.proto
- [`BucketInfo`](#bucket_info) - from bucket_info.proto
- [`BufferConfig`](#buffer_config) - from buffer_config.proto
- [`CPUUsage`](#cpu_usage) - from cpu_usage.proto
- [`ConfigurationSummary`](#configuration_summary) - from configuration_summary.proto
- [`CounterConfig`](#counter_config) - from counter_config.proto
- [`CounterMetric`](#counter_metric) - from counter_metric.proto
- [`CreateMetricRequest`](#create_metric_request) - from create_metric_request.proto
- [`CreateMetricResponse`](#create_metric_response) - from create_metric_response.proto
- [`CreateProviderRequest`](#create_provider_request) - from create_provider_request.proto
- [`CreateProviderResponse`](#create_provider_response) - from create_provider_response.proto
- [`DataVolumeDataPoint`](#data_volume_data_point) - from data_volume_data_point.proto
- [`DataVolumeStats`](#data_volume_stats) - from data_volume_stats.proto
- [`DataVolumeTrend`](#data_volume_trend) - from data_volume_trend.proto
- [`DeleteMetricRequest`](#delete_metric_request) - from delete_metric_request.proto
- [`DeleteMetricResponse`](#delete_metric_response) - from delete_metric_response.proto
- [`DeleteProviderRequest`](#delete_provider_request) - from delete_provider_request.proto
- [`DeleteProviderResponse`](#delete_provider_response) - from delete_provider_response.proto
- [`DeletionOptions`](#deletion_options) - from deletion_options.proto
- [`DeletionResult`](#deletion_result) - from deletion_result.proto
- [`DiskUsage`](#disk_usage) - from disk_usage.proto
- [`DryRunResult`](#dry_run_result) - from dry_run_result.proto
- [`ErrorDataPoint`](#error_data_point) - from error_data_point.proto
- [`ErrorEntry`](#error_entry) - from error_entry.proto
- [`ErrorTrend`](#error_trend) - from error_trend.proto
- [`ErrorTypeCount`](#error_type_count) - from error_type_count.proto
- [`ErrorTypeStats`](#error_type_stats) - from error_type_stats.proto
- [`ExportConfig`](#export_config) - from export_config.proto
- [`ExportConfigUpdate`](#export_config_update) - from export_config_update.proto
- [`ExportDestination`](#export_destination) - from export_destination.proto
- [`ExportDestinationStats`](#export_destination_stats) - from export_destination_stats.proto
- [`ExportDestinationUpdate`](#export_destination_update) - from export_destination_update.proto
- [`ExportMetricsRequest`](#export_metrics_request) - from export_metrics_request.proto
- [`ExportMetricsResponse`](#export_metrics_response) - from export_metrics_response.proto
- [`ExportStats`](#export_stats) - from export_stats.proto
- [`ExportStatus`](#export_status) - from export_status.proto
- [`ExporterStatus`](#exporter_status) - from exporter_status.proto
- [`GaugeConfig`](#gauge_config) - from gauge_config.proto
- [`GaugeMetric`](#gauge_metric) - from gauge_metric.proto
- [`GetAlertingRulesRequest`](#get_alerting_rules_request) - from get_alerting_rules_request.proto
- [`GetAlertingRulesResponse`](#get_alerting_rules_response) - from get_alerting_rules_response.proto
- [`GetMetricConfigRequest`](#get_metric_config_request) - from get_metric_config_request.proto
- [`GetMetricConfigResponse`](#get_metric_config_response) - from get_metric_config_response.proto
- [`GetMetricMetadataRequest`](#get_metric_metadata_request) - from get_metric_metadata_request.proto
- [`GetMetricMetadataResponse`](#get_metric_metadata_response) - from get_metric_metadata_response.proto
- [`GetMetricRequest`](#get_metric_request) - from get_metric_request.proto
- [`GetMetricResponse`](#get_metric_response) - from get_metric_response.proto
- [`GetMetricsSummaryRequest`](#get_metrics_summary_request) - from get_metrics_summary_request.proto
- [`GetMetricsSummaryResponse`](#get_metrics_summary_response) - from get_metrics_summary_response.proto
- [`GetProviderStatsRequest`](#get_provider_stats_request) - from get_provider_stats_request.proto
- [`GetProviderStatsResponse`](#get_provider_stats_response) - from get_provider_stats_response.proto
- [`GetScrapeConfigRequest`](#get_scrape_config_request) - from get_scrape_config_request.proto
- [`GetScrapeConfigResponse`](#get_scrape_config_response) - from get_scrape_config_response.proto
- [`GroupBySpec`](#group_by_spec) - from group_by_spec.proto
- [`HealthStatusEntry`](#health_status_entry) - from health_status_entry.proto
- [`HistogramBucket`](#histogram_bucket) - from histogram_bucket.proto
- [`HistogramConfig`](#histogram_config) - from histogram_config.proto
- [`HistogramMetric`](#histogram_metric) - from histogram_metric.proto
- [`HistogramStats`](#histogram_stats) - from histogram_stats.proto
- [`HistogramValue`](#histogram_value) - from histogram_value.proto
- [`ImportConfig`](#import_config) - from import_config.proto
- [`ImportMetricsRequest`](#import_metrics_request) - from import_metrics_request.proto
- [`ImportMetricsResponse`](#import_metrics_response) - from import_metrics_response.proto
- [`LabelDefinition`](#label_definition) - from label_definition.proto
- [`ListMetricsRequest`](#list_metrics_request) - from list_metrics_request.proto
- [`ListMetricsResponse`](#list_metrics_response) - from list_metrics_response.proto
- [`ListProvidersRequest`](#list_providers_request) - from list_providers_request.proto
- [`ListProvidersResponse`](#list_providers_response) - from list_providers_response.proto
- [`MemoryUsage`](#memory_usage) - from memory_usage.proto
- [`MetricAggregation`](#metric_aggregation) - from metric_aggregation.proto
- [`MetricBucket`](#metric_bucket) - from metric_bucket.proto
- [`MetricConfig`](#metric_config) - from metric_config.proto
- [`MetricData`](#metric_data) - from metric_data.proto
- [`MetricDefinition`](#metric_definition) - from metric_definition.proto
- [`MetricFilter`](#metric_filter) - from metric_filter.proto
- [`MetricHealth`](#metric_health) - from metric_health.proto
- [`MetricInfo`](#metric_info) - from metric_info.proto
- [`MetricLabel`](#metric_label) - from metric_label.proto
- [`MetricMetadata`](#metric_metadata) - from metric_metadata.proto
- [`MetricQuantile`](#metric_quantile) - from metric_quantile.proto
- [`MetricQuery`](#metric_query) - from metric_query.proto
- [`MetricResult`](#metric_result) - from metric_result.proto
- [`MetricSample`](#metric_sample) - from metric_sample.proto
- [`MetricSeries`](#metric_series) - from metric_series.proto
- [`MetricStats`](#metric_stats) - from metric_stats.proto
- [`MetricSummary`](#metric_summary) - from metric_summary.proto
- [`MetricTypeConfig`](#metric_type_config) - from metric_type_config.proto
- [`MetricTypeCounts`](#metric_type_counts) - from metric_type_counts.proto
- [`MetricValue`](#metric_value) - from metric_value.proto
- [`MetricsBackupInfo`](#backup_info) - from backup_info.proto
- [`MetricsBatchOptions`](#batch_options) - from batch_options.proto
- [`MetricsBatchStats`](#batch_stats) - from batch_stats.proto
- [`MetricsGetMetricsRequest`](#get_metrics_request) - from get_metrics_request.proto
- [`MetricsGetMetricsResponse`](#get_metrics_response) - from get_metrics_response.proto
- [`MetricsGetStatsRequest`](#get_stats_request) - from get_stats_request.proto
- [`MetricsGetStatsResponse`](#get_stats_response) - from get_stats_response.proto
- [`MetricsHealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`MetricsHealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`MetricsHealthInfo`](#metrics_health_info) - from metrics_health_info.proto
- [`MetricsPaginationInfo`](#pagination_info) - from pagination_info.proto
- [`MetricsPerformanceStats`](#performance_stats) - from performance_stats.proto
- [`MetricsQueryStats`](#query_stats) - from query_stats.proto
- [`MetricsResourceLimits`](#resource_limits) - from resource_limits.proto
- [`MetricsRetryConfig`](#metrics_retry_config) - from metrics_retry_config.proto
- [`MetricsSecurityConfig`](#security_config) - from security_config.proto
- [`MetricsStreamMetricsRequest`](#stream_metrics_request) - from stream_metrics_request.proto
- [`MetricsSummary`](#metrics_summary) - from metrics_summary.proto
- [`MetricsTLSConfig`](#tls_config) - from tls_config.proto
- [`MetricsTimestampRange`](#timestamp_range) - from timestamp_range.proto
- [`NetworkUsage`](#network_usage) - from network_usage.proto
- [`OpenTelemetrySettings`](#open_telemetry_settings) - from open_telemetry_settings.proto
- [`OpenTelemetrySettingsUpdate`](#open_telemetry_settings_update) - from open_telemetry_settings_update.proto
- [`OutputOptions`](#output_options) - from output_options.proto
- [`PercentileMeasurement`](#percentile_measurement) - from percentile_measurement.proto
- [`PerformanceDataPoint`](#performance_data_point) - from performance_data_point.proto
- [`PerformanceTrend`](#performance_trend) - from performance_trend.proto
- [`PrometheusSettings`](#prometheus_settings) - from prometheus_settings.proto
- [`PrometheusSettingsUpdate`](#prometheus_settings_update) - from prometheus_settings_update.proto
- [`ProviderConfig`](#provider_config) - from provider_config.proto
- [`ProviderConfigSummary`](#provider_config_summary) - from provider_config_summary.proto
- [`ProviderConfigUpdate`](#provider_config_update) - from provider_config_update.proto
- [`ProviderEndpoints`](#provider_endpoints) - from provider_endpoints.proto
- [`ProviderFilter`](#provider_filter) - from provider_filter.proto
- [`ProviderInfo`](#provider_info) - from provider_info.proto
- [`ProviderSettings`](#provider_settings) - from provider_settings.proto
- [`ProviderSettingsUpdate`](#provider_settings_update) - from provider_settings_update.proto
- [`ProviderStatistics`](#provider_statistics) - from provider_statistics.proto
- [`ProviderStats`](#provider_stats) - from provider_stats.proto
- [`ProviderStatus`](#provider_status) - from provider_status.proto
- [`ProviderSummary`](#provider_summary) - from provider_summary.proto
- [`Quantile`](#quantile) - from quantile.proto
- [`QueryMetricsRequest`](#query_metrics_request) - from query_metrics_request.proto
- [`QueryMetricsResponse`](#query_metrics_response) - from query_metrics_response.proto
- [`QueryOutputOptions`](#query_output_options) - from query_output_options.proto
- [`QueryPlan`](#query_plan) - from query_plan.proto
- [`QueryStatistics`](#query_statistics) - from query_statistics.proto
- [`QueryStep`](#query_step) - from query_step.proto
- [`RecordCounterRequest`](#record_counter_request) - from record_counter_request.proto
- [`RecordCounterResponse`](#record_counter_response) - from record_counter_response.proto
- [`RecordGaugeRequest`](#record_gauge_request) - from record_gauge_request.proto
- [`RecordGaugeResponse`](#record_gauge_response) - from record_gauge_response.proto
- [`RecordHistogramRequest`](#record_histogram_request) - from record_histogram_request.proto
- [`RecordHistogramResponse`](#record_histogram_response) - from record_histogram_response.proto
- [`RecordMetricRequest`](#record_metric_request) - from record_metric_request.proto
- [`RecordMetricResponse`](#record_metric_response) - from record_metric_response.proto
- [`RecordMetricsRequest`](#record_metrics_request) - from record_metrics_request.proto
- [`RecordMetricsResponse`](#record_metrics_response) - from record_metrics_response.proto
- [`RecordSummaryRequest`](#record_summary_request) - from record_summary_request.proto
- [`RecordSummaryResponse`](#record_summary_response) - from record_summary_response.proto
- [`RecordingStats`](#recording_stats) - from recording_stats.proto
- [`RegisterMetricRequest`](#register_metric_request) - from register_metric_request.proto
- [`RegisterMetricResponse`](#register_metric_response) - from register_metric_response.proto
- [`RegistrationOptions`](#registration_options) - from registration_options.proto
- [`RegistrationResult`](#registration_result) - from registration_result.proto
- [`RegistrationValidation`](#registration_validation) - from registration_validation.proto
- [`ResetMetricsRequest`](#reset_metrics_request) - from reset_metrics_request.proto
- [`ResetMetricsResponse`](#reset_metrics_response) - from reset_metrics_response.proto
- [`ResourceAllocations`](#resource_allocations) - from resource_allocations.proto
- [`ResourceDataPoint`](#resource_data_point) - from resource_data_point.proto
- [`ResourceLimitsSummary`](#resource_limits_summary) - from resource_limits_summary.proto
- [`ResourceLimitsUpdate`](#resource_limits_update) - from resource_limits_update.proto
- [`ResourceUsage`](#resource_usage) - from resource_usage.proto
- [`ResourceUsageStats`](#resource_usage_stats) - from resource_usage_stats.proto
- [`ResourceUsageTrend`](#resource_usage_trend) - from resource_usage_trend.proto
- [`SchemaChange`](#schema_change) - from schema_change.proto
- [`ScrapeConfig`](#scrape_config) - from scrape_config.proto
- [`ScrapeJob`](#scrape_job) - from scrape_job.proto
- [`ScrapeTarget`](#scrape_target) - from scrape_target.proto
- [`SecondarySortField`](#secondary_sort_field) - from secondary_sort_field.proto
- [`SecurityConfigUpdate`](#security_config_update) - from security_config_update.proto
- [`SecuritySummary`](#security_summary) - from security_summary.proto
- [`SetAlertingRulesRequest`](#set_alerting_rules_request) - from set_alerting_rules_request.proto
- [`SetAlertingRulesResponse`](#set_alerting_rules_response) - from set_alerting_rules_response.proto
- [`SetMetricConfigRequest`](#set_metric_config_request) - from set_metric_config_request.proto
- [`SetMetricConfigResponse`](#set_metric_config_response) - from set_metric_config_response.proto
- [`SetMetricMetadataRequest`](#set_metric_metadata_request) - from set_metric_metadata_request.proto
- [`SetMetricMetadataResponse`](#set_metric_metadata_response) - from set_metric_metadata_response.proto
- [`SetScrapeConfigRequest`](#set_scrape_config_request) - from set_scrape_config_request.proto
- [`SetScrapeConfigResponse`](#set_scrape_config_response) - from set_scrape_config_response.proto
- [`StartScrapingRequest`](#start_scraping_request) - from start_scraping_request.proto
- [`StartScrapingResponse`](#start_scraping_response) - from start_scraping_response.proto
- [`StatsDSettings`](#stats_d_settings) - from stats_d_settings.proto
- [`StatsDSettingsUpdate`](#stats_d_settings_update) - from stats_d_settings_update.proto
- [`StatsOptions`](#stats_options) - from stats_options.proto
- [`StopScrapingRequest`](#stop_scraping_request) - from stop_scraping_request.proto
- [`StopScrapingResponse`](#stop_scraping_response) - from stop_scraping_response.proto
- [`StreamOptions`](#stream_options) - from stream_options.proto
- [`StreamStart`](#stream_start) - from stream_start.proto
- [`SummaryConfig`](#summary_config) - from summary_config.proto
- [`SummaryMetric`](#summary_metric) - from summary_metric.proto
- [`SummaryOptions`](#summary_options) - from summary_options.proto
- [`SummaryQuantile`](#summary_quantile) - from summary_quantile.proto
- [`SummaryValue`](#summary_value) - from summary_value.proto
- [`TLSConfigUpdate`](#tls_config_update) - from tls_config_update.proto
- [`TagUpdates`](#tag_updates) - from tag_updates.proto
- [`TimeSeries`](#time_series) - from time_series.proto
- [`TimerMetric`](#timer_metric) - from timer_metric.proto
- [`TimerStatistics`](#timer_statistics) - from timer_statistics.proto
- [`TopMetrics`](#top_metrics) - from top_metrics.proto
- [`TrendAnalysis`](#trend_analysis) - from trend_analysis.proto
- [`UnregisterMetricRequest`](#unregister_metric_request) - from unregister_metric_request.proto
- [`UnregisterMetricResponse`](#unregister_metric_response) - from unregister_metric_response.proto
- [`UnregistrationOptions`](#unregistration_options) - from unregistration_options.proto
- [`UnregistrationResult`](#unregistration_result) - from unregistration_result.proto
- [`UpdateMetricRequest`](#update_metric_request) - from update_metric_request.proto
- [`UpdateMetricResponse`](#update_metric_response) - from update_metric_response.proto
- [`UpdateOptions`](#update_options) - from update_options.proto
- [`UpdateProviderRequest`](#update_provider_request) - from update_provider_request.proto
- [`UpdateProviderResponse`](#update_provider_response) - from update_provider_response.proto
- [`UpdateResult`](#update_result) - from update_result.proto
- [`ValidationRules`](#validation_rules) - from validation_rules.proto
- [`ValidationSummary`](#validation_summary) - from validation_summary.proto

### Files in this Module

- [aggregation_spec.proto](#aggregation_spec)
- [alert_notification.proto](#alert_notification)
- [alerting_condition.proto](#alerting_condition)
- [alerting_rule.proto](#alerting_rule)
- [bucket_info.proto](#bucket_info)
- [counter_metric.proto](#counter_metric)
- [cpu_usage.proto](#cpu_usage)
- [data_volume_data_point.proto](#data_volume_data_point)
- [data_volume_stats.proto](#data_volume_stats)
- [data_volume_trend.proto](#data_volume_trend)
- [deletion_options.proto](#deletion_options)
- [deletion_result.proto](#deletion_result)
- [disk_usage.proto](#disk_usage)
- [dry_run_result.proto](#dry_run_result)
- [error_data_point.proto](#error_data_point)
- [error_entry.proto](#error_entry)
- [error_trend.proto](#error_trend)
- [error_type_count.proto](#error_type_count)
- [error_type_stats.proto](#error_type_stats)
- [export_destination.proto](#export_destination)
- [export_destination_stats.proto](#export_destination_stats)
- [export_destination_update.proto](#export_destination_update)
- [export_stats.proto](#export_stats)
- [export_status.proto](#export_status)
- [exporter_status.proto](#exporter_status)
- [gauge_metric.proto](#gauge_metric)
- [group_by_spec.proto](#group_by_spec)
- [health_status_entry.proto](#health_status_entry)
- [histogram_bucket.proto](#histogram_bucket)
- [histogram_metric.proto](#histogram_metric)
- [histogram_stats.proto](#histogram_stats)
- [histogram_value.proto](#histogram_value)
- [label_definition.proto](#label_definition)
- [memory_usage.proto](#memory_usage)
- [metric_aggregation.proto](#metric_aggregation)
- [metric_bucket.proto](#metric_bucket)
- [metric_data.proto](#metric_data)
- [metric_definition.proto](#metric_definition)
- [metric_filter.proto](#metric_filter)
- [metric_health.proto](#metric_health)
- [metric_info.proto](#metric_info)
- [metric_label.proto](#metric_label)
- [metric_metadata.proto](#metric_metadata)
- [metric_quantile.proto](#metric_quantile)
- [metric_query.proto](#metric_query)
- [metric_result.proto](#metric_result)
- [metric_sample.proto](#metric_sample)
- [metric_series.proto](#metric_series)
- [metric_stats.proto](#metric_stats)
- [metric_summary.proto](#metric_summary)
- [metric_type_counts.proto](#metric_type_counts)
- [metric_value.proto](#metric_value)
- [metrics_health_info.proto](#metrics_health_info)
- [metrics_summary.proto](#metrics_summary)
- [network_usage.proto](#network_usage)
- [open_telemetry_settings.proto](#open_telemetry_settings)
- [open_telemetry_settings_update.proto](#open_telemetry_settings_update)
- [output_options.proto](#output_options)
- [pagination_info.proto](#pagination_info)
- [percentile_measurement.proto](#percentile_measurement)
- [performance_data_point.proto](#performance_data_point)
- [performance_stats.proto](#performance_stats)
- [performance_trend.proto](#performance_trend)
- [prometheus_settings.proto](#prometheus_settings)
- [prometheus_settings_update.proto](#prometheus_settings_update)
- [provider_endpoints.proto](#provider_endpoints)
- [provider_filter.proto](#provider_filter)
- [provider_info.proto](#provider_info)
- [provider_settings.proto](#provider_settings)
- [provider_settings_update.proto](#provider_settings_update)
- [provider_statistics.proto](#provider_statistics)
- [provider_stats.proto](#provider_stats)
- [provider_status.proto](#provider_status)
- [provider_summary.proto](#provider_summary)
- [quantile.proto](#quantile)
- [query_output_options.proto](#query_output_options)
- [query_plan.proto](#query_plan)
- [query_statistics.proto](#query_statistics)
- [query_stats.proto](#query_stats)
- [query_step.proto](#query_step)
- [recording_stats.proto](#recording_stats)
- [registration_options.proto](#registration_options)
- [registration_result.proto](#registration_result)
- [registration_validation.proto](#registration_validation)
- [resource_allocations.proto](#resource_allocations)
- [resource_data_point.proto](#resource_data_point)
- [resource_limits.proto](#resource_limits)
- [resource_limits_summary.proto](#resource_limits_summary)
- [resource_limits_update.proto](#resource_limits_update)
- [resource_usage.proto](#resource_usage)
- [resource_usage_stats.proto](#resource_usage_stats)
- [resource_usage_trend.proto](#resource_usage_trend)
- [schema_change.proto](#schema_change)
- [scrape_job.proto](#scrape_job)
- [scrape_target.proto](#scrape_target)
- [secondary_sort_field.proto](#secondary_sort_field)
- [security_summary.proto](#security_summary)
- [stats_d_settings.proto](#stats_d_settings)
- [stats_d_settings_update.proto](#stats_d_settings_update)
- [stats_options.proto](#stats_options)
- [stream_options.proto](#stream_options)
- [stream_start.proto](#stream_start)
- [summary_metric.proto](#summary_metric)
- [summary_options.proto](#summary_options)
- [summary_quantile.proto](#summary_quantile)
- [summary_value.proto](#summary_value)
- [tag_updates.proto](#tag_updates)
- [time_series.proto](#time_series)
- [timer_metric.proto](#timer_metric)
- [timer_statistics.proto](#timer_statistics)
- [timestamp_range.proto](#timestamp_range)
- [top_metrics.proto](#top_metrics)
- [trend_analysis.proto](#trend_analysis)
- [unregistration_options.proto](#unregistration_options)
- [unregistration_result.proto](#unregistration_result)
- [validation_rules.proto](#validation_rules)
- [validation_summary.proto](#validation_summary)
- [api_key_config_update.proto](#api_key_config_update)
- [applied_config.proto](#applied_config)
- [buffer_config.proto](#buffer_config)
- [configuration_summary.proto](#configuration_summary)
- [counter_config.proto](#counter_config)
- [export_config.proto](#export_config)
- [export_config_update.proto](#export_config_update)
- [gauge_config.proto](#gauge_config)
- [get_metric_config_request.proto](#get_metric_config_request)
- [get_metric_config_response.proto](#get_metric_config_response)
- [get_scrape_config_request.proto](#get_scrape_config_request)
- [get_scrape_config_response.proto](#get_scrape_config_response)
- [histogram_config.proto](#histogram_config)
- [import_config.proto](#import_config)
- [metric_config.proto](#metric_config)
- [metric_type_config.proto](#metric_type_config)
- [metrics_retry_config.proto](#metrics_retry_config)
- [provider_config.proto](#provider_config)
- [provider_config_summary.proto](#provider_config_summary)
- [provider_config_update.proto](#provider_config_update)
- [scrape_config.proto](#scrape_config)
- [security_config.proto](#security_config)
- [security_config_update.proto](#security_config_update)
- [set_metric_config_request.proto](#set_metric_config_request)
- [set_metric_config_response.proto](#set_metric_config_response)
- [set_scrape_config_request.proto](#set_scrape_config_request)
- [set_scrape_config_response.proto](#set_scrape_config_response)
- [summary_config.proto](#summary_config)
- [tls_config.proto](#tls_config)
- [tls_config_update.proto](#tls_config_update)
- [backup_info.proto](#backup_info)
- [batch_context.proto](#batch_context)
- [batch_options.proto](#batch_options)
- [batch_stats.proto](#batch_stats)
- [create_metric_request.proto](#create_metric_request)
- [create_metric_response.proto](#create_metric_response)
- [create_provider_request.proto](#create_provider_request)
- [create_provider_response.proto](#create_provider_response)
- [delete_metric_request.proto](#delete_metric_request)
- [delete_metric_response.proto](#delete_metric_response)
- [delete_provider_request.proto](#delete_provider_request)
- [delete_provider_response.proto](#delete_provider_response)
- [export_metrics_request.proto](#export_metrics_request)
- [export_metrics_response.proto](#export_metrics_response)
- [get_alerting_rules_request.proto](#get_alerting_rules_request)
- [get_alerting_rules_response.proto](#get_alerting_rules_response)
- [get_metric_metadata_request.proto](#get_metric_metadata_request)
- [get_metric_metadata_response.proto](#get_metric_metadata_response)
- [get_metric_request.proto](#get_metric_request)
- [get_metric_response.proto](#get_metric_response)
- [get_metrics_request.proto](#get_metrics_request)
- [get_metrics_response.proto](#get_metrics_response)
- [get_metrics_summary_request.proto](#get_metrics_summary_request)
- [get_metrics_summary_response.proto](#get_metrics_summary_response)
- [get_provider_stats_request.proto](#get_provider_stats_request)
- [get_provider_stats_response.proto](#get_provider_stats_response)
- [get_stats_request.proto](#get_stats_request)
- [get_stats_response.proto](#get_stats_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [import_metrics_request.proto](#import_metrics_request)
- [import_metrics_response.proto](#import_metrics_response)
- [list_metrics_request.proto](#list_metrics_request)
- [list_metrics_response.proto](#list_metrics_response)
- [list_providers_request.proto](#list_providers_request)
- [list_providers_response.proto](#list_providers_response)
- [query_metrics_request.proto](#query_metrics_request)
- [query_metrics_response.proto](#query_metrics_response)
- [record_counter_request.proto](#record_counter_request)
- [record_counter_response.proto](#record_counter_response)
- [record_gauge_request.proto](#record_gauge_request)
- [record_gauge_response.proto](#record_gauge_response)
- [record_histogram_request.proto](#record_histogram_request)
- [record_histogram_response.proto](#record_histogram_response)
- [record_metric_request.proto](#record_metric_request)
- [record_metric_response.proto](#record_metric_response)
- [record_metrics_request.proto](#record_metrics_request)
- [record_metrics_response.proto](#record_metrics_response)
- [record_summary_request.proto](#record_summary_request)
- [record_summary_response.proto](#record_summary_response)
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


## Messages Documentation

### aggregation_spec.proto {#aggregation_spec}

**Path**: `gcommon/v1/metrics/aggregation_spec.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `AggregationSpec`

**Imports** (4):

- `gcommon/v1/common/aggregation_type.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/aggregation_spec.proto
// version: 1.0.0
// guid: 169a9fb5-9a9e-4ba6-beaa-63915a9a9839

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/aggregation_type.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message AggregationSpec {
  // Type of aggregation to perform
  gcommon.v1.common.AggregationType aggregation_type = 1;

  // Field to aggregate on (if applicable)
  string field = 2 [(buf.validate.field).string.min_len = 1];

  // Time window for aggregation
  google.protobuf.Duration window = 3;

  // Step/resolution for time-based aggregation
  google.protobuf.Duration step = 4;

  // Additional parameters for complex aggregations
  map<string, string> parameters = 5;
}
```

---

### alert_notification.proto {#alert_notification}

**Path**: `gcommon/v1/metrics/alert_notification.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `AlertNotification`

**Imports** (4):

- `gcommon/v1/common/metrics_alert_severity.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alert_notification.proto
// version: 1.0.0
// guid: 91304a90-5966-4b20-af06-2668e7d2a958

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_alert_severity.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * AlertNotification represents a notification event generated when an
 * alerting rule is triggered.
 */
message AlertNotification {
  // Identifier of the alerting rule that triggered.
  string rule_id = 1 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the notification was generated.
  google.protobuf.Timestamp time = 2;

  // Severity level of the alert.
  gcommon.v1.common.MetricsAlertSeverity severity = 3;

  // Human readable message describing the alert.
  string message = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### alerting_condition.proto {#alerting_condition}

**Path**: `gcommon/v1/metrics/alerting_condition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `AlertingCondition`

**Imports** (3):

- `gcommon/v1/common/comparison_operator.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alerting_condition.proto
// version: 1.0.0
// guid: c1e0ab41-b93c-4d9f-91a4-035998d0488d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/comparison_operator.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * AlertingCondition specifies a single metric threshold comparison
 * that triggers an alert when satisfied.
 */
message AlertingCondition {
  // Operator to use when comparing the metric value to the threshold.
  gcommon.v1.common.ComparisonOperator operator = 1;

  // Metric name or query expression being evaluated.
  string metric = 2 [(buf.validate.field).string.min_len = 1];

  // Threshold value to compare against.
  double threshold = 3 [(buf.validate.field).double.gte = 0.0];

  // Duration in seconds the condition must hold true before firing.
  int32 duration_seconds = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### alerting_rule.proto {#alerting_rule}

**Path**: `gcommon/v1/metrics/alerting_rule.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `AlertingRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alerting_rule.proto
// version: 1.0.0
// guid: c5d6e7f8-901c-356b-0123-678901234567

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message AlertingRule {
  // Rule ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Rule name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Query expression
  string query = 3;

  // Alert condition
  string condition = 4;

  // Threshold value
  double threshold = 5;

  // Rule enabled status
  bool enabled = 6;
}
```

---

### bucket_info.proto {#bucket_info}

**Path**: `gcommon/v1/metrics/bucket_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `BucketInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/bucket_info.proto
// version: 1.0.0
// guid: 1e2d379b-a3a4-4bc6-9bc8-121a62e7c85b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message BucketInfo {
  // Upper bound of the bucket
  double upper_bound = 1 [(buf.validate.field).double.gte = 0.0];

  // Count in this bucket after the observation
  uint64 count = 2 [(buf.validate.field).uint64.gte = 0];

  // Bucket index
  int32 bucket_index = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### counter_metric.proto {#counter_metric}

**Path**: `gcommon/v1/metrics/counter_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `CounterMetric`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/counter_metric.proto
// version: 1.0.0
// guid: 22048541-e8e6-4cf5-b476-cf12764abfb4
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * CounterMetric represents a monotonically increasing counter.
 * Counters only increase in value and are typically used for tracking
 * cumulative values like total requests, errors, or bytes processed.
 */
message CounterMetric {
  // Unique identifier for this counter
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Counter name/label
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current counter value (must be monotonically increasing)
  double value = 3;

  // Timestamp when this value was recorded
  google.protobuf.Timestamp timestamp = 4;

  // Counter description/help text
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

  // Key-value labels for this counter
  map<string, string> labels = 6;

  // Sample count (for internal tracking)
  uint64 sample_count = 7;
}
```

---

### cpu_usage.proto {#cpu_usage}

**Path**: `gcommon/v1/metrics/cpu_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `CPUUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/cpu_usage.proto
// version: 1.0.0
// guid: cda5276c-5b68-4519-b1f6-c245a74b2d66

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CPUUsage {
  // Current CPU usage (percentage)
  double current_percent = 1 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Average CPU usage (percentage)
  double avg_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Peak CPU usage (percentage)
  double peak_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### data_volume_data_point.proto {#data_volume_data_point}

**Path**: `gcommon/v1/metrics/data_volume_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `DataVolumeDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/data_volume_data_point.proto
// version: 1.0.0
// guid: c039b372-c314-4b88-82b6-3838745f0299

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DataVolumeDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 total_bytes = 2 [(buf.validate.field).int64.gte = 0];
  int64 total_metrics = 3 [(buf.validate.field).int64.gte = 0];
  int64 total_data_points = 4 [(buf.validate.field).int64.gte = 0];
  double ingestion_rate = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### data_volume_stats.proto {#data_volume_stats}

**Path**: `gcommon/v1/metrics/data_volume_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 38

**Messages** (1): `DataVolumeStats`

**Imports** (3):

- `gcommon/v1/metrics/data_volume_data_point.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/data_volume_stats.proto
// version: 1.0.0
// guid: 85a18add-5de2-4de6-9e3a-05e4959520e4

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/data_volume_data_point.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DataVolumeStats {
  // Total data stored (bytes)
  int64 total_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of metrics
  int64 total_metrics = 2 [(buf.validate.field).int64.gte = 0];

  // Total number of data points
  int64 total_data_points = 3 [(buf.validate.field).int64.gte = 0];

  // Data ingestion rate (bytes per second)
  double ingestion_rate_bytes_per_second = 4 [(buf.validate.field).double.gte = 0.0];

  // Data points ingestion rate (points per second)
  double ingestion_rate_points_per_second = 5 [(buf.validate.field).double.gte = 0.0];

  // Compression ratio
  double compression_ratio = 6 [(buf.validate.field).double.gte = 0.0];

  // Time-series data volume
  repeated DataVolumeDataPoint volume_timeseries = 7 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### data_volume_trend.proto {#data_volume_trend}

**Path**: `gcommon/v1/metrics/data_volume_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `DataVolumeTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/data_volume_trend.proto
// version: 1.0.0
// guid: 069bcf6d-438e-4623-85fa-d0c875cc7370

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DataVolumeTrend {
  string volume_trend = 1; // "increasing", "decreasing", "stable"
  string ingestion_trend = 2; // "increasing", "decreasing", "stable"
  double trend_confidence = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### deletion_options.proto {#deletion_options}

**Path**: `gcommon/v1/metrics/deletion_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `DeletionOptions`

**Imports** (3):

- `gcommon/v1/common/cleanup_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/deletion_options.proto
// version: 1.0.0
// guid: 6e247c69-d9f2-452e-bb15-e81da5c53d42

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/cleanup_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * DeletionOptions configure the deletion process.
 */
message DeletionOptions {
  // Whether to delete all associated data
  bool delete_data = 1;

  // Whether to delete associated indices
  bool delete_indices = 2;

  // Whether to delete configuration backups
  bool delete_backups = 3;

  // Whether to stop all exports before deletion
  bool stop_exports = 4;

  // Grace period before actual deletion
  string grace_period = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to perform a dry run
  bool dry_run = 6;

  // Whether to force deletion even if provider is in use
  bool force = 7;

  // Whether to create a final backup before deletion
  bool create_backup = 8;

  // Cleanup strategy to use
  gcommon.v1.common.CleanupStrategy cleanup_strategy = 9;

  // Whether to wait for ongoing operations to complete
  bool wait_for_completion = 10;

  // Maximum time to wait for operations to complete
  string completion_timeout = 11 [(buf.validate.field).string.min_len = 1];
}
```

---

### deletion_result.proto {#deletion_result}

**Path**: `gcommon/v1/metrics/deletion_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `DeletionResult`

**Imports** (3):

- `gcommon/v1/metrics/dry_run_result.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/deletion_result.proto
// version: 1.0.0
// guid: a612d279-a201-40da-99b2-e6f962d0335f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/dry_run_result.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeletionResult {
  // Whether the provider was actually deleted
  bool provider_deleted = 1;

  // Amount of data that was deleted
  int64 data_deleted_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Number of metrics that were deleted
  int64 metrics_deleted = 3 [(buf.validate.field).int64.gte = 0];

  // Number of data points that were deleted
  int64 data_points_deleted = 4 [(buf.validate.field).int64.gte = 0];

  // Indices that were deleted
  repeated string deleted_indices = 5 [(buf.validate.field).repeated.min_items = 1];

  // Exports that were stopped
  repeated string stopped_exports = 6 [(buf.validate.field).repeated.min_items = 1];

  // Backups that were deleted
  repeated string deleted_backups = 7 [(buf.validate.field).repeated.min_items = 1];

  // Cleanup strategy that was used
  string cleanup_strategy_used = 8 [(buf.validate.field).string.min_len = 1];

  // Time taken for the deletion
  string deletion_duration = 9 [(buf.validate.field).string.min_len = 1];

  // What would be deleted (for dry run operations)
  DryRunResult dry_run_result = 10;
}
```

---

### disk_usage.proto {#disk_usage}

**Path**: `gcommon/v1/metrics/disk_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `DiskUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/disk_usage.proto
// version: 1.0.0
// guid: 1c6c18b3-8797-41ff-ba40-b31de4bb0e6d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DiskUsage {
  // Currently used disk space (bytes)
  int64 used_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Disk space limit (bytes)
  int64 limit_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Usage percentage
  double usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // I/O operations per second
  double iops = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### dry_run_result.proto {#dry_run_result}

**Path**: `gcommon/v1/metrics/dry_run_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `DryRunResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/dry_run_result.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174027

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * DryRunResult contains information about what would happen in a dry run.
 */
message DryRunResult {
  // Number of bytes that would be deleted
  int64 would_delete_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Number of data points that would be deleted
  int64 would_delete_points = 2 [(buf.validate.field).int64.gte = 0];

  // Number of indices that would be deleted
  int64 would_delete_indices = 3 [(buf.validate.field).int64.gte = 0];

  // Number of exports that would be stopped
  int64 would_stop_exports = 4 [(buf.validate.field).int64.gte = 0];

  // Estimated time for deletion to complete
  string estimated_deletion_time = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### error_data_point.proto {#error_data_point}

**Path**: `gcommon/v1/metrics/error_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `ErrorDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_data_point.proto
// version: 1.0.0
// guid: fc39a17b-849c-4ff7-ba0d-2d1afb9ff84c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 error_count = 2 [(buf.validate.field).int64.gte = 0];
  double error_rate = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### error_entry.proto {#error_entry}

**Path**: `gcommon/v1/metrics/error_entry.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `ErrorEntry`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_entry.proto
// version: 1.0.0
// guid: bbfe0393-e730-465d-a5fb-b1b75d58a866

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorEntry {
  google.protobuf.Timestamp timestamp = 1;
  string error_type = 2 [(buf.validate.field).string.min_len = 1];
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
  int32 count = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### error_trend.proto {#error_trend}

**Path**: `gcommon/v1/metrics/error_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `ErrorTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_trend.proto
// version: 1.0.0
// guid: 8dd5518b-cd7a-4978-b7c5-24368e5b51aa

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorTrend {
  string error_rate_trend = 1; // "improving", "worsening", "stable"
  double trend_confidence = 2 [(buf.validate.field).double.gte = 0.0];
  repeated string emerging_error_types = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### error_type_count.proto {#error_type_count}

**Path**: `gcommon/v1/metrics/error_type_count.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `ErrorTypeCount`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/error_type_count.proto
// version: 1.0.0
// guid: 8116a2bc-950e-407c-9db8-2f3985e9394d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorTypeCount {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double percentage = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### error_type_stats.proto {#error_type_stats}

**Path**: `gcommon/v1/metrics/error_type_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `ErrorTypeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/error_type_stats.proto
// version: 1.0.0
// guid: 93946dec-5ff0-40d4-8fd3-ff3d9c0b3dc4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ErrorTypeStats {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double rate = 3 [(buf.validate.field).double.gte = 0.0];
  double percentage = 4 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### export_destination.proto {#export_destination}

**Path**: `gcommon/v1/metrics/export_destination.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `ExportDestination`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_destination.proto
// version: 1.0.0
// guid: c917e7d5-f72f-494a-b1f4-7e72c44daa5c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportDestination {
  // Destination type (file, http, s3, etc.)
  string type = 1 [(buf.validate.field).string.min_len = 1];

  // Destination configuration
  map<string, string> config = 2;

  // Whether this destination is enabled
  bool enabled = 3;
}
```

---

### export_destination_stats.proto {#export_destination_stats}

**Path**: `gcommon/v1/metrics/export_destination_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `ExportDestinationStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_destination_stats.proto
// version: 1.0.0
// guid: 11866630-71dc-417d-b08e-c9e3802eb0fa

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportDestinationStats {
  string destination_id = 1 [(buf.validate.field).string.min_len = 1];
  string destination_type = 2 [(buf.validate.field).string.min_len = 1];
  int64 exported_metrics = 3 [(buf.validate.field).int64.gte = 0];
  int64 failed_exports = 4 [(buf.validate.field).int64.gte = 0];
  double success_rate = 5 [(buf.validate.field).double.gte = 0.0];
  google.protobuf.Timestamp last_export = 6;
}
```

---

### export_destination_update.proto {#export_destination_update}

**Path**: `gcommon/v1/metrics/export_destination_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ExportDestinationUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_destination_update.proto
// version: 1.0.0
// guid: a3b4c5d6-789a-134f-8901-456789012345

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportDestinationUpdate {
  // Destination ID
  string destination_id = 1 [(buf.validate.field).string.min_len = 1];

  // Destination URL
  string url = 2 [(buf.validate.field).string.uri = true];

  // Authentication token
  string auth_token = 3 [(buf.validate.field).string.min_len = 1];

  // Enabled status
  bool enabled = 4;
}
```

---

### export_stats.proto {#export_stats}

**Path**: `gcommon/v1/metrics/export_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `ExportStats`

**Imports** (4):

- `gcommon/v1/metrics/export_destination_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_stats.proto
// version: 1.0.0
// guid: 30936733-3e37-4587-a41e-e036c6532c58

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_destination_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportStats {
  // Total exported metrics
  int64 total_exported_metrics = 1 [(buf.validate.field).int64.gte = 0];

  // Total exported data points
  int64 total_exported_data_points = 2 [(buf.validate.field).int64.gte = 0];

  // Export rate (metrics per second)
  double export_rate_metrics_per_second = 3 [(buf.validate.field).double.gte = 0.0];

  // Failed exports
  int64 failed_exports = 4 [(buf.validate.field).int64.gte = 0];

  // Export success rate
  double export_success_rate = 5 [(buf.validate.field).double.gte = 0.0];

  // Exports by destination
  repeated ExportDestinationStats export_destinations = 6 [(buf.validate.field).repeated.min_items = 1];

  // Last successful export
  google.protobuf.Timestamp last_successful_export = 7;
}
```

---

### export_status.proto {#export_status}

**Path**: `gcommon/v1/metrics/export_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `ExportStatus`

**Imports** (4):

- `gcommon/v1/metrics/exporter_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/export_status.proto
// version: 1.0.0
// guid: 5893a5fc-3748-4c46-a896-6058cdc22a34

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/exporter_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportStatus {
  int64 total_exported_metrics = 1 [(buf.validate.field).int64.gte = 0];
  int64 failed_exports = 2 [(buf.validate.field).int64.gte = 0];
  google.protobuf.Timestamp last_export = 3;
  repeated ExporterStatus exporters = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### exporter_status.proto {#exporter_status}

**Path**: `gcommon/v1/metrics/exporter_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `ExporterStatus`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/exporter_status.proto
// version: 1.0.0
// guid: 852f34ef-6a24-4d4c-a324-3cd1192428e9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExporterStatus {
  string exporter_id = 1 [(buf.validate.field).string.min_len = 1];
  string exporter_type = 2 [(buf.validate.field).string.min_len = 1];
  string status = 3 [(buf.validate.field).string.min_len = 1];
  int64 exported_count = 4 [(buf.validate.field).int64.gte = 0];
  google.protobuf.Timestamp last_export = 5;
}
```

---

### gauge_metric.proto {#gauge_metric}

**Path**: `gcommon/v1/metrics/gauge_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `GaugeMetric`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/gauge_metric.proto
// version: 1.0.0
// guid: 027d4584-4656-45f0-9b73-2493b0ce219b
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GaugeMetric represents a value that can go up and down.
 * Gauges are used for tracking instantaneous values like memory usage,
 * temperature, active connections, or CPU utilization.
 */
message GaugeMetric {
  // Unique identifier for this gauge
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Gauge name/label
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current gauge value (can increase or decrease)
  double value = 3;

  // Timestamp when this value was recorded
  google.protobuf.Timestamp timestamp = 4;

  // Gauge description/help text
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];

  // Key-value labels for this gauge
  map<string, string> labels = 6;

  // Minimum allowed value (constraint)
  double min_value = 7;

  // Maximum allowed value (constraint)
  double max_value = 8;

  // Unit of measurement (e.g., "bytes", "percent", "connections")
  string unit = 9;
}
```

---

### group_by_spec.proto {#group_by_spec}

**Path**: `gcommon/v1/metrics/group_by_spec.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `GroupBySpec`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/group_by_spec.proto
// version: 1.0.0
// guid: 26a4cef4-118d-40a4-b4dc-daaed23b54a4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GroupBySpec {
  // Label keys to group by
  repeated string label_keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Time-based grouping (e.g., by hour, day)
  google.protobuf.Duration time_group = 2;

  // Maximum number of groups to return
  int32 max_groups = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### health_status_entry.proto {#health_status_entry}

**Path**: `gcommon/v1/metrics/health_status_entry.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `HealthStatusEntry`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/health_status_entry.proto
// version: 1.0.0
// guid: 9f50a418-6ad2-49ca-a7bc-f065f79e9a43

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HealthStatusEntry {
  google.protobuf.Timestamp timestamp = 1;
  string health_status = 2 [(buf.validate.field).string.min_len = 1];
  string status_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### histogram_bucket.proto {#histogram_bucket}

**Path**: `gcommon/v1/metrics/histogram_bucket.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `HistogramBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_bucket.proto
// version: 1.0.0
// guid: a9b0c1d2-345a-790f-4567-012345678901

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramBucket {
  // Upper bound for the bucket
  double upper_bound = 1 [(buf.validate.field).double.gte = 0.0];

  // Count of observations in this bucket
  int64 count = 2 [(buf.validate.field).int64.gte = 0];

  // Cumulative count
  int64 cumulative_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### histogram_metric.proto {#histogram_metric}

**Path**: `gcommon/v1/metrics/histogram_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `HistogramMetric`

**Imports** (4):

- `gcommon/v1/metrics/histogram_bucket.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_metric.proto
// version: 1.0.0
// guid: 1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/histogram_bucket.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// HistogramMetric represents a histogram metric with buckets
message HistogramMetric {
  // Metric name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Metric labels
  map<string, string> labels = 2;

  // Histogram buckets
  repeated HistogramBucket buckets = 3;

  // Sample count
  uint64 sample_count = 4;

  // Sample sum
  double sample_sum = 5;

  // Timestamp when the metric was recorded
  google.protobuf.Timestamp timestamp = 6;

  // Help text for the metric
  string help = 7;
}
```

---

### histogram_stats.proto {#histogram_stats}

**Path**: `gcommon/v1/metrics/histogram_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `HistogramStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_stats.proto
// version: 1.0.0
// guid: 7cf98dfc-ae0d-4d1b-95c2-cc76b9e021e1

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramStats {
  // Total number of observations
  uint64 total_count = 1 [(buf.validate.field).uint64.gte = 0];

  // Sum of all observed values
  double total_sum = 2 [(buf.validate.field).double.gte = 0.0];

  // Mean value
  double mean = 3 [(buf.validate.field).double.gte = 0.0];

  // Minimum observed value
  double min_value = 4 [(buf.validate.field).double.gte = 0.0];

  // Maximum observed value
  double max_value = 5 [(buf.validate.field).double.gte = 0.0];

  // Standard deviation (if calculated)
  double std_deviation = 6 [(buf.validate.field).double.gte = 0.0];
}
```

---

### histogram_value.proto {#histogram_value}

**Path**: `gcommon/v1/metrics/histogram_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `HistogramValue`

**Imports** (3):

- `gcommon/v1/metrics/histogram_bucket.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_value.proto
// version: 1.0.0
// guid: eb817cca-e34f-456c-8769-cb7f42cb931c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/histogram_bucket.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramValue {
  // Histogram buckets with their counts
  repeated HistogramBucket buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count of all samples
  uint64 count = 2 [(buf.validate.field).uint64.gte = 0];

  // Sum of all sample values
  double sum = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### label_definition.proto {#label_definition}

**Path**: `gcommon/v1/metrics/label_definition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `LabelDefinition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/label_definition.proto
// version: 1.0.0
// guid: 56dd3a22-ceda-4620-bfb2-c279efc6fab3

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message LabelDefinition {
  // Name of the label
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of what this label represents
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Whether this label is required
  bool required = 3;

  // Allowed values for this label (empty = any value allowed)
  repeated string allowed_values = 4;

  // Pattern for validating label values (regex)
  string validation_pattern = 5;

  // Default value if not specified
  string default_value = 6;
}
```

---

### memory_usage.proto {#memory_usage}

**Path**: `gcommon/v1/metrics/memory_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MemoryUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/memory_usage.proto
// version: 1.0.0
// guid: 7ae5e6f3-835f-4ab4-aa43-31e84d7fc642

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MemoryUsage {
  // Currently used memory (bytes)
  int64 used_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Memory limit (bytes)
  int64 limit_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Usage percentage
  double usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Peak memory usage (bytes)
  int64 peak_bytes = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_aggregation.proto {#metric_aggregation}

**Path**: `gcommon/v1/metrics/metric_aggregation.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricAggregation`

**Imports** (3):

- `gcommon/v1/common/aggregation_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_aggregation.proto
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/aggregation_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// Configuration for metric aggregation operations
message MetricAggregation {
  // Type of aggregation
  gcommon.v1.common.AggregationType type = 1;

  // Time window for aggregation
  int32 window_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Group by fields
  repeated string group_by = 3 [(buf.validate.field).repeated.min_items = 1];

  // Percentiles to calculate (for percentile aggregation)
  repeated double percentiles = 4 [(buf.validate.field).repeated.min_items = 1];

  // Custom aggregation function (for custom type)
  string custom_function = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to include null values in aggregation
  bool include_nulls = 6;

  // Minimum number of samples required
  int32 min_samples = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### metric_bucket.proto {#metric_bucket}

**Path**: `gcommon/v1/metrics/metric_bucket.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_bucket.proto
// version: 1.0.0
// guid: 97e038af-19d9-4d0a-8f3c-0030fd6f2b89

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricBucket represents a histogram bucket with bounds and count.
 */
message MetricBucket {
  // Lower bound inclusive.
  double lower_bound = 1 [(buf.validate.field).double.gte = 0.0];

  // Upper bound exclusive.
  double upper_bound = 2 [(buf.validate.field).double.gte = 0.0];

  // Number of samples in the bucket.
  int64 count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_data.proto {#metric_data}

**Path**: `gcommon/v1/metrics/metric_data.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `MetricData`

**Imports** (5):

- `gcommon/v1/common/metric_type.proto`
- `gcommon/v1/metrics/metric_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_data.proto
// version: 1.0.0
// guid: f9fcef53-3bbb-4860-9b50-b0a96ba93bd0

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metric_type.proto";
import "gcommon/v1/metrics/metric_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricData {
  // Unique identifier for this metric
  string metric_id = 1;

  // Metric name (e.g., "http_requests_total", "cpu_usage_percent")
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of metric (counter, gauge, histogram, etc.)
  gcommon.v1.common.MetricsMetricType type = 3;

  // Human-readable description of the metric
  string description = 4 [ (buf.validate.field).string.max_len = 1000 ];

  // Unit of measurement (e.g., "bytes", "seconds", "requests")
  string unit = 5;

  // Base labels/tags that apply to all values in this metric
  map<string, string> labels = 6;

  // The metric values (can be multiple for time series)
  repeated MetricValue values = 7;

  // When this metric data was collected/created
  google.protobuf.Timestamp created_at = 8 [ (buf.validate.field).required = true ];

  // Source system or component that generated this metric
  string source = 9;

  // Namespace or service this metric belongs to
  string namespace = 10;

  // Version of the metric schema/definition
  string schema_version = 11;
}
```

---

### metric_definition.proto {#metric_definition}

**Path**: `gcommon/v1/metrics/metric_definition.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `MetricDefinition`

**Imports** (8):

- `gcommon/v1/common/metric_type.proto`
- `gcommon/v1/common/metrics_retention_policy_config.proto`
- `gcommon/v1/metrics/export_config.proto`
- `gcommon/v1/metrics/label_definition.proto`
- `gcommon/v1/metrics/metric_type_config.proto`
- `gcommon/v1/metrics/validation_rules.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_definition.proto
// version: 1.0.0
// guid: 4368bdba-c3ff-4d80-bfa1-886b807d497b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metric_type.proto";
import "gcommon/v1/common/metrics_retention_policy_config.proto";
import "gcommon/v1/metrics/export_config.proto";
import "gcommon/v1/metrics/label_definition.proto";
import "gcommon/v1/metrics/metric_type_config.proto";
import "gcommon/v1/metrics/validation_rules.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricDefinition {
  // Unique name for the metric
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of metric (counter, gauge, histogram, etc.)
  gcommon.v1.common.MetricsMetricType type = 2;

  // Human-readable description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Unit of measurement (e.g., "bytes", "requests", "seconds")
  string unit = 4;

  // Labels that this metric supports
  repeated LabelDefinition labels = 5;

  // Metric-specific configuration
  MetricTypeConfig config = 6;

  // Retention policy for this metric
  gcommon.v1.common.MetricsRetentionPolicyConfig retention = 7;

  // Export configuration for this metric
  ExportConfig export_config = 8;

  // Validation rules for metric values
  ValidationRules validation = 9;

  // Tags for metric organization and discovery
  map<string, string> tags = 10;
}
```

---

### metric_filter.proto {#metric_filter}

**Path**: `gcommon/v1/metrics/metric_filter.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_filter.proto
// version: 1.0.0
// guid: 0608db8b-1fd3-4b4b-96f4-0635b55980e8
// Filter for metrics queries

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

// Filter for metrics queries
message MetricFilter {
  // Metric name patterns to include
  repeated string metric_names = 1 [(buf.validate.field).repeated.min_items = 1];

  // Label filters
  map<string, string> labels = 2;

  // Namespace filter
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Time range filter
  int64 start_timestamp = 4;
  int64 end_timestamp = 5;

  // Value threshold filters
  double min_value = 6 [(buf.validate.field).double.gte = 0.0];
  double max_value = 7 [(buf.validate.field).double.gte = 0.0];

  // Include/exclude patterns
  repeated string include_patterns = 8 [(buf.validate.field).repeated.min_items = 1];
  repeated string exclude_patterns = 9 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### metric_health.proto {#metric_health}

**Path**: `gcommon/v1/metrics/metric_health.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `MetricHealth`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_health.proto
// version: 1.0.0
// guid: c0c75431-e37e-4748-8a0d-44a7b15c5e3b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricHealth captures the health status of a metric source or scrape job.
 */
message MetricHealth {
  // Metric identifier or scrape job id
  string target_id = 1 [(buf.validate.field).string.min_len = 1];

  // Health status
  gcommon.v1.common.CommonHealthStatus status = 2;

  // When this health status was checked
  google.protobuf.Timestamp checked_at = 3;

  // Additional message or context
  string message = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### metric_info.proto {#metric_info}

**Path**: `gcommon/v1/metrics/metric_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_info.proto
// version: 1.0.0
// guid: 6e676b06-ec6f-40bb-bc0b-e2ce4484763e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricInfo {
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  string metric_type = 2;
  int64 data_points = 3;
  int64 data_volume_bytes = 4;
  double error_rate = 5;
  google.protobuf.Timestamp last_updated = 6;
}
```

---

### metric_label.proto {#metric_label}

**Path**: `gcommon/v1/metrics/metric_label.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricLabel`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_label.proto
// version: 1.0.0
// guid: 8a39fa3e-a2eb-4df9-9dcf-0c9482a16722

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricLabel represents a single key/value label used for
 * metric identification and filtering.
 */
message MetricLabel {
  // Label key
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Label value
  string value = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### metric_metadata.proto {#metric_metadata}

**Path**: `gcommon/v1/metrics/metric_metadata.proto` **Package**: `gcommon.v1.metrics` **Lines**: 62

**Messages** (1): `MetricMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_metadata.proto
// version: 1.0.0
// guid: 2f161084-caee-424c-a121-9b4907586446
// file: proto/gcommon/v1/metrics/v1/metric_metadata.proto
//
// Message definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricMetadata contains metadata information about a metric.
 */
message MetricMetadata {
  // Unique identifier for the metric
  string metric_id = 1;

  // Human-readable name of the metric
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Description of what this metric measures
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Metric type (counter, gauge, histogram, etc.)
  string type = 4;

  // Units of measurement (e.g., "bytes", "seconds", "requests")
  string unit = 5;

  // Labels associated with this metric
  map<string, string> labels = 6;

  // When this metric was first created
  google.protobuf.Timestamp created_at = 7 [ (buf.validate.field).required = true ];

  // When this metric was last updated
  google.protobuf.Timestamp updated_at = 8;

  // Whether this metric is currently active
  bool active = 9;

  // Data retention policy for this metric
  string retention_policy = 10;

  // Provider that owns this metric
  string provider_id = 11;

  // Namespace this metric belongs to
  string namespace = 12;
}
```

---

### metric_quantile.proto {#metric_quantile}

**Path**: `gcommon/v1/metrics/metric_quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricQuantile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_quantile.proto
// version: 1.0.0
// guid: 9ab5b0e2-0228-47d2-9a48-d714ee6f3d6f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricQuantile represents a quantile value calculated from a
 * distribution of metric samples.
 */
message MetricQuantile {
  // Quantile (0-1, e.g., 0.95 for 95th percentile).
  double quantile = 1 [(buf.validate.field).double.gte = 0.0];

  // Value observed at this quantile.
  double value = 2 [(buf.validate.field).double.gte = 0.0];
}
```

---

### metric_query.proto {#metric_query}

**Path**: `gcommon/v1/metrics/metric_query.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `MetricQuery`

**Imports** (7):

- `gcommon/v1/common/sort_options.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/aggregation_spec.proto`
- `gcommon/v1/metrics/group_by_spec.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_query.proto
// version: 1.0.0
// guid: b48baa90-492c-496f-bcef-674b2fa2d6d4

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/sort_options.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/aggregation_spec.proto";
import "gcommon/v1/metrics/group_by_spec.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricQuery {
  // Unique identifier for this query
  string query_id = 1;

  // Human-readable query name or description
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Query string (PromQL, SQL, or custom query language)
  string query_string = 3;

  // Filter criteria for selecting metrics
  MetricFilter filter = 4;

  // Time range for the query
  gcommon.v1.common.TimeRangeMetrics time_filter = 5;

  // Aggregation operations to apply
  repeated AggregationSpec aggregations = 6;

  // Group by specifications
  repeated GroupBySpec group_by = 7;

  // Sort criteria
  repeated gcommon.v1.common.SortOptions sort_criteria = 8;

  // Maximum number of results to return
  int32 limit = 9;

  // Offset for pagination
  int32 offset = 10;
}
```

---

### metric_result.proto {#metric_result}

**Path**: `gcommon/v1/metrics/metric_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `MetricResult`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_result.proto
// version: 1.0.0
// guid: ad1215aa-2323-42d2-aeeb-b89ff72ab926

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricResult {
  // Index of the metric in the original batch (0-based)
  int32 index = 1 [(buf.validate.field).int32.gte = 0];

  // Success status for this specific metric
  bool success = 2;

  // Error information if this metric failed
  gcommon.v1.common.Error error = 3;

  // Unique ID assigned to the metric (if successful)
  string metric_id = 4 [(buf.validate.field).string.min_len = 1];

  // Timestamp when this metric was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Warnings specific to this metric
  repeated string warnings = 6 [(buf.validate.field).repeated.min_items = 1];

  // Whether this metric was deduplicated
  bool deduplicated = 7;
}
```

---

### metric_sample.proto {#metric_sample}

**Path**: `gcommon/v1/metrics/metric_sample.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `MetricSample`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_sample.proto
// version: 1.0.0
// guid: 7f2e5cc8-7e1b-49d8-b994-556a6d3aa642

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricSample represents a single value for a metric at a point in time.
 */
message MetricSample {
  // Recorded value
  double value = 1 [(buf.validate.field).double.gte = 0.0];

  // Timestamp of the sample
  google.protobuf.Timestamp timestamp = 2;

  // Optional labels associated with this sample
  map<string, string> labels = 3;
}
```

---

### metric_series.proto {#metric_series}

**Path**: `gcommon/v1/metrics/metric_series.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `MetricSeries`

**Imports** (4):

- `gcommon/v1/common/metric_type.proto`
- `gcommon/v1/metrics/metric_value.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_series.proto
// version: 1.0.0
// guid: 642e0c7a-6461-4167-b3e3-746ed9f6e413

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metric_type.proto";
import "gcommon/v1/metrics/metric_value.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricSeries {
  // Metric metadata
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  gcommon.v1.common.MetricsMetricType type = 2;
  map<string, string> labels = 3;

  // Time-ordered series of values
  repeated MetricValue values = 4;

  // Resolution/step between data points
  int64 step_seconds = 5;
}
```

---

### metric_stats.proto {#metric_stats}

**Path**: `gcommon/v1/metrics/metric_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `MetricStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_stats.proto
// version: 1.0.0
// guid: 73f03142-2df5-4e09-a4cd-b067ec1a9fbb

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricStats provides summary statistics for a set of metric values.
 */
message MetricStats {
  // Minimum value observed.
  double min = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum value observed.
  double max = 2 [(buf.validate.field).double.gte = 0.0];

  // Average of all values.
  double average = 3 [(buf.validate.field).double.gte = 0.0];

  // Sum of all values.
  double sum = 4 [(buf.validate.field).double.gte = 0.0];

  // Number of samples.
  int64 count = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_summary.proto {#metric_summary}

**Path**: `gcommon/v1/metrics/metric_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `MetricSummary`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_summary.proto
// version: 1.0.0
// guid: 3bf744e5-01f0-4074-b7b9-5235934749bf

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricSummary {
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  string type = 2;
  int64 data_points = 3;
  int64 data_volume_bytes = 4;
  double error_rate = 5;
  google.protobuf.Timestamp last_updated = 6;
}
```

---

### metric_type_counts.proto {#metric_type_counts}

**Path**: `gcommon/v1/metrics/metric_type_counts.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `MetricTypeCounts`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_type_counts.proto
// version: 1.0.0
// guid: 85755727-af90-4676-b807-fa6c65517840

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricTypeCounts {
  int64 counter_count = 1 [(buf.validate.field).int64.gte = 0];
  int64 gauge_count = 2 [(buf.validate.field).int64.gte = 0];
  int64 histogram_count = 3 [(buf.validate.field).int64.gte = 0];
  int64 summary_count = 4 [(buf.validate.field).int64.gte = 0];
  int64 timer_count = 5 [(buf.validate.field).int64.gte = 0];
  int64 custom_count = 6 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_value.proto {#metric_value}

**Path**: `gcommon/v1/metrics/metric_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `MetricValue`

**Imports** (5):

- `gcommon/v1/metrics/histogram_value.proto`
- `gcommon/v1/metrics/summary_value.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_value.proto
// version: 1.0.0
// guid: 00d0ab12-bd33-48a1-a6d2-ce2262ed6790

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/histogram_value.proto";
import "gcommon/v1/metrics/summary_value.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricValue {
  // Timestamp when this metric value was recorded
  google.protobuf.Timestamp timestamp = 1;

  // The metric value - using oneof to support different value types
  oneof value {
    // Double precision floating point value
    double double_value = 2 [(buf.validate.field).double.gte = 0.0];

    // Integer value (64-bit signed)
    int64 int_value = 3 [(buf.validate.field).int64.gte = 0];

    // String value (for label/text metrics)
    string string_value = 4 [(buf.validate.field).string.min_len = 1];

    // Boolean value
    bool bool_value = 5;

    // Histogram bucket values (for histogram metrics)
    HistogramValue histogram_value = 6;

    // Summary quantile values (for summary metrics)
    SummaryValue summary_value = 7;
  }

  // Optional labels/tags associated with this specific value
  map<string, string> labels = 8;

  // Optional sample count (for aggregated values)
  uint64 sample_count = 9;
}
```

---

### metrics_health_info.proto {#metrics_health_info}

**Path**: `gcommon/v1/metrics/metrics_health_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `MetricsHealthInfo`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metrics_health_info.proto
// version: 1.0.0
// guid: e7ab1793-c874-4b03-ad41-59257c2f7cca

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsHealthInfo {
  gcommon.v1.common.CommonHealthStatus overall_status = 1;
  repeated string health_checks = 2 [(buf.validate.field).repeated.min_items = 1];
  repeated string warnings = 3 [(buf.validate.field).repeated.min_items = 1];
  google.protobuf.Timestamp last_check = 4;
}
```

---

### metrics_summary.proto {#metrics_summary}

**Path**: `gcommon/v1/metrics/metrics_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `MetricsSummary`

**Imports** (8):

- `gcommon/v1/common/metrics_error_stats.proto`
- `gcommon/v1/common/metrics_retention_info.proto`
- `gcommon/v1/metrics/export_status.proto`
- `gcommon/v1/metrics/metric_type_counts.proto`
- `gcommon/v1/metrics/performance_stats.proto`
- `gcommon/v1/metrics/top_metrics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metrics_summary.proto
// version: 1.0.0
// guid: df4c181e-98bb-488d-8052-2238af4f3a5c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_error_stats.proto";
import "gcommon/v1/common/metrics_retention_info.proto";
import "gcommon/v1/metrics/export_status.proto";
import "gcommon/v1/metrics/metric_type_counts.proto";
import "gcommon/v1/metrics/performance_stats.proto";
import "gcommon/v1/metrics/top_metrics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsSummary {
  // Total number of unique metrics
  int64 total_metrics = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of data points
  int64 total_data_points = 2 [(buf.validate.field).int64.gte = 0];

  // Total data volume (bytes)
  int64 total_data_volume_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Metrics by type
  MetricTypeCounts type_counts = 4;

  // Performance statistics
  MetricsPerformanceStats performance = 5;

  // Error statistics
  gcommon.v1.common.MetricsErrorStats errors = 6;

  // Top metrics by various criteria
  TopMetrics top_metrics = 7;

  // Retention information
  gcommon.v1.common.MetricsRetentionInfo retention = 8;

  // Export status information
  ExportStatus export_status = 9;
}
```

---

### network_usage.proto {#network_usage}

**Path**: `gcommon/v1/metrics/network_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `NetworkUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/network_usage.proto
// version: 1.0.0
// guid: b8df322e-99e1-49d7-97b0-fead8deb1998

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message NetworkUsage {
  // Bytes received per second
  int64 bytes_in_per_second = 1 [(buf.validate.field).int64.gte = 0];

  // Bytes sent per second
  int64 bytes_out_per_second = 2 [(buf.validate.field).int64.gte = 0];

  // Packets received per second
  int64 packets_in_per_second = 3 [(buf.validate.field).int64.gte = 0];

  // Packets sent per second
  int64 packets_out_per_second = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### open_telemetry_settings.proto {#open_telemetry_settings}

**Path**: `gcommon/v1/metrics/open_telemetry_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `OpenTelemetrySettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/open_telemetry_settings.proto
// version: 1.0.0
// guid: bc525cde-e766-4d2a-9ba9-d6383bdf2f6f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message OpenTelemetrySettings {
  // OTLP endpoint
  string endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to use TLS
  bool use_tls = 2;

  // Headers to include with requests
  map<string, string> headers = 3;

  // Resource attributes
  map<string, string> resource_attributes = 4;

  // Export timeout
  string timeout = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### open_telemetry_settings_update.proto {#open_telemetry_settings_update}

**Path**: `gcommon/v1/metrics/open_telemetry_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `OpenTelemetrySettingsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/open_telemetry_settings_update.proto
// version: 1.0.0
// guid: 191fb873-a4f2-418a-803f-6033ebcd28f4

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * OpenTelemetrySettingsUpdate contains updates to OpenTelemetry settings.
 */
message OpenTelemetrySettingsUpdate {
  // Updated endpoint
  string endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Updated TLS setting
  bool use_tls = 2;

  // Header updates
  map<string, string> header_updates = 3;

  // Headers to remove
  repeated string header_removes = 4 [(buf.validate.field).repeated.min_items = 1];

  // Resource attribute updates
  map<string, string> resource_attribute_updates = 5;

  // Resource attributes to remove
  repeated string resource_attribute_removes = 6 [(buf.validate.field).repeated.min_items = 1];

  // Updated timeout
  string timeout = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### output_options.proto {#output_options}

**Path**: `gcommon/v1/metrics/output_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `OutputOptions`

**Imports** (4):

- `gcommon/v1/common/numeric_format.proto`
- `gcommon/v1/common/response_compression.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/output_options.proto
// version: 1.0.0
// guid: 8f7b7904-aab3-4d73-a893-b9ea03d7b75a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/numeric_format.proto";
import "gcommon/v1/common/response_compression.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message OutputOptions {
  // Format for numeric values
  gcommon.v1.common.NumericFormat numeric_format = 1;

  // Whether to include timestamps
  bool include_timestamps = 2;

  // Whether to include labels
  bool include_labels = 3;

  // Compression for large responses
  gcommon.v1.common.ResponseCompression compression = 4;

  // Whether to flatten nested structures
  bool flatten_response = 5;

  // Time zone for timestamp formatting
  string timezone = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### pagination_info.proto {#pagination_info}

**Path**: `gcommon/v1/metrics/pagination_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 43

**Messages** (1): `MetricsPaginationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/pagination_info.proto
// version: 1.0.0
// guid: f1e2d3c4-b5a6-9c8d-7e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * PaginationInfo contains information about paginated results.
 */
message MetricsPaginationInfo {
  // Current page number (1-based)
  uint32 page = 1 [(buf.validate.field).uint32.gte = 0];

  // Number of items per page
  uint32 page_size = 2 [(buf.validate.field).uint32.gte = 0];

  // Total number of items across all pages
  uint64 total_items = 3 [(buf.validate.field).uint64.gte = 0];

  // Total number of pages
  uint32 total_pages = 4 [(buf.validate.field).uint32.gte = 0];

  // Whether there is a next page
  bool has_next = 5;

  // Whether there is a previous page
  bool has_previous = 6;

  // Cursor for cursor-based pagination (optional)
  string next_cursor = 7 [(buf.validate.field).string.min_len = 1];

  // Cursor for previous page (optional)
  string previous_cursor = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### percentile_measurement.proto {#percentile_measurement}

**Path**: `gcommon/v1/metrics/percentile_measurement.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `PercentileMeasurement`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/percentile_measurement.proto
// version: 1.0.0
// guid: 48293be8-c475-44ee-b41d-c428b059063a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PercentileMeasurement {
  // Percentile value (e.g., 50.0 for median, 95.0 for 95th percentile)
  double percentile = 1 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Duration value at this percentile
  google.protobuf.Duration duration = 2;

  // Number of samples at or below this percentile
  int64 sample_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### performance_data_point.proto {#performance_data_point}

**Path**: `gcommon/v1/metrics/performance_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `PerformanceDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/performance_data_point.proto
// version: 1.0.0
// guid: ffe66544-9090-4908-b499-8e6c339440a6

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PerformanceDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  double ops_per_second = 2 [(buf.validate.field).double.gte = 0.0];
  double latency_ms = 3 [(buf.validate.field).double.gte = 0.0];
  double throughput_bytes_per_second = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### performance_stats.proto {#performance_stats}

**Path**: `gcommon/v1/metrics/performance_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 61

**Messages** (1): `MetricsPerformanceStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/performance_stats.proto
// version: 1.0.0
// guid: b3c4d5e6-f7a8-9b0c-1d2e-3f4a5b6c7d8e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * PerformanceStats contains performance metrics for provider operations.
 */
message MetricsPerformanceStats {
  // Average response time in milliseconds
  double avg_response_time_ms = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum response time in milliseconds
  double max_response_time_ms = 2 [(buf.validate.field).double.gte = 0.0];

  // Minimum response time in milliseconds
  double min_response_time_ms = 3 [(buf.validate.field).double.gte = 0.0];

  // 95th percentile response time in milliseconds
  double p95_response_time_ms = 4 [(buf.validate.field).double.gte = 0.0];

  // 99th percentile response time in milliseconds
  double p99_response_time_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // Requests per second
  double requests_per_second = 6 [(buf.validate.field).double.gte = 0.0];

  // Total number of requests processed
  uint64 total_requests = 7 [(buf.validate.field).uint64.gte = 0];

  // Number of successful requests
  uint64 successful_requests = 8 [(buf.validate.field).uint64.gte = 0];

  // Number of failed requests
  uint64 failed_requests = 9 [(buf.validate.field).uint64.gte = 0];

  // Success rate (0.0 to 1.0)
  double success_rate = 10 [(buf.validate.field).double.gte = 0.0];

  // CPU utilization percentage (0.0 to 100.0)
  double cpu_utilization = 11 [(buf.validate.field).double.gte = 0.0];

  // Memory utilization percentage (0.0 to 100.0)
  double memory_utilization = 12 [(buf.validate.field).double.gte = 0.0];

  // Network I/O in bytes per second
  double network_io_bytes_per_sec = 13 [(buf.validate.field).double.gte = 0.0];

  // Disk I/O in bytes per second
  double disk_io_bytes_per_sec = 14 [(buf.validate.field).double.gte = 0.0];
}
```

---

### performance_trend.proto {#performance_trend}

**Path**: `gcommon/v1/metrics/performance_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 18

**Messages** (1): `PerformanceTrend`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/performance_trend.proto
// version: 1.0.1
// guid: f45758c7-cea2-4efa-92f7-88144b8a8d03

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PerformanceTrend {
  string latency_trend = 1; // "improving", "degrading", "stable"
  string throughput_trend = 2; // "increasing", "decreasing", "stable"
  double trend_confidence = 3; // 0.0 to 1.0
}
```

---

### prometheus_settings.proto {#prometheus_settings}

**Path**: `gcommon/v1/metrics/prometheus_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `PrometheusSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/prometheus_settings.proto
// version: 1.0.0
// guid: 6ebbab41-b5f1-4b3c-beb2-5625c0756224

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message PrometheusSettings {
  // Registry to use
  string registry = 1;

  // Whether to enable push gateway
  bool enable_push_gateway = 2;

  // Push gateway URL
  string push_gateway_url = 3 [ (buf.validate.field).string.uri = true ];

  // Job name for push gateway
  string job_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Instance name
  string instance = 5;

  // Additional labels
  map<string, string> labels = 6;
}
```

---

### prometheus_settings_update.proto {#prometheus_settings_update}

**Path**: `gcommon/v1/metrics/prometheus_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `PrometheusSettingsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/prometheus_settings_update.proto
// version: 1.0.0
// guid: 438c00d1-b391-4ced-b9d0-4ddbd6202b8d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * PrometheusSettingsUpdate contains updates to Prometheus-specific settings.
 */
message PrometheusSettingsUpdate {
  // Updated push gateway URL
  string push_gateway_url = 1 [ (buf.validate.field).string.uri = true ];

  // Updated job name
  string job_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated instance name
  string instance = 3;

  // Label updates
  map<string, string> label_updates = 4;

  // Labels to remove
  repeated string label_removes = 5;
}
```

---

### provider_endpoints.proto {#provider_endpoints}

**Path**: `gcommon/v1/metrics/provider_endpoints.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `ProviderEndpoints`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_endpoints.proto
// version: 1.0.0
// guid: f15d26e3-bb0f-47d8-a4f2-20cbebab5f75

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderEndpoints {
  // Main service endpoint
  string service_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Metrics endpoint (for scraping)
  string metrics_endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Health check endpoint
  string health_endpoint = 3 [(buf.validate.field).string.min_len = 1];

  // Admin/management endpoint
  string admin_endpoint = 4 [(buf.validate.field).string.min_len = 1];

  // Additional endpoints
  map<string, string> additional_endpoints = 5;
}
```

---

### provider_filter.proto {#provider_filter}

**Path**: `gcommon/v1/metrics/provider_filter.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `ProviderFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_filter.proto
// version: 1.0.0
// guid: ccf0f7e8-2de8-458d-b403-22b712773c55

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderFilter {
  // Filter by provider type
  repeated string provider_types = 1 [(buf.validate.field).repeated.min_items = 1];

  // Filter by provider state
  repeated string states = 2 [(buf.validate.field).repeated.min_items = 1];

  // Filter by tags
  map<string, string> tags = 3;

  // Filter by name pattern (regex)
  string name_pattern = 4 [(buf.validate.field).string.min_len = 1];

  // Filter by health status
  repeated string health_statuses = 5 [(buf.validate.field).repeated.min_items = 1];

  // Filter providers created after this time
  string created_after = 6 [(buf.validate.field).string.min_len = 1];

  // Filter providers created before this time
  string created_before = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### provider_info.proto {#provider_info}

**Path**: `gcommon/v1/metrics/provider_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 59

**Messages** (1): `ProviderInfo`

**Imports** (4):

- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_info.proto
// version: 1.0.0
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ProviderInfo contains information about a metrics provider.
 */
message ProviderInfo {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name of the provider
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Provider type (e.g., "prometheus", "datadog", "custom")
  string type = 3;

  // Current status of the provider
  string status = 4;

  // Detailed status information
  ProviderStatus detailed_status = 5;

  // Configuration settings
  map<string, string> config = 6;

  // Version of the provider
  string version = 7;

  // When this provider was created
  google.protobuf.Timestamp created_at = 8 [ (buf.validate.field).required = true ];

  // When this provider was last updated
  google.protobuf.Timestamp last_updated = 9;

  // Whether this provider is enabled
  bool enabled = 10;

  // Tags associated with this provider
  repeated string tags = 11;

  // Description of the provider
  string description = 12 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### provider_settings.proto {#provider_settings}

**Path**: `gcommon/v1/metrics/provider_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ProviderSettings`

**Imports** (4):

- `gcommon/v1/metrics/open_telemetry_settings.proto`
- `gcommon/v1/metrics/prometheus_settings.proto`
- `gcommon/v1/metrics/stats_d_settings.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_settings.proto
// version: 1.0.1
// guid: bfca385c-e614-41b8-a78b-1d073e6e8a3d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/open_telemetry_settings.proto";
import "gcommon/v1/metrics/prometheus_settings.proto";
import "gcommon/v1/metrics/stats_d_settings.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderSettings {
  // Prometheus-specific settings
  PrometheusSettings prometheus = 1;

  // OpenTelemetry-specific settings
  OpenTelemetrySettings opentelemetry = 2;

  // StatsD-specific settings
  StatsDSettings statsd = 3;

  // Custom provider settings
  map<string, string> custom = 4;
}
```

---

### provider_settings_update.proto {#provider_settings_update}

**Path**: `gcommon/v1/metrics/provider_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `ProviderSettingsUpdate`

**Imports** (4):

- `gcommon/v1/metrics/open_telemetry_settings_update.proto`
- `gcommon/v1/metrics/prometheus_settings_update.proto`
- `gcommon/v1/metrics/stats_d_settings_update.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_settings_update.proto
// version: 1.0.1
// guid: d2e3f4a5-678d-023c-7890-345678901234

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/open_telemetry_settings_update.proto";
import "gcommon/v1/metrics/prometheus_settings_update.proto";
import "gcommon/v1/metrics/stats_d_settings_update.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderSettingsUpdate {
  // Prometheus settings update
  PrometheusSettingsUpdate prometheus = 1;

  // OpenTelemetry settings update
  OpenTelemetrySettingsUpdate opentelemetry = 2;

  // StatsD settings update
  StatsDSettingsUpdate statsd = 3;
}
```

---

### provider_statistics.proto {#provider_statistics}

**Path**: `gcommon/v1/metrics/provider_statistics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 56

**Messages** (1): `ProviderStatistics`

**Imports** (12):

- `gcommon/v1/common/metrics_error_stats.proto`
- `gcommon/v1/metrics/configuration_summary.proto`
- `gcommon/v1/metrics/data_volume_stats.proto`
- `gcommon/v1/metrics/export_stats.proto`
- `gcommon/v1/metrics/health_status_entry.proto`
- `gcommon/v1/metrics/performance_stats.proto`
- `gcommon/v1/metrics/provider_info.proto`
- `gcommon/v1/metrics/resource_usage_stats.proto`
- `gcommon/v1/metrics/top_metrics.proto`
- `gcommon/v1/metrics/trend_analysis.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_statistics.proto
// version: 1.0.0
// guid: 65d32fe6-818b-4b23-a785-3a059bf52535

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_error_stats.proto";
import "gcommon/v1/metrics/configuration_summary.proto";
import "gcommon/v1/metrics/data_volume_stats.proto";
import "gcommon/v1/metrics/export_stats.proto";
import "gcommon/v1/metrics/health_status_entry.proto";
import "gcommon/v1/metrics/performance_stats.proto";
import "gcommon/v1/metrics/provider_info.proto";
import "gcommon/v1/metrics/resource_usage_stats.proto";
import "gcommon/v1/metrics/top_metrics.proto";
import "gcommon/v1/metrics/trend_analysis.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderStatistics {
  // Basic provider information
  ProviderInfo provider_info = 1;

  // Performance statistics
  MetricsPerformanceStats performance = 2;

  // Resource usage statistics
  ResourceUsageStats resource_usage = 3;

  // Error statistics
  gcommon.v1.common.MetricsErrorStats errors = 4;

  // Data volume statistics
  DataVolumeStats data_volume = 5;

  // Export statistics
  ExportStats exports = 6;

  // Health status history
  repeated HealthStatusEntry health_history = 7 [(buf.validate.field).repeated.min_items = 1];

  // Configuration summary
  ConfigurationSummary config = 8;

  // Top metrics
  TopMetrics top_metrics = 9;

  // Trend analysis
  TrendAnalysis trends = 10;
}
```

---

### provider_stats.proto {#provider_stats}

**Path**: `gcommon/v1/metrics/provider_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ProviderStats`

**Imports** (3):

- `gcommon/v1/metrics/resource_usage.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_stats.proto
// version: 1.0.0
// guid: 50e90cb9-edcb-4e84-b110-1e41adfa7b50

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_usage.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderStats {
  // Number of metrics managed
  int64 metrics_count = 1 [(buf.validate.field).int64.gte = 0];

  // Number of data points
  int64 data_points_count = 2 [(buf.validate.field).int64.gte = 0];

  // Data volume (bytes)
  int64 data_volume_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Operations per second
  double operations_per_second = 4 [(buf.validate.field).double.gte = 0.0];

  // Error rate
  double error_rate = 5 [(buf.validate.field).double.gte = 0.0];

  // Resource usage
  ResourceUsage resource_usage = 6;
}
```

---

### provider_status.proto {#provider_status}

**Path**: `gcommon/v1/metrics/provider_status.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ProviderStatus`

**Imports** (4):

- `gcommon/v1/common/provider_state.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/provider_status.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174023

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/provider_state.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * Status of a metrics provider.
 */
message ProviderStatus {
  // Current state
  gcommon.v1.common.ProviderState state = 1;

  // Status message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Health check status
  string health = 3 [(buf.validate.field).string.min_len = 1];

  // Last update time
  google.protobuf.Timestamp last_updated = 4;

  // Provider version
  string version = 5 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### provider_summary.proto {#provider_summary}

**Path**: `gcommon/v1/metrics/provider_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 65

**Messages** (1): `ProviderSummary`

**Imports** (4):

- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_summary.proto
// version: 1.0.0
// guid: d5e6f7a8-b9c0-1d2e-3f4a-5b6c7d8e9f0a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ProviderSummary contains summary information about a metrics provider.
 */
message ProviderSummary {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name of the provider
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Provider type (e.g., "prometheus", "datadog", "custom")
  string provider_type = 3;

  // Current status of the provider
  ProviderStatus status = 4;

  // Number of metrics currently managed by this provider
  uint64 metric_count = 5;

  // Number of active data points
  uint64 active_data_points = 6;

  // Storage size used by this provider (in bytes)
  uint64 storage_size_bytes = 7;

  // When this provider was registered
  google.protobuf.Timestamp registered_at = 8;

  // When this provider was last updated
  google.protobuf.Timestamp last_updated = 9;

  // Whether this provider is currently enabled
  bool enabled = 10;

  // Performance score (0.0 to 100.0)
  double performance_score = 11;

  // Health score (0.0 to 100.0)
  double health_score = 12;

  // Tags associated with this provider
  repeated string tags = 13;

  // Brief description of the provider
  string description = 14 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### quantile.proto {#quantile}

**Path**: `gcommon/v1/metrics/quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `Quantile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/quantile.proto
// version: 1.0.0
// guid: 9aa0660a-bf89-48a8-856e-cbc136a634b9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message Quantile {
  // Quantile value (0.0 to 1.0, e.g., 0.95 for 95th percentile)
  double quantile = 1 [(buf.validate.field).double.gte = 0.0];

  // Value at this quantile
  double value = 2 [(buf.validate.field).double.gte = 0.0];
}
```

---

### query_output_options.proto {#query_output_options}

**Path**: `gcommon/v1/metrics/query_output_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `QueryOutputOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_output_options.proto
// version: 1.0.0
// guid: b6da5ff6-e156-4256-b53f-bebc54538f99

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryOutputOptions {
  // Whether to include timestamps in results
  bool include_timestamps = 1;

  // Whether to include label information
  bool include_labels = 2;

  // Whether to compress/optimize output for network transfer
  bool compress_output = 3;

  // Maximum precision for numeric values (decimal places)
  int32 numeric_precision = 4 [(buf.validate.field).int32.gte = 0];

  // Whether to include statistics about the query execution
  bool include_statistics = 5;
}
```

---

### query_plan.proto {#query_plan}

**Path**: `gcommon/v1/metrics/query_plan.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `QueryPlan`

**Imports** (4):

- `gcommon/v1/metrics/query_step.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_plan.proto
// version: 1.0.0
// guid: 6acf658c-3ed4-4910-a68b-dc33ce5d816b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/query_step.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryPlan {
  // Query that this plan is for
  string query_id = 1 [(buf.validate.field).string.min_len = 1];

  // Estimated execution time
  google.protobuf.Duration estimated_duration = 2;

  // Estimated number of data points to process
  int64 estimated_data_points = 3 [(buf.validate.field).int64.gte = 0];

  // Execution steps
  repeated QueryStep steps = 4 [(buf.validate.field).repeated.min_items = 1];

  // Storage backends that will be queried
  repeated string storage_backends = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### query_statistics.proto {#query_statistics}

**Path**: `gcommon/v1/metrics/query_statistics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `QueryStatistics`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_statistics.proto
// version: 1.0.0
// guid: 65eeb9f0-7dbe-4fd5-92e0-622eb37743ee

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryStatistics {
  // Total execution time
  google.protobuf.Duration execution_time = 1;

  // Number of data points processed
  int64 data_points_processed = 2 [(buf.validate.field).int64.gte = 0];

  // Number of metrics examined
  int64 metrics_examined = 3 [(buf.validate.field).int64.gte = 0];

  // Number of series returned
  int64 series_returned = 4 [(buf.validate.field).int64.gte = 0];

  // Memory used during query execution (bytes)
  int64 memory_used_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Storage backends queried
  repeated string storage_backends_used = 6 [(buf.validate.field).repeated.min_items = 1];

  // Cache hit rate (0.0 to 1.0)
  double cache_hit_rate = 7 [(buf.validate.field).double.gte = 0.0];

  // When the query was executed
  google.protobuf.Timestamp query_time = 8;
}
```

---

### query_stats.proto {#query_stats}

**Path**: `gcommon/v1/metrics/query_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricsQueryStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_stats.proto
// version: 1.0.0
// guid: f8a9b0c1-234f-689e-3456-901234567890

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsQueryStats {
  // Total queries executed
  int64 total_queries = 1 [(buf.validate.field).int64.gte = 0];

  // Average execution time in milliseconds
  double avg_execution_time_ms = 2 [(buf.validate.field).double.gte = 0.0];

  // Number of failed queries
  int64 failed_queries = 3 [(buf.validate.field).int64.gte = 0];

  // Cache hit rate
  double cache_hit_rate = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### query_step.proto {#query_step}

**Path**: `gcommon/v1/metrics/query_step.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `QueryStep`

**Imports** (4):

- `gcommon/v1/common/query_operation.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_step.proto
// version: 1.0.0
// guid: 93f6a8f4-e54a-4531-86a5-bb96d2bc3bf4

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/query_operation.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryStep {
  // Step identifier
  string step_id = 1;

  // Operation to perform in this step
  gcommon.v1.common.QueryOperation operation = 2;

  // Description of the operation
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Estimated cost/time for this step
  google.protobuf.Duration estimated_duration = 4;

  // Input from previous steps
  repeated string input_step_ids = 5;
}
```

---

### recording_stats.proto {#recording_stats}

**Path**: `gcommon/v1/metrics/recording_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `RecordingStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/recording_stats.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174028

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordingStats contains performance information about recording operations.
 */
message RecordingStats {
  // Time taken to process the request (milliseconds)
  int64 processing_time_ms = 1 [(buf.validate.field).int64.gte = 0];

  // Number of retries attempted
  int32 retry_count = 2 [(buf.validate.field).int32.gte = 0];

  // Whether data was successfully buffered
  bool buffered = 3;

  // Whether data was successfully persisted
  bool persisted = 4;
}
```

---

### registration_options.proto {#registration_options}

**Path**: `gcommon/v1/metrics/registration_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `RegistrationOptions`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_options.proto
// version: 1.0.1
// guid: c171bdc3-4ccb-4042-b2f0-c6c6b89ee6f2

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegistrationOptions {
  // Whether to validate the definition before registration
  bool validate_definition = 1;

  // Whether to perform a dry run (validation only)
  bool dry_run = 2;

  // Whether to create indices for efficient querying
  bool create_indices = 3;

  // Whether to enable real-time alerts for this metric
  bool enable_alerting = 4;
}
```

---

### registration_result.proto {#registration_result}

**Path**: `gcommon/v1/metrics/registration_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `RegistrationResult`

**Imports** (4):

- `gcommon/v1/common/registration_action.proto`
- `gcommon/v1/metrics/schema_change.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_result.proto
// version: 1.0.0
// guid: ed484bf7-ea0c-42a0-8479-e2c6a9d205eb

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/registration_action.proto";
import "gcommon/v1/metrics/schema_change.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegistrationResult {
  // Whether a new metric was created or existing one updated
  gcommon.v1.common.RegistrationAction action = 1;

  // Indices that were created for the metric
  repeated string created_indices = 2 [(buf.validate.field).repeated.min_items = 1];

  // Alert rules that were created (if alerting was enabled)
  repeated string created_alerts = 3 [(buf.validate.field).repeated.min_items = 1];

  // Export configurations that were set up
  repeated string configured_exports = 4 [(buf.validate.field).repeated.min_items = 1];

  // Retention policies that were applied
  repeated string applied_retention_policies = 5 [(buf.validate.field).repeated.min_items = 1];

  // Schema changes that were made
  repeated SchemaChange schema_changes = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### registration_validation.proto {#registration_validation}

**Path**: `gcommon/v1/metrics/registration_validation.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `RegistrationValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_validation.proto
// version: 1.0.0
// guid: eb100fbc-634b-48da-8ca6-51f2695247d3

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RegistrationValidation {
  // Whether the metric definition is valid
  bool valid = 1;

  // Validation errors (if any)
  repeated string errors = 2 [(buf.validate.field).repeated.min_items = 1];

  // Validation warnings (if any)
  repeated string warnings = 3 [(buf.validate.field).repeated.min_items = 1];

  // Schema version used for validation
  string schema_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Suggestions for improving the metric definition
  repeated string suggestions = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### resource_allocations.proto {#resource_allocations}

**Path**: `gcommon/v1/metrics/resource_allocations.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ResourceAllocations`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_allocations.proto
// version: 1.0.0
// guid: 7b4880a1-d53a-4cf8-93db-907b2bd67f3b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceAllocations {
  // Allocated memory (bytes)
  int64 allocated_memory_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Allocated CPU (percentage)
  double allocated_cpu_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Allocated disk space (bytes)
  int64 allocated_disk_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Network ports allocated
  repeated int32 allocated_ports = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### resource_data_point.proto {#resource_data_point}

**Path**: `gcommon/v1/metrics/resource_data_point.proto` **Package**: `gcommon.v1.metrics` **Lines**: 23

**Messages** (1): `ResourceDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_data_point.proto
// version: 1.0.0
// guid: aada674f-48f3-4943-b35d-4866b7b17399

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  double memory_usage_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
  double cpu_usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
  double disk_usage_percent = 4 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
  int64 network_bytes_per_second = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_limits.proto {#resource_limits}

**Path**: `gcommon/v1/metrics/resource_limits.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `MetricsResourceLimits`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_limits.proto
// version: 1.0.0
// guid: bb6325e2-4ef3-438c-8593-00a3c550b17a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsResourceLimits {
  // Maximum memory usage (bytes)
  int64 max_memory_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Maximum CPU usage (percentage)
  double max_cpu_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Maximum disk usage (bytes)
  int64 max_disk_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum number of metrics
  int64 max_metrics = 4 [(buf.validate.field).int64.gte = 0];

  // Maximum data points per metric
  int64 max_data_points_per_metric = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_limits_summary.proto {#resource_limits_summary}

**Path**: `gcommon/v1/metrics/resource_limits_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `ResourceLimitsSummary`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_limits_summary.proto
// version: 1.0.0
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ResourceLimitsSummary contains information about resource limits.
 */
message ResourceLimitsSummary {
  // Memory limit in bytes
  int64 memory_limit_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // CPU limit as percentage (0.0 to 100.0)
  double cpu_limit_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Disk limit in bytes
  int64 disk_limit_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Network bandwidth limit in bytes per second
  int64 network_limit_bytes_per_sec = 4 [(buf.validate.field).int64.gte = 0];

  // Current memory usage in bytes
  int64 memory_used_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Current CPU usage as percentage (0.0 to 100.0)
  double cpu_used_percent = 6 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Current disk usage in bytes
  int64 disk_used_bytes = 7 [(buf.validate.field).int64.gte = 0];

  // Current network usage in bytes per second
  int64 network_used_bytes_per_sec = 8 [(buf.validate.field).int64.gte = 0];

  // Whether limits are enforced
  bool limits_enforced = 9;

  // Number of limit violations in the last hour
  uint32 violations_count = 10 [(buf.validate.field).uint32.gte = 0];
}
```

---

### resource_limits_update.proto {#resource_limits_update}

**Path**: `gcommon/v1/metrics/resource_limits_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `ResourceLimitsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_limits_update.proto
// version: 1.0.0
// guid: cc6398cf-50af-461a-a6de-d00d8a2e61d9

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ResourceLimitsUpdate contains updates to resource limits.
 */
message ResourceLimitsUpdate {
  // Updated memory limit
  int64 max_memory_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Updated CPU limit
  double max_cpu_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Updated disk limit
  int64 max_disk_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Updated metrics limit
  int64 max_metrics = 4 [(buf.validate.field).int64.gte = 0];

  // Updated data points per metric limit
  int64 max_data_points_per_metric = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_usage.proto {#resource_usage}

**Path**: `gcommon/v1/metrics/resource_usage.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ResourceUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_usage.proto
// version: 1.0.0
// guid: 9feb7ea0-10ae-4507-9d2e-265744c25ac7

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceUsage {
  // Current memory usage (bytes)
  int64 memory_used_bytes = 1 [(buf.validate.field).int64.gte = 0];

  // Current CPU usage (percentage)
  double cpu_used_percent = 2 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Current disk usage (bytes)
  int64 disk_used_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Network bandwidth usage (bytes/sec)
  int64 network_bandwidth_bytes_per_sec = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### resource_usage_stats.proto {#resource_usage_stats}

**Path**: `gcommon/v1/metrics/resource_usage_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ResourceUsageStats`

**Imports** (7):

- `gcommon/v1/metrics/cpu_usage.proto`
- `gcommon/v1/metrics/disk_usage.proto`
- `gcommon/v1/metrics/memory_usage.proto`
- `gcommon/v1/metrics/network_usage.proto`
- `gcommon/v1/metrics/resource_data_point.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_usage_stats.proto
// version: 1.0.0
// guid: 18e38b17-8e74-45c9-8f0e-1b1ce6da1c19

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/cpu_usage.proto";
import "gcommon/v1/metrics/disk_usage.proto";
import "gcommon/v1/metrics/memory_usage.proto";
import "gcommon/v1/metrics/network_usage.proto";
import "gcommon/v1/metrics/resource_data_point.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceUsageStats {
  // Current memory usage
  MemoryUsage memory = 1;

  // Current CPU usage
  CPUUsage cpu = 2;

  // Current disk usage
  DiskUsage disk = 3;

  // Network usage
  NetworkUsage network = 4;

  // Time-series resource usage data
  repeated ResourceDataPoint resource_timeseries = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### resource_usage_trend.proto {#resource_usage_trend}

**Path**: `gcommon/v1/metrics/resource_usage_trend.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `ResourceUsageTrend`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/resource_usage_trend.proto
// version: 1.0.0
// guid: 36fe825a-fefc-4c27-ab0f-5f371bfab0b8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ResourceUsageTrend {
  string memory_trend = 1; // "increasing", "decreasing", "stable"
  string cpu_trend = 2; // "increasing", "decreasing", "stable"
  string disk_trend = 3; // "increasing", "decreasing", "stable"
  double trend_confidence = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### schema_change.proto {#schema_change}

**Path**: `gcommon/v1/metrics/schema_change.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `SchemaChange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/schema_change.proto
// version: 1.0.0
// guid: 57c8fdff-d924-42a5-89a6-6a843c28e13e

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SchemaChange {
  // Type of change made
  string change_type = 1;

  // Description of the change
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Whether this change is backward compatible
  bool backward_compatible = 3;

  // Migration steps required (if any)
  repeated string migration_steps = 4;
}
```

---

### scrape_job.proto {#scrape_job}

**Path**: `gcommon/v1/metrics/scrape_job.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ScrapeJob`

**Imports** (4):

- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/scrape_job.proto
// version: 1.1.0
// guid: 4c4b2cc6-1c94-4bd4-9a40-e1e36e1f9d02

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ScrapeJob represents a scheduled scraping task for metrics collection.
 */
message ScrapeJob {
  // Unique identifier for the scrape job
  string job_id = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration used for the scrape
  ScrapeConfig config = 2;

  // Whether the job is currently active
  bool active = 3;

  // Timestamp of the last successful scrape
  google.protobuf.Timestamp last_scrape_time = 4;

  // Timestamp of the next scheduled scrape
  google.protobuf.Timestamp next_scrape_time = 5;
}
```

---

### scrape_target.proto {#scrape_target}

**Path**: `gcommon/v1/metrics/scrape_target.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `ScrapeTarget`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/scrape_target.proto
// version: 1.0.0
// guid: bc47b323-f2ec-45a1-9eb1-a02cee44f29d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ScrapeTarget describes a target endpoint to scrape metrics from.
 */
message ScrapeTarget {
  // Target URL
  string url = 1 [(buf.validate.field).string.uri = true];

  // Optional labels to associate with this target
  map<string, string> labels = 2;
}
```

---

### secondary_sort_field.proto {#secondary_sort_field}

**Path**: `gcommon/v1/metrics/secondary_sort_field.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `SecondarySortField`

**Imports** (3):

- `gcommon/v1/common/sort_direction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/secondary_sort_field.proto
// version: 1.0.0
// guid: 136c5347-b8ae-4bd7-bf04-163e6e550f8a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/sort_direction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SecondarySortField {
  string field = 1 [(buf.validate.field).string.min_len = 1];
  gcommon.v1.common.SortDirection direction = 2;
}
```

---

### security_summary.proto {#security_summary}

**Path**: `gcommon/v1/metrics/security_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 20

**Messages** (1): `SecuritySummary`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/security_summary.proto
// version: 1.0.0
// guid: 88866dac-7333-4ae4-9fa5-9985e01c00dc

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SecuritySummary {
  bool auth_enabled = 1;
  bool tls_enabled = 2;
  repeated string auth_methods = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### stats_d_settings.proto {#stats_d_settings}

**Path**: `gcommon/v1/metrics/stats_d_settings.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `StatsDSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stats_d_settings.proto
// version: 1.0.0
// guid: 195c250a-8ebe-4d7d-9948-acc9c69848f5

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StatsDSettings {
  // StatsD server address
  string address = 1 [(buf.validate.field).string.min_len = 1];

  // Protocol to use (udp, tcp)
  string protocol = 2 [(buf.validate.field).string.min_len = 1];

  // Prefix for all metrics
  string prefix = 3 [(buf.validate.field).string.min_len = 1];

  // Sampling rate
  double sample_rate = 4 [(buf.validate.field).double.gte = 0.0];

  // Buffer size
  int32 buffer_size = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### stats_d_settings_update.proto {#stats_d_settings_update}

**Path**: `gcommon/v1/metrics/stats_d_settings_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 34

**Messages** (1): `StatsDSettingsUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stats_d_settings_update.proto
// version: 1.0.0
// guid: d12fd84f-4de1-43f7-ad5d-5079bfa8b126

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * StatsDSettingsUpdate contains updates to StatsD settings.
 */
message StatsDSettingsUpdate {
  // Updated server address
  string address = 1 [(buf.validate.field).string.min_len = 1];

  // Updated protocol
  string protocol = 2 [(buf.validate.field).string.min_len = 1];

  // Updated prefix
  string prefix = 3 [(buf.validate.field).string.min_len = 1];

  // Updated sample rate
  double sample_rate = 4 [(buf.validate.field).double.gte = 0.0];

  // Updated buffer size
  int32 buffer_size = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### stats_options.proto {#stats_options}

**Path**: `gcommon/v1/metrics/stats_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `StatsOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stats_options.proto
// version: 1.0.0
// guid: 08b06fd3-e0a2-4e73-a871-038c11415178

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StatsOptions {
  // Include performance statistics
  bool include_performance = 1;

  // Include resource usage statistics
  bool include_resource_usage = 2;

  // Include error statistics
  bool include_errors = 3;

  // Include data volume statistics
  bool include_data_volume = 4;

  // Include export statistics
  bool include_exports = 5;

  // Include health status history
  bool include_health_history = 6;

  // Include configuration information
  bool include_config = 7;

  // Include top metrics by various criteria
  bool include_top_metrics = 8;

  // Maximum number of top metrics to include
  int32 top_metrics_limit = 9 [(buf.validate.field).int32.gte = 0];

  // Include trend analysis
  bool include_trends = 10;
}
```

---

### stream_options.proto {#stream_options}

**Path**: `gcommon/v1/metrics/stream_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 45

**Messages** (1): `StreamOptions`

**Imports** (4):

- `gcommon/v1/common/stream_compression.proto`
- `gcommon/v1/common/stream_qos.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_options.proto
// version: 1.0.0
// guid: dfdf5759-e1b6-489a-9a64-0477334ebb2a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/stream_compression.proto";
import "gcommon/v1/common/stream_qos.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StreamOptions {
  // Whether to include historical data or only new metrics
  bool include_historical = 1;

  // Maximum number of metrics to send per message
  int32 batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum time to wait before sending a batch (milliseconds)
  int32 batch_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Whether to include metadata with each metric
  bool include_metadata = 4;

  // Compression to use for the stream
  gcommon.v1.common.StreamCompression compression = 5;

  // Whether to send heartbeat messages during idle periods
  bool send_heartbeats = 6;

  // Heartbeat interval (seconds)
  int32 heartbeat_interval_seconds = 7 [(buf.validate.field).int32.gte = 0];

  // Whether to automatically retry on errors
  bool auto_retry = 8;

  // Quality of service level
  gcommon.v1.common.StreamQOS qos = 9;
}
```

---

### stream_start.proto {#stream_start}

**Path**: `gcommon/v1/metrics/stream_start.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `StreamStart`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_start.proto
// version: 1.0.0
// guid: 035f2196-05b5-429a-be1c-e7feae4a5b49

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message StreamStart {
  // Start from a specific timestamp
  google.protobuf.Timestamp from_timestamp = 1;

  // Start from the beginning of available data
  bool from_beginning = 2;

  // Start from the current time (live streaming only)
  bool from_now = 3;

  // Start from a specific offset or position
  string from_offset = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### summary_metric.proto {#summary_metric}

**Path**: `gcommon/v1/metrics/summary_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 52

**Messages** (1): `SummaryMetric`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/summary_quantile.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_metric.proto
// version: 1.0.0
// guid: b33d2c5c-ecf6-44ee-9472-340b3362d75d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/summary_quantile.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryMetric {
  // Metric name (e.g., "http_request_duration_seconds")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Total count of observations
  uint64 sample_count = 2;

  // Sum of all observed values
  double sample_sum = 3;

  // Quantiles (e.g., 0.5, 0.9, 0.95, 0.99)
  repeated SummaryQuantile quantiles = 4;

  // Labels for metric dimensions
  map<string, string> labels = 5;

  // Timestamp when metric was recorded
  google.protobuf.Timestamp timestamp = 6;

  // Help text describing the metric
  string help = 7;

  // Metric unit (e.g., "seconds", "bytes")
  string unit = 8;

  // Maximum age of observations in the summary
  google.protobuf.Duration max_age = 9;

  // Metadata for request tracing
  gcommon.v1.common.RequestMetadata metadata = 10;
}
```

---

### summary_options.proto {#summary_options}

**Path**: `gcommon/v1/metrics/summary_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `SummaryOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_options.proto
// version: 1.0.0
// guid: c4d787f0-9e09-4c12-a14d-12627a57902d

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryOptions {
  // Include metric count information
  bool include_counts = 1;

  // Include data volume information
  bool include_data_volume = 2;

  // Include performance statistics
  bool include_performance = 3;

  // Include error rates and statistics
  bool include_errors = 4;

  // Include top metrics by various criteria
  bool include_top_metrics = 5;

  // Include retention policy information
  bool include_retention = 6;

  // Include export status information
  bool include_export_status = 7;

  // Maximum number of top metrics to include
  int32 top_metrics_limit = 8 [(buf.validate.field).int32.gte = 0];
}
```

---

### summary_quantile.proto {#summary_quantile}

**Path**: `gcommon/v1/metrics/summary_quantile.proto` **Package**: `gcommon.v1.metrics` **Lines**: 22

**Messages** (1): `SummaryQuantile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_quantile.proto
// version: 1.0.0
// guid: 4e691373-59b7-411a-a555-70e922bd4b72

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryQuantile {
  // Quantile value (0.0-1.0, e.g., 0.5 for median, 0.95 for 95th percentile)
  double quantile = 1 [(buf.validate.field).double.gte = 0.0];

  // Value at this quantile
  double value = 2 [(buf.validate.field).double.gte = 0.0];
}
```

---

### summary_value.proto {#summary_value}

**Path**: `gcommon/v1/metrics/summary_value.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `SummaryValue`

**Imports** (3):

- `gcommon/v1/metrics/quantile.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_value.proto
// version: 1.0.0
// guid: 535bdb2a-1af8-4ed2-a092-892f8d42a85c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/quantile.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryValue {
  // Quantile values
  repeated Quantile quantiles = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count of all samples
  uint64 count = 2 [(buf.validate.field).uint64.gte = 0];

  // Sum of all sample values
  double sum = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### tag_updates.proto {#tag_updates}

**Path**: `gcommon/v1/metrics/tag_updates.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `TagUpdates`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/tag_updates.proto
// version: 1.0.0
// guid: 3f881144-83c6-471b-9db4-227cb066b468

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TagUpdates contains tag update operations.
 */
message TagUpdates {
  // Tags to add or update
  map<string, string> tag_updates = 1;

  // Tag keys to remove
  repeated string tag_removes = 2 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### time_series.proto {#time_series}

**Path**: `gcommon/v1/metrics/time_series.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `TimeSeries`

**Imports** (3):

- `gcommon/v1/metrics/metric_sample.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_series.proto
// version: 1.0.0
// guid: 0f1e1fe8-f8db-4e8f-8220-628a1b9c02bf

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/metric_sample.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TimeSeries represents a collection of metric samples over time.
 */
message TimeSeries {
  // Identifier of the metric this series belongs to
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Ordered list of samples
  repeated MetricSample samples = 2 [(buf.validate.field).repeated.min_items = 1];

  // Labels associated with the series
  map<string, string> labels = 3;
}
```

---

### timer_metric.proto {#timer_metric}

**Path**: `gcommon/v1/metrics/timer_metric.proto` **Package**: `gcommon.v1.metrics` **Lines**: 58

**Messages** (1): `TimerMetric`

**Imports** (6):

- `gcommon/v1/metrics/percentile_measurement.proto`
- `gcommon/v1/metrics/timer_statistics.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/timer_metric.proto
// version: 1.0.0
// guid: 13ed2d88-7499-4d64-83cb-9292a1e35065

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/percentile_measurement.proto";
import "gcommon/v1/metrics/timer_statistics.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message TimerMetric {
  // Unique identifier for this timer measurement
  string timer_id = 1;

  // Name or label for this timer (e.g., "api_request_duration")
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Start time of the measured operation
  google.protobuf.Timestamp start_time = 3;

  // End time of the measured operation
  google.protobuf.Timestamp end_time = 4;

  // Duration of the measured operation
  google.protobuf.Duration duration = 5;

  // Tags/labels for categorization and filtering
  map<string, string> tags = 6;

  // Statistical aggregations for this timer
  TimerStatistics statistics = 7;

  // Whether this timer is currently running
  bool is_running = 8;

  // Number of times this timer has been recorded
  int64 count = 9;

  // Total accumulated time across all recordings
  google.protobuf.Duration total_duration = 10;

  // Percentile measurements
  repeated PercentileMeasurement percentiles = 11;

  // Timestamp when this metric was recorded
  google.protobuf.Timestamp recorded_at = 12;
}
```

---

### timer_statistics.proto {#timer_statistics}

**Path**: `gcommon/v1/metrics/timer_statistics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `TimerStatistics`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/timer_statistics.proto
// version: 1.0.0
// guid: 19d58a3d-7ce0-4642-8116-3baba86aee49

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message TimerStatistics {
  // Minimum duration observed
  google.protobuf.Duration min_duration = 1;

  // Maximum duration observed
  google.protobuf.Duration max_duration = 2;

  // Mean (average) duration
  google.protobuf.Duration mean_duration = 3;

  // Standard deviation of durations
  double standard_deviation_ms = 4 [(buf.validate.field).double.gte = 0.0];

  // Variance of durations
  double variance_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // Number of samples used for these statistics
  int64 sample_count = 6 [(buf.validate.field).int64.gte = 0];

  // Rate of measurements per second
  double rate_per_second = 7 [(buf.validate.field).double.gte = 0.0];

  // Most recent measurement duration
  google.protobuf.Duration last_duration = 8;
}
```

---

### timestamp_range.proto {#timestamp_range}

**Path**: `gcommon/v1/metrics/timestamp_range.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `MetricsTimestampRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/timestamp_range.proto
// version: 1.0.1
// guid: e7f8a9b0-123e-578d-2345-890123456789

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsTimestampRange {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;
}
```

---

### top_metrics.proto {#top_metrics}

**Path**: `gcommon/v1/metrics/top_metrics.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `TopMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/top_metrics.proto
// version: 1.0.0
// guid: c4d5e6f7-a8b9-0c1d-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TopMetrics contains information about top performing/problematic metrics.
 */
message TopMetrics {
  // Most active metrics (by volume)
  repeated string most_active = 1 [(buf.validate.field).repeated.min_items = 1];

  // Largest metrics by data volume
  repeated string largest_by_volume = 2 [(buf.validate.field).repeated.min_items = 1];

  // Metrics with highest error rates
  repeated string highest_errors = 3 [(buf.validate.field).repeated.min_items = 1];

  // Most frequently queried metrics
  repeated string most_queried = 4 [(buf.validate.field).repeated.min_items = 1];

  // Slowest performing metrics
  repeated string slowest_performing = 5 [(buf.validate.field).repeated.min_items = 1];

  // Most resource-intensive metrics
  repeated string most_resource_intensive = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### trend_analysis.proto {#trend_analysis}

**Path**: `gcommon/v1/metrics/trend_analysis.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `TrendAnalysis`

**Imports** (5):

- `gcommon/v1/metrics/data_volume_trend.proto`
- `gcommon/v1/metrics/error_trend.proto`
- `gcommon/v1/metrics/performance_trend.proto`
- `gcommon/v1/metrics/resource_usage_trend.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/trend_analysis.proto
// version: 1.0.1
// guid: cb796e78-7aa6-47b8-8545-402a70e2c9e0

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/data_volume_trend.proto";
import "gcommon/v1/metrics/error_trend.proto";
import "gcommon/v1/metrics/performance_trend.proto";
import "gcommon/v1/metrics/resource_usage_trend.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message TrendAnalysis {
  // Performance trends
  PerformanceTrend performance = 1;

  // Resource usage trends
  ResourceUsageTrend resource_usage = 2;

  // Error trends
  ErrorTrend errors = 3;

  // Data volume trends
  DataVolumeTrend data_volume = 4;
}
```

---

### unregistration_options.proto {#unregistration_options}

**Path**: `gcommon/v1/metrics/unregistration_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 40

**Messages** (1): `UnregistrationOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/unregistration_options.proto
// version: 1.0.0
// guid: 158ebf54-a2dd-4dae-b8dc-9c9fb19344db

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UnregistrationOptions {
  // Whether to delete all associated data
  bool delete_data = 1;

  // Whether to delete associated indices
  bool delete_indices = 2;

  // Whether to remove alert rules
  bool remove_alerts = 3;

  // Whether to stop export configurations
  bool stop_exports = 4;

  // Grace period before actual deletion (duration string like "24h")
  string grace_period = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to perform a dry run (show what would be deleted)
  bool dry_run = 6;

  // Whether to force deletion even if metric is in use
  bool force = 7;

  // Whether to create a backup before deletion
  bool create_backup = 8;
}
```

---

### unregistration_result.proto {#unregistration_result}

**Path**: `gcommon/v1/metrics/unregistration_result.proto` **Package**: `gcommon.v1.metrics` **Lines**: 42

**Messages** (1): `UnregistrationResult`

**Imports** (4):

- `gcommon/v1/metrics/dry_run_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/unregistration_result.proto
// version: 1.0.0
// guid: ada4f63c-d9d5-496b-a0f9-a70062740177

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/dry_run_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message UnregistrationResult {
  // Whether the metric definition was deleted
  bool definition_deleted = 1;

  // Amount of data that was deleted (bytes)
  int64 data_deleted_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Number of data points deleted
  int64 data_points_deleted = 3 [(buf.validate.field).int64.gte = 0];

  // Indices that were deleted
  repeated string deleted_indices = 4 [(buf.validate.field).repeated.min_items = 1];

  // Alert rules that were removed
  repeated string removed_alerts = 5 [(buf.validate.field).repeated.min_items = 1];

  // Export configurations that were stopped
  repeated string stopped_exports = 6 [(buf.validate.field).repeated.min_items = 1];

  // Time when actual deletion will occur (if grace period is set)
  google.protobuf.Timestamp scheduled_deletion = 7;

  // What would be deleted (for dry run operations)
  DryRunResult dry_run_result = 8;
}
```

---

### validation_rules.proto {#validation_rules}

**Path**: `gcommon/v1/metrics/validation_rules.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ValidationRules`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/validation_rules.proto
// version: 1.0.0
// guid: 0d988017-d38b-43d4-bb5b-c076ce14326a

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ValidationRules {
  // Minimum allowed value
  double min_value = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum allowed value
  double max_value = 2 [(buf.validate.field).double.gte = 0.0];

  // Whether null/zero values are allowed
  bool allow_null = 3;

  // Custom validation expressions
  repeated string validation_expressions = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### validation_summary.proto {#validation_summary}

**Path**: `gcommon/v1/metrics/validation_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ValidationSummary`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/validation_summary.proto
// version: 1.0.0
// guid: 6bc5ca1a-e2c7-4863-a193-8ee676812c63

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ValidationSummary {
  // Number of metrics that passed validation
  int32 valid_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of metrics that failed validation
  int32 invalid_count = 2 [(buf.validate.field).int32.gte = 0];

  // Most common validation errors
  repeated string common_errors = 3 [(buf.validate.field).repeated.min_items = 1];

  // Schema version used for validation
  string schema_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### api_key_config_update.proto {#api_key_config_update}

**Path**: `gcommon/v1/metrics/api_key_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `APIKeyConfigUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/api_key_config_update.proto
// version: 1.0.0
// guid: f04936d2-7273-4746-bc4b-9a2c0794658f

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * APIKeyConfigUpdate contains updates to API key configuration.
 */
message APIKeyConfigUpdate {
  // Updated header name
  string header_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated required setting
  bool required = 2;

  // API key updates
  repeated string allowed_key_updates = 3;

  // API keys to remove
  repeated string allowed_key_removes = 4;
}
```

---

### applied_config.proto {#applied_config}

**Path**: `gcommon/v1/metrics/applied_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `AppliedConfig`

**Imports** (3):

- `gcommon/v1/metrics/resource_allocations.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/applied_config.proto
// version: 1.0.0
// guid: d569fe55-1ee6-4cbb-94c5-f4bd79df578d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_allocations.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message AppliedConfig {
  // Configuration that was actually applied (may differ from requested)
  string config_summary = 1 [(buf.validate.field).string.min_len = 1];

  // Default values that were applied
  map<string, string> applied_defaults = 2;

  // Configuration overrides that were applied
  map<string, string> applied_overrides = 3;

  // Resource allocations that were made
  ResourceAllocations resource_allocations = 4;
}
```

---

### buffer_config.proto {#buffer_config}

**Path**: `gcommon/v1/metrics/buffer_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `BufferConfig`

**Imports** (3):

- `gcommon/v1/common/buffer_overflow_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/buffer_config.proto
// version: 1.0.0
// guid: 3cbd27e2-8ac4-4dad-8b12-6ae61bca9e6c

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/buffer_overflow_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message BufferConfig {
  // Maximum number of metrics to buffer
  int32 max_buffer_size = 1 [(buf.validate.field).int32.gte = 0];

  // Buffer overflow strategy
  gcommon.v1.common.BufferOverflowStrategy overflow_strategy = 2;

  // Whether to persist buffer to disk during streaming
  bool persist_buffer = 3;

  // Maximum memory usage for buffering (bytes)
  int64 max_memory_bytes = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### configuration_summary.proto {#configuration_summary}

**Path**: `gcommon/v1/metrics/configuration_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `ConfigurationSummary`

**Imports** (4):

- `gcommon/v1/metrics/resource_limits_summary.proto`
- `gcommon/v1/metrics/security_summary.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/configuration_summary.proto
// version: 1.0.0
// guid: 9af1b63b-741f-454d-a992-90c457764c2d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_limits_summary.proto";
import "gcommon/v1/metrics/security_summary.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ConfigurationSummary {
  // Number of configured exporters
  int32 exporter_count = 1 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Security settings summary
  SecuritySummary security = 2;

  // Resource limits summary
  ResourceLimitsSummary resource_limits = 3;

  // Configuration version
  string config_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];
}
```

---

### counter_config.proto {#counter_config}

**Path**: `gcommon/v1/metrics/counter_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `CounterConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/counter_config.proto
// version: 1.0.0
// guid: 574d7f46-80ea-4a48-9dad-c55f07c5f558

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CounterConfig {
  // Starting value for the counter
  double initial_value = 1 [(buf.validate.field).double.gte = 0.0];

  // Whether the counter can be reset
  bool allow_reset = 2;

  // Maximum value before rolling over
  double max_value = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### export_config.proto {#export_config}

**Path**: `gcommon/v1/metrics/export_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `ExportConfig`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`
- `gcommon/v1/metrics/metrics_retry_config.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/export_config.proto
// version: 1.0.0
// guid: 498c1fb6-967a-4e05-b62a-fbeaa2214616

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";
import "gcommon/v1/metrics/metrics_retry_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportConfig {
  // Export destination URL or endpoint
  string destination = 1 [(buf.validate.field).string.min_len = 1];

  // Export format (json, csv, prometheus, etc.)
  string format = 2 [(buf.validate.field).string.min_len = 1];

  // Export frequency in seconds
  int32 frequency_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Whether to compress exported data
  bool compress = 4;

  // Batch size for exports
  int32 batch_size = 5 [(buf.validate.field).int32.gte = 0];

  // Timeout for export operations in seconds
  int32 timeout_seconds = 6 [(buf.validate.field).int32.gt = 0];

  // Custom headers for HTTP exports
  map<string, string> headers = 7;

  // Authentication configuration
  map<string, string> auth_config = 8;

  // Retry configuration
  MetricsRetryConfig retry_config = 9;

  // Filtering rules for what to export
  repeated string include_patterns = 10 [(buf.validate.field).repeated.min_items = 1];
  repeated string exclude_patterns = 11 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### export_config_update.proto {#export_config_update}

**Path**: `gcommon/v1/metrics/export_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `ExportConfigUpdate`

**Imports** (3):

- `gcommon/v1/metrics/export_destination_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_config_update.proto
// version: 1.0.0
// guid: fd6ebe54-a1db-4c08-84b4-a91b690e9af6

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_destination_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ExportConfigUpdate contains updates to export configuration.
 */
message ExportConfigUpdate {
  // Updated enabled status
  bool enabled = 1;

  // Format updates
  repeated string format_updates = 2 [(buf.validate.field).repeated.min_items = 1];

  // Formats to remove
  repeated string format_removes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Destination updates
  repeated ExportDestinationUpdate destination_updates = 4 [(buf.validate.field).repeated.min_items = 1];

  // Destinations to remove
  repeated string destination_removes = 5 [(buf.validate.field).repeated.min_items = 1];

  // Updated export frequency
  string frequency = 6 [(buf.validate.field).string.min_len = 1];

  // Updated batch size
  int32 batch_size = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### gauge_config.proto {#gauge_config}

**Path**: `gcommon/v1/metrics/gauge_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `GaugeConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/gauge_config.proto
// version: 1.0.0
// guid: 9f7c124b-e567-4c31-ad6b-19c05836a84b

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GaugeConfig {
  // Minimum allowed value
  double min_value = 1 [(buf.validate.field).double.gte = 0.0];

  // Maximum allowed value
  double max_value = 2 [(buf.validate.field).double.gte = 0.0];

  // Whether the gauge can go negative
  bool allow_negative = 3;
}
```

---

### get_metric_config_request.proto {#get_metric_config_request}

**Path**: `gcommon/v1/metrics/get_metric_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetMetricConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_config_request.proto
// version: 1.0.0
// guid: 82add51b-b9ac-4042-be4d-4acada2ae127
// file: proto/gcommon/v1/metrics/v1/get_metric_config_request.proto
//
// Request message to retrieve metric configuration.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricConfigRequest {
  // Metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_metric_config_response.proto {#get_metric_config_response}

**Path**: `gcommon/v1/metrics/get_metric_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetMetricConfigResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_config_response.proto
// version: 1.0.1
// guid: 1d1401a7-7986-407f-9b51-d77ceae3b42b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricConfigResponse contains metric configuration information.
 */
message GetMetricConfigResponse {
  // Operation success flag
  bool success = 1;

  // Error details if any
  gcommon.v1.common.Error error = 2;

  // Retrieved configuration
  MetricConfig config = 3;
}
```

---

### get_scrape_config_request.proto {#get_scrape_config_request}

**Path**: `gcommon/v1/metrics/get_scrape_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetScrapeConfigRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_request.proto
// version: 1.0.0
// guid: 9ddccca8-f23d-4cc8-b483-9aea96bae473
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_request.proto
//
// Request message for retrieving scrape configuration.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetScrapeConfigRequest {
  // Provider identifier
  string provider_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_scrape_config_response.proto {#get_scrape_config_response}

**Path**: `gcommon/v1/metrics/get_scrape_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetScrapeConfigResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_response.proto
// version: 1.0.1
// guid: fa33c699-3eb3-4466-82b0-f7983815994e
// file: proto/gcommon/v1/metrics/v1/get_scrape_config_response.proto
//
// Response containing scraping configuration for a provider.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetScrapeConfigResponse returns provider scrape configuration.
 */
message GetScrapeConfigResponse {
  // Current scrape configuration
  ScrapeConfig config = 1;

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}
```

---

### histogram_config.proto {#histogram_config}

**Path**: `gcommon/v1/metrics/histogram_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `HistogramConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/histogram_config.proto
// version: 1.0.0
// guid: d859806f-1fdc-4c74-a05d-c8872810e652

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message HistogramConfig {
  // Predefined buckets for the histogram
  repeated double buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Whether to automatically adjust buckets based on data
  bool auto_buckets = 2;

  // Maximum number of buckets to maintain
  int32 max_buckets = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### import_config.proto {#import_config}

**Path**: `gcommon/v1/metrics/import_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ImportConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/import_config.proto
// version: 1.0.0
// guid: f2e3c94f-e0d7-4e2d-9799-1a4005b10c64

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ImportConfig defines how external metrics should be imported
 * into the system.
 */
message ImportConfig {
  // List of source identifiers or URLs
  repeated string sources = 1 [(buf.validate.field).repeated.min_items = 1];

  // Cron-style schedule for imports
  string schedule = 2 [(buf.validate.field).string.min_len = 1];

  // Whether importing is enabled
  bool enabled = 3;
}
```

---

### metric_config.proto {#metric_config}

**Path**: `gcommon/v1/metrics/metric_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 53

**Messages** (1): `MetricConfig`

**Imports** (4):

- `gcommon/v1/metrics/export_config.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_config.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_config.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * MetricConfig contains configuration settings for a specific metric.
 */
message MetricConfig {
  // Metric name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Metric type (counter, gauge, histogram, summary, etc.)
  string metric_type = 2;

  // Whether this metric is enabled
  bool enabled = 3;

  // Collection interval
  google.protobuf.Duration collection_interval = 4;

  // Retention period for this metric
  google.protobuf.Duration retention_period = 5;

  // Labels to automatically add to this metric
  map<string, string> default_labels = 6;

  // Description of the metric
  string description = 7 [ (buf.validate.field).string.max_len = 1000 ];

  // Unit of measurement
  string unit = 8;

  // Sampling rate (0.0 to 1.0)
  double sampling_rate = 9;

  // Export configuration
  ExportConfig export_config = 10;
}
```

---

### metric_type_config.proto {#metric_type_config}

**Path**: `gcommon/v1/metrics/metric_type_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `MetricTypeConfig`

**Imports** (5):

- `gcommon/v1/metrics/counter_config.proto`
- `gcommon/v1/metrics/gauge_config.proto`
- `gcommon/v1/metrics/histogram_config.proto`
- `gcommon/v1/metrics/summary_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_type_config.proto
// version: 1.0.1
// guid: 440003e9-c836-4e1c-8e6f-754798a23832

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/counter_config.proto";
import "gcommon/v1/metrics/gauge_config.proto";
import "gcommon/v1/metrics/histogram_config.proto";
import "gcommon/v1/metrics/summary_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricTypeConfig {
  // Configuration for histogram metrics
  HistogramConfig histogram = 1;

  // Configuration for summary metrics
  SummaryConfig summary = 2;

  // Configuration for gauge metrics
  GaugeConfig gauge = 3;

  // Configuration for counter metrics
  CounterConfig counter = 4;
}
```

---

### metrics_retry_config.proto {#metrics_retry_config}

**Path**: `gcommon/v1/metrics/metrics_retry_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `MetricsRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/metrics_retry_config.proto
// version: 1.0.0
// guid: f77fa8d6-728f-4bd9-9dab-8965dfb38ff8

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsRetryConfig {
  // Maximum number of retries
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay in seconds
  int32 initial_delay_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay in seconds
  int32 max_delay_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];
}
```

---

### provider_config.proto {#provider_config}

**Path**: `gcommon/v1/metrics/provider_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 50

**Messages** (1): `ProviderConfig`

**Imports** (7):

- `gcommon/v1/common/metrics_provider_type.proto`
- `gcommon/v1/common/organization_resource_limits.proto`
- `gcommon/v1/metrics/export_config.proto`
- `gcommon/v1/metrics/provider_settings.proto`
- `gcommon/v1/metrics/security_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_config.proto
// version: 1.0.0
// guid: 3539da64-8631-416f-8d05-17a4810ed876

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_provider_type.proto";
import "gcommon/v1/common/organization_resource_limits.proto";
import "gcommon/v1/metrics/export_config.proto";
import "gcommon/v1/metrics/provider_settings.proto";
import "gcommon/v1/metrics/security_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderConfig {
  // Unique identifier for the provider
  string provider_id = 1;

  // Human-readable name for the provider
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of provider (prometheus, opentelemetry, custom, etc.)
  gcommon.v1.common.MetricsProviderType type = 3;

  // Provider-specific configuration
  ProviderSettings settings = 4;

  // Export configuration for this provider
  ExportConfig export_config = 5;

  // Resource limits imposed by the organization
  gcommon.v1.common.OrganizationResourceLimits resource_limits = 6;

  // Security configuration
  MetricsSecurityConfig security_config = 7;

  // Tags for provider organization
  map<string, string> tags = 8;

  // Description of the provider
  string description = 9 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### provider_config_summary.proto {#provider_config_summary}

**Path**: `gcommon/v1/metrics/provider_config_summary.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ProviderConfigSummary`

**Imports** (3):

- `gcommon/v1/metrics/resource_limits_summary.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_config_summary.proto
// version: 1.0.0
// guid: 394dfc33-7acb-4583-bd49-44bdcb86e5ba

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/resource_limits_summary.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ProviderConfigSummary {
  // Number of configured exporters
  int32 exporter_count = 1 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Whether security is enabled
  bool security_enabled = 2;

  // Resource limits summary
  ResourceLimitsSummary resource_limits = 3;

  // Export destinations
  repeated string export_destinations = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### provider_config_update.proto {#provider_config_update}

**Path**: `gcommon/v1/metrics/provider_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 47

**Messages** (1): `ProviderConfigUpdate`

**Imports** (7):

- `gcommon/v1/metrics/export_config_update.proto`
- `gcommon/v1/metrics/provider_settings_update.proto`
- `gcommon/v1/metrics/resource_limits_update.proto`
- `gcommon/v1/metrics/security_config_update.proto`
- `gcommon/v1/metrics/tag_updates.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_config_update.proto
// version: 1.0.0
// guid: 175e030e-5a4a-4d94-9f2a-6d8bb006602a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/export_config_update.proto";
import "gcommon/v1/metrics/provider_settings_update.proto";
import "gcommon/v1/metrics/resource_limits_update.proto";
import "gcommon/v1/metrics/security_config_update.proto";
import "gcommon/v1/metrics/tag_updates.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ProviderConfigUpdate contains the configuration updates to apply.
 */
message ProviderConfigUpdate {
  // Updated name (if changing)
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated description (if changing)
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Provider settings updates
  ProviderSettingsUpdate settings_update = 3;

  // Export configuration updates
  ExportConfigUpdate export_config_update = 4;

  // Resource limits updates
  ResourceLimitsUpdate resource_limits_update = 5;

  // Security configuration updates
  SecurityConfigUpdate security_config_update = 6;

  // Tag updates
  TagUpdates tag_updates = 7;
}
```

---

### scrape_config.proto {#scrape_config}

**Path**: `gcommon/v1/metrics/scrape_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `ScrapeConfig`

**Imports** (3):

- `gcommon/v1/metrics/scrape_target.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/scrape_config.proto
// version: 1.0.0
// guid: a754fb7e-a819-4731-82fd-6a587b928a9e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/scrape_target.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ScrapeConfig defines how metrics should be scraped from targets.
 */
message ScrapeConfig {
  // Job name for the scrape configuration
  string job_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Targets to scrape
  repeated ScrapeTarget targets = 2;

  // Interval between scrapes in seconds
  int32 scrape_interval_seconds = 3;
}
```

---

### security_config.proto {#security_config}

**Path**: `gcommon/v1/metrics/security_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 33

**Messages** (1): `MetricsSecurityConfig`

**Imports** (4):

- `gcommon/v1/common/metrics_api_key_config.proto`
- `gcommon/v1/metrics/tls_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/security_config.proto
// version: 1.0.0
// guid: 61377102-cbd1-4223-8342-a2f11b1c4d47

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_api_key_config.proto";
import "gcommon/v1/metrics/tls_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsSecurityConfig {
  // Whether authentication is required
  bool require_auth = 1;

  // Allowed authentication methods
  repeated string auth_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether TLS is required
  bool require_tls = 3;

  // TLS configuration
  MetricsTLSConfig tls_config = 4;

  // API key configuration
  gcommon.v1.common.MetricsAPIKeyConfig api_key_config = 5;
}
```

---

### security_config_update.proto {#security_config_update}

**Path**: `gcommon/v1/metrics/security_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `SecurityConfigUpdate`

**Imports** (4):

- `gcommon/v1/metrics/api_key_config_update.proto`
- `gcommon/v1/metrics/tls_config_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/security_config_update.proto
// version: 1.0.0
// guid: 94abaf44-d603-4b65-8bd3-d98ca462c20e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/api_key_config_update.proto";
import "gcommon/v1/metrics/tls_config_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SecurityConfigUpdate contains updates to security configuration.
 */
message SecurityConfigUpdate {
  // Updated authentication requirement
  bool require_auth = 1;

  // Updated authentication methods
  repeated string auth_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Updated TLS requirement
  bool require_tls = 3;

  // TLS configuration updates
  TLSConfigUpdate tls_config_update = 4;

  // API key configuration updates
  APIKeyConfigUpdate api_key_config_update = 5;
}
```

---

### set_metric_config_request.proto {#set_metric_config_request}

**Path**: `gcommon/v1/metrics/set_metric_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 21

**Messages** (1): `SetMetricConfigRequest`

**Imports** (2):

- `gcommon/v1/metrics/metric_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_metric_config_request.proto
// version: 1.0.1
// guid: d1b98b0c-98f7-47fc-9bb5-f18ebfbbe1d3

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/metrics/metric_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetMetricConfigRequest updates configuration for a metric.
 */
message SetMetricConfigRequest {
  // Updated configuration
  MetricConfig config = 1;
}
```

---

### set_metric_config_response.proto {#set_metric_config_response}

**Path**: `gcommon/v1/metrics/set_metric_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 24

**Messages** (1): `SetMetricConfigResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_metric_config_response.proto
// version: 1.0.1
// guid: 5faba194-b6ab-42ba-99c3-62eb07df9265

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetMetricConfigResponse is returned after updating metric config.
 */
message SetMetricConfigResponse {
  // Operation success flag
  bool success = 1;

  // Error details if any
  gcommon.v1.common.Error error = 2;
}
```

---

### set_scrape_config_request.proto {#set_scrape_config_request}

**Path**: `gcommon/v1/metrics/set_scrape_config_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `SetScrapeConfigRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/scrape_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_request.proto
// version: 1.0.0
// guid: 239855c3-0df1-42c3-a9dd-c6d7709f048f
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_request.proto
//
// Request message to set scraping configuration for a provider.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/scrape_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SetScrapeConfigRequest {
  // Provider identifier
  string provider_id = 1 [(buf.validate.field).string.min_len = 1];

  // New scrape configuration
  ScrapeConfig config = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### set_scrape_config_response.proto {#set_scrape_config_response}

**Path**: `gcommon/v1/metrics/set_scrape_config_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `SetScrapeConfigResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_response.proto
// version: 1.0.1
// guid: e328641f-32d3-4439-b78e-d7fbd14ede9d
// file: proto/gcommon/v1/metrics/v1/set_scrape_config_response.proto
//
// Response after updating scrape configuration.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * SetScrapeConfigResponse confirms new configuration.
 */
message SetScrapeConfigResponse {
  // Whether the update succeeded
  bool success = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### summary_config.proto {#summary_config}

**Path**: `gcommon/v1/metrics/summary_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `SummaryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/summary_config.proto
// version: 1.0.0
// guid: f54bfb16-e799-4222-881b-a86425813aa6

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message SummaryConfig {
  // Quantiles to calculate (e.g., 0.5, 0.95, 0.99)
  repeated double quantiles = 1 [(buf.validate.field).repeated.min_items = 1];

  // Time window for calculating quantiles
  string time_window = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum age of observations to include
  string max_age = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### tls_config.proto {#tls_config}

**Path**: `gcommon/v1/metrics/tls_config.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricsTLSConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/tls_config.proto
// version: 1.0.0
// guid: 7da056fd-4d1f-48fa-8ee0-fbad667fa085

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsTLSConfig {
  // Certificate file path
  string cert_file = 1 [(buf.validate.field).string.min_len = 1];

  // Private key file path
  string key_file = 2 [(buf.validate.field).string.min_len = 1];

  // CA certificate file path
  string ca_file = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to verify certificates
  bool verify_certs = 4;
}
```

---

### tls_config_update.proto {#tls_config_update}

**Path**: `gcommon/v1/metrics/tls_config_update.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `TLSConfigUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/tls_config_update.proto
// version: 1.0.0
// guid: d61cb51c-f2b6-403b-bf24-6b5fe08c3e61

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * TLSConfigUpdate contains updates to TLS configuration.
 */
message TLSConfigUpdate {
  // Updated certificate file path
  string cert_file = 1 [(buf.validate.field).string.min_len = 1];

  // Updated private key file path
  string key_file = 2 [(buf.validate.field).string.min_len = 1];

  // Updated CA certificate file path
  string ca_file = 3 [(buf.validate.field).string.min_len = 1];

  // Updated certificate verification setting
  bool verify_certs = 4;
}
```

---

### backup_info.proto {#backup_info}

**Path**: `gcommon/v1/metrics/backup_info.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `MetricsBackupInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/backup_info.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174026

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * BackupInfo contains information about backup operations.
 */
message MetricsBackupInfo {
  // Unique backup identifier
  string backup_id = 1 [(buf.validate.field).string.min_len = 1];

  // Location where backup is stored
  string backup_location = 2 [(buf.validate.field).string.min_len = 1];

  // Size of backup in bytes
  int64 backup_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // When backup was created
  google.protobuf.Timestamp backup_created_at = 4;

  // Backup retention period
  string backup_retention = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### batch_context.proto {#batch_context}

**Path**: `gcommon/v1/metrics/batch_context.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `BatchContext`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_context.proto
// version: 1.0.0
// guid: f2e4f42e-77e5-4086-89ea-b7d514304089

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message BatchContext {
  // Unique batch ID
  string batch_id = 1 [(buf.validate.field).string.min_len = 1];

  // Position in the batch (0-based)
  int32 batch_position = 2 [(buf.validate.field).int32.gte = 0];

  // Total size of the batch
  int32 batch_size = 3 [(buf.validate.field).int32.gte = 0];

  // Whether this is the last item in the batch
  bool is_last = 4;
}
```

---

### batch_options.proto {#batch_options}

**Path**: `gcommon/v1/metrics/batch_options.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `MetricsBatchOptions`

**Imports** (3):

- `gcommon/v1/common/batch_priority.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_options.proto
// version: 1.0.0
// guid: cb61183a-3b53-41cd-a131-685b4fd8be75

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/batch_priority.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * BatchOptions configures how batch operations should be processed.
 */
message MetricsBatchOptions {
  // Whether to process metrics in parallel
  bool parallel_processing = 1;

  // Maximum concurrent operations (if parallel processing is enabled)
  int32 max_concurrency = 2 [(buf.validate.field).int32.gte = 0];

  // Whether to deduplicate metrics within the batch
  bool deduplicate = 3;

  // Whether to return detailed results for each metric
  bool return_detailed_results = 4;

  // Timeout for the entire batch operation (seconds)
  int32 timeout_seconds = 5 [(buf.validate.field).int32.gt = 0];

  // Whether to enable transactional semantics (all or nothing)
  bool transactional = 6;

  // Priority level for the batch operation
  gcommon.v1.common.BatchPriority priority = 7;
}
```

---

### batch_stats.proto {#batch_stats}

**Path**: `gcommon/v1/metrics/batch_stats.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `MetricsBatchStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_stats.proto
// version: 1.0.0
// guid: 6e20b77a-ba63-4ecc-9089-0371258fb120

edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsBatchStats {
  // Total time taken to process the batch (milliseconds)
  int64 total_processing_time_ms = 1 [(buf.validate.field).int64.gte = 0];

  // Average time per metric (milliseconds)
  int64 avg_processing_time_ms = 2 [(buf.validate.field).int64.gte = 0];

  // Total size of all metrics data (bytes)
  int64 total_data_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Number of metrics that were deduplicated
  int32 deduplication_count = 4 [(buf.validate.field).int32.gte = 0];

  // Number of parallel workers used
  int32 parallel_workers = 5 [(buf.validate.field).int32.gte = 0];

  // Backend storage latency (milliseconds)
  int64 storage_latency_ms = 6 [(buf.validate.field).int64.gte = 0];

  // Memory usage during batch processing (bytes)
  int64 memory_usage_bytes = 7 [(buf.validate.field).int64.gte = 0];
}
```

---

### create_metric_request.proto {#create_metric_request}

**Path**: `gcommon/v1/metrics/create_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `CreateMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_metric_request.proto
// version: 1.0.1
// guid: 4fc0fab0-dc1a-42ff-bb58-35b524f790e1
// file: proto/gcommon/v1/metrics/v1/create_metric_request.proto
//
// Request definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CreateMetricRequest {
  // Metric to create
  MetricData metric = 1;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### create_metric_response.proto {#create_metric_response}

**Path**: `gcommon/v1/metrics/create_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `CreateMetricResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_metric_response.proto
// version: 1.0.1
// guid: 83588dec-abb1-410c-8a89-b2d53cdd2eec
// file: proto/gcommon/v1/metrics/v1/create_metric_response.proto
//
// Response returned after creating a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * CreateMetricResponse contains the result of a metric creation.
 */
message CreateMetricResponse {
  // Created metric metadata
  MetricMetadata metadata = 1;

  // Operation error details if any
  gcommon.v1.common.Error error = 2;
}
```

---

### create_provider_request.proto {#create_provider_request}

**Path**: `gcommon/v1/metrics/create_provider_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `CreateProviderRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/provider_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_provider_request.proto
// version: 1.0.1
// guid: 1bbe7bf6-5552-43f2-a429-d72f7fb4385f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/provider_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CreateProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider configuration
  ProviderConfig config = 2;

  // Whether to validate the configuration before creating
  bool validate_config = 3;

  // Whether to perform a dry run (validation only)
  bool dry_run = 4;

  // Whether to start the provider immediately after creation
  bool auto_start = 5;
}
```

---

### create_provider_response.proto {#create_provider_response}

**Path**: `gcommon/v1/metrics/create_provider_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 48

**Messages** (1): `CreateProviderResponse`

**Imports** (8):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/metrics/applied_config.proto`
- `gcommon/v1/metrics/provider_endpoints.proto`
- `gcommon/v1/metrics/provider_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/create_provider_response.proto
// version: 1.0.0
// guid: d3b0a595-52ae-4306-be02-6d7d23e8a0df

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/metrics/applied_config.proto";
import "gcommon/v1/metrics/provider_endpoints.proto";
import "gcommon/v1/metrics/provider_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message CreateProviderResponse {
  // Success status of the creation
  bool success = 1;

  // Error information if creation failed
  gcommon.v1.common.Error error = 2;

  // ID of the created provider
  string provider_id = 3;

  // When the provider was created
  google.protobuf.Timestamp created_at = 4 [ (buf.validate.field).required = true ];

  // Current status of the provider
  ProviderStatus status = 5;

  // Validation results
  gcommon.v1.common.MetricsValidationResult validation = 6;

  // Configuration details that were applied
  AppliedConfig applied_config = 7;

  // Warnings or informational messages
  repeated string warnings = 8;

  // Endpoint information for accessing the provider
  ProviderEndpoints endpoints = 9;
}
```

---

### delete_metric_request.proto {#delete_metric_request}

**Path**: `gcommon/v1/metrics/delete_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `DeleteMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_metric_request.proto
// version: 1.0.0
// guid: a9c3b698-cd8d-4405-b2f8-913d63eb25b4
// file: proto/gcommon/v1/metrics/v1/delete_metric_request.proto
//
// Request to delete an existing metric definition.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeleteMetricRequest {
  // Unique identifier of the metric
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Optional namespace
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### delete_metric_response.proto {#delete_metric_response}

**Path**: `gcommon/v1/metrics/delete_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `DeleteMetricResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_metric_response.proto
// version: 1.0.1
// guid: 8c8412a9-6dbd-4e4c-9b63-36745a456d41
// file: proto/gcommon/v1/metrics/v1/delete_metric_response.proto
//
// Response returned after deleting a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * DeleteMetricResponse confirms metric deletion.
 */
message DeleteMetricResponse {
  // Whether the delete succeeded
  bool success = 1;

  // Error details if the operation failed
  gcommon.v1.common.Error error = 2;
}
```

---

### delete_provider_request.proto {#delete_provider_request}

**Path**: `gcommon/v1/metrics/delete_provider_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `DeleteProviderRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_provider_request.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-9012-3456-789abcdef012

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeleteProviderRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to delete
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Optional force deletion (ignore dependencies)
  bool force = 3;

  // Dry run mode - just check what would be deleted
  bool dry_run = 4;
}
```

---

### delete_provider_response.proto {#delete_provider_response}

**Path**: `gcommon/v1/metrics/delete_provider_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `DeleteProviderResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/backup_info.proto`
- `gcommon/v1/metrics/deletion_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/delete_provider_response.proto
// version: 1.0.0
// guid: 0c3bdd9f-3771-4f0b-8c33-24d5a40b6c06

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/backup_info.proto";
import "gcommon/v1/metrics/deletion_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message DeleteProviderResponse {
  // Success status of the deletion
  bool success = 1;

  // Error information if deletion failed
  gcommon.v1.common.Error error = 2;

  // Provider ID that was deleted
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // When the deletion was completed
  google.protobuf.Timestamp deleted_at = 4;

  // Deletion results
  DeletionResult deletion_result = 5;

  // Warnings or informational messages
  repeated string warnings = 6 [(buf.validate.field).repeated.min_items = 1];

  // Backup information (if backup was created)
  MetricsBackupInfo backup_info = 7;

  // When scheduled deletion will occur (if grace period is set)
  google.protobuf.Timestamp scheduled_deletion = 8;
}
```

---

### export_metrics_request.proto {#export_metrics_request}

**Path**: `gcommon/v1/metrics/export_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `ExportMetricsRequest`

**Imports** (4):

- `gcommon/v1/common/metrics_export_format.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_metrics_request.proto
// version: 1.1.0
// guid: 2c9c223d-523d-4b0c-aa30-6249240e59d6

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/metrics_export_format.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ExportMetricsRequest {
  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Metrics provider to export from
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Desired export format
  gcommon.v1.common.MetricsExportFormat format = 3;

  // Destination URI or path
  string destination = 4 [(buf.validate.field).string.min_len = 1];

  // Specific metrics to include (optional)
  repeated string metric_names = 5 [(buf.validate.field).repeated.min_items = 1];

  // Include metadata such as descriptions and units
  bool include_metadata = 6;
}
```

---

### export_metrics_response.proto {#export_metrics_response}

**Path**: `gcommon/v1/metrics/export_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ExportMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_metrics_response.proto
// version: 1.1.0
// guid: 0d2df1e4-76e3-437b-855e-4dcc2b6f6b9e

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ExportMetricsResponse returns the result of a metrics export operation.
 */
message ExportMetricsResponse {
  // Whether the export succeeded
  bool success = 1;

  // Error information if the export failed
  gcommon.v1.common.Error error = 2;

  // Number of records exported
  int64 exported_records = 3;

  // Timestamp when the export completed
  google.protobuf.Timestamp exported_at = 4;

  // Location of the exported data
  string file_url = 5 [ (buf.validate.field).string.uri = true ];
}
```

---

### get_alerting_rules_request.proto {#get_alerting_rules_request}

**Path**: `gcommon/v1/metrics/get_alerting_rules_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetAlertingRulesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_request.proto
// version: 1.0.0
// guid: eb75f08e-4be4-41e8-8992-f9f95b7962bc
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_request.proto
//
// Request message for retrieving alerting rules associated with a metric.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetAlertingRulesRequest {
  // Metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_alerting_rules_response.proto {#get_alerting_rules_response}

**Path**: `gcommon/v1/metrics/get_alerting_rules_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `GetAlertingRulesResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/alerting_rule.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_response.proto
// version: 1.0.0
// guid: e6b7e2fc-4cd1-4e68-8d74-edab03688e54
// file: proto/gcommon/v1/metrics/v1/get_alerting_rules_response.proto
//
// Response message containing alerting rules for a metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/alerting_rule.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetAlertingRulesResponse returns configured alerting rules.
 */
message GetAlertingRulesResponse {
  // Alerting rules for the metric
  repeated AlertingRule rules = 1 [(buf.validate.field).repeated.min_items = 1];

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}
```

---

### get_metric_metadata_request.proto {#get_metric_metadata_request}

**Path**: `gcommon/v1/metrics/get_metric_metadata_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 51

**Messages** (1): `GetMetricMetadataRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_request.proto
// version: 1.0.0
// guid: 4706d64e-ea60-4994-a732-e8377db776b5
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_request.proto
//
// Request definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricMetadataRequest retrieves metadata for specific metrics.
 */
message GetMetricMetadataRequest {
  // Provider ID to query
  string provider_id = 1 [(buf.validate.field).string.min_len = 1];

  // Specific metric names to get metadata for (if empty, get all)
  repeated string metric_names = 2 [(buf.validate.field).repeated.min_items = 1];

  // Namespace to filter by (optional)
  string namespace = 3 [(buf.validate.field).string.min_len = 1];

  // Include inactive metrics
  bool include_inactive = 4;

  // Pagination options
  int32 page_size = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
  string page_token = 6 [(buf.validate.field).string.min_len = 1];

  // Filter by metric type (optional)
  string metric_type = 7 [(buf.validate.field).string.min_len = 1];

  // Filter by labels (optional)
  map<string, string> label_filters = 8;

  // Whether to include retention policy information
  bool include_retention_info = 9;

  // Whether to include usage statistics
  bool include_usage_stats = 10;
}
```

---

### get_metric_metadata_response.proto {#get_metric_metadata_response}

**Path**: `gcommon/v1/metrics/get_metric_metadata_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `GetMetricMetadataResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `gcommon/v1/metrics/pagination_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_response.proto
// version: 1.0.0
// guid: 118692f7-fe67-4e13-8a1f-416220925369
// file: proto/gcommon/v1/metrics/v1/get_metric_metadata_response.proto
//
// Response definitions for metrics module

//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "gcommon/v1/metrics/pagination_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricMetadataResponse contains metadata for requested metrics.
 */
message GetMetricMetadataResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Provider ID that handled the request
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Retrieved metadata entries
  repeated MetricMetadata metadata = 4;

  // Pagination information
  MetricsPaginationInfo pagination = 5;

  // Total number of matching metrics
  int64 total_count = 6 [(buf.validate.field).int64.gte = 0];

  // When the response was generated
  google.protobuf.Timestamp generated_at = 7;

  // Warnings or informational messages
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];

  // Query execution time in milliseconds
  int64 execution_time_ms = 9 [(buf.validate.field).int64.gte = 0];
}
```

---

### get_metric_request.proto {#get_metric_request}

**Path**: `gcommon/v1/metrics/get_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 27

**Messages** (1): `GetMetricRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_request.proto
// version: 1.0.0
// guid: 48d74623-574e-4253-b0dd-784417ffe50d
// file: proto/gcommon/v1/metrics/v1/get_metric_request.proto
//
// Request message for retrieving a metric by ID.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricRequest {
  // Unique metric identifier
  string metric_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_metric_response.proto {#get_metric_response}

**Path**: `gcommon/v1/metrics/get_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `GetMetricResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metric_response.proto
// version: 1.0.1
// guid: dc01ceeb-c2dd-4f50-9e0b-424293f1f529
// file: proto/gcommon/v1/metrics/v1/get_metric_response.proto
//
// Response containing a metric definition and data.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricResponse returns metric data.
 */
message GetMetricResponse {
  // Metric data requested
  MetricData metric = 1;

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2;
}
```

---

### get_metrics_request.proto {#get_metrics_request}

**Path**: `gcommon/v1/metrics/get_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `MetricsGetMetricsRequest`

**Imports** (8):

- `gcommon/v1/common/pagination_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metric_aggregation.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `gcommon/v1/metrics/output_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_request.proto
// version: 1.0.0
// guid: ec242bb6-5817-45b8-88de-7245b2536b35

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/pagination_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metric_aggregation.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "gcommon/v1/metrics/output_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsGetMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter to determine which metrics to retrieve
  MetricFilter filter = 2;

  // Time range for the request
  gcommon.v1.common.TimeRangeMetrics time_range = 3;

  // Aggregation options for the metrics
  MetricAggregation aggregation = 4;

  // Pagination options
  gcommon.v1.common.PaginationOptions pagination = 5;

  // Optional provider ID to query
  string provider_id = 6 [(buf.validate.field).string.min_len = 1];

  // Output format options
  OutputOptions output_options = 7;

  // Whether to include metadata with results
  bool include_metadata = 8;

  // Maximum number of metrics to return
  int32 limit = 9 [(buf.validate.field).int32.gte = 0];
}
```

---

### get_metrics_response.proto {#get_metrics_response}

**Path**: `gcommon/v1/metrics/get_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 59

**Messages** (1): `MetricsGetMetricsResponse`

**Imports** (9):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `gcommon/v1/metrics/pagination_info.proto`
- `gcommon/v1/metrics/query_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_response.proto
// version: 1.0.0
// guid: 55ced9dc-7d12-4f0b-883d-5e7de55a038e
// file: proto/gcommon/v1/metrics/v1/get_metrics_response.proto
//
// Get metrics response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "gcommon/v1/metrics/pagination_info.proto";
import "gcommon/v1/metrics/query_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetMetricsResponse contains the retrieved metrics data.
 */
message MetricsGetMetricsResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Retrieved metrics data
  repeated MetricData metrics = 3 [(buf.validate.field).repeated.min_items = 1];

  // Metadata for the metrics (if requested)
  repeated MetricMetadata metadata = 4;

  // Pagination information
  MetricsPaginationInfo pagination = 5;

  // Query execution statistics
  MetricsQueryStats stats = 6;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 7;

  // Time range covered by the response
  gcommon.v1.common.TimeRangeMetrics time_range = 8;

  // Warnings or informational messages
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Provider that handled the request
  string provider_id = 10 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_metrics_summary_request.proto {#get_metrics_summary_request}

**Path**: `gcommon/v1/metrics/get_metrics_summary_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `GetMetricsSummaryRequest`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metric_filter.proto`
- `gcommon/v1/metrics/summary_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_summary_request.proto
// version: 1.0.0
// guid: 9617cdf7-a614-4717-a660-aae208eb1774

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metric_filter.proto";
import "gcommon/v1/metrics/summary_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricsSummaryRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Optional filter to limit which metrics to include in summary
  MetricFilter filter = 2;

  // Time range for the summary
  gcommon.v1.common.TimeRangeMetrics time_range = 3;

  // What summary information to include
  SummaryOptions options = 4;

  // Optional provider ID to query
  string provider_id = 5 [(buf.validate.field).string.min_len = 1];

  // Whether to include provider-level statistics
  bool include_provider_stats = 6;

  // Whether to include health status information
  bool include_health_status = 7;
}
```

---

### get_metrics_summary_response.proto {#get_metrics_summary_response}

**Path**: `gcommon/v1/metrics/get_metrics_summary_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `GetMetricsSummaryResponse`

**Imports** (8):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/metrics_health_info.proto`
- `gcommon/v1/metrics/metrics_summary.proto`
- `gcommon/v1/metrics/provider_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_metrics_summary_response.proto
// version: 1.0.0
// guid: 9cd4897b-9464-4d95-adf3-9884dbc3d363

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/metrics_health_info.proto";
import "gcommon/v1/metrics/metrics_summary.proto";
import "gcommon/v1/metrics/provider_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetMetricsSummaryResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Summary information organized by category
  MetricsSummary summary = 3;

  // Provider-level statistics (if requested)
  repeated ProviderSummary provider_summaries = 4 [(buf.validate.field).repeated.min_items = 1];

  // Health status information (if requested)
  MetricsHealthInfo health_status = 5;

  // When the summary was generated
  google.protobuf.Timestamp generated_at = 6;

  // Time range covered by the summary
  gcommon.v1.common.TimeRangeMetrics time_range = 7;

  // Warnings or informational messages
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### get_provider_stats_request.proto {#get_provider_stats_request}

**Path**: `gcommon/v1/metrics/get_provider_stats_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `GetProviderStatsRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/stats_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_provider_stats_request.proto
// version: 1.0.0
// guid: 3325d42f-84b8-46c7-85ef-e324a05386d5

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/stats_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetProviderStatsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Provider ID to get stats for
  string provider_id = 2 [(buf.validate.field).string.min_len = 1];

  // Time range for statistics
  gcommon.v1.common.TimeRangeMetrics time_range = 3;

  // What statistics to include
  StatsOptions options = 4;

  // Granularity for time-series statistics
  string granularity = 5; // e.g., "1m", "5m", "1h"

  // Whether to include real-time metrics
  bool include_realtime = 6;
}
```

---

### get_provider_stats_response.proto {#get_provider_stats_response}

**Path**: `gcommon/v1/metrics/get_provider_stats_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 41

**Messages** (1): `GetProviderStatsResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/metrics/provider_statistics.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_provider_stats_response.proto
// version: 1.0.0
// guid: 26ba7b19-1782-4137-b19b-f6ee43e59f15

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/metrics/provider_statistics.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message GetProviderStatsResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Provider ID these stats are for
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Comprehensive provider statistics
  ProviderStatistics statistics = 4;

  // When the statistics were generated
  google.protobuf.Timestamp generated_at = 5;

  // Time range covered by the statistics
  gcommon.v1.common.TimeRangeMetrics time_range = 6;

  // Warnings or informational messages
  repeated string warnings = 7 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### get_stats_request.proto {#get_stats_request}

**Path**: `gcommon/v1/metrics/get_stats_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 31

**Messages** (1): `MetricsGetStatsRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/timestamp_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_stats_request.proto
// version: 1.0.0
// guid: 2595bd64-9fd4-4bfb-af86-63535bc068c1
// file: proto/gcommon/v1/metrics/v1/get_stats_request.proto
//
// Request for retrieving metric statistics over a time range.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/timestamp_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsGetStatsRequest {
  // Metric name or ID to query
  string metric = 1 [(buf.validate.field).string.min_len = 1];

  // Time range for stats
  MetricsTimestampRange range = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### get_stats_response.proto {#get_stats_response}

**Path**: `gcommon/v1/metrics/get_stats_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `MetricsGetStatsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/query_stats.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/get_stats_response.proto
// version: 1.0.1
// guid: d4229356-6c26-4e69-8437-475e88a0bdc6
// file: proto/gcommon/v1/metrics/v1/get_stats_response.proto
//
// Response containing metric statistics over a time range.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/query_stats.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * GetStatsResponse returns statistics for a metric.
 */
message MetricsGetStatsResponse {
  // Statistics for the query
  MetricsQueryStats stats = 1;

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/metrics/health_check_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 25

**Messages** (1): `MetricsHealthCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/health_check_request.proto
// version: 1.0.0
// guid: ffa1c922-b413-4b2d-a7fd-0d58fcd0b048
//
// HealthCheckRequest for the metrics module

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message MetricsHealthCheckRequest {
  // Metrics subsystem name (e.g., "prometheus").
  string subsystem = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/metrics/health_check_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `MetricsHealthCheckResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/health_check_response.proto
// version: 1.0.0
// guid: 2d9c7ce3-2e5b-42d7-9473-70bef7518cdd
//
// HealthCheckResponse for the metrics module
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * HealthCheckResponse contains the result of a metrics subsystem health check.
 */
message MetricsHealthCheckResponse {
  // Health status of the subsystem.
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Time taken to execute the health check.
  google.protobuf.Duration response_time = 2 [lazy = true];

  // Optional human-readable message.
  string message = 3 [(buf.validate.field).string.min_len = 1];

  // Error details if unhealthy.
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### import_metrics_request.proto {#import_metrics_request}

**Path**: `gcommon/v1/metrics/import_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 28

**Messages** (1): `ImportMetricsRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/import_metrics_request.proto
// version: 1.0.0
// guid: 761d0d0a-fb74-41bb-a5aa-e446fa8300bb
// file: proto/gcommon/v1/metrics/v1/import_metrics_request.proto
//
// Request message for importing multiple metrics.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ImportMetricsRequest {
  // Metrics to import
  repeated MetricData metrics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### import_metrics_response.proto {#import_metrics_response}

**Path**: `gcommon/v1/metrics/import_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 29

**Messages** (1): `ImportMetricsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/import_metrics_response.proto
// version: 1.0.0
// guid: 54556e65-80a3-4d79-b67e-d98ca9bf7b0e
// file: proto/gcommon/v1/metrics/v1/import_metrics_response.proto
//
// Response returned after importing metrics.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ImportMetricsResponse reports the result of a batch import.
 */
message ImportMetricsResponse {
  // Number of metrics successfully imported
  int32 imported_count = 1 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Error information if the import failed
  gcommon.v1.common.Error error = 2;
}
```

---

### list_metrics_request.proto {#list_metrics_request}

**Path**: `gcommon/v1/metrics/list_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 26

**Messages** (1): `ListMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/pagination.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_metrics_request.proto
// version: 1.0.0
// guid: a5ae698c-a783-4005-b054-167c31d44c8b

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/pagination.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ListMetricsRequest requests a paginated list of metrics.
 */
message ListMetricsRequest {
  // Pagination information
  gcommon.v1.common.Pagination pagination = 1;

  // Optional name filter
  string name_filter = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_metrics_response.proto {#list_metrics_response}

**Path**: `gcommon/v1/metrics/list_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `ListMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_metrics_response.proto
// version: 1.0.0
// guid: 12b3dcff-48a7-4a05-b427-45a55314dacb
// file: proto/gcommon/v1/metrics/v1/list_metrics_response.proto
//
// Response containing a list of metric metadata.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * ListMetricsResponse lists available metrics.
 */
message ListMetricsResponse {
  // Available metrics
  repeated MetricMetadata metrics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Error information
  gcommon.v1.common.Error error = 2;
}
```

---

### list_providers_request.proto {#list_providers_request}

**Path**: `gcommon/v1/metrics/list_providers_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 35

**Messages** (1): `ListProvidersRequest`

**Imports** (4):

- `gcommon/v1/common/pagination_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/provider_filter.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_providers_request.proto
// version: 1.0.1
// guid: cc2b7794-28e4-442f-88a3-24bcd696fe6a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/pagination_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/provider_filter.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ListProvidersRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Filter options for the list
  ProviderFilter filter = 2;

  // Pagination options
  gcommon.v1.common.PaginationOptions pagination = 3;

  // Whether to include detailed status information
  bool include_status = 4;

  // Whether to include configuration details
  bool include_config = 5;

  // Whether to include statistics
  bool include_stats = 6;
}
```

---

### list_providers_response.proto {#list_providers_response}

**Path**: `gcommon/v1/metrics/list_providers_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 39

**Messages** (1): `ListProvidersResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/pagination_info.proto`
- `gcommon/v1/metrics/provider_info.proto`
- `gcommon/v1/metrics/provider_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/list_providers_response.proto
// version: 1.0.0
// guid: ec44b05b-cb74-44b5-b495-4cf1e4c0877d

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/pagination_info.proto";
import "gcommon/v1/metrics/provider_info.proto";
import "gcommon/v1/metrics/provider_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message ListProvidersResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // List of providers
  repeated ProviderInfo providers = 3 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information
  MetricsPaginationInfo pagination = 4;

  // Summary statistics about the providers
  ProviderSummary summary = 5;

  // When the response was generated
  google.protobuf.Timestamp generated_at = 6;
}
```

---

### query_metrics_request.proto {#query_metrics_request}

**Path**: `gcommon/v1/metrics/query_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `QueryMetricsRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_query.proto`
- `gcommon/v1/metrics/query_output_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_metrics_request.proto
// version: 1.0.0
// guid: d6616950-fd6a-4863-9a2d-3c5bed911918

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_query.proto";
import "gcommon/v1/metrics/query_output_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // The metric query to execute
  MetricQuery query = 2;

  // Optional query timeout in seconds
  int32 timeout_seconds = 3 [(buf.validate.field).int32.gt = 0];

  // Whether to return query execution plan (for debugging)
  bool include_query_plan = 4;

  // Whether to return only metadata without actual values (for schema discovery)
  bool metadata_only = 5;

  // Output format preferences
  QueryOutputOptions output_options = 6;
}
```

---

### query_metrics_response.proto {#query_metrics_response}

**Path**: `gcommon/v1/metrics/query_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `QueryMetricsResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/metric_series.proto`
- `gcommon/v1/metrics/query_plan.proto`
- `gcommon/v1/metrics/query_statistics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_metrics_response.proto
// version: 1.0.0
// guid: 766d3060-cb60-4a59-8d9f-371e9f4e6eed

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/metric_series.proto";
import "gcommon/v1/metrics/query_plan.proto";
import "gcommon/v1/metrics/query_statistics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message QueryMetricsResponse {
  // Success status of the query
  bool success = 1;

  // Error information if query failed
  gcommon.v1.common.Error error = 2;

  // Query results organized as metric series
  repeated MetricSeries series = 3 [(buf.validate.field).repeated.min_items = 1];

  // Query execution statistics
  QueryStatistics statistics = 4;

  // Query execution plan (if requested)
  QueryPlan query_plan = 5;

  // Warnings or informational messages about the query
  repeated string warnings = 6 [(buf.validate.field).repeated.min_items = 1];

  // Pagination token for retrieving more results
  string next_page_token = 7 [(buf.validate.field).string.min_len = 1];

  // Total number of results available (for pagination)
  int64 total_results = 8 [(buf.validate.field).int64.gte = 0];
}
```

---

### record_counter_request.proto {#record_counter_request}

**Path**: `gcommon/v1/metrics/record_counter_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 46

**Messages** (1): `RecordCounterRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_counter_request.proto
// version: 1.0.0
// guid: af165336-0041-4c47-a00d-5f0470240fda
// file: proto/gcommon/v1/metrics/v1/record_counter_request.proto
//
// Record counter request definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordCounterRequest is used to record or increment a counter metric.
 */
message RecordCounterRequest {
  // Metric name (e.g., "http_requests_total")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Value to add to the counter (default: 1.0)
  double value = 2;

  // Labels for metric dimensions
  map<string, string> labels = 3;

  // Help text describing the metric
  string help = 4;

  // Metric unit (e.g., "requests", "bytes")
  string unit = 5;

  // Sample rate (0.0-1.0, used for sampling)
  double sample_rate = 6;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 7;
}
```

---

### record_counter_response.proto {#record_counter_response}

**Path**: `gcommon/v1/metrics/record_counter_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 37

**Messages** (1): `RecordCounterResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/counter_metric.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_counter_response.proto
// version: 1.0.1
// guid: 47ec1fef-7557-4265-802c-0988b554f2a3
// file: proto/gcommon/v1/metrics/v1/record_counter_response.proto
//
// Record counter response definitions for metrics module
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/counter_metric.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordCounterResponse {
  // Whether the operation was successful
  bool success = 1;

  // The recorded counter metric with updated value
  CounterMetric metric = 2;

  // Timestamp when the metric was recorded
  google.protobuf.Timestamp recorded_at = 3;

  // Error information if operation failed
  gcommon.v1.common.Error error = 4;

  // Response metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### record_gauge_request.proto {#record_gauge_request}

**Path**: `gcommon/v1/metrics/record_gauge_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 49

**Messages** (1): `RecordGaugeRequest`

**Imports** (5):

- `gcommon/v1/common/gauge_operation.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_gauge_request.proto
// version: 1.1.0
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/gauge_operation.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordGaugeRequest is used to set or update a gauge metric value.
 * Gauges can increase, decrease, or be set to specific values.
 */
message RecordGaugeRequest {
  // Metric name (e.g., "memory_usage_bytes", "cpu_usage_percent")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Value to set the gauge to
  double value = 2;

  // Labels for metric dimensions
  map<string, string> labels = 3;

  // Help text describing the metric
  string help = 4;

  // Metric unit (e.g., "bytes", "percent", "connections")
  string unit = 5;

  // Optional timestamp when the measurement was taken
  google.protobuf.Timestamp timestamp = 6;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 7;

  // Operation type for the gauge
  gcommon.v1.common.GaugeOperation operation = 8;
}
```

---

### record_gauge_response.proto {#record_gauge_response}

**Path**: `gcommon/v1/metrics/record_gauge_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `RecordGaugeResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/gauge_metric.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_gauge_response.proto
// version: 1.2.0
// guid: c1d2e3f4-g5h6-7890-i1j2-k3l4m5n6o7p8

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/gauge_metric.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordGaugeResponse is returned after recording a gauge metric.
 */
message RecordGaugeResponse {
  // Whether the operation was successful
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // The recorded gauge metric with updated value
  GaugeMetric metric = 3;

  // Previous value of the gauge (if applicable)
  double previous_value = 4 [(buf.validate.field).double.gte = 0.0];

  // Timestamp when the gauge was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Whether this was a new gauge or an update to existing
  bool is_new_metric = 6;

  // Processing statistics
  RecordingStats stats = 7;
}
```

---

### record_histogram_request.proto {#record_histogram_request}

**Path**: `gcommon/v1/metrics/record_histogram_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 55

**Messages** (1): `RecordHistogramRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_histogram_request.proto
// version: 1.0.0
// guid: 5d38efab-f98b-4ddf-8e50-08395f5e24fc
// file: proto/gcommon/v1/metrics/v1/record_histogram_request.proto
//
// Request definitions for metrics module

//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordHistogramRequest {
  // Metric name (e.g., "request_duration_seconds", "response_size_bytes")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Value to observe/record in the histogram
  double value = 2;

  // Labels for metric dimensions
  map<string, string> labels = 3;

  // Help text describing the metric
  string help = 4;

  // Metric unit (e.g., "seconds", "bytes", "milliseconds")
  string unit = 5;

  // Histogram bucket configuration (if not already defined)
  repeated double buckets = 6;

  // Optional timestamp when the observation was made
  google.protobuf.Timestamp timestamp = 7;

  // Request metadata for tracing and debugging
  gcommon.v1.common.RequestMetadata metadata = 8;

  // Optional sample weight (for weighted observations)
  double sample_weight = 9;

  // Whether to create the histogram if it doesn't exist
  bool create_if_missing = 10;
}
```

---

### record_histogram_response.proto {#record_histogram_response}

**Path**: `gcommon/v1/metrics/record_histogram_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 44

**Messages** (1): `RecordHistogramResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/bucket_info.proto`
- `gcommon/v1/metrics/histogram_metric.proto`
- `gcommon/v1/metrics/histogram_stats.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_histogram_response.proto
// version: 1.0.1
// guid: 33d2781c-78d0-4293-8c90-1a2b4e20c522

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/bucket_info.proto";
import "gcommon/v1/metrics/histogram_metric.proto";
import "gcommon/v1/metrics/histogram_stats.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordHistogramResponse {
  // Whether the operation was successful
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // The histogram metric with updated bucket counts
  HistogramMetric metric = 3;

  // Current histogram statistics
  HistogramStats current_stats = 4;

  // Timestamp when the observation was recorded
  google.protobuf.Timestamp recorded_at = 5;

  // Whether this was a new histogram or an update to existing
  bool is_new_metric = 6;

  // Bucket that the observation fell into
  BucketInfo affected_bucket = 7;

  // Processing statistics
  RecordingStats recording_stats = 8;
}
```

---

### record_metric_request.proto {#record_metric_request}

**Path**: `gcommon/v1/metrics/record_metric_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 38

**Messages** (1): `RecordMetricRequest`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/batch_context.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metric_request.proto
// version: 1.0.0
// guid: 8e0ace8f-cfd2-45c0-9e30-47eefe47b60f

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/batch_context.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordMetricRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // The metric data to record
  MetricData metric = 2;

  // Optional provider ID to use for recording
  string provider_id = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to validate the metric before recording
  bool validate = 4;

  // Timestamp override (if not provided, current time is used)
  google.protobuf.Timestamp timestamp = 5;

  // Batch context information (if this is part of a batch operation)
  BatchContext batch_context = 6;
}
```

---

### record_metric_response.proto {#record_metric_response}

**Path**: `gcommon/v1/metrics/record_metric_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 50

**Messages** (1): `RecordMetricResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metric_response.proto
// version: 1.0.0
// guid: f6b84950-9977-45e7-a9d6-1b3d9a800f62
// file: proto/gcommon/v1/metrics/v1/record_metric_response.proto
//
// Record metric response definitions for metrics module
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordMetricResponse contains the result of recording a metric data point.
 */
message RecordMetricResponse {
  // Success status of the operation
  bool success = 1;

  // Error information if the operation failed
  gcommon.v1.common.Error error = 2;

  // Unique ID assigned to the recorded metric (if applicable)
  string metric_id = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the metric was actually recorded
  google.protobuf.Timestamp recorded_at = 4;

  // Provider that handled the metric
  string provider_id = 5 [(buf.validate.field).string.min_len = 1];

  // Validation results if validation was requested
  gcommon.v1.common.MetricsValidationResult validation = 6;

  // Performance metrics about the recording operation
  RecordingStats stats = 7;

  // Warnings or informational messages
  repeated string warnings = 8 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### record_metrics_request.proto {#record_metrics_request}

**Path**: `gcommon/v1/metrics/record_metrics_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 36

**Messages** (1): `RecordMetricsRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/metric_data.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metrics_request.proto
// version: 1.0.0
// guid: a9b8c7d6-e5f4-3210-9876-543210abcdef

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/metric_data.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordMetricsRequest represents a batch request to record multiple metrics.
 */
message RecordMetricsRequest {
  // Standard request metadata (tracing, auth, etc.)
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Batch of metrics to record
  repeated MetricData metrics = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether to validate all metrics before recording any
  bool atomic = 3;

  // Optional batch ID for tracking
  string batch_id = 4 [(buf.validate.field).string.min_len = 1];

  // Maximum number of retries for failed metrics
  int32 max_retries = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### record_metrics_response.proto {#record_metrics_response}

**Path**: `gcommon/v1/metrics/record_metrics_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 54

**Messages** (1): `RecordMetricsResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/batch_stats.proto`
- `gcommon/v1/metrics/metric_result.proto`
- `gcommon/v1/metrics/validation_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_metrics_response.proto
// version: 1.0.0
// guid: 14d6d2f6-2386-4f1b-a00f-086e0bfb5653

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/batch_stats.proto";
import "gcommon/v1/metrics/metric_result.proto";
import "gcommon/v1/metrics/validation_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordMetricsResponse {
  // Overall success status of the batch operation
  bool success = 1;

  // Number of metrics successfully recorded
  int32 success_count = 2 [(buf.validate.field).int32.gte = 0];

  // Number of metrics that failed to record
  int32 failure_count = 3 [(buf.validate.field).int32.gte = 0];

  // Total number of metrics processed
  int32 total_count = 4 [(buf.validate.field).int32.gte = 0];

  // Overall error information if the batch operation failed
  gcommon.v1.common.Error error = 5;

  // Detailed results for each metric (if requested)
  repeated MetricResult results = 6 [(buf.validate.field).repeated.min_items = 1];

  // Timestamp when the batch operation was completed
  google.protobuf.Timestamp completed_at = 7;

  // Provider that handled the batch
  string provider_id = 8 [(buf.validate.field).string.min_len = 1];

  // Batch processing statistics
  MetricsBatchStats stats = 9;

  // Warnings or informational messages about the batch
  repeated string warnings = 10 [(buf.validate.field).repeated.min_items = 1];

  // Summary of validation results (if validation was enabled)
  ValidationSummary validation_summary = 11;
}
```

---

### record_summary_request.proto {#record_summary_request}

**Path**: `gcommon/v1/metrics/record_summary_request.proto` **Package**: `gcommon.v1.metrics` **Lines**: 30

**Messages** (1): `RecordSummaryRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/metrics/summary_metric.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_summary_request.proto
// version: 1.0.1
// guid: 5c052e01-88e7-4d02-b154-a1824090213b
// file: proto/gcommon/v1/metrics/v1/record_summary_request.proto
//
// Request message for recording a summary metric observation.
//

edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/metrics/summary_metric.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

message RecordSummaryRequest {
  // Summary metric data
  SummaryMetric metric = 1;

  // Optional timestamp for the observation
  google.protobuf.Timestamp observed_at = 2;

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### record_summary_response.proto {#record_summary_response}

**Path**: `gcommon/v1/metrics/record_summary_response.proto` **Package**: `gcommon.v1.metrics` **Lines**: 32

**Messages** (1): `RecordSummaryResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/metrics/recording_stats.proto`
- `gcommon/v1/metrics/summary_metric.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/record_summary_response.proto
// version: 1.0.1
// guid: d23c6f17-2028-4070-ad58-01c921f8f75d
// file: proto/gcommon/v1/metrics/v1/record_summary_response.proto
//
// Response after recording a summary metric.
//
edition = "2023";

package gcommon.v1.metrics;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/metrics/recording_stats.proto";
import "gcommon/v1/metrics/summary_metric.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/metrics";

/**
 * RecordSummaryResponse returns updated summary stats.
 */
message RecordSummaryResponse {
  // Updated summary metric
  SummaryMetric metric = 1;

  // Processing stats
  RecordingStats stats = 2;

  // Error information
  gcommon.v1.common.Error error = 3;
}
```

---

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

