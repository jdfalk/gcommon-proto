from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RateLimits(_message.Message):
    __slots__ = ("requests_per_second", "burst_size", "window_seconds")
    REQUESTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    BURST_SIZE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    requests_per_second: int
    burst_size: int
    window_seconds: int
    def __init__(self, requests_per_second: _Optional[int] = ..., burst_size: _Optional[int] = ..., window_seconds: _Optional[int] = ...) -> None: ...
