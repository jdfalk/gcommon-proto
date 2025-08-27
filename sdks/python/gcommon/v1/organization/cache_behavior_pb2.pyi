from gcommon.v1.organization import cache_key_policy_pb2 as _cache_key_policy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheBehavior(_message.Message):
    __slots__ = ("path_pattern", "ttl_seconds", "compress", "allowed_methods", "cache_key")
    PATH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_METHODS_FIELD_NUMBER: _ClassVar[int]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    path_pattern: str
    ttl_seconds: int
    compress: bool
    allowed_methods: _containers.RepeatedScalarFieldContainer[str]
    cache_key: _cache_key_policy_pb2.CacheKeyPolicy
    def __init__(self, path_pattern: _Optional[str] = ..., ttl_seconds: _Optional[int] = ..., compress: _Optional[bool] = ..., allowed_methods: _Optional[_Iterable[str]] = ..., cache_key: _Optional[_Union[_cache_key_policy_pb2.CacheKeyPolicy, _Mapping]] = ...) -> None: ...
