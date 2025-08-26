import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueCircuitBreakerConfig(_message.Message):
    __slots__ = ("enabled", "failure_threshold", "success_threshold", "timeout", "max_requests", "interval")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    failure_threshold: int
    success_threshold: int
    timeout: _duration_pb2.Duration
    max_requests: int
    interval: _duration_pb2.Duration
    def __init__(self, enabled: _Optional[bool] = ..., failure_threshold: _Optional[int] = ..., success_threshold: _Optional[int] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_requests: _Optional[int] = ..., interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
