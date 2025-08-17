# Protocol Buffer Documentation

Generated on: 2025-08-09 22:36:30

## Overview

This documentation covers 1304 protocol buffer files organized into 54 modules, containing:

- **1372** message definitions
- **25** service definitions
- ⚠️ **179** issues requiring attention

## Modules

### [auth](./auth.md)

- **Files**: 43
- **Messages**: 34
- **Services**: 0
- ⚠️ **Issues**: 8

**Proto Files**:

- [auth_context.proto](./auth.md#auth_context)
- [auth_method.proto](./auth.md#auth_method)
- [auth_provider.proto](./auth.md#auth_provider)
- [auth_token.proto](./auth.md#auth_token) ⚠️ 2 issues
- [claims.proto](./auth.md#claims)
- [grant_type.proto](./auth.md#grant_type) ⚠️ 1 issues
- [group.proto](./auth.md#group)
- [jwt_credentials.proto](./auth.md#jwt_credentials)
- [mfa_method.proto](./auth.md#mfa_method)
- [mfa_type.proto](./auth.md#mfa_type)
- [oauth2_credentials.proto](./auth.md#oauth2_credentials)
- [oauth2_flow_type.proto](./auth.md#oauth2_flow_type)
- [oauth_client.proto](./auth.md#oauth_client)
- [password_credentials.proto](./auth.md#password_credentials)
- [password_policy.proto](./auth.md#password_policy) ⚠️ 2 issues
- [permission.proto](./auth.md#permission)
- [permission_grant.proto](./auth.md#permission_grant)
- [permission_metadata.proto](./auth.md#permission_metadata)
- [permission_scope.proto](./auth.md#permission_scope)
- [permission_type.proto](./auth.md#permission_type) ⚠️ 1 issues
- [provider_type.proto](./auth.md#provider_type)
- [refresh_token.proto](./auth.md#refresh_token)
- [role.proto](./auth.md#role)
- [role_assignment.proto](./auth.md#role_assignment)
- [role_metadata.proto](./auth.md#role_metadata)
- [role_scope.proto](./auth.md#role_scope)
- [scope_type.proto](./auth.md#scope_type)
- [security_context.proto](./auth.md#security_context)
- [security_policy.proto](./auth.md#security_policy)
- [session.proto](./auth.md#session)
- [session_info.proto](./auth.md#session_info)
- [session_metadata.proto](./auth.md#session_metadata)
- [session_status.proto](./auth.md#session_status)
- [token.proto](./auth.md#token)
- [token_info.proto](./auth.md#token_info)
- [token_metadata.proto](./auth.md#token_metadata)
- [token_status.proto](./auth.md#token_status)
- [token_type.proto](./auth.md#token_type)
- [user.proto](./auth.md#user)
- [user_info.proto](./auth.md#user_info)
- [user_metadata.proto](./auth.md#user_metadata)
- [user_profile.proto](./auth.md#user_profile) ⚠️ 2 issues
- [user_status.proto](./auth.md#user_status)

### [auth_api_1](./auth_api_1.md)

- **Files**: 50
- **Messages**: 53
- **Services**: 0
- ⚠️ **Issues**: 2

**Proto Files**:

- [api_key.proto](./auth_api_1.md#api_key)
- [api_key_credentials.proto](./auth_api_1.md#api_key_credentials)
- [assign_role_request.proto](./auth_api_1.md#assign_role_request)
- [assign_role_response.proto](./auth_api_1.md#assign_role_response)
- [authenticate_request.proto](./auth_api_1.md#authenticate_request)
- [authenticate_response.proto](./auth_api_1.md#authenticate_response)
- [authorize_request.proto](./auth_api_1.md#authorize_request)
- [authorize_response.proto](./auth_api_1.md#authorize_response)
- [change_password_request.proto](./auth_api_1.md#change_password_request)
- [change_password_response.proto](./auth_api_1.md#change_password_response)
- [check_permission_request.proto](./auth_api_1.md#check_permission_request)
- [check_permission_response.proto](./auth_api_1.md#check_permission_response)
- [complete_password_reset_request.proto](./auth_api_1.md#complete_password_reset_request)
- [complete_password_reset_response.proto](./auth_api_1.md#complete_password_reset_response)
- [create_permission_request.proto](./auth_api_1.md#create_permission_request)
- [create_role_request.proto](./auth_api_1.md#create_role_request) ⚠️ 1 issues
- [create_role_response.proto](./auth_api_1.md#create_role_response)
- [create_session_request.proto](./auth_api_1.md#create_session_request)
- [create_session_response.proto](./auth_api_1.md#create_session_response)
- [create_user_request.proto](./auth_api_1.md#create_user_request)
- [create_user_response.proto](./auth_api_1.md#create_user_response)
- [delete_permission_request.proto](./auth_api_1.md#delete_permission_request)
- [delete_role_request.proto](./auth_api_1.md#delete_role_request) ⚠️ 1 issues
- [delete_role_response.proto](./auth_api_1.md#delete_role_response)
- [delete_session_request.proto](./auth_api_1.md#delete_session_request)
- [delete_session_response.proto](./auth_api_1.md#delete_session_response)
- [delete_user_request.proto](./auth_api_1.md#delete_user_request)
- [delete_user_response.proto](./auth_api_1.md#delete_user_response)
- [disable_2fa_request.proto](./auth_api_1.md#disable_2fa_request)
- [disable_mfa_request.proto](./auth_api_1.md#disable_mfa_request)
- [disable_mfa_response.proto](./auth_api_1.md#disable_mfa_response)
- [enable_2fa_request.proto](./auth_api_1.md#enable_2fa_request)
- [enable_mfa_request.proto](./auth_api_1.md#enable_mfa_request)
- [enable_mfa_response.proto](./auth_api_1.md#enable_mfa_response)
- [generate_api_key_request.proto](./auth_api_1.md#generate_api_key_request)
- [generate_api_key_response.proto](./auth_api_1.md#generate_api_key_response)
- [get_api_key_request.proto](./auth_api_1.md#get_api_key_request)
- [get_api_key_response.proto](./auth_api_1.md#get_api_key_response)
- [get_permission_request.proto](./auth_api_1.md#get_permission_request)
- [get_permission_response.proto](./auth_api_1.md#get_permission_response)
- [get_role_request.proto](./auth_api_1.md#get_role_request)
- [get_role_response.proto](./auth_api_1.md#get_role_response)
- [get_session_request.proto](./auth_api_1.md#get_session_request)
- [get_session_response.proto](./auth_api_1.md#get_session_response)
- [get_system_stats_request.proto](./auth_api_1.md#get_system_stats_request)
- [get_system_stats_response.proto](./auth_api_1.md#get_system_stats_response)
- [get_user_info_request.proto](./auth_api_1.md#get_user_info_request)
- [get_user_info_response.proto](./auth_api_1.md#get_user_info_response)
- [get_user_permissions_request.proto](./auth_api_1.md#get_user_permissions_request)
- [get_user_permissions_response.proto](./auth_api_1.md#get_user_permissions_response)

### [auth_api_2](./auth_api_2.md)

- **Files**: 50
- **Messages**: 52
- **Services**: 0
- ⚠️ **Issues**: 4

**Proto Files**:

- [get_user_request.proto](./auth_api_2.md#get_user_request)
- [get_user_response.proto](./auth_api_2.md#get_user_response)
- [get_user_roles_request.proto](./auth_api_2.md#get_user_roles_request)
- [get_user_roles_response.proto](./auth_api_2.md#get_user_roles_response)
- [grant_permission_request.proto](./auth_api_2.md#grant_permission_request)
- [grant_permission_response.proto](./auth_api_2.md#grant_permission_response)
- [health_check_request.proto](./auth_api_2.md#health_check_request)
- [health_check_response.proto](./auth_api_2.md#health_check_response)
- [initiate_password_reset_request.proto](./auth_api_2.md#initiate_password_reset_request)
- [initiate_password_reset_response.proto](./auth_api_2.md#initiate_password_reset_response)
- [invalidate_user_sessions_request.proto](./auth_api_2.md#invalidate_user_sessions_request)
- [list_api_keys_request.proto](./auth_api_2.md#list_api_keys_request)
- [list_api_keys_response.proto](./auth_api_2.md#list_api_keys_response)
- [list_permissions_request.proto](./auth_api_2.md#list_permissions_request)
- [list_permissions_response.proto](./auth_api_2.md#list_permissions_response)
- [list_roles_request.proto](./auth_api_2.md#list_roles_request) ⚠️ 1 issues
- [list_roles_response.proto](./auth_api_2.md#list_roles_response) ⚠️ 1 issues
- [list_sessions_request.proto](./auth_api_2.md#list_sessions_request)
- [list_sessions_response.proto](./auth_api_2.md#list_sessions_response)
- [list_user_sessions_request.proto](./auth_api_2.md#list_user_sessions_request)
- [list_user_sessions_response.proto](./auth_api_2.md#list_user_sessions_response)
- [list_users_request.proto](./auth_api_2.md#list_users_request)
- [list_users_response.proto](./auth_api_2.md#list_users_response)
- [logout_request.proto](./auth_api_2.md#logout_request)
- [logout_response.proto](./auth_api_2.md#logout_response)
- [refresh_token_request.proto](./auth_api_2.md#refresh_token_request)
- [refresh_token_response.proto](./auth_api_2.md#refresh_token_response) ⚠️ 1 issues
- [register_user_request.proto](./auth_api_2.md#register_user_request)
- [register_user_response.proto](./auth_api_2.md#register_user_response)
- [remove_role_request.proto](./auth_api_2.md#remove_role_request)
- [remove_role_response.proto](./auth_api_2.md#remove_role_response)
- [resend_verification_request.proto](./auth_api_2.md#resend_verification_request)
- [reset_password_request.proto](./auth_api_2.md#reset_password_request)
- [reset_password_response.proto](./auth_api_2.md#reset_password_response)
- [revoke_api_key_request.proto](./auth_api_2.md#revoke_api_key_request)
- [revoke_api_key_response.proto](./auth_api_2.md#revoke_api_key_response)
- [revoke_permission_request.proto](./auth_api_2.md#revoke_permission_request)
- [revoke_permission_response.proto](./auth_api_2.md#revoke_permission_response)
- [revoke_role_request.proto](./auth_api_2.md#revoke_role_request)
- [revoke_role_response.proto](./auth_api_2.md#revoke_role_response)
- [revoke_token_request.proto](./auth_api_2.md#revoke_token_request)
- [revoke_token_response.proto](./auth_api_2.md#revoke_token_response)
- [send_verification_email_request.proto](./auth_api_2.md#send_verification_email_request)
- [send_verification_email_response.proto](./auth_api_2.md#send_verification_email_response)
- [terminate_session_request.proto](./auth_api_2.md#terminate_session_request)
- [terminate_session_response.proto](./auth_api_2.md#terminate_session_response)
- [update_permission_request.proto](./auth_api_2.md#update_permission_request)
- [update_role_request.proto](./auth_api_2.md#update_role_request) ⚠️ 1 issues
- [update_role_response.proto](./auth_api_2.md#update_role_response)
- [update_session_request.proto](./auth_api_2.md#update_session_request)

### [auth_api_3](./auth_api_3.md)

- **Files**: 14
- **Messages**: 14
- **Services**: 0

**Proto Files**:

- [update_session_response.proto](./auth_api_3.md#update_session_response)
- [update_user_request.proto](./auth_api_3.md#update_user_request)
- [update_user_response.proto](./auth_api_3.md#update_user_response)
- [validate_session_request.proto](./auth_api_3.md#validate_session_request)
- [validate_session_response.proto](./auth_api_3.md#validate_session_response)
- [validate_token_request.proto](./auth_api_3.md#validate_token_request)
- [validate_token_response.proto](./auth_api_3.md#validate_token_response)
- [verify_2fa_request.proto](./auth_api_3.md#verify_2fa_request)
- [verify_credentials_request.proto](./auth_api_3.md#verify_credentials_request)
- [verify_credentials_response.proto](./auth_api_3.md#verify_credentials_response)
- [verify_email_request.proto](./auth_api_3.md#verify_email_request)
- [verify_email_response.proto](./auth_api_3.md#verify_email_response)
- [verify_mfa_request.proto](./auth_api_3.md#verify_mfa_request)
- [verify_mfa_response.proto](./auth_api_3.md#verify_mfa_response)

### [auth_config](./auth_config.md)

- **Files**: 9
- **Messages**: 9
- **Services**: 0
- ⚠️ **Issues**: 8

**Proto Files**:

- [auth_config.proto](./auth_config.md#auth_config)
- [get_auth_config_request.proto](./auth_config.md#get_auth_config_request)
- [jwt_config.proto](./auth_config.md#jwt_config)
- [ldap_config.proto](./auth_config.md#ldap_config) ⚠️ 2 issues
- [mfa_config.proto](./auth_config.md#mfa_config) ⚠️ 2 issues
- [oauth2_config.proto](./auth_config.md#oauth2_config)
- [rate_limit_config.proto](./auth_config.md#rate_limit_config)
- [saml_config.proto](./auth_config.md#saml_config) ⚠️ 2 issues
- [session_config.proto](./auth_config.md#session_config) ⚠️ 2 issues

### [auth_events](./auth_events.md)

- **Files**: 3
- **Messages**: 2
- **Services**: 0

**Proto Files**:

- [audit_action.proto](./auth_events.md#audit_action)
- [audit_event.proto](./auth_events.md#audit_event)
- [audit_log.proto](./auth_events.md#audit_log)

### [auth_services](./auth_services.md)

- **Files**: 4
- **Messages**: 0
- **Services**: 4

**Proto Files**:

- [auth_admin_service.proto](./auth_services.md#auth_admin_service)
- [auth_service.proto](./auth_services.md#auth_service)
- [authorization_service.proto](./auth_services.md#authorization_service)
- [session_service.proto](./auth_services.md#session_service)

### [cache](./cache.md)

- **Files**: 7
- **Messages**: 7
- **Services**: 0

**Proto Files**:

- [cache_entry.proto](./cache.md#cache_entry)
- [cache_info.proto](./cache.md#cache_info)
- [cache_metrics.proto](./cache.md#cache_metrics)
- [cache_operation_result.proto](./cache.md#cache_operation_result)
- [cache_stats.proto](./cache.md#cache_stats)
- [eviction_result.proto](./cache.md#eviction_result)
- [set_options.proto](./cache.md#set_options)

### [cache_api_1](./cache_api_1.md)

- **Files**: 50
- **Messages**: 52
- **Services**: 0

**Proto Files**:

- [append_request.proto](./cache_api_1.md#append_request)
- [backup_request.proto](./cache_api_1.md#backup_request)
- [clear_request.proto](./cache_api_1.md#clear_request)
- [clear_response.proto](./cache_api_1.md#clear_response)
- [create_namespace_request.proto](./cache_api_1.md#create_namespace_request)
- [create_namespace_response.proto](./cache_api_1.md#create_namespace_response)
- [decrement_request.proto](./cache_api_1.md#decrement_request)
- [decrement_response.proto](./cache_api_1.md#decrement_response)
- [defrag_request.proto](./cache_api_1.md#defrag_request)
- [delete_multiple_request.proto](./cache_api_1.md#delete_multiple_request)
- [delete_multiple_response.proto](./cache_api_1.md#delete_multiple_response)
- [delete_namespace_request.proto](./cache_api_1.md#delete_namespace_request)
- [delete_request.proto](./cache_api_1.md#delete_request)
- [delete_response.proto](./cache_api_1.md#delete_response)
- [exists_request.proto](./cache_api_1.md#exists_request)
- [exists_response.proto](./cache_api_1.md#exists_response)
- [expire_request.proto](./cache_api_1.md#expire_request)
- [export_request.proto](./cache_api_1.md#export_request)
- [flush_request.proto](./cache_api_1.md#flush_request)
- [flush_response.proto](./cache_api_1.md#flush_response)
- [gc_request.proto](./cache_api_1.md#gc_request)
- [get_memory_usage_request.proto](./cache_api_1.md#get_memory_usage_request)
- [get_memory_usage_response.proto](./cache_api_1.md#get_memory_usage_response)
- [get_multiple_request.proto](./cache_api_1.md#get_multiple_request)
- [get_multiple_response.proto](./cache_api_1.md#get_multiple_response)
- [get_namespace_stats_request.proto](./cache_api_1.md#get_namespace_stats_request)
- [get_namespace_stats_response.proto](./cache_api_1.md#get_namespace_stats_response)
- [get_request.proto](./cache_api_1.md#get_request)
- [get_response.proto](./cache_api_1.md#get_response)
- [get_stats_response.proto](./cache_api_1.md#get_stats_response)
- [health_check_request.proto](./cache_api_1.md#health_check_request)
- [import_request.proto](./cache_api_1.md#import_request)
- [increment_request.proto](./cache_api_1.md#increment_request)
- [increment_response.proto](./cache_api_1.md#increment_response)
- [info_request.proto](./cache_api_1.md#info_request)
- [keys_request.proto](./cache_api_1.md#keys_request)
- [keys_response.proto](./cache_api_1.md#keys_response)
- [list_namespaces_request.proto](./cache_api_1.md#list_namespaces_request)
- [list_namespaces_response.proto](./cache_api_1.md#list_namespaces_response)
- [list_subscriptions_request.proto](./cache_api_1.md#list_subscriptions_request)
- [lock_request.proto](./cache_api_1.md#lock_request)
- [mget_request.proto](./cache_api_1.md#mget_request)
- [optimize_request.proto](./cache_api_1.md#optimize_request)
- [pipeline_request.proto](./cache_api_1.md#pipeline_request)
- [prepend_request.proto](./cache_api_1.md#prepend_request)
- [publish_request.proto](./cache_api_1.md#publish_request)
- [restore_request.proto](./cache_api_1.md#restore_request)
- [scan_request.proto](./cache_api_1.md#scan_request)
- [set_multiple_request.proto](./cache_api_1.md#set_multiple_request)
- [set_multiple_response.proto](./cache_api_1.md#set_multiple_response)

### [cache_api_2](./cache_api_2.md)

- **Files**: 11
- **Messages**: 11
- **Services**: 0

**Proto Files**:

- [set_request.proto](./cache_api_2.md#set_request)
- [set_response.proto](./cache_api_2.md#set_response)
- [stats_request.proto](./cache_api_2.md#stats_request)
- [subscribe_request.proto](./cache_api_2.md#subscribe_request)
- [touch_expiration_response.proto](./cache_api_2.md#touch_expiration_response)
- [transaction_request.proto](./cache_api_2.md#transaction_request)
- [ttl_request.proto](./cache_api_2.md#ttl_request)
- [unlock_request.proto](./cache_api_2.md#unlock_request)
- [unsubscribe_request.proto](./cache_api_2.md#unsubscribe_request)
- [unwatch_request.proto](./cache_api_2.md#unwatch_request)
- [watch_request.proto](./cache_api_2.md#watch_request)

### [cache_config](./cache_config.md)

- **Files**: 3
- **Messages**: 3
- **Services**: 0

**Proto Files**:

- [cache_config.proto](./cache_config.md#cache_config)
- [configure_policy_request.proto](./cache_config.md#configure_policy_request)
- [configure_policy_response.proto](./cache_config.md#configure_policy_response)

### [cache_services](./cache_services.md)

- **Files**: 2
- **Messages**: 0
- **Services**: 2

**Proto Files**:

- [cache_admin_service.proto](./cache_services.md#cache_admin_service)
- [cache_service.proto](./cache_services.md#cache_service)

### [common](./common.md)

- **Files**: 40
- **Messages**: 30
- **Services**: 0
- ⚠️ **Issues**: 1

**Proto Files**:

- [ack_mode.proto](./common.md#ack_mode)
- [audit_log.proto](./common.md#audit_log)
- [audit_result.proto](./common.md#audit_result)
- [batch_operation.proto](./common.md#batch_operation)
- [batch_options.proto](./common.md#batch_options)
- [cache_policy.proto](./common.md#cache_policy)
- [circuit_breaker_config.proto](./common.md#circuit_breaker_config)
- [circuit_breaker_state.proto](./common.md#circuit_breaker_state)
- [client_info.proto](./common.md#client_info)
- [config_value.proto](./common.md#config_value)
- [debug_info.proto](./common.md#debug_info)
- [error.proto](./common.md#error)
- [error_code.proto](./common.md#error_code) ⚠️ 1 issues
- [eviction_policy.proto](./common.md#eviction_policy)
- [expiration_policy.proto](./common.md#expiration_policy)
- [filter_operation.proto](./common.md#filter_operation)
- [filter_options.proto](./common.md#filter_options)
- [filter_value.proto](./common.md#filter_value)
- [health_status.proto](./common.md#health_status)
- [int64_array.proto](./common.md#int64_array)
- [key_value.proto](./common.md#key_value)
- [metric_point.proto](./common.md#metric_point)
- [paginated_response.proto](./common.md#paginated_response)
- [pagination.proto](./common.md#pagination)
- [pagination_options.proto](./common.md#pagination_options)
- [rate_limit.proto](./common.md#rate_limit)
- [request_metadata.proto](./common.md#request_metadata)
- [resource_reference.proto](./common.md#resource_reference)
- [resource_status.proto](./common.md#resource_status)
- [response_metadata.proto](./common.md#response_metadata)
- [retry_policy.proto](./common.md#retry_policy)
- [service_version.proto](./common.md#service_version)
- [sort.proto](./common.md#sort)
- [sort_direction.proto](./common.md#sort_direction)
- [string_array.proto](./common.md#string_array)
- [subscription_info.proto](./common.md#subscription_info)
- [subscription_options.proto](./common.md#subscription_options)
- [subscription_status.proto](./common.md#subscription_status)
- [time_range.proto](./common.md#time_range)
- [value_type.proto](./common.md#value_type)

### [config_1](./config_1.md)

- **Files**: 50
- **Messages**: 14
- **Services**: 0

**Proto Files**:

- [access_control.proto](./config_1.md#access_control)
- [access_restriction.proto](./config_1.md#access_restriction)
- [alert_severity.proto](./config_1.md#alert_severity)
- [alert_type.proto](./config_1.md#alert_type)
- [approval_info.proto](./config_1.md#approval_info)
- [approval_requirement.proto](./config_1.md#approval_requirement)
- [approval_status.proto](./config_1.md#approval_status)
- [backoff_strategy.proto](./config_1.md#backoff_strategy)
- [backup_frequency.proto](./config_1.md#backup_frequency)
- [cache_invalidation_trigger.proto](./config_1.md#cache_invalidation_trigger)
- [cache_refresh_strategy.proto](./config_1.md#cache_refresh_strategy)
- [change_type.proto](./config_1.md#change_type)
- [channel_type.proto](./config_1.md#channel_type)
- [compliance_reporting.proto](./config_1.md#compliance_reporting)
- [compression_type.proto](./config_1.md#compression_type)
- [conflict_resolution.proto](./config_1.md#conflict_resolution)
- [dependency_type.proto](./config_1.md#dependency_type)
- [deployment_status.proto](./config_1.md#deployment_status)
- [deprecation_info.proto](./config_1.md#deprecation_info)
- [deprecation_level.proto](./config_1.md#deprecation_level)
- [environment_status.proto](./config_1.md#environment_status)
- [environment_type.proto](./config_1.md#environment_type)
- [filter_action.proto](./config_1.md#filter_action)
- [filter_type.proto](./config_1.md#filter_type)
- [health_check_type.proto](./config_1.md#health_check_type)
- [health_state.proto](./config_1.md#health_state)
- [hook_error_handling.proto](./config_1.md#hook_error_handling)
- [hook_type.proto](./config_1.md#hook_type)
- [inheritance_filter.proto](./config_1.md#inheritance_filter)
- [inheritance_strategy.proto](./config_1.md#inheritance_strategy)
- [inheritance_transformation.proto](./config_1.md#inheritance_transformation)
- [merge_strategy.proto](./config_1.md#merge_strategy)
- [metadata_status.proto](./config_1.md#metadata_status)
- [monitoring_alert.proto](./config_1.md#monitoring_alert)
- [notification_channel.proto](./config_1.md#notification_channel)
- [notification_trigger.proto](./config_1.md#notification_trigger)
- [parameter_constraints.proto](./config_1.md#parameter_constraints)
- [parameter_type.proto](./config_1.md#parameter_type)
- [rate_limits.proto](./config_1.md#rate_limits)
- [reference_type.proto](./config_1.md#reference_type)
- [restore_point_status.proto](./config_1.md#restore_point_status)
- [restore_point_type.proto](./config_1.md#restore_point_type)
- [restriction_type.proto](./config_1.md#restriction_type)
- [rollback_info.proto](./config_1.md#rollback_info)
- [rollback_method.proto](./config_1.md#rollback_method)
- [rotation_frequency.proto](./config_1.md#rotation_frequency)
- [secret_backup_frequency.proto](./config_1.md#secret_backup_frequency)
- [secret_status.proto](./config_1.md#secret_status)
- [secret_type.proto](./config_1.md#secret_type)
- [secret_validation_result.proto](./config_1.md#secret_validation_result)

### [config_2](./config_2.md)

- **Files**: 41
- **Messages**: 22
- **Services**: 0
- ⚠️ **Issues**: 3

**Proto Files**:

- [secret_validation_result_type.proto](./config_2.md#secret_validation_result_type)
- [secret_validation_severity.proto](./config_2.md#secret_validation_severity)
- [synchronization_frequency.proto](./config_2.md#synchronization_frequency)
- [synchronization_target.proto](./config_2.md#synchronization_target)
- [template_change.proto](./config_2.md#template_change)
- [template_format.proto](./config_2.md#template_format)
- [template_hook.proto](./config_2.md#template_hook)
- [template_output.proto](./config_2.md#template_output)
- [template_parameter.proto](./config_2.md#template_parameter) ⚠️ 2 issues
- [template_status.proto](./config_2.md#template_status)
- [transformation_step.proto](./config_2.md#transformation_step)
- [transformation_type.proto](./config_2.md#transformation_type)
- [usage_statistics.proto](./config_2.md#usage_statistics)
- [usage_trend.proto](./config_2.md#usage_trend)
- [validation_result.proto](./config_2.md#validation_result)
- [validation_result_type.proto](./config_2.md#validation_result_type)
- [validation_rule.proto](./config_2.md#validation_rule)
- [validation_rule_severity.proto](./config_2.md#validation_rule_severity)
- [validation_rule_type.proto](./config_2.md#validation_rule_type)
- [validation_severity.proto](./config_2.md#validation_severity)
- [value_dependency.proto](./config_2.md#value_dependency)
- [value_history_entry.proto](./config_2.md#value_history_entry)
- [value_reference.proto](./config_2.md#value_reference)
- [value_source.proto](./config_2.md#value_source)
- [value_status.proto](./config_2.md#value_status)
- [value_usage_statistics.proto](./config_2.md#value_usage_statistics)
- [value_usage_trend.proto](./config_2.md#value_usage_trend)
- [value_validation_result.proto](./config_2.md#value_validation_result)
- [value_validation_result_type.proto](./config_2.md#value_validation_result_type)
- [value_validation_severity.proto](./config_2.md#value_validation_severity)
- [version_artifact.proto](./config_2.md#version_artifact)
- [version_compatibility_info.proto](./config_2.md#version_compatibility_info)
- [version_dependency.proto](./config_2.md#version_dependency) ⚠️ 1 issues
- [version_dependency_type.proto](./config_2.md#version_dependency_type)
- [version_deployment_info.proto](./config_2.md#version_deployment_info)
- [version_deployment_status.proto](./config_2.md#version_deployment_status)
- [version_health_status.proto](./config_2.md#version_health_status)
- [version_quality_issue.proto](./config_2.md#version_quality_issue)
- [version_quality_metrics.proto](./config_2.md#version_quality_metrics)
- [version_status.proto](./config_2.md#version_status)
- [version_type.proto](./config_2.md#version_type)

### [config_api](./config_api.md)

- **Files**: 4
- **Messages**: 4
- **Services**: 0

**Proto Files**:

- [get_schema_request.proto](./config_api.md#get_schema_request)
- [get_schema_response.proto](./config_api.md#get_schema_response)
- [health_check_request.proto](./config_api.md#health_check_request)
- [health_check_response.proto](./config_api.md#health_check_response)

### [config_config_1](./config_config_1.md)

- **Files**: 50
- **Messages**: 64
- **Services**: 0

**Proto Files**:

- [audit_settings.proto](./config_config_1.md#audit_settings)
- [backup_config_request.proto](./config_config_1.md#backup_config_request)
- [backup_settings.proto](./config_config_1.md#backup_settings)
- [batching_settings.proto](./config_config_1.md#batching_settings)
- [caching_settings.proto](./config_config_1.md#caching_settings)
- [compliance_settings.proto](./config_config_1.md#compliance_settings)
- [config_backup.proto](./config_config_1.md#config_backup)
- [config_change.proto](./config_config_1.md#config_change)
- [config_change_type.proto](./config_config_1.md#config_change_type)
- [config_data_type.proto](./config_config_1.md#config_data_type)
- [config_diff.proto](./config_config_1.md#config_diff)
- [config_entry.proto](./config_config_1.md#config_entry)
- [config_environment.proto](./config_config_1.md#config_environment)
- [config_schema.proto](./config_config_1.md#config_schema)
- [config_snapshot.proto](./config_config_1.md#config_snapshot)
- [config_stats.proto](./config_config_1.md#config_stats)
- [config_validation_error.proto](./config_config_1.md#config_validation_error)
- [config_validation_warning.proto](./config_config_1.md#config_validation_warning)
- [config_watch.proto](./config_config_1.md#config_watch)
- [decrypt_config_request.proto](./config_config_1.md#decrypt_config_request)
- [delete_config_request.proto](./config_config_1.md#delete_config_request)
- [encrypt_config_request.proto](./config_config_1.md#encrypt_config_request)
- [export_config_request.proto](./config_config_1.md#export_config_request)
- [get_config_history_request.proto](./config_config_1.md#get_config_history_request)
- [get_config_history_response.proto](./config_config_1.md#get_config_history_response)
- [get_config_request.proto](./config_config_1.md#get_config_request)
- [get_config_response.proto](./config_config_1.md#get_config_response)
- [get_config_stats_request.proto](./config_config_1.md#get_config_stats_request)
- [get_config_stats_response.proto](./config_config_1.md#get_config_stats_response)
- [get_multiple_config_request.proto](./config_config_1.md#get_multiple_config_request)
- [get_multiple_config_response.proto](./config_config_1.md#get_multiple_config_response)
- [import_config_request.proto](./config_config_1.md#import_config_request)
- [inheritance_settings.proto](./config_config_1.md#inheritance_settings)
- [list_config_request.proto](./config_config_1.md#list_config_request)
- [list_config_response.proto](./config_config_1.md#list_config_response)
- [monitoring_settings.proto](./config_config_1.md#monitoring_settings)
- [notification_settings.proto](./config_config_1.md#notification_settings)
- [reload_config_request.proto](./config_config_1.md#reload_config_request)
- [restore_config_request.proto](./config_config_1.md#restore_config_request)
- [retry_settings.proto](./config_config_1.md#retry_settings)
- [rollback_config_request.proto](./config_config_1.md#rollback_config_request)
- [rotation_settings.proto](./config_config_1.md#rotation_settings)
- [secret_audit_settings.proto](./config_config_1.md#secret_audit_settings)
- [secret_backup_settings.proto](./config_config_1.md#secret_backup_settings)
- [set_config_request.proto](./config_config_1.md#set_config_request)
- [set_config_response.proto](./config_config_1.md#set_config_response)
- [set_config_schema_request.proto](./config_config_1.md#set_config_schema_request)
- [set_multiple_config_request.proto](./config_config_1.md#set_multiple_config_request)
- [set_multiple_config_response.proto](./config_config_1.md#set_multiple_config_response)
- [synchronization_settings.proto](./config_config_1.md#synchronization_settings)

### [config_config_2](./config_config_2.md)

- **Files**: 8
- **Messages**: 8
- **Services**: 0

**Proto Files**:

- [transformation_settings.proto](./config_config_2.md#transformation_settings)
- [unwatch_config_request.proto](./config_config_2.md#unwatch_config_request)
- [validate_config_request.proto](./config_config_2.md#validate_config_request)
- [validate_config_response.proto](./config_config_2.md#validate_config_response)
- [validation_settings.proto](./config_config_2.md#validation_settings)
- [versioning_settings.proto](./config_config_2.md#versioning_settings)
- [watch_config_request.proto](./config_config_2.md#watch_config_request)
- [watch_config_response.proto](./config_config_2.md#watch_config_response)

### [config_events](./config_events.md)

- **Files**: 6
- **Messages**: 3
- **Services**: 0

**Proto Files**:

- [audit_level.proto](./config_events.md#audit_level)
- [audit_operation_type.proto](./config_events.md#audit_operation_type)
- [compliance_audit.proto](./config_events.md#compliance_audit)
- [rotation_event.proto](./config_events.md#rotation_event)
- [secret_audit_level.proto](./config_events.md#secret_audit_level)
- [version_promotion_event.proto](./config_events.md#version_promotion_event)

### [config_services](./config_services.md)

- **Files**: 2
- **Messages**: 0
- **Services**: 2

**Proto Files**:

- [config_admin_service.proto](./config_services.md#config_admin_service)
- [config_service.proto](./config_services.md#config_service)

### [database](./database.md)

- **Files**: 23
- **Messages**: 20
- **Services**: 0

**Proto Files**:

- [batch_execute_options.proto](./database.md#batch_execute_options)
- [batch_operation.proto](./database.md#batch_operation)
- [batch_operation_result.proto](./database.md#batch_operation_result)
- [batch_stats.proto](./database.md#batch_stats)
- [column_metadata.proto](./database.md#column_metadata)
- [connection_pool_info.proto](./database.md#connection_pool_info)
- [consistency_level.proto](./database.md#consistency_level)
- [database_info.proto](./database.md#database_info)
- [database_status.proto](./database.md#database_status)
- [database_status_code.proto](./database.md#database_status_code)
- [execute_options.proto](./database.md#execute_options)
- [execute_stats.proto](./database.md#execute_stats)
- [isolation_level.proto](./database.md#isolation_level)
- [migration_info.proto](./database.md#migration_info)
- [migration_script.proto](./database.md#migration_script)
- [mysql_status.proto](./database.md#mysql_status)
- [pool_stats.proto](./database.md#pool_stats)
- [query_options.proto](./database.md#query_options)
- [query_parameter.proto](./database.md#query_parameter)
- [query_stats.proto](./database.md#query_stats)
- [result_set.proto](./database.md#result_set)
- [row.proto](./database.md#row)
- [transaction_options.proto](./database.md#transaction_options)

### [database_api](./database_api.md)

- **Files**: 38
- **Messages**: 38
- **Services**: 0

**Proto Files**:

- [begin_transaction_request.proto](./database_api.md#begin_transaction_request)
- [begin_transaction_response.proto](./database_api.md#begin_transaction_response)
- [commit_transaction_request.proto](./database_api.md#commit_transaction_request)
- [create_database_request.proto](./database_api.md#create_database_request)
- [create_database_response.proto](./database_api.md#create_database_response)
- [create_schema_request.proto](./database_api.md#create_schema_request)
- [create_schema_response.proto](./database_api.md#create_schema_response)
- [drop_database_request.proto](./database_api.md#drop_database_request)
- [drop_schema_request.proto](./database_api.md#drop_schema_request)
- [execute_batch_request.proto](./database_api.md#execute_batch_request)
- [execute_batch_response.proto](./database_api.md#execute_batch_response)
- [execute_request.proto](./database_api.md#execute_request)
- [execute_response.proto](./database_api.md#execute_response)
- [get_connection_info_request.proto](./database_api.md#get_connection_info_request)
- [get_connection_info_response.proto](./database_api.md#get_connection_info_response)
- [get_database_info_request.proto](./database_api.md#get_database_info_request)
- [get_database_info_response.proto](./database_api.md#get_database_info_response)
- [get_migration_status_request.proto](./database_api.md#get_migration_status_request)
- [get_migration_status_response.proto](./database_api.md#get_migration_status_response)
- [health_check_request.proto](./database_api.md#health_check_request)
- [health_check_response.proto](./database_api.md#health_check_response)
- [list_databases_request.proto](./database_api.md#list_databases_request)
- [list_databases_response.proto](./database_api.md#list_databases_response)
- [list_migrations_request.proto](./database_api.md#list_migrations_request)
- [list_migrations_response.proto](./database_api.md#list_migrations_response)
- [list_schemas_request.proto](./database_api.md#list_schemas_request)
- [list_schemas_response.proto](./database_api.md#list_schemas_response)
- [query_request.proto](./database_api.md#query_request)
- [query_response.proto](./database_api.md#query_response)
- [query_row_request.proto](./database_api.md#query_row_request)
- [query_row_response.proto](./database_api.md#query_row_response)
- [revert_migration_request.proto](./database_api.md#revert_migration_request)
- [revert_migration_response.proto](./database_api.md#revert_migration_response)
- [rollback_transaction_request.proto](./database_api.md#rollback_transaction_request)
- [run_migration_request.proto](./database_api.md#run_migration_request)
- [run_migration_response.proto](./database_api.md#run_migration_response)
- [transaction_status_request.proto](./database_api.md#transaction_status_request)
- [transaction_status_response.proto](./database_api.md#transaction_status_response)

### [database_config](./database_config.md)

- **Files**: 3
- **Messages**: 3
- **Services**: 0

**Proto Files**:

- [cockroach_config.proto](./database_config.md#cockroach_config)
- [mysql_config.proto](./database_config.md#mysql_config)
- [pebble_config.proto](./database_config.md#pebble_config)

### [database_services](./database_services.md)

- **Files**: 4
- **Messages**: 0
- **Services**: 4

**Proto Files**:

- [database_admin_service.proto](./database_services.md#database_admin_service)
- [database_service.proto](./database_services.md#database_service)
- [migration_service.proto](./database_services.md#migration_service)
- [transaction_service.proto](./database_services.md#transaction_service)

### [health](./health.md)

- **Files**: 35
- **Messages**: 33
- **Services**: 2

**Proto Files**:

- [check_result.proto](./health.md#check_result)
- [configure_alerting_request.proto](./health.md#configure_alerting_request)
- [configure_alerting_response.proto](./health.md#configure_alerting_response)
- [disable_check_request.proto](./health.md#disable_check_request)
- [disable_check_response.proto](./health.md#disable_check_response)
- [enable_check_request.proto](./health.md#enable_check_request)
- [enable_check_response.proto](./health.md#enable_check_response)
- [get_check_status_request.proto](./health.md#get_check_status_request)
- [get_health_history_request.proto](./health.md#get_health_history_request)
- [get_health_metrics_request.proto](./health.md#get_health_metrics_request)
- [get_health_metrics_response.proto](./health.md#get_health_metrics_response)
- [get_health_request.proto](./health.md#get_health_request)
- [get_service_health_request.proto](./health.md#get_service_health_request)
- [get_service_health_response.proto](./health.md#get_service_health_response)
- [health_admin_service.proto](./health.md#health_admin_service)
- [health_check_request.proto](./health.md#health_check_request)
- [health_check_response.proto](./health.md#health_check_response)
- [health_metric_data.proto](./health.md#health_metric_data)
- [health_metrics.proto](./health.md#health_metrics)
- [health_service.proto](./health.md#health_service)
- [list_checks_request.proto](./health.md#list_checks_request)
- [list_services_request.proto](./health.md#list_services_request)
- [list_services_response.proto](./health.md#list_services_response)
- [register_check_request.proto](./health.md#register_check_request)
- [register_check_response.proto](./health.md#register_check_response)
- [reset_health_stats_request.proto](./health.md#reset_health_stats_request)
- [reset_health_stats_response.proto](./health.md#reset_health_stats_response)
- [run_check_request.proto](./health.md#run_check_request)
- [run_check_response.proto](./health.md#run_check_response)
- [set_health_request.proto](./health.md#set_health_request)
- [set_health_response.proto](./health.md#set_health_response)
- [unregister_check_request.proto](./health.md#unregister_check_request)
- [unregister_check_response.proto](./health.md#unregister_check_response)
- [watch_request.proto](./health.md#watch_request)
- [watch_response.proto](./health.md#watch_response)

### [log](./log.md)

- **Files**: 14
- **Messages**: 9
- **Services**: 0

**Proto Files**:

- [appender_config.proto](./log.md#appender_config)
- [appender_type.proto](./log.md#appender_type)
- [archive_criteria.proto](./log.md#archive_criteria)
- [compression_type.proto](./log.md#compression_type)
- [error_info.proto](./log.md#error_info)
- [filter_type.proto](./log.md#filter_type)
- [formatter_type.proto](./log.md#formatter_type)
- [log_entry.proto](./log.md#log_entry)
- [log_level.proto](./log.md#log_level)
- [log_sort_field.proto](./log.md#log_sort_field)
- [log_statistics.proto](./log.md#log_statistics)
- [logger_config.proto](./log.md#logger_config)
- [logger_status.proto](./log.md#logger_status)
- [source_location.proto](./log.md#source_location)

### [media](./media.md)

- **Files**: 10
- **Messages**: 7
- **Services**: 0

**Proto Files**:

- [audio_track.proto](./media.md#audio_track)
- [media_file.proto](./media.md#media_file)
- [media_metadata.proto](./media.md#media_metadata)
- [media_quality.proto](./media.md#media_quality)
- [media_type.proto](./media.md#media_type)
- [movie_info.proto](./media.md#movie_info)
- [quality_score.proto](./media.md#quality_score)
- [resolution.proto](./media.md#resolution)
- [series_info.proto](./media.md#series_info)
- [subtitle_track.proto](./media.md#subtitle_track)

### [metrics_1](./metrics_1.md)

- **Files**: 50
- **Messages**: 39
- **Services**: 0
- ⚠️ **Issues**: 8

**Proto Files**:

- [aggregation_type.proto](./metrics_1.md#aggregation_type)
- [alert_channel_type.proto](./metrics_1.md#alert_channel_type)
- [alert_notification.proto](./metrics_1.md#alert_notification)
- [alert_severity.proto](./metrics_1.md#alert_severity)
- [alert_state.proto](./metrics_1.md#alert_state)
- [alerting_condition.proto](./metrics_1.md#alerting_condition)
- [alerting_rule.proto](./metrics_1.md#alerting_rule)
- [backup_info.proto](./metrics_1.md#backup_info)
- [batch_options.proto](./metrics_1.md#batch_options)
- [batch_priority.proto](./metrics_1.md#batch_priority)
- [buffer_overflow_strategy.proto](./metrics_1.md#buffer_overflow_strategy)
- [change_type.proto](./metrics_1.md#change_type)
- [cleanup_strategy.proto](./metrics_1.md#cleanup_strategy)
- [comparison_operator.proto](./metrics_1.md#comparison_operator)
- [compression_type.proto](./metrics_1.md#compression_type)
- [counter_metric.proto](./metrics_1.md#counter_metric)
- [dashboard_type.proto](./metrics_1.md#dashboard_type)
- [deletion_options.proto](./metrics_1.md#deletion_options)
- [dry_run_result.proto](./metrics_1.md#dry_run_result)
- [error_stats.proto](./metrics_1.md#error_stats)
- [export_destination_update.proto](./metrics_1.md#export_destination_update)
- [export_format.proto](./metrics_1.md#export_format)
- [gauge_metric.proto](./metrics_1.md#gauge_metric)
- [gauge_operation.proto](./metrics_1.md#gauge_operation)
- [health_status.proto](./metrics_1.md#health_status)
- [histogram_bucket.proto](./metrics_1.md#histogram_bucket)
- [histogram_metric.proto](./metrics_1.md#histogram_metric)
- [metric_aggregation.proto](./metrics_1.md#metric_aggregation)
- [metric_aggregation_result.proto](./metrics_1.md#metric_aggregation_result) ⚠️ 3 issues
- [metric_bucket.proto](./metrics_1.md#metric_bucket)
- [metric_data.proto](./metrics_1.md#metric_data)
- [metric_family.proto](./metrics_1.md#metric_family) ⚠️ 5 issues
- [metric_filter.proto](./metrics_1.md#metric_filter)
- [metric_health.proto](./metrics_1.md#metric_health)
- [metric_label.proto](./metrics_1.md#metric_label)
- [metric_metadata.proto](./metrics_1.md#metric_metadata)
- [metric_quantile.proto](./metrics_1.md#metric_quantile)
- [metric_query.proto](./metrics_1.md#metric_query)
- [metric_sample.proto](./metrics_1.md#metric_sample)
- [metric_source.proto](./metrics_1.md#metric_source)
- [metric_stats.proto](./metrics_1.md#metric_stats)
- [metric_status.proto](./metrics_1.md#metric_status)
- [metric_type.proto](./metrics_1.md#metric_type)
- [metric_value.proto](./metrics_1.md#metric_value)
- [notification_type.proto](./metrics_1.md#notification_type)
- [numeric_format.proto](./metrics_1.md#numeric_format)
- [pagination_info.proto](./metrics_1.md#pagination_info)
- [performance_stats.proto](./metrics_1.md#performance_stats)
- [provider_info.proto](./metrics_1.md#provider_info)
- [provider_sort_field.proto](./metrics_1.md#provider_sort_field)

### [metrics_2](./metrics_2.md)

- **Files**: 35
- **Messages**: 22
- **Services**: 0

**Proto Files**:

- [provider_state.proto](./metrics_2.md#provider_state)
- [provider_status.proto](./metrics_2.md#provider_status)
- [provider_summary.proto](./metrics_2.md#provider_summary)
- [provider_type.proto](./metrics_2.md#provider_type)
- [query_operation.proto](./metrics_2.md#query_operation)
- [query_stats.proto](./metrics_2.md#query_stats)
- [recording_stats.proto](./metrics_2.md#recording_stats)
- [registration_action.proto](./metrics_2.md#registration_action)
- [resource_limits_summary.proto](./metrics_2.md#resource_limits_summary)
- [resource_limits_update.proto](./metrics_2.md#resource_limits_update)
- [retention_policy.proto](./metrics_2.md#retention_policy)
- [retention_policy_retentionpolicy.proto](./metrics_2.md#retention_policy_retentionpolicy)
- [retention_unit.proto](./metrics_2.md#retention_unit)
- [sample_rate.proto](./metrics_2.md#sample_rate)
- [scrape_job.proto](./metrics_2.md#scrape_job)
- [scrape_status.proto](./metrics_2.md#scrape_status)
- [scrape_target.proto](./metrics_2.md#scrape_target)
- [storage_backend.proto](./metrics_2.md#storage_backend)
- [stream_compression.proto](./metrics_2.md#stream_compression)
- [stream_qos.proto](./metrics_2.md#stream_qos)
- [summary_metric.proto](./metrics_2.md#summary_metric)
- [tag_updates.proto](./metrics_2.md#tag_updates)
- [time_range.proto](./metrics_2.md#time_range)
- [time_series.proto](./metrics_2.md#time_series)
- [time_unit.proto](./metrics_2.md#time_unit)
- [time_window.proto](./metrics_2.md#time_window)
- [timer_metric.proto](./metrics_2.md#timer_metric)
- [timestamp_range.proto](./metrics_2.md#timestamp_range)
- [top_metrics.proto](./metrics_2.md#top_metrics)
- [update_action.proto](./metrics_2.md#update_action)
- [update_options.proto](./metrics_2.md#update_options)
- [update_result.proto](./metrics_2.md#update_result)
- [update_strategy.proto](./metrics_2.md#update_strategy)
- [validation_result.proto](./metrics_2.md#validation_result)
- [visualization_type.proto](./metrics_2.md#visualization_type)

### [metrics_api_1](./metrics_api_1.md)

- **Files**: 50
- **Messages**: 123
- **Services**: 0

**Proto Files**:

- [create_metric_request.proto](./metrics_api_1.md#create_metric_request)
- [create_metric_response.proto](./metrics_api_1.md#create_metric_response)
- [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- [create_provider_response.proto](./metrics_api_1.md#create_provider_response)
- [delete_metric_request.proto](./metrics_api_1.md#delete_metric_request)
- [delete_metric_response.proto](./metrics_api_1.md#delete_metric_response)
- [delete_provider_request.proto](./metrics_api_1.md#delete_provider_request)
- [delete_provider_response.proto](./metrics_api_1.md#delete_provider_response)
- [export_metrics_request.proto](./metrics_api_1.md#export_metrics_request)
- [export_metrics_response.proto](./metrics_api_1.md#export_metrics_response)
- [get_alerting_rules_request.proto](./metrics_api_1.md#get_alerting_rules_request)
- [get_alerting_rules_response.proto](./metrics_api_1.md#get_alerting_rules_response)
- [get_metric_metadata_request.proto](./metrics_api_1.md#get_metric_metadata_request)
- [get_metric_metadata_response.proto](./metrics_api_1.md#get_metric_metadata_response)
- [get_metric_request.proto](./metrics_api_1.md#get_metric_request)
- [get_metric_response.proto](./metrics_api_1.md#get_metric_response)
- [get_metrics_request.proto](./metrics_api_1.md#get_metrics_request)
- [get_metrics_response.proto](./metrics_api_1.md#get_metrics_response)
- [get_metrics_summary_request.proto](./metrics_api_1.md#get_metrics_summary_request)
- [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- [get_provider_stats_request.proto](./metrics_api_1.md#get_provider_stats_request)
- [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- [get_stats_request.proto](./metrics_api_1.md#get_stats_request)
- [get_stats_response.proto](./metrics_api_1.md#get_stats_response)
- [health_check_request.proto](./metrics_api_1.md#health_check_request)
- [health_check_response.proto](./metrics_api_1.md#health_check_response)
- [import_metrics_request.proto](./metrics_api_1.md#import_metrics_request)
- [import_metrics_response.proto](./metrics_api_1.md#import_metrics_response)
- [list_metrics_request.proto](./metrics_api_1.md#list_metrics_request)
- [list_metrics_response.proto](./metrics_api_1.md#list_metrics_response)
- [list_providers_request.proto](./metrics_api_1.md#list_providers_request)
- [list_providers_response.proto](./metrics_api_1.md#list_providers_response)
- [query_metrics_request.proto](./metrics_api_1.md#query_metrics_request)
- [query_metrics_response.proto](./metrics_api_1.md#query_metrics_response)
- [record_counter_request.proto](./metrics_api_1.md#record_counter_request)
- [record_counter_response.proto](./metrics_api_1.md#record_counter_response)
- [record_gauge_request.proto](./metrics_api_1.md#record_gauge_request)
- [record_gauge_response.proto](./metrics_api_1.md#record_gauge_response)
- [record_histogram_request.proto](./metrics_api_1.md#record_histogram_request)
- [record_histogram_response.proto](./metrics_api_1.md#record_histogram_response)
- [record_metric_request.proto](./metrics_api_1.md#record_metric_request)
- [record_metric_response.proto](./metrics_api_1.md#record_metric_response)
- [record_metrics_request.proto](./metrics_api_1.md#record_metrics_request)
- [record_metrics_response.proto](./metrics_api_1.md#record_metrics_response)
- [record_summary_request.proto](./metrics_api_1.md#record_summary_request)
- [record_summary_response.proto](./metrics_api_1.md#record_summary_response)
- [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- [register_metric_response.proto](./metrics_api_1.md#register_metric_response)
- [reset_metrics_request.proto](./metrics_api_1.md#reset_metrics_request)
- [reset_metrics_response.proto](./metrics_api_1.md#reset_metrics_response)

### [metrics_api_2](./metrics_api_2.md)

- **Files**: 16
- **Messages**: 20
- **Services**: 0

**Proto Files**:

- [response_compression.proto](./metrics_api_2.md#response_compression)
- [set_alerting_rules_request.proto](./metrics_api_2.md#set_alerting_rules_request)
- [set_alerting_rules_response.proto](./metrics_api_2.md#set_alerting_rules_response)
- [set_metric_metadata_request.proto](./metrics_api_2.md#set_metric_metadata_request)
- [set_metric_metadata_response.proto](./metrics_api_2.md#set_metric_metadata_response)
- [start_scraping_request.proto](./metrics_api_2.md#start_scraping_request)
- [start_scraping_response.proto](./metrics_api_2.md#start_scraping_response)
- [stop_scraping_request.proto](./metrics_api_2.md#stop_scraping_request)
- [stop_scraping_response.proto](./metrics_api_2.md#stop_scraping_response)
- [stream_metrics_request.proto](./metrics_api_2.md#stream_metrics_request)
- [unregister_metric_request.proto](./metrics_api_2.md#unregister_metric_request)
- [unregister_metric_response.proto](./metrics_api_2.md#unregister_metric_response)
- [update_metric_request.proto](./metrics_api_2.md#update_metric_request)
- [update_metric_response.proto](./metrics_api_2.md#update_metric_response)
- [update_provider_request.proto](./metrics_api_2.md#update_provider_request)
- [update_provider_response.proto](./metrics_api_2.md#update_provider_response)

### [metrics_config](./metrics_config.md)

- **Files**: 24
- **Messages**: 24
- **Services**: 0
- ⚠️ **Issues**: 3

**Proto Files**:

- [apikey_config_update.proto](./metrics_config.md#apikey_config_update)
- [config_change.proto](./metrics_config.md#config_change)
- [export_config.proto](./metrics_config.md#export_config)
- [export_config_options.proto](./metrics_config.md#export_config_options) ⚠️ 3 issues
- [export_config_update.proto](./metrics_config.md#export_config_update)
- [get_metric_config_request.proto](./metrics_config.md#get_metric_config_request)
- [get_metric_config_response.proto](./metrics_config.md#get_metric_config_response)
- [get_scrape_config_request.proto](./metrics_config.md#get_scrape_config_request)
- [get_scrape_config_response.proto](./metrics_config.md#get_scrape_config_response)
- [import_config.proto](./metrics_config.md#import_config)
- [metric_config.proto](./metrics_config.md#metric_config)
- [open_telemetry_settings_update.proto](./metrics_config.md#open_telemetry_settings_update)
- [prometheus_settings_update.proto](./metrics_config.md#prometheus_settings_update)
- [provider_config_update.proto](./metrics_config.md#provider_config_update)
- [provider_settings_update.proto](./metrics_config.md#provider_settings_update)
- [retention_policy_retentionpolicyconfig.proto](./metrics_config.md#retention_policy_retentionpolicyconfig)
- [scrape_config.proto](./metrics_config.md#scrape_config)
- [security_config_update.proto](./metrics_config.md#security_config_update)
- [set_metric_config_request.proto](./metrics_config.md#set_metric_config_request)
- [set_metric_config_response.proto](./metrics_config.md#set_metric_config_response)
- [set_scrape_config_request.proto](./metrics_config.md#set_scrape_config_request)
- [set_scrape_config_response.proto](./metrics_config.md#set_scrape_config_response)
- [stats_dsettings_update.proto](./metrics_config.md#stats_dsettings_update)
- [tlsconfig_update.proto](./metrics_config.md#tlsconfig_update)

### [metrics_services](./metrics_services.md)

- **Files**: 2
- **Messages**: 0
- **Services**: 2

**Proto Files**:

- [metrics_admin_service.proto](./metrics_services.md#metrics_admin_service)
- [metrics_service.proto](./metrics_services.md#metrics_service)

### [notification](./notification.md)

- **Files**: 22
- **Messages**: 19
- **Services**: 1
- ⚠️ **Issues**: 1

**Proto Files**:

- [delete_notification_request.proto](./notification.md#delete_notification_request)
- [delete_notification_response.proto](./notification.md#delete_notification_response)
- [delivery_channel.proto](./notification.md#delivery_channel)
- [delivery_channel_type.proto](./notification.md#delivery_channel_type)
- [delivery_status.proto](./notification.md#delivery_status)
- [event_notification.proto](./notification.md#event_notification)
- [get_preferences_request.proto](./notification.md#get_preferences_request)
- [get_preferences_response.proto](./notification.md#get_preferences_response)
- [get_template_request.proto](./notification.md#get_template_request)
- [get_template_response.proto](./notification.md#get_template_response)
- [list_notifications_request.proto](./notification.md#list_notifications_request)
- [list_notifications_response.proto](./notification.md#list_notifications_response)
- [mark_as_read_request.proto](./notification.md#mark_as_read_request)
- [mark_as_read_response.proto](./notification.md#mark_as_read_response)
- [notification_message.proto](./notification.md#notification_message)
- [notification_service.proto](./notification.md#notification_service)
- [send_notification_request.proto](./notification.md#send_notification_request)
- [send_notification_response.proto](./notification.md#send_notification_response)
- [subscription_preferences.proto](./notification.md#subscription_preferences)
- [template.proto](./notification.md#template) ⚠️ 1 issues
- [update_preferences_request.proto](./notification.md#update_preferences_request)
- [update_preferences_response.proto](./notification.md#update_preferences_response)

### [organization](./organization.md)

- **Files**: 13
- **Messages**: 39
- **Services**: 0

**Proto Files**:

- [department.proto](./organization.md#department)
- [hierarchy_type.proto](./organization.md#hierarchy_type)
- [isolation_level.proto](./organization.md#isolation_level)
- [member_role.proto](./organization.md#member_role)
- [organization.proto](./organization.md#organization)
- [organization_hierarchy.proto](./organization.md#organization_hierarchy)
- [organization_member.proto](./organization.md#organization_member)
- [organization_status.proto](./organization.md#organization_status)
- [team.proto](./organization.md#team)
- [tenant.proto](./organization.md#tenant)
- [tenant_isolation.proto](./organization.md#tenant_isolation)
- [tenant_quota.proto](./organization.md#tenant_quota)
- [tenant_status.proto](./organization.md#tenant_status)

### [organization_api_1](./organization_api_1.md)

- **Files**: 50
- **Messages**: 50
- **Services**: 0

**Proto Files**:

- [add_member_request.proto](./organization_api_1.md#add_member_request)
- [add_member_response.proto](./organization_api_1.md#add_member_response)
- [create_department_request.proto](./organization_api_1.md#create_department_request)
- [create_department_response.proto](./organization_api_1.md#create_department_response)
- [create_organization_request.proto](./organization_api_1.md#create_organization_request)
- [create_organization_response.proto](./organization_api_1.md#create_organization_response)
- [create_team_request.proto](./organization_api_1.md#create_team_request)
- [create_team_response.proto](./organization_api_1.md#create_team_response)
- [create_tenant_request.proto](./organization_api_1.md#create_tenant_request)
- [create_tenant_response.proto](./organization_api_1.md#create_tenant_response)
- [delete_department_request.proto](./organization_api_1.md#delete_department_request)
- [delete_department_response.proto](./organization_api_1.md#delete_department_response)
- [delete_organization_request.proto](./organization_api_1.md#delete_organization_request)
- [delete_organization_response.proto](./organization_api_1.md#delete_organization_response)
- [delete_team_request.proto](./organization_api_1.md#delete_team_request)
- [delete_team_response.proto](./organization_api_1.md#delete_team_response)
- [delete_tenant_request.proto](./organization_api_1.md#delete_tenant_request)
- [delete_tenant_response.proto](./organization_api_1.md#delete_tenant_response)
- [get_department_request.proto](./organization_api_1.md#get_department_request)
- [get_department_response.proto](./organization_api_1.md#get_department_response)
- [get_hierarchy_request.proto](./organization_api_1.md#get_hierarchy_request)
- [get_hierarchy_response.proto](./organization_api_1.md#get_hierarchy_response)
- [get_organization_request.proto](./organization_api_1.md#get_organization_request)
- [get_organization_response.proto](./organization_api_1.md#get_organization_response)
- [get_team_request.proto](./organization_api_1.md#get_team_request)
- [get_team_response.proto](./organization_api_1.md#get_team_response)
- [get_tenant_isolation_request.proto](./organization_api_1.md#get_tenant_isolation_request)
- [get_tenant_isolation_response.proto](./organization_api_1.md#get_tenant_isolation_response)
- [get_tenant_request.proto](./organization_api_1.md#get_tenant_request)
- [get_tenant_response.proto](./organization_api_1.md#get_tenant_response)
- [get_tenant_usage_request.proto](./organization_api_1.md#get_tenant_usage_request)
- [get_tenant_usage_response.proto](./organization_api_1.md#get_tenant_usage_response)
- [list_departments_request.proto](./organization_api_1.md#list_departments_request)
- [list_departments_response.proto](./organization_api_1.md#list_departments_response)
- [list_members_request.proto](./organization_api_1.md#list_members_request)
- [list_members_response.proto](./organization_api_1.md#list_members_response)
- [list_organizations_request.proto](./organization_api_1.md#list_organizations_request)
- [list_organizations_response.proto](./organization_api_1.md#list_organizations_response)
- [list_teams_request.proto](./organization_api_1.md#list_teams_request)
- [list_teams_response.proto](./organization_api_1.md#list_teams_response)
- [list_tenants_request.proto](./organization_api_1.md#list_tenants_request)
- [list_tenants_response.proto](./organization_api_1.md#list_tenants_response)
- [remove_member_request.proto](./organization_api_1.md#remove_member_request)
- [remove_member_response.proto](./organization_api_1.md#remove_member_response)
- [update_department_request.proto](./organization_api_1.md#update_department_request)
- [update_department_response.proto](./organization_api_1.md#update_department_response)
- [update_hierarchy_request.proto](./organization_api_1.md#update_hierarchy_request)
- [update_hierarchy_response.proto](./organization_api_1.md#update_hierarchy_response)
- [update_member_request.proto](./organization_api_1.md#update_member_request)
- [update_member_response.proto](./organization_api_1.md#update_member_response)

### [organization_api_2](./organization_api_2.md)

- **Files**: 8
- **Messages**: 8
- **Services**: 0

**Proto Files**:

- [update_organization_request.proto](./organization_api_2.md#update_organization_request)
- [update_organization_response.proto](./organization_api_2.md#update_organization_response)
- [update_team_request.proto](./organization_api_2.md#update_team_request)
- [update_team_response.proto](./organization_api_2.md#update_team_response)
- [update_tenant_quota_request.proto](./organization_api_2.md#update_tenant_quota_request)
- [update_tenant_quota_response.proto](./organization_api_2.md#update_tenant_quota_response)
- [update_tenant_request.proto](./organization_api_2.md#update_tenant_request)
- [update_tenant_response.proto](./organization_api_2.md#update_tenant_response)

### [organization_config](./organization_config.md)

- **Files**: 7
- **Messages**: 21
- **Services**: 0

**Proto Files**:

- [configure_tenant_isolation_request.proto](./organization_config.md#configure_tenant_isolation_request)
- [configure_tenant_isolation_response.proto](./organization_config.md#configure_tenant_isolation_response)
- [get_organization_settings_request.proto](./organization_config.md#get_organization_settings_request)
- [get_organization_settings_response.proto](./organization_config.md#get_organization_settings_response)
- [organization_settings.proto](./organization_config.md#organization_settings)
- [update_organization_settings_request.proto](./organization_config.md#update_organization_settings_request)
- [update_organization_settings_response.proto](./organization_config.md#update_organization_settings_response)

### [organization_services](./organization_services.md)

- **Files**: 3
- **Messages**: 0
- **Services**: 3

**Proto Files**:

- [hierarchy_service.proto](./organization_services.md#hierarchy_service)
- [organization_service.proto](./organization_services.md#organization_service)
- [tenant_service.proto](./organization_services.md#tenant_service)

### [queue_1](./queue_1.md)

- **Files**: 50
- **Messages**: 36
- **Services**: 0
- ⚠️ **Issues**: 2

**Proto Files**:

- [ack_level.proto](./queue_1.md#ack_level)
- [ack_type.proto](./queue_1.md#ack_type)
- [acknowledgment.proto](./queue_1.md#acknowledgment)
- [acknowledgment_mode.proto](./queue_1.md#acknowledgment_mode) ⚠️ 1 issues
- [alert_condition.proto](./queue_1.md#alert_condition)
- [alert_rule.proto](./queue_1.md#alert_rule)
- [alert_severity.proto](./queue_1.md#alert_severity)
- [anti_affinity_rule.proto](./queue_1.md#anti_affinity_rule)
- [anti_affinity_scope.proto](./queue_1.md#anti_affinity_scope)
- [binding_info.proto](./queue_1.md#binding_info)
- [cluster_info.proto](./queue_1.md#cluster_info)
- [cluster_state.proto](./queue_1.md#cluster_state)
- [cluster_stats.proto](./queue_1.md#cluster_stats)
- [compression_algorithm.proto](./queue_1.md#compression_algorithm)
- [connection_details.proto](./queue_1.md#connection_details)
- [consistency_level.proto](./queue_1.md#consistency_level)
- [consumer_group.proto](./queue_1.md#consumer_group)
- [consumer_state.proto](./queue_1.md#consumer_state)
- [consumer_stats.proto](./queue_1.md#consumer_stats)
- [dead_letter_policy.proto](./queue_1.md#dead_letter_policy)
- [delivery_mode.proto](./queue_1.md#delivery_mode)
- [delivery_options.proto](./queue_1.md#delivery_options)
- [durability_level.proto](./queue_1.md#durability_level)
- [export_format.proto](./queue_1.md#export_format)
- [flow_control.proto](./queue_1.md#flow_control)
- [flush_policy.proto](./queue_1.md#flush_policy)
- [format_options.proto](./queue_1.md#format_options)
- [health_status.proto](./queue_1.md#health_status)
- [load_balancing_strategy.proto](./queue_1.md#load_balancing_strategy)
- [message.proto](./queue_1.md#message)
- [message_envelope.proto](./queue_1.md#message_envelope)
- [message_id.proto](./queue_1.md#message_id) ⚠️ 1 issues
- [message_metadata.proto](./queue_1.md#message_metadata)
- [message_state.proto](./queue_1.md#message_state)
- [metric_type.proto](./queue_1.md#metric_type)
- [nack_error.proto](./queue_1.md#nack_error)
- [nack_error_category.proto](./queue_1.md#nack_error_category)
- [node_info.proto](./queue_1.md#node_info)
- [node_state.proto](./queue_1.md#node_state)
- [node_stats.proto](./queue_1.md#node_stats)
- [notification_channel.proto](./queue_1.md#notification_channel)
- [notification_channel_type.proto](./queue_1.md#notification_channel_type)
- [offset_info.proto](./queue_1.md#offset_info)
- [offset_type.proto](./queue_1.md#offset_type)
- [partition_info.proto](./queue_1.md#partition_info)
- [partition_offset.proto](./queue_1.md#partition_offset)
- [partition_strategy.proto](./queue_1.md#partition_strategy)
- [priority_level.proto](./queue_1.md#priority_level)
- [priority_range.proto](./queue_1.md#priority_range)
- [publish_result.proto](./queue_1.md#publish_result)

### [queue_2](./queue_2.md)

- **Files**: 31
- **Messages**: 16
- **Services**: 0
- ⚠️ **Issues**: 3

**Proto Files**:

- [queue_info.proto](./queue_2.md#queue_info) ⚠️ 1 issues
- [queue_message.proto](./queue_2.md#queue_message)
- [queue_state.proto](./queue_2.md#queue_state)
- [queue_stats.proto](./queue_2.md#queue_stats)
- [queue_type.proto](./queue_2.md#queue_type)
- [received_message.proto](./queue_2.md#received_message)
- [replication_mode.proto](./queue_2.md#replication_mode)
- [retention_policy.proto](./queue_2.md#retention_policy)
- [retry_delay_strategy.proto](./queue_2.md#retry_delay_strategy)
- [retry_policy.proto](./queue_2.md#retry_policy)
- [routing_condition.proto](./queue_2.md#routing_condition)
- [routing_key.proto](./queue_2.md#routing_key)
- [routing_pattern.proto](./queue_2.md#routing_pattern)
- [routing_rule.proto](./queue_2.md#routing_rule)
- [routing_strategy.proto](./queue_2.md#routing_strategy)
- [schema_compatibility_mode.proto](./queue_2.md#schema_compatibility_mode)
- [schema_evolution_strategy.proto](./queue_2.md#schema_evolution_strategy)
- [schema_format.proto](./queue_2.md#schema_format)
- [serialization_format.proto](./queue_2.md#serialization_format)
- [size_range.proto](./queue_2.md#size_range)
- [statistic_grouping.proto](./queue_2.md#statistic_grouping)
- [statistic_type.proto](./queue_2.md#statistic_type)
- [stats_granularity.proto](./queue_2.md#stats_granularity)
- [stream_restart_policy.proto](./queue_2.md#stream_restart_policy)
- [subscription_info.proto](./queue_2.md#subscription_info) ⚠️ 1 issues
- [subscription_state.proto](./queue_2.md#subscription_state)
- [subscription_stats.proto](./queue_2.md#subscription_stats)
- [time_range.proto](./queue_2.md#time_range)
- [timestamp_range.proto](./queue_2.md#timestamp_range) ⚠️ 1 issues
- [topic_info.proto](./queue_2.md#topic_info)
- [topic_stats.proto](./queue_2.md#topic_stats)

### [queue_api_1](./queue_api_1.md)

- **Files**: 50
- **Messages**: 58
- **Services**: 0
- ⚠️ **Issues**: 2

**Proto Files**:

- [ack_request.proto](./queue_api_1.md#ack_request) ⚠️ 1 issues
- [ack_response.proto](./queue_api_1.md#ack_response) ⚠️ 1 issues
- [acknowledge_request.proto](./queue_api_1.md#acknowledge_request)
- [acknowledge_response.proto](./queue_api_1.md#acknowledge_response)
- [backup_queue_request.proto](./queue_api_1.md#backup_queue_request)
- [backup_queue_response.proto](./queue_api_1.md#backup_queue_response)
- [batch_ack_request.proto](./queue_api_1.md#batch_ack_request)
- [batch_ack_response.proto](./queue_api_1.md#batch_ack_response)
- [batch_nack_request.proto](./queue_api_1.md#batch_nack_request)
- [batch_nack_response.proto](./queue_api_1.md#batch_nack_response)
- [batch_publish_request.proto](./queue_api_1.md#batch_publish_request)
- [batch_publish_response.proto](./queue_api_1.md#batch_publish_response)
- [batch_pull_request.proto](./queue_api_1.md#batch_pull_request)
- [batch_pull_response.proto](./queue_api_1.md#batch_pull_response)
- [commit_offset_request.proto](./queue_api_1.md#commit_offset_request)
- [commit_offset_response.proto](./queue_api_1.md#commit_offset_response)
- [create_queue_request.proto](./queue_api_1.md#create_queue_request)
- [create_queue_response.proto](./queue_api_1.md#create_queue_response)
- [create_subscription_request.proto](./queue_api_1.md#create_subscription_request)
- [create_subscription_response.proto](./queue_api_1.md#create_subscription_response)
- [create_topic_request.proto](./queue_api_1.md#create_topic_request)
- [create_topic_response.proto](./queue_api_1.md#create_topic_response)
- [delete_queue_request.proto](./queue_api_1.md#delete_queue_request)
- [delete_queue_response.proto](./queue_api_1.md#delete_queue_response)
- [delete_request.proto](./queue_api_1.md#delete_request)
- [delete_response.proto](./queue_api_1.md#delete_response)
- [delete_subscription_request.proto](./queue_api_1.md#delete_subscription_request)
- [delete_subscription_response.proto](./queue_api_1.md#delete_subscription_response)
- [delete_topic_request.proto](./queue_api_1.md#delete_topic_request)
- [delete_topic_response.proto](./queue_api_1.md#delete_topic_response)
- [dequeue_request.proto](./queue_api_1.md#dequeue_request)
- [dequeue_response.proto](./queue_api_1.md#dequeue_response)
- [enqueue_request.proto](./queue_api_1.md#enqueue_request)
- [enqueue_response.proto](./queue_api_1.md#enqueue_response)
- [export_queue_request.proto](./queue_api_1.md#export_queue_request)
- [export_queue_response.proto](./queue_api_1.md#export_queue_response)
- [flush_queue_request.proto](./queue_api_1.md#flush_queue_request)
- [flush_queue_response.proto](./queue_api_1.md#flush_queue_response)
- [get_cluster_info_request.proto](./queue_api_1.md#get_cluster_info_request)
- [get_cluster_info_response.proto](./queue_api_1.md#get_cluster_info_response)
- [get_message_request.proto](./queue_api_1.md#get_message_request)
- [get_message_response.proto](./queue_api_1.md#get_message_response)
- [get_node_info_request.proto](./queue_api_1.md#get_node_info_request)
- [get_node_info_response.proto](./queue_api_1.md#get_node_info_response)
- [get_offset_request.proto](./queue_api_1.md#get_offset_request)
- [get_offset_response.proto](./queue_api_1.md#get_offset_response)
- [get_partition_info_request.proto](./queue_api_1.md#get_partition_info_request)
- [get_partition_info_response.proto](./queue_api_1.md#get_partition_info_response)
- [get_queue_info_request.proto](./queue_api_1.md#get_queue_info_request)
- [get_queue_info_response.proto](./queue_api_1.md#get_queue_info_response)

### [queue_api_2](./queue_api_2.md)

- **Files**: 50
- **Messages**: 117
- **Services**: 0
- ⚠️ **Issues**: 6

**Proto Files**:

- [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- [get_subscription_info_request.proto](./queue_api_2.md#get_subscription_info_request)
- [get_subscription_info_response.proto](./queue_api_2.md#get_subscription_info_response)
- [get_topic_info_request.proto](./queue_api_2.md#get_topic_info_request)
- [get_topic_info_response.proto](./queue_api_2.md#get_topic_info_response)
- [health_check_request.proto](./queue_api_2.md#health_check_request)
- [health_check_response.proto](./queue_api_2.md#health_check_response)
- [import_queue_request.proto](./queue_api_2.md#import_queue_request)
- [import_queue_response.proto](./queue_api_2.md#import_queue_response)
- [list_messages_request.proto](./queue_api_2.md#list_messages_request)
- [list_messages_response.proto](./queue_api_2.md#list_messages_response)
- [list_queues_request.proto](./queue_api_2.md#list_queues_request) ⚠️ 1 issues
- [list_queues_response.proto](./queue_api_2.md#list_queues_response) ⚠️ 1 issues
- [list_subscriptions_request.proto](./queue_api_2.md#list_subscriptions_request) ⚠️ 1 issues
- [list_subscriptions_response.proto](./queue_api_2.md#list_subscriptions_response) ⚠️ 1 issues
- [list_topics_request.proto](./queue_api_2.md#list_topics_request)
- [list_topics_response.proto](./queue_api_2.md#list_topics_response)
- [migrate_queue_request.proto](./queue_api_2.md#migrate_queue_request)
- [migrate_queue_response.proto](./queue_api_2.md#migrate_queue_response)
- [nack_request.proto](./queue_api_2.md#nack_request)
- [nack_response.proto](./queue_api_2.md#nack_response)
- [pause_queue_request.proto](./queue_api_2.md#pause_queue_request)
- [pause_queue_response.proto](./queue_api_2.md#pause_queue_response)
- [peek_request.proto](./queue_api_2.md#peek_request)
- [peek_response.proto](./queue_api_2.md#peek_response)
- [publish_request.proto](./queue_api_2.md#publish_request)
- [publish_response.proto](./queue_api_2.md#publish_response)
- [pull_request.proto](./queue_api_2.md#pull_request) ⚠️ 1 issues
- [pull_response.proto](./queue_api_2.md#pull_response) ⚠️ 1 issues
- [purge_request.proto](./queue_api_2.md#purge_request)
- [purge_response.proto](./queue_api_2.md#purge_response)
- [push_request.proto](./queue_api_2.md#push_request)
- [push_response.proto](./queue_api_2.md#push_response)
- [reset_queue_stats_request.proto](./queue_api_2.md#reset_queue_stats_request)
- [reset_queue_stats_response.proto](./queue_api_2.md#reset_queue_stats_response)
- [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- [resume_queue_request.proto](./queue_api_2.md#resume_queue_request)
- [resume_queue_response.proto](./queue_api_2.md#resume_queue_response)
- [seek_request.proto](./queue_api_2.md#seek_request)
- [seek_response.proto](./queue_api_2.md#seek_response)
- [send_message_request.proto](./queue_api_2.md#send_message_request)
- [send_message_response.proto](./queue_api_2.md#send_message_response)
- [stream_messages_request.proto](./queue_api_2.md#stream_messages_request)
- [stream_messages_response.proto](./queue_api_2.md#stream_messages_response)
- [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- [subscribe_response.proto](./queue_api_2.md#subscribe_response)
- [unsubscribe_request.proto](./queue_api_2.md#unsubscribe_request)
- [unsubscribe_response.proto](./queue_api_2.md#unsubscribe_response)
- [update_message_request.proto](./queue_api_2.md#update_message_request)

### [queue_api_3](./queue_api_3.md)

- **Files**: 1
- **Messages**: 3
- **Services**: 0

**Proto Files**:

- [update_message_response.proto](./queue_api_3.md#update_message_response)

### [queue_config](./queue_config.md)

- **Files**: 41
- **Messages**: 75
- **Services**: 0

**Proto Files**:

- [alerting_config.proto](./queue_config.md#alerting_config)
- [authentication_config.proto](./queue_config.md#authentication_config)
- [authorization_config.proto](./queue_config.md#authorization_config)
- [backup_config.proto](./queue_config.md#backup_config)
- [batch_config.proto](./queue_config.md#batch_config)
- [circuit_breaker_config.proto](./queue_config.md#circuit_breaker_config)
- [cluster_config.proto](./queue_config.md#cluster_config)
- [compression_config.proto](./queue_config.md#compression_config)
- [consistency_config.proto](./queue_config.md#consistency_config)
- [dead_letter_config.proto](./queue_config.md#dead_letter_config)
- [deserialization_config.proto](./queue_config.md#deserialization_config)
- [durability_config.proto](./queue_config.md#durability_config)
- [encryption_config.proto](./queue_config.md#encryption_config)
- [exchange_config.proto](./queue_config.md#exchange_config)
- [header_routing_config.proto](./queue_config.md#header_routing_config)
- [load_balancing_config.proto](./queue_config.md#load_balancing_config)
- [migration_config.proto](./queue_config.md#migration_config)
- [monitoring_config.proto](./queue_config.md#monitoring_config)
- [partition_config.proto](./queue_config.md#partition_config)
- [performance_config.proto](./queue_config.md#performance_config)
- [queue_config.proto](./queue_config.md#queue_config)
- [rate_limit_config.proto](./queue_config.md#rate_limit_config)
- [replication_config.proto](./queue_config.md#replication_config)
- [restore_config.proto](./queue_config.md#restore_config)
- [retry_config.proto](./queue_config.md#retry_config)
- [routing_config.proto](./queue_config.md#routing_config)
- [schema_config.proto](./queue_config.md#schema_config)
- [serialization_config.proto](./queue_config.md#serialization_config)
- [stream_config.proto](./queue_config.md#stream_config)
- [subscription_config.proto](./queue_config.md#subscription_config)
- [timeout_config.proto](./queue_config.md#timeout_config)
- [topic_config.proto](./queue_config.md#topic_config)
- [topic_routing_config.proto](./queue_config.md#topic_routing_config)
- [transformation_config.proto](./queue_config.md#transformation_config)
- [update_queue_config_request.proto](./queue_config.md#update_queue_config_request)
- [update_queue_config_response.proto](./queue_config.md#update_queue_config_response)
- [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- [update_subscription_config_response.proto](./queue_config.md#update_subscription_config_response)
- [update_topic_config_request.proto](./queue_config.md#update_topic_config_request)
- [update_topic_config_response.proto](./queue_config.md#update_topic_config_response)
- [validation_config.proto](./queue_config.md#validation_config)

### [queue_services](./queue_services.md)

- **Files**: 3
- **Messages**: 9
- **Services**: 3

**Proto Files**:

- [queue_admin_service.proto](./queue_services.md#queue_admin_service)
- [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- [queue_service.proto](./queue_services.md#queue_service)

### [web](./web.md)

- **Files**: 36
- **Messages**: 15
- **Services**: 0

**Proto Files**:

- [auth_method.proto](./web.md#auth_method)
- [cache_strategy.proto](./web.md#cache_strategy)
- [compression_type.proto](./web.md#compression_type)
- [content_type.proto](./web.md#content_type)
- [cookie_data.proto](./web.md#cookie_data)
- [cookie_same_site.proto](./web.md#cookie_same_site)
- [file_info.proto](./web.md#file_info)
- [file_metadata.proto](./web.md#file_metadata)
- [file_sort_order.proto](./web.md#file_sort_order)
- [file_upload.proto](./web.md#file_upload)
- [handler_info.proto](./web.md#handler_info)
- [handler_type.proto](./web.md#handler_type)
- [health_status.proto](./web.md#health_status)
- [http_header.proto](./web.md#http_header)
- [http_method.proto](./web.md#http_method)
- [http_status.proto](./web.md#http_status)
- [load_balance_strategy.proto](./web.md#load_balance_strategy)
- [middleware_info.proto](./web.md#middleware_info)
- [middleware_type.proto](./web.md#middleware_type)
- [mime_type.proto](./web.md#mime_type)
- [performance_stats.proto](./web.md#performance_stats)
- [proxy_type.proto](./web.md#proxy_type)
- [rate_limit_strategy.proto](./web.md#rate_limit_strategy)
- [route_info.proto](./web.md#route_info)
- [route_type.proto](./web.md#route_type)
- [same_site_policy.proto](./web.md#same_site_policy)
- [server_state.proto](./web.md#server_state)
- [server_status.proto](./web.md#server_status)
- [session_data.proto](./web.md#session_data)
- [session_state.proto](./web.md#session_state)
- [ssl_protocol.proto](./web.md#ssl_protocol)
- [template_data.proto](./web.md#template_data)
- [url_path.proto](./web.md#url_path)
- [websocket_info.proto](./web.md#websocket_info)
- [websocket_message.proto](./web.md#websocket_message)
- [websocket_state.proto](./web.md#websocket_state)

### [web_api_1](./web_api_1.md)

- **Files**: 50
- **Messages**: 50
- **Services**: 0
- ⚠️ **Issues**: 43

**Proto Files**:

- [add_middleware_request.proto](./web_api_1.md#add_middleware_request) ⚠️ 1 issues
- [add_middleware_response.proto](./web_api_1.md#add_middleware_response) ⚠️ 1 issues
- [authenticate_request.proto](./web_api_1.md#authenticate_request) ⚠️ 1 issues
- [authenticate_response.proto](./web_api_1.md#authenticate_response) ⚠️ 1 issues
- [authorize_request.proto](./web_api_1.md#authorize_request) ⚠️ 1 issues
- [authorize_response.proto](./web_api_1.md#authorize_response) ⚠️ 1 issues
- [close_websocket_request.proto](./web_api_1.md#close_websocket_request) ⚠️ 1 issues
- [close_websocket_response.proto](./web_api_1.md#close_websocket_response) ⚠️ 1 issues
- [create_cookie_request.proto](./web_api_1.md#create_cookie_request)
- [create_cookie_response.proto](./web_api_1.md#create_cookie_response) ⚠️ 1 issues
- [create_server_request.proto](./web_api_1.md#create_server_request) ⚠️ 1 issues
- [create_server_response.proto](./web_api_1.md#create_server_response) ⚠️ 1 issues
- [create_session_request.proto](./web_api_1.md#create_session_request)
- [create_session_response.proto](./web_api_1.md#create_session_response)
- [create_template_request.proto](./web_api_1.md#create_template_request) ⚠️ 1 issues
- [create_template_response.proto](./web_api_1.md#create_template_response) ⚠️ 1 issues
- [create_websocket_request.proto](./web_api_1.md#create_websocket_request) ⚠️ 1 issues
- [create_websocket_response.proto](./web_api_1.md#create_websocket_response) ⚠️ 1 issues
- [delete_cookie_request.proto](./web_api_1.md#delete_cookie_request) ⚠️ 1 issues
- [delete_cookie_response.proto](./web_api_1.md#delete_cookie_response) ⚠️ 1 issues
- [delete_file_request.proto](./web_api_1.md#delete_file_request) ⚠️ 1 issues
- [delete_file_response.proto](./web_api_1.md#delete_file_response) ⚠️ 1 issues
- [delete_session_request.proto](./web_api_1.md#delete_session_request)
- [delete_session_response.proto](./web_api_1.md#delete_session_response)
- [delete_template_request.proto](./web_api_1.md#delete_template_request) ⚠️ 1 issues
- [delete_template_response.proto](./web_api_1.md#delete_template_response) ⚠️ 1 issues
- [download_file_request.proto](./web_api_1.md#download_file_request) ⚠️ 1 issues
- [download_file_response.proto](./web_api_1.md#download_file_response) ⚠️ 1 issues
- [flush_cache_request.proto](./web_api_1.md#flush_cache_request)
- [flush_cache_response.proto](./web_api_1.md#flush_cache_response)
- [generate_csrf_token_request.proto](./web_api_1.md#generate_csrf_token_request) ⚠️ 1 issues
- [generate_csrf_token_response.proto](./web_api_1.md#generate_csrf_token_response) ⚠️ 1 issues
- [get_access_logs_request.proto](./web_api_1.md#get_access_logs_request) ⚠️ 1 issues
- [get_access_logs_response.proto](./web_api_1.md#get_access_logs_response) ⚠️ 1 issues
- [get_cookie_request.proto](./web_api_1.md#get_cookie_request) ⚠️ 1 issues
- [get_cookie_response.proto](./web_api_1.md#get_cookie_response) ⚠️ 1 issues
- [get_file_info_request.proto](./web_api_1.md#get_file_info_request) ⚠️ 1 issues
- [get_file_info_response.proto](./web_api_1.md#get_file_info_response) ⚠️ 1 issues
- [get_handler_info_request.proto](./web_api_1.md#get_handler_info_request) ⚠️ 1 issues
- [get_handler_info_response.proto](./web_api_1.md#get_handler_info_response) ⚠️ 1 issues
- [get_metrics_request.proto](./web_api_1.md#get_metrics_request) ⚠️ 1 issues
- [get_metrics_response.proto](./web_api_1.md#get_metrics_response) ⚠️ 1 issues
- [get_middleware_info_request.proto](./web_api_1.md#get_middleware_info_request) ⚠️ 1 issues
- [get_middleware_info_response.proto](./web_api_1.md#get_middleware_info_response) ⚠️ 1 issues
- [get_performance_stats_request.proto](./web_api_1.md#get_performance_stats_request) ⚠️ 1 issues
- [get_performance_stats_response.proto](./web_api_1.md#get_performance_stats_response) ⚠️ 1 issues
- [get_route_info_request.proto](./web_api_1.md#get_route_info_request) ⚠️ 1 issues
- [get_route_info_response.proto](./web_api_1.md#get_route_info_response) ⚠️ 1 issues
- [get_route_metrics_request.proto](./web_api_1.md#get_route_metrics_request) ⚠️ 1 issues
- [get_route_metrics_response.proto](./web_api_1.md#get_route_metrics_response) ⚠️ 1 issues

### [web_api_2](./web_api_2.md)

- **Files**: 50
- **Messages**: 50
- **Services**: 0
- ⚠️ **Issues**: 33

**Proto Files**:

- [get_server_health_request.proto](./web_api_2.md#get_server_health_request) ⚠️ 1 issues
- [get_server_health_response.proto](./web_api_2.md#get_server_health_response) ⚠️ 1 issues
- [get_server_logs_request.proto](./web_api_2.md#get_server_logs_request) ⚠️ 1 issues
- [get_server_logs_response.proto](./web_api_2.md#get_server_logs_response) ⚠️ 1 issues
- [get_server_metrics_request.proto](./web_api_2.md#get_server_metrics_request) ⚠️ 1 issues
- [get_server_metrics_response.proto](./web_api_2.md#get_server_metrics_response) ⚠️ 1 issues
- [get_server_status_request.proto](./web_api_2.md#get_server_status_request) ⚠️ 1 issues
- [get_server_status_response.proto](./web_api_2.md#get_server_status_response) ⚠️ 1 issues
- [get_session_request.proto](./web_api_2.md#get_session_request)
- [get_session_response.proto](./web_api_2.md#get_session_response)
- [get_ssl_certificate_info_request.proto](./web_api_2.md#get_ssl_certificate_info_request) ⚠️ 1 issues
- [get_ssl_certificate_info_response.proto](./web_api_2.md#get_ssl_certificate_info_response) ⚠️ 1 issues
- [get_template_info_request.proto](./web_api_2.md#get_template_info_request) ⚠️ 1 issues
- [get_template_info_response.proto](./web_api_2.md#get_template_info_response) ⚠️ 1 issues
- [get_websocket_info_request.proto](./web_api_2.md#get_websocket_info_request) ⚠️ 1 issues
- [get_websocket_info_response.proto](./web_api_2.md#get_websocket_info_response) ⚠️ 1 issues
- [handle_request.proto](./web_api_2.md#handle_request) ⚠️ 1 issues
- [handle_request_request.proto](./web_api_2.md#handle_request_request) ⚠️ 1 issues
- [handle_request_response.proto](./web_api_2.md#handle_request_response) ⚠️ 1 issues
- [handle_response.proto](./web_api_2.md#handle_response) ⚠️ 1 issues
- [health_check_request.proto](./web_api_2.md#health_check_request)
- [health_check_response.proto](./web_api_2.md#health_check_response)
- [http_request.proto](./web_api_2.md#http_request)
- [http_request_per.proto](./web_api_2.md#http_request_per)
- [http_response.proto](./web_api_2.md#http_response)
- [http_response_per.proto](./web_api_2.md#http_response_per)
- [list_cookies_request.proto](./web_api_2.md#list_cookies_request) ⚠️ 1 issues
- [list_cookies_response.proto](./web_api_2.md#list_cookies_response) ⚠️ 1 issues
- [list_files_request.proto](./web_api_2.md#list_files_request)
- [list_files_response.proto](./web_api_2.md#list_files_response)
- [list_handlers_request.proto](./web_api_2.md#list_handlers_request)
- [list_handlers_response.proto](./web_api_2.md#list_handlers_response) ⚠️ 1 issues
- [list_middleware_request.proto](./web_api_2.md#list_middleware_request)
- [list_middleware_response.proto](./web_api_2.md#list_middleware_response)
- [list_routes_request.proto](./web_api_2.md#list_routes_request) ⚠️ 1 issues
- [list_routes_response.proto](./web_api_2.md#list_routes_response) ⚠️ 1 issues
- [list_servers_request.proto](./web_api_2.md#list_servers_request) ⚠️ 1 issues
- [list_servers_response.proto](./web_api_2.md#list_servers_response) ⚠️ 1 issues
- [list_sessions_request.proto](./web_api_2.md#list_sessions_request)
- [list_sessions_response.proto](./web_api_2.md#list_sessions_response)
- [list_templates_request.proto](./web_api_2.md#list_templates_request) ⚠️ 1 issues
- [list_templates_response.proto](./web_api_2.md#list_templates_response) ⚠️ 1 issues
- [list_websockets_request.proto](./web_api_2.md#list_websockets_request) ⚠️ 1 issues
- [list_websockets_response.proto](./web_api_2.md#list_websockets_response) ⚠️ 1 issues
- [register_handler_request.proto](./web_api_2.md#register_handler_request) ⚠️ 1 issues
- [register_handler_response.proto](./web_api_2.md#register_handler_response) ⚠️ 1 issues
- [register_middleware_request.proto](./web_api_2.md#register_middleware_request)
- [register_middleware_response.proto](./web_api_2.md#register_middleware_response)
- [register_route_request.proto](./web_api_2.md#register_route_request) ⚠️ 1 issues
- [register_route_response.proto](./web_api_2.md#register_route_response) ⚠️ 1 issues

### [web_api_3](./web_api_3.md)

- **Files**: 33
- **Messages**: 33
- **Services**: 0
- ⚠️ **Issues**: 27

**Proto Files**:

- [remove_middleware_request.proto](./web_api_3.md#remove_middleware_request) ⚠️ 1 issues
- [remove_middleware_response.proto](./web_api_3.md#remove_middleware_response) ⚠️ 1 issues
- [render_template_request.proto](./web_api_3.md#render_template_request) ⚠️ 1 issues
- [render_template_response.proto](./web_api_3.md#render_template_response) ⚠️ 1 issues
- [reset_stats_request.proto](./web_api_3.md#reset_stats_request) ⚠️ 1 issues
- [reset_stats_response.proto](./web_api_3.md#reset_stats_response) ⚠️ 1 issues
- [restart_server_request.proto](./web_api_3.md#restart_server_request) ⚠️ 1 issues
- [restart_server_response.proto](./web_api_3.md#restart_server_response) ⚠️ 1 issues
- [send_websocket_message_request.proto](./web_api_3.md#send_websocket_message_request) ⚠️ 1 issues
- [send_websocket_message_response.proto](./web_api_3.md#send_websocket_message_response) ⚠️ 1 issues
- [serve_static_request.proto](./web_api_3.md#serve_static_request) ⚠️ 1 issues
- [serve_static_response.proto](./web_api_3.md#serve_static_response) ⚠️ 1 issues
- [start_server_request.proto](./web_api_3.md#start_server_request)
- [start_server_response.proto](./web_api_3.md#start_server_response)
- [stop_server_request.proto](./web_api_3.md#stop_server_request) ⚠️ 1 issues
- [stop_server_response.proto](./web_api_3.md#stop_server_response) ⚠️ 1 issues
- [stream_server_events_request.proto](./web_api_3.md#stream_server_events_request) ⚠️ 1 issues
- [unregister_handler_request.proto](./web_api_3.md#unregister_handler_request) ⚠️ 1 issues
- [unregister_handler_response.proto](./web_api_3.md#unregister_handler_response) ⚠️ 1 issues
- [unregister_middleware_request.proto](./web_api_3.md#unregister_middleware_request)
- [unregister_middleware_response.proto](./web_api_3.md#unregister_middleware_response)
- [unregister_route_request.proto](./web_api_3.md#unregister_route_request) ⚠️ 1 issues
- [unregister_route_response.proto](./web_api_3.md#unregister_route_response) ⚠️ 1 issues
- [update_cookie_request.proto](./web_api_3.md#update_cookie_request) ⚠️ 1 issues
- [update_cookie_response.proto](./web_api_3.md#update_cookie_response) ⚠️ 1 issues
- [update_session_request.proto](./web_api_3.md#update_session_request)
- [update_session_response.proto](./web_api_3.md#update_session_response)
- [update_ssl_certificate_request.proto](./web_api_3.md#update_ssl_certificate_request) ⚠️ 1 issues
- [update_ssl_certificate_response.proto](./web_api_3.md#update_ssl_certificate_response) ⚠️ 1 issues
- [upload_file_request.proto](./web_api_3.md#upload_file_request) ⚠️ 1 issues
- [upload_file_response.proto](./web_api_3.md#upload_file_response) ⚠️ 1 issues
- [validate_csrf_token_request.proto](./web_api_3.md#validate_csrf_token_request) ⚠️ 1 issues
- [validate_csrf_token_response.proto](./web_api_3.md#validate_csrf_token_response) ⚠️ 1 issues

### [web_config_1](./web_config_1.md)

- **Files**: 50
- **Messages**: 50
- **Services**: 0
- ⚠️ **Issues**: 23

**Proto Files**:

- [auth_config.proto](./web_config_1.md#auth_config)
- [cache_config.proto](./web_config_1.md#cache_config)
- [compression_config.proto](./web_config_1.md#compression_config)
- [configure_global_request.proto](./web_config_1.md#configure_global_request) ⚠️ 1 issues
- [configure_global_response.proto](./web_config_1.md#configure_global_response) ⚠️ 1 issues
- [cookie_config.proto](./web_config_1.md#cookie_config)
- [cors_config.proto](./web_config_1.md#cors_config)
- [csrf_config.proto](./web_config_1.md#csrf_config)
- [export_server_config_request.proto](./web_config_1.md#export_server_config_request) ⚠️ 1 issues
- [export_server_config_response.proto](./web_config_1.md#export_server_config_response) ⚠️ 1 issues
- [get_cache_config_request.proto](./web_config_1.md#get_cache_config_request)
- [get_cache_config_response.proto](./web_config_1.md#get_cache_config_response)
- [get_cors_config_request.proto](./web_config_1.md#get_cors_config_request) ⚠️ 1 issues
- [get_cors_config_response.proto](./web_config_1.md#get_cors_config_response) ⚠️ 1 issues
- [get_security_config_request.proto](./web_config_1.md#get_security_config_request) ⚠️ 1 issues
- [get_security_config_response.proto](./web_config_1.md#get_security_config_response) ⚠️ 1 issues
- [get_server_config_request.proto](./web_config_1.md#get_server_config_request) ⚠️ 1 issues
- [get_server_config_response.proto](./web_config_1.md#get_server_config_response) ⚠️ 1 issues
- [handler_config.proto](./web_config_1.md#handler_config)
- [health_check_config.proto](./web_config_1.md#health_check_config)
- [import_server_config_request.proto](./web_config_1.md#import_server_config_request) ⚠️ 1 issues
- [import_server_config_response.proto](./web_config_1.md#import_server_config_response) ⚠️ 1 issues
- [load_balancer_config.proto](./web_config_1.md#load_balancer_config)
- [middleware_config.proto](./web_config_1.md#middleware_config)
- [proxy_config.proto](./web_config_1.md#proxy_config)
- [rate_limit_config.proto](./web_config_1.md#rate_limit_config)
- [reload_server_config_request.proto](./web_config_1.md#reload_server_config_request) ⚠️ 1 issues
- [reload_server_config_response.proto](./web_config_1.md#reload_server_config_response) ⚠️ 1 issues
- [route_config.proto](./web_config_1.md#route_config)
- [security_config.proto](./web_config_1.md#security_config)
- [server_config.proto](./web_config_1.md#server_config)
- [session_config.proto](./web_config_1.md#session_config)
- [ssl_config.proto](./web_config_1.md#ssl_config)
- [static_config.proto](./web_config_1.md#static_config)
- [template_config.proto](./web_config_1.md#template_config)
- [timeout_config.proto](./web_config_1.md#timeout_config)
- [tls_config.proto](./web_config_1.md#tls_config)
- [update_cache_config_request.proto](./web_config_1.md#update_cache_config_request)
- [update_cache_config_response.proto](./web_config_1.md#update_cache_config_response)
- [update_cors_config_request.proto](./web_config_1.md#update_cors_config_request) ⚠️ 1 issues
- [update_cors_config_response.proto](./web_config_1.md#update_cors_config_response) ⚠️ 1 issues
- [update_handler_config_request.proto](./web_config_1.md#update_handler_config_request) ⚠️ 1 issues
- [update_handler_config_response.proto](./web_config_1.md#update_handler_config_response) ⚠️ 1 issues
- [update_middleware_config_request.proto](./web_config_1.md#update_middleware_config_request)
- [update_middleware_config_response.proto](./web_config_1.md#update_middleware_config_response)
- [update_route_config_request.proto](./web_config_1.md#update_route_config_request) ⚠️ 1 issues
- [update_route_config_response.proto](./web_config_1.md#update_route_config_response) ⚠️ 1 issues
- [update_security_config_request.proto](./web_config_1.md#update_security_config_request) ⚠️ 1 issues
- [update_security_config_response.proto](./web_config_1.md#update_security_config_response) ⚠️ 1 issues
- [update_server_config_request.proto](./web_config_1.md#update_server_config_request) ⚠️ 1 issues

### [web_config_2](./web_config_2.md)

- **Files**: 2
- **Messages**: 2
- **Services**: 0
- ⚠️ **Issues**: 1

**Proto Files**:

- [update_server_config_response.proto](./web_config_2.md#update_server_config_response) ⚠️ 1 issues
- [websocket_config.proto](./web_config_2.md#websocket_config)

### [web_events](./web_events.md)

- **Files**: 1
- **Messages**: 1
- **Services**: 0
- ⚠️ **Issues**: 1

**Proto Files**:

- [server_event.proto](./web_events.md#server_event) ⚠️ 1 issues

### [web_services](./web_services.md)

- **Files**: 2
- **Messages**: 0
- **Services**: 2

**Proto Files**:

- [web_admin_service.proto](./web_services.md#web_admin_service)
- [web_service.proto](./web_services.md#web_service)

## Quick Navigation

- [All Messages](#all-messages)
- [All Services](#all-services)
- [Issues Summary](#issues-summary)

## All Messages

- `AuthContext` - [auth_context.proto](./auth.md#auth_context)
- `AuthProvider` - [auth_provider.proto](./auth.md#auth_provider)
- `AuthToken` - [auth_token.proto](./auth.md#auth_token)
- `Claims` - [claims.proto](./auth.md#claims)
- `Group` - [group.proto](./auth.md#group)
- `JWTCredentials` - [jwt_credentials.proto](./auth.md#jwt_credentials)
- `OAuth2Credentials` - [oauth2_credentials.proto](./auth.md#oauth2_credentials)
- `OAuthClient` - [oauth_client.proto](./auth.md#oauth_client)
- `PasswordCredentials` - [password_credentials.proto](./auth.md#password_credentials)
- `PasswordPolicy` - [password_policy.proto](./auth.md#password_policy)
- `Permission` - [permission.proto](./auth.md#permission)
- `PermissionGrant` - [permission_grant.proto](./auth.md#permission_grant)
- `PermissionMetadata` - [permission_metadata.proto](./auth.md#permission_metadata)
- `PermissionCondition` - [permission_metadata.proto](./auth.md#permission_metadata)
- `RefreshToken` - [refresh_token.proto](./auth.md#refresh_token)
- `Role` - [role.proto](./auth.md#role)
- `RoleAssignment` - [role_assignment.proto](./auth.md#role_assignment)
- `RoleMetadata` - [role_metadata.proto](./auth.md#role_metadata)
- `SecurityContext` - [security_context.proto](./auth.md#security_context)
- `SecurityPolicy` - [security_policy.proto](./auth.md#security_policy)
- `Session` - [session.proto](./auth.md#session)
- `SessionInfo` - [session_info.proto](./auth.md#session_info)
- `SessionMetadata` - [session_metadata.proto](./auth.md#session_metadata)
- `DeviceInfo` - [session_metadata.proto](./auth.md#session_metadata)
- `LocationInfo` - [session_metadata.proto](./auth.md#session_metadata)
- `Token` - [token.proto](./auth.md#token)
- `TokenInfo` - [token_info.proto](./auth.md#token_info)
- `TokenMetadata` - [token_metadata.proto](./auth.md#token_metadata)
- `User` - [user.proto](./auth.md#user)
- `UserInfo` - [user_info.proto](./auth.md#user_info)
- `UserMetadata` - [user_metadata.proto](./auth.md#user_metadata)
- `UserPreferences` - [user_metadata.proto](./auth.md#user_metadata)
- `VerificationStatus` - [user_metadata.proto](./auth.md#user_metadata)
- `UserProfile` - [user_profile.proto](./auth.md#user_profile)
- `APIKey` - [api_key.proto](./auth_api_1.md#api_key)
- `APIKeyCredentials` - [api_key_credentials.proto](./auth_api_1.md#api_key_credentials)
- `AssignRoleRequest` - [assign_role_request.proto](./auth_api_1.md#assign_role_request)
- `AssignRoleResponse` - [assign_role_response.proto](./auth_api_1.md#assign_role_response)
- `AuthenticateRequest` - [authenticate_request.proto](./auth_api_1.md#authenticate_request)
- `AuthenticateResponse` - [authenticate_response.proto](./auth_api_1.md#authenticate_response)
- `AuthorizeRequest` - [authorize_request.proto](./auth_api_1.md#authorize_request)
- `AuthorizeResponse` - [authorize_response.proto](./auth_api_1.md#authorize_response)
- `ChangePasswordRequest` - [change_password_request.proto](./auth_api_1.md#change_password_request)
- `ChangePasswordResponse` - [change_password_response.proto](./auth_api_1.md#change_password_response)
- `CheckPermissionRequest` - [check_permission_request.proto](./auth_api_1.md#check_permission_request)
- `CheckPermissionResponse` - [check_permission_response.proto](./auth_api_1.md#check_permission_response)
- `CompletePasswordResetRequest` - [complete_password_reset_request.proto](./auth_api_1.md#complete_password_reset_request)
- `CompletePasswordResetResponse` - [complete_password_reset_response.proto](./auth_api_1.md#complete_password_reset_response)
- `CreatePermissionRequest` - [create_permission_request.proto](./auth_api_1.md#create_permission_request)
- `CreateRoleRequest` - [create_role_request.proto](./auth_api_1.md#create_role_request)
- `CreateRoleResponse` - [create_role_response.proto](./auth_api_1.md#create_role_response)
- `CreateSessionRequest` - [create_session_request.proto](./auth_api_1.md#create_session_request)
- `CreateSessionResponse` - [create_session_response.proto](./auth_api_1.md#create_session_response)
- `CreateUserRequest` - [create_user_request.proto](./auth_api_1.md#create_user_request)
- `CreateUserResponse` - [create_user_response.proto](./auth_api_1.md#create_user_response)
- `DeletePermissionRequest` - [delete_permission_request.proto](./auth_api_1.md#delete_permission_request)
- `DeleteRoleRequest` - [delete_role_request.proto](./auth_api_1.md#delete_role_request)
- `DeleteRoleResponse` - [delete_role_response.proto](./auth_api_1.md#delete_role_response)
- `DeleteSessionRequest` - [delete_session_request.proto](./auth_api_1.md#delete_session_request)
- `DeleteSessionResponse` - [delete_session_response.proto](./auth_api_1.md#delete_session_response)
- `DeleteUserRequest` - [delete_user_request.proto](./auth_api_1.md#delete_user_request)
- `DeleteUserResponse` - [delete_user_response.proto](./auth_api_1.md#delete_user_response)
- `Disable2FaRequest` - [disable_2fa_request.proto](./auth_api_1.md#disable_2fa_request)
- `DisableMfaRequest` - [disable_mfa_request.proto](./auth_api_1.md#disable_mfa_request)
- `DisableMfaResponse` - [disable_mfa_response.proto](./auth_api_1.md#disable_mfa_response)
- `Enable2FaRequest` - [enable_2fa_request.proto](./auth_api_1.md#enable_2fa_request)
- `EnableMfaRequest` - [enable_mfa_request.proto](./auth_api_1.md#enable_mfa_request)
- `EnableMfaResponse` - [enable_mfa_response.proto](./auth_api_1.md#enable_mfa_response)
- `MfaSetupInstruction` - [enable_mfa_response.proto](./auth_api_1.md#enable_mfa_response)
- `GenerateAPIKeyRequest` - [generate_api_key_request.proto](./auth_api_1.md#generate_api_key_request)
- `GenerateAPIKeyResponse` - [generate_api_key_response.proto](./auth_api_1.md#generate_api_key_response)
- `GetApiKeyRequest` - [get_api_key_request.proto](./auth_api_1.md#get_api_key_request)
- `GetApiKeyResponse` - [get_api_key_response.proto](./auth_api_1.md#get_api_key_response)
- `ApiKeyStats` - [get_api_key_response.proto](./auth_api_1.md#get_api_key_response)
- `DailyUsage` - [get_api_key_response.proto](./auth_api_1.md#get_api_key_response)
- `GetPermissionRequest` - [get_permission_request.proto](./auth_api_1.md#get_permission_request)
- `GetPermissionResponse` - [get_permission_response.proto](./auth_api_1.md#get_permission_response)
- `GetRoleRequest` - [get_role_request.proto](./auth_api_1.md#get_role_request)
- `GetRoleResponse` - [get_role_response.proto](./auth_api_1.md#get_role_response)
- `GetSessionRequest` - [get_session_request.proto](./auth_api_1.md#get_session_request)
- `GetSessionResponse` - [get_session_response.proto](./auth_api_1.md#get_session_response)
- `GetSystemStatsRequest` - [get_system_stats_request.proto](./auth_api_1.md#get_system_stats_request)
- `GetSystemStatsResponse` - [get_system_stats_response.proto](./auth_api_1.md#get_system_stats_response)
- `GetUserInfoRequest` - [get_user_info_request.proto](./auth_api_1.md#get_user_info_request)
- `GetUserInfoResponse` - [get_user_info_response.proto](./auth_api_1.md#get_user_info_response)
- `GetUserPermissionsRequest` - [get_user_permissions_request.proto](./auth_api_1.md#get_user_permissions_request)
- `GetUserPermissionsResponse` - [get_user_permissions_response.proto](./auth_api_1.md#get_user_permissions_response)
- `GetUserRequest` - [get_user_request.proto](./auth_api_2.md#get_user_request)
- `UserDetails` - [get_user_response.proto](./auth_api_2.md#get_user_response)
- `GetUserResponse` - [get_user_response.proto](./auth_api_2.md#get_user_response)
- `GetUserRolesRequest` - [get_user_roles_request.proto](./auth_api_2.md#get_user_roles_request)
- `GetUserRolesResponse` - [get_user_roles_response.proto](./auth_api_2.md#get_user_roles_response)
- `GrantPermissionRequest` - [grant_permission_request.proto](./auth_api_2.md#grant_permission_request)
- `GrantPermissionResponse` - [grant_permission_response.proto](./auth_api_2.md#grant_permission_response)
- `HealthCheckRequest` - [health_check_request.proto](./auth_api_2.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./auth_api_2.md#health_check_response)
- `InitiatePasswordResetRequest` - [initiate_password_reset_request.proto](./auth_api_2.md#initiate_password_reset_request)
- `InitiatePasswordResetResponse` - [initiate_password_reset_response.proto](./auth_api_2.md#initiate_password_reset_response)
- `InvalidateUserSessionsRequest` - [invalidate_user_sessions_request.proto](./auth_api_2.md#invalidate_user_sessions_request)
- `ListApiKeysRequest` - [list_api_keys_request.proto](./auth_api_2.md#list_api_keys_request)
- `ListApiKeysResponse` - [list_api_keys_response.proto](./auth_api_2.md#list_api_keys_response)
- `ApiKey` - [list_api_keys_response.proto](./auth_api_2.md#list_api_keys_response)
- `ListPermissionsRequest` - [list_permissions_request.proto](./auth_api_2.md#list_permissions_request)
- `ListPermissionsResponse` - [list_permissions_response.proto](./auth_api_2.md#list_permissions_response)
- `ListRolesRequest` - [list_roles_request.proto](./auth_api_2.md#list_roles_request)
- `ListRolesResponse` - [list_roles_response.proto](./auth_api_2.md#list_roles_response)
- `ListSessionsRequest` - [list_sessions_request.proto](./auth_api_2.md#list_sessions_request)
- `ListSessionsResponse` - [list_sessions_response.proto](./auth_api_2.md#list_sessions_response)
- `ListUserSessionsRequest` - [list_user_sessions_request.proto](./auth_api_2.md#list_user_sessions_request)
- `ListUserSessionsResponse` - [list_user_sessions_response.proto](./auth_api_2.md#list_user_sessions_response)
- `ListUsersRequest` - [list_users_request.proto](./auth_api_2.md#list_users_request)
- `ListUsersResponse` - [list_users_response.proto](./auth_api_2.md#list_users_response)
- `LogoutRequest` - [logout_request.proto](./auth_api_2.md#logout_request)
- `LogoutResponse` - [logout_response.proto](./auth_api_2.md#logout_response)
- `RefreshTokenRequest` - [refresh_token_request.proto](./auth_api_2.md#refresh_token_request)
- `RefreshTokenResponse` - [refresh_token_response.proto](./auth_api_2.md#refresh_token_response)
- `RegisterUserRequest` - [register_user_request.proto](./auth_api_2.md#register_user_request)
- `RegisterUserResponse` - [register_user_response.proto](./auth_api_2.md#register_user_response)
- `RemoveRoleRequest` - [remove_role_request.proto](./auth_api_2.md#remove_role_request)
- `RemoveRoleResponse` - [remove_role_response.proto](./auth_api_2.md#remove_role_response)
- `ResendVerificationRequest` - [resend_verification_request.proto](./auth_api_2.md#resend_verification_request)
- `ResetPasswordRequest` - [reset_password_request.proto](./auth_api_2.md#reset_password_request)
- `ResetPasswordResponse` - [reset_password_response.proto](./auth_api_2.md#reset_password_response)
- `RevokeApiKeyRequest` - [revoke_api_key_request.proto](./auth_api_2.md#revoke_api_key_request)
- `RevokeApiKeyResponse` - [revoke_api_key_response.proto](./auth_api_2.md#revoke_api_key_response)
- `RevokePermissionRequest` - [revoke_permission_request.proto](./auth_api_2.md#revoke_permission_request)
- `RevokePermissionResponse` - [revoke_permission_response.proto](./auth_api_2.md#revoke_permission_response)
- `RevokeRoleRequest` - [revoke_role_request.proto](./auth_api_2.md#revoke_role_request)
- `RevokeRoleResponse` - [revoke_role_response.proto](./auth_api_2.md#revoke_role_response)
- `RevokeTokenRequest` - [revoke_token_request.proto](./auth_api_2.md#revoke_token_request)
- `RevokeTokenResponse` - [revoke_token_response.proto](./auth_api_2.md#revoke_token_response)
- `SendVerificationEmailRequest` - [send_verification_email_request.proto](./auth_api_2.md#send_verification_email_request)
- `SendVerificationEmailResponse` - [send_verification_email_response.proto](./auth_api_2.md#send_verification_email_response)
- `TerminateSessionRequest` - [terminate_session_request.proto](./auth_api_2.md#terminate_session_request)
- `TerminateSessionResponse` - [terminate_session_response.proto](./auth_api_2.md#terminate_session_response)
- `UpdatePermissionRequest` - [update_permission_request.proto](./auth_api_2.md#update_permission_request)
- `UpdateRoleRequest` - [update_role_request.proto](./auth_api_2.md#update_role_request)
- `UpdateRoleResponse` - [update_role_response.proto](./auth_api_2.md#update_role_response)
- `UpdateSessionRequest` - [update_session_request.proto](./auth_api_2.md#update_session_request)
- `UpdateSessionResponse` - [update_session_response.proto](./auth_api_3.md#update_session_response)
- `UpdateUserRequest` - [update_user_request.proto](./auth_api_3.md#update_user_request)
- `UpdateUserResponse` - [update_user_response.proto](./auth_api_3.md#update_user_response)
- `ValidateSessionRequest` - [validate_session_request.proto](./auth_api_3.md#validate_session_request)
- `ValidateSessionResponse` - [validate_session_response.proto](./auth_api_3.md#validate_session_response)
- `ValidateTokenRequest` - [validate_token_request.proto](./auth_api_3.md#validate_token_request)
- `ValidateTokenResponse` - [validate_token_response.proto](./auth_api_3.md#validate_token_response)
- `Verify2FaRequest` - [verify_2fa_request.proto](./auth_api_3.md#verify_2fa_request)
- `VerifyCredentialsRequest` - [verify_credentials_request.proto](./auth_api_3.md#verify_credentials_request)
- `VerifyCredentialsResponse` - [verify_credentials_response.proto](./auth_api_3.md#verify_credentials_response)
- `VerifyEmailRequest` - [verify_email_request.proto](./auth_api_3.md#verify_email_request)
- `VerifyEmailResponse` - [verify_email_response.proto](./auth_api_3.md#verify_email_response)
- `VerifyMfaRequest` - [verify_mfa_request.proto](./auth_api_3.md#verify_mfa_request)
- `VerifyMfaResponse` - [verify_mfa_response.proto](./auth_api_3.md#verify_mfa_response)
- `AuthConfig` - [auth_config.proto](./auth_config.md#auth_config)
- `GetAuthConfigRequest` - [get_auth_config_request.proto](./auth_config.md#get_auth_config_request)
- `JWTConfig` - [jwt_config.proto](./auth_config.md#jwt_config)
- `LdapConfig` - [ldap_config.proto](./auth_config.md#ldap_config)
- `MfaConfig` - [mfa_config.proto](./auth_config.md#mfa_config)
- `OAuth2Config` - [oauth2_config.proto](./auth_config.md#oauth2_config)
- `RateLimitConfig` - [rate_limit_config.proto](./auth_config.md#rate_limit_config)
- `SamlConfig` - [saml_config.proto](./auth_config.md#saml_config)
- `SessionConfig` - [session_config.proto](./auth_config.md#session_config)
- `AuditEvent` - [audit_event.proto](./auth_events.md#audit_event)
- `AuditLog` - [audit_log.proto](./auth_events.md#audit_log)
- `CacheEntry` - [cache_entry.proto](./cache.md#cache_entry)
- `CacheInfo` - [cache_info.proto](./cache.md#cache_info)
- `CacheMetrics` - [cache_metrics.proto](./cache.md#cache_metrics)
- `CacheOperationResult` - [cache_operation_result.proto](./cache.md#cache_operation_result)
- `CacheStats` - [cache_stats.proto](./cache.md#cache_stats)
- `EvictionResult` - [eviction_result.proto](./cache.md#eviction_result)
- `SetOptions` - [set_options.proto](./cache.md#set_options)
- `AppendRequest` - [append_request.proto](./cache_api_1.md#append_request)
- `BackupRequest` - [backup_request.proto](./cache_api_1.md#backup_request)
- `ClearRequest` - [clear_request.proto](./cache_api_1.md#clear_request)
- `ClearResponse` - [clear_response.proto](./cache_api_1.md#clear_response)
- `CreateNamespaceRequest` - [create_namespace_request.proto](./cache_api_1.md#create_namespace_request)
- `CreateNamespaceResponse` - [create_namespace_response.proto](./cache_api_1.md#create_namespace_response)
- `DecrementRequest` - [decrement_request.proto](./cache_api_1.md#decrement_request)
- `DecrementResponse` - [decrement_response.proto](./cache_api_1.md#decrement_response)
- `DefragRequest` - [defrag_request.proto](./cache_api_1.md#defrag_request)
- `DeleteMultipleRequest` - [delete_multiple_request.proto](./cache_api_1.md#delete_multiple_request)
- `DeleteMultipleResponse` - [delete_multiple_response.proto](./cache_api_1.md#delete_multiple_response)
- `DeleteNamespaceRequest` - [delete_namespace_request.proto](./cache_api_1.md#delete_namespace_request)
- `DeleteRequest` - [delete_request.proto](./cache_api_1.md#delete_request)
- `DeleteResponse` - [delete_response.proto](./cache_api_1.md#delete_response)
- `ExistsRequest` - [exists_request.proto](./cache_api_1.md#exists_request)
- `ExistsResponse` - [exists_response.proto](./cache_api_1.md#exists_response)
- `ExpireRequest` - [expire_request.proto](./cache_api_1.md#expire_request)
- `ExportRequest` - [export_request.proto](./cache_api_1.md#export_request)
- `FlushRequest` - [flush_request.proto](./cache_api_1.md#flush_request)
- `FlushResponse` - [flush_response.proto](./cache_api_1.md#flush_response)
- `GcRequest` - [gc_request.proto](./cache_api_1.md#gc_request)
- `GetMemoryUsageRequest` - [get_memory_usage_request.proto](./cache_api_1.md#get_memory_usage_request)
- `GetMemoryUsageResponse` - [get_memory_usage_response.proto](./cache_api_1.md#get_memory_usage_response)
- `GetMultipleRequest` - [get_multiple_request.proto](./cache_api_1.md#get_multiple_request)
- `GetMultipleResponse` - [get_multiple_response.proto](./cache_api_1.md#get_multiple_response)
- `GetNamespaceStatsRequest` - [get_namespace_stats_request.proto](./cache_api_1.md#get_namespace_stats_request)
- `NamespaceStats` - [get_namespace_stats_response.proto](./cache_api_1.md#get_namespace_stats_response)
- `GetNamespaceStatsResponse` - [get_namespace_stats_response.proto](./cache_api_1.md#get_namespace_stats_response)
- `GetRequest` - [get_request.proto](./cache_api_1.md#get_request)
- `GetResponse` - [get_response.proto](./cache_api_1.md#get_response)
- `GetStatsResponse` - [get_stats_response.proto](./cache_api_1.md#get_stats_response)
- `HealthCheckRequest` - [health_check_request.proto](./cache_api_1.md#health_check_request)
- `ImportRequest` - [import_request.proto](./cache_api_1.md#import_request)
- `IncrementRequest` - [increment_request.proto](./cache_api_1.md#increment_request)
- `IncrementResponse` - [increment_response.proto](./cache_api_1.md#increment_response)
- `InfoRequest` - [info_request.proto](./cache_api_1.md#info_request)
- `KeysRequest` - [keys_request.proto](./cache_api_1.md#keys_request)
- `KeysResponse` - [keys_response.proto](./cache_api_1.md#keys_response)
- `ListNamespacesRequest` - [list_namespaces_request.proto](./cache_api_1.md#list_namespaces_request)
- `NamespaceInfo` - [list_namespaces_response.proto](./cache_api_1.md#list_namespaces_response)
- `ListNamespacesResponse` - [list_namespaces_response.proto](./cache_api_1.md#list_namespaces_response)
- `ListSubscriptionsRequest` - [list_subscriptions_request.proto](./cache_api_1.md#list_subscriptions_request)
- `LockRequest` - [lock_request.proto](./cache_api_1.md#lock_request)
- `MGetRequest` - [mget_request.proto](./cache_api_1.md#mget_request)
- `OptimizeRequest` - [optimize_request.proto](./cache_api_1.md#optimize_request)
- `PipelineRequest` - [pipeline_request.proto](./cache_api_1.md#pipeline_request)
- `PrependRequest` - [prepend_request.proto](./cache_api_1.md#prepend_request)
- `PublishRequest` - [publish_request.proto](./cache_api_1.md#publish_request)
- `RestoreRequest` - [restore_request.proto](./cache_api_1.md#restore_request)
- `ScanRequest` - [scan_request.proto](./cache_api_1.md#scan_request)
- `SetMultipleRequest` - [set_multiple_request.proto](./cache_api_1.md#set_multiple_request)
- `SetMultipleResponse` - [set_multiple_response.proto](./cache_api_1.md#set_multiple_response)
- `SetRequest` - [set_request.proto](./cache_api_2.md#set_request)
- `SetResponse` - [set_response.proto](./cache_api_2.md#set_response)
- `GetStatsRequest` - [stats_request.proto](./cache_api_2.md#stats_request)
- `SubscribeRequest` - [subscribe_request.proto](./cache_api_2.md#subscribe_request)
- `TouchExpirationResponse` - [touch_expiration_response.proto](./cache_api_2.md#touch_expiration_response)
- `TransactionRequest` - [transaction_request.proto](./cache_api_2.md#transaction_request)
- `TouchExpirationRequest` - [ttl_request.proto](./cache_api_2.md#ttl_request)
- `UnlockRequest` - [unlock_request.proto](./cache_api_2.md#unlock_request)
- `UnsubscribeRequest` - [unsubscribe_request.proto](./cache_api_2.md#unsubscribe_request)
- `UnwatchRequest` - [unwatch_request.proto](./cache_api_2.md#unwatch_request)
- `WatchRequest` - [watch_request.proto](./cache_api_2.md#watch_request)
- `CacheConfig` - [cache_config.proto](./cache_config.md#cache_config)
- `ConfigurePolicyRequest` - [configure_policy_request.proto](./cache_config.md#configure_policy_request)
- `ConfigurePolicyResponse` - [configure_policy_response.proto](./cache_config.md#configure_policy_response)
- `AuditLog` - [audit_log.proto](./common.md#audit_log)
- `BatchOperation` - [batch_operation.proto](./common.md#batch_operation)
- `BatchOptions` - [batch_options.proto](./common.md#batch_options)
- `CachePolicy` - [cache_policy.proto](./common.md#cache_policy)
- `CircuitBreakerConfig` - [circuit_breaker_config.proto](./common.md#circuit_breaker_config)
- `ClientInfo` - [client_info.proto](./common.md#client_info)
- `ConfigValue` - [config_value.proto](./common.md#config_value)
- `DebugInfo` - [debug_info.proto](./common.md#debug_info)
- `Error` - [error.proto](./common.md#error)
- `FilterOptions` - [filter_options.proto](./common.md#filter_options)
- `FilterValue` - [filter_value.proto](./common.md#filter_value)
- `Int64Array` - [int64_array.proto](./common.md#int64_array)
- `KeyValue` - [key_value.proto](./common.md#key_value)
- `MetricPoint` - [metric_point.proto](./common.md#metric_point)
- `PaginatedResponse` - [paginated_response.proto](./common.md#paginated_response)
- `Pagination` - [pagination.proto](./common.md#pagination)
- `PaginationOptions` - [pagination_options.proto](./common.md#pagination_options)
- `RateLimit` - [rate_limit.proto](./common.md#rate_limit)
- `RequestMetadata` - [request_metadata.proto](./common.md#request_metadata)
- `ResourceReference` - [resource_reference.proto](./common.md#resource_reference)
- `ResponseMetadata` - [response_metadata.proto](./common.md#response_metadata)
- `RateLimitInfo` - [response_metadata.proto](./common.md#response_metadata)
- `PaginationInfo` - [response_metadata.proto](./common.md#response_metadata)
- `RetryPolicy` - [retry_policy.proto](./common.md#retry_policy)
- `ServiceVersion` - [service_version.proto](./common.md#service_version)
- `SortOptions` - [sort.proto](./common.md#sort)
- `StringArray` - [string_array.proto](./common.md#string_array)
- `SubscriptionInfo` - [subscription_info.proto](./common.md#subscription_info)
- `SubscriptionOptions` - [subscription_options.proto](./common.md#subscription_options)
- `TimeRange` - [time_range.proto](./common.md#time_range)
- `AccessControl` - [access_control.proto](./config_1.md#access_control)
- `AccessRestriction` - [access_restriction.proto](./config_1.md#access_restriction)
- `ApprovalInfo` - [approval_info.proto](./config_1.md#approval_info)
- `ApprovalRequirement` - [approval_requirement.proto](./config_1.md#approval_requirement)
- `ComplianceReporting` - [compliance_reporting.proto](./config_1.md#compliance_reporting)
- `DeprecationInfo` - [deprecation_info.proto](./config_1.md#deprecation_info)
- `InheritanceFilter` - [inheritance_filter.proto](./config_1.md#inheritance_filter)
- `InheritanceTransformation` - [inheritance_transformation.proto](./config_1.md#inheritance_transformation)
- `MonitoringAlert` - [monitoring_alert.proto](./config_1.md#monitoring_alert)
- `NotificationChannel` - [notification_channel.proto](./config_1.md#notification_channel)
- `ParameterConstraints` - [parameter_constraints.proto](./config_1.md#parameter_constraints)
- `RateLimits` - [rate_limits.proto](./config_1.md#rate_limits)
- `RollbackInfo` - [rollback_info.proto](./config_1.md#rollback_info)
- `SecretValidationResult` - [secret_validation_result.proto](./config_1.md#secret_validation_result)
- `SynchronizationTarget` - [synchronization_target.proto](./config_2.md#synchronization_target)
- `TemplateChange` - [template_change.proto](./config_2.md#template_change)
- `TemplateHook` - [template_hook.proto](./config_2.md#template_hook)
- `TemplateOutput` - [template_output.proto](./config_2.md#template_output)
- `TemplateParameter` - [template_parameter.proto](./config_2.md#template_parameter)
- `TransformationStep` - [transformation_step.proto](./config_2.md#transformation_step)
- `UsageStatistics` - [usage_statistics.proto](./config_2.md#usage_statistics)
- `UsageTrend` - [usage_trend.proto](./config_2.md#usage_trend)
- `ValidationResult` - [validation_result.proto](./config_2.md#validation_result)
- `ValidationRule` - [validation_rule.proto](./config_2.md#validation_rule)
- `ValueDependency` - [value_dependency.proto](./config_2.md#value_dependency)
- `ValueHistoryEntry` - [value_history_entry.proto](./config_2.md#value_history_entry)
- `ValueReference` - [value_reference.proto](./config_2.md#value_reference)
- `ValueUsageStatistics` - [value_usage_statistics.proto](./config_2.md#value_usage_statistics)
- `ValueUsageTrend` - [value_usage_trend.proto](./config_2.md#value_usage_trend)
- `ValueValidationResult` - [value_validation_result.proto](./config_2.md#value_validation_result)
- `VersionArtifact` - [version_artifact.proto](./config_2.md#version_artifact)
- `VersionCompatibilityInfo` - [version_compatibility_info.proto](./config_2.md#version_compatibility_info)
- `VersionDependency` - [version_dependency.proto](./config_2.md#version_dependency)
- `VersionDeploymentInfo` - [version_deployment_info.proto](./config_2.md#version_deployment_info)
- `VersionQualityIssue` - [version_quality_issue.proto](./config_2.md#version_quality_issue)
- `VersionQualityMetrics` - [version_quality_metrics.proto](./config_2.md#version_quality_metrics)
- `GetSchemaRequest` - [get_schema_request.proto](./config_api.md#get_schema_request)
- `GetSchemaResponse` - [get_schema_response.proto](./config_api.md#get_schema_response)
- `HealthCheckRequest` - [health_check_request.proto](./config_api.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./config_api.md#health_check_response)
- `AuditSettings` - [audit_settings.proto](./config_config_1.md#audit_settings)
- `BackupConfigRequest` - [backup_config_request.proto](./config_config_1.md#backup_config_request)
- `BackupSettings` - [backup_settings.proto](./config_config_1.md#backup_settings)
- `BatchingSettings` - [batching_settings.proto](./config_config_1.md#batching_settings)
- `CachingSettings` - [caching_settings.proto](./config_config_1.md#caching_settings)
- `ComplianceSettings` - [compliance_settings.proto](./config_config_1.md#compliance_settings)
- `ConfigBackup` - [config_backup.proto](./config_config_1.md#config_backup)
- `ConfigChange` - [config_change.proto](./config_config_1.md#config_change)
- `ConfigDiff` - [config_diff.proto](./config_config_1.md#config_diff)
- `ConfigDiffEntry` - [config_diff.proto](./config_config_1.md#config_diff)
- `ConfigEntry` - [config_entry.proto](./config_config_1.md#config_entry)
- `ConfigEnvironment` - [config_environment.proto](./config_config_1.md#config_environment)
- `PromotionRule` - [config_environment.proto](./config_config_1.md#config_environment)
- `DeploymentInfo` - [config_environment.proto](./config_config_1.md#config_environment)
- `HealthCheck` - [config_environment.proto](./config_config_1.md#config_environment)
- `DeploymentRollbackInfo` - [config_environment.proto](./config_config_1.md#config_environment)
- `HealthStatus` - [config_environment.proto](./config_config_1.md#config_environment)
- `HealthCheckResult` - [config_environment.proto](./config_config_1.md#config_environment)
- `ResourceLimits` - [config_environment.proto](./config_config_1.md#config_environment)
- `BackupPolicy` - [config_environment.proto](./config_config_1.md#config_environment)
- `ApprovalWorkflow` - [config_environment.proto](./config_config_1.md#config_environment)
- `ApprovalStage` - [config_environment.proto](./config_config_1.md#config_environment)
- `MonitoringConfig` - [config_environment.proto](./config_config_1.md#config_environment)
- `RetentionPolicy` - [config_environment.proto](./config_config_1.md#config_environment)
- `EncryptionSettings` - [config_environment.proto](./config_config_1.md#config_environment)
- `SyncSettings` - [config_environment.proto](./config_config_1.md#config_environment)
- `ConfigSchema` - [config_schema.proto](./config_config_1.md#config_schema)
- `ConfigSnapshot` - [config_snapshot.proto](./config_config_1.md#config_snapshot)
- `ConfigStats` - [config_stats.proto](./config_config_1.md#config_stats)
- `ConfigValidationError` - [config_validation_error.proto](./config_config_1.md#config_validation_error)
- `ConfigValidationWarning` - [config_validation_warning.proto](./config_config_1.md#config_validation_warning)
- `ConfigWatch` - [config_watch.proto](./config_config_1.md#config_watch)
- `ConfigWatchEvent` - [config_watch.proto](./config_config_1.md#config_watch)
- `DecryptConfigRequest` - [decrypt_config_request.proto](./config_config_1.md#decrypt_config_request)
- `DeleteConfigRequest` - [delete_config_request.proto](./config_config_1.md#delete_config_request)
- `EncryptConfigRequest` - [encrypt_config_request.proto](./config_config_1.md#encrypt_config_request)
- `ExportConfigRequest` - [export_config_request.proto](./config_config_1.md#export_config_request)
- `GetConfigHistoryRequest` - [get_config_history_request.proto](./config_config_1.md#get_config_history_request)
- `GetConfigHistoryResponse` - [get_config_history_response.proto](./config_config_1.md#get_config_history_response)
- `GetConfigRequest` - [get_config_request.proto](./config_config_1.md#get_config_request)
- `GetConfigResponse` - [get_config_response.proto](./config_config_1.md#get_config_response)
- `GetConfigStatsRequest` - [get_config_stats_request.proto](./config_config_1.md#get_config_stats_request)
- `GetConfigStatsResponse` - [get_config_stats_response.proto](./config_config_1.md#get_config_stats_response)
- `GetMultipleConfigRequest` - [get_multiple_config_request.proto](./config_config_1.md#get_multiple_config_request)
- `GetMultipleConfigResponse` - [get_multiple_config_response.proto](./config_config_1.md#get_multiple_config_response)
- `ImportConfigRequest` - [import_config_request.proto](./config_config_1.md#import_config_request)
- `InheritanceSettings` - [inheritance_settings.proto](./config_config_1.md#inheritance_settings)
- `ListConfigRequest` - [list_config_request.proto](./config_config_1.md#list_config_request)
- `ListConfigResponse` - [list_config_response.proto](./config_config_1.md#list_config_response)
- `MonitoringSettings` - [monitoring_settings.proto](./config_config_1.md#monitoring_settings)
- `NotificationSettings` - [notification_settings.proto](./config_config_1.md#notification_settings)
- `ReloadConfigRequest` - [reload_config_request.proto](./config_config_1.md#reload_config_request)
- `RestoreConfigRequest` - [restore_config_request.proto](./config_config_1.md#restore_config_request)
- `RetrySettings` - [retry_settings.proto](./config_config_1.md#retry_settings)
- `RollbackConfigRequest` - [rollback_config_request.proto](./config_config_1.md#rollback_config_request)
- `RotationSettings` - [rotation_settings.proto](./config_config_1.md#rotation_settings)
- `SecretAuditSettings` - [secret_audit_settings.proto](./config_config_1.md#secret_audit_settings)
- `SecretBackupSettings` - [secret_backup_settings.proto](./config_config_1.md#secret_backup_settings)
- `SetConfigRequest` - [set_config_request.proto](./config_config_1.md#set_config_request)
- `SetConfigResponse` - [set_config_response.proto](./config_config_1.md#set_config_response)
- `SetConfigSchemaRequest` - [set_config_schema_request.proto](./config_config_1.md#set_config_schema_request)
- `SetMultipleConfigRequest` - [set_multiple_config_request.proto](./config_config_1.md#set_multiple_config_request)
- `SetMultipleConfigResponse` - [set_multiple_config_response.proto](./config_config_1.md#set_multiple_config_response)
- `SynchronizationSettings` - [synchronization_settings.proto](./config_config_1.md#synchronization_settings)
- `TransformationSettings` - [transformation_settings.proto](./config_config_2.md#transformation_settings)
- `UnwatchConfigRequest` - [unwatch_config_request.proto](./config_config_2.md#unwatch_config_request)
- `ValidateConfigRequest` - [validate_config_request.proto](./config_config_2.md#validate_config_request)
- `ValidateConfigResponse` - [validate_config_response.proto](./config_config_2.md#validate_config_response)
- `ValidationSettings` - [validation_settings.proto](./config_config_2.md#validation_settings)
- `VersioningSettings` - [versioning_settings.proto](./config_config_2.md#versioning_settings)
- `WatchConfigRequest` - [watch_config_request.proto](./config_config_2.md#watch_config_request)
- `WatchConfigResponse` - [watch_config_response.proto](./config_config_2.md#watch_config_response)
- `ComplianceAudit` - [compliance_audit.proto](./config_events.md#compliance_audit)
- `RotationEvent` - [rotation_event.proto](./config_events.md#rotation_event)
- `VersionPromotionEvent` - [version_promotion_event.proto](./config_events.md#version_promotion_event)
- `BatchExecuteOptions` - [batch_execute_options.proto](./database.md#batch_execute_options)
- `BatchOperation` - [batch_operation.proto](./database.md#batch_operation)
- `BatchOperationResult` - [batch_operation_result.proto](./database.md#batch_operation_result)
- `BatchStats` - [batch_stats.proto](./database.md#batch_stats)
- `ColumnMetadata` - [column_metadata.proto](./database.md#column_metadata)
- `ConnectionPoolInfo` - [connection_pool_info.proto](./database.md#connection_pool_info)
- `DatabaseInfo` - [database_info.proto](./database.md#database_info)
- `DatabaseStatus` - [database_status.proto](./database.md#database_status)
- `ExecuteOptions` - [execute_options.proto](./database.md#execute_options)
- `ExecuteStats` - [execute_stats.proto](./database.md#execute_stats)
- `MigrationInfo` - [migration_info.proto](./database.md#migration_info)
- `MigrationScript` - [migration_script.proto](./database.md#migration_script)
- `MySQLStatus` - [mysql_status.proto](./database.md#mysql_status)
- `PoolStats` - [pool_stats.proto](./database.md#pool_stats)
- `QueryOptions` - [query_options.proto](./database.md#query_options)
- `QueryParameter` - [query_parameter.proto](./database.md#query_parameter)
- `QueryStats` - [query_stats.proto](./database.md#query_stats)
- `ResultSet` - [result_set.proto](./database.md#result_set)
- `Row` - [row.proto](./database.md#row)
- `TransactionOptions` - [transaction_options.proto](./database.md#transaction_options)
- `BeginTransactionRequest` - [begin_transaction_request.proto](./database_api.md#begin_transaction_request)
- `BeginTransactionResponse` - [begin_transaction_response.proto](./database_api.md#begin_transaction_response)
- `CommitTransactionRequest` - [commit_transaction_request.proto](./database_api.md#commit_transaction_request)
- `CreateDatabaseRequest` - [create_database_request.proto](./database_api.md#create_database_request)
- `CreateDatabaseResponse` - [create_database_response.proto](./database_api.md#create_database_response)
- `CreateSchemaRequest` - [create_schema_request.proto](./database_api.md#create_schema_request)
- `CreateSchemaResponse` - [create_schema_response.proto](./database_api.md#create_schema_response)
- `DropDatabaseRequest` - [drop_database_request.proto](./database_api.md#drop_database_request)
- `DropSchemaRequest` - [drop_schema_request.proto](./database_api.md#drop_schema_request)
- `ExecuteBatchRequest` - [execute_batch_request.proto](./database_api.md#execute_batch_request)
- `ExecuteBatchResponse` - [execute_batch_response.proto](./database_api.md#execute_batch_response)
- `ExecuteRequest` - [execute_request.proto](./database_api.md#execute_request)
- `ExecuteResponse` - [execute_response.proto](./database_api.md#execute_response)
- `GetConnectionInfoRequest` - [get_connection_info_request.proto](./database_api.md#get_connection_info_request)
- `GetConnectionInfoResponse` - [get_connection_info_response.proto](./database_api.md#get_connection_info_response)
- `GetDatabaseInfoRequest` - [get_database_info_request.proto](./database_api.md#get_database_info_request)
- `GetDatabaseInfoResponse` - [get_database_info_response.proto](./database_api.md#get_database_info_response)
- `GetMigrationStatusRequest` - [get_migration_status_request.proto](./database_api.md#get_migration_status_request)
- `GetMigrationStatusResponse` - [get_migration_status_response.proto](./database_api.md#get_migration_status_response)
- `HealthCheckRequest` - [health_check_request.proto](./database_api.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./database_api.md#health_check_response)
- `ListDatabasesRequest` - [list_databases_request.proto](./database_api.md#list_databases_request)
- `ListDatabasesResponse` - [list_databases_response.proto](./database_api.md#list_databases_response)
- `ListMigrationsRequest` - [list_migrations_request.proto](./database_api.md#list_migrations_request)
- `ListMigrationsResponse` - [list_migrations_response.proto](./database_api.md#list_migrations_response)
- `ListSchemasRequest` - [list_schemas_request.proto](./database_api.md#list_schemas_request)
- `ListSchemasResponse` - [list_schemas_response.proto](./database_api.md#list_schemas_response)
- `QueryRequest` - [query_request.proto](./database_api.md#query_request)
- `QueryResponse` - [query_response.proto](./database_api.md#query_response)
- `QueryRowRequest` - [query_row_request.proto](./database_api.md#query_row_request)
- `QueryRowResponse` - [query_row_response.proto](./database_api.md#query_row_response)
- `RevertMigrationRequest` - [revert_migration_request.proto](./database_api.md#revert_migration_request)
- `RevertMigrationResponse` - [revert_migration_response.proto](./database_api.md#revert_migration_response)
- `RollbackTransactionRequest` - [rollback_transaction_request.proto](./database_api.md#rollback_transaction_request)
- `RunMigrationRequest` - [run_migration_request.proto](./database_api.md#run_migration_request)
- `RunMigrationResponse` - [run_migration_response.proto](./database_api.md#run_migration_response)
- `TransactionStatusRequest` - [transaction_status_request.proto](./database_api.md#transaction_status_request)
- `TransactionStatusResponse` - [transaction_status_response.proto](./database_api.md#transaction_status_response)
- `CockroachConfig` - [cockroach_config.proto](./database_config.md#cockroach_config)
- `MySQLConfig` - [mysql_config.proto](./database_config.md#mysql_config)
- `PebbleConfig` - [pebble_config.proto](./database_config.md#pebble_config)
- `CheckResult` - [check_result.proto](./health.md#check_result)
- `ConfigureAlertingRequest` - [configure_alerting_request.proto](./health.md#configure_alerting_request)
- `ConfigureAlertingResponse` - [configure_alerting_response.proto](./health.md#configure_alerting_response)
- `DisableCheckRequest` - [disable_check_request.proto](./health.md#disable_check_request)
- `DisableCheckResponse` - [disable_check_response.proto](./health.md#disable_check_response)
- `EnableCheckRequest` - [enable_check_request.proto](./health.md#enable_check_request)
- `EnableCheckResponse` - [enable_check_response.proto](./health.md#enable_check_response)
- `GetCheckStatusRequest` - [get_check_status_request.proto](./health.md#get_check_status_request)
- `GetHealthHistoryRequest` - [get_health_history_request.proto](./health.md#get_health_history_request)
- `GetHealthMetricsRequest` - [get_health_metrics_request.proto](./health.md#get_health_metrics_request)
- `GetHealthMetricsResponse` - [get_health_metrics_response.proto](./health.md#get_health_metrics_response)
- `GetHealthRequest` - [get_health_request.proto](./health.md#get_health_request)
- `GetServiceHealthRequest` - [get_service_health_request.proto](./health.md#get_service_health_request)
- `GetServiceHealthResponse` - [get_service_health_response.proto](./health.md#get_service_health_response)
- `HealthCheckRequest` - [health_check_request.proto](./health.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./health.md#health_check_response)
- `HealthMetricData` - [health_metric_data.proto](./health.md#health_metric_data)
- `HealthMetrics` - [health_metrics.proto](./health.md#health_metrics)
- `ListChecksRequest` - [list_checks_request.proto](./health.md#list_checks_request)
- `ListServicesRequest` - [list_services_request.proto](./health.md#list_services_request)
- `ListServicesResponse` - [list_services_response.proto](./health.md#list_services_response)
- `RegisterCheckRequest` - [register_check_request.proto](./health.md#register_check_request)
- `RegisterCheckResponse` - [register_check_response.proto](./health.md#register_check_response)
- `ResetHealthStatsRequest` - [reset_health_stats_request.proto](./health.md#reset_health_stats_request)
- `ResetHealthStatsResponse` - [reset_health_stats_response.proto](./health.md#reset_health_stats_response)
- `RunCheckRequest` - [run_check_request.proto](./health.md#run_check_request)
- `RunCheckResponse` - [run_check_response.proto](./health.md#run_check_response)
- `SetHealthRequest` - [set_health_request.proto](./health.md#set_health_request)
- `SetHealthResponse` - [set_health_response.proto](./health.md#set_health_response)
- `UnregisterCheckRequest` - [unregister_check_request.proto](./health.md#unregister_check_request)
- `UnregisterCheckResponse` - [unregister_check_response.proto](./health.md#unregister_check_response)
- `WatchRequest` - [watch_request.proto](./health.md#watch_request)
- `WatchResponse` - [watch_response.proto](./health.md#watch_response)
- `AppenderConfig` - [appender_config.proto](./log.md#appender_config)
- `OutputConfig` - [appender_config.proto](./log.md#appender_config)
- `FormatterConfig` - [appender_config.proto](./log.md#appender_config)
- `ArchiveCriteria` - [archive_criteria.proto](./log.md#archive_criteria)
- `ErrorInfo` - [error_info.proto](./log.md#error_info)
- `LogEntry` - [log_entry.proto](./log.md#log_entry)
- `LogStatistics` - [log_statistics.proto](./log.md#log_statistics)
- `LoggerConfig` - [logger_config.proto](./log.md#logger_config)
- `SourceLocation` - [source_location.proto](./log.md#source_location)
- `AudioTrack` - [audio_track.proto](./media.md#audio_track)
- `MediaFile` - [media_file.proto](./media.md#media_file)
- `MediaMetadata` - [media_metadata.proto](./media.md#media_metadata)
- `MediaQuality` - [media_quality.proto](./media.md#media_quality)
- `MovieInfo` - [movie_info.proto](./media.md#movie_info)
- `SeriesInfo` - [series_info.proto](./media.md#series_info)
- `SubtitleTrack` - [subtitle_track.proto](./media.md#subtitle_track)
- `AlertNotification` - [alert_notification.proto](./metrics_1.md#alert_notification)
- `AlertingCondition` - [alerting_condition.proto](./metrics_1.md#alerting_condition)
- `AlertingRule` - [alerting_rule.proto](./metrics_1.md#alerting_rule)
- `BackupInfo` - [backup_info.proto](./metrics_1.md#backup_info)
- `BatchOptions` - [batch_options.proto](./metrics_1.md#batch_options)
- `CounterMetric` - [counter_metric.proto](./metrics_1.md#counter_metric)
- `DeletionOptions` - [deletion_options.proto](./metrics_1.md#deletion_options)
- `DryRunResult` - [dry_run_result.proto](./metrics_1.md#dry_run_result)
- `ErrorStats` - [error_stats.proto](./metrics_1.md#error_stats)
- `ErrorTypeCount` - [error_stats.proto](./metrics_1.md#error_stats)
- `ExportDestinationUpdate` - [export_destination_update.proto](./metrics_1.md#export_destination_update)
- `GaugeMetric` - [gauge_metric.proto](./metrics_1.md#gauge_metric)
- `HistogramBucket` - [histogram_bucket.proto](./metrics_1.md#histogram_bucket)
- `HistogramMetric` - [histogram_metric.proto](./metrics_1.md#histogram_metric)
- `MetricAggregation` - [metric_aggregation_result.proto](./metrics_1.md#metric_aggregation_result)
- `MetricBucket` - [metric_bucket.proto](./metrics_1.md#metric_bucket)
- `MetricData` - [metric_data.proto](./metrics_1.md#metric_data)
- `MetricSeries` - [metric_data.proto](./metrics_1.md#metric_data)
- `MetricFamily` - [metric_data.proto](./metrics_1.md#metric_data)
- `MetricFamily` - [metric_family.proto](./metrics_1.md#metric_family)
- `MetricFilter` - [metric_filter.proto](./metrics_1.md#metric_filter)
- `MetricHealth` - [metric_health.proto](./metrics_1.md#metric_health)
- `MetricLabel` - [metric_label.proto](./metrics_1.md#metric_label)
- `MetricMetadata` - [metric_metadata.proto](./metrics_1.md#metric_metadata)
- `MetricQuantile` - [metric_quantile.proto](./metrics_1.md#metric_quantile)
- `MetricQuery` - [metric_query.proto](./metrics_1.md#metric_query)
- `AggregationSpec` - [metric_query.proto](./metrics_1.md#metric_query)
- `GroupBySpec` - [metric_query.proto](./metrics_1.md#metric_query)
- `QueryPlan` - [metric_query.proto](./metrics_1.md#metric_query)
- `QueryStep` - [metric_query.proto](./metrics_1.md#metric_query)
- `MetricSample` - [metric_sample.proto](./metrics_1.md#metric_sample)
- `MetricStats` - [metric_stats.proto](./metrics_1.md#metric_stats)
- `MetricValue` - [metric_value.proto](./metrics_1.md#metric_value)
- `HistogramValue` - [metric_value.proto](./metrics_1.md#metric_value)
- `SummaryValue` - [metric_value.proto](./metrics_1.md#metric_value)
- `Quantile` - [metric_value.proto](./metrics_1.md#metric_value)
- `PaginationInfo` - [pagination_info.proto](./metrics_1.md#pagination_info)
- `PerformanceStats` - [performance_stats.proto](./metrics_1.md#performance_stats)
- `ProviderInfo` - [provider_info.proto](./metrics_1.md#provider_info)
- `ProviderStatus` - [provider_status.proto](./metrics_2.md#provider_status)
- `ProviderSummary` - [provider_summary.proto](./metrics_2.md#provider_summary)
- `QueryStats` - [query_stats.proto](./metrics_2.md#query_stats)
- `RecordingStats` - [recording_stats.proto](./metrics_2.md#recording_stats)
- `ResourceLimitsSummary` - [resource_limits_summary.proto](./metrics_2.md#resource_limits_summary)
- `ResourceLimitsUpdate` - [resource_limits_update.proto](./metrics_2.md#resource_limits_update)
- `RetentionPolicyInfo` - [retention_policy.proto](./metrics_2.md#retention_policy)
- `ScrapeJob` - [scrape_job.proto](./metrics_2.md#scrape_job)
- `ScrapeTarget` - [scrape_target.proto](./metrics_2.md#scrape_target)
- `SummaryQuantile` - [summary_metric.proto](./metrics_2.md#summary_metric)
- `SummaryMetric` - [summary_metric.proto](./metrics_2.md#summary_metric)
- `TagUpdates` - [tag_updates.proto](./metrics_2.md#tag_updates)
- `TimeRange` - [time_range.proto](./metrics_2.md#time_range)
- `TimeSeries` - [time_series.proto](./metrics_2.md#time_series)
- `TimerMetric` - [timer_metric.proto](./metrics_2.md#timer_metric)
- `TimerStatistics` - [timer_metric.proto](./metrics_2.md#timer_metric)
- `PercentileMeasurement` - [timer_metric.proto](./metrics_2.md#timer_metric)
- `TimestampRange` - [timestamp_range.proto](./metrics_2.md#timestamp_range)
- `TopMetrics` - [top_metrics.proto](./metrics_2.md#top_metrics)
- `UpdateOptions` - [update_options.proto](./metrics_2.md#update_options)
- `UpdateResult` - [update_result.proto](./metrics_2.md#update_result)
- `ValidationResult` - [validation_result.proto](./metrics_2.md#validation_result)
- `CreateMetricRequest` - [create_metric_request.proto](./metrics_api_1.md#create_metric_request)
- `CreateMetricResponse` - [create_metric_response.proto](./metrics_api_1.md#create_metric_response)
- `CreateProviderRequest` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `ProviderConfig` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `ProviderSettings` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `PrometheusSettings` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `OpenTelemetrySettings` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `StatsDSettings` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `ExportDestination` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `ResourceLimits` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `SecurityConfig` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `TLSConfig` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `APIKeyConfig` - [create_provider_request.proto](./metrics_api_1.md#create_provider_request)
- `CreateProviderResponse` - [create_provider_response.proto](./metrics_api_1.md#create_provider_response)
- `AppliedConfig` - [create_provider_response.proto](./metrics_api_1.md#create_provider_response)
- `ResourceAllocations` - [create_provider_response.proto](./metrics_api_1.md#create_provider_response)
- `ProviderEndpoints` - [create_provider_response.proto](./metrics_api_1.md#create_provider_response)
- `DeleteMetricRequest` - [delete_metric_request.proto](./metrics_api_1.md#delete_metric_request)
- `DeleteMetricResponse` - [delete_metric_response.proto](./metrics_api_1.md#delete_metric_response)
- `DeleteProviderRequest` - [delete_provider_request.proto](./metrics_api_1.md#delete_provider_request)
- `DeleteProviderResponse` - [delete_provider_response.proto](./metrics_api_1.md#delete_provider_response)
- `DeletionResult` - [delete_provider_response.proto](./metrics_api_1.md#delete_provider_response)
- `ExportMetricsRequest` - [export_metrics_request.proto](./metrics_api_1.md#export_metrics_request)
- `ExportMetricsResponse` - [export_metrics_response.proto](./metrics_api_1.md#export_metrics_response)
- `GetAlertingRulesRequest` - [get_alerting_rules_request.proto](./metrics_api_1.md#get_alerting_rules_request)
- `GetAlertingRulesResponse` - [get_alerting_rules_response.proto](./metrics_api_1.md#get_alerting_rules_response)
- `GetMetricMetadataRequest` - [get_metric_metadata_request.proto](./metrics_api_1.md#get_metric_metadata_request)
- `GetMetricMetadataResponse` - [get_metric_metadata_response.proto](./metrics_api_1.md#get_metric_metadata_response)
- `GetMetricRequest` - [get_metric_request.proto](./metrics_api_1.md#get_metric_request)
- `GetMetricResponse` - [get_metric_response.proto](./metrics_api_1.md#get_metric_response)
- `GetMetricsRequest` - [get_metrics_request.proto](./metrics_api_1.md#get_metrics_request)
- `SecondarySortField` - [get_metrics_request.proto](./metrics_api_1.md#get_metrics_request)
- `OutputOptions` - [get_metrics_request.proto](./metrics_api_1.md#get_metrics_request)
- `GetMetricsResponse` - [get_metrics_response.proto](./metrics_api_1.md#get_metrics_response)
- `GetMetricsSummaryRequest` - [get_metrics_summary_request.proto](./metrics_api_1.md#get_metrics_summary_request)
- `SummaryOptions` - [get_metrics_summary_request.proto](./metrics_api_1.md#get_metrics_summary_request)
- `GetMetricsSummaryResponse` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `MetricsSummary` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `MetricTypeCounts` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `MetricInfo` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `MetricsHealthInfo` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `RetentionInfo` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `ExportStatus` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `ExporterStatus` - [get_metrics_summary_response.proto](./metrics_api_1.md#get_metrics_summary_response)
- `GetProviderStatsRequest` - [get_provider_stats_request.proto](./metrics_api_1.md#get_provider_stats_request)
- `StatsOptions` - [get_provider_stats_request.proto](./metrics_api_1.md#get_provider_stats_request)
- `GetProviderStatsResponse` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ProviderStatistics` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `PerformanceDataPoint` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ResourceUsageStats` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `MemoryUsage` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `CPUUsage` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `DiskUsage` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `NetworkUsage` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ResourceDataPoint` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ErrorTypeStats` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ErrorEntry` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ErrorDataPoint` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `DataVolumeStats` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `DataVolumeDataPoint` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ExportStats` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ExportDestinationStats` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `HealthStatusEntry` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ConfigurationSummary` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `SecuritySummary` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `MetricSummary` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `TrendAnalysis` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `PerformanceTrend` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ResourceUsageTrend` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `ErrorTrend` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `DataVolumeTrend` - [get_provider_stats_response.proto](./metrics_api_1.md#get_provider_stats_response)
- `GetStatsRequest` - [get_stats_request.proto](./metrics_api_1.md#get_stats_request)
- `GetStatsResponse` - [get_stats_response.proto](./metrics_api_1.md#get_stats_response)
- `HealthCheckRequest` - [health_check_request.proto](./metrics_api_1.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./metrics_api_1.md#health_check_response)
- `ImportMetricsRequest` - [import_metrics_request.proto](./metrics_api_1.md#import_metrics_request)
- `ImportMetricsResponse` - [import_metrics_response.proto](./metrics_api_1.md#import_metrics_response)
- `ListMetricsRequest` - [list_metrics_request.proto](./metrics_api_1.md#list_metrics_request)
- `ListMetricsResponse` - [list_metrics_response.proto](./metrics_api_1.md#list_metrics_response)
- `ListProvidersRequest` - [list_providers_request.proto](./metrics_api_1.md#list_providers_request)
- `ProviderFilter` - [list_providers_request.proto](./metrics_api_1.md#list_providers_request)
- `ListProvidersResponse` - [list_providers_response.proto](./metrics_api_1.md#list_providers_response)
- `ProviderConfigSummary` - [list_providers_response.proto](./metrics_api_1.md#list_providers_response)
- `ProviderStats` - [list_providers_response.proto](./metrics_api_1.md#list_providers_response)
- `ResourceUsage` - [list_providers_response.proto](./metrics_api_1.md#list_providers_response)
- `QueryMetricsRequest` - [query_metrics_request.proto](./metrics_api_1.md#query_metrics_request)
- `QueryOutputOptions` - [query_metrics_request.proto](./metrics_api_1.md#query_metrics_request)
- `QueryMetricsResponse` - [query_metrics_response.proto](./metrics_api_1.md#query_metrics_response)
- `QueryStatistics` - [query_metrics_response.proto](./metrics_api_1.md#query_metrics_response)
- `RecordCounterRequest` - [record_counter_request.proto](./metrics_api_1.md#record_counter_request)
- `RecordCounterResponse` - [record_counter_response.proto](./metrics_api_1.md#record_counter_response)
- `RecordGaugeRequest` - [record_gauge_request.proto](./metrics_api_1.md#record_gauge_request)
- `RecordGaugeResponse` - [record_gauge_response.proto](./metrics_api_1.md#record_gauge_response)
- `RecordHistogramRequest` - [record_histogram_request.proto](./metrics_api_1.md#record_histogram_request)
- `RecordHistogramResponse` - [record_histogram_response.proto](./metrics_api_1.md#record_histogram_response)
- `BucketInfo` - [record_histogram_response.proto](./metrics_api_1.md#record_histogram_response)
- `HistogramStats` - [record_histogram_response.proto](./metrics_api_1.md#record_histogram_response)
- `RecordMetricRequest` - [record_metric_request.proto](./metrics_api_1.md#record_metric_request)
- `BatchContext` - [record_metric_request.proto](./metrics_api_1.md#record_metric_request)
- `RecordMetricResponse` - [record_metric_response.proto](./metrics_api_1.md#record_metric_response)
- `RecordMetricsRequest` - [record_metrics_request.proto](./metrics_api_1.md#record_metrics_request)
- `RecordMetricsResponse` - [record_metrics_response.proto](./metrics_api_1.md#record_metrics_response)
- `MetricResult` - [record_metrics_response.proto](./metrics_api_1.md#record_metrics_response)
- `BatchStats` - [record_metrics_response.proto](./metrics_api_1.md#record_metrics_response)
- `ValidationSummary` - [record_metrics_response.proto](./metrics_api_1.md#record_metrics_response)
- `RecordSummaryRequest` - [record_summary_request.proto](./metrics_api_1.md#record_summary_request)
- `RecordSummaryResponse` - [record_summary_response.proto](./metrics_api_1.md#record_summary_response)
- `RegisterMetricRequest` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `MetricDefinition` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `LabelDefinition` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `MetricTypeConfig` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `HistogramConfig` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `SummaryConfig` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `GaugeConfig` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `CounterConfig` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `ValidationRules` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `RegistrationOptions` - [register_metric_request.proto](./metrics_api_1.md#register_metric_request)
- `RegisterMetricResponse` - [register_metric_response.proto](./metrics_api_1.md#register_metric_response)
- `RegistrationValidation` - [register_metric_response.proto](./metrics_api_1.md#register_metric_response)
- `RegistrationResult` - [register_metric_response.proto](./metrics_api_1.md#register_metric_response)
- `SchemaChange` - [register_metric_response.proto](./metrics_api_1.md#register_metric_response)
- `ResetMetricsRequest` - [reset_metrics_request.proto](./metrics_api_1.md#reset_metrics_request)
- `ResetMetricsResponse` - [reset_metrics_response.proto](./metrics_api_1.md#reset_metrics_response)
- `SetAlertingRulesRequest` - [set_alerting_rules_request.proto](./metrics_api_2.md#set_alerting_rules_request)
- `SetAlertingRulesResponse` - [set_alerting_rules_response.proto](./metrics_api_2.md#set_alerting_rules_response)
- `SetMetricMetadataRequest` - [set_metric_metadata_request.proto](./metrics_api_2.md#set_metric_metadata_request)
- `SetMetricMetadataResponse` - [set_metric_metadata_response.proto](./metrics_api_2.md#set_metric_metadata_response)
- `StartScrapingRequest` - [start_scraping_request.proto](./metrics_api_2.md#start_scraping_request)
- `StartScrapingResponse` - [start_scraping_response.proto](./metrics_api_2.md#start_scraping_response)
- `StopScrapingRequest` - [stop_scraping_request.proto](./metrics_api_2.md#stop_scraping_request)
- `StopScrapingResponse` - [stop_scraping_response.proto](./metrics_api_2.md#stop_scraping_response)
- `StreamMetricsRequest` - [stream_metrics_request.proto](./metrics_api_2.md#stream_metrics_request)
- `StreamOptions` - [stream_metrics_request.proto](./metrics_api_2.md#stream_metrics_request)
- `StreamStart` - [stream_metrics_request.proto](./metrics_api_2.md#stream_metrics_request)
- `BufferConfig` - [stream_metrics_request.proto](./metrics_api_2.md#stream_metrics_request)
- `UnregisterMetricRequest` - [unregister_metric_request.proto](./metrics_api_2.md#unregister_metric_request)
- `UnregistrationOptions` - [unregister_metric_request.proto](./metrics_api_2.md#unregister_metric_request)
- `UnregisterMetricResponse` - [unregister_metric_response.proto](./metrics_api_2.md#unregister_metric_response)
- `UnregistrationResult` - [unregister_metric_response.proto](./metrics_api_2.md#unregister_metric_response)
- `UpdateMetricRequest` - [update_metric_request.proto](./metrics_api_2.md#update_metric_request)
- `UpdateMetricResponse` - [update_metric_response.proto](./metrics_api_2.md#update_metric_response)
- `UpdateProviderRequest` - [update_provider_request.proto](./metrics_api_2.md#update_provider_request)
- `UpdateProviderResponse` - [update_provider_response.proto](./metrics_api_2.md#update_provider_response)
- `APIKeyConfigUpdate` - [apikey_config_update.proto](./metrics_config.md#apikey_config_update)
- `ConfigChange` - [config_change.proto](./metrics_config.md#config_change)
- `ExportConfig` - [export_config.proto](./metrics_config.md#export_config)
- `ExportConfig` - [export_config_options.proto](./metrics_config.md#export_config_options)
- `ExportConfigUpdate` - [export_config_update.proto](./metrics_config.md#export_config_update)
- `GetMetricConfigRequest` - [get_metric_config_request.proto](./metrics_config.md#get_metric_config_request)
- `GetMetricConfigResponse` - [get_metric_config_response.proto](./metrics_config.md#get_metric_config_response)
- `GetScrapeConfigRequest` - [get_scrape_config_request.proto](./metrics_config.md#get_scrape_config_request)
- `GetScrapeConfigResponse` - [get_scrape_config_response.proto](./metrics_config.md#get_scrape_config_response)
- `ImportConfig` - [import_config.proto](./metrics_config.md#import_config)
- `MetricConfig` - [metric_config.proto](./metrics_config.md#metric_config)
- `OpenTelemetrySettingsUpdate` - [open_telemetry_settings_update.proto](./metrics_config.md#open_telemetry_settings_update)
- `PrometheusSettingsUpdate` - [prometheus_settings_update.proto](./metrics_config.md#prometheus_settings_update)
- `ProviderConfigUpdate` - [provider_config_update.proto](./metrics_config.md#provider_config_update)
- `ProviderSettingsUpdate` - [provider_settings_update.proto](./metrics_config.md#provider_settings_update)
- `RetentionPolicyConfig` - [retention_policy_retentionpolicyconfig.proto](./metrics_config.md#retention_policy_retentionpolicyconfig)
- `ScrapeConfig` - [scrape_config.proto](./metrics_config.md#scrape_config)
- `SecurityConfigUpdate` - [security_config_update.proto](./metrics_config.md#security_config_update)
- `SetMetricConfigRequest` - [set_metric_config_request.proto](./metrics_config.md#set_metric_config_request)
- `SetMetricConfigResponse` - [set_metric_config_response.proto](./metrics_config.md#set_metric_config_response)
- `SetScrapeConfigRequest` - [set_scrape_config_request.proto](./metrics_config.md#set_scrape_config_request)
- `SetScrapeConfigResponse` - [set_scrape_config_response.proto](./metrics_config.md#set_scrape_config_response)
- `StatsDSettingsUpdate` - [stats_dsettings_update.proto](./metrics_config.md#stats_dsettings_update)
- `TLSConfigUpdate` - [tlsconfig_update.proto](./metrics_config.md#tlsconfig_update)
- `DeleteNotificationRequest` - [delete_notification_request.proto](./notification.md#delete_notification_request)
- `DeleteNotificationResponse` - [delete_notification_response.proto](./notification.md#delete_notification_response)
- `DeliveryChannel` - [delivery_channel.proto](./notification.md#delivery_channel)
- `EventNotification` - [event_notification.proto](./notification.md#event_notification)
- `GetPreferencesRequest` - [get_preferences_request.proto](./notification.md#get_preferences_request)
- `GetPreferencesResponse` - [get_preferences_response.proto](./notification.md#get_preferences_response)
- `GetTemplateRequest` - [get_template_request.proto](./notification.md#get_template_request)
- `GetTemplateResponse` - [get_template_response.proto](./notification.md#get_template_response)
- `ListNotificationsRequest` - [list_notifications_request.proto](./notification.md#list_notifications_request)
- `ListNotificationsResponse` - [list_notifications_response.proto](./notification.md#list_notifications_response)
- `MarkAsReadRequest` - [mark_as_read_request.proto](./notification.md#mark_as_read_request)
- `MarkAsReadResponse` - [mark_as_read_response.proto](./notification.md#mark_as_read_response)
- `NotificationMessage` - [notification_message.proto](./notification.md#notification_message)
- `SendNotificationRequest` - [send_notification_request.proto](./notification.md#send_notification_request)
- `SendNotificationResponse` - [send_notification_response.proto](./notification.md#send_notification_response)
- `SubscriptionPreferences` - [subscription_preferences.proto](./notification.md#subscription_preferences)
- `Template` - [template.proto](./notification.md#template)
- `UpdatePreferencesRequest` - [update_preferences_request.proto](./notification.md#update_preferences_request)
- `UpdatePreferencesResponse` - [update_preferences_response.proto](./notification.md#update_preferences_response)
- `Department` - [department.proto](./organization.md#department)
- `Organization` - [organization.proto](./organization.md#organization)
- `OrganizationHierarchy` - [organization_hierarchy.proto](./organization.md#organization_hierarchy)
- `HierarchyNode` - [organization_hierarchy.proto](./organization.md#organization_hierarchy)
- `HierarchyPath` - [organization_hierarchy.proto](./organization.md#organization_hierarchy)
- `OrganizationMember` - [organization_member.proto](./organization.md#organization_member)
- `Team` - [team.proto](./organization.md#team)
- `Tenant` - [tenant.proto](./organization.md#tenant)
- `TenantIsolation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `DatabaseIsolation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `NetworkIsolation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `StorageIsolation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `ComputeIsolation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `EncryptionConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `AccessControl` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `AuditConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `BackupConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `NetworkACLRule` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `LoadBalancerConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `CDNConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `DomainConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `StorageEncryption` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `StoragePolicy` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `StorageBackupConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `StorageQuota` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `CPUAllocation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `MemoryAllocation` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `ResourceLimits` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `AutoScalingConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `TimeRestriction` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `AuditAlert` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `HealthCheckConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `SSLConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `CacheBehavior` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `OriginConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `DNSConfig` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `DNSRecord` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `CacheKeyPolicy` - [tenant_isolation.proto](./organization.md#tenant_isolation)
- `TenantQuota` - [tenant_quota.proto](./organization.md#tenant_quota)
- `AddMemberRequest` - [add_member_request.proto](./organization_api_1.md#add_member_request)
- `AddMemberResponse` - [add_member_response.proto](./organization_api_1.md#add_member_response)
- `CreateDepartmentRequest` - [create_department_request.proto](./organization_api_1.md#create_department_request)
- `CreateDepartmentResponse` - [create_department_response.proto](./organization_api_1.md#create_department_response)
- `CreateOrganizationRequest` - [create_organization_request.proto](./organization_api_1.md#create_organization_request)
- `CreateOrganizationResponse` - [create_organization_response.proto](./organization_api_1.md#create_organization_response)
- `CreateTeamRequest` - [create_team_request.proto](./organization_api_1.md#create_team_request)
- `CreateTeamResponse` - [create_team_response.proto](./organization_api_1.md#create_team_response)
- `CreateTenantRequest` - [create_tenant_request.proto](./organization_api_1.md#create_tenant_request)
- `CreateTenantResponse` - [create_tenant_response.proto](./organization_api_1.md#create_tenant_response)
- `DeleteDepartmentRequest` - [delete_department_request.proto](./organization_api_1.md#delete_department_request)
- `DeleteDepartmentResponse` - [delete_department_response.proto](./organization_api_1.md#delete_department_response)
- `DeleteOrganizationRequest` - [delete_organization_request.proto](./organization_api_1.md#delete_organization_request)
- `DeleteOrganizationResponse` - [delete_organization_response.proto](./organization_api_1.md#delete_organization_response)
- `DeleteTeamRequest` - [delete_team_request.proto](./organization_api_1.md#delete_team_request)
- `DeleteTeamResponse` - [delete_team_response.proto](./organization_api_1.md#delete_team_response)
- `DeleteTenantRequest` - [delete_tenant_request.proto](./organization_api_1.md#delete_tenant_request)
- `DeleteTenantResponse` - [delete_tenant_response.proto](./organization_api_1.md#delete_tenant_response)
- `GetDepartmentRequest` - [get_department_request.proto](./organization_api_1.md#get_department_request)
- `GetDepartmentResponse` - [get_department_response.proto](./organization_api_1.md#get_department_response)
- `GetHierarchyRequest` - [get_hierarchy_request.proto](./organization_api_1.md#get_hierarchy_request)
- `GetHierarchyResponse` - [get_hierarchy_response.proto](./organization_api_1.md#get_hierarchy_response)
- `GetOrganizationRequest` - [get_organization_request.proto](./organization_api_1.md#get_organization_request)
- `GetOrganizationResponse` - [get_organization_response.proto](./organization_api_1.md#get_organization_response)
- `GetTeamRequest` - [get_team_request.proto](./organization_api_1.md#get_team_request)
- `GetTeamResponse` - [get_team_response.proto](./organization_api_1.md#get_team_response)
- `GetTenantIsolationRequest` - [get_tenant_isolation_request.proto](./organization_api_1.md#get_tenant_isolation_request)
- `GetTenantIsolationResponse` - [get_tenant_isolation_response.proto](./organization_api_1.md#get_tenant_isolation_response)
- `GetTenantRequest` - [get_tenant_request.proto](./organization_api_1.md#get_tenant_request)
- `GetTenantResponse` - [get_tenant_response.proto](./organization_api_1.md#get_tenant_response)
- `GetTenantUsageRequest` - [get_tenant_usage_request.proto](./organization_api_1.md#get_tenant_usage_request)
- `GetTenantUsageResponse` - [get_tenant_usage_response.proto](./organization_api_1.md#get_tenant_usage_response)
- `ListDepartmentsRequest` - [list_departments_request.proto](./organization_api_1.md#list_departments_request)
- `ListDepartmentsResponse` - [list_departments_response.proto](./organization_api_1.md#list_departments_response)
- `ListMembersRequest` - [list_members_request.proto](./organization_api_1.md#list_members_request)
- `ListMembersResponse` - [list_members_response.proto](./organization_api_1.md#list_members_response)
- `ListOrganizationsRequest` - [list_organizations_request.proto](./organization_api_1.md#list_organizations_request)
- `ListOrganizationsResponse` - [list_organizations_response.proto](./organization_api_1.md#list_organizations_response)
- `ListTeamsRequest` - [list_teams_request.proto](./organization_api_1.md#list_teams_request)
- `ListTeamsResponse` - [list_teams_response.proto](./organization_api_1.md#list_teams_response)
- `ListTenantsRequest` - [list_tenants_request.proto](./organization_api_1.md#list_tenants_request)
- `ListTenantsResponse` - [list_tenants_response.proto](./organization_api_1.md#list_tenants_response)
- `RemoveMemberRequest` - [remove_member_request.proto](./organization_api_1.md#remove_member_request)
- `RemoveMemberResponse` - [remove_member_response.proto](./organization_api_1.md#remove_member_response)
- `UpdateDepartmentRequest` - [update_department_request.proto](./organization_api_1.md#update_department_request)
- `UpdateDepartmentResponse` - [update_department_response.proto](./organization_api_1.md#update_department_response)
- `UpdateHierarchyRequest` - [update_hierarchy_request.proto](./organization_api_1.md#update_hierarchy_request)
- `UpdateHierarchyResponse` - [update_hierarchy_response.proto](./organization_api_1.md#update_hierarchy_response)
- `UpdateMemberRequest` - [update_member_request.proto](./organization_api_1.md#update_member_request)
- `UpdateMemberResponse` - [update_member_response.proto](./organization_api_1.md#update_member_response)
- `UpdateOrganizationRequest` - [update_organization_request.proto](./organization_api_2.md#update_organization_request)
- `UpdateOrganizationResponse` - [update_organization_response.proto](./organization_api_2.md#update_organization_response)
- `UpdateTeamRequest` - [update_team_request.proto](./organization_api_2.md#update_team_request)
- `UpdateTeamResponse` - [update_team_response.proto](./organization_api_2.md#update_team_response)
- `UpdateTenantQuotaRequest` - [update_tenant_quota_request.proto](./organization_api_2.md#update_tenant_quota_request)
- `UpdateTenantQuotaResponse` - [update_tenant_quota_response.proto](./organization_api_2.md#update_tenant_quota_response)
- `UpdateTenantRequest` - [update_tenant_request.proto](./organization_api_2.md#update_tenant_request)
- `UpdateTenantResponse` - [update_tenant_response.proto](./organization_api_2.md#update_tenant_response)
- `ConfigureTenantIsolationRequest` - [configure_tenant_isolation_request.proto](./organization_config.md#configure_tenant_isolation_request)
- `ConfigureTenantIsolationResponse` - [configure_tenant_isolation_response.proto](./organization_config.md#configure_tenant_isolation_response)
- `GetOrganizationSettingsRequest` - [get_organization_settings_request.proto](./organization_config.md#get_organization_settings_request)
- `GetOrganizationSettingsResponse` - [get_organization_settings_response.proto](./organization_config.md#get_organization_settings_response)
- `OrganizationSettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `SecuritySettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `UISettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `IntegrationSettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `Integration` - [organization_settings.proto](./organization_config.md#organization_settings)
- `NotificationSettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `RateLimitConfig` - [organization_settings.proto](./organization_config.md#organization_settings)
- `WebhookConfig` - [organization_settings.proto](./organization_config.md#organization_settings)
- `APIKeyConfig` - [organization_settings.proto](./organization_config.md#organization_settings)
- `OAuthAppConfig` - [organization_settings.proto](./organization_config.md#organization_settings)
- `BillingSettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `ComplianceSettings` - [organization_settings.proto](./organization_config.md#organization_settings)
- `FeatureFlag` - [organization_settings.proto](./organization_config.md#organization_settings)
- `EmailTemplate` - [organization_settings.proto](./organization_config.md#organization_settings)
- `NotificationFrequency` - [organization_settings.proto](./organization_config.md#organization_settings)
- `UpdateOrganizationSettingsRequest` - [update_organization_settings_request.proto](./organization_config.md#update_organization_settings_request)
- `UpdateOrganizationSettingsResponse` - [update_organization_settings_response.proto](./organization_config.md#update_organization_settings_response)
- `Acknowledgment` - [acknowledgment.proto](./queue_1.md#acknowledgment)
- `AlertRule` - [alert_rule.proto](./queue_1.md#alert_rule)
- `AntiAffinityRule` - [anti_affinity_rule.proto](./queue_1.md#anti_affinity_rule)
- `BindingInfo` - [binding_info.proto](./queue_1.md#binding_info)
- `ClusterInfo` - [cluster_info.proto](./queue_1.md#cluster_info)
- `ClusterStats` - [cluster_stats.proto](./queue_1.md#cluster_stats)
- `ConnectionDetails` - [connection_details.proto](./queue_1.md#connection_details)
- `ConsumerGroup` - [consumer_group.proto](./queue_1.md#consumer_group)
- `ConsumerGroupConfig` - [consumer_group.proto](./queue_1.md#consumer_group)
- `AutoCommitConfig` - [consumer_group.proto](./queue_1.md#consumer_group)
- `RetryDelayConfig` - [consumer_group.proto](./queue_1.md#consumer_group)
- `Consumer` - [consumer_group.proto](./queue_1.md#consumer_group)
- `ConsumerClient` - [consumer_group.proto](./queue_1.md#consumer_group)
- `ConsumerConfig` - [consumer_group.proto](./queue_1.md#consumer_group)
- `PartitionAssignment` - [consumer_group.proto](./queue_1.md#consumer_group)
- `GroupCoordinator` - [consumer_group.proto](./queue_1.md#consumer_group)
- `ConsumerGroupStats` - [consumer_group.proto](./queue_1.md#consumer_group)
- `RebalanceStats` - [consumer_group.proto](./queue_1.md#consumer_group)
- `ConsumerErrorStats` - [consumer_group.proto](./queue_1.md#consumer_group)
- `ConsumerStats` - [consumer_stats.proto](./queue_1.md#consumer_stats)
- `DeadLetterPolicy` - [dead_letter_policy.proto](./queue_1.md#dead_letter_policy)
- `DeliveryOptions` - [delivery_options.proto](./queue_1.md#delivery_options)
- `FlowControl` - [flow_control.proto](./queue_1.md#flow_control)
- `FormatOptions` - [format_options.proto](./queue_1.md#format_options)
- `MessageEnvelope` - [message_envelope.proto](./queue_1.md#message_envelope)
- `MessageId` - [message_id.proto](./queue_1.md#message_id)
- `MessageMetadata` - [message_metadata.proto](./queue_1.md#message_metadata)
- `NackError` - [nack_error.proto](./queue_1.md#nack_error)
- `NodeInfo` - [node_info.proto](./queue_1.md#node_info)
- `NodeStats` - [node_stats.proto](./queue_1.md#node_stats)
- `NotificationChannel` - [notification_channel.proto](./queue_1.md#notification_channel)
- `OffsetInfo` - [offset_info.proto](./queue_1.md#offset_info)
- `PartitionInfo` - [partition_info.proto](./queue_1.md#partition_info)
- `PartitionOffset` - [partition_offset.proto](./queue_1.md#partition_offset)
- `PriorityRange` - [priority_range.proto](./queue_1.md#priority_range)
- `PublishResult` - [publish_result.proto](./queue_1.md#publish_result)
- `QueueInfo` - [queue_info.proto](./queue_2.md#queue_info)
- `QueueMessage` - [queue_message.proto](./queue_2.md#queue_message)
- `BasicQueueStats` - [queue_stats.proto](./queue_2.md#queue_stats)
- `ReceivedMessage` - [received_message.proto](./queue_2.md#received_message)
- `RetentionPolicy` - [retention_policy.proto](./queue_2.md#retention_policy)
- `RetryPolicy` - [retry_policy.proto](./queue_2.md#retry_policy)
- `RoutingCondition` - [routing_condition.proto](./queue_2.md#routing_condition)
- `RoutingKey` - [routing_key.proto](./queue_2.md#routing_key)
- `RoutingRule` - [routing_rule.proto](./queue_2.md#routing_rule)
- `SizeRange` - [size_range.proto](./queue_2.md#size_range)
- `SubscriptionInfo` - [subscription_info.proto](./queue_2.md#subscription_info)
- `SubscriptionStats` - [subscription_stats.proto](./queue_2.md#subscription_stats)
- `TimeRange` - [time_range.proto](./queue_2.md#time_range)
- `TimestampRange` - [timestamp_range.proto](./queue_2.md#timestamp_range)
- `TopicInfo` - [topic_info.proto](./queue_2.md#topic_info)
- `TopicStats` - [topic_stats.proto](./queue_2.md#topic_stats)
- `AckRequest` - [ack_request.proto](./queue_api_1.md#ack_request)
- `AckResponse` - [ack_response.proto](./queue_api_1.md#ack_response)
- `AcknowledgeRequest` - [acknowledge_request.proto](./queue_api_1.md#acknowledge_request)
- `MessageAckResult` - [acknowledge_response.proto](./queue_api_1.md#acknowledge_response)
- `AcknowledgeResponse` - [acknowledge_response.proto](./queue_api_1.md#acknowledge_response)
- `BackupQueueRequest` - [backup_queue_request.proto](./queue_api_1.md#backup_queue_request)
- `BackupQueueResponse` - [backup_queue_response.proto](./queue_api_1.md#backup_queue_response)
- `BatchAckRequest` - [batch_ack_request.proto](./queue_api_1.md#batch_ack_request)
- `BatchAckResponse` - [batch_ack_response.proto](./queue_api_1.md#batch_ack_response)
- `FailedAck` - [batch_ack_response.proto](./queue_api_1.md#batch_ack_response)
- `BatchNackRequest` - [batch_nack_request.proto](./queue_api_1.md#batch_nack_request)
- `MessageNack` - [batch_nack_request.proto](./queue_api_1.md#batch_nack_request)
- `BatchNackResponse` - [batch_nack_response.proto](./queue_api_1.md#batch_nack_response)
- `BatchPublishRequest` - [batch_publish_request.proto](./queue_api_1.md#batch_publish_request)
- `BatchPublishResponse` - [batch_publish_response.proto](./queue_api_1.md#batch_publish_response)
- `BatchPullRequest` - [batch_pull_request.proto](./queue_api_1.md#batch_pull_request)
- `BatchPullResponse` - [batch_pull_response.proto](./queue_api_1.md#batch_pull_response)
- `CommitOffsetRequest` - [commit_offset_request.proto](./queue_api_1.md#commit_offset_request)
- `CommitOffsetResponse` - [commit_offset_response.proto](./queue_api_1.md#commit_offset_response)
- `PartitionCommitResult` - [commit_offset_response.proto](./queue_api_1.md#commit_offset_response)
- `CreateQueueRequest` - [create_queue_request.proto](./queue_api_1.md#create_queue_request)
- `CreateQueueResponse` - [create_queue_response.proto](./queue_api_1.md#create_queue_response)
- `CreateSubscriptionRequest` - [create_subscription_request.proto](./queue_api_1.md#create_subscription_request)
- `CreateSubscriptionResponse` - [create_subscription_response.proto](./queue_api_1.md#create_subscription_response)
- `CreateTopicRequest` - [create_topic_request.proto](./queue_api_1.md#create_topic_request)
- `CreateTopicResponse` - [create_topic_response.proto](./queue_api_1.md#create_topic_response)
- `DeleteQueueRequest` - [delete_queue_request.proto](./queue_api_1.md#delete_queue_request)
- `DeleteQueueResponse` - [delete_queue_response.proto](./queue_api_1.md#delete_queue_response)
- `DeleteRequest` - [delete_request.proto](./queue_api_1.md#delete_request)
- `DeleteCriteria` - [delete_request.proto](./queue_api_1.md#delete_request)
- `DeleteResponse` - [delete_response.proto](./queue_api_1.md#delete_response)
- `DeletionStats` - [delete_response.proto](./queue_api_1.md#delete_response)
- `BackupInfo` - [delete_response.proto](./queue_api_1.md#delete_response)
- `DeleteSubscriptionRequest` - [delete_subscription_request.proto](./queue_api_1.md#delete_subscription_request)
- `DeleteSubscriptionResponse` - [delete_subscription_response.proto](./queue_api_1.md#delete_subscription_response)
- `DeleteTopicRequest` - [delete_topic_request.proto](./queue_api_1.md#delete_topic_request)
- `DeleteTopicResponse` - [delete_topic_response.proto](./queue_api_1.md#delete_topic_response)
- `DequeueRequest` - [dequeue_request.proto](./queue_api_1.md#dequeue_request)
- `DequeueResponse` - [dequeue_response.proto](./queue_api_1.md#dequeue_response)
- `EnqueueRequest` - [enqueue_request.proto](./queue_api_1.md#enqueue_request)
- `EnqueueResponse` - [enqueue_response.proto](./queue_api_1.md#enqueue_response)
- `ExportQueueRequest` - [export_queue_request.proto](./queue_api_1.md#export_queue_request)
- `ExportQueueResponse` - [export_queue_response.proto](./queue_api_1.md#export_queue_response)
- `FlushQueueRequest` - [flush_queue_request.proto](./queue_api_1.md#flush_queue_request)
- `FlushQueueResponse` - [flush_queue_response.proto](./queue_api_1.md#flush_queue_response)
- `GetClusterInfoRequest` - [get_cluster_info_request.proto](./queue_api_1.md#get_cluster_info_request)
- `GetClusterInfoResponse` - [get_cluster_info_response.proto](./queue_api_1.md#get_cluster_info_response)
- `GetMessageRequest` - [get_message_request.proto](./queue_api_1.md#get_message_request)
- `GetMessageResponse` - [get_message_response.proto](./queue_api_1.md#get_message_response)
- `GetNodeInfoRequest` - [get_node_info_request.proto](./queue_api_1.md#get_node_info_request)
- `GetNodeInfoResponse` - [get_node_info_response.proto](./queue_api_1.md#get_node_info_response)
- `GetOffsetRequest` - [get_offset_request.proto](./queue_api_1.md#get_offset_request)
- `GetOffsetResponse` - [get_offset_response.proto](./queue_api_1.md#get_offset_response)
- `GetPartitionInfoRequest` - [get_partition_info_request.proto](./queue_api_1.md#get_partition_info_request)
- `GetPartitionInfoResponse` - [get_partition_info_response.proto](./queue_api_1.md#get_partition_info_response)
- `GetQueueInfoRequest` - [get_queue_info_request.proto](./queue_api_1.md#get_queue_info_request)
- `TimeRangeFilter` - [get_queue_info_request.proto](./queue_api_1.md#get_queue_info_request)
- `GetQueueInfoResponse` - [get_queue_info_response.proto](./queue_api_1.md#get_queue_info_response)
- `GetQueueStatsResponse` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `QueueStatsSummary` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `QueueStats` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `MessageStateCounts` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `ThroughputMetrics` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `LatencyMetrics` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `QueueDepthSample` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `SizeDistribution` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `SizeBucket` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `AgeDistribution` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `AgeBucket` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `QueueConfiguration` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `QueueConsumerStats` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `HistoricalStats` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `HistoricalDataPoint` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `ErrorStats` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `ErrorTypeStat` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `PerformanceMetrics` - [get_queue_stats_response.proto](./queue_api_2.md#get_queue_stats_response)
- `GetSubscriptionInfoRequest` - [get_subscription_info_request.proto](./queue_api_2.md#get_subscription_info_request)
- `GetSubscriptionInfoResponse` - [get_subscription_info_response.proto](./queue_api_2.md#get_subscription_info_response)
- `GetTopicInfoRequest` - [get_topic_info_request.proto](./queue_api_2.md#get_topic_info_request)
- `GetTopicInfoResponse` - [get_topic_info_response.proto](./queue_api_2.md#get_topic_info_response)
- `TopicConfiguration` - [get_topic_info_response.proto](./queue_api_2.md#get_topic_info_response)
- `TopicPermissions` - [get_topic_info_response.proto](./queue_api_2.md#get_topic_info_response)
- `OwnerInfo` - [get_topic_info_response.proto](./queue_api_2.md#get_topic_info_response)
- `RetentionInfo` - [get_topic_info_response.proto](./queue_api_2.md#get_topic_info_response)
- `HealthCheckRequest` - [health_check_request.proto](./queue_api_2.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./queue_api_2.md#health_check_response)
- `ImportQueueRequest` - [import_queue_request.proto](./queue_api_2.md#import_queue_request)
- `ImportQueueResponse` - [import_queue_response.proto](./queue_api_2.md#import_queue_response)
- `ListMessagesRequest` - [list_messages_request.proto](./queue_api_2.md#list_messages_request)
- `ListMessagesResponse` - [list_messages_response.proto](./queue_api_2.md#list_messages_response)
- `ListQueuesRequest` - [list_queues_request.proto](./queue_api_2.md#list_queues_request)
- `ListQueuesResponse` - [list_queues_response.proto](./queue_api_2.md#list_queues_response)
- `ListSubscriptionsRequest` - [list_subscriptions_request.proto](./queue_api_2.md#list_subscriptions_request)
- `ListSubscriptionsResponse` - [list_subscriptions_response.proto](./queue_api_2.md#list_subscriptions_response)
- `ListTopicsRequest` - [list_topics_request.proto](./queue_api_2.md#list_topics_request)
- `ListTopicsResponse` - [list_topics_response.proto](./queue_api_2.md#list_topics_response)
- `MigrateQueueRequest` - [migrate_queue_request.proto](./queue_api_2.md#migrate_queue_request)
- `MigrateQueueResponse` - [migrate_queue_response.proto](./queue_api_2.md#migrate_queue_response)
- `NackRequest` - [nack_request.proto](./queue_api_2.md#nack_request)
- `NackResponse` - [nack_response.proto](./queue_api_2.md#nack_response)
- `PauseQueueRequest` - [pause_queue_request.proto](./queue_api_2.md#pause_queue_request)
- `PauseQueueResponse` - [pause_queue_response.proto](./queue_api_2.md#pause_queue_response)
- `PeekRequest` - [peek_request.proto](./queue_api_2.md#peek_request)
- `PeekResponse` - [peek_response.proto](./queue_api_2.md#peek_response)
- `PublishRequest` - [publish_request.proto](./queue_api_2.md#publish_request)
- `PublishResponse` - [publish_response.proto](./queue_api_2.md#publish_response)
- `PullRequest` - [pull_request.proto](./queue_api_2.md#pull_request)
- `PullResponse` - [pull_response.proto](./queue_api_2.md#pull_response)
- `PurgeRequest` - [purge_request.proto](./queue_api_2.md#purge_request)
- `PurgeOptions` - [purge_request.proto](./queue_api_2.md#purge_request)
- `PurgeResponse` - [purge_response.proto](./queue_api_2.md#purge_response)
- `PushRequest` - [push_request.proto](./queue_api_2.md#push_request)
- `Message` - [push_request.proto](./queue_api_2.md#push_request)
- `MessageProperties` - [push_request.proto](./queue_api_2.md#push_request)
- `RoutingInfo` - [push_request.proto](./queue_api_2.md#push_request)
- `PublishConfig` - [push_request.proto](./queue_api_2.md#push_request)
- `BatchSettings` - [push_request.proto](./queue_api_2.md#push_request)
- `PushResponse` - [push_response.proto](./queue_api_2.md#push_response)
- `ResetQueueStatsRequest` - [reset_queue_stats_request.proto](./queue_api_2.md#reset_queue_stats_request)
- `ResetQueueStatsResponse` - [reset_queue_stats_response.proto](./queue_api_2.md#reset_queue_stats_response)
- `PreservedStats` - [reset_queue_stats_response.proto](./queue_api_2.md#reset_queue_stats_response)
- `ResetDetails` - [reset_queue_stats_response.proto](./queue_api_2.md#reset_queue_stats_response)
- `RestoreQueueRequest` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `BackupSource` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `OriginalQueueInfo` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `EncryptionInfo` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `RestoreOptions` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `FilterCriteria` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `PerformanceOptions` - [restore_queue_request.proto](./queue_api_2.md#restore_queue_request)
- `RestoreQueueResponse` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `RestoreStatistics` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `RestoreStatus` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `RestoreError` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `RestoreWarning` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `PartitionRestoreResult` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `ValidationResult` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `ChecksumValidation` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `SchemaValidation` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `IntegrityValidation` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `ValidationError` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `OffsetRange` - [restore_queue_response.proto](./queue_api_2.md#restore_queue_response)
- `ResumeQueueRequest` - [resume_queue_request.proto](./queue_api_2.md#resume_queue_request)
- `ResumeQueueResponse` - [resume_queue_response.proto](./queue_api_2.md#resume_queue_response)
- `ResumeStats` - [resume_queue_response.proto](./queue_api_2.md#resume_queue_response)
- `SeekRequest` - [seek_request.proto](./queue_api_2.md#seek_request)
- `SeekResponse` - [seek_response.proto](./queue_api_2.md#seek_response)
- `SendMessageRequest` - [send_message_request.proto](./queue_api_2.md#send_message_request)
- `SendMessageResponse` - [send_message_response.proto](./queue_api_2.md#send_message_response)
- `StreamMessagesRequest` - [stream_messages_request.proto](./queue_api_2.md#stream_messages_request)
- `OffsetConfig` - [stream_messages_request.proto](./queue_api_2.md#stream_messages_request)
- `MessageFilter` - [stream_messages_request.proto](./queue_api_2.md#stream_messages_request)
- `FlowControlConfig` - [stream_messages_request.proto](./queue_api_2.md#stream_messages_request)
- `StreamMessagesResponse` - [stream_messages_response.proto](./queue_api_2.md#stream_messages_response)
- `SubscribeRequest` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `SubscriptionConfiguration` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `MessageFilterConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `ContentFilter` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `DeliveryConfiguration` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `DeliveryRetryConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `BatchDeliveryConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `FlowControlSettings` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `ErrorHandlingConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `DeadLetterQueueConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `ErrorActionConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `ErrorNotificationConfig` - [subscribe_request.proto](./queue_api_2.md#subscribe_request)
- `SubscribeResponse` - [subscribe_response.proto](./queue_api_2.md#subscribe_response)
- `UnsubscribeRequest` - [unsubscribe_request.proto](./queue_api_2.md#unsubscribe_request)
- `UnsubscribeResponse` - [unsubscribe_response.proto](./queue_api_2.md#unsubscribe_response)
- `UpdateMessageRequest` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `MessageUpdateProperties` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `VisibilityUpdate` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `PriorityUpdate` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `MetadataUpdate` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `ContentUpdate` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `UpdateCondition` - [update_message_request.proto](./queue_api_2.md#update_message_request)
- `UpdateMessageResponse` - [update_message_response.proto](./queue_api_3.md#update_message_response)
- `FailedFieldUpdate` - [update_message_response.proto](./queue_api_3.md#update_message_response)
- `UpdatedProperties` - [update_message_response.proto](./queue_api_3.md#update_message_response)
- `AlertingConfig` - [alerting_config.proto](./queue_config.md#alerting_config)
- `AuthenticationConfig` - [authentication_config.proto](./queue_config.md#authentication_config)
- `UsernamePasswordAuth` - [authentication_config.proto](./queue_config.md#authentication_config)
- `APIKeyAuth` - [authentication_config.proto](./queue_config.md#authentication_config)
- `TLSAuth` - [authentication_config.proto](./queue_config.md#authentication_config)
- `SASLAuth` - [authentication_config.proto](./queue_config.md#authentication_config)
- `OAuth2Auth` - [authentication_config.proto](./queue_config.md#authentication_config)
- `AuthorizationConfig` - [authorization_config.proto](./queue_config.md#authorization_config)
- `PermissionRule` - [authorization_config.proto](./queue_config.md#authorization_config)
- `RoleBasedAccessControl` - [authorization_config.proto](./queue_config.md#authorization_config)
- `RoleInheritance` - [authorization_config.proto](./queue_config.md#authorization_config)
- `ExternalRoleProvider` - [authorization_config.proto](./queue_config.md#authorization_config)
- `ApiKeyAuth` - [authorization_config.proto](./queue_config.md#authorization_config)
- `KeyValidationService` - [authorization_config.proto](./queue_config.md#authorization_config)
- `JwtAuth` - [authorization_config.proto](./queue_config.md#authorization_config)
- `ExternalAuthService` - [authorization_config.proto](./queue_config.md#authorization_config)
- `AuthCacheConfig` - [authorization_config.proto](./queue_config.md#authorization_config)
- `BackupConfig` - [backup_config.proto](./queue_config.md#backup_config)
- `BatchConfig` - [batch_config.proto](./queue_config.md#batch_config)
- `CircuitBreakerConfig` - [circuit_breaker_config.proto](./queue_config.md#circuit_breaker_config)
- `ClusterConfig` - [cluster_config.proto](./queue_config.md#cluster_config)
- `CompressionConfig` - [compression_config.proto](./queue_config.md#compression_config)
- `ConsistencyConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `ReplicationConsistency` - [consistency_config.proto](./queue_config.md#consistency_config)
- `ReadConsistency` - [consistency_config.proto](./queue_config.md#consistency_config)
- `WriteConsistency` - [consistency_config.proto](./queue_config.md#consistency_config)
- `SyncReplication` - [consistency_config.proto](./queue_config.md#consistency_config)
- `ConflictDetection` - [consistency_config.proto](./queue_config.md#consistency_config)
- `VectorClockConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `TimestampConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `OrderingConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `ConflictResolution` - [consistency_config.proto](./queue_config.md#consistency_config)
- `CustomResolution` - [consistency_config.proto](./queue_config.md#consistency_config)
- `LastWriterWins` - [consistency_config.proto](./queue_config.md#consistency_config)
- `MultiValueConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `ConsistencyValidation` - [consistency_config.proto](./queue_config.md#consistency_config)
- `ReadRetryConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `WriteRetryConfig` - [consistency_config.proto](./queue_config.md#consistency_config)
- `DeadLetterConfig` - [dead_letter_config.proto](./queue_config.md#dead_letter_config)
- `DeserializationConfig` - [deserialization_config.proto](./queue_config.md#deserialization_config)
- `DurabilityConfig` - [durability_config.proto](./queue_config.md#durability_config)
- `EncryptionConfig` - [encryption_config.proto](./queue_config.md#encryption_config)
- `ExchangeConfig` - [exchange_config.proto](./queue_config.md#exchange_config)
- `HeaderRoutingConfig` - [header_routing_config.proto](./queue_config.md#header_routing_config)
- `LoadBalancingConfig` - [load_balancing_config.proto](./queue_config.md#load_balancing_config)
- `MigrationConfig` - [migration_config.proto](./queue_config.md#migration_config)
- `MonitoringConfig` - [monitoring_config.proto](./queue_config.md#monitoring_config)
- `PartitionConfig` - [partition_config.proto](./queue_config.md#partition_config)
- `PerformanceConfig` - [performance_config.proto](./queue_config.md#performance_config)
- `QueueConfig` - [queue_config.proto](./queue_config.md#queue_config)
- `RateLimitConfig` - [rate_limit_config.proto](./queue_config.md#rate_limit_config)
- `ReplicationConfig` - [replication_config.proto](./queue_config.md#replication_config)
- `RestoreConfig` - [restore_config.proto](./queue_config.md#restore_config)
- `RetryConfig` - [retry_config.proto](./queue_config.md#retry_config)
- `RoutingConfig` - [routing_config.proto](./queue_config.md#routing_config)
- `SchemaConfig` - [schema_config.proto](./queue_config.md#schema_config)
- `SerializationConfig` - [serialization_config.proto](./queue_config.md#serialization_config)
- `StreamConfig` - [stream_config.proto](./queue_config.md#stream_config)
- `SubscriptionConfig` - [subscription_config.proto](./queue_config.md#subscription_config)
- `TimeoutConfig` - [timeout_config.proto](./queue_config.md#timeout_config)
- `TopicConfig` - [topic_config.proto](./queue_config.md#topic_config)
- `TopicRoutingConfig` - [topic_routing_config.proto](./queue_config.md#topic_routing_config)
- `TransformationConfig` - [transformation_config.proto](./queue_config.md#transformation_config)
- `UpdateQueueConfigRequest` - [update_queue_config_request.proto](./queue_config.md#update_queue_config_request)
- `UpdateQueueConfigResponse` - [update_queue_config_response.proto](./queue_config.md#update_queue_config_response)
- `UpdateSubscriptionConfigRequest` - [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- `SubscriptionConfigUpdate` - [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- `DeliverySettings` - [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- `RetrySettings` - [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- `FilterSettings` - [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- `RoutingSettings` - [update_subscription_config_request.proto](./queue_config.md#update_subscription_config_request)
- `UpdateSubscriptionConfigResponse` - [update_subscription_config_response.proto](./queue_config.md#update_subscription_config_response)
- `UpdateTopicConfigRequest` - [update_topic_config_request.proto](./queue_config.md#update_topic_config_request)
- `UpdateTopicConfigResponse` - [update_topic_config_response.proto](./queue_config.md#update_topic_config_response)
- `ValidationConfig` - [validation_config.proto](./queue_config.md#validation_config)
- `GetQueueHealthRequest` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `GetQueueHealthResponse` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `QueueHealth` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `ClusterHealth` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `GetQueueStatsRequest` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `QueueStatsResponse` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `QueueStatsPoint` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `StreamMetricsRequest` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `MetricsEvent` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `CookieData` - [cookie_data.proto](./web.md#cookie_data)
- `FileInfo` - [file_info.proto](./web.md#file_info)
- `FileMetadata` - [file_metadata.proto](./web.md#file_metadata)
- `FileUpload` - [file_upload.proto](./web.md#file_upload)
- `HandlerInfo` - [handler_info.proto](./web.md#handler_info)
- `HttpHeader` - [http_header.proto](./web.md#http_header)
- `MiddlewareInfo` - [middleware_info.proto](./web.md#middleware_info)
- `MimeType` - [mime_type.proto](./web.md#mime_type)
- `PerformanceStats` - [performance_stats.proto](./web.md#performance_stats)
- `RouteInfo` - [route_info.proto](./web.md#route_info)
- `SessionData` - [session_data.proto](./web.md#session_data)
- `TemplateData` - [template_data.proto](./web.md#template_data)
- `UrlPath` - [url_path.proto](./web.md#url_path)
- `WebsocketInfo` - [websocket_info.proto](./web.md#websocket_info)
- `WebsocketMessage` - [websocket_message.proto](./web.md#websocket_message)
- `AddMiddlewareRequest` - [add_middleware_request.proto](./web_api_1.md#add_middleware_request)
- `AddMiddlewareResponse` - [add_middleware_response.proto](./web_api_1.md#add_middleware_response)
- `AuthenticateRequest` - [authenticate_request.proto](./web_api_1.md#authenticate_request)
- `AuthenticateResponse` - [authenticate_response.proto](./web_api_1.md#authenticate_response)
- `AuthorizeRequest` - [authorize_request.proto](./web_api_1.md#authorize_request)
- `AuthorizeResponse` - [authorize_response.proto](./web_api_1.md#authorize_response)
- `CloseWebsocketRequest` - [close_websocket_request.proto](./web_api_1.md#close_websocket_request)
- `CloseWebsocketResponse` - [close_websocket_response.proto](./web_api_1.md#close_websocket_response)
- `CreateCookieRequest` - [create_cookie_request.proto](./web_api_1.md#create_cookie_request)
- `CreateCookieResponse` - [create_cookie_response.proto](./web_api_1.md#create_cookie_response)
- `CreateServerRequest` - [create_server_request.proto](./web_api_1.md#create_server_request)
- `CreateServerResponse` - [create_server_response.proto](./web_api_1.md#create_server_response)
- `CreateSessionRequest` - [create_session_request.proto](./web_api_1.md#create_session_request)
- `CreateSessionResponse` - [create_session_response.proto](./web_api_1.md#create_session_response)
- `CreateTemplateRequest` - [create_template_request.proto](./web_api_1.md#create_template_request)
- `CreateTemplateResponse` - [create_template_response.proto](./web_api_1.md#create_template_response)
- `CreateWebsocketRequest` - [create_websocket_request.proto](./web_api_1.md#create_websocket_request)
- `CreateWebsocketResponse` - [create_websocket_response.proto](./web_api_1.md#create_websocket_response)
- `DeleteCookieRequest` - [delete_cookie_request.proto](./web_api_1.md#delete_cookie_request)
- `DeleteCookieResponse` - [delete_cookie_response.proto](./web_api_1.md#delete_cookie_response)
- `DeleteFileRequest` - [delete_file_request.proto](./web_api_1.md#delete_file_request)
- `DeleteFileResponse` - [delete_file_response.proto](./web_api_1.md#delete_file_response)
- `DeleteSessionRequest` - [delete_session_request.proto](./web_api_1.md#delete_session_request)
- `DeleteSessionResponse` - [delete_session_response.proto](./web_api_1.md#delete_session_response)
- `DeleteTemplateRequest` - [delete_template_request.proto](./web_api_1.md#delete_template_request)
- `DeleteTemplateResponse` - [delete_template_response.proto](./web_api_1.md#delete_template_response)
- `DownloadFileRequest` - [download_file_request.proto](./web_api_1.md#download_file_request)
- `DownloadFileResponse` - [download_file_response.proto](./web_api_1.md#download_file_response)
- `FlushCacheRequest` - [flush_cache_request.proto](./web_api_1.md#flush_cache_request)
- `FlushCacheResponse` - [flush_cache_response.proto](./web_api_1.md#flush_cache_response)
- `GenerateCsrfTokenRequest` - [generate_csrf_token_request.proto](./web_api_1.md#generate_csrf_token_request)
- `GenerateCsrfTokenResponse` - [generate_csrf_token_response.proto](./web_api_1.md#generate_csrf_token_response)
- `GetAccessLogsRequest` - [get_access_logs_request.proto](./web_api_1.md#get_access_logs_request)
- `GetAccessLogsResponse` - [get_access_logs_response.proto](./web_api_1.md#get_access_logs_response)
- `GetCookieRequest` - [get_cookie_request.proto](./web_api_1.md#get_cookie_request)
- `GetCookieResponse` - [get_cookie_response.proto](./web_api_1.md#get_cookie_response)
- `GetFileInfoRequest` - [get_file_info_request.proto](./web_api_1.md#get_file_info_request)
- `GetFileInfoResponse` - [get_file_info_response.proto](./web_api_1.md#get_file_info_response)
- `GetHandlerInfoRequest` - [get_handler_info_request.proto](./web_api_1.md#get_handler_info_request)
- `GetHandlerInfoResponse` - [get_handler_info_response.proto](./web_api_1.md#get_handler_info_response)
- `GetMetricsRequest` - [get_metrics_request.proto](./web_api_1.md#get_metrics_request)
- `GetMetricsResponse` - [get_metrics_response.proto](./web_api_1.md#get_metrics_response)
- `GetMiddlewareInfoRequest` - [get_middleware_info_request.proto](./web_api_1.md#get_middleware_info_request)
- `GetMiddlewareInfoResponse` - [get_middleware_info_response.proto](./web_api_1.md#get_middleware_info_response)
- `GetPerformanceStatsRequest` - [get_performance_stats_request.proto](./web_api_1.md#get_performance_stats_request)
- `GetPerformanceStatsResponse` - [get_performance_stats_response.proto](./web_api_1.md#get_performance_stats_response)
- `GetRouteInfoRequest` - [get_route_info_request.proto](./web_api_1.md#get_route_info_request)
- `GetRouteInfoResponse` - [get_route_info_response.proto](./web_api_1.md#get_route_info_response)
- `GetRouteMetricsRequest` - [get_route_metrics_request.proto](./web_api_1.md#get_route_metrics_request)
- `GetRouteMetricsResponse` - [get_route_metrics_response.proto](./web_api_1.md#get_route_metrics_response)
- `GetServerHealthRequest` - [get_server_health_request.proto](./web_api_2.md#get_server_health_request)
- `GetServerHealthResponse` - [get_server_health_response.proto](./web_api_2.md#get_server_health_response)
- `GetServerLogsRequest` - [get_server_logs_request.proto](./web_api_2.md#get_server_logs_request)
- `GetServerLogsResponse` - [get_server_logs_response.proto](./web_api_2.md#get_server_logs_response)
- `GetServerMetricsRequest` - [get_server_metrics_request.proto](./web_api_2.md#get_server_metrics_request)
- `GetServerMetricsResponse` - [get_server_metrics_response.proto](./web_api_2.md#get_server_metrics_response)
- `GetServerStatusRequest` - [get_server_status_request.proto](./web_api_2.md#get_server_status_request)
- `GetServerStatusResponse` - [get_server_status_response.proto](./web_api_2.md#get_server_status_response)
- `GetSessionRequest` - [get_session_request.proto](./web_api_2.md#get_session_request)
- `GetSessionResponse` - [get_session_response.proto](./web_api_2.md#get_session_response)
- `GetSSLCertificateInfoRequest` - [get_ssl_certificate_info_request.proto](./web_api_2.md#get_ssl_certificate_info_request)
- `GetSSLCertificateInfoResponse` - [get_ssl_certificate_info_response.proto](./web_api_2.md#get_ssl_certificate_info_response)
- `GetTemplateInfoRequest` - [get_template_info_request.proto](./web_api_2.md#get_template_info_request)
- `GetTemplateInfoResponse` - [get_template_info_response.proto](./web_api_2.md#get_template_info_response)
- `GetWebsocketInfoRequest` - [get_websocket_info_request.proto](./web_api_2.md#get_websocket_info_request)
- `GetWebsocketInfoResponse` - [get_websocket_info_response.proto](./web_api_2.md#get_websocket_info_response)
- `HandleRequest` - [handle_request.proto](./web_api_2.md#handle_request)
- `HandleRequestRequest` - [handle_request_request.proto](./web_api_2.md#handle_request_request)
- `HandleRequestResponse` - [handle_request_response.proto](./web_api_2.md#handle_request_response)
- `HandleResponse` - [handle_response.proto](./web_api_2.md#handle_response)
- `HealthCheckRequest` - [health_check_request.proto](./web_api_2.md#health_check_request)
- `HealthCheckResponse` - [health_check_response.proto](./web_api_2.md#health_check_response)
- `HTTPRequest` - [http_request.proto](./web_api_2.md#http_request)
- `HttpRequest` - [http_request_per.proto](./web_api_2.md#http_request_per)
- `HTTPResponse` - [http_response.proto](./web_api_2.md#http_response)
- `HttpResponse` - [http_response_per.proto](./web_api_2.md#http_response_per)
- `ListCookiesRequest` - [list_cookies_request.proto](./web_api_2.md#list_cookies_request)
- `ListCookiesResponse` - [list_cookies_response.proto](./web_api_2.md#list_cookies_response)
- `ListFilesRequest` - [list_files_request.proto](./web_api_2.md#list_files_request)
- `ListFilesResponse` - [list_files_response.proto](./web_api_2.md#list_files_response)
- `ListHandlersRequest` - [list_handlers_request.proto](./web_api_2.md#list_handlers_request)
- `ListHandlersResponse` - [list_handlers_response.proto](./web_api_2.md#list_handlers_response)
- `ListMiddlewareRequest` - [list_middleware_request.proto](./web_api_2.md#list_middleware_request)
- `ListMiddlewareResponse` - [list_middleware_response.proto](./web_api_2.md#list_middleware_response)
- `ListRoutesRequest` - [list_routes_request.proto](./web_api_2.md#list_routes_request)
- `ListRoutesResponse` - [list_routes_response.proto](./web_api_2.md#list_routes_response)
- `ListServersRequest` - [list_servers_request.proto](./web_api_2.md#list_servers_request)
- `ListServersResponse` - [list_servers_response.proto](./web_api_2.md#list_servers_response)
- `ListSessionsRequest` - [list_sessions_request.proto](./web_api_2.md#list_sessions_request)
- `ListSessionsResponse` - [list_sessions_response.proto](./web_api_2.md#list_sessions_response)
- `ListTemplatesRequest` - [list_templates_request.proto](./web_api_2.md#list_templates_request)
- `ListTemplatesResponse` - [list_templates_response.proto](./web_api_2.md#list_templates_response)
- `ListWebsocketsRequest` - [list_websockets_request.proto](./web_api_2.md#list_websockets_request)
- `ListWebsocketsResponse` - [list_websockets_response.proto](./web_api_2.md#list_websockets_response)
- `RegisterHandlerRequest` - [register_handler_request.proto](./web_api_2.md#register_handler_request)
- `RegisterHandlerResponse` - [register_handler_response.proto](./web_api_2.md#register_handler_response)
- `RegisterMiddlewareRequest` - [register_middleware_request.proto](./web_api_2.md#register_middleware_request)
- `RegisterMiddlewareResponse` - [register_middleware_response.proto](./web_api_2.md#register_middleware_response)
- `RegisterRouteRequest` - [register_route_request.proto](./web_api_2.md#register_route_request)
- `RegisterRouteResponse` - [register_route_response.proto](./web_api_2.md#register_route_response)
- `RemoveMiddlewareRequest` - [remove_middleware_request.proto](./web_api_3.md#remove_middleware_request)
- `RemoveMiddlewareResponse` - [remove_middleware_response.proto](./web_api_3.md#remove_middleware_response)
- `RenderTemplateRequest` - [render_template_request.proto](./web_api_3.md#render_template_request)
- `RenderTemplateResponse` - [render_template_response.proto](./web_api_3.md#render_template_response)
- `ResetStatsRequest` - [reset_stats_request.proto](./web_api_3.md#reset_stats_request)
- `ResetStatsResponse` - [reset_stats_response.proto](./web_api_3.md#reset_stats_response)
- `RestartServerRequest` - [restart_server_request.proto](./web_api_3.md#restart_server_request)
- `RestartServerResponse` - [restart_server_response.proto](./web_api_3.md#restart_server_response)
- `SendWebsocketMessageRequest` - [send_websocket_message_request.proto](./web_api_3.md#send_websocket_message_request)
- `SendWebsocketMessageResponse` - [send_websocket_message_response.proto](./web_api_3.md#send_websocket_message_response)
- `ServeStaticRequest` - [serve_static_request.proto](./web_api_3.md#serve_static_request)
- `ServeStaticResponse` - [serve_static_response.proto](./web_api_3.md#serve_static_response)
- `StartServerRequest` - [start_server_request.proto](./web_api_3.md#start_server_request)
- `StartServerResponse` - [start_server_response.proto](./web_api_3.md#start_server_response)
- `StopServerRequest` - [stop_server_request.proto](./web_api_3.md#stop_server_request)
- `StopServerResponse` - [stop_server_response.proto](./web_api_3.md#stop_server_response)
- `StreamServerEventsRequest` - [stream_server_events_request.proto](./web_api_3.md#stream_server_events_request)
- `UnregisterHandlerRequest` - [unregister_handler_request.proto](./web_api_3.md#unregister_handler_request)
- `UnregisterHandlerResponse` - [unregister_handler_response.proto](./web_api_3.md#unregister_handler_response)
- `UnregisterMiddlewareRequest` - [unregister_middleware_request.proto](./web_api_3.md#unregister_middleware_request)
- `UnregisterMiddlewareResponse` - [unregister_middleware_response.proto](./web_api_3.md#unregister_middleware_response)
- `UnregisterRouteRequest` - [unregister_route_request.proto](./web_api_3.md#unregister_route_request)
- `UnregisterRouteResponse` - [unregister_route_response.proto](./web_api_3.md#unregister_route_response)
- `UpdateCookieRequest` - [update_cookie_request.proto](./web_api_3.md#update_cookie_request)
- `UpdateCookieResponse` - [update_cookie_response.proto](./web_api_3.md#update_cookie_response)
- `UpdateSessionRequest` - [update_session_request.proto](./web_api_3.md#update_session_request)
- `UpdateSessionResponse` - [update_session_response.proto](./web_api_3.md#update_session_response)
- `UpdateSSLCertificateRequest` - [update_ssl_certificate_request.proto](./web_api_3.md#update_ssl_certificate_request)
- `UpdateSSLCertificateResponse` - [update_ssl_certificate_response.proto](./web_api_3.md#update_ssl_certificate_response)
- `UploadFileRequest` - [upload_file_request.proto](./web_api_3.md#upload_file_request)
- `UploadFileResponse` - [upload_file_response.proto](./web_api_3.md#upload_file_response)
- `ValidateCsrfTokenRequest` - [validate_csrf_token_request.proto](./web_api_3.md#validate_csrf_token_request)
- `ValidateCsrfTokenResponse` - [validate_csrf_token_response.proto](./web_api_3.md#validate_csrf_token_response)
- `AuthConfig` - [auth_config.proto](./web_config_1.md#auth_config)
- `CacheConfig` - [cache_config.proto](./web_config_1.md#cache_config)
- `CompressionConfig` - [compression_config.proto](./web_config_1.md#compression_config)
- `ConfigureGlobalRequest` - [configure_global_request.proto](./web_config_1.md#configure_global_request)
- `ConfigureGlobalResponse` - [configure_global_response.proto](./web_config_1.md#configure_global_response)
- `CookieConfig` - [cookie_config.proto](./web_config_1.md#cookie_config)
- `CORSConfig` - [cors_config.proto](./web_config_1.md#cors_config)
- `CsrfConfig` - [csrf_config.proto](./web_config_1.md#csrf_config)
- `ExportServerConfigRequest` - [export_server_config_request.proto](./web_config_1.md#export_server_config_request)
- `ExportServerConfigResponse` - [export_server_config_response.proto](./web_config_1.md#export_server_config_response)
- `GetCacheConfigRequest` - [get_cache_config_request.proto](./web_config_1.md#get_cache_config_request)
- `GetCacheConfigResponse` - [get_cache_config_response.proto](./web_config_1.md#get_cache_config_response)
- `GetCorsConfigRequest` - [get_cors_config_request.proto](./web_config_1.md#get_cors_config_request)
- `GetCorsConfigResponse` - [get_cors_config_response.proto](./web_config_1.md#get_cors_config_response)
- `GetSecurityConfigRequest` - [get_security_config_request.proto](./web_config_1.md#get_security_config_request)
- `GetSecurityConfigResponse` - [get_security_config_response.proto](./web_config_1.md#get_security_config_response)
- `GetServerConfigRequest` - [get_server_config_request.proto](./web_config_1.md#get_server_config_request)
- `GetServerConfigResponse` - [get_server_config_response.proto](./web_config_1.md#get_server_config_response)
- `HandlerConfig` - [handler_config.proto](./web_config_1.md#handler_config)
- `HealthCheckConfig` - [health_check_config.proto](./web_config_1.md#health_check_config)
- `ImportServerConfigRequest` - [import_server_config_request.proto](./web_config_1.md#import_server_config_request)
- `ImportServerConfigResponse` - [import_server_config_response.proto](./web_config_1.md#import_server_config_response)
- `LoadBalancerConfig` - [load_balancer_config.proto](./web_config_1.md#load_balancer_config)
- `MiddlewareConfig` - [middleware_config.proto](./web_config_1.md#middleware_config)
- `ProxyConfig` - [proxy_config.proto](./web_config_1.md#proxy_config)
- `RateLimitConfig` - [rate_limit_config.proto](./web_config_1.md#rate_limit_config)
- `ReloadServerConfigRequest` - [reload_server_config_request.proto](./web_config_1.md#reload_server_config_request)
- `ReloadServerConfigResponse` - [reload_server_config_response.proto](./web_config_1.md#reload_server_config_response)
- `RouteConfig` - [route_config.proto](./web_config_1.md#route_config)
- `SecurityConfig` - [security_config.proto](./web_config_1.md#security_config)
- `ServerConfig` - [server_config.proto](./web_config_1.md#server_config)
- `SessionConfig` - [session_config.proto](./web_config_1.md#session_config)
- `SslConfig` - [ssl_config.proto](./web_config_1.md#ssl_config)
- `StaticConfig` - [static_config.proto](./web_config_1.md#static_config)
- `TemplateConfig` - [template_config.proto](./web_config_1.md#template_config)
- `TimeoutConfig` - [timeout_config.proto](./web_config_1.md#timeout_config)
- `TLSConfig` - [tls_config.proto](./web_config_1.md#tls_config)
- `UpdateCacheConfigRequest` - [update_cache_config_request.proto](./web_config_1.md#update_cache_config_request)
- `UpdateCacheConfigResponse` - [update_cache_config_response.proto](./web_config_1.md#update_cache_config_response)
- `UpdateCorsConfigRequest` - [update_cors_config_request.proto](./web_config_1.md#update_cors_config_request)
- `UpdateCorsConfigResponse` - [update_cors_config_response.proto](./web_config_1.md#update_cors_config_response)
- `UpdateHandlerConfigRequest` - [update_handler_config_request.proto](./web_config_1.md#update_handler_config_request)
- `UpdateHandlerConfigResponse` - [update_handler_config_response.proto](./web_config_1.md#update_handler_config_response)
- `UpdateMiddlewareConfigRequest` - [update_middleware_config_request.proto](./web_config_1.md#update_middleware_config_request)
- `UpdateMiddlewareConfigResponse` - [update_middleware_config_response.proto](./web_config_1.md#update_middleware_config_response)
- `UpdateRouteConfigRequest` - [update_route_config_request.proto](./web_config_1.md#update_route_config_request)
- `UpdateRouteConfigResponse` - [update_route_config_response.proto](./web_config_1.md#update_route_config_response)
- `UpdateSecurityConfigRequest` - [update_security_config_request.proto](./web_config_1.md#update_security_config_request)
- `UpdateSecurityConfigResponse` - [update_security_config_response.proto](./web_config_1.md#update_security_config_response)
- `UpdateServerConfigRequest` - [update_server_config_request.proto](./web_config_1.md#update_server_config_request)
- `UpdateServerConfigResponse` - [update_server_config_response.proto](./web_config_2.md#update_server_config_response)
- `WebsocketConfig` - [websocket_config.proto](./web_config_2.md#websocket_config)
- `ServerEvent` - [server_event.proto](./web_events.md#server_event)

## All Services

- `AuthAdminService` - [auth_admin_service.proto](./auth_services.md#auth_admin_service)
- `AuthService` - [auth_service.proto](./auth_services.md#auth_service)
- `AuthorizationService` - [authorization_service.proto](./auth_services.md#authorization_service)
- `SessionService` - [session_service.proto](./auth_services.md#session_service)
- `CacheAdminService` - [cache_admin_service.proto](./cache_services.md#cache_admin_service)
- `CacheService` - [cache_service.proto](./cache_services.md#cache_service)
- `ConfigAdminService` - [config_admin_service.proto](./config_services.md#config_admin_service)
- `ConfigService` - [config_service.proto](./config_services.md#config_service)
- `DatabaseAdminService` - [database_admin_service.proto](./database_services.md#database_admin_service)
- `DatabaseService` - [database_service.proto](./database_services.md#database_service)
- `MigrationService` - [migration_service.proto](./database_services.md#migration_service)
- `TransactionService` - [transaction_service.proto](./database_services.md#transaction_service)
- `HealthAdminService` - [health_admin_service.proto](./health.md#health_admin_service)
- `HealthService` - [health_service.proto](./health.md#health_service)
- `MetricsManagementService` - [metrics_admin_service.proto](./metrics_services.md#metrics_admin_service)
- `MetricsService` - [metrics_service.proto](./metrics_services.md#metrics_service)
- `NotificationService` - [notification_service.proto](./notification.md#notification_service)
- `HierarchyService` - [hierarchy_service.proto](./organization_services.md#hierarchy_service)
- `OrganizationService` - [organization_service.proto](./organization_services.md#organization_service)
- `TenantService` - [tenant_service.proto](./organization_services.md#tenant_service)
- `QueueAdminService` - [queue_admin_service.proto](./queue_services.md#queue_admin_service)
- `QueueMonitoringService` - [queue_monitoring_service.proto](./queue_services.md#queue_monitoring_service)
- `QueueManagementService` - [queue_service.proto](./queue_services.md#queue_service)
- `WebAdminService` - [web_admin_service.proto](./web_services.md#web_admin_service)
- `HTTPGatewayService` - [web_service.proto](./web_services.md#web_service)

## Issues Summary

### [auth](./auth.md) - 8 issues

- [auth_token.proto](./auth.md#auth_token) - 2 issues
- [grant_type.proto](./auth.md#grant_type) - 1 issues
- [password_policy.proto](./auth.md#password_policy) - 2 issues
- [permission_type.proto](./auth.md#permission_type) - 1 issues
- [user_profile.proto](./auth.md#user_profile) - 2 issues

### [auth_api_1](./auth_api_1.md) - 2 issues

- [create_role_request.proto](./auth_api_1.md#create_role_request) - 1 issues
- [delete_role_request.proto](./auth_api_1.md#delete_role_request) - 1 issues

### [auth_api_2](./auth_api_2.md) - 4 issues

- [list_roles_request.proto](./auth_api_2.md#list_roles_request) - 1 issues
- [list_roles_response.proto](./auth_api_2.md#list_roles_response) - 1 issues
- [refresh_token_response.proto](./auth_api_2.md#refresh_token_response) - 1 issues
- [update_role_request.proto](./auth_api_2.md#update_role_request) - 1 issues

### [auth_config](./auth_config.md) - 8 issues

- [ldap_config.proto](./auth_config.md#ldap_config) - 2 issues
- [mfa_config.proto](./auth_config.md#mfa_config) - 2 issues
- [saml_config.proto](./auth_config.md#saml_config) - 2 issues
- [session_config.proto](./auth_config.md#session_config) - 2 issues

### [common](./common.md) - 1 issues

- [error_code.proto](./common.md#error_code) - 1 issues

### [config_2](./config_2.md) - 3 issues

- [template_parameter.proto](./config_2.md#template_parameter) - 2 issues
- [version_dependency.proto](./config_2.md#version_dependency) - 1 issues

### [metrics_1](./metrics_1.md) - 8 issues

- [metric_aggregation_result.proto](./metrics_1.md#metric_aggregation_result) - 3 issues
- [metric_family.proto](./metrics_1.md#metric_family) - 5 issues

### [metrics_config](./metrics_config.md) - 3 issues

- [export_config_options.proto](./metrics_config.md#export_config_options) - 3 issues

### [notification](./notification.md) - 1 issues

- [template.proto](./notification.md#template) - 1 issues

### [queue_1](./queue_1.md) - 2 issues

- [acknowledgment_mode.proto](./queue_1.md#acknowledgment_mode) - 1 issues
- [message_id.proto](./queue_1.md#message_id) - 1 issues

### [queue_2](./queue_2.md) - 3 issues

- [queue_info.proto](./queue_2.md#queue_info) - 1 issues
- [subscription_info.proto](./queue_2.md#subscription_info) - 1 issues
- [timestamp_range.proto](./queue_2.md#timestamp_range) - 1 issues

### [queue_api_1](./queue_api_1.md) - 2 issues

- [ack_request.proto](./queue_api_1.md#ack_request) - 1 issues
- [ack_response.proto](./queue_api_1.md#ack_response) - 1 issues

### [queue_api_2](./queue_api_2.md) - 6 issues

- [list_queues_request.proto](./queue_api_2.md#list_queues_request) - 1 issues
- [list_queues_response.proto](./queue_api_2.md#list_queues_response) - 1 issues
- [list_subscriptions_request.proto](./queue_api_2.md#list_subscriptions_request) - 1 issues
- [list_subscriptions_response.proto](./queue_api_2.md#list_subscriptions_response) - 1 issues
- [pull_request.proto](./queue_api_2.md#pull_request) - 1 issues
- [pull_response.proto](./queue_api_2.md#pull_response) - 1 issues

### [web_api_1](./web_api_1.md) - 43 issues

- [add_middleware_request.proto](./web_api_1.md#add_middleware_request) - 1 issues
- [add_middleware_response.proto](./web_api_1.md#add_middleware_response) - 1 issues
- [authenticate_request.proto](./web_api_1.md#authenticate_request) - 1 issues
- [authenticate_response.proto](./web_api_1.md#authenticate_response) - 1 issues
- [authorize_request.proto](./web_api_1.md#authorize_request) - 1 issues
- [authorize_response.proto](./web_api_1.md#authorize_response) - 1 issues
- [close_websocket_request.proto](./web_api_1.md#close_websocket_request) - 1 issues
- [close_websocket_response.proto](./web_api_1.md#close_websocket_response) - 1 issues
- [create_cookie_response.proto](./web_api_1.md#create_cookie_response) - 1 issues
- [create_server_request.proto](./web_api_1.md#create_server_request) - 1 issues
- [create_server_response.proto](./web_api_1.md#create_server_response) - 1 issues
- [create_template_request.proto](./web_api_1.md#create_template_request) - 1 issues
- [create_template_response.proto](./web_api_1.md#create_template_response) - 1 issues
- [create_websocket_request.proto](./web_api_1.md#create_websocket_request) - 1 issues
- [create_websocket_response.proto](./web_api_1.md#create_websocket_response) - 1 issues
- [delete_cookie_request.proto](./web_api_1.md#delete_cookie_request) - 1 issues
- [delete_cookie_response.proto](./web_api_1.md#delete_cookie_response) - 1 issues
- [delete_file_request.proto](./web_api_1.md#delete_file_request) - 1 issues
- [delete_file_response.proto](./web_api_1.md#delete_file_response) - 1 issues
- [delete_template_request.proto](./web_api_1.md#delete_template_request) - 1 issues
- [delete_template_response.proto](./web_api_1.md#delete_template_response) - 1 issues
- [download_file_request.proto](./web_api_1.md#download_file_request) - 1 issues
- [download_file_response.proto](./web_api_1.md#download_file_response) - 1 issues
- [generate_csrf_token_request.proto](./web_api_1.md#generate_csrf_token_request) - 1 issues
- [generate_csrf_token_response.proto](./web_api_1.md#generate_csrf_token_response) - 1 issues
- [get_access_logs_request.proto](./web_api_1.md#get_access_logs_request) - 1 issues
- [get_access_logs_response.proto](./web_api_1.md#get_access_logs_response) - 1 issues
- [get_cookie_request.proto](./web_api_1.md#get_cookie_request) - 1 issues
- [get_cookie_response.proto](./web_api_1.md#get_cookie_response) - 1 issues
- [get_file_info_request.proto](./web_api_1.md#get_file_info_request) - 1 issues
- [get_file_info_response.proto](./web_api_1.md#get_file_info_response) - 1 issues
- [get_handler_info_request.proto](./web_api_1.md#get_handler_info_request) - 1 issues
- [get_handler_info_response.proto](./web_api_1.md#get_handler_info_response) - 1 issues
- [get_metrics_request.proto](./web_api_1.md#get_metrics_request) - 1 issues
- [get_metrics_response.proto](./web_api_1.md#get_metrics_response) - 1 issues
- [get_middleware_info_request.proto](./web_api_1.md#get_middleware_info_request) - 1 issues
- [get_middleware_info_response.proto](./web_api_1.md#get_middleware_info_response) - 1 issues
- [get_performance_stats_request.proto](./web_api_1.md#get_performance_stats_request) - 1 issues
- [get_performance_stats_response.proto](./web_api_1.md#get_performance_stats_response) - 1 issues
- [get_route_info_request.proto](./web_api_1.md#get_route_info_request) - 1 issues
- [get_route_info_response.proto](./web_api_1.md#get_route_info_response) - 1 issues
- [get_route_metrics_request.proto](./web_api_1.md#get_route_metrics_request) - 1 issues
- [get_route_metrics_response.proto](./web_api_1.md#get_route_metrics_response) - 1 issues

### [web_api_2](./web_api_2.md) - 33 issues

- [get_server_health_request.proto](./web_api_2.md#get_server_health_request) - 1 issues
- [get_server_health_response.proto](./web_api_2.md#get_server_health_response) - 1 issues
- [get_server_logs_request.proto](./web_api_2.md#get_server_logs_request) - 1 issues
- [get_server_logs_response.proto](./web_api_2.md#get_server_logs_response) - 1 issues
- [get_server_metrics_request.proto](./web_api_2.md#get_server_metrics_request) - 1 issues
- [get_server_metrics_response.proto](./web_api_2.md#get_server_metrics_response) - 1 issues
- [get_server_status_request.proto](./web_api_2.md#get_server_status_request) - 1 issues
- [get_server_status_response.proto](./web_api_2.md#get_server_status_response) - 1 issues
- [get_ssl_certificate_info_request.proto](./web_api_2.md#get_ssl_certificate_info_request) - 1 issues
- [get_ssl_certificate_info_response.proto](./web_api_2.md#get_ssl_certificate_info_response) - 1 issues
- [get_template_info_request.proto](./web_api_2.md#get_template_info_request) - 1 issues
- [get_template_info_response.proto](./web_api_2.md#get_template_info_response) - 1 issues
- [get_websocket_info_request.proto](./web_api_2.md#get_websocket_info_request) - 1 issues
- [get_websocket_info_response.proto](./web_api_2.md#get_websocket_info_response) - 1 issues
- [handle_request.proto](./web_api_2.md#handle_request) - 1 issues
- [handle_request_request.proto](./web_api_2.md#handle_request_request) - 1 issues
- [handle_request_response.proto](./web_api_2.md#handle_request_response) - 1 issues
- [handle_response.proto](./web_api_2.md#handle_response) - 1 issues
- [list_cookies_request.proto](./web_api_2.md#list_cookies_request) - 1 issues
- [list_cookies_response.proto](./web_api_2.md#list_cookies_response) - 1 issues
- [list_handlers_response.proto](./web_api_2.md#list_handlers_response) - 1 issues
- [list_routes_request.proto](./web_api_2.md#list_routes_request) - 1 issues
- [list_routes_response.proto](./web_api_2.md#list_routes_response) - 1 issues
- [list_servers_request.proto](./web_api_2.md#list_servers_request) - 1 issues
- [list_servers_response.proto](./web_api_2.md#list_servers_response) - 1 issues
- [list_templates_request.proto](./web_api_2.md#list_templates_request) - 1 issues
- [list_templates_response.proto](./web_api_2.md#list_templates_response) - 1 issues
- [list_websockets_request.proto](./web_api_2.md#list_websockets_request) - 1 issues
- [list_websockets_response.proto](./web_api_2.md#list_websockets_response) - 1 issues
- [register_handler_request.proto](./web_api_2.md#register_handler_request) - 1 issues
- [register_handler_response.proto](./web_api_2.md#register_handler_response) - 1 issues
- [register_route_request.proto](./web_api_2.md#register_route_request) - 1 issues
- [register_route_response.proto](./web_api_2.md#register_route_response) - 1 issues

### [web_api_3](./web_api_3.md) - 27 issues

- [remove_middleware_request.proto](./web_api_3.md#remove_middleware_request) - 1 issues
- [remove_middleware_response.proto](./web_api_3.md#remove_middleware_response) - 1 issues
- [render_template_request.proto](./web_api_3.md#render_template_request) - 1 issues
- [render_template_response.proto](./web_api_3.md#render_template_response) - 1 issues
- [reset_stats_request.proto](./web_api_3.md#reset_stats_request) - 1 issues
- [reset_stats_response.proto](./web_api_3.md#reset_stats_response) - 1 issues
- [restart_server_request.proto](./web_api_3.md#restart_server_request) - 1 issues
- [restart_server_response.proto](./web_api_3.md#restart_server_response) - 1 issues
- [send_websocket_message_request.proto](./web_api_3.md#send_websocket_message_request) - 1 issues
- [send_websocket_message_response.proto](./web_api_3.md#send_websocket_message_response) - 1 issues
- [serve_static_request.proto](./web_api_3.md#serve_static_request) - 1 issues
- [serve_static_response.proto](./web_api_3.md#serve_static_response) - 1 issues
- [stop_server_request.proto](./web_api_3.md#stop_server_request) - 1 issues
- [stop_server_response.proto](./web_api_3.md#stop_server_response) - 1 issues
- [stream_server_events_request.proto](./web_api_3.md#stream_server_events_request) - 1 issues
- [unregister_handler_request.proto](./web_api_3.md#unregister_handler_request) - 1 issues
- [unregister_handler_response.proto](./web_api_3.md#unregister_handler_response) - 1 issues
- [unregister_route_request.proto](./web_api_3.md#unregister_route_request) - 1 issues
- [unregister_route_response.proto](./web_api_3.md#unregister_route_response) - 1 issues
- [update_cookie_request.proto](./web_api_3.md#update_cookie_request) - 1 issues
- [update_cookie_response.proto](./web_api_3.md#update_cookie_response) - 1 issues
- [update_ssl_certificate_request.proto](./web_api_3.md#update_ssl_certificate_request) - 1 issues
- [update_ssl_certificate_response.proto](./web_api_3.md#update_ssl_certificate_response) - 1 issues
- [upload_file_request.proto](./web_api_3.md#upload_file_request) - 1 issues
- [upload_file_response.proto](./web_api_3.md#upload_file_response) - 1 issues
- [validate_csrf_token_request.proto](./web_api_3.md#validate_csrf_token_request) - 1 issues
- [validate_csrf_token_response.proto](./web_api_3.md#validate_csrf_token_response) - 1 issues

### [web_config_1](./web_config_1.md) - 23 issues

- [configure_global_request.proto](./web_config_1.md#configure_global_request) - 1 issues
- [configure_global_response.proto](./web_config_1.md#configure_global_response) - 1 issues
- [export_server_config_request.proto](./web_config_1.md#export_server_config_request) - 1 issues
- [export_server_config_response.proto](./web_config_1.md#export_server_config_response) - 1 issues
- [get_cors_config_request.proto](./web_config_1.md#get_cors_config_request) - 1 issues
- [get_cors_config_response.proto](./web_config_1.md#get_cors_config_response) - 1 issues
- [get_security_config_request.proto](./web_config_1.md#get_security_config_request) - 1 issues
- [get_security_config_response.proto](./web_config_1.md#get_security_config_response) - 1 issues
- [get_server_config_request.proto](./web_config_1.md#get_server_config_request) - 1 issues
- [get_server_config_response.proto](./web_config_1.md#get_server_config_response) - 1 issues
- [import_server_config_request.proto](./web_config_1.md#import_server_config_request) - 1 issues
- [import_server_config_response.proto](./web_config_1.md#import_server_config_response) - 1 issues
- [reload_server_config_request.proto](./web_config_1.md#reload_server_config_request) - 1 issues
- [reload_server_config_response.proto](./web_config_1.md#reload_server_config_response) - 1 issues
- [update_cors_config_request.proto](./web_config_1.md#update_cors_config_request) - 1 issues
- [update_cors_config_response.proto](./web_config_1.md#update_cors_config_response) - 1 issues
- [update_handler_config_request.proto](./web_config_1.md#update_handler_config_request) - 1 issues
- [update_handler_config_response.proto](./web_config_1.md#update_handler_config_response) - 1 issues
- [update_route_config_request.proto](./web_config_1.md#update_route_config_request) - 1 issues
- [update_route_config_response.proto](./web_config_1.md#update_route_config_response) - 1 issues
- [update_security_config_request.proto](./web_config_1.md#update_security_config_request) - 1 issues
- [update_security_config_response.proto](./web_config_1.md#update_security_config_response) - 1 issues
- [update_server_config_request.proto](./web_config_1.md#update_server_config_request) - 1 issues

### [web_config_2](./web_config_2.md) - 1 issues

- [update_server_config_response.proto](./web_config_2.md#update_server_config_response) - 1 issues

### [web_events](./web_events.md) - 1 issues

- [server_event.proto](./web_events.md#server_event) - 1 issues
