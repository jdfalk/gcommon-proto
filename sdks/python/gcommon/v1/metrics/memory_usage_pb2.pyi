from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MemoryUsage(_message.Message):
    __slots__ = ("used_bytes", "limit_bytes", "usage_percent", "peak_bytes")
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PEAK_BYTES_FIELD_NUMBER: _ClassVar[int]
    used_bytes: int
    limit_bytes: int
    usage_percent: float
    peak_bytes: int
    def __init__(self, used_bytes: _Optional[int] = ..., limit_bytes: _Optional[int] = ..., usage_percent: _Optional[float] = ..., peak_bytes: _Optional[int] = ...) -> None: ...
