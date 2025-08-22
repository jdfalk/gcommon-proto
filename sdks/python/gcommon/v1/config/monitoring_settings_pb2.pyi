from gcommon.v1.config import monitoring_alert_pb2 as _monitoring_alert_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringSettings(_message.Message):
    __slots__ = ("enabled", "alerts", "metrics", "dashboard", "retention_days")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    alerts: _containers.RepeatedCompositeFieldContainer[_monitoring_alert_pb2.MonitoringAlert]
    metrics: _containers.RepeatedScalarFieldContainer[str]
    dashboard: str
    retention_days: int
    def __init__(self, enabled: bool = ..., alerts: _Optional[_Iterable[_Union[_monitoring_alert_pb2.MonitoringAlert, _Mapping]]] = ..., metrics: _Optional[_Iterable[str]] = ..., dashboard: _Optional[str] = ..., retention_days: _Optional[int] = ...) -> None: ...
