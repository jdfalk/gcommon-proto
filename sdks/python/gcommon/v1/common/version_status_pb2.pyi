from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VersionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_STATUS_UNSPECIFIED: _ClassVar[VersionStatus]
    VERSION_STATUS_DRAFT: _ClassVar[VersionStatus]
    VERSION_STATUS_PENDING: _ClassVar[VersionStatus]
    VERSION_STATUS_ACTIVE: _ClassVar[VersionStatus]
    VERSION_STATUS_DEPRECATED: _ClassVar[VersionStatus]
    VERSION_STATUS_ARCHIVED: _ClassVar[VersionStatus]
    VERSION_STATUS_DELETED: _ClassVar[VersionStatus]
    VERSION_STATUS_FAILED: _ClassVar[VersionStatus]
    VERSION_STATUS_CANCELLED: _ClassVar[VersionStatus]

VERSION_STATUS_UNSPECIFIED: VersionStatus
VERSION_STATUS_DRAFT: VersionStatus
VERSION_STATUS_PENDING: VersionStatus
VERSION_STATUS_ACTIVE: VersionStatus
VERSION_STATUS_DEPRECATED: VersionStatus
VERSION_STATUS_ARCHIVED: VersionStatus
VERSION_STATUS_DELETED: VersionStatus
VERSION_STATUS_FAILED: VersionStatus
VERSION_STATUS_CANCELLED: VersionStatus
