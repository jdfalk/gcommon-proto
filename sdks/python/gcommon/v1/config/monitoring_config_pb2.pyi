from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigMonitoringConfig(_message.Message):
    __slots__ = (
        "enabled",
        "provider",
        "endpoints",
        "metrics",
        "alerts",
        "dashboards",
        "config",
    )
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    provider: str
    endpoints: _containers.RepeatedScalarFieldContainer[str]
    metrics: _containers.RepeatedScalarFieldContainer[str]
    alerts: _containers.RepeatedScalarFieldContainer[str]
    dashboards: _containers.RepeatedScalarFieldContainer[str]
    config: _containers.ScalarMap[str, str]
    def __init__(
        self,
        enabled: _Optional[bool] = ...,
        provider: _Optional[str] = ...,
        endpoints: _Optional[_Iterable[str]] = ...,
        metrics: _Optional[_Iterable[str]] = ...,
        alerts: _Optional[_Iterable[str]] = ...,
        dashboards: _Optional[_Iterable[str]] = ...,
        config: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
