from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HierarchyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HIERARCHY_TYPE_UNSPECIFIED: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_DEPARTMENT: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_TEAM: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_PROJECT: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_GEOGRAPHIC: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_FUNCTIONAL: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_MATRIX: _ClassVar[HierarchyType]
    HIERARCHY_TYPE_FLAT: _ClassVar[HierarchyType]
HIERARCHY_TYPE_UNSPECIFIED: HierarchyType
HIERARCHY_TYPE_DEPARTMENT: HierarchyType
HIERARCHY_TYPE_TEAM: HierarchyType
HIERARCHY_TYPE_PROJECT: HierarchyType
HIERARCHY_TYPE_GEOGRAPHIC: HierarchyType
HIERARCHY_TYPE_FUNCTIONAL: HierarchyType
HIERARCHY_TYPE_MATRIX: HierarchyType
HIERARCHY_TYPE_FLAT: HierarchyType
