import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthMetrics(_message.Message):
    __slots__ = ("total_checks", "healthy_checks", "unhealthy_checks", "unknown_checks", "average_response_time_ms", "last_updated", "uptime_seconds", "custom_metrics")
    class CustomMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    TOTAL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_CHECKS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METRICS_FIELD_NUMBER: _ClassVar[int]
    total_checks: int
    healthy_checks: int
    unhealthy_checks: int
    unknown_checks: int
    average_response_time_ms: float
    last_updated: _timestamp_pb2.Timestamp
    uptime_seconds: float
    custom_metrics: _containers.ScalarMap[str, float]
    def __init__(self, total_checks: _Optional[int] = ..., healthy_checks: _Optional[int] = ..., unhealthy_checks: _Optional[int] = ..., unknown_checks: _Optional[int] = ..., average_response_time_ms: _Optional[float] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., uptime_seconds: _Optional[float] = ..., custom_metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...
