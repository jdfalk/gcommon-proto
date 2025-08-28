from gcommon.v1.database import pool_stats_pb2 as _pool_stats_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionPoolInfo(_message.Message):
    __slots__ = ("max_connections", "active_connections", "idle_connections", "avg_lifetime", "stats")
    MAX_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    IDLE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    AVG_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    max_connections: int
    active_connections: int
    idle_connections: int
    avg_lifetime: _duration_pb2.Duration
    stats: _pool_stats_pb2.PoolStats
    def __init__(self, max_connections: _Optional[int] = ..., active_connections: _Optional[int] = ..., idle_connections: _Optional[int] = ..., avg_lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., stats: _Optional[_Union[_pool_stats_pb2.PoolStats, _Mapping]] = ...) -> None: ...
