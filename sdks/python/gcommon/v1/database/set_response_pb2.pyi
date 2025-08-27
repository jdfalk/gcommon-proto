from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetResponse(_message.Message):
    __slots__ = ("success", "overwritten", "size_bytes")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITTEN_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    success: bool
    overwritten: bool
    size_bytes: int
    def __init__(
        self,
        success: _Optional[bool] = ...,
        overwritten: _Optional[bool] = ...,
        size_bytes: _Optional[int] = ...,
    ) -> None: ...
