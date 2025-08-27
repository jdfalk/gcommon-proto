from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import recording_stats_pb2 as _recording_stats_pb2
from gcommon.v1.metrics import summary_metric_pb2 as _summary_metric_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordSummaryResponse(_message.Message):
    __slots__ = ("metric", "stats", "error")
    METRIC_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    metric: _summary_metric_pb2.SummaryMetric
    stats: _recording_stats_pb2.RecordingStats
    error: _error_pb2.Error
    def __init__(self, metric: _Optional[_Union[_summary_metric_pb2.SummaryMetric, _Mapping]] = ..., stats: _Optional[_Union[_recording_stats_pb2.RecordingStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
