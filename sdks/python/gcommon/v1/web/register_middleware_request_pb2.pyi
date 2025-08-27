from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.web import middleware_config_pb2 as _middleware_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterMiddlewareRequest(_message.Message):
    __slots__ = ("server_id", "middleware", "metadata")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    MIDDLEWARE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    middleware: _middleware_config_pb2.MiddlewareConfig
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, server_id: _Optional[str] = ..., middleware: _Optional[_Union[_middleware_config_pb2.MiddlewareConfig, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
