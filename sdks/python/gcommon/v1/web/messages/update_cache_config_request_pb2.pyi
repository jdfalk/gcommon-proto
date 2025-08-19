from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.web.messages import cache_config_pb2 as _cache_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateCacheConfigRequest(_message.Message):
    __slots__ = ("config", "metadata")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    config: _cache_config_pb2.WebCacheConfig
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, config: _Optional[_Union[_cache_config_pb2.WebCacheConfig, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
