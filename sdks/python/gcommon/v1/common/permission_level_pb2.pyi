from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthPermissionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERMISSION_LEVEL_UNSPECIFIED: _ClassVar[AuthPermissionLevel]
    PERMISSION_LEVEL_SYSTEM: _ClassVar[AuthPermissionLevel]
    PERMISSION_LEVEL_ORGANIZATION: _ClassVar[AuthPermissionLevel]
    PERMISSION_LEVEL_PROJECT: _ClassVar[AuthPermissionLevel]
    PERMISSION_LEVEL_RESOURCE: _ClassVar[AuthPermissionLevel]
PERMISSION_LEVEL_UNSPECIFIED: AuthPermissionLevel
PERMISSION_LEVEL_SYSTEM: AuthPermissionLevel
PERMISSION_LEVEL_ORGANIZATION: AuthPermissionLevel
PERMISSION_LEVEL_PROJECT: AuthPermissionLevel
PERMISSION_LEVEL_RESOURCE: AuthPermissionLevel
