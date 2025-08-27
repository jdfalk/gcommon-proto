from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthVerificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERIFICATION_TYPE_UNSPECIFIED: _ClassVar[AuthVerificationType]
    VERIFICATION_TYPE_EMAIL: _ClassVar[AuthVerificationType]
    VERIFICATION_TYPE_SMS: _ClassVar[AuthVerificationType]

VERIFICATION_TYPE_UNSPECIFIED: AuthVerificationType
VERIFICATION_TYPE_EMAIL: AuthVerificationType
VERIFICATION_TYPE_SMS: AuthVerificationType
