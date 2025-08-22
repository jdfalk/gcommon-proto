from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import metric_filter_pb2 as _metric_filter_pb2
from gcommon.v1.metrics import summary_options_pb2 as _summary_options_pb2
from gcommon.v1.metrics import time_range_pb2 as _time_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricsSummaryRequest(_message.Message):
    __slots__ = ("metadata", "filter", "time_range", "options", "provider_id", "include_provider_stats", "include_health_status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PROVIDER_STATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    filter: _metric_filter_pb2.MetricFilter
    time_range: _time_range_pb2.MetricsTimeRange
    options: _summary_options_pb2.SummaryOptions
    provider_id: str
    include_provider_stats: bool
    include_health_status: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., filter: _Optional[_Union[_metric_filter_pb2.MetricFilter, _Mapping]] = ..., time_range: _Optional[_Union[_time_range_pb2.MetricsTimeRange, _Mapping]] = ..., options: _Optional[_Union[_summary_options_pb2.SummaryOptions, _Mapping]] = ..., provider_id: _Optional[str] = ..., include_provider_stats: bool = ..., include_health_status: bool = ...) -> None: ...
