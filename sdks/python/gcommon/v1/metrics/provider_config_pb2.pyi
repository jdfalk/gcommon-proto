from gcommon.v1.common import metrics_provider_type_pb2 as _metrics_provider_type_pb2
from gcommon.v1.common import organization_resource_limits_pb2 as _organization_resource_limits_pb2
from gcommon.v1.metrics import export_config_pb2 as _export_config_pb2
from gcommon.v1.metrics import provider_settings_pb2 as _provider_settings_pb2
from gcommon.v1.metrics import security_config_pb2 as _security_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderConfig(_message.Message):
    __slots__ = ("provider_id", "name", "type", "settings", "export_config", "resource_limits", "security_config", "tags", "description")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    name: str
    type: _metrics_provider_type_pb2.MetricsProviderType
    settings: _provider_settings_pb2.ProviderSettings
    export_config: _export_config_pb2.ExportConfig
    resource_limits: _organization_resource_limits_pb2.OrganizationResourceLimits
    security_config: _security_config_pb2.MetricsSecurityConfig
    tags: _containers.ScalarMap[str, str]
    description: str
    def __init__(self, provider_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_metrics_provider_type_pb2.MetricsProviderType, str]] = ..., settings: _Optional[_Union[_provider_settings_pb2.ProviderSettings, _Mapping]] = ..., export_config: _Optional[_Union[_export_config_pb2.ExportConfig, _Mapping]] = ..., resource_limits: _Optional[_Union[_organization_resource_limits_pb2.OrganizationResourceLimits, _Mapping]] = ..., security_config: _Optional[_Union[_security_config_pb2.MetricsSecurityConfig, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ...) -> None: ...
