from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VersionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_TYPE_UNSPECIFIED: _ClassVar[VersionType]
    VERSION_TYPE_MAJOR: _ClassVar[VersionType]
    VERSION_TYPE_MINOR: _ClassVar[VersionType]
    VERSION_TYPE_PATCH: _ClassVar[VersionType]
    VERSION_TYPE_HOTFIX: _ClassVar[VersionType]
    VERSION_TYPE_PRERELEASE: _ClassVar[VersionType]
    VERSION_TYPE_SNAPSHOT: _ClassVar[VersionType]
    VERSION_TYPE_BRANCH: _ClassVar[VersionType]
    VERSION_TYPE_TAG: _ClassVar[VersionType]

VERSION_TYPE_UNSPECIFIED: VersionType
VERSION_TYPE_MAJOR: VersionType
VERSION_TYPE_MINOR: VersionType
VERSION_TYPE_PATCH: VersionType
VERSION_TYPE_HOTFIX: VersionType
VERSION_TYPE_PRERELEASE: VersionType
VERSION_TYPE_SNAPSHOT: VersionType
VERSION_TYPE_BRANCH: VersionType
VERSION_TYPE_TAG: VersionType
