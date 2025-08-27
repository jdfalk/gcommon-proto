from gcommon.v1.common import middleware_type_pb2 as _middleware_type_pb2
from gcommon.v1.common import pagination_pb2 as _pagination_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMiddlewareRequest(_message.Message):
    __slots__ = ("server_id", "type", "enabled", "pagination", "metadata")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    type: _middleware_type_pb2.MiddlewareType
    enabled: bool
    pagination: _pagination_pb2.Pagination
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, server_id: _Optional[str] = ..., type: _Optional[_Union[_middleware_type_pb2.MiddlewareType, str]] = ..., enabled: _Optional[bool] = ..., pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
