from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionAssignment(_message.Message):
    __slots__ = ("partition_id", "consumer_id", "current_offset", "committed_offset", "high_water_mark", "assigned_at", "last_commit")
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    HIGH_WATER_MARK_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMIT_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    consumer_id: str
    current_offset: int
    committed_offset: int
    high_water_mark: int
    assigned_at: _timestamp_pb2.Timestamp
    last_commit: _timestamp_pb2.Timestamp
    def __init__(self, partition_id: _Optional[int] = ..., consumer_id: _Optional[str] = ..., current_offset: _Optional[int] = ..., committed_offset: _Optional[int] = ..., high_water_mark: _Optional[int] = ..., assigned_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_commit: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
