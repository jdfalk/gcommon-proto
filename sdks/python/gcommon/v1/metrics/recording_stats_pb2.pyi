from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RecordingStats(_message.Message):
    __slots__ = ("processing_time_ms", "retry_count", "buffered", "persisted")
    PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUFFERED_FIELD_NUMBER: _ClassVar[int]
    PERSISTED_FIELD_NUMBER: _ClassVar[int]
    processing_time_ms: int
    retry_count: int
    buffered: bool
    persisted: bool
    def __init__(self, processing_time_ms: _Optional[int] = ..., retry_count: _Optional[int] = ..., buffered: _Optional[bool] = ..., persisted: _Optional[bool] = ...) -> None: ...
