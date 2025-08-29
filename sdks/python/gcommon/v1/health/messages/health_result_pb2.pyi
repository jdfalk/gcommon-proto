from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthResult(_message.Message):
    __slots__ = ("check_id", "status", "checked_at", "duration", "message", "error", "details", "sequence", "status_changed", "previous_status", "consecutive_count", "metrics")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CHANGED_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONSECUTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    check_id: str
    status: _health_status_pb2.HealthStatus
    checked_at: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    message: str
    error: str
    details: _containers.ScalarMap[str, str]
    sequence: int
    status_changed: bool
    previous_status: _health_status_pb2.HealthStatus
    consecutive_count: int
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, check_id: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., checked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., message: _Optional[str] = ..., error: _Optional[str] = ..., details: _Optional[_Mapping[str, str]] = ..., sequence: _Optional[int] = ..., status_changed: bool = ..., previous_status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., consecutive_count: _Optional[int] = ..., metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...
