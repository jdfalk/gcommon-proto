from gcommon.v1.queue import queue_stats_pb2 as _queue_stats_pb2
from gcommon.v1.queue import queue_stats_point_pb2 as _queue_stats_point_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueStatsResponse(_message.Message):
    __slots__ = ("stats", "time_series")
    STATS_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    stats: _queue_stats_pb2.QueueStats
    time_series: _containers.RepeatedCompositeFieldContainer[_queue_stats_point_pb2.QueueStatsPoint]
    def __init__(self, stats: _Optional[_Union[_queue_stats_pb2.QueueStats, _Mapping]] = ..., time_series: _Optional[_Iterable[_Union[_queue_stats_point_pb2.QueueStatsPoint, _Mapping]]] = ...) -> None: ...
