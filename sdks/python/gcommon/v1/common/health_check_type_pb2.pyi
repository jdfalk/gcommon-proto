from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_CHECK_TYPE_UNSPECIFIED: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_HTTP: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_HTTPS: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_TCP: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_UDP: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_GRPC: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_DATABASE: _ClassVar[HealthCheckType]
    HEALTH_CHECK_TYPE_CUSTOM: _ClassVar[HealthCheckType]

HEALTH_CHECK_TYPE_UNSPECIFIED: HealthCheckType
HEALTH_CHECK_TYPE_HTTP: HealthCheckType
HEALTH_CHECK_TYPE_HTTPS: HealthCheckType
HEALTH_CHECK_TYPE_TCP: HealthCheckType
HEALTH_CHECK_TYPE_UDP: HealthCheckType
HEALTH_CHECK_TYPE_GRPC: HealthCheckType
HEALTH_CHECK_TYPE_DATABASE: HealthCheckType
HEALTH_CHECK_TYPE_CUSTOM: HealthCheckType
