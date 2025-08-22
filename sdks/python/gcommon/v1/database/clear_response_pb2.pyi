from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClearResponse(_message.Message):
    __slots__ = ("cleared_count", "success", "error")
    CLEARED_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    cleared_count: int
    success: bool
    error: _error_pb2.Error
    def __init__(self, cleared_count: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
