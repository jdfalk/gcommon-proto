# Common Enums Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 218
- **Enums**: 218

## Table of Contents

### Enums

- [`AckLevel`](#ack_level) - from ack_level.proto
- [`AckMode`](#ack_mode) - from ack_mode.proto
- [`AckType`](#ack_type) - from ack_type.proto
- [`AcknowledgmentMode`](#acknowledgment_mode) - from acknowledgment_mode.proto
- [`AggregationType`](#aggregation_type) - from aggregation_type.proto
- [`AlertChannelType`](#alert_channel_type) - from alert_channel_type.proto
- [`AlertCondition`](#alert_condition) - from alert_condition.proto
- [`AlertState`](#alert_state) - from alert_state.proto
- [`AlertType`](#alert_type) - from alert_type.proto
- [`AntiAffinityScope`](#anti_affinity_scope) - from anti_affinity_scope.proto
- [`AppenderType`](#appender_type) - from appender_type.proto
- [`ApprovalStatus`](#approval_status) - from approval_status.proto
- [`AuditAction`](#audit_action) - from audit_action.proto
- [`AuditLevel`](#audit_level) - from audit_level.proto
- [`AuditOperationType`](#audit_operation_type) - from audit_operation_type.proto
- [`AuditResult`](#audit_result) - from audit_result.proto
- [`AuthAuthMethod`](#auth_method) - from auth_method.proto
- [`AuthPermissionLevel`](#permission_level) - from permission_level.proto
- [`AuthProviderType`](#provider_type) - from provider_type.proto
- [`AuthSubjectType`](#subject_type) - from subject_type.proto
- [`AuthTwoFaType`](#two_fa_type) - from two_fa_type.proto
- [`AuthVerificationType`](#verification_type) - from verification_type.proto
- [`BackoffStrategy`](#backoff_strategy) - from backoff_strategy.proto
- [`BackupFrequency`](#backup_frequency) - from backup_frequency.proto
- [`BatchPriority`](#batch_priority) - from batch_priority.proto
- [`BufferOverflowStrategy`](#buffer_overflow_strategy) - from buffer_overflow_strategy.proto
- [`CacheInvalidationTrigger`](#cache_invalidation_trigger) - from cache_invalidation_trigger.proto
- [`CacheRefreshStrategy`](#cache_refresh_strategy) - from cache_refresh_strategy.proto
- [`CacheStrategy`](#cache_strategy) - from cache_strategy.proto
- [`ChannelType`](#channel_type) - from channel_type.proto
- [`CheckType`](#check_type) - from check_type.proto
- [`CircuitBreakerState`](#circuit_breaker_state) - from circuit_breaker_state.proto
- [`CleanupStrategy`](#cleanup_strategy) - from cleanup_strategy.proto
- [`ClusterState`](#cluster_state) - from cluster_state.proto
- [`CommonAlertSeverity`](#alert_severity) - from alert_severity.proto
- [`CommonExportFormat`](#export_format) - from export_format.proto
- [`CommonHealthStatus`](#health_status) - from health_status.proto
- [`ComparisonOperator`](#comparison_operator) - from comparison_operator.proto
- [`CompressionAlgorithm`](#compression_algorithm) - from compression_algorithm.proto
- [`ConfigAlertSeverity`](#config_alert_severity) - from config_alert_severity.proto
- [`ConfigChangeType`](#config_config_change_type) - from config_config_change_type.proto
- [`ConfigDataType`](#config_data_type) - from config_data_type.proto
- [`ConflictResolution`](#conflict_resolution) - from conflict_resolution.proto
- [`ConflictStrategy`](#conflict_strategy) - from conflict_strategy.proto
- [`ConsumerGroupState`](#consumer_group_state) - from consumer_group_state.proto
- [`ConsumerState`](#consumer_state) - from consumer_state.proto
- [`ContentType`](#content_type) - from content_type.proto
- [`CookieSameSite`](#cookie_same_site) - from cookie_same_site.proto
- [`CoordinatorState`](#coordinator_state) - from coordinator_state.proto
- [`DashboardType`](#dashboard_type) - from dashboard_type.proto
- [`DatabaseConsistencyLevel`](#consistency_level) - from consistency_level.proto
- [`DatabaseIsolationLevel`](#database_isolation_level) - from database_isolation_level.proto
- [`DatabaseStatusCode`](#database_status_code) - from database_status_code.proto
- [`DeliveryChannelType`](#delivery_channel_type) - from delivery_channel_type.proto
- [`DeliveryMode`](#delivery_mode) - from delivery_mode.proto
- [`DeliveryStatus`](#delivery_status) - from delivery_status.proto
- [`DependencyType`](#dependency_type) - from dependency_type.proto
- [`DeploymentStatus`](#deployment_status) - from deployment_status.proto
- [`DeprecationLevel`](#deprecation_level) - from deprecation_level.proto
- [`DurabilityLevel`](#durability_level) - from durability_level.proto
- [`EnvironmentStatus`](#environment_status) - from environment_status.proto
- [`EnvironmentType`](#environment_type) - from environment_type.proto
- [`ErrorCode`](#error_code) - from error_code.proto
- [`EvictionPolicy`](#eviction_policy) - from eviction_policy.proto
- [`ExpirationPolicy`](#expiration_policy) - from expiration_policy.proto
- [`FileSortOrder`](#file_sort_order) - from file_sort_order.proto
- [`FilterAction`](#filter_action) - from filter_action.proto
- [`FilterOperation`](#filter_operation) - from filter_operation.proto
- [`FlushPolicy`](#flush_policy) - from flush_policy.proto
- [`FormatterType`](#formatter_type) - from formatter_type.proto
- [`GaugeOperation`](#gauge_operation) - from gauge_operation.proto
- [`GrantType`](#grant_type) - from grant_type.proto
- [`HTTPMethod`](#http_method) - from http_method.proto
- [`HTTPStatus`](#http_status) - from http_status.proto
- [`HandlerType`](#handler_type) - from handler_type.proto
- [`HealthCheckType`](#health_check_type) - from health_check_type.proto
- [`HealthState`](#health_state) - from health_state.proto
- [`HierarchyType`](#hierarchy_type) - from hierarchy_type.proto
- [`HookErrorHandling`](#hook_error_handling) - from hook_error_handling.proto
- [`HookType`](#hook_type) - from hook_type.proto
- [`InheritanceStrategy`](#inheritance_strategy) - from inheritance_strategy.proto
- [`LoadBalanceStrategy`](#load_balance_strategy) - from load_balance_strategy.proto
- [`LoadBalancingStrategy`](#load_balancing_strategy) - from load_balancing_strategy.proto
- [`LogCompressionType`](#compression_type) - from compression_type.proto
- [`LogFilterType`](#filter_type) - from filter_type.proto
- [`LogLevel`](#log_level) - from log_level.proto
- [`LogSortField`](#log_sort_field) - from log_sort_field.proto
- [`LoggerStatus`](#logger_status) - from logger_status.proto
- [`MFAType`](#mfa_type) - from mfa_type.proto
- [`MediaType`](#media_type) - from media_type.proto
- [`MemberRole`](#member_role) - from member_role.proto
- [`MergeStrategy`](#merge_strategy) - from merge_strategy.proto
- [`MessageState`](#message_state) - from message_state.proto
- [`MetadataStatus`](#metadata_status) - from metadata_status.proto
- [`MetricSource`](#metric_source) - from metric_source.proto
- [`MetricStatus`](#metric_status) - from metric_status.proto
- [`MetricsAlertSeverity`](#metrics_alert_severity) - from metrics_alert_severity.proto
- [`MetricsChangeType`](#change_type) - from change_type.proto
- [`MetricsExportFormat`](#metrics_export_format) - from metrics_export_format.proto
- [`MetricsMetricType`](#metric_type) - from metric_type.proto
- [`MetricsProviderType`](#metrics_provider_type) - from metrics_provider_type.proto
- [`MetricsRetentionPolicy`](#retention_policy) - from retention_policy.proto
- [`MfaMethod`](#mfa_method) - from mfa_method.proto
- [`MiddlewareType`](#middleware_type) - from middleware_type.proto
- [`NackErrorCategory`](#nack_error_category) - from nack_error_category.proto
- [`NodeState`](#node_state) - from node_state.proto
- [`NotificationChannelType`](#notification_channel_type) - from notification_channel_type.proto
- [`NotificationTrigger`](#notification_trigger) - from notification_trigger.proto
- [`NotificationType`](#notification_type) - from notification_type.proto
- [`NumericFormat`](#numeric_format) - from numeric_format.proto
- [`OAuth2FlowType`](#oauth2_flow_type) - from oauth2_flow_type.proto
- [`OffsetResetStrategy`](#offset_reset_strategy) - from offset_reset_strategy.proto
- [`OffsetType`](#offset_type) - from offset_type.proto
- [`OrderingLevel`](#ordering_level) - from ordering_level.proto
- [`OrganizationIsolationLevel`](#isolation_level) - from isolation_level.proto
- [`OrganizationStatus`](#organization_status) - from organization_status.proto
- [`ParameterType`](#parameter_type) - from parameter_type.proto
- [`PartitionStrategy`](#partition_strategy) - from partition_strategy.proto
- [`PermissionScope`](#permission_scope) - from permission_scope.proto
- [`PermissionType`](#permission_type) - from permission_type.proto
- [`PriorityLevel`](#priority_level) - from priority_level.proto
- [`ProcessingStatus`](#processing_status) - from processing_status.proto
- [`ProviderState`](#provider_state) - from provider_state.proto
- [`ProxyType`](#proxy_type) - from proxy_type.proto
- [`QualityScore`](#quality_score) - from quality_score.proto
- [`QueryOperation`](#query_operation) - from query_operation.proto
- [`QueueAlertSeverity`](#queue_alert_severity) - from queue_alert_severity.proto
- [`QueueConsistencyLevel`](#queue_consistency_level) - from queue_consistency_level.proto
- [`QueueExportFormat`](#queue_export_format) - from queue_export_format.proto
- [`QueueMetricType`](#queue_metric_type) - from queue_metric_type.proto
- [`QueueState`](#queue_state) - from queue_state.proto
- [`QueueType`](#queue_type) - from queue_type.proto
- [`RateLimitStrategy`](#rate_limit_strategy) - from rate_limit_strategy.proto
- [`ReadLevel`](#read_level) - from read_level.proto
- [`RebalanceStrategy`](#rebalance_strategy) - from rebalance_strategy.proto
- [`ReferenceType`](#reference_type) - from reference_type.proto
- [`RegistrationAction`](#registration_action) - from registration_action.proto
- [`ReplicationLevel`](#replication_level) - from replication_level.proto
- [`ReplicationMode`](#replication_mode) - from replication_mode.proto
- [`Resolution`](#resolution) - from resolution.proto
- [`ResolutionStrategy`](#resolution_strategy) - from resolution_strategy.proto
- [`ResourceStatus`](#resource_status) - from resource_status.proto
- [`ResponseCompression`](#response_compression) - from response_compression.proto
- [`RestorePointStatus`](#restore_point_status) - from restore_point_status.proto
- [`RestorePointType`](#restore_point_type) - from restore_point_type.proto
- [`RestrictionType`](#restriction_type) - from restriction_type.proto
- [`RetentionUnit`](#retention_unit) - from retention_unit.proto
- [`RetryDelayStrategy`](#retry_delay_strategy) - from retry_delay_strategy.proto
- [`RoleScope`](#role_scope) - from role_scope.proto
- [`RollbackMethod`](#rollback_method) - from rollback_method.proto
- [`RotationFrequency`](#rotation_frequency) - from rotation_frequency.proto
- [`RouteType`](#route_type) - from route_type.proto
- [`RoutingPattern`](#routing_pattern) - from routing_pattern.proto
- [`RoutingStrategy`](#routing_strategy) - from routing_strategy.proto
- [`SSLProtocol`](#ssl_protocol) - from ssl_protocol.proto
- [`SameSitePolicy`](#same_site_policy) - from same_site_policy.proto
- [`SampleRate`](#sample_rate) - from sample_rate.proto
- [`SchemaCompatibilityMode`](#schema_compatibility_mode) - from schema_compatibility_mode.proto
- [`SchemaEvolutionStrategy`](#schema_evolution_strategy) - from schema_evolution_strategy.proto
- [`SchemaFormat`](#schema_format) - from schema_format.proto
- [`ScopeType`](#scope_type) - from scope_type.proto
- [`ScrapeStatus`](#scrape_status) - from scrape_status.proto
- [`SecretAuditLevel`](#secret_audit_level) - from secret_audit_level.proto
- [`SecretBackupFrequency`](#secret_backup_frequency) - from secret_backup_frequency.proto
- [`SecretStatus`](#secret_status) - from secret_status.proto
- [`SecretType`](#secret_type) - from secret_type.proto
- [`SecretValidationResultType`](#secret_validation_result_type) - from secret_validation_result_type.proto
- [`SecretValidationSeverity`](#secret_validation_severity) - from secret_validation_severity.proto
- [`SerializationFormat`](#serialization_format) - from serialization_format.proto
- [`ServerState`](#server_state) - from server_state.proto
- [`ServerStatus`](#server_status) - from server_status.proto
- [`ServingStatus`](#serving_status) - from serving_status.proto
- [`SessionState`](#session_state) - from session_state.proto
- [`SessionStatus`](#session_status) - from session_status.proto
- [`SortDirection`](#sort_direction) - from sort_direction.proto
- [`SortField`](#sort_field) - from sort_field.proto
- [`StatisticGrouping`](#statistic_grouping) - from statistic_grouping.proto
- [`StatisticType`](#statistic_type) - from statistic_type.proto
- [`StatsGranularity`](#stats_granularity) - from stats_granularity.proto
- [`StorageBackend`](#storage_backend) - from storage_backend.proto
- [`StreamCompression`](#stream_compression) - from stream_compression.proto
- [`StreamQOS`](#stream_qos) - from stream_qos.proto
- [`StreamRestartPolicy`](#stream_restart_policy) - from stream_restart_policy.proto
- [`SubscriptionState`](#subscription_state) - from subscription_state.proto
- [`SubscriptionStatus`](#subscription_status) - from subscription_status.proto
- [`SubtitleFormat`](#subtitle_format) - from subtitle_format.proto
- [`SynchronizationFrequency`](#synchronization_frequency) - from synchronization_frequency.proto
- [`TemplateChangeType`](#config_change_type) - from config_change_type.proto
- [`TemplateFormat`](#template_format) - from template_format.proto
- [`TemplateStatus`](#template_status) - from template_status.proto
- [`TenantStatus`](#tenant_status) - from tenant_status.proto
- [`TimeUnit`](#time_unit) - from time_unit.proto
- [`TimeWindow`](#time_window) - from time_window.proto
- [`TokenStatus`](#token_status) - from token_status.proto
- [`TokenType`](#token_type) - from token_type.proto
- [`TransformationType`](#transformation_type) - from transformation_type.proto
- [`UpdateAction`](#update_action) - from update_action.proto
- [`UpdateStrategy`](#update_strategy) - from update_strategy.proto
- [`UserStatus`](#user_status) - from user_status.proto
- [`ValidationResultType`](#validation_result_type) - from validation_result_type.proto
- [`ValidationRuleSeverity`](#validation_rule_severity) - from validation_rule_severity.proto
- [`ValidationRuleType`](#validation_rule_type) - from validation_rule_type.proto
- [`ValidationSeverity`](#validation_severity) - from validation_severity.proto
- [`ValueSource`](#value_source) - from value_source.proto
- [`ValueStatus`](#value_status) - from value_status.proto
- [`ValueType`](#value_type) - from value_type.proto
- [`ValueValidationResultType`](#value_validation_result_type) - from value_validation_result_type.proto
- [`ValueValidationSeverity`](#value_validation_severity) - from value_validation_severity.proto
- [`VersionDependencyType`](#version_dependency_type) - from version_dependency_type.proto
- [`VersionDeploymentStatus`](#version_deployment_status) - from version_deployment_status.proto
- [`VersionHealthStatus`](#version_health_status) - from version_health_status.proto
- [`VersionStatus`](#version_status) - from version_status.proto
- [`VersionType`](#version_type) - from version_type.proto
- [`VisualizationType`](#visualization_type) - from visualization_type.proto
- [`WebAuthMethod`](#web_auth_method) - from web_auth_method.proto
- [`WebSessionState`](#web_session_state) - from web_session_state.proto
- [`WebSocketState`](#web_socket_state) - from web_socket_state.proto
- [`WriteLevel`](#write_level) - from write_level.proto

### Files in this Module

- [acknowledgment_mode.proto](#acknowledgment_mode)
- [aggregation_type.proto](#aggregation_type)
- [alert_channel_type.proto](#alert_channel_type)
- [alert_condition.proto](#alert_condition)
- [alert_severity.proto](#alert_severity)
- [alert_state.proto](#alert_state)
- [alert_type.proto](#alert_type)
- [anti_affinity_scope.proto](#anti_affinity_scope)
- [appender_type.proto](#appender_type)
- [approval_status.proto](#approval_status)
- [audit_action.proto](#audit_action)
- [audit_level.proto](#audit_level)
- [audit_operation_type.proto](#audit_operation_type)
- [audit_result.proto](#audit_result)
- [auth_method.proto](#auth_method)
- [backoff_strategy.proto](#backoff_strategy)
- [buffer_overflow_strategy.proto](#buffer_overflow_strategy)
- [cache_invalidation_trigger.proto](#cache_invalidation_trigger)
- [cache_refresh_strategy.proto](#cache_refresh_strategy)
- [cache_strategy.proto](#cache_strategy)
- [channel_type.proto](#channel_type)
- [check_type.proto](#check_type)
- [circuit_breaker_state.proto](#circuit_breaker_state)
- [cleanup_strategy.proto](#cleanup_strategy)
- [cluster_state.proto](#cluster_state)
- [comparison_operator.proto](#comparison_operator)
- [compression_algorithm.proto](#compression_algorithm)
- [compression_type.proto](#compression_type)
- [conflict_resolution.proto](#conflict_resolution)
- [conflict_strategy.proto](#conflict_strategy)
- [consistency_level.proto](#consistency_level)
- [consumer_group_state.proto](#consumer_group_state)
- [consumer_state.proto](#consumer_state)
- [content_type.proto](#content_type)
- [cookie_same_site.proto](#cookie_same_site)
- [coordinator_state.proto](#coordinator_state)
- [dashboard_type.proto](#dashboard_type)
- [database_isolation_level.proto](#database_isolation_level)
- [database_status_code.proto](#database_status_code)
- [delivery_channel_type.proto](#delivery_channel_type)
- [delivery_mode.proto](#delivery_mode)
- [delivery_status.proto](#delivery_status)
- [dependency_type.proto](#dependency_type)
- [deployment_status.proto](#deployment_status)
- [deprecation_level.proto](#deprecation_level)
- [durability_level.proto](#durability_level)
- [environment_status.proto](#environment_status)
- [environment_type.proto](#environment_type)
- [error_code.proto](#error_code)
- [eviction_policy.proto](#eviction_policy)
- [expiration_policy.proto](#expiration_policy)
- [export_format.proto](#export_format)
- [file_sort_order.proto](#file_sort_order)
- [filter_action.proto](#filter_action)
- [filter_operation.proto](#filter_operation)
- [filter_type.proto](#filter_type)
- [flush_policy.proto](#flush_policy)
- [formatter_type.proto](#formatter_type)
- [gauge_operation.proto](#gauge_operation)
- [grant_type.proto](#grant_type)
- [handler_type.proto](#handler_type)
- [health_check_type.proto](#health_check_type)
- [health_state.proto](#health_state)
- [health_status.proto](#health_status)
- [hierarchy_type.proto](#hierarchy_type)
- [hook_error_handling.proto](#hook_error_handling)
- [hook_type.proto](#hook_type)
- [http_method.proto](#http_method)
- [http_status.proto](#http_status)
- [inheritance_strategy.proto](#inheritance_strategy)
- [isolation_level.proto](#isolation_level)
- [load_balance_strategy.proto](#load_balance_strategy)
- [load_balancing_strategy.proto](#load_balancing_strategy)
- [log_level.proto](#log_level)
- [log_sort_field.proto](#log_sort_field)
- [logger_status.proto](#logger_status)
- [media_type.proto](#media_type)
- [member_role.proto](#member_role)
- [merge_strategy.proto](#merge_strategy)
- [message_state.proto](#message_state)
- [metadata_status.proto](#metadata_status)
- [metric_source.proto](#metric_source)
- [metric_status.proto](#metric_status)
- [metric_type.proto](#metric_type)
- [metrics_alert_severity.proto](#metrics_alert_severity)
- [metrics_export_format.proto](#metrics_export_format)
- [metrics_provider_type.proto](#metrics_provider_type)
- [mfa_method.proto](#mfa_method)
- [mfa_type.proto](#mfa_type)
- [middleware_type.proto](#middleware_type)
- [nack_error_category.proto](#nack_error_category)
- [node_state.proto](#node_state)
- [notification_channel_type.proto](#notification_channel_type)
- [notification_trigger.proto](#notification_trigger)
- [notification_type.proto](#notification_type)
- [numeric_format.proto](#numeric_format)
- [oauth2_flow_type.proto](#oauth2_flow_type)
- [offset_reset_strategy.proto](#offset_reset_strategy)
- [offset_type.proto](#offset_type)
- [ordering_level.proto](#ordering_level)
- [organization_status.proto](#organization_status)
- [parameter_type.proto](#parameter_type)
- [partition_strategy.proto](#partition_strategy)
- [permission_level.proto](#permission_level)
- [permission_scope.proto](#permission_scope)
- [permission_type.proto](#permission_type)
- [priority_level.proto](#priority_level)
- [processing_status.proto](#processing_status)
- [provider_state.proto](#provider_state)
- [provider_type.proto](#provider_type)
- [proxy_type.proto](#proxy_type)
- [quality_score.proto](#quality_score)
- [query_operation.proto](#query_operation)
- [rate_limit_strategy.proto](#rate_limit_strategy)
- [read_level.proto](#read_level)
- [rebalance_strategy.proto](#rebalance_strategy)
- [reference_type.proto](#reference_type)
- [registration_action.proto](#registration_action)
- [replication_level.proto](#replication_level)
- [replication_mode.proto](#replication_mode)
- [resolution.proto](#resolution)
- [resolution_strategy.proto](#resolution_strategy)
- [resource_status.proto](#resource_status)
- [response_compression.proto](#response_compression)
- [restriction_type.proto](#restriction_type)
- [retention_policy.proto](#retention_policy)
- [retention_unit.proto](#retention_unit)
- [retry_delay_strategy.proto](#retry_delay_strategy)
- [role_scope.proto](#role_scope)
- [rotation_frequency.proto](#rotation_frequency)
- [route_type.proto](#route_type)
- [routing_pattern.proto](#routing_pattern)
- [routing_strategy.proto](#routing_strategy)
- [same_site_policy.proto](#same_site_policy)
- [sample_rate.proto](#sample_rate)
- [schema_compatibility_mode.proto](#schema_compatibility_mode)
- [schema_evolution_strategy.proto](#schema_evolution_strategy)
- [schema_format.proto](#schema_format)
- [scope_type.proto](#scope_type)
- [scrape_status.proto](#scrape_status)
- [secret_audit_level.proto](#secret_audit_level)
- [secret_backup_frequency.proto](#secret_backup_frequency)
- [secret_status.proto](#secret_status)
- [secret_type.proto](#secret_type)
- [secret_validation_result_type.proto](#secret_validation_result_type)
- [secret_validation_severity.proto](#secret_validation_severity)
- [serialization_format.proto](#serialization_format)
- [server_state.proto](#server_state)
- [server_status.proto](#server_status)
- [serving_status.proto](#serving_status)
- [session_state.proto](#session_state)
- [session_status.proto](#session_status)
- [sort_direction.proto](#sort_direction)
- [sort_field.proto](#sort_field)
- [ssl_protocol.proto](#ssl_protocol)
- [statistic_grouping.proto](#statistic_grouping)
- [statistic_type.proto](#statistic_type)
- [stats_granularity.proto](#stats_granularity)
- [storage_backend.proto](#storage_backend)
- [stream_compression.proto](#stream_compression)
- [stream_qos.proto](#stream_qos)
- [stream_restart_policy.proto](#stream_restart_policy)
- [subject_type.proto](#subject_type)
- [subscription_state.proto](#subscription_state)
- [subscription_status.proto](#subscription_status)
- [subtitle_format.proto](#subtitle_format)
- [synchronization_frequency.proto](#synchronization_frequency)
- [template_format.proto](#template_format)
- [template_status.proto](#template_status)
- [tenant_status.proto](#tenant_status)
- [time_unit.proto](#time_unit)
- [time_window.proto](#time_window)
- [token_status.proto](#token_status)
- [token_type.proto](#token_type)
- [transformation_type.proto](#transformation_type)
- [two_fa_type.proto](#two_fa_type)
- [user_status.proto](#user_status)
- [validation_result_type.proto](#validation_result_type)
- [validation_rule_severity.proto](#validation_rule_severity)
- [validation_rule_type.proto](#validation_rule_type)
- [validation_severity.proto](#validation_severity)
- [value_source.proto](#value_source)
- [value_status.proto](#value_status)
- [value_type.proto](#value_type)
- [value_validation_result_type.proto](#value_validation_result_type)
- [value_validation_severity.proto](#value_validation_severity)
- [verification_type.proto](#verification_type)
- [version_dependency_type.proto](#version_dependency_type)
- [version_deployment_status.proto](#version_deployment_status)
- [version_health_status.proto](#version_health_status)
- [version_status.proto](#version_status)
- [version_type.proto](#version_type)
- [visualization_type.proto](#visualization_type)
- [web_auth_method.proto](#web_auth_method)
- [web_session_state.proto](#web_session_state)
- [web_socket_state.proto](#web_socket_state)
- [write_level.proto](#write_level)
- [config_alert_severity.proto](#config_alert_severity)
- [config_change_type.proto](#config_change_type)
- [config_config_change_type.proto](#config_config_change_type)
- [config_data_type.proto](#config_data_type)
- [ack_level.proto](#ack_level)
- [ack_mode.proto](#ack_mode)
- [ack_type.proto](#ack_type)
- [backup_frequency.proto](#backup_frequency)
- [batch_priority.proto](#batch_priority)
- [change_type.proto](#change_type)
- [queue_alert_severity.proto](#queue_alert_severity)
- [queue_consistency_level.proto](#queue_consistency_level)
- [queue_export_format.proto](#queue_export_format)
- [queue_metric_type.proto](#queue_metric_type)
- [queue_state.proto](#queue_state)
- [queue_type.proto](#queue_type)
- [restore_point_status.proto](#restore_point_status)
- [restore_point_type.proto](#restore_point_type)
- [rollback_method.proto](#rollback_method)
- [update_action.proto](#update_action)
- [update_strategy.proto](#update_strategy)

---

## Enums Documentation

### acknowledgment_mode.proto {#acknowledgment_mode}

**Path**: `gcommon/v1/common/acknowledgment_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `AcknowledgmentMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/acknowledgment_mode.proto
// version: 1.0.1
// guid: 6f4b2414-998e-4fc3-bc68-188dff6d2f25

// Enumeration describing how message acknowledgments are handled by a
// queue consumer. This was previously left as a placeholder during the
// 1-1-1 migration.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AcknowledgmentMode specifies how a message should be acknowledged
// by the consumer. It provides flexibility for different delivery
// guarantees and consumer implementations.
enum AcknowledgmentMode {
  // Default mode. The broker chooses a sensible default based on
  // queue configuration.
  ACKNOWLEDGMENT_MODE_UNSPECIFIED = 0;

  // Messages are automatically acknowledged immediately after
  // successful processing by the consumer.
  ACKNOWLEDGMENT_MODE_AUTO = 1;

  // The consumer is responsible for explicitly sending an AckRequest
  // after processing the message.
  ACKNOWLEDGMENT_MODE_MANUAL = 2;

  // No acknowledgment is required. Messages are considered processed
  // once delivered. Use with care.
  ACKNOWLEDGMENT_MODE_NONE = 3;
}
```

---

### aggregation_type.proto {#aggregation_type}

**Path**: `gcommon/v1/common/aggregation_type.proto` **Package**: `gcommon.v1.common` **Lines**: 59

**Enums** (1): `AggregationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/types/aggregation_type.proto
// version: 1.0.1
// guid: ab90e4af-40b2-4a70-94d5-3aef1bf40b63
// file: proto/gcommon/v1/metrics/aggregation_type.proto
//
// Aggregation type enum definitions for metrics module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AggregationType defines how metrics should be aggregated over time.
 */
enum AggregationType {
  // Unspecified aggregation type
  AGGREGATION_TYPE_UNSPECIFIED = 0;

  // Sum all values
  AGGREGATION_TYPE_SUM = 1;

  // Average all values
  AGGREGATION_TYPE_AVERAGE = 2;

  // Take minimum value
  AGGREGATION_TYPE_MIN = 3;

  // Take maximum value
  AGGREGATION_TYPE_MAX = 4;

  // Count number of values
  AGGREGATION_TYPE_COUNT = 5;

  // Standard deviation
  AGGREGATION_TYPE_STDDEV = 6;

  // Variance
  AGGREGATION_TYPE_VARIANCE = 7;

  // Median (50th percentile)
  AGGREGATION_TYPE_MEDIAN = 8;

  // 95th percentile
  AGGREGATION_TYPE_P95 = 9;

  // 99th percentile
  AGGREGATION_TYPE_P99 = 10;

  // Rate of change
  AGGREGATION_TYPE_RATE = 11;

  // Increase over time
  AGGREGATION_TYPE_INCREASE = 12;
}
```

---

### alert_channel_type.proto {#alert_channel_type}

**Path**: `gcommon/v1/common/alert_channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `AlertChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/alert_channel_type.proto
// version: 1.0.1
// guid: 6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AlertChannelType represents different types of alert channels
enum AlertChannelType {
  // Unspecified alert channel type
  ALERT_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email notification
  ALERT_CHANNEL_TYPE_EMAIL = 1;

  // Slack notification
  ALERT_CHANNEL_TYPE_SLACK = 2;

  // PagerDuty notification
  ALERT_CHANNEL_TYPE_PAGERDUTY = 3;

  // Webhook notification
  ALERT_CHANNEL_TYPE_WEBHOOK = 4;

  // SMS notification
  ALERT_CHANNEL_TYPE_SMS = 5;

  // Microsoft Teams notification
  ALERT_CHANNEL_TYPE_TEAMS = 6;

  // Discord notification
  ALERT_CHANNEL_TYPE_DISCORD = 7;

  // Telegram notification
  ALERT_CHANNEL_TYPE_TELEGRAM = 8;

  // Push notification
  ALERT_CHANNEL_TYPE_PUSH = 9;

  // JIRA ticket creation
  ALERT_CHANNEL_TYPE_JIRA = 10;

  // ServiceNow incident creation
  ALERT_CHANNEL_TYPE_SERVICENOW = 11;

  // Custom alert channel
  ALERT_CHANNEL_TYPE_CUSTOM = 12;
}
```

---

### alert_condition.proto {#alert_condition}

**Path**: `gcommon/v1/common/alert_condition.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `AlertCondition`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alert_condition.proto
// version: 1.0.1
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Condition types for alerts.
 */
enum AlertCondition {
  // Default unspecified condition
  ALERT_CONDITION_UNSPECIFIED = 0;

  // Metric greater than threshold
  ALERT_CONDITION_GREATER_THAN = 1;

  // Metric less than threshold
  ALERT_CONDITION_LESS_THAN = 2;

  // Metric equal to threshold
  ALERT_CONDITION_EQUALS = 3;

  // Metric not equal to threshold
  ALERT_CONDITION_NOT_EQUALS = 4;

  // Metric increasing rapidly
  ALERT_CONDITION_INCREASING = 5;

  // Metric decreasing rapidly
  ALERT_CONDITION_DECREASING = 6;
}
```

---

### alert_severity.proto {#alert_severity}

**Path**: `gcommon/v1/common/alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Enums** (1): `CommonAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/alert_severity.proto
// version: 1.0.1
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AlertSeverity enumerates alert severity levels used across all systems
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonAlertSeverity {
  ALERT_SEVERITY_UNSPECIFIED = 0;
  ALERT_SEVERITY_LOW = 1;
  ALERT_SEVERITY_MEDIUM = 2;
  ALERT_SEVERITY_HIGH = 3;
  ALERT_SEVERITY_CRITICAL = 4;
  ALERT_SEVERITY_INFO = 5; // From queue version
  ALERT_SEVERITY_WARNING = 6; // From queue version
  ALERT_SEVERITY_ERROR = 7; // From queue version
}
```

---

### alert_state.proto {#alert_state}

**Path**: `gcommon/v1/common/alert_state.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Enums** (1): `AlertState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alert_state.proto
// version: 1.0.1
// guid: a1dd0c23-a3f3-4e37-a662-d61897f80c3a
// file: proto/gcommon/v1/metrics/v1/alert_state.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AlertState defines the current state of a metric alert.
 * Represents the lifecycle states of alerts from creation to resolution.
 */
enum AlertState {
  // Unspecified state (default)
  ALERT_STATE_UNSPECIFIED = 0;

  // Alert condition is being evaluated but hasn't triggered
  ALERT_STATE_PENDING = 1;

  // Alert condition has been met and is actively firing
  ALERT_STATE_FIRING = 2;

  // Alert was firing but condition is no longer met
  ALERT_STATE_RESOLVED = 3;

  // Alert has been acknowledged by an operator
  ALERT_STATE_ACKNOWLEDGED = 4;

  // Alert has been manually silenced/suppressed
  ALERT_STATE_SILENCED = 5;

  // Alert is in an error state (evaluation failed)
  ALERT_STATE_ERROR = 6;
}
```

---

### alert_type.proto {#alert_type}

**Path**: `gcommon/v1/common/alert_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `AlertType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/alert_type.proto
// version: 1.0.1
// guid: 54407766-3304-4e90-90d6-973ac6ff0fc3

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum AlertType {
  ALERT_TYPE_UNSPECIFIED = 0;
  ALERT_TYPE_EXPIRATION = 1;
  ALERT_TYPE_ACCESS_ANOMALY = 2;
  ALERT_TYPE_FAILED_ACCESS = 3;
  ALERT_TYPE_ROTATION_FAILURE = 4;
  ALERT_TYPE_BACKUP_FAILURE = 5;
  ALERT_TYPE_COMPLIANCE_VIOLATION = 6;
  ALERT_TYPE_SECURITY_INCIDENT = 7;
}
```

---

### anti_affinity_scope.proto {#anti_affinity_scope}

**Path**: `gcommon/v1/common/anti_affinity_scope.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `AntiAffinityScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/anti_affinity_scope.proto
// version: 1.0.1
// guid: 719f1256-5001-4957-aa05-7b676cc4b90b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Scope for anti-affinity rules.
 */
enum AntiAffinityScope {
  // Default unspecified scope
  ANTI_AFFINITY_SCOPE_UNSPECIFIED = 0;

  // Same node
  ANTI_AFFINITY_SCOPE_NODE = 1;

  // Same rack
  ANTI_AFFINITY_SCOPE_RACK = 2;

  // Same datacenter
  ANTI_AFFINITY_SCOPE_DATACENTER = 3;

  // Same region
  ANTI_AFFINITY_SCOPE_REGION = 4;
}
```

---

### appender_type.proto {#appender_type}

**Path**: `gcommon/v1/common/appender_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `AppenderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/appender_type.proto
// version: 1.0.1
// guid: 5e2f63bf-35c4-4a2a-b35a-54017c979940

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// AppenderType enumerates logging output backends
enum AppenderType {
  APPENDER_TYPE_UNSPECIFIED = 0;
  APPENDER_TYPE_CONSOLE = 1;
  APPENDER_TYPE_FILE = 2;
  APPENDER_TYPE_ROLLING_FILE = 3;
  APPENDER_TYPE_SYSLOG = 4;
  APPENDER_TYPE_NETWORK = 5;
  APPENDER_TYPE_DATABASE = 6;
}
```

---

### approval_status.proto {#approval_status}

**Path**: `gcommon/v1/common/approval_status.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `ApprovalStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/approval_status.proto
// version: 1.0.1
// guid: a9b0c1d2-e3f4-5a6b-7c8d-9e0f1a2b3c4d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ApprovalStatus represents the approval status.
 * Specifies the current state of configuration change approval.
 */
enum ApprovalStatus {
  // Unspecified approval status
  APPROVAL_STATUS_UNSPECIFIED = 0;

  // Approval is pending
  APPROVAL_STATUS_PENDING = 1;

  // Change has been approved
  APPROVAL_STATUS_APPROVED = 2;

  // Change has been rejected
  APPROVAL_STATUS_REJECTED = 3;

  // Approval was cancelled
  APPROVAL_STATUS_CANCELLED = 4;

  // Approval request expired
  APPROVAL_STATUS_EXPIRED = 5;
}
```

---

### audit_action.proto {#audit_action}

**Path**: `gcommon/v1/common/audit_action.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Enums** (1): `AuditAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_action.proto
// version: 1.0.1
// guid: fe20f23e-ff61-4f78-b548-99cc5aded7b4
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Audit action enumeration for tracking user and system actions.
 * Used for security auditing and compliance logging.
 */
enum AuditAction {
  // Unspecified audit action
  AUDIT_ACTION_UNSPECIFIED = 0;

  // Authentication actions
  AUDIT_ACTION_LOGIN = 1;
  AUDIT_ACTION_LOGOUT = 2;
  AUDIT_ACTION_LOGIN_FAILED = 3;

  // Authorization actions
  AUDIT_ACTION_ACCESS_GRANTED = 4;
  AUDIT_ACTION_ACCESS_DENIED = 5;

  // User management actions
  AUDIT_ACTION_USER_CREATED = 6;
  AUDIT_ACTION_USER_UPDATED = 7;
  AUDIT_ACTION_USER_DELETED = 8;
  AUDIT_ACTION_USER_SUSPENDED = 9;

  // Role management actions
  AUDIT_ACTION_ROLE_ASSIGNED = 10;
  AUDIT_ACTION_ROLE_REMOVED = 11;
  AUDIT_ACTION_ROLE_CREATED = 12;
  AUDIT_ACTION_ROLE_UPDATED = 13;
  AUDIT_ACTION_ROLE_DELETED = 14;

  // Permission actions
  AUDIT_ACTION_PERMISSION_GRANTED = 15;
  AUDIT_ACTION_PERMISSION_REVOKED = 16;

  // Session actions
  AUDIT_ACTION_SESSION_CREATED = 17;
  AUDIT_ACTION_SESSION_TERMINATED = 18;

  // Configuration changes
  AUDIT_ACTION_CONFIG_UPDATED = 19;

  // System actions
  AUDIT_ACTION_SYSTEM_BACKUP = 20;
  AUDIT_ACTION_SYSTEM_RESTORE = 21;
}
```

---

### audit_level.proto {#audit_level}

**Path**: `gcommon/v1/common/audit_level.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `AuditLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/audit_level.proto
// version: 1.0.1
// guid: 8576474b-84f1-4a99-ab88-a865fb4e28ca

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum AuditLevel {
  AUDIT_LEVEL_UNSPECIFIED = 0;
  AUDIT_LEVEL_NONE = 1;
  AUDIT_LEVEL_MINIMAL = 2;
  AUDIT_LEVEL_STANDARD = 3;
  AUDIT_LEVEL_DETAILED = 4;
  AUDIT_LEVEL_VERBOSE = 5;
}
```

---

### audit_operation_type.proto {#audit_operation_type}

**Path**: `gcommon/v1/common/audit_operation_type.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Enums** (1): `AuditOperationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/audit_operation_type.proto
// version: 1.0.1
// guid: d6e7f8a9-b0c1-2d3e-4f5a-6b7c8d9e0f1a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuditOperationType represents the type of configuration operation.
 * Specifies the category of configuration change being audited.
 */
enum AuditOperationType {
  // Unspecified operation type
  AUDIT_OPERATION_TYPE_UNSPECIFIED = 0;

  // Create new configuration
  AUDIT_OPERATION_TYPE_CREATE = 1;

  // Update existing configuration
  AUDIT_OPERATION_TYPE_UPDATE = 2;

  // Delete configuration
  AUDIT_OPERATION_TYPE_DELETE = 3;

  // Bulk create multiple configurations
  AUDIT_OPERATION_TYPE_BULK_CREATE = 4;

  // Bulk update multiple configurations
  AUDIT_OPERATION_TYPE_BULK_UPDATE = 5;

  // Bulk delete multiple configurations
  AUDIT_OPERATION_TYPE_BULK_DELETE = 6;

  // Import configuration data
  AUDIT_OPERATION_TYPE_IMPORT = 7;

  // Export configuration data
  AUDIT_OPERATION_TYPE_EXPORT = 8;

  // Backup configuration
  AUDIT_OPERATION_TYPE_BACKUP = 9;

  // Restore configuration from backup
  AUDIT_OPERATION_TYPE_RESTORE = 10;

  // Rollback configuration changes
  AUDIT_OPERATION_TYPE_ROLLBACK = 11;

  // Validate configuration
  AUDIT_OPERATION_TYPE_VALIDATE = 12;

  // Synchronize configuration
  AUDIT_OPERATION_TYPE_SYNC = 13;
}
```

---

### audit_result.proto {#audit_result}

**Path**: `gcommon/v1/common/audit_result.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `AuditResult`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_result.proto
// version: 1.0.1
// guid: 27e8e7bb-a068-4e4b-b7d0-d69c6747f9bc
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Audit result enumeration for tracking operation outcomes in audit logs.
 * Provides standardized result classification for security and compliance
 * auditing across all GCommon modules.
 */
enum AuditResult {
  // Default value indicating no audit result was specified
  AUDIT_RESULT_UNSPECIFIED = 0;

  // Operation completed successfully
  AUDIT_RESULT_SUCCESS = 1;

  // Operation failed to complete
  AUDIT_RESULT_FAILURE = 2;

  // Operation completed with partial success/failure
  AUDIT_RESULT_PARTIAL = 3;
}
```

---

### auth_method.proto {#auth_method}

**Path**: `gcommon/v1/common/auth_method.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Enums** (1): `AuthAuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_method.proto
// version: 1.0.1
// guid: 815bb886-5864-44fd-ae07-c6102c110fd7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthMethod enumerates the supported authentication mechanisms.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthAuthMethod {
  // Default unknown method
  COMMON_AUTH_METHOD_UNSPECIFIED = 0;

  // Traditional username and password authentication
  COMMON_AUTH_METHOD_PASSWORD = 1;

  // API key based authentication
  COMMON_AUTH_METHOD_API_KEY = 2;

  // OAuth2 or OpenID Connect authentication
  COMMON_AUTH_METHOD_OAUTH2 = 3;

  // SAML identity provider authentication
  COMMON_AUTH_METHOD_SAML = 4;

  // LDAP directory authentication
  COMMON_AUTH_METHOD_LDAP = 5;

  // Multi-factor authentication method
  COMMON_AUTH_METHOD_MFA = 6;

  // Token-based authentication (e.g., JWT, bearer tokens)
  COMMON_AUTH_METHOD_TOKEN = 7;

  // No authentication required
  COMMON_AUTH_METHOD_NONE = 8;
}
```

---

### backoff_strategy.proto {#backoff_strategy}

**Path**: `gcommon/v1/common/backoff_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `BackoffStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/backoff_strategy.proto
// version: 1.0.1
// guid: 5aec3abd-38af-4436-a59a-c4140f44a461

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum BackoffStrategy {
  BACKOFF_STRATEGY_UNSPECIFIED = 0;
  BACKOFF_STRATEGY_FIXED = 1;
  BACKOFF_STRATEGY_LINEAR = 2;
  BACKOFF_STRATEGY_EXPONENTIAL = 3;
  BACKOFF_STRATEGY_CUSTOM = 4;
}
```

---

### buffer_overflow_strategy.proto {#buffer_overflow_strategy}

**Path**: `gcommon/v1/common/buffer_overflow_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `BufferOverflowStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/buffer_overflow_strategy.proto
// version: 1.0.1
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * BufferOverflowStrategy defines how to handle buffer overflow.
 * Specifies behavior when metric streaming buffers are full.
 */
enum BufferOverflowStrategy {
  // Unspecified strategy
  BUFFER_OVERFLOW_STRATEGY_UNSPECIFIED = 0;

  // Drop oldest entries when buffer is full
  BUFFER_OVERFLOW_STRATEGY_DROP_OLDEST = 1;

  // Drop newest entries when buffer is full
  BUFFER_OVERFLOW_STRATEGY_DROP_NEWEST = 2;

  // Block when buffer is full
  BUFFER_OVERFLOW_STRATEGY_BLOCK = 3;

  // Return error when buffer is full
  BUFFER_OVERFLOW_STRATEGY_ERROR = 4;
}
```

---

### cache_invalidation_trigger.proto {#cache_invalidation_trigger}

**Path**: `gcommon/v1/common/cache_invalidation_trigger.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `CacheInvalidationTrigger`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/cache_invalidation_trigger.proto
// version: 1.0.1
// guid: b09e744e-1475-4fcb-a8cc-0d121530e6b7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CacheInvalidationTrigger {
  CACHE_INVALIDATION_TRIGGER_UNSPECIFIED = 0;
  CACHE_INVALIDATION_TRIGGER_CHANGE = 1;
  CACHE_INVALIDATION_TRIGGER_DELETE = 2;
  CACHE_INVALIDATION_TRIGGER_EXPIRE = 3;
  CACHE_INVALIDATION_TRIGGER_MANUAL = 4;
  CACHE_INVALIDATION_TRIGGER_SCHEDULE = 5;
}
```

---

### cache_refresh_strategy.proto {#cache_refresh_strategy}

**Path**: `gcommon/v1/common/cache_refresh_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `CacheRefreshStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/cache_refresh_strategy.proto
// version: 1.0.1
// guid: c38dfb62-6d18-4f59-a901-6c4b5e659952

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CacheRefreshStrategy {
  CACHE_REFRESH_STRATEGY_UNSPECIFIED = 0;
  CACHE_REFRESH_STRATEGY_TTL = 1;
  CACHE_REFRESH_STRATEGY_LAZY = 2;
  CACHE_REFRESH_STRATEGY_PROACTIVE = 3;
  CACHE_REFRESH_STRATEGY_BACKGROUND = 4;
}
```

---

### cache_strategy.proto {#cache_strategy}

**Path**: `gcommon/v1/common/cache_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `CacheStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cache_strategy.proto
// version: 1.0.1
// guid: a2c186e6-9e1e-402b-802f-39fc7b4dfc0d
//
// CacheStrategy defines caching policies for HTTP handlers.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Available caching policies for responses.
enum CacheStrategy {
  CACHE_STRATEGY_UNSPECIFIED = 0;
  // Do not cache responses.
  CACHE_STRATEGY_NONE = 1;
  // Use in-memory caching only.
  CACHE_STRATEGY_MEMORY = 2;
  // Use distributed cache (e.g., Redis).
  CACHE_STRATEGY_DISTRIBUTED = 3;
  // Use external CDN cache.
  CACHE_STRATEGY_CDN = 4;
}
```

---

### channel_type.proto {#channel_type}

**Path**: `gcommon/v1/common/channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `ChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/channel_type.proto
// version: 1.0.1
// guid: 6f6a3985-1560-40b0-b6d5-b2985349b649

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ChannelType {
  CHANNEL_TYPE_UNSPECIFIED = 0;
  CHANNEL_TYPE_EMAIL = 1;
  CHANNEL_TYPE_SLACK = 2;
  CHANNEL_TYPE_WEBHOOK = 3;
  CHANNEL_TYPE_SMS = 4;
  CHANNEL_TYPE_PAGERDUTY = 5;
  CHANNEL_TYPE_TEAMS = 6;
  CHANNEL_TYPE_DISCORD = 7;
  CHANNEL_TYPE_JIRA = 8;
}
```

---

### check_type.proto {#check_type}

**Path**: `gcommon/v1/common/check_type.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Enums** (1): `CheckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_type.proto
// version: 1.0.1
// guid: 38e1041c-a418-4fe7-8834-b48f3c71f401
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * CheckType indicates the type of health check
 */
enum CheckType {
  // Unspecified check type
  CHECK_TYPE_UNSPECIFIED = 0;
  // Liveness check
  CHECK_TYPE_LIVENESS = 1;
  // Readiness check
  CHECK_TYPE_READINESS = 2;
  // Startup check
  CHECK_TYPE_STARTUP = 3;
  // Component check
  CHECK_TYPE_COMPONENT = 4;
  // Dependency check
  CHECK_TYPE_DEPENDENCY = 5;
}
```

---

### circuit_breaker_state.proto {#circuit_breaker_state}

**Path**: `gcommon/v1/common/circuit_breaker_state.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `CircuitBreakerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/circuit_breaker_state.proto
// version: 1.0.1
// guid: 1d26f112-976e-48db-b531-58892638701d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Circuit breaker state enumeration for fault tolerance patterns.
 * Defines the current state of circuit breaker components used
 * for resilience and stability across all GCommon modules.
 */
enum CircuitBreakerState {
  // Default value indicating no circuit breaker state was specified
  CIRCUIT_BREAKER_STATE_UNSPECIFIED = 0;

  // Circuit is closed - requests are flowing normally
  CIRCUIT_BREAKER_STATE_CLOSED = 1;

  // Circuit is open - requests are blocked due to failures
  CIRCUIT_BREAKER_STATE_OPEN = 2;

  // Circuit is half-open - testing if service has recovered
  CIRCUIT_BREAKER_STATE_HALF_OPEN = 3;
}
```

---

### cleanup_strategy.proto {#cleanup_strategy}

**Path**: `gcommon/v1/common/cleanup_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `CleanupStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/cleanup_strategy.proto
// version: 1.0.1
// guid: 98464e8e-3ad4-475d-8e19-cac3b3d813ca

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * CleanupStrategy defines how cleanup should be performed.
 */
enum CleanupStrategy {
  CLEANUP_STRATEGY_UNSPECIFIED = 0;
  CLEANUP_STRATEGY_IMMEDIATE = 1;
  CLEANUP_STRATEGY_GRACEFUL = 2;
  CLEANUP_STRATEGY_BACKGROUND = 3;
  CLEANUP_STRATEGY_SCHEDULED = 4;
}
```

---

### cluster_state.proto {#cluster_state}

**Path**: `gcommon/v1/common/cluster_state.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `ClusterState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_state.proto
// version: 1.0.1
// guid: f68fdc5e-d25f-4790-9362-9bf09eb27f4d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * State of the cluster.
 */
enum ClusterState {
  // Default unspecified state
  CLUSTER_STATE_UNSPECIFIED = 0;

  // Cluster is healthy and operational
  CLUSTER_STATE_HEALTHY = 1;

  // Cluster is degraded but operational
  CLUSTER_STATE_DEGRADED = 2;

  // Cluster is in recovery mode
  CLUSTER_STATE_RECOVERING = 3;

  // Cluster is down
  CLUSTER_STATE_DOWN = 4;

  // Cluster is in maintenance mode
  CLUSTER_STATE_MAINTENANCE = 5;
}
```

---

### comparison_operator.proto {#comparison_operator}

**Path**: `gcommon/v1/common/comparison_operator.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `ComparisonOperator`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/comparison_operator.proto
// version: 1.0.1
// guid: a2b3c4d5-6789-012d-6789-234567890123

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ComparisonOperator {
  COMPARISON_OPERATOR_UNSPECIFIED = 0;
  COMPARISON_OPERATOR_EQUAL = 1;
  COMPARISON_OPERATOR_NOT_EQUAL = 2;
  COMPARISON_OPERATOR_GREATER_THAN = 3;
  COMPARISON_OPERATOR_GREATER_THAN_OR_EQUAL = 4;
  COMPARISON_OPERATOR_LESS_THAN = 5;
  COMPARISON_OPERATOR_LESS_THAN_OR_EQUAL = 6;
}
```

---

### compression_algorithm.proto {#compression_algorithm}

**Path**: `gcommon/v1/common/compression_algorithm.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `CompressionAlgorithm`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/compression_algorithm.proto
// version: 1.0.1
// guid: 46070a52-0998-4b61-b36f-05b4861f8f6c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Compression algorithms for serialization.
 */
enum CompressionAlgorithm {
  // Default unspecified algorithm
  COMPRESSION_ALGORITHM_UNSPECIFIED = 0;

  // No compression
  COMPRESSION_ALGORITHM_NONE = 1;

  // GZIP compression
  COMPRESSION_ALGORITHM_GZIP = 2;

  // LZ4 compression
  COMPRESSION_ALGORITHM_LZ4 = 3;

  // Snappy compression
  COMPRESSION_ALGORITHM_SNAPPY = 4;

  // ZSTD compression
  COMPRESSION_ALGORITHM_ZSTD = 5;

  // Brotli compression
  COMPRESSION_ALGORITHM_BROTLI = 6;
}
```

---

### compression_type.proto {#compression_type}

**Path**: `gcommon/v1/common/compression_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `LogCompressionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/compression_type.proto
// version: 1.0.1
// guid: 357b1a04-97e4-4d82-86a3-b6672180ce22

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// CompressionType enumerates archive compression formats
// buf:lint:ignore ENUM_VALUE_PREFIX
enum LogCompressionType {
  COMPRESSION_TYPE_UNSPECIFIED = 0;
  COMPRESSION_TYPE_NONE = 1;
  COMPRESSION_TYPE_GZIP = 2;
  COMPRESSION_TYPE_ZIP = 3;
  COMPRESSION_TYPE_BZIP2 = 4;
  COMPRESSION_TYPE_TAR_GZ = 5;
}
```

---

### conflict_resolution.proto {#conflict_resolution}

**Path**: `gcommon/v1/common/conflict_resolution.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `ConflictResolution`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/conflict_resolution.proto
// version: 1.0.1
// guid: 8535d30e-d232-4d73-9362-10e717955b66

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConflictResolution {
  COMMON_CONFLICT_RESOLUTION_UNSPECIFIED = 0;
  COMMON_CONFLICT_RESOLUTION_MERGE = 1;
  COMMON_CONFLICT_RESOLUTION_OVERWRITE = 2;
  COMMON_CONFLICT_RESOLUTION_FAIL = 3;
}
```

---

### conflict_strategy.proto {#conflict_strategy}

**Path**: `gcommon/v1/common/conflict_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `ConflictStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/conflict_strategy.proto
// version: 1.0.1
// guid: 1f8fb98d-0197-472d-9b17-681ebc9772bf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConflictStrategy {
  CONFLICT_STRATEGY_UNSPECIFIED = 0;
  CONFLICT_STRATEGY_TIMESTAMP = 1; // Timestamp-based detection
  CONFLICT_STRATEGY_VECTOR_CLOCK = 2; // Vector clock-based detection
  CONFLICT_STRATEGY_CAUSAL = 3; // Causal consistency detection
}
```

---

### consistency_level.proto {#consistency_level}

**Path**: `gcommon/v1/common/consistency_level.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Enums** (1): `DatabaseConsistencyLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/consistency_level.proto
// version: 1.0.1
// guid: 5eaa6727-c2ff-40f4-b746-6782b5b18b05
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConsistencyLevel defines the data consistency requirements for database operations.
 * Controls the trade-off between consistency, availability, and partition tolerance.
 */
enum DatabaseConsistencyLevel {
  // Default unspecified consistency level
  DATABASE_CONSISTENCY_LEVEL_UNSPECIFIED = 0;

  // Eventual consistency - may read stale data but eventually consistent
  DATABASE_CONSISTENCY_LEVEL_EVENTUAL = 1;

  // Strong consistency - always reads most recent committed data
  DATABASE_CONSISTENCY_LEVEL_STRONG = 2;

  // Bounded staleness - reads data within specified time bounds
  DATABASE_CONSISTENCY_LEVEL_BOUNDED_STALENESS = 3;
}
```

---

### consumer_group_state.proto {#consumer_group_state}

**Path**: `gcommon/v1/common/consumer_group_state.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ConsumerGroupState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group_state.proto
// version: 1.0.1
// guid: 3c66ccb4-a4d4-43f9-952e-510a7b8086c9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConsumerGroupState {
  CONSUMER_GROUP_STATE_UNSPECIFIED = 0;
  CONSUMER_GROUP_STATE_STABLE = 1; // Group is stable with assigned partitions
  CONSUMER_GROUP_STATE_PREPARING_REBALANCE = 2; // Preparing for rebalance
  CONSUMER_GROUP_STATE_COMPLETING_REBALANCE = 3; // Completing rebalance operation
  CONSUMER_GROUP_STATE_DEAD = 4; // Group has no active consumers
  CONSUMER_GROUP_STATE_EMPTY = 5; // Group exists but no consumers
}
```

---

### consumer_state.proto {#consumer_state}

**Path**: `gcommon/v1/common/consumer_state.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Enums** (1): `ConsumerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/consumer_state.proto
// file: proto/gcommon/v1/queue/consumer_state.proto
// version: 1.0.1
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * State of a queue consumer.
 */
enum ConsumerState {
  // Default unspecified state
  CONSUMER_STATE_UNSPECIFIED = 0;

  // Consumer is active and processing messages
  CONSUMER_STATE_ACTIVE = 1;

  // Consumer is idle (connected but not processing)
  CONSUMER_STATE_IDLE = 2;

  // Consumer is paused
  CONSUMER_STATE_PAUSED = 3;

  // Consumer is stopped
  CONSUMER_STATE_STOPPED = 4;

  // Consumer has encountered an error
  CONSUMER_STATE_ERROR = 5;

  // Consumer is connecting
  CONSUMER_STATE_CONNECTING = 6;

  // Consumer is disconnected
  CONSUMER_STATE_DISCONNECTED = 7;
}
```

---

### content_type.proto {#content_type}

**Path**: `gcommon/v1/common/content_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `ContentType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/content_type.proto
// version: 1.0.1
// guid: 8bb9871c-690b-4fb4-83e1-735d6815a620
//
// ContentType enumerates common MIME types.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Well-known MIME types supported by the server.
enum ContentType {
  CONTENT_TYPE_UNSPECIFIED = 0;
  CONTENT_TYPE_HTML = 1;
  CONTENT_TYPE_JSON = 2;
  CONTENT_TYPE_XML = 3;
  CONTENT_TYPE_TEXT = 4;
  CONTENT_TYPE_BINARY = 5;
}
```

---

### cookie_same_site.proto {#cookie_same_site}

**Path**: `gcommon/v1/common/cookie_same_site.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `CookieSameSite`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/cookie_same_site.proto
// version: 1.0.1
// guid: b38945ee-58e0-4d5a-9637-f2c57a5a9b31
//
// CookieSameSite defines SameSite settings for cookies.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CookieSameSite {
  COOKIE_SAME_SITE_UNSPECIFIED = 0;
  COOKIE_SAME_SITE_DEFAULT = 1;
  COOKIE_SAME_SITE_LAX = 2;
  COOKIE_SAME_SITE_STRICT = 3;
  COOKIE_SAME_SITE_NONE = 4;
}
```

---

### coordinator_state.proto {#coordinator_state}

**Path**: `gcommon/v1/common/coordinator_state.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `CoordinatorState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/coordinator_state.proto
// version: 1.0.1
// guid: 834ccf4a-176f-479d-87af-833f052ccf71

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum CoordinatorState {
  COORDINATOR_STATE_UNSPECIFIED = 0;
  COORDINATOR_STATE_ACTIVE = 1; // Coordinator is active
  COORDINATOR_STATE_LOADING = 2; // Coordinator is loading metadata
  COORDINATOR_STATE_NOT_COORDINATOR = 3; // Node is not the coordinator
}
```

---

### dashboard_type.proto {#dashboard_type}

**Path**: `gcommon/v1/common/dashboard_type.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `DashboardType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/dashboard_type.proto
// version: 1.0.1
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// DashboardType represents different types of dashboards
enum DashboardType {
  // Unspecified dashboard type
  DASHBOARD_TYPE_UNSPECIFIED = 0;

  // System overview dashboard
  DASHBOARD_TYPE_SYSTEM_OVERVIEW = 1;

  // Application performance dashboard
  DASHBOARD_TYPE_APPLICATION_PERFORMANCE = 2;

  // Infrastructure monitoring dashboard
  DASHBOARD_TYPE_INFRASTRUCTURE = 3;

  // Business metrics dashboard
  DASHBOARD_TYPE_BUSINESS_METRICS = 4;

  // Security monitoring dashboard
  DASHBOARD_TYPE_SECURITY = 5;

  // Custom dashboard
  DASHBOARD_TYPE_CUSTOM = 6;

  // Real-time monitoring dashboard
  DASHBOARD_TYPE_REAL_TIME = 7;

  // Historical analysis dashboard
  DASHBOARD_TYPE_HISTORICAL = 8;

  // Alert summary dashboard
  DASHBOARD_TYPE_ALERT_SUMMARY = 9;

  // Service health dashboard
  DASHBOARD_TYPE_SERVICE_HEALTH = 10;

  // Capacity planning dashboard
  DASHBOARD_TYPE_CAPACITY_PLANNING = 11;

  // SLA/SLO tracking dashboard
  DASHBOARD_TYPE_SLA_SLO = 12;
}
```

---

### database_isolation_level.proto {#database_isolation_level}

**Path**: `gcommon/v1/common/database_isolation_level.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `DatabaseIsolationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/isolation_level.proto
// version: 1.0.1
// guid: 004cde4c-f6bc-40ff-b341-1408e58e37b6
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * IsolationLevel defines transaction isolation levels controlling concurrent access.
 * Balances data consistency with concurrency performance.
 */
enum DatabaseIsolationLevel {
  // Default unspecified isolation level
  DATABASE_ISOLATION_LEVEL_UNSPECIFIED = 0;

  // Read uncommitted - allows dirty reads, lowest isolation
  DATABASE_ISOLATION_LEVEL_READ_UNCOMMITTED = 1;

  // Read committed - prevents dirty reads, allows non-repeatable reads
  DATABASE_ISOLATION_LEVEL_READ_COMMITTED = 2;

  // Repeatable read - prevents dirty and non-repeatable reads
  DATABASE_ISOLATION_LEVEL_REPEATABLE_READ = 3;

  // Serializable - highest isolation, prevents all phenomena
  DATABASE_ISOLATION_LEVEL_SERIALIZABLE = 4;
}
```

---

### database_status_code.proto {#database_status_code}

**Path**: `gcommon/v1/common/database_status_code.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `DatabaseStatusCode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/database/database_status_code.proto
// version: 1.0.1
// guid: 9849ce1c-df0e-418d-9de6-27b7b1b99d99

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * DatabaseStatusCode represents the health state of a database
 * connection or service.
 */
enum DatabaseStatusCode {
  // Default unspecified status
  DATABASE_STATUS_CODE_UNSPECIFIED = 0;

  // Database is reachable and operational
  DATABASE_STATUS_CODE_OK = 1;

  // Database is unreachable or returned an error
  DATABASE_STATUS_CODE_ERROR = 2;
}
```

---

### delivery_channel_type.proto {#delivery_channel_type}

**Path**: `gcommon/v1/common/delivery_channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `DeliveryChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delivery_channel_type.proto
// version: 1.0.1
// guid: c5d6e7f8-a9b0-1c2d-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### delivery_mode.proto {#delivery_mode}

**Path**: `gcommon/v1/common/delivery_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `DeliveryMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/delivery_mode.proto
// file: proto/gcommon/v1/queue/delivery_mode.proto
// version: 1.0.1
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Message delivery mode for queue operations.
 */
enum DeliveryMode {
  // Default unspecified delivery mode
  DELIVERY_MODE_UNSPECIFIED = 0;

  // At most once delivery (may lose messages, no duplicates)
  DELIVERY_MODE_AT_MOST_ONCE = 1;

  // At least once delivery (no message loss, may have duplicates)
  DELIVERY_MODE_AT_LEAST_ONCE = 2;

  // Exactly once delivery (no loss, no duplicates - when supported)
  DELIVERY_MODE_EXACTLY_ONCE = 3;

  // Best effort delivery (no guarantees)
  DELIVERY_MODE_BEST_EFFORT = 4;
}
```

---

### delivery_status.proto {#delivery_status}

**Path**: `gcommon/v1/common/delivery_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `DeliveryStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delivery_status.proto
// version: 1.0.1
// guid: 6548d52a-11c5-44c0-bbf8-269fecf8eab3
// file: proto/gcommon/v1/common/delivery_status.proto
//
// Delivery status enumeration for tracking notification outcomes.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### dependency_type.proto {#dependency_type}

**Path**: `gcommon/v1/common/dependency_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `DependencyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/dependency_type.proto
// version: 1.0.1
// guid: 0dbbaf99-12ad-49af-8747-0eb055671d35

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum DependencyType {
  DEPENDENCY_TYPE_UNSPECIFIED = 0;
  DEPENDENCY_TYPE_REQUIRED = 1;
  DEPENDENCY_TYPE_OPTIONAL = 2;
  DEPENDENCY_TYPE_CONDITIONAL = 3;
  DEPENDENCY_TYPE_DERIVED = 4;
  DEPENDENCY_TYPE_CONFLICT = 5;
}
```

---

### deployment_status.proto {#deployment_status}

**Path**: `gcommon/v1/common/deployment_status.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `DeploymentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deployment_status.proto
// version: 1.0.1
// guid: e3f4a5b6-c7d8-9e0f-1a2b-3c4d5e6f7a8b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * DeploymentStatus represents the status of a deployment.
 * Specifies the current state of configuration deployment operations.
 */
enum DeploymentStatus {
  // Unspecified deployment status
  DEPLOYMENT_STATUS_UNSPECIFIED = 0;

  // Deployment is pending
  DEPLOYMENT_STATUS_PENDING = 1;

  // Deployment is in progress
  DEPLOYMENT_STATUS_IN_PROGRESS = 2;

  // Deployment completed successfully
  DEPLOYMENT_STATUS_SUCCESS = 3;

  // Deployment failed
  DEPLOYMENT_STATUS_FAILED = 4;

  // Deployment was rolled back
  DEPLOYMENT_STATUS_ROLLED_BACK = 5;

  // Deployment was cancelled
  DEPLOYMENT_STATUS_CANCELLED = 6;
}
```

---

### deprecation_level.proto {#deprecation_level}

**Path**: `gcommon/v1/common/deprecation_level.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `DeprecationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/deprecation_level.proto
// version: 1.0.1
// guid: 0a330fa1-9f33-458b-a37e-aeed96ad7530

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum DeprecationLevel {
  DEPRECATION_LEVEL_UNSPECIFIED = 0;
  DEPRECATION_LEVEL_SOFT = 1; // Soft deprecation (warning)
  DEPRECATION_LEVEL_HARD = 2; // Hard deprecation (error)
  DEPRECATION_LEVEL_REMOVAL = 3; // Scheduled for removal
}
```

---

### durability_level.proto {#durability_level}

**Path**: `gcommon/v1/common/durability_level.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `DurabilityLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/durability_level.proto
// file: proto/gcommon/v1/queue/durability_level.proto
// version: 1.0.1
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Durability levels for message persistence guarantees.
 */
enum DurabilityLevel {
  // Default unspecified level
  DURABILITY_LEVEL_UNSPECIFIED = 0;

  // No durability - messages may be lost on restart
  DURABILITY_LEVEL_NONE = 1;

  // Memory-only persistence with periodic snapshots
  DURABILITY_LEVEL_MEMORY = 2;

  // Synchronous disk persistence for each message
  DURABILITY_LEVEL_DISK_SYNC = 3;

  // Asynchronous disk persistence with batching
  DURABILITY_LEVEL_DISK_ASYNC = 4;

  // Replicated across multiple nodes with disk persistence
  DURABILITY_LEVEL_REPLICATED = 5;
}
```

---

### environment_status.proto {#environment_status}

**Path**: `gcommon/v1/common/environment_status.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `EnvironmentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/environment_status.proto
// version: 1.0.1
// guid: d2e3f4a5-b6c7-8d9e-0f1a-2b3c4d5e6f7a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * EnvironmentStatus represents the status of an environment.
 * Specifies the current operational state of a configuration environment.
 */
enum EnvironmentStatus {
  // Unspecified environment status
  ENVIRONMENT_STATUS_UNSPECIFIED = 0;

  // Environment is active and operational
  ENVIRONMENT_STATUS_ACTIVE = 1;

  // Environment is inactive
  ENVIRONMENT_STATUS_INACTIVE = 2;

  // Environment is under maintenance
  ENVIRONMENT_STATUS_MAINTENANCE = 3;

  // Environment is deprecated
  ENVIRONMENT_STATUS_DEPRECATED = 4;

  // Environment is archived
  ENVIRONMENT_STATUS_ARCHIVED = 5;

  // Environment is in error state
  ENVIRONMENT_STATUS_ERROR = 6;
}
```

---

### environment_type.proto {#environment_type}

**Path**: `gcommon/v1/common/environment_type.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Enums** (1): `EnvironmentType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/environment_type.proto
// version: 1.0.1
// guid: c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * EnvironmentType represents the type of environment.
 * Specifies the purpose and classification of configuration environments.
 */
enum EnvironmentType {
  // Unspecified environment type
  ENVIRONMENT_TYPE_UNSPECIFIED = 0;

  // Development environment
  ENVIRONMENT_TYPE_DEVELOPMENT = 1;

  // Testing environment
  ENVIRONMENT_TYPE_TESTING = 2;

  // Staging environment
  ENVIRONMENT_TYPE_STAGING = 3;

  // Production environment
  ENVIRONMENT_TYPE_PRODUCTION = 4;

  // Sandbox environment for experimentation
  ENVIRONMENT_TYPE_SANDBOX = 5;

  // Canary deployment environment
  ENVIRONMENT_TYPE_CANARY = 6;

  // Disaster recovery environment
  ENVIRONMENT_TYPE_DISASTER_RECOVERY = 7;

  // Integration testing environment
  ENVIRONMENT_TYPE_INTEGRATION = 8;

  // Performance testing environment
  ENVIRONMENT_TYPE_PERFORMANCE = 9;

  // Security testing environment
  ENVIRONMENT_TYPE_SECURITY = 10;
}
```

---

### error_code.proto {#error_code}

**Path**: `gcommon/v1/common/error_code.proto` **Package**: `gcommon.v1.common` **Lines**: 64

**Enums** (1): `ErrorCode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error_code.proto
// version: 1.0.1
// guid: 6177a6c6-ea53-448e-8ec8-b526bb86a53f
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Standardized error codes following gRPC conventions.
 * These codes provide consistent error handling across all GCommon modules.
 *
 * Each error code maps to standard gRPC status codes for cross-language compatibility.
 */
enum ErrorCode {
  // Default value indicating no error code was specified
  ERROR_CODE_UNSPECIFIED = 0;

  // Client specified an invalid argument. Request should not be retried without modification
  ERROR_CODE_INVALID_ARGUMENT = 1;

  // Some requested entity was not found
  ERROR_CODE_NOT_FOUND = 2;

  // The entity that a client attempted to create already exists
  ERROR_CODE_ALREADY_EXISTS = 3;

  // The caller does not have permission to execute the specified operation
  ERROR_CODE_PERMISSION_DENIED = 4;

  // The request does not have valid authentication credentials
  ERROR_CODE_UNAUTHENTICATED = 5;

  // Internal server error. Client should not retry
  ERROR_CODE_INTERNAL = 6;

  // The service is currently unavailable. Client may retry
  ERROR_CODE_UNAVAILABLE = 7;

  // Deadline expired before operation could complete
  ERROR_CODE_TIMEOUT = 8;

  // Resource has been exhausted (e.g., quota exceeded)
  ERROR_CODE_RESOURCE_EXHAUSTED = 9;

  // Operation was rejected because the system is not in required state
  ERROR_CODE_FAILED_PRECONDITION = 10;

  // The operation was aborted, typically due to concurrency issue
  ERROR_CODE_ABORTED = 11;

  // Operation was attempted past the valid range
  ERROR_CODE_OUT_OF_RANGE = 12;

  // Operation is not implemented or not supported
  ERROR_CODE_UNIMPLEMENTED = 13;

  // Unrecoverable data loss or corruption
  ERROR_CODE_DATA_LOSS = 14;
}
```

---

### eviction_policy.proto {#eviction_policy}

**Path**: `gcommon/v1/common/eviction_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `EvictionPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/eviction_policy.proto
// version: 1.0.1
// guid: 53ad7b97-17b7-45fc-b834-31d09296f358
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Cache eviction policy enumeration for cache management.
 * Defines which cached items should be removed when cache capacity
 * is reached across all GCommon modules.
 */
enum EvictionPolicy {
  // Default value indicating no eviction policy was specified
  EVICTION_POLICY_UNSPECIFIED = 0;

  // Least Recently Used - evict items that haven't been accessed recently
  EVICTION_POLICY_LRU = 1;

  // Least Frequently Used - evict items that are accessed least often
  EVICTION_POLICY_LFU = 2;

  // First In, First Out - evict items in order they were added
  EVICTION_POLICY_FIFO = 3;

  // Random eviction - evict randomly selected items
  EVICTION_POLICY_RANDOM = 4;
}
```

---

### expiration_policy.proto {#expiration_policy}

**Path**: `gcommon/v1/common/expiration_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `ExpirationPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/expiration_policy.proto
// version: 1.0.1
// guid: 788be552-a444-4860-9db6-1004f1f1fabf
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Cache expiration policy enumeration for cache management.
 * Defines how cached items expire and when they should be evicted
 * from cache storage across all GCommon modules.
 */
enum ExpirationPolicy {
  // Default value indicating no expiration policy was specified
  EXPIRATION_POLICY_UNSPECIFIED = 0;

  // Time-to-live based expiration - items expire after a fixed duration
  EXPIRATION_POLICY_TTL = 1;

  // Idle time expiration - items expire after being unused for a duration
  EXPIRATION_POLICY_IDLE = 2;

  // Write time expiration - items expire after a duration from last write
  EXPIRATION_POLICY_WRITE = 3;

  // Never expire - items remain in cache until explicitly removed
  EXPIRATION_POLICY_NEVER = 4;
}
```

---

### export_format.proto {#export_format}

**Path**: `gcommon/v1/common/export_format.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `CommonExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/export_format.proto
// version: 1.0.1
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ExportFormat enumerates data export formats used across all systems
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonExportFormat {
  EXPORT_FORMAT_UNSPECIFIED = 0;
  EXPORT_FORMAT_PROMETHEUS = 1;
  EXPORT_FORMAT_JSON = 2;
  EXPORT_FORMAT_CSV = 3;
  EXPORT_FORMAT_OPENTELEMETRY = 4;
}
```

---

### file_sort_order.proto {#file_sort_order}

**Path**: `gcommon/v1/common/file_sort_order.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `FileSortOrder`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/file_sort_order.proto
// version: 1.0.1
// guid: f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * File sorting options.
 * Defines how files should be ordered in directory listings.
 */
enum FileSortOrder {
  // Default sorting (name ascending)
  FILE_SORT_ORDER_UNSPECIFIED = 0;

  // Sort by name ascending
  FILE_SORT_ORDER_NAME_ASC = 1;

  // Sort by name descending
  FILE_SORT_ORDER_NAME_DESC = 2;

  // Sort by size ascending
  FILE_SORT_ORDER_SIZE_ASC = 3;

  // Sort by size descending
  FILE_SORT_ORDER_SIZE_DESC = 4;

  // Sort by modification time ascending
  FILE_SORT_ORDER_MODIFIED_ASC = 5;

  // Sort by modification time descending
  FILE_SORT_ORDER_MODIFIED_DESC = 6;
}
```

---

### filter_action.proto {#filter_action}

**Path**: `gcommon/v1/common/filter_action.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `FilterAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/filter_action.proto
// version: 1.0.1
// guid: 733209f2-fa3d-471a-b3c3-260adaecd3a2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum FilterAction {
  FILTER_ACTION_UNSPECIFIED = 0;
  FILTER_ACTION_INCLUDE = 1;
  FILTER_ACTION_EXCLUDE = 2;
  FILTER_ACTION_TRANSFORM = 3;
  FILTER_ACTION_VALIDATE = 4;
}
```

---

### filter_operation.proto {#filter_operation}

**Path**: `gcommon/v1/common/filter_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `FilterOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_operation.proto
// version: 1.0.1
// guid: 792c2366-c261-43b4-8647-d776a7245cc2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Filter operation types for query filtering across all GCommon modules.
 * Provides standardized filtering operations for database queries, search,
 * and other filtering requirements.
 */
enum FilterOperation {
  // Default value indicating no filter operation was specified
  FILTER_OPERATION_UNSPECIFIED = 0;

  // Exact equality match
  FILTER_OPERATION_EQUALS = 1;

  // Not equal to the specified value
  FILTER_OPERATION_NOT_EQUALS = 2;

  // Greater than the specified value (numeric/date comparison)
  FILTER_OPERATION_GREATER_THAN = 3;

  // Less than the specified value (numeric/date comparison)
  FILTER_OPERATION_LESS_THAN = 4;

  // Greater than or equal to the specified value
  FILTER_OPERATION_GREATER_THAN_OR_EQUAL = 5;

  // Less than or equal to the specified value
  FILTER_OPERATION_LESS_THAN_OR_EQUAL = 6;

  // Contains the specified substring (case-sensitive)
  FILTER_OPERATION_CONTAINS = 7;

  // Starts with the specified prefix
  FILTER_OPERATION_STARTS_WITH = 8;

  // Ends with the specified suffix
  FILTER_OPERATION_ENDS_WITH = 9;

  // Value is contained in the specified list
  FILTER_OPERATION_IN = 10;

  // Value is not contained in the specified list
  FILTER_OPERATION_NOT_IN = 11;
}
```

---

### filter_type.proto {#filter_type}

**Path**: `gcommon/v1/common/filter_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `LogFilterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_type.proto
// version: 1.0.1
// guid: eb317c45-0d04-48fb-ab44-ab82262f995b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// FilterType enumerates log filter strategies
// buf:lint:ignore ENUM_VALUE_PREFIX
enum LogFilterType {
  FILTER_TYPE_UNSPECIFIED = 0;
  FILTER_TYPE_LEVEL = 1;
  FILTER_TYPE_LOGGER = 2;
  FILTER_TYPE_MESSAGE = 3;
  FILTER_TYPE_FIELD = 4;
}
```

---

### flush_policy.proto {#flush_policy}

**Path**: `gcommon/v1/common/flush_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `FlushPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/flush_policy.proto
// file: proto/gcommon/v1/queue/flush_policy.proto
// version: 1.0.1
// guid: 0a9b8c7d-6e5f-4a3b-2c1d-0e9f8a7b6c5d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Policy for when to flush messages to persistent storage.
 */
enum FlushPolicy {
  // Default unspecified policy
  FLUSH_POLICY_UNSPECIFIED = 0;

  // Flush immediately after each message
  FLUSH_POLICY_IMMEDIATE = 1;

  // Flush after a certain number of messages
  FLUSH_POLICY_BATCH = 2;

  // Flush after a time interval
  FLUSH_POLICY_TIMED = 3;

  // Flush when buffer is full
  FLUSH_POLICY_BUFFER_FULL = 4;

  // Manual flush only
  FLUSH_POLICY_MANUAL = 5;
}
```

---

### formatter_type.proto {#formatter_type}

**Path**: `gcommon/v1/common/formatter_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `FormatterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/formatter_type.proto
// version: 1.0.1
// guid: 0d49c8f5-9abd-4a9e-8d96-ddab6f45249b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// FormatterType enumerates log formatting strategies
enum FormatterType {
  FORMATTER_TYPE_UNSPECIFIED = 0;
  FORMATTER_TYPE_TEXT = 1;
  FORMATTER_TYPE_JSON = 2;
  FORMATTER_TYPE_XML = 3;
  FORMATTER_TYPE_CUSTOM = 4;
}
```

---

### gauge_operation.proto {#gauge_operation}

**Path**: `gcommon/v1/common/gauge_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `GaugeOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/gauge_operation.proto
// version: 1.0.1
// guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GaugeOperation defines how to update the gauge value.
 * Specifies the operation to perform on a gauge metric.
 */
enum GaugeOperation {
  // Unspecified operation (defaults to SET)
  GAUGE_OPERATION_UNSPECIFIED = 0;

  // Set the gauge to the specified value
  GAUGE_OPERATION_SET = 1;

  // Add the value to the current gauge value
  GAUGE_OPERATION_ADD = 2;

  // Subtract the value from the current gauge value
  GAUGE_OPERATION_SUBTRACT = 3;

  // Increment the gauge by 1
  GAUGE_OPERATION_INCREMENT = 4;

  // Decrement the gauge by 1
  GAUGE_OPERATION_DECREMENT = 5;
}
```

---

### grant_type.proto {#grant_type}

**Path**: `gcommon/v1/common/grant_type.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Enums** (1): `GrantType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/grant_type.proto
// version: 1.0.1
// guid: 75a43fdc-3d73-410d-80b1-00ca7583f150
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth 2.0 grant types supported by the authentication system.
 */
enum GrantType {
  // Unspecified grant type.
  GRANT_TYPE_UNSPECIFIED = 0;

  // Authorization code grant.
  GRANT_TYPE_AUTHORIZATION_CODE = 1;

  // Implicit grant (legacy).
  GRANT_TYPE_IMPLICIT = 2;

  // Resource owner password credentials grant.
  GRANT_TYPE_PASSWORD = 3;

  // Client credentials grant.
  GRANT_TYPE_CLIENT_CREDENTIALS = 4;

  // Refresh token grant.
  GRANT_TYPE_REFRESH_TOKEN = 5;

  // Device code grant for device authorization flows.
  GRANT_TYPE_DEVICE_CODE = 6;

  // SAML2 bearer assertion grant.
  GRANT_TYPE_SAML2_BEARER = 7;
}
```

---

### handler_type.proto {#handler_type}

**Path**: `gcommon/v1/common/handler_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `HandlerType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/handler_type.proto
// version: 1.0.1
// guid: 38fcdb5d-d9f0-4109-b909-c1da72c74948
//
// HandlerType categorizes incoming request handlers.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HandlerType {
  HANDLER_TYPE_UNSPECIFIED = 0;
  HANDLER_TYPE_HTTP = 1;
  HANDLER_TYPE_GRPC = 2;
  HANDLER_TYPE_WEBSOCKET = 3;
}
```

---

### health_check_type.proto {#health_check_type}

**Path**: `gcommon/v1/common/health_check_type.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Enums** (1): `HealthCheckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_check_type.proto
// version: 1.0.1
// guid: f4a5b6c7-d8e9-0f1a-2b3c-4d5e6f7a8b9c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthCheckType represents the type of health check.
 * Specifies the protocol and method used for environment health checks.
 */
enum HealthCheckType {
  // Unspecified health check type
  HEALTH_CHECK_TYPE_UNSPECIFIED = 0;

  // HTTP health check
  HEALTH_CHECK_TYPE_HTTP = 1;

  // HTTPS health check
  HEALTH_CHECK_TYPE_HTTPS = 2;

  // TCP connection health check
  HEALTH_CHECK_TYPE_TCP = 3;

  // UDP connection health check
  HEALTH_CHECK_TYPE_UDP = 4;

  // gRPC health check
  HEALTH_CHECK_TYPE_GRPC = 5;

  // Database health check
  HEALTH_CHECK_TYPE_DATABASE = 6;

  // Custom health check
  HEALTH_CHECK_TYPE_CUSTOM = 7;
}
```

---

### health_state.proto {#health_state}

**Path**: `gcommon/v1/common/health_state.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `HealthState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/health_state.proto
// version: 1.0.1
// guid: a5b6c7d8-e9f0-1a2b-3c4d-5e6f7a8b9c0d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthState represents the state of health.
 * Specifies the current health condition of environment components.
 */
enum HealthState {
  // Unspecified health state
  HEALTH_STATE_UNSPECIFIED = 0;

  // Component is healthy
  HEALTH_STATE_HEALTHY = 1;

  // Component is degraded but functional
  HEALTH_STATE_DEGRADED = 2;

  // Component is unhealthy
  HEALTH_STATE_UNHEALTHY = 3;

  // Health state is unknown
  HEALTH_STATE_UNKNOWN = 4;
}
```

---

### health_status.proto {#health_status}

**Path**: `gcommon/v1/common/health_status.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `CommonHealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_status.proto
// version: 1.0.1
// guid: f5b71864-058c-43b1-8500-dd1845802068
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common health status enumeration used across all GCommon modules.
 * Provides consistent health reporting for services, components, and resources.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum CommonHealthStatus {
  // Default value indicating health status was not specified
  HEALTH_STATUS_UNSPECIFIED = 0;

  // Service/component is operating normally
  HEALTH_STATUS_HEALTHY = 1;

  // Service/component is not functioning properly
  HEALTH_STATUS_UNHEALTHY = 2;

  // Service/component is partially functioning with degraded performance
  HEALTH_STATUS_DEGRADED = 3;

  // Service/component is in the process of starting up
  HEALTH_STATUS_STARTING = 4;

  // Service/component is in the process of shutting down
  HEALTH_STATUS_STOPPING = 5;
}
```

---

### hierarchy_type.proto {#hierarchy_type}

**Path**: `gcommon/v1/common/hierarchy_type.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `HierarchyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/hierarchy_type.proto
// version: 1.0.1
// guid: 4618131c-f81c-417c-ba7a-46d3f5a9a06b
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Hierarchy type enumeration defining the type of organizational structure.
 * Used to categorize different organizational units and their relationships.
 */
enum HierarchyType {
  // Default value indicating no hierarchy type was specified
  HIERARCHY_TYPE_UNSPECIFIED = 0;

  // Department-based hierarchical structure
  HIERARCHY_TYPE_DEPARTMENT = 1;

  // Team-based organizational structure
  HIERARCHY_TYPE_TEAM = 2;

  // Project-based organizational structure
  HIERARCHY_TYPE_PROJECT = 3;

  // Geographic/location-based structure
  HIERARCHY_TYPE_GEOGRAPHIC = 4;

  // Functional role-based structure
  HIERARCHY_TYPE_FUNCTIONAL = 5;

  // Matrix organizational structure (multi-dimensional)
  HIERARCHY_TYPE_MATRIX = 6;

  // Flat organizational structure (minimal hierarchy)
  HIERARCHY_TYPE_FLAT = 7;
}
```

---

### hook_error_handling.proto {#hook_error_handling}

**Path**: `gcommon/v1/common/hook_error_handling.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `HookErrorHandling`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/hook_error_handling.proto
// version: 1.0.1
// guid: f5c075fd-6a9f-4072-bea8-ee82bb35c1b5

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HookErrorHandling {
  HOOK_ERROR_HANDLING_UNSPECIFIED = 0;
  HOOK_ERROR_HANDLING_IGNORE = 1;
  HOOK_ERROR_HANDLING_WARN = 2;
  HOOK_ERROR_HANDLING_FAIL = 3;
}
```

---

### hook_type.proto {#hook_type}

**Path**: `gcommon/v1/common/hook_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `HookType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/hook_type.proto
// version: 1.0.1
// guid: a9982046-4cf7-4320-91ff-66f4b56b6258

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HookType {
  HOOK_TYPE_UNSPECIFIED = 0;
  HOOK_TYPE_PRE_RENDER = 1;
  HOOK_TYPE_POST_RENDER = 2;
  HOOK_TYPE_PRE_APPLY = 3;
  HOOK_TYPE_POST_APPLY = 4;
  HOOK_TYPE_PRE_VALIDATE = 5;
  HOOK_TYPE_POST_VALIDATE = 6;
}
```

---

### http_method.proto {#http_method}

**Path**: `gcommon/v1/common/http_method.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `HTTPMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_method.proto
// version: 1.0.1
// guid: 91d1cc0e-2cad-460c-81e9-236116f31e05
//
// HTTPMethod enumerates supported request verbs.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HTTPMethod {
  HTTP_METHOD_UNSPECIFIED = 0;
  HTTP_METHOD_GET = 1;
  HTTP_METHOD_POST = 2;
  HTTP_METHOD_PUT = 3;
  HTTP_METHOD_DELETE = 4;
  HTTP_METHOD_PATCH = 5;
  HTTP_METHOD_OPTIONS = 6;
  HTTP_METHOD_HEAD = 7;
}
```

---

### http_status.proto {#http_status}

**Path**: `gcommon/v1/common/http_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `HTTPStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/http_status.proto
// version: 1.0.1
// guid: 8e7253f5-0453-42e2-b55a-336dd5c9b589
//
// HTTPStatus enumerates common response status codes.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum HTTPStatus {
  HTTP_STATUS_UNSPECIFIED = 0;
  HTTP_STATUS_OK = 200;
  HTTP_STATUS_BAD_REQUEST = 400;
  HTTP_STATUS_UNAUTHORIZED = 401;
  HTTP_STATUS_FORBIDDEN = 403;
  HTTP_STATUS_NOT_FOUND = 404;
  HTTP_STATUS_INTERNAL_ERROR = 500;
}
```

---

### inheritance_strategy.proto {#inheritance_strategy}

**Path**: `gcommon/v1/common/inheritance_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `InheritanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/inheritance_strategy.proto
// version: 1.0.1
// guid: 8dc7386b-afe2-4d9d-804d-2286b8ae6cf7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum InheritanceStrategy {
  INHERITANCE_STRATEGY_UNSPECIFIED = 0;
  INHERITANCE_STRATEGY_OVERRIDE = 1;
  INHERITANCE_STRATEGY_MERGE = 2;
  INHERITANCE_STRATEGY_FALLBACK = 3;
  INHERITANCE_STRATEGY_PRIORITY = 4;
  INHERITANCE_STRATEGY_WEIGHTED = 5;
}
```

---

### isolation_level.proto {#isolation_level}

**Path**: `gcommon/v1/common/isolation_level.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `OrganizationIsolationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/isolation_level.proto
// version: 1.0.1
// guid: a922822f-aac2-4d39-ab9c-546cfae195e4
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Isolation level enumeration defining the degree of tenant isolation.
 * Used in multi-tenant architectures to control data and resource separation.
 */
enum OrganizationIsolationLevel {
  // Default value indicating no isolation level was specified
  ISOLATION_LEVEL_UNSPECIFIED = 0;

  // Shared infrastructure with logical separation (lowest cost, shared resources)
  ISOLATION_LEVEL_SHARED = 1;

  // Dedicated database/schema per tenant (medium isolation)
  ISOLATION_LEVEL_DATABASE = 2;

  // Dedicated infrastructure per tenant (highest isolation)
  ISOLATION_LEVEL_INFRASTRUCTURE = 3;

  // Virtual private cloud isolation (network-level separation)
  ISOLATION_LEVEL_NETWORK = 4;

  // Physical server isolation (hardware-level separation)
  ISOLATION_LEVEL_PHYSICAL = 5;
}
```

---

### load_balance_strategy.proto {#load_balance_strategy}

**Path**: `gcommon/v1/common/load_balance_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `LoadBalanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/load_balance_strategy.proto
// version: 1.0.1
// guid: d147b3b5-5e20-4bf9-9cfe-467e528f59a7
//
// LoadBalanceStrategy lists supported balancing algorithms.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum LoadBalanceStrategy {
  LOAD_BALANCE_STRATEGY_UNSPECIFIED = 0;
  LOAD_BALANCE_STRATEGY_ROUND_ROBIN = 1;
  LOAD_BALANCE_STRATEGY_LEAST_CONNECTIONS = 2;
  LOAD_BALANCE_STRATEGY_IP_HASH = 3;
}
```

---

### load_balancing_strategy.proto {#load_balancing_strategy}

**Path**: `gcommon/v1/common/load_balancing_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `LoadBalancingStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/load_balancing_strategy.proto
// version: 1.0.1
// guid: 0d1e2f3a-4b5c-6d7e-8f9a-0b1c2d3e4f5a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Load balancing strategies.
 */
enum LoadBalancingStrategy {
  // Default unspecified strategy
  LOAD_BALANCING_STRATEGY_UNSPECIFIED = 0;

  // Round-robin distribution
  LOAD_BALANCING_STRATEGY_ROUND_ROBIN = 1;

  // Weighted round-robin
  LOAD_BALANCING_STRATEGY_WEIGHTED_ROUND_ROBIN = 2;

  // Least connections
  LOAD_BALANCING_STRATEGY_LEAST_CONNECTIONS = 3;

  // Random distribution
  LOAD_BALANCING_STRATEGY_RANDOM = 4;

  // Hash-based distribution
  LOAD_BALANCING_STRATEGY_HASH = 5;

  // Priority-based distribution
  LOAD_BALANCING_STRATEGY_PRIORITY = 6;
}
```

---

### log_level.proto {#log_level}

**Path**: `gcommon/v1/common/log_level.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `LogLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_level.proto
// version: 1.0.1
// guid: ef4e8667-0bff-4dda-bb43-56d0a1ef8421

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogLevel defines severity levels for log entries
enum LogLevel {
  LOG_LEVEL_UNSPECIFIED = 0;
  LOG_LEVEL_TRACE = 1;
  LOG_LEVEL_DEBUG = 2;
  LOG_LEVEL_INFO = 3;
  LOG_LEVEL_WARN = 4;
  LOG_LEVEL_ERROR = 5;
  LOG_LEVEL_FATAL = 6;
}
```

---

### log_sort_field.proto {#log_sort_field}

**Path**: `gcommon/v1/common/log_sort_field.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `LogSortField`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_sort_field.proto
// version: 1.0.1
// guid: 8d1776a3-51f0-43c4-8199-698ee5ba98e7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogSortField enumerates fields usable for log sorting
enum LogSortField {
  LOG_SORT_FIELD_UNSPECIFIED = 0;
  LOG_SORT_FIELD_TIMESTAMP = 1;
  LOG_SORT_FIELD_LEVEL = 2;
  LOG_SORT_FIELD_LOGGER = 3;
  LOG_SORT_FIELD_MESSAGE = 4;
}
```

---

### logger_status.proto {#logger_status}

**Path**: `gcommon/v1/common/logger_status.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `LoggerStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logger_status.proto
// version: 1.0.1
// guid: c65806e5-27c2-4c3e-8f3b-e23b66bca610

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LoggerStatus represents health of a logger instance
enum LoggerStatus {
  LOGGER_STATUS_UNSPECIFIED = 0;
  LOGGER_STATUS_ACTIVE = 1;
  LOGGER_STATUS_INACTIVE = 2;
  LOGGER_STATUS_ERROR = 3;
}
```

---

### media_type.proto {#media_type}

**Path**: `gcommon/v1/common/media_type.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `MediaType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_type.proto
// version: 1.0.1
// guid: d13c4939-a91b-4cb8-85e6-09ddda85220e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Media type classification for library items.
enum MediaType {
  MEDIA_TYPE_UNSPECIFIED = 0;
  MEDIA_TYPE_MOVIE = 1;
  MEDIA_TYPE_TV_EPISODE = 2;
  MEDIA_TYPE_DOCUMENTARY = 3;
  MEDIA_TYPE_ANIME = 4;
  MEDIA_TYPE_AUDIOBOOK = 5;
  MEDIA_TYPE_PODCAST = 6;
  MEDIA_TYPE_MUSIC = 7;
  MEDIA_TYPE_LECTURE = 8;
  MEDIA_TYPE_INTERVIEW = 9;
  MEDIA_TYPE_RADIO_SHOW = 10;
}
```

---

### member_role.proto {#member_role}

**Path**: `gcommon/v1/common/member_role.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `MemberRole`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/member_role.proto
// version: 1.0.1
// guid: b6c7d8e9-012b-467a-1234-789012345678

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MemberRole {
  MEMBER_ROLE_UNSPECIFIED = 0;
  MEMBER_ROLE_OWNER = 1;
  MEMBER_ROLE_ADMIN = 2;
  MEMBER_ROLE_MEMBER = 3;
  MEMBER_ROLE_VIEWER = 4;
  MEMBER_ROLE_GUEST = 5;
}
```

---

### merge_strategy.proto {#merge_strategy}

**Path**: `gcommon/v1/common/merge_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `MergeStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/merge_strategy.proto
// version: 1.0.1
// guid: 559ca0d7-17d4-49ab-861d-febdc5862a47

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MergeStrategy {
  MERGE_STRATEGY_UNSPECIFIED = 0;
  MERGE_STRATEGY_REPLACE = 1;
  MERGE_STRATEGY_MERGE_DEEP = 2;
  MERGE_STRATEGY_MERGE_SHALLOW = 3;
  MERGE_STRATEGY_ARRAY_CONCAT = 4;
  MERGE_STRATEGY_ARRAY_REPLACE = 5;
  MERGE_STRATEGY_ARRAY_MERGE = 6;
  MERGE_STRATEGY_CUSTOM = 7;
}
```

---

### message_state.proto {#message_state}

**Path**: `gcommon/v1/common/message_state.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `MessageState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_state.proto
// version: 1.0.1
// guid: 4eba7921-816c-420b-8880-172c0631fa22

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// MessageState represents the lifecycle state of a queue message.
enum MessageState {
  // Default unspecified state.
  MESSAGE_STATE_UNSPECIFIED = 0;

  // Message is queued and awaiting delivery.
  MESSAGE_STATE_PENDING = 1;

  // Message has been delivered to a consumer.
  MESSAGE_STATE_DELIVERED = 2;

  // Consumer acknowledged successful processing.
  MESSAGE_STATE_ACKNOWLEDGED = 3;

  // Delivery failed and will be retried.
  MESSAGE_STATE_FAILED = 4;

  // Message moved to dead letter queue.
  MESSAGE_STATE_DEAD_LETTER = 5;

  // Message expired before processing.
  MESSAGE_STATE_EXPIRED = 6;
}
```

---

### metadata_status.proto {#metadata_status}

**Path**: `gcommon/v1/common/metadata_status.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `MetadataStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/metadata_status.proto
// version: 1.0.1
// guid: b82301c8-c50d-454c-a434-ae44d4199677

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MetadataStatus {
  METADATA_STATUS_UNSPECIFIED = 0;
  METADATA_STATUS_ACTIVE = 1;
  METADATA_STATUS_INACTIVE = 2;
  METADATA_STATUS_DRAFT = 3;
  METADATA_STATUS_DEPRECATED = 4;
  METADATA_STATUS_DELETED = 5;
  METADATA_STATUS_ERROR = 6;
}
```

---

### metric_source.proto {#metric_source}

**Path**: `gcommon/v1/common/metric_source.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Enums** (1): `MetricSource`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_source.proto
// version: 1.0.1
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// MetricSource represents different sources of metrics data
enum MetricSource {
  // Unspecified metric source
  METRIC_SOURCE_UNSPECIFIED = 0;

  // Application metrics
  METRIC_SOURCE_APPLICATION = 1;

  // System metrics
  METRIC_SOURCE_SYSTEM = 2;

  // Infrastructure metrics
  METRIC_SOURCE_INFRASTRUCTURE = 3;

  // Container metrics
  METRIC_SOURCE_CONTAINER = 4;

  // Kubernetes metrics
  METRIC_SOURCE_KUBERNETES = 5;

  // Database metrics
  METRIC_SOURCE_DATABASE = 6;

  // Network metrics
  METRIC_SOURCE_NETWORK = 7;

  // Storage metrics
  METRIC_SOURCE_STORAGE = 8;

  // Security metrics
  METRIC_SOURCE_SECURITY = 9;

  // Business metrics
  METRIC_SOURCE_BUSINESS = 10;

  // Custom metrics
  METRIC_SOURCE_CUSTOM = 11;

  // Third-party metrics
  METRIC_SOURCE_THIRD_PARTY = 12;

  // Synthetic metrics
  METRIC_SOURCE_SYNTHETIC = 13;

  // Log-derived metrics
  METRIC_SOURCE_LOG_DERIVED = 14;
}
```

---

### metric_status.proto {#metric_status}

**Path**: `gcommon/v1/common/metric_status.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `MetricStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_status.proto
// version: 1.0.1
// guid: 0f4752cc-8120-45bb-a7c9-1fb475c11998

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MetricStatus indicates the lifecycle state of a metric definition.
 */
enum MetricStatus {
  // Unspecified status.
  METRIC_STATUS_UNSPECIFIED = 0;

  // Metric is active and being collected.
  METRIC_STATUS_ACTIVE = 1;

  // Metric is temporarily disabled.
  METRIC_STATUS_DISABLED = 2;

  // Metric is in error state and not reliable.
  METRIC_STATUS_ERROR = 3;

  // Metric has been removed and should no longer be used.
  METRIC_STATUS_DELETED = 4;
}
```

---

### metric_type.proto {#metric_type}

**Path**: `gcommon/v1/common/metric_type.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `MetricsMetricType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/metric_type.proto
// version: 1.0.1
// guid: ca7deb46-60dd-4b1b-a48a-ad30f651f2a2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MetricType defines the different types of metrics that can be collected.
 * Each type has specific semantics for how values are interpreted and aggregated.
 */
enum MetricsMetricType {
  // Unspecified metric type
  METRIC_TYPE_UNSPECIFIED = 0;

  // Counter: A monotonically increasing value (can only go up)
  METRIC_TYPE_COUNTER = 1;

  // Gauge: A value that can go up and down
  METRIC_TYPE_GAUGE = 2;

  // Histogram: Distribution of observed values in buckets
  METRIC_TYPE_HISTOGRAM = 3;

  // Summary: Similar to histogram but with configurable quantiles
  METRIC_TYPE_SUMMARY = 4;

  // Timer: Specialized counter for measuring durations
  METRIC_TYPE_TIMER = 5;

  // Set: Track unique values (cardinality metric)
  METRIC_TYPE_SET = 6;
}
```

---

### metrics_alert_severity.proto {#metrics_alert_severity}

**Path**: `gcommon/v1/common/metrics_alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `MetricsAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/alert_severity.proto
// version: 1.0.1
// guid: f1a2b3c4-5678-901c-5678-123456789012

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MetricsAlertSeverity {
  METRICS_ALERT_SEVERITY_UNSPECIFIED = 0;
  METRICS_ALERT_SEVERITY_LOW = 1;
  METRICS_ALERT_SEVERITY_MEDIUM = 2;
  METRICS_ALERT_SEVERITY_HIGH = 3;
  METRICS_ALERT_SEVERITY_CRITICAL = 4;
}
```

---

### metrics_export_format.proto {#metrics_export_format}

**Path**: `gcommon/v1/common/metrics_export_format.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `MetricsExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/export_format.proto
// version: 1.0.1
// guid: b4c5d6e7-890b-245a-9012-567890123456

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MetricsExportFormat {
  METRICS_EXPORT_FORMAT_UNSPECIFIED = 0;
  METRICS_EXPORT_FORMAT_PROMETHEUS = 1;
  METRICS_EXPORT_FORMAT_JSON = 2;
  METRICS_EXPORT_FORMAT_CSV = 3;
  METRICS_EXPORT_FORMAT_OPENTELEMETRY = 4;
}
```

---

### metrics_provider_type.proto {#metrics_provider_type}

**Path**: `gcommon/v1/common/metrics_provider_type.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Enums** (1): `MetricsProviderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/provider_type.proto
// version: 1.0.1
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Provider type enumeration.
 * Defines the different types of metrics providers supported.
 */
enum MetricsProviderType {
  METRICS_PROVIDER_TYPE_UNSPECIFIED = 0;
  METRICS_PROVIDER_TYPE_PROMETHEUS = 1;
  METRICS_PROVIDER_TYPE_INFLUXDB = 2;
  METRICS_PROVIDER_TYPE_GRAPHITE = 3;
  METRICS_PROVIDER_TYPE_DATADOG = 4;
  METRICS_PROVIDER_TYPE_NEW_RELIC = 5;
  METRICS_PROVIDER_TYPE_CLOUDWATCH = 6;
  METRICS_PROVIDER_TYPE_STACKDRIVER = 7;
  METRICS_PROVIDER_TYPE_CUSTOM = 8;
}
```

---

### mfa_method.proto {#mfa_method}

**Path**: `gcommon/v1/common/mfa_method.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `MfaMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_method.proto
// version: 1.0.1
// guid: 123e4567-e89b-12d3-a456-426614174123

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Multi-factor authentication methods supported by the system.
 */
enum MfaMethod {
  // Unspecified MFA method
  MFA_METHOD_UNSPECIFIED = 0;

  // SMS-based verification
  MFA_METHOD_SMS = 1;

  // Email-based verification
  MFA_METHOD_EMAIL = 2;

  // Time-based one-time password (TOTP)
  MFA_METHOD_TOTP = 3;

  // Hardware security key
  MFA_METHOD_HARDWARE_KEY = 4;
}
```

---

### mfa_type.proto {#mfa_type}

**Path**: `gcommon/v1/common/mfa_type.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `MFAType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_type.proto
// version: 1.0.1
// guid: a5e413ea-00e3-4585-9e9d-30348138c407

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MFAType enumerates supported multi-factor authentication methods.
 */
enum MFAType {
  // Unknown or unspecified MFA method
  MFA_TYPE_UNSPECIFIED = 0;

  // Time-based one-time password via authenticator apps
  MFA_TYPE_TOTP = 1;

  // One-time code delivered via SMS
  MFA_TYPE_SMS = 2;

  // One-time code delivered via email
  MFA_TYPE_EMAIL = 3;

  // Push notification to a trusted device
  MFA_TYPE_PUSH = 4;
}
```

---

### middleware_type.proto {#middleware_type}

**Path**: `gcommon/v1/common/middleware_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `MiddlewareType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/middleware_type.proto
// version: 1.0.1
// guid: e6a7b5cb-240b-4636-bb49-9615874e9f9d
//
// MiddlewareType represents categories of HTTP middleware.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum MiddlewareType {
  MIDDLEWARE_TYPE_UNSPECIFIED = 0;
  MIDDLEWARE_TYPE_LOGGING = 1;
  MIDDLEWARE_TYPE_AUTHENTICATION = 2;
  MIDDLEWARE_TYPE_METRICS = 3;
  MIDDLEWARE_TYPE_COMPRESSION = 4;
  MIDDLEWARE_TYPE_CORS = 5;
  MIDDLEWARE_TYPE_RATE_LIMIT = 6;
}
```

---

### nack_error_category.proto {#nack_error_category}

**Path**: `gcommon/v1/common/nack_error_category.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `NackErrorCategory`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_error_category.proto
// version: 1.0.1
// guid: 8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Categories of NACK errors.
 */
enum NackErrorCategory {
  // Default unspecified category
  NACK_ERROR_CATEGORY_UNSPECIFIED = 0;

  // Temporary/transient error
  NACK_ERROR_CATEGORY_TEMPORARY = 1;

  // Permanent error (should not retry)
  NACK_ERROR_CATEGORY_PERMANENT = 2;

  // Configuration error
  NACK_ERROR_CATEGORY_CONFIGURATION = 3;

  // Network error
  NACK_ERROR_CATEGORY_NETWORK = 4;

  // Authentication/authorization error
  NACK_ERROR_CATEGORY_AUTH = 5;

  // Rate limiting error
  NACK_ERROR_CATEGORY_RATE_LIMIT = 6;
}
```

---

### node_state.proto {#node_state}

**Path**: `gcommon/v1/common/node_state.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `NodeState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/node_state.proto
// version: 1.0.1
// guid: 9ee731f7-a1ea-4298-8579-c001d3b09060

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * State of a cluster node.
 */
enum NodeState {
  // Default unspecified state
  NODE_STATE_UNSPECIFIED = 0;

  // Node is active and healthy
  NODE_STATE_ACTIVE = 1;

  // Node is inactive but reachable
  NODE_STATE_INACTIVE = 2;

  // Node is unreachable
  NODE_STATE_UNREACHABLE = 3;

  // Node is joining the cluster
  NODE_STATE_JOINING = 4;

  // Node is leaving the cluster
  NODE_STATE_LEAVING = 5;
}
```

---

### notification_channel_type.proto {#notification_channel_type}

**Path**: `gcommon/v1/common/notification_channel_type.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `NotificationChannelType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/notification_channel_type.proto
// version: 1.0.1
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Types of notification channels.
 */
enum NotificationChannelType {
  // Default unspecified type
  NOTIFICATION_CHANNEL_TYPE_UNSPECIFIED = 0;

  // Email notifications
  NOTIFICATION_CHANNEL_TYPE_EMAIL = 1;

  // Slack notifications
  NOTIFICATION_CHANNEL_TYPE_SLACK = 2;

  // SMS notifications
  NOTIFICATION_CHANNEL_TYPE_SMS = 3;

  // Webhook notifications
  NOTIFICATION_CHANNEL_TYPE_WEBHOOK = 4;

  // PagerDuty integration
  NOTIFICATION_CHANNEL_TYPE_PAGERDUTY = 5;
}
```

---

### notification_trigger.proto {#notification_trigger}

**Path**: `gcommon/v1/common/notification_trigger.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `NotificationTrigger`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/notification_trigger.proto
// version: 1.0.1
// guid: e23c0d82-9395-4a27-840c-5765e4aaffbb

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum NotificationTrigger {
  NOTIFICATION_TRIGGER_UNSPECIFIED = 0;
  NOTIFICATION_TRIGGER_CHANGE = 1;
  NOTIFICATION_TRIGGER_DELETE = 2;
  NOTIFICATION_TRIGGER_ERROR = 3;
  NOTIFICATION_TRIGGER_APPROVAL = 4;
  NOTIFICATION_TRIGGER_DEPLOYMENT = 5;
  NOTIFICATION_TRIGGER_ROLLBACK = 6;
  NOTIFICATION_TRIGGER_SCHEDULE = 7;
}
```

---

### notification_type.proto {#notification_type}

**Path**: `gcommon/v1/common/notification_type.proto` **Package**: `gcommon.v1.common` **Lines**: 64

**Enums** (1): `NotificationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/types/notification_type.proto
// version: 1.0.1
// guid: c1381807-afc6-4139-8737-8691569a66f9
// file: proto/gcommon/v1/metrics/notification_type.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * NotificationType defines the types of notifications for metric alerts.
 * Used to specify how alerts should be delivered to users.
 */
enum NotificationType {
  // Unspecified notification type (default)
  NOTIFICATION_TYPE_UNSPECIFIED = 0;

  // Email notification
  NOTIFICATION_TYPE_EMAIL = 1;

  // SMS text message
  NOTIFICATION_TYPE_SMS = 2;

  // Push notification (mobile app)
  NOTIFICATION_TYPE_PUSH = 3;

  // Slack message
  NOTIFICATION_TYPE_SLACK = 4;

  // Microsoft Teams message
  NOTIFICATION_TYPE_TEAMS = 5;

  // Discord message
  NOTIFICATION_TYPE_DISCORD = 6;

  // PagerDuty incident
  NOTIFICATION_TYPE_PAGERDUTY = 7;

  // Webhook/HTTP POST
  NOTIFICATION_TYPE_WEBHOOK = 8;

  // In-app notification
  NOTIFICATION_TYPE_IN_APP = 9;

  // SNMP trap
  NOTIFICATION_TYPE_SNMP = 10;

  // Telegram message
  NOTIFICATION_TYPE_TELEGRAM = 11;

  // Matrix message
  NOTIFICATION_TYPE_MATRIX = 12;

  // Voice call
  NOTIFICATION_TYPE_VOICE = 13;
}
```

---

### numeric_format.proto {#numeric_format}

**Path**: `gcommon/v1/common/numeric_format.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `NumericFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/numeric_format.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * NumericFormat defines how numeric values should be formatted.
 * Specifies the display format for numeric metric values.
 */
enum NumericFormat {
  // Unspecified format
  NUMERIC_FORMAT_UNSPECIFIED = 0;

  // Default formatting
  NUMERIC_FORMAT_DEFAULT = 1;

  // Scientific notation
  NUMERIC_FORMAT_SCIENTIFIC = 2;

  // Engineering notation
  NUMERIC_FORMAT_ENGINEERING = 3;

  // Percentage format
  NUMERIC_FORMAT_PERCENTAGE = 4;
}
```

---

### oauth2_flow_type.proto {#oauth2_flow_type}

**Path**: `gcommon/v1/common/oauth2_flow_type.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Enums** (1): `OAuth2FlowType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/oauth2_flow_type.proto
// version: 1.1.1
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 flow types.
 * Defines the different OAuth2 authentication flows supported.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum OAuth2FlowType {
  // Unspecified flow type
  OAUTH2_FLOW_TYPE_UNSPECIFIED = 0;

  // Authorization code flow
  OAUTH2_FLOW_TYPE_AUTHORIZATION_CODE = 1;

  // Implicit flow
  OAUTH2_FLOW_TYPE_IMPLICIT = 2;

  // Client credentials flow
  OAUTH2_FLOW_TYPE_CLIENT_CREDENTIALS = 3;

  // Device code flow
  OAUTH2_FLOW_TYPE_DEVICE_CODE = 4;
}
```

---

### offset_reset_strategy.proto {#offset_reset_strategy}

**Path**: `gcommon/v1/common/offset_reset_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `OffsetResetStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_reset_strategy.proto
// version: 1.0.1
// guid: edeef434-6f08-4fc1-be80-abdba95096d6

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum OffsetResetStrategy {
  OFFSET_RESET_STRATEGY_UNSPECIFIED = 0;
  OFFSET_RESET_STRATEGY_EARLIEST = 1; // Start from earliest available offset
  OFFSET_RESET_STRATEGY_LATEST = 2; // Start from latest offset
  OFFSET_RESET_STRATEGY_NONE = 3; // Fail if no committed offset
  OFFSET_RESET_STRATEGY_TIMESTAMP = 4; // Start from specific timestamp
}
```

---

### offset_type.proto {#offset_type}

**Path**: `gcommon/v1/common/offset_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `OffsetType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_type.proto
// version: 1.0.1
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Types of offsets that can be retrieved.
 * Defines different offset positions in a queue or partition.
 */
enum OffsetType {
  // Unspecified offset type
  OFFSET_TYPE_UNSPECIFIED = 0;

  // Earliest available offset
  OFFSET_TYPE_EARLIEST = 1;

  // Latest available offset
  OFFSET_TYPE_LATEST = 2;

  // Current consumer offset
  OFFSET_TYPE_CURRENT = 3;

  // Committed offset for consumer group
  OFFSET_TYPE_COMMITTED = 4;
}
```

---

### ordering_level.proto {#ordering_level}

**Path**: `gcommon/v1/common/ordering_level.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `OrderingLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ordering_level.proto
// version: 1.0.1
// guid: e1d35748-c24e-4dd1-91e8-edd9e4b62959

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum OrderingLevel {
  ORDERING_LEVEL_UNSPECIFIED = 0;
  ORDERING_LEVEL_NONE = 1; // No ordering guarantees
  ORDERING_LEVEL_PARTIAL = 2; // Partial ordering
  ORDERING_LEVEL_TOTAL = 3; // Total ordering
}
```

---

### organization_status.proto {#organization_status}

**Path**: `gcommon/v1/common/organization_status.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `OrganizationStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/organization_status.proto
// version: 1.0.1
// guid: de37f968-280f-4858-9e68-72917e89b7c8
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Organization status enumeration defining the state of an organization.
 * Used to track organization lifecycle, operational status, and access permissions.
 */
enum OrganizationStatus {
  // Default value indicating no status was specified
  ORGANIZATION_STATUS_UNSPECIFIED = 0;

  // Organization is active and operational
  ORGANIZATION_STATUS_ACTIVE = 1;

  // Organization is inactive (temporarily suspended operations)
  ORGANIZATION_STATUS_INACTIVE = 2;

  // Organization is suspended due to policy violations or billing issues
  ORGANIZATION_STATUS_SUSPENDED = 3;

  // Organization is pending verification or onboarding completion
  ORGANIZATION_STATUS_PENDING = 4;

  // Organization is archived (read-only access, no new operations)
  ORGANIZATION_STATUS_ARCHIVED = 5;

  // Organization is marked for deletion and undergoing cleanup
  ORGANIZATION_STATUS_DELETED = 6;
}
```

---

### parameter_type.proto {#parameter_type}

**Path**: `gcommon/v1/common/parameter_type.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `ParameterType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/parameter_type.proto
// version: 1.0.1
// guid: ef891bab-fd5b-433d-9db4-42ff7a05b986

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ParameterType {
  PARAMETER_TYPE_UNSPECIFIED = 0;
  PARAMETER_TYPE_STRING = 1;
  PARAMETER_TYPE_INTEGER = 2;
  PARAMETER_TYPE_FLOAT = 3;
  PARAMETER_TYPE_BOOLEAN = 4;
  PARAMETER_TYPE_ENUM = 5;
  PARAMETER_TYPE_ARRAY = 6;
  PARAMETER_TYPE_OBJECT = 7;
  PARAMETER_TYPE_FILE = 8;
  PARAMETER_TYPE_URL = 9;
  PARAMETER_TYPE_EMAIL = 10;
  PARAMETER_TYPE_PASSWORD = 11;
  PARAMETER_TYPE_DATE = 12;
  PARAMETER_TYPE_TIME = 13;
  PARAMETER_TYPE_DATETIME = 14;
}
```

---

### partition_strategy.proto {#partition_strategy}

**Path**: `gcommon/v1/common/partition_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `PartitionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_strategy.proto
// version: 1.0.1
// guid: f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Partitioning strategies for queue messages.
 * Determines how messages are distributed across partitions.
 */
enum PartitionStrategy {
  // Default partitioning strategy
  PARTITION_STRATEGY_UNSPECIFIED = 0;

  // Round-robin distribution across partitions
  PARTITION_STRATEGY_ROUND_ROBIN = 1;

  // Hash-based partitioning using message key
  PARTITION_STRATEGY_HASH = 2;

  // Random partition assignment
  PARTITION_STRATEGY_RANDOM = 3;

  // Manual partition specification
  PARTITION_STRATEGY_MANUAL = 4;

  // Sticky partitioning (same producer uses same partition)
  PARTITION_STRATEGY_STICKY = 5;

  // Load-based partitioning (least loaded partition)
  PARTITION_STRATEGY_LOAD_BALANCED = 6;
}
```

---

### permission_level.proto {#permission_level}

**Path**: `gcommon/v1/common/permission_level.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `AuthPermissionLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_level.proto
// version: 1.0.1
// guid: 776ae326-7f13-4a07-9c1d-255140b0f83b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthPermissionLevel {
  PERMISSION_LEVEL_UNSPECIFIED = 0;
  PERMISSION_LEVEL_SYSTEM = 1;
  PERMISSION_LEVEL_ORGANIZATION = 2;
  PERMISSION_LEVEL_PROJECT = 3;
  PERMISSION_LEVEL_RESOURCE = 4;
}
```

---

### permission_scope.proto {#permission_scope}

**Path**: `gcommon/v1/common/permission_scope.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `PermissionScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_scope.proto
// version: 1.0.1
// guid: 223f7d62-a27f-4724-8f07-6c99d1afaa17
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission scope enumeration defining the level at which permissions apply.
 * Used for fine-grained access control and permission inheritance.
 */
enum PermissionScope {
  // Unspecified permission scope
  PERMISSION_SCOPE_UNSPECIFIED = 0;

  // Global system-wide permission
  PERMISSION_SCOPE_GLOBAL = 1;

  // Organization-level permission
  PERMISSION_SCOPE_ORGANIZATION = 2;

  // Project-level permission
  PERMISSION_SCOPE_PROJECT = 3;

  // Resource-level permission
  PERMISSION_SCOPE_RESOURCE = 4;

  // User-level permission
  PERMISSION_SCOPE_USER = 5;
}
```

---

### permission_type.proto {#permission_type}

**Path**: `gcommon/v1/common/permission_type.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Enums** (1): `PermissionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_type.proto
// version: 1.0.1
// guid: 2e23ed6f-5620-4c13-a485-eaeb2d0edf25
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission categories for authorization decisions.
 */
enum PermissionType {
  // Unspecified permission type.
  PERMISSION_TYPE_UNSPECIFIED = 0;

  // Read-only access.
  PERMISSION_TYPE_READ = 1;

  // Write access.
  PERMISSION_TYPE_WRITE = 2;

  // Delete access.
  PERMISSION_TYPE_DELETE = 3;

  // Administrative privileges.
  PERMISSION_TYPE_ADMIN = 4;

  // Execute or run operations.
  PERMISSION_TYPE_EXECUTE = 5;
}
```

---

### priority_level.proto {#priority_level}

**Path**: `gcommon/v1/common/priority_level.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `PriorityLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/priority_level.proto
// version: 1.0.1
// guid: e13c77fc-1bf7-42ed-947a-6e1ed4914bb2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// PriorityLevel defines generic priority classes for queue messages.
// buf:lint:ignore ENUM_VALUE_PREFIX
enum PriorityLevel {
  // Default unspecified priority.
  QUEUE_PRIORITY_LEVEL_UNSPECIFIED = 0;
  // Low priority messages are processed after normal traffic.
  QUEUE_PRIORITY_LEVEL_LOW = 1;
  // Normal priority for standard workload.
  QUEUE_PRIORITY_LEVEL_MEDIUM = 2;
  // High priority messages are processed before others.
  QUEUE_PRIORITY_LEVEL_HIGH = 3;
  // Critical messages are processed immediately with highest importance.
  QUEUE_PRIORITY_LEVEL_CRITICAL = 4;
}
```

---

### processing_status.proto {#processing_status}

**Path**: `gcommon/v1/common/processing_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `ProcessingStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/processing_status.proto
// version: 1.0.1
// guid: ef01234-5678-9abc-c5d6-e7f8a9b0c1d2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Status of media processing jobs.
enum ProcessingStatus {
  PROCESSING_STATUS_UNSPECIFIED = 0;
  PROCESSING_STATUS_PENDING = 1;
  PROCESSING_STATUS_PROCESSING = 2;
  PROCESSING_STATUS_COMPLETED = 3;
  PROCESSING_STATUS_FAILED = 4;
  PROCESSING_STATUS_CANCELLED = 5;
  PROCESSING_STATUS_PAUSED = 6;
}
```

---

### provider_state.proto {#provider_state}

**Path**: `gcommon/v1/common/provider_state.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `ProviderState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/provider_state.proto
// version: 1.0.1
// guid: 123e4567-e89b-12d3-a456-426614174024

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ProviderState defines the possible states of a provider.
 */
enum ProviderState {
  PROVIDER_STATE_UNSPECIFIED = 0;
  PROVIDER_STATE_CREATING = 1;
  PROVIDER_STATE_STARTING = 2;
  PROVIDER_STATE_RUNNING = 3;
  PROVIDER_STATE_STOPPING = 4;
  PROVIDER_STATE_STOPPED = 5;
  PROVIDER_STATE_ERROR = 6;
  PROVIDER_STATE_UNKNOWN = 7;
}
```

---

### provider_type.proto {#provider_type}

**Path**: `gcommon/v1/common/provider_type.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `AuthProviderType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/provider_type.proto
// version: 1.0.1
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f90

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ProviderType enumerates the supported authentication provider backends.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthProviderType {
  // Default unspecified provider type
  AUTH_PROVIDER_TYPE_UNSPECIFIED = 0;

  // Built-in local provider
  AUTH_PROVIDER_TYPE_LOCAL = 1;

  // LDAP directory provider
  AUTH_PROVIDER_TYPE_LDAP = 2;

  // Active Directory provider
  AUTH_PROVIDER_TYPE_ACTIVE_DIRECTORY = 3;

  // OAuth2 provider (generic)
  AUTH_PROVIDER_TYPE_OAUTH2 = 4;

  // SAML provider
  AUTH_PROVIDER_TYPE_SAML = 5;
}
```

---

### proxy_type.proto {#proxy_type}

**Path**: `gcommon/v1/common/proxy_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ProxyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/proxy_type.proto
// version: 1.0.1
// guid: 9b6f5494-a0d0-4832-a3f3-9d91dbf2c200
//
// ProxyType lists supported proxy configurations.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ProxyType {
  PROXY_TYPE_UNSPECIFIED = 0;
  PROXY_TYPE_FORWARD = 1;
  PROXY_TYPE_REVERSE = 2;
  PROXY_TYPE_TRANSPARENT = 3;
}
```

---

### quality_score.proto {#quality_score}

**Path**: `gcommon/v1/common/quality_score.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `QualityScore`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/quality_score.proto
// version: 1.0.1
// guid: 3d37a954-484a-4beb-acc4-7ec2fd05bf7d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Overall media quality rating.
enum QualityScore {
  QUALITY_SCORE_UNSPECIFIED = 0;
  QUALITY_SCORE_LOW = 1;
  QUALITY_SCORE_MEDIUM = 2;
  QUALITY_SCORE_HIGH = 3;
  QUALITY_SCORE_EXCELLENT = 4;
}
```

---

### query_operation.proto {#query_operation}

**Path**: `gcommon/v1/common/query_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 61

**Enums** (1): `QueryOperation`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/query_operation.proto
// version: 1.0.1
// guid: dcbbcb0c-451b-40d4-a928-ebe7659c8e66
// file: proto/gcommon/v1/metrics/v1/query_operation.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * QueryOperation defines the types of operations that can be performed on metrics queries.
 * Used for aggregating, filtering, and transforming metric data.
 */
enum QueryOperation {
  // Unspecified operation (default)
  QUERY_OPERATION_UNSPECIFIED = 0;

  // Select/filter metrics by criteria
  QUERY_OPERATION_SELECT = 1;

  // Group metrics by labels
  QUERY_OPERATION_GROUP_BY = 2;

  // Sum values across time or series
  QUERY_OPERATION_SUM = 3;

  // Average values across time or series
  QUERY_OPERATION_AVG = 4;

  // Find minimum value
  QUERY_OPERATION_MIN = 5;

  // Find maximum value
  QUERY_OPERATION_MAX = 6;

  // Count number of samples
  QUERY_OPERATION_COUNT = 7;

  // Calculate rate of change
  QUERY_OPERATION_RATE = 8;

  // Calculate increase over time
  QUERY_OPERATION_INCREASE = 9;

  // Sort results
  QUERY_OPERATION_SORT = 10;

  // Limit number of results
  QUERY_OPERATION_LIMIT = 11;

  // Join multiple metric series
  QUERY_OPERATION_JOIN = 12;
}
```

---

### rate_limit_strategy.proto {#rate_limit_strategy}

**Path**: `gcommon/v1/common/rate_limit_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `RateLimitStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/rate_limit_strategy.proto
// version: 1.0.1
// guid: dcc25ed5-f313-4ae4-8be6-bfbc050afb57

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// RateLimitStrategy enumeration defines available algorithms for rate limiting.
enum RateLimitStrategy {
  RATE_LIMIT_STRATEGY_UNSPECIFIED = 0;
  RATE_LIMIT_STRATEGY_TOKEN_BUCKET = 1;
  RATE_LIMIT_STRATEGY_FIXED_WINDOW = 2;
  RATE_LIMIT_STRATEGY_SLIDING_WINDOW = 3;
  RATE_LIMIT_STRATEGY_LEAKY_BUCKET = 4;
}
```

---

### read_level.proto {#read_level}

**Path**: `gcommon/v1/common/read_level.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ReadLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/read_level.proto
// version: 1.0.1
// guid: 955b2f22-8c91-4d05-98f4-0348ba5bf327

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ReadLevel {
  READ_LEVEL_UNSPECIFIED = 0;
  READ_LEVEL_EVENTUAL = 1; // Eventually consistent reads
  READ_LEVEL_STRONG = 2; // Strongly consistent reads
  READ_LEVEL_BOUNDED_STALENESS = 3; // Bounded staleness reads
  READ_LEVEL_SESSION = 4; // Session consistency
}
```

---

### rebalance_strategy.proto {#rebalance_strategy}

**Path**: `gcommon/v1/common/rebalance_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `RebalanceStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/rebalance_strategy.proto
// version: 1.0.1
// guid: def27fd7-f689-4591-b5ed-452ee9ca34ea

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RebalanceStrategy {
  REBALANCE_STRATEGY_UNSPECIFIED = 0;
  REBALANCE_STRATEGY_EAGER = 1; // Stop all consumers, then reassign
  REBALANCE_STRATEGY_COOPERATIVE = 2; // Incremental cooperative rebalancing
  REBALANCE_STRATEGY_STATIC = 3; // Static assignment (no rebalancing)
}
```

---

### reference_type.proto {#reference_type}

**Path**: `gcommon/v1/common/reference_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ReferenceType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/reference_type.proto
// version: 1.0.1
// guid: f7734726-4137-4441-b14d-c0c5479a50bd

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ReferenceType {
  REFERENCE_TYPE_UNSPECIFIED = 0;
  REFERENCE_TYPE_TEMPLATE = 1;
  REFERENCE_TYPE_POINTER = 2;
  REFERENCE_TYPE_ALIAS = 3;
  REFERENCE_TYPE_COMPUTED = 4;
  REFERENCE_TYPE_DERIVED = 5;
}
```

---

### registration_action.proto {#registration_action}

**Path**: `gcommon/v1/common/registration_action.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `RegistrationAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/registration_action.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RegistrationAction indicates what action was taken during registration.
 */
enum RegistrationAction {
  REGISTRATION_ACTION_UNSPECIFIED = 0;
  REGISTRATION_ACTION_CREATED = 1;
  REGISTRATION_ACTION_UPDATED = 2;
  REGISTRATION_ACTION_REPLACED = 3;
  REGISTRATION_ACTION_NO_CHANGE = 4;
}
```

---

### replication_level.proto {#replication_level}

**Path**: `gcommon/v1/common/replication_level.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `ReplicationLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/replication_level.proto
// version: 1.0.1
// guid: 3cf5a48e-2f5f-48ed-a2a9-6322f6010c4c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ReplicationLevel {
  REPLICATION_LEVEL_UNSPECIFIED = 0;
  REPLICATION_LEVEL_ONE = 1; // At least one replica
  REPLICATION_LEVEL_QUORUM = 2; // Majority of replicas
  REPLICATION_LEVEL_ALL = 3; // All replicas
}
```

---

### replication_mode.proto {#replication_mode}

**Path**: `gcommon/v1/common/replication_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `ReplicationMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/replication_mode.proto
// file: proto/gcommon/v1/queue/replication_mode.proto
// version: 1.0.1
// guid: 6d7e8f9a-0b1c-2d3e-4f5a-6b7c8d9e0f1a
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Replication mode for queue data across multiple nodes.
 */
enum ReplicationMode {
  // Default unspecified replication mode
  REPLICATION_MODE_UNSPECIFIED = 0;

  // No replication - single node only
  REPLICATION_MODE_NONE = 1;

  // Synchronous replication - wait for all replicas
  REPLICATION_MODE_SYNC = 2;

  // Asynchronous replication - don't wait for replicas
  REPLICATION_MODE_ASYNC = 3;

  // Quorum-based replication - wait for majority
  REPLICATION_MODE_QUORUM = 4;

  // Leader-follower replication
  REPLICATION_MODE_LEADER_FOLLOWER = 5;

  // Master-slave replication (legacy term)
  REPLICATION_MODE_MASTER_SLAVE = 6;
}
```

---

### resolution.proto {#resolution}

**Path**: `gcommon/v1/common/resolution.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `Resolution`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/resolution.proto
// version: 1.0.1
// guid: 2901b257-89ea-43db-8650-a3b6b48acfdb

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Media resolution enumeration.
enum Resolution {
  RESOLUTION_UNSPECIFIED = 0;
  RESOLUTION_480P = 1;
  RESOLUTION_720P = 2;
  RESOLUTION_1080P = 3;
  RESOLUTION_4K = 4;
}
```

---

### resolution_strategy.proto {#resolution_strategy}

**Path**: `gcommon/v1/common/resolution_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ResolutionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resolution_strategy.proto
// version: 1.0.1
// guid: 2c802dfc-d9ae-4cc2-81ea-ebbb90394cff

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ResolutionStrategy {
  RESOLUTION_STRATEGY_UNSPECIFIED = 0;
  RESOLUTION_STRATEGY_LAST_WRITER_WINS = 1; // Last writer wins
  RESOLUTION_STRATEGY_FIRST_WRITER_WINS = 2; // First writer wins
  RESOLUTION_STRATEGY_MERGE = 3; // Automatic merge
  RESOLUTION_STRATEGY_CUSTOM = 4; // Custom resolution function
  RESOLUTION_STRATEGY_MULTI_VALUE = 5; // Keep all conflicting values
}
```

---

### resource_status.proto {#resource_status}

**Path**: `gcommon/v1/common/resource_status.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Enums** (1): `ResourceStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/resource_status.proto
// version: 1.0.2
// guid: 789abc12-3456-7890-abcd-ef1234567890

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common resource status enumeration used across all GCommon modules.
 * Provides consistent status reporting for various resources like configurations,
 * cache entries, database connections, etc.
 */
enum ResourceStatus {
  // Default value indicating resource status was not specified
  RESOURCE_STATUS_UNSPECIFIED = 0;

  // Resource is active and available for use
  RESOURCE_STATUS_ACTIVE = 1;

  // Resource is inactive but can be activated
  RESOURCE_STATUS_INACTIVE = 2;

  // Resource is pending activation or processing
  RESOURCE_STATUS_PENDING = 3;

  // Resource has been marked for deletion or is deleted
  RESOURCE_STATUS_DELETED = 4;

  // Resource is in an error state and requires attention
  RESOURCE_STATUS_ERROR = 5;
}
```

---

### response_compression.proto {#response_compression}

**Path**: `gcommon/v1/common/response_compression.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `ResponseCompression`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/response_compression.proto
// version: 1.0.1
// guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ResponseCompression defines compression options for responses.
 * Specifies compression algorithms for metric response data.
 */
enum ResponseCompression {
  // Unspecified compression
  RESPONSE_COMPRESSION_UNSPECIFIED = 0;

  // No compression
  RESPONSE_COMPRESSION_NONE = 1;

  // GZIP compression
  RESPONSE_COMPRESSION_GZIP = 2;

  // Snappy compression
  RESPONSE_COMPRESSION_SNAPPY = 3;
}
```

---

### restriction_type.proto {#restriction_type}

**Path**: `gcommon/v1/common/restriction_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `RestrictionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/restriction_type.proto
// version: 1.0.1
// guid: 7444b7aa-6693-418e-ae6b-aa854f8c5400

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RestrictionType {
  RESTRICTION_TYPE_UNSPECIFIED = 0;
  RESTRICTION_TYPE_IP_ADDRESS = 1;
  RESTRICTION_TYPE_TIME_RANGE = 2;
  RESTRICTION_TYPE_LOCATION = 3;
  RESTRICTION_TYPE_USER_AGENT = 4;
  RESTRICTION_TYPE_CUSTOM = 5;
}
```

---

### retention_policy.proto {#retention_policy}

**Path**: `gcommon/v1/common/retention_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 48

**Enums** (1): `MetricsRetentionPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_policy.proto
// version: 1.0.1
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// RetentionPolicy represents different retention policies for metrics data
enum MetricsRetentionPolicy {
  // Unspecified retention policy
  RETENTION_POLICY_UNSPECIFIED = 0;

  // Short-term retention (minutes to hours)
  RETENTION_POLICY_SHORT_TERM = 1;

  // Medium-term retention (days to weeks)
  RETENTION_POLICY_MEDIUM_TERM = 2;

  // Long-term retention (months to years)
  RETENTION_POLICY_LONG_TERM = 3;

  // Archive retention (permanent storage)
  RETENTION_POLICY_ARCHIVE = 4;

  // Custom retention policy
  RETENTION_POLICY_CUSTOM = 5;

  // High-frequency data retention (seconds to minutes)
  RETENTION_POLICY_HIGH_FREQUENCY = 6;

  // Low-frequency data retention (hours to days)
  RETENTION_POLICY_LOW_FREQUENCY = 7;

  // Compliance retention (regulatory requirements)
  RETENTION_POLICY_COMPLIANCE = 8;

  // Real-time retention (immediate processing, no storage)
  RETENTION_POLICY_REAL_TIME = 9;

  // Aggregate retention (summary data only)
  RETENTION_POLICY_AGGREGATE = 10;
}
```

---

### retention_unit.proto {#retention_unit}

**Path**: `gcommon/v1/common/retention_unit.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Enums** (1): `RetentionUnit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_unit.proto
// version: 1.0.1
// guid: a5ffd419-c490-4f14-8c87-dd43c36de9ec
// file: proto/gcommon/v1/metrics/v1/retention_unit.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RetentionUnit defines the units for data retention policies.
 * Used to specify how long metric data should be kept in storage.
 */
enum RetentionUnit {
  // Unspecified retention unit (default)
  RETENTION_UNIT_UNSPECIFIED = 0;

  // Minutes
  RETENTION_UNIT_MINUTES = 1;

  // Hours
  RETENTION_UNIT_HOURS = 2;

  // Days
  RETENTION_UNIT_DAYS = 3;

  // Weeks
  RETENTION_UNIT_WEEKS = 4;

  // Months
  RETENTION_UNIT_MONTHS = 5;

  // Years
  RETENTION_UNIT_YEARS = 6;

  // Forever (no expiration)
  RETENTION_UNIT_FOREVER = 7;

  // Custom duration (specify in seconds)
  RETENTION_UNIT_CUSTOM = 8;
}
```

---

### retry_delay_strategy.proto {#retry_delay_strategy}

**Path**: `gcommon/v1/common/retry_delay_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `RetryDelayStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_delay_strategy.proto
// version: 1.0.1
// guid: e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Strategy for calculating retry delays.
 * Specifies how delays between retry attempts are computed.
 */
enum RetryDelayStrategy {
  // Default unspecified strategy
  RETRY_DELAY_STRATEGY_UNSPECIFIED = 0;

  // Fixed delay between retries
  RETRY_DELAY_STRATEGY_FIXED = 1;

  // Linear backoff (delay increases linearly)
  RETRY_DELAY_STRATEGY_LINEAR = 2;

  // Exponential backoff (delay doubles each time)
  RETRY_DELAY_STRATEGY_EXPONENTIAL = 3;

  // Custom backoff strategy
  RETRY_DELAY_STRATEGY_CUSTOM = 4;
}
```

---

### role_scope.proto {#role_scope}

**Path**: `gcommon/v1/common/role_scope.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `RoleScope`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role_scope.proto
// version: 1.0.1
// guid: d731d279-8c61-4854-ae41-17da08e62494
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Role scope enumeration defining the level at which roles apply.
 * Used for hierarchical role-based access control.
 */
enum RoleScope {
  // Unspecified role scope
  ROLE_SCOPE_UNSPECIFIED = 0;

  // Global system-wide role
  ROLE_SCOPE_GLOBAL = 1;

  // Organization-level role
  ROLE_SCOPE_ORGANIZATION = 2;

  // Project-level role
  ROLE_SCOPE_PROJECT = 3;

  // Team-level role
  ROLE_SCOPE_TEAM = 4;

  // Resource-level role
  ROLE_SCOPE_RESOURCE = 5;
}
```

---

### rotation_frequency.proto {#rotation_frequency}

**Path**: `gcommon/v1/common/rotation_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `RotationFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rotation_frequency.proto
// version: 1.0.1
// guid: 4bb020d8-2763-4ac1-96fc-6210bade7050

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RotationFrequency {
  ROTATION_FREQUENCY_UNSPECIFIED = 0;
  ROTATION_FREQUENCY_MANUAL = 1;
  ROTATION_FREQUENCY_DAILY = 2;
  ROTATION_FREQUENCY_WEEKLY = 3;
  ROTATION_FREQUENCY_MONTHLY = 4;
  ROTATION_FREQUENCY_QUARTERLY = 5;
  ROTATION_FREQUENCY_YEARLY = 6;
  ROTATION_FREQUENCY_ON_EXPIRY = 7;
}
```

---

### route_type.proto {#route_type}

**Path**: `gcommon/v1/common/route_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `RouteType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/route_type.proto
// version: 1.0.1
// guid: a655dd19-273c-4cb4-a5ea-71ce983e16cd
//
// RouteType distinguishes different route behaviors.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RouteType {
  ROUTE_TYPE_UNSPECIFIED = 0;
  ROUTE_TYPE_STATIC_FILE = 1;
  ROUTE_TYPE_API = 2;
  ROUTE_TYPE_REDIRECT = 3;
}
```

---

### routing_pattern.proto {#routing_pattern}

**Path**: `gcommon/v1/common/routing_pattern.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `RoutingPattern`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_pattern.proto
// version: 1.0.1
// guid: f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Routing pattern types for key matching.
 * Specifies how routing keys are matched against patterns.
 */
enum RoutingPattern {
  // Exact string match
  ROUTING_PATTERN_UNSPECIFIED = 0;

  // Wildcard pattern (* and ?)
  ROUTING_PATTERN_WILDCARD = 1;

  // Regular expression pattern
  ROUTING_PATTERN_REGEX = 2;

  // Topic-style pattern (dot separated, # and * wildcards)
  ROUTING_PATTERN_TOPIC = 3;

  // Prefix match
  ROUTING_PATTERN_PREFIX = 4;

  // Suffix match
  ROUTING_PATTERN_SUFFIX = 5;
}
```

---

### routing_strategy.proto {#routing_strategy}

**Path**: `gcommon/v1/common/routing_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `RoutingStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_strategy.proto
// version: 1.0.1
// guid: c0da3188-9710-4555-bbda-9632f6b3f29b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Routing strategies.
 */
enum RoutingStrategy {
  // Default unspecified strategy
  ROUTING_STRATEGY_UNSPECIFIED = 0;

  // Direct routing based on destination name
  ROUTING_STRATEGY_DIRECT = 1;

  // Topic-based routing using routing key
  ROUTING_STRATEGY_TOPIC = 2;

  // Fanout routing to all bound queues
  ROUTING_STRATEGY_FANOUT = 3;

  // Header-based routing using message headers
  ROUTING_STRATEGY_HEADER = 4;

  // Content-based routing using message content
  ROUTING_STRATEGY_CONTENT = 5;

  // Hash-based routing for load distribution
  ROUTING_STRATEGY_HASH = 6;
}
```

---

### same_site_policy.proto {#same_site_policy}

**Path**: `gcommon/v1/common/same_site_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `SameSitePolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/same_site_policy.proto
// version: 1.0.1
// guid: a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SameSite cookie policy options.
 * Controls when cookies are sent with cross-site requests.
 */
enum SameSitePolicy {
  // Default SameSite policy
  SAME_SITE_POLICY_UNSPECIFIED = 0;

  // No SameSite restriction
  SAME_SITE_POLICY_NONE = 1;

  // Lax SameSite policy
  SAME_SITE_POLICY_LAX = 2;

  // Strict SameSite policy
  SAME_SITE_POLICY_STRICT = 3;
}
```

---

### sample_rate.proto {#sample_rate}

**Path**: `gcommon/v1/common/sample_rate.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Enums** (1): `SampleRate`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/sample_rate.proto
// version: 1.0.1
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// SampleRate represents different sampling rates for metrics collection
enum SampleRate {
  // Unspecified sample rate
  SAMPLE_RATE_UNSPECIFIED = 0;

  // Collect every sample (100%)
  SAMPLE_RATE_FULL = 1;

  // Sample at 50% rate
  SAMPLE_RATE_HALF = 2;

  // Sample at 25% rate
  SAMPLE_RATE_QUARTER = 3;

  // Sample at 10% rate
  SAMPLE_RATE_TENTH = 4;

  // Sample at 5% rate
  SAMPLE_RATE_TWENTIETH = 5;

  // Sample at 1% rate
  SAMPLE_RATE_HUNDREDTH = 6;

  // Sample at 0.1% rate
  SAMPLE_RATE_THOUSANDTH = 7;

  // Adaptive sampling (dynamic rate)
  SAMPLE_RATE_ADAPTIVE = 8;

  // Custom sampling rate
  SAMPLE_RATE_CUSTOM = 9;
}
```

---

### schema_compatibility_mode.proto {#schema_compatibility_mode}

**Path**: `gcommon/v1/common/schema_compatibility_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Enums** (1): `SchemaCompatibilityMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_compatibility_mode.proto
// version: 1.0.1
// guid: 6c24f62f-1d37-4098-b5d4-a49e4a58d05e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Schema compatibility modes.
 */
enum SchemaCompatibilityMode {
  // Default unspecified mode
  SCHEMA_COMPATIBILITY_MODE_UNSPECIFIED = 0;

  // Strict compatibility checking
  SCHEMA_COMPATIBILITY_MODE_STRICT = 1;

  // Lenient compatibility checking
  SCHEMA_COMPATIBILITY_MODE_LENIENT = 2;

  // No compatibility checking
  SCHEMA_COMPATIBILITY_MODE_NONE = 3;
}
```

---

### schema_evolution_strategy.proto {#schema_evolution_strategy}

**Path**: `gcommon/v1/common/schema_evolution_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `SchemaEvolutionStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_evolution_strategy.proto
// version: 1.0.1
// guid: ef5f0572-3b2c-44c1-8e1c-247b8fad9c9c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Schema evolution strategies.
 */
enum SchemaEvolutionStrategy {
  // Default unspecified strategy
  SCHEMA_EVOLUTION_STRATEGY_UNSPECIFIED = 0;

  // No evolution allowed
  SCHEMA_EVOLUTION_STRATEGY_NONE = 1;

  // Forward compatibility (new schema can read old data)
  SCHEMA_EVOLUTION_STRATEGY_FORWARD = 2;

  // Backward compatibility (old schema can read new data)
  SCHEMA_EVOLUTION_STRATEGY_BACKWARD = 3;

  // Full compatibility (bidirectional)
  SCHEMA_EVOLUTION_STRATEGY_FULL = 4;

  // No compatibility checks
  SCHEMA_EVOLUTION_STRATEGY_NONE_CHECK = 5;
}
```

---

### schema_format.proto {#schema_format}

**Path**: `gcommon/v1/common/schema_format.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `SchemaFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_format.proto
// version: 1.0.1
// guid: 8dbf53aa-e92d-4de4-84a8-ec3fb37ce521

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Schema format types.
 */
enum SchemaFormat {
  // Default unspecified format
  SCHEMA_FORMAT_UNSPECIFIED = 0;

  // JSON Schema format
  SCHEMA_FORMAT_JSON_SCHEMA = 1;

  // Apache Avro schema
  SCHEMA_FORMAT_AVRO = 2;

  // Protocol Buffers schema
  SCHEMA_FORMAT_PROTOBUF = 3;

  // XML Schema (XSD)
  SCHEMA_FORMAT_XML_SCHEMA = 4;

  // Custom schema format
  SCHEMA_FORMAT_CUSTOM = 5;
}
```

---

### scope_type.proto {#scope_type}

**Path**: `gcommon/v1/common/scope_type.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `ScopeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/scope_type.proto
// version: 1.0.1
// guid: f8bce9e5-500a-40e6-aca9-4ce5c58d2d04
// file: proto/gcommon/v1/common/scope_type.proto
//
// Enum definitions for auth module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ScopeType defines the scope at which a permission can be applied
 */
enum ScopeType {
  // Unspecified scope type
  SCOPE_TYPE_UNSPECIFIED = 0;

  // Global scope - applies across the entire system
  SCOPE_TYPE_GLOBAL = 1;

  // Organization scope - applies within a specific organization
  SCOPE_TYPE_ORGANIZATION = 2;

  // Project scope - applies within a specific project
  SCOPE_TYPE_PROJECT = 3;

  // Resource scope - applies to a specific resource
  SCOPE_TYPE_RESOURCE = 4;
}
```

---

### scrape_status.proto {#scrape_status}

**Path**: `gcommon/v1/common/scrape_status.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Enums** (1): `ScrapeStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/types/scrape_status.proto
// version: 1.0.1
// guid: 8c8f682b-16a6-490f-84ce-c96e566d5fba
// file: proto/gcommon/v1/metrics/scrape_status.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ScrapeStatus defines the status of metric scraping operations.
 * Used to track the health and success of metric collection from targets.
 */
enum ScrapeStatus {
  // Unspecified scrape status (default)
  SCRAPE_STATUS_UNSPECIFIED = 0;

  // Scrape completed successfully
  SCRAPE_STATUS_SUCCESS = 1;

  // Scrape failed due to network/connection issues
  SCRAPE_STATUS_NETWORK_ERROR = 2;

  // Scrape failed due to authentication/authorization issues
  SCRAPE_STATUS_AUTH_ERROR = 3;

  // Scrape failed due to timeout
  SCRAPE_STATUS_TIMEOUT = 4;

  // Scrape failed due to invalid/malformed response
  SCRAPE_STATUS_PARSE_ERROR = 5;

  // Target is unreachable/down
  SCRAPE_STATUS_TARGET_DOWN = 6;

  // Target returned HTTP error status
  SCRAPE_STATUS_HTTP_ERROR = 7;

  // Scrape was cancelled/aborted
  SCRAPE_STATUS_CANCELLED = 8;

  // Rate limited by target
  SCRAPE_STATUS_RATE_LIMITED = 9;

  // Target configuration is invalid
  SCRAPE_STATUS_CONFIG_ERROR = 10;

  // Scrape is currently in progress
  SCRAPE_STATUS_IN_PROGRESS = 11;
}
```

---

### secret_audit_level.proto {#secret_audit_level}

**Path**: `gcommon/v1/common/secret_audit_level.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `SecretAuditLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_audit_level.proto
// version: 1.0.1
// guid: bc307b1b-aa5d-4b26-8724-6f1e537132c5

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretAuditLevel {
  SECRET_AUDIT_LEVEL_UNSPECIFIED = 0;
  SECRET_AUDIT_LEVEL_NONE = 1;
  SECRET_AUDIT_LEVEL_MINIMAL = 2;
  SECRET_AUDIT_LEVEL_STANDARD = 3;
  SECRET_AUDIT_LEVEL_DETAILED = 4;
  SECRET_AUDIT_LEVEL_VERBOSE = 5;
}
```

---

### secret_backup_frequency.proto {#secret_backup_frequency}

**Path**: `gcommon/v1/common/secret_backup_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `SecretBackupFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_backup_frequency.proto
// version: 1.0.1
// guid: d2ec4ba6-932e-4349-89f4-aa4af899c73f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretBackupFrequency {
  SECRET_BACKUP_FREQUENCY_UNSPECIFIED = 0;
  SECRET_BACKUP_FREQUENCY_MANUAL = 1;
  SECRET_BACKUP_FREQUENCY_HOURLY = 2;
  SECRET_BACKUP_FREQUENCY_DAILY = 3;
  SECRET_BACKUP_FREQUENCY_WEEKLY = 4;
  SECRET_BACKUP_FREQUENCY_MONTHLY = 5;
  SECRET_BACKUP_FREQUENCY_ON_CHANGE = 6;
}
```

---

### secret_status.proto {#secret_status}

**Path**: `gcommon/v1/common/secret_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `SecretStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_status.proto
// version: 1.0.1
// guid: 7fb6a7a0-ecc1-4dc0-b2a0-49c3e3fe88b9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretStatus {
  SECRET_STATUS_UNSPECIFIED = 0;
  SECRET_STATUS_ACTIVE = 1;
  SECRET_STATUS_INACTIVE = 2;
  SECRET_STATUS_EXPIRED = 3;
  SECRET_STATUS_ROTATED = 4;
  SECRET_STATUS_COMPROMISED = 5;
  SECRET_STATUS_DELETED = 6;
  SECRET_STATUS_ERROR = 7;
}
```

---

### secret_type.proto {#secret_type}

**Path**: `gcommon/v1/common/secret_type.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `SecretType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_type.proto
// version: 1.0.1
// guid: efadf8e9-2dc3-4ccc-8c9a-3a7f0a1c0895

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretType {
  SECRET_TYPE_UNSPECIFIED = 0;
  SECRET_TYPE_PASSWORD = 1;
  SECRET_TYPE_API_KEY = 2;
  SECRET_TYPE_TOKEN = 3;
  SECRET_TYPE_CERTIFICATE = 4;
  SECRET_TYPE_PRIVATE_KEY = 5;
  SECRET_TYPE_PUBLIC_KEY = 6;
  SECRET_TYPE_OAUTH_CLIENT_SECRET = 7;
  SECRET_TYPE_DATABASE_PASSWORD = 8;
  SECRET_TYPE_CONNECTION_STRING = 9;
  SECRET_TYPE_ENCRYPTION_KEY = 10;
  SECRET_TYPE_SIGNING_KEY = 11;
  SECRET_TYPE_SSH_KEY = 12;
  SECRET_TYPE_TLS_CERTIFICATE = 13;
  SECRET_TYPE_JWT_SECRET = 14;
  SECRET_TYPE_WEBHOOK_SECRET = 15;
  SECRET_TYPE_CUSTOM = 16;
}
```

---

### secret_validation_result_type.proto {#secret_validation_result_type}

**Path**: `gcommon/v1/common/secret_validation_result_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `SecretValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_validation_result_type.proto
// version: 1.0.1
// guid: b6bb65eb-d0bd-40b2-ad57-22253970cb05

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretValidationResultType {
  SECRET_VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;
  SECRET_VALIDATION_RESULT_TYPE_PASS = 1;
  SECRET_VALIDATION_RESULT_TYPE_FAIL = 2;
  SECRET_VALIDATION_RESULT_TYPE_WARNING = 3;
  SECRET_VALIDATION_RESULT_TYPE_SKIP = 4;
}
```

---

### secret_validation_severity.proto {#secret_validation_severity}

**Path**: `gcommon/v1/common/secret_validation_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `SecretValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/secret_validation_severity.proto
// version: 1.0.1
// guid: 8dc44dbd-dedb-4dfd-b5f9-ad2256d6a6c6

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SecretValidationSeverity {
  SECRET_VALIDATION_SEVERITY_UNSPECIFIED = 0;
  SECRET_VALIDATION_SEVERITY_INFO = 1;
  SECRET_VALIDATION_SEVERITY_WARNING = 2;
  SECRET_VALIDATION_SEVERITY_ERROR = 3;
  SECRET_VALIDATION_SEVERITY_CRITICAL = 4;
}
```

---

### serialization_format.proto {#serialization_format}

**Path**: `gcommon/v1/common/serialization_format.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Enums** (1): `SerializationFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/serialization_format.proto
// file: proto/gcommon/v1/queue/serialization_format.proto
// version: 1.0.1
// guid: 7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Supported message serialization formats for queue messages.
 */
enum SerializationFormat {
  // Default unspecified format
  SERIALIZATION_FORMAT_UNSPECIFIED = 0;

  // Protocol Buffers binary format
  SERIALIZATION_FORMAT_PROTOBUF = 1;

  // JSON text format
  SERIALIZATION_FORMAT_JSON = 2;

  // MessagePack binary format
  SERIALIZATION_FORMAT_MSGPACK = 3;

  // Apache Avro binary format
  SERIALIZATION_FORMAT_AVRO = 4;

  // Raw binary data (no specific format)
  SERIALIZATION_FORMAT_BINARY = 5;

  // Plain text format
  SERIALIZATION_FORMAT_TEXT = 6;

  // XML format
  SERIALIZATION_FORMAT_XML = 7;
}
```

---

### server_state.proto {#server_state}

**Path**: `gcommon/v1/common/server_state.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ServerState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_state.proto
// version: 1.0.1
// guid: edc8f45d-5db0-4b28-b04a-c6eedc98b19b
//
// ServerState represents lifecycle states of the server.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ServerState {
  SERVER_STATE_UNSPECIFIED = 0;
  SERVER_STATE_STARTING = 1;
  SERVER_STATE_RUNNING = 2;
  SERVER_STATE_STOPPING = 3;
  SERVER_STATE_STOPPED = 4;
}
```

---

### server_status.proto {#server_status}

**Path**: `gcommon/v1/common/server_status.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `ServerStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/server_status.proto
// version: 1.0.2
// guid: 1846bf32-3652-4e52-a6fc-333db4886d5c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ServerStatus enumeration describing server lifecycle states.
enum ServerStatus {
  SERVER_STATUS_UNSPECIFIED = 0;
  SERVER_STATUS_CREATED = 1;
  SERVER_STATUS_STARTING = 2;
  SERVER_STATUS_RUNNING = 3;
  SERVER_STATUS_STOPPING = 4;
  SERVER_STATUS_STOPPED = 5;
  SERVER_STATUS_ERROR = 6;
}
```

---

### serving_status.proto {#serving_status}

**Path**: `gcommon/v1/common/serving_status.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Enums** (1): `ServingStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/serving_status.proto
// version: 1.0.1
// guid: 61568d14-42ce-4cc7-b55e-a2fedc98db5f
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ServingStatus indicates the current serving status of a service
 */
enum ServingStatus {
  // Unknown status
  SERVING_STATUS_UNSPECIFIED = 0;
  // Service is serving
  SERVING_STATUS_SERVING = 1;
  // Service is not serving
  SERVING_STATUS_NOT_SERVING = 2;
  // Service is serving but degraded
  SERVING_STATUS_SERVING_DEGRADED = 3;
}
```

---

### session_state.proto {#session_state}

**Path**: `gcommon/v1/common/session_state.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `SessionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_state.proto
// version: 1.0.1
// guid: 1a1dfd90-4426-4329-a9ab-e7c705fb4f74

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum SessionState {
  COMMON_SESSION_STATE_UNSPECIFIED = 0;
  COMMON_SESSION_STATE_ACTIVE = 1;
  COMMON_SESSION_STATE_EXPIRED = 2;
}
```

---

### session_status.proto {#session_status}

**Path**: `gcommon/v1/common/session_status.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `SessionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_status.proto
// version: 1.0.1
// guid: df65ccac-c72e-48cf-ba09-e50b76276d9e
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Session status enumeration defining the current state of a user session.
 * Used for session lifecycle management and security validation.
 */
enum SessionStatus {
  // Default value indicating no status was specified
  SESSION_STATUS_UNSPECIFIED = 0;

  // Session is active and valid for authentication
  SESSION_STATUS_ACTIVE = 1;

  // Session has expired based on time-based expiration
  SESSION_STATUS_EXPIRED = 2;

  // Session was explicitly terminated (logout)
  SESSION_STATUS_TERMINATED = 3;

  // Session is invalid due to security concerns or corruption
  SESSION_STATUS_INVALID = 4;
}
```

---

### sort_direction.proto {#sort_direction}

**Path**: `gcommon/v1/common/sort_direction.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Enums** (1): `SortDirection`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/sort_direction.proto
// version: 1.0.1
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Sort direction enumeration.
 * Defines ascending or descending order for sorting operations.
 */
enum SortDirection {
  // Unspecified sort direction
  SORT_DIRECTION_UNSPECIFIED = 0;

  // Ascending order (A-Z, 0-9, oldest-newest)
  SORT_DIRECTION_ASC = 1;

  // Descending order (Z-A, 9-0, newest-oldest)
  SORT_DIRECTION_DESC = 2;
}
```

---

### sort_field.proto {#sort_field}

**Path**: `gcommon/v1/common/sort_field.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `SortField`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/sort_field.proto
// version: 1.0.1
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SortField defines fields that can be used for sorting providers.
 * Specifies available fields for provider list sorting.
 */
enum SortField {
  // Unspecified sort field
  SORT_FIELD_UNSPECIFIED = 0;

  // Sort by provider name
  SORT_FIELD_NAME = 1;

  // Sort by provider type
  SORT_FIELD_TYPE = 2;

  // Sort by creation timestamp
  SORT_FIELD_CREATED_AT = 3;

  // Sort by provider state
  SORT_FIELD_STATE = 4;

  // Sort by health status
  SORT_FIELD_HEALTH = 5;
}
```

---

### ssl_protocol.proto {#ssl_protocol}

**Path**: `gcommon/v1/common/ssl_protocol.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `SSLProtocol`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/ssl_protocol.proto
// version: 1.0.1
// guid: 2f6af5d4-4f52-42cd-9ae8-9c6506e0da5e
//
// SSLProtocol lists supported TLS protocol versions.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SSLProtocol {
  SSL_PROTOCOL_UNSPECIFIED = 0;
  SSL_PROTOCOL_TLS1_0 = 1;
  SSL_PROTOCOL_TLS1_1 = 2;
  SSL_PROTOCOL_TLS1_2 = 3;
  SSL_PROTOCOL_TLS1_3 = 4;
}
```

---

### statistic_grouping.proto {#statistic_grouping}

**Path**: `gcommon/v1/common/statistic_grouping.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `StatisticGrouping`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/statistic_grouping.proto
// version: 1.0.1
// guid: a8a72b1a-cc3a-46d1-a1ab-87af3535faac

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum StatisticGrouping {
  STATISTIC_GROUPING_UNSPECIFIED = 0;
  STATISTIC_GROUPING_NONE = 1; // No grouping, flat statistics
  STATISTIC_GROUPING_BY_QUEUE = 2; // Group by queue name
  STATISTIC_GROUPING_BY_CONSUMER = 3; // Group by consumer
  STATISTIC_GROUPING_BY_TIME_PERIOD = 4; // Group by time periods
  STATISTIC_GROUPING_BY_MESSAGE_TYPE = 5; // Group by message type
}
```

---

### statistic_type.proto {#statistic_type}

**Path**: `gcommon/v1/common/statistic_type.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `StatisticType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/statistic_type.proto
// version: 1.0.1
// guid: cb4f227d-f3e9-4698-aa3e-776544976e01

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum StatisticType {
  STATISTIC_TYPE_UNSPECIFIED = 0;
  STATISTIC_TYPE_MESSAGE_COUNT = 1;
  STATISTIC_TYPE_THROUGHPUT = 2;
  STATISTIC_TYPE_LATENCY = 3;
  STATISTIC_TYPE_ERROR_RATE = 4;
  STATISTIC_TYPE_QUEUE_DEPTH = 5;
  STATISTIC_TYPE_PROCESSING_TIME = 6;
  STATISTIC_TYPE_CONSUMER_COUNT = 7;
  STATISTIC_TYPE_MESSAGE_SIZE = 8;
  STATISTIC_TYPE_AGE_DISTRIBUTION = 9;
  STATISTIC_TYPE_SUCCESS_RATE = 10;
}
```

---

### stats_granularity.proto {#stats_granularity}

**Path**: `gcommon/v1/common/stats_granularity.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `StatsGranularity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stats_granularity.proto
// version: 1.0.1
// guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StatsGranularity represents the granularity for statistics.
 * Specifies the time interval granularity for statistical data collection and aggregation.
 */
enum StatsGranularity {
  // Default unspecified granularity
  STATS_GRANULARITY_UNSPECIFIED = 0;

  // Minute-level granularity
  STATS_GRANULARITY_MINUTE = 1;

  // Hour-level granularity
  STATS_GRANULARITY_HOUR = 2;

  // Day-level granularity
  STATS_GRANULARITY_DAY = 3;

  // Week-level granularity
  STATS_GRANULARITY_WEEK = 4;
}
```

---

### storage_backend.proto {#storage_backend}

**Path**: `gcommon/v1/common/storage_backend.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Enums** (1): `StorageBackend`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/storage_backend.proto
// version: 1.0.1
// guid: 5ee72796-5fec-4f25-8894-b75050c9f18e
// file: proto/gcommon/v1/metrics/v1/storage_backend.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StorageBackend defines the types of storage systems available for metrics.
 * Used to specify where metrics should be stored and retrieved from.
 */
enum StorageBackend {
  // Unspecified storage backend (default)
  STORAGE_BACKEND_UNSPECIFIED = 0;

  // In-memory storage (non-persistent, for testing/development)
  STORAGE_BACKEND_MEMORY = 1;

  // Prometheus time-series database
  STORAGE_BACKEND_PROMETHEUS = 2;

  // InfluxDB time-series database
  STORAGE_BACKEND_INFLUXDB = 3;

  // TimescaleDB (PostgreSQL extension for time-series)
  STORAGE_BACKEND_TIMESCALEDB = 4;

  // OpenTelemetry backend (various implementations)
  STORAGE_BACKEND_OPENTELEMETRY = 5;

  // Graphite time-series database
  STORAGE_BACKEND_GRAPHITE = 6;

  // ElasticSearch for metrics storage
  STORAGE_BACKEND_ELASTICSEARCH = 7;

  // CloudWatch (AWS managed metrics)
  STORAGE_BACKEND_CLOUDWATCH = 8;

  // Google Cloud Monitoring
  STORAGE_BACKEND_GCP_MONITORING = 9;

  // Azure Monitor
  STORAGE_BACKEND_AZURE_MONITOR = 10;

  // VictoriaMetrics time-series database
  STORAGE_BACKEND_VICTORIAMETRICS = 11;
}
```

---

### stream_compression.proto {#stream_compression}

**Path**: `gcommon/v1/common/stream_compression.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `StreamCompression`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_compression.proto
// version: 1.0.1
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StreamCompression defines compression options for streaming.
 * Specifies how metrics data should be compressed during streaming.
 */
enum StreamCompression {
  // Unspecified compression
  STREAM_COMPRESSION_UNSPECIFIED = 0;

  // No compression
  STREAM_COMPRESSION_NONE = 1;

  // GZIP compression
  STREAM_COMPRESSION_GZIP = 2;

  // Snappy compression
  STREAM_COMPRESSION_SNAPPY = 3;

  // LZ4 compression
  STREAM_COMPRESSION_LZ4 = 4;
}
```

---

### stream_qos.proto {#stream_qos}

**Path**: `gcommon/v1/common/stream_qos.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Enums** (1): `StreamQOS`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/stream_qos.proto
// version: 1.0.1
// guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * StreamQOS defines quality of service levels for streaming.
 * Specifies delivery guarantees for streaming metrics.
 */
enum StreamQOS {
  // Unspecified QOS level
  STREAM_QOS_UNSPECIFIED = 0;

  // Best effort delivery (fire and forget)
  STREAM_QOS_BEST_EFFORT = 1;

  // At least once delivery guarantee
  STREAM_QOS_AT_LEAST_ONCE = 2;

  // Exactly once delivery guarantee
  STREAM_QOS_EXACTLY_ONCE = 3;
}
```

---

### stream_restart_policy.proto {#stream_restart_policy}

**Path**: `gcommon/v1/common/stream_restart_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `StreamRestartPolicy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/stream_restart_policy.proto
// file: proto/gcommon/v1/queue/stream_restart_policy.proto
// version: 1.0.1
// guid: 6a5b4c3d-2e1f-0a9b-8c7d-6e5f4a3b2c1d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Stream restart behavior on failures.
 */
enum StreamRestartPolicy {
  // Default unspecified policy
  STREAM_RESTART_POLICY_UNSPECIFIED = 0;

  // Never restart streams automatically
  STREAM_RESTART_POLICY_NEVER = 1;

  // Restart immediately on failure
  STREAM_RESTART_POLICY_IMMEDIATE = 2;

  // Restart with exponential backoff
  STREAM_RESTART_POLICY_EXPONENTIAL_BACKOFF = 3;

  // Restart with fixed delay
  STREAM_RESTART_POLICY_FIXED_DELAY = 4;
}
```

---

### subject_type.proto {#subject_type}

**Path**: `gcommon/v1/common/subject_type.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `AuthSubjectType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subject_type.proto
// version: 1.0.1
// guid: d89bcd75-cade-444b-a4de-35078c41a269

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthSubjectType {
  SUBJECT_TYPE_UNSPECIFIED = 0;
  SUBJECT_TYPE_USER = 1;
  SUBJECT_TYPE_ROLE = 2;
}
```

---

### subscription_state.proto {#subscription_state}

**Path**: `gcommon/v1/common/subscription_state.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `SubscriptionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_state.proto
// version: 1.0.1
// guid: ddd7bd85-a329-4347-be1d-18983916cd3e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// SubscriptionState describes the lifecycle state of a subscription.
enum SubscriptionState {
  // Default state. Server decides behavior.
  SUBSCRIPTION_STATE_UNSPECIFIED = 0;
  // Actively receiving messages.
  SUBSCRIPTION_STATE_ACTIVE = 1;
  // Temporarily paused from delivering messages.
  SUBSCRIPTION_STATE_PAUSED = 2;
  // Permanently closed and cannot be resumed.
  SUBSCRIPTION_STATE_CLOSED = 3;
}
```

---

### subscription_status.proto {#subscription_status}

**Path**: `gcommon/v1/common/subscription_status.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `SubscriptionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_status.proto
// version: 1.0.1
// guid: 2b701f36-27a4-4a02-a1a8-d30ef84d277c
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Subscription status enumeration for streaming operations.
 * Provides consistent status tracking for event subscriptions, data streams,
 * and real-time updates across all GCommon modules.
 */
enum SubscriptionStatus {
  // Default value indicating no subscription status was specified
  SUBSCRIPTION_STATUS_UNSPECIFIED = 0;

  // Subscription is active and receiving events
  SUBSCRIPTION_STATUS_ACTIVE = 1;

  // Subscription is temporarily paused
  SUBSCRIPTION_STATUS_PAUSED = 2;

  // Subscription has been cancelled by client or system
  SUBSCRIPTION_STATUS_CANCELLED = 3;

  // Subscription is in an error state
  SUBSCRIPTION_STATUS_ERROR = 4;
}
```

---

### subtitle_format.proto {#subtitle_format}

**Path**: `gcommon/v1/common/subtitle_format.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `SubtitleFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/subtitle_format.proto
// version: 1.0.1
// guid: f012345-6789-abcd-d6e7-f8a9b0c1d2e3

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Supported subtitle formats.
enum SubtitleFormat {
  SUBTITLE_FORMAT_UNSPECIFIED = 0;
  SUBTITLE_FORMAT_SRT = 1; // SubRip
  SUBTITLE_FORMAT_VTT = 2; // WebVTT
  SUBTITLE_FORMAT_ASS = 3; // Advanced SubStation Alpha
  SUBTITLE_FORMAT_SSA = 4; // SubStation Alpha
  SUBTITLE_FORMAT_TTML = 5; // Timed Text Markup Language
  SUBTITLE_FORMAT_SCC = 6; // Scenarist Closed Caption
  SUBTITLE_FORMAT_SBV = 7; // YouTube subtitle format
}
```

---

### synchronization_frequency.proto {#synchronization_frequency}

**Path**: `gcommon/v1/common/synchronization_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `SynchronizationFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/synchronization_frequency.proto
// version: 1.0.1
// guid: 939438cc-2704-4ba7-ab8a-8ed45e882d94

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum SynchronizationFrequency {
  SYNCHRONIZATION_FREQUENCY_UNSPECIFIED = 0;
  SYNCHRONIZATION_FREQUENCY_REAL_TIME = 1;
  SYNCHRONIZATION_FREQUENCY_HOURLY = 2;
  SYNCHRONIZATION_FREQUENCY_DAILY = 3;
  SYNCHRONIZATION_FREQUENCY_WEEKLY = 4;
  SYNCHRONIZATION_FREQUENCY_ON_CHANGE = 5;
}
```

---

### template_format.proto {#template_format}

**Path**: `gcommon/v1/common/template_format.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `TemplateFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_format.proto
// version: 1.0.1
// guid: 5633815c-6ddb-47f1-b36e-a761ce96bd90

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TemplateFormat {
  TEMPLATE_FORMAT_UNSPECIFIED = 0;
  TEMPLATE_FORMAT_JSON = 1;
  TEMPLATE_FORMAT_YAML = 2;
  TEMPLATE_FORMAT_TOML = 3;
  TEMPLATE_FORMAT_XML = 4;
  TEMPLATE_FORMAT_PROPERTIES = 5;
  TEMPLATE_FORMAT_INI = 6;
  TEMPLATE_FORMAT_CUSTOM = 7;
}
```

---

### template_status.proto {#template_status}

**Path**: `gcommon/v1/common/template_status.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `TemplateStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/template_status.proto
// version: 1.0.1
// guid: fcaf0275-1145-4c6c-af44-a4386dd4c2a7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TemplateStatus {
  TEMPLATE_STATUS_UNSPECIFIED = 0;
  TEMPLATE_STATUS_DRAFT = 1;
  TEMPLATE_STATUS_ACTIVE = 2;
  TEMPLATE_STATUS_DEPRECATED = 3;
  TEMPLATE_STATUS_ARCHIVED = 4;
  TEMPLATE_STATUS_DELETED = 5;
}
```

---

### tenant_status.proto {#tenant_status}

**Path**: `gcommon/v1/common/tenant_status.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Enums** (1): `TenantStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/organization/tenant_status.proto
// version: 1.0.1
// guid: 180914cf-dfc6-4920-bf56-9a4b6972db9d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Tenant status enumeration defining the state of a tenant within an organization.
 * Used for multi-tenant architecture to control tenant access and operations.
 */
enum TenantStatus {
  // Default value indicating no status was specified
  TENANT_STATUS_UNSPECIFIED = 0;

  // Tenant is active and operational
  TENANT_STATUS_ACTIVE = 1;

  // Tenant is inactive (temporarily disabled)
  TENANT_STATUS_INACTIVE = 2;

  // Tenant is suspended due to policy violations or resource limits
  TENANT_STATUS_SUSPENDED = 3;

  // Tenant is pending setup or verification
  TENANT_STATUS_PENDING = 4;

  // Tenant has exceeded resource quotas and is throttled
  TENANT_STATUS_QUOTA_EXCEEDED = 5;

  // Tenant is in trial period with limited features
  TENANT_STATUS_TRIAL = 6;

  // Tenant is archived (read-only access)
  TENANT_STATUS_ARCHIVED = 7;

  // Tenant is marked for deletion
  TENANT_STATUS_DELETED = 8;
}
```

---

### time_unit.proto {#time_unit}

**Path**: `gcommon/v1/common/time_unit.proto` **Package**: `gcommon.v1.common` **Lines**: 55

**Enums** (1): `TimeUnit`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_unit.proto
// version: 1.0.1
// guid: a2bc1886-34e7-4229-93b2-c279f6d89b7a
// file: proto/gcommon/v1/metrics/v1/time_unit.proto
//
// Enum definitions for metrics module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * TimeUnit defines the units of time for metric intervals, retention, and aggregation.
 * Used throughout the metrics system for temporal operations.
 */
enum TimeUnit {
  // Unspecified time unit (default)
  TIME_UNIT_UNSPECIFIED = 0;

  // Nanoseconds
  TIME_UNIT_NANOSECONDS = 1;

  // Microseconds
  TIME_UNIT_MICROSECONDS = 2;

  // Milliseconds
  TIME_UNIT_MILLISECONDS = 3;

  // Seconds
  TIME_UNIT_SECONDS = 4;

  // Minutes
  TIME_UNIT_MINUTES = 5;

  // Hours
  TIME_UNIT_HOURS = 6;

  // Days
  TIME_UNIT_DAYS = 7;

  // Weeks
  TIME_UNIT_WEEKS = 8;

  // Months
  TIME_UNIT_MONTHS = 9;

  // Years
  TIME_UNIT_YEARS = 10;
}
```

---

### time_window.proto {#time_window}

**Path**: `gcommon/v1/common/time_window.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Enums** (1): `TimeWindow`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_window.proto
// version: 1.0.1
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// TimeWindow represents different time windows for metrics aggregation
enum TimeWindow {
  // Unspecified time window
  TIME_WINDOW_UNSPECIFIED = 0;

  // 1 minute window
  TIME_WINDOW_1_MINUTE = 1;

  // 5 minute window
  TIME_WINDOW_5_MINUTES = 2;

  // 15 minute window
  TIME_WINDOW_15_MINUTES = 3;

  // 30 minute window
  TIME_WINDOW_30_MINUTES = 4;

  // 1 hour window
  TIME_WINDOW_1_HOUR = 5;

  // 4 hour window
  TIME_WINDOW_4_HOURS = 6;

  // 12 hour window
  TIME_WINDOW_12_HOURS = 7;

  // 1 day window
  TIME_WINDOW_1_DAY = 8;

  // 1 week window
  TIME_WINDOW_1_WEEK = 9;

  // 1 month window
  TIME_WINDOW_1_MONTH = 10;

  // 1 year window
  TIME_WINDOW_1_YEAR = 11;

  // Custom time window
  TIME_WINDOW_CUSTOM = 12;
}
```

---

### token_status.proto {#token_status}

**Path**: `gcommon/v1/common/token_status.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `TokenStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_status.proto
// version: 1.0.1
// guid: 3d813f39-ef48-4c3e-b551-46ae673e7af1
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Token status enumeration for tracking token lifecycle.
 * Used for token management and security validation.
 */
enum TokenStatus {
  // Unspecified token status
  TOKEN_STATUS_UNSPECIFIED = 0;

  // Token is active and valid
  TOKEN_STATUS_ACTIVE = 1;

  // Token has expired
  TOKEN_STATUS_EXPIRED = 2;

  // Token has been revoked
  TOKEN_STATUS_REVOKED = 3;

  // Token is suspended (temporarily inactive)
  TOKEN_STATUS_SUSPENDED = 4;

  // Token is pending activation
  TOKEN_STATUS_PENDING = 5;

  // Token is invalid (malformed or corrupted)
  TOKEN_STATUS_INVALID = 6;
}
```

---

### token_type.proto {#token_type}

**Path**: `gcommon/v1/common/token_type.proto` **Package**: `gcommon.v1.common` **Lines**: 50

**Enums** (1): `TokenType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_type.proto
// version: 1.0.1
// guid: fe1ca2c9-528e-4485-8890-6b151d7d47ae
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Token type enumeration for different kinds of authentication tokens.
 * Used to distinguish between access tokens, refresh tokens, and other token types.
 */
enum TokenType {
  // Unspecified token type
  TOKEN_TYPE_UNSPECIFIED = 0;

  // Access token for API authentication
  TOKEN_TYPE_ACCESS = 1;

  // Refresh token for token renewal
  TOKEN_TYPE_REFRESH = 2;

  // ID token for user identity (OpenID Connect)
  TOKEN_TYPE_ID = 3;

  // Authorization code for OAuth2 flows
  TOKEN_TYPE_AUTHORIZATION_CODE = 4;

  // API key token for service authentication
  TOKEN_TYPE_API_KEY = 5;

  // Session token for web sessions
  TOKEN_TYPE_SESSION = 6;

  // Password reset token
  TOKEN_TYPE_PASSWORD_RESET = 7;

  // Email verification token
  TOKEN_TYPE_EMAIL_VERIFICATION = 8;

  // Phone verification token
  TOKEN_TYPE_PHONE_VERIFICATION = 9;

  // Invitation token
  TOKEN_TYPE_INVITATION = 10;
}
```

---

### transformation_type.proto {#transformation_type}

**Path**: `gcommon/v1/common/transformation_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `TransformationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/transformation_type.proto
// version: 1.0.1
// guid: 9c4d5ef1-c4a7-4f98-9315-43c2517e6f41

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TransformationType {
  TRANSFORMATION_TYPE_UNSPECIFIED = 0;
  TRANSFORMATION_TYPE_TEMPLATE = 1;
  TRANSFORMATION_TYPE_FUNCTION = 2;
  TRANSFORMATION_TYPE_SCRIPT = 3;
  TRANSFORMATION_TYPE_REGEX = 4;
  TRANSFORMATION_TYPE_JSONPATH = 5;
  TRANSFORMATION_TYPE_XPATH = 6;
  TRANSFORMATION_TYPE_CUSTOM = 7;
}
```

---

### two_fa_type.proto {#two_fa_type}

**Path**: `gcommon/v1/common/two_fa_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `AuthTwoFaType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/two_fa_type.proto
// version: 1.0.1
// guid: dcad7fe3-8803-479a-b205-bff3accb74d5

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthTwoFaType {
  TWO_FA_TYPE_UNSPECIFIED = 0;
  TWO_FA_TYPE_TOTP = 1; // Time-based One-Time Password
  TWO_FA_TYPE_SMS = 2; // SMS code
  TWO_FA_TYPE_BACKUP = 3; // Backup code
}
```

---

### user_status.proto {#user_status}

**Path**: `gcommon/v1/common/user_status.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `UserStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_status.proto
// version: 1.0.1
// guid: 8cc7b811-529b-4c10-8615-1593d65d7c0d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * User account status enumeration defining the state of a user account.
 * Used to track account lifecycle, security status, and access permissions.
 */
enum UserStatus {
  // Default value indicating no status was specified
  USER_STATUS_UNSPECIFIED = 0;

  // User account is active and in good standing
  USER_STATUS_ACTIVE = 1;

  // User account is inactive (user-initiated or policy-based)
  USER_STATUS_INACTIVE = 2;

  // User account is suspended due to policy violations or security concerns
  USER_STATUS_SUSPENDED = 3;

  // User account is pending email or identity verification
  USER_STATUS_PENDING_VERIFICATION = 4;

  // User account is locked due to security concerns (e.g., too many failed login attempts)
  USER_STATUS_LOCKED = 5;

  // User account has been soft-deleted and marked for cleanup
  USER_STATUS_DELETED = 6;
}
```

---

### validation_result_type.proto {#validation_result_type}

**Path**: `gcommon/v1/common/validation_result_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `ValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_result_type.proto
// version: 1.0.1
// guid: e7f8a9b0-c1d2-3e4f-5a6b-7c8d9e0f1a2b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ValidationResultType represents the result of validation.
 * Specifies the outcome of configuration validation checks.
 */
enum ValidationResultType {
  // Unspecified validation result
  VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;

  // Validation passed
  VALIDATION_RESULT_TYPE_PASS = 1;

  // Validation failed
  VALIDATION_RESULT_TYPE_FAIL = 2;

  // Validation completed with warnings
  VALIDATION_RESULT_TYPE_WARNING = 3;

  // Validation was skipped
  VALIDATION_RESULT_TYPE_SKIP = 4;
}
```

---

### validation_rule_severity.proto {#validation_rule_severity}

**Path**: `gcommon/v1/common/validation_rule_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValidationRuleSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_rule_severity.proto
// version: 1.0.1
// guid: 49607ba0-0d79-4402-a891-1a5d80c4286f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValidationRuleSeverity {
  VALIDATION_RULE_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_RULE_SEVERITY_INFO = 1;
  VALIDATION_RULE_SEVERITY_WARNING = 2;
  VALIDATION_RULE_SEVERITY_ERROR = 3;
  VALIDATION_RULE_SEVERITY_CRITICAL = 4;
}
```

---

### validation_rule_type.proto {#validation_rule_type}

**Path**: `gcommon/v1/common/validation_rule_type.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `ValidationRuleType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_rule_type.proto
// version: 1.0.1
// guid: 604ea5f1-2b57-45ce-9711-be0f342bde10

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValidationRuleType {
  VALIDATION_RULE_TYPE_UNSPECIFIED = 0;
  VALIDATION_RULE_TYPE_REGEX = 1;
  VALIDATION_RULE_TYPE_RANGE = 2;
  VALIDATION_RULE_TYPE_LENGTH = 3;
  VALIDATION_RULE_TYPE_FORMAT = 4;
  VALIDATION_RULE_TYPE_ENUM = 5;
  VALIDATION_RULE_TYPE_CUSTOM = 6;
  VALIDATION_RULE_TYPE_FUNCTION = 7;
  VALIDATION_RULE_TYPE_SCHEMA = 8;
}
```

---

### validation_severity.proto {#validation_severity}

**Path**: `gcommon/v1/common/validation_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/validation_severity.proto
// version: 1.0.1
// guid: e0f1a2b3-4567-890b-4567-012345678901

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValidationSeverity {
  VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALIDATION_SEVERITY_INFO = 1;
  VALIDATION_SEVERITY_WARNING = 2;
  VALIDATION_SEVERITY_ERROR = 3;
  VALIDATION_SEVERITY_CRITICAL = 4;
}
```

---

### value_source.proto {#value_source}

**Path**: `gcommon/v1/common/value_source.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `ValueSource`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_source.proto
// version: 1.0.1
// guid: a06a0eb7-f579-4539-87e5-4f5bf9181601

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueSource {
  VALUE_SOURCE_UNSPECIFIED = 0;
  VALUE_SOURCE_DEFAULT = 1;
  VALUE_SOURCE_ENVIRONMENT = 2;
  VALUE_SOURCE_FILE = 3;
  VALUE_SOURCE_DATABASE = 4;
  VALUE_SOURCE_CONSUL = 5;
  VALUE_SOURCE_ETCD = 6;
  VALUE_SOURCE_KUBERNETES = 7;
  VALUE_SOURCE_VAULT = 8;
  VALUE_SOURCE_AWS_PARAMETER_STORE = 9;
  VALUE_SOURCE_AWS_SECRETS_MANAGER = 10;
  VALUE_SOURCE_AZURE_KEY_VAULT = 11;
  VALUE_SOURCE_GCP_SECRET_MANAGER = 12;
  VALUE_SOURCE_REDIS = 13;
  VALUE_SOURCE_API = 14;
  VALUE_SOURCE_COMMAND_LINE = 15;
  VALUE_SOURCE_REMOTE = 16;
  VALUE_SOURCE_COMPUTED = 17;
  VALUE_SOURCE_INHERITED = 18;
  VALUE_SOURCE_OVERRIDE = 19;
  VALUE_SOURCE_CUSTOM = 20;
}
```

---

### value_status.proto {#value_status}

**Path**: `gcommon/v1/common/value_status.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Enums** (1): `ValueStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_status.proto
// version: 1.0.1
// guid: cd97b900-15cf-474b-a899-146f0e687253

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueStatus {
  VALUE_STATUS_UNSPECIFIED = 0;
  VALUE_STATUS_ACTIVE = 1;
  VALUE_STATUS_INACTIVE = 2;
  VALUE_STATUS_DRAFT = 3;
  VALUE_STATUS_DEPRECATED = 4;
  VALUE_STATUS_DELETED = 5;
  VALUE_STATUS_ERROR = 6;
  VALUE_STATUS_PENDING = 7;
  VALUE_STATUS_SYNCING = 8;
  VALUE_STATUS_VALIDATING = 9;
}
```

---

### value_type.proto {#value_type}

**Path**: `gcommon/v1/common/value_type.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Enums** (1): `ValueType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/value_type.proto
// version: 1.0.1
// guid: ad79b2ed-884b-4399-84c0-f29aa53ca0a3
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Value type enumeration for configuration values and other typed data.
 * Provides type safety and validation hints for stored values across
 * all GCommon modules.
 */
enum ValueType {
  // Default value indicating no value type was specified
  VALUE_TYPE_UNSPECIFIED = 0;

  // UTF-8 encoded string value
  VALUE_TYPE_STRING = 1;

  // 64-bit signed integer value
  VALUE_TYPE_INT = 2;

  // Double precision floating point value
  VALUE_TYPE_DOUBLE = 3;

  // Boolean true/false value
  VALUE_TYPE_BOOL = 4;

  // Raw binary data
  VALUE_TYPE_BYTES = 5;

  // JSON-formatted string that should be parsed as JSON
  VALUE_TYPE_JSON = 6;

  // YAML-formatted string that should be parsed as YAML
  VALUE_TYPE_YAML = 7;
}
```

---

### value_validation_result_type.proto {#value_validation_result_type}

**Path**: `gcommon/v1/common/value_validation_result_type.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValueValidationResultType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_validation_result_type.proto
// version: 1.0.1
// guid: 6558f48c-96da-4dc8-b0f1-691f0e0e8999

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueValidationResultType {
  VALUE_VALIDATION_RESULT_TYPE_UNSPECIFIED = 0;
  VALUE_VALIDATION_RESULT_TYPE_PASS = 1;
  VALUE_VALIDATION_RESULT_TYPE_FAIL = 2;
  VALUE_VALIDATION_RESULT_TYPE_WARNING = 3;
  VALUE_VALIDATION_RESULT_TYPE_SKIP = 4;
}
```

---

### value_validation_severity.proto {#value_validation_severity}

**Path**: `gcommon/v1/common/value_validation_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ValueValidationSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/value_validation_severity.proto
// version: 1.0.1
// guid: 55cd1c6a-887d-49f5-b248-9025dc9f5084

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ValueValidationSeverity {
  VALUE_VALIDATION_SEVERITY_UNSPECIFIED = 0;
  VALUE_VALIDATION_SEVERITY_INFO = 1;
  VALUE_VALIDATION_SEVERITY_WARNING = 2;
  VALUE_VALIDATION_SEVERITY_ERROR = 3;
  VALUE_VALIDATION_SEVERITY_CRITICAL = 4;
}
```

---

### verification_type.proto {#verification_type}

**Path**: `gcommon/v1/common/verification_type.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Enums** (1): `AuthVerificationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verification_type.proto
// version: 1.0.1
// guid: 0875b6fd-5225-43a7-a52d-fa98beee769d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// buf:lint:ignore ENUM_VALUE_PREFIX
enum AuthVerificationType {
  VERIFICATION_TYPE_UNSPECIFIED = 0;
  VERIFICATION_TYPE_EMAIL = 1;
  VERIFICATION_TYPE_SMS = 2;
}
```

---

### version_dependency_type.proto {#version_dependency_type}

**Path**: `gcommon/v1/common/version_dependency_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `VersionDependencyType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_dependency_type.proto
// version: 1.0.1
// guid: 34850372-1489-45d0-9f83-e262d595215b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionDependencyType {
  VERSION_DEPENDENCY_TYPE_UNSPECIFIED = 0;
  VERSION_DEPENDENCY_TYPE_RUNTIME = 1;
  VERSION_DEPENDENCY_TYPE_BUILD = 2;
  VERSION_DEPENDENCY_TYPE_TEST = 3;
  VERSION_DEPENDENCY_TYPE_DEV = 4;
  VERSION_DEPENDENCY_TYPE_PEER = 5;
  VERSION_DEPENDENCY_TYPE_OPTIONAL = 6;
}
```

---

### version_deployment_status.proto {#version_deployment_status}

**Path**: `gcommon/v1/common/version_deployment_status.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `VersionDeploymentStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_deployment_status.proto
// version: 1.0.1
// guid: ff99e66b-873a-415d-8f2e-df2a6b1a25c2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionDeploymentStatus {
  VERSION_DEPLOYMENT_STATUS_UNSPECIFIED = 0;
  VERSION_DEPLOYMENT_STATUS_PENDING = 1;
  VERSION_DEPLOYMENT_STATUS_IN_PROGRESS = 2;
  VERSION_DEPLOYMENT_STATUS_SUCCESS = 3;
  VERSION_DEPLOYMENT_STATUS_FAILED = 4;
  VERSION_DEPLOYMENT_STATUS_ROLLED_BACK = 5;
  VERSION_DEPLOYMENT_STATUS_CANCELLED = 6;
}
```

---

### version_health_status.proto {#version_health_status}

**Path**: `gcommon/v1/common/version_health_status.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `VersionHealthStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_health_status.proto
// version: 1.0.1
// guid: 71f9e59c-35f1-439c-9785-8149f061e4d9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionHealthStatus {
  VERSION_HEALTH_STATUS_UNSPECIFIED = 0;
  VERSION_HEALTH_STATUS_HEALTHY = 1;
  VERSION_HEALTH_STATUS_DEGRADED = 2;
  VERSION_HEALTH_STATUS_UNHEALTHY = 3;
  VERSION_HEALTH_STATUS_UNKNOWN = 4;
}
```

---

### version_status.proto {#version_status}

**Path**: `gcommon/v1/common/version_status.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `VersionStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_status.proto
// version: 1.0.1
// guid: 55704401-46f6-4b87-94a8-11020525cfe4

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionStatus {
  VERSION_STATUS_UNSPECIFIED = 0;
  VERSION_STATUS_DRAFT = 1;
  VERSION_STATUS_PENDING = 2;
  VERSION_STATUS_ACTIVE = 3;
  VERSION_STATUS_DEPRECATED = 4;
  VERSION_STATUS_ARCHIVED = 5;
  VERSION_STATUS_DELETED = 6;
  VERSION_STATUS_FAILED = 7;
  VERSION_STATUS_CANCELLED = 8;
}
```

---

### version_type.proto {#version_type}

**Path**: `gcommon/v1/common/version_type.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Enums** (1): `VersionType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/version_type.proto
// version: 1.0.1
// guid: 38337d79-8f7d-4d84-bc08-cf277adfd568

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum VersionType {
  VERSION_TYPE_UNSPECIFIED = 0;
  VERSION_TYPE_MAJOR = 1;
  VERSION_TYPE_MINOR = 2;
  VERSION_TYPE_PATCH = 3;
  VERSION_TYPE_HOTFIX = 4;
  VERSION_TYPE_PRERELEASE = 5;
  VERSION_TYPE_SNAPSHOT = 6;
  VERSION_TYPE_BRANCH = 7;
  VERSION_TYPE_TAG = 8;
}
```

---

### visualization_type.proto {#visualization_type}

**Path**: `gcommon/v1/common/visualization_type.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Enums** (1): `VisualizationType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/visualization_type.proto
// version: 1.0.1
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// VisualizationType represents different types of data visualizations
enum VisualizationType {
  // Unspecified visualization type
  VISUALIZATION_TYPE_UNSPECIFIED = 0;

  // Line chart
  VISUALIZATION_TYPE_LINE_CHART = 1;

  // Bar chart
  VISUALIZATION_TYPE_BAR_CHART = 2;

  // Pie chart
  VISUALIZATION_TYPE_PIE_CHART = 3;

  // Area chart
  VISUALIZATION_TYPE_AREA_CHART = 4;

  // Scatter plot
  VISUALIZATION_TYPE_SCATTER_PLOT = 5;

  // Heatmap
  VISUALIZATION_TYPE_HEATMAP = 6;

  // Histogram
  VISUALIZATION_TYPE_HISTOGRAM = 7;

  // Gauge
  VISUALIZATION_TYPE_GAUGE = 8;

  // Table
  VISUALIZATION_TYPE_TABLE = 9;

  // Single stat
  VISUALIZATION_TYPE_SINGLE_STAT = 10;

  // Graph
  VISUALIZATION_TYPE_GRAPH = 11;

  // Worldmap
  VISUALIZATION_TYPE_WORLDMAP = 12;

  // Text panel
  VISUALIZATION_TYPE_TEXT = 13;

  // Custom visualization
  VISUALIZATION_TYPE_CUSTOM = 14;
}
```

---

### web_auth_method.proto {#web_auth_method}

**Path**: `gcommon/v1/common/web_auth_method.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `WebAuthMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/auth_method.proto
// version: 1.0.1
// guid: f8f4a7c2-b0ea-4b6f-8c70-8bd37e0615f9
//
// AuthMethod defines supported authentication mechanisms for the web module.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// Supported authentication mechanisms for HTTP requests.
enum WebAuthMethod {
  WEB_AUTH_METHOD_UNSPECIFIED = 0;
  WEB_AUTH_METHOD_NONE = 1;
  // Token-based authentication (JWT, API keys, etc.)
  WEB_AUTH_METHOD_TOKEN = 2;
  // OAuth2 with various providers
  WEB_AUTH_METHOD_OAUTH2 = 3;
}
```

---

### web_session_state.proto {#web_session_state}

**Path**: `gcommon/v1/common/web_session_state.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `WebSessionState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/session_state.proto
// version: 1.0.1
// guid: a34ac56d-96ba-4c3e-b36b-a60ba1e62d86
//
// SessionState describes the lifecycle of a user session.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum WebSessionState {
  WEB_SESSION_STATE_UNSPECIFIED = 0;
  WEB_SESSION_STATE_ACTIVE = 1;
  WEB_SESSION_STATE_EXPIRED = 2;
  WEB_SESSION_STATE_REVOKED = 3;
}
```

---

### web_socket_state.proto {#web_socket_state}

**Path**: `gcommon/v1/common/web_socket_state.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `WebSocketState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/web/web_socket_state.proto
// version: 1.0.1
// guid: 0d71bf70-328b-459b-8bc7-674138f22f92
//
// WebSocketState tracks connection lifecycle stages.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum WebSocketState {
  WEB_SOCKET_STATE_UNSPECIFIED = 0;
  WEB_SOCKET_STATE_CONNECTING = 1;
  WEB_SOCKET_STATE_OPEN = 2;
  WEB_SOCKET_STATE_CLOSING = 3;
  WEB_SOCKET_STATE_CLOSED = 4;
}
```

---

### write_level.proto {#write_level}

**Path**: `gcommon/v1/common/write_level.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `WriteLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/write_level.proto
// version: 1.0.1
// guid: 4d949bc0-a987-4e3f-b104-24538f7ae53e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum WriteLevel {
  WRITE_LEVEL_UNSPECIFIED = 0;
  WRITE_LEVEL_ASYNC = 1; // Asynchronous writes
  WRITE_LEVEL_SYNC_ONE = 2; // Synchronous to one replica
  WRITE_LEVEL_SYNC_QUORUM = 3; // Synchronous to quorum
  WRITE_LEVEL_SYNC_ALL = 4; // Synchronous to all replicas
}
```

---

### config_alert_severity.proto {#config_alert_severity}

**Path**: `gcommon/v1/common/config_alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Enums** (1): `ConfigAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/alert_severity.proto
// version: 1.0.1
// guid: e4538794-5759-4c3f-a3ed-b3794a014e86

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConfigAlertSeverity {
  CONFIG_ALERT_SEVERITY_UNSPECIFIED = 0;
  CONFIG_ALERT_SEVERITY_LOW = 1;
  CONFIG_ALERT_SEVERITY_MEDIUM = 2;
  CONFIG_ALERT_SEVERITY_HIGH = 3;
  CONFIG_ALERT_SEVERITY_CRITICAL = 4;
}
```

---

### config_change_type.proto {#config_change_type}

**Path**: `gcommon/v1/common/config_change_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `TemplateChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/change_type.proto
// version: 1.0.1
// guid: 0e330584-b155-45f0-8c79-0aa19e9aa30e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum TemplateChangeType {
  TEMPLATE_CHANGE_TYPE_UNSPECIFIED = 0;
  TEMPLATE_CHANGE_TYPE_FEATURE = 1;
  TEMPLATE_CHANGE_TYPE_BUGFIX = 2;
  TEMPLATE_CHANGE_TYPE_ENHANCEMENT = 3;
  TEMPLATE_CHANGE_TYPE_DEPRECATED = 4;
  TEMPLATE_CHANGE_TYPE_SECURITY = 5;
  CHANGE_TYPE_BREAKING = 6;
}
```

---

### config_config_change_type.proto {#config_config_change_type}

**Path**: `gcommon/v1/common/config_config_change_type.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `ConfigChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_change_type.proto
// version: 1.0.1
// guid: 0d47edd3-705c-42cb-a851-afe79bc2973d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigChangeType enumerates configuration change events.
 */
enum ConfigChangeType {
  CONFIG_CHANGE_TYPE_UNSPECIFIED = 0;
  CONFIG_CHANGE_TYPE_CREATED = 1;
  CONFIG_CHANGE_TYPE_UPDATED = 2;
  CONFIG_CHANGE_TYPE_DELETED = 3;
}
```

---

### config_data_type.proto {#config_data_type}

**Path**: `gcommon/v1/common/config_data_type.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `ConfigDataType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/config_data_type.proto
// version: 1.0.1
// guid: f619e4df-f067-46db-a813-30458f7fd517

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum ConfigDataType {
  CONFIG_DATA_TYPE_UNSPECIFIED = 0;
  CONFIG_DATA_TYPE_STRING = 1;
  CONFIG_DATA_TYPE_INTEGER = 2;
  CONFIG_DATA_TYPE_FLOAT = 3;
  CONFIG_DATA_TYPE_BOOLEAN = 4;
  CONFIG_DATA_TYPE_ENUM = 5;
  CONFIG_DATA_TYPE_LIST = 6;
  CONFIG_DATA_TYPE_MAP = 7;
  CONFIG_DATA_TYPE_JSON = 8;
  CONFIG_DATA_TYPE_YAML = 9;
  CONFIG_DATA_TYPE_URL = 10;
  CONFIG_DATA_TYPE_EMAIL = 11;
  CONFIG_DATA_TYPE_PASSWORD = 12;
  CONFIG_DATA_TYPE_CERTIFICATE = 13;
  CONFIG_DATA_TYPE_PRIVATE_KEY = 14;
  CONFIG_DATA_TYPE_PUBLIC_KEY = 15;
  CONFIG_DATA_TYPE_DURATION = 16;
  CONFIG_DATA_TYPE_TIMESTAMP = 17;
  CONFIG_DATA_TYPE_REGEX = 18;
  CONFIG_DATA_TYPE_IPV4 = 19;
  CONFIG_DATA_TYPE_IPV6 = 20;
  CONFIG_DATA_TYPE_CIDR = 21;
  CONFIG_DATA_TYPE_PORT = 22;
  CONFIG_DATA_TYPE_UUID = 23;
  CONFIG_DATA_TYPE_BASE64 = 24;
  CONFIG_DATA_TYPE_HEX = 25;
}
```

---

### ack_level.proto {#ack_level}

**Path**: `gcommon/v1/common/ack_level.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Enums** (1): `AckLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/ack_level.proto
// file: proto/gcommon/v1/queue/ack_level.proto
// version: 1.0.1
// guid: 9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Acknowledgment level for durability guarantees.
 */
enum AckLevel {
  // Default unspecified level
  ACK_LEVEL_UNSPECIFIED = 0;

  // No acknowledgment required (fire and forget)
  ACK_LEVEL_NONE = 1;

  // Wait for leader acknowledgment only
  ACK_LEVEL_LEADER = 2;

  // Wait for all replicas to acknowledge
  ACK_LEVEL_ALL = 3;

  // Wait for majority of replicas
  ACK_LEVEL_MAJORITY = 4;
}
```

---

### ack_mode.proto {#ack_mode}

**Path**: `gcommon/v1/common/ack_mode.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Enums** (1): `AckMode`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/ack_mode.proto
// version: 1.0.1
// guid: 1ea916c3-cb02-4ad8-9ff0-03396568398a
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Acknowledgment mode enumeration for message processing.
 * Defines how message acknowledgments are handled in streaming operations,
 * queue processing, and event handling across all GCommon modules.
 */
enum AckMode {
  // Default value indicating no acknowledgment mode was specified
  ACK_MODE_UNSPECIFIED = 0;

  // Manual acknowledgment - client must explicitly acknowledge messages
  ACK_MODE_MANUAL = 1;

  // Automatic acknowledgment - messages are acknowledged upon delivery
  ACK_MODE_AUTO = 2;

  // Client-side acknowledgment - acknowledgment is handled by client logic
  ACK_MODE_CLIENT = 3;
}
```

---

### ack_type.proto {#ack_type}

**Path**: `gcommon/v1/common/ack_type.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `AckType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ack_type.proto
// version: 1.0.1
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Types of acknowledgments.
 * Defines how a consumed message was processed.
 */
enum AckType {
  // Unspecified acknowledgment type
  ACK_TYPE_UNSPECIFIED = 0;

  // Successful processing acknowledgment
  ACK_TYPE_SUCCESS = 1;

  // Failed processing - retry message
  ACK_TYPE_RETRY = 2;

  // Failed processing - reject message (dead letter)
  ACK_TYPE_REJECT = 3;

  // Processing timeout
  ACK_TYPE_TIMEOUT = 4;
}
```

---

### backup_frequency.proto {#backup_frequency}

**Path**: `gcommon/v1/common/backup_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `BackupFrequency`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/backup_frequency.proto
// version: 1.0.1
// guid: 4efc5d0f-be87-47e1-8f01-f42fa2926368

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum BackupFrequency {
  BACKUP_FREQUENCY_UNSPECIFIED = 0;
  BACKUP_FREQUENCY_MANUAL = 1;
  BACKUP_FREQUENCY_HOURLY = 2;
  BACKUP_FREQUENCY_DAILY = 3;
  BACKUP_FREQUENCY_WEEKLY = 4;
  BACKUP_FREQUENCY_MONTHLY = 5;
  BACKUP_FREQUENCY_ON_CHANGE = 6;
}
```

---

### batch_priority.proto {#batch_priority}

**Path**: `gcommon/v1/common/batch_priority.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `BatchPriority`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/batch_priority.proto
// version: 1.0.1
// guid: f9429991-ff0a-4c70-a6e5-7d639281f030

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * BatchPriority defines the processing priority for batch operations.
 */
enum BatchPriority {
  BATCH_PRIORITY_UNSPECIFIED = 0;
  BATCH_PRIORITY_LOW = 1;
  BATCH_PRIORITY_NORMAL = 2;
  BATCH_PRIORITY_HIGH = 3;
  BATCH_PRIORITY_URGENT = 4;
}
```

---

### change_type.proto {#change_type}

**Path**: `gcommon/v1/common/change_type.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `MetricsChangeType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/change_type.proto
// version: 1.0.1
// guid: 43b77608-77cc-40ad-97ae-4055d556fe1f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ChangeType defines the type of configuration change.
 */
enum MetricsChangeType {
  CHANGE_TYPE_UNSPECIFIED = 0;
  CHANGE_TYPE_ADDED = 1;
  CHANGE_TYPE_UPDATED = 2;
  CHANGE_TYPE_REMOVED = 3;
  CHANGE_TYPE_REPLACED = 4;
}
```

---

### queue_alert_severity.proto {#queue_alert_severity}

**Path**: `gcommon/v1/common/queue_alert_severity.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Enums** (1): `QueueAlertSeverity`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alert_severity.proto
// version: 1.0.1
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Alert severity levels.
 */
enum QueueAlertSeverity {
  // Default unspecified severity
  QUEUE_ALERT_SEVERITY_UNSPECIFIED = 0;

  // Informational alert
  QUEUE_ALERT_SEVERITY_INFO = 1;

  // Warning level alert
  QUEUE_ALERT_SEVERITY_WARNING = 2;

  // Error level alert
  QUEUE_ALERT_SEVERITY_ERROR = 3;

  // Critical alert requiring immediate attention
  QUEUE_ALERT_SEVERITY_CRITICAL = 4;
}
```

---

### queue_consistency_level.proto {#queue_consistency_level}

**Path**: `gcommon/v1/common/queue_consistency_level.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Enums** (1): `QueueConsistencyLevel`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/consistency_level.proto
// file: proto/gcommon/v1/queue/consistency_level.proto
// version: 1.0.1
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Consistency level for queue operations.
 */
enum QueueConsistencyLevel {
  // Default unspecified consistency level
  QUEUE_CONSISTENCY_LEVEL_UNSPECIFIED = 0;

  // Eventual consistency (fastest, may read stale data)
  QUEUE_CONSISTENCY_LEVEL_EVENTUAL = 1;

  // Weak consistency (balance between speed and consistency)
  QUEUE_CONSISTENCY_LEVEL_WEAK = 2;

  // Strong consistency (slower, guarantees latest data)
  QUEUE_CONSISTENCY_LEVEL_STRONG = 3;

  // Sequential consistency (operations appear in some sequential order)
  QUEUE_CONSISTENCY_LEVEL_SEQUENTIAL = 4;

  // Linearizable consistency (strongest, operations appear instantaneous)
  QUEUE_CONSISTENCY_LEVEL_LINEARIZABLE = 5;
}
```

---

### queue_export_format.proto {#queue_export_format}

**Path**: `gcommon/v1/common/queue_export_format.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Enums** (1): `QueueExportFormat`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/export_format.proto
// file: proto/gcommon/v1/queue/export_format.proto
// version: 1.0.1
// guid: 3a2b1c0d-9e8f-7a6b-5c4d-3e2f1a0b9c8d
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Export format options.
 */
enum QueueExportFormat {
  // Default unspecified format
  QUEUE_EXPORT_FORMAT_UNSPECIFIED = 0;

  // JSON format
  QUEUE_EXPORT_FORMAT_JSON = 1;

  // Protocol Buffers binary format
  QUEUE_EXPORT_FORMAT_PROTOBUF = 2;

  // CSV format (metadata only)
  QUEUE_EXPORT_FORMAT_CSV = 3;

  // Custom format
  QUEUE_EXPORT_FORMAT_CUSTOM = 4;
}
```

---

### queue_metric_type.proto {#queue_metric_type}

**Path**: `gcommon/v1/common/queue_metric_type.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Enums** (1): `QueueMetricType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/metric_type.proto
// version: 1.0.1
// guid: 8b7a6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * MetricType represents the types of metrics that can be monitored.
 * Specifies different types of queue metrics for monitoring and analysis.
 */
enum QueueMetricType {
  // Default unspecified type
  QUEUE_METRIC_TYPE_UNSPECIFIED = 0;

  // Message count
  QUEUE_METRIC_TYPE_MESSAGE_COUNT = 1;

  // Message rate (per second)
  QUEUE_METRIC_TYPE_MESSAGE_RATE = 2;

  // Processing time
  QUEUE_METRIC_TYPE_PROCESSING_TIME = 3;

  // Error rate
  QUEUE_METRIC_TYPE_ERROR_RATE = 4;

  // Consumer count
  QUEUE_METRIC_TYPE_CONSUMER_COUNT = 5;

  // Queue depth
  QUEUE_METRIC_TYPE_QUEUE_DEPTH = 6;
}
```

---

### queue_state.proto {#queue_state}

**Path**: `gcommon/v1/common/queue_state.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Enums** (1): `QueueState`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_state.proto
// version: 1.0.1
// guid: 8f9a0b1c-2d3e-4f5a-6b7c-8d9e0f1a2b3c
//
// Enum definitions for queue module
//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Represents the operational state of a queue.
 */
// buf:lint:ignore ENUM_VALUE_PREFIX
enum QueueState {
  // Default unknown state
  QUEUE_STATE_UNSPECIFIED = 0;

  // Queue is active and processing messages
  QUEUE_STATE_ACTIVE = 1;

  // Queue is paused (not processing messages but accepting them)
  QUEUE_STATE_PAUSED = 2;

  // Queue is suspended (not accepting new messages)
  QUEUE_STATE_SUSPENDED = 3;

  // Queue is in the process of being deleted
  QUEUE_STATE_DELETING = 4;

  // Queue is in maintenance mode
  QUEUE_STATE_MAINTENANCE = 5;

  // Queue has encountered an error and needs attention
  QUEUE_STATE_ERROR = 6;
}
```

---

### queue_type.proto {#queue_type}

**Path**: `gcommon/v1/common/queue_type.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Enums** (1): `QueueType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_type.proto
// version: 1.0.1
// guid: d6bb0e83-91d3-406a-9a66-519b5860d137

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// QueueType enumerates supported queue implementations.
enum QueueType {
  // Default unspecified implementation.
  QUEUE_TYPE_UNSPECIFIED = 0;
  // In-memory queue for testing or lightweight workloads.
  QUEUE_TYPE_MEMORY = 1;
  // Redis-backed queue.
  QUEUE_TYPE_REDIS = 2;
  // NATS-based streaming queue.
  QUEUE_TYPE_NATS = 3;
  // Cloud provider queue (e.g., AWS SQS).
  QUEUE_TYPE_CLOUD = 4;
}
```

---

### restore_point_status.proto {#restore_point_status}

**Path**: `gcommon/v1/common/restore_point_status.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Enums** (1): `RestorePointStatus`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/restore_point_status.proto
// version: 1.0.1
// guid: 83838713-4e8f-494e-93ec-7bdf0b406982

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RestorePointStatus {
  RESTORE_POINT_STATUS_UNSPECIFIED = 0;
  RESTORE_POINT_STATUS_CREATING = 1;
  RESTORE_POINT_STATUS_ACTIVE = 2;
  RESTORE_POINT_STATUS_EXPIRED = 3;
  RESTORE_POINT_STATUS_DELETED = 4;
  RESTORE_POINT_STATUS_ERROR = 5;
}
```

---

### restore_point_type.proto {#restore_point_type}

**Path**: `gcommon/v1/common/restore_point_type.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Enums** (1): `RestorePointType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/restore_point_type.proto
// version: 1.0.1
// guid: 2f531175-07c6-46a3-a5ab-01b240355ab8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

enum RestorePointType {
  RESTORE_POINT_TYPE_UNSPECIFIED = 0;
  RESTORE_POINT_TYPE_MANUAL = 1; // Manually created restore point
  RESTORE_POINT_TYPE_AUTOMATIC = 2; // Automatically created restore point
  RESTORE_POINT_TYPE_SCHEDULED = 3; // Scheduled restore point
  RESTORE_POINT_TYPE_PRE_CHANGE = 4; // Created before configuration change
  RESTORE_POINT_TYPE_MILESTONE = 5; // Milestone restore point
  RESTORE_POINT_TYPE_BACKUP = 6; // Backup restore point
}
```

---

### rollback_method.proto {#rollback_method}

**Path**: `gcommon/v1/common/rollback_method.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Enums** (1): `RollbackMethod`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/rollback_method.proto
// version: 1.0.1
// guid: b0c1d2e3-f4a5-6b7c-8d9e-0f1a2b3c4d5e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RollbackMethod represents how the rollback was performed.
 * Specifies the technique used to revert configuration changes.
 */
enum RollbackMethod {
  // Unspecified rollback method
  ROLLBACK_METHOD_UNSPECIFIED = 0;

  // Restore individual values
  ROLLBACK_METHOD_VALUE_RESTORE = 1;

  // Restore from version history
  ROLLBACK_METHOD_VERSION_RESTORE = 2;

  // Restore from snapshot
  ROLLBACK_METHOD_SNAPSHOT_RESTORE = 3;

  // Manual rollback process
  ROLLBACK_METHOD_MANUAL = 4;
}
```

---

### update_action.proto {#update_action}

**Path**: `gcommon/v1/common/update_action.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `UpdateAction`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_action.proto
// version: 1.0.1
// guid: cb7f4802-67a0-4c44-a5b3-b98fc2aab61a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * UpdateAction indicates what action was taken during the update.
 */
enum UpdateAction {
  UPDATE_ACTION_UNSPECIFIED = 0;
  UPDATE_ACTION_UPDATED = 1;
  UPDATE_ACTION_NO_CHANGE = 2;
  UPDATE_ACTION_RESTARTED = 3;
  UPDATE_ACTION_RECREATED = 4;
}
```

---

### update_strategy.proto {#update_strategy}

**Path**: `gcommon/v1/common/update_strategy.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Enums** (1): `UpdateStrategy`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/update_strategy.proto
// version: 1.0.1
// guid: 33aabd04-d32c-4267-94a4-dca8e8c580ad

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * UpdateStrategy defines how updates should be applied.
 */
enum UpdateStrategy {
  UPDATE_STRATEGY_UNSPECIFIED = 0;
  UPDATE_STRATEGY_ROLLING = 1;
  UPDATE_STRATEGY_BLUE_GREEN = 2;
  UPDATE_STRATEGY_IMMEDIATE = 3;
  UPDATE_STRATEGY_SCHEDULED = 4;
}
```

---
