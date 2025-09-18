# Common Messages Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 282
- **Messages**: 282

## Table of Contents

### Messages

- [`APIKey`](#api_key) - from api_key.proto
- [`APIKeyCredentials`](#api_key_credentials) - from api_key_credentials.proto
- [`ApiKeyStats`](#api_key_stats) - from api_key_stats.proto
- [`AppenderConfig`](#appender_config) - from appender_config.proto
- [`ArchiveCriteria`](#archive_criteria) - from archive_criteria.proto
- [`AssignRoleRequest`](#assign_role_request) - from assign_role_request.proto
- [`AssignRoleResponse`](#assign_role_response) - from assign_role_response.proto
- [`AuditEvent`](#audit_event) - from audit_event.proto
- [`AuthAuthConfig`](#auth_config) - from auth_config.proto
- [`AuthAuthenticateRequest`](#authenticate_request) - from authenticate_request.proto
- [`AuthAuthenticateResponse`](#authenticate_response) - from authenticate_response.proto
- [`AuthAuthorizeRequest`](#authorize_request) - from authorize_request.proto
- [`AuthAuthorizeResponse`](#authorize_response) - from authorize_response.proto
- [`AuthContext`](#auth_context) - from auth_context.proto
- [`AuthCreateSessionRequest`](#create_session_request) - from create_session_request.proto
- [`AuthCreateSessionResponse`](#create_session_response) - from create_session_response.proto
- [`AuthDeleteSessionRequest`](#delete_session_request) - from delete_session_request.proto
- [`AuthDeleteSessionResponse`](#delete_session_response) - from delete_session_response.proto
- [`AuthGetSessionRequest`](#get_session_request) - from get_session_request.proto
- [`AuthGetSessionResponse`](#get_session_response) - from get_session_response.proto
- [`AuthListSessionsRequest`](#list_sessions_request) - from list_sessions_request.proto
- [`AuthListSessionsResponse`](#list_sessions_response) - from list_sessions_response.proto
- [`AuthProvider`](#auth_provider) - from auth_provider.proto
- [`AuthRateLimitConfig`](#rate_limit_config) - from rate_limit_config.proto
- [`AuthSessionConfig`](#session_config) - from session_config.proto
- [`AuthToken`](#auth_token) - from auth_token.proto
- [`AuthUpdateSessionRequest`](#update_session_request) - from update_session_request.proto
- [`AuthUpdateSessionResponse`](#update_session_response) - from update_session_response.proto
- [`CachePolicy`](#cache_policy) - from cache_policy.proto
- [`ChangePasswordRequest`](#change_password_request) - from change_password_request.proto
- [`ChangePasswordResponse`](#change_password_response) - from change_password_response.proto
- [`CheckPermissionRequest`](#check_permission_request) - from check_permission_request.proto
- [`CheckPermissionResponse`](#check_permission_response) - from check_permission_response.proto
- [`CheckResult`](#check_result) - from check_result.proto
- [`Claims`](#claims) - from claims.proto
- [`ClientInfo`](#client_info) - from client_info.proto
- [`CommonAuditLog`](#audit_log) - from audit_log.proto
- [`CommonBatchOperation`](#batch_operation) - from batch_operation.proto
- [`CommonBatchOptions`](#batch_options) - from batch_options.proto
- [`CommonCircuitBreakerConfig`](#circuit_breaker_config) - from circuit_breaker_config.proto
- [`CommonPaginationInfo`](#pagination_info) - from pagination_info.proto
- [`CommonRetryPolicy`](#retry_policy) - from retry_policy.proto
- [`CommonSubscriptionInfo`](#subscription_info) - from subscription_info.proto
- [`CommonTimeRange`](#metrics_time_range) - from metrics_time_range.proto
- [`CompletePasswordResetRequest`](#complete_password_reset_request) - from complete_password_reset_request.proto
- [`CompletePasswordResetResponse`](#complete_password_reset_response) - from complete_password_reset_response.proto
- [`ComponentHealth`](#component_health) - from component_health.proto
- [`ConfigRetrySettings`](#config_retry_settings) - from config_retry_settings.proto
- [`ConfigValue`](#config_value) - from config_value.proto
- [`ConfigureAlertingRequest`](#configure_alerting_request) - from configure_alerting_request.proto
- [`ConfigureAlertingResponse`](#configure_alerting_response) - from configure_alerting_response.proto
- [`ConfigureLoggerRequest`](#configure_logger_request) - from configure_logger_request.proto
- [`ConfigureLoggerResponse`](#configure_logger_response) - from configure_logger_response.proto
- [`CreatePermissionRequest`](#create_permission_request) - from create_permission_request.proto
- [`CreateRoleRequest`](#create_role_request) - from create_role_request.proto
- [`CreateRoleResponse`](#create_role_response) - from create_role_response.proto
- [`CreateUserRequest`](#create_user_request) - from create_user_request.proto
- [`CreateUserResponse`](#create_user_response) - from create_user_response.proto
- [`DailyUsage`](#daily_usage) - from daily_usage.proto
- [`DebugInfo`](#debug_info) - from debug_info.proto
- [`DeleteNotificationRequest`](#delete_notification_request) - from delete_notification_request.proto
- [`DeleteNotificationResponse`](#delete_notification_response) - from delete_notification_response.proto
- [`DeletePermissionRequest`](#delete_permission_request) - from delete_permission_request.proto
- [`DeleteRoleRequest`](#delete_role_request) - from delete_role_request.proto
- [`DeleteRoleResponse`](#delete_role_response) - from delete_role_response.proto
- [`DeleteUserRequest`](#delete_user_request) - from delete_user_request.proto
- [`DeleteUserResponse`](#delete_user_response) - from delete_user_response.proto
- [`DeliveryChannel`](#delivery_channel) - from delivery_channel.proto
- [`DeviceInfo`](#device_info) - from device_info.proto
- [`Disable2FaRequest`](#disable2_fa_request) - from disable2_fa_request.proto
- [`DisableCheckRequest`](#disable_check_request) - from disable_check_request.proto
- [`DisableCheckResponse`](#disable_check_response) - from disable_check_response.proto
- [`DisableMfaRequest`](#disable_mfa_request) - from disable_mfa_request.proto
- [`DisableMfaResponse`](#disable_mfa_response) - from disable_mfa_response.proto
- [`EmailTemplate`](#email_template) - from email_template.proto
- [`Enable2FaRequest`](#enable2_fa_request) - from enable2_fa_request.proto
- [`EnableCheckRequest`](#enable_check_request) - from enable_check_request.proto
- [`EnableCheckResponse`](#enable_check_response) - from enable_check_response.proto
- [`EnableMfaRequest`](#enable_mfa_request) - from enable_mfa_request.proto
- [`EnableMfaResponse`](#enable_mfa_response) - from enable_mfa_response.proto
- [`Error`](#error) - from error.proto
- [`ErrorInfo`](#error_info) - from error_info.proto
- [`ErrorTypeCount`](#error_type_count) - from error_type_count.proto
- [`EventNotification`](#event_notification) - from event_notification.proto
- [`FilterOptions`](#filter_options) - from filter_options.proto
- [`FilterValue`](#filter_value) - from filter_value.proto
- [`GenerateAPIKeyRequest`](#generate_api_key_request) - from generate_api_key_request.proto
- [`GenerateAPIKeyResponse`](#generate_api_key_response) - from generate_api_key_response.proto
- [`GetApiKeyRequest`](#get_api_key_request) - from get_api_key_request.proto
- [`GetApiKeyResponse`](#get_api_key_response) - from get_api_key_response.proto
- [`GetAuthConfigRequest`](#get_auth_config_request) - from get_auth_config_request.proto
- [`GetCheckStatusRequest`](#get_check_status_request) - from get_check_status_request.proto
- [`GetHealthHistoryRequest`](#get_health_history_request) - from get_health_history_request.proto
- [`GetHealthMetricsRequest`](#get_health_metrics_request) - from get_health_metrics_request.proto
- [`GetHealthMetricsResponse`](#get_health_metrics_response) - from get_health_metrics_response.proto
- [`GetHealthRequest`](#get_health_request) - from get_health_request.proto
- [`GetPermissionRequest`](#get_permission_request) - from get_permission_request.proto
- [`GetPermissionResponse`](#get_permission_response) - from get_permission_response.proto
- [`GetPreferencesRequest`](#get_preferences_request) - from get_preferences_request.proto
- [`GetPreferencesResponse`](#get_preferences_response) - from get_preferences_response.proto
- [`GetRoleRequest`](#get_role_request) - from get_role_request.proto
- [`GetRoleResponse`](#get_role_response) - from get_role_response.proto
- [`GetServiceHealthRequest`](#get_service_health_request) - from get_service_health_request.proto
- [`GetServiceHealthResponse`](#get_service_health_response) - from get_service_health_response.proto
- [`GetSystemStatsRequest`](#get_system_stats_request) - from get_system_stats_request.proto
- [`GetSystemStatsResponse`](#get_system_stats_response) - from get_system_stats_response.proto
- [`GetTemplateRequest`](#get_template_request) - from get_template_request.proto
- [`GetTemplateResponse`](#get_template_response) - from get_template_response.proto
- [`GetUserInfoRequest`](#get_user_info_request) - from get_user_info_request.proto
- [`GetUserInfoResponse`](#get_user_info_response) - from get_user_info_response.proto
- [`GetUserPermissionsRequest`](#get_user_permissions_request) - from get_user_permissions_request.proto
- [`GetUserPermissionsResponse`](#get_user_permissions_response) - from get_user_permissions_response.proto
- [`GetUserRequest`](#get_user_request) - from get_user_request.proto
- [`GetUserResponse`](#get_user_response) - from get_user_response.proto
- [`GetUserRolesRequest`](#get_user_roles_request) - from get_user_roles_request.proto
- [`GetUserRolesResponse`](#get_user_roles_response) - from get_user_roles_response.proto
- [`GrantPermissionRequest`](#grant_permission_request) - from grant_permission_request.proto
- [`GrantPermissionResponse`](#grant_permission_response) - from grant_permission_response.proto
- [`Group`](#group) - from group.proto
- [`HealthCheckAllRequest`](#health_check_all_request) - from health_check_all_request.proto
- [`HealthCheckAllResponse`](#health_check_all_response) - from health_check_all_response.proto
- [`HealthConfig`](#health_config) - from health_config.proto
- [`HealthHealthCheckRequest`](#health_check_request) - from health_check_request.proto
- [`HealthHealthCheckResponse`](#health_check_response) - from health_check_response.proto
- [`HealthHealthCheckResult`](#health_check_result) - from health_check_result.proto
- [`HealthMetricData`](#health_metric_data) - from health_metric_data.proto
- [`HealthMetrics`](#health_metrics) - from health_metrics.proto
- [`HealthWatchRequest`](#watch_request) - from watch_request.proto
- [`InitiatePasswordResetRequest`](#initiate_password_reset_request) - from initiate_password_reset_request.proto
- [`InitiatePasswordResetResponse`](#initiate_password_reset_response) - from initiate_password_reset_response.proto
- [`Int64Array`](#int64_array) - from int64_array.proto
- [`InvalidateUserSessionsRequest`](#invalidate_user_sessions_request) - from invalidate_user_sessions_request.proto
- [`JWTConfig`](#jwt_config) - from jwt_config.proto
- [`JWTCredentials`](#jwt_credentials) - from jwt_credentials.proto
- [`KeyValue`](#key_value) - from key_value.proto
- [`LdapConfig`](#ldap_config) - from ldap_config.proto
- [`ListApiKeysRequest`](#list_api_keys_request) - from list_api_keys_request.proto
- [`ListApiKeysResponse`](#list_api_keys_response) - from list_api_keys_response.proto
- [`ListChecksRequest`](#list_checks_request) - from list_checks_request.proto
- [`ListNotificationsRequest`](#list_notifications_request) - from list_notifications_request.proto
- [`ListNotificationsResponse`](#list_notifications_response) - from list_notifications_response.proto
- [`ListPermissionsRequest`](#list_permissions_request) - from list_permissions_request.proto
- [`ListPermissionsResponse`](#list_permissions_response) - from list_permissions_response.proto
- [`ListRolesRequest`](#list_roles_request) - from list_roles_request.proto
- [`ListRolesResponse`](#list_roles_response) - from list_roles_response.proto
- [`ListServicesRequest`](#list_services_request) - from list_services_request.proto
- [`ListServicesResponse`](#list_services_response) - from list_services_response.proto
- [`ListUserSessionsRequest`](#list_user_sessions_request) - from list_user_sessions_request.proto
- [`ListUserSessionsResponse`](#list_user_sessions_response) - from list_user_sessions_response.proto
- [`ListUsersRequest`](#list_users_request) - from list_users_request.proto
- [`ListUsersResponse`](#list_users_response) - from list_users_response.proto
- [`LocationInfo`](#location_info) - from location_info.proto
- [`LogEntry`](#log_entry) - from log_entry.proto
- [`LogFormatterConfig`](#formatter_config) - from formatter_config.proto
- [`LogStatistics`](#log_statistics) - from log_statistics.proto
- [`LoggerConfig`](#logger_config) - from logger_config.proto
- [`LogoutRequest`](#logout_request) - from logout_request.proto
- [`LogoutResponse`](#logout_response) - from logout_response.proto
- [`MarkAsReadRequest`](#mark_as_read_request) - from mark_as_read_request.proto
- [`MarkAsReadResponse`](#mark_as_read_response) - from mark_as_read_response.proto
- [`MetricPoint`](#metric_point) - from metric_point.proto
- [`MetricsAPIKeyConfig`](#metrics_api_key_config) - from metrics_api_key_config.proto
- [`MetricsConfigChange`](#metrics_config_change) - from metrics_config_change.proto
- [`MetricsErrorStats`](#metrics_error_stats) - from metrics_error_stats.proto
- [`MetricsRetentionInfo`](#metrics_retention_info) - from metrics_retention_info.proto
- [`MetricsRetentionPolicyConfig`](#metrics_retention_policy_config) - from metrics_retention_policy_config.proto
- [`MetricsValidationResult`](#metrics_validation_result) - from metrics_validation_result.proto
- [`MfaConfig`](#mfa_config) - from mfa_config.proto
- [`MfaSetupInstruction`](#mfa_setup_instruction) - from mfa_setup_instruction.proto
- [`NotificationFrequency`](#notification_frequency) - from notification_frequency.proto
- [`NotificationMessage`](#notification_message) - from notification_message.proto
- [`OAuth2Config`](#o_auth2_config) - from o_auth2_config.proto
- [`OAuth2Credentials`](#o_auth2_credentials) - from o_auth2_credentials.proto
- [`OAuthClient`](#o_auth_client) - from o_auth_client.proto
- [`OrganizationAccessControl`](#organization_access_control) - from organization_access_control.proto
- [`OrganizationComplianceSettings`](#organization_compliance_settings) - from organization_compliance_settings.proto
- [`OrganizationNotificationSettings`](#organization_notification_settings) - from organization_notification_settings.proto
- [`OrganizationResourceLimits`](#organization_resource_limits) - from organization_resource_limits.proto
- [`OutputConfig`](#output_config) - from output_config.proto
- [`PaginatedResponse`](#paginated_response) - from paginated_response.proto
- [`Pagination`](#pagination) - from pagination.proto
- [`PaginationOptions`](#pagination_options) - from pagination_options.proto
- [`ParameterConstraints`](#parameter_constraints) - from parameter_constraints.proto
- [`PasswordCredentials`](#password_credentials) - from password_credentials.proto
- [`PasswordPolicy`](#password_policy) - from password_policy.proto
- [`Permission`](#permission) - from permission.proto
- [`PermissionCondition`](#permission_condition) - from permission_condition.proto
- [`PermissionGrant`](#permission_grant) - from permission_grant.proto
- [`PermissionMetadata`](#permission_metadata) - from permission_metadata.proto
- [`RateLimit`](#rate_limit) - from rate_limit.proto
- [`RateLimitInfo`](#rate_limit_info) - from rate_limit_info.proto
- [`ReadLogsRequest`](#read_logs_request) - from read_logs_request.proto
- [`ReadLogsResponse`](#read_logs_response) - from read_logs_response.proto
- [`RefreshToken`](#refresh_token) - from refresh_token.proto
- [`RefreshTokenRequest`](#refresh_token_request) - from refresh_token_request.proto
- [`RefreshTokenResponse`](#refresh_token_response) - from refresh_token_response.proto
- [`RegisterCheckRequest`](#register_check_request) - from register_check_request.proto
- [`RegisterCheckResponse`](#register_check_response) - from register_check_response.proto
- [`RegisterUserRequest`](#register_user_request) - from register_user_request.proto
- [`RegisterUserResponse`](#register_user_response) - from register_user_response.proto
- [`RemediationDetails`](#remediation_details) - from remediation_details.proto
- [`RemoveRoleRequest`](#remove_role_request) - from remove_role_request.proto
- [`RemoveRoleResponse`](#remove_role_response) - from remove_role_response.proto
- [`RequestMetadata`](#request_metadata) - from request_metadata.proto
- [`ResendVerificationRequest`](#resend_verification_request) - from resend_verification_request.proto
- [`ResetHealthStatsRequest`](#reset_health_stats_request) - from reset_health_stats_request.proto
- [`ResetHealthStatsResponse`](#reset_health_stats_response) - from reset_health_stats_response.proto
- [`ResetPasswordRequest`](#reset_password_request) - from reset_password_request.proto
- [`ResetPasswordResponse`](#reset_password_response) - from reset_password_response.proto
- [`ResourceReference`](#resource_reference) - from resource_reference.proto
- [`ResponseMetadata`](#response_metadata) - from response_metadata.proto
- [`RetentionPolicyInfo`](#retention_policy_info) - from retention_policy_info.proto
- [`RevokeApiKeyRequest`](#revoke_api_key_request) - from revoke_api_key_request.proto
- [`RevokeApiKeyResponse`](#revoke_api_key_response) - from revoke_api_key_response.proto
- [`RevokePermissionRequest`](#revoke_permission_request) - from revoke_permission_request.proto
- [`RevokePermissionResponse`](#revoke_permission_response) - from revoke_permission_response.proto
- [`RevokeRoleRequest`](#revoke_role_request) - from revoke_role_request.proto
- [`RevokeRoleResponse`](#revoke_role_response) - from revoke_role_response.proto
- [`RevokeTokenRequest`](#revoke_token_request) - from revoke_token_request.proto
- [`RevokeTokenResponse`](#revoke_token_response) - from revoke_token_response.proto
- [`Role`](#role) - from role.proto
- [`RoleAssignment`](#role_assignment) - from role_assignment.proto
- [`RoleMetadata`](#role_metadata) - from role_metadata.proto
- [`RunCheckRequest`](#run_check_request) - from run_check_request.proto
- [`RunCheckResponse`](#run_check_response) - from run_check_response.proto
- [`SamlConfig`](#saml_config) - from saml_config.proto
- [`SecurityContext`](#security_context) - from security_context.proto
- [`SecurityPolicy`](#security_policy) - from security_policy.proto
- [`SendNotificationRequest`](#send_notification_request) - from send_notification_request.proto
- [`SendNotificationResponse`](#send_notification_response) - from send_notification_response.proto
- [`SendVerificationEmailRequest`](#send_verification_email_request) - from send_verification_email_request.proto
- [`SendVerificationEmailResponse`](#send_verification_email_response) - from send_verification_email_response.proto
- [`ServiceVersion`](#service_version) - from service_version.proto
- [`Session`](#session) - from session.proto
- [`SessionInfo`](#session_info) - from session_info.proto
- [`SessionMetadata`](#session_metadata) - from session_metadata.proto
- [`SetHealthRequest`](#set_health_request) - from set_health_request.proto
- [`SetHealthResponse`](#set_health_response) - from set_health_response.proto
- [`SortOptions`](#sort_options) - from sort_options.proto
- [`SourceLocation`](#source_location) - from source_location.proto
- [`StringArray`](#string_array) - from string_array.proto
- [`SubscriptionOptions`](#subscription_options) - from subscription_options.proto
- [`SubscriptionPreferences`](#subscription_preferences) - from subscription_preferences.proto
- [`Template`](#template) - from template.proto
- [`TemplateParameter`](#template_parameter) - from template_parameter.proto
- [`TerminateSessionRequest`](#terminate_session_request) - from terminate_session_request.proto
- [`TerminateSessionResponse`](#terminate_session_response) - from terminate_session_response.proto
- [`TimeRangeMetrics`](#time_range_metrics) - from time_range_metrics.proto
- [`TimeRestriction`](#time_restriction) - from time_restriction.proto
- [`Token`](#token) - from token.proto
- [`TokenInfo`](#token_info) - from token_info.proto
- [`TokenMetadata`](#token_metadata) - from token_metadata.proto
- [`UnregisterCheckRequest`](#unregister_check_request) - from unregister_check_request.proto
- [`UnregisterCheckResponse`](#unregister_check_response) - from unregister_check_response.proto
- [`UpdatePermissionRequest`](#update_permission_request) - from update_permission_request.proto
- [`UpdatePreferencesRequest`](#update_preferences_request) - from update_preferences_request.proto
- [`UpdatePreferencesResponse`](#update_preferences_response) - from update_preferences_response.proto
- [`UpdateRoleRequest`](#update_role_request) - from update_role_request.proto
- [`UpdateRoleResponse`](#update_role_response) - from update_role_response.proto
- [`UpdateUserRequest`](#update_user_request) - from update_user_request.proto
- [`UpdateUserResponse`](#update_user_response) - from update_user_response.proto
- [`User`](#user) - from user.proto
- [`UserDetails`](#user_details) - from user_details.proto
- [`UserInfo`](#user_info) - from user_info.proto
- [`UserMetadata`](#user_metadata) - from user_metadata.proto
- [`UserPreferences`](#user_preferences) - from user_preferences.proto
- [`UserProfile`](#user_profile) - from user_profile.proto
- [`ValidateSessionRequest`](#validate_session_request) - from validate_session_request.proto
- [`ValidateSessionResponse`](#validate_session_response) - from validate_session_response.proto
- [`ValidateTokenRequest`](#validate_token_request) - from validate_token_request.proto
- [`ValidateTokenResponse`](#validate_token_response) - from validate_token_response.proto
- [`VerificationStatus`](#verification_status) - from verification_status.proto
- [`Verify2FaRequest`](#verify2_fa_request) - from verify2_fa_request.proto
- [`VerifyCredentialsRequest`](#verify_credentials_request) - from verify_credentials_request.proto
- [`VerifyCredentialsResponse`](#verify_credentials_response) - from verify_credentials_response.proto
- [`VerifyEmailRequest`](#verify_email_request) - from verify_email_request.proto
- [`VerifyEmailResponse`](#verify_email_response) - from verify_email_response.proto
- [`VerifyMfaRequest`](#verify_mfa_request) - from verify_mfa_request.proto
- [`VerifyMfaResponse`](#verify_mfa_response) - from verify_mfa_response.proto
- [`WatchResponse`](#watch_response) - from watch_response.proto
- [`WriteLogRequest`](#write_log_request) - from write_log_request.proto
- [`WriteLogResponse`](#write_log_response) - from write_log_response.proto

### Files in this Module

- [api_key.proto](#api_key)
- [api_key_credentials.proto](#api_key_credentials)
- [api_key_stats.proto](#api_key_stats)
- [archive_criteria.proto](#archive_criteria)
- [audit_log.proto](#audit_log)
- [auth_context.proto](#auth_context)
- [auth_provider.proto](#auth_provider)
- [auth_token.proto](#auth_token)
- [cache_policy.proto](#cache_policy)
- [check_result.proto](#check_result)
- [claims.proto](#claims)
- [client_info.proto](#client_info)
- [component_health.proto](#component_health)
- [daily_usage.proto](#daily_usage)
- [debug_info.proto](#debug_info)
- [delivery_channel.proto](#delivery_channel)
- [device_info.proto](#device_info)
- [email_template.proto](#email_template)
- [error.proto](#error)
- [error_info.proto](#error_info)
- [error_type_count.proto](#error_type_count)
- [filter_options.proto](#filter_options)
- [filter_value.proto](#filter_value)
- [group.proto](#group)
- [health_check_result.proto](#health_check_result)
- [health_metric_data.proto](#health_metric_data)
- [health_metrics.proto](#health_metrics)
- [int64_array.proto](#int64_array)
- [jwt_credentials.proto](#jwt_credentials)
- [key_value.proto](#key_value)
- [location_info.proto](#location_info)
- [log_entry.proto](#log_entry)
- [log_statistics.proto](#log_statistics)
- [metric_point.proto](#metric_point)
- [metrics_error_stats.proto](#metrics_error_stats)
- [metrics_retention_info.proto](#metrics_retention_info)
- [metrics_time_range.proto](#metrics_time_range)
- [metrics_validation_result.proto](#metrics_validation_result)
- [mfa_setup_instruction.proto](#mfa_setup_instruction)
- [notification_frequency.proto](#notification_frequency)
- [notification_message.proto](#notification_message)
- [o_auth2_credentials.proto](#o_auth2_credentials)
- [o_auth_client.proto](#o_auth_client)
- [organization_access_control.proto](#organization_access_control)
- [organization_compliance_settings.proto](#organization_compliance_settings)
- [organization_notification_settings.proto](#organization_notification_settings)
- [organization_resource_limits.proto](#organization_resource_limits)
- [pagination.proto](#pagination)
- [pagination_info.proto](#pagination_info)
- [pagination_options.proto](#pagination_options)
- [parameter_constraints.proto](#parameter_constraints)
- [password_credentials.proto](#password_credentials)
- [password_policy.proto](#password_policy)
- [permission.proto](#permission)
- [permission_condition.proto](#permission_condition)
- [permission_grant.proto](#permission_grant)
- [permission_metadata.proto](#permission_metadata)
- [rate_limit.proto](#rate_limit)
- [rate_limit_info.proto](#rate_limit_info)
- [refresh_token.proto](#refresh_token)
- [remediation_details.proto](#remediation_details)
- [request_metadata.proto](#request_metadata)
- [resource_reference.proto](#resource_reference)
- [response_metadata.proto](#response_metadata)
- [retention_policy_info.proto](#retention_policy_info)
- [retry_policy.proto](#retry_policy)
- [role.proto](#role)
- [role_assignment.proto](#role_assignment)
- [role_metadata.proto](#role_metadata)
- [security_context.proto](#security_context)
- [security_policy.proto](#security_policy)
- [session.proto](#session)
- [session_info.proto](#session_info)
- [session_metadata.proto](#session_metadata)
- [sort_options.proto](#sort_options)
- [source_location.proto](#source_location)
- [string_array.proto](#string_array)
- [subscription_info.proto](#subscription_info)
- [subscription_options.proto](#subscription_options)
- [subscription_preferences.proto](#subscription_preferences)
- [template.proto](#template)
- [template_parameter.proto](#template_parameter)
- [time_range_metrics.proto](#time_range_metrics)
- [time_restriction.proto](#time_restriction)
- [token.proto](#token)
- [token_info.proto](#token_info)
- [token_metadata.proto](#token_metadata)
- [user.proto](#user)
- [user_details.proto](#user_details)
- [user_info.proto](#user_info)
- [user_metadata.proto](#user_metadata)
- [user_preferences.proto](#user_preferences)
- [user_profile.proto](#user_profile)
- [verification_status.proto](#verification_status)
- [appender_config.proto](#appender_config)
- [auth_config.proto](#auth_config)
- [circuit_breaker_config.proto](#circuit_breaker_config)
- [config_retry_settings.proto](#config_retry_settings)
- [config_value.proto](#config_value)
- [configure_alerting_request.proto](#configure_alerting_request)
- [configure_alerting_response.proto](#configure_alerting_response)
- [configure_logger_request.proto](#configure_logger_request)
- [configure_logger_response.proto](#configure_logger_response)
- [formatter_config.proto](#formatter_config)
- [get_auth_config_request.proto](#get_auth_config_request)
- [health_config.proto](#health_config)
- [jwt_config.proto](#jwt_config)
- [ldap_config.proto](#ldap_config)
- [logger_config.proto](#logger_config)
- [metrics_api_key_config.proto](#metrics_api_key_config)
- [metrics_config_change.proto](#metrics_config_change)
- [metrics_retention_policy_config.proto](#metrics_retention_policy_config)
- [mfa_config.proto](#mfa_config)
- [o_auth2_config.proto](#o_auth2_config)
- [output_config.proto](#output_config)
- [rate_limit_config.proto](#rate_limit_config)
- [saml_config.proto](#saml_config)
- [session_config.proto](#session_config)
- [assign_role_request.proto](#assign_role_request)
- [assign_role_response.proto](#assign_role_response)
- [authenticate_request.proto](#authenticate_request)
- [authenticate_response.proto](#authenticate_response)
- [authorize_request.proto](#authorize_request)
- [authorize_response.proto](#authorize_response)
- [batch_operation.proto](#batch_operation)
- [batch_options.proto](#batch_options)
- [change_password_request.proto](#change_password_request)
- [change_password_response.proto](#change_password_response)
- [check_permission_request.proto](#check_permission_request)
- [check_permission_response.proto](#check_permission_response)
- [complete_password_reset_request.proto](#complete_password_reset_request)
- [complete_password_reset_response.proto](#complete_password_reset_response)
- [create_permission_request.proto](#create_permission_request)
- [create_role_request.proto](#create_role_request)
- [create_role_response.proto](#create_role_response)
- [create_session_request.proto](#create_session_request)
- [create_session_response.proto](#create_session_response)
- [create_user_request.proto](#create_user_request)
- [create_user_response.proto](#create_user_response)
- [delete_notification_request.proto](#delete_notification_request)
- [delete_notification_response.proto](#delete_notification_response)
- [delete_permission_request.proto](#delete_permission_request)
- [delete_role_request.proto](#delete_role_request)
- [delete_role_response.proto](#delete_role_response)
- [delete_session_request.proto](#delete_session_request)
- [delete_session_response.proto](#delete_session_response)
- [delete_user_request.proto](#delete_user_request)
- [delete_user_response.proto](#delete_user_response)
- [disable2_fa_request.proto](#disable2_fa_request)
- [disable_check_request.proto](#disable_check_request)
- [disable_check_response.proto](#disable_check_response)
- [disable_mfa_request.proto](#disable_mfa_request)
- [disable_mfa_response.proto](#disable_mfa_response)
- [enable2_fa_request.proto](#enable2_fa_request)
- [enable_check_request.proto](#enable_check_request)
- [enable_check_response.proto](#enable_check_response)
- [enable_mfa_request.proto](#enable_mfa_request)
- [enable_mfa_response.proto](#enable_mfa_response)
- [generate_api_key_request.proto](#generate_api_key_request)
- [generate_api_key_response.proto](#generate_api_key_response)
- [get_api_key_request.proto](#get_api_key_request)
- [get_api_key_response.proto](#get_api_key_response)
- [get_check_status_request.proto](#get_check_status_request)
- [get_health_history_request.proto](#get_health_history_request)
- [get_health_metrics_request.proto](#get_health_metrics_request)
- [get_health_metrics_response.proto](#get_health_metrics_response)
- [get_health_request.proto](#get_health_request)
- [get_permission_request.proto](#get_permission_request)
- [get_permission_response.proto](#get_permission_response)
- [get_preferences_request.proto](#get_preferences_request)
- [get_preferences_response.proto](#get_preferences_response)
- [get_role_request.proto](#get_role_request)
- [get_role_response.proto](#get_role_response)
- [get_session_request.proto](#get_session_request)
- [get_session_response.proto](#get_session_response)
- [get_system_stats_request.proto](#get_system_stats_request)
- [get_system_stats_response.proto](#get_system_stats_response)
- [get_template_request.proto](#get_template_request)
- [get_template_response.proto](#get_template_response)
- [get_user_info_request.proto](#get_user_info_request)
- [get_user_info_response.proto](#get_user_info_response)
- [get_user_permissions_request.proto](#get_user_permissions_request)
- [get_user_permissions_response.proto](#get_user_permissions_response)
- [get_user_request.proto](#get_user_request)
- [get_user_response.proto](#get_user_response)
- [get_user_roles_request.proto](#get_user_roles_request)
- [get_user_roles_response.proto](#get_user_roles_response)
- [grant_permission_request.proto](#grant_permission_request)
- [grant_permission_response.proto](#grant_permission_response)
- [health_check_all_request.proto](#health_check_all_request)
- [health_check_all_response.proto](#health_check_all_response)
- [health_check_request.proto](#health_check_request)
- [health_check_response.proto](#health_check_response)
- [initiate_password_reset_request.proto](#initiate_password_reset_request)
- [initiate_password_reset_response.proto](#initiate_password_reset_response)
- [invalidate_user_sessions_request.proto](#invalidate_user_sessions_request)
- [list_api_keys_request.proto](#list_api_keys_request)
- [list_api_keys_response.proto](#list_api_keys_response)
- [list_checks_request.proto](#list_checks_request)
- [list_notifications_request.proto](#list_notifications_request)
- [list_notifications_response.proto](#list_notifications_response)
- [list_permissions_request.proto](#list_permissions_request)
- [list_permissions_response.proto](#list_permissions_response)
- [list_roles_request.proto](#list_roles_request)
- [list_roles_response.proto](#list_roles_response)
- [list_sessions_request.proto](#list_sessions_request)
- [list_sessions_response.proto](#list_sessions_response)
- [list_user_sessions_request.proto](#list_user_sessions_request)
- [list_user_sessions_response.proto](#list_user_sessions_response)
- [list_users_request.proto](#list_users_request)
- [list_users_response.proto](#list_users_response)
- [logout_request.proto](#logout_request)
- [logout_response.proto](#logout_response)
- [mark_as_read_request.proto](#mark_as_read_request)
- [mark_as_read_response.proto](#mark_as_read_response)
- [paginated_response.proto](#paginated_response)
- [read_logs_request.proto](#read_logs_request)
- [read_logs_response.proto](#read_logs_response)
- [refresh_token_request.proto](#refresh_token_request)
- [refresh_token_response.proto](#refresh_token_response)
- [register_check_request.proto](#register_check_request)
- [register_check_response.proto](#register_check_response)
- [register_user_request.proto](#register_user_request)
- [register_user_response.proto](#register_user_response)
- [remove_role_request.proto](#remove_role_request)
- [remove_role_response.proto](#remove_role_response)
- [resend_verification_request.proto](#resend_verification_request)
- [reset_health_stats_request.proto](#reset_health_stats_request)
- [reset_health_stats_response.proto](#reset_health_stats_response)
- [reset_password_request.proto](#reset_password_request)
- [reset_password_response.proto](#reset_password_response)
- [revoke_api_key_request.proto](#revoke_api_key_request)
- [revoke_api_key_response.proto](#revoke_api_key_response)
- [revoke_permission_request.proto](#revoke_permission_request)
- [revoke_permission_response.proto](#revoke_permission_response)
- [revoke_role_request.proto](#revoke_role_request)
- [revoke_role_response.proto](#revoke_role_response)
- [revoke_token_request.proto](#revoke_token_request)
- [revoke_token_response.proto](#revoke_token_response)
- [run_check_request.proto](#run_check_request)
- [run_check_response.proto](#run_check_response)
- [send_notification_request.proto](#send_notification_request)
- [send_notification_response.proto](#send_notification_response)
- [send_verification_email_request.proto](#send_verification_email_request)
- [send_verification_email_response.proto](#send_verification_email_response)
- [set_health_request.proto](#set_health_request)
- [set_health_response.proto](#set_health_response)
- [terminate_session_request.proto](#terminate_session_request)
- [terminate_session_response.proto](#terminate_session_response)
- [unregister_check_request.proto](#unregister_check_request)
- [unregister_check_response.proto](#unregister_check_response)
- [update_permission_request.proto](#update_permission_request)
- [update_preferences_request.proto](#update_preferences_request)
- [update_preferences_response.proto](#update_preferences_response)
- [update_role_request.proto](#update_role_request)
- [update_role_response.proto](#update_role_response)
- [update_session_request.proto](#update_session_request)
- [update_session_response.proto](#update_session_response)
- [update_user_request.proto](#update_user_request)
- [update_user_response.proto](#update_user_response)
- [validate_session_request.proto](#validate_session_request)
- [validate_session_response.proto](#validate_session_response)
- [validate_token_request.proto](#validate_token_request)
- [validate_token_response.proto](#validate_token_response)
- [verify2_fa_request.proto](#verify2_fa_request)
- [verify_credentials_request.proto](#verify_credentials_request)
- [verify_credentials_response.proto](#verify_credentials_response)
- [verify_email_request.proto](#verify_email_request)
- [verify_email_response.proto](#verify_email_response)
- [verify_mfa_request.proto](#verify_mfa_request)
- [verify_mfa_response.proto](#verify_mfa_response)
- [watch_request.proto](#watch_request)
- [watch_response.proto](#watch_response)
- [write_log_request.proto](#write_log_request)
- [write_log_response.proto](#write_log_response)
- [audit_event.proto](#audit_event)
- [event_notification.proto](#event_notification)
- [get_service_health_request.proto](#get_service_health_request)
- [get_service_health_response.proto](#get_service_health_response)
- [list_services_request.proto](#list_services_request)
- [list_services_response.proto](#list_services_response)
- [service_version.proto](#service_version)

---

## Messages Documentation

### api_key.proto {#api_key}

**Path**: `gcommon/v1/common/api_key.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `APIKey`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/api_key.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-789a-b0c1-d2e3f4a5b6c7

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto"; // Added for field validation rules

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * APIKey represents a user-issued API key used for authenticating
 * programmatic access. The key value itself should be stored securely
 * and only the hashed form transmitted.
 */
message APIKey {
  // Unique identifier for the API key (UUID required)
  string id = 1 [
    (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    (buf.validate.field).required = true
  ];

  // ID of the user this key belongs to (UUID required)
  string user_id = 2 [
    (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    (buf.validate.field).required = true
  ];

  // Human readable description for the key (limit length)
  string description = 3 [(buf.validate.field).string.max_len = 500];

  // Hash of the API key value (non-empty)
  string key_hash = 4 [(buf.validate.field).string.min_len = 1];

  // Creation timestamp (must be present)
  google.protobuf.Timestamp created_at = 5 [lazy = true, (buf.validate.field).required = true];

  // Optional expiration timestamp
  google.protobuf.Timestamp expires_at = 6 [lazy = true];

  // Whether the key is currently active
  bool active = 7;
}

```

---

### api_key_credentials.proto {#api_key_credentials}

**Path**: `gcommon/v1/common/api_key_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `APIKeyCredentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/api_key_credentials.proto
// version: 1.0.0
// guid: 3a18b7a0-491c-4ddb-a97e-81168333896d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * API key credentials for programmatic authentication.
 * Supports both simple API key and key-pair authentication schemes.
 */
message APIKeyCredentials {
  // API key value used for authentication
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional API key ID for key-pair authentication schemes
  // Used when the API key is associated with a specific key identifier
  string key_id = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### api_key_stats.proto {#api_key_stats}

**Path**: `gcommon/v1/common/api_key_stats.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `ApiKeyStats`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/api_key_stats.proto
// version: 1.0.0
// guid: 118f177f-69fa-465e-9cc9-88c6aa87643f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

// TODO FIX THIS
//

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ApiKeyStats {
  int32 total_requests = 1 [(buf.validate.field).int32.gte = 0];
  int32 successful_requests = 2 [(buf.validate.field).int32.gte = 0];
  int32 failed_requests = 3 [(buf.validate.field).int32.gte = 0];
  int64 last_used_at = 4 [(buf.validate.field).int64.gte = 0];
  // TODO FIX THIS
  // repeated DailyUsage daily_usage = 5;
}
```

---

### archive_criteria.proto {#archive_criteria}

**Path**: `gcommon/v1/common/archive_criteria.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `ArchiveCriteria`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/archive_criteria.proto
// version: 1.0.0
// guid: b7d23f2c-0017-462f-a6d2-51ca4405bc2c

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ArchiveCriteria defines rules for selecting log files to archive
message ArchiveCriteria {
  // Only archive logs older than this duration
  google.protobuf.Duration older_than = 1;

  // Minimum size threshold in bytes
  int64 size_threshold_bytes = 2 [(buf.validate.field).int64.gte = 0];
}
```

---

### audit_log.proto {#audit_log}

**Path**: `gcommon/v1/common/audit_log.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Messages** (1): `CommonAuditLog`

**Imports** (5):

- `gcommon/v1/common/audit_result.proto`
- `gcommon/v1/common/resource_reference.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/audit_log.proto
// version: 1.0.0
// guid: 95446d3f-aa5e-4be7-a7bb-5b0b0b1cf19b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/audit_result.proto";
import "gcommon/v1/common/resource_reference.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Audit log entry for tracking operations and security events.
 * Provides comprehensive audit trail with user identification,
 * action details, and contextual metadata for compliance and debugging.
 */
message CommonAuditLog {
  // Unique audit log entry identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User identifier who performed the action
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Action or operation that was performed
  string action = 3;

  // Resource that was acted upon
  ResourceReference resource = 4;

  // Timestamp when the action occurred
  google.protobuf.Timestamp timestamp = 5;

  // Source IP address of the request
  string source_ip = 6;

  // User agent string from the client
  string user_agent = 7;

  // Additional contextual metadata about the action
  map<string, string> metadata = 8;

  // Result of the action (success, failure, partial)
  AuditResult result = 9;

  // Session identifier if applicable
  string session_id = 10;
}
```

---

### auth_context.proto {#auth_context}

**Path**: `gcommon/v1/common/auth_context.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `AuthContext`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_context.proto
// version: 1.0.0
// guid: 70848c6a-eeb6-46ee-b108-9159435b2475

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthContext carries user identity and authorization details
 * generated during authentication.
 */
message AuthContext {
  // ID of the authenticated user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Roles assigned to the user
  repeated string roles = 2;

  // Permissions granted to the user
  repeated string permissions = 3;

  // When this context was generated
  google.protobuf.Timestamp issued_at = 4 [lazy = true];

  // Arbitrary metadata passed between services
  map<string, string> metadata = 5;
}
```

---

### auth_provider.proto {#auth_provider}

**Path**: `gcommon/v1/common/auth_provider.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `AuthProvider`

**Imports** (3):

- `gcommon/v1/common/provider_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_provider.proto
// version: 1.0.0
// guid: 7293f6cc-7049-493d-9e7c-b17f00dd8a76

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/provider_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthProvider represents an external authentication provider configuration.
 * It defines the provider type and connection details used for authentication.
 */
message AuthProvider {
  // Unique provider identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human readable provider name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Provider type (e.g., LDAP, OAUTH2, SAML)
  gcommon.v1.common.AuthProviderType type = 3;

  // Provider-specific configuration reference or JSON blob
  string config = 4;
}
```

---

### auth_token.proto {#auth_token}

**Path**: `gcommon/v1/common/auth_token.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `AuthToken`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_token.proto
// version: 1.0.0
// guid: 61671511-e4c8-4e25-a0a6-5f82f7e45002

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Combined authentication token pair containing access and refresh tokens.
 */
message AuthToken {
  // Access token used for authenticated requests.
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // Refresh token used to obtain new access tokens.
  string refresh_token = 2 [(buf.validate.field).string.min_len = 1];

  // Expiration time of the access token.
  google.protobuf.Timestamp expires_at = 3 [lazy = true];

  // Optional metadata associated with the token pair.
  map<string, string> metadata = 4 [lazy = true];
}
```

---

### cache_policy.proto {#cache_policy}

**Path**: `gcommon/v1/common/cache_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `CachePolicy`

**Imports** (5):

- `gcommon/v1/common/eviction_policy.proto`
- `gcommon/v1/common/expiration_policy.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/cache_policy.proto
// version: 1.0.0
// guid: c37fc88f-0b7c-4fa4-9c60-23736d2bed76
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/eviction_policy.proto";
import "gcommon/v1/common/expiration_policy.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Cache policy configuration for cache behavior and performance tuning.
 * Defines expiration, eviction, sizing, and operational policies
 * for consistent cache management across GCommon modules.
 */
message CachePolicy {
  // Cache expiration policy strategy
  gcommon.v1.common.ExpirationPolicy expiration = 1;

  // Eviction policy when cache reaches capacity
  gcommon.v1.common.EvictionPolicy eviction = 2;

  // Maximum cache size in bytes (0 for unlimited)
  int64 max_size_bytes = 3 [(buf.validate.field).int64.gte = 0];

  // Maximum number of cache entries (0 for unlimited)
  int64 max_entries = 4 [(buf.validate.field).int64.gte = 0];

  // Default time-to-live for cache entries
  google.protobuf.Duration default_ttl = 5;

  // Whether to refresh entries before they expire
  bool refresh_ahead = 6;

  // Whether to collect and expose cache statistics
  bool enable_stats = 7;
}
```

---

### check_result.proto {#check_result}

**Path**: `gcommon/v1/common/check_result.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Messages** (1): `CheckResult`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_result.proto
// version: 1.0.0
// guid: 0e8f3ad4-be75-42b2-b880-fda7ebd7de1c
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Individual health check result for a specific component or subsystem.
 * Provides detailed information about the health status of a single check.
 */
message CheckResult {
  // Check name or identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Health status of this specific check
  // Overall status of the health check
  gcommon.v1.common.CommonHealthStatus status = 2;

  // Check execution timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Time taken to execute this check
  google.protobuf.Duration execution_time = 4;

  // Human-readable message about the check result
  string message = 5;

  // Error details if the check failed
  gcommon.v1.common.Error error = 6;

  // Additional metadata for this check
  map<string, string> metadata = 7;
}
```

---

### claims.proto {#claims}

**Path**: `gcommon/v1/common/claims.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Messages** (1): `Claims`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/claims.proto
// version: 1.0.0
// guid: 47901ef8-6b22-4b73-8bba-9c53ccaa46c8
// file: proto/gcommon/v1/common/claims.proto
//
// Type definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Claims {
  // Standard JWT claims
  string issuer = 1; // iss
  string subject = 2; // sub
  repeated string audience = 3; // aud
  int64 expires_at = 4; // exp
  int64 not_before = 5; // nbf
  int64 issued_at = 6; // iat
  string jwt_id = 7; // jti

  // Custom claims
  string user_id = 8 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
  string username = 9;
  string email = 10 [ (buf.validate.field).string.email = true ];
  bool email_verified = 11;
  repeated string roles = 12;
  repeated string permissions = 13;
  repeated string scopes = 14;

  // MFA claims
  bool mfa_verified = 15;
  string mfa_method = 16;

  // Session claims
  string session_id = 17;
  bool is_refresh_token = 18;

  // Additional metadata
  map<string, string> metadata = 19;
}
```

---

### client_info.proto {#client_info}

**Path**: `gcommon/v1/common/client_info.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `ClientInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/client_info.proto
// version: 1.0.0
// guid: d1b1396a-9610-4eb4-b5ea-bc7218024dee
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Client information for request identification and monitoring.
 * Provides standardized client metadata for logging, analytics,
 * and security purposes across all GCommon modules.
 */
message ClientInfo {
  // Client application name (e.g., "mobile-app", "web-frontend")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Client version using semantic versioning (e.g., "1.2.3")
  string version = 2;

  // Client IP address (IPv4 or IPv6)
  string ip_address = 3;

  // User agent string for web clients or application identifier
  string user_agent = 4;

  // Platform information (e.g., "iOS 15.0", "Chrome 95", "Go 1.19")
  string platform = 5;
}
```

---

### component_health.proto {#component_health}

**Path**: `gcommon/v1/common/component_health.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `ComponentHealth`

**Imports** (3):

- `gcommon/v1/common/serving_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/component_health.proto
// version: 1.0.0
// guid: 1eb070ba-060f-44c9-97ad-8a3d68800129

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/serving_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ComponentHealth {
  // Component name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];
  // Component status
  gcommon.v1.common.ServingStatus status = 2;
  // Component-specific message
  string message = 3;
  // Component check duration in milliseconds
  int64 duration_ms = 4;
}
```

---

### daily_usage.proto {#daily_usage}

**Path**: `gcommon/v1/common/daily_usage.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Messages** (1): `DailyUsage`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/daily_usage.proto
// version: 1.0.0
// guid: d5da361d-f967-4f15-9afa-951271665ecb

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DailyUsage {
  string date = 1; // YYYY-MM-DD format
  int32 request_count = 2 [(buf.validate.field).int32.gte = 0];
}
```

---

### debug_info.proto {#debug_info}

**Path**: `gcommon/v1/common/debug_info.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `DebugInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/debug_info.proto
// version: 1.0.0
// guid: 5cfc62b5-b458-4d97-bf91-b5a1c3eccadf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * DebugInfo provides supplemental debugging information
 * that can be included in request or response messages.
 * It captures contextual details useful for tracing and
 * troubleshooting complex issues.
 */
message DebugInfo {
  // Service or component name emitting this debug info
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Optional method or operation identifier
  string method = 2 [(buf.validate.field).string.min_len = 1];

  // Time when this debug info was generated
  google.protobuf.Timestamp timestamp = 3;

  // Arbitrary key/value details for debugging
  map<string, string> details = 4;

  // Additional tags to categorize or filter debug entries
  repeated string tags = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### delivery_channel.proto {#delivery_channel}

**Path**: `gcommon/v1/common/delivery_channel.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeliveryChannel`

**Imports** (3):

- `gcommon/v1/common/delivery_channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delivery_channel.proto
// version: 1.1.0
// guid: 5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Delivery channel specifying how a notification is sent.
 */
message DeliveryChannel {
  // Channel type such as email or SMS
  gcommon.v1.common.DeliveryChannelType type = 1;

  // Destination address (email, phone number, webhook URL, etc.)
  string target = 2 [(buf.validate.field).string.min_len = 1];

  // Optional channel specific configuration
  map<string, string> config = 3 [lazy = true];
}
```

---

### device_info.proto {#device_info}

**Path**: `gcommon/v1/common/device_info.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `DeviceInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/device_info.proto
// version: 1.0.0
// guid: 3c9b9c62-c45a-4919-bbf2-88ae536fc5e6

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeviceInfo {
  string device_id = 1 [(buf.validate.field).string.min_len = 1];
  string device_type = 2; // mobile, desktop, tablet
  string os = 3 [(buf.validate.field).string.min_len = 1];
  string browser = 4 [(buf.validate.field).string.min_len = 1];
  bool is_trusted = 5;
}
```

---

### email_template.proto {#email_template}

**Path**: `gcommon/v1/common/email_template.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `EmailTemplate`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/email_template.proto
// version: 1.0.0
// guid: 03debb46-12b4-4099-9c8f-99523c435029

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EmailTemplate {
  // Template name/type (e.g., "welcome", "password_reset")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Email subject template
  string subject = 2;

  // Email body template (HTML)
  string body_html = 3;

  // Email body template (plain text)
  string body_text = 4;
}
```

---

### error.proto {#error}

**Path**: `gcommon/v1/common/error.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `Error`

**Imports** (4):

- `gcommon/v1/common/error_code.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error.proto
// version: 1.0.0
// guid: 6998154e-e6c6-4156-b1d8-3633dc509d8a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_code.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common error message structure for standardized error handling.
 * Provides comprehensive error information including code, message,
 * debugging details, and traceability across all GCommon modules.
 */
message Error {
  // Standardized error code for programmatic handling
  gcommon.v1.common.ErrorCode code = 1;

  // Human-readable error message describing what went wrong
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Additional error details for debugging and troubleshooting
  map<string, string> details = 3;

  // Distributed trace ID for request correlation across services
  string trace_id = 4 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the error occurred
  google.protobuf.Timestamp timestamp = 5;

  // Source module or component that generated the error
  string source = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### error_info.proto {#error_info}

**Path**: `gcommon/v1/common/error_info.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `ErrorInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error_info.proto
// version: 1.0.0
// guid: ba36f77a-0141-43fc-a77e-fde479168a40

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// ErrorInfo provides structured error details for log entries
message ErrorInfo {
  // Error message
  string message = 1 [(buf.validate.field).string.min_len = 1];

  // Error type or class name
  string type = 2 [(buf.validate.field).string.min_len = 1];

  // Full stack trace if available
  string stack_trace = 3 [(buf.validate.field).string.min_len = 1];

  // Application-specific error code
  string code = 4 [(buf.validate.field).string.min_len = 1];

  // Arbitrary key/value context information
  map<string, string> context = 5;

  // Nested causes for error propagation
  repeated ErrorInfo causes = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### error_type_count.proto {#error_type_count}

**Path**: `gcommon/v1/common/error_type_count.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `ErrorTypeCount`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/error_type_count.proto
// version: 1.0.0
// guid: 8116a2bc-950e-407c-9db8-2f3985e9394d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ErrorTypeCount {
  string error_type = 1 [(buf.validate.field).string.min_len = 1];
  int64 count = 2 [(buf.validate.field).int64.gte = 0];
  double percentage = 3 [(buf.validate.field).double.gte = 0.0, (buf.validate.field).double.lte = 100.0];
}
```

---

### filter_options.proto {#filter_options}

**Path**: `gcommon/v1/common/filter_options.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `FilterOptions`

**Imports** (4):

- `gcommon/v1/common/filter_value.proto`
- `gcommon/v1/common/metrics_time_range.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_options.proto
// version: 1.0.0
// guid: 1c91c5f0-6774-405a-bb94-4a646e1e859d
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/filter_value.proto";
import "gcommon/v1/common/metrics_time_range.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common filtering options for search and query operations.
 * Provides a unified interface for filtering data across all GCommon modules.
 *
 * Supports field-based filters, text search, and time range filtering,
 * enabling flexible and powerful query capabilities.
 */
message FilterOptions {
  // Field-based filters with typed values and operations
  map<string, FilterValue> filters = 1;

  // Full-text search query for text-based filtering
  string search_query = 2 [(buf.validate.field).string.min_len = 1];

  // Time range filter for temporal data
  CommonTimeRange time_range = 3;
}
```

---

### filter_value.proto {#filter_value}

**Path**: `gcommon/v1/common/filter_value.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `FilterValue`

**Imports** (5):

- `gcommon/v1/common/filter_operation.proto`
- `gcommon/v1/common/int64_array.proto`
- `gcommon/v1/common/string_array.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/filter_value.proto
// version: 1.0.0
// guid: e873017a-bb7e-4509-bb4b-ba7a2d08bb2b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/filter_operation.proto";
import "gcommon/v1/common/int64_array.proto";
import "gcommon/v1/common/string_array.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Filter value with multiple type support and operation specification.
 * Enables type-safe filtering with various data types and comparison operations.
 *
 * Supports scalar values (string, int, double, bool) and array values
 * for IN/NOT_IN operations, with explicit operation specification.
 */
message FilterValue {
  // The value to filter by (one of the supported types)
  oneof value {
    // String value for text-based filtering
    string string_value = 1 [(buf.validate.field).string.min_len = 1];

    // Integer value for numeric filtering
    int64 int_value = 2 [(buf.validate.field).int64.gte = 0];

    // Double value for floating-point filtering
    double double_value = 3 [(buf.validate.field).double.gte = 0.0];

    // Boolean value for true/false filtering
    bool bool_value = 4;

    // Array of strings for multi-value filtering
    gcommon.v1.common.StringArray string_array = 5 [lazy = true];

    // Array of integers for multi-value filtering
    gcommon.v1.common.Int64Array int_array = 6 [lazy = true];
  }

  // Filter operation type (equals, contains, greater than, etc.)
  gcommon.v1.common.FilterOperation operation = 7;
}
```

---

### group.proto {#group}

**Path**: `gcommon/v1/common/group.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Messages** (1): `Group`

**Imports** (4):

- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/group.proto
// version: 1.0.0
// guid: 3d1addaa-66d2-4768-9214-6f57d3dea222
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Group entity for organizing users into collections.
 * Used for bulk permission management and organizational structure.
 * Supports hierarchical group relationships.
 */
message Group {
  // Unique group identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Group name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Group description
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Parent group ID (for hierarchical groups)
  string parent_group_id = 4;

  // Group permissions
  repeated string permissions = 5;

  // Group metadata for extensibility
  map<string, string> metadata = 6 [lazy = true];

  // Group creation timestamp
  google.protobuf.Timestamp created_at = 7 [lazy = true, (buf.validate.field).required = true];

  // Group status
  gcommon.v1.common.ResourceStatus status = 8;

  // Group member count
  int32 member_count = 9;

  // Group administrator user IDs
  repeated string admin_user_ids = 10;
}
```

---

### health_check_result.proto {#health_check_result}

**Path**: `gcommon/v1/common/health_check_result.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `HealthHealthCheckResult`

**Imports** (5):

- `gcommon/v1/common/check_type.proto`
- `gcommon/v1/common/component_health.proto`
- `gcommon/v1/common/serving_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_result.proto
// version: 1.0.0
// guid: f29a3085-ffb9-4d33-8e60-ee52f8ff4570

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_type.proto";
import "gcommon/v1/common/component_health.proto";
import "gcommon/v1/common/serving_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message HealthHealthCheckResult {
  // Service name being checked
  string service = 1 [(buf.validate.field).string.min_len = 1];
  // Overall status of the health check
  ServingStatus status = 2;
  // Type of health check performed
  CheckType check_type = 3;
  // Timestamp when the check was performed
  int64 timestamp = 4;
  // Duration of the check in milliseconds
  int64 duration_ms = 5 [(buf.validate.field).int64.gt = 0];
  // Human-readable message about the check result
  string message = 6 [(buf.validate.field).string.min_len = 1];
  // Error details if the check failed
  string error = 7 [(buf.validate.field).string.min_len = 1];
  // Additional metadata about the check
  map<string, string> metadata = 8;
  // Component-specific health details
  repeated ComponentHealth components = 9 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### health_metric_data.proto {#health_metric_data}

**Path**: `gcommon/v1/common/health_metric_data.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `HealthMetricData`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_metric_data.proto
// version: 1.0.0
// guid: 2d079e14-0602-4a9a-9b6b-dc8bbf629fe8
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Individual health metric data point.
 * Represents a single metric measurement with associated metadata.
 */
message HealthMetricData {
  // Metric name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Metric value
  double value = 2;

  // Timestamp of the metric
  google.protobuf.Timestamp timestamp = 3;

  // Labels for the metric
  map<string, string> labels = 4;

  // Unit of measurement (e.g., "ms", "count", "percentage")
  string unit = 5;

  // Description of what this metric measures
  string description = 6 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### health_metrics.proto {#health_metrics}

**Path**: `gcommon/v1/common/health_metrics.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `HealthMetrics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_metrics.proto
// version: 1.0.0
// guid: 5abc1dde-0895-4d4d-b970-d9784a116f26
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Health metrics aggregation containing overall system health statistics.
 * Provides quantitative data about health check performance and system status.
 */
message HealthMetrics {
  // Total number of health checks
  int32 total_checks = 1 [(buf.validate.field).int32.gte = 0];

  // Number of healthy checks
  int32 healthy_checks = 2 [(buf.validate.field).int32.gte = 0];

  // Number of unhealthy checks
  int32 unhealthy_checks = 3 [(buf.validate.field).int32.gte = 0];

  // Number of unknown status checks
  int32 unknown_checks = 4 [(buf.validate.field).int32.gte = 0];

  // Average response time across all checks
  double average_response_time_ms = 5 [(buf.validate.field).double.gte = 0.0];

  // Last update timestamp
  google.protobuf.Timestamp last_updated = 6;

  // System uptime
  double uptime_seconds = 7 [(buf.validate.field).double.gte = 0.0];

  // Additional custom metrics
  map<string, double> custom_metrics = 8;
}
```

---

### int64_array.proto {#int64_array}

**Path**: `gcommon/v1/common/int64_array.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `Int64Array`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/int64_array.proto
// version: 1.0.0
// guid: 319f8be8-1a6c-4543-b1fe-14beb5e83c0c
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Int64 array wrapper for oneof usage in filter values and other contexts.
 * Required because oneof fields cannot directly contain repeated types,
 * so arrays must be wrapped in a message.
 */
message Int64Array {
  // Array of 64-bit signed integer values
  repeated int64 values = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### jwt_credentials.proto {#jwt_credentials}

**Path**: `gcommon/v1/common/jwt_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `JWTCredentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/jwt_credentials.proto
// version: 1.0.0
// guid: f1c445cd-2b3d-49ec-bc9e-80e3ed12e215
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * JWT (JSON Web Token) credentials for token-based authentication.
 * Supports validation of externally issued JWTs with optional issuer verification.
 */
message JWTCredentials {
  // JWT token string (header.payload.signature format)
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Expected issuer for JWT validation (optional)
  // When provided, the JWT's 'iss' claim must match this value
  string issuer = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### key_value.proto {#key_value}

**Path**: `gcommon/v1/common/key_value.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `KeyValue`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/key_value.proto
// version: 1.0.0
// guid: 947f80d9-fca1-447c-aa5e-4f8b18e65816
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Generic key-value pair for metadata and configuration storage.
 * Provides a simple, reusable structure for storing arbitrary
 * string-based key-value data across all GCommon modules.
 */
message KeyValue {
  // The key identifier for this pair
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // The value associated with the key
  string value = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### location_info.proto {#location_info}

**Path**: `gcommon/v1/common/location_info.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `LocationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/location_info.proto
// version: 1.0.0
// guid: 9baeac22-b20b-45fb-89cf-b857c53282d8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message LocationInfo {
  string country = 1 [(buf.validate.field).string.min_len = 1];
  string region = 2 [(buf.validate.field).string.min_len = 1];
  string city = 3 [(buf.validate.field).string.min_len = 1];
  double latitude = 4 [(buf.validate.field).double.gte = 0.0];
  double longitude = 5 [(buf.validate.field).double.gte = 0.0];
}
```

---

### log_entry.proto {#log_entry}

**Path**: `gcommon/v1/common/log_entry.proto` **Package**: `gcommon.v1.common` **Lines**: 63

**Messages** (1): `LogEntry`

**Imports** (7):

- `gcommon/v1/common/error_info.proto`
- `gcommon/v1/common/log_level.proto`
- `gcommon/v1/common/source_location.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_entry.proto
// version: 1.0.0
// guid: 86cfa864-b9da-428c-9ca9-78f614600049

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_info.proto";
import "gcommon/v1/common/log_level.proto";
import "gcommon/v1/common/source_location.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogEntry represents a single structured log event
message LogEntry {
  // Log level
  LogLevel level = 1;

  // Log message
  string message = 2;

  // Timestamp of the log event
  google.protobuf.Timestamp timestamp = 3;

  // Logger name
  string logger = 4;

  // Thread or goroutine identifier
  string thread = 5;

  // Source code location
  SourceLocation source = 6;

  // Structured fields for context
  map<string, google.protobuf.Any> fields = 7;

  // Tags for categorization
  repeated string tags = 8;

  // Trace ID for distributed tracing
  string trace_id = 9;

  // Span ID for distributed tracing
  string span_id = 10;

  // User ID associated with the log
  string user_id = 11 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request ID for correlation
  string request_id = 12;

  // Detailed error information
  ErrorInfo error_info = 13;
}
```

---

### log_statistics.proto {#log_statistics}

**Path**: `gcommon/v1/common/log_statistics.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `LogStatistics`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/log_statistics.proto
// version: 1.0.0
// guid: 98acfd30-4a7f-43f6-ac8d-f10a598a805a

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogStatistics provides aggregated metrics about log entries
message LogStatistics {
  // Total log entries
  int64 total_entries = 1 [(buf.validate.field).int64.gte = 0];

  // Entries per second
  double entries_per_second = 2 [(buf.validate.field).double.gte = 0.0];

  // Average entry size
  int64 average_size = 3 [(buf.validate.field).int64.gte = 0];

  // Total size of all log entries
  int64 total_size = 4 [(buf.validate.field).int64.gte = 0];

  // Count of log entries with level ERROR
  int64 error_count = 5 [(buf.validate.field).int64.gte = 0];

  // Count of log entries with level WARNING
  int64 warning_count = 6 [(buf.validate.field).int64.gte = 0];
}
```

---

### metric_point.proto {#metric_point}

**Path**: `gcommon/v1/common/metric_point.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `MetricPoint`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/metric_point.proto
// version: 1.0.0
// guid: 33062748-1b9e-47b6-9fbe-be60f9f3fb7d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common metrics data point for standardized metric collection.
 * Provides a unified structure for metrics across all GCommon modules
 * with timestamp, labels, and unit information for observability.
 */
message MetricPoint {
  // Metric name identifier (e.g., "request_count", "response_time")
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Numeric value of the metric
  double value = 2;

  // Timestamp when the metric was recorded
  google.protobuf.Timestamp timestamp = 3;

  // Key-value labels for metric dimensions and filtering
  map<string, string> labels = 4;

  // Unit of measurement (e.g., "seconds", "bytes", "requests")
  string unit = 5;
}
```

---

### metrics_error_stats.proto {#metrics_error_stats}

**Path**: `gcommon/v1/common/metrics_error_stats.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `MetricsErrorStats`

**Imports** (3):

- `gcommon/v1/common/error_type_count.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/error_stats.proto
// version: 1.1.0
// guid: ba56b09c-77ad-41e9-80ae-0a95c96c8394

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_type_count.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MetricsErrorStats {
  // Total number of errors
  int64 total_errors = 1 [(buf.validate.field).int64.gte = 0];

  // Error rate (errors per total operations)
  double error_rate = 2 [(buf.validate.field).double.gte = 0.0];

  // Most common error types
  repeated ErrorTypeCount error_types = 3 [(buf.validate.field).repeated.min_items = 1];

  // Recent error trend (increasing/decreasing/stable)
  string error_trend = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### metrics_retention_info.proto {#metrics_retention_info}

**Path**: `gcommon/v1/common/metrics_retention_info.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `MetricsRetentionInfo`

**Imports** (3):

- `gcommon/v1/common/metrics_retention_policy_config.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_info.proto
// version: 1.0.0
// guid: 1274ff0f-5103-48bf-a7f2-6068f7fbb53e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/metrics_retention_policy_config.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MetricsRetentionInfo {
  int64 total_retained_bytes = 1 [(buf.validate.field).int64.gte = 0];
  int64 total_purged_bytes = 2 [(buf.validate.field).int64.gte = 0];
  string oldest_data_age = 3 [(buf.validate.field).string.min_len = 1];
  repeated gcommon.v1.common.MetricsRetentionPolicyConfig policies = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### metrics_time_range.proto {#metrics_time_range}

**Path**: `gcommon/v1/common/metrics_time_range.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `CommonTimeRange`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/metrics_time_range.proto
// version: 1.0.1
// guid: cdd6726e-7f39-47bb-b9d3-23e7e3a1be64
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common time range specification for filtering operations.
 * Provides standardized time-based filtering across all GCommon modules
 * for queries, reports, and data analysis.
 */
message CommonTimeRange {
  // Start time (inclusive) - operations at or after this time are included
  google.protobuf.Timestamp start_time = 1;

  // End time (exclusive) - operations before this time are included
  google.protobuf.Timestamp end_time = 2;
}
```

---

### metrics_validation_result.proto {#metrics_validation_result}

**Path**: `gcommon/v1/common/metrics_validation_result.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `MetricsValidationResult`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/validation_result.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174025

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ValidationResult contains validation results from creation.
 */
message MetricsValidationResult {
  // Whether the configuration is valid
  bool valid = 1;

  // Validation errors
  repeated string errors = 2 [(buf.validate.field).repeated.min_items = 1];

  // Validation warnings
  repeated string warnings = 3 [(buf.validate.field).repeated.min_items = 1];

  // Configuration suggestions
  repeated string suggestions = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### mfa_setup_instruction.proto {#mfa_setup_instruction}

**Path**: `gcommon/v1/common/mfa_setup_instruction.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `MfaSetupInstruction`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_setup_instruction.proto
// version: 1.0.0
// guid: bf15a5c9-23b0-4e2d-9583-24ed000c4656

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MfaSetupInstruction {
  MfaMethod method = 1;
  string instruction = 2 [(buf.validate.field).string.min_len = 1];
  string qr_code = 3 [(buf.validate.field).string.min_len = 1];
  string secret_key = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### notification_frequency.proto {#notification_frequency}

**Path**: `gcommon/v1/common/notification_frequency.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `NotificationFrequency`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/notification_frequency.proto
// version: 1.0.0
// guid: 49798a1d-bd35-44a3-bcdc-4e5d2bfaa330

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message NotificationFrequency {
  // Daily digest enabled
  bool daily_digest = 1;

  // Weekly summary enabled
  bool weekly_summary = 2;

  // Instant notifications enabled
  bool instant_notifications = 3;

  // Quiet hours start time (24-hour format, e.g., "22:00")
  string quiet_hours_start = 4 [(buf.validate.field).string.min_len = 1];

  // Quiet hours end time (24-hour format, e.g., "08:00")
  string quiet_hours_end = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### notification_message.proto {#notification_message}

**Path**: `gcommon/v1/common/notification_message.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `NotificationMessage`

**Imports** (6):

- `gcommon/v1/common/delivery_channel.proto`
- `gcommon/v1/common/delivery_status.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/notification_message.proto
// version: 1.0.0
// guid: 145b3e1e-f6ae-4bbf-9efb-78ebe3c659c8
// file: proto/gcommon/v1/common/notification_message.proto
//
// Message definitions for notification module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_channel.proto";
import "gcommon/v1/common/delivery_status.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Notification message containing content and delivery details.
 * Supports scheduling, multi-channel delivery, and custom data.
 */
message NotificationMessage {
  // Unique notification identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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
  google.protobuf.Timestamp created_at = 8 [lazy = true, (buf.validate.field).required = true];
}
```

---

### o_auth2_credentials.proto {#o_auth2_credentials}

**Path**: `gcommon/v1/common/o_auth2_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `OAuth2Credentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/o_auth2_credentials.proto
// version: 1.0.0
// guid: ebee6621-9f47-4dc4-a8ed-59da2ba599a2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 credentials for authorization code flow authentication.
 * Implements standard OAuth2 authorization code exchange for tokens.
 */
message OAuth2Credentials {
  // Authorization code received from OAuth2 provider
  string code = 1;

  // Redirect URI that was used in the authorization request
  // Must match the URI registered with the OAuth2 provider
  string redirect_uri = 2 [ (buf.validate.field).string.uri = true ];

  // OAuth2 client identifier
  string client_id = 3;

  // OAuth2 client secret (for confidential clients only)
  // Should be omitted for public clients (e.g., mobile apps, SPAs)
  string client_secret = 4;
}
```

---

### o_auth_client.proto {#o_auth_client}

**Path**: `gcommon/v1/common/o_auth_client.proto` **Package**: `gcommon.v1.common` **Lines**: 69

**Messages** (1): `OAuthClient`

**Imports** (4):

- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/o_auth_client.proto
// version: 1.0.0
// guid: 436333b4-e6f3-4a6d-ad0c-a4b0cb8975f8
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 client configuration for third-party integrations.
 * Used for OAuth2 authorization code and implicit flows.
 * Contains client credentials and configuration.
 */
message OAuthClient {
  // Unique client identifier
  string client_id = 1;

  // Client secret (for confidential clients)
  string client_secret = 2;

  // Client name
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Client description
  string description = 4 [ (buf.validate.field).string.max_len = 1000 ];

  // Client type ("public" or "confidential")
  string client_type = 5;

  // Allowed redirect URIs
  repeated string redirect_uris = 6;

  // Allowed grant types
  repeated string grant_types = 7;

  // Allowed response types
  repeated string response_types = 8;

  // Allowed scopes
  repeated string scopes = 9;

  // Client creation timestamp
  google.protobuf.Timestamp created_at = 10 [lazy = true, (buf.validate.field).required = true];

  // Client status
  gcommon.v1.common.ResourceStatus status = 11;

  // Client metadata
  map<string, string> metadata = 12 [lazy = true];

  // Client logo URL
  string logo_url = 13 [ (buf.validate.field).string.uri = true ];

  // Client website URL
  string website_url = 14 [ (buf.validate.field).string.uri = true ];

  // Client owner user ID
  string owner_user_id = 15;
}
```

---

### organization_access_control.proto {#organization_access_control}

**Path**: `gcommon/v1/common/organization_access_control.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `OrganizationAccessControl`

**Imports** (3):

- `gcommon/v1/common/time_restriction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_access_control.proto
// version: 1.1.0
// guid: 0327cd1d-766b-46e4-b980-f039bbde89ef

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/time_restriction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationAccessControl {
  // IP address whitelist for tenant access
  repeated string ip_whitelist = 1 [(buf.validate.field).repeated.min_items = 1];

  // Allowed authentication methods
  repeated string auth_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Session timeout in minutes
  int32 session_timeout = 3 [(buf.validate.field).int32.gt = 0];

  // Maximum concurrent sessions
  int32 max_concurrent_sessions = 4 [(buf.validate.field).int32.gte = 0];

  // Geographic access restrictions
  repeated string allowed_countries = 5 [(buf.validate.field).repeated.min_items = 1];

  // Time-based access restrictions
  repeated TimeRestriction time_restrictions = 6 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### organization_compliance_settings.proto {#organization_compliance_settings}

**Path**: `gcommon/v1/common/organization_compliance_settings.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `OrganizationComplianceSettings`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_compliance_settings.proto
// version: 1.0.0
// guid: 01fb3d5c-a366-4271-a336-2312368dd4f2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationComplianceSettings {
  // GDPR compliance enabled
  bool gdpr_enabled = 1;

  // Data retention period in days
  int32 data_retention_days = 2 [(buf.validate.field).int32.gte = 0];

  // Whether data export is allowed
  bool data_export_enabled = 3;

  // Whether data deletion is allowed
  bool data_deletion_enabled = 4;

  // Compliance certifications
  repeated string certifications = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### organization_notification_settings.proto {#organization_notification_settings}

**Path**: `gcommon/v1/common/organization_notification_settings.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Messages** (1): `OrganizationNotificationSettings`

**Imports** (4):

- `gcommon/v1/common/email_template.proto`
- `gcommon/v1/common/notification_frequency.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_notification_settings.proto
// version: 1.1.0
// guid: 5c93685f-3692-4596-bb11-a848cfce9365

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/email_template.proto";
import "gcommon/v1/common/notification_frequency.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationNotificationSettings {
  // Default email sender address for organization notifications
  string sender_email = 1 [ (buf.validate.field).string.email = true ];

  // Default email sender name
  string sender_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether email notifications are enabled
  bool email_enabled = 3;

  // Whether SMS notifications are enabled
  bool sms_enabled = 4;

  // Whether in-app notifications are enabled
  bool in_app_enabled = 5;

  // Email template customizations
  repeated EmailTemplate email_templates = 6;

  // Notification frequency settings
  NotificationFrequency frequency = 7;
}
```

---

### organization_resource_limits.proto {#organization_resource_limits}

**Path**: `gcommon/v1/common/organization_resource_limits.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `OrganizationResourceLimits`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/organization_resource_limits.proto
// version: 1.0.0
// guid: 53f1daa8-81b3-439e-a815-562120cd11a8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OrganizationResourceLimits {
  // Maximum CPU usage percentage
  int32 max_cpu_percent = 1 [(buf.validate.field).int32.gte = 0];

  // Maximum memory usage in MB
  int64 max_memory_mb = 2 [(buf.validate.field).int64.gte = 0];

  // Maximum disk I/O operations per second
  int32 max_disk_iops = 3 [(buf.validate.field).int32.gte = 0];

  // Maximum network bandwidth in Mbps
  int32 max_network_mbps = 4 [(buf.validate.field).int32.gte = 0];

  // Maximum number of processes
  int32 max_processes = 5 [(buf.validate.field).int32.gte = 0];

  // Maximum number of file descriptors
  int32 max_file_descriptors = 6 [(buf.validate.field).int32.gte = 0];
}
```

---

### pagination.proto {#pagination}

**Path**: `gcommon/v1/common/pagination.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `Pagination`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/pagination.proto
// version: 1.0.0
// guid: 362a2da2-f93c-4652-9287-11938d1af4c3
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common pagination parameters for list operations.
 * Provides standardized pagination controls for queries and lists
 * across all GCommon modules to ensure consistent behavior.
 */
message Pagination {
  // Maximum number of items to return in a single page (0 means use server default)
  int32 page_size = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Opaque token for retrieving the next page (empty for first page)
  string page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Optional: specific page number (alternative to page_token for simple pagination)
  int32 page_number = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
}
```

---

### pagination_info.proto {#pagination_info}

**Path**: `gcommon/v1/common/pagination_info.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `CommonPaginationInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/pagination_info.proto
// version: 1.0.0
// guid: 085f52cb-b1d9-4c82-ada7-9783f2807a33

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message CommonPaginationInfo {
  // Current page number (1-based)
  int32 current_page = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items per page
  int32 page_size = 2 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total number of items available
  int64 total_items = 3 [(buf.validate.field).int64.gte = 0];

  // Total number of pages available
  int32 total_pages = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Whether there is a next page
  bool has_next = 5;

  // Whether there is a previous page
  bool has_previous = 6;

  // Token for retrieving the next page
  string next_page_token = 7 [(buf.validate.field).string.min_len = 1];

  // Token for retrieving the previous page
  string previous_page_token = 8 [(buf.validate.field).string.min_len = 1];
}
```

---

### pagination_options.proto {#pagination_options}

**Path**: `gcommon/v1/common/pagination_options.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `PaginationOptions`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/pagination_options.proto
// version: 1.1.0
// guid: 5c1c9ffd-3554-4f8b-91d6-82d7a453683f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// PaginationOptions defines standard paging parameters.
message PaginationOptions {
  // Maximum number of items to return.
  int32 page_size = 1 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Opaque token representing the next page.
  string page_token = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### parameter_constraints.proto {#parameter_constraints}

**Path**: `gcommon/v1/common/parameter_constraints.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `ParameterConstraints`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/parameter_constraints.proto
// version: 1.0.0
// guid: c8d9e0f1-2345-6789-2345-890123456789

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ParameterConstraints {
  // Minimum value
  string min_value = 1 [(buf.validate.field).string.min_len = 1];

  // Maximum value
  string max_value = 2 [(buf.validate.field).string.min_len = 1];

  // Pattern validation
  string pattern = 3 [(buf.validate.field).string.min_len = 1];

  // Required flag
  bool required = 4;

  // Default value
  string default_value = 5 [(buf.validate.field).string.min_len = 1];
}
```

---

### password_credentials.proto {#password_credentials}

**Path**: `gcommon/v1/common/password_credentials.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `PasswordCredentials`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/password_credentials.proto
// version: 1.0.0
// guid: 1ebf6a98-d3d5-4921-9d97-59280e8ba216
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Username/password credentials for traditional authentication.
 * Supports both username and email-based authentication with optional
 * remember-me functionality for extended session duration.
 */
message PasswordCredentials {
  // Username or email address for authentication
  string username = 1 [(buf.validate.field).string.min_len = 1];

  // User's password (should be transmitted over secure channels only)
  string password = 2 [(buf.validate.field).string.min_len = 8];

  // Remember me option for extended session duration
  // When true, session may have longer expiration time
  bool remember_me = 3;
}
```

---

### password_policy.proto {#password_policy}

**Path**: `gcommon/v1/common/password_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Messages** (1): `PasswordPolicy`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/password_policy.proto
// version: 1.0.0
// guid: d19b7fa7-bd0d-4d6c-bc5b-2453bd250890

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Requirements and restrictions for user passwords.
 */
message PasswordPolicy {
  // Minimum required length for passwords.
  int32 min_length = 1 [(buf.validate.field).int32.gte = 0];

  // Require at least one uppercase letter.
  bool require_uppercase = 2;

  // Require at least one lowercase letter.
  bool require_lowercase = 3;

  // Require at least one numeric digit.
  bool require_number = 4;

  // Require at least one symbol character.
  bool require_symbol = 5;

  // Maximum password age in days before expiration.
  int32 max_age_days = 6 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of previous passwords disallowed for reuse.
  int32 history = 7 [(buf.validate.field).int32.gte = 0];

  // Whether password reuse is permitted after history is exhausted.
  bool allow_reuse = 8;
}
```

---

### permission.proto {#permission}

**Path**: `gcommon/v1/common/permission.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `Permission`

**Imports** (4):

- `gcommon/v1/common/scope_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission.proto
// version: 1.0.0
// guid: 38e2195b-8510-48b4-9c7c-2f87ab8e9a1a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/scope_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission represents a specific action that can be granted
 * to a user or role within the authentication system.
 */
message Permission {
  // Unique identifier for the permission
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Short machine friendly permission name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Human readable description of what the permission allows
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Scope at which this permission applies
  gcommon.v1.common.ScopeType scope = 4;

  // Timestamp when the permission was created
  google.protobuf.Timestamp created_at = 5 [lazy = true, (buf.validate.field).required = true];
}
```

---

### permission_condition.proto {#permission_condition}

**Path**: `gcommon/v1/common/permission_condition.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `PermissionCondition`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_condition.proto
// version: 1.0.0
// guid: 54038d4d-21ce-4ccb-a735-255fae2bcd86

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message PermissionCondition {
  string key = 1 [(buf.validate.field).string.min_len = 1];
  string operator = 2; // eq, ne, in, not_in, etc.
  repeated string values = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### permission_grant.proto {#permission_grant}

**Path**: `gcommon/v1/common/permission_grant.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Messages** (1): `PermissionGrant`

**Imports** (4):

- `gcommon/v1/common/permission_scope.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_grant.proto
// version: 1.0.0
// guid: c33e6d90-d966-45f1-ad79-4b6142211caf
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/permission_scope.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Permission grant entity representing granted permissions.
 * Used for tracking direct permission assignments to users.
 * Supports scoped permissions and expiration.
 */
message PermissionGrant {
  // Unique grant identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User ID receiving the permission
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Permission being granted
  string permission = 3;

  // Resource the permission applies to (optional)
  string resource = 4;

  // Permission scope
  PermissionScope scope = 5;

  // Grant creation timestamp
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];

  // Grant expiration timestamp (optional)
  google.protobuf.Timestamp expires_at = 7 [lazy = true];

  // User who granted the permission
  string granted_by_user_id = 8;

  // Grant metadata
  map<string, string> metadata = 9 [lazy = true];

  // Grant active flag
  bool active = 10;
}
```

---

### permission_metadata.proto {#permission_metadata}

**Path**: `gcommon/v1/common/permission_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Messages** (1): `PermissionMetadata`

**Imports** (4):

- `gcommon/v1/common/permission_condition.proto`
- `gcommon/v1/common/permission_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/permission_metadata.proto
// version: 1.0.0
// guid: e953942b-bd06-424a-8c5a-2b2b9f60d4ab

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/permission_condition.proto";
import "gcommon/v1/common/permission_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message PermissionMetadata {
  // Permission ID
  string permission_id = 1;

  // Permission name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Resource types this permission applies to
  repeated string resource_types = 3;

  // Actions allowed by this permission
  repeated string actions = 4;

  // Conditions or constraints
  repeated gcommon.v1.common.PermissionCondition conditions = 5;

  // Permission level (system, organization, project, etc.)

  AuthPermissionLevel level = 6;

  // Creation metadata
  int64 created_at = 7;
  string created_by = 8 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];
}
```

---

### rate_limit.proto {#rate_limit}

**Path**: `gcommon/v1/common/rate_limit.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `RateLimit`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/rate_limit.proto
// version: 1.0.0
// guid: ba20cc02-8ef6-4de0-9c0a-30ddcb8c7b14
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Rate limiting information for API throttling and quota management.
 * Provides current rate limit status and reset timing information
 * for client-side rate limit handling and backoff strategies.
 */
message RateLimit {
  // Maximum number of requests allowed per time window
  int32 limit = 1 [(buf.validate.field).int32.gte = 0];

  // Duration of the time window for rate limiting
  google.protobuf.Duration window = 2;

  // Number of requests remaining in the current window
  int32 remaining = 3 [(buf.validate.field).int32.gte = 0];

  // Time until the rate limit window resets
  google.protobuf.Duration reset_time = 4;
}
```

---

### rate_limit_info.proto {#rate_limit_info}

**Path**: `gcommon/v1/common/rate_limit_info.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `RateLimitInfo`

**Imports** (4):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/rate_limit_info.proto
// version: 1.0.0
// guid: f124ed67-fd26-47d4-a6f7-c318a926d5f2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RateLimitInfo {
  // Number of requests remaining in the current window
  int64 remaining = 1 [(buf.validate.field).int64.gte = 0];

  // Total requests allowed in the current window
  int64 limit = 2 [(buf.validate.field).int64.gte = 0];

  // Time when the current rate limit window resets
  google.protobuf.Timestamp reset_time = 3;

  // Duration until the rate limit resets
  google.protobuf.Duration retry_after = 4;
}
```

---

### refresh_token.proto {#refresh_token}

**Path**: `gcommon/v1/common/refresh_token.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `RefreshToken`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/refresh_token.proto
// version: 1.0.0
// guid: 19426e54-07ed-40a6-bb1a-739ec97c225f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Refresh token details for token renewal workflows.
 */
message RefreshToken {
  // Refresh token string
  string value = 1;

  // Associated user ID
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // When the refresh token expires
  google.protobuf.Timestamp expires_at = 3 [lazy = true];
}
```

---

### remediation_details.proto {#remediation_details}

**Path**: `gcommon/v1/common/remediation_details.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `RemediationDetails`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/remediation_details.proto
// version: 1.0.0
// guid: 6c9c153d-ad84-44c3-978c-b045473b6345
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RemediationDetails provides information about health remediation actions
 */
message RemediationDetails {
  // Type of remediation action
  string action_type = 1;
  // Description of the remediation action
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];
  // Whether automatic remediation is enabled
  bool auto_remediation_enabled = 3;
  // Maximum number of remediation attempts
  int32 max_attempts = 4;
  // Current attempt count
  int32 current_attempts = 5;
  // Last remediation timestamp
  int64 last_attempt_timestamp = 6;
  // Whether remediation was successful
  bool success = 7;
  // Error message if remediation failed
  string error_message = 8;
}
```

---

### request_metadata.proto {#request_metadata}

**Path**: `gcommon/v1/common/request_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Messages** (1): `RequestMetadata`

**Imports** (4):

- `gcommon/v1/common/client_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/request_metadata.proto
// version: 1.0.0
// guid: 04acf7f8-db07-4855-a3c6-ec7145088149
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Common request metadata for observability and security.
 * Provides standardized metadata that should be included with all
 * requests for distributed tracing, monitoring, and security auditing.
 */
message RequestMetadata {
  // Distributed tracing ID for correlating requests across services
  string trace_id = 1;

  // User ID of the authenticated user making the request
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Correlation ID for grouping related requests in a workflow
  string correlation_id = 3;

  // HTTP headers or gRPC metadata from the original request
  map<string, string> headers = 4;

  // Client application information
  gcommon.v1.common.ClientInfo client = 5;

  // Timestamp when the request was initiated
  google.protobuf.Timestamp timestamp = 6;

  // Session ID if the request is part of a user session
  string session_id = 7;
}
```

---

### resource_reference.proto {#resource_reference}

**Path**: `gcommon/v1/common/resource_reference.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `ResourceReference`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/resource_reference.proto
// version: 1.0.0
// guid: 3be67606-1200-41ca-ab13-9197830e75c2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Resource reference for cross-module operations and relationships.
 * Provides a standardized way to reference resources across different
 * GCommon modules with consistent identification and ownership tracking.
 */
message ResourceReference {
  // Resource type identifier (e.g., "user", "config", "queue", "metric")
  string type = 1;

  // Unique resource identifier within the module
  string id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human-readable resource name for display purposes
  string name = 3 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Module that owns and manages this resource
  string module = 4;
}
```

---

### response_metadata.proto {#response_metadata}

**Path**: `gcommon/v1/common/response_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Messages** (1): `ResponseMetadata`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/pagination_info.proto`
- `gcommon/v1/common/rate_limit_info.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/response_metadata.proto
// version: 1.0.0
// guid: ef32bc34-15e2-49e7-82a9-0c0577f76c38

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/pagination_info.proto";
import "gcommon/v1/common/rate_limit_info.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ResponseMetadata {
  // Trace ID from the corresponding request for correlation
  string trace_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request ID for unique identification of this specific request
  string request_id = 2 [(buf.validate.field).string.min_len = 1];

  // Timestamp when the response was generated
  google.protobuf.Timestamp timestamp = 3;

  // Total processing time for the request
  google.protobuf.Duration processing_time = 4;

  // Service version that processed the request
  string service_version = 5 [(buf.validate.field).string.pattern = "^v?\\d+\\.\\d+\\.\\d+"];

  // Success indicator (true if operation succeeded)
  bool success = 6;

  // Error information if the operation failed
  Error error = 7;

  // Additional metadata specific to the response
  map<string, string> metadata = 8;

  // Rate limiting information
  RateLimitInfo rate_limit = 9;

  // Pagination information for list responses
  CommonPaginationInfo pagination = 10;
}
```

---

### retention_policy_info.proto {#retention_policy_info}

**Path**: `gcommon/v1/common/retention_policy_info.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `RetentionPolicyInfo`

**Imports** (3):

- `gcommon/v1/common/metrics_retention_policy_config.proto`
- `gcommon/v1/common/retention_policy.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_policy_info.proto
// version: 1.0.1
// guid: 9b18ea2c-8470-4b90-93e1-437821fdd7f8

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/metrics_retention_policy_config.proto";
import "gcommon/v1/common/retention_policy.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RetentionPolicyInfo combines a retention policy enum with
 * optional configuration details.
 */
message RetentionPolicyInfo {
  // Predefined policy selection
  gcommon.v1.common.MetricsRetentionPolicy policy = 1;

  // Detailed configuration for custom policies
  gcommon.v1.common.MetricsRetentionPolicyConfig config = 2;
}
```

---

### retry_policy.proto {#retry_policy}

**Path**: `gcommon/v1/common/retry_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 43

**Messages** (1): `CommonRetryPolicy`

**Imports** (4):

- `gcommon/v1/common/error_code.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/retry_policy.proto
// version: 1.0.0
// guid: 8377a6ed-7891-46dd-9cc3-88fabf03ddf8
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error_code.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Retry policy configuration for resilient operation handling.
 * Defines retry behavior with exponential backoff, jitter,
 * and configurable error handling for robust service interactions.
 */
message CommonRetryPolicy {
  // Maximum number of retry attempts (including initial attempt)
  int32 max_attempts = 1 [(buf.validate.field).int32.gte = 0];

  // Initial delay before first retry
  google.protobuf.Duration initial_delay = 2;

  // Maximum delay between retry attempts
  google.protobuf.Duration max_delay = 3;

  // Multiplier for exponential backoff (e.g., 2.0 for doubling)
  double backoff_multiplier = 4 [(buf.validate.field).double.gte = 0.0];

  // Whether to add random jitter to retry timing
  bool enable_jitter = 5;

  // List of error codes that should trigger retries
  repeated ErrorCode retryable_errors = 6 [(buf.validate.field).repeated.min_items = 1];

  // Total timeout for all retry attempts combined
  google.protobuf.Duration total_timeout = 7;
}
```

---

### role.proto {#role}

**Path**: `gcommon/v1/common/role.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `Role`

**Imports** (4):

- `gcommon/v1/common/resource_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role.proto
// version: 1.0.1
// guid: 456e789a-b1c2-3d4e-5f6a-7b8c9d0e1f2a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/resource_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Role definition for role-based access control (RBAC).
 * Represents a collection of permissions that can be assigned to users.
 * Supports hierarchical roles and metadata for extensibility.
 */
message Role {
  // Unique role identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human-readable role name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Role description explaining its purpose
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // Permissions granted by this role
  repeated string permissions = 4;

  // Role metadata for extensibility
  map<string, string> metadata = 5 [lazy = true];

  // Role creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];

  // Role status (active, inactive, etc.)
  ResourceStatus status = 7;
}
```

---

### role_assignment.proto {#role_assignment}

**Path**: `gcommon/v1/common/role_assignment.proto` **Package**: `gcommon.v1.common` **Lines**: 57

**Messages** (1): `RoleAssignment`

**Imports** (4):

- `gcommon/v1/common/role_scope.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role_assignment.proto
// version: 1.0.0
// guid: 91143e0d-5e46-40b4-bf89-ab8d51c7be38
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role_scope.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Role assignment entity representing role grants to users.
 * Used for tracking role-based access control assignments.
 * Supports scoped roles and expiration.
 */
message RoleAssignment {
  // Unique assignment identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User ID receiving the role
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID being assigned
  string role_id = 3;

  // Resource the role applies to (optional, for scoped roles)
  string resource = 4;

  // Role scope
  RoleScope scope = 5;

  // Assignment creation timestamp
  google.protobuf.Timestamp created_at = 6 [lazy = true, (buf.validate.field).required = true];

  // Assignment expiration timestamp (optional)
  google.protobuf.Timestamp expires_at = 7 [lazy = true];

  // User who assigned the role
  string assigned_by_user_id = 8;

  // Assignment metadata
  map<string, string> metadata = 9 [lazy = true];

  // Assignment active flag
  bool active = 10;
}
```

---

### role_metadata.proto {#role_metadata}

**Path**: `gcommon/v1/common/role_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `RoleMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/role_metadata.proto
// version: 1.0.0
// guid: 1b935f51-d35c-4113-aa68-03457b4294db

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RoleMetadata provides metadata about role creation and updates.
 */
message RoleMetadata {
  // Timestamp when the role was created
  google.protobuf.Timestamp created_at = 1 [lazy = true, (buf.validate.field).required = true];

  // Timestamp of the last update to the role
  google.protobuf.Timestamp updated_at = 2 [lazy = true];

  // User ID that created the role
  string created_by = 3 [ (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$" ];
}
```

---

### security_context.proto {#security_context}

**Path**: `gcommon/v1/common/security_context.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `SecurityContext`

**Imports** (3):

- `gcommon/v1/common/auth_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/security_context.proto
// version: 1.0.0
// guid: 80402f15-2486-4290-92b0-77a7f38f1820

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/auth_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SecurityContext {
  // User ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session ID
  string session_id = 2;

  // User roles
  repeated string roles = 3;

  // User permissions
  repeated string permissions = 4;

  // Authentication method used
  gcommon.v1.common.AuthAuthMethod auth_method = 5;

  // MFA verified
  bool mfa_verified = 6;

  // IP address
  string ip_address = 7;

  // User agent
  string user_agent = 8;

  // Authentication timestamp
  int64 auth_timestamp = 9;

  // Context metadata
  map<string, string> metadata = 10;
}
```

---

### security_policy.proto {#security_policy}

**Path**: `gcommon/v1/common/security_policy.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `SecurityPolicy`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/security_policy.proto
// version: 1.0.0
// guid: 1d12dbb5-c796-48b9-beab-f89a58a4d115

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * SecurityPolicy defines account and token security requirements.
 */
message SecurityPolicy {
  // Minimum password length requirement
  uint32 min_password_length = 1 [(buf.validate.field).uint32.gte = 0];

  // Password expiration duration
  google.protobuf.Duration password_ttl = 2;

  // Maximum failed login attempts before lockout
  uint32 max_failed_attempts = 3 [(buf.validate.field).uint32.gte = 0];
}
```

---

### session.proto {#session}

**Path**: `gcommon/v1/common/session.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Messages** (1): `Session`

**Imports** (5):

- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/session_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session.proto
// version: 1.0.0
// guid: 9f1dffb9-b42d-48ad-a0df-25008ed44303
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/session_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Session information representing an authenticated user session.
 * Contains session lifecycle data, client information, and metadata
 * for session management and security tracking.
 */
message Session {
  // Unique session identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // User ID associated with this session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 3 [lazy = true, (buf.validate.field).required = true];

  // Last activity timestamp (updated on each request)
  google.protobuf.Timestamp last_activity_at = 4 [lazy = true];

  // Session expiration timestamp
  google.protobuf.Timestamp expires_at = 5 [lazy = true];

  // Client information from session creation
  ClientInfo client_info = 6 [lazy = true];

  // Current session status
  gcommon.v1.common.SessionStatus status = 7;

  // Session metadata for extensibility and tracking
  map<string, string> metadata = 8 [lazy = true];

  // IP address when session was created
  string ip_address = 9;

  // User agent when session was created
  string user_agent = 10;
}
```

---

### session_info.proto {#session_info}

**Path**: `gcommon/v1/common/session_info.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Messages** (1): `SessionInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_info.proto
// version: 1.0.0
// guid: 805af1d3-ee56-4be2-9807-baeedd9fc6d3
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Session information for lightweight session tracking.
 * Contains essential session data without full session details.
 * Used in responses where full session data is not needed.
 */
message SessionInfo {
  // Session identifier
  string session_id = 1;

  // User ID associated with session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session creation time
  google.protobuf.Timestamp created_at = 3 [ (buf.validate.field).required = true ];

  // Session expiration time
  google.protobuf.Timestamp expires_at = 4;

  // Last activity time
  google.protobuf.Timestamp last_activity_at = 5;

  // IP address
  string ip_address = 6;

  // User agent
  string user_agent = 7;

  // Session active flag
  bool active = 8;
}
```

---

### session_metadata.proto {#session_metadata}

**Path**: `gcommon/v1/common/session_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `SessionMetadata`

**Imports** (5):

- `gcommon/v1/common/device_info.proto`
- `gcommon/v1/common/location_info.proto`
- `gcommon/v1/common/session_state.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_metadata.proto
// version: 1.0.0
// guid: 01cd27dc-f07e-4fe5-805f-ff4fc49ef91b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/device_info.proto";
import "gcommon/v1/common/location_info.proto";
import "gcommon/v1/common/session_state.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SessionMetadata {
  // Session ID
  string session_id = 1;

  // User ID
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Session start time
  int64 started_at = 3;

  // Last activity time
  int64 last_activity = 4;

  // Session expiry time
  int64 expires_at = 5;

  // IP address
  string ip_address = 6;

  // User agent
  string user_agent = 7;

  // Device information
  gcommon.v1.common.DeviceInfo device_info = 8;

  // Location information
  gcommon.v1.common.LocationInfo location_info = 9;

  // Session state

  gcommon.v1.common.SessionState state = 10;
}
```

---

### sort_options.proto {#sort_options}

**Path**: `gcommon/v1/common/sort_options.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `SortOptions`

**Imports** (3):

- `gcommon/v1/common/sort_direction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/sort_options.proto
// version: 1.1.0
// guid: 34507f56-8bd2-4dd8-af7e-c9045ddbf029

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/sort_direction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Sort options for configuring list sorting.
 * Defines field and direction for sorting operations.
 */
message SortOptions {
  // Field to sort by
  string sort_field = 1 [(buf.validate.field).string.min_len = 1];

  // Sort direction
  gcommon.v1.common.SortDirection direction = 2;
}
```

---

### source_location.proto {#source_location}

**Path**: `gcommon/v1/common/source_location.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `SourceLocation`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/source_location.proto
// version: 1.0.0
// guid: b529bc13-5c0e-4b3e-9d64-5025a5889fa2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// SourceLocation describes the origin of a log entry
message SourceLocation {
  // File name where the log occurred
  string file = 1 [(buf.validate.field).string.min_len = 1];

  // Line number in the source file
  int32 line = 2 [(buf.validate.field).int32.gte = 0];

  // Function name
  string function = 3 [(buf.validate.field).string.min_len = 1];

  // Package or module name
  string package = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### string_array.proto {#string_array}

**Path**: `gcommon/v1/common/string_array.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `StringArray`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/string_array.proto
// version: 1.0.0
// guid: 5ff69d27-5bdf-4475-a029-e9f948b8a078
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * String array wrapper for oneof usage in filter values and other contexts.
 * Required because oneof fields cannot directly contain repeated types,
 * so arrays must be wrapped in a message.
 */
message StringArray {
  // Array of string values
  repeated string values = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### subscription_info.proto {#subscription_info}

**Path**: `gcommon/v1/common/subscription_info.proto` **Package**: `gcommon.v1.common` **Lines**: 46

**Messages** (1): `CommonSubscriptionInfo`

**Imports** (7):

- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/filter_options.proto`
- `gcommon/v1/common/subscription_options.proto`
- `gcommon/v1/common/subscription_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_info.proto
// version: 1.0.0
// guid: 890b3e39-196c-4fe4-8153-4f73bdf677e6
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/filter_options.proto";
import "gcommon/v1/common/subscription_options.proto";
import "gcommon/v1/common/subscription_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Subscription information for streaming and event-driven operations.
 * Manages long-lived subscriptions with filtering, time ranges,
 * and client-specific configuration for real-time data streaming.
 */
message CommonSubscriptionInfo {
  // Unique identifier for this subscription
  string subscription_id = 1 [(buf.validate.field).string.min_len = 1];

  // Filter criteria for subscription events
  FilterOptions filter = 2;

  // When the subscription started
  google.protobuf.Timestamp start_time = 3;

  // Optional end time for the subscription (null for indefinite)
  google.protobuf.Timestamp end_time = 4;

  // Information about the subscribing client
  ClientInfo subscriber = 5;

  // Subscription configuration options
  SubscriptionOptions options = 6;

  // Current status of the subscription
  SubscriptionStatus status = 7;
}
```

---

### subscription_options.proto {#subscription_options}

**Path**: `gcommon/v1/common/subscription_options.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `SubscriptionOptions`

**Imports** (4):

- `gcommon/v1/common/ack_mode.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_options.proto
// version: 1.0.0
// guid: 8c54ce21-f38c-48cb-8631-3f92c91cbd67
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/ack_mode.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Subscription options for configuring streaming behavior.
 * Controls historical data inclusion, batching, acknowledgment,
 * and keep-alive settings for optimal streaming performance.
 */
message SubscriptionOptions {
  // Whether to include historical data in the subscription
  bool include_history = 1;

  // Maximum number of events to batch together
  int32 max_batch_size = 2 [(buf.validate.field).int32.gte = 0];

  // Acknowledgment mode for message delivery
  gcommon.v1.common.AckMode ack_mode = 3;

  // Keep-alive interval to maintain connection
  google.protobuf.Duration keep_alive = 4;
}
```

---

### subscription_preferences.proto {#subscription_preferences}

**Path**: `gcommon/v1/common/subscription_preferences.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `SubscriptionPreferences`

**Imports** (3):

- `gcommon/v1/common/delivery_channel_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/subscription_preferences.proto
// version: 1.2.0
// guid: e1f2g3h4-i5j6-7890-k1l2-m3n4o5p6q7r8

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_channel_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * User subscription preferences for event notifications.
 */
message SubscriptionPreferences {
  // User or entity identifier
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

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

**Path**: `gcommon/v1/common/template.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `Template`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/template.proto
// version: 1.0.0
// guid: b40be0b3-2832-4999-be82-78423c52b4d3
// file: proto/gcommon/v1/common/template.proto
//
// Notification template definition for reusable messages.
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Template for rendering notification content.
 */
message Template {
  // Template identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Human readable name
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Template body using placeholders
  string body = 3;

  // Time the template was created
  google.protobuf.Timestamp created_at = 4 [lazy = true, (buf.validate.field).required = true];

  // Time the template was last updated
  google.protobuf.Timestamp updated_at = 5 [lazy = true];
}
```

---

### template_parameter.proto {#template_parameter}

**Path**: `gcommon/v1/common/template_parameter.proto` **Package**: `gcommon.v1.common` **Lines**: 68

**Messages** (1): `TemplateParameter`

**Imports** (4):

- `gcommon/v1/common/parameter_constraints.proto`
- `gcommon/v1/common/parameter_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/template_parameter.proto
// version: 1.1.0
// guid: 800be7b5-ca05-4137-a8d2-7d1a3fe5cc97

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/parameter_constraints.proto";
import "gcommon/v1/common/parameter_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TemplateParameter {
  // Parameter name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Parameter description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Parameter type
  gcommon.v1.common.ParameterType type = 3;

  // Whether parameter is required
  bool required = 4;

  // Default value
  string default_value = 5;

  // Allowed values (for enum types)
  repeated string allowed_values = 6;

  // Parameter constraints
  gcommon.v1.common.ParameterConstraints constraints = 7;

  // Parameter group
  string group = 8;

  // Display order
  int32 order = 9;

  // Whether parameter is sensitive
  bool sensitive = 10;

  // Parameter validation pattern
  string validation_pattern = 11;

  // Parameter examples
  repeated string examples = 12;

  // Parameter documentation
  string documentation = 13;

  // Parameter display name
  string display_name = 14 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Parameter placeholder text
  string placeholder = 15;
}
```

---

### time_range_metrics.proto {#time_range_metrics}

**Path**: `gcommon/v1/common/time_range_metrics.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `TimeRangeMetrics`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/time_range.proto
// version: 1.0.0
// guid: d6e7f8a9-012d-467c-1234-789012345678

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TimeRangeMetrics {
  // Start timestamp
  google.protobuf.Timestamp start = 1;

  // End timestamp
  google.protobuf.Timestamp end = 2;

  // Duration in seconds
  int64 duration_seconds = 3 [(buf.validate.field).int64.gt = 0];
}
```

---

### time_restriction.proto {#time_restriction}

**Path**: `gcommon/v1/common/time_restriction.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `TimeRestriction`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/time_restriction.proto
// version: 1.0.0
// guid: e1c0e36e-397a-42c1-a74a-e7aeca18ade2

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TimeRestriction {
  // Day of week (0-6, 0=Sunday)
  int32 day_of_week = 1 [(buf.validate.field).int32.gte = 0];

  // Start time (24-hour format, e.g., "09:00")
  string start_time = 2 [(buf.validate.field).string.min_len = 1];

  // End time (24-hour format, e.g., "17:00")
  string end_time = 3 [(buf.validate.field).string.min_len = 1];

  // Timezone for this restriction
  string timezone = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### token.proto {#token}

**Path**: `gcommon/v1/common/token.proto` **Package**: `gcommon.v1.common` **Lines**: 70

**Messages** (1): `Token`

**Imports** (5):

- `gcommon/v1/common/token_status.proto`
- `gcommon/v1/common/token_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token.proto
// version: 1.0.0
// guid: caf60cc1-beab-4119-bb01-f426fbb8b680
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/token_status.proto";
import "gcommon/v1/common/token_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Token entity representing authentication and authorization tokens.
 * Used for access tokens, refresh tokens, and other security tokens.
 * Contains token metadata and lifecycle information.
 */
message Token {
  // Unique token identifier
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Token value (may be JWT or opaque)
  string value = 2;

  // Token type (access, refresh, etc.)
  gcommon.v1.common.TokenType type = 3;

  // Token status
  gcommon.v1.common.TokenStatus status = 4;

  // User ID associated with this token
  string user_id = 5 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Client ID that requested this token
  string client_id = 6;

  // Token scopes/permissions
  repeated string scopes = 7;

  // Token creation timestamp
  google.protobuf.Timestamp created_at = 8 [lazy = true, (buf.validate.field).required = true];

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 9 [lazy = true];

  // Last time token was used
  google.protobuf.Timestamp last_used_at = 10 [lazy = true];

  // Token metadata for extensibility
  map<string, string> metadata = 11 [lazy = true];

  // IP address when token was created
  string ip_address = 12;

  // User agent when token was created
  string user_agent = 13;

  // Refresh token ID (for access tokens)
  string refresh_token_id = 14;
}
```

---

### token_info.proto {#token_info}

**Path**: `gcommon/v1/common/token_info.proto` **Package**: `gcommon.v1.common` **Lines**: 51

**Messages** (1): `TokenInfo`

**Imports** (4):

- `gcommon/v1/common/token_type.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_info.proto
// version: 1.0.0
// guid: 4c29c1f8-c076-4308-b035-5ac388999383
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/token_type.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Token information for lightweight token tracking.
 * Contains essential token data without sensitive information.
 * Used in responses where full token data is not needed.
 */
message TokenInfo {
  // Token identifier
  string token_id = 1;

  // Token type
  gcommon.v1.common.TokenType type = 2;

  // User ID associated with token
  string user_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Client ID that owns the token
  string client_id = 4;

  // Token scopes
  repeated string scopes = 5;

  // Token creation time
  google.protobuf.Timestamp created_at = 6 [ (buf.validate.field).required = true ];

  // Token expiration time
  google.protobuf.Timestamp expires_at = 7;

  // Token active flag
  bool active = 8;

  // Time until expiration (seconds)
  int64 expires_in = 9;
}
```

---

### token_metadata.proto {#token_metadata}

**Path**: `gcommon/v1/common/token_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `TokenMetadata`

**Imports** (3):

- `gcommon/v1/common/token_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/token_metadata.proto
// version: 1.0.0
// guid: 038ee237-f0cb-43e1-95c5-5869754a969d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/token_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message TokenMetadata {
  // Token ID
  string token_id = 1 [(buf.validate.field).string.min_len = 1];

  // Token type
  gcommon.v1.common.TokenType type = 2;

  // Subject (user ID)
  string subject = 3 [(buf.validate.field).string.min_len = 1];

  // Audience
  repeated string audience = 4 [(buf.validate.field).repeated.min_items = 1];

  // Scopes
  repeated string scopes = 5 [(buf.validate.field).repeated.min_items = 1];

  // Issued at timestamp
  int64 issued_at = 6 [(buf.validate.field).int64.gte = 0];

  // Expires at timestamp
  int64 expires_at = 7 [(buf.validate.field).int64.gte = 0];

  // Not before timestamp
  int64 not_before = 8 [(buf.validate.field).int64.gte = 0];

  // Issuer
  string issuer = 9 [(buf.validate.field).string.min_len = 1];
}
```

---

### user.proto {#user}

**Path**: `gcommon/v1/common/user.proto` **Package**: `gcommon.v1.common` **Lines**: 87

**Messages** (1): `User`

**Imports** (4):

- `gcommon/v1/common/user_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user.proto
// version: 1.0.0
// guid: 00ae1e1a-a2c9-4e7a-bd91-dda7967d8647
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * User entity representing a complete user account.
 * Contains comprehensive user data for account management.
 * Includes profile, security, and administrative information.
 */
message User {
  // Unique user identifier (immutable)
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username (may be mutable depending on system policy)
  string username = 2;

  // Primary email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Display name
  string display_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // First name
  string first_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Last name
  string last_name = 6 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // User account status
  gcommon.v1.common.UserStatus status = 7;

  // Account creation timestamp (immutable)
  google.protobuf.Timestamp created_at = 8 [lazy = true, (buf.validate.field).required = true];

  // Last account update timestamp
  google.protobuf.Timestamp updated_at = 9 [lazy = true];

  // Last successful login timestamp
  google.protobuf.Timestamp last_login_at = 10 [lazy = true];

  // Email verification status
  bool email_verified = 11;

  // Phone number (optional)
  string phone_number = 12;

  // Phone verification status
  bool phone_verified = 13;

  // User preferences and settings
  map<string, string> preferences = 14 [lazy = true];

  // User metadata for extensibility
  map<string, string> metadata = 15 [lazy = true];

  // Avatar/profile image URL
  string avatar_url = 16 [ (buf.validate.field).string.uri = true ];

  // User timezone
  string timezone = 17;

  // User locale/language preference
  string locale = 18;
}
```

---

### user_details.proto {#user_details}

**Path**: `gcommon/v1/common/user_details.proto` **Package**: `gcommon.v1.common` **Lines**: 70

**Messages** (1): `UserDetails`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_details.proto
// version: 1.0.0
// guid: 3dfa4bc7-c4c7-4c1c-89e9-e3e3d3219d52

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UserDetails {
  // Unique identifier for the user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username
  string username = 2;

  // Email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Full name
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account is enabled
  bool enabled = 5;

  // Assigned roles
  repeated string roles = 6;

  // User permissions
  repeated string permissions = 7;

  // Additional metadata
  map<string, string> metadata = 8;

  // When the account was created
  google.protobuf.Timestamp created_at = 9 [ (buf.validate.field).required = true ];

  // When the account was last updated
  google.protobuf.Timestamp updated_at = 10;

  // Last login time
  google.protobuf.Timestamp last_login_at = 11;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 12;

  // Whether the account is deleted
  bool deleted = 13;

  // Email verification status
  bool email_verified = 14;

  // Multi-factor authentication enabled
  bool mfa_enabled = 15;

  // Number of active sessions
  int32 active_sessions = 16;
}
```

---

### user_info.proto {#user_info}

**Path**: `gcommon/v1/common/user_info.proto` **Package**: `gcommon.v1.common` **Lines**: 67

**Messages** (1): `UserInfo`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_info.proto
// version: 1.0.0
// guid: a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * UserInfo contains information about a user.
 */
message UserInfo {
  // Unique user identifier
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username
  string username = 2;

  // User's email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // User's display name
  string display_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // User roles
  repeated string roles = 5;

  // User permissions
  repeated string permissions = 6;

  // User groups
  repeated string groups = 7;

  // User metadata
  map<string, string> metadata = 8;

  // When the user was created
  google.protobuf.Timestamp created_at = 9 [ (buf.validate.field).required = true ];

  // When the user was last updated
  google.protobuf.Timestamp updated_at = 10;

  // When the user last logged in
  google.protobuf.Timestamp last_login_at = 11;

  // Whether the user account is active
  bool active = 12;

  // Whether the user's email is verified
  bool email_verified = 13;

  // User's profile picture URL
  string avatar_url = 14 [ (buf.validate.field).string.uri = true ];
}
```

---

### user_metadata.proto {#user_metadata}

**Path**: `gcommon/v1/common/user_metadata.proto` **Package**: `gcommon.v1.common` **Lines**: 66

**Messages** (1): `UserMetadata`

**Imports** (5):

- `gcommon/v1/common/user_preferences.proto`
- `gcommon/v1/common/verification_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_metadata.proto
// version: 1.0.0
// guid: 18290eba-bd6e-4e3a-8aea-ffb79b9fa0f9

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_preferences.proto";
import "gcommon/v1/common/verification_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UserMetadata {
  // User's preferred display name
  string display_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // User's profile picture URL
  string avatar_url = 2 [ (buf.validate.field).string.uri = true ];

  // User's timezone
  string timezone = 3;

  // User's preferred language
  string language = 4;

  // User's locale
  string locale = 5;

  // User's profile bio/description
  string bio = 6;

  // User's website URL
  string website = 7;

  // User's location/address
  string location = 8;

  // Date of birth for age verification purposes
  google.protobuf.Timestamp birth_date = 9;

  // User's gender
  string gender = 10;

  // User's occupation/job title
  string occupation = 11;

  // User's company/organization
  string company = 12;

  // Additional custom metadata
  map<string, string> custom_fields = 13;

  // User preferences
  gcommon.v1.common.UserPreferences preferences = 14;

  // Account verification status
  gcommon.v1.common.VerificationStatus verification = 15;
}
```

---

### user_preferences.proto {#user_preferences}

**Path**: `gcommon/v1/common/user_preferences.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `UserPreferences`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_preferences.proto
// version: 1.0.0
// guid: 484a49f6-ee77-4683-b2f7-3bb3f64107f9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UserPreferences {
  // Email notification preferences
  bool email_notifications = 1;

  // SMS notification preferences
  bool sms_notifications = 2;

  // Push notification preferences
  bool push_notifications = 3;

  // Marketing email preferences
  bool marketing_emails = 4;

  // Two-factor authentication enabled
  bool two_factor_enabled = 5;

  // Session timeout preference (minutes)
  int32 session_timeout_minutes = 6 [(buf.validate.field).int32.gt = 0];

  // Theme preference (light, dark, auto)
  string theme = 7 [(buf.validate.field).string.min_len = 1];
}
```

---

### user_profile.proto {#user_profile}

**Path**: `gcommon/v1/common/user_profile.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Messages** (1): `UserProfile`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/user_profile.proto
// version: 1.0.0
// guid: 9554454d-6823-42b3-aac9-341f375031ea

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Public profile information for a user.
 */
message UserProfile {
  // Unique identifier for the user.
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Display name for the user.
  string display_name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Primary email address.
  string email = 3 [ (buf.validate.field).string.email = true ];

  // URL to the user's avatar image.
  string avatar_url = 4 [ (buf.validate.field).string.uri = true ];

  // Additional custom attributes for the profile.
  map<string, string> attributes = 5 [lazy = true];
}
```

---

### verification_status.proto {#verification_status}

**Path**: `gcommon/v1/common/verification_status.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `VerificationStatus`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verification_status.proto
// version: 1.0.1
// guid: 2e8605fa-61b3-4b0c-8322-8e47f1d58d0e

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerificationStatus {
  // Email verification status
  bool email_verified = 1;

  // Phone number verification status
  bool phone_verified = 2;

  // Identity verification status
  bool identity_verified = 3;

  // When email was verified
  google.protobuf.Timestamp email_verified_at = 4;

  // When phone was verified
  google.protobuf.Timestamp phone_verified_at = 5;

  // When identity was verified
  google.protobuf.Timestamp identity_verified_at = 6;
}
```

---

### appender_config.proto {#appender_config}

**Path**: `gcommon/v1/common/appender_config.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `AppenderConfig`

**Imports** (5):

- `gcommon/v1/common/appender_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`
- `gcommon/v1/common/output_config.proto`
- `gcommon/v1/common/formatter_config.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/appender_config.proto
// version: 1.0.0
// guid: 1423b6a1-54da-4a63-8427-4225cd81621a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/appender_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";
import "gcommon/v1/common/output_config.proto";
import "gcommon/v1/common/formatter_config.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message AppenderConfig {
  // Unique appender name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Appender backend type
  AppenderType type = 2;

  // Output destination details
  OutputConfig output = 3;

  // Formatting configuration
  LogFormatterConfig formatter = 4;

  // Arbitrary appender properties
  map<string, string> properties = 5;
}
```

---

### auth_config.proto {#auth_config}

**Path**: `gcommon/v1/common/auth_config.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `AuthAuthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/auth_config.proto
// version: 1.0.1
// guid: b2c3d4e5-f6a7-890b-c1d2-e3f4a5b6c7d8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * AuthConfig defines authentication configuration for the application
 * including token lifetimes and password requirements.
 */
message AuthAuthConfig {
  // How long issued access tokens remain valid
  google.protobuf.Timestamp access_token_ttl = 1;

  // How long refresh tokens remain valid
  google.protobuf.Timestamp refresh_token_ttl = 2;

  // Whether multi-factor authentication is required
  bool require_mfa = 3;
}
```

---

### circuit_breaker_config.proto {#circuit_breaker_config}

**Path**: `gcommon/v1/common/circuit_breaker_config.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `CommonCircuitBreakerConfig`

**Imports** (4):

- `gcommon/v1/common/circuit_breaker_state.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/circuit_breaker_config.proto
// version: 1.0.0
// guid: 2fa42a3e-78ac-439f-ab85-af2587126423
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/circuit_breaker_state.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Circuit breaker configuration for fault tolerance and system protection.
 * Implements the circuit breaker pattern with configurable thresholds,
 * timeouts, and state management for preventing cascade failures.
 */
message CommonCircuitBreakerConfig {
  // Number of consecutive failures to trigger circuit opening
  int32 failure_threshold = 1 [(buf.validate.field).int32.gte = 0];

  // Number of consecutive successes to close the circuit
  int32 success_threshold = 2 [(buf.validate.field).int32.gte = 0];

  // Duration to keep circuit open before attempting half-open
  google.protobuf.Duration timeout = 3;

  // Maximum concurrent requests allowed in half-open state
  int32 max_requests = 4 [(buf.validate.field).int32.gte = 0];

  // Time window for counting failures and successes
  google.protobuf.Duration window_size = 5;

  // Current state of the circuit breaker
  CircuitBreakerState state = 6;
}
```

---

### config_retry_settings.proto {#config_retry_settings}

**Path**: `gcommon/v1/common/config_retry_settings.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `ConfigRetrySettings`

**Imports** (3):

- `gcommon/v1/common/backoff_strategy.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/config/v1/retry_settings.proto
// version: 1.0.0
// guid: 97d15dc6-ddeb-4e88-a455-16bb8fb5c292

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/backoff_strategy.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ConfigRetrySettings {
  // Whether retry is enabled
  bool enabled = 1;

  // Maximum retry count
  int32 max_retries = 2 [(buf.validate.field).int32.gte = 0];

  // Retry delay in seconds
  int32 delay_seconds = 3 [(buf.validate.field).int32.gte = 0];

  // Retry backoff strategy
  gcommon.v1.common.BackoffStrategy backoff_strategy = 4;

  // Retry conditions
  repeated string conditions = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### config_value.proto {#config_value}

**Path**: `gcommon/v1/common/config_value.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `ConfigValue`

**Imports** (4):

- `gcommon/v1/common/value_type.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/config_value.proto
// version: 1.0.0
// guid: 343ca568-969b-4136-953b-7eac76c64553
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/value_type.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration value with type information and metadata.
 * Supports multiple value types with encryption and validation capabilities
 * for secure and type-safe configuration management.
 */
message ConfigValue {
  // The configuration value (one of the supported types)
  oneof value {
    // String value for text configuration
    string string_value = 1 [(buf.validate.field).string.min_len = 1];

    // Integer value for numeric configuration
    int64 int_value = 2 [(buf.validate.field).int64.gte = 0];

    // Double value for floating-point configuration
    double double_value = 3 [(buf.validate.field).double.gte = 0.0];

    // Boolean value for true/false configuration
    bool bool_value = 4;

    // Binary data for complex configuration
    bytes bytes_value = 5;

    // Any protobuf message for structured configuration
    google.protobuf.Any any_value = 6 [lazy = true];
  }

  // Value type for validation and serialization
  gcommon.v1.common.ValueType type = 7;

  // Whether the value is encrypted at rest
  bool encrypted = 8;

  // Additional metadata about the configuration value
  map<string, string> metadata = 9 [lazy = true];
}
```

---

### configure_alerting_request.proto {#configure_alerting_request}

**Path**: `gcommon/v1/common/configure_alerting_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ConfigureAlertingRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/configure_alerting_request.proto
// version: 1.0.0
// guid: 760eeee5-189e-489d-b385-42e80f43726f
// file: proto/gcommon/v1/common/configure_alerting_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ConfigureAlertingRequest {
  // Name of the service or check to configure
  string target = 1 [(buf.validate.field).string.min_len = 1];

  // Whether alerting is enabled for this check
  bool enabled = 2;

  // Number of consecutive failures required before alerting
  int32 failure_threshold = 3 [(buf.validate.field).int32.gte = 0];

  // Optional notification channels (email, slack, etc.)
  repeated string channels = 4 [(buf.validate.field).repeated.min_items = 1];

  // Standard request metadata for tracing and auth
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### configure_alerting_response.proto {#configure_alerting_response}

**Path**: `gcommon/v1/common/configure_alerting_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `ConfigureAlertingResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/configure_alerting_response.proto
// version: 1.0.0
// guid: f996c2ec-cfc9-45c8-8d78-97eef22d2df4
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for configuring alerting settings.
 * Contains the result of alerting configuration changes.
 */
message ConfigureAlertingResponse {
  // Success status
  bool success = 1;

  // Configuration ID
  string config_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if configuration failed
  gcommon.v1.common.Error error = 3;

  // Applied alerting rules
  repeated string applied_rules = 4 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### configure_logger_request.proto {#configure_logger_request}

**Path**: `gcommon/v1/common/configure_logger_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `ConfigureLoggerRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/configure_logger_request.proto
// version: 1.0.0
// guid: 2f3e4d5c-6b7a-8190-2e3f-4a5b6c7d8e9f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigureLoggerRequest defines the request for configuring logger settings.
 */
message ConfigureLoggerRequest {
  // Logger name or identifier
  string logger_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Log level to set
  string level = 2;

  // Output configuration
  string output_config = 3;
}
```

---

### configure_logger_response.proto {#configure_logger_response}

**Path**: `gcommon/v1/common/configure_logger_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `ConfigureLoggerResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/configure_logger_response.proto
// version: 1.0.0
// guid: 3f4e5d6c-7b8a-9201-3e4f-5a6b7c8d9e0f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigureLoggerResponse defines the response from configuring logger settings.
 */
message ConfigureLoggerResponse {
  // Status of the configuration
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### formatter_config.proto {#formatter_config}

**Path**: `gcommon/v1/common/formatter_config.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `LogFormatterConfig`

**Imports** (3):

- `gcommon/v1/common/formatter_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/formatter_config.proto
// version: 1.0.0
// guid: d4e8088a-7b07-48cf-b572-0d850b7218e4

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/formatter_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message LogFormatterConfig {
  // Formatting strategy
  gcommon.v1.common.FormatterType type = 1;

  // Optional format pattern
  string pattern = 2 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_auth_config_request.proto {#get_auth_config_request}

**Path**: `gcommon/v1/common/get_auth_config_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetAuthConfigRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_auth_config_request.proto
// version: 1.0.0
// guid: 8931da09-15df-4c40-a4c1-6be6ad1806f5
// file: proto/gcommon/v1/common/get_auth_config_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetAuthConfigRequest {
  // Optional specific config keys to retrieve
  repeated string keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Include sensitive configuration
  bool include_sensitive = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### health_config.proto {#health_config}

**Path**: `gcommon/v1/common/health_config.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `HealthConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_config.proto
// version: 1.0.0
// guid: ebed5c7e-06be-4527-8d87-41afd0b1320d
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthConfig represents health configuration
 */
message HealthConfig {
  // Whether health checking is enabled
  bool enabled = 1;
  // Health endpoint path
  string endpoint = 2 [(buf.validate.field).string.min_len = 1];
  // Liveness check path
  string liveness_path = 3 [(buf.validate.field).string.min_len = 1];
  // Readiness check path
  string readiness_path = 4 [(buf.validate.field).string.min_len = 1];
  // Startup check path
  string startup_path = 5 [(buf.validate.field).string.min_len = 1];
  // Check timeout in seconds
  int32 timeout_seconds = 6 [(buf.validate.field).int32.gt = 0];
  // Check interval in seconds
  int32 interval_seconds = 7 [(buf.validate.field).int32.gte = 0];
  // Grace period in seconds
  int32 grace_period_seconds = 8 [(buf.validate.field).int32.gte = 0];
  // Number of retries
  int32 retries = 9 [(buf.validate.field).int32.gte = 0];
}
```

---

### jwt_config.proto {#jwt_config}

**Path**: `gcommon/v1/common/jwt_config.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `JWTConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/jwt_config.proto
// version: 1.0.0
// guid: c3d4e5f6-a7b8-90c1-d2e3-f4a5b6c7d8e9

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * JWTConfig defines parameters for JWT token generation and validation.
 */
message JWTConfig {
  // Signing algorithm used for tokens (e.g., HS256, RS256)
  string signing_algorithm = 1 [(buf.validate.field).string.min_len = 1];

  // Duration access tokens remain valid
  google.protobuf.Duration access_token_ttl = 2;

  // Duration refresh tokens remain valid
  google.protobuf.Duration refresh_token_ttl = 3;
}
```

---

### ldap_config.proto {#ldap_config}

**Path**: `gcommon/v1/common/ldap_config.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `LdapConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/ldap_config.proto
// version: 1.0.0
// guid: de3eeaac-ad85-4f66-a525-670864c5815d

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration options for LDAP authentication providers.
 */
message LdapConfig {
  // Hostname or IP address of the LDAP server.
  string host = 1 [(buf.validate.field).string.min_len = 1];

  // Port number for the LDAP server.
  int32 port = 2 [(buf.validate.field).int32.gte = 1, (buf.validate.field).int32.lte = 65535];

  // Whether to use TLS for connections.
  bool use_tls = 3;

  // Distinguished name used to bind to the server.
  string bind_dn = 4 [(buf.validate.field).string.min_len = 1];

  // Password for the bind DN.
  string bind_password = 5 [(buf.validate.field).string.min_len = 8];

  // Base DN for searches.
  string base_dn = 6 [(buf.validate.field).string.min_len = 1];

  // LDAP filter used to locate user records.
  string user_filter = 7 [(buf.validate.field).string.min_len = 1];

  // LDAP filter used to locate group records.
  string group_filter = 8 [(buf.validate.field).string.min_len = 1];

  // Connection timeout in seconds.
  int32 timeout_seconds = 9 [(buf.validate.field).int32.gt = 0];

  // Additional provider-specific attributes.
  map<string, string> attributes = 10 [lazy = true];
}
```

---

### logger_config.proto {#logger_config}

**Path**: `gcommon/v1/common/logger_config.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `LoggerConfig`

**Imports** (4):

- `gcommon/v1/common/appender_config.proto`
- `gcommon/v1/common/log_level.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logger_config.proto
// version: 1.0.0
// guid: 37c6c755-fc97-46c2-8116-248fc5a0ce3c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/appender_config.proto";
import "gcommon/v1/common/log_level.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LoggerConfig defines configuration for a logger instance
message LoggerConfig {
  // Minimum log level for this logger
  LogLevel level = 1;

  // Output appenders used by this logger
  repeated AppenderConfig appenders = 2 [(buf.validate.field).repeated.min_items = 1];

  // Inherit appenders from parent logger
  bool inherit_appenders = 3;

  // Propagate log entries to parent logger
  bool propagate = 4;

  // Additional logger properties
  map<string, string> properties = 5;
}
```

---

### metrics_api_key_config.proto {#metrics_api_key_config}

**Path**: `gcommon/v1/common/metrics_api_key_config.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `MetricsAPIKeyConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/api_key_config.proto
// version: 1.0.0
// guid: af9b891a-1959-43c2-a287-891b402b4cdf

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MetricsAPIKeyConfig {
  // Header name for API key
  string header_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether API key is required
  bool required = 2;

  // Allowed API keys (for validation)
  repeated string allowed_keys = 3;
}
```

---

### metrics_config_change.proto {#metrics_config_change}

**Path**: `gcommon/v1/common/metrics_config_change.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `MetricsConfigChange`

**Imports** (3):

- `gcommon/v1/common/change_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/config_change.proto
// version: 1.1.0
// guid: 29bbb593-9903-43ef-a25e-1c3c7c0a4e64

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/change_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ConfigChange describes a configuration change that was made.
 */
message MetricsConfigChange {
  // Type of change
  gcommon.v1.common.MetricsChangeType change_type = 1;

  // Setting that was changed
  string setting_path = 2;

  // Old value (if applicable)
  string old_value = 3;

  // New value
  string new_value = 4;

  // Description of the change
  string description = 5 [ (buf.validate.field).string.max_len = 1000 ];
}
```

---

### metrics_retention_policy_config.proto {#metrics_retention_policy_config}

**Path**: `gcommon/v1/common/metrics_retention_policy_config.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `MetricsRetentionPolicyConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/metrics/v1/retention_policy_config.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174024

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Retention policy configuration for metric data.
 */
message MetricsRetentionPolicyConfig {
  // How long to retain data
  google.protobuf.Duration duration = 1;

  // Storage tier configuration
  string storage_tier = 2 [(buf.validate.field).string.min_len = 1];

  // Compression settings
  string compression = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### mfa_config.proto {#mfa_config}

**Path**: `gcommon/v1/common/mfa_config.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `MfaConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mfa_config.proto
// version: 1.0.0
// guid: ae560b06-340b-4dca-9a42-dc0eb623fbb1

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Multi-factor authentication configuration settings.
 */
message MfaConfig {
  // Whether MFA is enabled.
  bool enabled = 1;

  // Supported MFA methods (e.g., "totp", "sms", "email").
  repeated string methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Time-based one-time password period in seconds.
  int32 totp_period = 3 [(buf.validate.field).int32.gte = 0];

  // Number of digits for TOTP codes.
  int32 totp_digits = 4 [(buf.validate.field).int32.gte = 0];

  // Whether SMS delivery is enabled.
  bool sms_enabled = 5;

  // Whether email delivery is enabled.
  bool email_enabled = 6;
}
```

---

### o_auth2_config.proto {#o_auth2_config}

**Path**: `gcommon/v1/common/o_auth2_config.proto` **Package**: `gcommon.v1.common` **Lines**: 60

**Messages** (1): `OAuth2Config`

**Imports** (4):

- `gcommon/v1/common/jwt_config.proto`
- `gcommon/v1/common/oauth2_flow_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/o_auth2_config.proto
// version: 1.1.0
// guid: a0b1c2d3-e4f5-6a7b-8c9d-0e1f2a3b4c5d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/jwt_config.proto";
import "gcommon/v1/common/oauth2_flow_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * OAuth2 configuration for authentication providers.
 * Supports various OAuth2 flows and provider configurations.
 */
message OAuth2Config {
  // OAuth2 provider name
  string provider_name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Client ID for OAuth2 application
  string client_id = 2;

  // Client secret for OAuth2 application
  string client_secret = 3;

  // Authorization endpoint URL
  string authorization_endpoint = 4;

  // Token endpoint URL
  string token_endpoint = 5;

  // User info endpoint URL
  string userinfo_endpoint = 6;

  // Redirect URI after authorization
  string redirect_uri = 7 [ (buf.validate.field).string.uri = true ];

  // Requested scopes
  repeated string scopes = 8;

  // OAuth2 flow type
  gcommon.v1.common.OAuth2FlowType flow_type = 9;

  // Additional provider-specific parameters
  map<string, string> additional_params = 10;

  // Whether PKCE is required
  bool require_pkce = 11;

  // JWT configuration for token validation
  JWTConfig jwt_config = 12;
}
```

---

### output_config.proto {#output_config}

**Path**: `gcommon/v1/common/output_config.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `OutputConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/output_config.proto
// version: 1.0.0
// guid: 0ee0198f-adab-435c-b8b9-0d67f7c06af0

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message OutputConfig {
  // Output target (file path, network address, etc.)
  string target = 1 [(buf.validate.field).string.min_len = 1];

  // Additional output options
  map<string, string> options = 2;
}
```

---

### rate_limit_config.proto {#rate_limit_config}

**Path**: `gcommon/v1/common/rate_limit_config.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `AuthRateLimitConfig`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/rate_limit_config.proto
// version: 1.0.0
// guid: 5769fd20-09d6-4038-bf86-8087ee0374a0
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Rate limiting configuration for authentication operations.
 * Used to prevent abuse and enforce security policies.
 * Supports various rate limiting strategies.
 */
message AuthRateLimitConfig {
  // Maximum number of requests allowed
  int32 max_requests = 1 [(buf.validate.field).int32.gte = 0];

  // Time window for rate limiting
  google.protobuf.Duration time_window = 2;

  // Burst allowance (max requests in short burst)
  int32 burst_allowance = 3 [(buf.validate.field).int32.gte = 0];

  // Rate limit scope (per user, per IP, etc.)
  string scope = 4 [(buf.validate.field).string.min_len = 1];

  // Action to take when rate limit is exceeded
  string action = 5; // "block", "delay", "throttle"

  // Rate limit enabled flag
  bool enabled = 6;

  // Rate limit metadata
  map<string, string> metadata = 7 [lazy = true];
}
```

---

### saml_config.proto {#saml_config}

**Path**: `gcommon/v1/common/saml_config.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `SamlConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/saml_config.proto
// version: 1.0.0
// guid: b1088674-0c17-45db-8c6d-3022ce0a629b

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration options for SAML authentication.
 */
message SamlConfig {
  // URL for the identity provider metadata.
  string idp_metadata_url = 1 [ (buf.validate.field).string.uri = true ];

  // Service provider entity ID.
  string sp_entity_id = 2;

  // Service provider assertion consumer service URL.
  string sp_acs_url = 3 [ (buf.validate.field).string.uri = true ];

  // X.509 certificate for the service provider.
  string certificate = 4;

  // Private key for the service provider certificate.
  string private_key = 5;

  // Allowed domains for SAML assertions.
  repeated string allowed_domains = 6;
}
```

---

### session_config.proto {#session_config}

**Path**: `gcommon/v1/common/session_config.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `AuthSessionConfig`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/session_config.proto
// version: 1.0.0
// guid: cf31dcbd-ba1f-402c-a37c-c1a2afe2dba8

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Configuration parameters for user sessions.
 */
message AuthSessionConfig {
  // Idle timeout in seconds before session expiration.
  int32 idle_timeout_seconds = 1;

  // Absolute lifetime of a session in seconds.
  int32 absolute_lifetime_seconds = 2;

  // Whether sessions persist across server restarts.
  bool persist_across_restarts = 3;

  // Name of the session cookie.
  string cookie_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether to mark the cookie as secure.
  bool secure_cookie = 5;
}
```

---

### assign_role_request.proto {#assign_role_request}

**Path**: `gcommon/v1/common/assign_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 59

**Messages** (1): `AssignRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/assign_role_request.proto
// version: 1.1.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to assign a role to a user.
 * Used for role-based access control management.
 * Grants the specified role permissions to the user.
 *
 * Example usage:
 * - Assigning admin role to a user
 * - Granting specific permissions through role assignment
 * - Managing user access control in the system
 */
message AssignRoleRequest {
  // User ID to assign role to (required)
  // Must be a valid user identifier in the system
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID to assign (required)
  // Must be a valid role identifier in the system
  string role_id = 2;

  // Optional organization context for scoped role assignment
  // If not provided, role is assigned globally
  string organization_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Audit information for tracking who made the assignment
  string assigned_by = 5;

  // Reason for role assignment (optional)
  string reason = 6;

  // Whether the assignment should be temporary
  bool temporary = 7;

  // Expiration time for temporary assignments
  int64 expires_at = 8;
}
```

---

### assign_role_response.proto {#assign_role_response}

**Path**: `gcommon/v1/common/assign_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `AssignRoleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/assign_role_response.proto
// version: 1.0.0
// guid: 71268c4b-6cea-4997-9b67-ce60cc72de2b
// file: proto/gcommon/v1/common/assign_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message AssignRoleResponse {
  // Assignment success
  bool success = 1;

  // Error message if assignment failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Effective permissions after assignment
  repeated string effective_permissions = 3 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### authenticate_request.proto {#authenticate_request}

**Path**: `gcommon/v1/common/authenticate_request.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Messages** (1): `AuthAuthenticateRequest`

**Imports** (7):

- `gcommon/v1/common/api_key_credentials.proto`
- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/jwt_credentials.proto`
- `gcommon/v1/common/o_auth2_credentials.proto`
- `gcommon/v1/common/password_credentials.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authenticate_request.proto
// version: 1.0.1
// guid: 3662d31f-ad12-4066-be86-6a74f4e4a884
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key_credentials.proto";
import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/jwt_credentials.proto";
import "gcommon/v1/common/o_auth2_credentials.proto";
import "gcommon/v1/common/password_credentials.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Authentication request supporting multiple credential types.
 * Uses oneof to ensure only one authentication method is provided per request.
 * Supports comprehensive metadata and client information for security and auditing.
 */
message AuthAuthenticateRequest {
  // Request metadata for tracing, correlation, and auditing
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // Authentication credentials (oneof ensures only one type is used)
  oneof credentials {
    // Username/password authentication
    PasswordCredentials password = 2;
    // API key authentication
    APIKeyCredentials api_key = 3;
    // OAuth2 authorization code flow
    OAuth2Credentials oauth2 = 4;
    // JWT bearer token authentication
    JWTCredentials jwt = 5;
  }

  // Requested authorization scopes
  repeated string scopes = 6;

  // Client information for security and session management
  gcommon.v1.common.ClientInfo client_info = 7 [lazy = true];
}
```

---

### authenticate_response.proto {#authenticate_response}

**Path**: `gcommon/v1/common/authenticate_response.proto` **Package**: `gcommon.v1.common` **Lines**: 47

**Messages** (1): `AuthAuthenticateResponse`

**Imports** (5):

- `gcommon/v1/common/rate_limit.proto`
- `gcommon/v1/common/session.proto`
- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authenticate_response.proto
// version: 1.0.0
// guid: c28da8ae-a463-4446-83b2-50a947fd8826
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/rate_limit.proto";
import "gcommon/v1/common/session.proto";
import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Authentication response containing access tokens and user information.
 * Follows OAuth2 token response format with additional session and user data.
 * Includes rate limiting information for client throttling.
 */
message AuthAuthenticateResponse {
  // Access token for API authentication (JWT format)
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // Refresh token for token renewal (opaque format)
  string refresh_token = 2 [(buf.validate.field).string.min_len = 1];

  // Token type (always "Bearer" for OAuth2 compliance)
  string token_type = 3 [(buf.validate.field).string.min_len = 1];

  // Access token expiration time in seconds
  int32 expires_in = 4 [(buf.validate.field).int32.gte = 0];

  // Granted authorization scopes
  repeated string scopes = 5 [(buf.validate.field).repeated.min_items = 1];

  // Complete user information
  UserInfo user_info = 6 [lazy = true];

  // Session information for session management
  Session session = 7 [lazy = true];

  // Rate limiting information for client throttling
  gcommon.v1.common.RateLimit rate_limit = 8 [lazy = true];
}
```

---

### authorize_request.proto {#authorize_request}

**Path**: `gcommon/v1/common/authorize_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `AuthAuthorizeRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authorize_request.proto
// version: 1.0.0
// guid: 06edf238-40f2-4d28-a7dc-0b6a972bf7b2
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to check if a user is authorized for a specific action.
 * Used for fine-grained access control and permission validation.
 * Supports contextual authorization with additional metadata.
 */
message AuthAuthorizeRequest {
  // Access token for the user being authorized
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Resource being accessed (e.g., "user:123", "project:456")
  string resource = 2 [(buf.validate.field).string.min_len = 1];

  // Action being performed (e.g., "read", "write", "delete")
  string action = 3 [(buf.validate.field).string.min_len = 1];

  // Additional context for authorization decision
  map<string, string> context = 4;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 5;
}
```

---

### authorize_response.proto {#authorize_response}

**Path**: `gcommon/v1/common/authorize_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `AuthAuthorizeResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/authorize_response.proto
// version: 1.0.0
// guid: 698cde09-444b-45ef-abbd-239e622ddc4f
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to authorization request.
 * Contains authorization decision and relevant permission information.
 * Includes denial reason if authorization fails.
 */
message AuthAuthorizeResponse {
  // Whether the user is authorized for the requested action
  bool authorized = 1;

  // Permissions that granted this authorization (if any)
  repeated string permissions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Reason for denial if authorization failed
  string denial_reason = 3 [(buf.validate.field).string.min_len = 1];

  // Error information if authorization check failed
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### batch_operation.proto {#batch_operation}

**Path**: `gcommon/v1/common/batch_operation.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `CommonBatchOperation`

**Imports** (5):

- `buf/validate/validate.proto`
- `gcommon/v1/common/batch_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/any.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/batch_operation.proto
// version: 1.0.1
// guid: 5671d63f-77bd-4415-a7ec-3c22d3557b37
edition = "2023";

package gcommon.v1.common;

import "buf/validate/validate.proto";
import "gcommon/v1/common/batch_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/any.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Batch operation wrapper for bulk request processing.
 * Enables efficient processing of multiple operations with
 * configurable parallelism, error handling, and timeout policies.
 */
message CommonBatchOperation {
  // Unique identifier for this batch operation
  string batch_id = 1 [(buf.validate.field).string.min_len = 1];

  // Type of operation being performed in batch
  string operation_type = 2 [(buf.validate.field).string.min_len = 1];

  // Individual operations within the batch (type-specific)
  repeated google.protobuf.Any operations = 3 [
    lazy = true,
    (buf.validate.field).repeated.min_items = 1
  ];

  // Batch processing configuration options
  CommonBatchOptions options = 4 [lazy = true];

  // Request metadata for tracing and correlation
  RequestMetadata metadata = 5 [lazy = true];
}
```

---

### batch_options.proto {#batch_options}

**Path**: `gcommon/v1/common/batch_options.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `CommonBatchOptions`

**Imports** (3):

- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/batch_options.proto
// version: 1.0.0
// guid: 66c5dc7e-add8-44b2-8bde-bf1845acbd3f
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Batch processing options for configuring bulk operation behavior.
 * Controls parallelism, error handling, timeout policies, and
 * result handling for efficient batch processing.
 */
message CommonBatchOptions {
  // Maximum number of operations to process in parallel
  int32 max_parallel = 1 [(buf.validate.field).int32.gte = 0];

  // Whether to stop processing on the first error encountered
  bool fail_fast = 2;

  // Total timeout for the entire batch operation
  google.protobuf.Duration timeout = 3;

  // Whether to return partial results if timeout is reached
  bool return_partial = 4;
}
```

---

### change_password_request.proto {#change_password_request}

**Path**: `gcommon/v1/common/change_password_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `ChangePasswordRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/change_password_request.proto
// version: 1.0.0
// guid: a3ff57ec-81fd-4ed4-89ab-1d804175aabd
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to change user password (authenticated).
 * Requires current password for security validation.
 * Used for authenticated password change operations.
 */
message ChangePasswordRequest {
  // Current password for verification
  string current_password = 1 [(buf.validate.field).string.min_len = 8];

  // New password to set
  string new_password = 2 [(buf.validate.field).string.min_len = 8];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### change_password_response.proto {#change_password_response}

**Path**: `gcommon/v1/common/change_password_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ChangePasswordResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/change_password_response.proto
// version: 1.0.0
// guid: 0b8b2b05-a63d-43c6-abd4-49e3fb0c7409
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to password change request.
 * Contains confirmation of password change and any relevant metadata.
 * Provides feedback to the user about the operation status.
 */
message ChangePasswordResponse {
  // Whether the password change was successful
  bool success = 1;

  // Confirmation message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if password change failed
  gcommon.v1.common.Error error = 3 [lazy = true];

  // Whether all existing sessions should be terminated
  bool sessions_terminated = 4;

  // Number of sessions that were terminated
  int32 terminated_session_count = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### check_permission_request.proto {#check_permission_request}

**Path**: `gcommon/v1/common/check_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `CheckPermissionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_permission_request.proto
// version: 1.0.0
// guid: db7aca7d-742a-443b-b641-448ddf4a8518

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to verify that a user possesses a specific permission.
 */
message CheckPermissionRequest {
  // Metadata for tracing and audit purposes
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // User ID being verified
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Permission ID to check
  string permission_id = 3;
}
```

---

### check_permission_response.proto {#check_permission_response}

**Path**: `gcommon/v1/common/check_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `CheckPermissionResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/check_permission_response.proto
// version: 1.0.1
// guid: 909a647b-cd2d-44d1-b612-5ea1e54bda39

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response indicating whether the user has the requested permission.
 */
message CheckPermissionResponse {
  // True if the user possesses the permission
  bool allowed = 1;
}
```

---

### complete_password_reset_request.proto {#complete_password_reset_request}

**Path**: `gcommon/v1/common/complete_password_reset_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `CompletePasswordResetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/complete_password_reset_request.proto
// version: 1.0.0
// guid: 66afc3ec-b304-45c8-ad75-7dff63410987
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to complete password reset with token.
 * Validates reset token and sets new password.
 * Completes the password recovery flow.
 */
message CompletePasswordResetRequest {
  // Password reset token from initiate request
  string reset_token = 1 [(buf.validate.field).string.min_len = 1];

  // New password to set
  string new_password = 2 [(buf.validate.field).string.min_len = 8];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### complete_password_reset_response.proto {#complete_password_reset_response}

**Path**: `gcommon/v1/common/complete_password_reset_response.proto` **Package**: `gcommon.v1.common` **Lines**: 50

**Messages** (1): `CompletePasswordResetResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/complete_password_reset_response.proto
// version: 1.0.0
// guid: abe29553-64dd-4743-bf15-c3f35155de70
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * CompletePasswordResetResponse confirms successful password reset completion.
 * Provides confirmation and security information about the password reset
 * operation for audit logging and user notification.
 */
message CompletePasswordResetResponse {
  // User ID whose password was reset
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username or email of the user
  string username = 2;

  // Timestamp when the password was successfully reset
  google.protobuf.Timestamp reset_completed_at = 3;

  // Whether all existing sessions were terminated
  bool sessions_terminated = 4;

  // Number of sessions that were terminated
  int32 terminated_session_count = 5;

  // Whether all tokens for this user were revoked
  bool tokens_revoked = 6;

  // Number of tokens that were revoked
  int32 revoked_token_count = 7;

  // Security notice: next login will require additional verification
  bool requires_additional_verification = 8;

  // Success message for user display
  string message = 9;
}
```

---

### create_permission_request.proto {#create_permission_request}

**Path**: `gcommon/v1/common/create_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `CreatePermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/create_permission_request.proto
// version: 1.0.0
// guid: dee162c4-dfc6-4ebf-94f8-7f7871349e23
// file: proto/gcommon/v1/common/create_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message CreatePermissionRequest {
  // Permission name
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Permission description
  string description = 2 [ (buf.validate.field).string.max_len = 1000 ];

  // Actions this permission grants
  repeated string actions = 3;

  // Resources this permission applies to
  repeated string resources = 4;
}
```

---

### create_role_request.proto {#create_role_request}

**Path**: `gcommon/v1/common/create_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `CreateRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_role_request.proto
// version: 1.0.1
// guid: f08ba415-9259-4f93-a889-7405b082f9cd
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to create a new role.
 * Used for role management and access control setup.
 * Creates a role with specified permissions and metadata.
 */
message CreateRoleRequest {
  // Role data to create
  Role role = 1;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### create_role_response.proto {#create_role_response}

**Path**: `gcommon/v1/common/create_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `CreateRoleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/create_role_response.proto
// file: proto/gcommon/v1/common/create_role_response.proto
// version: 1.0.1
// guid: 345e6789-a1b2-3c4d-5e6f-7a8b9c0d1e2f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for creating a new role.
 * Returns the created role with its assigned ID.
 */
message CreateRoleResponse {
  // The created role
  Role role = 1;

  // Error information if creation failed
  gcommon.v1.common.Error error = 2;
}
```

---

### create_session_request.proto {#create_session_request}

**Path**: `gcommon/v1/common/create_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Messages** (1): `AuthCreateSessionRequest`

**Imports** (4):

- `gcommon/v1/common/client_info.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_session_request.proto
// version: 1.0.0
// guid: 4e2786c7-f3d0-442e-bb3b-c88772e7aece
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/client_info.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to create a new user session.
 * Used after successful authentication to establish a session
 * with specific duration and metadata tracking.
 */
message AuthCreateSessionRequest {
  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];

  // User ID for which to create the session
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Client information for session tracking
  gcommon.v1.common.ClientInfo client_info = 3 [lazy = true];

  // Session duration in seconds (0 for system default)
  int32 duration_seconds = 4;

  // Additional session metadata
  map<string, string> session_metadata = 5 [lazy = true];
}
```

---

### create_session_response.proto {#create_session_response}

**Path**: `gcommon/v1/common/create_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 39

**Messages** (1): `AuthCreateSessionResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_session_response.proto
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-1234-567890abcdef

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for session creation operations.
 * Contains session token, expiration details, and user context.
 */
message AuthCreateSessionResponse {
  // Standard response metadata
  gcommon.v1.common.ResponseMetadata metadata = 1;

  // Created session details
  string session_id = 2;
  string access_token = 3;
  string refresh_token = 4;
  google.protobuf.Timestamp expires_at = 5;
  google.protobuf.Timestamp refresh_expires_at = 6;

  // User context
  string user_id = 7 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
  repeated string roles = 8;
  repeated string permissions = 9;
}
```

---

### create_user_request.proto {#create_user_request}

**Path**: `gcommon/v1/common/create_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `CreateUserRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174001

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to create a new user account.
 */
message CreateUserRequest {
  // Username for the new account
  string username = 1;

  // Email address for the new account
  string email = 2 [ (buf.validate.field).string.email = true ];

  // Password for the new account (should be hashed)
  string password = 3;

  // Full name of the user
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account should be enabled immediately
  bool enabled = 5;

  // Initial roles to assign to the user
  repeated string roles = 6;

  // Additional metadata for the user
  map<string, string> metadata = 7;

  // Whether to require email verification
  bool require_email_verification = 8;

  // Account expiration time (optional)
  google.protobuf.Timestamp expires_at = 9;
}
```

---

### create_user_response.proto {#create_user_response}

**Path**: `gcommon/v1/common/create_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 55

**Messages** (1): `CreateUserResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/create_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174002

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for creating a new user account.
 */
message CreateUserResponse {
  // Unique identifier for the created user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username of the created account
  string username = 2;

  // Email address of the created account
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Full name of the user
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account is enabled
  bool enabled = 5;

  // Assigned roles
  repeated string roles = 6;

  // When the account was created
  google.protobuf.Timestamp created_at = 7 [ (buf.validate.field).required = true ];

  // Whether email verification is required
  bool email_verification_required = 8;

  // Email verification token (if required)
  string verification_token = 9;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 10;
}
```

---

### delete_notification_request.proto {#delete_notification_request}

**Path**: `gcommon/v1/common/delete_notification_request.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `DeleteNotificationRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_notification_request.proto
// version: 1.0.0
// guid: 20a32413-3de3-416f-a3ad-23c2172121c9

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeleteNotificationRequest {
  // Identifier of the notification to delete.
  string notification_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### delete_notification_response.proto {#delete_notification_response}

**Path**: `gcommon/v1/common/delete_notification_response.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `DeleteNotificationResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_notification_response.proto
// version: 1.0.1
// guid: d7f015d6-70a1-4fcd-82b3-560a134d7a45

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response after deleting a notification.
 */
message DeleteNotificationResponse {
  // True if the deletion succeeded.
  bool success = 1;
}
```

---

### delete_permission_request.proto {#delete_permission_request}

**Path**: `gcommon/v1/common/delete_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `DeletePermissionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_permission_request.proto
// version: 1.0.0
// guid: e40a5914-c7d8-41e0-bb7d-07495308e638
// file: proto/gcommon/v1/common/delete_permission_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeletePermissionRequest {
  // Permission ID to delete
  string permission_id = 1 [(buf.validate.field).string.min_len = 1];

  // Force deletion even if assigned
  bool force = 2;
}
```

---

### delete_role_request.proto {#delete_role_request}

**Path**: `gcommon/v1/common/delete_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeleteRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_role_request.proto
// version: 1.0.0
// guid: c6fef1ce-1633-4607-967d-1b42b93dcf8c
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to delete a role.
 * Used for role management and cleanup.
 * Role must not be assigned to any users before deletion.
 */
message DeleteRoleRequest {
  // Role ID to delete
  string role_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### delete_role_response.proto {#delete_role_response}

**Path**: `gcommon/v1/common/delete_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeleteRoleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_role_response.proto
// version: 1.0.0
// guid: d7a5181a-727d-4f09-85fb-70407122b1eb
// file: proto/gcommon/v1/common/delete_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeleteRoleResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Number of users/entities that lost this role
  int32 affected_subjects = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### delete_session_request.proto {#delete_session_request}

**Path**: `gcommon/v1/common/delete_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `AuthDeleteSessionRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_session_request.proto
// version: 1.0.0
// guid: 81f54c30-c375-4c15-a847-2a7296c9741c
// file: proto/gcommon/v1/common/delete_session_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to delete a session.
 * Used for session cleanup and administrative purposes.
 */
message AuthDeleteSessionRequest {
  // Session ID to delete
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // Force delete even if session is active (admin only)
  bool force = 2;
}
```

---

### delete_session_response.proto {#delete_session_response}

**Path**: `gcommon/v1/common/delete_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `AuthDeleteSessionResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_session_response.proto
// version: 1.0.1
// guid: e99771c5-4060-4cd9-a8f5-7919d9b8cb61
// file: proto/gcommon/v1/common/delete_session_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for session deletion request.
 * Confirms successful deletion or provides error information.
 */
message AuthDeleteSessionResponse {
  // Whether the session was successfully deleted
  bool deleted = 1;

  // Error information if deletion failed
  gcommon.v1.common.Error error = 2;
}
```

---

### delete_user_request.proto {#delete_user_request}

**Path**: `gcommon/v1/common/delete_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `DeleteUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/delete_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174003

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to delete a user account.
 */
message DeleteUserRequest {
  // Unique identifier of the user to delete
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Whether to perform a soft delete (mark as deleted) or hard delete
  bool soft_delete = 2;

  // Reason for deletion (optional, for audit purposes)
  string reason = 3;

  // Whether to transfer ownership of resources to another user
  string transfer_to_user_id = 4;

  // Whether to immediately revoke all active sessions
  bool revoke_sessions = 5;
}
```

---

### delete_user_response.proto {#delete_user_response}

**Path**: `gcommon/v1/common/delete_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DeleteUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/delete_user_response.proto
// version: 1.0.0
// guid: 1c98d374-f744-4078-bb80-826832a42620
// file: proto/gcommon/v1/common/delete_user_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DeleteUserResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Data retention information
  string data_retention_info = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### disable2_fa_request.proto {#disable2_fa_request}

**Path**: `gcommon/v1/common/disable2_fa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `Disable2FaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable2_fa_request.proto
// version: 1.0.0
// guid: 00c046b6-37b9-4a79-a9a4-05f73d7c0d7f
// file: proto/gcommon/v1/common/disable2_fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Disable2FaRequest {
  // User ID requesting 2FA disable
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Current password for verification
  string password = 2;

  // 2FA code for verification
  string verification_code = 3;
}
```

---

### disable_check_request.proto {#disable_check_request}

**Path**: `gcommon/v1/common/disable_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `DisableCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable_check_request.proto
// version: 1.0.0
// guid: 57c84c2e-3f48-4a3d-a2c3-a910d1956773
// file: proto/gcommon/v1/common/disable_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DisableCheckRequest {
  // Name or ID of the check to disable
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### disable_check_response.proto {#disable_check_response}

**Path**: `gcommon/v1/common/disable_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `DisableCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/disable_check_response.proto
// version: 1.0.0
// guid: 0cba0a9a-f486-48cc-b449-1245a11558c4
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for disabling a health check.
 * Contains the result of disabling an active check.
 */
message DisableCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was disabled
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if disabling failed
  gcommon.v1.common.Error error = 3;

  // Reason for disabling (if provided)
  string reason = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### disable_mfa_request.proto {#disable_mfa_request}

**Path**: `gcommon/v1/common/disable_mfa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `DisableMfaRequest`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable_mfa_request.proto
// version: 1.0.0
// guid: 69fe90b5-14de-44b2-a3dc-8768c27f6617
// file: proto/gcommon/v1/common/disable_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DisableMfaRequest {
  // User ID requesting MFA disable
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Current password for verification
  string password = 2;

  // MFA verification code
  string verification_code = 3;

  // Specific methods to disable (empty = all)
  repeated gcommon.v1.common.MfaMethod methods = 4;
}
```

---

### disable_mfa_response.proto {#disable_mfa_response}

**Path**: `gcommon/v1/common/disable_mfa_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `DisableMfaResponse`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/disable_mfa_response.proto
// version: 1.0.0
// guid: 8fa6daf5-aee9-414d-95a0-ed59c3c11334
// file: proto/gcommon/v1/common/disable_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message DisableMfaResponse {
  // Success status
  bool success = 1;

  // Methods that were disabled
  repeated gcommon.v1.common.MfaMethod disabled_methods = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error message if operation failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### enable2_fa_request.proto {#enable2_fa_request}

**Path**: `gcommon/v1/common/enable2_fa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `Enable2FaRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/enable2_fa_request.proto
// version: 1.0.0
// guid: 2f270251-6e96-4864-9c75-1e9a381549d6
// file: proto/gcommon/v1/common/enable2_fa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Enable2FaRequest {
  // User ID requesting 2FA enablement
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Phone number for SMS-based 2FA
  string phone_number = 2;

  // Whether to use authenticator app
  bool use_authenticator = 3;

  // Backup codes preference
  bool generate_backup_codes = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### enable_check_request.proto {#enable_check_request}

**Path**: `gcommon/v1/common/enable_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `EnableCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/enable_check_request.proto
// version: 1.0.0
// guid: 0377eaa7-a0d8-46c3-b427-2743c1062111
// file: proto/gcommon/v1/common/enable_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EnableCheckRequest {
  // Name or ID of the check to enable
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### enable_check_response.proto {#enable_check_response}

**Path**: `gcommon/v1/common/enable_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `EnableCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/enable_check_response.proto
// version: 1.0.0
// guid: e785b271-7a1a-42e8-add6-deda8ce9f5b1
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for enabling a health check.
 * Contains the result of enabling a previously disabled check.
 */
message EnableCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was enabled
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if enabling failed
  gcommon.v1.common.Error error = 3;

  // Check status after enabling
  string status = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### enable_mfa_request.proto {#enable_mfa_request}

**Path**: `gcommon/v1/common/enable_mfa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `EnableMfaRequest`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/enable_mfa_request.proto
// version: 1.0.0
// guid: 1277fc9b-bcd3-49c3-9c5d-2596a743c594
// file: proto/gcommon/v1/common/enable_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EnableMfaRequest {
  // User ID requesting MFA enablement
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // MFA methods to enable
  repeated gcommon.v1.common.MfaMethod methods = 2;

  // Primary contact method
  string primary_contact = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### enable_mfa_response.proto {#enable_mfa_response}

**Path**: `gcommon/v1/common/enable_mfa_response.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `EnableMfaResponse`

**Imports** (3):

- `gcommon/v1/common/mfa_setup_instruction.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/enable_mfa_response.proto
// version: 1.0.0
// guid: 7fe3c97f-1a88-419f-b2f9-9f699a13b78c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_setup_instruction.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message EnableMfaResponse {
  // Success status
  bool success = 1;

  // Setup instructions for each method
  repeated MfaSetupInstruction setup_instructions = 2 [(buf.validate.field).repeated.min_items = 1];

  // Error message if operation failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### generate_api_key_request.proto {#generate_api_key_request}

**Path**: `gcommon/v1/common/generate_api_key_request.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `GenerateAPIKeyRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/generate_api_key_request.proto
// version: 1.0.0
// guid: 5590365e-02f0-4a3d-96eb-15bc615c14ef

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GenerateAPIKeyRequest requests creation of a new API key for a user.
 */
message GenerateAPIKeyRequest {
  // User ID for whom to generate the key
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional name/description for the key
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Optional expiration in seconds
  int32 expires_in = 3;

  // Metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### generate_api_key_response.proto {#generate_api_key_response}

**Path**: `gcommon/v1/common/generate_api_key_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GenerateAPIKeyResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/generate_api_key_response.proto
// version: 1.0.0
// guid: 026770a4-919a-4111-818f-ab932e8523ea

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * GenerateAPIKeyResponse returns the newly created API key.
 */
message GenerateAPIKeyResponse {
  // Generated API key value
  string key = 1 [(buf.validate.field).string.min_len = 1];

  // Optional key identifier
  string key_id = 2 [(buf.validate.field).string.min_len = 1];

  // Response metadata for rate limiting and tracing
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### get_api_key_request.proto {#get_api_key_request}

**Path**: `gcommon/v1/common/get_api_key_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetApiKeyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_api_key_request.proto
// version: 1.0.0
// guid: 942d4a7c-b73d-43e7-a95d-bcd51091d1be
// file: proto/gcommon/v1/common/get_api_key_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetApiKeyRequest {
  // API key ID
  string key_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include usage statistics
  bool include_stats = 2;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### get_api_key_response.proto {#get_api_key_response}

**Path**: `gcommon/v1/common/get_api_key_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `GetApiKeyResponse`

**Imports** (4):

- `gcommon/v1/common/api_key.proto`
- `gcommon/v1/common/api_key_stats.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_api_key_response.proto
// version: 1.0.0
// guid: 584574e5-3a49-4346-ada5-78a7454f921e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key.proto";
import "gcommon/v1/common/api_key_stats.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetApiKeyResponse {
  // API key details
  gcommon.v1.common.APIKey api_key = 1;

  // Usage statistics if requested
  gcommon.v1.common.ApiKeyStats stats = 2;

  // Error message if not found
  string error_message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### get_check_status_request.proto {#get_check_status_request}

**Path**: `gcommon/v1/common/get_check_status_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetCheckStatusRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_check_status_request.proto
// version: 1.0.0
// guid: b22eabcb-b556-4dd9-bd5b-4016956b8e69
// file: proto/gcommon/v1/common/get_check_status_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetCheckStatusRequest {
  // Name or ID of the check
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_health_history_request.proto {#get_health_history_request}

**Path**: `gcommon/v1/common/get_health_history_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `GetHealthHistoryRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_health_history_request.proto
// version: 1.0.0
// guid: b0eb3b6a-e7f2-454f-addf-e8c9a9d2313a
// file: proto/gcommon/v1/common/get_health_history_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthHistoryRequest {
  // Service name to query
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Optional start time for history records
  google.protobuf.Timestamp start_time = 2;

  // Optional end time for history records
  google.protobuf.Timestamp end_time = 3;

  // Request metadata for authentication and tracing
  gcommon.v1.common.RequestMetadata metadata = 4 [lazy = true];
}
```

---

### get_health_metrics_request.proto {#get_health_metrics_request}

**Path**: `gcommon/v1/common/get_health_metrics_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `GetHealthMetricsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_health_metrics_request.proto
// version: 1.0.0
// guid: 85ebb0e8-dd6f-4a2d-9e83-386b9d84d776
// file: proto/gcommon/v1/common/get_health_metrics_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthMetricsRequest {
  // Service name (optional)
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata used for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_health_metrics_response.proto {#get_health_metrics_response}

**Path**: `gcommon/v1/common/get_health_metrics_response.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `GetHealthMetricsResponse`

**Imports** (4):

- `gcommon/v1/common/health_metric_data.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_health_metrics_response.proto
// version: 1.0.0
// guid: 53811a7b-91b9-44c9-8045-42ff44f502c2

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_metric_data.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthMetricsResponse {
  // Health metrics data
  repeated HealthMetricData metrics = 1 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_health_request.proto {#get_health_request}

**Path**: `gcommon/v1/common/get_health_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `GetHealthRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_health_request.proto
// version: 1.0.0
// guid: 9c9295ed-ade9-4dd4-843c-f8f78a380b7f
// file: proto/gcommon/v1/common/get_health_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetHealthRequest {
  // Service name to query
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to include detailed check results
  bool include_details = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### get_permission_request.proto {#get_permission_request}

**Path**: `gcommon/v1/common/get_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `GetPermissionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_permission_request.proto
// version: 1.0.0
// guid: 0658829b-708a-480e-942d-42b7ce0e4fdd

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to fetch details about a permission entry.
 */
message GetPermissionRequest {
  // Permission identifier
  string permission_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_permission_response.proto {#get_permission_response}

**Path**: `gcommon/v1/common/get_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetPermissionResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/permission.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_permission_response.proto
// version: 1.0.1
// guid: fabb3420-290d-4f58-8be9-b363ef1adefd

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/permission.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for a permission retrieval request.
 */
message GetPermissionResponse {
  // Permission details if found
  Permission permission = 1 [lazy = true];

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2 [lazy = true];
}
```

---

### get_preferences_request.proto {#get_preferences_request}

**Path**: `gcommon/v1/common/get_preferences_request.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetPreferencesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_preferences_request.proto
// version: 1.0.0
// guid: fb16c45a-545c-4d05-b3fd-34dbc4a9d0c1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetPreferencesRequest {
  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Identifier for the user whose preferences are being requested.
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}
```

---

### get_preferences_response.proto {#get_preferences_response}

**Path**: `gcommon/v1/common/get_preferences_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetPreferencesResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/common/subscription_preferences.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_preferences_response.proto
// version: 1.0.1
// guid: 3c2f540d-f827-4df1-9afe-6f31f6d73dd9

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/common/subscription_preferences.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

### get_role_request.proto {#get_role_request}

**Path**: `gcommon/v1/common/get_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_role_request.proto
// version: 1.0.0
// guid: 554e7499-0070-40fe-a99c-3428bec2651f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to retrieve details about a specific role.
 */
message GetRoleRequest {
  // Unique identifier of the role
  string role_id = 1 [(buf.validate.field).string.min_len = 1];

  // Include permissions in the response
  bool include_permissions = 2;

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### get_role_response.proto {#get_role_response}

**Path**: `gcommon/v1/common/get_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetRoleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_role_response.proto
// version: 1.0.1
// guid: 4da329f9-4bb7-4695-85e7-a7083ae930e1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing role information or an error.
 */
message GetRoleResponse {
  // Role details if found
  Role role = 1 [lazy = true];

  // Error information if retrieval failed
  gcommon.v1.common.Error error = 2 [lazy = true];
}
```

---

### get_session_request.proto {#get_session_request}

**Path**: `gcommon/v1/common/get_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `AuthGetSessionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_session_request.proto
// version: 1.1.0
// guid: d3e4f5a6-b7c8-9d0e-1f2a-3b4c5d6e7f8a

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get session information.
 * Used to retrieve detailed session data by session ID.
 * Provides session status, metadata, and activity information.
 */
message AuthGetSessionRequest {
  // Session ID to retrieve (required)
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether to include detailed session activity
  bool include_activity = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### get_session_response.proto {#get_session_response}

**Path**: `gcommon/v1/common/get_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `AuthGetSessionResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/session.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/get_session_response.proto
// version: 1.0.1
// guid: e2dfbf3c-a64b-4e03-8728-bb79288e0998
// file: proto/gcommon/v1/common/get_session_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/session.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for getting session information.
 * Contains session details if found, or error information if not found.
 */
message AuthGetSessionResponse {
  // Session information if found
  Session session = 1;

  // Error information if session not found or access denied
  gcommon.v1.common.Error error = 2;
}
```

---

### get_system_stats_request.proto {#get_system_stats_request}

**Path**: `gcommon/v1/common/get_system_stats_request.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `GetSystemStatsRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_system_stats_request.proto
// version: 1.0.1
// guid: 789eabcd-e1f2-3a4b-5c6d-7e8f9a0b1c2d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get authentication system statistics.
 */
message GetSystemStatsRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1 [lazy = true];
}
```

---

### get_system_stats_response.proto {#get_system_stats_response}

**Path**: `gcommon/v1/common/get_system_stats_response.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `GetSystemStatsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_system_stats_response.proto
// version: 1.0.0
// guid: 8a9ebcde-f1a2-3b4c-5d6e-7f8a9b0c1d2e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing authentication system statistics.
 */
message GetSystemStatsResponse {
  // Total number of active users
  int64 active_users = 1 [(buf.validate.field).int64.gte = 0];

  // Total number of roles
  int64 total_roles = 2 [(buf.validate.field).int64.gte = 0];

  // Total number of active sessions
  int64 active_sessions = 3 [(buf.validate.field).int64.gte = 0];

  // Total number of failed login attempts (last 24h)
  int64 failed_logins = 4 [(buf.validate.field).int64.gte = 0];

  // Authentication system uptime in seconds
  int64 uptime_seconds = 5 [(buf.validate.field).int64.gte = 0];

  // Error information if stats retrieval failed
  gcommon.v1.common.Error error = 6;
}
```

---

### get_template_request.proto {#get_template_request}

**Path**: `gcommon/v1/common/get_template_request.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetTemplateRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_template_request.proto
// version: 1.0.0
// guid: 4b8dae31-438b-4407-8f5e-25e99ebd347b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetTemplateRequest {
  // Template identifier to fetch
  string id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### get_template_response.proto {#get_template_response}

**Path**: `gcommon/v1/common/get_template_response.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `GetTemplateResponse`

**Imports** (2):

- `gcommon/v1/common/template.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_template_response.proto
// version: 1.2.1
// guid: 525e0a4f-3e9f-4b1a-8d33-fa9c295964a0

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/template.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a requested notification template.
 */
message GetTemplateResponse {
  // Template data
  gcommon.v1.common.Template template = 1 [lazy = true];
}
```

---

### get_user_info_request.proto {#get_user_info_request}

**Path**: `gcommon/v1/common/get_user_info_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `GetUserInfoRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_info_request.proto
// version: 1.0.0
// guid: 43e29c52-26b2-4a16-899e-5eb46029783d
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get user information from a valid token.
 * Extracts user profile data from an authenticated session.
 * Used for user profile display and authorization decisions.
 */
message GetUserInfoRequest {
  // Access token to extract user info from
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_user_info_response.proto {#get_user_info_response}

**Path**: `gcommon/v1/common/get_user_info_response.proto` **Package**: `gcommon.v1.common` **Lines**: 25

**Messages** (1): `GetUserInfoResponse`

**Imports** (2):

- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_info_response.proto
// version: 1.0.1
// guid: b6270468-8ca0-4f87-9843-2528bd262254
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing user information from token validation.
 * Provides comprehensive user profile and metadata.
 * Used for user profile display and application authorization.
 */
message GetUserInfoResponse {
  // Complete user information
  UserInfo user_info = 1;

  // Additional user attributes/metadata
  map<string, string> attributes = 2 [lazy = true];
}
```

---

### get_user_permissions_request.proto {#get_user_permissions_request}

**Path**: `gcommon/v1/common/get_user_permissions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetUserPermissionsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_permissions_request.proto
// version: 1.0.0
// guid: 38097153-2bce-47ac-ab8a-20605ee39939
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get all permissions for a user.
 * Returns direct permissions and role-based permissions.
 * Used for user permission auditing and UI authorization.
 */
message GetUserPermissionsRequest {
  // User ID to get permissions for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_user_permissions_response.proto {#get_user_permissions_response}

**Path**: `gcommon/v1/common/get_user_permissions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `GetUserPermissionsResponse`

**Imports** (3):

- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_permissions_response.proto
// version: 1.0.1
// guid: 732b72be-148e-459b-861f-220b83fc9903
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing all permissions for a user.
 * Includes direct permissions, role-based permissions, and effective permissions.
 * Provides comprehensive permission information for authorization decisions.
 */
message GetUserPermissionsResponse {
  // Direct permissions assigned to the user
  repeated string permissions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Permissions inherited from roles
  repeated string role_permissions = 2 [(buf.validate.field).repeated.min_items = 1];

  // All effective permissions (union of direct and role permissions)
  repeated string effective_permissions = 3 [(buf.validate.field).repeated.min_items = 1];

  // User's roles (includes permission details)
  repeated Role roles = 4 [lazy = true, (buf.validate.field).repeated.min_items = 1];
}
```

---

### get_user_request.proto {#get_user_request}

**Path**: `gcommon/v1/common/get_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `GetUserRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174008

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get a specific user's details.
 */
message GetUserRequest {
  // Unique identifier of the user to retrieve
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Include detailed information (roles, permissions, etc.)
  bool include_details = 2;

  // Include deleted users in search
  bool include_deleted = 3;

  // Specific fields to return (if empty, all fields returned)
  repeated string fields = 4;
}
```

---

### get_user_response.proto {#get_user_response}

**Path**: `gcommon/v1/common/get_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `GetUserResponse`

**Imports** (2):

- `gcommon/v1/common/user_details.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_response.proto
// version: 1.0.1
// guid: 3c135848-65ac-40ed-9e96-bab2045c4997

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_details.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetUserResponse {
  // User details
  gcommon.v1.common.UserDetails user = 1;

  // Whether the user was found
  bool found = 2;
}
```

---

### get_user_roles_request.proto {#get_user_roles_request}

**Path**: `gcommon/v1/common/get_user_roles_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetUserRolesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_roles_request.proto
// version: 1.0.0
// guid: b97cd079-474d-492b-a33e-8c35d42c445a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to get all roles assigned to a user.
 * Used for user role management and authorization decisions.
 * Returns detailed role information including permissions.
 */
message GetUserRolesRequest {
  // User ID to get roles for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_user_roles_response.proto {#get_user_roles_response}

**Path**: `gcommon/v1/common/get_user_roles_response.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `GetUserRolesResponse`

**Imports** (3):

- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_user_roles_response.proto
// version: 1.0.0
// guid: c8a7e641-1fb8-46ee-9491-d3612c2c2400
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing all roles assigned to a user.
 * Provides complete role information including permissions and metadata.
 * Used for role management and authorization display.
 */
message GetUserRolesResponse {
  // All roles assigned to the user
  repeated Role roles = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### grant_permission_request.proto {#grant_permission_request}

**Path**: `gcommon/v1/common/grant_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `GrantPermissionRequest`

**Imports** (3):

- `gcommon/v1/common/subject_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/grant_permission_request.proto
// version: 1.0.0
// guid: f01c2811-f92f-4582-bfca-c77c277c3e12

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/subject_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GrantPermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subject type
  AuthSubjectType subject_type = 2;

  // Permission ID to grant
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### grant_permission_response.proto {#grant_permission_response}

**Path**: `gcommon/v1/common/grant_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `GrantPermissionResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/grant_permission_response.proto
// version: 1.0.0
// guid: e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for permission grant operations.
 * Indicates whether the permission was successfully granted.
 */
message GrantPermissionResponse {
  // Whether the permission grant was successful
  bool success = 1;

  // Error message if grant failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // The granted permission ID
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];

  // User or entity the permission was granted to
  string grantee_id = 4 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}
```

---

### health_check_all_request.proto {#health_check_all_request}

**Path**: `gcommon/v1/common/health_check_all_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `HealthCheckAllRequest`

**Imports** (3):

- `gcommon/v1/common/check_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_all_request.proto
// version: 1.0.0
// guid: 6e150288-20ca-4892-9582-6ca93070073b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthCheckAllRequest requests health status for all services or filtered by type
 */
message HealthCheckAllRequest {
  // Optional filter by check types
  repeated gcommon.v1.common.CheckType types = 1 [(buf.validate.field).repeated.min_items = 1];
  // Whether to include detailed component information
  bool include_details = 2;
  // Timeout for the overall check in seconds
  int32 timeout_seconds = 3 [(buf.validate.field).int32.gt = 0];
}
```

---

### health_check_all_response.proto {#health_check_all_response}

**Path**: `gcommon/v1/common/health_check_all_response.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `HealthCheckAllResponse`

**Imports** (4):

- `gcommon/v1/common/health_check_result.proto`
- `gcommon/v1/common/serving_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_all_response.proto
// version: 1.0.0
// guid: 64089a6a-9c0e-43db-a038-6e271809004e
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_check_result.proto";
import "gcommon/v1/common/serving_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * HealthCheckAllResponse contains comprehensive health information for all services
 */
message HealthCheckAllResponse {
  // Overall system status
  ServingStatus overall_status = 1;
  // Individual service health results
  repeated HealthHealthCheckResult results = 2 [(buf.validate.field).repeated.min_items = 1];
  // Total number of services checked
  int32 total_services = 3 [(buf.validate.field).int32.gte = 0];
  // Number of healthy services
  int32 healthy_services = 4 [(buf.validate.field).int32.gte = 0];
  // Number of unhealthy services
  int32 unhealthy_services = 5 [(buf.validate.field).int32.gte = 0];
  // Total check duration in milliseconds
  int64 total_duration_ms = 6 [(buf.validate.field).int64.gt = 0];
  // Timestamp when the check was completed
  int64 timestamp = 7;
}
```

---

### health_check_request.proto {#health_check_request}

**Path**: `gcommon/v1/common/health_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `HealthHealthCheckRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_request.proto
// version: 1.0.0
// guid: f260a75e-1b70-48df-a829-d4d53e277a16
//
// Health check request message definition
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message HealthHealthCheckRequest {
  // Service name to check (empty for overall health)
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;

  // Check timeout
  google.protobuf.Duration timeout = 3;

  // Include detailed check results
  bool include_details = 4;
}
```

---

### health_check_response.proto {#health_check_response}

**Path**: `gcommon/v1/common/health_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 49

**Messages** (1): `HealthHealthCheckResponse`

**Imports** (8):

- `gcommon/v1/common/check_result.proto`
- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_metrics.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/health_check_response.proto
// version: 1.0.0
// guid: 2276a26b-e231-4da7-86b6-3cf35110b85f
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_result.proto";
import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_metrics.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for health check operations.
 * Contains comprehensive health status information including detailed results and metrics.
 */
message HealthHealthCheckResponse {
  // Overall health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Service name
  string service = 2 [(buf.validate.field).string.min_len = 1];

  // Check timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Response time
  google.protobuf.Duration response_time = 4;

  // Detailed check results
  repeated CheckResult check_results = 5 [(buf.validate.field).repeated.min_items = 1];

  // Health message
  string message = 6 [(buf.validate.field).string.min_len = 1];

  // Error information if unhealthy
  gcommon.v1.common.Error error = 7;

  // Health metrics
  HealthMetrics metrics = 8;
}
```

---

### initiate_password_reset_request.proto {#initiate_password_reset_request}

**Path**: `gcommon/v1/common/initiate_password_reset_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `InitiatePasswordResetRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/initiate_password_reset_request.proto
// version: 1.0.0
// guid: 16ce7615-af01-41a5-b5be-86728f975870
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to initiate password reset flow.
 * Sends reset instructions to user's email or generates reset token.
 * Used for self-service password recovery.
 */
message InitiatePasswordResetRequest {
  // User identifier (username or email)
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### initiate_password_reset_response.proto {#initiate_password_reset_response}

**Path**: `gcommon/v1/common/initiate_password_reset_response.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `InitiatePasswordResetResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/initiate_password_reset_response.proto
// version: 1.0.0
// guid: 418382e8-da43-4470-a00c-41b8ad9d699b
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to password reset initiation request.
 * Contains reset token and expiration information.
 * May include additional instructions for the user.
 */
message InitiatePasswordResetResponse {
  // Password reset token (may be sent via email instead)
  string reset_token = 1 [(buf.validate.field).string.min_len = 1];

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 2;

  // Message to display to user (e.g., "Check your email")
  string message = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### invalidate_user_sessions_request.proto {#invalidate_user_sessions_request}

**Path**: `gcommon/v1/common/invalidate_user_sessions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `InvalidateUserSessionsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/invalidate_user_sessions_request.proto
// version: 1.0.0
// guid: 678e9abc-d1e2-3f4a-5b6c-7d8e9f0a1b2c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to invalidate all sessions for a user.
 */
message InvalidateUserSessionsRequest {
  // User ID whose sessions should be invalidated
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### list_api_keys_request.proto {#list_api_keys_request}

**Path**: `gcommon/v1/common/list_api_keys_request.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `ListApiKeysRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_api_keys_request.proto
// version: 1.0.0
// guid: 978a16cb-4ec7-45ce-b762-c2a2b40a4e6f
// file: proto/gcommon/v1/common/list_api_keys_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListApiKeysRequest {
  // User ID to list API keys for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Include expired keys
  bool include_expired = 2;

  // Pagination
  int32 page_size = 3;
  string page_token = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### list_api_keys_response.proto {#list_api_keys_response}

**Path**: `gcommon/v1/common/list_api_keys_response.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `ListApiKeysResponse`

**Imports** (3):

- `gcommon/v1/common/api_key.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_api_keys_response.proto
// version: 1.0.0
// guid: 1c9b335d-ac56-4d22-aced-e1e6722e9247

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListApiKeysResponse {
  // List of API keys
  repeated gcommon.v1.common.APIKey api_keys = 1 [(buf.validate.field).repeated.min_items = 1];

  // Next page token
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total count
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}
```

---

### list_checks_request.proto {#list_checks_request}

**Path**: `gcommon/v1/common/list_checks_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `ListChecksRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_checks_request.proto
// version: 1.0.0
// guid: 15ac39bc-301a-4120-a333-5c07d417d4fb
// file: proto/gcommon/v1/common/list_checks_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListChecksRequest {
  // Optional service name to filter checks
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### list_notifications_request.proto {#list_notifications_request}

**Path**: `gcommon/v1/common/list_notifications_request.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `ListNotificationsRequest`

**Imports** (2):

- `gcommon/v1/common/pagination.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_notifications_request.proto
// version: 1.0.1
// guid: 34151d3e-f3cb-4445-a801-c9a44078e3cd

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/pagination.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

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

**Path**: `gcommon/v1/common/list_notifications_response.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `ListNotificationsResponse`

**Imports** (3):

- `gcommon/v1/common/notification_message.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_notifications_response.proto
// version: 1.0.0
// guid: 7986e6b9-6a3e-4b7e-b093-5a87133742a3

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/notification_message.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a list of notifications.
 */
message ListNotificationsResponse {
  // Notifications sorted by creation time descending.
  repeated NotificationMessage notifications = 1 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### list_permissions_request.proto {#list_permissions_request}

**Path**: `gcommon/v1/common/list_permissions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `ListPermissionsRequest`

**Imports** (3):

- `gcommon/v1/common/subject_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_permissions_request.proto
// version: 1.0.0
// guid: b28e318d-b0e8-41bb-9c90-d6b98f138e4f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/subject_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListPermissionsRequest {
  // User or role ID to list permissions for
  string subject_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subject type

  AuthSubjectType subject_type = 2;

  // Pagination
  int32 page_size = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
  string page_token = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### list_permissions_response.proto {#list_permissions_response}

**Path**: `gcommon/v1/common/list_permissions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `ListPermissionsResponse`

**Imports** (3):

- `gcommon/v1/common/permission.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_permissions_response.proto
// version: 1.0.0
// guid: 4aecc4bd-409d-4724-a679-a189e3390d5d
// file: proto/gcommon/v1/common/list_permissions_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/permission.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListPermissionsResponse {
  // List of permissions
  repeated Permission permissions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Next page token
  string next_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total count
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### list_roles_request.proto {#list_roles_request}

**Path**: `gcommon/v1/common/list_roles_request.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ListRolesRequest`

**Imports** (5):

- `gcommon/v1/common/filter_options.proto`
- `gcommon/v1/common/pagination.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/sort_options.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_roles_request.proto
// version: 1.0.1
// guid: 10d4a32a-06da-4751-965f-97c0d522d456
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/filter_options.proto";
import "gcommon/v1/common/pagination.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/sort_options.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to list roles with filtering and pagination.
 * Used for role management interfaces and administration.
 * Supports filtering, sorting, and pagination.
 */
message ListRolesRequest {
  // Pagination parameters
  gcommon.v1.common.Pagination pagination = 1;

  // Filter options for role selection
  gcommon.v1.common.FilterOptions filter = 2;

  // Sort options for result ordering
  gcommon.v1.common.SortOptions sort = 3;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### list_roles_response.proto {#list_roles_response}

**Path**: `gcommon/v1/common/list_roles_response.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `ListRolesResponse`

**Imports** (4):

- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_roles_response.proto
// version: 1.0.0
// guid: b0d2291f-7911-45f0-94d1-6dee153b5841
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a list of roles.
 * Includes pagination information for large result sets.
 * Used for role management interfaces and administration.
 */
message ListRolesResponse {
  // List of roles matching the request criteria
  repeated Role roles = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information for the response
  gcommon.v1.common.PaginatedResponse pagination = 2;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### list_sessions_request.proto {#list_sessions_request}

**Path**: `gcommon/v1/common/list_sessions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `AuthListSessionsRequest`

**Imports** (3):

- `gcommon/v1/common/pagination.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_sessions_request.proto
// version: 1.0.0
// guid: b293be7c-9588-4756-9429-52fe8a24a7b5
// file: proto/gcommon/v1/common/list_sessions_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/pagination.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to list all sessions (admin only).
 * Used for administrative monitoring and management.
 */
message AuthListSessionsRequest {
  // Pagination parameters
  gcommon.v1.common.Pagination pagination = 1;

  // Filter by user ID (optional)
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Filter by session status (optional)
  string status = 3;
}
```

---

### list_sessions_response.proto {#list_sessions_response}

**Path**: `gcommon/v1/common/list_sessions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `AuthListSessionsResponse`

**Imports** (4):

- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/common/session.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/list_sessions_response.proto
// version: 1.0.0
// guid: a07e1500-4f58-4fb0-9741-29e10c17d095
// file: proto/gcommon/v1/common/list_sessions_response.proto
//
// Response definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/common/session.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response containing a list of sessions.
 * Includes pagination information for large result sets.
 */
message AuthListSessionsResponse {
  // List of sessions
  repeated Session sessions = 1 [(buf.validate.field).repeated.min_items = 1];

  // Pagination information
  gcommon.v1.common.PaginatedResponse pagination = 2;
}
```

---

### list_user_sessions_request.proto {#list_user_sessions_request}

**Path**: `gcommon/v1/common/list_user_sessions_request.proto` **Package**: `gcommon.v1.common` **Lines**: 89

**Messages** (1): `ListUserSessionsRequest`

**Imports** (5):

- `gcommon/v1/common/pagination_options.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_user_sessions_request.proto
// version: 1.0.0
// guid: 8a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/pagination_options.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ListUserSessionsRequest requests a list of active sessions for a user.
 * Used by administrators to monitor user sessions and by users to view
 * their own active sessions across devices.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListUserSessionsRequest {
  // Required fields (1-10)

  /**
   * The ID of the user whose sessions should be listed.
   * This can be the requesting user's own ID or another user's ID
   * if the requester has appropriate permissions.
   */
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Pagination options for large result sets.
   * Defaults to first 50 sessions if not specified.
   */
  gcommon.v1.common.PaginationOptions pagination = 12;

  /**
   * Filter sessions by status (active, expired, terminated).
   * If not specified, returns all sessions.
   */
  string status_filter = 13;

  /**
   * Filter sessions by device type (web, mobile, api, etc.).
   * If not specified, returns sessions from all device types.
   */
  string device_type_filter = 14;

  /**
   * Only return sessions created after this timestamp.
   * Useful for finding recent sessions.
   */
  google.protobuf.Timestamp created_after = 15;

  /**
   * Only return sessions created before this timestamp.
   * Useful for historical analysis.
   */
  google.protobuf.Timestamp created_before = 16;

  /**
   * Include detailed session information (IP addresses, user agents, etc.).
   * May require additional permissions. Defaults to false.
   */
  bool include_details = 17;

  /**
   * Sort order for results. Valid values: "created_asc", "created_desc",
   * "last_activity_asc", "last_activity_desc". Defaults to "created_desc".
   */
  string sort_order = 18;
}
```

---

### list_user_sessions_response.proto {#list_user_sessions_response}

**Path**: `gcommon/v1/common/list_user_sessions_response.proto` **Package**: `gcommon.v1.common` **Lines**: 103

**Messages** (1): `ListUserSessionsResponse`

**Imports** (7):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/paginated_response.proto`
- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/session_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_user_sessions_response.proto
// version: 1.0.0
// guid: ac4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/paginated_response.proto";
import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/session_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports

// Common types

// Auth module types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ListUserSessionsResponse returns a list of user sessions.
 * Contains session details, pagination information, and metadata
 * for administrative session management and user self-service.
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message ListUserSessionsResponse {
  // Required fields (1-10)

  /**
   * List of session information for the requested user.
   * Empty if no sessions match the filters.
   */
  repeated SessionInfo sessions = 1;

  /**
   * Total number of sessions that match the query filters,
   * regardless of pagination. Useful for calculating page counts.
   */
  int32 total_count = 2;

  // Optional fields (11-50)

  /**
   * Pagination information for navigating through large result sets.
   * Contains next_page_token for retrieving additional results.
   */
  gcommon.v1.common.PaginatedResponse pagination = 11;

  /**
   * Request processing metadata including timing, request ID,
   * and other observability information.
   */
  gcommon.v1.common.RequestMetadata request_metadata = 12;

  /**
   * Indicates if the current request's session is included
   * in the results. Useful for UI highlighting.
   */
  bool includes_current_session = 13;

  /**
   * Number of active sessions (not expired/terminated).
   * Subset of total_count for quick status information.
   */
  int32 active_session_count = 14;

  /**
   * User ID for which sessions were retrieved.
   * Echoed from the request for verification.
   */
  string user_id = 15 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Status and error fields (61-70)

  /**
   * Error information if the request failed partially
   * or if there were issues retrieving some session data.
   */
  gcommon.v1.common.Error error = 61;

  // Timestamps (51-60)

  /**
   * Timestamp when this response was generated.
   * Useful for caching and staleness detection.
   */
  google.protobuf.Timestamp generated_at = 51;

  /**
   * Timestamp when the session data was last refreshed
   * from the authoritative source.
   */
  google.protobuf.Timestamp data_refreshed_at = 52;
}
```

---

### list_users_request.proto {#list_users_request}

**Path**: `gcommon/v1/common/list_users_request.proto` **Package**: `gcommon.v1.common` **Lines**: 45

**Messages** (1): `ListUsersRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_users_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174004

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to list users with pagination and filtering.
 */
message ListUsersRequest {
  // Page number (starting from 1)
  int32 page = 1;

  // Number of items per page
  int32 page_size = 2;

  // Filter by username (partial match)
  string username_filter = 3;

  // Filter by email (partial match)
  string email_filter = 4 [ (buf.validate.field).string.email = true ];

  // Filter by enabled status
  bool enabled_filter = 5;

  // Filter by role
  string role_filter = 6;

  // Sort field (username, email, created_at, etc.)
  string sort_by = 7;

  // Sort direction (asc or desc)
  string sort_direction = 8;

  // Include deleted users in results
  bool include_deleted = 9;
}
```

---

### list_users_response.proto {#list_users_response}

**Path**: `gcommon/v1/common/list_users_response.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Messages** (1): `ListUsersResponse`

**Imports** (3):

- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_users_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174005

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for listing users.
 */
message ListUsersResponse {
  // List of users
  repeated UserInfo users = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total number of users (before pagination)
  int32 total_count = 2 [(buf.validate.field).int32.gte = 0];

  // Current page number
  int32 page = 3 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items per page
  int32 page_size = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total number of pages
  int32 total_pages = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Whether there are more pages
  bool has_next_page = 6;

  // Whether this is not the first page
  bool has_previous_page = 7;
}
```

---

### logout_request.proto {#logout_request}

**Path**: `gcommon/v1/common/logout_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `LogoutRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logout_request.proto
// version: 1.0.0
// guid: b22adc38-523e-4fbf-8fae-d3f890525589

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogoutRequest ends a user session and invalidates tokens
message LogoutRequest {
  // ID of the session to terminate
  string session_id = 1;

  // Optional user ID for audit purposes
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### logout_response.proto {#logout_response}

**Path**: `gcommon/v1/common/logout_response.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `LogoutResponse`

**Imports** (2):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/logout_response.proto
// version: 1.0.1
// guid: 96821169-cc26-45e4-a7e3-b81f44ddeb99

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

// LogoutResponse provides the result of a logout request
message LogoutResponse {
  // Whether the logout was successful
  bool success = 1;

  // Optional error information if logout failed
  gcommon.v1.common.Error error = 2;
}
```

---

### mark_as_read_request.proto {#mark_as_read_request}

**Path**: `gcommon/v1/common/mark_as_read_request.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `MarkAsReadRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mark_as_read_request.proto
// version: 1.0.0
// guid: 106b287f-61f9-4551-8526-53a606fbd0d1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message MarkAsReadRequest {
  // Identifier of the notification to mark as read.
  string notification_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### mark_as_read_response.proto {#mark_as_read_response}

**Path**: `gcommon/v1/common/mark_as_read_response.proto` **Package**: `gcommon.v1.common` **Lines**: 20

**Messages** (1): `MarkAsReadResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/mark_as_read_response.proto
// version: 1.0.1
// guid: 1fd2817b-1b04-474f-ba5b-190ee82693bd

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for marking a notification as read.
 */
message MarkAsReadResponse {
  // True if the operation succeeded.
  bool success = 1;
}
```

---

### paginated_response.proto {#paginated_response}

**Path**: `gcommon/v1/common/paginated_response.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `PaginatedResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/paginated_response.proto
// version: 1.0.0
// guid: b51b64d3-29b8-4d03-bde5-dcaeb915a1f2
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Standard pagination response metadata for list operations.
 * Provides comprehensive pagination information to clients for
 * implementing pagination controls and navigation.
 */
message PaginatedResponse {
  // Opaque token for retrieving the next page (empty if no more pages)
  string next_page_token = 1 [(buf.validate.field).string.min_len = 1];

  // Opaque token for retrieving the previous page (empty if first page)
  string prev_page_token = 2 [(buf.validate.field).string.min_len = 1];

  // Total number of items across all pages (may be expensive to compute)
  int32 total_count = 3 [(buf.validate.field).int32.gte = 0];

  // Current page number (starts from 1)
  int32 current_page = 4 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Total number of pages available
  int32 total_pages = 5 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];

  // Number of items in the current page
  int32 page_size = 6 [(buf.validate.field).int32.gte = 0, (buf.validate.field).int32.lte = 150];
}
```

---

### read_logs_request.proto {#read_logs_request}

**Path**: `gcommon/v1/common/read_logs_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `ReadLogsRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/read_logs_request.proto
// version: 1.0.0
// guid: 9f0e1d2c-3b4a-5867-9e0f-1a2b3c4d5e6f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ReadLogsRequest defines the request for reading log entries.
 */
message ReadLogsRequest {
  // Filter by log level
  string level = 1 [(buf.validate.field).string.min_len = 1];

  // Filter by source
  string source = 2 [(buf.validate.field).string.min_len = 1];

  // Start time for log range
  int64 start_time = 3 [(buf.validate.field).int64.gte = 0];

  // End time for log range
  int64 end_time = 4 [(buf.validate.field).int64.gte = 0];

  // Maximum number of entries to return
  int32 limit = 5 [(buf.validate.field).int32.gte = 0];
}
```

---

### read_logs_response.proto {#read_logs_response}

**Path**: `gcommon/v1/common/read_logs_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `ReadLogsResponse`

**Imports** (3):

- `gcommon/v1/common/log_entry.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/read_logs_response.proto
// version: 1.0.0
// guid: 0f1e2d3c-4b5a-6978-0e1f-2a3b4c5d6e7f

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/log_entry.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ReadLogsResponse defines the response from reading log entries.
 */
message ReadLogsResponse {
  // Retrieved log entries
  repeated LogEntry entries = 1 [(buf.validate.field).repeated.min_items = 1];

  // Total count of matching entries
  int32 total_count = 2 [(buf.validate.field).int32.gte = 0];

  // Error message if any
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### refresh_token_request.proto {#refresh_token_request}

**Path**: `gcommon/v1/common/refresh_token_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `RefreshTokenRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/refresh_token_request.proto
// version: 1.0.0
// guid: b0a6426f-06af-49ad-85eb-2a4eb2bc2de6
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to refresh an access token using a refresh token.
 * Exchanges a valid refresh token for a new access token.
 * Optionally requests new scopes for the refreshed token.
 */
message RefreshTokenRequest {
  // Refresh token to exchange for new access token
  string refresh_token = 1 [(buf.validate.field).string.min_len = 1];

  // Requested scopes for the new access token
  repeated string scopes = 2 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### refresh_token_response.proto {#refresh_token_response}

**Path**: `gcommon/v1/common/refresh_token_response.proto` **Package**: `gcommon.v1.common` **Lines**: 37

**Messages** (1): `RefreshTokenResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/refresh_token_response.proto
// version: 1.0.0
// guid: 6dee199f-3a40-4f11-8207-16c802534230
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to token refresh request.
 * Contains new access token and potentially new refresh token.
 * Follows OAuth2 token response format.
 */
message RefreshTokenResponse {
  // New access token for API authentication
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // New refresh token (may be the same as input)
  string refresh_token = 2 [(buf.validate.field).string.min_len = 1];

  // Token type (always "Bearer")
  string token_type = 3 [(buf.validate.field).string.min_len = 1];

  // Access token expiration time in seconds
  int32 expires_in = 4 [(buf.validate.field).int32.gte = 0];

  // Granted scopes for the new access token
  repeated string scopes = 5 [(buf.validate.field).repeated.min_items = 1];
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### register_check_request.proto {#register_check_request}

**Path**: `gcommon/v1/common/register_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `RegisterCheckRequest`

**Imports** (4):

- `gcommon/v1/common/health_check_request.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/register_check_request.proto
// version: 1.0.0
// guid: d0def031-b6c4-482c-8e68-7d395ac76697
// file: proto/gcommon/v1/common/register_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_check_request.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RegisterCheckRequest {
  // Service name this check belongs to
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Parameters describing the check to execute
  HealthHealthCheckRequest check = 2;

  // Standard request metadata
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### register_check_response.proto {#register_check_response}

**Path**: `gcommon/v1/common/register_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `RegisterCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/register_check_response.proto
// version: 1.0.0
// guid: c52bced5-89bc-4021-81d6-491a104872a8
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for health check registration.
 * Contains the result of registering a new health check.
 */
message RegisterCheckResponse {
  // Success status
  bool success = 1;

  // Registered check ID
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information
  gcommon.v1.common.Error error = 3;
}
```

---

### register_user_request.proto {#register_user_request}

**Path**: `gcommon/v1/common/register_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 68

**Messages** (1): `RegisterUserRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/register_user_request.proto
// version: 1.0.0
// guid: b1c2d3e4-f5a6-7b8c-9d0e-1f2a3b4c5d6e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to register a new user account.
 * Creates a new user with the provided credentials and profile information.
 */
message RegisterUserRequest {
  // Username for the new account (required)
  string username = 1;

  // Email address for the new account (required)
  string email = 2 [ (buf.validate.field).string.email = true ];

  // Password for the new account (required)
  string password = 3;

  // First name of the user
  string first_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Last name of the user
  string last_name = 5 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Phone number (optional)
  string phone_number = 6;

  // Initial organization to associate user with (optional)
  string organization_id = 7 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Whether email verification is required
  bool require_email_verification = 8;

  // Invitation token (if registering via invitation)
  string invitation_token = 9;

  // Additional user metadata
  map<string, string> metadata = 10;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata request_metadata = 11;

  // Terms of service acceptance timestamp
  int64 tos_accepted_at = 12;

  // Privacy policy acceptance timestamp
  int64 privacy_accepted_at = 13;
}
```

---

### register_user_response.proto {#register_user_response}

**Path**: `gcommon/v1/common/register_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `RegisterUserResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/register_user_response.proto
// version: 1.0.0
// guid: 5bda08f2-024d-4dfb-8ba4-45b84fe8d4ef
// file: proto/gcommon/v1/common/register_user_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RegisterUserResponse {
  // Registration success
  bool success = 1;

  // User ID of created user
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Whether email verification is required
  bool email_verification_required = 3;

  // Error message if registration failed
  string error_message = 4;

  // Session token if immediate login is allowed
  string session_token = 5;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### remove_role_request.proto {#remove_role_request}

**Path**: `gcommon/v1/common/remove_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `RemoveRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/remove_role_request.proto
// version: 1.0.0
// guid: dfde5734-62db-444c-b390-fda716da06e1
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to remove a role from a user.
 * Used for role-based access control management.
 * Removes the specified role assignment from the user.
 */
message RemoveRoleRequest {
  // User ID to remove role from
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID to remove
  string role_id = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### remove_role_response.proto {#remove_role_response}

**Path**: `gcommon/v1/common/remove_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 54

**Messages** (1): `RemoveRoleResponse`

**Imports** (4):

- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/remove_role_response.proto
// version: 1.0.0
// guid: d8f9ff14-27d8-4495-bba6-2a8a944df6be
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RemoveRoleResponse confirms successful role removal from a user.
 * Provides information about the removal operation including
 * the removed role and removal metadata for audit purposes.
 */
message RemoveRoleResponse {
  // User ID from whom the role was removed
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username of the user
  string username = 2;

  // Role that was removed from the user
  Role role = 3;

  // Timestamp when the role was removed
  google.protobuf.Timestamp removed_at = 4;

  // ID of the admin user who performed the removal
  string removed_by_user_id = 5;

  // Username of the admin who performed the removal
  string removed_by_username = 6;

  // Whether this removal was effective immediately
  bool effective_immediately = 7;

  // Whether the user still has other roles assigned
  bool has_remaining_roles = 8;

  // Count of remaining roles for the user
  int32 remaining_role_count = 9;

  // Success message describing the removal
  string message = 10;
}
```

---

### resend_verification_request.proto {#resend_verification_request}

**Path**: `gcommon/v1/common/resend_verification_request.proto` **Package**: `gcommon.v1.common` **Lines**: 24

**Messages** (1): `ResendVerificationRequest`

**Imports** (3):

- `gcommon/v1/common/verification_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/resend_verification_request.proto
// version: 1.0.0
// guid: 59477f5d-a132-4166-97a0-58e8a4534c3e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/verification_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ResendVerificationRequest {
  // User ID or email address
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Verification type

  AuthVerificationType type = 2;
}
```

---

### reset_health_stats_request.proto {#reset_health_stats_request}

**Path**: `gcommon/v1/common/reset_health_stats_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `ResetHealthStatsRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/reset_health_stats_request.proto
// version: 1.0.0
// guid: e8903f7e-5da9-40bf-8b9b-1a6747e1391e
// file: proto/gcommon/v1/common/reset_health_stats_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ResetHealthStatsRequest {
  // Service name whose stats should be reset
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### reset_health_stats_response.proto {#reset_health_stats_response}

**Path**: `gcommon/v1/common/reset_health_stats_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `ResetHealthStatsResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/reset_health_stats_response.proto
// version: 1.0.0
// guid: 6b989b99-80f9-42fe-8a61-817a735351b1
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for resetting health statistics.
 * Contains the result of clearing stored health metrics and statistics.
 */
message ResetHealthStatsResponse {
  // Success status
  bool success = 1;

  // Number of statistics entries cleared
  int32 cleared_entries = 2 [(buf.validate.field).int32.gte = 0];

  // Reset timestamp
  google.protobuf.Timestamp reset_at = 3;

  // Error information if reset failed
  gcommon.v1.common.Error error = 4;

  // Statistics categories that were reset
  repeated string reset_categories = 5 [(buf.validate.field).repeated.min_items = 1];
}
```

---

### reset_password_request.proto {#reset_password_request}

**Path**: `gcommon/v1/common/reset_password_request.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `ResetPasswordRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/reset_password_request.proto
// version: 1.0.0
// guid: 79c62bc6-23ed-4b2e-9bb4-4e3091880b22

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ResetPasswordRequest triggers a password reset for a user.
 */
message ResetPasswordRequest {
  // User ID to reset password for
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Temporary reset token provided to the user
  string token = 2;

  // New password to set
  string new_password = 3;

  // Metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;
}
```

---

### reset_password_response.proto {#reset_password_response}

**Path**: `gcommon/v1/common/reset_password_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `ResetPasswordResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/reset_password_response.proto
// version: 1.0.0
// guid: 9de139b4-5d77-49c3-b18b-7cf12ea5c132

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * ResetPasswordResponse indicates success or failure of password reset.
 */
message ResetPasswordResponse {
  // Whether the reset was successful
  bool success = 1;

  // Optional message describing the result
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Response metadata for rate limiting and tracing
  gcommon.v1.common.ResponseMetadata metadata = 3;
}
```

---

### revoke_api_key_request.proto {#revoke_api_key_request}

**Path**: `gcommon/v1/common/revoke_api_key_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `RevokeApiKeyRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/revoke_api_key_request.proto
// version: 1.0.0
// guid: 889f38ad-dde7-41cd-aa20-ec974b0207f1
// file: proto/gcommon/v1/common/revoke_api_key_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokeApiKeyRequest {
  // API key ID to revoke
  string key_id = 1 [(buf.validate.field).string.min_len = 1];

  // Reason for revocation
  string reason = 2 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### revoke_api_key_response.proto {#revoke_api_key_response}

**Path**: `gcommon/v1/common/revoke_api_key_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `RevokeApiKeyResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/revoke_api_key_response.proto
// version: 1.0.0
// guid: 408b6755-7ee3-44e4-80c2-af76cc4cf87b
// file: proto/gcommon/v1/common/revoke_api_key_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokeApiKeyResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Revocation timestamp
  int64 revoked_at = 3 [(buf.validate.field).int64.gte = 0];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### revoke_permission_request.proto {#revoke_permission_request}

**Path**: `gcommon/v1/common/revoke_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `RevokePermissionRequest`

**Imports** (3):

- `gcommon/v1/common/subject_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_permission_request.proto
// version: 1.0.0
// guid: 08a90c9d-4730-427a-b445-35cbadc141a6

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/subject_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokePermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1 [(buf.validate.field).string.min_len = 1];

  // Subject type

  AuthSubjectType subject_type = 2;

  // Permission ID to revoke
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

### revoke_permission_response.proto {#revoke_permission_response}

**Path**: `gcommon/v1/common/revoke_permission_response.proto` **Package**: `gcommon.v1.common` **Lines**: 36

**Messages** (1): `RevokePermissionResponse`

**Imports** (3):

- `gcommon/v1/common/response_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_permission_response.proto
// version: 1.0.0
// guid: f5a6b7c8-d9e0-1f2a-3b4c-5d6e7f8a9b0c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for permission revocation operations.
 * Indicates whether the permission was successfully revoked.
 */
message RevokePermissionResponse {
  // Whether the permission revocation was successful
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // The revoked permission ID
  string permission_id = 3 [(buf.validate.field).string.min_len = 1];

  // User or entity the permission was revoked from
  string revokee_id = 4 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 5;
}
```

---

### revoke_role_request.proto {#revoke_role_request}

**Path**: `gcommon/v1/common/revoke_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 48

**Messages** (1): `RevokeRoleRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_role_request.proto
// version: 1.0.0
// guid: a6b7c8d9-e0f1-2a3b-4c5d-6e7f8a9b0c1d

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to revoke a role from a user.
 * Used for role-based access control management.
 * Removes the specified role permissions from the user.
 */
message RevokeRoleRequest {
  // User ID to revoke role from (required)
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Role ID to revoke (required)
  string role_id = 2;

  // Optional organization context for scoped role revocation
  string organization_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 4;

  // Audit information for tracking who made the revocation
  string revoked_by = 5;

  // Reason for role revocation (optional)
  string reason = 6;

  // Whether to force revocation even if user has dependencies
  bool force = 7;
}
```

---

### revoke_role_response.proto {#revoke_role_response}

**Path**: `gcommon/v1/common/revoke_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `RevokeRoleResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/revoke_role_response.proto
// version: 1.0.0
// guid: acfab4c3-a30b-45ba-9590-745f492f55bd
// file: proto/gcommon/v1/common/revoke_role_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RevokeRoleResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Remaining permissions after revocation
  repeated string remaining_permissions = 3 [(buf.validate.field).repeated.min_items = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### revoke_token_request.proto {#revoke_token_request}

**Path**: `gcommon/v1/common/revoke_token_request.proto` **Package**: `gcommon.v1.common` **Lines**: 30

**Messages** (1): `RevokeTokenRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_token_request.proto
// version: 1.0.0
// guid: 0fc4421f-09e3-4cf7-8e64-d11797c80088
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to revoke a token (access or refresh).
 * Invalidates the specified token and prevents further use.
 * Used for logout operations and security revocation.
 */
message RevokeTokenRequest {
  // Token to revoke (access or refresh token)
  string token = 1 [(buf.validate.field).string.min_len = 1];

  // Token type hint ("access_token" or "refresh_token")
  string token_type_hint = 2 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
```

---

### revoke_token_response.proto {#revoke_token_response}

**Path**: `gcommon/v1/common/revoke_token_response.proto` **Package**: `gcommon.v1.common` **Lines**: 41

**Messages** (1): `RevokeTokenResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/revoke_token_response.proto
// version: 1.0.0
// guid: f25b7f00-5a70-4776-8dfd-fb942ffd6980
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * RevokeTokenResponse confirms successful token revocation.
 * Provides information about the revoked token and revocation timestamp
 * for audit logging and confirmation purposes.
 */
message RevokeTokenResponse {
  // Token ID that was revoked
  string token_id = 1;

  // Type of token that was revoked (access, refresh, etc.)
  string token_type = 2;

  // Timestamp when the token was revoked
  google.protobuf.Timestamp revoked_at = 3;

  // User ID associated with the revoked token
  string user_id = 4 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Reason for revocation (logout, security, expiry, etc.)
  string revocation_reason = 5;

  // Whether this was the last token for the user session
  bool last_token_in_session = 6;
}
```

---

### run_check_request.proto {#run_check_request}

**Path**: `gcommon/v1/common/run_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `RunCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/run_check_request.proto
// version: 1.0.0
// guid: baa819a3-645e-4309-9473-1bb8bbd18e40
// file: proto/gcommon/v1/common/run_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message RunCheckRequest {
  // Name or ID of the check to run
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Request metadata used for tracing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### run_check_response.proto {#run_check_response}

**Path**: `gcommon/v1/common/run_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 44

**Messages** (1): `RunCheckResponse`

**Imports** (6):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/run_check_response.proto
// version: 1.0.0
// guid: 573c89a4-b638-49c8-bb99-29d1e4db5b60
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for manually running a health check.
 * Contains the result of executing a health check on demand.
 */
message RunCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was executed
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Health status result
  gcommon.v1.common.CommonHealthStatus status = 3;

  // Execution timestamp
  google.protobuf.Timestamp executed_at = 4;

  // Execution duration
  google.protobuf.Duration execution_time = 5;

  // Check result message
  string message = 6 [(buf.validate.field).string.min_len = 1];

  // Error information if check failed
  gcommon.v1.common.Error error = 7;
}
```

---

### send_notification_request.proto {#send_notification_request}

**Path**: `gcommon/v1/common/send_notification_request.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `SendNotificationRequest`

**Imports** (3):

- `gcommon/v1/common/notification_message.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/send_notification_request.proto
// version: 1.0.1
// guid: 42b9620e-9388-4ee6-be25-e4a3a0928211

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/notification_message.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SendNotificationRequest {
  // Standard request metadata for tracing and auth.
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Notification to be delivered.
  NotificationMessage notification = 2;
}
```

---

### send_notification_response.proto {#send_notification_response}

**Path**: `gcommon/v1/common/send_notification_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `SendNotificationResponse`

**Imports** (3):

- `gcommon/v1/common/delivery_status.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/send_notification_response.proto
// version: 1.0.0
// guid: 4c4e1ac6-1393-496b-80b5-cb0bd7ef41f1

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/delivery_status.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response returned after sending a notification.
 */
message SendNotificationResponse {
  // Unique identifier for the queued notification.
  string notification_id = 1 [(buf.validate.field).string.min_len = 1];

  // Whether the notification was accepted for delivery
  bool accepted = 2;

  // Current delivery status of the notification
  gcommon.v1.common.DeliveryStatus status = 3;
}
```

---

### send_verification_email_request.proto {#send_verification_email_request}

**Path**: `gcommon/v1/common/send_verification_email_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `SendVerificationEmailRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/send_verification_email_request.proto
// version: 1.0.0
// guid: 0e006386-d269-49b5-b99f-3794275714db
// file: proto/gcommon/v1/common/send_verification_email_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SendVerificationEmailRequest {
  // User ID or email address
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Template to use for email
  string template = 2 [(buf.validate.field).string.min_len = 1];

  // Additional context data
  map<string, string> context = 3;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### send_verification_email_response.proto {#send_verification_email_response}

**Path**: `gcommon/v1/common/send_verification_email_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `SendVerificationEmailResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/send_verification_email_response.proto
// version: 1.0.0
// guid: f17880d2-6f37-4b9d-a6d6-06c70e75e7d6
// file: proto/gcommon/v1/common/send_verification_email_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SendVerificationEmailResponse {
  // Send success
  bool sent = 1;

  // Error message if send failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Token expiry time
  int64 expires_at = 3 [(buf.validate.field).int64.gte = 0];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### set_health_request.proto {#set_health_request}

**Path**: `gcommon/v1/common/set_health_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `SetHealthRequest`

**Imports** (4):

- `gcommon/v1/common/health_status.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/set_health_request.proto
// version: 1.0.0
// guid: 448c2377-fccd-47a6-bb60-977a92b8eaac
// file: proto/gcommon/v1/common/set_health_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/health_status.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message SetHealthRequest {
  // Service name to update
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Desired health status
  gcommon.v1.common.CommonHealthStatus status = 2;

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 3 [lazy = true];
}
```

---

### set_health_response.proto {#set_health_response}

**Path**: `gcommon/v1/common/set_health_response.proto` **Package**: `gcommon.v1.common` **Lines**: 40

**Messages** (1): `SetHealthResponse`

**Imports** (5):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/set_health_response.proto
// version: 1.0.0
// guid: 5ec27f13-872f-47b7-acb8-58d9d37ae159
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for manually setting health status.
 * Contains the result of administratively setting the health status.
 */
message SetHealthResponse {
  // Success status
  bool success = 1;

  // Previous health status before the change
  gcommon.v1.common.CommonHealthStatus previous_status = 2;

  // New health status after the change
  gcommon.v1.common.CommonHealthStatus new_status = 3;

  // Timestamp when status was changed
  google.protobuf.Timestamp changed_at = 4;

  // Error information if setting failed
  gcommon.v1.common.Error error = 5;

  // Reason for the manual status change
  string reason = 6 [(buf.validate.field).string.min_len = 1];
}
```

---

### terminate_session_request.proto {#terminate_session_request}

**Path**: `gcommon/v1/common/terminate_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 102

**Messages** (1): `TerminateSessionRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/terminate_session_request.proto
// version: 1.0.0
// guid: 9b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";
// Standard imports
// Common types

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * TerminateSessionRequest terminates one or more user sessions.
 * Used by administrators to forcibly terminate user sessions,
 * or by users to terminate their own sessions (e.g., "log out all devices").
 *
 * Follows 1-1-1 pattern: one message per file.
 */
message TerminateSessionRequest {
  // Required fields (1-10)

  /**
   * The ID of the user whose session(s) should be terminated.
   * This can be the requesting user's own ID or another user's ID
   * if the requester has appropriate permissions.
   */
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  /**
   * Specific session IDs to terminate. If empty, the termination
   * scope is determined by other filters.
   */
  repeated string session_ids = 2;

  // Optional fields (11-50)

  /**
   * Standard request metadata including authentication context,
   * tracing information, and client details.
   */
  gcommon.v1.common.RequestMetadata metadata = 11;

  /**
   * Terminate all sessions for this user. When true, ignores
   * session_ids and other filters. Requires admin permissions
   * unless user is terminating their own sessions.
   */
  bool terminate_all = 12;

  /**
   * Only terminate sessions matching this device type filter.
   * Valid values: "web", "mobile", "api", "desktop".
   * If not specified, applies to all device types.
   */
  string device_type_filter = 13;

  /**
   * Only terminate sessions created before this timestamp.
   * Useful for terminating old/stale sessions.
   */
  google.protobuf.Timestamp created_before = 14;

  /**
   * Only terminate sessions with last activity before this timestamp.
   * Useful for terminating inactive sessions.
   */
  google.protobuf.Timestamp last_activity_before = 15;

  /**
   * Exclude the current session (the one making this request)
   * from termination. Defaults to true to prevent self-logout.
   */
  bool exclude_current_session = 16;

  /**
   * Reason for termination (for audit logging).
   * Examples: "user_logout", "admin_action", "security_breach", "policy_violation".
   */
  string termination_reason = 17;

  /**
   * Send notification to user about session termination.
   * May include email, push notification, etc. Defaults to true.
   */
  bool send_notification = 18;

  /**
   * Force immediate termination without graceful cleanup.
   * Use with caution as it may result in data loss. Defaults to false.
   */
  bool force_immediate = 19;
}
```

---

### terminate_session_response.proto {#terminate_session_response}

**Path**: `gcommon/v1/common/terminate_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 53

**Messages** (1): `TerminateSessionResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/terminate_session_response.proto
// version: 1.0.0
// guid: b183b962-3ed6-499a-8c81-3fd2bcaaf65b
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * TerminateSessionResponse confirms successful session termination.
 * Provides information about the terminated session and cleanup operations
 * for audit logging and confirmation purposes.
 */
message TerminateSessionResponse {
  // Session ID that was terminated
  string session_id = 1;

  // User ID whose session was terminated
  string user_id = 2 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Username of the user
  string username = 3;

  // Timestamp when the session was terminated
  google.protobuf.Timestamp terminated_at = 4;

  // Reason for termination (logout, timeout, security, admin, etc.)
  string termination_reason = 5;

  // Whether any associated tokens were revoked
  bool tokens_revoked = 6;

  // Number of tokens that were revoked
  int32 revoked_token_count = 7;

  // Whether this was a forced termination (by admin or security)
  bool forced_termination = 8;

  // Number of remaining active sessions for this user
  int32 remaining_session_count = 9;

  // Success message describing the termination
  string message = 10;
}
```

---

### unregister_check_request.proto {#unregister_check_request}

**Path**: `gcommon/v1/common/unregister_check_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `UnregisterCheckRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/unregister_check_request.proto
// version: 1.0.0
// guid: 97f6ba81-dd35-4406-a842-01af8b19471b
// file: proto/gcommon/v1/common/unregister_check_request.proto
//
// Request definitions for health module
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UnregisterCheckRequest {
  // ID of the check to unregister
  string check_id = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### unregister_check_response.proto {#unregister_check_response}

**Path**: `gcommon/v1/common/unregister_check_response.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `UnregisterCheckResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/unregister_check_response.proto
// version: 1.0.0
// guid: 6acc368e-830b-4b51-be8d-104cf86040f4
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for unregistering a health check.
 * Contains the result of removing a health check from the system.
 */
message UnregisterCheckResponse {
  // Success status
  bool success = 1;

  // Check ID that was unregistered
  string check_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error information if unregistration failed
  gcommon.v1.common.Error error = 3;

  // Confirmation message
  string message = 4 [(buf.validate.field).string.min_len = 1];
}
```

---

### update_permission_request.proto {#update_permission_request}

**Path**: `gcommon/v1/common/update_permission_request.proto` **Package**: `gcommon.v1.common` **Lines**: 53

**Messages** (1): `UpdatePermissionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_permission_request.proto
// version: 1.0.0
// guid: e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update an existing permission.
 * Allows modification of permission properties and constraints.
 */
message UpdatePermissionRequest {
  // Permission ID to update (required)
  string permission_id = 1;

  // New permission name (optional)
  string name = 2 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // New permission description (optional)
  string description = 3 [ (buf.validate.field).string.max_len = 1000 ];

  // New resource this permission applies to (optional)
  string resource = 4;

  // New action this permission allows (optional)
  string action = 5;

  // New conditions for the permission (optional)
  repeated string conditions = 6;

  // Whether the permission should be active (optional)
  bool active = 7;

  // Fields to update (field mask)
  repeated string update_mask = 8;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 9;

  // Reason for the update
  string reason = 10;
}
```

---

### update_preferences_request.proto {#update_preferences_request}

**Path**: `gcommon/v1/common/update_preferences_request.proto` **Package**: `gcommon.v1.common` **Lines**: 22

**Messages** (1): `UpdatePreferencesRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/subscription_preferences.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_preferences_request.proto
// version: 1.0.1
// guid: c74c733f-1a03-4b74-b5f1-cfa062e66475

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/subscription_preferences.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message UpdatePreferencesRequest {
  // Subscription preferences to apply
  SubscriptionPreferences preferences = 1 [lazy = true];

  // Request metadata for auditing
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];
}
```

---

### update_preferences_response.proto {#update_preferences_response}

**Path**: `gcommon/v1/common/update_preferences_response.proto` **Package**: `gcommon.v1.common` **Lines**: 19

**Messages** (1): `UpdatePreferencesResponse`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_preferences_response.proto
// version: 1.0.1
// guid: 3eb0a369-6ebb-48fb-b5a1-8e7e3d5d7f39
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for updating subscription preferences.
 */
message UpdatePreferencesResponse {
  // Whether the update succeeded
  bool success = 1;
}
```

---

### update_role_request.proto {#update_role_request}

**Path**: `gcommon/v1/common/update_role_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `UpdateRoleRequest`

**Imports** (4):

- `gcommon/v1/common/request_metadata.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/field_mask.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_role_request.proto
// version: 1.0.1
// guid: b5502816-55e0-4610-93d1-c0d0d470d118
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/field_mask.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update an existing role.
 * Used for role management and permission modification.
 * Supports partial updates using field mask.
 */
message UpdateRoleRequest {
  // Role data with updates
  Role role = 1;

  // Field mask specifying which fields to update
  google.protobuf.FieldMask update_mask = 2;

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 3;
}
// This is a placeholder file created during 1-1-1 migration
// Implement the actual protobuf definitions according to the auth module requirements
```

---

### update_role_response.proto {#update_role_response}

**Path**: `gcommon/v1/common/update_role_response.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `UpdateRoleResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/role.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/update_role_response.proto
// file: proto/gcommon/v1/common/update_role_response.proto
// version: 1.0.1
// guid: 567e89ab-c1d2-3e4f-5a6b-7c8d9e0f1a2b

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/role.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for updating a role.
 * Returns the updated role.
 */
message UpdateRoleResponse {
  // The updated role
  Role role = 1;

  // Error information if update failed
  gcommon.v1.common.Error error = 2;
}
```

---

### update_session_request.proto {#update_session_request}

**Path**: `gcommon/v1/common/update_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `AuthUpdateSessionRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/update_session_request.proto
// version: 1.0.0
// guid: 7e7565ed-c945-498a-8b56-705b4e113e51
// file: proto/gcommon/v1/common/update_session_request.proto
//
// Request definitions for auth module
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update session information.
 * Used to refresh session activity or update session metadata.
 */
message AuthUpdateSessionRequest {
  // Session ID to update
  string session_id = 1 [(buf.validate.field).string.min_len = 1];

  // Updated session metadata
  map<string, string> metadata = 2;

  // New expiration time (optional)
  google.protobuf.Timestamp expires_at = 3;
}
```

---

### update_session_response.proto {#update_session_response}

**Path**: `gcommon/v1/common/update_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `AuthUpdateSessionResponse`

**Imports** (4):

- `gcommon/v1/common/response_metadata.proto`
- `gcommon/v1/common/session_info.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_session_response.proto
// version: 1.0.0
// guid: f9a0b1c2-d3e4-5f6a-7b8c-9d0e1f2a3b4c

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/response_metadata.proto";
import "gcommon/v1/common/session_info.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for session update operations.
 * Contains the updated session information.
 */
message AuthUpdateSessionResponse {
  // Whether the update was successful
  bool success = 1;

  // Updated session information
  SessionInfo session = 2;

  // Error message if update failed
  string error_message = 3 [(buf.validate.field).string.min_len = 1];

  // Response metadata
  gcommon.v1.common.ResponseMetadata metadata = 4;
}
```

---

### update_user_request.proto {#update_user_request}

**Path**: `gcommon/v1/common/update_user_request.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `UpdateUserRequest`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_user_request.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174006

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to update an existing user account.
 */
message UpdateUserRequest {
  // Unique identifier of the user to update
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // New email address (optional)
  string email = 2 [ (buf.validate.field).string.email = true ];

  // New password (should be hashed, optional)
  string password = 3;

  // New full name (optional)
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether to enable/disable the account (optional)
  bool enabled = 5;

  // New roles to assign (replaces existing roles)
  repeated string roles = 6;

  // Additional metadata updates
  map<string, string> metadata = 7;

  // New account expiration time (optional)
  google.protobuf.Timestamp expires_at = 8;

  // Fields to update (if empty, all provided fields are updated)
  repeated string update_mask = 9;
}
```

---

### update_user_response.proto {#update_user_response}

**Path**: `gcommon/v1/common/update_user_response.proto` **Package**: `gcommon.v1.common` **Lines**: 52

**Messages** (1): `UpdateUserResponse`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/update_user_response.proto
// version: 1.0.0
// guid: 123e4567-e89b-12d3-a456-426614174007

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for updating a user account.
 */
message UpdateUserResponse {
  // Unique identifier for the updated user
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // Updated username
  string username = 2;

  // Updated email address
  string email = 3 [ (buf.validate.field).string.email = true ];

  // Updated full name
  string full_name = 4 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Whether the account is enabled
  bool enabled = 5;

  // Updated roles
  repeated string roles = 6;

  // When the account was last updated
  google.protobuf.Timestamp updated_at = 7;

  // Account expiration time (if set)
  google.protobuf.Timestamp expires_at = 8;

  // List of fields that were actually updated
  repeated string updated_fields = 9;
}
```

---

### validate_session_request.proto {#validate_session_request}

**Path**: `gcommon/v1/common/validate_session_request.proto` **Package**: `gcommon.v1.common` **Lines**: 27

**Messages** (1): `ValidateSessionRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_session_request.proto
// version: 1.0.0
// guid: 0100439d-a620-4991-9d73-231ae604bf9a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to validate a session token.
 * Used to verify session validity and retrieve session information.
 * Returns session and user data if token is valid.
 */
message ValidateSessionRequest {
  // Session token to validate
  string session_token = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### validate_session_response.proto {#validate_session_response}

**Path**: `gcommon/v1/common/validate_session_response.proto` **Package**: `gcommon.v1.common` **Lines**: 33

**Messages** (1): `ValidateSessionResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/session.proto`
- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_session_response.proto
// version: 1.0.1
// guid: 53da0a29-4520-4990-9822-6b18b3dedc2a
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/session.proto";
import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to session validation request.
 * Contains session validity status and associated user/session information.
 * Includes error information if validation fails.
 */
message ValidateSessionResponse {
  // Whether the session is valid
  bool valid = 1;

  // Session information if valid
  Session session = 2 [lazy = true];

  // User information associated with the session
  UserInfo user_info = 3 [lazy = true];

  // Error information if validation fails
  gcommon.v1.common.Error error = 4 [lazy = true];
}
```

---

### validate_token_request.proto {#validate_token_request}

**Path**: `gcommon/v1/common/validate_token_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `ValidateTokenRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_token_request.proto
// version: 1.0.0
// guid: 337bc0eb-8b0a-4a0c-b173-506f0eae4f52
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to validate an access token.
 * Used to verify token authenticity, expiration, and extract user information.
 */
message ValidateTokenRequest {
  // Access token to validate (Bearer token format)
  string access_token = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 2 [lazy = true];

  // Whether to include user information in response
  bool include_user_info = 3;

  // Whether to include permissions in response
  bool include_permissions = 4;
}
```

---

### validate_token_response.proto {#validate_token_response}

**Path**: `gcommon/v1/common/validate_token_response.proto` **Package**: `gcommon.v1.common` **Lines**: 42

**Messages** (1): `ValidateTokenResponse`

**Imports** (4):

- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/validate_token_response.proto
// version: 1.0.0
// guid: b1fc9b36-9860-473f-b59b-a7b9ffbe218b
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response for token validation requests.
 * Contains token validity status and associated user information.
 */
message ValidateTokenResponse {
  // Whether the token is valid
  bool valid = 1;

  // Token expiration timestamp
  google.protobuf.Timestamp expires_at = 2 [lazy = true];

  // User information associated with the token
  UserInfo user_info = 3 [lazy = true];

  // Token scopes/permissions
  repeated string scopes = 4 [(buf.validate.field).repeated.min_items = 1];

  // Token subject (user ID)
  string subject = 5 [(buf.validate.field).string.min_len = 1];

  // Token issuer
  string issuer = 6 [(buf.validate.field).string.min_len = 1];

  // Time until token expires (in seconds)
  int32 expires_in = 7 [(buf.validate.field).int32.gte = 0];
}
```

---

### verify2_fa_request.proto {#verify2_fa_request}

**Path**: `gcommon/v1/common/verify2_fa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `Verify2FaRequest`

**Imports** (3):

- `gcommon/v1/common/two_fa_type.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verify2_fa_request.proto
// version: 1.0.0
// guid: fa64bc16-24a7-4b50-ba76-fc8fdd7079de

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/two_fa_type.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message Verify2FaRequest {
  // User ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // 2FA verification code
  string code = 2;

  // Type of 2FA being verified

  AuthTwoFaType type = 3;
}
```

---

### verify_credentials_request.proto {#verify_credentials_request}

**Path**: `gcommon/v1/common/verify_credentials_request.proto` **Package**: `gcommon.v1.common` **Lines**: 32

**Messages** (1): `VerifyCredentialsRequest`

**Imports** (4):

- `gcommon/v1/common/api_key_credentials.proto`
- `gcommon/v1/common/password_credentials.proto`
- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verify_credentials_request.proto
// version: 1.0.1
// guid: 11047805-0f53-4b8a-b2b5-355b1abfea63
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/api_key_credentials.proto";
import "gcommon/v1/common/password_credentials.proto";
import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Request to verify user credentials without issuing tokens.
 * Used for credential validation without creating an authenticated session.
 * Supports password and API key credential verification.
 */
message VerifyCredentialsRequest {
  // Request metadata for tracing and correlation
  gcommon.v1.common.RequestMetadata metadata = 1;

  // Credentials to verify (oneof ensures only one type is used)
  oneof credentials {
    // Username/password credentials
    PasswordCredentials password = 2;
    // API key credentials
    APIKeyCredentials api_key = 3;
  }
}
```

---

### verify_credentials_response.proto {#verify_credentials_response}

**Path**: `gcommon/v1/common/verify_credentials_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `VerifyCredentialsResponse`

**Imports** (3):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/user_info.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/verify_credentials_response.proto
// version: 1.0.1
// guid: e7457cd0-baf1-4e73-a64c-ac0a8ed7946f
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/user_info.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response to credential verification request.
 * Contains verification result and user information if credentials are valid.
 * Includes error information if verification fails.
 */
message VerifyCredentialsResponse {
  // Whether the credentials are valid
  bool verified = 1;

  // User information if credentials are verified
  UserInfo user_info = 2 [lazy = true];

  // Error information if verification fails
  gcommon.v1.common.Error error = 3 [lazy = true];
}
```

---

### verify_email_request.proto {#verify_email_request}

**Path**: `gcommon/v1/common/verify_email_request.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `VerifyEmailRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_email_request.proto
// version: 1.0.0
// guid: 8f68392c-3cc1-408c-a8ac-4c48d08a70a0
// file: proto/gcommon/v1/common/verify_email_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyEmailRequest {
  // User ID or email to verify
  string identifier = 1 [(buf.validate.field).string.min_len = 1];

  // Verification token from email
  string verification_token = 2 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### verify_email_response.proto {#verify_email_response}

**Path**: `gcommon/v1/common/verify_email_response.proto` **Package**: `gcommon.v1.common` **Lines**: 34

**Messages** (1): `VerifyEmailResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_email_response.proto
// version: 1.0.0
// guid: 93319a70-2b96-4a96-8bfd-c8412437d883
// file: proto/gcommon/v1/common/verify_email_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyEmailResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  string error_message = 2;

  // User ID that was verified
  string user_id = 3 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### verify_mfa_request.proto {#verify_mfa_request}

**Path**: `gcommon/v1/common/verify_mfa_request.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `VerifyMfaRequest`

**Imports** (3):

- `gcommon/v1/common/mfa_method.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_mfa_request.proto
// version: 1.0.0
// guid: a628ba55-dd40-4025-bd1b-a634add55417
// file: proto/gcommon/v1/common/verify_mfa_request.proto
//
// Request definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/mfa_method.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyMfaRequest {
  // User ID
  string user_id = 1 [
      (buf.validate.field).string.pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
      (buf.validate.field).required = true
    ];

  // MFA verification code
  string code = 2;

  // Method being verified
  MfaMethod method = 3;

  // Context for the verification (login, transaction, etc.)
  string context = 4;
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### verify_mfa_response.proto {#verify_mfa_response}

**Path**: `gcommon/v1/common/verify_mfa_response.proto` **Package**: `gcommon.v1.common` **Lines**: 35

**Messages** (1): `VerifyMfaResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/types/verify_mfa_response.proto
// version: 1.0.0
// guid: 352b7b8d-1237-45ac-89b7-63228d94c5d0
// file: proto/gcommon/v1/common/verify_mfa_response.proto
//
// Response definitions for auth module

//
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message VerifyMfaResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  string error_message = 2 [(buf.validate.field).string.min_len = 1];

  // Remaining attempts (for rate limiting)
  int32 remaining_attempts = 3 [(buf.validate.field).int32.gte = 0];

  // Session token if successful
  string session_token = 4 [(buf.validate.field).string.min_len = 1];
}

// Implement the actual protobuf definitions according to the auth module requirements
// This file needs proper implementation
```

---

### watch_request.proto {#watch_request}

**Path**: `gcommon/v1/common/watch_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `HealthWatchRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/watch_request.proto
// version: 1.0.0
// guid: dc2cc626-d629-4419-8765-3f7cd4010a51
//
// Watch request message definition for streaming health updates
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message HealthWatchRequest {
  // Service name to watch (empty for all services)
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### watch_response.proto {#watch_response}

**Path**: `gcommon/v1/common/watch_response.proto` **Package**: `gcommon.v1.common` **Lines**: 58

**Messages** (1): `WatchResponse`

**Imports** (8):

- `gcommon/v1/common/check_result.proto`
- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_metrics.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/duration.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/watch_response.proto
// version: 1.0.0
// guid: 63859080-ce23-4630-b180-012a9c86ae1f
//
// Watch response message definition for streaming health updates
//
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/check_result.proto";
import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_metrics.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * WatchResponse represents a streaming health status update
 * containing real-time health information for services.
 *
 * This message provides:
 * - Real-time health status changes
 * - Service-specific health updates
 * - Detailed check results and metrics
 * - Error information for unhealthy services
 */
message WatchResponse {
  // Overall health status
  CommonHealthStatus status = 1;

  // Service name
  string service = 2 [(buf.validate.field).string.min_len = 1];

  // Check timestamp
  google.protobuf.Timestamp timestamp = 3;

  // Response time
  google.protobuf.Duration response_time = 4;

  // Detailed check results
  repeated CheckResult check_results = 5 [(buf.validate.field).repeated.min_items = 1];

  // Health message
  string message = 6 [(buf.validate.field).string.min_len = 1];

  // Error information if unhealthy
  gcommon.v1.common.Error error = 7;

  // Health metrics
  HealthMetrics metrics = 8;
}
```

---

### write_log_request.proto {#write_log_request}

**Path**: `gcommon/v1/common/write_log_request.proto` **Package**: `gcommon.v1.common` **Lines**: 31

**Messages** (1): `WriteLogRequest`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/write_log_request.proto
// version: 1.0.0
// guid: 7f8e9d0c-1b2a-3645-7e8f-9a0b1c2d3e4f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * WriteLogRequest defines the request for writing a log entry.
 */
message WriteLogRequest {
  // Log level (e.g., "INFO", "ERROR", "DEBUG")
  string level = 1 [(buf.validate.field).string.min_len = 1];

  // Log message
  string message = 2 [(buf.validate.field).string.min_len = 1];

  // Source component or service
  string source = 3 [(buf.validate.field).string.min_len = 1];

  // Additional metadata
  map<string, string> metadata = 4;
}
```

---

### write_log_response.proto {#write_log_response}

**Path**: `gcommon/v1/common/write_log_response.proto` **Package**: `gcommon.v1.common` **Lines**: 28

**Messages** (1): `WriteLogResponse`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/write_log_response.proto
// version: 1.0.0
// guid: 8f9e0d1c-2b3a-4756-8e9f-0a1b2c3d4e5f

edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * WriteLogResponse defines the response from writing a log entry.
 */
message WriteLogResponse {
  // Status of the write operation
  string status = 1 [(buf.validate.field).string.min_len = 1];

  // Log entry ID if applicable
  string log_id = 2 [(buf.validate.field).string.min_len = 1];

  // Error message if any
  string error = 3 [(buf.validate.field).string.min_len = 1];
}
```

---

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

### get_service_health_request.proto {#get_service_health_request}

**Path**: `gcommon/v1/common/get_service_health_request.proto` **Package**: `gcommon.v1.common` **Lines**: 26

**Messages** (1): `GetServiceHealthRequest`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_service_health_request.proto
// version: 1.0.0
// guid: 46ca267d-39dc-40ba-a77d-238f56c0f282
//
// Get service health request message definition
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message GetServiceHealthRequest {
  // Service name
  string service = 1 [(buf.validate.field).string.min_len = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### get_service_health_response.proto {#get_service_health_response}

**Path**: `gcommon/v1/common/get_service_health_response.proto` **Package**: `gcommon.v1.common` **Lines**: 29

**Messages** (1): `GetServiceHealthResponse`

**Imports** (4):

- `gcommon/v1/common/error.proto`
- `gcommon/v1/common/health_status.proto`
- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/get_service_health_response.proto
// version: 1.0.1
// guid: eb2e3f53-909e-4bd0-a9e8-3162f317a1ae
edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/error.proto";
import "gcommon/v1/common/health_status.proto";
import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Response message for service health status requests.
 * Provides health status for a specific service.
 */
message GetServiceHealthResponse {
  // Health status
  gcommon.v1.common.CommonHealthStatus status = 1;

  // Last check timestamp
  google.protobuf.Timestamp last_check = 2;

  // Error information if unhealthy
  gcommon.v1.common.Error error = 3;
}
```

---

### list_services_request.proto {#list_services_request}

**Path**: `gcommon/v1/common/list_services_request.proto` **Package**: `gcommon.v1.common` **Lines**: 21

**Messages** (1): `ListServicesRequest`

**Imports** (2):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_services_request.proto
// version: 1.0.1
// guid: ef4885eb-ad77-4dff-a074-83ad474e25a2
//
// List services request message definition
//

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListServicesRequest {
  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 1;
}
```

---

### list_services_response.proto {#list_services_response}

**Path**: `gcommon/v1/common/list_services_response.proto` **Package**: `gcommon.v1.common` **Lines**: 23

**Messages** (1): `ListServicesResponse`

**Imports** (3):

- `gcommon/v1/common/request_metadata.proto`
- `google/protobuf/go_features.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/list_services_response.proto
// version: 1.0.0
// guid: 09285493-9262-4105-aec3-9a02d03db370

edition = "2023";

package gcommon.v1.common;

import "gcommon/v1/common/request_metadata.proto";
import "google/protobuf/go_features.proto";
import "buf/validate/validate.proto";


option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

message ListServicesResponse {
  // List of service names
  repeated string services = 1 [(buf.validate.field).repeated.min_items = 1];

  // Request metadata
  gcommon.v1.common.RequestMetadata metadata = 2;
}
```

---

### service_version.proto {#service_version}

**Path**: `gcommon/v1/common/service_version.proto` **Package**: `gcommon.v1.common` **Lines**: 38

**Messages** (1): `ServiceVersion`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `buf/validate/validate.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/common/service_version.proto
// version: 1.0.0
// guid: c43e033c-3b21-4e79-b0e3-b4eee94d8cf1
edition = "2023";

package gcommon.v1.common;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/common";

/**
 * Service version information for deployment tracking and compatibility.
 * Provides comprehensive build and version metadata for service
 * identification, debugging, and compatibility checking.
 */
message ServiceVersion {
  // Service name identifier
  string name = 1 [
      (buf.validate.field).string.min_len = 1,
      (buf.validate.field).string.max_len = 100
    ];

  // Semantic version string (e.g., "1.2.3")
  string version = 2;

  // Git commit hash used for the build
  string commit = 3;

  // Timestamp when the service was built
  google.protobuf.Timestamp build_time = 4;

  // Go version used for compilation
  string go_version = 5;
}
```

---
