import datetime

from gcommon.v1.metrics import histogram_value_pb2 as _histogram_value_pb2
from gcommon.v1.metrics import summary_value_pb2 as _summary_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricValue(_message.Message):
    __slots__ = ("timestamp", "double_value", "int_value", "string_value", "bool_value", "histogram_value", "summary_value", "labels", "sample_count")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_VALUE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    double_value: float
    int_value: int
    string_value: str
    bool_value: bool
    histogram_value: _histogram_value_pb2.HistogramValue
    summary_value: _summary_value_pb2.SummaryValue
    labels: _containers.ScalarMap[str, str]
    sample_count: int
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., double_value: _Optional[float] = ..., int_value: _Optional[int] = ..., string_value: _Optional[str] = ..., bool_value: _Optional[bool] = ..., histogram_value: _Optional[_Union[_histogram_value_pb2.HistogramValue, _Mapping]] = ..., summary_value: _Optional[_Union[_summary_value_pb2.SummaryValue, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., sample_count: _Optional[int] = ...) -> None: ...
