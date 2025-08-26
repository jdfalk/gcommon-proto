from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatsOptions(_message.Message):
    __slots__ = ("include_performance", "include_resource_usage", "include_errors", "include_data_volume", "include_exports", "include_health_history", "include_config", "include_top_metrics", "top_metrics_limit", "include_trends")
    INCLUDE_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DATA_VOLUME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEALTH_HISTORY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOP_METRICS_FIELD_NUMBER: _ClassVar[int]
    TOP_METRICS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRENDS_FIELD_NUMBER: _ClassVar[int]
    include_performance: bool
    include_resource_usage: bool
    include_errors: bool
    include_data_volume: bool
    include_exports: bool
    include_health_history: bool
    include_config: bool
    include_top_metrics: bool
    top_metrics_limit: int
    include_trends: bool
    def __init__(self, include_performance: bool = ..., include_resource_usage: bool = ..., include_errors: bool = ..., include_data_volume: bool = ..., include_exports: bool = ..., include_health_history: bool = ..., include_config: bool = ..., include_top_metrics: bool = ..., top_metrics_limit: _Optional[int] = ..., include_trends: bool = ...) -> None: ...
