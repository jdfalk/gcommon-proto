import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import pagination_info_pb2 as _pagination_info_pb2
from gcommon.v1.metrics import provider_info_pb2 as _provider_info_pb2
from gcommon.v1.metrics import provider_summary_pb2 as _provider_summary_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProvidersResponse(_message.Message):
    __slots__ = (
        "success",
        "error",
        "providers",
        "pagination",
        "summary",
        "generated_at",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    providers: _containers.RepeatedCompositeFieldContainer[
        _provider_info_pb2.ProviderInfo
    ]
    pagination: _pagination_info_pb2.MetricsPaginationInfo
    summary: _provider_summary_pb2.ProviderSummary
    generated_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        success: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        providers: _Optional[
            _Iterable[_Union[_provider_info_pb2.ProviderInfo, _Mapping]]
        ] = ...,
        pagination: _Optional[
            _Union[_pagination_info_pb2.MetricsPaginationInfo, _Mapping]
        ] = ...,
        summary: _Optional[
            _Union[_provider_summary_pb2.ProviderSummary, _Mapping]
        ] = ...,
        generated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
