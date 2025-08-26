from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricTypeCounts(_message.Message):
    __slots__ = ("counter_count", "gauge_count", "histogram_count", "summary_count", "timer_count", "custom_count")
    COUNTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    GAUGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMER_COUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COUNT_FIELD_NUMBER: _ClassVar[int]
    counter_count: int
    gauge_count: int
    histogram_count: int
    summary_count: int
    timer_count: int
    custom_count: int
    def __init__(self, counter_count: _Optional[int] = ..., gauge_count: _Optional[int] = ..., histogram_count: _Optional[int] = ..., summary_count: _Optional[int] = ..., timer_count: _Optional[int] = ..., custom_count: _Optional[int] = ...) -> None: ...
