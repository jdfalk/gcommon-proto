from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import pagination_pb2 as _pagination_pb2
from gcommon.v1.web import middleware_info_pb2 as _middleware_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMiddlewareResponse(_message.Message):
    __slots__ = ("middleware", "pagination", "error")
    MIDDLEWARE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    middleware: _containers.RepeatedCompositeFieldContainer[_middleware_info_pb2.MiddlewareInfo]
    pagination: _pagination_pb2.Pagination
    error: _error_pb2.Error
    def __init__(self, middleware: _Optional[_Iterable[_Union[_middleware_info_pb2.MiddlewareInfo, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.Pagination, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
