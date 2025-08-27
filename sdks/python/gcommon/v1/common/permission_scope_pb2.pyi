from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERMISSION_SCOPE_UNSPECIFIED: _ClassVar[PermissionScope]
    PERMISSION_SCOPE_GLOBAL: _ClassVar[PermissionScope]
    PERMISSION_SCOPE_ORGANIZATION: _ClassVar[PermissionScope]
    PERMISSION_SCOPE_PROJECT: _ClassVar[PermissionScope]
    PERMISSION_SCOPE_RESOURCE: _ClassVar[PermissionScope]
    PERMISSION_SCOPE_USER: _ClassVar[PermissionScope]
PERMISSION_SCOPE_UNSPECIFIED: PermissionScope
PERMISSION_SCOPE_GLOBAL: PermissionScope
PERMISSION_SCOPE_ORGANIZATION: PermissionScope
PERMISSION_SCOPE_PROJECT: PermissionScope
PERMISSION_SCOPE_RESOURCE: PermissionScope
PERMISSION_SCOPE_USER: PermissionScope
