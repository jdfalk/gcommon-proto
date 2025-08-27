from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SizeBucket(_message.Message):
    __slots__ = ("min_size_bytes", "max_size_bytes", "message_count")
    MIN_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_size_bytes: int
    max_size_bytes: int
    message_count: int
    def __init__(self, min_size_bytes: _Optional[int] = ..., max_size_bytes: _Optional[int] = ..., message_count: _Optional[int] = ...) -> None: ...
