# Queue Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 317
- **Messages**: 317

## Table of Contents

### Messages

- [`APIKeyAuth`](#api_key_auth) - from api_key_auth.proto
- [`AckRequest`](#ack_request) - from ack_request.proto
- [`AckResponse`](#ack_response) - from ack_response.proto
- [`AcknowledgeRequest`](#acknowledge_request) - from acknowledge_request.proto
- [`AcknowledgeResponse`](#acknowledge_response) - from acknowledge_response.proto
- [`Acknowledgment`](#acknowledgment) - from acknowledgment.proto
- [`AgeBucket`](#age_bucket) - from age_bucket.proto
- [`AgeDistribution`](#age_distribution) - from age_distribution.proto
- [`AlertRule`](#alert_rule) - from alert_rule.proto
- [`AlertingConfig`](#alerting_config) - from alerting_config.proto
- [`AntiAffinityRule`](#anti_affinity_rule) - from anti_affinity_rule.proto
- [`AuthCacheConfig`](#auth_cache_config) - from auth_cache_config.proto
- [`AuthenticationConfig`](#authentication_config) - from authentication_config.proto
- [`AuthorizationConfig`](#authorization_config) - from authorization_config.proto
- [`AutoCommitConfig`](#auto_commit_config) - from auto_commit_config.proto
- [`BackupQueueRequest`](#backup_queue_request) - from backup_queue_request.proto
- [`BackupQueueResponse`](#backup_queue_response) - from backup_queue_response.proto
- [`BackupSource`](#backup_source) - from backup_source.proto
- [`BasicQueueStats`](#basic_queue_stats) - from basic_queue_stats.proto
- [`BatchAckRequest`](#batch_ack_request) - from batch_ack_request.proto
- [`BatchAckResponse`](#batch_ack_response) - from batch_ack_response.proto
- [`BatchConfig`](#batch_config) - from batch_config.proto
- [`BatchDeliveryConfig`](#batch_delivery_config) - from batch_delivery_config.proto
- [`BatchNackRequest`](#batch_nack_request) - from batch_nack_request.proto
- [`BatchNackResponse`](#batch_nack_response) - from batch_nack_response.proto
- [`BatchPublishRequest`](#batch_publish_request) - from batch_publish_request.proto
- [`BatchPublishResponse`](#batch_publish_response) - from batch_publish_response.proto
- [`BatchPullRequest`](#batch_pull_request) - from batch_pull_request.proto
- [`BatchPullResponse`](#batch_pull_response) - from batch_pull_response.proto
- [`BatchSettings`](#batch_settings) - from batch_settings.proto
- [`BindingInfo`](#binding_info) - from binding_info.proto
- [`ChecksumValidation`](#checksum_validation) - from checksum_validation.proto
- [`ClusterConfig`](#cluster_config) - from cluster_config.proto
- [`ClusterHealth`](#cluster_health) - from cluster_health.proto
- [`ClusterInfo`](#cluster_info) - from cluster_info.proto
- [`ClusterStats`](#cluster_stats) - from cluster_stats.proto
- [`CommitOffsetRequest`](#commit_offset_request) - from commit_offset_request.proto
- [`CommitOffsetResponse`](#commit_offset_response) - from commit_offset_response.proto
- [`ConflictDetection`](#conflict_detection) - from conflict_detection.proto
- [`ConnectionDetails`](#connection_details) - from connection_details.proto
- [`ConsistencyConfig`](#consistency_config) - from consistency_config.proto
- [`ConsistencyValidation`](#consistency_validation) - from consistency_validation.proto
- [`Consumer`](#consumer) - from consumer.proto
- [`ConsumerClient`](#consumer_client) - from consumer_client.proto
- [`ConsumerConfig`](#consumer_config) - from consumer_config.proto
- [`ConsumerErrorStats`](#consumer_error_stats) - from consumer_error_stats.proto
- [`ConsumerGroup`](#consumer_group) - from consumer_group.proto
- [`ConsumerGroupConfig`](#consumer_group_config) - from consumer_group_config.proto
- [`ConsumerGroupStats`](#consumer_group_stats) - from consumer_group_stats.proto
- [`ConsumerStats`](#consumer_stats) - from consumer_stats.proto
- [`ContentFilter`](#content_filter) - from content_filter.proto
- [`ContentUpdate`](#content_update) - from content_update.proto
- [`CreateQueueRequest`](#create_queue_request) - from create_queue_request.proto
- [`CreateQueueResponse`](#create_queue_response) - from create_queue_response.proto
- [`CreateSubscriptionRequest`](#create_subscription_request) - from create_subscription_request.proto
- [`CreateSubscriptionResponse`](#create_subscription_response) - from create_subscription_response.proto
- [`CreateTopicRequest`](#create_topic_request) - from create_topic_request.proto
- [`CreateTopicResponse`](#create_topic_response) - from create_topic_response.proto
- [`CustomResolution`](#custom_resolution) - from custom_resolution.proto
- [`DeadLetterConfig`](#dead_letter_config) - from dead_letter_config.proto
- [`DeadLetterPolicy`](#dead_letter_policy) - from dead_letter_policy.proto
- [`DeadLetterQueueConfig`](#dead_letter_queue_config) - from dead_letter_queue_config.proto
- [`DeleteCriteria`](#delete_criteria) - from delete_criteria.proto
- [`DeleteQueueRequest`](#delete_queue_request) - from delete_queue_request.proto
- [`DeleteQueueResponse`](#delete_queue_response) - from delete_queue_response.proto
- [`DeleteSubscriptionRequest`](#delete_subscription_request) - from delete_subscription_request.proto
- [`DeleteSubscriptionResponse`](#delete_subscription_response) - from delete_subscription_response.proto
- [`DeleteTopicRequest`](#delete_topic_request) - from delete_topic_request.proto
- [`DeleteTopicResponse`](#delete_topic_response) - from delete_topic_response.proto
- [`DeletionStats`](#deletion_stats) - from deletion_stats.proto
- [`DeliveryConfiguration`](#delivery_configuration) - from delivery_configuration.proto
- [`DeliveryOptions`](#delivery_options) - from delivery_options.proto
- [`DeliveryRetryConfig`](#delivery_retry_config) - from delivery_retry_config.proto
- [`DeliverySettings`](#delivery_settings) - from delivery_settings.proto
- [`DequeueRequest`](#dequeue_request) - from dequeue_request.proto
- [`DequeueResponse`](#dequeue_response) - from dequeue_response.proto
- [`DeserializationConfig`](#deserialization_config) - from deserialization_config.proto
- [`DurabilityConfig`](#durability_config) - from durability_config.proto
- [`EncryptionInfo`](#encryption_info) - from encryption_info.proto
- [`EnqueueRequest`](#enqueue_request) - from enqueue_request.proto
- [`EnqueueResponse`](#enqueue_response) - from enqueue_response.proto
- [`ErrorActionConfig`](#error_action_config) - from error_action_config.proto
- [`ErrorHandlingConfig`](#error_handling_config) - from error_handling_config.proto
- [`ErrorNotificationConfig`](#error_notification_config) - from error_notification_config.proto
- [`ErrorTypeStat`](#error_type_stat) - from error_type_stat.proto
- [`ExchangeConfig`](#exchange_config) - from exchange_config.proto
- [`ExportQueueRequest`](#export_queue_request) - from export_queue_request.proto
- [`ExportQueueResponse`](#export_queue_response) - from export_queue_response.proto
- [`ExternalAuthService`](#external_auth_service) - from external_auth_service.proto
- [`ExternalRoleProvider`](#external_role_provider) - from external_role_provider.proto
- [`FailedAck`](#failed_ack) - from failed_ack.proto
- [`FailedFieldUpdate`](#failed_field_update) - from failed_field_update.proto
- [`FilterCriteria`](#filter_criteria) - from filter_criteria.proto
- [`FilterSettings`](#filter_settings) - from filter_settings.proto
- [`FlowControl`](#flow_control) - from flow_control.proto
- [`FlowControlConfig`](#flow_control_config) - from flow_control_config.proto
- [`FlowControlSettings`](#flow_control_settings) - from flow_control_settings.proto
- [`FlushQueueRequest`](#flush_queue_request) - from flush_queue_request.proto
- [`FlushQueueResponse`](#flush_queue_response) - from flush_queue_response.proto
- [`FormatOptions`](#format_options) - from format_options.proto
- [`GetClusterInfoRequest`](#get_cluster_info_request) - from get_cluster_info_request.proto
- [`GetClusterInfoResponse`](#get_cluster_info_response) - from get_cluster_info_response.proto
- [`GetMessageRequest`](#get_message_request) - from get_message_request.proto
- [`GetMessageResponse`](#get_message_response) - from get_message_response.proto
- [`GetNodeInfoRequest`](#get_node_info_request) - from get_node_info_request.proto
- [`GetNodeInfoResponse`](#get_node_info_response) - from get_node_info_response.proto
- [`GetOffsetRequest`](#get_offset_request) - from get_offset_request.proto
- [`GetOffsetResponse`](#get_offset_response) - from get_offset_response.proto
- [`GetPartitionInfoRequest`](#get_partition_info_request) - from get_partition_info_request.proto
- [`GetPartitionInfoResponse`](#get_partition_info_response) - from get_partition_info_response.proto
- [`GetQueueHealthRequest`](#get_queue_health_request) - from get_queue_health_request.proto
- [`GetQueueHealthResponse`](#get_queue_health_response) - from get_queue_health_response.proto
- [`GetQueueInfoRequest`](#get_queue_info_request) - from get_queue_info_request.proto
- [`GetQueueInfoResponse`](#get_queue_info_response) - from get_queue_info_response.proto
- [`GetQueueStatsRequest`](#get_queue_stats_request) - from get_queue_stats_request.proto
- [`GetQueueStatsResponse`](#get_queue_stats_response) - from get_queue_stats_response.proto
- [`GetSubscriptionInfoRequest`](#get_subscription_info_request) - from get_subscription_info_request.proto
- [`GetSubscriptionInfoResponse`](#get_subscription_info_response) - from get_subscription_info_response.proto
- [`GetTopicInfoRequest`](#get_topic_info_request) - from get_topic_info_request.proto
- [`GetTopicInfoResponse`](#get_topic_info_response) - from get_topic_info_response.proto
- [`GroupCoordinator`](#group_coordinator) - from group_coordinator.proto
- [`HeaderRoutingConfig`](#header_routing_config) - from header_routing_config.proto
- [`HistoricalDataPoint`](#historical_data_point) - from historical_data_point.proto
- [`HistoricalStats`](#historical_stats) - from historical_stats.proto
- [`ImportQueueRequest`](#import_queue_request) - from import_queue_request.proto
- [`ImportQueueResponse`](#import_queue_response) - from import_queue_response.proto
- [`IntegrityValidation`](#integrity_validation) - from integrity_validation.proto
- [`JwtAuth`](#jwt_auth) - from jwt_auth.proto
- [`KeyValidationService`](#key_validation_service) - from key_validation_service.proto
- [`LastWriterWins`](#last_writer_wins) - from last_writer_wins.proto
- [`LatencyMetrics`](#latency_metrics) - from latency_metrics.proto
- [`ListMessagesRequest`](#list_messages_request) - from list_messages_request.proto
- [`ListMessagesResponse`](#list_messages_response) - from list_messages_response.proto
- [`ListQueuesRequest`](#list_queues_request) - from list_queues_request.proto
- [`ListQueuesResponse`](#list_queues_response) - from list_queues_response.proto
- [`ListSubscriptionsResponse`](#list_subscriptions_response) - from list_subscriptions_response.proto
- [`ListTopicsRequest`](#list_topics_request) - from list_topics_request.proto
- [`ListTopicsResponse`](#list_topics_response) - from list_topics_response.proto
- [`LoadBalancingConfig`](#load_balancing_config) - from load_balancing_config.proto
- [`MessageAckResult`](#message_ack_result) - from message_ack_result.proto
- [`MessageEnvelope`](#message_envelope) - from message_envelope.proto
- [`MessageFilter`](#message_filter) - from message_filter.proto
- [`MessageFilterConfig`](#message_filter_config) - from message_filter_config.proto
- [`MessageId`](#message_id) - from message_id.proto
- [`MessageMetadata`](#message_metadata) - from message_metadata.proto
- [`MessageNack`](#message_nack) - from message_nack.proto
- [`MessageProperties`](#message_properties) - from message_properties.proto
- [`MessageStateCounts`](#message_state_counts) - from message_state_counts.proto
- [`MessageUpdateProperties`](#message_update_properties) - from message_update_properties.proto
- [`MetadataUpdate`](#metadata_update) - from metadata_update.proto
- [`MetricsEvent`](#metrics_event) - from metrics_event.proto
- [`MigrateQueueRequest`](#migrate_queue_request) - from migrate_queue_request.proto
- [`MigrateQueueResponse`](#migrate_queue_response) - from migrate_queue_response.proto
- [`MigrationConfig`](#migration_config) - from migration_config.proto
- [`MultiValueConfig`](#multi_value_config) - from multi_value_config.proto
- [`NackError`](#nack_error) - from nack_error.proto
- [`NackRequest`](#nack_request) - from nack_request.proto
- [`NackResponse`](#nack_response) - from nack_response.proto
- [`NodeInfo`](#node_info) - from node_info.proto
- [`NodeStats`](#node_stats) - from node_stats.proto
- [`OAuth2Auth`](#o_auth2_auth) - from o_auth2_auth.proto
- [`OffsetConfig`](#offset_config) - from offset_config.proto
- [`OffsetInfo`](#offset_info) - from offset_info.proto
- [`OffsetRange`](#offset_range) - from offset_range.proto
- [`OrderingConfig`](#ordering_config) - from ordering_config.proto
- [`OriginalQueueInfo`](#original_queue_info) - from original_queue_info.proto
- [`OwnerInfo`](#owner_info) - from owner_info.proto
- [`PartitionAssignment`](#partition_assignment) - from partition_assignment.proto
- [`PartitionCommitResult`](#partition_commit_result) - from partition_commit_result.proto
- [`PartitionConfig`](#partition_config) - from partition_config.proto
- [`PartitionInfo`](#partition_info) - from partition_info.proto
- [`PartitionOffset`](#partition_offset) - from partition_offset.proto
- [`PartitionRestoreResult`](#partition_restore_result) - from partition_restore_result.proto
- [`PauseQueueRequest`](#pause_queue_request) - from pause_queue_request.proto
- [`PauseQueueResponse`](#pause_queue_response) - from pause_queue_response.proto
- [`PeekRequest`](#peek_request) - from peek_request.proto
- [`PeekResponse`](#peek_response) - from peek_response.proto
- [`PerformanceConfig`](#performance_config) - from performance_config.proto
- [`PerformanceMetrics`](#performance_metrics) - from performance_metrics.proto
- [`PerformanceOptions`](#performance_options) - from performance_options.proto
- [`PermissionRule`](#permission_rule) - from permission_rule.proto
- [`PreservedStats`](#preserved_stats) - from preserved_stats.proto
- [`PriorityRange`](#priority_range) - from priority_range.proto
- [`PriorityUpdate`](#priority_update) - from priority_update.proto
- [`PublishConfig`](#publish_config) - from publish_config.proto
- [`PublishResponse`](#publish_response) - from publish_response.proto
- [`PublishResult`](#publish_result) - from publish_result.proto
- [`PullRequest`](#pull_request) - from pull_request.proto
- [`PullResponse`](#pull_response) - from pull_response.proto
- [`PurgeOptions`](#purge_options) - from purge_options.proto
- [`PurgeRequest`](#purge_request) - from purge_request.proto
- [`PurgeResponse`](#purge_response) - from purge_response.proto
- [`PushRequest`](#push_request) - from push_request.proto
- [`PushResponse`](#push_response) - from push_response.proto
- [`QueueBackupConfig`](#backup_config) - from backup_config.proto
- [`QueueBackupInfo`](#backup_info) - from backup_info.proto
- [`QueueCircuitBreakerConfig`](#circuit_breaker_config) - from circuit_breaker_config.proto
- [`QueueCompressionConfig`](#compression_config) - from compression_config.proto
- [`QueueConfig`](#queue_config) - from queue_config.proto
- [`QueueConfiguration`](#queue_configuration) - from queue_configuration.proto
- [`QueueConflictResolution`](#conflict_resolution) - from conflict_resolution.proto
- [`QueueConsumerStats`](#queue_consumer_stats) - from queue_consumer_stats.proto
- [`QueueDeleteRequest`](#delete_request) - from delete_request.proto
- [`QueueDeleteResponse`](#delete_response) - from delete_response.proto
- [`QueueDepthSample`](#queue_depth_sample) - from queue_depth_sample.proto
- [`QueueEncryptionConfig`](#encryption_config) - from encryption_config.proto
- [`QueueErrorStats`](#error_stats) - from error_stats.proto
- [`QueueHealth`](#queue_health) - from queue_health.proto
- [`QueueHealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`QueueHealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`QueueInfo`](#queue_info) - from queue_info.proto
- [`QueueListSubscriptionsRequest`](#list_subscriptions_request) - from list_subscriptions_request.proto
- [`QueueMessage`](#queue_message) - from queue_message.proto
- [`QueueMonitoringConfig`](#monitoring_config) - from monitoring_config.proto
- [`QueueNotificationChannel`](#notification_channel) - from notification_channel.proto
- [`QueuePublishRequest`](#publish_request) - from publish_request.proto
- [`QueueRateLimitConfig`](#rate_limit_config) - from rate_limit_config.proto
- [`QueueRetentionInfo`](#retention_info) - from retention_info.proto
- [`QueueRetentionPolicy`](#retention_policy) - from retention_policy.proto
- [`QueueRetryConfig`](#retry_config) - from retry_config.proto
- [`QueueRetryPolicy`](#retry_policy) - from retry_policy.proto
- [`QueueRetrySettings`](#retry_settings) - from retry_settings.proto
- [`QueueStats`](#queue_stats) - from queue_stats.proto
- [`QueueStatsPoint`](#queue_stats_point) - from queue_stats_point.proto
- [`QueueStatsResponse`](#queue_stats_response) - from queue_stats_response.proto
- [`QueueStatsSummary`](#queue_stats_summary) - from queue_stats_summary.proto
- [`QueueStreamMetricsRequest`](#stream_metrics_request) - from stream_metrics_request.proto
- [`QueueSubscribeRequest`](#subscribe_request) - from subscribe_request.proto
- [`QueueSubscriptionInfo`](#subscription_info) - from subscription_info.proto
- [`QueueTimeRange`](#time_range) - from time_range.proto
- [`QueueTimeoutConfig`](#timeout_config) - from timeout_config.proto
- [`QueueTimestampRange`](#timestamp_range) - from timestamp_range.proto
- [`QueueUnsubscribeRequest`](#unsubscribe_request) - from unsubscribe_request.proto
- [`QueueValidationResult`](#validation_result) - from validation_result.proto
- [`QueueWorkflow`](#workflow) - from workflow.proto
- [`ReadConsistency`](#read_consistency) - from read_consistency.proto
- [`ReadRetryConfig`](#read_retry_config) - from read_retry_config.proto
- [`RebalanceStats`](#rebalance_stats) - from rebalance_stats.proto
- [`ReceivedMessage`](#received_message) - from received_message.proto
- [`ReplicationConfig`](#replication_config) - from replication_config.proto
- [`ReplicationConsistency`](#replication_consistency) - from replication_consistency.proto
- [`ResetDetails`](#reset_details) - from reset_details.proto
- [`ResetQueueStatsRequest`](#reset_queue_stats_request) - from reset_queue_stats_request.proto
- [`ResetQueueStatsResponse`](#reset_queue_stats_response) - from reset_queue_stats_response.proto
- [`RestoreConfig`](#restore_config) - from restore_config.proto
- [`RestoreError`](#restore_error) - from restore_error.proto
- [`RestoreOptions`](#restore_options) - from restore_options.proto
- [`RestoreQueueRequest`](#restore_queue_request) - from restore_queue_request.proto
- [`RestoreQueueResponse`](#restore_queue_response) - from restore_queue_response.proto
- [`RestoreStatistics`](#restore_statistics) - from restore_statistics.proto
- [`RestoreStatus`](#restore_status) - from restore_status.proto
- [`RestoreWarning`](#restore_warning) - from restore_warning.proto
- [`ResumeQueueRequest`](#resume_queue_request) - from resume_queue_request.proto
- [`ResumeQueueResponse`](#resume_queue_response) - from resume_queue_response.proto
- [`ResumeStats`](#resume_stats) - from resume_stats.proto
- [`RetryDelayConfig`](#retry_delay_config) - from retry_delay_config.proto
- [`RoleBasedAccessControl`](#role_based_access_control) - from role_based_access_control.proto
- [`RoleInheritance`](#role_inheritance) - from role_inheritance.proto
- [`RoutingCondition`](#routing_condition) - from routing_condition.proto
- [`RoutingConfig`](#routing_config) - from routing_config.proto
- [`RoutingInfo`](#routing_info) - from routing_info.proto
- [`RoutingKey`](#routing_key) - from routing_key.proto
- [`RoutingRule`](#routing_rule) - from routing_rule.proto
- [`RoutingSettings`](#routing_settings) - from routing_settings.proto
- [`SASLAuth`](#sasl_auth) - from sasl_auth.proto
- [`SchemaConfig`](#schema_config) - from schema_config.proto
- [`SchemaValidation`](#schema_validation) - from schema_validation.proto
- [`SeekRequest`](#seek_request) - from seek_request.proto
- [`SeekResponse`](#seek_response) - from seek_response.proto
- [`SendMessageRequest`](#send_message_request) - from send_message_request.proto
- [`SendMessageResponse`](#send_message_response) - from send_message_response.proto
- [`SerializationConfig`](#serialization_config) - from serialization_config.proto
- [`SizeBucket`](#size_bucket) - from size_bucket.proto
- [`SizeDistribution`](#size_distribution) - from size_distribution.proto
- [`SizeRange`](#size_range) - from size_range.proto
- [`StartWorkflowRequest`](#start_workflow_request) - from start_workflow_request.proto
- [`StartWorkflowResponse`](#start_workflow_response) - from start_workflow_response.proto
- [`StopWorkflowRequest`](#stop_workflow_request) - from stop_workflow_request.proto
- [`StopWorkflowResponse`](#stop_workflow_response) - from stop_workflow_response.proto
- [`StreamConfig`](#stream_config) - from stream_config.proto
- [`StreamMessagesRequest`](#stream_messages_request) - from stream_messages_request.proto
- [`StreamMessagesResponse`](#stream_messages_response) - from stream_messages_response.proto
- [`SubscribeResponse`](#subscribe_response) - from subscribe_response.proto
- [`SubscriptionConfig`](#subscription_config) - from subscription_config.proto
- [`SubscriptionConfigUpdate`](#subscription_config_update) - from subscription_config_update.proto
- [`SubscriptionConfiguration`](#subscription_configuration) - from subscription_configuration.proto
- [`SubscriptionStats`](#subscription_stats) - from subscription_stats.proto
- [`SyncReplication`](#sync_replication) - from sync_replication.proto
- [`TLSAuth`](#tls_auth) - from tls_auth.proto
- [`ThroughputMetrics`](#throughput_metrics) - from throughput_metrics.proto
- [`TimeRangeFilter`](#time_range_filter) - from time_range_filter.proto
- [`TimestampConfig`](#timestamp_config) - from timestamp_config.proto
- [`TopicConfig`](#topic_config) - from topic_config.proto
- [`TopicConfiguration`](#topic_configuration) - from topic_configuration.proto
- [`TopicInfo`](#topic_info) - from topic_info.proto
- [`TopicPermissions`](#topic_permissions) - from topic_permissions.proto
- [`TopicRoutingConfig`](#topic_routing_config) - from topic_routing_config.proto
- [`TopicStats`](#topic_stats) - from topic_stats.proto
- [`TransformationConfig`](#transformation_config) - from transformation_config.proto
- [`UnsubscribeResponse`](#unsubscribe_response) - from unsubscribe_response.proto
- [`UpdateCondition`](#update_condition) - from update_condition.proto
- [`UpdateMessageRequest`](#update_message_request) - from update_message_request.proto
- [`UpdateMessageResponse`](#update_message_response) - from update_message_response.proto
- [`UpdateQueueConfigRequest`](#update_queue_config_request) - from update_queue_config_request.proto
- [`UpdateQueueConfigResponse`](#update_queue_config_response) - from update_queue_config_response.proto
- [`UpdateSubscriptionConfigRequest`](#update_subscription_config_request) - from update_subscription_config_request.proto
- [`UpdateSubscriptionConfigResponse`](#update_subscription_config_response) - from update_subscription_config_response.proto
- [`UpdateTopicConfigRequest`](#update_topic_config_request) - from update_topic_config_request.proto
- [`UpdateTopicConfigResponse`](#update_topic_config_response) - from update_topic_config_response.proto
- [`UpdatedProperties`](#updated_properties) - from updated_properties.proto
- [`UsernamePasswordAuth`](#username_password_auth) - from username_password_auth.proto
- [`ValidationConfig`](#validation_config) - from validation_config.proto
- [`ValidationError`](#validation_error) - from validation_error.proto
- [`VectorClockConfig`](#vector_clock_config) - from vector_clock_config.proto
- [`VisibilityUpdate`](#visibility_update) - from visibility_update.proto
- [`WriteConsistency`](#write_consistency) - from write_consistency.proto
- [`WriteRetryConfig`](#write_retry_config) - from write_retry_config.proto

### Files in this Module

- [ack_request.proto](#ack_request)
- [ack_response.proto](#ack_response)
- [acknowledge_request.proto](#acknowledge_request)
- [acknowledge_response.proto](#acknowledge_response)
- [backup_info.proto](#backup_info)
- [backup_queue_request.proto](#backup_queue_request)
- [backup_queue_response.proto](#backup_queue_response)
- [backup_source.proto](#backup_source)
- [batch_ack_request.proto](#batch_ack_request)
- [batch_ack_response.proto](#batch_ack_response)
- [batch_nack_request.proto](#batch_nack_request)
- [batch_nack_response.proto](#batch_nack_response)
- [batch_publish_request.proto](#batch_publish_request)
- [batch_publish_response.proto](#batch_publish_response)
- [batch_pull_request.proto](#batch_pull_request)
- [batch_pull_response.proto](#batch_pull_response)
- [batch_settings.proto](#batch_settings)
- [commit_offset_request.proto](#commit_offset_request)
- [commit_offset_response.proto](#commit_offset_response)
- [create_queue_request.proto](#create_queue_request)
- [create_queue_response.proto](#create_queue_response)
- [create_subscription_request.proto](#create_subscription_request)
- [create_subscription_response.proto](#create_subscription_response)
- [create_topic_request.proto](#create_topic_request)
- [create_topic_response.proto](#create_topic_response)
- [delete_criteria.proto](#delete_criteria)
- [delete_queue_request.proto](#delete_queue_request)
- [delete_queue_response.proto](#delete_queue_response)
- [delete_request.proto](#delete_request)
- [delete_response.proto](#delete_response)
- [delete_subscription_request.proto](#delete_subscription_request)
- [delete_subscription_response.proto](#delete_subscription_response)
- [delete_topic_request.proto](#delete_topic_request)
- [delete_topic_response.proto](#delete_topic_response)
- [dequeue_request.proto](#dequeue_request)
- [dequeue_response.proto](#dequeue_response)
- [enqueue_request.proto](#enqueue_request)
- [enqueue_response.proto](#enqueue_response)
- [export_queue_request.proto](#export_queue_request)
- [export_queue_response.proto](#export_queue_response)
- [flush_queue_request.proto](#flush_queue_request)
- [flush_queue_response.proto](#flush_queue_response)
- [get_cluster_info_request.proto](#get_cluster_info_request)
- [get_cluster_info_response.proto](#get_cluster_info_response)
- [get_message_request.proto](#get_message_request)
- [get_message_response.proto](#get_message_response)
- [get_node_info_request.proto](#get_node_info_request)
- [get_node_info_response.proto](#get_node_info_response)
- [get_offset_request.proto](#get_offset_request)
- [get_offset_response.proto](#get_offset_response)
- [get_partition_info_request.proto](#get_partition_info_request)
- [get_partition_info_response.proto](#get_partition_info_response)
- [get_queue_health_request.proto](#get_queue_health_request)
- [get_queue_health_response.proto](#get_queue_health_response)
- [get_queue_info_request.proto](#get_queue_info_request)
- [get_queue_info_response.proto](#get_queue_info_response)
- [get_queue_stats_request.proto](#get_queue_stats_request)
- [get_queue_stats_response.proto](#get_queue_stats_response)
- [get_subscription_info_request.proto](#get_subscription_info_request)
- [get_subscription_info_response.proto](#get_subscription_info_response)
- [get_topic_info_request.proto](#get_topic_info_request)
- [get_topic_info_response.proto](#get_topic_info_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [import_queue_request.proto](#import_queue_request)
- [import_queue_response.proto](#import_queue_response)
- [list_messages_request.proto](#list_messages_request)
- [list_messages_response.proto](#list_messages_response)
- [list_queues_request.proto](#list_queues_request)
- [list_queues_response.proto](#list_queues_response)
- [list_subscriptions_request.proto](#list_subscriptions_request)
- [list_subscriptions_response.proto](#list_subscriptions_response)
- [list_topics_request.proto](#list_topics_request)
- [list_topics_response.proto](#list_topics_response)
- [migrate_queue_request.proto](#migrate_queue_request)
- [migrate_queue_response.proto](#migrate_queue_response)
- [nack_request.proto](#nack_request)
- [nack_response.proto](#nack_response)
- [pause_queue_request.proto](#pause_queue_request)
- [pause_queue_response.proto](#pause_queue_response)
- [peek_request.proto](#peek_request)
- [peek_response.proto](#peek_response)
- [publish_request.proto](#publish_request)
- [publish_response.proto](#publish_response)
- [publish_result.proto](#publish_result)
- [pull_request.proto](#pull_request)
- [pull_response.proto](#pull_response)
- [purge_request.proto](#purge_request)
- [purge_response.proto](#purge_response)
- [push_request.proto](#push_request)
- [push_response.proto](#push_response)
- [queue_consumer_stats.proto](#queue_consumer_stats)
- [queue_depth_sample.proto](#queue_depth_sample)
- [queue_health.proto](#queue_health)
- [queue_info.proto](#queue_info)
- [queue_message.proto](#queue_message)
- [queue_stats.proto](#queue_stats)
- [queue_stats_point.proto](#queue_stats_point)
- [queue_stats_response.proto](#queue_stats_response)
- [queue_stats_summary.proto](#queue_stats_summary)
- [reset_details.proto](#reset_details)
- [reset_queue_stats_request.proto](#reset_queue_stats_request)
- [reset_queue_stats_response.proto](#reset_queue_stats_response)
- [restore_error.proto](#restore_error)
- [restore_options.proto](#restore_options)
- [restore_queue_request.proto](#restore_queue_request)
- [restore_queue_response.proto](#restore_queue_response)
- [restore_statistics.proto](#restore_statistics)
- [restore_status.proto](#restore_status)
- [restore_warning.proto](#restore_warning)
- [resume_queue_request.proto](#resume_queue_request)
- [resume_queue_response.proto](#resume_queue_response)
- [seek_request.proto](#seek_request)
- [seek_response.proto](#seek_response)
- [send_message_request.proto](#send_message_request)
- [send_message_response.proto](#send_message_response)
- [start_workflow_request.proto](#start_workflow_request)
- [start_workflow_response.proto](#start_workflow_response)
- [stop_workflow_request.proto](#stop_workflow_request)
- [stop_workflow_response.proto](#stop_workflow_response)
- [stream_messages_request.proto](#stream_messages_request)
- [stream_messages_response.proto](#stream_messages_response)
- [stream_metrics_request.proto](#stream_metrics_request)
- [subscribe_request.proto](#subscribe_request)
- [subscribe_response.proto](#subscribe_response)
- [unsubscribe_request.proto](#unsubscribe_request)
- [unsubscribe_response.proto](#unsubscribe_response)
- [update_condition.proto](#update_condition)
- [update_message_request.proto](#update_message_request)
- [update_message_response.proto](#update_message_response)
- [acknowledgment.proto](#acknowledgment)
- [age_bucket.proto](#age_bucket)
- [age_distribution.proto](#age_distribution)
- [alert_rule.proto](#alert_rule)
- [anti_affinity_rule.proto](#anti_affinity_rule)
- [api_key_auth.proto](#api_key_auth)
- [basic_queue_stats.proto](#basic_queue_stats)
- [binding_info.proto](#binding_info)
- [checksum_validation.proto](#checksum_validation)
- [cluster_health.proto](#cluster_health)
- [cluster_info.proto](#cluster_info)
- [cluster_stats.proto](#cluster_stats)
- [conflict_detection.proto](#conflict_detection)
- [conflict_resolution.proto](#conflict_resolution)
- [connection_details.proto](#connection_details)
- [consistency_validation.proto](#consistency_validation)
- [consumer.proto](#consumer)
- [consumer_client.proto](#consumer_client)
- [consumer_error_stats.proto](#consumer_error_stats)
- [consumer_group.proto](#consumer_group)
- [consumer_group_stats.proto](#consumer_group_stats)
- [consumer_stats.proto](#consumer_stats)
- [content_filter.proto](#content_filter)
- [content_update.proto](#content_update)
- [custom_resolution.proto](#custom_resolution)
- [dead_letter_policy.proto](#dead_letter_policy)
- [deletion_stats.proto](#deletion_stats)
- [delivery_options.proto](#delivery_options)
- [delivery_settings.proto](#delivery_settings)
- [encryption_info.proto](#encryption_info)
- [error_stats.proto](#error_stats)
- [error_type_stat.proto](#error_type_stat)
- [external_role_provider.proto](#external_role_provider)
- [failed_ack.proto](#failed_ack)
- [failed_field_update.proto](#failed_field_update)
- [filter_criteria.proto](#filter_criteria)
- [filter_settings.proto](#filter_settings)
- [flow_control.proto](#flow_control)
- [flow_control_settings.proto](#flow_control_settings)
- [format_options.proto](#format_options)
- [group_coordinator.proto](#group_coordinator)
- [historical_data_point.proto](#historical_data_point)
- [historical_stats.proto](#historical_stats)
- [integrity_validation.proto](#integrity_validation)
- [jwt_auth.proto](#jwt_auth)
- [last_writer_wins.proto](#last_writer_wins)
- [latency_metrics.proto](#latency_metrics)
- [message_ack_result.proto](#message_ack_result)
- [message_envelope.proto](#message_envelope)
- [message_filter.proto](#message_filter)
- [message_id.proto](#message_id)
- [message_metadata.proto](#message_metadata)
- [message_nack.proto](#message_nack)
- [message_properties.proto](#message_properties)
- [message_state_counts.proto](#message_state_counts)
- [message_update_properties.proto](#message_update_properties)
- [metadata_update.proto](#metadata_update)
- [nack_error.proto](#nack_error)
- [node_info.proto](#node_info)
- [node_stats.proto](#node_stats)
- [notification_channel.proto](#notification_channel)
- [o_auth2_auth.proto](#o_auth2_auth)
- [offset_info.proto](#offset_info)
- [offset_range.proto](#offset_range)
- [original_queue_info.proto](#original_queue_info)
- [owner_info.proto](#owner_info)
- [partition_assignment.proto](#partition_assignment)
- [partition_commit_result.proto](#partition_commit_result)
- [partition_info.proto](#partition_info)
- [partition_offset.proto](#partition_offset)
- [partition_restore_result.proto](#partition_restore_result)
- [performance_metrics.proto](#performance_metrics)
- [performance_options.proto](#performance_options)
- [permission_rule.proto](#permission_rule)
- [preserved_stats.proto](#preserved_stats)
- [priority_range.proto](#priority_range)
- [priority_update.proto](#priority_update)
- [purge_options.proto](#purge_options)
- [read_consistency.proto](#read_consistency)
- [rebalance_stats.proto](#rebalance_stats)
- [received_message.proto](#received_message)
- [replication_consistency.proto](#replication_consistency)
- [resume_stats.proto](#resume_stats)
- [retention_info.proto](#retention_info)
- [retention_policy.proto](#retention_policy)
- [retry_policy.proto](#retry_policy)
- [retry_settings.proto](#retry_settings)
- [role_based_access_control.proto](#role_based_access_control)
- [role_inheritance.proto](#role_inheritance)
- [routing_condition.proto](#routing_condition)
- [routing_info.proto](#routing_info)
- [routing_key.proto](#routing_key)
- [routing_rule.proto](#routing_rule)
- [routing_settings.proto](#routing_settings)
- [sasl_auth.proto](#sasl_auth)
- [schema_validation.proto](#schema_validation)
- [size_bucket.proto](#size_bucket)
- [size_distribution.proto](#size_distribution)
- [size_range.proto](#size_range)
- [subscription_info.proto](#subscription_info)
- [subscription_stats.proto](#subscription_stats)
- [sync_replication.proto](#sync_replication)
- [throughput_metrics.proto](#throughput_metrics)
- [time_range.proto](#time_range)
- [time_range_filter.proto](#time_range_filter)
- [timestamp_range.proto](#timestamp_range)
- [tls_auth.proto](#tls_auth)
- [topic_info.proto](#topic_info)
- [topic_permissions.proto](#topic_permissions)
- [topic_stats.proto](#topic_stats)
- [updated_properties.proto](#updated_properties)
- [username_password_auth.proto](#username_password_auth)
- [validation_error.proto](#validation_error)
- [validation_result.proto](#validation_result)
- [visibility_update.proto](#visibility_update)
- [workflow.proto](#workflow)
- [write_consistency.proto](#write_consistency)
- [alerting_config.proto](#alerting_config)
- [auth_cache_config.proto](#auth_cache_config)
- [authentication_config.proto](#authentication_config)
- [authorization_config.proto](#authorization_config)
- [auto_commit_config.proto](#auto_commit_config)
- [backup_config.proto](#backup_config)
- [batch_config.proto](#batch_config)
- [batch_delivery_config.proto](#batch_delivery_config)
- [circuit_breaker_config.proto](#circuit_breaker_config)
- [cluster_config.proto](#cluster_config)
- [compression_config.proto](#compression_config)
- [consistency_config.proto](#consistency_config)
- [consumer_config.proto](#consumer_config)
- [consumer_group_config.proto](#consumer_group_config)
- [dead_letter_config.proto](#dead_letter_config)
- [dead_letter_queue_config.proto](#dead_letter_queue_config)
- [delivery_configuration.proto](#delivery_configuration)
- [delivery_retry_config.proto](#delivery_retry_config)
- [deserialization_config.proto](#deserialization_config)
- [durability_config.proto](#durability_config)
- [encryption_config.proto](#encryption_config)
- [error_action_config.proto](#error_action_config)
- [error_handling_config.proto](#error_handling_config)
- [error_notification_config.proto](#error_notification_config)
- [exchange_config.proto](#exchange_config)
- [flow_control_config.proto](#flow_control_config)
- [header_routing_config.proto](#header_routing_config)
- [load_balancing_config.proto](#load_balancing_config)
- [message_filter_config.proto](#message_filter_config)
- [migration_config.proto](#migration_config)
- [monitoring_config.proto](#monitoring_config)
- [multi_value_config.proto](#multi_value_config)
- [offset_config.proto](#offset_config)
- [ordering_config.proto](#ordering_config)
- [partition_config.proto](#partition_config)
- [performance_config.proto](#performance_config)
- [publish_config.proto](#publish_config)
- [queue_config.proto](#queue_config)
- [queue_configuration.proto](#queue_configuration)
- [rate_limit_config.proto](#rate_limit_config)
- [read_retry_config.proto](#read_retry_config)
- [replication_config.proto](#replication_config)
- [restore_config.proto](#restore_config)
- [retry_config.proto](#retry_config)
- [retry_delay_config.proto](#retry_delay_config)
- [routing_config.proto](#routing_config)
- [schema_config.proto](#schema_config)
- [serialization_config.proto](#serialization_config)
- [stream_config.proto](#stream_config)
- [subscription_config.proto](#subscription_config)
- [subscription_config_update.proto](#subscription_config_update)
- [subscription_configuration.proto](#subscription_configuration)
- [timeout_config.proto](#timeout_config)
- [timestamp_config.proto](#timestamp_config)
- [topic_config.proto](#topic_config)
- [topic_configuration.proto](#topic_configuration)
- [topic_routing_config.proto](#topic_routing_config)
- [transformation_config.proto](#transformation_config)
- [update_queue_config_request.proto](#update_queue_config_request)
- [update_queue_config_response.proto](#update_queue_config_response)
- [update_subscription_config_request.proto](#update_subscription_config_request)
- [update_subscription_config_response.proto](#update_subscription_config_response)
- [update_topic_config_request.proto](#update_topic_config_request)
- [update_topic_config_response.proto](#update_topic_config_response)
- [validation_config.proto](#validation_config)
- [vector_clock_config.proto](#vector_clock_config)
- [write_retry_config.proto](#write_retry_config)
- [external_auth_service.proto](#external_auth_service)
- [key_validation_service.proto](#key_validation_service)
- [metrics_event.proto](#metrics_event)

---

## Messages Documentation

### ack_request.proto {#ack_request}

**Path**: `gcommon/v1/queue/ack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `AckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ack_request.proto
// version: 1.0.0
// guid: 3a91b3b5-86fd-443c-876b-5b7b4da2fa73
// AckRequest acknowledges successful processing of a message and
// removes it from the queue. This file was previously a placeholder
// and now contains the full request definition following the 1-1-1
// protobuf pattern.
// AckRequest contains the information required to acknowledge a
// single message. The receipt handle is provided by the queue when
// the message is received.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AckRequest {
  // Name of the queue containing the message.
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Receipt handle identifying the message instance.
  string receipt_handle = 2;

  // Standard request metadata including authentication and tracing.
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### ack_response.proto {#ack_response}

**Path**: `gcommon/v1/queue/ack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `AckResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ack_response.proto
// version: 1.0.1
// guid: e0629319-177a-44c0-9ec6-f97c73c03cbc

// AckResponse indicates whether a message acknowledgment was
// successfully processed. This replaces the previous placeholder
// created during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// AckResponse is returned after successfully acknowledging a message.
// If `success` is false, the `error` field contains additional
// information about why the acknowledgment failed.
message AckResponse {
  // True if the message was removed from the queue.
  bool success = 1;

  // Optional error information when success is false.
  gcommon.v1.common.Error error = 2;
}
```

---

### acknowledge_request.proto {#acknowledge_request}

**Path**: `gcommon/v1/queue/acknowledge_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 86

**Messages** (1): `AcknowledgeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/acknowledge_request.proto
// version: 1.0.0
// guid: 3f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * AcknowledgeRequest confirms successful processing of one or more messages.
 * Once acknowledged, messages are permanently removed from the queue
 * and will not be redelivered.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message AcknowledgeRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue containing the messages.
   * Must match the queue from which messages were dequeued.
   */
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * Receipt handles of messages to acknowledge.
   * These handles were provided in the DequeueResponse.
   */
  repeated string receipt_handles = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Consumer ID that processed these messages.
   * Used for tracking and metrics.
   */
  string consumer_id = 12;

  /**
   * Processing result for each message (same order as receipt_handles).
   * Valid values: "success", "failed", "retry", "skip".
   * If not provided, "success" is assumed for all messages.
   */
  repeated string processing_results = 13;

  /**
   * Optional processing notes or error details for each message.
   * Useful for debugging and audit trails.
   */
  repeated string processing_notes = 14;

  /**
   * Processing time in milliseconds for each message.
   * Used for performance monitoring and SLA tracking.
   */
  repeated int64 processing_times_ms = 15;

  /**
   * Whether to force acknowledgment even if visibility timeout expired.
   * Use with caution as it may cause duplicate processing. Default: false.
   */
  bool force_acknowledge = 16;

  /**
   * Batch acknowledgment mode. If true, all messages succeed or fail together.
   * If false, each message is processed individually. Default: false.
   */
  bool batch_mode = 17;
}
```

---

### acknowledge_response.proto {#acknowledge_response}

**Path**: `gcommon/v1/queue/acknowledge_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 109

**Messages** (1): `AcknowledgeResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/message_ack_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/acknowledge_response.proto
// version: 1.0.0
// guid: 69fb5b85-226c-407d-9aaf-dd8810a3b662

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/message_ack_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AcknowledgeResponse {
  // Required fields (1-10)

  /**
   * Overall success status of the acknowledgment operation.
   * True if all messages were successfully acknowledged.
   */
  bool success = 1;

  /**
   * Number of messages that were successfully acknowledged.
   */
  int32 acknowledged_count = 2;

  /**
   * Number of messages that failed to be acknowledged.
   */
  int32 failed_count = 3;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue where messages were acknowledged.
   * Echoed from the request for verification.
   */
  string queue_name = 12 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * Detailed results for each message acknowledgment.
   * Only populated if there were failures or if detailed results were requested.
   */
  repeated MessageAckResult message_results = 13;

  /**
   * Consumer ID that was used for acknowledgment.
   * Echoed from the request for verification.
   */
  string consumer_id = 14;

  /**
   * Total processing time for the acknowledgment operation in milliseconds.
   */
  int64 operation_time_ms = 15;

  /**
   * Whether the operation was completed in batch mode.
   * Echoed from the request for verification.
   */
  bool batch_mode = 16;

  /**
   * Number of messages that were already acknowledged (duplicates).
   * These don't count as failures but indicate potential issues.
   */
  int32 already_acknowledged_count = 17;

  /**
   * Number of messages with expired visibility timeouts.
   * These may have been redelivered to other consumers.
   */
  int32 expired_timeout_count = 18;

  // Status and error fields (61-70)

  /**
   * Error information if the overall acknowledgment operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the acknowledgment operation was processed.
   */
  google.protobuf.Timestamp acknowledged_at = 51;

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}
```

---

### backup_info.proto {#backup_info}

**Path**: `gcommon/v1/queue/backup_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `QueueBackupInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/backup_info.proto
// version: 1.0.0
// guid: 7e0f3e6b-8c36-4f63-9aa6-06ee60e83a15

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueBackupInfo {
  // Backup identifier
  string backup_id = 1 [(buf.validate.field).string.min_len = 1];

  // Backup location
  string backup_location = 2 [(buf.validate.field).string.min_len = 1];

  // Backup size (bytes)
  int64 backup_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Backup timestamp
  google.protobuf.Timestamp backup_created_at = 4;

  // Backup expiration time
  google.protobuf.Timestamp backup_expires_at = 5;
}
```

---

### backup_queue_request.proto {#backup_queue_request}

**Path**: `gcommon/v1/queue/backup_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `BackupQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/backup_queue_request.proto
// version: 1.0.0
// guid: 0f505896-49b9-4ca3-8a27-d0f9a79ad1ac
// Request to backup a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to backup a queue
message BackupQueueRequest {
  // Queue name to backup
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Backup destination path
  string backup_path = 2;

  // Include message data
  bool include_messages = 3;

  // Include metadata only
  bool metadata_only = 4;

  // Backup format (JSON, binary, etc.)
  string format = 5;

  // Compression type (none, gzip, etc.)
  string compression = 6;

  // Start timestamp for backup range
  int64 start_timestamp = 7;

  // End timestamp for backup range
  int64 end_timestamp = 8;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 9;
}
```

---

### backup_queue_response.proto {#backup_queue_response}

**Path**: `gcommon/v1/queue/backup_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `BackupQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/backup_queue_response.proto
// version: 1.0.0
// guid: f0001260-db1f-4a6a-8b58-21f91e69dc4d
// Response for queue backup operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue backup operations
message BackupQueueResponse {
  // Whether the backup was successful
  bool success = 1;

  // Backup file path or identifier
  string backup_location = 2 [(buf.validate.field).string.min_len = 1];

  // Number of messages backed up
  int64 messages_backed_up = 3 [(buf.validate.field).int64.gte = 0];

  // Size of backup in bytes
  int64 backup_size_bytes = 4 [(buf.validate.field).int64.gte = 0];

  // Backup duration (milliseconds)
  int32 backup_duration_ms = 5 [(buf.validate.field).int32.gt = 0];

  // Backup checksum for integrity verification
  string checksum = 6 [(buf.validate.field).string.min_len = 1];

  // Backup timestamp
  int64 backup_timestamp = 7;

  // Error message if backup failed
  string error = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### backup_source.proto {#backup_source}

**Path**: `gcommon/v1/queue/backup_source.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `BackupSource`

**Imports** (5):

- `gcommon/v1/queue/encryption_info.proto`
- `gcommon/v1/queue/original_queue_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/backup_source.proto
// version: 1.0.0
// guid: 07747072-2f4d-414e-a232-b282cd58bd5e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/encryption_info.proto";
import "gcommon/v1/queue/original_queue_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message BackupSource {
  // Backup identifier
  string backup_id = 1 [(buf.validate.field).string.min_len = 1];

  // Backup location/path
  string backup_path = 2 [(buf.validate.field).string.min_len = 1];

  // Backup storage type (s3, gcs, local, etc.)
  string storage_type = 3 [(buf.validate.field).string.min_len = 1];

  // Storage credentials
  map<string, string> credentials = 4;

  // Backup creation timestamp
  google.protobuf.Timestamp backup_timestamp = 5;

  // Original queue information
  OriginalQueueInfo original_queue = 6;

  // Backup format version
  string backup_version = 7 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Backup compression format
  string compression_format = 8 [(buf.validate.field).string.min_len = 1];

  // Backup encryption details
  EncryptionInfo encryption = 9;
}
```

---

### batch_ack_request.proto {#batch_ack_request}

**Path**: `gcommon/v1/queue/batch_ack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `BatchAckRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_ack_request.proto
// version: 1.0.0
// guid: 73ed83fb-3706-45cc-895d-fec71d0a2184
// Request for batch acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request for batch acknowledgment operations
message BatchAckRequest {
  // List of message IDs to acknowledge
  repeated string message_ids = 1 [(buf.validate.field).repeated.min_items = 1];

  // Consumer group ID
  string consumer_group_id = 2 [(buf.validate.field).string.min_len = 1];

  // Subscription ID
  string subscription_id = 3 [(buf.validate.field).string.min_len = 1];

  // Acknowledgment level
  string ack_level = 4 [(buf.validate.field).string.min_len = 1];

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### batch_ack_response.proto {#batch_ack_response}

**Path**: `gcommon/v1/queue/batch_ack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `BatchAckResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/failed_ack.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_ack_response.proto
// version: 1.0.0
// guid: f9db0dcc-9ce1-4f92-87fd-2ed15dd3fefb

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/failed_ack.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message BatchAckResponse {
  // Overall success status
  bool success = 1;

  // Number of messages successfully acknowledged
  int32 acknowledged_count = 2 [(buf.validate.field).int32.gte = 0];

  // Number of messages that failed to acknowledge
  int32 failed_count = 3 [(buf.validate.field).int32.gte = 0];

  // Failed message IDs and their error reasons
  repeated FailedAck failed_acks = 4 [(buf.validate.field).repeated.min_items = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;

  // Batch ID for tracking
  string batch_id = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### batch_nack_request.proto {#batch_nack_request}

**Path**: `gcommon/v1/queue/batch_nack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `BatchNackRequest`

**Imports** (3):

- `gcommon/v1/queue/message_nack.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_nack_request.proto
// version: 1.0.0
// guid: a97a83e4-7bab-4c6e-9770-d11334535e11

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/message_nack.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message BatchNackRequest {
  // Consumer group ID performing the nack
  string consumer_group_id = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer ID within the group
  string consumer_id = 2 [(buf.validate.field).string.min_len = 1];

  // Messages to negative acknowledge
  repeated MessageNack message_nacks = 3 [(buf.validate.field).repeated.min_items = 1];

  // Requeue messages after nack
  bool requeue_messages = 4;

  // Delay before requeuing (milliseconds)
  int64 requeue_delay_ms = 5 [(buf.validate.field).int64.gte = 0];

  // Maximum number of requeue attempts
  int32 max_requeue_attempts = 6 [(buf.validate.field).int32.gte = 0];

  // Send failed messages to dead letter queue
  bool send_to_dlq = 7;

  // Reason for batch nack operation
  string nack_reason = 8 [(buf.validate.field).string.min_len = 1];

  // Additional metadata for the nack operation
  map<string, string> metadata = 9;
}
```

---

### batch_nack_response.proto {#batch_nack_response}

**Path**: `gcommon/v1/queue/batch_nack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `BatchNackResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_nack_response.proto
// version: 1.0.0
// guid: c89cb423-a81c-4024-b081-c61406804442
// Response for batch negative acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for batch negative acknowledgment operations
message BatchNackResponse {
  // Number of messages successfully nacked
  int32 successful_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of messages that failed to nack
  int32 failed_count = 2 [(buf.validate.field).int32.gte = 0];

  // List of message IDs that were successfully nacked
  repeated string successful_message_ids = 3 [(buf.validate.field).repeated.min_items = 1];

  // List of message IDs that failed to nack
  repeated string failed_message_ids = 4 [(buf.validate.field).repeated.min_items = 1];

  // Error messages for failed nacks (indexed by failed_message_ids)
  repeated string error_messages = 5 [(buf.validate.field).repeated.min_items = 1];

  // Overall operation error if any
  string error = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### batch_publish_request.proto {#batch_publish_request}

**Path**: `gcommon/v1/queue/batch_publish_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `BatchPublishRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_publish_request.proto
// version: 1.0.0
// guid: e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to publish multiple messages to a queue in a single operation.
 * Provides better performance for high-throughput scenarios.
 */
message BatchPublishRequest {
  // Queue name to publish messages to
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Messages to publish
  repeated QueueMessage messages = 2;

  // Whether to use a transaction for the batch
  bool use_transaction = 3;

  // Timeout for the batch operation (milliseconds)
  int32 timeout_ms = 4;

  // Whether to wait for acknowledgment from all brokers
  bool wait_for_all = 5;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;

  // Maximum number of retries for failed messages
  int32 max_retries = 7;

  // Batch ID for tracking (optional)
  string batch_id = 8;
}
```

---

### batch_publish_response.proto {#batch_publish_response}

**Path**: `gcommon/v1/queue/batch_publish_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `BatchPublishResponse`

**Imports** (3):

- `gcommon/v1/queue/publish_result.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_publish_response.proto
// version: 1.0.0
// guid: c8485218-1d5d-459f-89f3-5389ae0c4aab
// Response for batch publish operations

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/publish_result.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for batch publish operations
message BatchPublishResponse {
  // Results for each published message
  repeated PublishResult results = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of messages attempted
  int32 total_attempted = 2 [(buf.validate.field).int32.gte = 0];

  // Number of successful publishes
  int32 successful_count = 3 [(buf.validate.field).int32.gte = 0];

  // Number of failed publishes
  int32 failed_count = 4 [(buf.validate.field).int32.gte = 0];

  // Overall error message if any
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### batch_pull_request.proto {#batch_pull_request}

**Path**: `gcommon/v1/queue/batch_pull_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `BatchPullRequest`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/batch_pull_request.proto
// file: proto/gcommon/v1/queue/batch_pull_request.proto
// version: 1.0.0
// guid: 7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to pull multiple messages from a queue in a single operation.
 */
message BatchPullRequest {
  // Name of the queue to pull from
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Maximum number of messages to pull
  uint32 max_messages = 2;

  // Maximum time to wait for messages
  google.protobuf.Duration wait_timeout = 3;

  // Whether to acknowledge messages automatically
  bool auto_acknowledge = 4;

  // Consumer group ID (optional)
  string consumer_group = 5;

  // Subscription name (optional)
  string subscription = 6;

  // Maximum payload size in bytes
  uint64 max_payload_size = 7;
}
```

---

### batch_pull_response.proto {#batch_pull_response}

**Path**: `gcommon/v1/queue/batch_pull_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `BatchPullResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/batch_pull_response.proto
// file: proto/gcommon/v1/queue/batch_pull_response.proto
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-0a1b-2c3d-4e5f6a7b8c9d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for batch pull operations containing multiple messages.
 */
message BatchPullResponse {
  // List of messages pulled from the queue
  repeated QueueMessage messages = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of messages retrieved
  uint32 message_count = 2 [(buf.validate.field).uint32.gte = 0];

  // Whether more messages are available
  bool has_more = 3;

  // Next token for pagination
  string next_token = 4 [(buf.validate.field).string.min_len = 1];

  // Total bytes of message payloads
  uint64 total_bytes = 5 [(buf.validate.field).uint64.gte = 0];
}
```

---

### batch_settings.proto {#batch_settings}

**Path**: `gcommon/v1/queue/batch_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `BatchSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_settings.proto
// version: 1.0.0
// guid: 2fbffbe6-e92a-4e99-a5f4-b325fcd2e05b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message BatchSettings {
  // Enable batch publishing
  bool enabled = 1;

  // Maximum messages per batch
  int32 max_batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum batch size in bytes
  int64 max_batch_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum time to wait for batch completion (milliseconds)
  int32 batch_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Flush batch on publish request completion
  bool flush_on_complete = 5;
}
```

---

### commit_offset_request.proto {#commit_offset_request}

**Path**: `gcommon/v1/queue/commit_offset_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `CommitOffsetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/commit_offset_request.proto
// version: 1.0.0
// guid: dd17ade2-5399-4fe8-83ba-ffe1227da728
// CommitOffsetRequest records the latest processed offset for a
// consumer group. This allows the queue provider to resume message
// delivery from the correct position on reconnect.
// CommitOffsetRequest stores the offset a consumer has successfully
// processed within a queue or topic.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message CommitOffsetRequest {
  // Name of the queue or topic.
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Identifier for the consumer group.
  string consumer_group = 2;

  // Offset that was last processed successfully.
  int64 offset = 3;

  // Optional request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### commit_offset_response.proto {#commit_offset_response}

**Path**: `gcommon/v1/queue/commit_offset_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `CommitOffsetResponse`

**Imports** (4):

- `gcommon/v1/queue/partition_commit_result.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/commit_offset_response.proto
// version: 1.0.0
// guid: 748d3d88-f8aa-4f39-9a7a-5feb16d005d9

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/partition_commit_result.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message CommitOffsetResponse {
  // Overall success status
  bool success = 1;

  // Error message if commit failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 3 [(buf.validate.field).string.min_len = 1];

  // Results for each partition commit
  repeated PartitionCommitResult partition_results = 4 [(buf.validate.field).repeated.min_items = 1];

  // Total number of offsets committed
  int32 committed_count = 5 [(buf.validate.field).int32.gte = 0];

  // Total number of failed commits
  int32 failed_count = 6 [(buf.validate.field).int32.gte = 0];

  // Commit timestamp
  google.protobuf.Timestamp commit_timestamp = 7;

  // Consumer group generation at time of commit
  int64 consumer_generation = 8 [(buf.validate.field).int64.gte = 0];

  // Additional metadata about the commit operation
  map<string, string> metadata = 9;
}
```

---

### create_queue_request.proto {#create_queue_request}

**Path**: `gcommon/v1/queue/create_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `CreateQueueRequest`

**Imports** (4):

- `buf/validate/validate.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/create_queue_request.proto
// version: 1.1.0
// guid: c6d7e8f9-a0b1-2c3d-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.queue;

import "buf/validate/validate.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to create a new queue.
 * Defines the queue name and configuration parameters.
 */
message CreateQueueRequest {
  // Name of the queue to create (required) - alphanumeric with hyphens/underscores, 3-63 chars
  string queue_name = 1 [
    (buf.validate.field).required = true,
    (buf.validate.field).string.pattern = "^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$",
    (buf.validate.field).string.min_len = 3,
    (buf.validate.field).string.max_len = 63
  ];

  // Configuration for the new queue - required
  QueueConfig config = 2 [(buf.validate.field).required = true];

  // Whether to create the queue even if it already exists
  bool if_not_exists = 3;

  // Request metadata for tracing and correlation - required
  gcommon.v1.common.RequestMetadata metadata = 4 [(buf.validate.field).required = true];

  // Tags to associate with the queue - max 20 tags, each key/value max 100 chars
  map<string, string> tags = 5 [
    (buf.validate.field).map.max_pairs = 20,
    (buf.validate.field).map.keys.string.max_len = 100,
    (buf.validate.field).map.values.string.max_len = 100
  ];

  // Description of the queue - max 500 characters
  string description = 6 [(buf.validate.field).string.max_len = 500];
}
```

---

### create_queue_response.proto {#create_queue_response}

**Path**: `gcommon/v1/queue/create_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `CreateQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/create_queue_response.proto
// version: 1.0.0
// guid: 20edcd60-9765-404c-9193-f8b419e9af03
// Response for queue creation operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue creation operations
message CreateQueueResponse {
  // Whether the queue was successfully created
  bool success = 1;

  // Name of the created queue
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Queue endpoint URL
  string queue_endpoint = 3;

  // Number of partitions created
  int32 partition_count = 4;

  // Queue configuration that was applied
  map<string, string> applied_config = 5;

  // Error message if creation failed
  string error = 6;
}
```

---

### create_subscription_request.proto {#create_subscription_request}

**Path**: `gcommon/v1/queue/create_subscription_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `CreateSubscriptionRequest`

**Imports** (3):

- `gcommon/v1/queue/subscription_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/create_subscription_request.proto
// version: 1.0.0
// guid: 5b7ce7f0-2023-49f1-9801-b105699049ac
// Request to create a new subscription

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/subscription_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to create a new subscription
message CreateSubscriptionRequest {
  // Subscription name
  string subscription_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic to subscribe to
  string topic = 2;

  // Consumer group ID
  string consumer_group_id = 3;

  // Subscription configuration
  SubscriptionConfig config = 4;

  // Starting position (earliest, latest, or specific offset)
  string start_position = 5;

  // Specific offset (if start_position is "offset")
  int64 start_offset = 6;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 7;
}
```

---

### create_subscription_response.proto {#create_subscription_response}

**Path**: `gcommon/v1/queue/create_subscription_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `CreateSubscriptionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/create_subscription_response.proto
// file: proto/gcommon/v1/queue/create_subscription_response.proto
// version: 1.0.0
// guid: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for creating a subscription.
 */
message CreateSubscriptionResponse {
  // Whether the subscription was created successfully
  bool success = 1;

  // Error message if creation failed
  string error_message = 2;

  // ID of the created subscription
  string subscription_id = 3;

  // Name of the created subscription
  string subscription_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Timestamp when subscription was created
  uint64 created_at = 5;

  // Initial position in the queue
  uint64 initial_position = 6;
}
```

---

### create_topic_request.proto {#create_topic_request}

**Path**: `gcommon/v1/queue/create_topic_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `CreateTopicRequest`

**Imports** (3):

- `gcommon/v1/queue/topic_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/create_topic_request.proto
// file: proto/gcommon/v1/queue/create_topic_request.proto
// version: 1.0.0
// guid: 3f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/topic_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to create a new topic.
 */
message CreateTopicRequest {
  // Name of the topic to create
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Configuration for the topic
  TopicConfig config = 2;

  // Whether the topic should be durable
  bool durable = 3;

  // Whether to auto-delete when unused
  bool auto_delete = 4;

  // Optional arguments for topic creation
  map<string, string> arguments = 5;
}
```

---

### create_topic_response.proto {#create_topic_response}

**Path**: `gcommon/v1/queue/create_topic_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `CreateTopicResponse`

**Imports** (5):

- `gcommon/v1/queue/topic_config.proto`
- `gcommon/v1/queue/topic_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/create_topic_response.proto
// file: proto/gcommon/v1/queue/create_topic_response.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/topic_config.proto";
import "gcommon/v1/queue/topic_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for topic creation operations.
 */
message CreateTopicResponse {
  // Information about the created topic
  TopicInfo topic_info = 1;

  // Whether the topic was actually created (false if it already existed)
  bool created = 2;

  // Timestamp when the topic was created
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

  // Any warnings during topic creation
  repeated string warnings = 4;

  // Topic configuration that was applied
  TopicConfig applied_config = 5;
}
// This file needs proper implementation
```

---

### delete_criteria.proto {#delete_criteria}

**Path**: `gcommon/v1/queue/delete_criteria.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `DeleteCriteria`

**Imports** (3):

- `gcommon/v1/common/message_state.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_criteria.proto
// version: 1.0.0
// guid: 351be276-91ef-4408-9e3d-1931faddc070

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/message_state.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeleteCriteria {
  // Delete messages older than this timestamp
  int64 older_than_timestamp = 1;

  // Delete messages with specific headers
  map<string, string> header_filters = 2;

  // Delete messages with specific priority
  int32 priority = 3 [(buf.validate.field).int32.gte = 0];

  // Delete messages with specific correlation ID
  string correlation_id = 4 [(buf.validate.field).string.min_len = 1];

  // Maximum number of messages to delete
  int32 max_messages = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Delete messages in specific state
  gcommon.v1.common.MessageState state = 6;
}
```

---

### delete_queue_request.proto {#delete_queue_request}

**Path**: `gcommon/v1/queue/delete_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `DeleteQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/delete_queue_request.proto
// file: proto/gcommon/v1/queue/delete_queue_request.proto
// version: 1.0.0
// guid: 9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeleteQueueRequest {
  // Queue ID or name to delete
  string queue = 1 [(buf.validate.field).string.min_len = 1];

  // Force deletion even if not empty
  bool force = 2;

  // Purge messages before deletion
  bool purge_first = 3;
}

/**
 * Request to delete a queue and all its messages.
 * This is a destructive operation that cannot be undone.
 */
// This file needs proper implementation
```

---

### delete_queue_response.proto {#delete_queue_response}

**Path**: `gcommon/v1/queue/delete_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `DeleteQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_queue_response.proto
// version: 1.0.0
// guid: 0c0494d6-bfac-476c-a900-f79b5c260fd0
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for deleting a queue.
 * Confirms successful deletion and provides cleanup information.
 */
message DeleteQueueResponse {
  // Whether the queue was successfully deleted
  bool success = 1;

  // Number of messages that were purged during deletion
  int64 purged_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Human-readable message describing the deletion result
  string message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_request.proto {#delete_request}

**Path**: `gcommon/v1/queue/delete_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `QueueDeleteRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/delete_criteria.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_request.proto
// version: 1.0.0
// guid: 6b38ff92-a226-4afc-9a2e-4f1f47ab36a2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/delete_criteria.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueDeleteRequest {
  // Name of the queue containing the message
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Unique identifier of the message to delete
  string message_id = 2;

  // Acknowledgment token (if message was previously consumed)
  string ack_token = 3;

  // Whether to force deletion even if message is locked
  bool force = 4;

  // Reason for deletion
  string reason = 5;

  // Delete criteria (alternative to message_id)
  DeleteCriteria criteria = 6;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
```

---

### delete_response.proto {#delete_response}

**Path**: `gcommon/v1/queue/delete_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `QueueDeleteResponse`

**Imports** (5):

- `gcommon/v1/queue/backup_info.proto`
- `gcommon/v1/queue/deletion_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_response.proto
// version: 1.0.0
// guid: 9de9c1b0-9bc8-44a6-af2b-133a1f578373

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/backup_info.proto";
import "gcommon/v1/queue/deletion_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueDeleteResponse {
  // Success status of the delete operation
  bool success = 1;

  // Identifier of the deleted resource
  string deleted_resource_id = 2 [(buf.validate.field).string.min_len = 1];

  // Type of resource that was deleted
  string resource_type = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when deletion completed
  google.protobuf.Timestamp deleted_at = 4;

  // Error message if deletion failed
  string error_message = 5 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 6 [(buf.validate.field).string.min_len = 1];

  // Statistics about the deletion
  DeletionStats deletion_stats = 7;

  // Backup information (if backup was created)
  QueueBackupInfo backup_info = 8;

  // Warning messages
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Operation metadata
  map<string, string> metadata = 10;
}
```

---

### delete_subscription_request.proto {#delete_subscription_request}

**Path**: `gcommon/v1/queue/delete_subscription_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `DeleteSubscriptionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_subscription_request.proto
// version: 1.0.0
// guid: 6b8bf50f-c08d-4ad7-abec-06504c697d42
// Request to delete a subscription

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to delete a subscription
message DeleteSubscriptionRequest {
  // Subscription ID to delete
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Force deletion even if active
  bool force = 2;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 3 [(buf.validate.field).int32.gt = 0];
}
```

---

### delete_subscription_response.proto {#delete_subscription_response}

**Path**: `gcommon/v1/queue/delete_subscription_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `DeleteSubscriptionResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_subscription_response.proto
// version: 1.0.0
// guid: f0abf288-da03-42ac-8fb3-9640ebce6528
// Response for delete subscription operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for deleting a subscription
message DeleteSubscriptionResponse {
  // Whether the subscription was successfully deleted
  bool success = 1;

  // Number of undelivered messages that were purged
  int64 purged_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Human-readable message describing the deletion result
  string message = 3 [(buf.validate.field).string.min_len = 1];

  // Error message if deletion failed
  string error = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### delete_topic_request.proto {#delete_topic_request}

**Path**: `gcommon/v1/queue/delete_topic_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `DeleteTopicRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_topic_request.proto
// version: 1.1.0
// guid: 2f1d966a-514b-46ca-b291-17db26ec7f72
// Request to delete a topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeleteTopicRequest {
  // Topic ID or name to delete
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Force deletion even if not empty
  bool force = 2;
}

// DeleteTopicRequest removes a topic and its associated resources
// This file needs proper implementation
```

---

### delete_topic_response.proto {#delete_topic_response}

**Path**: `gcommon/v1/queue/delete_topic_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `DeleteTopicResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delete_topic_response.proto
// version: 1.0.0
// guid: 321c289e-7bff-430d-b737-60c42c418beb
// Response for topic deletion operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for deleting a topic
message DeleteTopicResponse {
  // Whether the topic was successfully deleted
  bool success = 1;

  // Number of active subscriptions that were also deleted
  int64 deleted_subscriptions = 2 [(buf.validate.field).int64.gte = 0];

  // Number of messages that were purged during deletion
  int64 purged_messages = 3 [(buf.validate.field).int64.gte = 0];

  // Human-readable message describing the deletion result
  string message = 4 [(buf.validate.field).string.min_len = 1];

  // Error message if deletion failed
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### dequeue_request.proto {#dequeue_request}

**Path**: `gcommon/v1/queue/dequeue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 113

**Messages** (1): `DequeueRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/dequeue_request.proto
// version: 1.0.0
// guid: ce6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * DequeueRequest retrieves one or more messages from a queue.
 * Supports various consumption patterns including polling,
 * long polling, and batch operations.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message DequeueRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue to receive messages from.
   * Must be a valid existing queue.
   */
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Maximum number of messages to receive in this request.
   * Range: 1-100. Default: 1.
   */
  int32 max_messages = 12;

  /**
   * Visibility timeout - how long the message is hidden from
   * other consumers after being received. Must be acknowledged
   * or rejected within this time. Default: queue configuration.
   */
  google.protobuf.Duration visibility_timeout = 13;

  /**
   * Wait time for long polling. If no messages are available,
   * the request will wait up to this duration for messages
   * to arrive. Set to 0 for immediate return.
   */
  google.protobuf.Duration wait_time = 14;

  /**
   * Message group ID filter. If specified, only messages
   * from this group will be returned. Useful for ordered processing.
   */
  string group_id_filter = 15;

  /**
   * Attribute filters for selective message consumption.
   * Only messages matching all specified attributes will be returned.
   */
  map<string, string> attribute_filters = 16;

  /**
   * Message type filter. If specified, only messages of
   * this type will be returned.
   */
  string message_type_filter = 17;

  /**
   * Consumer ID for tracking and load balancing.
   * Helps with consumer group coordination and metrics.
   */
  string consumer_id = 18;

  /**
   * Include message attributes in the response.
   * Default: true. Set to false to reduce response size.
   */
  bool include_attributes = 19;

  /**
   * Include message metadata (timestamps, delivery count, etc.)
   * in the response. Default: true.
   */
  bool include_metadata = 20;

  /**
   * Peek mode - return messages without removing them from
   * the queue. Useful for inspection. Default: false.
   */
  bool peek_only = 21;

  /**
   * Priority threshold - only return messages with priority
   * greater than or equal to this value. Range: 0-255.
   */
  int32 min_priority = 22;
}
```

---

### dequeue_response.proto {#dequeue_response}

**Path**: `gcommon/v1/queue/dequeue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 115

**Messages** (1): `DequeueResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/dequeue_response.proto
// version: 1.0.0
// guid: ea8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

// Queue message types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * DequeueResponse returns messages retrieved from a queue.
 * Contains message data, delivery metadata, and operation status
 * for consumption and acknowledgment processing.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message DequeueResponse {
  // Required fields (1-10)

  /**
   * Messages retrieved from the queue.
   * Empty if no messages were available.
   */
  repeated QueueMessage messages = 1;

  /**
   * Indicates whether the dequeue operation was successful.
   */
  bool success = 2;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue messages were retrieved from.
   * Echoed from the request for verification.
   */
  string queue_name = 12 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * Number of messages that were available but not returned
   * due to max_messages limit.
   */
  int32 messages_remaining = 13;

  /**
   * Approximate number of messages currently in the queue.
   * Useful for monitoring and capacity planning.
   */
  int64 approximate_queue_size = 14;

  /**
   * Consumer ID that was used for this request.
   * Helpful for debugging and load balancing.
   */
  string consumer_id = 15;

  /**
   * Time the request waited for messages (for long polling).
   * Useful for performance monitoring.
   */
  google.protobuf.Timestamp wait_started_at = 16;

  /**
   * Duration the request waited for messages.
   */
  int64 wait_duration_ms = 17;

  /**
   * Indicates if the response was due to wait timeout
   * rather than message availability.
   */
  bool timed_out = 18;

  // Status and error fields (61-70)

  /**
   * Error information if the dequeue operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the dequeue operation started.
   */
  google.protobuf.Timestamp operation_started_at = 51;

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}
```

---

### enqueue_request.proto {#enqueue_request}

**Path**: `gcommon/v1/queue/enqueue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 126

**Messages** (1): `EnqueueRequest`

**Imports** (6):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/enqueue_request.proto
// version: 1.0.0
// guid: bd5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * EnqueueRequest adds a message to a queue.
 * Supports both simple message enqueuing and advanced features
 * like scheduling, priority, and message grouping.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message EnqueueRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue to send the message to.
   * Must be a valid queue that exists or will be created.
   */
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * The message payload. Can contain any data type.
   * The receiving application is responsible for deserializing.
   */
  google.protobuf.Any payload = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Message priority (0-255, where 255 is highest priority).
   * Higher priority messages are delivered first. Default: 128.
   */
  int32 priority = 12;

  /**
   * Delay before the message becomes available for consumption.
   * Use for scheduled message delivery.
   */
  google.protobuf.Duration delay = 13;

  /**
   * Message expiration time. Message will be removed if not
   * consumed before this time. If not set, uses queue default.
   */
  google.protobuf.Timestamp expires_at = 14;

  /**
   * Message group ID for ordered processing. Messages with
   * the same group_id are processed in FIFO order.
   */
  string group_id = 15;

  /**
   * Deduplication ID to prevent duplicate message processing.
   * If a message with the same dedup_id is already in the queue,
   * this request will be ignored.
   */
  string deduplication_id = 16;

  /**
   * Maximum number of delivery attempts before the message
   * is moved to dead letter queue. Default: queue configuration.
   */
  int32 max_delivery_attempts = 17;

  /**
   * Custom attributes/headers for the message.
   * Can be used for routing, filtering, or application-specific metadata.
   */
  map<string, string> attributes = 18;

  /**
   * Content type of the payload (e.g., "application/json", "text/plain").
   * Helps consumers understand how to process the message.
   */
  string content_type = 19;

  /**
   * Message source identifier. Useful for tracking which
   * application or service generated the message.
   */
  string source = 20;

  /**
   * Message type/event name. Helps consumers route messages
   * to appropriate handlers.
   */
  string message_type = 21;

  /**
   * Correlation ID for linking related messages across
   * different queues or processing stages.
   */
  string correlation_id = 22;

  /**
   * Reply-to queue name for request-response patterns.
   * If set, response should be sent to this queue.
   */
  string reply_to = 23;
}
```

---

### enqueue_response.proto {#enqueue_response}

**Path**: `gcommon/v1/queue/enqueue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 128

**Messages** (1): `EnqueueResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/enqueue_response.proto
// version: 1.0.0
// guid: df7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * EnqueueResponse confirms successful message enqueuing.
 * Returns message identifiers and metadata for tracking
 * and potential message management operations.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message EnqueueResponse {
  // Required fields (1-10)

  /**
   * Unique identifier assigned to the enqueued message.
   * Can be used for message tracking, cancellation, or status queries.
   */
  string message_id = 1;

  /**
   * Indicates whether the message was successfully enqueued.
   * True if the message is now in the queue and will be processed.
   */
  bool success = 2;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue where the message was enqueued.
   * Echoed from the request for verification.
   */
  string queue_name = 12 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * MD5 hash of the message payload for integrity verification.
   * Can be used to detect corruption during transmission.
   */
  string payload_md5 = 13;

  /**
   * Size of the enqueued message in bytes.
   * Useful for monitoring and capacity planning.
   */
  int64 message_size = 14;

  /**
   * Position/sequence number of the message in the queue.
   * Useful for ordered queues and processing metrics.
   */
  int64 sequence_number = 15;

  /**
   * Assigned priority of the message (may differ from requested
   * priority due to queue configuration or policy).
   */
  int32 assigned_priority = 16;

  /**
   * Deduplication ID that was used (if any).
   * Helps track duplicate detection results.
   */
  string deduplication_id = 17;

  /**
   * Message group ID that was assigned (if any).
   * Important for ordered processing verification.
   */
  string group_id = 18;

  /**
   * Estimated time when the message will become available
   * for consumption (considering delays).
   */
  google.protobuf.Timestamp available_at = 19;

  /**
   * Message expiration time as stored in the queue.
   * May differ from requested expiration due to queue policies.
   */
  google.protobuf.Timestamp expires_at = 20;

  // Status and error fields (61-70)

  /**
   * Error information if the enqueue operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the message was enqueued.
   * Precise timing for SLA and performance monitoring.
   */
  google.protobuf.Timestamp enqueued_at = 51;

  /**
   * Timestamp when this response was generated.
   * Useful for measuring request processing time.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}
```

---

### export_queue_request.proto {#export_queue_request}

**Path**: `gcommon/v1/queue/export_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `ExportQueueRequest`

**Imports** (4):

- `gcommon/v1/common/queue_export_format.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/export_queue_request.proto
// file: proto/gcommon/v1/queue/export_queue_request.proto
// version: 1.0.0
// guid: 4a3b2c1d-0e9f-8a7b-6c5d-4e3f2a1b0c9d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/queue_export_format.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to export queue data for backup or migration purposes.
 */
message ExportQueueRequest {
  // Name of the queue to export
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Export destination (file path, cloud storage URI, etc.)
  string destination = 2;

  // Export format
  gcommon.v1.common.QueueExportFormat format = 3;

  // Whether to include message data or just metadata
  bool include_message_data = 4;

  // Time range for filtering exported data
  // If not specified, exports all available data
  gcommon.v1.common.TimeRangeMetrics time_range = 5;

  // Whether to compress the export
  bool compress = 6;

  // Maximum number of messages to export (0 = no limit)
  int64 max_messages = 7;

  // Export configuration options
  map<string, string> options = 8;
}
// This file needs proper implementation
```

---

### export_queue_response.proto {#export_queue_response}

**Path**: `gcommon/v1/queue/export_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `ExportQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/export_queue_response.proto
// version: 1.0.0
// guid: 16445ad6-52b3-4890-bf35-31e17a689135
// Response for queue export operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue export operations
message ExportQueueResponse {
  // Export job ID
  string export_id = 1 [(buf.validate.field).string.min_len = 1];

  // Export status
  string status = 2 [(buf.validate.field).string.min_len = 1];

  // File path or URL where export is stored
  string export_path = 3 [(buf.validate.field).string.min_len = 1];

  // Number of messages exported
  int64 message_count = 4 [(buf.validate.field).int64.gte = 0];

  // Size of exported data in bytes
  int64 data_size_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Export format (JSON, CSV, etc.)
  string format = 6 [(buf.validate.field).string.min_len = 1];

  // Start timestamp of exported data
  int64 start_timestamp = 7;

  // End timestamp of exported data
  int64 end_timestamp = 8;

  // Error message if export failed
  string error = 9 [(buf.validate.field).string.min_len = 1];
}
```

---

### flush_queue_request.proto {#flush_queue_request}

**Path**: `gcommon/v1/queue/flush_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `FlushQueueRequest`

**Imports** (4):

- `gcommon/v1/common/flush_policy.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flush_queue_request.proto
// version: 1.1.0
// guid: 7ddb0fbd-7f80-45ed-9a91-db95b2111a42
// Request to flush queue messages to persistent storage

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/flush_policy.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// FlushQueueRequest forces queue messages to be flushed to persistent storage
message FlushQueueRequest {
  // Queue identifier to flush
  string queue_id = 1 [(buf.validate.field).string.min_len = 1];

  // Flush policy to apply
  gcommon.v1.common.FlushPolicy flush_policy = 2;

  // Wait for flush completion before returning
  bool wait_for_completion = 3;

  // Maximum time to wait for flush completion (milliseconds)
  int32 timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Flush only messages up to this timestamp
  google.protobuf.Timestamp flush_until = 5;

  // Include specific partitions only (empty = all partitions)
  repeated int32 partition_ids = 6 [(buf.validate.field).repeated.min_items = 1];

  // Force flush even if not needed
  bool force_flush = 7;

  // Optional metadata for the flush operation
  map<string, string> metadata = 8;
}
```

---

### flush_queue_response.proto {#flush_queue_response}

**Path**: `gcommon/v1/queue/flush_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `FlushQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flush_queue_response.proto
// version: 1.0.0
// guid: b7bddce0-67bc-4158-a9b7-c3e15f1606fe
// Response for queue flush operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue flush operations
message FlushQueueResponse {
  // Whether the flush was successful
  bool success = 1;

  // Number of messages flushed
  int64 messages_flushed = 2 [(buf.validate.field).int64.gte = 0];

  // Bytes flushed from queue
  int64 bytes_flushed = 3 [(buf.validate.field).int64.gte = 0];

  // Time taken for flush operation (milliseconds)
  int32 flush_duration_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Error message if flush failed
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_cluster_info_request.proto {#get_cluster_info_request}

**Path**: `gcommon/v1/queue/get_cluster_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `GetClusterInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_cluster_info_request.proto
// version: 1.0.0
// guid: 796bd8f4-f731-447d-9cf7-e1b29047192f
// Request to get cluster information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to get cluster information
message GetClusterInfoRequest {
  // Include node details
  bool include_nodes = 1;

  // Include performance metrics
  bool include_metrics = 2;

  // Include health status
  bool include_health = 3;

  // Include resource usage
  bool include_resources = 4;

  // Include topology information
  bool include_topology = 5;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 6 [(buf.validate.field).int32.gt = 0];
}
```

---

### get_cluster_info_response.proto {#get_cluster_info_response}

**Path**: `gcommon/v1/queue/get_cluster_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `GetClusterInfoResponse`

**Imports** (4):

- `gcommon/v1/queue/cluster_info.proto`
- `gcommon/v1/queue/node_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/get_cluster_info_response.proto
// file: proto/gcommon/v1/queue/get_cluster_info_response.proto
// version: 1.0.0
// guid: 3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/cluster_info.proto";
import "gcommon/v1/queue/node_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response containing cluster information.
 */
message GetClusterInfoResponse {
  // Detailed cluster information
  ClusterInfo cluster_info = 1;

  // Node information
  repeated NodeInfo nodes = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether the cluster is currently healthy
  bool is_healthy = 3;

  // Any warnings or issues with the cluster
  repeated string warnings = 4 [(buf.validate.field).repeated.min_items = 1];

  // Error message if failed to get info
  string error_message = 5 [(buf.validate.field).string.min_len = 1];
}
// This file needs proper implementation
```

---

### get_message_request.proto {#get_message_request}

**Path**: `gcommon/v1/queue/get_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `GetMessageRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_message_request.proto
// version: 1.0.0
// guid: eac57fd6-c5de-4130-9724-13f89a0f623f
// Request to get a specific message

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to get a specific message
message GetMessageRequest {
  // Topic name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Message ID to retrieve
  string message_id = 2 [(buf.validate.field).string.min_len = 1];

  // Partition ID (optional)
  int32 partition_id = 3 [(buf.validate.field).int32.gte = 0];

  // Offset within partition (optional)
  int64 offset = 4 [(buf.validate.field).int64.gte = 0];

  // Include message metadata
  bool include_metadata = 5;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 6 [(buf.validate.field).int32.gt = 0];
}
```

---

### get_message_response.proto {#get_message_response}

**Path**: `gcommon/v1/queue/get_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `GetMessageResponse`

**Imports** (3):

- `gcommon/v1/queue/message_envelope.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/get_message_response.proto
// file: proto/gcommon/v1/queue/get_message_response.proto
// version: 1.0.0
// guid: 8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/message_envelope.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response containing a message retrieved from a queue.
 */
message GetMessageResponse {
  // The retrieved message (null if no message available)
  MessageEnvelope message = 1;

  // Acknowledgment token for this message (used to ack/nack)
  string ack_token = 2 [(buf.validate.field).string.min_len = 1];

  // Whether more messages are available in the queue
  bool has_more = 3;

  // Position/offset of this message in the queue
  int64 message_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Queue depth at the time of retrieval
  int64 queue_depth = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### get_node_info_request.proto {#get_node_info_request}

**Path**: `gcommon/v1/queue/get_node_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `GetNodeInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_node_info_request.proto
// version: 1.0.0
// guid: 929d869b-d6be-4182-8711-293847f5ba56
// Request to get node information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to get node information
message GetNodeInfoRequest {
  // Node ID to get info for (optional, defaults to current node)
  string node_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include performance metrics
  bool include_metrics = 2;

  // Include health status
  bool include_health = 3;

  // Include resource usage
  bool include_resources = 4;

  // Include network topology
  bool include_topology = 5;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 6 [(buf.validate.field).int32.gt = 0];
}
```

---

### get_node_info_response.proto {#get_node_info_response}

**Path**: `gcommon/v1/queue/get_node_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `GetNodeInfoResponse`

**Imports** (3):

- `gcommon/v1/queue/node_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_node_info_response.proto
// version: 1.0.0
// guid: fb3ad530-511f-4fec-9508-7ae00be0ee92
// Response with node information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/node_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response with node information
message GetNodeInfoResponse {
  // Node information
  NodeInfo node_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_offset_request.proto {#get_offset_request}

**Path**: `gcommon/v1/queue/get_offset_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `GetOffsetRequest`

**Imports** (4):

- `gcommon/v1/common/offset_type.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_offset_request.proto
// version: 1.1.0
// guid: d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/offset_type.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to get the current offset for a consumer or partition.
 * Used for tracking message consumption progress.
 */
message GetOffsetRequest {
  // Queue or topic name
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Partition ID (for partitioned queues)
  int32 partition_id = 2;

  // Consumer group ID (optional)
  string consumer_group = 3;

  // Consumer ID within the group (optional)
  string consumer_id = 4;

  // Type of offset to retrieve
  gcommon.v1.common.OffsetType offset_type = 5;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 6;
}
```

---

### get_offset_response.proto {#get_offset_response}

**Path**: `gcommon/v1/queue/get_offset_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `GetOffsetResponse`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_offset_response.proto
// version: 1.0.0
// guid: 28ce7fa9-da40-4119-8167-285e4ff6179a
// GetOffsetResponse returns the current committed offset for a
// consumer group within a queue or topic.
// GetOffsetResponse provides offset information for a consumer group.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetOffsetResponse {
  // The currently committed offset.
  int64 offset = 1;

  // Name of the queue or topic.
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional request metadata.
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### get_partition_info_request.proto {#get_partition_info_request}

**Path**: `gcommon/v1/queue/get_partition_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 50

**Messages** (1): `GetPartitionInfoRequest`

**Imports** (3):

- `gcommon/v1/queue/time_range_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_partition_info_request.proto
// version: 1.1.0
// guid: 7478ffad-9bff-42f2-b8c9-cd583c1adcea
// Request to get partition information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/time_range_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// GetPartitionInfoRequest retrieves information about topic partitions
message GetPartitionInfoRequest {
  // Topic identifier
  string topic_id = 1 [(buf.validate.field).string.min_len = 1];

  // Specific partition IDs (empty = all partitions)
  repeated int32 partition_ids = 2 [(buf.validate.field).repeated.min_items = 1];

  // Include partition statistics
  bool include_stats = 3;

  // Include consumer information
  bool include_consumers = 4;

  // Include offset information
  bool include_offsets = 5;

  // Include partition health status
  bool include_health_status = 6;

  // Include leader/replica information
  bool include_leader_info = 7;

  // Include partition configuration
  bool include_config = 8;

  // Time range for historical statistics - references existing TimeRangeFilter from get_queue_info_request.proto
  TimeRangeFilter time_range = 9;

  // Access control context
  string access_token = 10 [(buf.validate.field).string.min_len = 1];
}
// This file needs proper implementation
```

---

### get_partition_info_response.proto {#get_partition_info_response}

**Path**: `gcommon/v1/queue/get_partition_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `GetPartitionInfoResponse`

**Imports** (3):

- `gcommon/v1/queue/partition_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_partition_info_response.proto
// version: 1.0.0
// guid: 414613a0-0192-43b0-9f7f-347bd35d0bfc
// Response with partition information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/partition_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response with partition information
message GetPartitionInfoResponse {
  // Partition information
  PartitionInfo partition_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_queue_health_request.proto {#get_queue_health_request}

**Path**: `gcommon/v1/queue/get_queue_health_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `GetQueueHealthRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_health_request.proto
// version: 1.0.0
// guid: 9862f197-381f-41d3-a980-953ef636c78d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueHealthRequest {
  // Specific queue names to check (empty = all queues)
  repeated string queue_names = 1 [(buf.validate.field).repeated.min_items = 1];

  // Whether to include detailed health metrics
  bool include_details = 2;
}
```

---

### get_queue_health_response.proto {#get_queue_health_response}

**Path**: `gcommon/v1/queue/get_queue_health_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `GetQueueHealthResponse`

**Imports** (4):

- `gcommon/v1/queue/cluster_health.proto`
- `gcommon/v1/queue/queue_health.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_health_response.proto
// version: 1.0.0
// guid: ca800078-3add-48f9-9559-c95d23232cea

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/cluster_health.proto";
import "gcommon/v1/queue/queue_health.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueHealthResponse {
  // Health status for each queue
  repeated QueueHealth queue_health = 1 [(buf.validate.field).repeated.min_items = 1];

  // Overall cluster health
  ClusterHealth cluster_health = 2;
}
```

---

### get_queue_info_request.proto {#get_queue_info_request}

**Path**: `gcommon/v1/queue/get_queue_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 50

**Messages** (1): `GetQueueInfoRequest`

**Imports** (3):

- `gcommon/v1/queue/time_range_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_info_request.proto
// version: 1.0.0
// guid: 9c3c8693-8a62-4458-86af-19a28b6b250a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/time_range_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueInfoRequest {
  // Queue identifier
  string queue_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include queue statistics in response
  bool include_stats = 2;

  // Include queue configuration in response
  bool include_config = 3;

  // Include partition information
  bool include_partitions = 4;

  // Include consumer group information
  bool include_consumer_groups = 5;

  // Include current subscriptions
  bool include_subscriptions = 6;

  // Include topic binding information
  bool include_bindings = 7;

  // Include recent error information
  bool include_errors = 8;

  // Time range for statistics (if not specified, returns current state)
  TimeRangeFilter time_range = 9;

  // Specific information sections to retrieve
  repeated string info_sections = 10 [(buf.validate.field).repeated.min_items = 1];

  // Access control context
  string access_token = 11 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_queue_info_response.proto {#get_queue_info_response}

**Path**: `gcommon/v1/queue/get_queue_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `GetQueueInfoResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_info_response.proto
// version: 1.0.0
// guid: 06258d4a-8574-4cd1-977b-59927a7ad597
// Response with queue information

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response with queue information
message GetQueueInfoResponse {
  // Queue information
  QueueInfo queue_info = 1;

  // Whether request was successful
  bool success = 2;

  // Error message if request failed
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_queue_stats_request.proto {#get_queue_stats_request}

**Path**: `gcommon/v1/queue/get_queue_stats_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `GetQueueStatsRequest`

**Imports** (4):

- `gcommon/v1/common/stats_granularity.proto`
- `gcommon/v1/common/time_range_metrics.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_stats_request.proto
// version: 1.0.0
// guid: 7dc18176-1123-444f-8040-b7e352b501d6

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/stats_granularity.proto";
import "gcommon/v1/common/time_range_metrics.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueStatsRequest {
  // Name of the queue
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Time range for statistics
  gcommon.v1.common.TimeRangeMetrics time_range = 2;

  // Granularity of statistics (hourly, daily, etc.)
  gcommon.v1.common.StatsGranularity granularity = 3;
}
```

---

### get_queue_stats_response.proto {#get_queue_stats_response}

**Path**: `gcommon/v1/queue/get_queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `GetQueueStatsResponse`

**Imports** (10):

- `gcommon/v1/common/metrics_error_stats.proto`
- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/consumer_stats.proto`
- `gcommon/v1/queue/historical_stats.proto`
- `gcommon/v1/queue/performance_metrics.proto`
- `gcommon/v1/queue/queue_stats.proto`
- `gcommon/v1/queue/queue_stats_summary.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_queue_stats_response.proto
// version: 1.0.0
// guid: 7014296b-b332-416c-9de8-7d0fd264251c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_error_stats.proto";
import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/consumer_stats.proto";
import "gcommon/v1/queue/historical_stats.proto";
import "gcommon/v1/queue/performance_metrics.proto";
import "gcommon/v1/queue/queue_stats.proto";
import "gcommon/v1/queue/queue_stats_summary.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetQueueStatsResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Overall statistics summary
  QueueStatsSummary summary = 2;

  // Per-queue statistics (if multiple queues requested)
  repeated QueueStats queue_stats = 3 [(buf.validate.field).repeated.min_items = 1];

  // Consumer statistics (if requested)
  repeated ConsumerStats consumer_stats = 4 [(buf.validate.field).repeated.min_items = 1];

  // Historical statistics (if requested)
  HistoricalStats historical_stats = 5;

  // Error statistics (if requested)
  gcommon.v1.common.MetricsErrorStats error_stats = 6;

  // Performance metrics
  PerformanceMetrics performance_metrics = 7;

  // Timestamp when these statistics were generated
  google.protobuf.Timestamp generated_at = 8;
}
```

---

### get_subscription_info_request.proto {#get_subscription_info_request}

**Path**: `gcommon/v1/queue/get_subscription_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `GetSubscriptionInfoRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_subscription_info_request.proto
// version: 1.0.0
// guid: 560f1d95-f68d-41e7-821f-fbb741872dc8
// Request to get subscription information

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to get subscription information
message GetSubscriptionInfoRequest {
  // Subscription ID to get info for
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include detailed metrics
  bool include_metrics = 2;

  // Include consumer group details
  bool include_consumer_details = 3;

  // Include partition assignments
  bool include_partitions = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### get_subscription_info_response.proto {#get_subscription_info_response}

**Path**: `gcommon/v1/queue/get_subscription_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 67

**Messages** (1): `GetSubscriptionInfoResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/get_subscription_info_response.proto
// file: proto/gcommon/v1/queue/get_subscription_info_response.proto
// version: 1.0.0
// guid: 3f2e1d0c-9b8a-7f6e-5d4c-3b2a1f0e9d8c
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response message for subscription information retrieval.
 */
message GetSubscriptionInfoResponse {
  // Unique identifier for the subscription
  string subscription_id = 1;

  // Name of the subscription
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic this subscription is bound to
  string topic_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current state of the subscription
  string state = 4;

  // Consumer group associated with this subscription
  string consumer_group = 5;

  // Current message offset position
  uint64 current_offset = 6;

  // Latest available message offset
  uint64 latest_offset = 7;

  // Number of unacknowledged messages
  uint64 unacked_count = 8;

  // Subscription creation timestamp
  google.protobuf.Timestamp created_at = 9 [ (buf.validate.field).required = true ];

  // Last activity timestamp
  google.protobuf.Timestamp last_activity = 10;

  // Number of active consumers
  uint32 active_consumers = 11;

  // Total messages consumed
  uint64 total_consumed = 12;

  // Message consumption rate (messages per second)
  double consumption_rate = 13;
}
```

---

### get_topic_info_request.proto {#get_topic_info_request}

**Path**: `gcommon/v1/queue/get_topic_info_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `GetTopicInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_topic_info_request.proto
// version: 1.0.0
// guid: f3a4b5c6-d7e8-9f0a-1b2c-3d4e5f6a7b8c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to get information about a topic.
 * Used for retrieving topic metadata and configuration.
 */
message GetTopicInfoRequest {
  // Name of the topic to get information for
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether to include detailed statistics
  bool include_stats = 2;

  // Whether to include partition information
  bool include_partitions = 3;

  // Whether to include consumer group information
  bool include_consumer_groups = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### get_topic_info_response.proto {#get_topic_info_response}

**Path**: `gcommon/v1/queue/get_topic_info_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 67

**Messages** (1): `GetTopicInfoResponse`

**Imports** (9):

- `gcommon/v1/common/metrics_retention_info.proto`
- `gcommon/v1/queue/owner_info.proto`
- `gcommon/v1/queue/partition_info.proto`
- `gcommon/v1/queue/topic_configuration.proto`
- `gcommon/v1/queue/topic_permissions.proto`
- `gcommon/v1/queue/topic_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/get_topic_info_response.proto
// version: 1.0.0
// guid: 1a5f0bc1-5c84-4d82-9730-028810eadf04

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_retention_info.proto";
import "gcommon/v1/queue/owner_info.proto";
import "gcommon/v1/queue/partition_info.proto";
import "gcommon/v1/queue/topic_configuration.proto";
import "gcommon/v1/queue/topic_permissions.proto";
import "gcommon/v1/queue/topic_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GetTopicInfoResponse {
  // Topic identifier
  string topic_id = 1;

  // Topic name
  string topic_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Topic creation timestamp
  google.protobuf.Timestamp created_at = 4 [ (buf.validate.field).required = true ];

  // Last modification timestamp
  google.protobuf.Timestamp updated_at = 5;

  // Topic statistics
  TopicStats stats = 6;

  // Partition information
  repeated PartitionInfo partitions = 7;

  // Topic configuration
  TopicConfiguration config = 8;

  // Topic state (active, paused, deleted)
  string state = 9;

  // Access permissions for the requesting user
  TopicPermissions permissions = 10;

  // Topic metadata
  map<string, string> metadata = 11;

  // Topic tags for categorization
  repeated string tags = 12;

  // Owner information
  OwnerInfo owner = 13;

  // Retention policy for messages in this topic
  gcommon.v1.common.MetricsRetentionInfo retention = 14;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/queue/health_check_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `QueueHealthCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/health_check_request.proto
// version: 1.0.0
// guid: e9e95e53-7d2b-4dbf-896d-e9dea8853bd0
//
// HealthCheckRequest for the queue module

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueHealthCheckRequest {
  // Name of the queue to check.
  string queue = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing.
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/queue/health_check_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `QueueHealthCheckResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/health_check_response.proto
// version: 1.0.1
// guid: 24f4fcb1-f84d-4f02-845d-01b9759bfb6a
//
// HealthCheckResponse for the queue module
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * HealthCheckResponse returns queue service health status.
 */
message QueueHealthCheckResponse {
  // Overall queue service health.
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Whether the queue connection is operational.
  bool connection_ok = 2;

  // Time taken to check the queue health.
  google.protobuf.Duration response_time = 3 [lazy = true];

  // Error information if the check failed.
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### import_queue_request.proto {#import_queue_request}

**Path**: `gcommon/v1/queue/import_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `ImportQueueRequest`

**Imports** (3):

- `gcommon/v1/common/queue_export_format.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/import_queue_request.proto
// file: proto/gcommon/v1/queue/import_queue_request.proto
// version: 1.0.0
// guid: 5d6e7f8a-9b0c-1d2e-3f4a-5b6c7d8e9f0a
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/queue_export_format.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to import queue data from external source.
 */
message ImportQueueRequest {
  // Name of the queue to import into
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Source location for import data
  string source_path = 2;

  // Format of the import data
  gcommon.v1.common.QueueExportFormat format = 3;

  // Whether to overwrite existing data
  bool overwrite = 4;

  // Whether to validate data before import
  bool validate = 5;

  // Maximum number of messages to import
  uint64 max_messages = 6;

  // Import timeout in milliseconds
  uint64 timeout_ms = 7;
}
```

---

### import_queue_response.proto {#import_queue_response}

**Path**: `gcommon/v1/queue/import_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 53

**Messages** (1): `ImportQueueResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/import_queue_response.proto
// file: proto/gcommon/v1/queue/import_queue_response.proto
// version: 1.0.0
// guid: 5d4c3b2a-1f0e-9d8c-7b6a-5e4f3a2b1c0d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response message for queue import operations.
 */
message ImportQueueResponse {
  // Unique identifier for the import operation
  string import_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the import was successful
  bool success = 2;

  // Error message if import failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];

  // Number of messages imported
  uint64 imported_count = 4 [(buf.validate.field).uint64.gte = 0];

  // Number of messages that failed to import
  uint64 failed_count = 5 [(buf.validate.field).uint64.gte = 0];

  // Total number of messages processed
  uint64 total_count = 6 [(buf.validate.field).uint64.gte = 0];

  // Timestamp when import started
  google.protobuf.Timestamp start_time = 7;

  // Timestamp when import completed
  google.protobuf.Timestamp end_time = 8;

  // Import duration in milliseconds
  uint64 duration_ms = 9 [(buf.validate.field).uint64.gte = 0];

  // Import progress as percentage (0-100)
  float progress_percent = 10 [(buf.validate.field).float.gte = 0.0, (buf.validate.field).float.lte = 100.0];
}
```

---

### list_messages_request.proto {#list_messages_request}

**Path**: `gcommon/v1/queue/list_messages_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `ListMessagesRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_messages_request.proto
// version: 1.0.0
// guid: 176dd26f-bea8-4823-aa6a-eda00afdfeb6
// Request to list messages in a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to list messages in a queue
message ListMessagesRequest {
  // Topic name
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Partition ID (optional, all partitions if not specified)
  int32 partition_id = 2 [(buf.validate.field).int32.gte = 0];

  // Starting offset
  int64 start_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum number of messages to return
  int32 limit = 4 [(buf.validate.field).int32.gte = 0];

  // Include message headers
  bool include_headers = 5;

  // Include message metadata
  bool include_metadata = 6;

  // Filter by message status (optional)
  string status_filter = 7 [(buf.validate.field).string.min_len = 1];

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 8 [(buf.validate.field).int32.gt = 0];
}
```

---

### list_messages_response.proto {#list_messages_response}

**Path**: `gcommon/v1/queue/list_messages_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ListMessagesResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_messages_response.proto
// version: 1.0.0
// guid: 2a7aef43-6b98-462f-a3bd-9f06cb6636de
// Response for listing messages

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for listing messages
message ListMessagesResponse {
  // List of messages
  repeated QueueMessage messages = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of messages available
  int64 total_count = 2 [(buf.validate.field).int64.gte = 0];

  // Next page token for pagination
  string next_page_token = 3 [(buf.validate.field).string.min_len = 1];

  // Whether there are more messages
  bool has_more = 4;

  // Error message if listing failed
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_queues_request.proto {#list_queues_request}

**Path**: `gcommon/v1/queue/list_queues_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ListQueuesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_queues_request.proto
// version: 1.0.0
// guid: 10aa0104-6a4e-4092-98f4-8eabba61ea69
// ListQueuesRequest retrieves available queues for the current
// user or service account. This file was a placeholder and now
// implements the request following the 1-1-1 pattern.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListQueuesRequest {
  // Standard request metadata used across all services
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Optional page size for results
  int32 page_size = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Optional token for fetching the next page
  string page_token = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_queues_response.proto {#list_queues_response}

**Path**: `gcommon/v1/queue/list_queues_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListQueuesResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/queue_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_queues_response.proto
// version: 1.0.0
// guid: c2ffc959-d7b5-451f-94f4-a9334e02725f

// ListQueuesResponse returns a list of queues visible to the
// requester along with pagination information. This replaces the
// placeholder file generated during the migration.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/queue_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListQueuesResponse {
  // Collection of queues
  repeated QueueInfo queues = 1 [(buf.validate.field).repeated.min_items = 1];

  // Token to retrieve the next page
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### list_subscriptions_request.proto {#list_subscriptions_request}

**Path**: `gcommon/v1/queue/list_subscriptions_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `QueueListSubscriptionsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_subscriptions_request.proto
// version: 1.0.0
// guid: 781a6513-601b-4ef8-87bf-7c881f4b8a79
// ListSubscriptionsRequest returns subscriptions for a given topic or queue.
// Previously a placeholder, this file now contains the full request definition.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueListSubscriptionsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Name of the topic or queue to list subscriptions for
  string parent = 2 [(buf.validate.field).string.min_len = 1];

  // Optional page size
  int32 page_size = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Optional page token
  string page_token = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_subscriptions_response.proto {#list_subscriptions_response}

**Path**: `gcommon/v1/queue/list_subscriptions_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListSubscriptionsResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/common/subscription_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_subscriptions_response.proto
// version: 1.0.0
// guid: c20dc6c8-336b-4626-b709-22be9663d29d

// ListSubscriptionsResponse contains the subscriptions under a
// specific topic or queue. This file now implements the message
// rather than acting as a placeholder.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/common/subscription_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListSubscriptionsResponse {
  // Subscriptions returned
  repeated gcommon.v1.common.CommonSubscriptionInfo subscriptions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Token for fetching the next page
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Response metadata common across services
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### list_topics_request.proto {#list_topics_request}

**Path**: `gcommon/v1/queue/list_topics_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `ListTopicsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_topics_request.proto
// version: 1.1.0
// guid: f939cf46-c0f6-4815-a201-7cebdf9c255d
// Request to list available topics in the queue system

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ListTopicsRequest retrieves a list of available topics
message ListTopicsRequest {
  // Filter topics by name pattern (supports wildcards)
  string name_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Filter topics by namespace/category
  string namespace = 2 [(buf.validate.field).string.min_len = 1];

  // Include topic metadata in response
  bool include_metadata = 3;

  // Include topic statistics in response
  bool include_stats = 4;

  // Maximum number of topics to return
  int32 limit = 5 [(buf.validate.field).int32.gte = 0];

  // Pagination token for continued listing
  string page_token = 6 [(buf.validate.field).string.min_len = 1];

  // Sort topics by specified field (name, created_at, message_count)
  string sort_by = 7 [(buf.validate.field).string.min_len = 1];

  // Sort order (asc, desc)
  string sort_order = 8 [(buf.validate.field).string.min_len = 1];

  // Filter by topic state (active, paused, deleted)
  repeated string topic_states = 9 [(buf.validate.field).repeated.min_items = 1];

  // Include only topics user has access to
  bool access_check = 10;

  // Additional filter criteria
  map<string, string> filters = 11;
}
```

---

### list_topics_response.proto {#list_topics_response}

**Path**: `gcommon/v1/queue/list_topics_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `ListTopicsResponse`

**Imports** (3):

- `gcommon/v1/queue/topic_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/list_topics_response.proto
// version: 1.1.0
// guid: 64d60266-e2ca-4927-9db1-d3824b83d9a5
// Response containing list of available topics

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/topic_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ListTopicsResponse {
  // List of topics
  repeated TopicInfo topics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Next page token
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total count
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}

// ListTopicsResponse returns a list of available topics
// This file needs proper implementation
```

---

### migrate_queue_request.proto {#migrate_queue_request}

**Path**: `gcommon/v1/queue/migrate_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `MigrateQueueRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/migrate_queue_request.proto
// version: 1.0.0
// guid: 2d4044aa-7bd3-43a9-91c7-d4f8c0be36f9
// Request to migrate a queue

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to migrate a queue to a new location
message MigrateQueueRequest {
  // Source queue name to migrate from
  string source_queue = 1 [(buf.validate.field).string.min_len = 1];

  // Destination queue name to migrate to
  string destination_queue = 2 [(buf.validate.field).string.min_len = 1];

  // Destination endpoint/server
  string destination_endpoint = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to preserve message ordering
  bool preserve_order = 4;

  // Whether to verify data integrity after migration
  bool verify_integrity = 5;

  // Maximum migration duration (milliseconds)
  int32 max_duration_ms = 6 [(buf.validate.field).int32.gt = 0];

  // Batch size for migration
  int32 batch_size = 7 [(buf.validate.field).int32.gte = 0];

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 8 [(buf.validate.field).int32.gt = 0];
}
```

---

### migrate_queue_response.proto {#migrate_queue_response}

**Path**: `gcommon/v1/queue/migrate_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `MigrateQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/migrate_queue_response.proto
// version: 1.0.0
// guid: 331ebb05-f30d-46d3-8d6e-ef766fd0cc51
// Response for queue migration operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue migration operations
message MigrateQueueResponse {
  // Whether the migration was successful
  bool success = 1;

  // New queue location/endpoint
  string new_queue_endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Number of messages migrated
  int64 messages_migrated = 3 [(buf.validate.field).int64.gte = 0];

  // Migration duration (milliseconds)
  int32 migration_duration_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Source queue name
  string source_queue = 5 [(buf.validate.field).string.min_len = 1];

  // Destination queue name
  string destination_queue = 6 [(buf.validate.field).string.min_len = 1];

  // Error message if migration failed
  string error = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### nack_request.proto {#nack_request}

**Path**: `gcommon/v1/queue/nack_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `NackRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/nack_error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_request.proto
// version: 1.1.0
// guid: 5b6c7d8e-9f0a-1b2c-3d4e-5f6a7b8c9d0e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/nack_error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to negatively acknowledge (NACK) a message.
 * This indicates that the message could not be processed and may need to be requeued.
 */
message NackRequest {
  // Acknowledgment token received with the message
  string ack_token = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the message should be requeued for retry
  bool requeue = 2;

  // Reason for the negative acknowledgment
  string reason = 3 [(buf.validate.field).string.min_len = 1];

  // Error details if processing failed
  NackError error = 4;

  // Delay before requeuing (if requeue is true)
  int64 requeue_delay_seconds = 5 [(buf.validate.field).int64.gte = 0];

  // Maximum number of retry attempts for this message
  int32 max_retries = 6 [(buf.validate.field).int32.gte = 0];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
```

---

### nack_response.proto {#nack_response}

**Path**: `gcommon/v1/queue/nack_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `NackResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_response.proto
// version: 1.0.0
// guid: 70f01290-1e6f-484c-aa71-1cd5f50aa7f5
// Response for negative acknowledgment operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for negative acknowledgment operations
message NackResponse {
  // Whether the nack was successful
  bool success = 1;

  // Error message if nack failed
  string error = 2 [(buf.validate.field).string.min_len = 1];

  // Message ID that was nacked
  string message_id = 3 [(buf.validate.field).string.min_len = 1];

  // Timestamp when nack was processed
  int64 timestamp = 4;
}
```

---

### pause_queue_request.proto {#pause_queue_request}

**Path**: `gcommon/v1/queue/pause_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PauseQueueRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pause_queue_request.proto
// version: 1.0.0
// guid: a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to pause a queue.
 * Stops message processing while keeping messages in the queue.
 */
message PauseQueueRequest {
  // Name of the queue to pause
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reason for pausing the queue
  string reason = 2;

  // Whether to wait for current messages to finish processing
  bool graceful = 3;

  // Timeout for graceful pause (milliseconds)
  int32 timeout_ms = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;

  // Whether to pause specific partitions only
  repeated int32 partition_ids = 6;
}
```

---

### pause_queue_response.proto {#pause_queue_response}

**Path**: `gcommon/v1/queue/pause_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PauseQueueResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pause_queue_response.proto
// version: 1.0.0
// guid: 8d32dd33-5b24-4d1f-b32c-fc9e172e7b9a
// Response for queue pause operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue pause operations
message PauseQueueResponse {
  // Whether the pause was successful
  bool success = 1;

  // Queue name that was paused
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current pause status
  string pause_status = 3;

  // Number of active consumers affected
  int32 affected_consumers = 4;

  // Timestamp when pause took effect
  int64 pause_timestamp = 5;

  // Error message if pause failed
  string error = 6;
}
```

---

### peek_request.proto {#peek_request}

**Path**: `gcommon/v1/queue/peek_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 100

**Messages** (1): `PeekRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/peek_request.proto
// version: 1.0.0
// guid: 1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";
// Standard imports

// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * PeekRequest allows viewing messages in a queue without removing them.
 * Useful for inspection, monitoring, and debugging queue contents
 * without affecting message processing.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message PeekRequest {
  // Required fields (1-10)

  /**
   * The name/identifier of the queue to peek into.
   * Must be a valid existing queue.
   */
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Maximum number of messages to peek at.
   * Range: 1-100. Default: 1.
   */
  int32 max_messages = 12;

  /**
   * Starting position in the queue for peeking.
   * 0 = first message, 1 = second message, etc.
   * Default: 0 (peek at head of queue).
   */
  int32 start_position = 13;

  /**
   * Message group ID filter. If specified, only messages
   * from this group will be returned.
   */
  string group_id_filter = 14;

  /**
   * Attribute filters for selective message viewing.
   * Only messages matching all specified attributes will be returned.
   */
  map<string, string> attribute_filters = 15;

  /**
   * Message type filter. If specified, only messages of
   * this type will be returned.
   */
  string message_type_filter = 16;

  /**
   * Priority threshold - only return messages with priority
   * greater than or equal to this value. Range: 0-255.
   */
  int32 min_priority = 17;

  /**
   * Include message content/payload in the response.
   * Default: true. Set to false to only get metadata.
   */
  bool include_payload = 18;

  /**
   * Include message attributes in the response.
   * Default: true. Set to false to reduce response size.
   */
  bool include_attributes = 19;

  /**
   * Include detailed delivery metadata (timestamps, delivery count, etc.).
   * Default: false for performance.
   */
  bool include_delivery_metadata = 20;
}
```

---

### peek_response.proto {#peek_response}

**Path**: `gcommon/v1/queue/peek_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 127

**Messages** (1): `PeekResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/peek_response.proto
// version: 1.0.0
// guid: 2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

// Queue message types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * PeekResponse returns messages viewed from a queue without removing them.
 * Contains message data and metadata for inspection purposes
 * without affecting the queue state.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message PeekResponse {
  // Required fields (1-10)

  /**
   * Messages viewed from the queue.
   * Empty if no messages were found matching the criteria.
   */
  repeated QueueMessage messages = 1;

  /**
   * Indicates whether the peek operation was successful.
   */
  bool success = 2;

  // Optional fields (11-50)

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  /**
   * Name of the queue that was peeked.
   * Echoed from the request for verification.
   */
  string queue_name = 12 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  /**
   * Total number of messages that matched the peek criteria.
   * May be larger than the number of messages returned due to max_messages limit.
   */
  int32 total_matching_messages = 13;

  /**
   * Approximate total number of messages currently in the queue.
   * Useful for monitoring and capacity planning.
   */
  int64 approximate_queue_size = 14;

  /**
   * Position in the queue where peeking started.
   * Echoed from the request for verification.
   */
  int32 start_position = 15;

  /**
   * Position in the queue where peeking ended.
   * Helpful for subsequent peek operations.
   */
  int32 end_position = 16;

  /**
   * Whether there are more messages available beyond the returned set.
   * True if total_matching_messages > returned messages count.
   */
  bool has_more_messages = 17;

  /**
   * Number of messages that were skipped due to filters.
   * Useful for understanding filter effectiveness.
   */
  int32 filtered_message_count = 18;

  /**
   * Oldest message timestamp in the peeked set.
   * Useful for understanding queue age/staleness.
   */
  google.protobuf.Timestamp oldest_message_time = 19;

  /**
   * Newest message timestamp in the peeked set.
   */
  google.protobuf.Timestamp newest_message_time = 20;

  // Status and error fields (61-70)

  /**
   * Error information if the peek operation failed
   * or completed with warnings.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when the peek operation was performed.
   */
  google.protobuf.Timestamp peeked_at = 51;

  /**
   * Timestamp when this response was generated.
   */
  google.protobuf.Timestamp response_generated_at = 52;
}
```

---

### publish_request.proto {#publish_request}

**Path**: `gcommon/v1/queue/publish_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `QueuePublishRequest`

**Imports** (5):

- `buf/validate/validate.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/delivery_options.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_request.proto
// version: 1.1.0
// guid: 59dc8120-bc2f-4d56-a9f1-f0957cb9bafb
// PublishRequest publishes a single message to a named topic. It is
// used for pub/sub style messaging where consumers subscribe to
// topics rather than specific queues.
// PublishRequest contains all information required to publish a
// message to a topic.

edition = "2023";

package gcommon.v1.queue;

import "buf/validate/validate.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/delivery_options.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueuePublishRequest {
  // Name of the topic to publish to - required, alphanumeric with dots/hyphens, 3-255 chars
  string topic_name = 1 [
    (buf.validate.field).required = true,
    (buf.validate.field).string.pattern = "^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$",
    (buf.validate.field).string.min_len = 3,
    (buf.validate.field).string.max_len = 255
  ];

  // Message to publish - required
  QueueMessage message = 2 [(buf.validate.field).required = true];

  // Optional delivery parameters controlling retries and delays
  DeliveryOptions delivery_options = 3;

  // Standard request metadata for tracing and auth - required
  gcommon.v1.common.RequestMetadata metadata = 4 [(buf.validate.field).required = true];
}
```

---

### publish_response.proto {#publish_response}

**Path**: `gcommon/v1/queue/publish_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PublishResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_response.proto
// version: 1.0.0
// guid: 8b12b279-f7c6-40fe-9147-4a663fb0c9c6

// PublishResponse reports the outcome of publishing a message to a
// topic.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// PublishResponse contains the identifier of the published message
// and success status.
message PublishResponse {
  // Unique identifier of the message as stored by the broker.
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the publish operation succeeded.
  bool success = 2;

  // Error information when success is false.
  gcommon.v1.common.Error error = 3;

  // Request metadata echoed back for tracing.
  gcommon.v1.common.RequestMetadata request_metadata = 4;
}
```

---

### publish_result.proto {#publish_result}

**Path**: `gcommon/v1/queue/publish_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `PublishResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_result.proto
// version: 1.0.0
// guid: aabfd67d-e9a2-40c7-99b8-464c242bc864
// Result information for individual message publish operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Result for an individual message publish
message PublishResult {
  // Message ID assigned by the queue
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the publish was successful
  bool success = 2;

  // Error message if publish failed
  string error = 3 [(buf.validate.field).string.min_len = 1];

  // Partition ID where message was published
  int32 partition_id = 4 [(buf.validate.field).int32.gte = 0];

  // Offset within the partition
  int64 offset = 5 [(buf.validate.field).int64.gte = 0];

  // Timestamp when message was published
  int64 timestamp = 6;
}
```

---

### pull_request.proto {#pull_request}

**Path**: `gcommon/v1/queue/pull_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PullRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pull_request.proto
// version: 1.0.0
// guid: dae5ea8a-77c7-4b90-ab25-d2981ba423df
// PullRequest retrieves a single message from the specified queue
// without establishing a subscription. This file replaces the
// placeholder generated during migration.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PullRequest {
  // Request metadata for tracing and authentication
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Queue to pull from
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional visibility timeout for the pulled message
  int32 visibility_timeout_seconds = 3;
}
```

---

### pull_response.proto {#pull_response}

**Path**: `gcommon/v1/queue/pull_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `PullResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/queue/received_message.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/pull_response.proto
// version: 1.0.1
// guid: 5c55b3fd-beda-4758-90c9-2084f2d6ea8f

// PullResponse returns a message pulled from the queue. This file
// now contains the actual response definition instead of a placeholder.
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/queue/received_message.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PullResponse {
  // The received message. May be null if no message was available.
  ReceivedMessage message = 1;

  // Response metadata including error details
  gcommon.v1.common.ResponseMetadata metadata = 2;
}
```

---

### purge_request.proto {#purge_request}

**Path**: `gcommon/v1/queue/purge_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `PurgeRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/purge_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/purge_request.proto
// version: 1.0.0
// guid: 8d7b880f-5830-44c2-ab26-58afb465d587

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/purge_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PurgeRequest {
  // Name of the queue to purge
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Purge options
  PurgeOptions options = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
```

---

### purge_response.proto {#purge_response}

**Path**: `gcommon/v1/queue/purge_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `PurgeResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/purge_response.proto
// version: 1.0.0
// guid: 14d5741d-3af8-49b9-8ec4-887527a72cfb
// Response for queue purge operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for queue purge operations
message PurgeResponse {
  // Whether the purge was successful
  bool success = 1;

  // Number of messages purged
  int64 messages_purged = 2 [(buf.validate.field).int64.gte = 0];

  // Number of bytes freed
  int64 bytes_freed = 3 [(buf.validate.field).int64.gte = 0];

  // Purge duration (milliseconds)
  int32 purge_duration_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Partitions that were purged
  repeated int32 purged_partitions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Error message if purge failed
  string error = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### push_request.proto {#push_request}

**Path**: `gcommon/v1/queue/push_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `PushRequest`

**Imports** (5):

- `gcommon/v1/queue/batch_settings.proto`
- `gcommon/v1/queue/publish_config.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/push_request.proto
// version: 1.0.0
// guid: ab6bdde8-25b2-424c-a85a-db3364d8cdaf

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/batch_settings.proto";
import "gcommon/v1/queue/publish_config.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PushRequest {
  // Target topic or queue identifier
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Messages to publish
  repeated QueueMessage messages = 2 [(buf.validate.field).repeated.min_items = 1];

  // Publishing configuration
  PublishConfig publish_config = 3;

  // Batch publishing settings
  BatchSettings batch_settings = 4;

  // Transaction ID for transactional publishing
  string transaction_id = 5 [(buf.validate.field).string.min_len = 1];

  // Producer ID for message tracking
  string producer_id = 6 [(buf.validate.field).string.min_len = 1];

  // Publishing metadata
  map<string, string> metadata = 7;
}
```

---

### push_response.proto {#push_response}

**Path**: `gcommon/v1/queue/push_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `PushResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/push_response.proto
// file: proto/gcommon/v1/queue/push_response.proto
// version: 1.0.0
// guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for message publishing operations.
 */
message PushResponse {
  // Unique identifier assigned to the published message
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the message was accepted by the queue
  google.protobuf.Timestamp accepted_at = 2;

  // Position/offset of the message in the queue
  int64 message_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Current queue depth after the message was added
  int64 queue_depth = 4 [(buf.validate.field).int64.gte = 0];

  // Whether the message was persisted to storage
  bool persisted = 5;

  // Estimated delivery time (for delayed messages)
  google.protobuf.Timestamp estimated_delivery_time = 6;
}
// This file needs proper implementation
```

---

### queue_consumer_stats.proto {#queue_consumer_stats}

**Path**: `gcommon/v1/queue/queue_consumer_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `QueueConsumerStats`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_consumer_stats.proto
// version: 1.0.0
// guid: b0ed0505-1d76-4961-8937-36fcad7a7185

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueConsumerStats {
  string consumer_id = 1;
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  int64 messages_processed = 3;
  double processing_rate = 4;
  double success_rate = 5;
  google.protobuf.Timestamp last_activity = 6;
  google.protobuf.Duration average_processing_time = 7;
}
```

---

### queue_depth_sample.proto {#queue_depth_sample}

**Path**: `gcommon/v1/queue/queue_depth_sample.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `QueueDepthSample`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_depth_sample.proto
// version: 1.0.0
// guid: 6f770e99-3809-4efb-848d-f2c554a669f8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueDepthSample {
  google.protobuf.Timestamp timestamp = 1;
  int64 depth = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### queue_health.proto {#queue_health}

**Path**: `gcommon/v1/queue/queue_health.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `QueueHealth`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_health.proto
// version: 1.0.0
// guid: 1524854f-4eb8-4bb2-8942-cd7ca2544b2d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueHealth {
  // Name of the queue
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Health status
  gcommon.v1.common.CommonHealthStatus status = 2;

  // Health score (0-100)
  int32 health_score = 3;

  // List of health issues
  repeated string issues = 4;

  // Last health check timestamp
  google.protobuf.Timestamp last_check = 5;
}
```

---

### queue_info.proto {#queue_info}

**Path**: `gcommon/v1/queue/queue_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `QueueInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_info.proto
// version: 1.0.0
// guid: d2ab2b72-14e2-4afe-80f7-2ecf00daacac

// QueueInfo provides metadata about a queue instance. This replaces the
// empty placeholder created during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * QueueInfo describes the configuration and current status of a queue.
 * It is returned by administrative APIs such as ListQueues.
 */
message QueueInfo {
  // Name of the queue
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Type of queue implementation (e.g., "rabbitmq", "nats")
  string type = 2;

  // Current approximate number of messages in the queue
  int64 message_count = 3;

  // Number of active consumers
  int32 consumer_count = 4;

  // Time when the queue was created
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // Additional metadata or labels for the queue
  map<string, string> labels = 6;
}
```

---

### queue_message.proto {#queue_message}

**Path**: `gcommon/v1/queue/queue_message.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `QueueMessage`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_message.proto
// version: 1.0.0
// guid: a2597962-4731-4f47-b6dd-4da9a937c834

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// QueueMessage represents a single item in a queue.
message QueueMessage {
  // Message ID (auto-generated if not provided).
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Arbitrary payload for the message.
  google.protobuf.Any body = 2;

  // Custom key/value attributes for routing or metadata.
  map<string, string> attributes = 3;

  // Additional headers attached to the message.
  map<string, string> headers = 4;

  // Priority value (0-255, higher values processed first).
  int32 priority = 5;

  // Expiration time for the message.
  google.protobuf.Timestamp expires_at = 6;

  // Optional correlation identifier.
  string correlation_id = 7;

  // Queue name for replies.
  string reply_to = 8;

  // MIME type of the message body.
  string content_type = 9;

  // Encoding used for the message body.
  string content_encoding = 10;

  // Creation timestamp of the message.
  google.protobuf.Timestamp created_at = 11 [ (buf.validate.field).required = true ];
}
```

---

### queue_stats.proto {#queue_stats}

**Path**: `gcommon/v1/queue/queue_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `QueueStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Statistics for a specific queue
message QueueStats {
  // Queue name
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Current message count
  int64 message_count = 2;

  // Total bytes stored
  int64 total_bytes = 3;

  // Average message size
  double avg_message_size = 4;

  // Messages processed per second
  double throughput = 5;

  // Queue depth over time
  int64 current_depth = 6;

  // Peak depth in the measurement period
  int64 peak_depth = 7;

  // Last activity timestamp
  google.protobuf.Timestamp last_activity = 8;
}
```

---

### queue_stats_point.proto {#queue_stats_point}

**Path**: `gcommon/v1/queue/queue_stats_point.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `QueueStatsPoint`

**Imports** (3):

- `gcommon/v1/queue/queue_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats_point.proto
// version: 1.0.1
// guid: f6478b51-fafb-4571-b43b-cac8ec0cfd13

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStatsPoint {
  // Timestamp for this data point
  google.protobuf.Timestamp timestamp = 1;

  // Statistics at this point in time
  QueueStats stats = 2;
}
```

---

### queue_stats_response.proto {#queue_stats_response}

**Path**: `gcommon/v1/queue/queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `QueueStatsResponse`

**Imports** (4):

- `gcommon/v1/queue/queue_stats.proto`
- `gcommon/v1/queue/queue_stats_point.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats_response.proto
// version: 1.0.0
// guid: 5944c9a3-ae37-4aac-b6dc-36b7a9c0eaa5

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_stats.proto";
import "gcommon/v1/queue/queue_stats_point.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStatsResponse {
  // Queue statistics
  QueueStats stats = 1;

  // Time series data
  repeated QueueStatsPoint time_series = 2 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### queue_stats_summary.proto {#queue_stats_summary}

**Path**: `gcommon/v1/queue/queue_stats_summary.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `QueueStatsSummary`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_stats_summary.proto
// version: 1.0.0
// guid: beb6cfcc-70db-4a5a-9ec1-2e241e98f71f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStatsSummary {
  // Total number of queues
  int64 total_queues = 1 [(buf.validate.field).int64.gte = 0];

  // Total messages across all queues
  int64 total_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Total messages processed in the last hour
  int64 messages_processed_last_hour = 3 [(buf.validate.field).int64.gte = 0];

  // Average processing time across all queues
  google.protobuf.Duration average_processing_time = 4;

  // Overall system health score (0-100)
  int32 health_score = 5 [(buf.validate.field).int32.gte = 0];

  // Total active consumers
  int64 active_consumers = 6 [(buf.validate.field).int64.gte = 0];

  // Total storage used by messages
  int64 total_storage_bytes = 7 [(buf.validate.field).int64.gte = 0];
}
```

---

### reset_details.proto {#reset_details}

**Path**: `gcommon/v1/queue/reset_details.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `ResetDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/reset_details.proto
// version: 1.0.0
// guid: b0e2cbdc-ca09-41a1-81b3-771cf6e15072

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResetDetails {
  // Number of metrics reset
  int32 metrics_reset_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of counters reset
  int32 counters_reset_count = 2 [(buf.validate.field).int32.gte = 0];

  // Number of histograms reset
  int32 histograms_reset_count = 3 [(buf.validate.field).int32.gte = 0];

  // Number of partitions affected
  int32 partitions_affected = 4 [(buf.validate.field).int32.gte = 0];

  // Time taken to complete reset (milliseconds)
  int64 reset_duration_ms = 5 [(buf.validate.field).int64.gt = 0];

  // Whether reset was partial or complete
  bool partial_reset = 6;

  // Reason for reset operation
  string reset_reason = 7 [(buf.validate.field).string.min_len = 1];

  // User or system that initiated reset
  string initiated_by = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### reset_queue_stats_request.proto {#reset_queue_stats_request}

**Path**: `gcommon/v1/queue/reset_queue_stats_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `ResetQueueStatsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/reset_queue_stats_request.proto
// version: 1.0.0
// guid: d2059a85-daa1-4c7e-85c1-e55409000e9d
// Request to reset queue statistics

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to reset queue statistics
message ResetQueueStatsRequest {
  // Queue name to reset stats for
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reset specific stat types (empty means reset all)
  repeated string stat_types = 2;

  // Reset stats for specific partitions only
  repeated int32 partition_ids = 3;

  // Preserve historical data before this timestamp
  int64 preserve_before_timestamp = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}
```

---

### reset_queue_stats_response.proto {#reset_queue_stats_response}

**Path**: `gcommon/v1/queue/reset_queue_stats_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `ResetQueueStatsResponse`

**Imports** (5):

- `gcommon/v1/queue/preserved_stats.proto`
- `gcommon/v1/queue/reset_details.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/reset_queue_stats_response.proto
// version: 1.0.0
// guid: 11f82fe8-4d3f-4188-b0c9-4fb2a7d24591

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/preserved_stats.proto";
import "gcommon/v1/queue/reset_details.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResetQueueStatsResponse {
  // Success status of the reset operation
  bool success = 1;

  // Queue identifier whose stats were reset
  string queue_id = 2 [(buf.validate.field).string.min_len = 1];

  // Timestamp when reset operation completed
  google.protobuf.Timestamp reset_at = 3;

  // Statistics that were preserved before reset
  PreservedStats preserved_stats = 4;

  // Types of statistics that were reset
  repeated string reset_stat_types = 5 [(buf.validate.field).repeated.min_items = 1];

  // Types of statistics that were preserved
  repeated string preserved_stat_types = 6 [(buf.validate.field).repeated.min_items = 1];

  // Error message if reset failed
  string error_message = 7 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 8 [(buf.validate.field).string.min_len = 1];

  // Warning messages about the reset operation
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Reset operation details
  ResetDetails reset_details = 10;

  // Operation metadata
  map<string, string> metadata = 11;
}
```

---

### restore_error.proto {#restore_error}

**Path**: `gcommon/v1/queue/restore_error.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `RestoreError`

**Imports** (4):

- `gcommon/v1/queue/offset_range.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_error.proto
// version: 1.0.0
// guid: 9b5c3655-3a8b-40fa-ab5d-ddcec3f98462

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/offset_range.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreError {
  // Error code for programmatic handling
  string error_code = 1 [(buf.validate.field).string.min_len = 1];

  // Human-readable error message
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Error category (validation, io, corruption, etc.)
  string error_category = 3 [(buf.validate.field).string.min_len = 1];

  // Specific component that failed
  string failed_component = 4 [(buf.validate.field).string.min_len = 1];

  // Partition ID if error is partition-specific
  int32 partition_id = 5 [(buf.validate.field).int32.gte = 0];

  // Message offset range affected by error
  OffsetRange affected_range = 6;

  // Error timestamp
  google.protobuf.Timestamp error_time = 7;

  // Whether error is recoverable
  bool recoverable = 8;
}
```

---

### restore_options.proto {#restore_options}

**Path**: `gcommon/v1/queue/restore_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `RestoreOptions`

**Imports** (6):

- `gcommon/v1/common/time_range_metrics.proto`
- `gcommon/v1/queue/filter_criteria.proto`
- `gcommon/v1/queue/offset_range.proto`
- `gcommon/v1/queue/performance_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_options.proto
// version: 1.0.0
// guid: 5747b00e-cec5-49aa-adb9-514b7eefc3c4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/time_range_metrics.proto";
import "gcommon/v1/queue/filter_criteria.proto";
import "gcommon/v1/queue/offset_range.proto";
import "gcommon/v1/queue/performance_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreOptions {
  // Skip message content (restore structure only)
  bool skip_message_content = 1;

  // Restore message metadata only
  bool metadata_only = 2;

  // Maximum number of messages to restore
  int64 max_messages = 3 [(buf.validate.field).int64.gte = 0];

  // Restore messages from specific offset range
  OffsetRange offset_range = 4;

  // Restore messages within time range
  // Time range for restore
  gcommon.v1.common.TimeRangeMetrics time_range = 5;

  // Restore specific message priorities
  repeated int32 priority_levels = 6 [(buf.validate.field).repeated.min_items = 1];

  // Include/exclude patterns for message filtering
  FilterCriteria filter_criteria = 7;

  // Performance tuning options
  PerformanceOptions performance = 8;
}
```

---

### restore_queue_request.proto {#restore_queue_request}

**Path**: `gcommon/v1/queue/restore_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `RestoreQueueRequest`

**Imports** (6):

- `gcommon/v1/queue/backup_source.proto`
- `gcommon/v1/queue/restore_config.proto`
- `gcommon/v1/queue/restore_options.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_queue_request.proto
// version: 1.0.0
// guid: 8dbc0f2d-31af-48e8-9785-3d801a7d7e95

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/backup_source.proto";
import "gcommon/v1/queue/restore_config.proto";
import "gcommon/v1/queue/restore_options.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreQueueRequest {
  // Target queue identifier for restoration
  string target_queue_id = 1 [(buf.validate.field).string.min_len = 1];

  // Backup source information
  BackupSource backup_source = 2;

  // Restoration configuration
  RestoreConfig restore_config = 3;

  // Restore to specific point in time
  google.protobuf.Timestamp restore_point = 4;

  // Overwrite existing queue if it exists
  bool overwrite_existing = 5;

  // Validate backup integrity before restore
  bool validate_backup = 6;

  // Restore only specific partitions (empty = all partitions)
  repeated int32 partition_ids = 7 [(buf.validate.field).repeated.min_items = 1];

  // Restore options
  RestoreOptions options = 8;

  // Operation metadata
  map<string, string> metadata = 9;
}
```

---

### restore_queue_response.proto {#restore_queue_response}

**Path**: `gcommon/v1/queue/restore_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 63

**Messages** (1): `RestoreQueueResponse`

**Imports** (10):

- `gcommon/v1/common/metrics_validation_result.proto`
- `gcommon/v1/queue/partition_restore_result.proto`
- `gcommon/v1/queue/restore_error.proto`
- `gcommon/v1/queue/restore_statistics.proto`
- `gcommon/v1/queue/restore_status.proto`
- `gcommon/v1/queue/restore_warning.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_queue_response.proto
// version: 1.0.0
// guid: 949d5078-96a1-43dd-adb1-5e57d6a82a57

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_validation_result.proto";
import "gcommon/v1/queue/partition_restore_result.proto";
import "gcommon/v1/queue/restore_error.proto";
import "gcommon/v1/queue/restore_statistics.proto";
import "gcommon/v1/queue/restore_status.proto";
import "gcommon/v1/queue/restore_warning.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreQueueResponse {
  // Operation success status
  bool success = 1;

  // Restore operation ID for tracking
  string operation_id = 2 [(buf.validate.field).string.min_len = 1];

  // Restored queue identifier
  string restored_queue_id = 3 [(buf.validate.field).string.min_len = 1];

  // Restoration start timestamp
  google.protobuf.Timestamp start_time = 4;

  // Restoration completion timestamp
  google.protobuf.Timestamp completion_time = 5;

  // Total restoration duration
  google.protobuf.Duration duration = 6;

  // Restoration statistics
  RestoreStatistics statistics = 7;

  // Restoration status details
  RestoreStatus status = 8;

  // Any errors encountered during restore
  repeated RestoreError errors = 9 [(buf.validate.field).repeated.min_items = 1];

  // Warnings generated during restore
  repeated RestoreWarning warnings = 10 [(buf.validate.field).repeated.min_items = 1];

  // Partition restoration results
  repeated PartitionRestoreResult partition_results = 11 [(buf.validate.field).repeated.min_items = 1];

  // Validation results if validation was requested
  gcommon.v1.common.MetricsValidationResult validation_result = 12;

  // Operation metadata
  map<string, string> metadata = 13;
}
```

---

### restore_statistics.proto {#restore_statistics}

**Path**: `gcommon/v1/queue/restore_statistics.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `RestoreStatistics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_statistics.proto
// version: 1.0.0
// guid: f83290f6-3fb7-42fe-9473-6cf7028461e1

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreStatistics {
  // Total messages restored
  int64 messages_restored = 1 [(buf.validate.field).int64.gte = 0];

  // Total bytes restored
  int64 bytes_restored = 2 [(buf.validate.field).int64.gte = 0];

  // Number of partitions restored
  int32 partitions_restored = 3 [(buf.validate.field).int32.gte = 0];

  // Messages skipped due to filters
  int64 messages_skipped = 4 [(buf.validate.field).int64.gte = 0];

  // Messages failed to restore
  int64 messages_failed = 5 [(buf.validate.field).int64.gte = 0];

  // Average restore rate (messages/second)
  double restore_rate = 6 [(buf.validate.field).double.gte = 0.0];

  // Throughput (bytes/second)
  double throughput_bps = 7 [(buf.validate.field).double.gte = 0.0];

  // Backup file size processed
  int64 backup_size_bytes = 8 [(buf.validate.field).int64.gte = 0];

  // Compression ratio achieved
  double compression_ratio = 9 [(buf.validate.field).double.gte = 0.0];
}
```

---

### restore_status.proto {#restore_status}

**Path**: `gcommon/v1/queue/restore_status.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `RestoreStatus`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_status.proto
// version: 1.0.0
// guid: 49efaefe-393a-43b4-8e5e-af25695292fc

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreStatus {
  // Status code (pending, in_progress, completed, failed, cancelled)
  string status_code = 1 [(buf.validate.field).string.min_len = 1];

  // Human-readable status message
  string status_message = 2 [(buf.validate.field).string.min_len = 1];

  // Progress percentage (0-100)
  int32 progress_percentage = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Current operation phase
  string current_phase = 4 [(buf.validate.field).string.min_len = 1];

  // Estimated time remaining
  google.protobuf.Duration estimated_remaining = 5;

  // Last status update timestamp
  google.protobuf.Timestamp last_update = 6;
}
```

---

### restore_warning.proto {#restore_warning}

**Path**: `gcommon/v1/queue/restore_warning.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `RestoreWarning`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/restore_warning.proto
// version: 1.0.0
// guid: 97e72ea7-3c16-4e40-8dba-5845c294bf28

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RestoreWarning {
  // Warning code
  string warning_code = 1 [(buf.validate.field).string.min_len = 1];

  // Warning message
  string warning_message = 2 [(buf.validate.field).string.min_len = 1];

  // Warning category
  string warning_category = 3 [(buf.validate.field).string.min_len = 1];

  // Affected component
  string affected_component = 4 [(buf.validate.field).string.min_len = 1];

  // Partition ID if warning is partition-specific
  int32 partition_id = 5 [(buf.validate.field).int32.gte = 0];

  // Warning timestamp
  google.protobuf.Timestamp warning_time = 6;
}
```

---

### resume_queue_request.proto {#resume_queue_request}

**Path**: `gcommon/v1/queue/resume_queue_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `ResumeQueueRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resume_queue_request.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to resume a paused queue.
 * Restarts message processing for a previously paused queue.
 */
message ResumeQueueRequest {
  // Name of the queue to resume
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reason for resuming the queue
  string reason = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;

  // Whether to resume specific partitions only
  repeated int32 partition_ids = 4;

  // Whether to start processing from where it left off
  bool resume_from_last_position = 5;
}
```

---

### resume_queue_response.proto {#resume_queue_response}

**Path**: `gcommon/v1/queue/resume_queue_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 58

**Messages** (1): `ResumeQueueResponse`

**Imports** (5):

- `gcommon/v1/common/queue_state.proto`
- `gcommon/v1/queue/resume_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resume_queue_response.proto
// version: 1.0.0
// guid: 43e76b2f-3350-49a8-b002-e38b946919ad

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/queue_state.proto";
import "gcommon/v1/queue/resume_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResumeQueueResponse {
  // Success status of the resume operation
  bool success = 1;

  // Queue identifier that was resumed
  string queue_id = 2 [(buf.validate.field).string.min_len = 1];

  // Previous queue state before resume
  gcommon.v1.common.QueueState previous_state = 3;

  // Current queue state after resume
  gcommon.v1.common.QueueState current_state = 4;

  // Timestamp when resume operation completed
  google.protobuf.Timestamp resumed_at = 5;

  // Duration the queue was paused (milliseconds)
  int64 pause_duration_ms = 6 [(buf.validate.field).int64.gt = 0];

  // Messages that were queued during pause
  int64 messages_queued_during_pause = 7 [(buf.validate.field).int64.gte = 0];

  // Consumer groups affected by resume
  repeated string affected_consumer_groups = 8 [(buf.validate.field).repeated.min_items = 1];

  // Error message if resume failed
  string error_message = 9 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 10 [(buf.validate.field).string.min_len = 1];

  // Warning messages about resume operation
  repeated string warnings = 11 [(buf.validate.field).repeated.min_items = 1];

  // Resume operation statistics
  ResumeStats resume_stats = 12;

  // Operation metadata
  map<string, string> metadata = 13;
}
```

---

### seek_request.proto {#seek_request}

**Path**: `gcommon/v1/queue/seek_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 58

**Messages** (1): `SeekRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/seek_request.proto
// file: proto/gcommon/v1/queue/seek_request.proto
// version: 1.0.0
// guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d
//
// Request definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to seek to a specific position in a queue or topic.
 * Used for replaying messages from a particular point in time or offset.
 */
message SeekRequest {
  // Name of the queue or topic to seek within
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Subscription name (for topics with multiple subscribers)
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Seek position specification
  oneof seek_position {
    // Seek to a specific timestamp
    google.protobuf.Timestamp timestamp = 3;

    // Seek to a specific message offset/position
    int64 offset = 4;

    // Seek to the beginning of the queue
    bool beginning = 5;

    // Seek to the end of the queue (latest message)
    bool end = 6;

    // Seek to a specific message ID
    string message_id = 7;
  }

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 100;
}
// This file needs proper implementation
```

---

### seek_response.proto {#seek_response}

**Path**: `gcommon/v1/queue/seek_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `SeekResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/seek_response.proto
// version: 1.0.0
// guid: d1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for seek operations on a queue.
 * Contains the result of attempting to seek to a specific position.
 */
message SeekResponse {
  // Whether the seek operation was successful
  bool success = 1;

  // The actual position seeked to
  int64 position = 2 [(buf.validate.field).int64.gte = 0];

  // The offset within the partition (for partitioned queues)
  int64 offset = 3 [(buf.validate.field).int64.gte = 0];

  // The partition ID (for partitioned queues)
  int32 partition_id = 4 [(buf.validate.field).int32.gte = 0];

  // Error message if seek failed
  string error_message = 5 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 6;
}
```

---

### send_message_request.proto {#send_message_request}

**Path**: `gcommon/v1/queue/send_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `SendMessageRequest`

**Imports** (5):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/delivery_options.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/send_message_request.proto
// version: 1.0.0
// guid: 0acd1eb1-8464-4f9c-8fd2-0562acde190f
// SendMessageRequest sends a single message to a queue.

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/delivery_options.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SendMessageRequest {
  // Name of the target queue.
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Message to be enqueued.
  QueueMessage message = 2;

  // Optional delivery parameters.
  DeliveryOptions delivery_options = 3;

  // Standard request metadata.
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### send_message_response.proto {#send_message_response}

**Path**: `gcommon/v1/queue/send_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `SendMessageResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/send_message_response.proto
// version: 1.0.0
// guid: 2bbac133-fc81-4653-a03a-e5227ae81d4e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// SendMessageResponse contains the result of a send operation.
message SendMessageResponse {
  // Identifier of the queued message.
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the send operation succeeded.
  bool success = 2;

  // Position in the queue if known.
  int64 queue_position = 3 [(buf.validate.field).int64.gte = 0];

  // Error information when `success` is false.
  gcommon.v1.common.Error error = 4;
}
```

---

### start_workflow_request.proto {#start_workflow_request}

**Path**: `gcommon/v1/queue/start_workflow_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `StartWorkflowRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/start_workflow_request.proto
// version: 1.0.0
// guid: 2f3e4d5c-6b7a-8190-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StartWorkflowRequest defines the request for starting a workflow.
 */
message StartWorkflowRequest {
  // Workflow identifier
  string workflow_id = 1 [(buf.validate.field).string.min_len = 1];

  // Workflow definition or template
  string workflow_definition = 2 [(buf.validate.field).string.min_len = 1];

  // Input parameters for the workflow
  map<string, string> parameters = 3;
}
```

---

### start_workflow_response.proto {#start_workflow_response}

**Path**: `gcommon/v1/queue/start_workflow_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `StartWorkflowResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/start_workflow_response.proto
// version: 1.0.0
// guid: 3f4e5d6c-7b8a-9201-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StartWorkflowResponse defines the response from starting a workflow.
 */
message StartWorkflowResponse {
  // Workflow execution ID
  string execution_id = 1 [(buf.validate.field).string.min_len = 1];

  // Status of the workflow start
  string status = 2 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_workflow_request.proto {#stop_workflow_request}

**Path**: `gcommon/v1/queue/stop_workflow_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `StopWorkflowRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stop_workflow_request.proto
// version: 1.0.0
// guid: 4f5e6d7c-8b9a-0312-4e5f-6a7b8c9d0e1f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StopWorkflowRequest defines the request for stopping a workflow.
 */
message StopWorkflowRequest {
  // Workflow execution ID
  string execution_id = 1 [(buf.validate.field).string.min_len = 1];

  // Reason for stopping
  string reason = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### stop_workflow_response.proto {#stop_workflow_response}

**Path**: `gcommon/v1/queue/stop_workflow_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `StopWorkflowResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stop_workflow_response.proto
// version: 1.0.0
// guid: 5f6e7d8c-9b0a-1423-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * StopWorkflowResponse defines the response from stopping a workflow.
 */
message StopWorkflowResponse {
  // Status of the workflow stop
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### stream_messages_request.proto {#stream_messages_request}

**Path**: `gcommon/v1/queue/stream_messages_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 62

**Messages** (1): `StreamMessagesRequest`

**Imports** (6):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/queue/message_filter.proto`
- `gcommon/v1/queue/offset_config.proto`
- `gcommon/v1/queue/stream_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stream_messages_request.proto
// version: 1.0.0
// guid: 8571acf9-5131-45f6-b0ad-b227ce7f2980

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/queue/message_filter.proto";
import "gcommon/v1/queue/offset_config.proto";
import "gcommon/v1/queue/stream_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message StreamMessagesRequest {
  // Topic or queue identifier to stream from
  string topic = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer group ID for coordinated consumption
  string consumer_group_id = 2 [(buf.validate.field).string.min_len = 1];

  // Individual consumer ID within the group
  string consumer_id = 3 [(buf.validate.field).string.min_len = 1];

  // Starting offset configuration
  OffsetConfig offset_config = 4;

  // Maximum number of messages to stream
  int64 max_messages = 5 [(buf.validate.field).int64.gte = 0];

  // Maximum time to keep stream open (milliseconds)
  int32 stream_timeout_ms = 6 [(buf.validate.field).int32.gt = 0];

  // Acknowledgment level required
  gcommon.v1.common.AckLevel ack_level = 7;

  // Batch size for message delivery
  int32 batch_size = 8 [(buf.validate.field).int32.gte = 0];

  // Message filter criteria
  MessageFilter filter = 9;

  // Auto-acknowledge messages after delivery
  bool auto_acknowledge = 10;

  // Pause stream on error
  bool pause_on_error = 11;

  // Include message metadata in stream
  bool include_metadata = 12;

  // Specific partition IDs to stream from (empty = all partitions)
  repeated int32 partition_ids = 13 [(buf.validate.field).repeated.min_items = 1];

  // Stream configuration options
  StreamConfig stream_config = 14;
}
```

---

### stream_messages_response.proto {#stream_messages_response}

**Path**: `gcommon/v1/queue/stream_messages_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `StreamMessagesResponse`

**Imports** (3):

- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/stream_messages_response.proto
// file: proto/gcommon/v1/queue/stream_messages_response.proto
// version: 1.0.0
// guid: 4c5d6e7f-8a9b-0c1d-2e3f-4a5b6c7d8e9f
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for streaming messages from a queue.
 */
message StreamMessagesResponse {
  // List of messages in the stream
  repeated QueueMessage messages = 1 [(buf.validate.field).repeated.min_items = 1];

  // Whether there are more messages available
  bool has_more = 2;

  // Continuation token for next batch
  string continuation_token = 3 [(buf.validate.field).string.min_len = 1];

  // Total number of messages available
  uint64 total_messages = 4 [(buf.validate.field).uint64.gte = 0];

  // Current stream position
  uint64 stream_position = 5 [(buf.validate.field).uint64.gte = 0];

  // Whether the stream has ended
  bool stream_ended = 6;
}
```

---

### stream_metrics_request.proto {#stream_metrics_request}

**Path**: `gcommon/v1/queue/stream_metrics_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `QueueStreamMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/metric_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/stream_metrics_request.proto
// version: 1.0.0
// guid: 7ec20686-7f14-4488-9222-e6d189b494fe

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metric_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueStreamMetricsRequest {
  // Queue names to monitor (empty = all queues)
  repeated string queue_names = 1 [(buf.validate.field).repeated.min_items = 1];

  // Types of metrics to include
  repeated gcommon.v1.common.MetricsMetricType metric_types = 2 [(buf.validate.field).repeated.min_items = 1];

  // Streaming interval in seconds
  int32 interval_seconds = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### subscribe_request.proto {#subscribe_request}

**Path**: `gcommon/v1/queue/subscribe_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `QueueSubscribeRequest`

**Imports** (6):

- `gcommon/v1/queue/delivery_configuration.proto`
- `gcommon/v1/queue/error_handling_config.proto`
- `gcommon/v1/queue/message_filter_config.proto`
- `gcommon/v1/queue/subscription_configuration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscribe_request.proto
// version: 1.0.0
// guid: 6a573217-0297-4408-bcce-72b9172dd071

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/delivery_configuration.proto";
import "gcommon/v1/queue/error_handling_config.proto";
import "gcommon/v1/queue/message_filter_config.proto";
import "gcommon/v1/queue/subscription_configuration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueSubscribeRequest {
  // Topic or queue to subscribe to
  string topic = 1;

  // Subscription name/identifier
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Consumer group ID for coordinated consumption
  string consumer_group_id = 3;

  // Individual consumer ID
  string consumer_id = 4;

  // Subscription configuration
  SubscriptionConfiguration config = 5;

  // Message filtering criteria
  MessageFilterConfig filter_config = 6;

  // Delivery configuration
  DeliveryConfiguration delivery_config = 7;

  // Error handling configuration
  ErrorHandlingConfig error_handling = 8;

  // Subscription metadata
  map<string, string> metadata = 9;
}
```

---

### subscribe_response.proto {#subscribe_response}

**Path**: `gcommon/v1/queue/subscribe_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `SubscribeResponse`

**Imports** (5):

- `gcommon/v1/queue/connection_details.proto`
- `gcommon/v1/queue/partition_offset.proto`
- `gcommon/v1/queue/queue_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscribe_response.proto
// version: 1.0.0
// guid: 0d059538-5ecd-4438-9e3e-8aca86b7cf82
// Response for queue subscription with messages

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/connection_details.proto";
import "gcommon/v1/queue/partition_offset.proto";
import "gcommon/v1/queue/queue_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for subscription requests
message SubscribeResponse {
  // Message data
  QueueMessage message = 1;

  // Partition assignment info
  PartitionOffset partition_offset = 2;

  // Connection details for streaming
  ConnectionDetails connection_details = 3;

  // Subscription ID
  string subscription_id = 4 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### unsubscribe_request.proto {#unsubscribe_request}

**Path**: `gcommon/v1/queue/unsubscribe_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `QueueUnsubscribeRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/unsubscribe_request.proto
// version: 1.0.0
// guid: 69c55038-151d-4d97-a390-6bf4dc28d4aa
// Request to unsubscribe from a topic

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to unsubscribe from a topic
message QueueUnsubscribeRequest {
  // Subscription ID to unsubscribe
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer group ID
  string consumer_group_id = 2 [(buf.validate.field).string.min_len = 1];

  // Force unsubscribe even if messages are pending
  bool force = 3;

  // Close underlying connections
  bool close_connections = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### unsubscribe_response.proto {#unsubscribe_response}

**Path**: `gcommon/v1/queue/unsubscribe_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `UnsubscribeResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/unsubscribe_response.proto
// file: proto/gcommon/v1/queue/unsubscribe_response.proto
// version: 1.0.0
// guid: 5a4b3c2d-1e0f-9a8b-7c6d-5e4f3a2b1c0d
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for unsubscription operations.
 */
message UnsubscribeResponse {
  // Whether the unsubscription was successful
  bool success = 1;

  // Name of the subscription that was removed
  string subscription_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Timestamp when the unsubscription occurred
  google.protobuf.Timestamp unsubscribed_at = 3;

  // Number of pending messages that were lost due to unsubscription
  int64 lost_messages = 4;

  // Any warnings related to the unsubscription
  repeated string warnings = 5;
}
// This file needs proper implementation
```

---

### update_condition.proto {#update_condition}

**Path**: `gcommon/v1/queue/update_condition.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `UpdateCondition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_condition.proto
// version: 1.0.0
// guid: a5897f37-2d03-405d-b7c0-dc980257f2b4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateCondition {
  // Expected current version/etag
  string expected_version = 1 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Expected current state
  string expected_state = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum age for update (seconds)
  int64 max_age_seconds = 3 [(buf.validate.field).int64.gte = 0];

  // Update only if message hasn't been delivered
  bool only_if_not_delivered = 4;

  // Update only if message is visible
  bool only_if_visible = 5;

  // Custom condition expression
  string condition_expression = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_message_request.proto {#update_message_request}

**Path**: `gcommon/v1/queue/update_message_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 58

**Messages** (1): `UpdateMessageRequest`

**Imports** (8):

- `gcommon/v1/queue/content_update.proto`
- `gcommon/v1/queue/message_update_properties.proto`
- `gcommon/v1/queue/metadata_update.proto`
- `gcommon/v1/queue/priority_update.proto`
- `gcommon/v1/queue/update_condition.proto`
- `gcommon/v1/queue/visibility_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_message_request.proto
// version: 1.0.0
// guid: 78c4ac61-c4dc-4bfc-bfa1-93a723303fbb

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/content_update.proto";
import "gcommon/v1/queue/message_update_properties.proto";
import "gcommon/v1/queue/metadata_update.proto";
import "gcommon/v1/queue/priority_update.proto";
import "gcommon/v1/queue/update_condition.proto";
import "gcommon/v1/queue/visibility_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateMessageRequest {
  // Message identifier to update
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Topic or queue containing the message
  string topic = 2 [(buf.validate.field).string.min_len = 1];

  // Partition ID (if applicable)
  int32 partition_id = 3 [(buf.validate.field).int32.gte = 0];

  // Message offset (for precise identification)
  int64 message_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Updated message properties
  MessageUpdateProperties properties = 5;

  // Update visibility timeout for the message
  VisibilityUpdate visibility_update = 6;

  // Update message priority
  PriorityUpdate priority_update = 7;

  // Update message metadata
  MetadataUpdate metadata_update = 8;

  // Update message content (if allowed)
  ContentUpdate content_update = 9;

  // Specify which fields to update
  repeated string update_fields = 10 [(buf.validate.field).repeated.min_items = 1];

  // Conditional update based on current state
  UpdateCondition condition = 11;

  // Update operation metadata
  map<string, string> operation_metadata = 12;
}
```

---

### update_message_response.proto {#update_message_response}

**Path**: `gcommon/v1/queue/update_message_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `UpdateMessageResponse`

**Imports** (5):

- `gcommon/v1/queue/failed_field_update.proto`
- `gcommon/v1/queue/updated_properties.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_message_response.proto
// version: 1.0.0
// guid: f8af2c52-28d1-49c0-9813-a87e5f5a411d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/failed_field_update.proto";
import "gcommon/v1/queue/updated_properties.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateMessageResponse {
  // Success status of the update operation
  bool success = 1;

  // Updated message identifier
  string message_id = 2 [(buf.validate.field).string.min_len = 1];

  // New message version/etag after update
  string new_version = 3 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Timestamp when update was applied
  google.protobuf.Timestamp updated_at = 4;

  // Fields that were successfully updated
  repeated string updated_fields = 5 [(buf.validate.field).repeated.min_items = 1];

  // Fields that failed to update
  repeated FailedFieldUpdate failed_fields = 6 [(buf.validate.field).repeated.min_items = 1];

  // Error message if update failed
  string error_message = 7 [(buf.validate.field).string.min_len = 1];

  // Error code for programmatic handling
  string error_code = 8 [(buf.validate.field).string.min_len = 1];

  // Warning messages for partial updates
  repeated string warnings = 9 [(buf.validate.field).repeated.min_items = 1];

  // Updated message properties summary
  UpdatedProperties updated_properties = 10;

  // Operation metadata
  map<string, string> metadata = 11;
}
```

---

### acknowledgment.proto {#acknowledgment}

**Path**: `gcommon/v1/queue/acknowledgment.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `Acknowledgment`

**Imports** (4):

- `gcommon/v1/common/ack_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/acknowledgment.proto
// version: 1.1.0
// guid: c2d3e4f5-a6b7-8c9d-0e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Message acknowledgment information.
 * Tracks the processing status of consumed messages.
 */
message Acknowledgment {
  // Message ID being acknowledged
  string message_id = 1;

  // Consumer ID that processed the message
  string consumer_id = 2;

  // Queue or topic name
  string queue_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Partition ID (for partitioned queues)
  int32 partition_id = 4;

  // Message offset within the partition
  int64 offset = 5;

  // Acknowledgment type
  gcommon.v1.common.AckType ack_type = 6;

  // Timestamp when message was acknowledged
  google.protobuf.Timestamp ack_timestamp = 7;

  // Processing duration in milliseconds
  int64 processing_duration_ms = 8;

  // Error message if processing failed
  string error_message = 9;

  // Number of retry attempts made
  int32 retry_count = 10;
}
```

---

### age_bucket.proto {#age_bucket}

**Path**: `gcommon/v1/queue/age_bucket.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `AgeBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/age_bucket.proto
// version: 1.0.0
// guid: b9e2ab5f-72b7-4a4b-bade-21762099184a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AgeBucket {
  int64 min_age_seconds = 1 [(buf.validate.field).int64.gte = 0];
  int64 max_age_seconds = 2 [(buf.validate.field).int64.gte = 0];
  int64 message_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### age_distribution.proto {#age_distribution}

**Path**: `gcommon/v1/queue/age_distribution.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `AgeDistribution`

**Imports** (3):

- `gcommon/v1/queue/age_bucket.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/age_distribution.proto
// version: 1.0.0
// guid: 5599d940-19cf-4e9c-a4ce-d102c9c0ae57

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/age_bucket.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AgeDistribution {
  // Age buckets in seconds
  repeated AgeBucket buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Summary statistics
  double average_age_seconds = 2 [(buf.validate.field).double.gte = 0.0];
  double oldest_message_age_seconds = 3 [(buf.validate.field).double.gte = 0.0];
}
```

---

### alert_rule.proto {#alert_rule}

**Path**: `gcommon/v1/queue/alert_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `AlertRule`

**Imports** (5):

- `gcommon/v1/common/alert_condition.proto`
- `gcommon/v1/common/metrics_alert_severity.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alert_rule.proto
// version: 1.0.0
// guid: 5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/alert_condition.proto";
import "gcommon/v1/common/metrics_alert_severity.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * An individual alert rule.
 */
message AlertRule {
  // Unique name for the rule
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Human-readable description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Metric to monitor
  string metric_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Condition for triggering the alert
  gcommon.v1.common.AlertCondition condition = 4;

  // Threshold value
  double threshold = 5;

  // Duration the condition must persist before alerting
  google.protobuf.Duration duration = 6;

  // Severity of the alert
  gcommon.v1.common.MetricsAlertSeverity severity = 7;

  // Whether the rule is enabled
  bool enabled = 8;

  // Labels to attach to the alert
  map<string, string> labels = 9;
}
```

---

### anti_affinity_rule.proto {#anti_affinity_rule}

**Path**: `gcommon/v1/queue/anti_affinity_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `AntiAffinityRule`

**Imports** (3):

- `gcommon/v1/common/anti_affinity_scope.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/anti_affinity_rule.proto
// version: 1.0.0
// guid: a0d26ff8-7127-4e69-b8f3-eec85c695787

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/anti_affinity_scope.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Anti-affinity rule for replica placement.
 */
message AntiAffinityRule {
  // Label key to check for anti-affinity
  string label_key = 1 [(buf.validate.field).string.min_len = 1];

  // Label values that should not be co-located
  repeated string label_values = 2 [(buf.validate.field).repeated.min_items = 1];

  // Scope of the anti-affinity rule
  gcommon.v1.common.AntiAffinityScope scope = 3;
}
```

---

### api_key_auth.proto {#api_key_auth}

**Path**: `gcommon/v1/queue/api_key_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `APIKeyAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api_key_auth.proto
// version: 1.0.0
// guid: 4ac6d133-bd64-491e-8c17-2a716164dd87

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message APIKeyAuth {
  // API key for authentication
  string api_key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional API key ID
  string key_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### basic_queue_stats.proto {#basic_queue_stats}

**Path**: `gcommon/v1/queue/basic_queue_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 54

**Messages** (1): `BasicQueueStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/basic_queue_stats.proto
// file: proto/gcommon/v1/queue/basic_queue_stats.proto
// version: 1.0.0
// guid: 0e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Basic statistics for a queue.
 */
message BasicQueueStats {
  // Queue name
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Total number of messages in the queue
  uint64 total_messages = 2;

  // Number of unacknowledged messages
  uint64 unacked_messages = 3;

  // Queue size in bytes
  uint64 size_bytes = 4;

  // Number of consumers
  uint32 consumer_count = 5;

  // Number of producers
  uint32 producer_count = 6;

  // Messages per second (ingress rate)
  double ingress_rate = 7;

  // Messages per second (egress rate)
  double egress_rate = 8;

  // Average message size in bytes
  double avg_message_size = 9;

  // Queue depth (oldest unprocessed message age)
  uint64 queue_depth_ms = 10;
}
```

---

### binding_info.proto {#binding_info}

**Path**: `gcommon/v1/queue/binding_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `BindingInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/binding_info.proto
// file: proto/gcommon/v1/queue/binding_info.proto
// version: 1.0.0
// guid: 1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Information about queue and topic bindings.
 */
message BindingInfo {
  // Name of the binding
  string binding_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Source queue or topic name
  string source = 2;

  // Destination queue or topic name
  string destination = 3;

  // Routing key for the binding
  string routing_key = 4;

  // Arguments for the binding (key-value pairs)
  map<string, string> arguments = 5;

  // Whether the binding is durable
  bool durable = 6;

  // Whether to auto-delete when unused
  bool auto_delete = 7;

  // Binding type (direct, topic, fanout, headers)
  string binding_type = 8;

  // Creation timestamp
  uint64 created_at = 9;
}
```

---

### checksum_validation.proto {#checksum_validation}

**Path**: `gcommon/v1/queue/checksum_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ChecksumValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/checksum_validation.proto
// version: 1.0.0
// guid: 34bd9a2b-54d5-4c3e-aa17-382d38a98306

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ChecksumValidation {
  // Overall checksum validation passed
  bool passed = 1;

  // Expected checksum
  string expected_checksum = 2 [(buf.validate.field).string.min_len = 1];

  // Actual checksum
  string actual_checksum = 3 [(buf.validate.field).string.min_len = 1];

  // Checksum algorithm used
  string checksum_algorithm = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### cluster_health.proto {#cluster_health}

**Path**: `gcommon/v1/queue/cluster_health.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ClusterHealth`

**Imports** (3):

- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_health.proto
// version: 1.0.0
// guid: a0aa1fd8-9db2-427a-b5d5-359c620f271a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ClusterHealth {
  // Overall health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Number of healthy nodes
  int32 healthy_nodes = 2 [(buf.validate.field).int32.gte = 0];

  // Total number of nodes
  int32 total_nodes = 3 [(buf.validate.field).int32.gte = 0];

  // Health issues affecting the cluster
  repeated string issues = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### cluster_info.proto {#cluster_info}

**Path**: `gcommon/v1/queue/cluster_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 59

**Messages** (1): `ClusterInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_info.proto
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Cluster information for queue management.
 * Contains metadata about the message queue cluster.
 */
message ClusterInfo {
  // Cluster identifier
  string cluster_id = 1;

  // Cluster name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Cluster version
  string version = 3;

  // Number of nodes in cluster
  int32 node_count = 4;

  // Number of active brokers
  int32 active_brokers = 5;

  // Cluster status (healthy, degraded, offline)
  string status = 6;

  // Cluster uptime in seconds
  int64 uptime_seconds = 7;

  // Total topics in cluster
  int32 total_topics = 8;

  // Total partitions in cluster
  int32 total_partitions = 9;

  // Cluster leader node
  string leader_node = 10;

  // Cluster metadata
  map<string, string> metadata = 11 [lazy = true];

  // Last health check timestamp
  google.protobuf.Timestamp last_health_check = 12 [lazy = true];
}
```

---

### cluster_stats.proto {#cluster_stats}

**Path**: `gcommon/v1/queue/cluster_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ClusterStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_stats.proto
// version: 1.0.0
// guid: 6318f554-f8e9-434a-a33f-84ab2582e93c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics for the entire cluster.
 */
message ClusterStats {
  // Total number of queues across all nodes
  int64 total_queues = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of messages across all queues
  int64 total_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Total throughput (messages per second)
  double total_throughput = 3 [(buf.validate.field).double.gte = 0.0];

  // Number of active connections
  int64 active_connections = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### conflict_detection.proto {#conflict_detection}

**Path**: `gcommon/v1/queue/conflict_detection.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ConflictDetection`

**Imports** (4):

- `gcommon/v1/common/conflict_strategy.proto`
- `gcommon/v1/queue/timestamp_config.proto`
- `gcommon/v1/queue/vector_clock_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/conflict_detection.proto
// version: 1.0.1
// guid: 49cc6bab-66b1-4e09-9337-76d6644a2b81

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/conflict_strategy.proto";
import "gcommon/v1/queue/timestamp_config.proto";
import "gcommon/v1/queue/vector_clock_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConflictDetection {
  // Enable conflict detection
  bool enabled = 1;

  // Conflict detection strategy
  gcommon.v1.common.ConflictStrategy strategy = 2;

  // Vector clock configuration
  VectorClockConfig vector_clock = 3;

  // Timestamp-based detection settings
  TimestampConfig timestamp_config = 4;
}
```

---

### conflict_resolution.proto {#conflict_resolution}

**Path**: `gcommon/v1/queue/conflict_resolution.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `QueueConflictResolution`

**Imports** (5):

- `gcommon/v1/common/resolution_strategy.proto`
- `gcommon/v1/queue/custom_resolution.proto`
- `gcommon/v1/queue/last_writer_wins.proto`
- `gcommon/v1/queue/multi_value_config.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/conflict_resolution.proto
// version: 1.0.1
// guid: 6757adde-ed50-4ff7-9771-170223aaeca8

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/resolution_strategy.proto";
import "gcommon/v1/queue/custom_resolution.proto";
import "gcommon/v1/queue/last_writer_wins.proto";
import "gcommon/v1/queue/multi_value_config.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueConflictResolution {
  // Conflict resolution strategy
  gcommon.v1.common.ResolutionStrategy strategy = 1;

  // Custom resolution function settings
  CustomResolution custom_resolution = 2;

  // Last-writer-wins settings
  LastWriterWins lww_config = 3;

  // Multi-value conflict handling
  MultiValueConfig multi_value = 4;
}
```

---

### connection_details.proto {#connection_details}

**Path**: `gcommon/v1/queue/connection_details.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `ConnectionDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/connection_details.proto
// version: 1.0.0
// guid: e63faacd-909b-487c-9be3-1cba61d1e2c9
// Connection details for queue message delivery

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ConnectionDetails contains information for establishing message delivery connections
message ConnectionDetails {
  // Delivery endpoint (for push mode)
  string delivery_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Authentication token for delivery
  string auth_token = 2 [(buf.validate.field).string.min_len = 1];

  // Heartbeat interval (milliseconds)
  int32 heartbeat_interval_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Keep-alive timeout (milliseconds)
  int32 keep_alive_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // SSL/TLS configuration
  bool ssl_enabled = 5;

  // Connection metadata
  map<string, string> connection_metadata = 6;
}
```

---

### consistency_validation.proto {#consistency_validation}

**Path**: `gcommon/v1/queue/consistency_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ConsistencyValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consistency_validation.proto
// version: 1.0.0
// guid: ed16a632-9594-4189-90f8-2d0db13c7f9d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsistencyValidation {
  // Enable consistency validation
  bool enabled = 1;

  // Validation interval (seconds)
  int32 validation_interval_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Validation scope (local, cluster, global)
  string validation_scope = 3 [(buf.validate.field).string.min_len = 1];

  // Actions to take on validation failure
  repeated string failure_actions = 4 [(buf.validate.field).repeated.min_items = 1];

  // Validation timeout (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### consumer.proto {#consumer}

**Path**: `gcommon/v1/queue/consumer.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `Consumer`

**Imports** (7):

- `gcommon/v1/common/consumer_state.proto`
- `gcommon/v1/queue/consumer_client.proto`
- `gcommon/v1/queue/consumer_config.proto`
- `gcommon/v1/queue/consumer_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer.proto
// version: 1.0.0
// guid: 1bb92667-7d61-4aea-b8df-a372aa46cf8a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/consumer_state.proto";
import "gcommon/v1/queue/consumer_client.proto";
import "gcommon/v1/queue/consumer_config.proto";
import "gcommon/v1/queue/consumer_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message Consumer {
  // Unique consumer identifier
  string consumer_id = 1 [(buf.validate.field).string.min_len = 1];

  // Consumer client information
  ConsumerClient client_info = 2;

  // Consumer state
  gcommon.v1.common.ConsumerState state = 3;

  // Assigned partitions
  repeated int32 assigned_partitions = 4 [(buf.validate.field).repeated.min_items = 1];

  // Consumer configuration
  ConsumerConfig config = 5;

  // Consumer statistics
  ConsumerStats stats = 6;

  // Last heartbeat timestamp
  google.protobuf.Timestamp last_heartbeat = 7;

  // Join timestamp
  google.protobuf.Timestamp joined_at = 8;
}
```

---

### consumer_client.proto {#consumer_client}

**Path**: `gcommon/v1/queue/consumer_client.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ConsumerClient`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_client.proto
// version: 1.0.0
// guid: 30ccc081-9c0b-470f-8c9a-fcc26b8b9cde

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerClient {
  // Client ID
  string client_id = 1 [(buf.validate.field).string.min_len = 1];

  // Client host/IP address
  string client_host = 2 [(buf.validate.field).string.min_len = 1];

  // Client application name
  string client_app = 3 [(buf.validate.field).string.min_len = 1];

  // Client version
  string client_version = 4 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Client rack (for rack-aware assignment)
  string client_rack = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### consumer_error_stats.proto {#consumer_error_stats}

**Path**: `gcommon/v1/queue/consumer_error_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `ConsumerErrorStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_error_stats.proto
// version: 1.0.0
// guid: 1d9e7970-3641-4541-a107-2c4736fa88be

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerErrorStats {
  // Total processing errors
  int64 total_errors = 1 [(buf.validate.field).int64.gte = 0];

  // Connection errors
  int64 connection_errors = 2 [(buf.validate.field).int64.gte = 0];

  // Timeout errors
  int64 timeout_errors = 3 [(buf.validate.field).int64.gt = 0];

  // Serialization errors
  int64 serialization_errors = 4 [(buf.validate.field).int64.gte = 0];

  // Last error timestamp
  google.protobuf.Timestamp last_error = 5;
}
```

---

### consumer_group.proto {#consumer_group}

**Path**: `gcommon/v1/queue/consumer_group.proto` **Package**: `gcommon.v1.queue` **Lines**: 61

**Messages** (1): `ConsumerGroup`

**Imports** (9):

- `gcommon/v1/common/consumer_group_state.proto`
- `gcommon/v1/queue/consumer.proto`
- `gcommon/v1/queue/consumer_group_config.proto`
- `gcommon/v1/queue/consumer_group_stats.proto`
- `gcommon/v1/queue/group_coordinator.proto`
- `gcommon/v1/queue/partition_assignment.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group.proto
// version: 1.0.0
// guid: 04a92687-cec2-4eac-a15d-f6f0c884eab3

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/consumer_group_state.proto";
import "gcommon/v1/queue/consumer.proto";
import "gcommon/v1/queue/consumer_group_config.proto";
import "gcommon/v1/queue/consumer_group_stats.proto";
import "gcommon/v1/queue/group_coordinator.proto";
import "gcommon/v1/queue/partition_assignment.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerGroup {
  // Unique identifier for the consumer group
  string group_id = 1;

  // Group name (human-readable)
  string group_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic or queue this group is consuming from
  string topic = 3;

  // Consumer group configuration
  ConsumerGroupConfig config = 4;

  // Current group state
  gcommon.v1.common.ConsumerGroupState state = 5;

  // List of active consumers in the group
  repeated Consumer consumers = 6;

  // Partition assignments
  repeated PartitionAssignment partition_assignments = 7;

  // Group coordinator information
  GroupCoordinator coordinator = 8;

  // Consumer group statistics
  ConsumerGroupStats stats = 9;

  // Group metadata
  map<string, string> metadata = 10;

  // Creation timestamp
  google.protobuf.Timestamp created_at = 11 [ (buf.validate.field).required = true ];

  // Last updated timestamp
  google.protobuf.Timestamp updated_at = 12;
}
```

---

### consumer_group_stats.proto {#consumer_group_stats}

**Path**: `gcommon/v1/queue/consumer_group_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `ConsumerGroupStats`

**Imports** (4):

- `gcommon/v1/queue/consumer_error_stats.proto`
- `gcommon/v1/queue/rebalance_stats.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group_stats.proto
// version: 1.0.0
// guid: b8b6993f-38ea-4912-8d9b-b5d70c3968fc

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/consumer_error_stats.proto";
import "gcommon/v1/queue/rebalance_stats.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerGroupStats {
  // Total number of active consumers
  int32 active_consumers = 1 [(buf.validate.field).int32.gte = 0];

  // Total number of assigned partitions
  int32 assigned_partitions = 2 [(buf.validate.field).int32.gte = 0];

  // Total messages consumed by the group
  int64 total_messages_consumed = 3 [(buf.validate.field).int64.gte = 0];

  // Total bytes consumed by the group
  int64 total_bytes_consumed = 4 [(buf.validate.field).int64.gte = 0];

  // Average group consumption rate (messages/second)
  double group_consumption_rate = 5 [(buf.validate.field).double.gte = 0.0];

  // Total group lag
  int64 total_lag = 6 [(buf.validate.field).int64.gte = 0];

  // Rebalance statistics
  RebalanceStats rebalance_stats = 7;

  // Error statistics for the consumer group
  ConsumerErrorStats error_stats = 8;
}
```

---

### consumer_stats.proto {#consumer_stats}

**Path**: `gcommon/v1/queue/consumer_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ConsumerStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_stats.proto
// version: 1.0.0
// guid: f4a5b6c7-890d-234e-5678-890123456789

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerStats {
  // Consumer ID
  string consumer_id = 1 [(buf.validate.field).string.min_len = 1];

  // Messages processed
  int64 messages_processed = 2 [(buf.validate.field).int64.gte = 0];

  // Processing rate per second
  double processing_rate = 3 [(buf.validate.field).double.gte = 0.0];

  // Error count
  int64 error_count = 4 [(buf.validate.field).int64.gte = 0];

  // Last active timestamp
  int64 last_active = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### content_filter.proto {#content_filter}

**Path**: `gcommon/v1/queue/content_filter.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ContentFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/content_filter.proto
// version: 1.0.0
// guid: 54ce7d22-49b5-4c41-86a5-4a5156d1e74b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ContentFilter {
  // JSON path or field name
  string field_path = 1 [(buf.validate.field).string.min_len = 1];

  // Filter operator (equals, contains, regex, gt, lt, etc.)
  string operator = 2 [(buf.validate.field).string.min_len = 1];

  // Filter value
  string value = 3 [(buf.validate.field).string.min_len = 1];

  // Case sensitive matching
  bool case_sensitive = 4;
}
```

---

### content_update.proto {#content_update}

**Path**: `gcommon/v1/queue/content_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `ContentUpdate`

**Imports** (3):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/content_update.proto
// version: 1.0.0
// guid: 9acab812-6e9a-44f3-8206-8aee653ad5da

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ContentUpdate {
  // New message payload
  google.protobuf.Any new_payload = 1;

  // Content encoding
  string content_encoding = 2 [(buf.validate.field).string.min_len = 1];

  // Content type
  string content_type = 3 [(buf.validate.field).string.min_len = 1];

  // Compression applied to content
  string compression = 4 [(buf.validate.field).string.min_len = 1];

  // Checksum of new content
  string content_checksum = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### custom_resolution.proto {#custom_resolution}

**Path**: `gcommon/v1/queue/custom_resolution.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `CustomResolution`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/custom_resolution.proto
// version: 1.0.0
// guid: 94eb8c9d-f368-4910-9841-128a9ceee9c8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message CustomResolution {
  // Resolution function name or identifier
  string function_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Function parameters
  map<string, string> parameters = 2;

  // Timeout for resolution function (milliseconds)
  int32 timeout_ms = 3;
}
```

---

### dead_letter_policy.proto {#dead_letter_policy}

**Path**: `gcommon/v1/queue/dead_letter_policy.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `DeadLetterPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/dead_letter_policy.proto
// file: proto/gcommon/v1/queue/dead_letter_policy.proto
// version: 1.0.0
// guid: 5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Dead letter policy configuration for handling failed messages.
 * Messages that exceed retry limits or cannot be processed will be
 * sent to a dead letter queue for manual inspection.
 */
message DeadLetterPolicy {
  // Name of the dead letter queue where failed messages will be sent
  string dead_letter_queue = 1 [(buf.validate.field).string.min_len = 1];

  // Maximum number of delivery attempts before sending to dead letter queue
  int32 max_delivery_attempts = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum age of a message before it's considered expired and sent to DLQ
  google.protobuf.Duration max_message_age = 3;

  // Whether to include the original failure reason in the dead letter message
  bool include_failure_reason = 4;

  // Additional metadata to attach to dead letter messages
  map<string, string> dead_letter_metadata = 5;

  // Whether dead letter policy is enabled
  bool enabled = 6;
}
```

---

### deletion_stats.proto {#deletion_stats}

**Path**: `gcommon/v1/queue/deletion_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `DeletionStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/deletion_stats.proto
// version: 1.0.0
// guid: 671eaddd-dddd-48e2-8910-428b3f80a7d1

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeletionStats {
  // Number of messages deleted
  int64 messages_deleted = 1 [(buf.validate.field).int64.gte = 0];

  // Amount of data deleted (bytes)
  int64 data_deleted_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Number of subscriptions deleted
  int32 subscriptions_deleted = 3 [(buf.validate.field).int32.gte = 0];

  // Number of partitions deleted
  int32 partitions_deleted = 4 [(buf.validate.field).int32.gte = 0];

  // Time taken for deletion (milliseconds)
  int64 deletion_duration_ms = 5 [(buf.validate.field).int64.gt = 0];
}
```

---

### delivery_options.proto {#delivery_options}

**Path**: `gcommon/v1/queue/delivery_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `DeliveryOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_options.proto
// version: 1.0.0
// guid: 226d4794-23ca-4b54-9a0d-7c6671093c04

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// DeliveryOptions control message routing and retries.
message DeliveryOptions {
  // Optional delivery delay.
  google.protobuf.Duration delay = 1;

  // Maximum retry attempts before sending to dead letter queue.
  int32 max_retries = 2 [(buf.validate.field).int32.gte = 0];

  // Delay between retry attempts.
  google.protobuf.Duration retry_delay = 3;

  // Multiplier for exponential backoff.
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Maximum delay allowed between retries.
  google.protobuf.Duration max_retry_delay = 5;

  // Name of the dead letter queue.
  string dead_letter_queue = 6 [(buf.validate.field).string.min_len = 1];

  // Whether acknowledgment is required for delivery.
  bool require_ack = 7;

  // Timeout waiting for acknowledgment.
  google.protobuf.Duration ack_timeout = 8;
}
```

---

### delivery_settings.proto {#delivery_settings}

**Path**: `gcommon/v1/queue/delivery_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `DeliverySettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_settings.proto
// version: 1.0.0
// guid: 90fc8ba9-b70c-41e9-afaf-a90b7097d4dd

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeliverySettings {
  // Delivery mode (push, pull, streaming)
  string delivery_mode = 1 [(buf.validate.field).string.min_len = 1];

  // Endpoint for push delivery
  string push_endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Delivery timeout (milliseconds)
  int32 delivery_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Enable ordered delivery
  bool ordered_delivery = 4;
}
```

---

### encryption_info.proto {#encryption_info}

**Path**: `gcommon/v1/queue/encryption_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `EncryptionInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/encryption_info.proto
// version: 1.0.0
// guid: 79dc45f4-d25b-40cb-8380-45f54e170aa7

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message EncryptionInfo {
  // Encryption enabled
  bool enabled = 1;

  // Encryption algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Key management service
  string kms_provider = 3 [(buf.validate.field).string.min_len = 1];

  // Key identifier
  string key_id = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### error_stats.proto {#error_stats}

**Path**: `gcommon/v1/queue/error_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `QueueErrorStats`

**Imports** (3):

- `gcommon/v1/queue/error_type_stat.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_stats.proto
// version: 1.0.0
// guid: f679dd1a-539c-42a7-aa4e-0c14ef8adac2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/error_type_stat.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueErrorStats {
  int64 total_errors = 1 [(buf.validate.field).int64.gte = 0];
  double error_rate = 2 [(buf.validate.field).double.gte = 0.0];
  repeated ErrorTypeStat error_types = 3 [(buf.validate.field).repeated.min_items = 1];
  repeated string recent_error_messages = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### error_type_stat.proto {#error_type_stat}

**Path**: `gcommon/v1/queue/error_type_stat.proto` **Package**: `gcommon.v1.queue` **Lines**: 21

**Messages** (1): `ErrorTypeStat`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_type_stat.proto
// version: 1.0.0
// guid: 14988398-e55c-484b-a755-0e18d26b7d8f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorTypeStat {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double rate = 3 [(buf.validate.field).double.gte = 0.0];
  string last_occurrence = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### external_role_provider.proto {#external_role_provider}

**Path**: `gcommon/v1/queue/external_role_provider.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ExternalRoleProvider`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/external_role_provider.proto
// version: 1.0.0
// guid: 890e55e1-8627-452f-95dc-f799e0316fec

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ExternalRoleProvider {
  // Provider type (ldap, oauth, etc.)
  string provider_type = 1 [(buf.validate.field).string.min_len = 1];

  // Provider endpoint URL
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Authentication credentials for provider
  map<string, string> credentials = 3;

  // Cache TTL for role lookups (seconds)
  int32 cache_ttl_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### failed_ack.proto {#failed_ack}

**Path**: `gcommon/v1/queue/failed_ack.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `FailedAck`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/failed_ack.proto
// version: 1.0.0
// guid: 576df787-4718-4249-a439-b368117dec41

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FailedAck {
  // Message ID that failed to acknowledge
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Reason for acknowledgment failure
  string error_reason = 2 [(buf.validate.field).string.min_len = 1];

  // Error code
  string error_code = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### failed_field_update.proto {#failed_field_update}

**Path**: `gcommon/v1/queue/failed_field_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `FailedFieldUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/failed_field_update.proto
// version: 1.0.0
// guid: 3fbfa5f5-c2fc-4c93-9fec-823125628ddb

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FailedFieldUpdate {
  // Field name that failed to update
  string field_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Reason for failure
  string failure_reason = 2;

  // Error code specific to this field
  string error_code = 3;

  // Original value that couldn't be updated
  string original_value = 4;

  // Attempted new value
  string attempted_value = 5;
}
```

---

### filter_criteria.proto {#filter_criteria}

**Path**: `gcommon/v1/queue/filter_criteria.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `FilterCriteria`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/filter_criteria.proto
// version: 1.0.0
// guid: 202f243e-e814-4448-8117-d5f74fc966a0

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FilterCriteria {
  // Include message patterns
  repeated string include_patterns = 1 [(buf.validate.field).repeated.min_items = 1];

  // Exclude message patterns
  repeated string exclude_patterns = 2 [(buf.validate.field).repeated.min_items = 1];

  // Header-based filters
  map<string, string> header_filters = 3;

  // Content-type filters
  repeated string content_types = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### filter_settings.proto {#filter_settings}

**Path**: `gcommon/v1/queue/filter_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `FilterSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/filter_settings.proto
// version: 1.0.0
// guid: aae01edc-d403-456d-9c93-e9f4c0c8c699

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FilterSettings {
  // Content-based filters
  map<string, string> content_filters = 1;

  // Header-based filters
  map<string, string> header_filters = 2;

  // Filter expression
  string filter_expression = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### flow_control.proto {#flow_control}

**Path**: `gcommon/v1/queue/flow_control.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `FlowControl`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flow_control.proto
// version: 1.0.0
// guid: 40b0fde3-4f0f-4bef-b893-248588fbf4a6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// FlowControl settings influence how the queue handles
// bursts of incoming messages.
message FlowControl {
  // Maximum number of unacknowledged messages allowed.
  int32 max_in_flight = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum amount of data in flight (bytes).
  int64 max_bytes_in_flight = 2 [(buf.validate.field).int64.gte = 0];

  // Deadline before a message is redelivered if not acknowledged.
  google.protobuf.Duration ack_deadline = 3;
}
```

---

### flow_control_settings.proto {#flow_control_settings}

**Path**: `gcommon/v1/queue/flow_control_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `FlowControlSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flow_control_settings.proto
// version: 1.0.0
// guid: 072cab5f-9831-4a0e-8727-f69e8354fe4a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FlowControlSettings {
  // Maximum outstanding messages
  int32 max_outstanding_messages = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // Flow control algorithm
  string algorithm = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### format_options.proto {#format_options}

**Path**: `gcommon/v1/queue/format_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `FormatOptions`

**Imports** (4):

- `gcommon/v1/common/compression_algorithm.proto`
- `gcommon/v1/common/serialization_format.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/format_options.proto
// version: 1.0.0
// guid: be0dbb05-7495-4e4c-b7c7-97774a7e0489

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/compression_algorithm.proto";
import "gcommon/v1/common/serialization_format.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Serialization options for a specific format.
 */
message FormatOptions {
  // Serialization format
  gcommon.v1.common.SerializationFormat format = 1;

  // Format-specific configuration
  map<string, string> options = 2;

  // Whether to enable compression for this format
  bool enable_compression = 3;

  // Compression algorithm
  gcommon.v1.common.CompressionAlgorithm compression_algorithm = 4;

  // Maximum message size for this format
  int64 max_message_size = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### group_coordinator.proto {#group_coordinator}

**Path**: `gcommon/v1/queue/group_coordinator.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `GroupCoordinator`

**Imports** (3):

- `gcommon/v1/common/coordinator_state.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/group_coordinator.proto
// version: 1.0.0
// guid: e3e0d17b-a593-44ec-a32c-8b282cf136fc

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/coordinator_state.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message GroupCoordinator {
  // Coordinator node ID
  string node_id = 1 [(buf.validate.field).string.min_len = 1];

  // Coordinator host
  string host = 2 [(buf.validate.field).string.min_len = 1];

  // Coordinator port
  int32 port = 3 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Coordinator state
  gcommon.v1.common.CoordinatorState state = 4;

  // Leadership epoch
  int64 epoch = 5 [(buf.validate.field).int64.gte = 0];
}
```

---

### historical_data_point.proto {#historical_data_point}

**Path**: `gcommon/v1/queue/historical_data_point.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `HistoricalDataPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/historical_data_point.proto
// version: 1.0.0
// guid: 8e947e6d-7509-4f8b-931c-cb36d515b5e5

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message HistoricalDataPoint {
  google.protobuf.Timestamp timestamp = 1;
  int64 message_count = 2 [(buf.validate.field).int64.gte = 0];
  double throughput = 3 [(buf.validate.field).double.gte = 0.0];
  double average_latency_ms = 4 [(buf.validate.field).double.gte = 0.0];
  double error_rate = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### historical_stats.proto {#historical_stats}

**Path**: `gcommon/v1/queue/historical_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 21

**Messages** (1): `HistoricalStats`

**Imports** (4):

- `gcommon/v1/queue/historical_data_point.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/historical_stats.proto
// version: 1.0.0
// guid: 7e6ca4d3-82ff-42f7-9761-fbb25977f58d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/historical_data_point.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message HistoricalStats {
  repeated HistoricalDataPoint data_points = 1 [(buf.validate.field).repeated.min_items = 1];
  google.protobuf.Duration aggregation_period = 2;
}
```

---

### integrity_validation.proto {#integrity_validation}

**Path**: `gcommon/v1/queue/integrity_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `IntegrityValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/integrity_validation.proto
// version: 1.0.0
// guid: 98819329-10f2-4edf-85cb-52919123d92f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message IntegrityValidation {
  // Integrity validation passed
  bool passed = 1;

  // Corrupted message count
  int64 corrupted_messages = 2 [(buf.validate.field).int64.gte = 0];

  // Missing message count
  int64 missing_messages = 3 [(buf.validate.field).int64.gte = 0];

  // Duplicate message count
  int64 duplicate_messages = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### jwt_auth.proto {#jwt_auth}

**Path**: `gcommon/v1/queue/jwt_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `JwtAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/jwt_auth.proto
// version: 1.0.0
// guid: 105a22e1-20d6-4414-9bf3-36161857c31d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message JwtAuth {
  // Enable JWT authentication
  bool enabled = 1;

  // JWT signing algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Public key or secret for verification
  string verification_key = 3 [(buf.validate.field).string.min_len = 1];

  // Expected issuer
  string expected_issuer = 4 [(buf.validate.field).string.min_len = 1];

  // Expected audience
  repeated string expected_audience = 5 [(buf.validate.field).repeated.min_items = 1];

  // Clock skew tolerance (seconds)
  int32 clock_skew_seconds = 6 [(buf.validate.field).int32.gte = 0];

  // Required claims
  map<string, string> required_claims = 7;
}
```

---

### last_writer_wins.proto {#last_writer_wins}

**Path**: `gcommon/v1/queue/last_writer_wins.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `LastWriterWins`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/last_writer_wins.proto
// version: 1.0.1
// guid: 39e817ba-1ee6-4093-97a2-d4fda4de5312

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message LastWriterWins {
  // Use server timestamp instead of client timestamp
  bool use_server_timestamp = 1;

  // Timestamp precision for comparison
  string timestamp_precision = 2;
}
```

---

### latency_metrics.proto {#latency_metrics}

**Path**: `gcommon/v1/queue/latency_metrics.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `LatencyMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/latency_metrics.proto
// version: 1.0.0
// guid: 3e90b50a-4d0c-440a-911c-75bf6da02e43

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message LatencyMetrics {
  // Processing latency percentiles (in milliseconds)
  double p50_processing_latency_ms = 1 [(buf.validate.field).double.gte = 0.0];
  double p95_processing_latency_ms = 2 [(buf.validate.field).double.gte = 0.0];
  double p99_processing_latency_ms = 3 [(buf.validate.field).double.gte = 0.0];

  // Queue latency (time from enqueue to dequeue)
  double average_queue_latency_ms = 4 [(buf.validate.field).double.gte = 0.0];
  double p95_queue_latency_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // End-to-end latency (enqueue to completion)
  double average_e2e_latency_ms = 6 [(buf.validate.field).double.gte = 0.0];
  double p95_e2e_latency_ms = 7 [(buf.validate.field).double.gte = 0.0];
}
```

---

### message_ack_result.proto {#message_ack_result}

**Path**: `gcommon/v1/queue/message_ack_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `MessageAckResult`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_ack_result.proto
// version: 1.0.0
// guid: d7c68f75-1f4d-4758-ba66-a6aaa0dcf1a4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageAckResult {
  /**
   * Receipt handle of the message this result applies to.
   */
  string receipt_handle = 1 [(buf.validate.field).string.min_len = 1];

  /**
   * Whether this specific message was successfully acknowledged.
   */
  bool success = 2;

  /**
   * Error information if acknowledgment failed for this message.
   */
  gcommon.v1.common.Error error = 3;

  /**
   * Message ID for correlation (if available).
   */
  string message_id = 4 [(buf.validate.field).string.min_len = 1];

  /**
   * Processing result that was recorded (echoed from request).
   */
  string processing_result = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_envelope.proto {#message_envelope}

**Path**: `gcommon/v1/queue/message_envelope.proto` **Package**: `gcommon.v1.queue` **Lines**: 66

**Messages** (1): `MessageEnvelope`

**Imports** (4):

- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/message_envelope.proto
// file: proto/gcommon/v1/queue/message_envelope.proto
// version: 1.0.0
// guid: 2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Message envelope that wraps the actual message payload with metadata.
 * This is the container that gets stored and transmitted through the queue system.
 */
message MessageEnvelope {
  // Unique identifier for this message
  string message_id = 1;

  // The actual message payload
  google.protobuf.Any payload = 2;

  // Message headers for routing and metadata
  map<string, string> headers = 3;

  // Priority of the message (higher numbers = higher priority)
  int32 priority = 4;

  // Timestamp when the message was created
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // Timestamp when the message should be processed (for delayed messages)
  google.protobuf.Timestamp process_at = 6;

  // Timestamp when the message expires
  google.protobuf.Timestamp expires_at = 7;

  // Number of delivery attempts for this message
  int32 delivery_count = 8;

  // Correlation ID for linking related messages
  string correlation_id = 9;

  // Reply-to queue for response messages
  string reply_to = 10;

  // Content type of the payload
  string content_type = 11;

  // Encoding of the payload (e.g., "gzip", "none")
  string content_encoding = 12;

  // Whether this message requires acknowledgment
  bool requires_ack = 13;

  // Trace context for distributed tracing
  map<string, string> trace_context = 14;
}
```

---

### message_filter.proto {#message_filter}

**Path**: `gcommon/v1/queue/message_filter.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `MessageFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_filter.proto
// version: 1.0.0
// guid: 705dd4ef-6cef-458f-b70b-588f3e13eda0

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageFilter {
  // Filter by message headers
  map<string, string> header_filters = 1;

  // Filter by message properties
  map<string, string> property_filters = 2;

  // Minimum message priority
  int32 min_priority = 3 [(buf.validate.field).int32.gte = 0];

  // Maximum message age (seconds)
  int32 max_age_seconds = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Content type filter
  string content_type = 5 [(buf.validate.field).string.min_len = 1];

  // Custom filter expression
  string filter_expression = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_id.proto {#message_id}

**Path**: `gcommon/v1/queue/message_id.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `MessageId`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_id.proto
// version: 1.0.0
// guid: 9bd8b62d-3655-4ff5-9f3a-4d5da241dc77

// MessageId is a simple wrapper type used for referencing messages
// in a type-safe manner across the Queue API. This replaces the
// placeholder created during the migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// MessageId uniquely identifies a message within a queue.
// It can be referenced by other messages or API calls.
message MessageId {
  // Opaque identifier assigned by the queue implementation.
  string value = 1 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_metadata.proto {#message_metadata}

**Path**: `gcommon/v1/queue/message_metadata.proto` **Package**: `gcommon.v1.queue` **Lines**: 56

**Messages** (1): `MessageMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/message_metadata.proto
// file: proto/gcommon/v1/queue/message_metadata.proto
// version: 1.0.0
// guid: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Metadata associated with a queue message.
 */
message MessageMetadata {
  // Unique message identifier
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Message timestamp
  google.protobuf.Timestamp timestamp = 2;

  // Producer/sender identifier
  string producer_id = 3 [(buf.validate.field).string.min_len = 1];

  // Content type of the message
  string content_type = 4 [(buf.validate.field).string.min_len = 1];

  // Content encoding (gzip, deflate, etc.)
  string content_encoding = 5 [(buf.validate.field).string.min_len = 1];

  // Message priority (0-255, higher is more priority)
  uint32 priority = 6 [(buf.validate.field).uint32.gte = 0];

  // Time-to-live in milliseconds
  uint64 ttl_ms = 7 [(buf.validate.field).uint64.gte = 0];

  // Custom headers
  map<string, string> headers = 8;

  // Routing key
  string routing_key = 9 [(buf.validate.field).string.min_len = 1];

  // Correlation ID for request-response patterns
  string correlation_id = 10 [(buf.validate.field).string.min_len = 1];

  // Reply-to address
  string reply_to = 11 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_nack.proto {#message_nack}

**Path**: `gcommon/v1/queue/message_nack.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `MessageNack`

**Imports** (3):

- `gcommon/v1/common/nack_error_category.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_nack.proto
// version: 1.0.0
// guid: b5bb9e75-3346-4684-9529-764a3cdb3e3d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/nack_error_category.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageNack {
  // Message identifier
  string message_id = 1 [(buf.validate.field).string.min_len = 1];

  // Message delivery tag
  string delivery_tag = 2 [(buf.validate.field).string.min_len = 1];

  // Partition ID containing the message
  int32 partition_id = 3 [(buf.validate.field).int32.gte = 0];

  // Message offset
  int64 message_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Reason for negative acknowledgment
  string nack_reason = 5 [(buf.validate.field).string.min_len = 1];

  // Error category for the nack
  gcommon.v1.common.NackErrorCategory error_category = 6;

  // Specific error code
  string error_code = 7 [(buf.validate.field).string.min_len = 1];

  // Retry this specific message
  bool retry_message = 8;

  // Custom retry delay for this message (milliseconds)
  int64 retry_delay_ms = 9 [(buf.validate.field).int64.gte = 0];

  // Message-specific metadata
  map<string, string> message_metadata = 10;
}
```

---

### message_properties.proto {#message_properties}

**Path**: `gcommon/v1/queue/message_properties.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `MessageProperties`

**Imports** (5):

- `gcommon/v1/common/delivery_mode.proto`
- `gcommon/v1/common/priority_level.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_properties.proto
// version: 1.0.0
// guid: 57ef0850-feeb-42b0-b724-f14b542cfd08

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/delivery_mode.proto";
import "gcommon/v1/common/priority_level.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageProperties {
  // Message priority level
  gcommon.v1.common.PriorityLevel priority = 1;

  // Delivery mode for the message
  gcommon.v1.common.DeliveryMode delivery_mode = 2;

  // Message expiration time
  google.protobuf.Timestamp expiration_time = 3;

  // Correlation ID for request-response patterns
  string correlation_id = 4 [(buf.validate.field).string.min_len = 1];

  // Reply-to address/topic
  string reply_to = 5 [(buf.validate.field).string.min_len = 1];

  // Content type of the payload
  string content_type = 6 [(buf.validate.field).string.min_len = 1];

  // Content encoding
  string content_encoding = 7 [(buf.validate.field).string.min_len = 1];

  // Compression applied to payload
  string compression = 8 [(buf.validate.field).string.min_len = 1];

  // Message deduplication ID
  string deduplication_id = 9 [(buf.validate.field).string.min_len = 1];

  // Delay before message becomes available (milliseconds)
  int64 delivery_delay_ms = 10 [(buf.validate.field).int64.gte = 0];
}
```

---

### message_state_counts.proto {#message_state_counts}

**Path**: `gcommon/v1/queue/message_state_counts.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `MessageStateCounts`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_state_counts.proto
// version: 1.0.0
// guid: ed6cdf6e-a32e-4ea4-942c-92e90ea2d061

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageStateCounts {
  int64 pending = 1 [(buf.validate.field).int64.gte = 0];
  int64 processing = 2 [(buf.validate.field).int64.gte = 0];
  int64 completed = 3 [(buf.validate.field).int64.gte = 0];
  int64 failed = 4 [(buf.validate.field).int64.gte = 0];
  int64 retrying = 5 [(buf.validate.field).int64.gte = 0];
  int64 dead_letter = 6 [(buf.validate.field).int64.gte = 0];
}
```

---

### message_update_properties.proto {#message_update_properties}

**Path**: `gcommon/v1/queue/message_update_properties.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `MessageUpdateProperties`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_update_properties.proto
// version: 1.0.0
// guid: db9a2627-8ff1-4dc6-b551-e15416cd3bbe

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageUpdateProperties {
  // New expiration time
  google.protobuf.Timestamp expiration_time = 1;

  // New delivery delay
  int64 delivery_delay_ms = 2 [(buf.validate.field).int64.gte = 0];

  // New retry count
  int32 retry_count = 3 [(buf.validate.field).int32.gte = 0];

  // New routing key
  string routing_key = 4 [(buf.validate.field).string.min_len = 1];

  // New correlation ID
  string correlation_id = 5 [(buf.validate.field).string.min_len = 1];

  // New reply-to address
  string reply_to = 6 [(buf.validate.field).string.min_len = 1];

  // Updated message headers
  map<string, string> headers = 7;
}
```

---

### metadata_update.proto {#metadata_update}

**Path**: `gcommon/v1/queue/metadata_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `MetadataUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/metadata_update.proto
// version: 1.0.0
// guid: 6cb1a95a-0fdd-464d-a156-b7cff3414a7d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MetadataUpdate {
  // Metadata fields to add or update
  map<string, string> add_metadata = 1;

  // Metadata fields to remove
  repeated string remove_metadata = 2;

  // Replace all metadata with new values
  map<string, string> replace_metadata = 3;

  // Update operation (add, remove, replace)
  string operation_type = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### nack_error.proto {#nack_error}

**Path**: `gcommon/v1/queue/nack_error.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `NackError`

**Imports** (3):

- `gcommon/v1/common/nack_error_category.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/nack_error.proto
// version: 1.0.0
// guid: 9c0d1e2f-3a4b-5c6d-7e8f-9a0b1c2d3e4f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/nack_error_category.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Error information for NACK operations.
 */
message NackError {
  // Error code
  string code = 1 [(buf.validate.field).string.min_len = 1];

  // Error message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Error category
  gcommon.v1.common.NackErrorCategory category = 3;

  // Whether the error is retryable
  bool retryable = 4;

  // Stack trace or additional details
  string details = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### node_info.proto {#node_info}

**Path**: `gcommon/v1/queue/node_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `NodeInfo`

**Imports** (5):

- `gcommon/v1/common/node_state.proto`
- `gcommon/v1/queue/node_stats.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/node_info.proto
// version: 1.0.0
// guid: d73ea780-8ed0-4b73-8aae-ab5c4fc1a48f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/node_state.proto";
import "gcommon/v1/queue/node_stats.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Information about a single node in the cluster.
 */
message NodeInfo {
  // Unique identifier for the node
  string node_id = 1 [(buf.validate.field).string.min_len = 1];

  // Hostname or address of the node
  string hostname = 2 [(buf.validate.field).string.min_len = 1];

  // Port number for the node
  int32 port = 3 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Current state of the node
  gcommon.v1.common.NodeState state = 4;

  // Node roles (leader, follower, etc.)
  repeated string roles = 5 [(buf.validate.field).repeated.min_items = 1];

  // Timestamp when node was last seen
  google.protobuf.Timestamp last_heartbeat = 6;

  // Node-specific statistics
  NodeStats stats = 7;
}
```

---

### node_stats.proto {#node_stats}

**Path**: `gcommon/v1/queue/node_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `NodeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/node_stats.proto
// version: 1.0.0
// guid: f64f009b-e23d-4540-9785-817fe7acb9f3

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics for a single node.
 */
message NodeStats {
  // Number of queues hosted on this node
  int32 queue_count = 1 [(buf.validate.field).int32.gte = 0];

  // Number of messages on this node
  int64 message_count = 2 [(buf.validate.field).int64.gte = 0];

  // CPU usage percentage
  double cpu_usage = 3 [(buf.validate.field).double.gte = 0.0];

  // Memory usage in bytes
  int64 memory_usage = 4 [(buf.validate.field).int64.gte = 0];

  // Disk usage in bytes
  int64 disk_usage = 5 [(buf.validate.field).int64.gte = 0];

  // Network throughput in bytes per second
  double network_throughput = 6 [(buf.validate.field).double.gte = 0.0];
}
```

---

### notification_channel.proto {#notification_channel}

**Path**: `gcommon/v1/queue/notification_channel.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `QueueNotificationChannel`

**Imports** (4):

- `gcommon/v1/common/metrics_alert_severity.proto`
- `gcommon/v1/common/notification_channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/notification_channel.proto
// version: 1.0.0
// guid: 6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/metrics_alert_severity.proto";
import "gcommon/v1/common/notification_channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Notification channel for sending alerts.
 */
message QueueNotificationChannel {
  // Unique identifier for the channel
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Type of notification channel
  gcommon.v1.common.NotificationChannelType type = 2;

  // Configuration specific to the channel type
  map<string, string> config = 3;

  // Whether the channel is enabled
  bool enabled = 4;

  // Minimum severity level for notifications
  gcommon.v1.common.MetricsAlertSeverity min_severity = 5;
}
```

---

### o_auth2_auth.proto {#o_auth2_auth}

**Path**: `gcommon/v1/queue/o_auth2_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `OAuth2Auth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/o_auth2_auth.proto
// version: 1.0.0
// guid: ed719ecf-6477-4d68-b022-dc57bed659ce

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OAuth2Auth {
  // OAuth2 token endpoint
  string token_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Client ID
  string client_id = 2 [(buf.validate.field).string.min_len = 1];

  // Client secret
  string client_secret = 3 [(buf.validate.field).string.min_len = 1];

  // Scopes to request
  repeated string scopes = 4 [(buf.validate.field).repeated.min_items = 1];

  // Additional OAuth2 parameters
  map<string, string> parameters = 5;
}
```

---

### offset_info.proto {#offset_info}

**Path**: `gcommon/v1/queue/offset_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `OffsetInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/offset_info.proto
// file: proto/gcommon/v1/queue/offset_info.proto
// version: 1.0.0
// guid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Information about message offset position in a queue.
 */
message OffsetInfo {
  // The offset value
  uint64 offset = 1 [(buf.validate.field).uint64.gte = 0];

  // Partition this offset belongs to
  uint32 partition_id = 2 [(buf.validate.field).uint32.gte = 0];

  // Timestamp of the message at this offset
  google.protobuf.Timestamp timestamp = 3;

  // Size of the message at this offset
  uint64 message_size = 4 [(buf.validate.field).uint64.gte = 0];

  // Whether this offset is valid/available
  bool is_valid = 5;

  // Consumer group that owns this offset
  string consumer_group = 6 [(buf.validate.field).string.min_len = 1];

  // Last committed offset for this consumer
  uint64 committed_offset = 7 [(buf.validate.field).uint64.gte = 0];
}
```

---

### offset_range.proto {#offset_range}

**Path**: `gcommon/v1/queue/offset_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `OffsetRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_range.proto
// version: 1.0.0
// guid: 83e606c1-e57b-4ca4-a62b-2460a5ae302f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OffsetRange {
  // Start offset
  int64 start_offset = 1 [(buf.validate.field).int64.gte = 0];

  // End offset
  int64 end_offset = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### original_queue_info.proto {#original_queue_info}

**Path**: `gcommon/v1/queue/original_queue_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `OriginalQueueInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/original_queue_info.proto
// version: 1.0.0
// guid: a939a9d0-aaf5-4d3a-b47d-16dad566fe50

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OriginalQueueInfo {
  // Original queue ID
  string queue_id = 1;

  // Original queue name
  string queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Original partition count
  int32 partition_count = 3;

  // Original configuration snapshot
  map<string, string> config_snapshot = 4;

  // Backup creation point
  google.protobuf.Timestamp backup_point = 5;
}
```

---

### owner_info.proto {#owner_info}

**Path**: `gcommon/v1/queue/owner_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `OwnerInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/owner_info.proto
// version: 1.0.0
// guid: bafca048-b678-49a0-853b-ba2cb7e220a9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OwnerInfo {
  // Owner user ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Owner username
  string username = 2;

  // Owner email
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Organization/team
  string organization = 4;

  // Ownership timestamp
  google.protobuf.Timestamp owned_since = 5;
}
```

---

### partition_assignment.proto {#partition_assignment}

**Path**: `gcommon/v1/queue/partition_assignment.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PartitionAssignment`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_assignment.proto
// version: 1.0.0
// guid: 7da7ff24-741c-4f7d-840c-ae433c0bf313

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PartitionAssignment {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Assigned consumer ID
  string consumer_id = 2 [(buf.validate.field).string.min_len = 1];

  // Current offset position
  int64 current_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Committed offset
  int64 committed_offset = 4 [(buf.validate.field).int64.gte = 0];

  // High water mark (latest available offset)
  int64 high_water_mark = 5 [(buf.validate.field).int64.gte = 0];

  // Assignment timestamp
  google.protobuf.Timestamp assigned_at = 6;

  // Last commit timestamp
  google.protobuf.Timestamp last_commit = 7;
}
```

---

### partition_commit_result.proto {#partition_commit_result}

**Path**: `gcommon/v1/queue/partition_commit_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PartitionCommitResult`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_commit_result.proto
// version: 1.0.0
// guid: c39fc412-24d3-4f3f-873f-f825a3dee3af

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PartitionCommitResult {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Success status for this partition
  bool success = 2;

  // Committed offset value
  int64 committed_offset = 3 [(buf.validate.field).int64.gte = 0];

  // Previous offset before commit
  int64 previous_offset = 4 [(buf.validate.field).int64.gte = 0];

  // Error message if commit failed for this partition
  string error_message = 5 [(buf.validate.field).string.min_len = 1];

  // Error code for this partition
  string error_code = 6 [(buf.validate.field).string.min_len = 1];

  // Timestamp when this offset was committed
  google.protobuf.Timestamp commit_timestamp = 7;

  // Metadata for this partition commit
  map<string, string> partition_metadata = 8;
}
```

---

### partition_info.proto {#partition_info}

**Path**: `gcommon/v1/queue/partition_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `PartitionInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/partition_info.proto
// file: proto/gcommon/v1/queue/partition_info.proto
// version: 1.0.0
// guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Information about a queue partition.
 */
message PartitionInfo {
  // Partition identifier
  uint32 partition_id = 1 [(buf.validate.field).uint32.gte = 0];

  // Leader node for this partition
  string leader_node = 2 [(buf.validate.field).string.min_len = 1];

  // Replica nodes for this partition
  repeated string replica_nodes = 3 [(buf.validate.field).repeated.min_items = 1];

  // Current offset (latest message)
  uint64 current_offset = 4 [(buf.validate.field).uint64.gte = 0];

  // Earliest available offset
  uint64 earliest_offset = 5 [(buf.validate.field).uint64.gte = 0];

  // Number of messages in partition
  uint64 message_count = 6 [(buf.validate.field).uint64.gte = 0];

  // Partition size in bytes
  uint64 size_bytes = 7 [(buf.validate.field).uint64.gte = 0];

  // Whether partition is online
  bool is_online = 8;
}
```

---

### partition_offset.proto {#partition_offset}

**Path**: `gcommon/v1/queue/partition_offset.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PartitionOffset`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_offset.proto
// version: 1.0.0
// guid: 0d54df2b-ee96-4361-8361-b047c9a198f6
// Partition offset information for queue operations

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// PartitionOffset represents the offset position within a partition
message PartitionOffset {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Starting offset value
  int64 offset = 2 [(buf.validate.field).int64.gte = 0];

  // Offset timestamp
  google.protobuf.Timestamp offset_timestamp = 3;

  // High water mark for this partition
  int64 high_water_mark = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### partition_restore_result.proto {#partition_restore_result}

**Path**: `gcommon/v1/queue/partition_restore_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `PartitionRestoreResult`

**Imports** (4):

- `gcommon/v1/queue/restore_error.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/partition_restore_result.proto
// version: 1.0.0
// guid: b39d8964-9b75-4f60-9e91-1c838aa2546e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/restore_error.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PartitionRestoreResult {
  // Partition ID
  int32 partition_id = 1 [(buf.validate.field).int32.gte = 0];

  // Success status for this partition
  bool success = 2;

  // Messages restored in this partition
  int64 messages_restored = 3 [(buf.validate.field).int64.gte = 0];

  // Bytes restored in this partition
  int64 bytes_restored = 4 [(buf.validate.field).int64.gte = 0];

  // Start offset restored
  int64 start_offset = 5 [(buf.validate.field).int64.gte = 0];

  // End offset restored
  int64 end_offset = 6 [(buf.validate.field).int64.gte = 0];

  // Partition restore duration
  google.protobuf.Duration restore_duration = 7;

  // Any partition-specific errors
  repeated RestoreError partition_errors = 8 [(buf.validate.field).repeated.min_items = 1];

  // Partition metadata
  map<string, string> partition_metadata = 9;
}
```

---

### performance_metrics.proto {#performance_metrics}

**Path**: `gcommon/v1/queue/performance_metrics.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PerformanceMetrics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/performance_metrics.proto
// version: 1.0.0
// guid: 05dd3b07-903d-4e03-97dc-1a79fa3bd75b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PerformanceMetrics {
  // Memory usage
  int64 memory_used_bytes = 1 [(buf.validate.field).int64.gte = 0];
  int64 memory_available_bytes = 2 [(buf.validate.field).int64.gte = 0];

  // CPU usage percentage
  double cpu_usage_percent = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];

  // Disk usage for persistent storage
  int64 disk_used_bytes = 4 [(buf.validate.field).int64.gte = 0];
  int64 disk_available_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Network metrics
  double network_bytes_per_second = 6 [(buf.validate.field).double.gte = 0.0];

  // Connection metrics
  int32 active_connections = 7 [(buf.validate.field).int32.gte = 0];
  int32 max_connections = 8 [(buf.validate.field).int32.gte = 0];
}
```

---

### performance_options.proto {#performance_options}

**Path**: `gcommon/v1/queue/performance_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PerformanceOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/performance_options.proto
// version: 1.0.0
// guid: da533c28-4c1d-47aa-af5b-b6f7ec77d916

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PerformanceOptions {
  // Parallel restore workers
  int32 worker_count = 1 [(buf.validate.field).int32.gte = 0];

  // Batch size for restore operations
  int32 batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Buffer size for reading backup data
  int32 buffer_size_mb = 3 [(buf.validate.field).int32.gte = 0];

  // Compression during restore
  bool enable_compression = 4;

  // Throttle restore rate (messages/second)
  int32 throttle_rate = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### permission_rule.proto {#permission_rule}

**Path**: `gcommon/v1/queue/permission_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `PermissionRule`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/permission_rule.proto
// version: 1.0.0
// guid: a9f45dd7-43a2-47cd-812c-8a08ee0100e2

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PermissionRule {
  // Resource pattern (queue name, topic name, etc.)
  string resource_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Operation (read, write, admin, etc.)
  string operation = 2 [(buf.validate.field).string.min_len = 1];

  // Required roles or permissions
  repeated string required_roles = 3 [(buf.validate.field).repeated.min_items = 1];

  // Allow or deny rule
  bool allow = 4;

  // Priority of this rule (higher number = higher priority)
  int32 priority = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### preserved_stats.proto {#preserved_stats}

**Path**: `gcommon/v1/queue/preserved_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `PreservedStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/preserved_stats.proto
// version: 1.0.0
// guid: d380f24a-2b42-4096-bfe3-4e251cf55325

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PreservedStats {
  // Total message count (lifetime)
  int64 lifetime_message_count = 1;

  // Queue creation timestamp
  google.protobuf.Timestamp created_at = 2 [ (buf.validate.field).required = true ];

  // Last configuration change timestamp
  google.protobuf.Timestamp last_config_change = 3;

  // Peak message count (historical high)
  int64 peak_message_count = 4;

  // Peak throughput (historical high)
  double peak_throughput = 5;

  // Total uptime (milliseconds)
  int64 total_uptime_ms = 6;
}
```

---

### priority_range.proto {#priority_range}

**Path**: `gcommon/v1/queue/priority_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `PriorityRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/priority_range.proto
// version: 1.0.0
// guid: 1efceade-7805-4b90-bdd0-2484a86cb6c9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Priority range for filtering.
 */
message PriorityRange {
  // Minimum priority (inclusive)
  int32 min_priority = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum priority (inclusive)
  int32 max_priority = 2 [(buf.validate.field).int32.gte = 0];
}
```

---

### priority_update.proto {#priority_update}

**Path**: `gcommon/v1/queue/priority_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `PriorityUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/priority_update.proto
// version: 1.0.0
// guid: 65ef02ba-9810-4cd5-9b8e-d1db580b22f6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PriorityUpdate {
  // New priority level
  int32 priority_level = 1 [(buf.validate.field).int32.gte = 0];

  // Priority change reason
  string priority_reason = 2 [(buf.validate.field).string.min_len = 1];

  // Maintain relative priority ordering
  bool maintain_order = 3;
}
```

---

### purge_options.proto {#purge_options}

**Path**: `gcommon/v1/queue/purge_options.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `PurgeOptions`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/purge_options.proto
// version: 1.0.0
// guid: 05f20447-a209-4b0a-bbe3-d46d178c07c6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PurgeOptions {
  // Whether to purge all messages (if true, other filters are ignored)
  bool purge_all = 1;

  // Purge messages older than this timestamp
  google.protobuf.Timestamp older_than = 2;

  // Purge messages with specific headers (all headers must match)
  map<string, string> header_filters = 3;

  // Purge messages with priority below this value
  int32 priority_below = 4 [(buf.validate.field).int32.gte = 0];

  // Purge messages with priority above this value
  int32 priority_above = 5 [(buf.validate.field).int32.gte = 0];

  // Maximum number of messages to purge (0 = no limit)
  int64 max_messages = 6 [(buf.validate.field).int64.gte = 0];

  // Whether to purge only failed/undeliverable messages
  bool only_failed = 7;

  // Whether to purge only expired messages
  bool only_expired = 8;
}
```

---

### read_consistency.proto {#read_consistency}

**Path**: `gcommon/v1/queue/read_consistency.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `ReadConsistency`

**Imports** (4):

- `gcommon/v1/common/read_level.proto`
- `gcommon/v1/queue/read_retry_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/read_consistency.proto
// version: 1.0.0
// guid: 76f69c9b-abbb-4704-a74e-3dddcab24330

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/read_level.proto";
import "gcommon/v1/queue/read_retry_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReadConsistency {
  // Read consistency level
  gcommon.v1.common.ReadLevel level = 1;

  // Maximum staleness allowed for reads (milliseconds)
  int64 max_staleness_ms = 2 [(buf.validate.field).int64.gte = 0];

  // Enable read-your-writes consistency
  bool read_your_writes = 3;

  // Enable monotonic read consistency
  bool monotonic_reads = 4;

  // Timeout for read operations (milliseconds)
  int32 timeout_ms = 5 [(buf.validate.field).int32.gt = 0];

  // Retry configuration for read failures
  ReadRetryConfig retry_config = 6;
}
```

---

### rebalance_stats.proto {#rebalance_stats}

**Path**: `gcommon/v1/queue/rebalance_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `RebalanceStats`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/rebalance_stats.proto
// version: 1.0.0
// guid: 3a965b27-4706-4f72-ada6-d9f3547ebd00

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RebalanceStats {
  // Total number of rebalances
  int64 total_rebalances = 1 [(buf.validate.field).int64.gte = 0];

  // Last rebalance timestamp
  google.protobuf.Timestamp last_rebalance = 2;

  // Average rebalance duration (milliseconds)
  int64 avg_rebalance_duration_ms = 3 [(buf.validate.field).int64.gt = 0];

  // Failed rebalances
  int64 failed_rebalances = 4 [(buf.validate.field).int64.gte = 0];
}
```

---

### received_message.proto {#received_message}

**Path**: `gcommon/v1/queue/received_message.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `ReceivedMessage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/received_message.proto
// version: 1.0.0
// guid: c7d8e9f0-123a-567b-8901-123456789012

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReceivedMessage {
  // Message ID
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Message data
  bytes data = 2;

  // Message attributes
  map<string, string> attributes = 3;

  // Receive timestamp
  int64 receive_timestamp = 4;

  // Acknowledgment ID
  string ack_id = 5;
}
```

---

### replication_consistency.proto {#replication_consistency}

**Path**: `gcommon/v1/queue/replication_consistency.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `ReplicationConsistency`

**Imports** (3):

- `gcommon/v1/common/replication_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/replication_consistency.proto
// version: 1.0.0
// guid: 6edbf0fb-990f-446b-bec1-14f1ec84397c

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/replication_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReplicationConsistency {
  // Minimum number of replicas that must acknowledge writes
  int32 min_write_replicas = 1 [(buf.validate.field).int32.gte = 0];

  // Minimum number of replicas that must be available for reads
  int32 min_read_replicas = 2 [(buf.validate.field).int32.gte = 0];

  // Replication factor (total number of replicas)
  int32 replication_factor = 3 [(buf.validate.field).int32.gte = 0];

  // Consistency level for replication
  gcommon.v1.common.ReplicationLevel replication_level = 4;

  // Enable anti-entropy repair
  bool anti_entropy_enabled = 5;

  // Anti-entropy repair interval (seconds)
  int32 repair_interval_seconds = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### resume_stats.proto {#resume_stats}

**Path**: `gcommon/v1/queue/resume_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ResumeStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/resume_stats.proto
// version: 1.0.0
// guid: dd734c97-7ac1-4b56-8ea6-dbd08cac6e27

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ResumeStats {
  // Number of partitions resumed
  int32 partitions_resumed = 1 [(buf.validate.field).int32.gte = 0];

  // Number of subscriptions reactivated
  int32 subscriptions_reactivated = 2 [(buf.validate.field).int32.gte = 0];

  // Number of consumers reconnected
  int32 consumers_reconnected = 3 [(buf.validate.field).int32.gte = 0];

  // Time taken to complete resume (milliseconds)
  int64 resume_time_ms = 4 [(buf.validate.field).int64.gte = 0];

  // Messages processed immediately after resume
  int64 immediate_messages_processed = 5 [(buf.validate.field).int64.gte = 0];

  // Throughput after resume (messages/second)
  double post_resume_throughput = 6 [(buf.validate.field).double.gte = 0.0];
}
```

---

### retention_info.proto {#retention_info}

**Path**: `gcommon/v1/queue/retention_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `QueueRetentionInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retention_info.proto
// version: 1.0.0
// guid: ecd5cb6b-db6b-42d3-b953-fa57bdfd4483

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueRetentionInfo {
  // Current retention policy
  string retention_policy = 1 [(buf.validate.field).string.min_len = 1];

  // Retention period (seconds)
  int64 retention_seconds = 2 [(buf.validate.field).int64.gte = 0];

  // Size-based retention limit (bytes)
  int64 retention_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Number of messages retained
  int64 retained_messages = 4 [(buf.validate.field).int64.gte = 0];

  // Oldest message timestamp
  google.protobuf.Timestamp oldest_message_time = 5;

  // Next cleanup scheduled time
  google.protobuf.Timestamp next_cleanup_time = 6;
}
```

---

### retention_policy.proto {#retention_policy}

**Path**: `gcommon/v1/queue/retention_policy.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `QueueRetentionPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retention_policy.proto
// version: 1.0.0
// guid: 5a069bb8-66bf-413e-a9e8-a1856f52eb01

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// RetentionPolicy controls how long messages are kept before deletion.
message QueueRetentionPolicy {
  // Maximum age of a message before it is removed.
  google.protobuf.Duration max_age = 1;
  // Maximum total storage size for the queue in bytes.
  int64 max_size_bytes = 2 [(buf.validate.field).int64.gte = 0];
  // If true, older messages are discarded when limits are reached.
  bool discard_old = 3;
}
```

---

### retry_policy.proto {#retry_policy}

**Path**: `gcommon/v1/queue/retry_policy.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `QueueRetryPolicy`

**Imports** (4):

- `gcommon/v1/common/retry_delay_strategy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_policy.proto
// version: 1.1.0
// guid: 4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/retry_delay_strategy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Retry policy for failed message processing.
 * Defines how failed messages should be retried before being
 * sent to dead letter queue.
 */
message QueueRetryPolicy {
  // Maximum number of retry attempts
  int32 max_attempts = 1 [(buf.validate.field).int32.gte = 0];

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 2;

  // Maximum delay between retries
  google.protobuf.Duration max_delay = 3;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Retry delay strategy
  gcommon.v1.common.RetryDelayStrategy delay_strategy = 5;

  // Whether to enable jitter in retry delays
  bool enable_jitter = 6;

  // Jitter factor (0.0 to 1.0) for randomizing delays
  double jitter_factor = 7 [(buf.validate.field).double.gte = 0.0];
}
```

---

### retry_settings.proto {#retry_settings}

**Path**: `gcommon/v1/queue/retry_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `QueueRetrySettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_settings.proto
// version: 1.0.0
// guid: dc848673-c62f-4cd2-b373-ed1570d3f5aa

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueRetrySettings {
  // Maximum retry attempts
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Dead letter queue topic
  string dead_letter_topic = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### role_based_access_control.proto {#role_based_access_control}

**Path**: `gcommon/v1/queue/role_based_access_control.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `RoleBasedAccessControl`

**Imports** (4):

- `gcommon/v1/queue/external_role_provider.proto`
- `gcommon/v1/queue/role_inheritance.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/role_based_access_control.proto
// version: 1.0.0
// guid: 090db6f2-ad16-49c5-aa6c-ef8f279279e2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/external_role_provider.proto";
import "gcommon/v1/queue/role_inheritance.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoleBasedAccessControl {
  // Enable RBAC
  bool enabled = 1;

  // Default roles for new users
  repeated string default_roles = 2 [(buf.validate.field).repeated.min_items = 1];

  // Role inheritance rules
  map<string, RoleInheritance> role_inheritance = 3;

  // External role provider settings
  ExternalRoleProvider external_provider = 4;
}
```

---

### role_inheritance.proto {#role_inheritance}

**Path**: `gcommon/v1/queue/role_inheritance.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `RoleInheritance`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/role_inheritance.proto
// version: 1.0.0
// guid: 85442141-e1a3-4392-94b8-44d4f53e79fb

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoleInheritance {
  // Parent roles that this role inherits from
  repeated string inherits_from = 1 [(buf.validate.field).repeated.min_items = 1];

  // Additional permissions for this role
  repeated string additional_permissions = 2 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### routing_condition.proto {#routing_condition}

**Path**: `gcommon/v1/queue/routing_condition.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `RoutingCondition`

**Imports** (4):

- `gcommon/v1/queue/priority_range.proto`
- `gcommon/v1/queue/size_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_condition.proto
// version: 1.0.0
// guid: c5586126-e8b2-47e8-b657-e837b38179bd

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/priority_range.proto";
import "gcommon/v1/queue/size_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Condition for routing rules.
 */
message RoutingCondition {
  // Header-based conditions
  map<string, string> header_matches = 1;

  // Content pattern matching
  string content_pattern = 2 [(buf.validate.field).string.min_len = 1];

  // Routing key pattern
  string routing_key_pattern = 3 [(buf.validate.field).string.min_len = 1];

  // Message type filter
  string message_type = 4 [(buf.validate.field).string.min_len = 1];

  // Priority range filter
  PriorityRange priority_range = 5;

  // Size range filter
  SizeRange size_range = 6;
}
```

---

### routing_info.proto {#routing_info}

**Path**: `gcommon/v1/queue/routing_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `RoutingInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_info.proto
// version: 1.0.0
// guid: 08017b3e-df77-4338-ba13-aadde0c41612

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoutingInfo {
  // Routing key for topic-based routing
  string routing_key = 1;

  // Specific partition ID (if applicable)
  int32 partition_id = 2;

  // Partition key for automatic partitioning
  string partition_key = 3;

  // Exchange name (for exchange-based routing)
  string exchange_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Routing tags for advanced routing
  repeated string routing_tags = 5;
}
```

---

### routing_key.proto {#routing_key}

**Path**: `gcommon/v1/queue/routing_key.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `RoutingKey`

**Imports** (3):

- `gcommon/v1/common/routing_pattern.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_key.proto
// version: 1.1.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/routing_pattern.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Routing key for message delivery.
 * Determines how messages are routed to queues and consumers.
 */
message RoutingKey {
  // The routing key string
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Pattern type for key matching
  gcommon.v1.common.RoutingPattern pattern_type = 2;

  // Whether the pattern is case sensitive
  bool case_sensitive = 3;

  // Priority for routing (higher numbers = higher priority)
  int32 priority = 4 [(buf.validate.field).int32.gte = 0];

  // Additional routing attributes
  map<string, string> attributes = 5;
}
```

---

### routing_rule.proto {#routing_rule}

**Path**: `gcommon/v1/queue/routing_rule.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `RoutingRule`

**Imports** (3):

- `gcommon/v1/queue/routing_condition.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_rule.proto
// version: 1.0.0
// guid: 6ce2389f-a9b6-4850-bdf9-6b5225cd61d4

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/routing_condition.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Individual routing rule.
 */
message RoutingRule {
  // Unique name for the rule
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Priority of the rule (higher numbers = higher priority)
  int32 priority = 2;

  // Condition for applying the rule
  RoutingCondition condition = 3;

  // Target destination for matching messages
  string destination = 4;

  // Whether the rule is enabled
  bool enabled = 5;

  // Additional metadata for the rule
  map<string, string> metadata = 6;
}
```

---

### routing_settings.proto {#routing_settings}

**Path**: `gcommon/v1/queue/routing_settings.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `RoutingSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_settings.proto
// version: 1.0.0
// guid: f9f28b94-889d-4b4b-859e-dd55251a2aa6

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RoutingSettings {
  // Routing key pattern
  string routing_key_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Target partitions
  repeated int32 target_partitions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Routing strategy
  string routing_strategy = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### sasl_auth.proto {#sasl_auth}

**Path**: `gcommon/v1/queue/sasl_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `SASLAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/sasl_auth.proto
// version: 1.0.0
// guid: 24c2c7a1-8dbb-44e3-9d87-bb207c23207d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SASLAuth {
  // SASL mechanism (PLAIN, SCRAM-SHA-256, etc.)
  string mechanism = 1 [(buf.validate.field).string.min_len = 1];

  // Username
  string username = 2 [(buf.validate.field).string.min_len = 1];

  // Password
  string password = 3 [(buf.validate.field).string.min_len = 8];

  // Additional SASL properties
  map<string, string> properties = 4;
}
```

---

### schema_validation.proto {#schema_validation}

**Path**: `gcommon/v1/queue/schema_validation.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `SchemaValidation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_validation.proto
// version: 1.0.0
// guid: ee7fffd9-460b-48d0-bea8-533482d34e85

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SchemaValidation {
  // Schema validation passed
  bool passed = 1;

  // Schema version in backup
  string backup_schema_version = 2 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Current schema version
  string current_schema_version = 3 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Schema compatibility status
  string compatibility_status = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### size_bucket.proto {#size_bucket}

**Path**: `gcommon/v1/queue/size_bucket.proto` **Package**: `gcommon.v1.queue` **Lines**: 20

**Messages** (1): `SizeBucket`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/size_bucket.proto
// version: 1.0.0
// guid: 01e90e2f-62e8-47a9-86bf-0a684d65a463

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SizeBucket {
  int64 min_size_bytes = 1 [(buf.validate.field).int64.gte = 0];
  int64 max_size_bytes = 2 [(buf.validate.field).int64.gte = 0];
  int64 message_count = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### size_distribution.proto {#size_distribution}

**Path**: `gcommon/v1/queue/size_distribution.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `SizeDistribution`

**Imports** (3):

- `gcommon/v1/queue/size_bucket.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/size_distribution.proto
// version: 1.0.0
// guid: 6a630c77-ef52-498c-b0c7-0be5177f3a90

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/size_bucket.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SizeDistribution {
  // Size buckets in bytes
  repeated SizeBucket buckets = 1 [(buf.validate.field).repeated.min_items = 1];

  // Summary statistics
  int64 min_size_bytes = 2 [(buf.validate.field).int64.gte = 0];
  int64 max_size_bytes = 3 [(buf.validate.field).int64.gte = 0];
  double average_size_bytes = 4 [(buf.validate.field).double.gte = 0.0];
  double median_size_bytes = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### size_range.proto {#size_range}

**Path**: `gcommon/v1/queue/size_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `SizeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/size_range.proto
// version: 1.0.0
// guid: 644269a7-7ae9-4ab3-98d3-d7111c89451b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Size range for filtering.
 */
message SizeRange {
  // Minimum size in bytes (inclusive)
  int64 min_size = 1 [(buf.validate.field).int64.gte = 0];

  // Maximum size in bytes (inclusive)
  int64 max_size = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### subscription_info.proto {#subscription_info}

**Path**: `gcommon/v1/queue/subscription_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `QueueSubscriptionInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_info.proto
// version: 1.0.0
// guid: 9b9d0532-72ff-4a42-b3b2-689a1a26dd9f

// SubscriptionInfo provides metadata about a subscription to a topic
// or queue. It replaces the placeholder file created during the
// 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * SubscriptionInfo describes a subscriber's configuration and status.
 */
message QueueSubscriptionInfo {
  // Name of the subscription
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic or queue this subscription belongs to
  string topic = 2;

  // Whether the subscription is currently active
  bool active = 3;

  // Number of pending messages for this subscription
  int64 pending_message_count = 4;

  // Time when the subscription was created
  google.protobuf.Timestamp created_at = 5 [ (buf.validate.field).required = true ];

  // Arbitrary labels associated with the subscription
  map<string, string> labels = 6;
}
```

---

### subscription_stats.proto {#subscription_stats}

**Path**: `gcommon/v1/queue/subscription_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `SubscriptionStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/subscription_stats.proto
// file: proto/gcommon/v1/queue/subscription_stats.proto
// version: 1.0.0
// guid: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics for a subscription.
 */
message SubscriptionStats {
  // Subscription identifier
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Number of messages consumed
  uint64 messages_consumed = 2 [(buf.validate.field).uint64.gte = 0];

  // Number of messages acknowledged
  uint64 messages_acknowledged = 3 [(buf.validate.field).uint64.gte = 0];

  // Number of messages rejected/nacked
  uint64 messages_rejected = 4 [(buf.validate.field).uint64.gte = 0];

  // Current lag (unprocessed messages)
  uint64 consumer_lag = 5 [(buf.validate.field).uint64.gte = 0];

  // Messages per second consumption rate
  double consumption_rate = 6 [(buf.validate.field).double.gte = 0.0];

  // Average processing time per message (milliseconds)
  double avg_processing_time_ms = 7 [(buf.validate.field).double.gte = 0.0];

  // Number of active consumers
  uint32 active_consumers = 8 [(buf.validate.field).uint32.gte = 0];

  // Last activity timestamp
  uint64 last_activity_time = 9 [(buf.validate.field).uint64.gte = 0];
}
```

---

### sync_replication.proto {#sync_replication}

**Path**: `gcommon/v1/queue/sync_replication.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `SyncReplication`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/sync_replication.proto
// version: 1.0.0
// guid: fb10fe6a-cf7a-47e7-9be7-c31f4e37b22e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SyncReplication {
  // Enable synchronous replication
  bool enabled = 1;

  // Minimum synchronous replicas
  int32 min_sync_replicas = 2 [(buf.validate.field).int32.gte = 0];

  // Timeout for synchronous replication (milliseconds)
  int32 sync_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Fallback to async on timeout
  bool fallback_to_async = 4;
}
```

---

### throughput_metrics.proto {#throughput_metrics}

**Path**: `gcommon/v1/queue/throughput_metrics.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `ThroughputMetrics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/throughput_metrics.proto
// version: 1.0.0
// guid: 238519f5-1808-4bcc-9cd5-e5700aca75e4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ThroughputMetrics {
  // Messages per second over different time windows
  double messages_per_second_1m = 1 [(buf.validate.field).double.gte = 0.0];
  double messages_per_second_5m = 2 [(buf.validate.field).double.gte = 0.0];
  double messages_per_second_15m = 3 [(buf.validate.field).double.gte = 0.0];
  double messages_per_second_1h = 4 [(buf.validate.field).double.gte = 0.0];

  // Peak throughput observed
  double peak_messages_per_second = 5 [(buf.validate.field).double.gte = 0.0];
  google.protobuf.Timestamp peak_timestamp = 6;
}
```

---

### time_range.proto {#time_range}

**Path**: `gcommon/v1/queue/time_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 27

**Messages** (1): `QueueTimeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/time_range.proto
// file: proto/gcommon/v1/queue/time_range.proto
// version: 1.0.1
// guid: 2a1b0c9d-8e7f-6a5b-4c3d-2e1f0a9b8c7d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Time range for filtering messages.
 */
message QueueTimeRange {
  // Start time (inclusive)
  google.protobuf.Timestamp start_time = 1;

  // End time (exclusive)
  google.protobuf.Timestamp end_time = 2;
}
```

---

### time_range_filter.proto {#time_range_filter}

**Path**: `gcommon/v1/queue/time_range_filter.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `TimeRangeFilter`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/time_range_filter.proto
// version: 1.0.0
// guid: a130528f-ed39-48b7-8dbf-b82f4db21916

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TimeRangeFilter {
  // Start time for the range (ISO 8601)
  string start_time = 1 [(buf.validate.field).string.min_len = 1];

  // End time for the range (ISO 8601)
  string end_time = 2 [(buf.validate.field).string.min_len = 1];

  // Granularity for aggregated data (minute, hour, day)
  string granularity = 3 [(buf.validate.field).string.min_len = 1];

  // Maximum number of data points to return
  int32 max_data_points = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### timestamp_range.proto {#timestamp_range}

**Path**: `gcommon/v1/queue/timestamp_range.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `QueueTimestampRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/timestamp_range.proto
// version: 1.0.1
// guid: 4fdb7c93-4616-4db9-a2d6-50f41676b4b6

// TimestampRange defines a start and end time for filtering or
// statistics queries. This implementation replaces the placeholder
// added during the 1-1-1 migration.
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// TimestampRange is used to specify a time window when querying
// statistics or messages.
message QueueTimestampRange {
  // Start of the range (inclusive).
  google.protobuf.Timestamp start = 1;

  // End of the range (exclusive).
  google.protobuf.Timestamp end = 2;
}
```

---

### tls_auth.proto {#tls_auth}

**Path**: `gcommon/v1/queue/tls_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `TLSAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/tls_auth.proto
// version: 1.0.0
// guid: f7982aad-6216-4a98-ae5a-3e86d058ae84

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TLSAuth {
  // Client certificate (PEM format)
  string cert_pem = 1 [(buf.validate.field).string.min_len = 1];

  // Client private key (PEM format)
  string key_pem = 2 [(buf.validate.field).string.min_len = 1];

  // CA certificate (PEM format)
  string ca_pem = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to verify server certificate
  bool verify_server = 4;
}
```

---

### topic_info.proto {#topic_info}

**Path**: `gcommon/v1/queue/topic_info.proto` **Package**: `gcommon.v1.queue` **Lines**: 53

**Messages** (1): `TopicInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_info.proto
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Topic information for queue management.
 * Contains metadata and status about a message queue topic.
 */
message TopicInfo {
  // Topic name/identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Topic description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Topic creation timestamp
  google.protobuf.Timestamp created_at = 3 [lazy = true, (buf.validate.field).required = true];

  // Topic last update timestamp
  google.protobuf.Timestamp updated_at = 4 [lazy = true];

  // Number of partitions
  int32 partition_count = 5;

  // Replication factor
  int32 replication_factor = 6;

  // Total message count
  int64 message_count = 7;

  // Topic size in bytes
  int64 size_bytes = 8;

  // Topic status (active, paused, etc.)
  string status = 9;

  // Topic metadata
  map<string, string> metadata = 10 [lazy = true];
}
```

---

### topic_permissions.proto {#topic_permissions}

**Path**: `gcommon/v1/queue/topic_permissions.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `TopicPermissions`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_permissions.proto
// version: 1.0.1
// guid: a2131871-2610-442f-93e7-5ab90e53e36c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TopicPermissions {
  // Can read messages from topic
  bool can_read = 1;

  // Can write messages to topic
  bool can_write = 2;

  // Can modify topic configuration
  bool can_configure = 3;

  // Can delete the topic
  bool can_delete = 4;

  // Can manage topic permissions
  bool can_manage_permissions = 5;

  // Can view topic statistics
  bool can_view_stats = 6;
}
```

---

### topic_stats.proto {#topic_stats}

**Path**: `gcommon/v1/queue/topic_stats.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `TopicStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/types/topic_stats.proto
// file: proto/gcommon/v1/queue/topic_stats.proto
// version: 1.0.0
// guid: 9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Statistics information for a topic.
 */
message TopicStats {
  // Name of the topic
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Total number of messages in the topic
  uint64 total_messages = 2;

  // Total size of all messages in bytes
  uint64 total_size_bytes = 3;

  // Number of active subscriptions
  uint32 subscription_count = 4;

  // Number of producers
  uint32 producer_count = 5;

  // Messages produced per second
  double messages_per_second = 6;

  // Bytes produced per second
  double bytes_per_second = 7;

  // Last message timestamp
  uint64 last_message_time = 8;

  // Average message size in bytes
  double average_message_size = 9;
}
```

---

### updated_properties.proto {#updated_properties}

**Path**: `gcommon/v1/queue/updated_properties.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `UpdatedProperties`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/updated_properties.proto
// version: 1.0.0
// guid: d960456c-efea-47df-8809-e0e34d8b8437

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdatedProperties {
  // New priority level (if updated)
  int32 priority_level = 1 [(buf.validate.field).int32.gte = 0];

  // New expiration time (if updated)
  google.protobuf.Timestamp expiration_time = 2;

  // New visibility timeout (if updated)
  int64 visibility_timeout_ms = 3 [(buf.validate.field).int64.gt = 0];

  // New routing key (if updated)
  string routing_key = 4 [(buf.validate.field).string.min_len = 1];

  // Updated metadata count
  int32 metadata_count = 5;

  // Updated headers count
  int32 headers_count = 6 [(buf.validate.field).int32.gte = 0];

  // Content was updated
  bool content_updated = 7;

  // Size of updated content (bytes)
  int64 content_size_bytes = 8 [(buf.validate.field).int64.gte = 0];
}
```

---

### username_password_auth.proto {#username_password_auth}

**Path**: `gcommon/v1/queue/username_password_auth.proto` **Package**: `gcommon.v1.queue` **Lines**: 22

**Messages** (1): `UsernamePasswordAuth`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/username_password_auth.proto
// version: 1.0.0
// guid: 3fc55294-5eb0-4d0a-8e1e-e00a7f1fdd98

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UsernamePasswordAuth {
  // Username for authentication
  string username = 1 [(buf.validate.field).string.min_len = 1];

  // Password for authentication (should be encrypted)
  string password = 2 [(buf.validate.field).string.min_len = 8];
}
```

---

### validation_error.proto {#validation_error}

**Path**: `gcommon/v1/queue/validation_error.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ValidationError`

**Imports** (3):

- `gcommon/v1/queue/offset_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/validation_error.proto
// version: 1.0.0
// guid: c3c484a5-cc5a-41e5-926d-91ba8263600e

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/offset_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ValidationError {
  // Error type
  string error_type = 1;

  // Error description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Affected partition
  int32 partition_id = 3;

  // Affected offset range
  OffsetRange affected_range = 4;
}
```

---

### validation_result.proto {#validation_result}

**Path**: `gcommon/v1/queue/validation_result.proto` **Package**: `gcommon.v1.queue` **Lines**: 39

**Messages** (1): `QueueValidationResult`

**Imports** (7):

- `gcommon/v1/queue/checksum_validation.proto`
- `gcommon/v1/queue/integrity_validation.proto`
- `gcommon/v1/queue/schema_validation.proto`
- `gcommon/v1/queue/validation_error.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/validation_result.proto
// version: 1.0.0
// guid: 26c1b8e2-a8aa-436b-9707-1f47c8c3e8d8

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/checksum_validation.proto";
import "gcommon/v1/queue/integrity_validation.proto";
import "gcommon/v1/queue/schema_validation.proto";
import "gcommon/v1/queue/validation_error.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueValidationResult {
  // Validation success status
  bool validation_passed = 1;

  // Checksum verification results
  ChecksumValidation checksum_validation = 2;

  // Schema validation results
  SchemaValidation schema_validation = 3;

  // Data integrity validation
  IntegrityValidation integrity_validation = 4;

  // Validation errors found
  repeated ValidationError validation_errors = 5 [(buf.validate.field).repeated.min_items = 1];

  // Validation duration
  google.protobuf.Duration validation_duration = 6;
}
```

---

### visibility_update.proto {#visibility_update}

**Path**: `gcommon/v1/queue/visibility_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `VisibilityUpdate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/visibility_update.proto
// version: 1.0.0
// guid: 9e5fd0b6-9d67-467e-b8a6-29addbcc72e4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message VisibilityUpdate {
  // New visibility timeout duration (milliseconds)
  int64 visibility_timeout_ms = 1 [(buf.validate.field).int64.gt = 0];

  // Extend current timeout (if true) or set absolute timeout
  bool extend_current = 2;

  // Maximum visibility timeout allowed
  int64 max_visibility_ms = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### workflow.proto {#workflow}

**Path**: `gcommon/v1/queue/workflow.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `QueueWorkflow`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/workflow.proto
// version: 1.0.0
// guid: 6f7e8d9c-0b1a-2534-6e7f-8a9b0c1d2e3f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Workflow represents a multi-step process definition.
 * Contains workflow metadata and execution configuration.
 */
message QueueWorkflow {
  // Unique identifier for the workflow
  string workflow_id = 1;

  // Human-readable workflow name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Workflow version
  string version = 3;

  // Workflow description
  string description = 4 [ (buf.validate.field).string.max_len = 1000 ];

  // Whether the workflow is active
  bool enabled = 5;
}
```

---

### write_consistency.proto {#write_consistency}

**Path**: `gcommon/v1/queue/write_consistency.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `WriteConsistency`

**Imports** (6):

- `gcommon/v1/common/write_level.proto`
- `gcommon/v1/queue/conflict_detection.proto`
- `gcommon/v1/queue/sync_replication.proto`
- `gcommon/v1/queue/write_retry_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/write_consistency.proto
// version: 1.0.0
// guid: 25356885-1f2a-4629-a203-6fd654cb6821

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/write_level.proto";
import "gcommon/v1/queue/conflict_detection.proto";
import "gcommon/v1/queue/sync_replication.proto";
import "gcommon/v1/queue/write_retry_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message WriteConsistency {
  // Write consistency level
  gcommon.v1.common.WriteLevel level = 1;

  // Synchronous replication requirements
  SyncReplication sync_replication = 2;

  // Write conflict detection
  ConflictDetection conflict_detection = 3;

  // Timeout for write operations (milliseconds)
  int32 timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Retry configuration for write failures
  WriteRetryConfig retry_config = 5;
}
```

---

### alerting_config.proto {#alerting_config}

**Path**: `gcommon/v1/queue/alerting_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `AlertingConfig`

**Imports** (6):

- `gcommon/v1/common/alert_severity.proto`
- `gcommon/v1/queue/alert_rule.proto`
- `gcommon/v1/queue/notification_channel.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/alerting_config.proto
// version: 1.1.0
// guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/alert_severity.proto";
import "gcommon/v1/queue/alert_rule.proto";
import "gcommon/v1/queue/notification_channel.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for queue alerting and notifications.
 */
message AlertingConfig {
  // Whether alerting is enabled
  bool enabled = 1;

  // List of alert rules
  repeated AlertRule rules = 2 [(buf.validate.field).repeated.min_items = 1];

  // Notification channels for alerts
  repeated QueueNotificationChannel channels = 3 [(buf.validate.field).repeated.min_items = 1];

  // Default alert severity level
  gcommon.v1.common.CommonAlertSeverity default_severity = 4;

  // Alert aggregation window
  google.protobuf.Duration aggregation_window = 5;
}
```

---

### auth_cache_config.proto {#auth_cache_config}

**Path**: `gcommon/v1/queue/auth_cache_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `AuthCacheConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/auth_cache_config.proto
// version: 1.0.0
// guid: 4282b3d6-375a-4b30-aaad-1763d882936a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AuthCacheConfig {
  // Enable caching
  bool enabled = 1;

  // Cache TTL (seconds)
  int32 ttl_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum cache size
  int32 max_size = 3 [(buf.validate.field).int32.gte = 0];

  // Cache cleanup interval (seconds)
  int32 cleanup_interval_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### authentication_config.proto {#authentication_config}

**Path**: `gcommon/v1/queue/authentication_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `AuthenticationConfig`

**Imports** (6):

- `gcommon/v1/queue/api_key_auth.proto`
- `gcommon/v1/queue/o_auth2_auth.proto`
- `gcommon/v1/queue/sasl_auth.proto`
- `gcommon/v1/queue/tls_auth.proto`
- `gcommon/v1/queue/username_password_auth.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/authentication_config.proto
// version: 1.0.1
// guid: b6fb3968-5534-4c9b-a4bb-55245fb334e3

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/api_key_auth.proto";
import "gcommon/v1/queue/o_auth2_auth.proto";
import "gcommon/v1/queue/sasl_auth.proto";
import "gcommon/v1/queue/tls_auth.proto";
import "gcommon/v1/queue/username_password_auth.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AuthenticationConfig {
  // Authentication type
  oneof auth_type {
    // No authentication required
    bool none = 1;

    // Username/password authentication
    UsernamePasswordAuth username_password = 2;

    // API key authentication
    APIKeyAuth api_key = 3;

    // TLS certificate authentication
    TLSAuth tls = 4;

    // SASL authentication
    SASLAuth sasl = 5;

    // OAuth2 authentication
    OAuth2Auth oauth2 = 6;
  }
}
```

---

### authorization_config.proto {#authorization_config}

**Path**: `gcommon/v1/queue/authorization_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 42

**Messages** (1): `AuthorizationConfig`

**Imports** (7):

- `gcommon/v1/queue/api_key_auth.proto`
- `gcommon/v1/queue/external_auth_service.proto`
- `gcommon/v1/queue/jwt_auth.proto`
- `gcommon/v1/queue/permission_rule.proto`
- `gcommon/v1/queue/role_based_access_control.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/authorization_config.proto
// version: 1.0.0
// guid: 813cabd6-f8af-423b-be9a-0c4d74b35cf2

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/api_key_auth.proto";
import "gcommon/v1/queue/external_auth_service.proto";
import "gcommon/v1/queue/jwt_auth.proto";
import "gcommon/v1/queue/permission_rule.proto";
import "gcommon/v1/queue/role_based_access_control.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AuthorizationConfig {
  // Enable authorization checking
  bool enabled = 1;

  // Default permission policy (allow/deny)
  string default_policy = 2 [(buf.validate.field).string.min_len = 1];

  // Permission rules for different operations
  repeated PermissionRule rules = 3 [(buf.validate.field).repeated.min_items = 1];

  // Role-based access control settings
  RoleBasedAccessControl rbac = 4;

  // API key authentication settings
  APIKeyAuth api_key_auth = 5;

  // JWT token authentication settings
  JwtAuth jwt_auth = 6;

  // External authorization service settings
  ExternalAuthService external_auth = 7;
}
```

---

### auto_commit_config.proto {#auto_commit_config}

**Path**: `gcommon/v1/queue/auto_commit_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `AutoCommitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/auto_commit_config.proto
// version: 1.0.0
// guid: 7f79c66e-a2a7-427d-844c-6010e165135d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message AutoCommitConfig {
  // Enable auto-commit of offsets
  bool enabled = 1;

  // Auto-commit interval (milliseconds)
  int32 interval_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Commit on message processing completion
  bool commit_on_completion = 3;

  // Batch size for auto-commit
  int32 batch_size = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### backup_config.proto {#backup_config}

**Path**: `gcommon/v1/queue/backup_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `QueueBackupConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/backup_config.proto
// version: 1.0.0
// guid: 2e127d68-6db3-4c2e-a0ff-bb7a2e5542b8

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// BackupConfig defines how queued messages should be backed up
// for disaster recovery.
message QueueBackupConfig {
  // Interval between automatic backups.
  google.protobuf.Duration interval = 1;

  // Duration to retain each backup before deletion.
  google.protobuf.Duration retention = 2;

  // Storage location for backups (e.g., S3 bucket).
  string location = 3 [(buf.validate.field).string.min_len = 1];

  // Whether backups are enabled for this queue.
  bool enabled = 4;
}
```

---

### batch_config.proto {#batch_config}

**Path**: `gcommon/v1/queue/batch_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `BatchConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/batch_config.proto
// file: proto/gcommon/v1/queue/batch_config.proto
// version: 1.0.0
// guid: 7d8e9f0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for batch operations in queue processing.
 */
message BatchConfig {
  // Maximum number of messages per batch
  uint32 max_batch_size = 1 [(buf.validate.field).uint32.gte = 0];

  // Maximum time to wait before sending partial batch
  google.protobuf.Duration max_wait_time = 2;

  // Maximum total size of batch in bytes
  uint64 max_batch_bytes = 3 [(buf.validate.field).uint64.gte = 0];

  // Whether to enable batch compression
  bool enable_compression = 4;

  // Number of parallel batch workers
  uint32 worker_count = 5 [(buf.validate.field).uint32.gte = 0];

  // Buffer size for pending batches
  uint32 buffer_size = 6 [(buf.validate.field).uint32.gte = 0];
}
```

---

### batch_delivery_config.proto {#batch_delivery_config}

**Path**: `gcommon/v1/queue/batch_delivery_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `BatchDeliveryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/batch_delivery_config.proto
// version: 1.0.0
// guid: 2f43a02c-2696-4c1f-820c-b97ddd38fe31

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message BatchDeliveryConfig {
  // Enable batch delivery
  bool enabled = 1;

  // Maximum messages per batch
  int32 max_batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum batch size in bytes
  int64 max_batch_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum time to wait for batch completion (milliseconds)
  int32 batch_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### circuit_breaker_config.proto {#circuit_breaker_config}

**Path**: `gcommon/v1/queue/circuit_breaker_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `QueueCircuitBreakerConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/circuit_breaker_config.proto
// file: proto/gcommon/v1/queue/circuit_breaker_config.proto
// version: 1.0.0
// guid: 6c7d8e9f-0a1b-2c3d-4e5f-6a7b8c9d0e1f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for circuit breaker pattern in queue operations.
 */
message QueueCircuitBreakerConfig {
  // Whether circuit breaker is enabled
  bool enabled = 1;

  // Failure threshold to open circuit
  uint32 failure_threshold = 2 [(buf.validate.field).uint32.gte = 0];

  // Success threshold to close circuit
  uint32 success_threshold = 3 [(buf.validate.field).uint32.gte = 0];

  // Timeout before attempting to close circuit
  google.protobuf.Duration timeout = 4;

  // Maximum number of concurrent requests in half-open state
  uint32 max_requests = 5 [(buf.validate.field).uint32.gte = 0];

  // Time window for failure counting
  google.protobuf.Duration interval = 6;
}
```

---

### cluster_config.proto {#cluster_config}

**Path**: `gcommon/v1/queue/cluster_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ClusterConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/cluster_config.proto
// version: 1.0.0
// guid: 6ab9cf18-3f43-40f4-b289-163545acdc05

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for the cluster.
 */
message ClusterConfig {
  // Minimum number of nodes for quorum
  int32 quorum_size = 1 [(buf.validate.field).int32.gte = 0];

  // Replication factor
  int32 replication_factor = 2 [(buf.validate.field).int32.gte = 0];

  // Heartbeat interval in seconds
  int32 heartbeat_interval = 3 [(buf.validate.field).int32.gte = 0];

  // Election timeout in seconds
  int32 election_timeout = 4 [(buf.validate.field).int32.gt = 0];
}
```

---

### compression_config.proto {#compression_config}

**Path**: `gcommon/v1/queue/compression_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `QueueCompressionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/compression_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174000

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// CompressionConfig message definition.
message QueueCompressionConfig {
  // Enable compression
  bool enabled = 1;

  // Compression algorithm
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Compression level (0-9)
  int32 level = 3 [(buf.validate.field).int32.gte = 0];

  // Minimum message size to compress
  int32 min_size_bytes = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### consistency_config.proto {#consistency_config}

**Path**: `gcommon/v1/queue/consistency_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `ConsistencyConfig`

**Imports** (9):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/common/conflict_resolution.proto`
- `gcommon/v1/common/durability_level.proto`
- `gcommon/v1/queue/consistency_validation.proto`
- `gcommon/v1/queue/ordering_config.proto`
- `gcommon/v1/queue/read_consistency.proto`
- `gcommon/v1/queue/replication_consistency.proto`
- `gcommon/v1/queue/write_consistency.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consistency_config.proto
// version: 1.0.1
// guid: 038986e0-4267-432c-99a3-7271a9427b29

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/common/conflict_resolution.proto";
import "gcommon/v1/common/durability_level.proto";
import "gcommon/v1/queue/consistency_validation.proto";
import "gcommon/v1/queue/ordering_config.proto";
import "gcommon/v1/queue/read_consistency.proto";
import "gcommon/v1/queue/replication_consistency.proto";
import "gcommon/v1/queue/write_consistency.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsistencyConfig {
  // Durability level for message persistence
  gcommon.v1.common.DurabilityLevel durability_level = 1;

  // Acknowledgment level required for message delivery
  gcommon.v1.common.AckLevel ack_level = 2;

  // Replication configuration
  ReplicationConsistency replication = 3;

  // Read consistency settings
  ReadConsistency read_consistency = 4;

  // Write consistency settings
  WriteConsistency write_consistency = 5;

  // Ordering guarantees
  OrderingConfig ordering = 6;

  // Conflict resolution settings
  gcommon.v1.common.ConflictResolution conflict_resolution = 7;

  // Consistency validation settings
  ConsistencyValidation validation = 8;
}
```

---

### consumer_config.proto {#consumer_config}

**Path**: `gcommon/v1/queue/consumer_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ConsumerConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_config.proto
// version: 1.0.0
// guid: 75004ee5-2574-4d9a-bbf6-5d010b09af89

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerConfig {
  // Consumer timeout (milliseconds)
  int32 timeout_ms = 1 [(buf.validate.field).int32.gt = 0];

  // Maximum messages to poll at once
  int32 max_poll_records = 2 [(buf.validate.field).int32.gte = 0];

  // Fetch minimum bytes
  int32 fetch_min_bytes = 3 [(buf.validate.field).int32.gte = 0];

  // Fetch maximum wait time (milliseconds)
  int32 fetch_max_wait_ms = 4 [(buf.validate.field).int32.gte = 0];

  // Enable auto-offset reset
  bool auto_offset_reset = 5;

  // Consumer priority (for priority-based assignment)
  int32 priority = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### consumer_group_config.proto {#consumer_group_config}

**Path**: `gcommon/v1/queue/consumer_group_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `ConsumerGroupConfig`

**Imports** (7):

- `gcommon/v1/common/load_balancing_strategy.proto`
- `gcommon/v1/common/offset_reset_strategy.proto`
- `gcommon/v1/common/rebalance_strategy.proto`
- `gcommon/v1/queue/auto_commit_config.proto`
- `gcommon/v1/queue/dead_letter_queue_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/consumer_group_config.proto
// version: 1.0.0
// guid: 8f71a5d7-ed37-4020-94fb-4c8960ef1e5d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/load_balancing_strategy.proto";
import "gcommon/v1/common/offset_reset_strategy.proto";
import "gcommon/v1/common/rebalance_strategy.proto";
import "gcommon/v1/queue/auto_commit_config.proto";
import "gcommon/v1/queue/dead_letter_queue_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ConsumerGroupConfig {
  // Load balancing strategy for partition assignment
  gcommon.v1.common.LoadBalancingStrategy load_balancing_strategy = 1;

  // Rebalance strategy when consumers join/leave
  gcommon.v1.common.RebalanceStrategy rebalance_strategy = 2;

  // Session timeout for consumer heartbeats (milliseconds)
  int32 session_timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Heartbeat interval (milliseconds)
  int32 heartbeat_interval_ms = 4 [(buf.validate.field).int32.gte = 0];

  // Maximum poll interval (milliseconds)
  int32 max_poll_interval_ms = 5 [(buf.validate.field).int32.gte = 0];

  // Auto-commit configuration
  AutoCommitConfig auto_commit = 6;

  // Offset reset strategy for new consumers
  gcommon.v1.common.OffsetResetStrategy offset_reset_strategy = 7;

  // Maximum number of consumers allowed in the group
  int32 max_consumers = 8 [(buf.validate.field).int32.gte = 0];

  // Enable exactly-once semantics
  bool exactly_once_enabled = 9;

  // Dead letter queue configuration
  DeadLetterQueueConfig dlq_config = 10;
}
```

---

### dead_letter_config.proto {#dead_letter_config}

**Path**: `gcommon/v1/queue/dead_letter_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `DeadLetterConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/dead_letter_config.proto
// file: proto/gcommon/v1/queue/dead_letter_config.proto
// version: 1.0.0
// guid: 8a7b6c5d-4e3f-2a1b-0c9d-8e7f6a5b4c3d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for dead letter queue behavior.
 * Defines how messages that cannot be processed are handled.
 */
message DeadLetterConfig {
  // Whether dead letter queue functionality is enabled
  bool enabled = 1;

  // Name of the dead letter queue
  string dead_letter_queue_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Maximum number of delivery attempts before sending to DLQ
  int32 max_delivery_attempts = 3;

  // Time to live for messages in the dead letter queue
  google.protobuf.Duration ttl = 4;

  // Whether to preserve the original message headers
  bool preserve_headers = 5;

  // Additional metadata to attach to dead letter messages
  map<string, string> additional_metadata = 6;
}
```

---

### dead_letter_queue_config.proto {#dead_letter_queue_config}

**Path**: `gcommon/v1/queue/dead_letter_queue_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `DeadLetterQueueConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/dead_letter_queue_config.proto
// version: 1.0.0
// guid: f8d651b6-6f08-48f8-96a3-ad28ada68da7

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeadLetterQueueConfig {
  // Enable dead letter queue
  bool enabled = 1;

  // Dead letter queue topic
  string dlq_topic = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum message age in DLQ (seconds)
  int64 dlq_max_age_seconds = 3 [(buf.validate.field).int64.gte = 0];

  // Include original error information
  bool include_error_info = 4;
}
```

---

### delivery_configuration.proto {#delivery_configuration}

**Path**: `gcommon/v1/queue/delivery_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 40

**Messages** (1): `DeliveryConfiguration`

**Imports** (5):

- `gcommon/v1/queue/batch_delivery_config.proto`
- `gcommon/v1/queue/delivery_retry_config.proto`
- `gcommon/v1/queue/flow_control_settings.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_configuration.proto
// version: 1.0.0
// guid: 4f995a26-dac9-451d-9d56-fb21aa66e2fa

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/batch_delivery_config.proto";
import "gcommon/v1/queue/delivery_retry_config.proto";
import "gcommon/v1/queue/flow_control_settings.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeliveryConfiguration {
  // Delivery endpoint (for push subscriptions)
  string push_endpoint = 1 [(buf.validate.field).string.min_len = 1];

  // Delivery timeout (milliseconds)
  int32 delivery_timeout_ms = 2 [(buf.validate.field).int32.gt = 0];

  // Retry configuration for failed deliveries
  DeliveryRetryConfig retry_config = 3;

  // Batch delivery settings
  BatchDeliveryConfig batch_config = 4;

  // Flow control settings
  FlowControlSettings flow_control = 5;

  // Enable compression for delivery
  bool enable_compression = 6;

  // Authentication for push endpoints
  map<string, string> auth_headers = 7;
}
```

---

### delivery_retry_config.proto {#delivery_retry_config}

**Path**: `gcommon/v1/queue/delivery_retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `DeliveryRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/delivery_retry_config.proto
// version: 1.0.0
// guid: b4d42c13-fbcd-4e8b-a74d-ac360b2f5814

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message DeliveryRetryConfig {
  // Enable retry on delivery failures
  bool enabled = 1;

  // Maximum retry attempts
  int32 max_retries = 2 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 4 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 5 [(buf.validate.field).double.gte = 0.0];

  // Retry only for specific error codes
  repeated string retry_error_codes = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### deserialization_config.proto {#deserialization_config}

**Path**: `gcommon/v1/queue/deserialization_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `DeserializationConfig`

**Imports** (3):

- `gcommon/v1/common/serialization_format.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/deserialization_config.proto
// file: proto/gcommon/v1/queue/deserialization_config.proto
// version: 1.0.0
// guid: 1b2c3d4e-5f6a-7b8c-9d0e-1f2a3b4c5d6e
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/serialization_format.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message deserialization.
 */
message DeserializationConfig {
  // Supported serialization formats
  repeated gcommon.v1.common.SerializationFormat supported_formats = 1 [(buf.validate.field).repeated.min_items = 1];

  // Default format if not specified
  gcommon.v1.common.SerializationFormat default_format = 2;

  // Whether to validate schema during deserialization
  bool validate_schema = 3;

  // Whether to allow unknown fields
  bool allow_unknown_fields = 4;

  // Custom deserializer class name
  string custom_deserializer = 5 [(buf.validate.field).string.min_len = 1];

  // Maximum message size for deserialization (bytes)
  uint64 max_message_size = 6 [(buf.validate.field).uint64.gte = 0];
}
```

---

### durability_config.proto {#durability_config}

**Path**: `gcommon/v1/queue/durability_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 49

**Messages** (1): `DurabilityConfig`

**Imports** (5):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/common/flush_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/durability_config.proto
// file: proto/gcommon/v1/queue/durability_config.proto
// version: 1.0.0
// guid: 1a0b9c8d-7e6f-5a4b-3c2d-1e0f9a8b7c6d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/common/flush_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message durability and persistence.
 */
message DurabilityConfig {
  // Whether messages are persisted to disk
  bool persistent = 1;

  // Flush policy for writing messages to storage
  gcommon.v1.common.FlushPolicy flush_policy = 2;

  // Number of replicas for each message
  int32 replication_factor = 3 [(buf.validate.field).int32.gte = 0];

  // Acknowledgment level required before considering message durable
  gcommon.v1.common.AckLevel ack_level = 4;

  // Timeout for durability operations
  google.protobuf.Duration durability_timeout = 5;

  // Whether to use write-ahead logging
  bool write_ahead_log = 6;

  // Sync frequency for flushing to disk
  google.protobuf.Duration sync_interval = 7;

  // Whether to verify checksums on read
  bool verify_checksums = 8;
}
```

---

### encryption_config.proto {#encryption_config}

**Path**: `gcommon/v1/queue/encryption_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `QueueEncryptionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/encryption_config.proto
// file: proto/gcommon/v1/queue/encryption_config.proto
// version: 1.0.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message encryption in queues.
 */
message QueueEncryptionConfig {
  // Whether encryption is enabled
  bool enabled = 1;

  // Encryption algorithm (AES256, ChaCha20, etc.)
  string algorithm = 2 [(buf.validate.field).string.min_len = 1];

  // Key derivation function (PBKDF2, scrypt, argon2)
  string key_derivation = 3 [(buf.validate.field).string.min_len = 1];

  // Encryption key identifier
  string key_id = 4 [(buf.validate.field).string.min_len = 1];

  // Whether to encrypt message headers
  bool encrypt_headers = 5;

  // Whether to encrypt routing keys
  bool encrypt_routing_keys = 6;

  // Key rotation interval in hours
  uint32 rotation_interval_hours = 7 [(buf.validate.field).uint32.gte = 0];
}
```

---

### error_action_config.proto {#error_action_config}

**Path**: `gcommon/v1/queue/error_action_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `ErrorActionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_action_config.proto
// version: 1.0.0
// guid: 97538011-4ce0-4da2-8495-54204f07556a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorActionConfig {
  // Error code or pattern
  string error_pattern = 1 [(buf.validate.field).string.min_len = 1];

  // Action to take (retry, dlq, drop, pause)
  string action = 2 [(buf.validate.field).string.min_len = 1];

  // Action parameters
  map<string, string> action_params = 3;
}
```

---

### error_handling_config.proto {#error_handling_config}

**Path**: `gcommon/v1/queue/error_handling_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 34

**Messages** (1): `ErrorHandlingConfig`

**Imports** (5):

- `gcommon/v1/queue/dead_letter_queue_config.proto`
- `gcommon/v1/queue/error_action_config.proto`
- `gcommon/v1/queue/error_notification_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_handling_config.proto
// version: 1.0.0
// guid: 49c9649a-c944-4438-b21f-d3645782576f

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/dead_letter_queue_config.proto";
import "gcommon/v1/queue/error_action_config.proto";
import "gcommon/v1/queue/error_notification_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorHandlingConfig {
  // Dead letter queue configuration
  DeadLetterQueueConfig dlq_config = 1;

  // Maximum delivery attempts before DLQ
  int32 max_delivery_attempts = 2 [(buf.validate.field).int32.gte = 0];

  // Actions to take on specific errors
  repeated ErrorActionConfig error_actions = 3 [(buf.validate.field).repeated.min_items = 1];

  // Enable error logging
  bool enable_error_logging = 4;

  // Error notification settings
  ErrorNotificationConfig notification_config = 5;
}
```

---

### error_notification_config.proto {#error_notification_config}

**Path**: `gcommon/v1/queue/error_notification_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `ErrorNotificationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/error_notification_config.proto
// version: 1.0.0
// guid: 0fffcb32-c66a-4876-acb0-c7d756601f4d

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ErrorNotificationConfig {
  // Enable error notifications
  bool enabled = 1;

  // Notification channels
  repeated string notification_channels = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error threshold for notifications
  int32 error_threshold = 3 [(buf.validate.field).int32.gte = 0];

  // Notification frequency (seconds)
  int32 notification_frequency_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### exchange_config.proto {#exchange_config}

**Path**: `gcommon/v1/queue/exchange_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `ExchangeConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/exchange_config.proto
// file: proto/gcommon/v1/queue/exchange_config.proto
// version: 1.0.0
// guid: 4e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message exchange operations between queues.
 */
message ExchangeConfig {
  // Exchange name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Exchange type (direct, topic, fanout, headers)
  string exchange_type = 2;

  // Whether exchange is durable
  bool durable = 3;

  // Whether to auto-delete when unused
  bool auto_delete = 4;

  // Whether exchange is internal
  bool internal = 5;

  // Custom exchange arguments
  map<string, string> arguments = 6;

  // Routing configuration
  string routing_key = 7;

  // Whether to enable alternate exchange
  string alternate_exchange = 8;
}
```

---

### flow_control_config.proto {#flow_control_config}

**Path**: `gcommon/v1/queue/flow_control_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `FlowControlConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/flow_control_config.proto
// version: 1.0.0
// guid: e0dba279-5bac-45a2-8bd5-b341fa734230

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message FlowControlConfig {
  // Enable flow control
  bool enabled = 1;

  // Maximum outstanding messages
  int32 max_outstanding_messages = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Maximum outstanding bytes
  int64 max_outstanding_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Flow control algorithm (token_bucket, leaky_bucket, sliding_window)
  string algorithm = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### header_routing_config.proto {#header_routing_config}

**Path**: `gcommon/v1/queue/header_routing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `HeaderRoutingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/header_routing_config.proto
// version: 1.0.0
// guid: 048332dd-afed-41ee-b803-dd1574fd07d9

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Header-based routing configuration.
 */
message HeaderRoutingConfig {
  // Header key to use for routing
  string routing_header = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to use exact match or pattern matching
  bool exact_match = 2;

  // Case sensitivity for header matching
  bool case_sensitive = 3;
}
```

---

### load_balancing_config.proto {#load_balancing_config}

**Path**: `gcommon/v1/queue/load_balancing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `LoadBalancingConfig`

**Imports** (3):

- `gcommon/v1/common/load_balancing_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/load_balancing_config.proto
// version: 1.1.0
// guid: 8e9f0a1b-2c3d-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/load_balancing_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for load balancing across queue consumers.
 */
message LoadBalancingConfig {
  // Load balancing strategy
  gcommon.v1.common.LoadBalancingStrategy strategy = 1;

  // Weight for this consumer (for weighted strategies)
  int32 weight = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum concurrent messages per consumer
  int32 max_concurrent_messages = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Prefetch count for batch consumption
  int32 prefetch_count = 4 [(buf.validate.field).int32.gte = 0];

  // Consumer priority (higher numbers = higher priority)
  int32 priority = 5 [(buf.validate.field).int32.gte = 0];

  // Whether to enable sticky sessions
  bool sticky_sessions = 6;

  // Session affinity key
  string affinity_key = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### message_filter_config.proto {#message_filter_config}

**Path**: `gcommon/v1/queue/message_filter_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 35

**Messages** (1): `MessageFilterConfig`

**Imports** (3):

- `gcommon/v1/queue/content_filter.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/message_filter_config.proto
// version: 1.0.0
// guid: e63e4778-4555-4c0c-a835-7f83564e8513

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/content_filter.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MessageFilterConfig {
  // Header-based filters
  map<string, string> header_filters = 1;

  // Content-based filters
  repeated ContentFilter content_filters = 2 [(buf.validate.field).repeated.min_items = 1];

  // Routing key patterns
  repeated string routing_key_patterns = 3 [(buf.validate.field).repeated.min_items = 1];

  // Message type filters
  repeated string message_types = 4 [(buf.validate.field).repeated.min_items = 1];

  // Custom filter expressions
  repeated string filter_expressions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Exclude messages matching these criteria
  bool exclude_matching = 6;
}
```

---

### migration_config.proto {#migration_config}

**Path**: `gcommon/v1/queue/migration_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `MigrationConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/migration_config.proto
// file: proto/gcommon/v1/queue/migration_config.proto
// version: 1.0.0
// guid: 3d4e5f6a-7b8c-9d0e-1f2a-3b4c5d6e7f8a
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for queue migration operations.
 */
message MigrationConfig {
  // Source queue configuration
  string source_queue = 1 [(buf.validate.field).string.min_len = 1];

  // Destination queue configuration
  string destination_queue = 2 [(buf.validate.field).string.min_len = 1];

  // Migration strategy (live, batch, hybrid)
  string migration_strategy = 3 [(buf.validate.field).string.min_len = 1];

  // Batch size for batch migration
  uint32 batch_size = 4 [(buf.validate.field).uint32.gte = 0];

  // Migration timeout
  google.protobuf.Duration timeout = 5;

  // Whether to verify data integrity
  bool verify_integrity = 6;

  // Whether to keep source after migration
  bool keep_source = 7;

  // Maximum concurrent operations
  uint32 max_concurrency = 8 [(buf.validate.field).uint32.gte = 0];
}
```

---

### monitoring_config.proto {#monitoring_config}

**Path**: `gcommon/v1/queue/monitoring_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `QueueMonitoringConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/monitoring_config.proto
// version: 1.0.0
// guid: 81f93ee4-708c-478c-9c19-1baf15830c08

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// MonitoringConfig controls runtime monitoring for a queue.
message QueueMonitoringConfig {
  // Enable or disable monitoring for this queue.
  bool enabled = 1;

  // Optional endpoint for publishing metrics.
  string metrics_endpoint = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### multi_value_config.proto {#multi_value_config}

**Path**: `gcommon/v1/queue/multi_value_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `MultiValueConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/multi_value_config.proto
// version: 1.0.0
// guid: 9ed9dcb6-f12f-4eea-92c1-7ee4a199f462

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message MultiValueConfig {
  // Maximum number of concurrent values to keep
  int32 max_values = 1 [(buf.validate.field).int32.gte = 0];

  // Value expiration time (seconds)
  int32 value_ttl_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Conflict value cleanup strategy
  string cleanup_strategy = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### offset_config.proto {#offset_config}

**Path**: `gcommon/v1/queue/offset_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `OffsetConfig`

**Imports** (4):

- `gcommon/v1/common/offset_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/offset_config.proto
// version: 1.0.0
// guid: 4c4657d1-5745-47d4-b9e3-6e685a1d4785

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/offset_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OffsetConfig {
  // Offset type (earliest, latest, timestamp, specific)
  gcommon.v1.common.OffsetType offset_type = 1;

  // Specific offset value (when offset_type = specific)
  int64 offset_value = 2 [(buf.validate.field).int64.gte = 0];

  // Timestamp to start from (when offset_type = timestamp)
  google.protobuf.Timestamp start_timestamp = 3;

  // Reset to beginning if offset not found
  bool reset_on_not_found = 4;
}
```

---

### ordering_config.proto {#ordering_config}

**Path**: `gcommon/v1/queue/ordering_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 32

**Messages** (1): `OrderingConfig`

**Imports** (3):

- `gcommon/v1/common/ordering_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/ordering_config.proto
// version: 1.0.0
// guid: 38b7cd46-8313-4c25-86de-04401a1cb1ae

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ordering_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message OrderingConfig {
  // Global ordering guarantee level
  gcommon.v1.common.OrderingLevel global_ordering = 1;

  // Per-partition ordering guarantee
  gcommon.v1.common.OrderingLevel partition_ordering = 2;

  // Per-producer ordering guarantee
  gcommon.v1.common.OrderingLevel producer_ordering = 3;

  // Enable causal ordering
  bool causal_ordering = 4;

  // Ordering timeout (milliseconds)
  int32 ordering_timeout_ms = 5 [(buf.validate.field).int32.gt = 0];
}
```

---

### partition_config.proto {#partition_config}

**Path**: `gcommon/v1/queue/partition_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `PartitionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/partition_config.proto
// file: proto/gcommon/v1/queue/partition_config.proto
// version: 1.0.0
// guid: 0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for queue partitioning.
 */
message PartitionConfig {
  // Number of partitions
  uint32 partition_count = 1 [(buf.validate.field).uint32.gte = 0];

  // Partitioning strategy (hash, round-robin, custom)
  string partition_strategy = 2 [(buf.validate.field).string.min_len = 1];

  // Key field to use for partitioning
  string partition_key = 3 [(buf.validate.field).string.min_len = 1];

  // Custom partition function (if strategy is custom)
  string custom_partition_function = 4 [(buf.validate.field).string.min_len = 1];

  // Whether to enable partition auto-scaling
  bool auto_scale = 5;

  // Minimum number of partitions
  uint32 min_partitions = 6 [(buf.validate.field).uint32.gte = 0];

  // Maximum number of partitions
  uint32 max_partitions = 7 [(buf.validate.field).uint32.gte = 0];

  // Partition size threshold for auto-scaling (in MB)
  uint64 scale_threshold_mb = 8 [(buf.validate.field).uint64.gte = 0];
}
```

---

### performance_config.proto {#performance_config}

**Path**: `gcommon/v1/queue/performance_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 56

**Messages** (1): `PerformanceConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/performance_config.proto
// file: proto/gcommon/v1/queue/performance_config.proto
// version: 1.0.0
// guid: 2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for performance tuning and optimization.
 */
message PerformanceConfig {
  // Buffer size for batching operations
  uint32 buffer_size = 1 [(buf.validate.field).uint32.gte = 0];

  // Maximum batch size for operations
  uint32 max_batch_size = 2 [(buf.validate.field).uint32.gte = 0];

  // Flush interval for buffered operations
  google.protobuf.Duration flush_interval = 3;

  // Number of worker threads
  uint32 worker_threads = 4 [(buf.validate.field).uint32.gte = 0];

  // Queue capacity for in-memory operations
  uint32 queue_capacity = 5 [(buf.validate.field).uint32.gte = 0];

  // Enable async processing
  bool async_processing = 6;

  // Connection pool size
  uint32 connection_pool_size = 7 [(buf.validate.field).uint32.gte = 0];

  // Maximum idle time for connections
  google.protobuf.Duration max_idle_time = 8;

  // Enable connection multiplexing
  bool enable_multiplexing = 9;

  // Read timeout
  google.protobuf.Duration read_timeout = 10;

  // Write timeout
  google.protobuf.Duration write_timeout = 11;
}
```

---

### publish_config.proto {#publish_config}

**Path**: `gcommon/v1/queue/publish_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 38

**Messages** (1): `PublishConfig`

**Imports** (3):

- `gcommon/v1/common/retry_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/publish_config.proto
// version: 1.0.0
// guid: 684eaa80-e0bc-4fa2-876a-8d97d9865ae8

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/retry_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message PublishConfig {
  // Wait for acknowledgment before returning
  bool wait_for_ack = 1;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 2 [(buf.validate.field).int32.gt = 0];

  // Enable duplicate detection
  bool duplicate_detection = 3;

  // Compression for message batch
  bool enable_compression = 4;

  // Enable message ordering
  bool enable_ordering = 5;

  // Retry configuration for failed publishes - references existing RetryConfig
  gcommon.v1.common.CommonRetryPolicy retry_config = 6;

  // Persistence level required
  string persistence_level = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### queue_config.proto {#queue_config}

**Path**: `gcommon/v1/queue/queue_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `QueueConfig`

**Imports** (5):

- `gcommon/v1/common/priority_level.proto`
- `gcommon/v1/common/queue_type.proto`
- `gcommon/v1/common/retention_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_config.proto
// version: 1.0.0
// guid: c64defde-30d1-41e5-bfac-b415cbf929c6

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/priority_level.proto";
import "gcommon/v1/common/queue_type.proto";
import "gcommon/v1/common/retention_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// QueueConfig defines settings for creating a queue instance.
message QueueConfig {
  // Name of the queue.
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  // Queue implementation type.
  gcommon.v1.common.QueueType type = 2;
  // Number of partitions for the queue.
  int32 partitions = 3;
  // Retention policy for stored messages.
  gcommon.v1.common.MetricsRetentionPolicy retention = 4;
  // Default priority applied when publishing.
  gcommon.v1.common.PriorityLevel default_priority = 5;
  // If true, queue persists messages to disk.
  bool durable = 6;
  // Whether the queue should be automatically deleted when unused.
  bool auto_delete = 7;
}
```

---

### queue_configuration.proto {#queue_configuration}

**Path**: `gcommon/v1/queue/queue_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 23

**Messages** (1): `QueueConfiguration`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/queue_configuration.proto
// version: 1.0.0
// guid: a7660f75-3be5-49a6-bcd6-fc522e7e5c9a

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message QueueConfiguration {
  int64 max_messages = 1 [(buf.validate.field).int64.gte = 0];
  google.protobuf.Duration visibility_timeout = 2;
  google.protobuf.Duration message_retention_period = 3;
  int32 max_retry_attempts = 4 [(buf.validate.field).int32.gte = 0];
  bool dead_letter_queue_enabled = 5;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/queue/rate_limit_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 26

**Messages** (1): `QueueRateLimitConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/rate_limit_config.proto
// version: 1.0.0
// guid: 436ea189-70d7-4f1d-bf93-3c88f1f0de3b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// RateLimitConfig defines throughput limits for a queue.
message QueueRateLimitConfig {
  // Maximum messages allowed per second.
  int32 max_per_second = 1 [(buf.validate.field).int32.gte = 0];

  // Allowed burst capacity above the per-second rate.
  int32 burst = 2 [(buf.validate.field).int32.gte = 0];

  // Whether rate limiting is enabled.
  bool enabled = 3;
}
```

---

### read_retry_config.proto {#read_retry_config}

**Path**: `gcommon/v1/queue/read_retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `ReadRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/read_retry_config.proto
// version: 1.0.0
// guid: 123c273c-25e2-4af1-85ab-48ac7f8a28d5

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ReadRetryConfig {
  // Maximum retry attempts
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Retry on different replica
  bool retry_different_replica = 5;
}
```

---

### replication_config.proto {#replication_config}

**Path**: `gcommon/v1/queue/replication_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `ReplicationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/replication_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ReplicationConfig message definition.
message ReplicationConfig {
  // Number of replicas
  int32 replica_count = 1 [(buf.validate.field).int32.gte = 0];

  // Replication factor
  int32 factor = 2 [(buf.validate.field).int32.gte = 0];

  // Enable synchronous replication
  bool synchronous = 3;

  // Minimum in-sync replicas
  int32 min_in_sync_replicas = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

### restore_config.proto {#restore_config}

**Path**: `gcommon/v1/queue/restore_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 47

**Messages** (1): `RestoreConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/restore_config.proto
// file: proto/gcommon/v1/queue/restore_config.proto
// version: 1.0.0
// guid: 9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for queue restore operations.
 */
message RestoreConfig {
  // Source backup location
  string backup_source = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to verify backup integrity before restore
  bool verify_integrity = 2;

  // Restore strategy (full, incremental, selective)
  string restore_strategy = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to overwrite existing data
  bool overwrite_existing = 4;

  // Restore timeout
  google.protobuf.Duration timeout = 5;

  // Whether to preserve original timestamps
  bool preserve_timestamps = 6;

  // Maximum concurrent restore operations
  uint32 max_concurrency = 7 [(buf.validate.field).uint32.gte = 0];

  // Whether to skip corrupted messages
  bool skip_corrupted = 8;
}
```

---

### retry_config.proto {#retry_config}

**Path**: `gcommon/v1/queue/retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 44

**Messages** (1): `QueueRetryConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/retry_config.proto
// file: proto/gcommon/v1/queue/retry_config.proto
// version: 1.0.0
// guid: 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for retry behavior in queue operations.
 */
message QueueRetryConfig {
  // Whether retry is enabled
  bool enabled = 1;

  // Maximum number of retry attempts
  uint32 max_retries = 2 [(buf.validate.field).uint32.gte = 0];

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 3;

  // Maximum delay between retries
  google.protobuf.Duration max_delay = 4;

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 5 [(buf.validate.field).double.gte = 0.0];

  // Jitter factor to randomize delays (0.0 to 1.0)
  double jitter_factor = 6 [(buf.validate.field).double.gte = 0.0];

  // Total timeout for all retry attempts
  google.protobuf.Duration total_timeout = 7;
}
```

---

### retry_delay_config.proto {#retry_delay_config}

**Path**: `gcommon/v1/queue/retry_delay_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `RetryDelayConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/retry_delay_config.proto
// version: 1.0.0
// guid: b8735b0b-be09-4ce0-8445-a49b8b97e6db

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message RetryDelayConfig {
  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier for exponential backoff
  double backoff_multiplier = 3 [(buf.validate.field).double.gte = 0.0];

  // Enable jitter for retry delays
  bool jitter_enabled = 4;
}
```

---

### routing_config.proto {#routing_config}

**Path**: `gcommon/v1/queue/routing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `RoutingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/routing_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174002

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// RoutingConfig message definition.
message RoutingConfig {
  // Routing strategy
  string strategy = 1 [(buf.validate.field).string.min_len = 1];

  // Routing key pattern
  string key_pattern = 2 [(buf.validate.field).string.min_len = 1];

  // Enable sticky routing
  bool sticky = 3;

  // Load balancing algorithm
  string load_balancer = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### schema_config.proto {#schema_config}

**Path**: `gcommon/v1/queue/schema_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 29

**Messages** (1): `SchemaConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/schema_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174003

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// SchemaConfig message definition.
message SchemaConfig {
  // Schema version
  int32 version = 1 [(buf.validate.field).int32.gte = 0];

  // Schema definition
  string definition = 2 [(buf.validate.field).string.min_len = 1];

  // Schema type
  string type = 3 [(buf.validate.field).string.min_len = 1];

  // Enable schema validation
  bool validate = 4;
}
```

---

### serialization_config.proto {#serialization_config}

**Path**: `gcommon/v1/queue/serialization_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 52

**Messages** (1): `SerializationConfig`

**Imports** (5):

- `gcommon/v1/common/compression_algorithm.proto`
- `gcommon/v1/common/serialization_format.proto`
- `gcommon/v1/queue/format_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/serialization_config.proto
// version: 1.0.0
// guid: e5f6a7b8-9c0d-1e2f-3a4b-5c6d7e8f9a0b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/compression_algorithm.proto";
import "gcommon/v1/common/serialization_format.proto";
import "gcommon/v1/queue/format_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message serialization and deserialization.
 */
message SerializationConfig {
  // Default serialization format
  gcommon.v1.common.SerializationFormat default_format = 1;

  // Supported serialization formats
  repeated gcommon.v1.common.SerializationFormat supported_formats = 2 [(buf.validate.field).repeated.min_items = 1];

  // Whether to auto-detect format from message headers
  bool auto_detect_format = 3;

  // Default compression algorithm
  gcommon.v1.common.CompressionAlgorithm default_compression = 4;

  // Supported compression algorithms
  repeated gcommon.v1.common.CompressionAlgorithm supported_compressions = 5 [(buf.validate.field).repeated.min_items = 1];

  // Whether to auto-detect compression from message headers
  bool auto_detect_compression = 6;

  // Format-specific options
  map<string, FormatOptions> format_options = 7;

  // Whether to validate message format on deserialization
  bool validate_on_deserialize = 8;

  // Maximum message size for serialization
  uint64 max_message_size = 9 [(buf.validate.field).uint64.gte = 0];

  // Whether to enable backwards compatibility mode
  bool backwards_compatible = 10;
}
```

---

### stream_config.proto {#stream_config}

**Path**: `gcommon/v1/queue/stream_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 51

**Messages** (1): `StreamConfig`

**Imports** (4):

- `gcommon/v1/common/stream_restart_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/stream_config.proto
// file: proto/gcommon/v1/queue/stream_config.proto
// version: 1.0.0
// guid: 7a6b5c4d-3e2f-1a0b-9c8d-7e6f5a4b3c2d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/stream_restart_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for streaming message consumption.
 */
message StreamConfig {
  // Maximum number of messages to buffer
  int32 buffer_size = 1 [(buf.validate.field).int32.gte = 0];

  // Timeout for stream read operations
  google.protobuf.Duration read_timeout = 2;

  // Whether to enable flow control
  bool flow_control_enabled = 3;

  // Maximum outstanding messages before flow control kicks in
  int32 max_outstanding_messages = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Maximum outstanding bytes before flow control kicks in
  int64 max_outstanding_bytes = 5 [(buf.validate.field).int64.gte = 0];

  // Whether to automatically acknowledge messages
  bool auto_ack = 6;

  // Acknowledgment deadline for manually acknowledged messages
  google.protobuf.Duration ack_deadline = 7;

  // Whether to enable message ordering
  bool enable_message_ordering = 8;

  // Stream restart policy on failure
  gcommon.v1.common.StreamRestartPolicy restart_policy = 9;
}
```

---

### subscription_config.proto {#subscription_config}

**Path**: `gcommon/v1/queue/subscription_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `SubscriptionConfig`

**Imports** (6):

- `gcommon/v1/common/priority_level.proto`
- `gcommon/v1/common/routing_strategy.proto`
- `gcommon/v1/common/subscription_state.proto`
- `gcommon/v1/queue/delivery_options.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_config.proto
// version: 1.0.0
// guid: 27b1d56b-2e7b-4003-9ddd-6b30086ff0fb

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/priority_level.proto";
import "gcommon/v1/common/routing_strategy.proto";
import "gcommon/v1/common/subscription_state.proto";
import "gcommon/v1/queue/delivery_options.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// SubscriptionConfig describes how a consumer subscribes to a queue.
message SubscriptionConfig {
  // Name of the subscription.
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  // Current state of the subscription.
  gcommon.v1.common.SubscriptionState state = 2;
  // Message routing strategy for this subscription.
  gcommon.v1.common.RoutingStrategy routing_strategy = 3;
  // Default priority applied to published messages if unspecified.
  gcommon.v1.common.PriorityLevel default_priority = 4;
  // Delivery options controlling retries and dead letter handling.
  DeliveryOptions delivery_options = 5;
  // Maximum number of unacknowledged messages allowed.
  int32 max_inflight = 6;
}
```

---

### subscription_config_update.proto {#subscription_config_update}

**Path**: `gcommon/v1/queue/subscription_config_update.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `SubscriptionConfigUpdate`

**Imports** (6):

- `gcommon/v1/common/config_retry_settings.proto`
- `gcommon/v1/queue/delivery_settings.proto`
- `gcommon/v1/queue/filter_settings.proto`
- `gcommon/v1/queue/routing_settings.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_config_update.proto
// version: 1.0.0
// guid: 4ec44184-d7ed-48cf-af8f-5984c57c687d

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/config_retry_settings.proto";
import "gcommon/v1/queue/delivery_settings.proto";
import "gcommon/v1/queue/filter_settings.proto";
import "gcommon/v1/queue/routing_settings.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SubscriptionConfigUpdate {
  // Updated subscription name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Updated delivery settings
  DeliverySettings delivery_settings = 2;

  // Updated retry configuration
  gcommon.v1.common.ConfigRetrySettings retry_settings = 3;

  // Updated filtering rules
  FilterSettings filter_settings = 4;

  // Updated routing configuration
  RoutingSettings routing_settings = 5;

  // Maximum inflight messages
  int32 max_inflight_messages = 6;

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 7;

  // Priority level for messages
  int32 priority_level = 8;
}
```

---

### subscription_configuration.proto {#subscription_configuration}

**Path**: `gcommon/v1/queue/subscription_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `SubscriptionConfiguration`

**Imports** (4):

- `gcommon/v1/common/ack_level.proto`
- `gcommon/v1/common/delivery_mode.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/subscription_configuration.proto
// version: 1.0.0
// guid: c1883113-aa7a-4cba-b38a-4d695cefecf3

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/ack_level.proto";
import "gcommon/v1/common/delivery_mode.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message SubscriptionConfiguration {
  // Acknowledgment level required
  gcommon.v1.common.AckLevel ack_level = 1;

  // Delivery mode for messages
  gcommon.v1.common.DeliveryMode delivery_mode = 2;

  // Maximum number of unacknowledged messages
  int32 max_unacked_messages = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Acknowledgment timeout (milliseconds)
  int32 ack_timeout_ms = 4 [(buf.validate.field).int32.gt = 0];

  // Message priority filter (minimum priority)
  int32 min_priority = 5 [(buf.validate.field).int32.gte = 0];

  // Enable message ordering
  bool ordered_delivery = 6;

  // Auto-acknowledge messages after delivery
  bool auto_acknowledge = 7;

  // Subscription expiration time (seconds, 0 = no expiration)
  int64 expiration_seconds = 8 [(buf.validate.field).int64.gte = 0];

  // Enable duplicate message detection
  bool duplicate_detection = 9;

  // Maximum message age to accept (seconds)
  int64 max_message_age_seconds = 10 [(buf.validate.field).int64.gte = 0];
}
```

---

### timeout_config.proto {#timeout_config}

**Path**: `gcommon/v1/queue/timeout_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 45

**Messages** (1): `QueueTimeoutConfig`

**Imports** (2):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/timeout_config.proto
// file: proto/gcommon/v1/queue/timeout_config.proto
// version: 1.0.1
// guid: 3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Timeout configuration for various queue operations.
 */
message QueueTimeoutConfig {
  // Timeout for message publishing operations
  google.protobuf.Duration publish_timeout = 1;

  // Timeout for message consumption operations
  google.protobuf.Duration consume_timeout = 2;

  // Timeout for acknowledgment operations
  google.protobuf.Duration ack_timeout = 3;

  // Timeout for connection establishment
  google.protobuf.Duration connect_timeout = 4;

  // Timeout for message processing before automatic nack
  google.protobuf.Duration processing_timeout = 5;

  // Timeout for queue management operations (create, delete, etc.)
  google.protobuf.Duration management_timeout = 6;

  // Timeout for health check operations
  google.protobuf.Duration health_check_timeout = 7;

  // Timeout for subscription operations
  google.protobuf.Duration subscription_timeout = 8;
}
```

---

### timestamp_config.proto {#timestamp_config}

**Path**: `gcommon/v1/queue/timestamp_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `TimestampConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/timestamp_config.proto
// version: 1.0.0
// guid: 5767f48a-e0df-4536-9127-4fcbd0ed4e1e

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TimestampConfig {
  // Timestamp source (system, ntp, atomic)
  string source = 1 [(buf.validate.field).string.min_len = 1];

  // Clock synchronization interval (seconds)
  int32 sync_interval_seconds = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum timestamp skew tolerance (milliseconds)
  int64 max_skew_ms = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### topic_config.proto {#topic_config}

**Path**: `gcommon/v1/queue/topic_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 48

**Messages** (1): `TopicConfig`

**Imports** (4):

- `gcommon/v1/queue/partition_config.proto`
- `gcommon/v1/queue/retention_policy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/topic_config.proto
// file: proto/gcommon/v1/queue/topic_config.proto
// version: 1.0.0
// guid: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/partition_config.proto";
import "gcommon/v1/queue/retention_policy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration settings for a topic.
 */
message TopicConfig {
  // Maximum number of messages in the topic
  uint64 max_messages = 1 [(buf.validate.field).uint64.gte = 0];

  // Maximum size of the topic in bytes
  uint64 max_size_bytes = 2 [(buf.validate.field).uint64.gte = 0];

  // Message retention policy
  QueueRetentionPolicy retention_policy = 3;

  // Partitioning configuration
  PartitionConfig partition_config = 4;

  // Whether messages are persistent
  bool persistent = 5;

  // Whether topic is replicated
  bool replicated = 6;

  // Replication factor
  uint32 replication_factor = 7 [(buf.validate.field).uint32.gte = 0];

  // Whether to compact duplicate messages
  bool enable_compaction = 8;
}
```

---

### topic_configuration.proto {#topic_configuration}

**Path**: `gcommon/v1/queue/topic_configuration.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `TopicConfiguration`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_configuration.proto
// version: 1.0.0
// guid: 5214c267-e8b7-4b1c-af8d-d3343914c498

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message TopicConfiguration {
  // Number of partitions
  int32 partition_count = 1 [(buf.validate.field).int32.gte = 0];

  // Replication factor
  int32 replication_factor = 2 [(buf.validate.field).int32.gte = 0];

  // Message retention period (seconds)
  int64 retention_period_seconds = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum message size (bytes)
  int64 max_message_size_bytes = 4 [(buf.validate.field).int64.gte = 0];

  // Compression enabled
  bool compression_enabled = 5;

  // Compression algorithm
  string compression_algorithm = 6 [(buf.validate.field).string.min_len = 1];

  // Encryption enabled
  bool encryption_enabled = 7;

  // Cleanup policy (delete, compact)
  string cleanup_policy = 8 [(buf.validate.field).string.min_len = 1];

  // Minimum in-sync replicas
  int32 min_insync_replicas = 9 [(buf.validate.field).int32.gte = 0];

  // Segment size (bytes)
  int64 segment_size_bytes = 10 [(buf.validate.field).int64.gte = 0];
}
```

---

### topic_routing_config.proto {#topic_routing_config}

**Path**: `gcommon/v1/queue/topic_routing_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 30

**Messages** (1): `TopicRoutingConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/topic_routing_config.proto
// version: 1.0.0
// guid: 502467f7-3d79-4329-8e44-4e499071092b

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Topic-based routing configuration.
 */
message TopicRoutingConfig {
  // Topic exchange name
  string exchange_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Default routing key
  string default_routing_key = 2;

  // Whether to use wildcard matching
  bool wildcard_matching = 3;
}
```

---

### transformation_config.proto {#transformation_config}

**Path**: `gcommon/v1/queue/transformation_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `TransformationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/config/transformation_config.proto
// file: proto/gcommon/v1/queue/transformation_config.proto
// version: 1.0.0
// guid: 2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f
//
// Message definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Configuration for message transformation operations.
 */
message TransformationConfig {
  // Whether transformation is enabled
  bool enabled = 1;

  // Transformation script or function name
  string transformation_script = 2 [(buf.validate.field).string.min_len = 1];

  // Script language (javascript, python, lua, etc.)
  string script_language = 3 [(buf.validate.field).string.min_len = 1];

  // Whether to transform on ingress
  bool transform_on_ingress = 4;

  // Whether to transform on egress
  bool transform_on_egress = 5;

  // Transformation timeout in milliseconds
  uint64 timeout_ms = 6 [(buf.validate.field).uint64.gte = 0];

  // Maximum script execution memory in MB
  uint32 max_memory_mb = 7 [(buf.validate.field).uint32.gte = 0];

  // Custom transformation parameters
  map<string, string> parameters = 8;
}
```

---

### update_queue_config_request.proto {#update_queue_config_request}

**Path**: `gcommon/v1/queue/update_queue_config_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 43

**Messages** (1): `UpdateQueueConfigRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/queue/queue_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_queue_config_request.proto
// version: 1.0.0
// guid: e2f3a4b5-c6d7-8e9f-0a1b-2c3d4e5f6a7b

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/queue/queue_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Request to update configuration for an existing queue.
 * Allows modification of queue properties after creation.
 */
message UpdateQueueConfigRequest {
  // Name of the queue to update
  string queue_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // New configuration for the queue
  // New queue configuration
  QueueConfig config = 2;

  // Fields to update (field mask)
  repeated string update_mask = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Force update even if it might cause data loss
  bool force = 5;

  // Reason for the configuration update
  string reason = 6;
}
```

---

### update_queue_config_response.proto {#update_queue_config_response}

**Path**: `gcommon/v1/queue/update_queue_config_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 37

**Messages** (1): `UpdateQueueConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/update_queue_config_response.proto
// file: proto/gcommon/v1/queue/update_queue_config_response.proto
// version: 1.0.0
// guid: 6e7f8a9b-0c1d-2e3f-4a5b-6c7d8e9f0a1b
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response for updating queue configuration.
 */
message UpdateQueueConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Error message if update failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Updated configuration version
  uint64 config_version = 3 [(buf.validate.field).uint64.gte = 0];

  // Timestamp of the update
  uint64 updated_at = 4 [(buf.validate.field).uint64.gte = 0];

  // List of configuration fields that were updated
  repeated string updated_fields = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### update_subscription_config_request.proto {#update_subscription_config_request}

**Path**: `gcommon/v1/queue/update_subscription_config_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 41

**Messages** (1): `UpdateSubscriptionConfigRequest`

**Imports** (3):

- `gcommon/v1/queue/subscription_config_update.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_subscription_config_request.proto
// version: 1.0.0
// guid: 9ffb7149-231c-448f-9678-a8fa3130fe10

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/subscription_config_update.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message UpdateSubscriptionConfigRequest {
  // Subscription identifier
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Configuration updates to apply
  SubscriptionConfigUpdate config_update = 2;

  // Specify which fields to update (empty = update all)
  repeated string update_fields = 3 [(buf.validate.field).repeated.min_items = 1];

  // Validate configuration without applying changes
  bool validate_only = 4;

  // Force update even if subscription is active
  bool force_update = 5;

  // Apply changes immediately or schedule for later
  bool immediate_apply = 6;

  // Optional reason for the configuration change
  string change_reason = 7 [(buf.validate.field).string.min_len = 1];

  // Metadata for the update operation
  map<string, string> metadata = 8;
}
```

---

### update_subscription_config_response.proto {#update_subscription_config_response}

**Path**: `gcommon/v1/queue/update_subscription_config_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 33

**Messages** (1): `UpdateSubscriptionConfigResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_subscription_config_response.proto
// version: 1.0.0
// guid: 43035b6d-1872-4b79-af8d-8852b38643e3
// Response for subscription configuration updates

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Response for subscription configuration updates
message UpdateSubscriptionConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Subscription ID that was updated
  string subscription_id = 2 [(buf.validate.field).string.min_len = 1];

  // Configuration changes that were applied
  map<string, string> applied_changes = 3;

  // Validation warnings (non-fatal)
  repeated string warnings = 4 [(buf.validate.field).repeated.min_items = 1];

  // Error message if update failed
  string error = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_topic_config_request.proto {#update_topic_config_request}

**Path**: `gcommon/v1/queue/update_topic_config_request.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `UpdateTopicConfigRequest`

**Imports** (3):

- `gcommon/v1/queue/topic_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/update_topic_config_request.proto
// version: 1.0.0
// guid: b7623d06-10e5-4b18-9b4f-976ff9116f5c
// Request to update topic configuration

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/topic_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// Request to update topic configuration
message UpdateTopicConfigRequest {
  // Topic name to update
  string topic_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // New topic configuration
  TopicConfig config = 2;

  // Whether to validate config before applying
  bool validate_only = 3;

  // Apply changes incrementally if possible
  bool incremental_update = 4;

  // Timeout for the operation (milliseconds)
  int32 timeout_ms = 5;
}
```

---

### update_topic_config_response.proto {#update_topic_config_response}

**Path**: `gcommon/v1/queue/update_topic_config_response.proto` **Package**: `gcommon.v1.queue` **Lines**: 46

**Messages** (1): `UpdateTopicConfigResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/api/update_topic_config_response.proto
// file: proto/gcommon/v1/queue/update_topic_config_response.proto
// version: 1.0.0
// guid: 2e1f0d9c-8b7a-6e5f-4d3c-2b1a0f9e8d7c
//
// Response definitions for queue module
//
edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

/**
 * Response message for topic configuration update operations.
 */
message UpdateTopicConfigResponse {
  // Whether the update was successful
  bool success = 1;

  // Error message if update failed
  string error_message = 2;

  // The name of the topic that was updated
  string topic_name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Timestamp when the update was applied
  google.protobuf.Timestamp updated_at = 4;

  // Configuration revision number after update
  uint64 config_revision = 5;

  // List of configuration fields that were modified
  repeated string modified_fields = 6;

  // Validation warnings (non-fatal issues)
  repeated string warnings = 7;
}
```

---

### validation_config.proto {#validation_config}

**Path**: `gcommon/v1/queue/validation_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 24

**Messages** (1): `ValidationConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/validation_config.proto
// version: 1.0.0
// guid: 50a55c81-98ea-49a5-8d18-c188a48acc5f

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

// ValidationConfig defines rules for validating queued messages.
message ValidationConfig {
  // Whether to validate message schema.
  bool validate_schema = 1;
  // Maximum allowed size of the message body in bytes.
  int64 max_body_bytes = 2 [(buf.validate.field).int64.gte = 0];
  // If true, reject messages that exceed validation limits.
  bool reject_invalid = 3;
}
```

---

### vector_clock_config.proto {#vector_clock_config}

**Path**: `gcommon/v1/queue/vector_clock_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 25

**Messages** (1): `VectorClockConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/vector_clock_config.proto
// version: 1.0.0
// guid: 3374bcbe-3bf2-4e5f-b46a-03e4131fcd98

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message VectorClockConfig {
  // Enable vector clocks
  bool enabled = 1;

  // Clock precision (nanoseconds, microseconds, milliseconds)
  string precision = 2 [(buf.validate.field).string.min_len = 1];

  // Maximum clock drift tolerance (milliseconds)
  int64 max_drift_ms = 3 [(buf.validate.field).int64.gte = 0];
}
```

---

### write_retry_config.proto {#write_retry_config}

**Path**: `gcommon/v1/queue/write_retry_config.proto` **Package**: `gcommon.v1.queue` **Lines**: 31

**Messages** (1): `WriteRetryConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/write_retry_config.proto
// version: 1.0.0
// guid: c409f58a-7032-4fd2-b236-bd6bb3fc6f4c

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message WriteRetryConfig {
  // Maximum retry attempts
  int32 max_retries = 1 [(buf.validate.field).int32.gte = 0];

  // Initial retry delay (milliseconds)
  int32 initial_delay_ms = 2 [(buf.validate.field).int32.gte = 0];

  // Maximum retry delay (milliseconds)
  int32 max_delay_ms = 3 [(buf.validate.field).int32.gte = 0];

  // Backoff multiplier
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Retry idempotent operations only
  bool idempotent_only = 5;
}
```

---

### external_auth_service.proto {#external_auth_service}

**Path**: `gcommon/v1/queue/external_auth_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 36

**Messages** (1): `ExternalAuthService`

**Imports** (4):

- `gcommon/v1/queue/auth_cache_config.proto`
- `gcommon/v1/queue/retry_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/external_auth_service.proto
// version: 1.0.0
// guid: 888d52ef-a351-4fe1-a31e-6d7085e83b26

edition = "2023";

package gcommon.v1.queue;

import "gcommon/v1/queue/auth_cache_config.proto";
import "gcommon/v1/queue/retry_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message ExternalAuthService {
  // Enable external authorization
  bool enabled = 1;

  // Authorization service endpoint
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Request timeout (milliseconds)
  int32 timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Retry configuration - references existing RetryConfig
  QueueRetryConfig retry_config = 4;

  // Cache configuration
  AuthCacheConfig cache_config = 5;

  // Headers to include in authorization requests
  map<string, string> request_headers = 6;
}
```

---

### key_validation_service.proto {#key_validation_service}

**Path**: `gcommon/v1/queue/key_validation_service.proto` **Package**: `gcommon.v1.queue` **Lines**: 28

**Messages** (1): `KeyValidationService`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/queue/key_validation_service.proto
// version: 1.0.0
// guid: 796890cb-3593-41dc-bd46-52b840d476a4

edition = "2023";

package gcommon.v1.queue;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/queue";

message KeyValidationService {
  // Service type (local, external, etc.)
  string service_type = 1 [(buf.validate.field).string.min_len = 1];

  // Service endpoint (for external validation)
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];

  // Timeout for validation requests (milliseconds)
  int32 timeout_ms = 3 [(buf.validate.field).int32.gt = 0];

  // Cache TTL for validation results (seconds)
  int32 cache_ttl_seconds = 4 [(buf.validate.field).int32.gte = 0];
}
```

---

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
