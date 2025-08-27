from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CommonHealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATUS_UNSPECIFIED: _ClassVar[CommonHealthStatus]
    HEALTH_STATUS_HEALTHY: _ClassVar[CommonHealthStatus]
    HEALTH_STATUS_UNHEALTHY: _ClassVar[CommonHealthStatus]
    HEALTH_STATUS_DEGRADED: _ClassVar[CommonHealthStatus]
    HEALTH_STATUS_STARTING: _ClassVar[CommonHealthStatus]
    HEALTH_STATUS_STOPPING: _ClassVar[CommonHealthStatus]

HEALTH_STATUS_UNSPECIFIED: CommonHealthStatus
HEALTH_STATUS_HEALTHY: CommonHealthStatus
HEALTH_STATUS_UNHEALTHY: CommonHealthStatus
HEALTH_STATUS_DEGRADED: CommonHealthStatus
HEALTH_STATUS_STARTING: CommonHealthStatus
HEALTH_STATUS_STOPPING: CommonHealthStatus
