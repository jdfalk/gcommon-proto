from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TimeRangeFilter(_message.Message):
    __slots__ = ("start_time", "end_time", "granularity", "max_data_points")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    end_time: str
    granularity: str
    max_data_points: int
    def __init__(self, start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., granularity: _Optional[str] = ..., max_data_points: _Optional[int] = ...) -> None: ...
