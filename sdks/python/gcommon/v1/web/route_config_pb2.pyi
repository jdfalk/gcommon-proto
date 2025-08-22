from gcommon.v1.web import handler_type_pb2 as _handler_type_pb2
from gcommon.v1.web import http_method_pb2 as _http_method_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RouteConfig(_message.Message):
    __slots__ = ("path", "methods", "handler", "handler_type", "middleware_ids", "auth_required")
    PATH_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    HANDLER_FIELD_NUMBER: _ClassVar[int]
    HANDLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIDDLEWARE_IDS_FIELD_NUMBER: _ClassVar[int]
    AUTH_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    path: str
    methods: _containers.RepeatedScalarFieldContainer[_http_method_pb2.HTTPMethod]
    handler: str
    handler_type: _handler_type_pb2.HandlerType
    middleware_ids: _containers.RepeatedScalarFieldContainer[str]
    auth_required: bool
    def __init__(self, path: _Optional[str] = ..., methods: _Optional[_Iterable[_Union[_http_method_pb2.HTTPMethod, str]]] = ..., handler: _Optional[str] = ..., handler_type: _Optional[_Union[_handler_type_pb2.HandlerType, str]] = ..., middleware_ids: _Optional[_Iterable[str]] = ..., auth_required: bool = ...) -> None: ...
