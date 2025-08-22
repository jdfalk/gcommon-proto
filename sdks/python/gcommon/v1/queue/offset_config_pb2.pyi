from gcommon.v1.queue import offset_type_pb2 as _offset_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetConfig(_message.Message):
    __slots__ = ("offset_type", "offset_value", "start_timestamp", "reset_on_not_found")
    OFFSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_VALUE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESET_ON_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    offset_type: _offset_type_pb2.OffsetType
    offset_value: int
    start_timestamp: _timestamp_pb2.Timestamp
    reset_on_not_found: bool
    def __init__(self, offset_type: _Optional[_Union[_offset_type_pb2.OffsetType, str]] = ..., offset_value: _Optional[int] = ..., start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reset_on_not_found: bool = ...) -> None: ...
