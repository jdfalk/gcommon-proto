from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TimestampConfig(_message.Message):
    __slots__ = ("source", "sync_interval_seconds", "max_skew_ms")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SYNC_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_SKEW_MS_FIELD_NUMBER: _ClassVar[int]
    source: str
    sync_interval_seconds: int
    max_skew_ms: int
    def __init__(self, source: _Optional[str] = ..., sync_interval_seconds: _Optional[int] = ..., max_skew_ms: _Optional[int] = ...) -> None: ...
