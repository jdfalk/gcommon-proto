from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetInfo(_message.Message):
    __slots__ = ("offset", "partition_id", "timestamp", "message_size", "is_valid", "consumer_group", "committed_offset")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int
    partition_id: int
    timestamp: _timestamp_pb2.Timestamp
    message_size: int
    is_valid: bool
    consumer_group: str
    committed_offset: int
    def __init__(self, offset: _Optional[int] = ..., partition_id: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message_size: _Optional[int] = ..., is_valid: bool = ..., consumer_group: _Optional[str] = ..., committed_offset: _Optional[int] = ...) -> None: ...
