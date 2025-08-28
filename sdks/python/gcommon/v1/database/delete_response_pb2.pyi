from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheDeleteResponse(_message.Message):
    __slots__ = ("success", "error", "deleted_count")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    deleted_count: int
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., deleted_count: _Optional[int] = ...) -> None: ...
