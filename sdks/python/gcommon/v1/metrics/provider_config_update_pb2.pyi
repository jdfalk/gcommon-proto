from gcommon.v1.metrics import export_config_update_pb2 as _export_config_update_pb2
from gcommon.v1.metrics import (
    provider_settings_update_pb2 as _provider_settings_update_pb2,
)
from gcommon.v1.metrics import resource_limits_update_pb2 as _resource_limits_update_pb2
from gcommon.v1.metrics import security_config_update_pb2 as _security_config_update_pb2
from gcommon.v1.metrics import tag_updates_pb2 as _tag_updates_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderConfigUpdate(_message.Message):
    __slots__ = (
        "name",
        "description",
        "settings_update",
        "export_config_update",
        "resource_limits_update",
        "security_config_update",
        "tag_updates",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONFIG_UPDATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONFIG_UPDATE_FIELD_NUMBER: _ClassVar[int]
    TAG_UPDATES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    settings_update: _provider_settings_update_pb2.ProviderSettingsUpdate
    export_config_update: _export_config_update_pb2.ExportConfigUpdate
    resource_limits_update: _resource_limits_update_pb2.ResourceLimitsUpdate
    security_config_update: _security_config_update_pb2.SecurityConfigUpdate
    tag_updates: _tag_updates_pb2.TagUpdates
    def __init__(
        self,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        settings_update: _Optional[
            _Union[_provider_settings_update_pb2.ProviderSettingsUpdate, _Mapping]
        ] = ...,
        export_config_update: _Optional[
            _Union[_export_config_update_pb2.ExportConfigUpdate, _Mapping]
        ] = ...,
        resource_limits_update: _Optional[
            _Union[_resource_limits_update_pb2.ResourceLimitsUpdate, _Mapping]
        ] = ...,
        security_config_update: _Optional[
            _Union[_security_config_update_pb2.SecurityConfigUpdate, _Mapping]
        ] = ...,
        tag_updates: _Optional[_Union[_tag_updates_pb2.TagUpdates, _Mapping]] = ...,
    ) -> None: ...
