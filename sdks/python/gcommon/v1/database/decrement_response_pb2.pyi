from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DecrementResponse(_message.Message):
    __slots__ = ("new_value", "success", "error")
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    new_value: int
    success: bool
    error: _error_pb2.Error
    def __init__(self, new_value: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
