from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetClusterInfoRequest(_message.Message):
    __slots__ = ("include_nodes", "include_metrics", "include_health", "include_resources", "include_topology", "timeout_ms")
    INCLUDE_NODES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METRICS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEALTH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    include_nodes: bool
    include_metrics: bool
    include_health: bool
    include_resources: bool
    include_topology: bool
    timeout_ms: int
    def __init__(self, include_nodes: bool = ..., include_metrics: bool = ..., include_health: bool = ..., include_resources: bool = ..., include_topology: bool = ..., timeout_ms: _Optional[int] = ...) -> None: ...
