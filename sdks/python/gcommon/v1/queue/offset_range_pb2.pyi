from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetRange(_message.Message):
    __slots__ = ("start_offset", "end_offset")
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_offset: int
    end_offset: int
    def __init__(self, start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...
