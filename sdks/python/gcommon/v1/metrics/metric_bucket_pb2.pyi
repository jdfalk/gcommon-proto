from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricBucket(_message.Message):
    __slots__ = ("lower_bound", "upper_bound", "count")
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    lower_bound: float
    upper_bound: float
    count: int
    def __init__(self, lower_bound: _Optional[float] = ..., upper_bound: _Optional[float] = ..., count: _Optional[int] = ...) -> None: ...
