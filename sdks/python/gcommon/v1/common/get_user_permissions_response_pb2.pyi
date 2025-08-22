from gcommon.v1.common import role_pb2 as _role_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserPermissionsResponse(_message.Message):
    __slots__ = ("permissions", "role_permissions", "effective_permissions", "roles")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    role_permissions: _containers.RepeatedScalarFieldContainer[str]
    effective_permissions: _containers.RepeatedScalarFieldContainer[str]
    roles: _containers.RepeatedCompositeFieldContainer[_role_pb2.Role]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ..., role_permissions: _Optional[_Iterable[str]] = ..., effective_permissions: _Optional[_Iterable[str]] = ..., roles: _Optional[_Iterable[_Union[_role_pb2.Role, _Mapping]]] = ...) -> None: ...
