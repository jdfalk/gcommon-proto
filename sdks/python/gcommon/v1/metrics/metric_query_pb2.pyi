from gcommon.v1.common import sort_options_pb2 as _sort_options_pb2
from gcommon.v1.metrics import aggregation_spec_pb2 as _aggregation_spec_pb2
from gcommon.v1.metrics import group_by_spec_pb2 as _group_by_spec_pb2
from gcommon.v1.metrics import metric_filter_pb2 as _metric_filter_pb2
from gcommon.v1.metrics import time_range_pb2 as _time_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricQuery(_message.Message):
    __slots__ = ("query_id", "name", "query_string", "filter", "time_filter", "aggregations", "group_by", "sort_criteria", "limit", "offset")
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRING_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    query_id: str
    name: str
    query_string: str
    filter: _metric_filter_pb2.MetricFilter
    time_filter: _time_range_pb2.MetricsTimeRange
    aggregations: _containers.RepeatedCompositeFieldContainer[_aggregation_spec_pb2.AggregationSpec]
    group_by: _containers.RepeatedCompositeFieldContainer[_group_by_spec_pb2.GroupBySpec]
    sort_criteria: _containers.RepeatedCompositeFieldContainer[_sort_options_pb2.SortOptions]
    limit: int
    offset: int
    def __init__(self, query_id: _Optional[str] = ..., name: _Optional[str] = ..., query_string: _Optional[str] = ..., filter: _Optional[_Union[_metric_filter_pb2.MetricFilter, _Mapping]] = ..., time_filter: _Optional[_Union[_time_range_pb2.MetricsTimeRange, _Mapping]] = ..., aggregations: _Optional[_Iterable[_Union[_aggregation_spec_pb2.AggregationSpec, _Mapping]]] = ..., group_by: _Optional[_Iterable[_Union[_group_by_spec_pb2.GroupBySpec, _Mapping]]] = ..., sort_criteria: _Optional[_Iterable[_Union[_sort_options_pb2.SortOptions, _Mapping]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...
