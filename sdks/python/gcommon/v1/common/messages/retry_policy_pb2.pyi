from gcommon.v1.common.enums import error_code_pb2 as _error_code_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonRetryPolicy(_message.Message):
    __slots__ = ("max_attempts", "initial_delay", "max_delay", "backoff_multiplier", "enable_jitter", "retryable_errors", "total_timeout")
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_JITTER_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    initial_delay: _duration_pb2.Duration
    max_delay: _duration_pb2.Duration
    backoff_multiplier: float
    enable_jitter: bool
    retryable_errors: _containers.RepeatedScalarFieldContainer[_error_code_pb2.ErrorCode]
    total_timeout: _duration_pb2.Duration
    def __init__(self, max_attempts: _Optional[int] = ..., initial_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., backoff_multiplier: _Optional[float] = ..., enable_jitter: bool = ..., retryable_errors: _Optional[_Iterable[_Union[_error_code_pb2.ErrorCode, str]]] = ..., total_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
