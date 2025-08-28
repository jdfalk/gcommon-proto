from gcommon.v1.common import environment_status_pb2 as _environment_status_pb2
from gcommon.v1.common import environment_type_pb2 as _environment_type_pb2
from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from gcommon.v1.common import organization_access_control_pb2 as _organization_access_control_pb2
from gcommon.v1.common import organization_compliance_settings_pb2 as _organization_compliance_settings_pb2
from gcommon.v1.common import organization_notification_settings_pb2 as _organization_notification_settings_pb2
from gcommon.v1.common import organization_resource_limits_pb2 as _organization_resource_limits_pb2
from gcommon.v1.common import retention_policy_pb2 as _retention_policy_pb2
from gcommon.v1.config import approval_workflow_pb2 as _approval_workflow_pb2
from gcommon.v1.config import audit_settings_pb2 as _audit_settings_pb2
from gcommon.v1.config import backup_policy_pb2 as _backup_policy_pb2
from gcommon.v1.config import deployment_info_pb2 as _deployment_info_pb2
from gcommon.v1.config import encryption_settings_pb2 as _encryption_settings_pb2
from gcommon.v1.config import monitoring_config_pb2 as _monitoring_config_pb2
from gcommon.v1.config import promotion_rule_pb2 as _promotion_rule_pb2
from gcommon.v1.config import sync_settings_pb2 as _sync_settings_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigEnvironment(_message.Message):
    __slots__ = ("environment_id", "name", "description", "type", "status", "created_at", "updated_at", "owner", "tags", "metadata", "config", "secrets", "variables", "parent_environment_id", "child_environment_ids", "promotion_rules", "access_controls", "deployment_info", "health_status", "resource_limits", "backup_policy", "approval_workflow", "monitoring_config", "retention_policy", "compliance_settings", "encryption_settings", "audit_settings", "notification_settings", "sync_settings", "version")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SecretsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VariablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_ENVIRONMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_RULES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SYNC_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    name: str
    description: str
    type: _environment_type_pb2.EnvironmentType
    status: _environment_status_pb2.EnvironmentStatus
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    config: _containers.ScalarMap[str, str]
    secrets: _containers.ScalarMap[str, str]
    variables: _containers.ScalarMap[str, str]
    parent_environment_id: str
    child_environment_ids: _containers.RepeatedScalarFieldContainer[str]
    promotion_rules: _containers.RepeatedCompositeFieldContainer[_promotion_rule_pb2.PromotionRule]
    access_controls: _containers.RepeatedCompositeFieldContainer[_organization_access_control_pb2.OrganizationAccessControl]
    deployment_info: _deployment_info_pb2.DeploymentInfo
    health_status: _health_status_pb2.CommonHealthStatus
    resource_limits: _organization_resource_limits_pb2.OrganizationResourceLimits
    backup_policy: _backup_policy_pb2.BackupPolicy
    approval_workflow: _approval_workflow_pb2.ApprovalWorkflow
    monitoring_config: _monitoring_config_pb2.ConfigMonitoringConfig
    retention_policy: _retention_policy_pb2.MetricsRetentionPolicy
    compliance_settings: _organization_compliance_settings_pb2.OrganizationComplianceSettings
    encryption_settings: _encryption_settings_pb2.EncryptionSettings
    audit_settings: _audit_settings_pb2.AuditSettings
    notification_settings: _organization_notification_settings_pb2.OrganizationNotificationSettings
    sync_settings: _sync_settings_pb2.SyncSettings
    version: str
    def __init__(self, environment_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_environment_type_pb2.EnvironmentType, str]] = ..., status: _Optional[_Union[_environment_status_pb2.EnvironmentStatus, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., owner: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., config: _Optional[_Mapping[str, str]] = ..., secrets: _Optional[_Mapping[str, str]] = ..., variables: _Optional[_Mapping[str, str]] = ..., parent_environment_id: _Optional[str] = ..., child_environment_ids: _Optional[_Iterable[str]] = ..., promotion_rules: _Optional[_Iterable[_Union[_promotion_rule_pb2.PromotionRule, _Mapping]]] = ..., access_controls: _Optional[_Iterable[_Union[_organization_access_control_pb2.OrganizationAccessControl, _Mapping]]] = ..., deployment_info: _Optional[_Union[_deployment_info_pb2.DeploymentInfo, _Mapping]] = ..., health_status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., resource_limits: _Optional[_Union[_organization_resource_limits_pb2.OrganizationResourceLimits, _Mapping]] = ..., backup_policy: _Optional[_Union[_backup_policy_pb2.BackupPolicy, _Mapping]] = ..., approval_workflow: _Optional[_Union[_approval_workflow_pb2.ApprovalWorkflow, _Mapping]] = ..., monitoring_config: _Optional[_Union[_monitoring_config_pb2.ConfigMonitoringConfig, _Mapping]] = ..., retention_policy: _Optional[_Union[_retention_policy_pb2.MetricsRetentionPolicy, str]] = ..., compliance_settings: _Optional[_Union[_organization_compliance_settings_pb2.OrganizationComplianceSettings, _Mapping]] = ..., encryption_settings: _Optional[_Union[_encryption_settings_pb2.EncryptionSettings, _Mapping]] = ..., audit_settings: _Optional[_Union[_audit_settings_pb2.AuditSettings, _Mapping]] = ..., notification_settings: _Optional[_Union[_organization_notification_settings_pb2.OrganizationNotificationSettings, _Mapping]] = ..., sync_settings: _Optional[_Union[_sync_settings_pb2.SyncSettings, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...
