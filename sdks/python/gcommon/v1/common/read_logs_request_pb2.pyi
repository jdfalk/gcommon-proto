from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReadLogsRequest(_message.Message):
    __slots__ = ("level", "source", "start_time", "end_time", "limit")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    level: str
    source: str
    start_time: int
    end_time: int
    limit: int
    def __init__(self, level: _Optional[str] = ..., source: _Optional[str] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...
