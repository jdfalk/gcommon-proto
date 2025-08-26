import datetime

from gcommon.v1.metrics import percentile_measurement_pb2 as _percentile_measurement_pb2
from gcommon.v1.metrics import timer_statistics_pb2 as _timer_statistics_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimerMetric(_message.Message):
    __slots__ = ("timer_id", "name", "start_time", "end_time", "duration", "tags", "statistics", "is_running", "count", "total_duration", "percentiles", "recorded_at")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    PERCENTILES_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    tags: _containers.ScalarMap[str, str]
    statistics: _timer_statistics_pb2.TimerStatistics
    is_running: bool
    count: int
    total_duration: _duration_pb2.Duration
    percentiles: _containers.RepeatedCompositeFieldContainer[_percentile_measurement_pb2.PercentileMeasurement]
    recorded_at: _timestamp_pb2.Timestamp
    def __init__(self, timer_id: _Optional[str] = ..., name: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., statistics: _Optional[_Union[_timer_statistics_pb2.TimerStatistics, _Mapping]] = ..., is_running: _Optional[bool] = ..., count: _Optional[int] = ..., total_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., percentiles: _Optional[_Iterable[_Union[_percentile_measurement_pb2.PercentileMeasurement, _Mapping]]] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
