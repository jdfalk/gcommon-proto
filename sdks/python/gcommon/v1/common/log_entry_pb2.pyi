import datetime

from gcommon.v1.common import error_info_pb2 as _error_info_pb2
from gcommon.v1.common import log_level_pb2 as _log_level_pb2
from gcommon.v1.common import source_location_pb2 as _source_location_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogEntry(_message.Message):
    __slots__ = ("level", "message", "timestamp", "logger", "thread", "source", "fields", "tags", "trace_id", "span_id", "user_id", "request_id", "error_info")
    class FieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOGGER_FIELD_NUMBER: _ClassVar[int]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    level: _log_level_pb2.LogLevel
    message: str
    timestamp: _timestamp_pb2.Timestamp
    logger: str
    thread: str
    source: _source_location_pb2.SourceLocation
    fields: _containers.MessageMap[str, _any_pb2.Any]
    tags: _containers.RepeatedScalarFieldContainer[str]
    trace_id: str
    span_id: str
    user_id: str
    request_id: str
    error_info: _error_info_pb2.ErrorInfo
    def __init__(self, level: _Optional[_Union[_log_level_pb2.LogLevel, str]] = ..., message: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., logger: _Optional[str] = ..., thread: _Optional[str] = ..., source: _Optional[_Union[_source_location_pb2.SourceLocation, _Mapping]] = ..., fields: _Optional[_Mapping[str, _any_pb2.Any]] = ..., tags: _Optional[_Iterable[str]] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., user_id: _Optional[str] = ..., request_id: _Optional[str] = ..., error_info: _Optional[_Union[_error_info_pb2.ErrorInfo, _Mapping]] = ...) -> None: ...
