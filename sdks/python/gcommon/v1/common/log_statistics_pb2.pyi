from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LogStatistics(_message.Message):
    __slots__ = ("total_entries", "entries_per_second", "average_size", "total_size", "error_count", "warning_count")
    TOTAL_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    WARNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_entries: int
    entries_per_second: float
    average_size: int
    total_size: int
    error_count: int
    warning_count: int
    def __init__(self, total_entries: _Optional[int] = ..., entries_per_second: _Optional[float] = ..., average_size: _Optional[int] = ..., total_size: _Optional[int] = ..., error_count: _Optional[int] = ..., warning_count: _Optional[int] = ...) -> None: ...
