from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_UNSPECIFIED: _ClassVar[UserStatus]
    USER_STATUS_ACTIVE: _ClassVar[UserStatus]
    USER_STATUS_INACTIVE: _ClassVar[UserStatus]
    USER_STATUS_SUSPENDED: _ClassVar[UserStatus]
    USER_STATUS_PENDING_VERIFICATION: _ClassVar[UserStatus]
    USER_STATUS_LOCKED: _ClassVar[UserStatus]
    USER_STATUS_DELETED: _ClassVar[UserStatus]

USER_STATUS_UNSPECIFIED: UserStatus
USER_STATUS_ACTIVE: UserStatus
USER_STATUS_INACTIVE: UserStatus
USER_STATUS_SUSPENDED: UserStatus
USER_STATUS_PENDING_VERIFICATION: UserStatus
USER_STATUS_LOCKED: UserStatus
USER_STATUS_DELETED: UserStatus
