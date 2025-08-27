import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import bucket_info_pb2 as _bucket_info_pb2
from gcommon.v1.metrics import histogram_metric_pb2 as _histogram_metric_pb2
from gcommon.v1.metrics import histogram_stats_pb2 as _histogram_stats_pb2
from gcommon.v1.metrics import recording_stats_pb2 as _recording_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordHistogramResponse(_message.Message):
    __slots__ = (
        "success",
        "error",
        "metric",
        "current_stats",
        "recorded_at",
        "is_new_metric",
        "affected_bucket",
        "recording_stats",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATS_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_METRIC_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_BUCKET_FIELD_NUMBER: _ClassVar[int]
    RECORDING_STATS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    metric: _histogram_metric_pb2.HistogramMetric
    current_stats: _histogram_stats_pb2.HistogramStats
    recorded_at: _timestamp_pb2.Timestamp
    is_new_metric: bool
    affected_bucket: _bucket_info_pb2.BucketInfo
    recording_stats: _recording_stats_pb2.RecordingStats
    def __init__(
        self,
        success: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        metric: _Optional[
            _Union[_histogram_metric_pb2.HistogramMetric, _Mapping]
        ] = ...,
        current_stats: _Optional[
            _Union[_histogram_stats_pb2.HistogramStats, _Mapping]
        ] = ...,
        recorded_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        is_new_metric: _Optional[bool] = ...,
        affected_bucket: _Optional[_Union[_bucket_info_pb2.BucketInfo, _Mapping]] = ...,
        recording_stats: _Optional[
            _Union[_recording_stats_pb2.RecordingStats, _Mapping]
        ] = ...,
    ) -> None: ...
