from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ReferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REFERENCE_TYPE_UNSPECIFIED: _ClassVar[ReferenceType]
    REFERENCE_TYPE_TEMPLATE: _ClassVar[ReferenceType]
    REFERENCE_TYPE_POINTER: _ClassVar[ReferenceType]
    REFERENCE_TYPE_ALIAS: _ClassVar[ReferenceType]
    REFERENCE_TYPE_COMPUTED: _ClassVar[ReferenceType]
    REFERENCE_TYPE_DERIVED: _ClassVar[ReferenceType]

REFERENCE_TYPE_UNSPECIFIED: ReferenceType
REFERENCE_TYPE_TEMPLATE: ReferenceType
REFERENCE_TYPE_POINTER: ReferenceType
REFERENCE_TYPE_ALIAS: ReferenceType
REFERENCE_TYPE_COMPUTED: ReferenceType
REFERENCE_TYPE_DERIVED: ReferenceType
