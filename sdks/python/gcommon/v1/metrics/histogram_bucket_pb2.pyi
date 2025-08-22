from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramBucket(_message.Message):
    __slots__ = ("upper_bound", "count", "cumulative_count")
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    upper_bound: float
    count: int
    cumulative_count: int
    def __init__(self, upper_bound: _Optional[float] = ..., count: _Optional[int] = ..., cumulative_count: _Optional[int] = ...) -> None: ...
