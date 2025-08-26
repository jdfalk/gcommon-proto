import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import metric_metadata_pb2 as _metric_metadata_pb2
from gcommon.v1.metrics import pagination_info_pb2 as _pagination_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricMetadataResponse(_message.Message):
    __slots__ = ("success", "error", "provider_id", "metadata", "pagination", "total_count", "generated_at", "warnings", "execution_time_ms")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    provider_id: str
    metadata: _containers.RepeatedCompositeFieldContainer[_metric_metadata_pb2.MetricMetadata]
    pagination: _pagination_info_pb2.MetricsPaginationInfo
    total_count: int
    generated_at: _timestamp_pb2.Timestamp
    warnings: _containers.RepeatedScalarFieldContainer[str]
    execution_time_ms: int
    def __init__(self, success: _Optional[bool] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., provider_id: _Optional[str] = ..., metadata: _Optional[_Iterable[_Union[_metric_metadata_pb2.MetricMetadata, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_info_pb2.MetricsPaginationInfo, _Mapping]] = ..., total_count: _Optional[int] = ..., generated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., execution_time_ms: _Optional[int] = ...) -> None: ...
