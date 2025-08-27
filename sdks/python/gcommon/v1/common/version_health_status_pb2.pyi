from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VersionHealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_HEALTH_STATUS_UNSPECIFIED: _ClassVar[VersionHealthStatus]
    VERSION_HEALTH_STATUS_HEALTHY: _ClassVar[VersionHealthStatus]
    VERSION_HEALTH_STATUS_DEGRADED: _ClassVar[VersionHealthStatus]
    VERSION_HEALTH_STATUS_UNHEALTHY: _ClassVar[VersionHealthStatus]
    VERSION_HEALTH_STATUS_UNKNOWN: _ClassVar[VersionHealthStatus]

VERSION_HEALTH_STATUS_UNSPECIFIED: VersionHealthStatus
VERSION_HEALTH_STATUS_HEALTHY: VersionHealthStatus
VERSION_HEALTH_STATUS_DEGRADED: VersionHealthStatus
VERSION_HEALTH_STATUS_UNHEALTHY: VersionHealthStatus
VERSION_HEALTH_STATUS_UNKNOWN: VersionHealthStatus
