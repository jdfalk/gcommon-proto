from gcommon.v1.common.enums import eviction_policy_pb2 as _eviction_policy_pb2
from gcommon.v1.common.enums import expiration_policy_pb2 as _expiration_policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CachePolicy(_message.Message):
    __slots__ = ("expiration", "eviction", "max_size_bytes", "max_entries", "default_ttl", "refresh_ahead", "enable_stats")
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    EVICTION_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TTL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_AHEAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STATS_FIELD_NUMBER: _ClassVar[int]
    expiration: _expiration_policy_pb2.ExpirationPolicy
    eviction: _eviction_policy_pb2.EvictionPolicy
    max_size_bytes: int
    max_entries: int
    default_ttl: _duration_pb2.Duration
    refresh_ahead: bool
    enable_stats: bool
    def __init__(self, expiration: _Optional[_Union[_expiration_policy_pb2.ExpirationPolicy, str]] = ..., eviction: _Optional[_Union[_eviction_policy_pb2.EvictionPolicy, str]] = ..., max_size_bytes: _Optional[int] = ..., max_entries: _Optional[int] = ..., default_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., refresh_ahead: bool = ..., enable_stats: bool = ...) -> None: ...
