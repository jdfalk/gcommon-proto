from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RoleScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLE_SCOPE_UNSPECIFIED: _ClassVar[RoleScope]
    ROLE_SCOPE_GLOBAL: _ClassVar[RoleScope]
    ROLE_SCOPE_ORGANIZATION: _ClassVar[RoleScope]
    ROLE_SCOPE_PROJECT: _ClassVar[RoleScope]
    ROLE_SCOPE_TEAM: _ClassVar[RoleScope]
    ROLE_SCOPE_RESOURCE: _ClassVar[RoleScope]

ROLE_SCOPE_UNSPECIFIED: RoleScope
ROLE_SCOPE_GLOBAL: RoleScope
ROLE_SCOPE_ORGANIZATION: RoleScope
ROLE_SCOPE_PROJECT: RoleScope
ROLE_SCOPE_TEAM: RoleScope
ROLE_SCOPE_RESOURCE: RoleScope
