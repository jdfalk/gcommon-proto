from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import metric_series_pb2 as _metric_series_pb2
from gcommon.v1.metrics import query_plan_pb2 as _query_plan_pb2
from gcommon.v1.metrics import query_statistics_pb2 as _query_statistics_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryMetricsResponse(_message.Message):
    __slots__ = (
        "success",
        "error",
        "series",
        "statistics",
        "query_plan",
        "warnings",
        "next_page_token",
        "total_results",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    QUERY_PLAN_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    series: _containers.RepeatedCompositeFieldContainer[_metric_series_pb2.MetricSeries]
    statistics: _query_statistics_pb2.QueryStatistics
    query_plan: _query_plan_pb2.QueryPlan
    warnings: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    total_results: int
    def __init__(
        self,
        success: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        series: _Optional[
            _Iterable[_Union[_metric_series_pb2.MetricSeries, _Mapping]]
        ] = ...,
        statistics: _Optional[
            _Union[_query_statistics_pb2.QueryStatistics, _Mapping]
        ] = ...,
        query_plan: _Optional[_Union[_query_plan_pb2.QueryPlan, _Mapping]] = ...,
        warnings: _Optional[_Iterable[str]] = ...,
        next_page_token: _Optional[str] = ...,
        total_results: _Optional[int] = ...,
    ) -> None: ...
