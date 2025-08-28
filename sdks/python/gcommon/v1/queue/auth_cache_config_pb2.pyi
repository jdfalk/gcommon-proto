from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthCacheConfig(_message.Message):
    __slots__ = ("enabled", "ttl_seconds", "max_size", "cleanup_interval_seconds")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    ttl_seconds: int
    max_size: int
    cleanup_interval_seconds: int
    def __init__(self, enabled: bool = ..., ttl_seconds: _Optional[int] = ..., max_size: _Optional[int] = ..., cleanup_interval_seconds: _Optional[int] = ...) -> None: ...
