from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMultipleResponse(_message.Message):
    __slots__ = ("success", "failed_keys", "error", "set_count")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SET_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    failed_keys: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.Error
    set_count: int
    def __init__(self, success: _Optional[bool] = ..., failed_keys: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., set_count: _Optional[int] = ...) -> None: ...
