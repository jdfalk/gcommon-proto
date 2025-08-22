from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from gcommon.v1.organization import billing_settings_pb2 as _billing_settings_pb2
from gcommon.v1.organization import compliance_settings_pb2 as _compliance_settings_pb2
from gcommon.v1.organization import feature_flag_pb2 as _feature_flag_pb2
from gcommon.v1.organization import integration_settings_pb2 as _integration_settings_pb2
from gcommon.v1.organization import notification_settings_pb2 as _notification_settings_pb2
from gcommon.v1.organization import security_settings_pb2 as _security_settings_pb2
from gcommon.v1.organization import ui_settings_pb2 as _ui_settings_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationSettings(_message.Message):
    __slots__ = ("organization_id", "security", "ui", "integrations", "notifications", "billing", "compliance", "feature_flags", "custom_settings", "updated_at", "updated_by")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    UI_FIELD_NUMBER: _ClassVar[int]
    INTEGRATIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    BILLING_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    security: _security_settings_pb2.SecuritySettings
    ui: _ui_settings_pb2.UISettings
    integrations: _integration_settings_pb2.IntegrationSettings
    notifications: _notification_settings_pb2.OrganizationNotificationSettings
    billing: _billing_settings_pb2.BillingSettings
    compliance: _compliance_settings_pb2.OrganizationComplianceSettings
    feature_flags: _containers.RepeatedCompositeFieldContainer[_feature_flag_pb2.FeatureFlag]
    custom_settings: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, organization_id: _Optional[str] = ..., security: _Optional[_Union[_security_settings_pb2.SecuritySettings, _Mapping]] = ..., ui: _Optional[_Union[_ui_settings_pb2.UISettings, _Mapping]] = ..., integrations: _Optional[_Union[_integration_settings_pb2.IntegrationSettings, _Mapping]] = ..., notifications: _Optional[_Union[_notification_settings_pb2.OrganizationNotificationSettings, _Mapping]] = ..., billing: _Optional[_Union[_billing_settings_pb2.BillingSettings, _Mapping]] = ..., compliance: _Optional[_Union[_compliance_settings_pb2.OrganizationComplianceSettings, _Mapping]] = ..., feature_flags: _Optional[_Iterable[_Union[_feature_flag_pb2.FeatureFlag, _Mapping]]] = ..., custom_settings: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...
