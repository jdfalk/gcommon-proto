from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListHandlersRequest(_message.Message):
    __slots__ = ("method_filter", "path_filter", "include_middleware", "limit", "offset", "metadata")
    METHOD_FILTER_FIELD_NUMBER: _ClassVar[int]
    PATH_FILTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MIDDLEWARE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    method_filter: str
    path_filter: str
    include_middleware: bool
    limit: int
    offset: int
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, method_filter: _Optional[str] = ..., path_filter: _Optional[str] = ..., include_middleware: bool = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
