from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimerStatistics(_message.Message):
    __slots__ = ("min_duration", "max_duration", "mean_duration", "standard_deviation_ms", "variance_ms", "sample_count", "rate_per_second", "last_duration")
    MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    MEAN_DURATION_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_MS_FIELD_NUMBER: _ClassVar[int]
    VARIANCE_MS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RATE_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    LAST_DURATION_FIELD_NUMBER: _ClassVar[int]
    min_duration: _duration_pb2.Duration
    max_duration: _duration_pb2.Duration
    mean_duration: _duration_pb2.Duration
    standard_deviation_ms: float
    variance_ms: float
    sample_count: int
    rate_per_second: float
    last_duration: _duration_pb2.Duration
    def __init__(self, min_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mean_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., standard_deviation_ms: _Optional[float] = ..., variance_ms: _Optional[float] = ..., sample_count: _Optional[int] = ..., rate_per_second: _Optional[float] = ..., last_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
