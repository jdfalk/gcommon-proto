import datetime

from gcommon.v1.common import retry_delay_strategy_pb2 as _retry_delay_strategy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueRetryPolicy(_message.Message):
    __slots__ = ("max_attempts", "initial_delay", "max_delay", "backoff_multiplier", "delay_strategy", "enable_jitter", "jitter_factor")
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    DELAY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_JITTER_FIELD_NUMBER: _ClassVar[int]
    JITTER_FACTOR_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    initial_delay: _duration_pb2.Duration
    max_delay: _duration_pb2.Duration
    backoff_multiplier: float
    delay_strategy: _retry_delay_strategy_pb2.RetryDelayStrategy
    enable_jitter: bool
    jitter_factor: float
    def __init__(self, max_attempts: _Optional[int] = ..., initial_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., backoff_multiplier: _Optional[float] = ..., delay_strategy: _Optional[_Union[_retry_delay_strategy_pb2.RetryDelayStrategy, str]] = ..., enable_jitter: _Optional[bool] = ..., jitter_factor: _Optional[float] = ...) -> None: ...
