import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import gauge_metric_pb2 as _gauge_metric_pb2
from gcommon.v1.metrics import recording_stats_pb2 as _recording_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordGaugeResponse(_message.Message):
    __slots__ = (
        "success",
        "error",
        "metric",
        "previous_value",
        "recorded_at",
        "is_new_metric",
        "stats",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_METRIC_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    metric: _gauge_metric_pb2.GaugeMetric
    previous_value: float
    recorded_at: _timestamp_pb2.Timestamp
    is_new_metric: bool
    stats: _recording_stats_pb2.RecordingStats
    def __init__(
        self,
        success: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        metric: _Optional[_Union[_gauge_metric_pb2.GaugeMetric, _Mapping]] = ...,
        previous_value: _Optional[float] = ...,
        recorded_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        is_new_metric: _Optional[bool] = ...,
        stats: _Optional[_Union[_recording_stats_pb2.RecordingStats, _Mapping]] = ...,
    ) -> None: ...
