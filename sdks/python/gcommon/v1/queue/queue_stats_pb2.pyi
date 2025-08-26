from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueStats(_message.Message):
    __slots__ = ("queue_name", "message_count", "total_bytes", "avg_message_size", "throughput", "current_depth", "peak_depth", "last_activity")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVG_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    PEAK_DEPTH_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    message_count: int
    total_bytes: int
    avg_message_size: float
    throughput: float
    current_depth: int
    peak_depth: int
    last_activity: _timestamp_pb2.Timestamp
    def __init__(self, queue_name: _Optional[str] = ..., message_count: _Optional[int] = ..., total_bytes: _Optional[int] = ..., avg_message_size: _Optional[float] = ..., throughput: _Optional[float] = ..., current_depth: _Optional[int] = ..., peak_depth: _Optional[int] = ..., last_activity: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
