import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthMetrics(_message.Message):
    __slots__ = ("collected_at", "total_checks", "healthy_checks", "unhealthy_checks", "unknown_checks", "avg_check_duration_ms", "success_rate_percent", "status_changes_last_hour", "last_failure", "uptime_percent", "service_metrics")
    class ServiceMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ServiceHealthMetrics
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ServiceHealthMetrics, _Mapping]] = ...) -> None: ...
    COLLECTED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_CHECKS_FIELD_NUMBER: _ClassVar[int]
    AVG_CHECK_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_CHANGES_LAST_HOUR_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    UPTIME_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_METRICS_FIELD_NUMBER: _ClassVar[int]
    collected_at: _timestamp_pb2.Timestamp
    total_checks: int
    healthy_checks: int
    unhealthy_checks: int
    unknown_checks: int
    avg_check_duration_ms: float
    success_rate_percent: float
    status_changes_last_hour: int
    last_failure: _timestamp_pb2.Timestamp
    uptime_percent: float
    service_metrics: _containers.MessageMap[str, ServiceHealthMetrics]
    def __init__(self, collected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_checks: _Optional[int] = ..., healthy_checks: _Optional[int] = ..., unhealthy_checks: _Optional[int] = ..., unknown_checks: _Optional[int] = ..., avg_check_duration_ms: _Optional[float] = ..., success_rate_percent: _Optional[float] = ..., status_changes_last_hour: _Optional[int] = ..., last_failure: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., uptime_percent: _Optional[float] = ..., service_metrics: _Optional[_Mapping[str, ServiceHealthMetrics]] = ...) -> None: ...

class ServiceHealthMetrics(_message.Message):
    __slots__ = ("service_name", "check_count", "health_score", "uptime_percent", "avg_response_time_ms")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECK_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_SCORE_FIELD_NUMBER: _ClassVar[int]
    UPTIME_PERCENT_FIELD_NUMBER: _ClassVar[int]
    AVG_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    check_count: int
    health_score: int
    uptime_percent: float
    avg_response_time_ms: float
    def __init__(self, service_name: _Optional[str] = ..., check_count: _Optional[int] = ..., health_score: _Optional[int] = ..., uptime_percent: _Optional[float] = ..., avg_response_time_ms: _Optional[float] = ...) -> None: ...
