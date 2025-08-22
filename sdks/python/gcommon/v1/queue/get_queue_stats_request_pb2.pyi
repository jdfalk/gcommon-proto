from gcommon.v1.common import stats_granularity_pb2 as _stats_granularity_pb2
from gcommon.v1.metrics import time_range_pb2 as _time_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueueStatsRequest(_message.Message):
    __slots__ = ("queue_name", "time_range", "granularity")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    time_range: _time_range_pb2.MetricsTimeRange
    granularity: _stats_granularity_pb2.StatsGranularity
    def __init__(self, queue_name: _Optional[str] = ..., time_range: _Optional[_Union[_time_range_pb2.MetricsTimeRange, _Mapping]] = ..., granularity: _Optional[_Union[_stats_granularity_pb2.StatsGranularity, str]] = ...) -> None: ...
