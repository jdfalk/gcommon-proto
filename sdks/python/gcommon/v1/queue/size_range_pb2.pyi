from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SizeRange(_message.Message):
    __slots__ = ("min_size", "max_size")
    MIN_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    min_size: int
    max_size: int
    def __init__(self, min_size: _Optional[int] = ..., max_size: _Optional[int] = ...) -> None: ...
