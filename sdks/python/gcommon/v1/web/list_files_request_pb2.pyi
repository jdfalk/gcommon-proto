from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.web import file_sort_order_pb2 as _file_sort_order_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFilesRequest(_message.Message):
    __slots__ = ("directory_path", "recursive", "pattern", "limit", "offset", "include_hidden", "sort_order", "metadata")
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    directory_path: str
    recursive: bool
    pattern: str
    limit: int
    offset: int
    include_hidden: bool
    sort_order: _file_sort_order_pb2.FileSortOrder
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, directory_path: _Optional[str] = ..., recursive: bool = ..., pattern: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_hidden: bool = ..., sort_order: _Optional[_Union[_file_sort_order_pb2.FileSortOrder, str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
