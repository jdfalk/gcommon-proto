from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterConfig(_message.Message):
    __slots__ = ("quorum_size", "replication_factor", "heartbeat_interval", "election_timeout")
    QUORUM_SIZE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ELECTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    quorum_size: int
    replication_factor: int
    heartbeat_interval: int
    election_timeout: int
    def __init__(self, quorum_size: _Optional[int] = ..., replication_factor: _Optional[int] = ..., heartbeat_interval: _Optional[int] = ..., election_timeout: _Optional[int] = ...) -> None: ...
