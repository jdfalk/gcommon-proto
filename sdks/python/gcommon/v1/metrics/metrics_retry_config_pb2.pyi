from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsRetryConfig(_message.Message):
    __slots__ = ("max_retries", "initial_delay_seconds", "max_delay_seconds", "backoff_multiplier")
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    max_retries: int
    initial_delay_seconds: int
    max_delay_seconds: int
    backoff_multiplier: float
    def __init__(self, max_retries: _Optional[int] = ..., initial_delay_seconds: _Optional[int] = ..., max_delay_seconds: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ...) -> None: ...
