from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunMigrationResponse(_message.Message):
    __slots__ = ("success", "applied_versions", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    applied_versions: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.Error
    def __init__(self, success: _Optional[bool] = ..., applied_versions: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
