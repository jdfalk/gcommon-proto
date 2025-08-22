from gcommon.v1.common import metrics_error_stats_pb2 as _metrics_error_stats_pb2
from gcommon.v1.common import metrics_retention_info_pb2 as _metrics_retention_info_pb2
from gcommon.v1.metrics import export_status_pb2 as _export_status_pb2
from gcommon.v1.metrics import metric_type_counts_pb2 as _metric_type_counts_pb2
from gcommon.v1.metrics import performance_stats_pb2 as _performance_stats_pb2
from gcommon.v1.metrics import top_metrics_pb2 as _top_metrics_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsSummary(_message.Message):
    __slots__ = ("total_metrics", "total_data_points", "total_data_volume_bytes", "type_counts", "performance", "errors", "top_metrics", "retention", "export_status")
    TOTAL_METRICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_VOLUME_BYTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    TOP_METRICS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    EXPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    total_metrics: int
    total_data_points: int
    total_data_volume_bytes: int
    type_counts: _metric_type_counts_pb2.MetricTypeCounts
    performance: _performance_stats_pb2.MetricsPerformanceStats
    errors: _metrics_error_stats_pb2.MetricsErrorStats
    top_metrics: _top_metrics_pb2.TopMetrics
    retention: _metrics_retention_info_pb2.MetricsRetentionInfo
    export_status: _export_status_pb2.ExportStatus
    def __init__(self, total_metrics: _Optional[int] = ..., total_data_points: _Optional[int] = ..., total_data_volume_bytes: _Optional[int] = ..., type_counts: _Optional[_Union[_metric_type_counts_pb2.MetricTypeCounts, _Mapping]] = ..., performance: _Optional[_Union[_performance_stats_pb2.MetricsPerformanceStats, _Mapping]] = ..., errors: _Optional[_Union[_metrics_error_stats_pb2.MetricsErrorStats, _Mapping]] = ..., top_metrics: _Optional[_Union[_top_metrics_pb2.TopMetrics, _Mapping]] = ..., retention: _Optional[_Union[_metrics_retention_info_pb2.MetricsRetentionInfo, _Mapping]] = ..., export_status: _Optional[_Union[_export_status_pb2.ExportStatus, _Mapping]] = ...) -> None: ...
