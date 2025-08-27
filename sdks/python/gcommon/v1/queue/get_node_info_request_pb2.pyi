from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetNodeInfoRequest(_message.Message):
    __slots__ = (
        "node_id",
        "include_metrics",
        "include_health",
        "include_resources",
        "include_topology",
        "timeout_ms",
    )
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METRICS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEALTH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    include_metrics: bool
    include_health: bool
    include_resources: bool
    include_topology: bool
    timeout_ms: int
    def __init__(
        self,
        node_id: _Optional[str] = ...,
        include_metrics: _Optional[bool] = ...,
        include_health: _Optional[bool] = ...,
        include_resources: _Optional[bool] = ...,
        include_topology: _Optional[bool] = ...,
        timeout_ms: _Optional[int] = ...,
    ) -> None: ...
