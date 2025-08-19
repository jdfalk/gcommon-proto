from gcommon.v1.metrics.messages import open_telemetry_settings_update_pb2 as _open_telemetry_settings_update_pb2
from gcommon.v1.metrics.messages import prometheus_settings_update_pb2 as _prometheus_settings_update_pb2
from gcommon.v1.metrics.messages import stats_d_settings_update_pb2 as _stats_d_settings_update_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderSettingsUpdate(_message.Message):
    __slots__ = ("prometheus", "opentelemetry", "statsd")
    PROMETHEUS_FIELD_NUMBER: _ClassVar[int]
    OPENTELEMETRY_FIELD_NUMBER: _ClassVar[int]
    STATSD_FIELD_NUMBER: _ClassVar[int]
    prometheus: _prometheus_settings_update_pb2.PrometheusSettingsUpdate
    opentelemetry: _open_telemetry_settings_update_pb2.OpenTelemetrySettingsUpdate
    statsd: _stats_d_settings_update_pb2.StatsDSettingsUpdate
    def __init__(self, prometheus: _Optional[_Union[_prometheus_settings_update_pb2.PrometheusSettingsUpdate, _Mapping]] = ..., opentelemetry: _Optional[_Union[_open_telemetry_settings_update_pb2.OpenTelemetrySettingsUpdate, _Mapping]] = ..., statsd: _Optional[_Union[_stats_d_settings_update_pb2.StatsDSettingsUpdate, _Mapping]] = ...) -> None: ...
