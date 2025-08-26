from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryRetryConfig(_message.Message):
    __slots__ = ("enabled", "max_retries", "initial_delay_ms", "max_delay_ms", "backoff_multiplier", "retry_error_codes")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    RETRY_ERROR_CODES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    max_retries: int
    initial_delay_ms: int
    max_delay_ms: int
    backoff_multiplier: float
    retry_error_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: bool = ..., max_retries: _Optional[int] = ..., initial_delay_ms: _Optional[int] = ..., max_delay_ms: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ..., retry_error_codes: _Optional[_Iterable[str]] = ...) -> None: ...
