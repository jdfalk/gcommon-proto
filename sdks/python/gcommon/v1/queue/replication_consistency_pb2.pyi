from gcommon.v1.common import replication_level_pb2 as _replication_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationConsistency(_message.Message):
    __slots__ = ("min_write_replicas", "min_read_replicas", "replication_factor", "replication_level", "anti_entropy_enabled", "repair_interval_seconds")
    MIN_WRITE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MIN_READ_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ANTI_ENTROPY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REPAIR_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    min_write_replicas: int
    min_read_replicas: int
    replication_factor: int
    replication_level: _replication_level_pb2.ReplicationLevel
    anti_entropy_enabled: bool
    repair_interval_seconds: int
    def __init__(self, min_write_replicas: _Optional[int] = ..., min_read_replicas: _Optional[int] = ..., replication_factor: _Optional[int] = ..., replication_level: _Optional[_Union[_replication_level_pb2.ReplicationLevel, str]] = ..., anti_entropy_enabled: bool = ..., repair_interval_seconds: _Optional[int] = ...) -> None: ...
