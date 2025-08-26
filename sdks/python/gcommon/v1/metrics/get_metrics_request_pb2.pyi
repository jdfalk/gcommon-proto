from gcommon.v1.common import pagination_options_pb2 as _pagination_options_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import time_range_metrics_pb2 as _time_range_metrics_pb2
from gcommon.v1.metrics import metric_aggregation_pb2 as _metric_aggregation_pb2
from gcommon.v1.metrics import metric_filter_pb2 as _metric_filter_pb2
from gcommon.v1.metrics import output_options_pb2 as _output_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsGetMetricsRequest(_message.Message):
    __slots__ = ("metadata", "filter", "time_range", "aggregation", "pagination", "provider_id", "output_options", "include_metadata", "limit")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    filter: _metric_filter_pb2.MetricFilter
    time_range: _time_range_metrics_pb2.TimeRangeMetrics
    aggregation: _metric_aggregation_pb2.MetricAggregation
    pagination: _pagination_options_pb2.PaginationOptions
    provider_id: str
    output_options: _output_options_pb2.OutputOptions
    include_metadata: bool
    limit: int
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., filter: _Optional[_Union[_metric_filter_pb2.MetricFilter, _Mapping]] = ..., time_range: _Optional[_Union[_time_range_metrics_pb2.TimeRangeMetrics, _Mapping]] = ..., aggregation: _Optional[_Union[_metric_aggregation_pb2.MetricAggregation, _Mapping]] = ..., pagination: _Optional[_Union[_pagination_options_pb2.PaginationOptions, _Mapping]] = ..., provider_id: _Optional[str] = ..., output_options: _Optional[_Union[_output_options_pb2.OutputOptions, _Mapping]] = ..., include_metadata: _Optional[bool] = ..., limit: _Optional[int] = ...) -> None: ...
