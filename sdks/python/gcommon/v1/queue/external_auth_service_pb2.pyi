from gcommon.v1.queue import auth_cache_config_pb2 as _auth_cache_config_pb2
from gcommon.v1.queue import retry_config_pb2 as _retry_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalAuthService(_message.Message):
    __slots__ = ("enabled", "endpoint", "timeout_ms", "retry_config", "cache_config", "request_headers")
    class RequestHeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    endpoint: str
    timeout_ms: int
    retry_config: _retry_config_pb2.QueueRetryConfig
    cache_config: _auth_cache_config_pb2.AuthCacheConfig
    request_headers: _containers.ScalarMap[str, str]
    def __init__(self, enabled: _Optional[bool] = ..., endpoint: _Optional[str] = ..., timeout_ms: _Optional[int] = ..., retry_config: _Optional[_Union[_retry_config_pb2.QueueRetryConfig, _Mapping]] = ..., cache_config: _Optional[_Union[_auth_cache_config_pb2.AuthCacheConfig, _Mapping]] = ..., request_headers: _Optional[_Mapping[str, str]] = ...) -> None: ...
