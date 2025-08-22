from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DependencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPENDENCY_TYPE_UNSPECIFIED: _ClassVar[DependencyType]
    DEPENDENCY_TYPE_REQUIRED: _ClassVar[DependencyType]
    DEPENDENCY_TYPE_OPTIONAL: _ClassVar[DependencyType]
    DEPENDENCY_TYPE_CONDITIONAL: _ClassVar[DependencyType]
    DEPENDENCY_TYPE_DERIVED: _ClassVar[DependencyType]
    DEPENDENCY_TYPE_CONFLICT: _ClassVar[DependencyType]
DEPENDENCY_TYPE_UNSPECIFIED: DependencyType
DEPENDENCY_TYPE_REQUIRED: DependencyType
DEPENDENCY_TYPE_OPTIONAL: DependencyType
DEPENDENCY_TYPE_CONDITIONAL: DependencyType
DEPENDENCY_TYPE_DERIVED: DependencyType
DEPENDENCY_TYPE_CONFLICT: DependencyType
