from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENVIRONMENT_TYPE_UNSPECIFIED: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_DEVELOPMENT: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_TESTING: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_STAGING: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_PRODUCTION: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_SANDBOX: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_CANARY: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_DISASTER_RECOVERY: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_INTEGRATION: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_PERFORMANCE: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_SECURITY: _ClassVar[EnvironmentType]
ENVIRONMENT_TYPE_UNSPECIFIED: EnvironmentType
ENVIRONMENT_TYPE_DEVELOPMENT: EnvironmentType
ENVIRONMENT_TYPE_TESTING: EnvironmentType
ENVIRONMENT_TYPE_STAGING: EnvironmentType
ENVIRONMENT_TYPE_PRODUCTION: EnvironmentType
ENVIRONMENT_TYPE_SANDBOX: EnvironmentType
ENVIRONMENT_TYPE_CANARY: EnvironmentType
ENVIRONMENT_TYPE_DISASTER_RECOVERY: EnvironmentType
ENVIRONMENT_TYPE_INTEGRATION: EnvironmentType
ENVIRONMENT_TYPE_PERFORMANCE: EnvironmentType
ENVIRONMENT_TYPE_SECURITY: EnvironmentType
