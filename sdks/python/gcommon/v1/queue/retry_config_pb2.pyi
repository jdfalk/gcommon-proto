import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueRetryConfig(_message.Message):
    __slots__ = ("enabled", "max_retries", "initial_delay", "max_delay", "backoff_multiplier", "jitter_factor", "total_timeout")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    JITTER_FACTOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    max_retries: int
    initial_delay: _duration_pb2.Duration
    max_delay: _duration_pb2.Duration
    backoff_multiplier: float
    jitter_factor: float
    total_timeout: _duration_pb2.Duration
    def __init__(self, enabled: _Optional[bool] = ..., max_retries: _Optional[int] = ..., initial_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., backoff_multiplier: _Optional[float] = ..., jitter_factor: _Optional[float] = ..., total_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
