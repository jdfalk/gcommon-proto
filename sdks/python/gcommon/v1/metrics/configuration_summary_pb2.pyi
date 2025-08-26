from gcommon.v1.metrics import resource_limits_summary_pb2 as _resource_limits_summary_pb2
from gcommon.v1.metrics import security_summary_pb2 as _security_summary_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigurationSummary(_message.Message):
    __slots__ = ("exporter_count", "security", "resource_limits", "config_version")
    EXPORTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    exporter_count: int
    security: _security_summary_pb2.SecuritySummary
    resource_limits: _resource_limits_summary_pb2.ResourceLimitsSummary
    config_version: str
    def __init__(self, exporter_count: _Optional[int] = ..., security: _Optional[_Union[_security_summary_pb2.SecuritySummary, _Mapping]] = ..., resource_limits: _Optional[_Union[_resource_limits_summary_pb2.ResourceLimitsSummary, _Mapping]] = ..., config_version: _Optional[str] = ...) -> None: ...
