from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResetQueueStatsRequest(_message.Message):
    __slots__ = ("queue_name", "stat_types", "partition_ids", "preserve_before_timestamp", "timeout_ms")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    STAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_BEFORE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    stat_types: _containers.RepeatedScalarFieldContainer[str]
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    preserve_before_timestamp: int
    timeout_ms: int
    def __init__(self, queue_name: _Optional[str] = ..., stat_types: _Optional[_Iterable[str]] = ..., partition_ids: _Optional[_Iterable[int]] = ..., preserve_before_timestamp: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
