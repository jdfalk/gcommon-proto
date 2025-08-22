from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import time_range_metrics_pb2 as _time_range_metrics_pb2
from gcommon.v1.metrics import metric_data_pb2 as _metric_data_pb2
from gcommon.v1.metrics import metric_metadata_pb2 as _metric_metadata_pb2
from gcommon.v1.metrics import pagination_info_pb2 as _pagination_info_pb2
from gcommon.v1.metrics import query_stats_pb2 as _query_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsGetMetricsResponse(_message.Message):
    __slots__ = ("success", "error", "metrics", "metadata", "pagination", "stats", "generated_at", "time_range", "warnings", "provider_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    metrics: _containers.RepeatedCompositeFieldContainer[_metric_data_pb2.MetricData]
    metadata: _containers.RepeatedCompositeFieldContainer[_metric_metadata_pb2.MetricMetadata]
    pagination: _pagination_info_pb2.MetricsPaginationInfo
    stats: _query_stats_pb2.MetricsQueryStats
    generated_at: _timestamp_pb2.Timestamp
    time_range: _time_range_metrics_pb2.TimeRangeMetrics
    warnings: _containers.RepeatedScalarFieldContainer[str]
    provider_id: str
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[_metric_data_pb2.MetricData, _Mapping]]] = ..., metadata: _Optional[_Iterable[_Union[_metric_metadata_pb2.MetricMetadata, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_info_pb2.MetricsPaginationInfo, _Mapping]] = ..., stats: _Optional[_Union[_query_stats_pb2.MetricsQueryStats, _Mapping]] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_range: _Optional[_Union[_time_range_metrics_pb2.TimeRangeMetrics, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., provider_id: _Optional[str] = ...) -> None: ...
