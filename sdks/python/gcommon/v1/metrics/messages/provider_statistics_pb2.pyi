from gcommon.v1.metrics.messages import configuration_summary_pb2 as _configuration_summary_pb2
from gcommon.v1.metrics.messages import data_volume_stats_pb2 as _data_volume_stats_pb2
from gcommon.v1.metrics.messages import error_stats_pb2 as _error_stats_pb2
from gcommon.v1.metrics.messages import export_stats_pb2 as _export_stats_pb2
from gcommon.v1.metrics.messages import health_status_entry_pb2 as _health_status_entry_pb2
from gcommon.v1.metrics.messages import performance_stats_pb2 as _performance_stats_pb2
from gcommon.v1.metrics.messages import provider_info_pb2 as _provider_info_pb2
from gcommon.v1.metrics.messages import resource_usage_stats_pb2 as _resource_usage_stats_pb2
from gcommon.v1.metrics.messages import top_metrics_pb2 as _top_metrics_pb2
from gcommon.v1.metrics.messages import trend_analysis_pb2 as _trend_analysis_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderStatistics(_message.Message):
    __slots__ = ("provider_info", "performance", "resource_usage", "errors", "data_volume", "exports", "health_history", "config", "top_metrics", "trends")
    PROVIDER_INFO_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    DATA_VOLUME_FIELD_NUMBER: _ClassVar[int]
    EXPORTS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_HISTORY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TOP_METRICS_FIELD_NUMBER: _ClassVar[int]
    TRENDS_FIELD_NUMBER: _ClassVar[int]
    provider_info: _provider_info_pb2.ProviderInfo
    performance: _performance_stats_pb2.MetricsPerformanceStats
    resource_usage: _resource_usage_stats_pb2.ResourceUsageStats
    errors: _error_stats_pb2.MetricsErrorStats
    data_volume: _data_volume_stats_pb2.DataVolumeStats
    exports: _export_stats_pb2.ExportStats
    health_history: _containers.RepeatedCompositeFieldContainer[_health_status_entry_pb2.HealthStatusEntry]
    config: _configuration_summary_pb2.ConfigurationSummary
    top_metrics: _top_metrics_pb2.TopMetrics
    trends: _trend_analysis_pb2.TrendAnalysis
    def __init__(self, provider_info: _Optional[_Union[_provider_info_pb2.ProviderInfo, _Mapping]] = ..., performance: _Optional[_Union[_performance_stats_pb2.MetricsPerformanceStats, _Mapping]] = ..., resource_usage: _Optional[_Union[_resource_usage_stats_pb2.ResourceUsageStats, _Mapping]] = ..., errors: _Optional[_Union[_error_stats_pb2.MetricsErrorStats, _Mapping]] = ..., data_volume: _Optional[_Union[_data_volume_stats_pb2.DataVolumeStats, _Mapping]] = ..., exports: _Optional[_Union[_export_stats_pb2.ExportStats, _Mapping]] = ..., health_history: _Optional[_Iterable[_Union[_health_status_entry_pb2.HealthStatusEntry, _Mapping]]] = ..., config: _Optional[_Union[_configuration_summary_pb2.ConfigurationSummary, _Mapping]] = ..., top_metrics: _Optional[_Union[_top_metrics_pb2.TopMetrics, _Mapping]] = ..., trends: _Optional[_Union[_trend_analysis_pb2.TrendAnalysis, _Mapping]] = ...) -> None: ...
