from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MfaMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MFA_METHOD_UNSPECIFIED: _ClassVar[MfaMethod]
    MFA_METHOD_SMS: _ClassVar[MfaMethod]
    MFA_METHOD_EMAIL: _ClassVar[MfaMethod]
    MFA_METHOD_TOTP: _ClassVar[MfaMethod]
    MFA_METHOD_HARDWARE_KEY: _ClassVar[MfaMethod]

MFA_METHOD_UNSPECIFIED: MfaMethod
MFA_METHOD_SMS: MfaMethod
MFA_METHOD_EMAIL: MfaMethod
MFA_METHOD_TOTP: MfaMethod
MFA_METHOD_HARDWARE_KEY: MfaMethod
