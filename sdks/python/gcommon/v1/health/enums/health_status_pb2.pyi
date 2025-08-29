from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATUS_UNSPECIFIED: _ClassVar[HealthStatus]
    HEALTH_STATUS_HEALTHY: _ClassVar[HealthStatus]
    HEALTH_STATUS_UNHEALTHY: _ClassVar[HealthStatus]
    HEALTH_STATUS_DEGRADED: _ClassVar[HealthStatus]
    HEALTH_STATUS_STARTING: _ClassVar[HealthStatus]
    HEALTH_STATUS_STOPPING: _ClassVar[HealthStatus]
    HEALTH_STATUS_UNKNOWN: _ClassVar[HealthStatus]
    HEALTH_STATUS_MAINTENANCE: _ClassVar[HealthStatus]
HEALTH_STATUS_UNSPECIFIED: HealthStatus
HEALTH_STATUS_HEALTHY: HealthStatus
HEALTH_STATUS_UNHEALTHY: HealthStatus
HEALTH_STATUS_DEGRADED: HealthStatus
HEALTH_STATUS_STARTING: HealthStatus
HEALTH_STATUS_STOPPING: HealthStatus
HEALTH_STATUS_UNKNOWN: HealthStatus
HEALTH_STATUS_MAINTENANCE: HealthStatus
