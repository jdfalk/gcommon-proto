from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_STATE_UNSPECIFIED: _ClassVar[ClusterState]
    CLUSTER_STATE_HEALTHY: _ClassVar[ClusterState]
    CLUSTER_STATE_DEGRADED: _ClassVar[ClusterState]
    CLUSTER_STATE_RECOVERING: _ClassVar[ClusterState]
    CLUSTER_STATE_DOWN: _ClassVar[ClusterState]
    CLUSTER_STATE_MAINTENANCE: _ClassVar[ClusterState]

CLUSTER_STATE_UNSPECIFIED: ClusterState
CLUSTER_STATE_HEALTHY: ClusterState
CLUSTER_STATE_DEGRADED: ClusterState
CLUSTER_STATE_RECOVERING: ClusterState
CLUSTER_STATE_DOWN: ClusterState
CLUSTER_STATE_MAINTENANCE: ClusterState
