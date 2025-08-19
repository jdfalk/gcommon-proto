from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PerformanceOptions(_message.Message):
    __slots__ = ("worker_count", "batch_size", "buffer_size_mb", "enable_compression", "throttle_rate")
    WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_RATE_FIELD_NUMBER: _ClassVar[int]
    worker_count: int
    batch_size: int
    buffer_size_mb: int
    enable_compression: bool
    throttle_rate: int
    def __init__(self, worker_count: _Optional[int] = ..., batch_size: _Optional[int] = ..., buffer_size_mb: _Optional[int] = ..., enable_compression: bool = ..., throttle_rate: _Optional[int] = ...) -> None: ...
