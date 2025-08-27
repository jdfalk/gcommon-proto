from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MFAType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MFA_TYPE_UNSPECIFIED: _ClassVar[MFAType]
    MFA_TYPE_TOTP: _ClassVar[MFAType]
    MFA_TYPE_SMS: _ClassVar[MFAType]
    MFA_TYPE_EMAIL: _ClassVar[MFAType]
    MFA_TYPE_PUSH: _ClassVar[MFAType]

MFA_TYPE_UNSPECIFIED: MFAType
MFA_TYPE_TOTP: MFAType
MFA_TYPE_SMS: MFAType
MFA_TYPE_EMAIL: MFAType
MFA_TYPE_PUSH: MFAType
