from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricStats(_message.Message):
    __slots__ = ("min", "max", "average", "sum", "count")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    average: float
    sum: float
    count: int
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., average: _Optional[float] = ..., sum: _Optional[float] = ..., count: _Optional[int] = ...) -> None: ...
