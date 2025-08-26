import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsHealthCheckResponse(_message.Message):
    __slots__ = ("status", "response_time", "message", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.CommonHealthStatus
    response_time: _duration_pb2.Duration
    message: str
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., response_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., message: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
