from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResetHealthStatsResponse(_message.Message):
    __slots__ = ("success", "cleared_entries", "reset_at", "error", "reset_categories")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CLEARED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    RESET_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESET_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    success: bool
    cleared_entries: int
    reset_at: _timestamp_pb2.Timestamp
    error: _error_pb2.Error
    reset_categories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: bool = ..., cleared_entries: _Optional[int] = ..., reset_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., reset_categories: _Optional[_Iterable[str]] = ...) -> None: ...
