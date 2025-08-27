import datetime

from gcommon.v1.queue import queue_stats_pb2 as _queue_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueStatsPoint(_message.Message):
    __slots__ = ("timestamp", "stats")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    stats: _queue_stats_pb2.QueueStats
    def __init__(
        self,
        timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        stats: _Optional[_Union[_queue_stats_pb2.QueueStats, _Mapping]] = ...,
    ) -> None: ...
