from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TimeRestriction(_message.Message):
    __slots__ = ("day_of_week", "start_time", "end_time", "timezone")
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    day_of_week: int
    start_time: str
    end_time: str
    timezone: str
    def __init__(self, day_of_week: _Optional[int] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., timezone: _Optional[str] = ...) -> None: ...
