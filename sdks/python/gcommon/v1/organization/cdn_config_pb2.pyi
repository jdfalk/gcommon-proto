from gcommon.v1.organization import cache_behavior_pb2 as _cache_behavior_pb2
from gcommon.v1.organization import origin_config_pb2 as _origin_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDNConfig(_message.Message):
    __slots__ = ("provider", "distribution_id", "cache_behaviors", "origin")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_ID_FIELD_NUMBER: _ClassVar[int]
    CACHE_BEHAVIORS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    provider: str
    distribution_id: str
    cache_behaviors: _containers.RepeatedCompositeFieldContainer[_cache_behavior_pb2.CacheBehavior]
    origin: _origin_config_pb2.OriginConfig
    def __init__(self, provider: _Optional[str] = ..., distribution_id: _Optional[str] = ..., cache_behaviors: _Optional[_Iterable[_Union[_cache_behavior_pb2.CacheBehavior, _Mapping]]] = ..., origin: _Optional[_Union[_origin_config_pb2.OriginConfig, _Mapping]] = ...) -> None: ...
