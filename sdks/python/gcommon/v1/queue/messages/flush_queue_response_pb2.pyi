from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FlushQueueResponse(_message.Message):
    __slots__ = ("success", "messages_flushed", "bytes_flushed", "flush_duration_ms", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FLUSHED_FIELD_NUMBER: _ClassVar[int]
    BYTES_FLUSHED_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    messages_flushed: int
    bytes_flushed: int
    flush_duration_ms: int
    error: str
    def __init__(self, success: bool = ..., messages_flushed: _Optional[int] = ..., bytes_flushed: _Optional[int] = ..., flush_duration_ms: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
