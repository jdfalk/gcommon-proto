from gcommon.v1.queue import node_state_pb2 as _node_state_pb2
from gcommon.v1.queue import node_stats_pb2 as _node_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeInfo(_message.Message):
    __slots__ = ("node_id", "hostname", "port", "state", "roles", "last_heartbeat", "stats")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    hostname: str
    port: int
    state: _node_state_pb2.NodeState
    roles: _containers.RepeatedScalarFieldContainer[str]
    last_heartbeat: _timestamp_pb2.Timestamp
    stats: _node_stats_pb2.NodeStats
    def __init__(self, node_id: _Optional[str] = ..., hostname: _Optional[str] = ..., port: _Optional[int] = ..., state: _Optional[_Union[_node_state_pb2.NodeState, str]] = ..., roles: _Optional[_Iterable[str]] = ..., last_heartbeat: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stats: _Optional[_Union[_node_stats_pb2.NodeStats, _Mapping]] = ...) -> None: ...
