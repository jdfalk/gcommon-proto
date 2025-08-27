from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENVIRONMENT_STATUS_UNSPECIFIED: _ClassVar[EnvironmentStatus]
    ENVIRONMENT_STATUS_ACTIVE: _ClassVar[EnvironmentStatus]
    ENVIRONMENT_STATUS_INACTIVE: _ClassVar[EnvironmentStatus]
    ENVIRONMENT_STATUS_MAINTENANCE: _ClassVar[EnvironmentStatus]
    ENVIRONMENT_STATUS_DEPRECATED: _ClassVar[EnvironmentStatus]
    ENVIRONMENT_STATUS_ARCHIVED: _ClassVar[EnvironmentStatus]
    ENVIRONMENT_STATUS_ERROR: _ClassVar[EnvironmentStatus]

ENVIRONMENT_STATUS_UNSPECIFIED: EnvironmentStatus
ENVIRONMENT_STATUS_ACTIVE: EnvironmentStatus
ENVIRONMENT_STATUS_INACTIVE: EnvironmentStatus
ENVIRONMENT_STATUS_MAINTENANCE: EnvironmentStatus
ENVIRONMENT_STATUS_DEPRECATED: EnvironmentStatus
ENVIRONMENT_STATUS_ARCHIVED: EnvironmentStatus
ENVIRONMENT_STATUS_ERROR: EnvironmentStatus
