from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationConfig(_message.Message):
    __slots__ = ("replica_count", "factor", "synchronous", "min_in_sync_replicas")
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONOUS_FIELD_NUMBER: _ClassVar[int]
    MIN_IN_SYNC_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    replica_count: int
    factor: int
    synchronous: bool
    min_in_sync_replicas: int
    def __init__(self, replica_count: _Optional[int] = ..., factor: _Optional[int] = ..., synchronous: _Optional[bool] = ..., min_in_sync_replicas: _Optional[int] = ...) -> None: ...
