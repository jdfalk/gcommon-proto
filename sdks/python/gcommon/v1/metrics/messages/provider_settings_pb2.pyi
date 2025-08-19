from gcommon.v1.metrics.messages import open_telemetry_settings_pb2 as _open_telemetry_settings_pb2
from gcommon.v1.metrics.messages import prometheus_settings_pb2 as _prometheus_settings_pb2
from gcommon.v1.metrics.messages import stats_d_settings_pb2 as _stats_d_settings_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderSettings(_message.Message):
    __slots__ = ("prometheus", "opentelemetry", "statsd", "custom")
    class CustomEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROMETHEUS_FIELD_NUMBER: _ClassVar[int]
    OPENTELEMETRY_FIELD_NUMBER: _ClassVar[int]
    STATSD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    prometheus: _prometheus_settings_pb2.PrometheusSettings
    opentelemetry: _open_telemetry_settings_pb2.OpenTelemetrySettings
    statsd: _stats_d_settings_pb2.StatsDSettings
    custom: _containers.ScalarMap[str, str]
    def __init__(self, prometheus: _Optional[_Union[_prometheus_settings_pb2.PrometheusSettings, _Mapping]] = ..., opentelemetry: _Optional[_Union[_open_telemetry_settings_pb2.OpenTelemetrySettings, _Mapping]] = ..., statsd: _Optional[_Union[_stats_d_settings_pb2.StatsDSettings, _Mapping]] = ..., custom: _Optional[_Mapping[str, str]] = ...) -> None: ...
