from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.web import middleware_info_pb2 as _middleware_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterMiddlewareResponse(_message.Message):
    __slots__ = ("success", "middleware", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MIDDLEWARE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    middleware: _middleware_info_pb2.MiddlewareInfo
    error: _error_pb2.Error
    def __init__(
        self,
        success: _Optional[bool] = ...,
        middleware: _Optional[
            _Union[_middleware_info_pb2.MiddlewareInfo, _Mapping]
        ] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
    ) -> None: ...
