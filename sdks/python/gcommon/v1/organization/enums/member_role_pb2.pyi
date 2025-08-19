from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MemberRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBER_ROLE_UNSPECIFIED: _ClassVar[MemberRole]
    MEMBER_ROLE_OWNER: _ClassVar[MemberRole]
    MEMBER_ROLE_ADMIN: _ClassVar[MemberRole]
    MEMBER_ROLE_MEMBER: _ClassVar[MemberRole]
    MEMBER_ROLE_VIEWER: _ClassVar[MemberRole]
    MEMBER_ROLE_GUEST: _ClassVar[MemberRole]
MEMBER_ROLE_UNSPECIFIED: MemberRole
MEMBER_ROLE_OWNER: MemberRole
MEMBER_ROLE_ADMIN: MemberRole
MEMBER_ROLE_MEMBER: MemberRole
MEMBER_ROLE_VIEWER: MemberRole
MEMBER_ROLE_GUEST: MemberRole
