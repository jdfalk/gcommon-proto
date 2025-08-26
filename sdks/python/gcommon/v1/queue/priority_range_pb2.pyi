from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PriorityRange(_message.Message):
    __slots__ = ("min_priority", "max_priority")
    MIN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MAX_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    min_priority: int
    max_priority: int
    def __init__(self, min_priority: _Optional[int] = ..., max_priority: _Optional[int] = ...) -> None: ...
