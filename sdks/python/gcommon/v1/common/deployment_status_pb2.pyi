from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_STATUS_UNSPECIFIED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_PENDING: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_IN_PROGRESS: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_SUCCESS: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_FAILED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_ROLLED_BACK: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_CANCELLED: _ClassVar[DeploymentStatus]

DEPLOYMENT_STATUS_UNSPECIFIED: DeploymentStatus
DEPLOYMENT_STATUS_PENDING: DeploymentStatus
DEPLOYMENT_STATUS_IN_PROGRESS: DeploymentStatus
DEPLOYMENT_STATUS_SUCCESS: DeploymentStatus
DEPLOYMENT_STATUS_FAILED: DeploymentStatus
DEPLOYMENT_STATUS_ROLLED_BACK: DeploymentStatus
DEPLOYMENT_STATUS_CANCELLED: DeploymentStatus
