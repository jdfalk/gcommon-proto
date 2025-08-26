from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SummaryOptions(_message.Message):
    __slots__ = ("include_counts", "include_data_volume", "include_performance", "include_errors", "include_top_metrics", "include_retention", "include_export_status", "top_metrics_limit")
    INCLUDE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DATA_VOLUME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOP_METRICS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RETENTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    TOP_METRICS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    include_counts: bool
    include_data_volume: bool
    include_performance: bool
    include_errors: bool
    include_top_metrics: bool
    include_retention: bool
    include_export_status: bool
    top_metrics_limit: int
    def __init__(self, include_counts: bool = ..., include_data_volume: bool = ..., include_performance: bool = ..., include_errors: bool = ..., include_top_metrics: bool = ..., include_retention: bool = ..., include_export_status: bool = ..., top_metrics_limit: _Optional[int] = ...) -> None: ...
