import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import time_range_metrics_pb2 as _time_range_metrics_pb2
from gcommon.v1.metrics import metrics_health_info_pb2 as _metrics_health_info_pb2
from gcommon.v1.metrics import metrics_summary_pb2 as _metrics_summary_pb2
from gcommon.v1.metrics import provider_summary_pb2 as _provider_summary_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricsSummaryResponse(_message.Message):
    __slots__ = ("success", "error", "summary", "provider_summaries", "health_status", "generated_at", "time_range", "warnings")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    summary: _metrics_summary_pb2.MetricsSummary
    provider_summaries: _containers.RepeatedCompositeFieldContainer[_provider_summary_pb2.ProviderSummary]
    health_status: _metrics_health_info_pb2.MetricsHealthInfo
    generated_at: _timestamp_pb2.Timestamp
    time_range: _time_range_metrics_pb2.TimeRangeMetrics
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: _Optional[bool] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., summary: _Optional[_Union[_metrics_summary_pb2.MetricsSummary, _Mapping]] = ..., provider_summaries: _Optional[_Iterable[_Union[_provider_summary_pb2.ProviderSummary, _Mapping]]] = ..., health_status: _Optional[_Union[_metrics_health_info_pb2.MetricsHealthInfo, _Mapping]] = ..., generated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_range: _Optional[_Union[_time_range_metrics_pb2.TimeRangeMetrics, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
