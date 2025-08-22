from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncReplication(_message.Message):
    __slots__ = ("enabled", "min_sync_replicas", "sync_timeout_ms", "fallback_to_async")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_SYNC_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    SYNC_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TO_ASYNC_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    min_sync_replicas: int
    sync_timeout_ms: int
    fallback_to_async: bool
    def __init__(self, enabled: bool = ..., min_sync_replicas: _Optional[int] = ..., sync_timeout_ms: _Optional[int] = ..., fallback_to_async: bool = ...) -> None: ...
