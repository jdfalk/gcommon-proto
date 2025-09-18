from gcommon.v1.organization import audit_alert_pb2 as _audit_alert_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditConfig(_message.Message):
    __slots__ = ("audit_enabled", "retention_days", "storage_location", "audited_events", "real_time_monitoring", "alerts")
    AUDIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    AUDITED_EVENTS_FIELD_NUMBER: _ClassVar[int]
    REAL_TIME_MONITORING_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    audit_enabled: bool
    retention_days: int
    storage_location: str
    audited_events: _containers.RepeatedScalarFieldContainer[str]
    real_time_monitoring: bool
    alerts: _containers.RepeatedCompositeFieldContainer[_audit_alert_pb2.AuditAlert]
    def __init__(self, audit_enabled: _Optional[bool] = ..., retention_days: _Optional[int] = ..., storage_location: _Optional[str] = ..., audited_events: _Optional[_Iterable[str]] = ..., real_time_monitoring: _Optional[bool] = ..., alerts: _Optional[_Iterable[_Union[_audit_alert_pb2.AuditAlert, _Mapping]]] = ...) -> None: ...
