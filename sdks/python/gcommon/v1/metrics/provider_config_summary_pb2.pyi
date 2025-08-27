from gcommon.v1.metrics import (
    resource_limits_summary_pb2 as _resource_limits_summary_pb2,
)
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderConfigSummary(_message.Message):
    __slots__ = (
        "exporter_count",
        "security_enabled",
        "resource_limits",
        "export_destinations",
    )
    EXPORTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    exporter_count: int
    security_enabled: bool
    resource_limits: _resource_limits_summary_pb2.ResourceLimitsSummary
    export_destinations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        exporter_count: _Optional[int] = ...,
        security_enabled: _Optional[bool] = ...,
        resource_limits: _Optional[
            _Union[_resource_limits_summary_pb2.ResourceLimitsSummary, _Mapping]
        ] = ...,
        export_destinations: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
