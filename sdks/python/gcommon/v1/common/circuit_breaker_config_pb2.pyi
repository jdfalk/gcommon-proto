import datetime

from gcommon.v1.common import circuit_breaker_state_pb2 as _circuit_breaker_state_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonCircuitBreakerConfig(_message.Message):
    __slots__ = ("failure_threshold", "success_threshold", "timeout", "max_requests", "window_size", "state")
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    failure_threshold: int
    success_threshold: int
    timeout: _duration_pb2.Duration
    max_requests: int
    window_size: _duration_pb2.Duration
    state: _circuit_breaker_state_pb2.CircuitBreakerState
    def __init__(self, failure_threshold: _Optional[int] = ..., success_threshold: _Optional[int] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_requests: _Optional[int] = ..., window_size: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., state: _Optional[_Union[_circuit_breaker_state_pb2.CircuitBreakerState, str]] = ...) -> None: ...
