from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.web import middleware_config_pb2 as _middleware_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMiddlewareConfigRequest(_message.Message):
    __slots__ = ("metadata", "config")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    config: _middleware_config_pb2.MiddlewareConfig
    def __init__(
        self,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        config: _Optional[
            _Union[_middleware_config_pb2.MiddlewareConfig, _Mapping]
        ] = ...,
    ) -> None: ...
