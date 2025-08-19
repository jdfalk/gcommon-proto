from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RetryDelayConfig(_message.Message):
    __slots__ = ("initial_delay_ms", "max_delay_ms", "backoff_multiplier", "jitter_enabled")
    INITIAL_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    JITTER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    initial_delay_ms: int
    max_delay_ms: int
    backoff_multiplier: float
    jitter_enabled: bool
    def __init__(self, initial_delay_ms: _Optional[int] = ..., max_delay_ms: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ..., jitter_enabled: bool = ...) -> None: ...
