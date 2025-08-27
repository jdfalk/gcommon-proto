from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramStats(_message.Message):
    __slots__ = ("total_count", "total_sum", "mean", "min_value", "max_value", "std_deviation")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SUM_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    STD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    total_sum: float
    mean: float
    min_value: float
    max_value: float
    std_deviation: float
    def __init__(self, total_count: _Optional[int] = ..., total_sum: _Optional[float] = ..., mean: _Optional[float] = ..., min_value: _Optional[float] = ..., max_value: _Optional[float] = ..., std_deviation: _Optional[float] = ...) -> None: ...
