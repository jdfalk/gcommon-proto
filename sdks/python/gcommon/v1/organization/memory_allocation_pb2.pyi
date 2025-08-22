from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MemoryAllocation(_message.Message):
    __slots__ = ("size_mb", "usage_limit_percent", "swap_mb")
    SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    USAGE_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SWAP_MB_FIELD_NUMBER: _ClassVar[int]
    size_mb: int
    usage_limit_percent: int
    swap_mb: int
    def __init__(self, size_mb: _Optional[int] = ..., usage_limit_percent: _Optional[int] = ..., swap_mb: _Optional[int] = ...) -> None: ...
