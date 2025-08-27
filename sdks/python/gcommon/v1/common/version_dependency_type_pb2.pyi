from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VersionDependencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_DEPENDENCY_TYPE_UNSPECIFIED: _ClassVar[VersionDependencyType]
    VERSION_DEPENDENCY_TYPE_RUNTIME: _ClassVar[VersionDependencyType]
    VERSION_DEPENDENCY_TYPE_BUILD: _ClassVar[VersionDependencyType]
    VERSION_DEPENDENCY_TYPE_TEST: _ClassVar[VersionDependencyType]
    VERSION_DEPENDENCY_TYPE_DEV: _ClassVar[VersionDependencyType]
    VERSION_DEPENDENCY_TYPE_PEER: _ClassVar[VersionDependencyType]
    VERSION_DEPENDENCY_TYPE_OPTIONAL: _ClassVar[VersionDependencyType]
VERSION_DEPENDENCY_TYPE_UNSPECIFIED: VersionDependencyType
VERSION_DEPENDENCY_TYPE_RUNTIME: VersionDependencyType
VERSION_DEPENDENCY_TYPE_BUILD: VersionDependencyType
VERSION_DEPENDENCY_TYPE_TEST: VersionDependencyType
VERSION_DEPENDENCY_TYPE_DEV: VersionDependencyType
VERSION_DEPENDENCY_TYPE_PEER: VersionDependencyType
VERSION_DEPENDENCY_TYPE_OPTIONAL: VersionDependencyType
