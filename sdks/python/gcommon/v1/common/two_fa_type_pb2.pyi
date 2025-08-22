from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthTwoFaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TWO_FA_TYPE_UNSPECIFIED: _ClassVar[AuthTwoFaType]
    TWO_FA_TYPE_TOTP: _ClassVar[AuthTwoFaType]
    TWO_FA_TYPE_SMS: _ClassVar[AuthTwoFaType]
    TWO_FA_TYPE_BACKUP: _ClassVar[AuthTwoFaType]
TWO_FA_TYPE_UNSPECIFIED: AuthTwoFaType
TWO_FA_TYPE_TOTP: AuthTwoFaType
TWO_FA_TYPE_SMS: AuthTwoFaType
TWO_FA_TYPE_BACKUP: AuthTwoFaType
