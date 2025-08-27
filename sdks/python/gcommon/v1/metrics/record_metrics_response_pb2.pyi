import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import batch_stats_pb2 as _batch_stats_pb2
from gcommon.v1.metrics import metric_result_pb2 as _metric_result_pb2
from gcommon.v1.metrics import validation_summary_pb2 as _validation_summary_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordMetricsResponse(_message.Message):
    __slots__ = (
        "success",
        "success_count",
        "failure_count",
        "total_count",
        "error",
        "results",
        "completed_at",
        "provider_id",
        "stats",
        "warnings",
        "validation_summary",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    success: bool
    success_count: int
    failure_count: int
    total_count: int
    error: _error_pb2.Error
    results: _containers.RepeatedCompositeFieldContainer[
        _metric_result_pb2.MetricResult
    ]
    completed_at: _timestamp_pb2.Timestamp
    provider_id: str
    stats: _batch_stats_pb2.MetricsBatchStats
    warnings: _containers.RepeatedScalarFieldContainer[str]
    validation_summary: _validation_summary_pb2.ValidationSummary
    def __init__(
        self,
        success: _Optional[bool] = ...,
        success_count: _Optional[int] = ...,
        failure_count: _Optional[int] = ...,
        total_count: _Optional[int] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        results: _Optional[
            _Iterable[_Union[_metric_result_pb2.MetricResult, _Mapping]]
        ] = ...,
        completed_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        provider_id: _Optional[str] = ...,
        stats: _Optional[_Union[_batch_stats_pb2.MetricsBatchStats, _Mapping]] = ...,
        warnings: _Optional[_Iterable[str]] = ...,
        validation_summary: _Optional[
            _Union[_validation_summary_pb2.ValidationSummary, _Mapping]
        ] = ...,
    ) -> None: ...
