from gcommon.v1.common import backoff_strategy_pb2 as _backoff_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigRetrySettings(_message.Message):
    __slots__ = ("enabled", "max_retries", "delay_seconds", "backoff_strategy", "conditions")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    max_retries: int
    delay_seconds: int
    backoff_strategy: _backoff_strategy_pb2.BackoffStrategy
    conditions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: _Optional[bool] = ..., max_retries: _Optional[int] = ..., delay_seconds: _Optional[int] = ..., backoff_strategy: _Optional[_Union[_backoff_strategy_pb2.BackoffStrategy, str]] = ..., conditions: _Optional[_Iterable[str]] = ...) -> None: ...
