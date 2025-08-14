#!/bin/bash
# Auto-generated script to fix missing proto imports

# Fix imports for organization/proto/integration_settings.proto
sed -i '/^import.*proto";$/a import "organization/proto/webhook_config.proto";' 'pkg/organization/proto/integration_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/api_key_config.proto";' 'pkg/organization/proto/integration_settings.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/api_key_config.proto";' 'pkg/organization/proto/integration_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/integration.proto";' 'pkg/organization/proto/integration_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/o_auth_app_config.proto";' 'pkg/organization/proto/integration_settings.proto'

# Fix imports for metrics/proto/security_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/api_key_config.proto";' 'pkg/metrics/proto/security_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/api_key_config.proto";' 'pkg/metrics/proto/security_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/tls_config.proto";' 'pkg/metrics/proto/security_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/tls_config.proto";' 'pkg/metrics/proto/security_config.proto'

# Fix imports for organization/proto/security_settings.proto
sed -i '/^import.*proto";$/a import "organization/proto/rate_limit_config.proto";' 'pkg/organization/proto/security_settings.proto'
sed -i '/^import.*proto";$/a import "auth/proto/rate_limit_config.proto";' 'pkg/organization/proto/security_settings.proto'
sed -i '/^import.*proto";$/a import "web/proto/rate_limit_config.proto";' 'pkg/organization/proto/security_settings.proto'
sed -i '/^import.*proto";$/a import "queue/proto/rate_limit_config.proto";' 'pkg/organization/proto/security_settings.proto'

# Fix imports for organization/proto/hierarchy_service.proto
sed -i '/^import.*proto";$/a import "organization/proto/create_team_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_teams_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_department_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_department_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_hierarchy_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_departments_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_hierarchy_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_department_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_departments_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_team_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_department_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_team_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_department_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_teams_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_team_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_hierarchy_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_department_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_team_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_department_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_team_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_hierarchy_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_team_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_department_request.proto";' 'pkg/organization/proto/hierarchy_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_team_response.proto";' 'pkg/organization/proto/hierarchy_service.proto'

# Fix imports for organization/proto/tenant_service.proto
sed -i '/^import.*proto";$/a import "organization/proto/update_tenant_quota_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_tenant_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_tenant_usage_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/configure_tenant_isolation_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_tenant_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_tenant_isolation_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_tenant_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_tenant_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_tenant_usage_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/configure_tenant_isolation_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_tenant_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_tenant_isolation_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_tenants_request.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_tenant_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_tenants_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_tenant_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_tenant_quota_response.proto";' 'pkg/organization/proto/tenant_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_tenant_request.proto";' 'pkg/organization/proto/tenant_service.proto'

# Fix imports for organization/proto/audit_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/audit_alert.proto";' 'pkg/organization/proto/audit_config.proto'

# Fix imports for organization/proto/cache_behavior.proto
sed -i '/^import.*proto";$/a import "organization/proto/cache_key_policy.proto";' 'pkg/organization/proto/cache_behavior.proto'

# Fix imports for organization/proto/database_isolation.proto
sed -i '/^import.*proto";$/a import "organization/proto/backup_config.proto";' 'pkg/organization/proto/database_isolation.proto'
sed -i '/^import.*proto";$/a import "queue/proto/backup_config.proto";' 'pkg/organization/proto/database_isolation.proto'

# Fix imports for organization/proto/load_balancer_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/ssl_config.proto";' 'pkg/organization/proto/load_balancer_config.proto'
sed -i '/^import.*proto";$/a import "organization/proto/health_check_config.proto";' 'pkg/organization/proto/load_balancer_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_config.proto";' 'pkg/organization/proto/load_balancer_config.proto'

# Fix imports for organization/proto/network_isolation.proto
sed -i '/^import.*proto";$/a import "organization/proto/cdn_config.proto";' 'pkg/organization/proto/network_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/network_acl_rule.proto";' 'pkg/organization/proto/network_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/load_balancer_config.proto";' 'pkg/organization/proto/network_isolation.proto'
sed -i '/^import.*proto";$/a import "web/proto/load_balancer_config.proto";' 'pkg/organization/proto/network_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/domain_config.proto";' 'pkg/organization/proto/network_isolation.proto'

# Fix imports for organization/proto/cdn_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/cache_behavior.proto";' 'pkg/organization/proto/cdn_config.proto'
sed -i '/^import.*proto";$/a import "organization/proto/origin_config.proto";' 'pkg/organization/proto/cdn_config.proto'

# Fix imports for organization/proto/organization_member.proto
sed -i '/^import.*proto";$/a import "organization/proto/member_role.proto";' 'pkg/organization/proto/organization_member.proto'

# Fix imports for organization/proto/organization_hierarchy.proto
sed -i '/^import.*proto";$/a import "organization/proto/hierarchy_node.proto";' 'pkg/organization/proto/organization_hierarchy.proto'
sed -i '/^import.*proto";$/a import "organization/proto/hierarchy_type.proto";' 'pkg/organization/proto/organization_hierarchy.proto'

# Fix imports for organization/proto/create_organization_request.proto
sed -i '/^import.*proto";$/a import "organization/proto/organization.proto";' 'pkg/organization/proto/create_organization_request.proto'

# Fix imports for organization/proto/update_organization_request.proto
sed -i '/^import.*proto";$/a import "organization/proto/organization.proto";' 'pkg/organization/proto/update_organization_request.proto'

# Fix imports for organization/proto/update_organization_response.proto
sed -i '/^import.*proto";$/a import "organization/proto/organization.proto";' 'pkg/organization/proto/update_organization_response.proto'

# Fix imports for organization/proto/get_organization_response.proto
sed -i '/^import.*proto";$/a import "organization/proto/organization.proto";' 'pkg/organization/proto/get_organization_response.proto'
sed -i '/^import.*proto";$/a import "organization/proto/tenant.proto";' 'pkg/organization/proto/get_organization_response.proto'
sed -i '/^import.*proto";$/a import "organization/proto/organization_settings.proto";' 'pkg/organization/proto/get_organization_response.proto'

# Fix imports for organization/proto/create_organization_response.proto
sed -i '/^import.*proto";$/a import "organization/proto/organization.proto";' 'pkg/organization/proto/create_organization_response.proto'
sed -i '/^import.*proto";$/a import "organization/proto/tenant.proto";' 'pkg/organization/proto/create_organization_response.proto'

# Fix imports for organization/proto/access_control.proto
sed -i '/^import.*proto";$/a import "organization/proto/time_restriction.proto";' 'pkg/organization/proto/access_control.proto'

# Fix imports for organization/proto/tenant.proto
sed -i '/^import.*proto";$/a import "organization/proto/tenant_quota.proto";' 'pkg/organization/proto/tenant.proto'
sed -i '/^import.*proto";$/a import "organization/proto/isolation_level.proto";' 'pkg/organization/proto/tenant.proto'
sed -i '/^import.*proto";$/a import "db/proto/isolation_level.proto";' 'pkg/organization/proto/tenant.proto'
sed -i '/^import.*proto";$/a import "organization/proto/tenant_status.proto";' 'pkg/organization/proto/tenant.proto'

# Fix imports for organization/proto/tenant_isolation.proto
sed -i '/^import.*proto";$/a import "organization/proto/isolation_level.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "db/proto/isolation_level.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/storage_isolation.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/compute_isolation.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/network_isolation.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/encryption_config.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "queue/proto/encryption_config.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/access_control.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "config/proto/access_control.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/audit_config.proto";' 'pkg/organization/proto/tenant_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/database_isolation.proto";' 'pkg/organization/proto/tenant_isolation.proto'

# Fix imports for db/proto/execute_options.proto
sed -i '/^import.*proto";$/a import "organization/proto/isolation_level.proto";' 'pkg/db/proto/execute_options.proto'
sed -i '/^import.*proto";$/a import "db/proto/isolation_level.proto";' 'pkg/db/proto/execute_options.proto'

# Fix imports for db/proto/transaction_options.proto
sed -i '/^import.*proto";$/a import "organization/proto/isolation_level.proto";' 'pkg/db/proto/transaction_options.proto'
sed -i '/^import.*proto";$/a import "db/proto/isolation_level.proto";' 'pkg/db/proto/transaction_options.proto'

# Fix imports for organization/proto/notification_settings.proto
sed -i '/^import.*proto";$/a import "organization/proto/email_template.proto";' 'pkg/organization/proto/notification_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/notification_frequency.proto";' 'pkg/organization/proto/notification_settings.proto'

# Fix imports for organization/proto/compute_isolation.proto
sed -i '/^import.*proto";$/a import "organization/proto/cpu_allocation.proto";' 'pkg/organization/proto/compute_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/auto_scaling_config.proto";' 'pkg/organization/proto/compute_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/memory_allocation.proto";' 'pkg/organization/proto/compute_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/resource_limits.proto";' 'pkg/organization/proto/compute_isolation.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_limits.proto";' 'pkg/organization/proto/compute_isolation.proto'
sed -i '/^import.*proto";$/a import "config/proto/resource_limits.proto";' 'pkg/organization/proto/compute_isolation.proto'

# Fix imports for metrics/proto/provider_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/resource_limits.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_limits.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "config/proto/resource_limits.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_settings.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/security_config.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/security_config.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_type.proto";' 'pkg/metrics/proto/provider_config.proto'
sed -i '/^import.*proto";$/a import "auth/proto/provider_type.proto";' 'pkg/metrics/proto/provider_config.proto'

# Fix imports for config/proto/config_environment.proto
sed -i '/^import.*proto";$/a import "organization/proto/resource_limits.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_limits.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/resource_limits.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "organization/proto/compliance_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/compliance_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "organization/proto/notification_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/notification_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "organization/proto/access_control.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/access_control.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_status.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_status.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_status.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "common/proto/health_status.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_status.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/retention_policy.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/retention_policy.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retention_policy.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/sync_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/backup_policy.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/promotion_rule.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/environment_status.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/encryption_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/environment_type.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/deployment_info.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/monitoring_config.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "queue/proto/monitoring_config.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/audit_settings.proto";' 'pkg/config/proto/config_environment.proto'
sed -i '/^import.*proto";$/a import "config/proto/approval_workflow.proto";' 'pkg/config/proto/config_environment.proto'

# Fix imports for organization/proto/storage_isolation.proto
sed -i '/^import.*proto";$/a import "organization/proto/storage_backup_config.proto";' 'pkg/organization/proto/storage_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/storage_policy.proto";' 'pkg/organization/proto/storage_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/storage_encryption.proto";' 'pkg/organization/proto/storage_isolation.proto'
sed -i '/^import.*proto";$/a import "organization/proto/storage_quota.proto";' 'pkg/organization/proto/storage_isolation.proto'

# Fix imports for organization/proto/dns_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/dns_record.proto";' 'pkg/organization/proto/dns_config.proto'

# Fix imports for organization/proto/organization_settings.proto
sed -i '/^import.*proto";$/a import "organization/proto/billing_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/compliance_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/compliance_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/feature_flag.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/ui_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/notification_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/notification_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/integration_settings.proto";' 'pkg/organization/proto/organization_settings.proto'
sed -i '/^import.*proto";$/a import "organization/proto/security_settings.proto";' 'pkg/organization/proto/organization_settings.proto'

# Fix imports for organization/proto/domain_config.proto
sed -i '/^import.*proto";$/a import "organization/proto/dns_config.proto";' 'pkg/organization/proto/domain_config.proto'

# Fix imports for organization/proto/organization.proto
sed -i '/^import.*proto";$/a import "organization/proto/organization_status.proto";' 'pkg/organization/proto/organization.proto'

# Fix imports for organization/proto/organization_service.proto
sed -i '/^import.*proto";$/a import "organization/proto/get_organization_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_organization_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_organization_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_members_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_organizations_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_organization_settings_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/remove_member_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_organization_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_organization_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/create_organization_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/add_member_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_member_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_organization_settings_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/delete_organization_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_member_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_members_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_organization_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/add_member_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/remove_member_request.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/list_organizations_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/update_organization_settings_response.proto";' 'pkg/organization/proto/organization_service.proto'
sed -i '/^import.*proto";$/a import "organization/proto/get_organization_settings_request.proto";' 'pkg/organization/proto/organization_service.proto'

# Fix imports for metrics/proto/get_stats_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_stats.proto";' 'pkg/metrics/proto/get_stats_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_stats.proto";' 'pkg/metrics/proto/get_stats_response.proto'

# Fix imports for metrics/proto/get_metrics_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_stats.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_stats.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/pagination_info.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "common/proto/pagination_info.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/get_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/get_metrics_response.proto'

# Fix imports for db/proto/query_row_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_stats.proto";' 'pkg/db/proto/query_row_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_stats.proto";' 'pkg/db/proto/query_row_response.proto'

# Fix imports for db/proto/query_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_stats.proto";' 'pkg/db/proto/query_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_stats.proto";' 'pkg/db/proto/query_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/result_set.proto";' 'pkg/db/proto/query_response.proto'

# Fix imports for metrics/proto/scrape_job.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_config.proto";' 'pkg/metrics/proto/scrape_job.proto'

# Fix imports for metrics/proto/set_scrape_config_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_config.proto";' 'pkg/metrics/proto/set_scrape_config_request.proto'

# Fix imports for metrics/proto/start_scraping_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_config.proto";' 'pkg/metrics/proto/start_scraping_request.proto'

# Fix imports for metrics/proto/get_scrape_config_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_config.proto";' 'pkg/metrics/proto/get_scrape_config_response.proto'

# Fix imports for metrics/proto/summary_value.proto
sed -i '/^import.*proto";$/a import "metrics/proto/quantile.proto";' 'pkg/metrics/proto/summary_value.proto'

# Fix imports for metrics/proto/record_gauge_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/gauge_metric.proto";' 'pkg/metrics/proto/record_gauge_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/recording_stats.proto";' 'pkg/metrics/proto/record_gauge_response.proto'

# Fix imports for metrics/proto/record_summary_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/recording_stats.proto";' 'pkg/metrics/proto/record_summary_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/summary_metric.proto";' 'pkg/metrics/proto/record_summary_response.proto'

# Fix imports for metrics/proto/record_histogram_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/recording_stats.proto";' 'pkg/metrics/proto/record_histogram_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/histogram_stats.proto";' 'pkg/metrics/proto/record_histogram_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/histogram_metric.proto";' 'pkg/metrics/proto/record_histogram_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/bucket_info.proto";' 'pkg/metrics/proto/record_histogram_response.proto'

# Fix imports for metrics/proto/record_metric_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/recording_stats.proto";' 'pkg/metrics/proto/record_metric_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/validation_result.proto";' 'pkg/metrics/proto/record_metric_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/validation_result.proto";' 'pkg/metrics/proto/record_metric_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/validation_result.proto";' 'pkg/metrics/proto/record_metric_response.proto'

# Fix imports for metrics/proto/register_metric_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/registration_validation.proto";' 'pkg/metrics/proto/register_metric_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/registration_result.proto";' 'pkg/metrics/proto/register_metric_response.proto'

# Fix imports for metrics/proto/metrics_management_service.proto
sed -i '/^import.*proto";$/a import "metrics/proto/list_providers_response.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_provider_stats_request.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/list_providers_request.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/update_provider_response.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/update_provider_request.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/create_provider_response.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/delete_provider_response.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/delete_provider_request.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_provider_stats_response.proto";' 'pkg/metrics/proto/metrics_management_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/create_provider_request.proto";' 'pkg/metrics/proto/metrics_management_service.proto'

# Fix imports for metrics/proto/metric_definition.proto
sed -i '/^import.*proto";$/a import "metrics/proto/validation_rules.proto";' 'pkg/metrics/proto/metric_definition.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/retention_policy_config.proto";' 'pkg/metrics/proto/metric_definition.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type.proto";' 'pkg/metrics/proto/metric_definition.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metric_type.proto";' 'pkg/metrics/proto/metric_definition.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/label_definition.proto";' 'pkg/metrics/proto/metric_definition.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type_config.proto";' 'pkg/metrics/proto/metric_definition.proto'

# Fix imports for metrics/proto/retention_info.proto
sed -i '/^import.*proto";$/a import "metrics/proto/retention_policy_config.proto";' 'pkg/metrics/proto/retention_info.proto'

# Fix imports for metrics/proto/retention_policy_info.proto
sed -i '/^import.*proto";$/a import "metrics/proto/retention_policy_config.proto";' 'pkg/metrics/proto/retention_policy_info.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/retention_policy.proto";' 'pkg/metrics/proto/retention_policy_info.proto'
sed -i '/^import.*proto";$/a import "config/proto/retention_policy.proto";' 'pkg/metrics/proto/retention_policy_info.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retention_policy.proto";' 'pkg/metrics/proto/retention_policy_info.proto'

# Fix imports for metrics/proto/metric_data.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type.proto";' 'pkg/metrics/proto/metric_data.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metric_type.proto";' 'pkg/metrics/proto/metric_data.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_value.proto";' 'pkg/metrics/proto/metric_data.proto'

# Fix imports for metrics/proto/metric_series.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type.proto";' 'pkg/metrics/proto/metric_series.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metric_type.proto";' 'pkg/metrics/proto/metric_series.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_value.proto";' 'pkg/metrics/proto/metric_series.proto'

# Fix imports for metrics/proto/messages/metric_family.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type.proto";' 'pkg/metrics/proto/messages/metric_family.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metric_type.proto";' 'pkg/metrics/proto/messages/metric_family.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/messages/metric_family.proto'

# Fix imports for queue/proto/stream_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type.proto";' 'pkg/queue/proto/stream_metrics_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metric_type.proto";' 'pkg/queue/proto/stream_metrics_request.proto'

# Fix imports for queue/proto/metrics_event.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type.proto";' 'pkg/queue/proto/metrics_event.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metric_type.proto";' 'pkg/queue/proto/metrics_event.proto'

# Fix imports for metrics/proto/record_summary_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/summary_metric.proto";' 'pkg/metrics/proto/record_summary_request.proto'

# Fix imports for metrics/proto/list_providers_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/pagination_info.proto";' 'pkg/metrics/proto/list_providers_response.proto'
sed -i '/^import.*proto";$/a import "common/proto/pagination_info.proto";' 'pkg/metrics/proto/list_providers_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_info.proto";' 'pkg/metrics/proto/list_providers_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_summary.proto";' 'pkg/metrics/proto/list_providers_response.proto'

# Fix imports for metrics/proto/get_metric_metadata_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/pagination_info.proto";' 'pkg/metrics/proto/get_metric_metadata_response.proto'
sed -i '/^import.*proto";$/a import "common/proto/pagination_info.proto";' 'pkg/metrics/proto/get_metric_metadata_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/get_metric_metadata_response.proto'

# Fix imports for common/proto/response_metadata.proto
sed -i '/^import.*proto";$/a import "metrics/proto/pagination_info.proto";' 'pkg/common/proto/response_metadata.proto'
sed -i '/^import.*proto";$/a import "common/proto/pagination_info.proto";' 'pkg/common/proto/response_metadata.proto'
sed -i '/^import.*proto";$/a import "common/proto/rate_limit_info.proto";' 'pkg/common/proto/response_metadata.proto'
sed -i '/^import.*proto";$/a import "common/proto/error.proto";' 'pkg/common/proto/response_metadata.proto'

# Fix imports for metrics/proto/provider_statistics.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_info.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/top_metrics.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/error_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "queue/proto/error_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/performance_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "web/proto/performance_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_usage_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/configuration_summary.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_status_entry.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/trend_analysis.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/data_volume_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/export_stats.proto";' 'pkg/metrics/proto/provider_statistics.proto'

# Fix imports for metrics/proto/get_metrics_summary_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_summary.proto";' 'pkg/metrics/proto/get_metrics_summary_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_summary_response.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_summary_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_summary_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metrics_summary.proto";' 'pkg/metrics/proto/get_metrics_summary_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metrics_health_info.proto";' 'pkg/metrics/proto/get_metrics_summary_response.proto'

# Fix imports for metrics/proto/get_metric_config_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_config.proto";' 'pkg/metrics/proto/get_metric_config_response.proto'

# Fix imports for metrics/proto/set_metric_config_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_config.proto";' 'pkg/metrics/proto/set_metric_config_request.proto'

# Fix imports for metrics/proto/get_provider_stats_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/stats_options.proto";' 'pkg/metrics/proto/get_provider_stats_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/get_provider_stats_request.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/get_provider_stats_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/get_provider_stats_request.proto'

# Fix imports for metrics/proto/get_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_request.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_filter.proto";' 'pkg/metrics/proto/get_metrics_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/output_options.proto";' 'pkg/metrics/proto/get_metrics_request.proto'

# Fix imports for metrics/proto/get_metrics_summary_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_summary_request.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_summary_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/get_metrics_summary_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_filter.proto";' 'pkg/metrics/proto/get_metrics_summary_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/summary_options.proto";' 'pkg/metrics/proto/get_metrics_summary_request.proto'

# Fix imports for metrics/proto/metric_query.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/metric_query.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/metric_query.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/metric_query.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_filter.proto";' 'pkg/metrics/proto/metric_query.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/group_by_spec.proto";' 'pkg/metrics/proto/metric_query.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/aggregation_spec.proto";' 'pkg/metrics/proto/metric_query.proto'

# Fix imports for metrics/proto/get_provider_stats_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/metrics/proto/get_provider_stats_response.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/metrics/proto/get_provider_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/metrics/proto/get_provider_stats_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_statistics.proto";' 'pkg/metrics/proto/get_provider_stats_response.proto'

# Fix imports for common/proto/filter_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/common/proto/filter_options.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/common/proto/filter_options.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/common/proto/filter_options.proto'
sed -i '/^import.*proto";$/a import "common/proto/filter_value.proto";' 'pkg/common/proto/filter_options.proto'

# Fix imports for queue/proto/get_queue_stats_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/queue/proto/get_queue_stats_request.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/queue/proto/get_queue_stats_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/queue/proto/get_queue_stats_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/stats_granularity.proto";' 'pkg/queue/proto/get_queue_stats_request.proto'

# Fix imports for queue/proto/restore_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/time_range.proto";' 'pkg/queue/proto/restore_options.proto'
sed -i '/^import.*proto";$/a import "common/proto/time_range.proto";' 'pkg/queue/proto/restore_options.proto'
sed -i '/^import.*proto";$/a import "queue/proto/time_range.proto";' 'pkg/queue/proto/restore_options.proto'
sed -i '/^import.*proto";$/a import "queue/proto/offset_range.proto";' 'pkg/queue/proto/restore_options.proto'
sed -i '/^import.*proto";$/a import "queue/proto/performance_options.proto";' 'pkg/queue/proto/restore_options.proto'
sed -i '/^import.*proto";$/a import "queue/proto/filter_criteria.proto";' 'pkg/queue/proto/restore_options.proto'

# Fix imports for metrics/proto/config_change.proto
sed -i '/^import.*proto";$/a import "metrics/proto/change_type.proto";' 'pkg/metrics/proto/config_change.proto'
sed -i '/^import.*proto";$/a import "config/proto/change_type.proto";' 'pkg/metrics/proto/config_change.proto'

# Fix imports for config/proto/template_change.proto
sed -i '/^import.*proto";$/a import "metrics/proto/change_type.proto";' 'pkg/config/proto/template_change.proto'
sed -i '/^import.*proto";$/a import "config/proto/change_type.proto";' 'pkg/config/proto/template_change.proto'

# Fix imports for config/proto/value_history_entry.proto
sed -i '/^import.*proto";$/a import "metrics/proto/change_type.proto";' 'pkg/config/proto/value_history_entry.proto'
sed -i '/^import.*proto";$/a import "config/proto/change_type.proto";' 'pkg/config/proto/value_history_entry.proto'

# Fix imports for metrics/proto/buffer_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/buffer_overflow_strategy.proto";' 'pkg/metrics/proto/buffer_config.proto'

# Fix imports for metrics/proto/get_stats_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/timestamp_range.proto";' 'pkg/metrics/proto/get_stats_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/timestamp_range.proto";' 'pkg/metrics/proto/get_stats_request.proto'

# Fix imports for metrics/proto/delete_provider_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/backup_info.proto";' 'pkg/metrics/proto/delete_provider_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/backup_info.proto";' 'pkg/metrics/proto/delete_provider_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/deletion_result.proto";' 'pkg/metrics/proto/delete_provider_response.proto'

# Fix imports for metrics/proto/unregister_metric_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/backup_info.proto";' 'pkg/metrics/proto/unregister_metric_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/backup_info.proto";' 'pkg/metrics/proto/unregister_metric_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/unregistration_result.proto";' 'pkg/metrics/proto/unregister_metric_response.proto'

# Fix imports for queue/proto/delete_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/backup_info.proto";' 'pkg/queue/proto/delete_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/backup_info.proto";' 'pkg/queue/proto/delete_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/deletion_stats.proto";' 'pkg/queue/proto/delete_response.proto'

# Fix imports for metrics/proto/histogram_metric.proto
sed -i '/^import.*proto";$/a import "metrics/proto/histogram_bucket.proto";' 'pkg/metrics/proto/histogram_metric.proto'

# Fix imports for metrics/proto/histogram_value.proto
sed -i '/^import.*proto";$/a import "metrics/proto/histogram_bucket.proto";' 'pkg/metrics/proto/histogram_value.proto'

# Fix imports for metrics/proto/metric_health.proto
sed -i '/^import.*proto";$/a import "metrics/proto/health_status.proto";' 'pkg/metrics/proto/metric_health.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_status.proto";' 'pkg/metrics/proto/metric_health.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_status.proto";' 'pkg/metrics/proto/metric_health.proto'
sed -i '/^import.*proto";$/a import "common/proto/health_status.proto";' 'pkg/metrics/proto/metric_health.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_status.proto";' 'pkg/metrics/proto/metric_health.proto'

# Fix imports for metrics/proto/metrics_health_info.proto
sed -i '/^import.*proto";$/a import "metrics/proto/health_status.proto";' 'pkg/metrics/proto/metrics_health_info.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_status.proto";' 'pkg/metrics/proto/metrics_health_info.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_status.proto";' 'pkg/metrics/proto/metrics_health_info.proto'
sed -i '/^import.*proto";$/a import "common/proto/health_status.proto";' 'pkg/metrics/proto/metrics_health_info.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_status.proto";' 'pkg/metrics/proto/metrics_health_info.proto'

# Fix imports for metrics/proto/create_provider_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_config.proto";' 'pkg/metrics/proto/create_provider_request.proto'

# Fix imports for metrics/proto/data_volume_stats.proto
sed -i '/^import.*proto";$/a import "metrics/proto/data_volume_data_point.proto";' 'pkg/metrics/proto/data_volume_stats.proto'

# Fix imports for metrics/proto/record_metrics_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/validation_summary.proto";' 'pkg/metrics/proto/record_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/batch_stats.proto";' 'pkg/metrics/proto/record_metrics_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/batch_stats.proto";' 'pkg/metrics/proto/record_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_result.proto";' 'pkg/metrics/proto/record_metrics_response.proto'

# Fix imports for db/proto/execute_batch_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/batch_stats.proto";' 'pkg/db/proto/execute_batch_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/batch_stats.proto";' 'pkg/db/proto/execute_batch_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/batch_operation_result.proto";' 'pkg/db/proto/execute_batch_response.proto'

# Fix imports for metrics/proto/registration_result.proto
sed -i '/^import.*proto";$/a import "metrics/proto/schema_change.proto";' 'pkg/metrics/proto/registration_result.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/registration_action.proto";' 'pkg/metrics/proto/registration_result.proto'

# Fix imports for metrics/proto/export_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/export_format.proto";' 'pkg/metrics/proto/export_metrics_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/export_format.proto";' 'pkg/metrics/proto/export_metrics_request.proto'

# Fix imports for metrics/proto/deletion_result.proto
sed -i '/^import.*proto";$/a import "metrics/proto/dry_run_result.proto";' 'pkg/metrics/proto/deletion_result.proto'

# Fix imports for metrics/proto/unregistration_result.proto
sed -i '/^import.*proto";$/a import "metrics/proto/dry_run_result.proto";' 'pkg/metrics/proto/unregistration_result.proto'

# Fix imports for metrics/proto/configuration_summary.proto
sed -i '/^import.*proto";$/a import "metrics/proto/resource_limits_summary.proto";' 'pkg/metrics/proto/configuration_summary.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/security_summary.proto";' 'pkg/metrics/proto/configuration_summary.proto'

# Fix imports for metrics/proto/provider_config_summary.proto
sed -i '/^import.*proto";$/a import "metrics/proto/resource_limits_summary.proto";' 'pkg/metrics/proto/provider_config_summary.proto'

# Fix imports for metrics/proto/metrics_summary.proto
sed -i '/^import.*proto";$/a import "metrics/proto/top_metrics.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_type_counts.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/error_stats.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "queue/proto/error_stats.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/performance_stats.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "web/proto/performance_stats.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/retention_info.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retention_info.proto";' 'pkg/metrics/proto/metrics_summary.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/export_status.proto";' 'pkg/metrics/proto/metrics_summary.proto'

# Fix imports for queue/proto/get_queue_stats_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/error_stats.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/error_stats.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_stats_summary.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/messages/queue_stats.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/historical_stats.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/performance_metrics.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer_stats.proto";' 'pkg/queue/proto/get_queue_stats_response.proto'

# Fix imports for queue/proto/get_topic_info_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/retention_info.proto";' 'pkg/queue/proto/get_topic_info_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retention_info.proto";' 'pkg/queue/proto/get_topic_info_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/partition_info.proto";' 'pkg/queue/proto/get_topic_info_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/topic_configuration.proto";' 'pkg/queue/proto/get_topic_info_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/topic_stats.proto";' 'pkg/queue/proto/get_topic_info_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/topic_permissions.proto";' 'pkg/queue/proto/get_topic_info_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/owner_info.proto";' 'pkg/queue/proto/get_topic_info_response.proto'

# Fix imports for metrics/proto/stream_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/stream_options.proto";' 'pkg/metrics/proto/stream_metrics_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/stream_start.proto";' 'pkg/metrics/proto/stream_metrics_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_filter.proto";' 'pkg/metrics/proto/stream_metrics_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/buffer_config.proto";' 'pkg/metrics/proto/stream_metrics_request.proto'

# Fix imports for metrics/proto/metric_type_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/gauge_config.proto";' 'pkg/metrics/proto/metric_type_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/histogram_config.proto";' 'pkg/metrics/proto/metric_type_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/summary_config.proto";' 'pkg/metrics/proto/metric_type_config.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/counter_config.proto";' 'pkg/metrics/proto/metric_type_config.proto'

# Fix imports for metrics/proto/provider_info.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_status.proto";' 'pkg/metrics/proto/provider_info.proto'

# Fix imports for metrics/proto/update_provider_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_status.proto";' 'pkg/metrics/proto/update_provider_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/validation_result.proto";' 'pkg/metrics/proto/update_provider_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/validation_result.proto";' 'pkg/metrics/proto/update_provider_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/validation_result.proto";' 'pkg/metrics/proto/update_provider_response.proto'

# Fix imports for metrics/proto/provider_summary.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_status.proto";' 'pkg/metrics/proto/provider_summary.proto'

# Fix imports for metrics/proto/create_provider_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_status.proto";' 'pkg/metrics/proto/create_provider_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/validation_result.proto";' 'pkg/metrics/proto/create_provider_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/validation_result.proto";' 'pkg/metrics/proto/create_provider_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/validation_result.proto";' 'pkg/metrics/proto/create_provider_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_endpoints.proto";' 'pkg/metrics/proto/create_provider_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/applied_config.proto";' 'pkg/metrics/proto/create_provider_response.proto'

# Fix imports for metrics/proto/export_status.proto
sed -i '/^import.*proto";$/a import "metrics/proto/exporter_status.proto";' 'pkg/metrics/proto/export_status.proto'

# Fix imports for web/proto/security_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/tls_config.proto";' 'pkg/web/proto/security_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/tls_config.proto";' 'pkg/web/proto/security_config.proto'

# Fix imports for metrics/proto/query_metrics_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_statistics.proto";' 'pkg/metrics/proto/query_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/query_plan.proto";' 'pkg/metrics/proto/query_metrics_response.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_series.proto";' 'pkg/metrics/proto/query_metrics_response.proto'

# Fix imports for metrics/proto/time_series.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_sample.proto";' 'pkg/metrics/proto/time_series.proto'

# Fix imports for metrics/proto/export_stats.proto
sed -i '/^import.*proto";$/a import "metrics/proto/export_destination_stats.proto";' 'pkg/metrics/proto/export_stats.proto'

# Fix imports for metrics/proto/set_metric_metadata_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/set_metric_metadata_response.proto'

# Fix imports for metrics/proto/set_metric_metadata_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/set_metric_metadata_request.proto'

# Fix imports for metrics/proto/list_metrics_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/list_metrics_response.proto'

# Fix imports for metrics/proto/create_metric_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/create_metric_response.proto'

# Fix imports for metrics/proto/update_metric_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_metadata.proto";' 'pkg/metrics/proto/update_metric_response.proto'

# Fix imports for metrics/proto/output_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/response_compression.proto";' 'pkg/metrics/proto/output_options.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/numeric_format.proto";' 'pkg/metrics/proto/output_options.proto'

# Fix imports for metrics/proto/set_alerting_rules_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/alerting_rule.proto";' 'pkg/metrics/proto/set_alerting_rules_request.proto'

# Fix imports for metrics/proto/get_alerting_rules_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/alerting_rule.proto";' 'pkg/metrics/proto/get_alerting_rules_response.proto'

# Fix imports for metrics/proto/unregister_metric_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/unregistration_options.proto";' 'pkg/metrics/proto/unregister_metric_request.proto'

# Fix imports for metrics/proto/get_metric_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/get_metric_response.proto'

# Fix imports for metrics/proto/record_metric_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/record_metric_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/batch_context.proto";' 'pkg/metrics/proto/record_metric_request.proto'

# Fix imports for metrics/proto/create_metric_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/create_metric_request.proto'

# Fix imports for metrics/proto/update_metric_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/update_metric_request.proto'

# Fix imports for metrics/proto/record_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/record_metrics_request.proto'

# Fix imports for metrics/proto/metrics_service.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/unregister_metric_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/record_metric_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/query_metrics_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_metrics_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/get_metrics_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_metric_metadata_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/query_metrics_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_metrics_summary_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/unregister_metric_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_metrics_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/get_metrics_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/record_metrics_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_metrics_summary_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/stream_metrics_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/stream_metrics_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/record_metrics_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/record_metric_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/register_metric_request.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_metric_metadata_response.proto";' 'pkg/metrics/proto/metrics_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/register_metric_response.proto";' 'pkg/metrics/proto/metrics_service.proto'

# Fix imports for metrics/proto/import_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_data.proto";' 'pkg/metrics/proto/import_metrics_request.proto'

# Fix imports for metrics/proto/record_gauge_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/gauge_operation.proto";' 'pkg/metrics/proto/record_gauge_request.proto'

# Fix imports for metrics/proto/alerting_condition.proto
sed -i '/^import.*proto";$/a import "metrics/proto/comparison_operator.proto";' 'pkg/metrics/proto/alerting_condition.proto'

# Fix imports for metrics/proto/record_counter_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/counter_metric.proto";' 'pkg/metrics/proto/record_counter_response.proto'

# Fix imports for metrics/proto/provider_settings.proto
sed -i '/^import.*proto";$/a import "metrics/proto/prometheus_settings.proto";' 'pkg/metrics/proto/provider_settings.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/stats_d_settings.proto";' 'pkg/metrics/proto/provider_settings.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/open_telemetry_settings.proto";' 'pkg/metrics/proto/provider_settings.proto'

# Fix imports for auth/proto/auth_provider.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_type.proto";' 'pkg/auth/proto/auth_provider.proto'
sed -i '/^import.*proto";$/a import "auth/proto/provider_type.proto";' 'pkg/auth/proto/auth_provider.proto'

# Fix imports for metrics/proto/summary_metric.proto
sed -i '/^import.*proto";$/a import "metrics/proto/summary_quantile.proto";' 'pkg/metrics/proto/summary_metric.proto'

# Fix imports for metrics/proto/metric_value.proto
sed -i '/^import.*proto";$/a import "metrics/proto/summary_value.proto";' 'pkg/metrics/proto/metric_value.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/histogram_value.proto";' 'pkg/metrics/proto/metric_value.proto'

# Fix imports for metrics/proto/provider_settings_update.proto
sed -i '/^import.*proto";$/a import "metrics/proto/open_telemetry_settings_update.proto";' 'pkg/metrics/proto/provider_settings_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/prometheus_settings_update.proto";' 'pkg/metrics/proto/provider_settings_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/stats_d_settings_update.proto";' 'pkg/metrics/proto/provider_settings_update.proto'

# Fix imports for queue/proto/restore_queue_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/validation_result.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/validation_result.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/validation_result.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/restore_error.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/partition_restore_result.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/restore_statistics.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/restore_status.proto";' 'pkg/queue/proto/restore_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/restore_warning.proto";' 'pkg/queue/proto/restore_queue_response.proto'

# Fix imports for queue/proto/queue_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/retention_policy.proto";' 'pkg/queue/proto/queue_config.proto'
sed -i '/^import.*proto";$/a import "config/proto/retention_policy.proto";' 'pkg/queue/proto/queue_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retention_policy.proto";' 'pkg/queue/proto/queue_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/priority_level.proto";' 'pkg/queue/proto/queue_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_type.proto";' 'pkg/queue/proto/queue_config.proto'

# Fix imports for metrics/proto/register_metric_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/metric_definition.proto";' 'pkg/metrics/proto/register_metric_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/registration_options.proto";' 'pkg/metrics/proto/register_metric_request.proto'

# Fix imports for metrics/proto/start_scraping_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_job.proto";' 'pkg/metrics/proto/start_scraping_response.proto'

# Fix imports for metrics/proto/stop_scraping_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_job.proto";' 'pkg/metrics/proto/stop_scraping_response.proto'

# Fix imports for metrics/proto/export_config_update.proto
sed -i '/^import.*proto";$/a import "metrics/proto/export_destination_update.proto";' 'pkg/metrics/proto/export_config_update.proto'

# Fix imports for metrics/proto/resource_usage_stats.proto
sed -i '/^import.*proto";$/a import "metrics/proto/network_usage.proto";' 'pkg/metrics/proto/resource_usage_stats.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/memory_usage.proto";' 'pkg/metrics/proto/resource_usage_stats.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_data_point.proto";' 'pkg/metrics/proto/resource_usage_stats.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/disk_usage.proto";' 'pkg/metrics/proto/resource_usage_stats.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/cpu_usage.proto";' 'pkg/metrics/proto/resource_usage_stats.proto'

# Fix imports for metrics/proto/trend_analysis.proto
sed -i '/^import.*proto";$/a import "metrics/proto/performance_trend.proto";' 'pkg/metrics/proto/trend_analysis.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/data_volume_trend.proto";' 'pkg/metrics/proto/trend_analysis.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_usage_trend.proto";' 'pkg/metrics/proto/trend_analysis.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/error_trend.proto";' 'pkg/metrics/proto/trend_analysis.proto'

# Fix imports for metrics/proto/applied_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/resource_allocations.proto";' 'pkg/metrics/proto/applied_config.proto'

# Fix imports for metrics/proto/query_step.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_operation.proto";' 'pkg/metrics/proto/query_step.proto'

# Fix imports for metrics/proto/security_config_update.proto
sed -i '/^import.*proto";$/a import "metrics/proto/tls_config_update.proto";' 'pkg/metrics/proto/security_config_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/api_key_config_update.proto";' 'pkg/metrics/proto/security_config_update.proto'

# Fix imports for metrics/proto/deletion_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/cleanup_strategy.proto";' 'pkg/metrics/proto/deletion_options.proto'

# Fix imports for metrics/proto/provider_config_update.proto
sed -i '/^import.*proto";$/a import "metrics/proto/tag_updates.proto";' 'pkg/metrics/proto/provider_config_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/provider_settings_update.proto";' 'pkg/metrics/proto/provider_config_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/security_config_update.proto";' 'pkg/metrics/proto/provider_config_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/resource_limits_update.proto";' 'pkg/metrics/proto/provider_config_update.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/export_config_update.proto";' 'pkg/metrics/proto/provider_config_update.proto'

# Fix imports for metrics/proto/update_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/update_strategy.proto";' 'pkg/metrics/proto/update_options.proto'

# Fix imports for metrics/proto/query_plan.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_step.proto";' 'pkg/metrics/proto/query_plan.proto'

# Fix imports for metrics/proto/batch_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/batch_priority.proto";' 'pkg/metrics/proto/batch_options.proto'

# Fix imports for metrics/proto/provider_stats.proto
sed -i '/^import.*proto";$/a import "metrics/proto/resource_usage.proto";' 'pkg/metrics/proto/provider_stats.proto'

# Fix imports for queue/proto/queue_monitoring_service.proto
sed -i '/^import.*proto";$/a import "metrics/proto/stream_metrics_request.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/stream_metrics_request.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_stats_request.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_health_response.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metrics_event.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_cluster_info_request.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_health_request.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_stats_response.proto";' 'pkg/queue/proto/queue_monitoring_service.proto'

# Fix imports for metrics/proto/update_result.proto
sed -i '/^import.*proto";$/a import "metrics/proto/config_change.proto";' 'pkg/metrics/proto/update_result.proto'
sed -i '/^import.*proto";$/a import "config/proto/config_change.proto";' 'pkg/metrics/proto/update_result.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/update_action.proto";' 'pkg/metrics/proto/update_result.proto'

# Fix imports for config/proto/get_config_history_response.proto
sed -i '/^import.*proto";$/a import "metrics/proto/config_change.proto";' 'pkg/config/proto/get_config_history_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/config_change.proto";' 'pkg/config/proto/get_config_history_response.proto'

# Fix imports for metrics/proto/timer_metric.proto
sed -i '/^import.*proto";$/a import "metrics/proto/timer_statistics.proto";' 'pkg/metrics/proto/timer_metric.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/percentile_measurement.proto";' 'pkg/metrics/proto/timer_metric.proto'

# Fix imports for metrics/proto/scrape_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/scrape_target.proto";' 'pkg/metrics/proto/scrape_config.proto'

# Fix imports for metrics/proto/aggregation_spec.proto
sed -i '/^import.*proto";$/a import "metrics/proto/aggregation_type.proto";' 'pkg/metrics/proto/aggregation_spec.proto'

# Fix imports for metrics/proto/error_stats.proto
sed -i '/^import.*proto";$/a import "metrics/proto/error_type_count.proto";' 'pkg/metrics/proto/error_stats.proto'

# Fix imports for metrics/proto/provider_status.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_state.proto";' 'pkg/metrics/proto/provider_status.proto'

# Fix imports for metrics/proto/list_providers_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/provider_filter.proto";' 'pkg/metrics/proto/list_providers_request.proto'

# Fix imports for metrics/proto/query_metrics_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/query_output_options.proto";' 'pkg/metrics/proto/query_metrics_request.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/metric_query.proto";' 'pkg/metrics/proto/query_metrics_request.proto'

# Fix imports for metrics/proto/alert_notification.proto
sed -i '/^import.*proto";$/a import "metrics/proto/alert_severity.proto";' 'pkg/metrics/proto/alert_notification.proto'
sed -i '/^import.*proto";$/a import "config/proto/alert_severity.proto";' 'pkg/metrics/proto/alert_notification.proto'
sed -i '/^import.*proto";$/a import "queue/proto/alert_severity.proto";' 'pkg/metrics/proto/alert_notification.proto'

# Fix imports for queue/proto/alert_rule.proto
sed -i '/^import.*proto";$/a import "metrics/proto/alert_severity.proto";' 'pkg/queue/proto/alert_rule.proto'
sed -i '/^import.*proto";$/a import "config/proto/alert_severity.proto";' 'pkg/queue/proto/alert_rule.proto'
sed -i '/^import.*proto";$/a import "queue/proto/alert_severity.proto";' 'pkg/queue/proto/alert_rule.proto'
sed -i '/^import.*proto";$/a import "queue/proto/alert_condition.proto";' 'pkg/queue/proto/alert_rule.proto'

# Fix imports for queue/proto/notification_channel.proto
sed -i '/^import.*proto";$/a import "metrics/proto/alert_severity.proto";' 'pkg/queue/proto/notification_channel.proto'
sed -i '/^import.*proto";$/a import "config/proto/alert_severity.proto";' 'pkg/queue/proto/notification_channel.proto'
sed -i '/^import.*proto";$/a import "queue/proto/alert_severity.proto";' 'pkg/queue/proto/notification_channel.proto'
sed -i '/^import.*proto";$/a import "queue/proto/notification_channel_type.proto";' 'pkg/queue/proto/notification_channel.proto'

# Fix imports for queue/proto/alerting_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/alert_severity.proto";' 'pkg/queue/proto/alerting_config.proto'
sed -i '/^import.*proto";$/a import "config/proto/alert_severity.proto";' 'pkg/queue/proto/alerting_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/alert_severity.proto";' 'pkg/queue/proto/alerting_config.proto'
sed -i '/^import.*proto";$/a import "config/proto/notification_channel.proto";' 'pkg/queue/proto/alerting_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/notification_channel.proto";' 'pkg/queue/proto/alerting_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/alert_rule.proto";' 'pkg/queue/proto/alerting_config.proto'

# Fix imports for metrics/proto/stream_options.proto
sed -i '/^import.*proto";$/a import "metrics/proto/stream_qos.proto";' 'pkg/metrics/proto/stream_options.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/stream_compression.proto";' 'pkg/metrics/proto/stream_options.proto'

# Fix imports for cache/proto/get_namespace_stats_response.proto
sed -i '/^import.*proto";$/a import "cache/proto/namespace_stats.proto";' 'pkg/cache/proto/get_namespace_stats_response.proto'

# Fix imports for cache/proto/get_response.proto
sed -i '/^import.*proto";$/a import "cache/proto/cache_entry.proto";' 'pkg/cache/proto/get_response.proto'

# Fix imports for cache/proto/cache_admin_service.proto
sed -i '/^import.*proto";$/a import "cache/proto/delete_namespace_request.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/list_namespaces_request.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_namespace_stats_request.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/configure_policy_request.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/create_namespace_request.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_namespace_stats_response.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/list_namespaces_response.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/configure_policy_response.proto";' 'pkg/cache/proto/cache_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/create_namespace_response.proto";' 'pkg/cache/proto/cache_admin_service.proto'

# Fix imports for cache/proto/cache_service.proto
sed -i '/^import.*proto";$/a import "cache/proto/flush_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_stats_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_stats_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/exists_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/get_stats_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_stats_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/keys_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_multiple_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/flush_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/delete_multiple_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/delete_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delete_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/clear_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/touch_expiration_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/set_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/clear_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/increment_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/decrement_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_multiple_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/set_multiple_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/decrement_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/set_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/keys_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/get_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/increment_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/set_multiple_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/delete_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delete_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/exists_response.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/delete_multiple_request.proto";' 'pkg/cache/proto/cache_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/touch_expiration_request.proto";' 'pkg/cache/proto/cache_service.proto'

# Fix imports for cache/proto/list_namespaces_response.proto
sed -i '/^import.*proto";$/a import "cache/proto/namespace_info.proto";' 'pkg/cache/proto/list_namespaces_response.proto'

# Fix imports for config/proto/approval_workflow.proto
sed -i '/^import.*proto";$/a import "config/proto/approval_stage.proto";' 'pkg/config/proto/approval_workflow.proto'

# Fix imports for config/proto/inheritance_filter.proto
sed -i '/^import.*proto";$/a import "config/proto/filter_type.proto";' 'pkg/config/proto/inheritance_filter.proto'
sed -i '/^import.*proto";$/a import "log/proto/filter_type.proto";' 'pkg/config/proto/inheritance_filter.proto'
sed -i '/^import.*proto";$/a import "config/proto/filter_action.proto";' 'pkg/config/proto/inheritance_filter.proto'

# Fix imports for config/proto/health_check.proto
sed -i '/^import.*proto";$/a import "config/proto/health_check_type.proto";' 'pkg/config/proto/health_check.proto'

# Fix imports for config/proto/get_schema_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_schema.proto";' 'pkg/config/proto/get_schema_response.proto'

# Fix imports for config/proto/set_config_schema_request.proto
sed -i '/^import.*proto";$/a import "config/proto/config_schema.proto";' 'pkg/config/proto/set_config_schema_request.proto'

# Fix imports for config/proto/secret_audit_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/secret_audit_level.proto";' 'pkg/config/proto/secret_audit_settings.proto'

# Fix imports for config/proto/rotation_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/rotation_event.proto";' 'pkg/config/proto/rotation_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/rotation_frequency.proto";' 'pkg/config/proto/rotation_settings.proto'

# Fix imports for config/proto/get_multiple_config_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_entry.proto";' 'pkg/config/proto/get_multiple_config_response.proto'

# Fix imports for config/proto/set_config_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_entry.proto";' 'pkg/config/proto/set_config_response.proto'

# Fix imports for config/proto/watch_config_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_entry.proto";' 'pkg/config/proto/watch_config_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/config_change_type.proto";' 'pkg/config/proto/watch_config_response.proto'

# Fix imports for config/proto/list_config_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_entry.proto";' 'pkg/config/proto/list_config_response.proto'

# Fix imports for config/proto/validate_config_request.proto
sed -i '/^import.*proto";$/a import "config/proto/config_entry.proto";' 'pkg/config/proto/validate_config_request.proto'

# Fix imports for config/proto/get_config_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_entry.proto";' 'pkg/config/proto/get_config_response.proto'

# Fix imports for config/proto/validation_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/retry_settings.proto";' 'pkg/config/proto/validation_settings.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retry_settings.proto";' 'pkg/config/proto/validation_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/validation_rule.proto";' 'pkg/config/proto/validation_settings.proto'

# Fix imports for queue/proto/subscription_config_update.proto
sed -i '/^import.*proto";$/a import "config/proto/retry_settings.proto";' 'pkg/queue/proto/subscription_config_update.proto'
sed -i '/^import.*proto";$/a import "queue/proto/retry_settings.proto";' 'pkg/queue/proto/subscription_config_update.proto'
sed -i '/^import.*proto";$/a import "queue/proto/filter_settings.proto";' 'pkg/queue/proto/subscription_config_update.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delivery_settings.proto";' 'pkg/queue/proto/subscription_config_update.proto'
sed -i '/^import.*proto";$/a import "queue/proto/routing_settings.proto";' 'pkg/queue/proto/subscription_config_update.proto'

# Fix imports for config/proto/retry_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/backoff_strategy.proto";' 'pkg/config/proto/retry_settings.proto'

# Fix imports for config/proto/transformation_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/transformation_step.proto";' 'pkg/config/proto/transformation_settings.proto'

# Fix imports for config/proto/version_quality_metrics.proto
sed -i '/^import.*proto";$/a import "config/proto/version_quality_issue.proto";' 'pkg/config/proto/version_quality_metrics.proto'

# Fix imports for config/proto/value_validation_result.proto
sed -i '/^import.*proto";$/a import "config/proto/value_validation_result_type.proto";' 'pkg/config/proto/value_validation_result.proto'
sed -i '/^import.*proto";$/a import "config/proto/value_validation_severity.proto";' 'pkg/config/proto/value_validation_result.proto'

# Fix imports for config/proto/deployment_info.proto
sed -i '/^import.*proto";$/a import "config/proto/deployment_status.proto";' 'pkg/config/proto/deployment_info.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check.proto";' 'pkg/config/proto/deployment_info.proto'
sed -i '/^import.*proto";$/a import "config/proto/deployment_rollback_info.proto";' 'pkg/config/proto/deployment_info.proto'

# Fix imports for config/proto/config_service.proto
sed -i '/^import.*proto";$/a import "config/proto/set_multiple_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/watch_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/validate_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_multiple_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/set_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_multiple_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/validate_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_schema_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_schema_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/set_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/watch_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/list_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/set_multiple_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/list_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_config_request.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_config_response.proto";' 'pkg/config/proto/config_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/delete_config_request.proto";' 'pkg/config/proto/config_service.proto'

# Fix imports for config/proto/synchronization_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/synchronization_target.proto";' 'pkg/config/proto/synchronization_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/synchronization_frequency.proto";' 'pkg/config/proto/synchronization_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/conflict_resolution.proto";' 'pkg/config/proto/synchronization_settings.proto'
sed -i '/^import.*proto";$/a import "queue/proto/conflict_resolution.proto";' 'pkg/config/proto/synchronization_settings.proto'

# Fix imports for queue/proto/consistency_config.proto
sed -i '/^import.*proto";$/a import "config/proto/conflict_resolution.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/conflict_resolution.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/replication_consistency.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/ack_level.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/ordering_config.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/write_consistency.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/read_consistency.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/durability_level.proto";' 'pkg/queue/proto/consistency_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consistency_validation.proto";' 'pkg/queue/proto/consistency_config.proto'

# Fix imports for config/proto/config_diff.proto
sed -i '/^import.*proto";$/a import "config/proto/config_diff_entry.proto";' 'pkg/config/proto/config_diff.proto'

# Fix imports for config/proto/template_parameter.proto
sed -i '/^import.*proto";$/a import "config/proto/parameter_type.proto";' 'pkg/config/proto/template_parameter.proto'
sed -i '/^import.*proto";$/a import "config/proto/parameter_constraints.proto";' 'pkg/config/proto/template_parameter.proto'

# Fix imports for config/proto/audit_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/audit_level.proto";' 'pkg/config/proto/audit_settings.proto'

# Fix imports for config/proto/validate_config_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_validation_error.proto";' 'pkg/config/proto/validate_config_response.proto'
sed -i '/^import.*proto";$/a import "config/proto/config_validation_warning.proto";' 'pkg/config/proto/validate_config_response.proto'

# Fix imports for config/proto/backup_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/backup_frequency.proto";' 'pkg/config/proto/backup_settings.proto'

# Fix imports for config/proto/value_dependency.proto
sed -i '/^import.*proto";$/a import "config/proto/dependency_type.proto";' 'pkg/config/proto/value_dependency.proto'

# Fix imports for config/proto/access_control.proto
sed -i '/^import.*proto";$/a import "config/proto/rate_limits.proto";' 'pkg/config/proto/access_control.proto'
sed -i '/^import.*proto";$/a import "config/proto/access_restriction.proto";' 'pkg/config/proto/access_control.proto'

# Fix imports for config/proto/value_reference.proto
sed -i '/^import.*proto";$/a import "config/proto/reference_type.proto";' 'pkg/config/proto/value_reference.proto'

# Fix imports for config/proto/notification_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/notification_channel.proto";' 'pkg/config/proto/notification_settings.proto'
sed -i '/^import.*proto";$/a import "queue/proto/notification_channel.proto";' 'pkg/config/proto/notification_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/notification_trigger.proto";' 'pkg/config/proto/notification_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/batching_settings.proto";' 'pkg/config/proto/notification_settings.proto'

# Fix imports for config/proto/value_usage_statistics.proto
sed -i '/^import.*proto";$/a import "config/proto/value_usage_trend.proto";' 'pkg/config/proto/value_usage_statistics.proto'

# Fix imports for config/proto/notification_channel.proto
sed -i '/^import.*proto";$/a import "config/proto/channel_type.proto";' 'pkg/config/proto/notification_channel.proto'

# Fix imports for config/proto/deprecation_info.proto
sed -i '/^import.*proto";$/a import "config/proto/deprecation_level.proto";' 'pkg/config/proto/deprecation_info.proto'

# Fix imports for config/proto/version_dependency.proto
sed -i '/^import.*proto";$/a import "config/proto/version_dependency_type.proto";' 'pkg/config/proto/version_dependency.proto'

# Fix imports for config/proto/health_status.proto
sed -i '/^import.*proto";$/a import "config/proto/health_check_result.proto";' 'pkg/config/proto/health_status.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_result.proto";' 'pkg/config/proto/health_status.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_state.proto";' 'pkg/config/proto/health_status.proto'

# Fix imports for health/proto/health_check_all_response.proto
sed -i '/^import.*proto";$/a import "config/proto/health_check_result.proto";' 'pkg/health/proto/health_check_all_response.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_result.proto";' 'pkg/health/proto/health_check_all_response.proto'
sed -i '/^import.*proto";$/a import "health/proto/serving_status.proto";' 'pkg/health/proto/health_check_all_response.proto'

# Fix imports for config/proto/health_check_result.proto
sed -i '/^import.*proto";$/a import "config/proto/health_state.proto";' 'pkg/config/proto/health_check_result.proto'

# Fix imports for config/proto/inheritance_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/inheritance_transformation.proto";' 'pkg/config/proto/inheritance_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/inheritance_filter.proto";' 'pkg/config/proto/inheritance_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/merge_strategy.proto";' 'pkg/config/proto/inheritance_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/inheritance_strategy.proto";' 'pkg/config/proto/inheritance_settings.proto'

# Fix imports for config/proto/approval_info.proto
sed -i '/^import.*proto";$/a import "config/proto/approval_status.proto";' 'pkg/config/proto/approval_info.proto'

# Fix imports for config/proto/secret_validation_result.proto
sed -i '/^import.*proto";$/a import "config/proto/secret_validation_result_type.proto";' 'pkg/config/proto/secret_validation_result.proto'
sed -i '/^import.*proto";$/a import "config/proto/secret_validation_severity.proto";' 'pkg/config/proto/secret_validation_result.proto'

# Fix imports for config/proto/template_hook.proto
sed -i '/^import.*proto";$/a import "config/proto/hook_type.proto";' 'pkg/config/proto/template_hook.proto'
sed -i '/^import.*proto";$/a import "config/proto/hook_error_handling.proto";' 'pkg/config/proto/template_hook.proto'

# Fix imports for config/proto/transformation_step.proto
sed -i '/^import.*proto";$/a import "config/proto/transformation_type.proto";' 'pkg/config/proto/transformation_step.proto'

# Fix imports for config/proto/inheritance_transformation.proto
sed -i '/^import.*proto";$/a import "config/proto/transformation_type.proto";' 'pkg/config/proto/inheritance_transformation.proto'

# Fix imports for config/proto/get_config_stats_response.proto
sed -i '/^import.*proto";$/a import "config/proto/config_stats.proto";' 'pkg/config/proto/get_config_stats_response.proto'

# Fix imports for config/proto/validation_rule.proto
sed -i '/^import.*proto";$/a import "config/proto/validation_severity.proto";' 'pkg/config/proto/validation_rule.proto'

# Fix imports for config/proto/validation_result.proto
sed -i '/^import.*proto";$/a import "config/proto/validation_severity.proto";' 'pkg/config/proto/validation_result.proto'
sed -i '/^import.*proto";$/a import "config/proto/validation_result_type.proto";' 'pkg/config/proto/validation_result.proto'

# Fix imports for config/proto/usage_statistics.proto
sed -i '/^import.*proto";$/a import "config/proto/usage_trend.proto";' 'pkg/config/proto/usage_statistics.proto'

# Fix imports for config/proto/version_deployment_info.proto
sed -i '/^import.*proto";$/a import "config/proto/version_health_status.proto";' 'pkg/config/proto/version_deployment_info.proto'
sed -i '/^import.*proto";$/a import "config/proto/version_deployment_status.proto";' 'pkg/config/proto/version_deployment_info.proto'

# Fix imports for config/proto/access_restriction.proto
sed -i '/^import.*proto";$/a import "config/proto/restriction_type.proto";' 'pkg/config/proto/access_restriction.proto'

# Fix imports for config/proto/monitoring_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/monitoring_alert.proto";' 'pkg/config/proto/monitoring_settings.proto'

# Fix imports for config/proto/rollback_info.proto
sed -i '/^import.*proto";$/a import "config/proto/rollback_method.proto";' 'pkg/config/proto/rollback_info.proto'

# Fix imports for config/proto/config_admin_service.proto
sed -i '/^import.*proto";$/a import "config/proto/unwatch_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/backup_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/import_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/export_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/config_backup.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/config_snapshot.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_config_history_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_config_stats_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_config_stats_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_response.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/get_config_history_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/rollback_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/restore_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/set_config_schema_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/reload_config_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_request.proto";' 'pkg/config/proto/config_admin_service.proto'

# Fix imports for web/proto/web_service.proto
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_request.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/handle_request_response.proto";' 'pkg/web/proto/web_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/handle_request_request.proto";' 'pkg/web/proto/web_service.proto'

# Fix imports for health/proto/health_service.proto
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/watch_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/unregister_check_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/get_health_metrics_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/list_services_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/unregister_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_all_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/register_check_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_all_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/watch_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/watch_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/get_service_health_request.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/get_service_health_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/list_services_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/get_health_metrics_response.proto";' 'pkg/health/proto/health_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/register_check_request.proto";' 'pkg/health/proto/health_service.proto'

# Fix imports for db/proto/database_service.proto
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_row_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_row_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/execute_batch_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/execute_batch_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/execute_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/get_connection_info_response.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/get_connection_info_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_request.proto";' 'pkg/db/proto/database_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/execute_response.proto";' 'pkg/db/proto/database_service.proto'

# Fix imports for health/proto/register_check_request.proto
sed -i '/^import.*proto";$/a import "metrics/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "cache/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "config/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "auth/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "web/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "health/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'
sed -i '/^import.*proto";$/a import "db/proto/health_check_request.proto";' 'pkg/health/proto/register_check_request.proto'

# Fix imports for config/proto/caching_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/cache_refresh_strategy.proto";' 'pkg/config/proto/caching_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/cache_invalidation_trigger.proto";' 'pkg/config/proto/caching_settings.proto'

# Fix imports for config/proto/secret_backup_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/secret_backup_frequency.proto";' 'pkg/config/proto/secret_backup_settings.proto'

# Fix imports for config/proto/compliance_settings.proto
sed -i '/^import.*proto";$/a import "config/proto/compliance_reporting.proto";' 'pkg/config/proto/compliance_settings.proto'
sed -i '/^import.*proto";$/a import "config/proto/compliance_audit.proto";' 'pkg/config/proto/compliance_settings.proto'

# Fix imports for auth/proto/get_user_info_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_info.proto";' 'pkg/auth/proto/get_user_info_response.proto'

# Fix imports for auth/proto/list_users_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_info.proto";' 'pkg/auth/proto/list_users_response.proto'

# Fix imports for auth/proto/verify_credentials_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_info.proto";' 'pkg/auth/proto/verify_credentials_response.proto'

# Fix imports for auth/proto/authenticate_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_info.proto";' 'pkg/auth/proto/authenticate_response.proto'
sed -i '/^import.*proto";$/a import "auth/proto/session.proto";' 'pkg/auth/proto/authenticate_response.proto'

# Fix imports for auth/proto/validate_token_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_info.proto";' 'pkg/auth/proto/validate_token_response.proto'

# Fix imports for auth/proto/validate_session_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_info.proto";' 'pkg/auth/proto/validate_session_response.proto'
sed -i '/^import.*proto";$/a import "auth/proto/session.proto";' 'pkg/auth/proto/validate_session_response.proto'

# Fix imports for auth/proto/list_sessions_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/session.proto";' 'pkg/auth/proto/list_sessions_response.proto'

# Fix imports for auth/proto/get_session_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/session.proto";' 'pkg/auth/proto/get_session_response.proto'

# Fix imports for auth/proto/remove_role_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/remove_role_response.proto'

# Fix imports for auth/proto/get_role_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/get_role_response.proto'

# Fix imports for auth/proto/create_role_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/create_role_request.proto'

# Fix imports for auth/proto/get_user_permissions_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/get_user_permissions_response.proto'

# Fix imports for auth/proto/list_roles_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/list_roles_response.proto'

# Fix imports for auth/proto/get_user_roles_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/get_user_roles_response.proto'

# Fix imports for auth/proto/update_role_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/role.proto";' 'pkg/auth/proto/update_role_request.proto'

# Fix imports for auth/proto/token_info.proto
sed -i '/^import.*proto";$/a import "auth/proto/token_type.proto";' 'pkg/auth/proto/token_info.proto'
sed -i '/^import.*proto";$/a import "auth/proto/enums/token_type.proto";' 'pkg/auth/proto/token_info.proto'

# Fix imports for auth/proto/token.proto
sed -i '/^import.*proto";$/a import "auth/proto/token_type.proto";' 'pkg/auth/proto/token.proto'
sed -i '/^import.*proto";$/a import "auth/proto/enums/token_type.proto";' 'pkg/auth/proto/token.proto'
sed -i '/^import.*proto";$/a import "auth/proto/token_status.proto";' 'pkg/auth/proto/token.proto'

# Fix imports for auth/proto/token_metadata.proto
sed -i '/^import.*proto";$/a import "auth/proto/token_type.proto";' 'pkg/auth/proto/token_metadata.proto'
sed -i '/^import.*proto";$/a import "auth/proto/enums/token_type.proto";' 'pkg/auth/proto/token_metadata.proto'

# Fix imports for auth/proto/list_permissions_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/permission.proto";' 'pkg/auth/proto/list_permissions_response.proto'

# Fix imports for auth/proto/get_permission_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/permission.proto";' 'pkg/auth/proto/get_permission_response.proto'

# Fix imports for auth/proto/revoke_permission_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/subject_type.proto";' 'pkg/auth/proto/revoke_permission_request.proto'

# Fix imports for auth/proto/grant_permission_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/subject_type.proto";' 'pkg/auth/proto/grant_permission_request.proto'

# Fix imports for auth/proto/list_permissions_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/subject_type.proto";' 'pkg/auth/proto/list_permissions_request.proto'

# Fix imports for auth/proto/get_user_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_details.proto";' 'pkg/auth/proto/get_user_response.proto'

# Fix imports for auth/proto/list_api_keys_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/messages/api_key.proto";' 'pkg/auth/proto/list_api_keys_response.proto'

# Fix imports for auth/proto/verify_credentials_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/api_key_credentials.proto";' 'pkg/auth/proto/verify_credentials_request.proto'
sed -i '/^import.*proto";$/a import "auth/proto/password_credentials.proto";' 'pkg/auth/proto/verify_credentials_request.proto'

# Fix imports for auth/proto/authenticate_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/api_key_credentials.proto";' 'pkg/auth/proto/authenticate_request.proto'
sed -i '/^import.*proto";$/a import "auth/proto/password_credentials.proto";' 'pkg/auth/proto/authenticate_request.proto'
sed -i '/^import.*proto";$/a import "auth/proto/jwt_credentials.proto";' 'pkg/auth/proto/authenticate_request.proto'
sed -i '/^import.*proto";$/a import "auth/proto/o_auth2_credentials.proto";' 'pkg/auth/proto/authenticate_request.proto'

# Fix imports for auth/proto/verify_mfa_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/mfa_method.proto";' 'pkg/auth/proto/verify_mfa_request.proto'

# Fix imports for auth/proto/enable_mfa_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/mfa_method.proto";' 'pkg/auth/proto/enable_mfa_request.proto'

# Fix imports for auth/proto/disable_mfa_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/mfa_method.proto";' 'pkg/auth/proto/disable_mfa_request.proto'

# Fix imports for auth/proto/mfa_setup_instruction.proto
sed -i '/^import.*proto";$/a import "auth/proto/mfa_method.proto";' 'pkg/auth/proto/mfa_setup_instruction.proto'

# Fix imports for auth/proto/disable_mfa_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/mfa_method.proto";' 'pkg/auth/proto/disable_mfa_response.proto'

# Fix imports for auth/proto/api_key_stats.proto
sed -i '/^import.*proto";$/a import "auth/proto/daily_usage.proto";' 'pkg/auth/proto/api_key_stats.proto'

# Fix imports for auth/proto/role_assignment.proto
sed -i '/^import.*proto";$/a import "auth/proto/role_scope.proto";' 'pkg/auth/proto/role_assignment.proto'

# Fix imports for auth/proto/authorization_service.proto
sed -i '/^import.*proto";$/a import "auth/proto/get_user_permissions_request.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_user_roles_request.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_user_roles_response.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_user_permissions_response.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/authorize_response.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/authorize_response.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/authorize_request.proto";' 'pkg/auth/proto/authorization_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/authorize_request.proto";' 'pkg/auth/proto/authorization_service.proto'

# Fix imports for auth/proto/security_context.proto
sed -i '/^import.*proto";$/a import "auth/proto/auth_method.proto";' 'pkg/auth/proto/security_context.proto'
sed -i '/^import.*proto";$/a import "auth/proto/enums/auth_method.proto";' 'pkg/auth/proto/security_context.proto'
sed -i '/^import.*proto";$/a import "web/proto/auth_method.proto";' 'pkg/auth/proto/security_context.proto'

# Fix imports for auth/proto/session_service.proto
sed -i '/^import.*proto";$/a import "auth/proto/update_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/update_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/delete_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/delete_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/delete_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/delete_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/terminate_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_sessions_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/list_sessions_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/get_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/create_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/create_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_user_sessions_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/terminate_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/update_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/update_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/get_session_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_sessions_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/list_sessions_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_user_sessions_response.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/validate_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/create_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/create_session_request.proto";' 'pkg/auth/proto/session_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/validate_session_response.proto";' 'pkg/auth/proto/session_service.proto'

# Fix imports for auth/proto/get_api_key_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/api_key.proto";' 'pkg/auth/proto/get_api_key_response.proto'
sed -i '/^import.*proto";$/a import "auth/proto/api_key_stats.proto";' 'pkg/auth/proto/get_api_key_response.proto'

# Fix imports for auth/proto/permission_grant.proto
sed -i '/^import.*proto";$/a import "auth/proto/permission_scope.proto";' 'pkg/auth/proto/permission_grant.proto'

# Fix imports for auth/proto/auth_service.proto
sed -i '/^import.*proto";$/a import "auth/proto/complete_password_reset_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/revoke_token_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/change_password_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/validate_token_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/change_password_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/refresh_token_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_user_info_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/verify_credentials_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/authenticate_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/authenticate_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/initiate_password_reset_response.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_user_info_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/complete_password_reset_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/refresh_token_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/revoke_token_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/validate_token_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/initiate_password_reset_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/authenticate_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/authenticate_request.proto";' 'pkg/auth/proto/auth_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/verify_credentials_response.proto";' 'pkg/auth/proto/auth_service.proto'

# Fix imports for auth/proto/permission.proto
sed -i '/^import.*proto";$/a import "auth/proto/scope_type.proto";' 'pkg/auth/proto/permission.proto'

# Fix imports for auth/proto/auth_admin_service.proto
sed -i '/^import.*proto";$/a import "auth/proto/get_user_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/create_role_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/remove_role_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_user_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/update_user_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/create_user_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/update_role_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_system_stats_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/update_user_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/delete_role_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_roles_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/create_user_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_users_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/update_role_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/invalidate_user_sessions_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/create_role_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/assign_role_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_users_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/list_roles_response.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/delete_user_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'
sed -i '/^import.*proto";$/a import "auth/proto/get_system_stats_request.proto";' 'pkg/auth/proto/auth_admin_service.proto'

# Fix imports for auth/proto/enable_mfa_response.proto
sed -i '/^import.*proto";$/a import "auth/proto/mfa_setup_instruction.proto";' 'pkg/auth/proto/enable_mfa_response.proto'

# Fix imports for auth/proto/resend_verification_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/verification_type.proto";' 'pkg/auth/proto/resend_verification_request.proto'

# Fix imports for auth/proto/session.proto
sed -i '/^import.*proto";$/a import "auth/proto/session_status.proto";' 'pkg/auth/proto/session.proto'

# Fix imports for auth/proto/verify2_fa_request.proto
sed -i '/^import.*proto";$/a import "auth/proto/two_fa_type.proto";' 'pkg/auth/proto/verify2_fa_request.proto'

# Fix imports for auth/proto/user_metadata.proto
sed -i '/^import.*proto";$/a import "auth/proto/verification_status.proto";' 'pkg/auth/proto/user_metadata.proto'
sed -i '/^import.*proto";$/a import "auth/proto/user_preferences.proto";' 'pkg/auth/proto/user_metadata.proto'

# Fix imports for auth/proto/permission_metadata.proto
sed -i '/^import.*proto";$/a import "auth/proto/permission_condition.proto";' 'pkg/auth/proto/permission_metadata.proto'
sed -i '/^import.*proto";$/a import "auth/proto/permission_level.proto";' 'pkg/auth/proto/permission_metadata.proto'

# Fix imports for auth/proto/o_auth2_config.proto
sed -i '/^import.*proto";$/a import "auth/proto/o_auth2_flow_type.proto";' 'pkg/auth/proto/o_auth2_config.proto'

# Fix imports for auth/proto/session_metadata.proto
sed -i '/^import.*proto";$/a import "auth/proto/session_state.proto";' 'pkg/auth/proto/session_metadata.proto'
sed -i '/^import.*proto";$/a import "web/proto/session_state.proto";' 'pkg/auth/proto/session_metadata.proto'
sed -i '/^import.*proto";$/a import "auth/proto/device_info.proto";' 'pkg/auth/proto/session_metadata.proto'
sed -i '/^import.*proto";$/a import "auth/proto/location_info.proto";' 'pkg/auth/proto/session_metadata.proto'

# Fix imports for web/proto/session_data.proto
sed -i '/^import.*proto";$/a import "auth/proto/session_state.proto";' 'pkg/web/proto/session_data.proto'
sed -i '/^import.*proto";$/a import "web/proto/session_state.proto";' 'pkg/web/proto/session_data.proto'

# Fix imports for auth/proto/user.proto
sed -i '/^import.*proto";$/a import "auth/proto/user_status.proto";' 'pkg/auth/proto/user.proto'

# Fix imports for notification/proto/get_preferences_response.proto
sed -i '/^import.*proto";$/a import "notification/proto/subscription_preferences.proto";' 'pkg/notification/proto/get_preferences_response.proto'

# Fix imports for notification/proto/update_preferences_request.proto
sed -i '/^import.*proto";$/a import "notification/proto/subscription_preferences.proto";' 'pkg/notification/proto/update_preferences_request.proto'

# Fix imports for notification/proto/event_notification.proto
sed -i '/^import.*proto";$/a import "notification/proto/notification_message.proto";' 'pkg/notification/proto/event_notification.proto'

# Fix imports for notification/proto/send_notification_request.proto
sed -i '/^import.*proto";$/a import "notification/proto/notification_message.proto";' 'pkg/notification/proto/send_notification_request.proto'

# Fix imports for notification/proto/list_notifications_response.proto
sed -i '/^import.*proto";$/a import "notification/proto/notification_message.proto";' 'pkg/notification/proto/list_notifications_response.proto'

# Fix imports for notification/proto/delivery_channel.proto
sed -i '/^import.*proto";$/a import "notification/proto/delivery_channel_type.proto";' 'pkg/notification/proto/delivery_channel.proto'

# Fix imports for notification/proto/subscription_preferences.proto
sed -i '/^import.*proto";$/a import "notification/proto/delivery_channel_type.proto";' 'pkg/notification/proto/subscription_preferences.proto'

# Fix imports for notification/proto/send_notification_response.proto
sed -i '/^import.*proto";$/a import "notification/proto/delivery_status.proto";' 'pkg/notification/proto/send_notification_response.proto'

# Fix imports for notification/proto/notification_message.proto
sed -i '/^import.*proto";$/a import "notification/proto/delivery_status.proto";' 'pkg/notification/proto/notification_message.proto'
sed -i '/^import.*proto";$/a import "notification/proto/delivery_channel.proto";' 'pkg/notification/proto/notification_message.proto'

# Fix imports for notification/proto/get_template_response.proto
sed -i '/^import.*proto";$/a import "notification/proto/template.proto";' 'pkg/notification/proto/get_template_response.proto'

# Fix imports for notification/proto/notification_service.proto
sed -i '/^import.*proto";$/a import "notification/proto/get_template_request.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/get_template_response.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/list_notifications_response.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/update_preferences_request.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/list_notifications_request.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/delete_notification_request.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/update_preferences_response.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/send_notification_response.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/mark_as_read_response.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/delete_notification_response.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/send_notification_request.proto";' 'pkg/notification/proto/notification_service.proto'
sed -i '/^import.*proto";$/a import "notification/proto/mark_as_read_request.proto";' 'pkg/notification/proto/notification_service.proto'

# Fix imports for web/proto/list_sessions_response.proto
sed -i '/^import.*proto";$/a import "web/proto/session_data.proto";' 'pkg/web/proto/list_sessions_response.proto'

# Fix imports for web/proto/get_session_response.proto
sed -i '/^import.*proto";$/a import "web/proto/session_data.proto";' 'pkg/web/proto/get_session_response.proto'

# Fix imports for web/proto/create_session_response.proto
sed -i '/^import.*proto";$/a import "web/proto/session_data.proto";' 'pkg/web/proto/create_session_response.proto'

# Fix imports for web/proto/update_session_response.proto
sed -i '/^import.*proto";$/a import "web/proto/session_data.proto";' 'pkg/web/proto/update_session_response.proto'

# Fix imports for web/proto/handler_info.proto
sed -i '/^import.*proto";$/a import "web/proto/handler_config.proto";' 'pkg/web/proto/handler_info.proto'

# Fix imports for web/proto/handler_config.proto
sed -i '/^import.*proto";$/a import "web/proto/handler_type.proto";' 'pkg/web/proto/handler_config.proto'

# Fix imports for web/proto/route_config.proto
sed -i '/^import.*proto";$/a import "web/proto/handler_type.proto";' 'pkg/web/proto/route_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/http_method.proto";' 'pkg/web/proto/route_config.proto'

# Fix imports for web/proto/start_server_response.proto
sed -i '/^import.*proto";$/a import "web/proto/server_status.proto";' 'pkg/web/proto/start_server_response.proto'

# Fix imports for web/proto/get_cache_config_response.proto
sed -i '/^import.*proto";$/a import "cache/proto/cache_config.proto";' 'pkg/web/proto/get_cache_config_response.proto'
sed -i '/^import.*proto";$/a import "web/proto/cache_config.proto";' 'pkg/web/proto/get_cache_config_response.proto'

# Fix imports for web/proto/update_cache_config_request.proto
sed -i '/^import.*proto";$/a import "cache/proto/cache_config.proto";' 'pkg/web/proto/update_cache_config_request.proto'
sed -i '/^import.*proto";$/a import "web/proto/cache_config.proto";' 'pkg/web/proto/update_cache_config_request.proto'

# Fix imports for web/proto/rate_limit_config.proto
sed -i '/^import.*proto";$/a import "web/proto/rate_limit_strategy.proto";' 'pkg/web/proto/rate_limit_config.proto'

# Fix imports for web/proto/web_admin_service.proto
sed -i '/^import.*proto";$/a import "web/proto/flush_cache_response.proto";' 'pkg/web/proto/web_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/update_cache_config_request.proto";' 'pkg/web/proto/web_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/get_cache_config_request.proto";' 'pkg/web/proto/web_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/get_cache_config_response.proto";' 'pkg/web/proto/web_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/flush_cache_request.proto";' 'pkg/web/proto/web_admin_service.proto'
sed -i '/^import.*proto";$/a import "web/proto/update_cache_config_response.proto";' 'pkg/web/proto/web_admin_service.proto'

# Fix imports for web/proto/route_info.proto
sed -i '/^import.*proto";$/a import "web/proto/route_type.proto";' 'pkg/web/proto/route_info.proto'
sed -i '/^import.*proto";$/a import "web/proto/route_config.proto";' 'pkg/web/proto/route_info.proto'

# Fix imports for web/proto/file_upload.proto
sed -i '/^import.*proto";$/a import "web/proto/mime_type.proto";' 'pkg/web/proto/file_upload.proto'

# Fix imports for web/proto/file_metadata.proto
sed -i '/^import.*proto";$/a import "web/proto/mime_type.proto";' 'pkg/web/proto/file_metadata.proto'

# Fix imports for web/proto/file_info.proto
sed -i '/^import.*proto";$/a import "web/proto/mime_type.proto";' 'pkg/web/proto/file_info.proto'

# Fix imports for web/proto/register_middleware_request.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_config.proto";' 'pkg/web/proto/register_middleware_request.proto'

# Fix imports for web/proto/update_middleware_config_request.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_config.proto";' 'pkg/web/proto/update_middleware_config_request.proto'

# Fix imports for web/proto/load_balancer_config.proto
sed -i '/^import.*proto";$/a import "web/proto/load_balance_strategy.proto";' 'pkg/web/proto/load_balancer_config.proto'

# Fix imports for web/proto/proxy_config.proto
sed -i '/^import.*proto";$/a import "web/proto/proxy_type.proto";' 'pkg/web/proto/proxy_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/http_header.proto";' 'pkg/web/proto/proxy_config.proto'

# Fix imports for web/proto/cookie_config.proto
sed -i '/^import.*proto";$/a import "web/proto/cookie_same_site.proto";' 'pkg/web/proto/cookie_config.proto'

# Fix imports for web/proto/session_config.proto
sed -i '/^import.*proto";$/a import "web/proto/cookie_same_site.proto";' 'pkg/web/proto/session_config.proto'

# Fix imports for web/proto/cookie_data.proto
sed -i '/^import.*proto";$/a import "web/proto/cookie_same_site.proto";' 'pkg/web/proto/cookie_data.proto'

# Fix imports for web/proto/register_middleware_response.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_info.proto";' 'pkg/web/proto/register_middleware_response.proto'

# Fix imports for web/proto/list_middleware_response.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_info.proto";' 'pkg/web/proto/list_middleware_response.proto'

# Fix imports for web/proto/list_middleware_request.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_type.proto";' 'pkg/web/proto/list_middleware_request.proto'

# Fix imports for web/proto/middleware_info.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_type.proto";' 'pkg/web/proto/middleware_info.proto'

# Fix imports for web/proto/middleware_config.proto
sed -i '/^import.*proto";$/a import "web/proto/middleware_type.proto";' 'pkg/web/proto/middleware_config.proto'

# Fix imports for web/proto/list_files_request.proto
sed -i '/^import.*proto";$/a import "web/proto/file_sort_order.proto";' 'pkg/web/proto/list_files_request.proto'

# Fix imports for web/proto/create_cookie_request.proto
sed -i '/^import.*proto";$/a import "web/proto/same_site_policy.proto";' 'pkg/web/proto/create_cookie_request.proto'

# Fix imports for web/proto/cache_config.proto
sed -i '/^import.*proto";$/a import "web/proto/cache_strategy.proto";' 'pkg/web/proto/cache_config.proto'

# Fix imports for web/proto/compression_config.proto
sed -i '/^import.*proto";$/a import "metrics/proto/compression_type.proto";' 'pkg/web/proto/compression_config.proto'
sed -i '/^import.*proto";$/a import "config/proto/compression_type.proto";' 'pkg/web/proto/compression_config.proto'
sed -i '/^import.*proto";$/a import "web/proto/compression_type.proto";' 'pkg/web/proto/compression_config.proto'
sed -i '/^import.*proto";$/a import "log/proto/compression_type.proto";' 'pkg/web/proto/compression_config.proto'

# Fix imports for web/proto/ssl_config.proto
sed -i '/^import.*proto";$/a import "web/proto/ssl_protocol.proto";' 'pkg/web/proto/ssl_config.proto'

# Fix imports for health/proto/watch_response.proto
sed -i '/^import.*proto";$/a import "health/proto/health_metrics.proto";' 'pkg/health/proto/watch_response.proto'
sed -i '/^import.*proto";$/a import "health/proto/check_result.proto";' 'pkg/health/proto/watch_response.proto'

# Fix imports for health/proto/health_check_response.proto
sed -i '/^import.*proto";$/a import "health/proto/health_metrics.proto";' 'pkg/health/proto/health_check_response.proto'
sed -i '/^import.*proto";$/a import "health/proto/check_result.proto";' 'pkg/health/proto/health_check_response.proto'

# Fix imports for health/proto/health_admin_service.proto
sed -i '/^import.*proto";$/a import "health/proto/reset_health_stats_request.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/set_health_response.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/enable_check_response.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/enable_check_request.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/reset_health_stats_response.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/set_health_request.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/disable_check_response.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/disable_check_request.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/configure_alerting_request.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/run_check_request.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/run_check_response.proto";' 'pkg/health/proto/health_admin_service.proto'
sed -i '/^import.*proto";$/a import "health/proto/configure_alerting_response.proto";' 'pkg/health/proto/health_admin_service.proto'

# Fix imports for health/proto/get_health_metrics_response.proto
sed -i '/^import.*proto";$/a import "health/proto/health_metric_data.proto";' 'pkg/health/proto/get_health_metrics_response.proto'

# Fix imports for health/proto/component_health.proto
sed -i '/^import.*proto";$/a import "health/proto/serving_status.proto";' 'pkg/health/proto/component_health.proto'

# Fix imports for health/proto/health_check_result.proto
sed -i '/^import.*proto";$/a import "health/proto/serving_status.proto";' 'pkg/health/proto/health_check_result.proto'
sed -i '/^import.*proto";$/a import "health/proto/check_type.proto";' 'pkg/health/proto/health_check_result.proto'
sed -i '/^import.*proto";$/a import "health/proto/component_health.proto";' 'pkg/health/proto/health_check_result.proto'

# Fix imports for health/proto/health_check_all_request.proto
sed -i '/^import.*proto";$/a import "health/proto/check_type.proto";' 'pkg/health/proto/health_check_all_request.proto'

# Fix imports for common/proto/filter_value.proto
sed -i '/^import.*proto";$/a import "common/proto/int64_array.proto";' 'pkg/common/proto/filter_value.proto'
sed -i '/^import.*proto";$/a import "common/proto/string_array.proto";' 'pkg/common/proto/filter_value.proto'
sed -i '/^import.*proto";$/a import "common/proto/filter_operation.proto";' 'pkg/common/proto/filter_value.proto'

# Fix imports for common/proto/config_value.proto
sed -i '/^import.*proto";$/a import "common/proto/value_type.proto";' 'pkg/common/proto/config_value.proto'

# Fix imports for common/proto/audit_log.proto
sed -i '/^import.*proto";$/a import "common/proto/resource_reference.proto";' 'pkg/common/proto/audit_log.proto'
sed -i '/^import.*proto";$/a import "common/proto/audit_result.proto";' 'pkg/common/proto/audit_log.proto'

# Fix imports for common/proto/request_metadata.proto
sed -i '/^import.*proto";$/a import "common/proto/client_info.proto";' 'pkg/common/proto/request_metadata.proto'

# Fix imports for common/proto/subscription_info.proto
sed -i '/^import.*proto";$/a import "common/proto/client_info.proto";' 'pkg/common/proto/subscription_info.proto'
sed -i '/^import.*proto";$/a import "common/proto/subscription_options.proto";' 'pkg/common/proto/subscription_info.proto'
sed -i '/^import.*proto";$/a import "common/proto/filter_options.proto";' 'pkg/common/proto/subscription_info.proto'
sed -i '/^import.*proto";$/a import "common/proto/subscription_status.proto";' 'pkg/common/proto/subscription_info.proto'

# Fix imports for common/proto/batch_operation.proto
sed -i '/^import.*proto";$/a import "common/proto/request_metadata.proto";' 'pkg/common/proto/batch_operation.proto'
sed -i '/^import.*proto";$/a import "metrics/proto/batch_options.proto";' 'pkg/common/proto/batch_operation.proto'
sed -i '/^import.*proto";$/a import "common/proto/batch_options.proto";' 'pkg/common/proto/batch_operation.proto'

# Fix imports for common/proto/sort_options.proto
sed -i '/^import.*proto";$/a import "common/proto/sort_direction.proto";' 'pkg/common/proto/sort_options.proto'

# Fix imports for common/proto/subscription_options.proto
sed -i '/^import.*proto";$/a import "common/proto/ack_mode.proto";' 'pkg/common/proto/subscription_options.proto'

# Fix imports for common/proto/circuit_breaker_config.proto
sed -i '/^import.*proto";$/a import "common/proto/circuit_breaker_state.proto";' 'pkg/common/proto/circuit_breaker_config.proto'

# Fix imports for common/proto/error.proto
sed -i '/^import.*proto";$/a import "common/proto/error_code.proto";' 'pkg/common/proto/error.proto'

# Fix imports for common/proto/retry_policy.proto
sed -i '/^import.*proto";$/a import "common/proto/error_code.proto";' 'pkg/common/proto/retry_policy.proto'

# Fix imports for common/proto/cache_policy.proto
sed -i '/^import.*proto";$/a import "common/proto/expiration_policy.proto";' 'pkg/common/proto/cache_policy.proto'
sed -i '/^import.*proto";$/a import "common/proto/eviction_policy.proto";' 'pkg/common/proto/cache_policy.proto'

# Fix imports for queue/proto/pull_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/received_message.proto";' 'pkg/queue/proto/pull_response.proto'

# Fix imports for queue/proto/batch_publish_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/publish_result.proto";' 'pkg/queue/proto/batch_publish_response.proto'

# Fix imports for queue/proto/historical_stats.proto
sed -i '/^import.*proto";$/a import "queue/proto/historical_data_point.proto";' 'pkg/queue/proto/historical_stats.proto'

# Fix imports for queue/proto/age_distribution.proto
sed -i '/^import.*proto";$/a import "queue/proto/age_bucket.proto";' 'pkg/queue/proto/age_distribution.proto'

# Fix imports for queue/proto/queue_stats_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/messages/queue_stats.proto";' 'pkg/queue/proto/queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_stats_point.proto";' 'pkg/queue/proto/queue_stats_response.proto'

# Fix imports for queue/proto/queue_stats_point.proto
sed -i '/^import.*proto";$/a import "queue/proto/messages/queue_stats.proto";' 'pkg/queue/proto/queue_stats_point.proto'

# Fix imports for queue/proto/consumer.proto
sed -i '/^import.*proto";$/a import "queue/proto/consumer_stats.proto";' 'pkg/queue/proto/consumer.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer_config.proto";' 'pkg/queue/proto/consumer.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer_client.proto";' 'pkg/queue/proto/consumer.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer_state.proto";' 'pkg/queue/proto/consumer.proto'

# Fix imports for queue/proto/publish_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/retry_config.proto";' 'pkg/queue/proto/publish_config.proto'

# Fix imports for queue/proto/external_auth_service.proto
sed -i '/^import.*proto";$/a import "queue/proto/retry_config.proto";' 'pkg/queue/proto/external_auth_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/auth_cache_config.proto";' 'pkg/queue/proto/external_auth_service.proto'

# Fix imports for queue/proto/stream_messages_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/ack_level.proto";' 'pkg/queue/proto/stream_messages_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/stream_config.proto";' 'pkg/queue/proto/stream_messages_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/message_filter.proto";' 'pkg/queue/proto/stream_messages_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/offset_config.proto";' 'pkg/queue/proto/stream_messages_request.proto'

# Fix imports for queue/proto/subscription_configuration.proto
sed -i '/^import.*proto";$/a import "queue/proto/ack_level.proto";' 'pkg/queue/proto/subscription_configuration.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delivery_mode.proto";' 'pkg/queue/proto/subscription_configuration.proto'

# Fix imports for queue/proto/update_subscription_config_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/subscription_config_update.proto";' 'pkg/queue/proto/update_subscription_config_request.proto'

# Fix imports for queue/proto/commit_offset_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/partition_commit_result.proto";' 'pkg/queue/proto/commit_offset_response.proto'

# Fix imports for queue/proto/batch_ack_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/failed_ack.proto";' 'pkg/queue/proto/batch_ack_response.proto'

# Fix imports for queue/proto/read_consistency.proto
sed -i '/^import.*proto";$/a import "queue/proto/read_retry_config.proto";' 'pkg/queue/proto/read_consistency.proto'
sed -i '/^import.*proto";$/a import "queue/proto/read_level.proto";' 'pkg/queue/proto/read_consistency.proto'

# Fix imports for queue/proto/flush_queue_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/flush_policy.proto";' 'pkg/queue/proto/flush_queue_request.proto'

# Fix imports for queue/proto/create_subscription_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/subscription_config.proto";' 'pkg/queue/proto/create_subscription_request.proto'

# Fix imports for queue/proto/message_properties.proto
sed -i '/^import.*proto";$/a import "queue/proto/priority_level.proto";' 'pkg/queue/proto/message_properties.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delivery_mode.proto";' 'pkg/queue/proto/message_properties.proto'

# Fix imports for queue/proto/subscription_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/priority_level.proto";' 'pkg/queue/proto/subscription_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delivery_options.proto";' 'pkg/queue/proto/subscription_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/subscription_state.proto";' 'pkg/queue/proto/subscription_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/routing_strategy.proto";' 'pkg/queue/proto/subscription_config.proto'

# Fix imports for queue/proto/routing_rule.proto
sed -i '/^import.*proto";$/a import "queue/proto/routing_condition.proto";' 'pkg/queue/proto/routing_rule.proto'

# Fix imports for queue/proto/validation_error.proto
sed -i '/^import.*proto";$/a import "queue/proto/offset_range.proto";' 'pkg/queue/proto/validation_error.proto'

# Fix imports for queue/proto/restore_error.proto
sed -i '/^import.*proto";$/a import "queue/proto/offset_range.proto";' 'pkg/queue/proto/restore_error.proto'

# Fix imports for queue/proto/authorization_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/permission_rule.proto";' 'pkg/queue/proto/authorization_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/role_based_access_control.proto";' 'pkg/queue/proto/authorization_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/external_auth_service.proto";' 'pkg/queue/proto/authorization_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/jwt_auth.proto";' 'pkg/queue/proto/authorization_config.proto'

# Fix imports for queue/proto/replication_consistency.proto
sed -i '/^import.*proto";$/a import "queue/proto/replication_level.proto";' 'pkg/queue/proto/replication_consistency.proto'

# Fix imports for queue/proto/conflict_detection.proto
sed -i '/^import.*proto";$/a import "queue/proto/conflict_strategy.proto";' 'pkg/queue/proto/conflict_detection.proto'
sed -i '/^import.*proto";$/a import "queue/proto/vector_clock_config.proto";' 'pkg/queue/proto/conflict_detection.proto'
sed -i '/^import.*proto";$/a import "queue/proto/timestamp_config.proto";' 'pkg/queue/proto/conflict_detection.proto'

# Fix imports for queue/proto/acknowledge_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/message_ack_result.proto";' 'pkg/queue/proto/acknowledge_response.proto'

# Fix imports for queue/proto/update_topic_config_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/topic_config.proto";' 'pkg/queue/proto/update_topic_config_request.proto'

# Fix imports for queue/proto/queue_service.proto
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_info_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/publish_response.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/subscribe_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/subscribe_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/dequeue_response.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/enqueue_response.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/peek_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/dequeue_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_stats_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "cache/proto/publish_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/publish_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_info_response.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_stats_response.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/subscribe_response.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/enqueue_request.proto";' 'pkg/queue/proto/queue_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/peek_response.proto";' 'pkg/queue/proto/queue_service.proto'

# Fix imports for queue/proto/queue_admin_service.proto
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_info_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/get_queue_info_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/create_queue_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/reset_queue_stats_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/pause_queue_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/resume_queue_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/purge_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delete_topic_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/purge_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delete_topic_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/reset_queue_stats_request.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/resume_queue_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/pause_queue_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/create_queue_response.proto";' 'pkg/queue/proto/queue_admin_service.proto'

# Fix imports for queue/proto/list_subscriptions_response.proto
sed -i '/^import.*proto";$/a import "common/proto/subscription_info.proto";' 'pkg/queue/proto/list_subscriptions_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/subscription_info.proto";' 'pkg/queue/proto/list_subscriptions_response.proto'

# Fix imports for queue/proto/send_message_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/delivery_options.proto";' 'pkg/queue/proto/send_message_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_message.proto";' 'pkg/queue/proto/send_message_request.proto'

# Fix imports for queue/proto/publish_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/delivery_options.proto";' 'pkg/queue/proto/publish_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_message.proto";' 'pkg/queue/proto/publish_request.proto'

# Fix imports for queue/proto/subscribe_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/queue_message.proto";' 'pkg/queue/proto/subscribe_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/connection_details.proto";' 'pkg/queue/proto/subscribe_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/partition_offset.proto";' 'pkg/queue/proto/subscribe_response.proto'

# Fix imports for queue/proto/list_messages_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/queue_message.proto";' 'pkg/queue/proto/list_messages_response.proto'

# Fix imports for queue/proto/message_filter_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/content_filter.proto";' 'pkg/queue/proto/message_filter_config.proto'

# Fix imports for queue/proto/consumer_group.proto
sed -i '/^import.*proto";$/a import "queue/proto/consumer_group_stats.proto";' 'pkg/queue/proto/consumer_group.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer_group_config.proto";' 'pkg/queue/proto/consumer_group.proto'
sed -i '/^import.*proto";$/a import "queue/proto/group_coordinator.proto";' 'pkg/queue/proto/consumer_group.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer_group_state.proto";' 'pkg/queue/proto/consumer_group.proto'
sed -i '/^import.*proto";$/a import "queue/proto/consumer.proto";' 'pkg/queue/proto/consumer_group.proto'
sed -i '/^import.*proto";$/a import "queue/proto/partition_assignment.proto";' 'pkg/queue/proto/consumer_group.proto'

# Fix imports for queue/proto/get_node_info_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/node_info.proto";' 'pkg/queue/proto/get_node_info_response.proto'

# Fix imports for queue/proto/get_partition_info_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/partition_info.proto";' 'pkg/queue/proto/get_partition_info_response.proto'

# Fix imports for queue/proto/list_queues_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/queue_info.proto";' 'pkg/queue/proto/list_queues_response.proto'

# Fix imports for queue/proto/get_queue_info_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/queue_info.proto";' 'pkg/queue/proto/get_queue_info_response.proto'

# Fix imports for queue/proto/update_message_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/failed_field_update.proto";' 'pkg/queue/proto/update_message_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/updated_properties.proto";' 'pkg/queue/proto/update_message_response.proto'

# Fix imports for queue/proto/resume_queue_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/queue_state.proto";' 'pkg/queue/proto/resume_queue_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/resume_stats.proto";' 'pkg/queue/proto/resume_queue_response.proto'

# Fix imports for queue/proto/list_topics_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/topic_info.proto";' 'pkg/queue/proto/list_topics_response.proto'

# Fix imports for queue/proto/reset_queue_stats_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/reset_details.proto";' 'pkg/queue/proto/reset_queue_stats_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/preserved_stats.proto";' 'pkg/queue/proto/reset_queue_stats_response.proto'

# Fix imports for queue/proto/routing_condition.proto
sed -i '/^import.*proto";$/a import "queue/proto/priority_range.proto";' 'pkg/queue/proto/routing_condition.proto'
sed -i '/^import.*proto";$/a import "queue/proto/size_range.proto";' 'pkg/queue/proto/routing_condition.proto'

# Fix imports for queue/proto/push_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/messages/message.proto";' 'pkg/queue/proto/push_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/batch_settings.proto";' 'pkg/queue/proto/push_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/publish_config.proto";' 'pkg/queue/proto/push_request.proto'

# Fix imports for queue/proto/subscribe_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/subscription_configuration.proto";' 'pkg/queue/proto/subscribe_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/error_handling_config.proto";' 'pkg/queue/proto/subscribe_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delivery_configuration.proto";' 'pkg/queue/proto/subscribe_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/message_filter_config.proto";' 'pkg/queue/proto/subscribe_request.proto'

# Fix imports for queue/proto/get_partition_info_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/time_range_filter.proto";' 'pkg/queue/proto/get_partition_info_request.proto'

# Fix imports for queue/proto/get_queue_info_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/time_range_filter.proto";' 'pkg/queue/proto/get_queue_info_request.proto'

# Fix imports for queue/proto/error_handling_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/dead_letter_queue_config.proto";' 'pkg/queue/proto/error_handling_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/error_notification_config.proto";' 'pkg/queue/proto/error_handling_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/error_action_config.proto";' 'pkg/queue/proto/error_handling_config.proto'

# Fix imports for queue/proto/consumer_group_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/dead_letter_queue_config.proto";' 'pkg/queue/proto/consumer_group_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/offset_reset_strategy.proto";' 'pkg/queue/proto/consumer_group_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/load_balancing_strategy.proto";' 'pkg/queue/proto/consumer_group_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/rebalance_strategy.proto";' 'pkg/queue/proto/consumer_group_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/auto_commit_config.proto";' 'pkg/queue/proto/consumer_group_config.proto'

# Fix imports for queue/proto/ordering_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/ordering_level.proto";' 'pkg/queue/proto/ordering_config.proto'

# Fix imports for queue/proto/conflict_resolution.proto
sed -i '/^import.*proto";$/a import "queue/proto/custom_resolution.proto";' 'pkg/queue/proto/conflict_resolution.proto'
sed -i '/^import.*proto";$/a import "queue/proto/last_writer_wins.proto";' 'pkg/queue/proto/conflict_resolution.proto'
sed -i '/^import.*proto";$/a import "queue/proto/multi_value_config.proto";' 'pkg/queue/proto/conflict_resolution.proto'
sed -i '/^import.*proto";$/a import "queue/proto/resolution_strategy.proto";' 'pkg/queue/proto/conflict_resolution.proto'

# Fix imports for queue/proto/partition_restore_result.proto
sed -i '/^import.*proto";$/a import "queue/proto/restore_error.proto";' 'pkg/queue/proto/partition_restore_result.proto'

# Fix imports for queue/proto/anti_affinity_rule.proto
sed -i '/^import.*proto";$/a import "queue/proto/anti_affinity_scope.proto";' 'pkg/queue/proto/anti_affinity_rule.proto'

# Fix imports for queue/proto/consumer_group_stats.proto
sed -i '/^import.*proto";$/a import "queue/proto/consumer_error_stats.proto";' 'pkg/queue/proto/consumer_group_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/rebalance_stats.proto";' 'pkg/queue/proto/consumer_group_stats.proto'

# Fix imports for queue/proto/format_options.proto
sed -i '/^import.*proto";$/a import "queue/proto/compression_algorithm.proto";' 'pkg/queue/proto/format_options.proto'

# Fix imports for queue/proto/serialization_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/compression_algorithm.proto";' 'pkg/queue/proto/serialization_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/format_options.proto";' 'pkg/queue/proto/serialization_config.proto'

# Fix imports for queue/proto/batch_nack_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/message_nack.proto";' 'pkg/queue/proto/batch_nack_request.proto'

# Fix imports for queue/proto/write_consistency.proto
sed -i '/^import.*proto";$/a import "queue/proto/conflict_detection.proto";' 'pkg/queue/proto/write_consistency.proto'
sed -i '/^import.*proto";$/a import "queue/proto/sync_replication.proto";' 'pkg/queue/proto/write_consistency.proto'
sed -i '/^import.*proto";$/a import "queue/proto/write_retry_config.proto";' 'pkg/queue/proto/write_consistency.proto'
sed -i '/^import.*proto";$/a import "queue/proto/write_level.proto";' 'pkg/queue/proto/write_consistency.proto'

# Fix imports for queue/proto/retry_policy.proto
sed -i '/^import.*proto";$/a import "queue/proto/retry_delay_strategy.proto";' 'pkg/queue/proto/retry_policy.proto'

# Fix imports for queue/proto/size_distribution.proto
sed -i '/^import.*proto";$/a import "queue/proto/size_bucket.proto";' 'pkg/queue/proto/size_distribution.proto'

# Fix imports for queue/proto/nack_error.proto
sed -i '/^import.*proto";$/a import "queue/proto/nack_error_category.proto";' 'pkg/queue/proto/nack_error.proto'

# Fix imports for queue/proto/message_nack.proto
sed -i '/^import.*proto";$/a import "queue/proto/nack_error_category.proto";' 'pkg/queue/proto/message_nack.proto'

# Fix imports for queue/proto/update_message_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/priority_update.proto";' 'pkg/queue/proto/update_message_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/update_condition.proto";' 'pkg/queue/proto/update_message_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/visibility_update.proto";' 'pkg/queue/proto/update_message_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/content_update.proto";' 'pkg/queue/proto/update_message_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/message_update_properties.proto";' 'pkg/queue/proto/update_message_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/metadata_update.proto";' 'pkg/queue/proto/update_message_request.proto'

# Fix imports for queue/proto/get_queue_health_response.proto
sed -i '/^import.*proto";$/a import "queue/proto/queue_health.proto";' 'pkg/queue/proto/get_queue_health_response.proto'
sed -i '/^import.*proto";$/a import "queue/proto/cluster_health.proto";' 'pkg/queue/proto/get_queue_health_response.proto'

# Fix imports for queue/proto/workflow_service.proto
sed -i '/^import.*proto";$/a import "queue/proto/stop_workflow_request.proto";' 'pkg/queue/proto/workflow_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/start_workflow_response.proto";' 'pkg/queue/proto/workflow_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/start_workflow_request.proto";' 'pkg/queue/proto/workflow_service.proto'
sed -i '/^import.*proto";$/a import "queue/proto/stop_workflow_response.proto";' 'pkg/queue/proto/workflow_service.proto'

# Fix imports for queue/proto/load_balancing_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/load_balancing_strategy.proto";' 'pkg/queue/proto/load_balancing_config.proto'

# Fix imports for queue/proto/restore_queue_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/restore_config.proto";' 'pkg/queue/proto/restore_queue_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/backup_source.proto";' 'pkg/queue/proto/restore_queue_request.proto'
sed -i '/^import.*proto";$/a import "queue/proto/restore_options.proto";' 'pkg/queue/proto/restore_queue_request.proto'

# Fix imports for queue/proto/delivery_configuration.proto
sed -i '/^import.*proto";$/a import "queue/proto/batch_delivery_config.proto";' 'pkg/queue/proto/delivery_configuration.proto'
sed -i '/^import.*proto";$/a import "queue/proto/flow_control_settings.proto";' 'pkg/queue/proto/delivery_configuration.proto'
sed -i '/^import.*proto";$/a import "queue/proto/delivery_retry_config.proto";' 'pkg/queue/proto/delivery_configuration.proto'

# Fix imports for queue/proto/nack_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/nack_error.proto";' 'pkg/queue/proto/nack_request.proto'

# Fix imports for queue/proto/offset_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/offset_type.proto";' 'pkg/queue/proto/offset_config.proto'

# Fix imports for queue/proto/get_offset_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/offset_type.proto";' 'pkg/queue/proto/get_offset_request.proto'

# Fix imports for queue/proto/purge_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/purge_options.proto";' 'pkg/queue/proto/purge_request.proto'

# Fix imports for queue/proto/role_based_access_control.proto
sed -i '/^import.*proto";$/a import "queue/proto/external_role_provider.proto";' 'pkg/queue/proto/role_based_access_control.proto'
sed -i '/^import.*proto";$/a import "queue/proto/role_inheritance.proto";' 'pkg/queue/proto/role_based_access_control.proto'

# Fix imports for queue/proto/delete_request.proto
sed -i '/^import.*proto";$/a import "queue/proto/delete_criteria.proto";' 'pkg/queue/proto/delete_request.proto'

# Fix imports for queue/proto/routing_key.proto
sed -i '/^import.*proto";$/a import "queue/proto/routing_pattern.proto";' 'pkg/queue/proto/routing_key.proto'

# Fix imports for queue/proto/error_stats.proto
sed -i '/^import.*proto";$/a import "queue/proto/error_type_stat.proto";' 'pkg/queue/proto/error_stats.proto'

# Fix imports for queue/proto/authentication_config.proto
sed -i '/^import.*proto";$/a import "queue/proto/api_key_auth.proto";' 'pkg/queue/proto/authentication_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/sasl_auth.proto";' 'pkg/queue/proto/authentication_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/username_password_auth.proto";' 'pkg/queue/proto/authentication_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/tls_auth.proto";' 'pkg/queue/proto/authentication_config.proto'
sed -i '/^import.*proto";$/a import "queue/proto/o_auth2_auth.proto";' 'pkg/queue/proto/authentication_config.proto'

# Fix imports for queue/proto/node_info.proto
sed -i '/^import.*proto";$/a import "queue/proto/node_state.proto";' 'pkg/queue/proto/node_info.proto'
sed -i '/^import.*proto";$/a import "queue/proto/node_stats.proto";' 'pkg/queue/proto/node_info.proto'

# Fix imports for queue/proto/group_coordinator.proto
sed -i '/^import.*proto";$/a import "queue/proto/coordinator_state.proto";' 'pkg/queue/proto/group_coordinator.proto'

# Fix imports for queue/proto/validation_result.proto
sed -i '/^import.*proto";$/a import "queue/proto/schema_validation.proto";' 'pkg/queue/proto/validation_result.proto'
sed -i '/^import.*proto";$/a import "queue/proto/validation_error.proto";' 'pkg/queue/proto/validation_result.proto'
sed -i '/^import.*proto";$/a import "queue/proto/integrity_validation.proto";' 'pkg/queue/proto/validation_result.proto'
sed -i '/^import.*proto";$/a import "queue/proto/checksum_validation.proto";' 'pkg/queue/proto/validation_result.proto'

# Fix imports for queue/proto/backup_source.proto
sed -i '/^import.*proto";$/a import "queue/proto/encryption_info.proto";' 'pkg/queue/proto/backup_source.proto'
sed -i '/^import.*proto";$/a import "queue/proto/original_queue_info.proto";' 'pkg/queue/proto/backup_source.proto'

# Fix imports for queue/proto/acknowledgment.proto
sed -i '/^import.*proto";$/a import "queue/proto/ack_type.proto";' 'pkg/queue/proto/acknowledgment.proto'

# Fix imports for queue/proto/messages/queue_stats.proto
sed -i '/^import.*proto";$/a import "queue/proto/age_distribution.proto";' 'pkg/queue/proto/messages/queue_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_configuration.proto";' 'pkg/queue/proto/messages/queue_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/size_distribution.proto";' 'pkg/queue/proto/messages/queue_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/queue_depth_sample.proto";' 'pkg/queue/proto/messages/queue_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/latency_metrics.proto";' 'pkg/queue/proto/messages/queue_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/throughput_metrics.proto";' 'pkg/queue/proto/messages/queue_stats.proto'
sed -i '/^import.*proto";$/a import "queue/proto/message_state_counts.proto";' 'pkg/queue/proto/messages/queue_stats.proto'

# Fix imports for queue/proto/messages/message.proto
sed -i '/^import.*proto";$/a import "queue/proto/message_properties.proto";' 'pkg/queue/proto/messages/message.proto'
sed -i '/^import.*proto";$/a import "queue/proto/message_metadata.proto";' 'pkg/queue/proto/messages/message.proto'
sed -i '/^import.*proto";$/a import "queue/proto/routing_info.proto";' 'pkg/queue/proto/messages/message.proto'

# Fix imports for db/proto/execute_batch_request.proto
sed -i '/^import.*proto";$/a import "db/proto/batch_execute_options.proto";' 'pkg/db/proto/execute_batch_request.proto'
sed -i '/^import.*proto";$/a import "common/proto/batch_operation.proto";' 'pkg/db/proto/execute_batch_request.proto'
sed -i '/^import.*proto";$/a import "db/proto/batch_operation.proto";' 'pkg/db/proto/execute_batch_request.proto'

# Fix imports for db/proto/execute_response.proto
sed -i '/^import.*proto";$/a import "db/proto/execute_stats.proto";' 'pkg/db/proto/execute_response.proto'

# Fix imports for db/proto/query_options.proto
sed -i '/^import.*proto";$/a import "queue/proto/consistency_level.proto";' 'pkg/db/proto/query_options.proto'
sed -i '/^import.*proto";$/a import "db/proto/consistency_level.proto";' 'pkg/db/proto/query_options.proto'

# Fix imports for db/proto/get_database_info_response.proto
sed -i '/^import.*proto";$/a import "db/proto/database_info.proto";' 'pkg/db/proto/get_database_info_response.proto'

# Fix imports for db/proto/get_connection_info_response.proto
sed -i '/^import.*proto";$/a import "db/proto/database_info.proto";' 'pkg/db/proto/get_connection_info_response.proto'
sed -i '/^import.*proto";$/a import "db/proto/connection_pool_info.proto";' 'pkg/db/proto/get_connection_info_response.proto'

# Fix imports for db/proto/database_admin_service.proto
sed -i '/^import.*proto";$/a import "db/proto/list_databases_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/drop_schema_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/create_schema_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/list_databases_response.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/get_database_info_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/get_database_info_response.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/create_schema_response.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/create_database_response.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/list_schemas_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/drop_database_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/create_database_request.proto";' 'pkg/db/proto/database_admin_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/list_schemas_response.proto";' 'pkg/db/proto/database_admin_service.proto'

# Fix imports for db/proto/connection_pool_info.proto
sed -i '/^import.*proto";$/a import "db/proto/pool_stats.proto";' 'pkg/db/proto/connection_pool_info.proto'

# Fix imports for db/proto/run_migration_request.proto
sed -i '/^import.*proto";$/a import "db/proto/migration_script.proto";' 'pkg/db/proto/run_migration_request.proto'

# Fix imports for db/proto/migration_service.proto
sed -i '/^import.*proto";$/a import "db/proto/list_migrations_response.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/revert_migration_response.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/run_migration_request.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/get_migration_status_request.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/list_migrations_request.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/run_migration_response.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/revert_migration_request.proto";' 'pkg/db/proto/migration_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/get_migration_status_response.proto";' 'pkg/db/proto/migration_service.proto'

# Fix imports for db/proto/transaction_service.proto
sed -i '/^import.*proto";$/a import "db/proto/begin_transaction_request.proto";' 'pkg/db/proto/transaction_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/transaction_status_response.proto";' 'pkg/db/proto/transaction_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/begin_transaction_response.proto";' 'pkg/db/proto/transaction_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/transaction_status_request.proto";' 'pkg/db/proto/transaction_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/rollback_transaction_request.proto";' 'pkg/db/proto/transaction_service.proto'
sed -i '/^import.*proto";$/a import "db/proto/commit_transaction_request.proto";' 'pkg/db/proto/transaction_service.proto'

# Fix imports for db/proto/list_migrations_response.proto
sed -i '/^import.*proto";$/a import "db/proto/migration_info.proto";' 'pkg/db/proto/list_migrations_response.proto'

# Fix imports for db/proto/batch_operation.proto
sed -i '/^import.*proto";$/a import "db/proto/query_parameter.proto";' 'pkg/db/proto/batch_operation.proto'

# Fix imports for db/proto/execute_request.proto
sed -i '/^import.*proto";$/a import "db/proto/query_parameter.proto";' 'pkg/db/proto/execute_request.proto'
sed -i '/^import.*proto";$/a import "db/proto/execute_options.proto";' 'pkg/db/proto/execute_request.proto'

# Fix imports for db/proto/query_request.proto
sed -i '/^import.*proto";$/a import "db/proto/query_parameter.proto";' 'pkg/db/proto/query_request.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_options.proto";' 'pkg/db/proto/query_request.proto'

# Fix imports for db/proto/query_row_request.proto
sed -i '/^import.*proto";$/a import "db/proto/query_parameter.proto";' 'pkg/db/proto/query_row_request.proto'
sed -i '/^import.*proto";$/a import "db/proto/query_options.proto";' 'pkg/db/proto/query_row_request.proto'

# Fix imports for db/proto/begin_transaction_request.proto
sed -i '/^import.*proto";$/a import "db/proto/transaction_options.proto";' 'pkg/db/proto/begin_transaction_request.proto'

# Fix imports for db/proto/result_set.proto
sed -i '/^import.*proto";$/a import "db/proto/row.proto";' 'pkg/db/proto/result_set.proto'
sed -i '/^import.*proto";$/a import "db/proto/column_metadata.proto";' 'pkg/db/proto/result_set.proto'

# Fix imports for db/proto/database_status.proto
sed -i '/^import.*proto";$/a import "db/proto/database_status_code.proto";' 'pkg/db/proto/database_status.proto'

# Fix imports for log/proto/log_admin_service.proto
sed -i '/^import.*proto";$/a import "log/proto/configure_logger_response.proto";' 'pkg/log/proto/log_admin_service.proto'
sed -i '/^import.*proto";$/a import "log/proto/configure_logger_request.proto";' 'pkg/log/proto/log_admin_service.proto'

# Fix imports for log/proto/read_logs_response.proto
sed -i '/^import.*proto";$/a import "log/proto/log_entry.proto";' 'pkg/log/proto/read_logs_response.proto'

# Fix imports for log/proto/appender_config.proto
sed -i '/^import.*proto";$/a import "log/proto/formatter_type.proto";' 'pkg/log/proto/appender_config.proto'
sed -i '/^import.*proto";$/a import "log/proto/appender_type.proto";' 'pkg/log/proto/appender_config.proto'
sed -i '/^import.*proto";$/a import "log/proto/formatter_config.proto";' 'pkg/log/proto/appender_config.proto'
sed -i '/^import.*proto";$/a import "log/proto/output_config.proto";' 'pkg/log/proto/appender_config.proto'

# Fix imports for log/proto/formatter_config.proto
sed -i '/^import.*proto";$/a import "log/proto/formatter_type.proto";' 'pkg/log/proto/formatter_config.proto'

# Fix imports for log/proto/logger_config.proto
sed -i '/^import.*proto";$/a import "log/proto/appender_config.proto";' 'pkg/log/proto/logger_config.proto'
sed -i '/^import.*proto";$/a import "log/proto/log_level.proto";' 'pkg/log/proto/logger_config.proto'

# Fix imports for log/proto/log_entry.proto
sed -i '/^import.*proto";$/a import "log/proto/log_level.proto";' 'pkg/log/proto/log_entry.proto'
sed -i '/^import.*proto";$/a import "log/proto/source_location.proto";' 'pkg/log/proto/log_entry.proto'
sed -i '/^import.*proto";$/a import "log/proto/error_info.proto";' 'pkg/log/proto/log_entry.proto'

# Fix imports for log/proto/log_service.proto
sed -i '/^import.*proto";$/a import "log/proto/read_logs_request.proto";' 'pkg/log/proto/log_service.proto'
sed -i '/^import.*proto";$/a import "log/proto/write_log_request.proto";' 'pkg/log/proto/log_service.proto'
sed -i '/^import.*proto";$/a import "log/proto/read_logs_response.proto";' 'pkg/log/proto/log_service.proto'
sed -i '/^import.*proto";$/a import "log/proto/write_log_response.proto";' 'pkg/log/proto/log_service.proto'

# Fix imports for media/proto/media_metadata.proto
sed -i '/^import.*proto";$/a import "media/proto/series_info.proto";' 'pkg/media/proto/media_metadata.proto'
sed -i '/^import.*proto";$/a import "media/proto/movie_info.proto";' 'pkg/media/proto/media_metadata.proto'

# Fix imports for media/proto/media_quality.proto
sed -i '/^import.*proto";$/a import "media/proto/quality_score.proto";' 'pkg/media/proto/media_quality.proto'
sed -i '/^import.*proto";$/a import "media/proto/resolution.proto";' 'pkg/media/proto/media_quality.proto'

# Fix imports for media/proto/media_file.proto
sed -i '/^import.*proto";$/a import "media/proto/audio_track.proto";' 'pkg/media/proto/media_file.proto'
sed -i '/^import.*proto";$/a import "media/proto/media_metadata.proto";' 'pkg/media/proto/media_file.proto'
sed -i '/^import.*proto";$/a import "media/proto/media_type.proto";' 'pkg/media/proto/media_file.proto'
sed -i '/^import.*proto";$/a import "media/proto/subtitle_track.proto";' 'pkg/media/proto/media_file.proto'
sed -i '/^import.*proto";$/a import "media/proto/media_quality.proto";' 'pkg/media/proto/media_file.proto'
