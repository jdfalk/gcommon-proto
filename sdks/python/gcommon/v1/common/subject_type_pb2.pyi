from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthSubjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBJECT_TYPE_UNSPECIFIED: _ClassVar[AuthSubjectType]
    SUBJECT_TYPE_USER: _ClassVar[AuthSubjectType]
    SUBJECT_TYPE_ROLE: _ClassVar[AuthSubjectType]

SUBJECT_TYPE_UNSPECIFIED: AuthSubjectType
SUBJECT_TYPE_USER: AuthSubjectType
SUBJECT_TYPE_ROLE: AuthSubjectType
