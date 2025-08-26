from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteRetryConfig(_message.Message):
    __slots__ = ("max_retries", "initial_delay_ms", "max_delay_ms", "backoff_multiplier", "idempotent_only")
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_ONLY_FIELD_NUMBER: _ClassVar[int]
    max_retries: int
    initial_delay_ms: int
    max_delay_ms: int
    backoff_multiplier: float
    idempotent_only: bool
    def __init__(self, max_retries: _Optional[int] = ..., initial_delay_ms: _Optional[int] = ..., max_delay_ms: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ..., idempotent_only: bool = ...) -> None: ...
