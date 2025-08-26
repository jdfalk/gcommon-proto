from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DailyUsage(_message.Message):
    __slots__ = ("date", "request_count")
    DATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    date: str
    request_count: int
    def __init__(self, date: _Optional[str] = ..., request_count: _Optional[int] = ...) -> None: ...
