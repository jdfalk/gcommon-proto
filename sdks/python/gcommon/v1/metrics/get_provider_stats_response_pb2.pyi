import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import time_range_metrics_pb2 as _time_range_metrics_pb2
from gcommon.v1.metrics import provider_statistics_pb2 as _provider_statistics_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProviderStatsResponse(_message.Message):
    __slots__ = ("success", "error", "provider_id", "statistics", "generated_at", "time_range", "warnings")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    provider_id: str
    statistics: _provider_statistics_pb2.ProviderStatistics
    generated_at: _timestamp_pb2.Timestamp
    time_range: _time_range_metrics_pb2.TimeRangeMetrics
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: _Optional[bool] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., provider_id: _Optional[str] = ..., statistics: _Optional[_Union[_provider_statistics_pb2.ProviderStatistics, _Mapping]] = ..., generated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_range: _Optional[_Union[_time_range_metrics_pb2.TimeRangeMetrics, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
