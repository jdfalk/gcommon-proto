from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import role_pb2 as _role_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRoleResponse(_message.Message):
    __slots__ = ("role", "error")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    role: _role_pb2.Role
    error: _error_pb2.Error
    def __init__(self, role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
