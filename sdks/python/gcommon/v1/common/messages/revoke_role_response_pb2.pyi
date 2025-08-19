from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RevokeRoleResponse(_message.Message):
    __slots__ = ("success", "error_message", "remaining_permissions")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMAINING_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    remaining_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ..., remaining_permissions: _Optional[_Iterable[str]] = ...) -> None: ...
