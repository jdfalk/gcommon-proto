from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERMISSION_TYPE_UNSPECIFIED: _ClassVar[PermissionType]
    PERMISSION_TYPE_READ: _ClassVar[PermissionType]
    PERMISSION_TYPE_WRITE: _ClassVar[PermissionType]
    PERMISSION_TYPE_DELETE: _ClassVar[PermissionType]
    PERMISSION_TYPE_ADMIN: _ClassVar[PermissionType]
    PERMISSION_TYPE_EXECUTE: _ClassVar[PermissionType]

PERMISSION_TYPE_UNSPECIFIED: PermissionType
PERMISSION_TYPE_READ: PermissionType
PERMISSION_TYPE_WRITE: PermissionType
PERMISSION_TYPE_DELETE: PermissionType
PERMISSION_TYPE_ADMIN: PermissionType
PERMISSION_TYPE_EXECUTE: PermissionType
