from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionInfo(_message.Message):
    __slots__ = (
        "partition_id",
        "leader_node",
        "replica_nodes",
        "current_offset",
        "earliest_offset",
        "message_count",
        "size_bytes",
        "is_online",
    )
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    LEADER_NODE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NODES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    leader_node: str
    replica_nodes: _containers.RepeatedScalarFieldContainer[str]
    current_offset: int
    earliest_offset: int
    message_count: int
    size_bytes: int
    is_online: bool
    def __init__(
        self,
        partition_id: _Optional[int] = ...,
        leader_node: _Optional[str] = ...,
        replica_nodes: _Optional[_Iterable[str]] = ...,
        current_offset: _Optional[int] = ...,
        earliest_offset: _Optional[int] = ...,
        message_count: _Optional[int] = ...,
        size_bytes: _Optional[int] = ...,
        is_online: _Optional[bool] = ...,
    ) -> None: ...
