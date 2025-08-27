from gcommon.v1.common import filter_options_pb2 as _filter_options_pb2
from gcommon.v1.common import pagination_pb2 as _pagination_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import sort_options_pb2 as _sort_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListRolesRequest(_message.Message):
    __slots__ = ("pagination", "filter", "sort", "metadata")
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.Pagination
    filter: _filter_options_pb2.FilterOptions
    sort: _sort_options_pb2.SortOptions
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ...,
        filter: _Optional[_Union[_filter_options_pb2.FilterOptions, _Mapping]] = ...,
        sort: _Optional[_Union[_sort_options_pb2.SortOptions, _Mapping]] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
