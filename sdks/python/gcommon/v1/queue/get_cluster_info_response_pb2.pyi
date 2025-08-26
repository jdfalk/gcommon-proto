from gcommon.v1.queue import cluster_info_pb2 as _cluster_info_pb2
from gcommon.v1.queue import node_info_pb2 as _node_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetClusterInfoResponse(_message.Message):
    __slots__ = ("cluster_info", "nodes", "is_healthy", "warnings", "error_message")
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    IS_HEALTHY_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    cluster_info: _cluster_info_pb2.ClusterInfo
    nodes: _containers.RepeatedCompositeFieldContainer[_node_info_pb2.NodeInfo]
    is_healthy: bool
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error_message: str
    def __init__(self, cluster_info: _Optional[_Union[_cluster_info_pb2.ClusterInfo, _Mapping]] = ..., nodes: _Optional[_Iterable[_Union[_node_info_pb2.NodeInfo, _Mapping]]] = ..., is_healthy: _Optional[bool] = ..., warnings: _Optional[_Iterable[str]] = ..., error_message: _Optional[str] = ...) -> None: ...
