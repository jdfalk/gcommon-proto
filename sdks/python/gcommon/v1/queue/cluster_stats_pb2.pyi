from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterStats(_message.Message):
    __slots__ = ("total_queues", "total_messages", "total_throughput", "active_connections")
    TOTAL_QUEUES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    total_queues: int
    total_messages: int
    total_throughput: float
    active_connections: int
    def __init__(self, total_queues: _Optional[int] = ..., total_messages: _Optional[int] = ..., total_throughput: _Optional[float] = ..., active_connections: _Optional[int] = ...) -> None: ...
