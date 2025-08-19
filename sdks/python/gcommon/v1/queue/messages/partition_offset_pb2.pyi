from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionOffset(_message.Message):
    __slots__ = ("partition_id", "offset", "offset_timestamp", "high_water_mark")
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    OFFSET_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HIGH_WATER_MARK_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    offset: int
    offset_timestamp: _timestamp_pb2.Timestamp
    high_water_mark: int
    def __init__(self, partition_id: _Optional[int] = ..., offset: _Optional[int] = ..., offset_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., high_water_mark: _Optional[int] = ...) -> None: ...
