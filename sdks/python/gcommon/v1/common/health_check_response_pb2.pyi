import datetime

from gcommon.v1.common import check_result_pb2 as _check_result_pb2
from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import health_metrics_pb2 as _health_metrics_pb2
from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthHealthCheckResponse(_message.Message):
    __slots__ = (
        "status",
        "service",
        "timestamp",
        "response_time",
        "check_results",
        "message",
        "error",
        "metrics",
    )
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.CommonHealthStatus
    service: str
    timestamp: _timestamp_pb2.Timestamp
    response_time: _duration_pb2.Duration
    check_results: _containers.RepeatedCompositeFieldContainer[
        _check_result_pb2.CheckResult
    ]
    message: str
    error: _error_pb2.Error
    metrics: _health_metrics_pb2.HealthMetrics
    def __init__(
        self,
        status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ...,
        service: _Optional[str] = ...,
        timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        response_time: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        check_results: _Optional[
            _Iterable[_Union[_check_result_pb2.CheckResult, _Mapping]]
        ] = ...,
        message: _Optional[str] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        metrics: _Optional[_Union[_health_metrics_pb2.HealthMetrics, _Mapping]] = ...,
    ) -> None: ...
