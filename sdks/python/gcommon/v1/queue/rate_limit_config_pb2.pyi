from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueueRateLimitConfig(_message.Message):
    __slots__ = ("max_per_second", "burst", "enabled")
    MAX_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    BURST_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    max_per_second: int
    burst: int
    enabled: bool
    def __init__(self, max_per_second: _Optional[int] = ..., burst: _Optional[int] = ..., enabled: _Optional[bool] = ...) -> None: ...
