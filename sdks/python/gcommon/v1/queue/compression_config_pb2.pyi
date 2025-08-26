from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueueCompressionConfig(_message.Message):
    __slots__ = ("enabled", "algorithm", "level", "min_size_bytes")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MIN_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    algorithm: str
    level: int
    min_size_bytes: int
    def __init__(self, enabled: bool = ..., algorithm: _Optional[str] = ..., level: _Optional[int] = ..., min_size_bytes: _Optional[int] = ...) -> None: ...
