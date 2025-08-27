from gcommon.v1.common import pagination_options_pb2 as _pagination_options_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import provider_filter_pb2 as _provider_filter_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProvidersRequest(_message.Message):
    __slots__ = (
        "metadata",
        "filter",
        "pagination",
        "include_status",
        "include_config",
        "include_stats",
    )
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATUS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    filter: _provider_filter_pb2.ProviderFilter
    pagination: _pagination_options_pb2.PaginationOptions
    include_status: bool
    include_config: bool
    include_stats: bool
    def __init__(
        self,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        filter: _Optional[_Union[_provider_filter_pb2.ProviderFilter, _Mapping]] = ...,
        pagination: _Optional[
            _Union[_pagination_options_pb2.PaginationOptions, _Mapping]
        ] = ...,
        include_status: _Optional[bool] = ...,
        include_config: _Optional[bool] = ...,
        include_stats: _Optional[bool] = ...,
    ) -> None: ...
