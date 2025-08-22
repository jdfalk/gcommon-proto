from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VersionDeploymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_DEPLOYMENT_STATUS_UNSPECIFIED: _ClassVar[VersionDeploymentStatus]
    VERSION_DEPLOYMENT_STATUS_PENDING: _ClassVar[VersionDeploymentStatus]
    VERSION_DEPLOYMENT_STATUS_IN_PROGRESS: _ClassVar[VersionDeploymentStatus]
    VERSION_DEPLOYMENT_STATUS_SUCCESS: _ClassVar[VersionDeploymentStatus]
    VERSION_DEPLOYMENT_STATUS_FAILED: _ClassVar[VersionDeploymentStatus]
    VERSION_DEPLOYMENT_STATUS_ROLLED_BACK: _ClassVar[VersionDeploymentStatus]
    VERSION_DEPLOYMENT_STATUS_CANCELLED: _ClassVar[VersionDeploymentStatus]
VERSION_DEPLOYMENT_STATUS_UNSPECIFIED: VersionDeploymentStatus
VERSION_DEPLOYMENT_STATUS_PENDING: VersionDeploymentStatus
VERSION_DEPLOYMENT_STATUS_IN_PROGRESS: VersionDeploymentStatus
VERSION_DEPLOYMENT_STATUS_SUCCESS: VersionDeploymentStatus
VERSION_DEPLOYMENT_STATUS_FAILED: VersionDeploymentStatus
VERSION_DEPLOYMENT_STATUS_ROLLED_BACK: VersionDeploymentStatus
VERSION_DEPLOYMENT_STATUS_CANCELLED: VersionDeploymentStatus
