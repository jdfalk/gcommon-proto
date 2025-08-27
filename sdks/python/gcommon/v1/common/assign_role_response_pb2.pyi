from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AssignRoleResponse(_message.Message):
    __slots__ = ("success", "error_message", "effective_permissions")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    effective_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: _Optional[bool] = ..., error_message: _Optional[str] = ..., effective_permissions: _Optional[_Iterable[str]] = ...) -> None: ...
